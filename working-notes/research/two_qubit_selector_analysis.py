#!/usr/bin/env python3
"""Numerical checks for the two-qubit Hamiltonian-selection problem.

This script supports the preliminary analysis in
feedback/two-qubit-preliminary-analysis.md. It is exploratory code, not a
computer-assisted proof.

Requirements: Python 3 and NumPy.
"""

import argparse
import itertools

import numpy as np


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
NONLOCAL_GENERATORS = [
    np.kron(left, right) / 2
    for left in (X, Y, Z)
    for right in (X, Y, Z)
]


def partial_trace_b(matrix):
    return np.trace(matrix.reshape(2, 2, 2, 2), axis1=1, axis2=3)


def partial_trace_a(matrix):
    return np.trace(matrix.reshape(2, 2, 2, 2), axis1=0, axis2=2)


def local_projection(matrix):
    scalar = np.trace(matrix).real / 4
    part_a = partial_trace_b(matrix) / 2
    part_b = partial_trace_a(matrix) / 2
    return (
        np.kron(part_a, I2)
        + np.kron(I2, part_b)
        - scalar * np.eye(4)
    )


def interaction_cost(matrix):
    scalar = np.trace(matrix).real / 4
    denominator = np.linalg.norm(matrix - scalar * np.eye(4), "fro") ** 2
    interaction = matrix - local_projection(matrix)
    return float(np.linalg.norm(interaction, "fro") ** 2 / denominator)


def pure_state_entropy(state):
    coefficient_matrix = state.reshape(2, 2)
    reduced = coefficient_matrix @ coefficient_matrix.conj().T
    eigenvalues = np.linalg.eigvalsh(reduced)
    eigenvalues = eigenvalues[eigenvalues > 1e-14]
    return float(-np.sum(eigenvalues * np.log(eigenvalues)))


def unitary_from_hermitian(generator):
    eigenvalues, eigenvectors = np.linalg.eigh(generator)
    return (eigenvectors * np.exp(-1j * eigenvalues)) @ eigenvectors.conj().T


def quotient_hessian(matrix, step=2e-4):
    """Finite-difference Hessian along the nine nonlocal Pauli directions."""

    count = len(NONLOCAL_GENERATORS)
    zero = np.zeros(count)

    def value(coordinates):
        generator = sum(
            coefficient * basis
            for coefficient, basis in zip(coordinates, NONLOCAL_GENERATORS)
        )
        unitary = unitary_from_hermitian(generator)
        transformed = unitary.conj().T @ matrix @ unitary
        return interaction_cost(transformed)

    origin = value(zero)
    result = np.zeros((count, count))
    for row in range(count):
        e_row = np.zeros(count)
        e_row[row] = step
        result[row, row] = (
            value(e_row) - 2 * origin + value(-e_row)
        ) / step**2
        for column in range(row):
            e_column = np.zeros(count)
            e_column[column] = step
            mixed = (
                value(e_row + e_column)
                - value(e_row - e_column)
                - value(-e_row + e_column)
                + value(-e_row - e_column)
            ) / (4 * step**2)
            result[row, column] = result[column, row] = mixed
    return result


def exact_global_cost(eigenvalues):
    eigenvalues = np.asarray(eigenvalues, dtype=float)
    denominator = np.sum((eigenvalues - eigenvalues.mean()) ** 2)
    pairings = (
        ((0, 1), (2, 3)),
        ((0, 2), (1, 3)),
        ((0, 3), (1, 2)),
    )
    costs = []
    for first, second in pairings:
        contrast = (
            eigenvalues[list(first)].sum()
            - eigenvalues[list(second)].sum()
        )
        costs.append(contrast**2 / (4 * denominator))
    return min(costs), costs


def haar_unitary(random, dimension=4):
    matrix = random.normal(size=(dimension, dimension)) + 1j * random.normal(
        size=(dimension, dimension)
    )
    unitary, triangular = np.linalg.qr(matrix)
    phases = np.diag(triangular).copy()
    phases /= np.abs(phases)
    return unitary @ np.diag(phases.conj())


def exp_antihermitian(generator, scale):
    hermitian = 1j * generator
    eigenvalues, eigenvectors = np.linalg.eigh(hermitian)
    return (eigenvectors * np.exp(-1j * scale * eigenvalues)) @ eigenvectors.conj().T


