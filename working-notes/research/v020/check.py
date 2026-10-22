"""Finite matrix diagnostics, not a proof of the continuum or physical model."""

import json

import numpy as np
from numpy.polynomial.legendre import leggauss


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
VECTORS = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]]) / np.sqrt(3)
F = np.array([(I2 + x * X + y * Y + z * Z) / 4 for x, y, z in VECTORS])
M = np.sqrt(2) * F


def error(a, b):
    return float(np.linalg.norm(a - b))


def quadrature(end, order):
    nodes, weights = leggauss(order)
    return (nodes + 1) * end / 2, weights * end / 2


def evaluate(order, coupling):
    # A fixed three-level surrogate checks bookkeeping, not field limits.
    hf = np.diag([0.0, 0.9, 2.2])
    q = np.array([[0.2, 0.6, 0.1j], [0.6, -0.3, 0.4], [-0.1j, 0.4, 0.1]])
    omega, gamma, horizon = 0.8, 0.7, 1.3
    nf = len(hf)
    identity = np.eye(nf)
    p = [(I2 + Z) / 2, (I2 - Z) / 2]
    spectra = [np.linalg.eigh(hf + s * coupling * q + s * omega / 2 * identity) for s in (1, -1)]

    def sectors(t):
        return [(v * np.exp(-1j * values * t)) @ v.conj().T for values, v in spectra]

    def unitary(t):
        return sum(np.kron(u, ps) for u, ps in zip(sectors(t), p))

    injection = np.kron(identity, np.array([[1], [1]]) / np.sqrt(2))
    measurement = np.array([np.kron(identity, mj) for mj in M])
    readout = np.array([np.kron(identity, fj) for fj in F])

    def effects(t):
        a = unitary(t) @ injection
        return np.array([a.conj().T @ fj @ a for fj in readout])

    single = np.zeros((4, nf, nf), dtype=complex)
    both = np.zeros((4, 4, nf, nf), dtype=complex)
    first_direct = np.zeros_like(single)
    z2 = np.zeros((nf, nf), dtype=complex)
    nodes, weights = quadrature(horizon, order)
    for t2, weight2 in zip(nodes, weights):
        ft = effects(t2)
        single += weight2 * gamma * np.exp(-gamma * horizon) * ft
        first_direct += weight2 * gamma * np.exp(-gamma * t2) * ft
        up, um = sectors(t2)
        z2 += weight2 * gamma**2 * t2 * np.exp(-gamma * t2) * (up.conj().T @ um)
        inner_nodes, inner_weights = quadrature(t2, order)
        for t1, weight1 in zip(inner_nodes, inner_weights):
            first = measurement @ (unitary(t1) @ injection)
            after_wait = unitary(t2 - t1) @ first
            factor = weight1 * weight2 * gamma**2 * np.exp(-gamma * t2)
            for j in range(4):
                amplitudes = measurement @ after_wait[j]
                both[j] += factor * (amplitudes.conj().transpose(0, 2, 1) @ amplitudes)

    p0 = np.exp(-gamma * horizon)
    q2 = 1 - p0 * (1 + gamma * horizon)
    c2 = (z2 + z2.conj().T) / 2
    s2 = (z2 - z2.conj().T) / (2j)
    second_formula = np.array([q2 * identity / 4 + (x * c2 + y * s2) / 12 for x, y, _ in VECTORS])
    first_from_records = single + both.sum(axis=1)
    second_from_records = both.sum(axis=0)
    records = np.concatenate([[p0 * identity], single, both.reshape(16, nf, nf)])
    numbers = {
        "order": order,
        "coupling": coupling,
        "normalization_error": error(records.sum(axis=0), identity),
        "first_marginal_error": error(first_from_records, first_direct),
        "second_marginal_error": error(second_from_records, second_formula),
        "second_completion_error": error(second_from_records.sum(axis=0), q2 * identity),
        "minimum_record_eigenvalue": float(min(np.linalg.eigvalsh((a + a.conj().T) / 2).min() for a in records)),
    }
    if coupling == 0:
        numbers["zero_coupling_scalar_error"] = float(max(np.linalg.norm(a - np.trace(a) / nf * identity) for a in records))
    for key, value in numbers.items():
        if key.endswith("_error"):
            assert value < 1e-10, (key, value)
    assert numbers["minimum_record_eigenvalue"] > -1e-10
    return numbers, records


def main():
    completeness = error(sum(m.conj().T @ m for m in M), I2)
    depolarization = max(error(sum(m @ a @ m.conj().T for m in M), (a + np.trace(a) * I2) / 3) for a in (I2, X, Y, Z))
    # A label-preserving energy-covariant readout cannot have these effects.
    hj = Z / 2
    transverse = min(float(np.linalg.norm(hj @ f - f @ hj)) for f in F)
    dephased = np.array([np.diag(np.diag(f)) for f in F])
    covariance_control = max(float(np.linalg.norm(hj @ f - f @ hj)) for f in dephased)
    assert completeness < 1e-14 and depolarization < 1e-14
    assert transverse > 0.1 and covariance_control == 0
    coarse, a = evaluate(16, 0.35)
    fine, b = evaluate(24, 0.35)
    zero, _ = evaluate(16, 0.0)
    convergence = error(a, b)
    assert convergence < 1e-10
    print(json.dumps({
        "status": "passed",
        "completeness_error": completeness,
        "tetrahedral_channel_error": depolarization,
        "minimum_transverse_commutator_norm": transverse,
        "energy_diagonal_control_commutator_norm": covariance_control,
        "quadrature_convergence_error": convergence,
        "cases": [coarse, fine, zero],
        "scope": "Finite matrix checks of formulas and negative controls only; no continuum, microscopic, or Lean certificate.",
    }, indent=2))


if __name__ == "__main__":
    main()
