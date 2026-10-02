"""Check one finite-time ranking reversal, not a selector or ICC mechanism.

Requires NumPy. Uses only 4-by-4 matrices and deterministic quadrature.
"""

import json
import math

import numpy as np
from numpy.polynomial.legendre import leggauss


def hs_squared(matrix):
    return float(np.vdot(matrix, matrix).real)


def main():
    identity = np.eye(2, dtype=complex)
    x = np.array([[0, 1], [1, 0]], dtype=complex)
    y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    z = np.diag([1, -1]).astype(complex)
    paulis = (identity, x, y, z)
    probes_a = [np.kron(p, identity) for p in paulis]
    probes_b = [np.kron(identity, p) for p in paulis]
    hamiltonian = 2 * probes_a[3] + 0.5 * probes_b[3] + np.kron(z, z)
    rho = np.diag([1, 0, 0, 0]).astype(complex)
    controlled_x = np.zeros((4, 4), dtype=complex)
    for a in range(2):
        for b in range(2):
            controlled_x[2 * (a ^ b) + b, 2 * a + b] = 1
    nodes, weights = leggauss(64)
    times = (nodes + 1) / 2
    weights = weights / 2
    max_error = 0.0
    results = []

    for name, unitary, coupling, expected_cost in (
        ("identity", np.eye(4), 1.0, 4 / 21),
        ("controlled_x_from_second_qubit", controlled_x, 2.0, 16 / 21),
    ):
        k = unitary.conj().T @ hamiltonian @ unitary
        tensor = k.reshape(2, 2, 2, 2)
        local_a = np.trace(tensor, axis1=1, axis2=3) / 2
        local_b = np.trace(tensor, axis1=0, axis2=2) / 2
        scalar = np.trace(k) / 4
        residual = (k - np.kron(local_a, identity)
                    - np.kron(identity, local_b) + scalar * np.eye(4))
        cost = hs_squared(residual) / hs_squared(hamiltonian)
        eigenvalues, eigenvectors = np.linalg.eigh(k)
        assert np.min(np.diff(eigenvalues)) > 0
        assert np.allclose(unitary.conj().T @ unitary, np.eye(4))
        integrated = 0.0

        for time, weight in zip(times, weights):
            v = (eigenvectors * np.exp(-1j * time * eigenvalues)) @ eigenvectors.conj().T
            realigned = v.reshape(2, 2, 2, 2).transpose(0, 2, 1, 3).reshape(4, 4)
            product = realigned @ realigned.conj().T
            g_realignment = 1 - float(np.trace(product @ product).real) / 16

            # Pauli twirling is exact for the first Haar moments used here.
            g_commutator = 0.0
            for a in probes_a:
                for b in probes_b:
                    evolved_b = v @ b @ v.conj().T
                    g_commutator += hs_squared(a @ evolved_b - evolved_b @ a)
            g_commutator /= 16 * 2 * 4
            g_exact = 0.5 * math.sin(2 * coupling * time) ** 2
            max_error = max(max_error, abs(g_realignment - g_exact),
                            abs(g_commutator - g_exact))
            integrated += weight * g_realignment

        exact_average = 0.25 - math.sin(4 * coupling) / (16 * coupling)
        max_error = max(max_error, abs(integrated - exact_average),
                        abs(cost - expected_cost))
        state = unitary.conj().T @ rho @ unitary
        reduced = np.trace(state.reshape(2, 2, 2, 2), axis1=1, axis2=3)
        purity = float(np.trace(reduced @ reduced).real)
        assert abs(purity - 1) < 1e-13
        results.append({"candidate": name, "interaction_cost": cost,
                        "finite_time_average_T1": float(integrated),
                        "exact_average": exact_average,
                        "selected_state_reduced_purity": purity})

    assert max_error < 1e-12, max_error
    assert results[0]["interaction_cost"] < results[1]["interaction_cost"]
    assert results[0]["finite_time_average_T1"] > results[1]["finite_time_average_T1"]
    print(json.dumps({"candidates": results, "maximum_absolute_error": max_error,
                      "scope": "Ranking only; both state entropies are zero. "
                               "No optimization or strict-minimum certification."}, indent=2))


if __name__ == "__main__":
    main()
