"""Bounded two-qubit access audit; no selector, optimization, or dynamics.

Run without -O. Requires NumPy and the adjacent observational_entropy_checks.
Protocol: measurement-access-closure-2026-10-01.md.
"""

import argparse
import json
import math
from pathlib import Path

import numpy as np

from observational_entropy_checks import (
    I2, I4, NOISE, PAULIS, PHI, RHO, SHARPNESS, U, X, Y, Z,
    adjoint, binary_entropy, observations, partial_trace_b, protocols, von_neumann,
)


TOL = 1e-11
SIGNS = (1, -1)


def projector(observable, sign):
    return (I2 + sign * observable) / 2


def branches(axis, sign):
    """Local projective branch Kraus operators; intermediate label is omitted."""
    if axis == "X":
        return [np.kron(projector((X + b * Z) / math.sqrt(2), sign),
                        projector(X, b)) for b in SIGNS]
    if axis == "Y":
        return [np.kron(projector(Y, a),
                        projector((Y + a * Z) / math.sqrt(2), sign)) for a in SIGNS]
    return [np.kron(projector(Z, a), projector(Z, sign * a)) for a in SIGNS]


def effect(kraus):
    return sum(adjoint(k) @ k for k in kraus)


def channel(state, kraus):
    return sum(k @ state @ adjoint(k) for k in kraus)


def output_flip_kraus(axis, sign, eta):
    return [math.sqrt((1 + eta) / 2) * k for k in branches(axis, sign)] + [
        math.sqrt((1 - eta) / 2) * k for k in branches(axis, -sign)]


def pure(vector):
    return np.outer(vector, vector.conj())


