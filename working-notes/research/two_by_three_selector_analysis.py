#!/usr/bin/env python3
"""Exploratory checks of the interaction selector in 2 x 3 dimensions.

This is numerical support for the general proof sketch in
feedback/general-no-go-analysis.md. It is not a computer-assisted proof.

Requirements: Python 3 and NumPy.
"""

import argparse

import numpy as np


D_A = 2
D_B = 3
DIMENSION = D_A * D_B


def partial_trace_b(matrix):
    reshaped = matrix.reshape(D_A, D_B, D_A, D_B)
    return np.trace(reshaped, axis1=1, axis2=3)


def partial_trace_a(matrix):
    reshaped = matrix.reshape(D_A, D_B, D_A, D_B)
    return np.trace(reshaped, axis1=0, axis2=2)


def local_projection(matrix):
    scalar = np.trace(matrix).real / DIMENSION
    return (
        np.kron(partial_trace_b(matrix) / D_B, np.eye(D_B))
        + np.kron(np.eye(D_A), partial_trace_a(matrix) / D_A)
        - scalar * np.eye(DIMENSION)
    )


def interaction_cost(matrix):
    scalar = np.trace(matrix).real / DIMENSION
    denominator = np.linalg.norm(
        matrix - scalar * np.eye(DIMENSION), "fro"
    ) ** 2
    interaction = matrix - local_projection(matrix)
    return float(np.linalg.norm(interaction, "fro") ** 2 / denominator)


def pure_state_entropy(state):
    coefficient_matrix = state.reshape(D_A, D_B)
    reduced = coefficient_matrix @ coefficient_matrix.conj().T
    eigenvalues = np.linalg.eigvalsh(reduced)
    eigenvalues = eigenvalues[eigenvalues > 1e-14]
    return float(-np.sum(eigenvalues * np.log(eigenvalues)))


def haar_unitary(random):
    matrix = random.normal(size=(DIMENSION, DIMENSION)) + 1j * random.normal(
        size=(DIMENSION, DIMENSION)
    )
    unitary, triangular = np.linalg.qr(matrix)
    phases = np.diag(triangular).copy()
    phases /= np.abs(phases)
    return unitary @ np.diag(phases.conj())


def exp_antihermitian(generator, scale):
    hermitian = 1j * generator
    eigenvalues, eigenvectors = np.linalg.eigh(hermitian)
    return (eigenvectors * np.exp(-1j * scale * eigenvalues)) @ eigenvectors.conj().T


def descend(hamiltonian, unitary, max_steps=4000, tolerance=1e-10):
    cost = interaction_cost(unitary.conj().T @ hamiltonian @ unitary)
    for _ in range(max_steps):
        transformed = unitary.conj().T @ hamiltonian @ unitary
        local = local_projection(transformed)
        direction = transformed @ local - local @ transformed
        residual = np.linalg.norm(direction, "fro")
        if residual < tolerance:
            break
        direction /= max(1.0, residual)

        step = 1.0
        accepted = False
        while step > 1e-11:
            trial = unitary @ exp_antihermitian(direction, step)
            trial_cost = interaction_cost(
                trial.conj().T @ hamiltonian @ trial
            )
            if trial_cost < cost - 1e-14:
                unitary, cost, accepted = trial, trial_cost, True
                break
            step *= 0.5
        if not accepted:
            break

    transformed = unitary.conj().T @ hamiltonian @ unitary
    critical_residual = np.linalg.norm(
        transformed @ local_projection(transformed)
        - local_projection(transformed) @ transformed,
        "fro",
    )
    return unitary, cost, critical_residual


def random_search(spectrum, starts, seed):
    random = np.random.default_rng(seed)
    hamiltonian = np.diag(spectrum).astype(complex)
    eigenvectors = np.eye(DIMENSION, dtype=complex)
    rows = []
    for _ in range(starts):
        unitary, cost, residual = descend(hamiltonian, haar_unitary(random))
        entropies = [
            pure_state_entropy(unitary.conj().T @ eigenvectors[:, index])
            for index in range(DIMENSION)
        ]
        rows.append((cost, max(entropies), residual))
    rows.sort()
    return rows


