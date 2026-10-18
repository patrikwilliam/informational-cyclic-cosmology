"""Run the two bounded v0.1.8 numerical suites without altering saved results."""

import argparse
import hashlib
import json
from pathlib import Path
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
    reports = {}
    for name in ("three-qubit-memory", "measurement-capability"):
        script = root / name / "checks.py"
        remaining = args.timeout - (time.monotonic() - started)
        if remaining <= 0:
            raise TimeoutError("Overall numerical verification deadline reached")
        run = subprocess.run([sys.executable, "-BO", str(script)],
                             capture_output=True, text=True, timeout=remaining, check=True)
        result = json.loads(run.stdout)
        if result["status"] != "passed":
            raise RuntimeError(f"Failed suite: {name}")
        if result["source_sha256"] != hashlib.sha256(script.read_bytes()).hexdigest():
            raise RuntimeError(f"Source hash mismatch: {name}")
        if name == "measurement-capability":
            model = root / "three-qubit-memory" / "checks.py"
            if result["model_source_sha256"] != hashlib.sha256(model.read_bytes()).hexdigest():
                raise RuntimeError("Imported model hash mismatch")
        (output / f"{name}.json").write_text(run.stdout)
        reports[name] = {"status": result["status"],
                         "largest_residual": max(result["max_residuals"].values()),
                         "source_sha256": result["source_sha256"]}
        print(f"{name}: passed; largest residual {reports[name]['largest_residual']:.3g}")
    report = {"status": "passed", "elapsed_seconds": time.monotonic() - started,
              "suites": reports,
              "scope": "Numerical cross-checks, not formal or physical validation."}
    (output / "verification.json").write_text(json.dumps(report, indent=2) + "\n")
    print(f"Completed in {report['elapsed_seconds']:.3f} seconds")


if __name__ == "__main__":
    main()
