#!/usr/bin/env python3
"""Finite CAR check of an Einstein-Cartan-inspired algebra selector.

This is exploratory code for a two-cell truncation with four Dirac modes per
cell.  It uses the normal-ordered axial-current contact operator

    H_4 = sum_x (:J^0_{5,x} J^0_{5,x}:
                 - sum_i :J^i_{5,x} J^i_{5,x}:)

and a massless one-link Dirac kinetic term.  Candidate subsystem structures
are obtained from a common U(2) rotation of the two cells, lifted to fermionic
Fock space.  The script checks the Hilbert-Schmidt interaction-projection cost
against a closed-form expression on this restricted CAR-preserving family.

The model is a finite relativistic truncation, not a discretization of the
full Einstein-Cartan field equations or a cosmological solution.
"""

from __future__ import annotations

import argparse
import itertools

import numpy as np


SPINOR_DIMENSION = 4
CELL_COUNT = 2
MODE_COUNT = SPINOR_DIMENSION * CELL_COUNT
FOCK_DIMENSION = 1 << MODE_COUNT
FACTOR_DIMENSION = 1 << SPINOR_DIMENSION


def annihilation_operator(mode: int) -> np.ndarray:
    """Return c_mode in the ordered occupation-number basis."""

    result = np.zeros((FOCK_DIMENSION, FOCK_DIMENSION), dtype=complex)
    bit = MODE_COUNT - 1 - mode
    for source in range(FOCK_DIMENSION):
        if not (source >> bit) & 1:
            continue
        occupied_before = sum(
            (source >> (MODE_COUNT - 1 - earlier)) & 1
            for earlier in range(mode)
        )
        target = source & ~(1 << bit)
        result[target, source] = -1 if occupied_before % 2 else 1
    return result


def dirac_matrices() -> tuple[list[np.ndarray], np.ndarray, list[np.ndarray]]:
    """Return gamma matrices, gamma^5, and alpha matrices in Dirac basis."""

    identity_2 = np.eye(2, dtype=complex)
    zero_2 = np.zeros((2, 2), dtype=complex)
    pauli = [
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    ]
    gamma_0 = np.block([[identity_2, zero_2], [zero_2, -identity_2]])
    gamma_spatial = [
        np.block([[zero_2, sigma], [-sigma, zero_2]]) for sigma in pauli
    ]
    gamma = [gamma_0, *gamma_spatial]
    gamma_5 = 1j * gamma[0] @ gamma[1] @ gamma[2] @ gamma[3]
    alpha = [gamma_0 @ matrix for matrix in gamma_spatial]
    return gamma, gamma_5, alpha


def bilinear(
    matrix: np.ndarray,
    cell: int,
    creators: list[np.ndarray],
    annihilators: list[np.ndarray],
) -> np.ndarray:
    """Return psi_cell^dagger matrix psi_cell."""

    result = np.zeros((FOCK_DIMENSION, FOCK_DIMENSION), dtype=complex)
    offset = cell * SPINOR_DIMENSION
    for row in range(SPINOR_DIMENSION):
        for column in range(SPINOR_DIMENSION):
            coefficient = matrix[row, column]
            if abs(coefficient) > 1e-15:
                result += (
                    coefficient
                    * creators[offset + row]
                    @ annihilators[offset + column]
                )
    return result


def cross_bilinear(
    matrix: np.ndarray,
    left_cell: int,
    right_cell: int,
    creators: list[np.ndarray],
    annihilators: list[np.ndarray],
) -> np.ndarray:
    """Return psi_left^dagger matrix psi_right."""

    result = np.zeros((FOCK_DIMENSION, FOCK_DIMENSION), dtype=complex)
    left_offset = left_cell * SPINOR_DIMENSION
    right_offset = right_cell * SPINOR_DIMENSION
    for row in range(SPINOR_DIMENSION):
        for column in range(SPINOR_DIMENSION):
            coefficient = matrix[row, column]
            if abs(coefficient) > 1e-15:
                result += (
                    coefficient
                    * creators[left_offset + row]
                    @ annihilators[right_offset + column]
                )
    return result


def quadratic_operator(matrix: np.ndarray) -> np.ndarray:
    """Second-quantize an eight-mode one-particle Hermitian matrix."""

    annihilators = [annihilation_operator(mode) for mode in range(MODE_COUNT)]
    creators = [operator.conj().T for operator in annihilators]
    result = np.zeros((FOCK_DIMENSION, FOCK_DIMENSION), dtype=complex)
    for row in range(MODE_COUNT):
        for column in range(MODE_COUNT):
            coefficient = matrix[row, column]
            if abs(coefficient) > 1e-15:
                result += coefficient * creators[row] @ annihilators[column]
    return result