def partial_transpose_b(state):
    return state.reshape(2, 2, 2, 2).transpose(0, 3, 2, 1).reshape(4, 4)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    residuals = {}

    def check(name, actual, expected):
        difference = float(np.max(np.abs(np.asarray(actual) - np.asarray(expected))))
        residuals[name] = max(residuals.get(name, 0.0), difference)
        assert difference < TOL, (name, difference)

    explicit = {"X": (np.kron(X, I2) + np.kron(Z, X)) / math.sqrt(2),
                "Y": (np.kron(I2, Y) + np.kron(Y, Z)) / math.sqrt(2),
                "Z": np.kron(Z, Z)}
    check("unitary", adjoint(U) @ U, I4)
    margins = {"effect_positivity": math.inf, "refinement_entropy": math.inf}
    access_residuals = {}
    ideal_kraus = {}
    for axis, sigma in PAULIS.items():
        observable = U @ np.kron(sigma, I2) @ adjoint(U)
        check("pauli_decomposition", observable, explicit[axis])
        check("observable_square", observable @ observable, I4)
        # Projection onto M2 tensor I2: all A-only observable components.
        local_part = np.kron(partial_trace_b(observable) / 2, I2)
        access_residuals[axis] = float(np.linalg.norm(observable - local_part))
        assert access_residuals[axis] > 1
        for sign in SIGNS:
            ks = branches(axis, sign)
            ideal_kraus[(axis, sign)] = ks
            for k in ks:
                check("branch_hermitian", k, adjoint(k))
                check("branch_projector", k @ k, k)
                check("branch_trace", np.trace(k), 1)
            check("ideal_effect", effect(ks), (I4 + sign * observable) / 2)
        check("axis_completeness", sum(effect(branches(axis, s)) for s in SIGNS), I4)

    z0, z1 = np.array([1, 0], complex), np.array([0, 1], complex)
    plus = (z0 + z1) / math.sqrt(2)
    plus_i = (z0 + 1j * z1) / math.sqrt(2)
    local_states = [pure(v) for v in (z0, z1, plus, plus_i)]
    spanning_states = [np.kron(a, b) for a in local_states for b in local_states]
    assert np.linalg.matrix_rank(np.array([s.reshape(-1) for s in spanning_states])) == 16
    witness_0, witness_1 = pure(I4[:, 0]), pure(I4[:, 1])
    check("same_A_marginal", partial_trace_b(witness_0), partial_trace_b(witness_1))

    probability_cases = 0
    entropy_rows = []
    witness_rows = []
    for eta in SHARPNESS:
        implemented = []
        for axis in PAULIS:
            for sign in SIGNS:
                ks = output_flip_kraus(axis, sign, eta)
                target = (I4 + sign * eta * explicit[axis]) / 2
                actual = effect(ks)
                check("unsharp_effect", actual, target)
                check("unsharp_effect_volume", np.trace(actual), 2)
                margins["effect_positivity"] = min(margins["effect_positivity"],
                                                     float(np.linalg.eigvalsh(actual)[0]))
                implemented.append(actual / 3)
                for state in spanning_states:
                    check("spanning_state_probability", np.trace(state @ actual),
                          np.trace(state @ target))
                    check("kraus_outcome_probability", np.trace(channel(state, ks)),
                          np.trace(state @ target))
                    probability_cases += 1
        check("full_povm_completeness", sum(implemented), I4)
        original = protocols(U, eta)["random_axes_recorded"]
        check("original_protocol_effects", implemented, original)
        for p in NOISE:
            state = (1 - p) * RHO + p * I4 / 4
            data, _ = observations(state, implemented)
            previous_data, _ = observations(state, original)
            check("original_protocol_probabilities", data["probabilities"],
                  previous_data["probabilities"])
            expected = 5 / 3 + binary_entropy((1 + eta * (1 - p)) / 2) / 3
            check("original_protocol_entropy", data["observational_entropy_bits"], expected)
            entropy_rows.append({"p": p, "eta": eta,
                                 "entropy_bits": data["observational_entropy_bits"]})
        parity_plus = effect(output_flip_kraus("Z", 1, eta))
        probabilities = [float(np.trace(state @ parity_plus).real)
                         for state in (witness_0, witness_1)]
        check("A_only_witness", probabilities, [(1 + eta) / 2, (1 - eta) / 2])
        witness_rows.append({"eta": eta, "plus_probabilities_00_01": probabilities})

    # The locally obtained intermediate labels refine the reported POVM.
    refined = [adjoint(k) @ k / 3 for ks in ideal_kraus.values() for k in ks]
    coarse = [effect(ks) / 3 for ks in ideal_kraus.values()]
    check("refined_completeness", sum(refined), I4)
    check("refined_volumes", [np.trace(e) for e in refined], [1 / 3] * 12)
    check("record_merging", [sum(refined[i:i + 2]) for i in range(0, 12, 2)], coarse)
    for p in NOISE:
        state = (1 - p) * RHO + p * I4 / 4
        refined_data, _ = observations(state, refined)
        coarse_data, _ = observations(state, coarse)
        margins["refinement_entropy"] = min(margins["refinement_entropy"],
            coarse_data["observational_entropy_bits"] - refined_data["observational_entropy_bits"])
    refined_ideal, _ = observations(RHO, refined)
    coarse_ideal, _ = observations(RHO, coarse)

    # Same parity statistics, different conditional state on a product input.
    product_input = pure(np.kron(plus, plus))
    parity_projector = (I4 + np.kron(Z, Z)) / 2
    luders_output = channel(product_input, [parity_projector])
    local_output = channel(product_input, branches("Z", 1))
    check("parity_outcome_probability", [np.trace(luders_output), np.trace(local_output)], [.5, .5])
    luders_conditional, local_conditional = 2 * luders_output, 2 * local_output
    check("luders_conditional", luders_conditional, pure(PHI))
    check("local_conditional", local_conditional, np.diag([.5, 0, 0, .5]))
    check("conditional_entropies", [von_neumann(luders_conditional),
                                     von_neumann(local_conditional)], [0, 1])
    ppt_luders = np.linalg.eigvalsh(partial_transpose_b(luders_conditional))
    ppt_local = np.linalg.eigvalsh(partial_transpose_b(local_conditional))
    check("luders_partial_transpose", ppt_luders, [-.5, .5, .5, .5])
    check("local_partial_transpose", ppt_local, [0, 0, .5, .5])
    for eta in SHARPNESS:
        for axis in PAULIS:
            ks = [k for sign in SIGNS for k in output_flip_kraus(axis, sign, eta)]
            check("instrument_completeness", effect(ks), I4)
    assert min(margins.values()) >= -TOL, margins

    result = {
        "status": "bounded finite access closure; no physical algebra selector",
        "numpy_version": np.__version__, "tolerance": TOL,
        "conditional_effect_checks": 18, "spanning_state_probability_checks": probability_cases,
        "spanning_input_states": 16, "matched_previous_entropy_cases": len(entropy_rows),
        "max_residuals": residuals, "minimum_margins": margins,
        "A_only_observable_projection_residuals": access_residuals,
        "A_only_witness": witness_rows, "entropy_rows": entropy_rows,
        "ideal_record_entropy_bits": {"intermediate_records_retained": refined_ideal[
            "observational_entropy_bits"], "intermediate_records_omitted": coarse_ideal[
            "observational_entropy_bits"]},
        "parity_instrument_witness": {"input": "|++>", "plus_probability": .5,
            "luders_conditional_state": "|Phi+><Phi+|",
            "local_conditional_state": "(|00><00| + |11><11|)/2",
            "luders_partial_transpose_eigenvalues": ppt_luders.tolist(),
            "local_partial_transpose_eigenvalues": ppt_local.tolist()},
    }
    if args.output:
        args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: value for key, value in result.items() if key != "entropy_rows"}, indent=2))


if __name__ == "__main__":
    main()
