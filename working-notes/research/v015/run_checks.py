"""Run the six fixed v0.1.5 checks without changing bundled results."""

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parent
SCRIPTS = (
    "finite_time_ranking_check",
    "finite_time_second_variation",
    "finite_time_bell_certificate",
    "operational_selector_checks",
    "observational_entropy_checks",
    "measurement_access_checks",
)


def coefficient_data(record):
    """Compare exact data, not platform-dependent decimal displays."""
    keys = ("H0", "T0", "generator_normalization",
            "horizontal_gradient_coefficients", "bell_cost_fourier_coefficients")
    result = {key: record[key] for key in keys}
    rows = record["normal_hessian_eigenvalues"]
    coefficients = {row["direction"]: row["fourier_coefficients"] for row in rows}
    if len(rows) != 6 or len(coefficients) != 6:
        raise ValueError("certificate must contain six distinct normal directions")
    result["normal_hessian_coefficients"] = coefficients
    return result


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

    print(f"Python {sys.version.split()[0]}; NumPy {np.__version__}; "
          f"interpreter: {sys.executable}", flush=True)
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    environment.pop("PYTHONOPTIMIZE", None)
    completed = 0
    with tempfile.TemporaryDirectory(prefix="icc-v015-") as directory:
        temporary = Path(directory)
        for stem in SCRIPTS:
            command = [sys.executable, "-B", str(ROOT / f"{stem}.py")]
            output = temporary / f"{stem}_results.json"
            if stem != "finite_time_ranking_check":
                command.extend(("--output", str(output)))
            captured = ""
            try:
                process = subprocess.run(
                    command, cwd=temporary, env=environment,
                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                    text=True, timeout=180, check=False,
                )
                captured = process.stdout
                if process.returncode:
                    raise RuntimeError(f"exit status {process.returncode}")
                record = json.loads(captured if stem == "finite_time_ranking_check"
                                    else output.read_text())
                if stem == "finite_time_bell_certificate":
                    reference = json.loads(
                        (ROOT / f"{stem}_results.json").read_text())
                    if coefficient_data(record) != coefficient_data(reference):
                        raise ValueError("regenerated exact certificate coefficients "
                                         "do not match the bundled reference")
            except (OSError, ValueError, KeyError, TypeError, RuntimeError,
                    subprocess.TimeoutExpired) as error:
                print(f"FAIL {stem}.py: {error}", file=sys.stderr)
                diagnostic = getattr(error, "stdout", None) or captured
                if isinstance(diagnostic, bytes):
                    diagnostic = diagnostic.decode(errors="replace")
                if diagnostic:
                    print(diagnostic.rstrip(), file=sys.stderr)
                print(f"{completed}/{len(SCRIPTS)} checks passed before failure.",
                      file=sys.stderr)
                return 1
            completed += 1
            print(f"PASS {stem}.py", flush=True)
    print(f"{completed}/{len(SCRIPTS)} checks passed; exact certificate coefficients "
          "match the bundled reference. Temporary outputs removed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