def build_hamiltonians() -> tuple[np.ndarray, np.ndarray]:
    """Construct the one-link kinetic and axial-current contact operators."""

    annihilators = [annihilation_operator(mode) for mode in range(MODE_COUNT)]
    creators = [operator.conj().T for operator in annihilators]
    _, gamma_5, alpha = dirac_matrices()

    forward = cross_bilinear(alpha[0], 0, 1, creators, annihilators)
    kinetic = -1j * (forward - forward.conj().T)

    axial_matrices = [gamma_5, *(matrix @ gamma_5 for matrix in alpha)]
    identity_4 = np.eye(SPINOR_DIMENSION, dtype=complex)
    contact = np.zeros_like(kinetic)
    for cell in range(CELL_COUNT):
        number = bilinear(identity_4, cell, creators, annihilators)
        currents = [
            bilinear(matrix, cell, creators, annihilators)
            for matrix in axial_matrices
        ]
        normal_squares = [current @ current - number for current in currents]
        contact += normal_squares[0] - sum(normal_squares[1:])

    return kinetic, contact


def build_one_body_perturbations() -> tuple[np.ndarray, np.ndarray]:
    """Return a cell detuning and a uniform Dirac mass operator."""

    gamma, _, _ = dirac_matrices()
    sigma_z = np.diag([1.0, -1.0]).astype(complex)
    detuning = quadratic_operator(np.kron(sigma_z, np.eye(SPINOR_DIMENSION)))
    mass = quadratic_operator(np.kron(np.eye(CELL_COUNT), gamma[0]))
    return detuning, mass


def occupation_index(modes: tuple[int, ...]) -> int:
    result = 0
    for mode in modes:
        result |= 1 << (MODE_COUNT - 1 - mode)
    return result


def fock_lift(single_particle_unitary: np.ndarray) -> np.ndarray:
    """Return the number-preserving second quantization Gamma(V)."""

    result = np.zeros((FOCK_DIMENSION, FOCK_DIMENSION), dtype=complex)
    result[0, 0] = 1
    all_modes = range(MODE_COUNT)
    for particle_count in range(1, MODE_COUNT + 1):
        subsets = list(itertools.combinations(all_modes, particle_count))
        for source_modes in subsets:
            source = occupation_index(source_modes)
            for target_modes in subsets:
                target = occupation_index(target_modes)
                minor = single_particle_unitary[np.ix_(target_modes, source_modes)]
                result[target, source] = np.linalg.det(minor)
    return result


