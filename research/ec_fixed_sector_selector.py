#!/usr/bin/env python3
"""Fixed-N gate for the finite Einstein-Cartan-inspired CAR selector.

This script replaces the full-Fock Hilbert-Schmidt inner product by the trace
on the four-particle sector.  The local Hamiltonian subspace is fixed before
the candidate orientation is chosen: it is the restriction of number-
preserving one-factor operators A_+ tensor I + I tensor A_-.
"""

from __future__ import annotations

import argparse
import math

import numpy as np

import ec_axial_selector_analysis as model


PARTICLE_NUMBER = 4
SECTOR_INDICES = tuple(
    index
    for index in range(model.FOCK_DIMENSION)
    if index.bit_count() == PARTICLE_NUMBER
)
SECTOR_DIMENSION = len(SECTOR_INDICES)
SECTOR_POSITION = {index: position for position, index in enumerate(SECTOR_INDICES)}
LOCAL_INDICES = {
    particle_number: tuple(
        index
        for index in range(model.FACTOR_DIMENSION)
        if index.bit_count() == particle_number
    )
    for particle_number in range(model.SPINOR_DIMENSION + 1)
}


def sector_block_positions(local_particle_number: int) -> tuple[int, ...]:
    """Return sector coordinates in tensor-product order for one charge block."""

    first_indices = LOCAL_INDICES[local_particle_number]
    second_indices = LOCAL_INDICES[PARTICLE_NUMBER - local_particle_number]
    return tuple(
        SECTOR_POSITION[first * model.FACTOR_DIMENSION + second]
        for first in first_indices
        for second in second_indices
    )


BLOCK_POSITIONS = {
    particle_number: sector_block_positions(particle_number)
    for particle_number in range(PARTICLE_NUMBER + 1)
}


def restrict_to_sector(matrix: np.ndarray) -> np.ndarray:
    return matrix[np.ix_(SECTOR_INDICES, SECTOR_INDICES)]


def rectangular_local_projection(
    matrix: np.ndarray,
    first_dimension: int,
    second_dimension: int,
) -> np.ndarray:
    """Project onto A tensor I + I tensor B for rectangular factors."""

    tensor = matrix.reshape(
        first_dimension,
        second_dimension,
        first_dimension,
        second_dimension,
    )
    trace_second = np.trace(tensor, axis1=1, axis2=3)
    trace_first = np.trace(tensor, axis1=0, axis2=2)
    scalar = np.trace(matrix) / (first_dimension * second_dimension)
    return (
        np.kron(trace_second / second_dimension, np.eye(second_dimension))
        + np.kron(np.eye(first_dimension), trace_first / first_dimension)
        - scalar * np.eye(first_dimension * second_dimension)
    )


def fixed_sector_local_projection(matrix: np.ndarray) -> np.ndarray:
    """Project onto the fixed number-preserving local Hamiltonian subspace."""

    if matrix.shape != (SECTOR_DIMENSION, SECTOR_DIMENSION):
        raise ValueError("matrix must act on the four-particle sector")
    result = np.zeros_like(matrix)
    for first_particles, positions in BLOCK_POSITIONS.items():
        first_dimension = len(LOCAL_INDICES[first_particles])
        second_dimension = len(
            LOCAL_INDICES[PARTICLE_NUMBER - first_particles]
        )
        block = matrix[np.ix_(positions, positions)]
        result[np.ix_(positions, positions)] = rectangular_local_projection(
            block,
            first_dimension,
            second_dimension,
        )
    return result


def squared_norm(matrix: np.ndarray) -> float:
    return float(np.vdot(matrix, matrix).real)


def sector_components(
    kinetic: np.ndarray,
    contact: np.ndarray,
    orientation: np.ndarray,
) -> tuple[float, float, float]:
    """Return fixed-sector residual norms for K, Q, and their cross term."""

    unitary = model.lifted_cell_unitary(orientation)
    transformed_kinetic = restrict_to_sector(unitary.conj().T @ kinetic @ unitary)
    transformed_contact = restrict_to_sector(unitary.conj().T @ contact @ unitary)
    residual_kinetic = transformed_kinetic - fixed_sector_local_projection(
        transformed_kinetic
    )
    residual_contact = transformed_contact - fixed_sector_local_projection(
        transformed_contact
    )
    return (
        squared_norm(residual_kinetic),
        squared_norm(residual_contact),
        float(np.vdot(residual_kinetic, residual_contact).real),
    )


