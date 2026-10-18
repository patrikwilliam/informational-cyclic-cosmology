"""Recheck the bounded Lean project, its axiom inventory, and a failing control."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import signal
import subprocess
import time
from datetime import datetime, timezone


EXPECTED = {
    "IccWitness.two_fiber_hausdorff_eq_one",
    "IccConcrete.algebraBundled",
    "IccConcrete.phaseFlip_star",
    "IccConcrete.concrete_distance_one",
    "IccConcrete.shift_difference_norm",
    "IccConcrete.phaseFlip_tendsto_identity",
    "IccConcrete.arbitrarily_close_vectors_distance_one",
    "IccArithmetic.positiveLabels",
    "IccArithmetic.label_shift",
    "IccOperational.effect_mem",
    "IccOperational.effect_projection",
    "IccOperational.ray_norm_sq",
    "IccOperational.flipped_effect_valid",
    "IccOperational.probability_range",
    "IccOperational.fixed_two_probe_obstruction",
    "IccOperational.phase_perturbation_bound",
}
ALLOWED_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}


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
        step_start = time.monotonic()
        process = subprocess.Popen(
            command, cwd=root, start_new_session=True, stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT, text=True,
        )
        try:
            text, _ = process.communicate(timeout=remaining)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGTERM)
            try:
                process.communicate(timeout=2)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.communicate()
            raise TimeoutError(f"Verification deadline reached during {name}") from None
        (output / f"{name}.log").write_text(text)
        report["steps"].append({
            "name": name, "command": command, "exit_code": process.returncode,
            "elapsed_seconds": round(time.monotonic() - step_start, 3),
            "expected_failure": expected_failure,
        })
        if expected_failure == (process.returncode == 0):
            raise RuntimeError(f"Unexpected exit status in {name}: {process.returncode}\n{text}")
        print(f"{name}: expected exit status ({process.returncode})", flush=True)
        return text

    try:
        source_files = sorted(root.glob("*.lean"))
        forbidden = re.compile(r"\b(sorry|admit|axiom|unsafe|native_decide|implemented_by)\b")
        for path in source_files:
            if forbidden.search(path.read_text()):
                raise RuntimeError(f"Proof escape hatch found in {path.name}")
        report["source_sha256"] = {
            path.name: hashlib.sha256(path.read_bytes()).hexdigest()
            for path in source_files + [
                root / "lakefile.toml", root / "lean-toolchain",
                root / "lake-manifest.json", root / "verify.py",
            ]
        }
        report["lean_version"] = run("version", [args.lake, "env", "lean", "--version"]).strip()
        run("build", [args.lake, "build"])
        audit = run("audit", [args.lake, "env", "lean", "Audit.lean"])
        inventories = {
            name: [entry.strip() for entry in axioms.split(",") if entry.strip()]
            for name, axioms in re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]", audit)
        }
        if set(inventories) != EXPECTED:
            raise RuntimeError("Axiom audit did not cover exactly the expected declarations")
        for name, axioms in inventories.items():
            if not set(axioms) <= ALLOWED_AXIOMS:
                raise RuntimeError(f"Unexpected axiom dependencies: {name}: {axioms}")
        report["axioms"] = inventories
        negative = run("negative-control", [args.lake, "env", "lean", "NegativeControl.lean"], True)
        if "Type mismatch" not in negative or "IccConcrete.concrete_distance_one r" not in negative:
            raise RuntimeError("Negative control failed for an unexpected reason")
        negative_operational = run("negative-control-operational",
            [args.lake, "env", "lean", "NegativeControlOperational.lean"], True)
        if "Type mismatch" not in negative_operational or "fixed_two_probe_obstruction a ha" not in negative_operational:
            raise RuntimeError("Operational negative control failed for an unexpected reason")
        report["status"] = "passed"
    except Exception as error:
        report["status"] = "failed"
        report["error"] = str(error)
        raise
    finally:
        report["elapsed_seconds"] = round(time.monotonic() - started, 3)
        report["finished_utc"] = datetime.now(timezone.utc).isoformat()
        (output / "verification.json").write_text(json.dumps(report, indent=2) + "\n")
    print(f"Verified in {report['elapsed_seconds']} seconds; report: {output / 'verification.json'}")


if __name__ == "__main__":
    main()
