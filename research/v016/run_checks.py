"""Run the bounded v0.1.6 diagnostics without changing bundled results."""

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parent
SCRIPTS = (("entropy_stability_checks", 7), ("transport_checks", 6))


def main():
    if sys.version_info < (3, 10):
        print("ERROR: Python 3.10+ is required.", file=sys.stderr)
        return 2
    if sys.flags.optimize:
        print("ERROR: assertions must be enabled; remove -O/-OO and "
              "unset PYTHONOPTIMIZE.", file=sys.stderr)
        return 2
    try:
        import numpy as np
    except ImportError:
        print("ERROR: install NumPy in the invoking Python environment.", file=sys.stderr)
        return 2

    print(f"Python {sys.version.split()[0]}; NumPy {np.__version__}", flush=True)
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    environment.pop("PYTHONOPTIMIZE", None)
    total = 0
    with tempfile.TemporaryDirectory(prefix="icc-v016-") as directory:
        temporary = Path(directory)
        for stem, count in SCRIPTS:
            command = [sys.executable, "-B", str(ROOT / f"{stem}.py")]
            output = temporary / "entropy.json"
            if stem == "entropy_stability_checks":
                command.extend(("--json", str(output)))
            captured = ""
            try:
                process = subprocess.run(
                    command, cwd=temporary, env=environment, text=True,
                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                    timeout=120, check=False,
                )
                captured = process.stdout
                if process.returncode:
                    raise RuntimeError(f"exit status {process.returncode}")
                if sum(line.startswith("PASS ") for line in captured.splitlines()) != count:
                    raise ValueError("unexpected diagnostic count")
                if stem == "entropy_stability_checks":
                    record = json.loads(output.read_text())
                    reference = json.loads(
                        (ROOT / "entropy_stability_checks_results.json").read_text())
                    for key in ("seed", "absolute_tolerance", "scope", "passed"):
                        if record[key] != reference[key]:
                            raise ValueError(f"recorded diagnostic configuration differs: {key}")
                    expected = [item["name"] for item in reference["checks"]]
                    if [item["name"] for item in record["checks"]] != expected:
                        raise ValueError("diagnostic names differ from the bundled record")
                    if not all(item["passed"] is True for item in record["checks"]):
                        raise ValueError("a diagnostic failed")
            except (OSError, ValueError, KeyError, TypeError, RuntimeError,
                    subprocess.TimeoutExpired) as error:
                print(f"FAIL {stem}: {error}", file=sys.stderr)
                if captured:
                    print(captured.rstrip(), file=sys.stderr)
                return 1
            total += count
            print(captured.rstrip(), flush=True)
    print(f"{total}/13 diagnostic groups passed. Temporary outputs removed; "
          "no exact KK-distance computation, selector search, or Lean audit.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
