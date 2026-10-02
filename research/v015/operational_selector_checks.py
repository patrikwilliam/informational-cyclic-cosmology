"""Fixed normalization and timing checks; no selector search or optimization.

Requires NumPy. Protocol: operational-selector-gate-2026-09-29.md.
Choi ordering is output tensor reference; all Choi matrices have trace one.
"""

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss


I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
TOL = 1e-11


def adjoint(matrix):
    return matrix.conj().T


def purity(matrix):
    return float(np.trace(matrix @ matrix).real)


def channel(w, da, db, matrix):
    evolved = w @ np.kron(matrix, np.eye(db) / db) @ adjoint(w)
    return np.einsum("iaka->ik", evolved.reshape(da, db, da, db))


def choi_by_matrix_units(w, da, db):
    return choi_from_action(lambda matrix: channel(w, da, db, matrix), da)


def choi_from_action(action, da):
    result = np.zeros((da * da, da * da), dtype=complex)
    for j in range(da):
        for k in range(da):
            unit = np.zeros((da, da), dtype=complex)
            unit[j, k] = 1
            result += np.kron(action(unit), unit) / da
    return result


def choi_by_realignment(w, da, db):
    m = w.reshape(da, db, da, db).transpose(0, 2, 1, 3)
    m = m.reshape(da * da, db * db)
    return m @ adjoint(m) / (da * db)


def weyl_unitaries(dimension):
    shift = np.roll(np.eye(dimension), 1, axis=0)
    phase = np.diag(np.exp(2j * np.pi * np.arange(dimension) / dimension))
    return [np.linalg.matrix_power(shift, p) @ np.linalg.matrix_power(phase, q)
            for p in range(dimension) for q in range(dimension)]


def commutator_score(w, da, db):
    costs = []
    for a in weyl_unitaries(da):
        full_a = np.kron(a, np.eye(db))
        for b in weyl_unitaries(db):
            evolved_b = w @ np.kron(np.eye(da), b) @ adjoint(w)
            commutator = full_a @ evolved_b - evolved_b @ full_a
            costs.append(np.linalg.norm(commutator, "fro") ** 2 / (2 * da * db))
    return float(np.mean(costs))


def random_unitary(dimension, rng):
    matrix = rng.normal(size=(dimension, dimension))
    matrix = matrix + 1j * rng.normal(size=(dimension, dimension))
    q, r = np.linalg.qr(matrix)
    phases = np.diag(r)
    return q * (phases / np.abs(phases))


def propagator(h, time):
    energies, vectors = np.linalg.eigh(h)
    return (vectors * np.exp(-1j * time * energies)) @ adjoint(vectors)


def integrated_channel_cost(h, horizon, count):
    nodes, weights = leggauss(count)
    states = [choi_by_matrix_units(propagator(h, horizon * (node + 1) / 2), 2, 2)
              for node in nodes]
    weights = weights / 2
    mean_purity = float(weights @ np.array([purity(state) for state in states]))
    mean_state = np.einsum("n,nij->ij", weights, states)
    variance = float(weights @ np.array([
        np.linalg.norm(state - mean_state, "fro") ** 2 for state in states]))
    return {"cost": 1 - mean_purity,
            "unrecorded_time_choi_entropy": 1 - purity(mean_state),
            "timing_variance": variance,
            "jensen_residual": abs(mean_purity - purity(mean_state) - variance)}