def operator_convention_errors(
    kinetic: np.ndarray,
    contact: np.ndarray,
) -> dict[str, float]:
    """Audit the CAR, gamma, Fock-lift, and local-projection conventions."""

    identity_fock = np.eye(FOCK_DIMENSION, dtype=complex)
    annihilators = [annihilation_operator(mode) for mode in range(MODE_COUNT)]
    creators = [operator.conj().T for operator in annihilators]

    car_error = 0.0
    for left in range(MODE_COUNT):
        for right in range(MODE_COUNT):
            annihilator_anticommutator = (
                annihilators[left] @ annihilators[right]
                + annihilators[right] @ annihilators[left]
            )
            mixed_anticommutator = (
                annihilators[left] @ creators[right]
                + creators[right] @ annihilators[left]
            )
            if left == right:
                mixed_anticommutator -= identity_fock
            car_error = max(
                car_error,
                float(np.max(np.abs(annihilator_anticommutator))),
                float(np.max(np.abs(mixed_anticommutator))),
            )

    gamma, gamma_5, alpha = dirac_matrices()
    identity_4 = np.eye(SPINOR_DIMENSION, dtype=complex)
    signature = (1.0, -1.0, -1.0, -1.0)
    clifford_error = 0.0
    for left in range(4):
        for right in range(4):
            anticommutator = gamma[left] @ gamma[right] + gamma[right] @ gamma[left]
            if left == right:
                anticommutator -= 2.0 * signature[left] * identity_4
            clifford_error = max(
                clifford_error, float(np.max(np.abs(anticommutator)))
            )

    axial_matrices = [gamma_5, *(matrix @ gamma_5 for matrix in alpha)]
    axial_error = max(
        max(float(np.max(np.abs(matrix - matrix.conj().T))) for matrix in axial_matrices),
        max(float(np.max(np.abs(matrix @ matrix - identity_4))) for matrix in axial_matrices),
    )

    orientation = np.array([2.0, -3.0, 5.0])
    orientation /= np.linalg.norm(orientation)
    cell_unitary = cell_unitary_from_orientation(orientation)
    single_particle = np.kron(cell_unitary, identity_4)
    lift = fock_lift(single_particle)
    lift_error = float(np.max(np.abs(lift.conj().T @ lift - identity_fock)))
    for source_mode in range(MODE_COUNT):
        transformed_creator = lift @ creators[source_mode] @ lift.conj().T
        expected_creator = sum(
            single_particle[target_mode, source_mode] * creators[target_mode]
            for target_mode in range(MODE_COUNT)
        )
        lift_error = max(
            lift_error,
            float(np.max(np.abs(transformed_creator - expected_creator))),
        )

    pauli = (
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    )
    first_column = cell_unitary[:, 0]
    recovered_orientation = np.array(
        [np.vdot(first_column, matrix @ first_column).real for matrix in pauli]
    )
    orientation_error = float(np.max(np.abs(recovered_orientation - orientation)))

    transformed = lift.conj().T @ (kinetic + contact / 3.0) @ lift
    projected = local_projection(transformed)
    projection_error = float(
        np.max(np.abs(local_projection(projected) - projected))
    )
    random = np.random.default_rng(20260717)
    first_local = random.normal(size=(FACTOR_DIMENSION, FACTOR_DIMENSION))
    first_local = first_local + first_local.T
    second_local = random.normal(size=(FACTOR_DIMENSION, FACTOR_DIMENSION))
    second_local = second_local + second_local.T
    local_test = np.kron(first_local, np.eye(FACTOR_DIMENSION)) + np.kron(
        np.eye(FACTOR_DIMENSION), second_local
    )
    residual = transformed - projected
    orthogonality_error = float(abs(np.vdot(residual, local_test)))

    factor_parity = np.diag(
        [(-1.0) ** basis_index.bit_count() for basis_index in range(FACTOR_DIMENSION)]
    )
    first_reduction = partial_trace_second(transformed)
    second_reduction = partial_trace_first(transformed)
    parity_error = max(
        float(np.max(np.abs(first_reduction @ factor_parity - factor_parity @ first_reduction))),
        float(np.max(np.abs(second_reduction @ factor_parity - factor_parity @ second_reduction))),
    )

    return {
        "CAR": car_error,
        "Clifford": clifford_error,
        "axial Hermiticity/square": axial_error,
        "Fock lift covariance": lift_error,
        "Bloch orientation": orientation_error,
        "local projection idempotence": projection_error,
        "local projection orthogonality": orthogonality_error,
        "local parity": parity_error,
    }


def cell_unitary_from_orientation(orientation: np.ndarray) -> np.ndarray:
    """Return W whose first column has Bloch vector orientation."""

    x, y, z = np.asarray(orientation, dtype=float)
    norm = np.linalg.norm([x, y, z])
    if norm == 0:
        raise ValueError("orientation must be nonzero")
    x, y, z = np.array([x, y, z]) / norm
    theta = np.arccos(np.clip(z, -1.0, 1.0))
    phi = np.arctan2(y, x)
    first = np.array(
        [np.cos(theta / 2), np.exp(1j * phi) * np.sin(theta / 2)],
        dtype=complex,
    )
    second = np.array(
        [-np.exp(-1j * phi) * np.sin(theta / 2), np.cos(theta / 2)],
        dtype=complex,
    )
    return np.column_stack([first, second])


def lifted_cell_unitary(orientation: np.ndarray) -> np.ndarray:
    cell_unitary = cell_unitary_from_orientation(orientation)
    single_particle = np.kron(cell_unitary, np.eye(SPINOR_DIMENSION))
    return fock_lift(single_particle)


def partial_trace_second(matrix: np.ndarray) -> np.ndarray:
    tensor = matrix.reshape(
        FACTOR_DIMENSION,
        FACTOR_DIMENSION,
        FACTOR_DIMENSION,
        FACTOR_DIMENSION,
    )
    return np.trace(tensor, axis1=1, axis2=3)


def partial_trace_first(matrix: np.ndarray) -> np.ndarray:
    tensor = matrix.reshape(
        FACTOR_DIMENSION,
        FACTOR_DIMENSION,
        FACTOR_DIMENSION,
        FACTOR_DIMENSION,
    )
    return np.trace(tensor, axis1=0, axis2=2)


