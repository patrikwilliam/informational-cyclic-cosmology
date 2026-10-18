"""Run the bounded arithmetic diagnostics without changing bundled records."""

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parent


def main():
    if sys.version_info < (3, 10):
        print("ERROR: Python 3.10+ is required.", file=sys.stderr)
        return 2
    if sys.flags.optimize:
        print("ERROR: assertions must be enabled; remove -O/-OO and unset "
              "PYTHONOPTIMIZE.", file=sys.stderr)
        return 2
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    environment.pop("PYTHONOPTIMIZE", None)
    with tempfile.TemporaryDirectory(prefix="icc-v017-") as directory:
        output = Path(directory) / "checks.json"
        process = subprocess.run(
            [sys.executable, "-B", str(ROOT / "arithmetic_checks.py"),
             "--json", str(output)], cwd=directory, env=environment,
            capture_output=True, text=True, timeout=120, check=False,
        )
        if process.returncode:
            print(process.stdout + process.stderr, file=sys.stderr)
            return 1
        actual = json.loads(output.read_text())
        recorded = json.loads((ROOT / "arithmetic_checks_results.json").read_text())
        for key in ("configuration", "diagnostic_names", "status", "scope"):
            if actual[key] != recorded[key]:
                raise ValueError(f"Diagnostic configuration differs: {key}")
        for name in actual["diagnostic_names"]:
            print(f"PASS {name}")
        operational_output = Path(directory) / "operational.json"
        operational_process = subprocess.run(
            [sys.executable, "-B", str(ROOT / "operational_stability_checks.py"),
             "--output", str(operational_output)], cwd=directory, env=environment,
            capture_output=True, text=True, timeout=120, check=False,
        )
        if operational_process.returncode:
            print(operational_process.stdout + operational_process.stderr, file=sys.stderr)
            return 1
        operational = json.loads(operational_output.read_text())
        operational_record = json.loads((ROOT / "operational_stability_results.json").read_text())
        for key in ("status", "seed", "tolerance", "checks", "limits"):
            if operational[key] != operational_record[key]:
                raise ValueError(f"Operational diagnostic configuration differs: {key}")
        if [window["window"] for window in operational["windows"]] != [6, 12]:
            raise ValueError("Operational access windows changed")
        for name in operational["checks"]:
            print(f"PASS {name}")
        total = len(actual["diagnostic_names"]) + len(operational["checks"])
        print(f"{total} finite diagnostic groups passed; "
              "no infinite-dimensional or physical validation claimed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