def recovery_supplement(controls):
    phi = lambda n: np.eye(n).reshape(-1) / math.sqrt(n)
    lower_identity_residual = 0.0
    for _, da, db, w, _ in controls:
        j = choi_by_matrix_units(w, da, db)
        recovered = choi_from_action(lambda matrix: channel(
            adjoint(w), da, db, channel(w, da, db, matrix)), da)
        overlap = float(np.vdot(phi(da), recovered @ phi(da)).real)
        lower_identity_residual = max(lower_identity_residual, abs(overlap - purity(j)))
    assert lower_identity_residual < TOL

    theta = math.acos(3 ** (-0.25))
    c = math.pi / 4 - theta / 2
    swap = np.eye(4)[:, [0, 2, 1, 3]]
    h = theta * swap + c * (np.kron(Z, I) + np.kron(I, Z))
    v = np.array([[0, 0, 1, 0], [1, 1, 0, 0],
                  [-1, 1, 0, 0], [0, 0, 0, 1]], dtype=complex)
    v[:, :2] /= math.sqrt(2)
    expected = np.array([-theta, theta, math.pi / 2, 2 * theta - math.pi / 2])
    assert np.max(abs(adjoint(v) @ h @ v - np.diag(expected))) < TOL
    assert np.min(expected[1:] - expected[0]) > 0
    rows = []
    for name, k, optimum, reverse_decoder in (
            ("reference", h, (1 + math.sqrt(3)) / 4, propagator(c * Z, 1)),
            ("energy_product", adjoint(v) @ h @ v, 0.5, I)):
        w = propagator(k, 1)
        j = choi_by_matrix_units(w, 2, 2)
        values = np.linalg.eigvalsh(j)
        # Degenerate eigenspaces need not have maximally entangled solver eigenvectors.
        # Use the explicit decoder from the analytic channel expression instead.
        assert np.max(abs(adjoint(reverse_decoder) @ reverse_decoder - I)) < TOL
        recovered = choi_from_action(lambda matrix: adjoint(reverse_decoder)
            @ channel(w, 2, 2, matrix) @ reverse_decoder, 2)
        fidelity = float(np.vdot(phi(2), recovered @ phi(2)).real)
        assert abs(fidelity - values[-1]) < TOL
        assert abs(fidelity - optimum) < TOL
        assert abs(purity(j) - 0.5) < TOL
        rows.append({"embedding": name, "choi_purity": purity(j),
                     "optimal_fidelity_attained": fidelity,
                     "choi_eigenvalues": values.tolist()})

    # Reuse the existing rational integration certificate, not decimal costs.
    from finite_time_bell_certificate import integrate
    record = json.loads(Path(__file__).with_name(
        "finite_time_bell_certificate_results.json").read_text())
    coefficients = {int(k): Fraction(v) for k, v in
                    record["bell_cost_fourier_coefficients"].items()}
    bell_lower, _ = integrate(coefficients)
    _, product_upper = integrate({0: Fraction(1, 4), -4: Fraction(-1, 8),
                                  4: Fraction(-1, 8)})
    assert 1 - bell_lower < Fraction(670, 1000) ** 2
    assert 1 - product_upper > Fraction(772, 1000)
    return {"adjoint_decoder_identity_residual": lower_identity_residual,
            "same_H_equal_purity_cases": rows,
            "certified_known_time_bell_optimum_less_than": "670/1000",
            "certified_known_time_product_optimum_greater_than": "772/1000",
            "certificate_dependency": "existing Bell Fourier coefficients and rational sinc enclosures",
            "scope": "Derived-claim supplement; no new horizon, optimizer or minimum claim"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rng = np.random.default_rng(20260929)
    cnot = np.array([[1, 0, 0, 0], [0, 1, 0, 0],
                     [0, 0, 0, 1], [0, 0, 1, 0]], dtype=complex)
    swap = np.eye(4, dtype=complex)[:, [0, 2, 1, 3]]
    controls = [("identity", 2, 2, np.eye(4), 0.0),
                ("cnot", 2, 2, cnot, 0.5), ("swap", 2, 2, swap, 0.75)]
    for da, db in ((2, 2), (2, 3), (3, 2)):
        for index in range(3):
            controls.append((f"seeded_{da}x{db}_{index}", da, db,
                             random_unitary(da * db, rng), None))

    residuals = {"choi_identity": 0.0, "commutator_identity": 0.0,
                 "trace_preserving": 0.0, "unital": 0.0,
                 "trace_one": 0.0, "hermitian": 0.0,
                 "negative_eigenvalue": 0.0, "control_value": 0.0,
                 "unitary": 0.0}
    rows = []
    for name, da, db, w, expected in controls:
        j = choi_by_matrix_units(w, da, db)
        realigned = choi_by_realignment(w, da, db)
        tensor = j.reshape(da, da, da, da)
        score = 1 - purity(j)
        checks = {
            "choi_identity": float(np.max(abs(j - realigned))),
            "commutator_identity": abs(score - commutator_score(w, da, db)),
            "trace_preserving": float(np.max(abs(
                np.einsum("ijil->jl", tensor) - np.eye(da) / da))),
            "unital": float(np.max(abs(
                np.einsum("ijkj->ik", tensor) - np.eye(da) / da))),
            "trace_one": float(abs(np.trace(j) - 1)),
            "hermitian": float(np.max(abs(j - adjoint(j)))),
            "negative_eigenvalue": max(0.0, -float(np.linalg.eigvalsh(j)[0])),
            "control_value": 0.0 if expected is None else abs(score - expected),
            "unitary": float(np.max(abs(adjoint(w) @ w - np.eye(da * db)))),
        }
        for key, val in checks.items():
            residuals[key] = max(residuals[key], val)
        rows.append({"case": name, "d_a": da, "d_b": db, "score": score})
    assert max(residuals.values()) < TOL, residuals

    time_states = [choi_by_matrix_units(propagator(np.kron(Z, I), t), 2, 2)
                   for t in (0, math.pi / 2)]
    mean = sum(time_states) / 2
    timing = {"recorded_time_average_score": 1 - sum(map(purity, time_states)) / 2,
              "unrecorded_time_channel_score": 1 - purity(mean),
              "unrecorded_time_choi_eigenvalues": np.linalg.eigvalsh(mean).tolist()}
    assert abs(timing["recorded_time_average_score"]) < TOL, timing
    assert abs(timing["unrecorded_time_channel_score"] - 0.5) < TOL, timing

    bell = sum(c * np.kron(p, p) for c, p in ((1, X), (2, Y), (3, Z))) / math.sqrt(14)
    product = np.diag([-6, 0, 2, 4]) / math.sqrt(14)
    costs = {}
    quadrature_residual = 0.0
    for name, h in (("bell", bell), ("product_competitor", product)):
        first = integrated_channel_cost(h, 8, 64)
        second = integrated_channel_cost(h, 8, 128)
        quadrature_residual = max(quadrature_residual,
                                  max(abs(first[key] - second[key]) for key in first))
        assert second["jensen_residual"] < TOL, second
        costs[name] = second
    assert quadrature_residual < TOL, quadrature_residual
    assert abs(costs["bell"]["cost"] - 0.5520317539568727) < TOL
    assert abs(costs["product_competitor"]["cost"] - 0.22761185052885366) < TOL
    assert costs["bell"]["cost"] - costs["product_competitor"]["cost"] > 0.3

    result = {"status": "bounded numerical checks and reused exact scalar bounds; not a physical selector",
              "seed": 20260929, "numpy_version": np.__version__,
              "tolerance": TOL, "residuals": residuals, "identity_cases": rows,
              "known_vs_unknown_time": timing, "existing_competitor_costs": costs,
              "quadrature_residual": quadrature_residual,
              "recovery_supplement": recovery_supplement(controls)}
    if args.output:
        args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