def local_projection(matrix: np.ndarray) -> np.ndarray:
    identity = np.eye(FACTOR_DIMENSION, dtype=complex)
    scalar = np.trace(matrix) / FOCK_DIMENSION
    return (
        np.kron(partial_trace_second(matrix) / FACTOR_DIMENSION, identity)
        + np.kron(identity, partial_trace_first(matrix) / FACTOR_DIMENSION)
        - scalar * np.eye(FOCK_DIMENSION, dtype=complex)
    )


def squared_norm(matrix: np.ndarray) -> float:
    return float(np.vdot(matrix, matrix).real)


def centered_squared_norm(matrix: np.ndarray) -> float:
    """Return the squared norm after removing the scalar component."""

    dimension = matrix.shape[0]
    centered = matrix - np.trace(matrix) / dimension * np.eye(dimension)
    return squared_norm(centered)


def interaction_norm(matrix: np.ndarray) -> float:
    return squared_norm(matrix - local_projection(matrix))


def pure_state_entropy_bits(state: np.ndarray) -> float:
    coefficients = state.reshape(FACTOR_DIMENSION, FACTOR_DIMENSION)
    reduced = coefficients @ coefficients.conj().T
    eigenvalues = np.linalg.eigvalsh(reduced)
    eigenvalues = eigenvalues[eigenvalues > 1e-14]
    return float(-np.sum(eigenvalues * np.log2(eigenvalues)))


def maximal_contrast_state() -> tuple[np.ndarray, np.ndarray]:
    """Return a state filling the four +y modes and its factorizing unitary."""

    momentum_unitary = lifted_cell_unitary(np.array([0.0, 1.0, 0.0]))
    reference = np.zeros(FOCK_DIMENSION, dtype=complex)
    reference[(FACTOR_DIMENSION - 1) * FACTOR_DIMENSION] = 1
    return momentum_unitary @ reference, momentum_unitary


def isolated_ground_state_diagnostic(
    kinetic: np.ndarray,
    contact: np.ndarray,
) -> dict[str, float]:
    """Numerically inspect the ground state at the equal-cost coupling."""

    hamiltonian = kinetic + contact / 3.0
    eigenvalues, eigenvectors = np.linalg.eigh(hamiltonian)
    state = eigenvectors[:, 0]
    momentum_unitary = lifted_cell_unitary(np.array([0.0, 1.0, 0.0]))
    residual = np.linalg.norm(hamiltonian @ state - eigenvalues[0] * state)
    site_entropy = pure_state_entropy_bits(state)
    momentum_entropy = pure_state_entropy_bits(momentum_unitary.conj().T @ state)
    number_values = np.array(
        [basis_index.bit_count() for basis_index in range(FOCK_DIMENSION)],
        dtype=float,
    )
    probabilities = np.abs(state) ** 2
    number_mean = float(probabilities @ number_values)
    number_variance = float(
        probabilities @ (number_values**2) - number_mean**2
    )
    if abs(number_variance) < 1e-12:
        number_variance = 0.0
    return {
        "energy": float(eigenvalues[0]),
        "gap": float(eigenvalues[1] - eigenvalues[0]),
        "residual": float(residual),
        "site_entropy": site_entropy,
        "momentum_entropy": momentum_entropy,
        "entropy_contrast": site_entropy - momentum_entropy,
        "particle_number": number_mean,
        "particle_number_variance": number_variance,
    }


def scan_bistability_window(
    kinetic: np.ndarray,
    contact: np.ndarray,
    sample_count: int,
) -> dict[str, float]:
    """Numerically sample stationary-state data between the two spinodals."""

    if sample_count < 2:
        raise ValueError("sample_count must be at least two")
    lower = 1.0 / np.sqrt(12.0) + 1e-6
    upper = 1.0 / np.sqrt(6.0) - 1e-6
    momentum_unitary = lifted_cell_unitary(np.array([0.0, 1.0, 0.0]))
    smallest_gap = (float("inf"), 0.0)
    smallest_contrast = (float("inf"), 0.0)
    for coupling in np.linspace(lower, upper, sample_count):
        eigenvalues, eigenvectors = np.linalg.eigh(kinetic + coupling * contact)
        state = eigenvectors[:, 0]
        gap = float(eigenvalues[1] - eigenvalues[0])
        contrast = pure_state_entropy_bits(state) - pure_state_entropy_bits(
            momentum_unitary.conj().T @ state
        )
        if gap < smallest_gap[0]:
            smallest_gap = (gap, float(coupling))
        if contrast < smallest_contrast[0]:
            smallest_contrast = (contrast, float(coupling))
    return {
        "samples": float(sample_count),
        "smallest_gap": smallest_gap[0],
        "smallest_gap_coupling": smallest_gap[1],
        "smallest_entropy_contrast": smallest_contrast[0],
        "smallest_entropy_contrast_coupling": smallest_contrast[1],
    }