def sector_selector(
    components: tuple[float, float, float],
    coupling: float,
    denominator: float,
) -> float:
    kinetic, contact, cross = components
    return (kinetic + coupling * coupling * contact + 2 * coupling * cross) / denominator


def predicted_sector_components(
    orientation: np.ndarray,
) -> tuple[float, float, float]:
    """Closed fixed-sector CAR traces for K, Q, and their residual cross term."""

    x, y, z = np.asarray(orientation, dtype=float)
    x, y, z = np.array([x, y, z]) / np.linalg.norm([x, y, z])
    return (
        160.0 * (1.0 - y * y),
        24.0 * (1.0 - z * z) * (71.0 + 25.0 * z * z),
        0.0,
    )


def projection_audit() -> dict[str, float]:
    random = np.random.default_rng(20260717)
    matrix = random.normal(size=(SECTOR_DIMENSION, SECTOR_DIMENSION))
    matrix = matrix + matrix.T
    projected = fixed_sector_local_projection(matrix)
    residual = matrix - projected

    local_test = np.zeros_like(matrix)
    for first_particles, positions in BLOCK_POSITIONS.items():
        first_dimension = len(LOCAL_INDICES[first_particles])
        second_dimension = len(
            LOCAL_INDICES[PARTICLE_NUMBER - first_particles]
        )
        first = random.normal(size=(first_dimension, first_dimension))
        second = random.normal(size=(second_dimension, second_dimension))
        block = np.kron(first + first.T, np.eye(second_dimension))
        block += np.kron(np.eye(first_dimension), second + second.T)
        local_test[np.ix_(positions, positions)] = block

    return {
        "idempotence": float(
            np.max(np.abs(fixed_sector_local_projection(projected) - projected))
        ),
        "orthogonality": float(abs(np.vdot(residual, local_test))),
    }


def stationary_state_diagnostic(
    kinetic: np.ndarray,
    contact: np.ndarray,
    coupling: float,
) -> dict[str, float]:
    """Inspect the full-Fock ground state at a sector-selector coupling."""

    hamiltonian = kinetic + coupling * contact
    eigenvalues, eigenvectors = np.linalg.eigh(hamiltonian)
    state = eigenvectors[:, 0]
    momentum_unitary = model.lifted_cell_unitary(np.array([0.0, 1.0, 0.0]))
    number_values = np.array(
        [index.bit_count() for index in range(model.FOCK_DIMENSION)], dtype=float
    )
    probabilities = np.abs(state) ** 2
    number_mean = float(probabilities @ number_values)
    number_variance = float(
        probabilities @ (number_values**2) - number_mean * number_mean
    )
    return {
        "energy": float(eigenvalues[0]),
        "gap": float(eigenvalues[1] - eigenvalues[0]),
        "residual": float(
            np.linalg.norm(hamiltonian @ state - eigenvalues[0] * state)
        ),
        "particle_number": number_mean,
        "particle_number_variance": max(0.0, number_variance),
        "site_entropy": model.pure_state_entropy_bits(state),
        "momentum_entropy": model.pure_state_entropy_bits(
            momentum_unitary.conj().T @ state
        ),
    }


