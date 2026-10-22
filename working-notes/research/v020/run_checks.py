"""Run the two finite tick diagnostics under one shared wall-clock limit."""

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--timeout", type=float, default=120)
    args = parser.parse_args()
    if args.timeout <= 0:
        parser.error("--timeout must be positive")
    root = Path(__file__).resolve().parent
    output = root / "verification-output"
    output.mkdir(exist_ok=True)
    started = time.monotonic()
    report = {"started_utc": datetime.now(timezone.utc).isoformat(), "suites": {}}
    env = dict(os.environ, PYTHONOPTIMIZE="0", PYTHONDONTWRITEBYTECODE="1")
    try:
        for filename in ("check.py", "audit-check.py"):
            remaining = args.timeout - (time.monotonic() - started)
            if remaining <= 0:
                raise TimeoutError("Shared diagnostic deadline reached")
            process = subprocess.Popen([sys.executable, "-B", str(root / filename)],
                                       cwd=root, env=env, start_new_session=True,
                                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            try:
                text, _ = process.communicate(timeout=remaining)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.communicate(timeout=2)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.communicate()
                raise TimeoutError(f"Deadline reached during {filename}") from None
            (output / f"{filename}.log").write_text(text)
            if process.returncode:
                raise RuntimeError(f"{filename} failed: {text}")
            result = json.loads(text)
            statuses = ([result["status"]] if "status" in result
                        else [result[key]["status"] for key in ("mathematics", "physics_control")])
            if any(status != "passed" for status in statuses):
                raise RuntimeError(f"Reported failure in {filename}")
            report["suites"][filename] = result
            print(f"{filename}: passed", flush=True)
        report["status"] = "passed"
    except Exception as error:
        report["status"] = "failed"
        report["error"] = str(error)
        raise
    finally:
        report["elapsed_seconds"] = round(time.monotonic() - started, 3)
        report["finished_utc"] = datetime.now(timezone.utc).isoformat()
        report["source_sha256"] = {name: hashlib.sha256((root / name).read_bytes()).hexdigest()
                                   for name in ("check.py", "audit-check.py", "run_checks.py")}
        report["scope"] = "Finite diagnostics with assertions enabled; not continuum or physical validation."
        (output / "checks-results.json").write_text(json.dumps(report, indent=2) + "\n")
    print(f"Completed in {report['elapsed_seconds']} seconds")


if __name__ == "__main__":
    main()
