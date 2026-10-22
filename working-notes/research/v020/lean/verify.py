"""Bounded kernel recheck, dependency audit, and intentional failure controls."""

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import signal
import subprocess
import time


ALLOWED_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}
MATHLIB_REV = "f897ebcf72cd16f89ab4577d0c826cd14afaafc7"
MODULES = ("IccOutcomeTick", "IccTickSeparation")
NEGATIVE_CONTROLS = {
    "NegativeControlInstrument.lean": ("Type mismatch", "density_outputs_differ"),
    "NegativeControlAttenuation.lean": ("Type mismatch", "luders_offdiagonal"),
    "NegativeControlIndependence.lean": ("unsolved goals",),
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lake", default="lake")
    parser.add_argument("--timeout", type=float, default=300)
    args = parser.parse_args()
    if args.timeout <= 0:
        parser.error("--timeout must be positive")

    root = Path(__file__).resolve().parent
    output = root / "verification-output"
    output.mkdir(exist_ok=True)
    started = time.monotonic()
    deadline = started + args.timeout
    report = {"started_utc": datetime.now(timezone.utc).isoformat(), "steps": []}

    def run(name, command, expected_failure=False):
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise TimeoutError("Overall verification deadline reached")
        step_started = time.monotonic()
        process = subprocess.Popen(
            command, cwd=root, start_new_session=True,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
        )
        try:
            result, _ = process.communicate(timeout=remaining)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGTERM)
            try:
                process.communicate(timeout=2)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.communicate()
            raise TimeoutError(f"Deadline reached during {name}") from None
        (output / f"{name}.log").write_text(result)
        report["steps"].append({
            "name": name, "command": command, "exit_code": process.returncode,
            "elapsed_seconds": round(time.monotonic() - step_started, 3),
            "expected_failure": expected_failure,
        })
        if expected_failure == (process.returncode == 0):
            raise RuntimeError(f"Unexpected exit status in {name}:\n{result}")
        print(f"{name}: expected exit status ({process.returncode})", flush=True)
        return result

    try:
        source_files = sorted(root.glob("*.lean"))
        forbidden = re.compile(r"\b(sorry|admit|axiom|unsafe|native_decide|implemented_by)\b")
        for path in source_files:
            if forbidden.search(path.read_text()):
                raise RuntimeError(f"Forbidden proof escape in {path.name}")
        expected = {
            f"{module}.{name}"
            for module in MODULES
            for name in re.findall(r"^theorem\s+(\w+)", (root / f"{module}.lean").read_text(), re.M)
        }
        if not expected:
            raise RuntimeError("No theorem declarations found")
        report["source_sha256"] = {
            path.name: hashlib.sha256(path.read_bytes()).hexdigest()
            for path in source_files + [
                root / "lakefile.toml", root / "lean-toolchain",
                root / "lake-manifest.json", root / "verify.py",
            ]
        }
        manifest = json.loads((root / "lake-manifest.json").read_text())
        mathlib = next(p for p in manifest["packages"] if p["name"] == "mathlib")
        if mathlib["rev"] != MATHLIB_REV:
            raise RuntimeError("Unexpected mathlib pin")
        actual_rev = run("mathlib-revision", [
            "git", "-C", str(root / ".lake/packages/mathlib"), "rev-parse", "HEAD",
        ]).strip()
        if actual_rev != MATHLIB_REV:
            raise RuntimeError("Cached mathlib checkout differs from manifest")
        run("mathlib-clean", [
            "git", "-C", str(root / ".lake/packages/mathlib"), "diff", "--exit-code", "HEAD",
        ])
        report["mathlib_revision"] = actual_rev
        report["lean_version"] = run("version", [args.lake, "env", "lean", "--version"]).strip()
        run("build", [args.lake, "build"])
        # Direct checks prevent a successful cached build from being the only evidence.
        for module in MODULES:
            run(f"check-{module}", [args.lake, "env", "lean", f"{module}.lean"])
        audit = run("audit", [args.lake, "env", "lean", "Audit.lean"])
        matches = re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]", audit)
        inventories = {
            name: [entry.strip() for entry in dependencies.split(",") if entry.strip()]
            for name, dependencies in matches
        }
        if set(inventories) != expected or len(matches) != len(expected):
            raise RuntimeError("Audit must cover every theorem exactly once")
        for name, dependencies in inventories.items():
            if not set(dependencies) <= ALLOWED_AXIOMS:
                raise RuntimeError(f"Unexpected dependencies: {name}: {dependencies}")
        report["axioms"] = inventories
        for filename, markers in NEGATIVE_CONTROLS.items():
            result = run(filename.removesuffix(".lean"),
                         [args.lake, "env", "lean", filename], expected_failure=True)
            if not all(marker in result for marker in markers):
                raise RuntimeError(f"Wrong failure reason in {filename}:\n{result}")
        report["status"] = "passed"
    except Exception as error:
        report["status"] = "failed"
        report["error"] = str(error)
        raise
    finally:
        report["elapsed_seconds"] = round(time.monotonic() - started, 3)
        report["finished_utc"] = datetime.now(timezone.utc).isoformat()
        (output / "verification.json").write_text(json.dumps(report, indent=2) + "\n")
    print(f"Verified {len(report['axioms'])} theorems in {report['elapsed_seconds']} seconds")


if __name__ == "__main__":
    main()