def scan_bistability_ground_states(
    kinetic: np.ndarray,
    contact: np.ndarray,
    sample_count: int,
) -> dict[str, float]:
    """Sample the stationary gap and entropy contrast between the spinodals."""

    if sample_count < 2:
        raise ValueError("sample_count must be at least two")
    lower = math.sqrt(5.0 / 72.0) + 1e-6
    upper = math.sqrt(10.0 / 69.0) - 1e-6
    smallest_gap = (float("inf"), 0.0)
    smallest_contrast = (float("inf"), 0.0)
    largest_number_error = 0.0
    for coupling in np.linspace(lower, upper, sample_count):
        diagnostic = stationary_state_diagnostic(kinetic, contact, float(coupling))
        contrast = diagnostic["site_entropy"] - diagnostic["momentum_entropy"]
        if diagnostic["gap"] < smallest_gap[0]:
            smallest_gap = (diagnostic["gap"], float(coupling))
        if contrast < smallest_contrast[0]:
            smallest_contrast = (contrast, float(coupling))
        largest_number_error = max(
            largest_number_error,
            abs(diagnostic["particle_number"] - PARTICLE_NUMBER),
            diagnostic["particle_number_variance"],
        )
    return {
        "samples": float(sample_count),
        "smallest_gap": smallest_gap[0],
        "smallest_gap_coupling": smallest_gap[1],
        "smallest_entropy_contrast": smallest_contrast[0],
        "smallest_entropy_contrast_coupling": smallest_contrast[1],
        "largest_particle_number_error": largest_number_error,
    }