def numerical_components(
    kinetic: np.ndarray,
    contact: np.ndarray,
    orientation: np.ndarray,
) -> tuple[float, float, float]:
    unitary = lifted_cell_unitary(orientation)
    transformed_kinetic = unitary.conj().T @ kinetic @ unitary
    transformed_contact = unitary.conj().T @ contact @ unitary
    residual_kinetic = transformed_kinetic - local_projection(transformed_kinetic)
    residual_contact = transformed_contact - local_projection(transformed_contact)
    return (
        squared_norm(residual_kinetic),
        squared_norm(residual_contact),
        float(np.vdot(residual_kinetic, residual_contact).real),
    )


def predicted_components(orientation: np.ndarray) -> tuple[float, float, float]:
    x, y, z = np.asarray(orientation, dtype=float)
    x, y, z = np.array([x, y, z]) / np.linalg.norm([x, y, z])
    contact = 1536.0 * (1.0 - z * z) * (3.0 + z * z)
    return 512.0 * (1.0 - y * y), contact, 0.0


def run_checks(seed: int, samples: int, bistability_samples: int) -> None:
    kinetic, contact = build_hamiltonians()
    detuning, mass = build_one_body_perturbations()
    print("operator checks")
    print("  hermitian kinetic", np.allclose(kinetic, kinetic.conj().T))
    print("  hermitian contact", np.allclose(contact, contact.conj().T))
    print("  ||H_K||^2", squared_norm(kinetic))
    print("  Tr(H_4)/dim", np.trace(contact) / FOCK_DIMENSION)
    print("  ||H_4 - Tr(H_4)/dim I||^2", centered_squared_norm(contact))
    print("  <H_K,H_4>", np.vdot(kinetic, contact))
    print("  ||H_delta||^2", squared_norm(detuning))
    print("  ||H_mass||^2", squared_norm(mass))
    if abs(np.trace(contact) / FOCK_DIMENSION - 4.0) > 1e-12:
        raise AssertionError("unexpected scalar contact component")
    if abs(centered_squared_norm(contact) - 8192.0) > 1e-8:
        raise AssertionError("centered contact norm changed")
    convention_errors = operator_convention_errors(kinetic, contact)
    for name, error in convention_errors.items():
        print(f"  {name} error", error)
    if max(convention_errors.values()) > 1e-8:
        raise AssertionError("an operator convention audit failed")

    orientations = [
        np.array([0.0, 0.0, 1.0]),
        np.array([0.0, 1.0, 0.0]),
        np.array([1.0, 0.0, 0.0]),
        np.array([0.0, 1.0, 1.0]),
    ]
    random = np.random.default_rng(seed)
    orientations.extend(random.normal(size=3) for _ in range(samples))

    largest_error = 0.0
    print("\norientation checks: numerical versus closed form")
    for orientation in orientations:
        orientation = orientation / np.linalg.norm(orientation)
        numerical = np.array(numerical_components(kinetic, contact, orientation))
        predicted = np.array(predicted_components(orientation))
        error = float(np.max(np.abs(numerical - predicted)))
        largest_error = max(largest_error, error)
        print(
            "  n=",
            np.round(orientation, 6),
            " numerical=",
            np.round(numerical, 9),
            " predicted=",
            np.round(predicted, 9),
        )
    print("  largest absolute error", largest_error)
    if largest_error > 1e-8:
        raise AssertionError("closed-form component formula failed")

    print("\nrestricted selector")
    print("  C(n;g) = [512(1-n_y^2)")
    print("              + 1536 g^2(1-n_z^2)(3+n_z^2)]")
    print("           / [512 + 8192 g^2]")
    print("  critical coupling |g_c| = 1/3")
    print("  |g| < 1/3: n = +/- y (phase-momentum factorization)")
    print("  |g| > 1/3: n = +/- z (site factorization)")
    print("  |g| = 1/3: the two endpoint minima are degenerate")
    print("  momentum minimum is locally stable for |g| < 1/sqrt(6)")
    print("  site minimum is locally stable for |g| > 1/sqrt(12)")
    print("  bistability window: 1/sqrt(12) < |g| < 1/sqrt(6)")
    print("  at |g|=1/3: C_min=9/25, C_barrier=39/100, delta=3/100")
    critical_squared = 1.0 / 9.0
    denominator = 512.0 + 8192.0 * critical_squared
    minimum_cost = 512.0 / denominator
    barrier_cost = (256.0 + critical_squared * 2688.0) / denominator
    if abs(minimum_cost - 9.0 / 25.0) > 1e-12:
        raise AssertionError("unexpected full-Fock critical minimum cost")
    if abs(barrier_cost - 39.0 / 100.0) > 1e-12:
        raise AssertionError("unexpected full-Fock critical barrier cost")
    if abs(barrier_cost - minimum_cost - 3.0 / 100.0) > 1e-12:
        raise AssertionError("unexpected full-Fock critical barrier height")

    state, momentum_unitary = maximal_contrast_state()
    site_entropy = pure_state_entropy_bits(state)
    momentum_entropy = pure_state_entropy_bits(momentum_unitary.conj().T @ state)
    print("\nfixed-state diagnostic")
    print("  site-factor entropy (bits)", site_entropy)
    print("  momentum-factor entropy (bits)", momentum_entropy)
    print("  entropy contrast (bits)", site_entropy - momentum_entropy)
    print("  <H(g)> = 4g and Var[H(g)] = 48g^2 for this state")
    for coupling in (0.0, 0.25, 1.0 / 3.0, 0.5):
        hamiltonian = kinetic + coupling * contact
        expectation = np.vdot(state, hamiltonian @ state)
        variance = np.vdot(state, hamiltonian @ hamiltonian @ state)
        variance -= expectation * expectation
        print(
            f"  g={coupling:.6f}: <H>={expectation.real:.12g}, "
            f"Var[H]={variance.real:.12g}"
        )
    print("  consequence: the contrast state is not stationary for g != 0")

    ground_state = isolated_ground_state_diagnostic(kinetic, contact)
    print("\nstationary-state diagnostic at g=1/3 (numerical)")
    for key, value in ground_state.items():
        print(f"  {key}: {value:.15g}")
    if ground_state["gap"] < 0.6 or ground_state["residual"] > 1e-10:
        raise AssertionError("critical ground-state isolation check failed")
    if ground_state["entropy_contrast"] < 1.8:
        raise AssertionError("critical ground-state entropy contrast was lost")

    if bistability_samples:
        scan = scan_bistability_window(kinetic, contact, bistability_samples)
        print("\nbistability-window ground-state scan (numerical)")
        for key, value in scan.items():
            print(f"  {key}: {value:.15g}")
        if scan["smallest_gap"] < 0.49:
            raise AssertionError("ground-state gap became unexpectedly small")
        if scan["smallest_entropy_contrast"] < 1.32:
            raise AssertionError("ground-state entropy contrast became too small")

    print("\ncontrolled one-body perturbations")
    perturbation_error = 0.0
    for orientation in orientations:
        orientation = orientation / np.linalg.norm(orientation)
        unitary = lifted_cell_unitary(orientation)
        transformed_detuning = unitary.conj().T @ detuning @ unitary
        transformed_mass = unitary.conj().T @ mass @ unitary
        predicted_detuning = 512.0 * (1.0 - orientation[2] ** 2)
        perturbation_error = max(
            perturbation_error,
            abs(interaction_norm(transformed_detuning) - predicted_detuning),
            interaction_norm(transformed_mass),
        )
    print("  max formula error", perturbation_error)
    print("  uniform mass has zero interaction cost for every n")
    print("  detuning contribution = 512 delta^2 (1-n_z^2)")
    print("  with kinetic scale t, transition survives for |delta| < |t|")
    print("  g_c^2 = (t^2-delta^2)/9")
    print("  bistability: (t^2-delta^2)/12 < g^2 < (t^2-delta^2)/6")
    if perturbation_error > 1e-8:
        raise AssertionError("one-body perturbation formula failed")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=20260717)
    parser.add_argument("--samples", type=int, default=4)
    parser.add_argument("--bistability-samples", type=int, default=41)
    arguments = parser.parse_args()
    run_checks(arguments.seed, arguments.samples, arguments.bistability_samples)


if __name__ == "__main__":
    main()