def descend(hamiltonian, unitary, max_steps=2000, tolerance=1e-11):
    cost = interaction_cost(unitary.conj().T @ hamiltonian @ unitary)
    for _ in range(max_steps):
        transformed = unitary.conj().T @ hamiltonian @ unitary
        local = local_projection(transformed)
        direction = transformed @ local - local @ transformed
        norm = np.linalg.norm(direction, "fro")
        if norm < tolerance:
            break
        direction /= max(1.0, norm)

        step = 1.0
        accepted = False
        while step > 1e-10:
            trial = unitary @ exp_antihermitian(direction, step)
            trial_cost = interaction_cost(trial.conj().T @ hamiltonian @ trial)
            if trial_cost < cost - 1e-14:
                unitary, cost, accepted = trial, trial_cost, True
                break
            step *= 0.5
        if not accepted:
            break
    return unitary, cost


def degenerate_near_example():
    ket00, ket01, ket10, ket11 = np.eye(4, dtype=complex)
    bell_plus = (ket01 + ket10) / np.sqrt(2)
    bell_minus = (ket01 - ket10) / np.sqrt(2)
    hamiltonian = np.kron(Z, I2) + np.kron(I2, Z)
    product_factorization = np.column_stack(
        [ket00, bell_plus, bell_minus, ket11]
    )

    high_state = bell_plus
    low_state = product_factorization.conj().T @ bell_plus
    low_hamiltonian = product_factorization.conj().T @ hamiltonian @ product_factorization
    return {
        "high_cost": interaction_cost(hamiltonian),
        "high_entropy": pure_state_entropy(high_state),
        "low_cost": interaction_cost(low_hamiltonian),
        "low_entropy": pure_state_entropy(low_state),
        "hessian": np.linalg.eigvalsh(quotient_hessian(hamiltonian)),
    }


def resonant_saddle(a=1.0, g=0.1, j=0.3):
    hamiltonian = (
        a * (np.kron(Z, I2) + np.kron(I2, Z))
        + g * (np.kron(X, X) + np.kron(Y, Y))
        + j * np.kron(Z, Z)
    )
    return interaction_cost(hamiltonian), np.linalg.eigvalsh(
        quotient_hessian(hamiltonian)
    )


def random_search(eigenvalues, starts, seed):
    random = np.random.default_rng(seed)
    hamiltonian = np.diag(eigenvalues).astype(complex)
    eigenvectors = np.eye(4, dtype=complex)
    observed = []
    for _ in range(starts):
        unitary, cost = descend(hamiltonian, haar_unitary(random))
        entropies = [
            pure_state_entropy(unitary.conj().T @ eigenvectors[:, index])
            for index in range(4)
        ]
        observed.append((cost, max(entropies)))
    return exact_global_cost(eigenvalues), observed


def permutation_hessian_counts(eigenvalues):
    rows = []
    for permutation in itertools.permutations(eigenvalues):
        matrix = np.diag(permutation).astype(complex)
        hessian = np.linalg.eigvalsh(quotient_hessian(matrix))
        nonzero = hessian[np.abs(hessian) > 2e-5]
        rows.append(
            (
                interaction_cost(matrix),
                int(np.sum(nonzero < 0)),
            )
        )
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--starts", type=int, default=24)
    parser.add_argument("--permutations", action="store_true")
    arguments = parser.parse_args()

    print("DEGENERATE NEAR-EXAMPLE")
    result = degenerate_near_example()
    for key, value in result.items():
        print(key, np.round(value, 10))

    print("\nRESONANT BELL-STATE CANDIDATE")
    cost, hessian = resonant_saddle()
    print("cost", cost)
    print("hessian", np.round(hessian, 10))

    spectra = (
        (-2.3, -0.7, 0.4, 3.8),
        (-3.0, -1.0, 1.5, 2.2),
        (-4.0, -0.2, 0.9, 5.1),
    )
    print("\nRANDOM MULTI-START DESCENT")
    for index, spectrum in enumerate(spectra):
        (exact, pairing_costs), observed = random_search(
            spectrum, arguments.starts, 100 + index
        )
        print("spectrum", spectrum)
        print("exact global", exact, "pairings", np.round(pairing_costs, 10))
        print("largest final cost error", max(abs(cost - exact) for cost, _ in observed))
        print("largest final entropy", max(entropy for _, entropy in observed))

    if arguments.permutations:
        rows = permutation_hessian_counts(spectra[0])
        summary = {}
        for cost, negatives in rows:
            key = (round(cost, 9), negatives)
            summary[key] = summary.get(key, 0) + 1
        print("\nPRODUCT-DIAGONAL CRITICAL POINTS")
        for key, count in sorted(summary.items()):
            print("cost/negative-directions", key, "count", count)


if __name__ == "__main__":
    main()