def rotation(first, second, angle):
    result = np.eye(DIMENSION, dtype=complex)
    cosine = np.cos(angle)
    sine = np.sin(angle)
    result[first, first] = cosine
    result[first, second] = sine
    result[second, first] = -sine
    result[second, second] = cosine
    return result


def degenerate_and_resonant_examples(coupling=0.2):
    energies_a = np.array([0.0, 1.0])
    energies_b = np.array([0.0, 1.0, 3.0])
    local_hamiltonian = np.diag(
        [a + b for a in energies_a for b in energies_b]
    ).astype(complex)

    # |0,1> and |1,0> both have energy 1.
    first = 1
    second = 3
    basis = np.eye(DIMENSION, dtype=complex)
    bell_like = (basis[:, first] + basis[:, second]) / np.sqrt(2)

    product_factorization = rotation(first, second, np.pi / 4)
    low_state = product_factorization.conj().T @ bell_like

    interaction = np.zeros((DIMENSION, DIMENSION), dtype=complex)
    interaction[first, second] = interaction[second, first] = coupling
    resonant_hamiltonian = local_hamiltonian + interaction

    step = 1e-4
    costs = []
    for angle in (-step, 0.0, step, np.pi / 4):
        unitary = rotation(first, second, angle)
        transformed = unitary.conj().T @ resonant_hamiltonian @ unitary
        costs.append((angle, interaction_cost(transformed)))
    second_derivative = (costs[0][1] - 2 * costs[1][1] + costs[2][1]) / step**2

    return {
        "degenerate_high_cost": interaction_cost(local_hamiltonian),
        "degenerate_high_entropy": pure_state_entropy(bell_like),
        "degenerate_low_cost": interaction_cost(
            product_factorization.conj().T
            @ local_hamiltonian
            @ product_factorization
        ),
        "degenerate_low_entropy": pure_state_entropy(low_state),
        "resonant_costs": costs,
        "resonant_second_derivative": second_derivative,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--starts", type=int, default=32)
    arguments = parser.parse_args()

    print("DEGENERATE AND RESONANT 2 x 3 EXAMPLES")
    examples = degenerate_and_resonant_examples()
    for key, value in examples.items():
        print(key, value)

    spectra = (
        (-3.2, -1.7, -0.4, 0.8, 2.1, 4.6),
        (-4.1, -2.0, -0.3, 1.2, 2.8, 5.7),
    )
    print("\nRANDOM SIMPLE-SPECTRUM SEARCH")
    for index, spectrum in enumerate(spectra):
        rows = random_search(spectrum, arguments.starts, 300 + index)
        best_cost = rows[0][0]
        near_best = [row for row in rows if row[0] <= best_cost + 1e-8]
        print("spectrum", spectrum)
        print("best cost", best_cost)
        print("near-best runs", len(near_best), "of", len(rows))
        print("largest near-best entropy", max(row[1] for row in near_best))
        print("largest near-best critical residual", max(row[2] for row in near_best))
        clusters = {}
        for cost, entropy, residual in rows:
            key = round(cost, 8)
            cluster = clusters.setdefault(
                key, {"count": 0, "entropy": 0.0, "residual": 0.0}
            )
            cluster["count"] += 1
            cluster["entropy"] = max(cluster["entropy"], entropy)
            cluster["residual"] = max(cluster["residual"], residual)
        for cost, cluster in sorted(clusters.items())[:10]:
            print(
                "cluster",
                cost,
                "count",
                cluster["count"],
                "max entropy",
                cluster["entropy"],
                "max residual",
                cluster["residual"],
            )


if __name__ == "__main__":
    main()
