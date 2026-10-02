"""Fixed finite POVM entropy checks, not an algebra selector or transition model.

Requires NumPy. Protocol: observational-entropy-gate-2026-10-01.md.
All volumes use the unnormalized trace on the SAME four-dimensional space.
"""

import argparse
import json
import math
from pathlib import Path

import numpy as np


I2 = np.eye(2, dtype=complex)
I4 = np.eye(4, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
PAULIS = {"X": X, "Y": Y, "Z": Z}
PHI = np.array([1, 0, 0, 1], dtype=complex) / math.sqrt(2)
RHO = np.outer(PHI, PHI.conj())
U = np.column_stack((PHI, np.array([1, 0, 0, -1]) / math.sqrt(2),
                     I4[:, 1], I4[:, 2]))
NOISE = (0.0, 0.1, 0.5, 1.0)
SHARPNESS = (0.0, 0.5, 1.0)
TOL = 1e-11


def adjoint(matrix):
    return matrix.conj().T


def entropy(probabilities):
    probabilities = np.asarray(probabilities, dtype=float)
    assert float(np.min(probabilities)) >= -TOL
    assert abs(float(np.sum(probabilities)) - 1) < TOL
    positive = probabilities[probabilities > 0]
    return float(-np.sum(positive * np.log2(positive)))


def von_neumann(matrix):
    assert np.max(abs(matrix - adjoint(matrix))) < TOL
    return entropy(np.linalg.eigvalsh(matrix))


def binary_entropy(probability):
    return entropy([probability, 1 - probability])


def partial_trace_b(matrix):
    return np.einsum("iaka->ik", matrix.reshape(2, 2, 2, 2))


def protocols(embedding, eta):
    singles = {}
    main = []
    for axis, sigma in PAULIS.items():
        effects = [embedding @ np.kron((I2 + sign * eta * sigma) / 2, I2)
                   @ adjoint(embedding) for sign in (1, -1)]
        singles[axis] = effects
        main.extend([effect / 3 for effect in effects])
    return {"random_axes_recorded": main, **singles,
            "uninformative": [I4],
            "axis_forgotten": [sum(main[index::2]) for index in (0, 1)],
            "sign_forgotten": [sum(main[index:index + 2]) for index in (0, 2, 4)]}


def observations(state, effects):
    probabilities = np.array([np.trace(state @ effect).real for effect in effects])
    volumes = np.array([np.trace(effect).real for effect in effects])
    assert min(volumes) > 0
    assert min(probabilities) >= -TOL
    assert max(abs(np.trace(state @ effect).imag) for effect in effects) < TOL
    probabilities = np.maximum(probabilities, 0)
    positive = probabilities > 0
    value = float(-np.sum(probabilities[positive] * np.log2(
        probabilities[positive] / volumes[positive])))
    coarse_state = sum(p * effect / volume for p, effect, volume in
                       zip(probabilities, effects, volumes))
    return {"probabilities": probabilities.tolist(), "volumes": volumes.tolist(),
            "observational_entropy_bits": value,
            "outcome_shannon_entropy_bits": entropy(probabilities),
            "petz_coarse_state_entropy_bits": von_neumann(coarse_state)}, coarse_state


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    assert np.max(abs(adjoint(U) @ U - I4)) < TOL
    assert np.max(abs(U @ np.kron(Z, I2) @ adjoint(U) - np.kron(Z, Z))) < TOL
    assert np.max(abs(adjoint(U) @ RHO @ U - np.diag([1, 0, 0, 0]))) < TOL
    hadamard = np.array([[1, 1], [1, -1]]) / math.sqrt(2)
    frame_controls = (U, np.kron(hadamard, np.diag([1, 1j])))
    rows = []
    maxima = {"povm_completeness": 0.0, "probability_sum": 0.0,
              "volume_sum": 0.0, "negative_effect_eigenvalue": 0.0,
              "analytic_entropy": 0.0, "global_entropy": 0.0,
              "reduced_entropy": 0.0, "petz_state_formula": 0.0,
              "covariance_probability": 0.0, "covariance_volume": 0.0,
              "covariance_entropy": 0.0}
    margins = {"observational_above_global": math.inf,
               "petz_entropy_above_observational": math.inf,
               "observational_above_algebra_completion": math.inf,
               "postprocessing_entropy_increase": math.inf}

    for p in NOISE:
        state = (1 - p) * RHO + p * I4 / 4
        global_entropy = von_neumann(state)
        global_expected = entropy([1 - 3 * p / 4] + [p / 4] * 3)
        maxima["global_entropy"] = max(maxima["global_entropy"],
                                         abs(global_entropy - global_expected))
        for name, embedding in (("old", I4), ("new", U)):
            coordinates = adjoint(embedding) @ state @ embedding
            local_state = partial_trace_b(coordinates)
            reduced_entropy = von_neumann(local_state)
            expected_reduced = 1.0 if name == "old" else binary_entropy(p / 2)
            maxima["reduced_entropy"] = max(maxima["reduced_entropy"],
                                             abs(reduced_entropy - expected_reduced))
            for eta in SHARPNESS:
                results = {}
                for protocol, effects in protocols(embedding, eta).items():
                    completeness = float(np.max(abs(sum(effects) - I4)))
                    maxima["povm_completeness"] = max(maxima["povm_completeness"], completeness)
                    for effect in effects:
                        assert np.max(abs(effect - adjoint(effect))) < TOL
                        negative = max(0.0, -float(np.linalg.eigvalsh(effect)[0]))
                        maxima["negative_effect_eigenvalue"] = max(
                            maxima["negative_effect_eigenvalue"], negative)
                    result, coarse_state = observations(state, effects)
                    results[protocol] = result
                    so = result["observational_entropy_bits"]
                    maxima["probability_sum"] = max(maxima["probability_sum"],
                        abs(sum(result["probabilities"]) - 1))
                    maxima["volume_sum"] = max(maxima["volume_sum"],
                        abs(sum(result["volumes"]) - 4))
                    x = eta * (1 - p)
                    expected = 2.0
                    if name == "new":
                        if protocol == "Z":
                            expected = 1 + binary_entropy((1 + x) / 2)
                        elif protocol == "random_axes_recorded":
                            expected = 1 + (2 + binary_entropy((1 + x) / 2)) / 3
                        elif protocol == "axis_forgotten":
                            expected = 1 + binary_entropy((1 + x / 3) / 2)
                    maxima["analytic_entropy"] = max(maxima["analytic_entropy"], abs(so - expected))
                    margins["observational_above_global"] = min(
                        margins["observational_above_global"], so - global_entropy)
                    margins["petz_entropy_above_observational"] = min(
                        margins["petz_entropy_above_observational"],
                        result["petz_coarse_state_entropy_bits"] - so)
                    margins["observational_above_algebra_completion"] = min(
                        margins["observational_above_algebra_completion"], so - 1 - reduced_entropy)
                    if protocol == "random_axes_recorded":
                        expected_local = I2 / 2 if name == "old" else (
                            I2 + eta ** 2 * (1 - p) * Z / 3) / 2
                        expected_coarse = embedding @ np.kron(expected_local, I2 / 2) @ adjoint(embedding)
                        maxima["petz_state_formula"] = max(maxima["petz_state_formula"],
                            float(np.max(abs(coarse_state - expected_coarse))))
                    for frame in frame_controls:
                        transformed, _ = observations(frame @ state @ adjoint(frame),
                            [frame @ effect @ adjoint(frame) for effect in effects])
                        for key, result_key in (("covariance_probability", "probabilities"),
                                                ("covariance_volume", "volumes")):
                            maxima[key] = max(maxima[key], float(np.max(abs(
                                np.array(result[result_key]) - transformed[result_key]))))
                        maxima["covariance_entropy"] = max(maxima["covariance_entropy"],
                            abs(so - transformed["observational_entropy_bits"]))
                for protocol in ("axis_forgotten", "sign_forgotten", "uninformative"):
                    increase = results[protocol]["observational_entropy_bits"] - results[
                        "random_axes_recorded"]["observational_entropy_bits"]
                    margins["postprocessing_entropy_increase"] = min(
                        margins["postprocessing_entropy_increase"], increase)
                rows.append({"noise_p": p, "sharpness_eta": eta, "embedding": name,
                             "global_entropy_bits": global_entropy,
                             "reduced_state_entropy_bits": reduced_entropy,
                             "algebra_completion_entropy_bits": 1 + reduced_entropy,
                             "protocols": results})

    assert max(maxima.values()) < TOL, maxima
    assert min(margins.values()) >= -TOL, margins
    ideal = {row["embedding"]: row for row in rows
             if row["noise_p"] == 0 and row["sharpness_eta"] == 1}
    assert abs(ideal["old"]["protocols"]["random_axes_recorded"][
        "observational_entropy_bits"] - 2) < TOL
    assert abs(ideal["new"]["protocols"]["random_axes_recorded"][
        "observational_entropy_bits"] - 5 / 3) < TOL
    result = {"status": "fixed protocol identity checks, not a physical entropy reset",
              "numpy_version": np.__version__, "tolerance": TOL,
              "units": "bits, global trace volumes on dimension four",
              "state_embedding_cases": len(rows), "povm_cases": 7 * len(rows),
              "max_residuals": maxima, "minimum_inequality_margins": margins,
              "ideal_cases": ideal, "rows": rows}
    if args.output:
        args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: value for key, value in result.items() if key != "rows"}, indent=2))


if __name__ == "__main__":
    main()