def run(samples: int, bistability_samples: int) -> None:
    kinetic, contact = model.build_hamiltonians()
    sector_kinetic = restrict_to_sector(kinetic)
    sector_contact = restrict_to_sector(contact)
    identity = np.eye(SECTOR_DIMENSION)
    kinetic_mean = np.trace(sector_kinetic) / SECTOR_DIMENSION
    contact_mean = np.trace(sector_contact) / SECTOR_DIMENSION
    centered_kinetic = sector_kinetic - kinetic_mean * identity
    centered_contact = sector_contact - contact_mean * identity
    kinetic_norm = squared_norm(centered_kinetic)
    contact_norm = squared_norm(centered_contact)
    total_cross = float(np.vdot(centered_kinetic, centered_contact).real)

    print("fixed-N selector gate")
    print("  particle number", PARTICLE_NUMBER)
    print("  sector dimension", SECTOR_DIMENSION)
    print(
        "  charge-block dimensions",
        [len(BLOCK_POSITIONS[number]) for number in range(PARTICLE_NUMBER + 1)],
    )
    print(
        "  local-subspace dimension",
        sum(
            len(LOCAL_INDICES[number]) ** 2
            + len(LOCAL_INDICES[PARTICLE_NUMBER - number]) ** 2
            - 1
            for number in range(PARTICLE_NUMBER + 1)
        ),
    )
    for name, error in projection_audit().items():
        print(f"  projection {name} error", error)
        if error > 1e-8:
            raise AssertionError("fixed-sector projection audit failed")
    print("  Tr(K_N)/dim", kinetic_mean)
    print("  Tr(Q_N)/dim", contact_mean)
    print("  ||K_N - Tr(K_N)/dim I||^2", kinetic_norm)
    print("  ||Q_N - Tr(Q_N)/dim I||^2", contact_norm)
    print("  <K_N-centered,Q_N-centered>", total_cross)
    if abs(kinetic_mean) > 1e-12 or abs(contact_mean - 24.0 / 7.0) > 1e-12:
        raise AssertionError("unexpected fixed-sector scalar component")
    if abs(kinetic_norm - 160.0) > 1e-10:
        raise AssertionError("centered fixed-sector kinetic norm changed")
    if abs(contact_norm - 15744.0 / 7.0) > 1e-10:
        raise AssertionError("centered fixed-sector contact norm changed")

    orientations: list[tuple[str, np.ndarray]] = [
        ("site z", np.array([0.0, 0.0, 1.0])),
        ("momentum y", np.array([0.0, 1.0, 0.0])),
        ("x", np.array([1.0, 0.0, 0.0])),
        ("yz midpoint", np.array([0.0, 1.0, 1.0])),
    ]

    random = np.random.default_rng(20260717)
    for _ in range(samples):
        orientation = random.normal(size=3)
        orientation /= np.linalg.norm(orientation)
        orientations.append(("random", orientation))

    largest_formula_error = 0.0
    print("\nsector residual components: numerical versus closed form")
    for name, orientation in orientations:
        numerical = np.array(sector_components(kinetic, contact, orientation))
        predicted = np.array(predicted_sector_components(orientation))
        largest_formula_error = max(
            largest_formula_error, float(np.max(np.abs(numerical - predicted)))
        )
        print(
            f"  {name}: n={np.round(orientation / np.linalg.norm(orientation), 6)}, "
            f"numerical={np.round(numerical, 9)}, "
            f"predicted={np.round(predicted, 9)}"
        )
    print("  largest absolute formula error", largest_formula_error)
    if largest_formula_error > 1e-8:
        raise AssertionError("fixed-sector component formula failed")

    critical_squared = 20.0 / 213.0
    critical = math.sqrt(critical_squared)
    lower_spinodal = math.sqrt(5.0 / 72.0)
    upper_spinodal = math.sqrt(10.0 / 69.0)
    denominator = kinetic_norm + critical_squared * contact_norm
    site_components = predicted_sector_components(np.array([0.0, 0.0, 1.0]))
    midpoint_components = predicted_sector_components(np.array([0.0, 1.0, 1.0]))
    minimum_cost = sector_selector(site_components, critical, denominator)
    barrier_cost = sector_selector(midpoint_components, critical, denominator)

    print("\nclosed fixed-sector selector")
    print("  numerator = 160(1-n_y^2)")
    print("              + 24 g^2(1-n_z^2)(71+25 n_z^2)")
    print("  denominator = 160 + (15744/7) g^2")
    print("  critical coupling |g_c| = sqrt(20/213) =", critical)
    print("  |g| < |g_c|: n = +/- y (phase-momentum factorization)")
    print("  |g| > |g_c|: n = +/- z (site factorization)")
    print("  momentum minimum stable for |g| < sqrt(10/69) =", upper_spinodal)
    print("  site minimum stable for |g| > sqrt(5/72) =", lower_spinodal)
    print("  critical minimum cost = 497/1153 =", minimum_cost)
    print("  critical barrier cost = 2163/4612 =", barrier_cost)
    print("  critical barrier height = 175/4612 =", barrier_cost - minimum_cost)

    expected_minimum = 497.0 / 1153.0
    expected_barrier = 2163.0 / 4612.0
    if abs(minimum_cost - expected_minimum) > 1e-12:
        raise AssertionError("unexpected critical minimum cost")
    if abs(barrier_cost - expected_barrier) > 1e-12:
        raise AssertionError("unexpected critical barrier cost")
    if not (lower_spinodal < critical < upper_spinodal):
        raise AssertionError("critical point left the bistability interval")

    diagnostic = stationary_state_diagnostic(kinetic, contact, critical)
    entropy_contrast = diagnostic["site_entropy"] - diagnostic["momentum_entropy"]
    print("\nstationary state at the fixed-sector transition (numerical)")
    for name, value in diagnostic.items():
        print(f"  {name}: {value:.15g}")
    print(f"  entropy_contrast: {entropy_contrast:.15g}")
    if diagnostic["gap"] <= 0.0 or diagnostic["residual"] > 1e-10:
        raise AssertionError("stationary state is not numerically isolated")
    if abs(diagnostic["particle_number"] - PARTICLE_NUMBER) > 1e-10:
        raise AssertionError("stationary state left the tested charge sector")
    if diagnostic["particle_number_variance"] > 1e-10:
        raise AssertionError("stationary state has nonzero number variance")
    if entropy_contrast <= 0.0:
        raise AssertionError("stationary entropy contrast was lost")

    if bistability_samples:
        scan = scan_bistability_ground_states(
            kinetic, contact, bistability_samples
        )
        print("\nbistability-window stationary-state scan (numerical)")
        for name, value in scan.items():
            print(f"  {name}: {value:.15g}")
        if scan["smallest_gap"] <= 0.0:
            raise AssertionError("a sampled stationary gap closed")
        if scan["smallest_entropy_contrast"] <= 0.0:
            raise AssertionError("sampled stationary entropy contrast was lost")
        if scan["largest_particle_number_error"] > 1e-10:
            raise AssertionError("a sampled ground state left the four-particle sector")

    print("\nGATE VERDICT: PASS")
    print("  The two-branch selector, bistability, and stationary entropy contrast")
    print("  survive the fixed-N=4 Hilbert-Schmidt weighting.")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=int, default=4)
    parser.add_argument("--bistability-samples", type=int, default=121)
    arguments = parser.parse_args()
    run(arguments.samples, arguments.bistability_samples)


if __name__ == "__main__":
    main()
