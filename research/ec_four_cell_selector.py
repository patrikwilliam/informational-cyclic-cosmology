#!/usr/bin/env python3
"""Four-cell finite gate for the restricted EC-inspired CAR selector.

The half-filled four-cell sector has dimension 12,870, so this implementation
never constructs a dense fixed-sector Hamiltonian.  It carries the one- and
two-body coefficient matrices and evaluates the exact fixed-number overlaps
with one-cell matrix units by combinatorial partial traces.

This remains a finite feasibility test of one candidate selector.  It is not a
continuum, dynamical, or cosmological calculation.
"""

from __future__ import annotations

import argparse
import itertools
import math
import time
from dataclasses import dataclass

import numpy as np

import ec_three_cell_selector as dense


SPINOR_DIMENSION = dense.SPINOR_DIMENSION
TOLERANCE = 1e-9
STATIONARITY_TOLERANCE = 1e-7


def pair_basis(mode_count: int) -> tuple[tuple[int, int], ...]:
    return tuple(itertools.combinations(range(mode_count), 2))


def exterior_square(unitary: np.ndarray) -> np.ndarray:
    """Return the two-particle exterior-power representation of `unitary`."""

    pairs = pair_basis(unitary.shape[0])
    first = np.asarray([pair[0] for pair in pairs], dtype=int)
    second = np.asarray([pair[1] for pair in pairs], dtype=int)
    return (
        unitary[np.ix_(first, first)] * unitary[np.ix_(second, second)]
        - unitary[np.ix_(first, second)] * unitary[np.ix_(second, first)]
    )


@dataclass(frozen=True)
class LowBodyOperator:
    one_body: np.ndarray
    two_body: np.ndarray

    @property
    def mode_count(self) -> int:
        return self.one_body.shape[0]

    def transformed(self, cell_unitary: np.ndarray) -> "LowBodyOperator":
        mode_unitary = np.kron(
            cell_unitary, np.eye(SPINOR_DIMENSION, dtype=complex)
        )
        pair_unitary = exterior_square(mode_unitary)
        return LowBodyOperator(
            mode_unitary.conj().T @ self.one_body @ mode_unitary,
            pair_unitary.conj().T @ self.two_body @ pair_unitary,
        )

    def scaled_add(
        self, other: "LowBodyOperator", scale: float
    ) -> "LowBodyOperator":
        return LowBodyOperator(
            self.one_body + scale * other.one_body,
            self.two_body + scale * other.two_body,
        )


def low_body_operators(
    cell_count: int, periodic: bool
) -> tuple[LowBodyOperator, LowBodyOperator, np.ndarray]:
    one_geometry = dense.FixedSectorGeometry(cell_count, 1)
    two_geometry = dense.FixedSectorGeometry(cell_count, 2)
    kinetic_one, _, _, kinetic_basis = dense.build_hamiltonians(
        one_geometry, periodic
    )
    _, contact_two, _, _ = dense.build_hamiltonians(two_geometry, periodic)
    mode_count = SPINOR_DIMENSION * cell_count
    pair_count = math.comb(mode_count, 2)
    kinetic = LowBodyOperator(
        kinetic_one,
        np.zeros((pair_count, pair_count), dtype=complex),
    )
    contact = LowBodyOperator(
        np.zeros((mode_count, mode_count), dtype=complex),
        contact_two,
    )
    return kinetic, contact, kinetic_basis


def one_body_block(states: tuple[int, ...], matrix: np.ndarray) -> np.ndarray:
    position = {mask: index for index, mask in enumerate(states)}
    result = np.zeros((len(states), len(states)), dtype=complex)
    terms = np.argwhere(np.abs(matrix) > 1e-14)
    for column, source in enumerate(states):
        for row_mode, column_mode in terms:
            applied = dense.apply_number_conserving_monomial(
                source, (int(column_mode),), (int(row_mode),)
            )
            if applied is None:
                continue
            target, sign = applied
            result[position[target], column] += matrix[row_mode, column_mode] * sign
    return result


def two_body_block(states: tuple[int, ...], matrix: np.ndarray) -> np.ndarray:
    local_pairs = pair_basis(SPINOR_DIMENSION)
    position = {mask: index for index, mask in enumerate(states)}
    result = np.zeros((len(states), len(states)), dtype=complex)
    terms = np.argwhere(np.abs(matrix) > 1e-14)
    for column, source in enumerate(states):
        for target_pair_index, source_pair_index in terms:
            target_pair = local_pairs[int(target_pair_index)]
            source_pair = local_pairs[int(source_pair_index)]
            applied = dense.apply_number_conserving_monomial(
                source,
                source_pair,
                (target_pair[1], target_pair[0]),
            )
            if applied is None:
                continue
            target, sign = applied
            result[position[target], column] += (
                matrix[target_pair_index, source_pair_index] * sign
            )
    return result


def projection_overlaps(
    geometry: dense.FixedSectorGeometry, operator: LowBodyOperator
) -> np.ndarray:
    """Exact overlaps with fixed-sector one-cell matrix units.

    For a cell containing q particles, the complementary environment contains
    R=N-q particles.  An operator of body order at most two contributes through local,
    one-environment contraction, and two-environment trace terms.  Their
    spectator multiplicities are binomial coefficients.
    """

    mode_count = geometry.mode_count
    global_pairs = pair_basis(mode_count)
    pair_position = {pair: index for index, pair in enumerate(global_pairs)}
    overlaps: list[complex] = []

    for cell in range(geometry.cell_count):
        local_modes = tuple(
            cell * SPINOR_DIMENSION + flavor
            for flavor in range(SPINOR_DIMENSION)
        )
        environment_modes = tuple(
            mode for mode in range(mode_count) if mode not in local_modes
        )
        environment_dimension = len(environment_modes)

        h_local = operator.one_body[np.ix_(local_modes, local_modes)]
        h_environment_trace = np.trace(
            operator.one_body[np.ix_(environment_modes, environment_modes)]
        )

        local_pair_indices = tuple(
            pair_position[tuple(sorted((left, right)))]
            for left, right in itertools.combinations(local_modes, 2)
        )
        v_local = operator.two_body[
            np.ix_(local_pair_indices, local_pair_indices)
        ]
        environment_pair_indices = tuple(
            pair_position[pair]
            for pair in itertools.combinations(environment_modes, 2)
        )
        v_environment_trace = np.trace(
            operator.two_body[
                np.ix_(environment_pair_indices, environment_pair_indices)
            ]
        )

        mixed = np.zeros(
            (SPINOR_DIMENSION, SPINOR_DIMENSION), dtype=complex
        )
        for target_local, target_mode in enumerate(local_modes):
            for source_local, source_mode in enumerate(local_modes):
                mixed[target_local, source_local] = sum(
                    operator.two_body[
                        pair_position[tuple(sorted((target_mode, environment)))],
                        pair_position[tuple(sorted((source_mode, environment)))],
                    ]
                    for environment in environment_modes
                )

        for particles, states in geometry.local_states.items():
            environment_particles = geometry.particle_number - particles
            local_identity = np.eye(len(states), dtype=complex)
            local_one = one_body_block(states, h_local)
            mixed_one = one_body_block(states, mixed)
            local_two = two_body_block(states, v_local)
            block = (
                dense.binomial_or_zero(
                    environment_dimension, environment_particles
                )
                * (local_one + local_two)
                + dense.binomial_or_zero(
                    environment_dimension - 1, environment_particles - 1
                )
                * (h_environment_trace * local_identity + mixed_one)
                + dense.binomial_or_zero(
                    environment_dimension - 2, environment_particles - 2
                )
                * v_environment_trace
                * local_identity
            )
            state_position = {state: index for index, state in enumerate(states)}
            overlaps.extend(
                block[state_position[row], state_position[column]]
                for row in states
                for column in states
            )

    return np.asarray(overlaps, dtype=complex)


def sparse_terms(
    operator: LowBodyOperator,
) -> tuple[tuple[tuple[int, int, complex], ...], tuple[tuple[int, int, complex], ...]]:
    one_terms = tuple(
        (int(row), int(column), operator.one_body[row, column])
        for row, column in np.argwhere(np.abs(operator.one_body) > 1e-14)
    )
    two_terms = tuple(
        (int(row), int(column), operator.two_body[row, column])
        for row, column in np.argwhere(np.abs(operator.two_body) > 1e-14)
    )
    return one_terms, two_terms


def apply_low_body(
    mask: int,
    operator: LowBodyOperator,
    terms: tuple[
        tuple[tuple[int, int, complex], ...],
        tuple[tuple[int, int, complex], ...],
    ]
    | None = None,
) -> dict[int, complex]:
    one_terms, two_terms = sparse_terms(operator) if terms is None else terms
    pairs = pair_basis(operator.mode_count)
    result: dict[int, complex] = {}
    for row, column, coefficient in one_terms:
        applied = dense.apply_number_conserving_monomial(mask, (column,), (row,))
        if applied is None:
            continue
        target, sign = applied
        result[target] = result.get(target, 0.0j) + coefficient * sign
    for target_index, source_index, coefficient in two_terms:
        target_pair = pairs[target_index]
        source_pair = pairs[source_index]
        applied = dense.apply_number_conserving_monomial(
            mask, source_pair, (target_pair[1], target_pair[0])
        )
        if applied is None:
            continue
        target, sign = applied
        result[target] = result.get(target, 0.0j) + coefficient * sign
    return result


def fixed_sector_matrix(
    geometry: dense.FixedSectorGeometry, operator: LowBodyOperator
) -> np.ndarray:
    terms = sparse_terms(operator)
    result = np.zeros((geometry.dimension, geometry.dimension), dtype=complex)
    for column, mask in enumerate(geometry.masks):
        for target, coefficient in apply_low_body(mask, operator, terms).items():
            result[geometry.position[target], column] += coefficient
    return result


def sector_inner_product(
    geometry: dense.FixedSectorGeometry,
    left: LowBodyOperator,
    right: LowBodyOperator,
) -> complex:
    left_terms = sparse_terms(left)
    right_terms = sparse_terms(right)
    value = 0.0j
    for mask in geometry.masks:
        left_action = apply_low_body(mask, left, left_terms)
        right_action = apply_low_body(mask, right, right_terms)
        value += sum(
            coefficient.conjugate() * right_action.get(target, 0.0j)
            for target, coefficient in left_action.items()
        )
    return value


def sector_trace(
    geometry: dense.FixedSectorGeometry, operator: LowBodyOperator
) -> complex:
    return (
        dense.binomial_or_zero(
            geometry.mode_count - 1, geometry.particle_number - 1
        )
        * np.trace(operator.one_body)
        + dense.binomial_or_zero(
            geometry.mode_count - 2, geometry.particle_number - 2
        )
        * np.trace(operator.two_body)
    )


@dataclass(frozen=True)
class InvariantStatistics:
    kinetic_norm: float
    contact_norm: float
    cross: float
    kinetic_trace: complex
    contact_trace: complex

    def norm(self, coupling: float) -> float:
        return (
            self.kinetic_norm
            + 2.0 * coupling * self.cross
            + coupling**2 * self.contact_norm
        )

    def centered_norm(self, dimension: int, coupling: float) -> float:
        trace = self.kinetic_trace + coupling * self.contact_trace
        return self.norm(coupling) - abs(trace) ** 2 / dimension


def invariant_statistics(
    geometry: dense.FixedSectorGeometry,
    kinetic: LowBodyOperator,
    contact: LowBodyOperator,
) -> InvariantStatistics:
    return InvariantStatistics(
        float(sector_inner_product(geometry, kinetic, kinetic).real),
        float(sector_inner_product(geometry, contact, contact).real),
        float(sector_inner_product(geometry, kinetic, contact).real),
        sector_trace(geometry, kinetic),
        sector_trace(geometry, contact),
    )


def residual_components(
    geometry: dense.FixedSectorGeometry,
    statistics: InvariantStatistics,
    kinetic: LowBodyOperator,
    contact: LowBodyOperator,
    cell_unitary: np.ndarray,
) -> tuple[float, float, float]:
    transformed_kinetic = kinetic.transformed(cell_unitary)
    transformed_contact = contact.transformed(cell_unitary)
    kinetic_overlap = projection_overlaps(geometry, transformed_kinetic)
    contact_overlap = projection_overlaps(geometry, transformed_contact)
    inverse = geometry.gram_pseudoinverse
    kinetic_projection = float(
        np.vdot(kinetic_overlap, inverse @ kinetic_overlap).real
    )
    contact_projection = float(
        np.vdot(contact_overlap, inverse @ contact_overlap).real
    )
    projected_cross = np.vdot(kinetic_overlap, inverse @ contact_overlap)
    values = (
        statistics.kinetic_norm - kinetic_projection,
        statistics.contact_norm - contact_projection,
        statistics.cross - float(projected_cross.real),
    )
    return tuple(0.0 if abs(value) < 1e-8 else value for value in values)


class LowBodyObjective:
    def __init__(
        self,
        geometry: dense.FixedSectorGeometry,
        operator: LowBodyOperator,
        invariant_norm: float,
        invariant_trace: complex,
    ) -> None:
        self.geometry = geometry
        self.operator = operator
        self.denominator = invariant_norm - abs(invariant_trace) ** 2 / geometry.dimension
        self.evaluations = 0
        self.elapsed = 0.0

    def __call__(self, cell_unitary: np.ndarray) -> float:
        started = time.perf_counter()
        overlap = projection_overlaps(
            self.geometry, self.operator.transformed(cell_unitary)
        )
        projection_norm = float(
            np.vdot(overlap, self.geometry.gram_pseudoinverse @ overlap).real
        )
        numerator = self.denominator + abs(
            sector_trace(self.geometry, self.operator)
        ) ** 2 / self.geometry.dimension - projection_norm
        self.evaluations += 1
        self.elapsed += time.perf_counter() - started
        return numerator / self.denominator


def dense_components(
    geometry: dense.FixedSectorGeometry,
    kinetic: np.ndarray,
    contact: np.ndarray,
    cell_unitary: np.ndarray,
) -> tuple[float, float, float]:
    return dense.transformed_components(
        geometry, kinetic, contact, cell_unitary
    )


def validate_case(
    cell_count: int,
    particle_number: int,
    periodic: bool,
    seed: int,
) -> dict[str, float]:
    geometry = dense.FixedSectorGeometry(cell_count, particle_number)
    kinetic_matrix, contact_matrix, _, kinetic_basis = dense.build_hamiltonians(
        geometry, periodic
    )
    kinetic, contact, _ = low_body_operators(cell_count, periodic)

    reconstructed_kinetic = fixed_sector_matrix(geometry, kinetic)
    reconstructed_contact = fixed_sector_matrix(geometry, contact)
    reconstruction_error = max(
        float(np.max(np.abs(reconstructed_kinetic - kinetic_matrix))),
        float(np.max(np.abs(reconstructed_contact - contact_matrix))),
    )

    random = np.random.default_rng(seed)
    unitary = dense.haar_unitary(cell_count, random)
    lift = geometry.lifted_cell_unitary(unitary)
    transformed_kinetic = lift.conj().T @ kinetic_matrix @ lift
    transformed_contact = lift.conj().T @ contact_matrix @ lift
    dense_kinetic_overlap = geometry.local_projection_data(
        transformed_kinetic
    )[0]
    dense_contact_overlap = geometry.local_projection_data(
        transformed_contact
    )[0]
    low_kinetic_overlap = projection_overlaps(
        geometry, kinetic.transformed(unitary)
    )
    low_contact_overlap = projection_overlaps(
        geometry, contact.transformed(unitary)
    )
    overlap_error = max(
        float(np.max(np.abs(dense_kinetic_overlap - low_kinetic_overlap))),
        float(np.max(np.abs(dense_contact_overlap - low_contact_overlap))),
    )

    statistics = invariant_statistics(geometry, kinetic, contact)
    component_error = max(
        float(
            np.max(
                np.abs(
                    np.asarray(
                        residual_components(
                            geometry,
                            statistics,
                            kinetic,
                            contact,
                            candidate,
                        )
                    )
                    - dense_components(
                        geometry,
                        kinetic_matrix,
                        contact_matrix,
                        candidate,
                    )
                )
            )
        )
        for candidate in (
            np.eye(cell_count, dtype=complex),
            kinetic_basis,
            unitary,
        )
    )

    two_geometry = dense.FixedSectorGeometry(cell_count, 2)
    lift_two = two_geometry.lifted_cell_unitary(unitary)
    mode_unitary = np.kron(
        unitary, np.eye(SPINOR_DIMENSION, dtype=complex)
    )
    exterior_error = float(
        np.max(np.abs(exterior_square(mode_unitary) - lift_two))
    )
    norm_error = max(
        abs(
            statistics.kinetic_norm
            - float(np.vdot(kinetic_matrix, kinetic_matrix).real)
        ),
        abs(
            statistics.contact_norm
            - float(np.vdot(contact_matrix, contact_matrix).real)
        ),
        abs(
            statistics.cross
            - float(np.vdot(kinetic_matrix, contact_matrix).real)
        ),
    )
    return {
        "reconstruction": reconstruction_error,
        "exterior_square": exterior_error,
        "overlaps": overlap_error,
        "components": component_error,
        "sector_norms": float(norm_error),
    }


def validation_suite() -> dict[str, dict[str, float]]:
    cases = (
        (2, 4, False, 2026080701),
        (3, 6, False, 2026080702),
        (3, 6, True, 2026080703),
        (4, 3, False, 2026080704),
        (4, 3, True, 2026080705),
    )
    results = {
        f"L={cells},N={particles},{'periodic' if periodic else 'open'}": (
            validate_case(cells, particles, periodic, seed)
        )
        for cells, particles, periodic, seed in cases
    }
    random = np.random.default_rng(2026080711)
    one_body = random.normal(size=(16, 16)) + 1j * random.normal(size=(16, 16))
    one_body = (one_body + one_body.conj().T) / 2.0
    two_body = random.normal(size=(120, 120)) + 1j * random.normal(
        size=(120, 120)
    )
    two_body = (two_body + two_body.conj().T) / 2.0
    generic = LowBodyOperator(one_body, two_body)
    generic_geometry = dense.FixedSectorGeometry(4, 3)
    generic_matrix = fixed_sector_matrix(generic_geometry, generic)
    generic_dense_overlaps = generic_geometry.local_projection_data(
        generic_matrix
    )[0]
    generic_low_overlaps = projection_overlaps(generic_geometry, generic)
    results["L=4,N=3,generic Hermitian"] = {
        "overlaps": float(
            np.max(np.abs(generic_dense_overlaps - generic_low_overlaps))
        ),
        "sector_trace": float(
            abs(np.trace(generic_matrix) - sector_trace(generic_geometry, generic))
        ),
        "sector_norm": float(
            abs(
                np.vdot(generic_matrix, generic_matrix)
                - sector_inner_product(generic_geometry, generic, generic)
            )
        ),
        "hermiticity": float(
            np.max(np.abs(generic_matrix - generic_matrix.conj().T))
        ),
    }
    maximum = max(value for result in results.values() for value in result.values())
    if maximum > 2e-8:
        raise AssertionError(
            f"low-body validation failed with maximum error {maximum:.3e}"
        )
    return results


def exact_local_rank_audit(
    geometry: dense.FixedSectorGeometry,
) -> dict[str, int]:
    """Certify the L=4 local-subspace rank over the rational numbers."""

    integer_gram = np.rint(geometry.gram).astype(np.int64)
    generator_count = len(geometry.units)
    identities = []
    local_numbers = []
    for cell in range(geometry.cell_count):
        identity = np.zeros(generator_count, dtype=np.int64)
        number = np.zeros(generator_count, dtype=np.int64)
        for index, unit in enumerate(geometry.units):
            if unit.cell == cell and unit.row == unit.column:
                identity[index] = 1
                number[index] = unit.particles
        identities.append(identity)
        local_numbers.append(number)

    relations = [
        identities[cell] - identities[0]
        for cell in range(1, geometry.cell_count)
    ]
    relations.append(
        sum(local_numbers, np.zeros(generator_count, dtype=np.int64))
        - geometry.particle_number * identities[0]
    )
    relation_residual = max(
        int(np.max(np.abs(integer_gram @ relation))) for relation in relations
    )
    prime = 1_000_003
    modular_rank = dense.rank_modulo(integer_gram, prime)
    certified_rank = generator_count - len(relations)
    if relation_residual != 0 or modular_rank != certified_rank:
        raise AssertionError("exact four-cell local-rank audit failed")
    return {
        "generator_count": generator_count,
        "exact_relation_count": len(relations),
        "modular_prime": prime,
        "modular_rank": modular_rank,
        "relation_residual": relation_residual,
    }


def zero_mode_unitary(theta: float, phase: float) -> np.ndarray:
    cosine = math.cos(theta / 2.0)
    sine = math.sin(theta / 2.0)
    return np.asarray(
        [
            [cosine, -np.exp(-1j * phase) * sine],
            [np.exp(1j * phase) * sine, cosine],
        ],
        dtype=complex,
    )


def periodic_kinetic_representative(
    objective: LowBodyObjective,
    kinetic_basis: np.ndarray,
    theta_points: int = 25,
    phase_points: int = 48,
) -> tuple[np.ndarray, dict[str, float]]:
    eigenvalues = np.linalg.eigvalsh(dense.cell_kinetic_matrix(4, True))
    zero_indices = tuple(
        int(index) for index in np.flatnonzero(np.abs(eigenvalues) < 1e-10)
    )
    if len(zero_indices) != 2:
        raise AssertionError("periodic four-cell kinetic zero-space is not 2D")

    best_value = float("inf")
    best_unitary = kinetic_basis
    sampled_values = []
    for theta in np.linspace(0.0, math.pi, theta_points):
        for phase in np.linspace(
            0.0, 2.0 * math.pi, phase_points, endpoint=False
        ):
            rotation = np.eye(4, dtype=complex)
            rotation[np.ix_(zero_indices, zero_indices)] = zero_mode_unitary(
                float(theta), float(phase)
            )
            candidate = kinetic_basis @ rotation
            value = objective(candidate)
            sampled_values.append(value)
            if value < best_value:
                best_value = value
                best_unitary = candidate

    zero_generators = []
    left, right = zero_indices
    real = np.zeros((4, 4), dtype=complex)
    real[left, right] = real[right, left] = 1.0 / math.sqrt(2.0)
    imaginary = np.zeros((4, 4), dtype=complex)
    imaginary[left, right] = -1j / math.sqrt(2.0)
    imaginary[right, left] = 1j / math.sqrt(2.0)
    zero_generators.extend((real, imaginary))
    value, representative, iterations, gradient = dense.optimize_unitary(
        objective,
        best_unitary,
        tuple(zero_generators),
        max_iterations=80,
    )
    gradient_before_newton = float(gradient)
    newton_iterations = 0
    for newton_iterations in range(1, 9):
        gradient_vector = numerical_gradient(
            objective, representative, tuple(zero_generators), 2e-5
        )
        if float(np.linalg.norm(gradient_vector)) < 5e-10:
            newton_iterations -= 1
            break
        hessian = dense.numerical_hessian(
            objective, representative, tuple(zero_generators), 2e-4
        )
        displacement = -np.linalg.solve(hessian, gradient_vector)
        direction = sum(
            displacement[index] * generator
            for index, generator in enumerate(zero_generators)
        )
        representative = dense.unitary_chart(representative, direction)
    value = objective(representative)
    final_gradient = numerical_gradient(
        objective, representative, tuple(zero_generators), 2e-5
    )
    hessian = dense.numerical_hessian(
        objective, representative, tuple(zero_generators), 5e-4
    )
    return representative, {
        "grid_minimum": float(np.min(sampled_values)),
        "grid_maximum": float(np.max(sampled_values)),
        "refined_minimum": float(value),
        "iterations": float(iterations),
        "gradient_before_newton": gradient_before_newton,
        "newton_iterations": float(newton_iterations),
        "gradient_norm": float(np.linalg.norm(final_gradient)),
        "zero_family_hessian_minimum": float(
            np.min(np.linalg.eigvalsh(hessian))
        ),
    }


def endpoint_coupling(
    site: tuple[float, float, float],
    kinetic: tuple[float, float, float],
) -> float:
    if (
        abs(site[1]) > 2e-7
        or abs(site[2]) > 2e-7
        or abs(kinetic[0]) > 2e-7
        or abs(kinetic[2]) > 2e-7
    ):
        raise AssertionError(
            "endpoint locality identities failed; equal-coupling shortcut invalid"
        )
    if site[0] <= 0.0 or kinetic[1] <= 0.0:
        raise AssertionError("endpoint residuals do not define a positive coupling")
    return math.sqrt(site[0] / kinetic[1])


def numerical_gradient(
    objective: LowBodyObjective,
    cell_unitary: np.ndarray,
    generators: tuple[np.ndarray, ...],
    epsilon: float,
) -> np.ndarray:
    return np.asarray(
        [
            (
                objective(dense.unitary_chart(cell_unitary, epsilon * generator))
                - objective(
                    dense.unitary_chart(cell_unitary, -epsilon * generator)
                )
            )
            / (2.0 * epsilon)
            for generator in generators
        ],
        dtype=float,
    )


def stationarity_step_audit(
    objective: LowBodyObjective,
    cell_unitary: np.ndarray,
    generators: tuple[np.ndarray, ...],
) -> tuple[np.ndarray, dict[str, float]]:
    steps = (2e-3, 1e-3, 5e-4, 2.5e-4)
    gradients = tuple(
        numerical_gradient(objective, cell_unitary, generators, step)
        for step in steps
    )
    norms = tuple(float(np.linalg.norm(value)) for value in gradients)
    return gradients[2], {
        "step_2e-3": norms[0],
        "step_1e-3": norms[1],
        "step_5e-4": norms[2],
        "step_2_5e-4": norms[3],
        "minimum": min(norms),
        "maximum": max(norms),
    }


def hessian_step_audit(
    objective: LowBodyObjective,
    cell_unitary: np.ndarray,
    generators: tuple[np.ndarray, ...],
) -> tuple[np.ndarray, dict[str, float]]:
    steps = (2e-3, 1e-3, 5e-4, 2.5e-4)
    hessians = tuple(
        dense.numerical_hessian(objective, cell_unitary, generators, step)
        for step in steps
    )
    minima = tuple(float(np.min(np.linalg.eigvalsh(value))) for value in hessians)
    return hessians[2], {
        "step_2e-3": minima[0],
        "step_1e-3": minima[1],
        "step_5e-4": minima[2],
        "step_2_5e-4": minima[3],
        "minimum": min(minima),
        "maximum": max(minima),
    }


def downhill_certificate(
    objective: LowBodyObjective,
    endpoint: np.ndarray,
    gradient: np.ndarray,
    hessian: np.ndarray,
    generators: tuple[np.ndarray, ...],
    max_iterations: int,
) -> dict[str, object] | None:
    eigenvalues, eigenvectors = np.linalg.eigh(hessian)
    gradient_norm = float(np.linalg.norm(gradient))
    directions: list[tuple[str, np.ndarray]] = []
    if gradient_norm >= STATIONARITY_TOLERANCE:
        directions.append(
            (
                "nonstationary_gradient",
                sum(
                    -gradient[index] / gradient_norm * generator
                    for index, generator in enumerate(generators)
                ),
            )
        )
    if eigenvalues[0] < 0.0:
        directions.append(
            (
                "negative_chart_curvature",
                sum(
                    eigenvectors[index, 0] * generator
                    for index, generator in enumerate(generators)
                ),
            )
        )
    if not directions:
        return None
    endpoint_cost = objective(endpoint)
    runs = []
    for reason, direction in directions:
        candidates = []
        for amplitude in (0.01, 0.025, 0.05, 0.1):
            for sign in (-1.0, 1.0):
                candidate = dense.unitary_chart(
                    endpoint, sign * amplitude * direction
                )
                candidates.append((objective(candidate), candidate, amplitude, sign))
        sampled_cost, initial, amplitude, sign = min(
            candidates, key=lambda item: item[0]
        )
        optimized_cost, _, iterations, optimized_gradient = dense.optimize_unitary(
            objective, initial, generators, max_iterations=max_iterations
        )
        runs.append(
            {
                "reason": reason,
                "sampled_cost": float(sampled_cost),
                "sampled_amplitude": amplitude,
                "sampled_sign": sign,
                "optimized_cost": float(optimized_cost),
                "iterations": float(iterations),
                "optimized_gradient_norm": float(optimized_gradient),
            }
        )
    return {
        "failure_modes": tuple(reason for reason, _ in directions),
        "gradient_norm": gradient_norm,
        "hessian_eigenvalue": float(eigenvalues[0]),
        "endpoint_cost": float(endpoint_cost),
        "sampled_cost": min(float(run["sampled_cost"]) for run in runs),
        "optimized_cost": min(float(run["optimized_cost"]) for run in runs),
        "runs": tuple(runs),
    }


def evaluate_boundary(
    periodic: bool,
    random_samples: int,
    optimized_starts: int,
    max_iterations: int,
    seed: int,
) -> dict[str, object]:
    geometry = dense.FixedSectorGeometry(4, 8)
    rank_audit = exact_local_rank_audit(geometry)
    kinetic, contact, kinetic_basis = low_body_operators(4, periodic)
    statistics = invariant_statistics(geometry, kinetic, contact)
    identity = np.eye(4, dtype=complex)

    contact_objective = LowBodyObjective(
        geometry,
        contact,
        statistics.contact_norm,
        statistics.contact_trace,
    )
    zero_data: dict[str, float] | None = None
    if periodic:
        kinetic_representative, zero_data = periodic_kinetic_representative(
            contact_objective, kinetic_basis
        )
    else:
        kinetic_representative = kinetic_basis

    site_components = residual_components(
        geometry, statistics, kinetic, contact, identity
    )
    kinetic_components = residual_components(
        geometry, statistics, kinetic, contact, kinetic_representative
    )
    coupling = endpoint_coupling(site_components, kinetic_components)
    hamiltonian = kinetic.scaled_add(contact, coupling)
    denominator = statistics.centered_norm(geometry.dimension, coupling)
    objective = LowBodyObjective(
        geometry,
        hamiltonian,
        statistics.norm(coupling),
        statistics.kinetic_trace + coupling * statistics.contact_trace,
    )
    generators = dense.off_diagonal_generators(4)
    site_cost = objective(identity)
    kinetic_cost = objective(kinetic_representative)
    site_gradient, site_gradient_steps = stationarity_step_audit(
        objective, identity, generators
    )
    kinetic_gradient, kinetic_gradient_steps = stationarity_step_audit(
        objective, kinetic_representative, generators
    )
    site_hessian, site_hessian_steps = hessian_step_audit(
        objective, identity, generators
    )
    kinetic_hessian, kinetic_hessian_steps = hessian_step_audit(
        objective, kinetic_representative, generators
    )
    site_minimum = float(np.min(np.linalg.eigvalsh(site_hessian)))
    kinetic_minimum = float(np.min(np.linalg.eigvalsh(kinetic_hessian)))
    zero_minimum = (
        float(zero_data["zero_family_hessian_minimum"])
        if zero_data is not None
        else float("inf")
    )
    endpoint_gate = (
        abs(site_cost - kinetic_cost) < 2e-8
        and float(np.linalg.norm(site_gradient)) < STATIONARITY_TOLERANCE
        and float(np.linalg.norm(kinetic_gradient)) < STATIONARITY_TOLERANCE
        and site_minimum > 2e-5
        and kinetic_minimum > 2e-5
        and zero_minimum > 2e-5
    )
    site_downhill = downhill_certificate(
        objective,
        identity,
        site_gradient,
        site_hessian,
        generators,
        max_iterations,
    )
    kinetic_downhill = downhill_certificate(
        objective,
        kinetic_representative,
        kinetic_gradient,
        kinetic_hessian,
        generators,
        max_iterations,
    )

    phase_permutation_error = 0.0
    random = np.random.default_rng(seed)
    for _ in range(4):
        unitary = dense.haar_unitary(4, random)
        phases = np.diag(np.exp(2j * math.pi * random.random(4)))
        permutation = np.eye(4)[random.permutation(4)]
        reference = objective(unitary)
        phase_permutation_error = max(
            phase_permutation_error,
            abs(objective(unitary @ phases) - reference),
            abs(objective(unitary @ permutation) - reference),
        )
    if phase_permutation_error > 2e-8:
        raise AssertionError("four-cell quotient-invariance audit failed")

    random_costs: list[float] = []
    optimized: list[dict[str, float]] = []
    if endpoint_gate:
        starts = []
        for _ in range(random_samples):
            candidate = dense.haar_unitary(4, random)
            candidate_cost = float(objective(candidate))
            random_costs.append(candidate_cost)
            starts.append((candidate_cost, candidate))
        starts.sort(key=lambda item: item[0])
        for _, initial in starts[:optimized_starts]:
            value, _, iterations, gradient = dense.optimize_unitary(
                objective, initial, generators, max_iterations
            )
            optimized.append(
                {
                    "cost": float(value),
                    "iterations": float(iterations),
                    "gradient_norm": float(gradient),
                }
            )
    downhill_costs = [
        certificate["optimized_cost"]
        for certificate in (site_downhill, kinetic_downhill)
        if certificate is not None
    ]
    lowest = min(
        [site_cost, kinetic_cost]
        + downhill_costs
        + random_costs
        + [result["cost"] for result in optimized]
    )
    landscape_gate = endpoint_gate and lowest >= site_cost - 2e-7

    return {
        "boundary": "periodic" if periodic else "open",
        "geometry_dimension": geometry.dimension,
        "local_rank": geometry.local_subspace_dimension,
        "rank_audit": rank_audit,
        "kinetic_spectrum": np.linalg.eigvalsh(
            dense.cell_kinetic_matrix(4, periodic)
        ),
        "site_components": site_components,
        "kinetic_components": kinetic_components,
        "coupling": coupling,
        "denominator": denominator,
        "site_cost": site_cost,
        "kinetic_cost": kinetic_cost,
        "site_hessian_eigenvalues": np.linalg.eigvalsh(site_hessian),
        "kinetic_hessian_eigenvalues": np.linalg.eigvalsh(kinetic_hessian),
        "site_gradient": site_gradient,
        "kinetic_gradient": kinetic_gradient,
        "site_gradient_steps": site_gradient_steps,
        "kinetic_gradient_steps": kinetic_gradient_steps,
        "site_hessian_steps": site_hessian_steps,
        "kinetic_hessian_steps": kinetic_hessian_steps,
        "site_downhill": site_downhill,
        "kinetic_downhill": kinetic_downhill,
        "zero_family": zero_data,
        "phase_permutation_error": phase_permutation_error,
        "random_minimum": min(random_costs) if random_costs else None,
        "optimized": optimized,
        "lowest_cost": lowest,
        "endpoint_gate": endpoint_gate,
        "landscape_gate": landscape_gate,
        "evaluations": objective.evaluations + contact_objective.evaluations,
        "objective_seconds": objective.elapsed + contact_objective.elapsed,
    }


def print_validation(results: dict[str, dict[str, float]]) -> None:
    print("low-body validation against dense fixed-sector calculations")
    for label, checks in results.items():
        print(f"  {label}")
        for check, value in checks.items():
            print(f"    {check:18s} {value:.3e}")


def print_boundary(result: dict[str, object]) -> None:
    print(f"\n{result['boundary']} four-cell boundary")
    print("  sector dimension", result["geometry_dimension"])
    print("  local-subspace rank", result["local_rank"])
    print("  exact rank audit", result["rank_audit"])
    print("  kinetic spectrum", result["kinetic_spectrum"])
    if result["zero_family"] is not None:
        print("  periodic zero-family", result["zero_family"])
    print("  site components", result["site_components"])
    print("  kinetic components", result["kinetic_components"])
    print("  equal-endpoint coupling", result["coupling"])
    print("  site / kinetic costs", result["site_cost"], result["kinetic_cost"])
    print("  site Hessian", result["site_hessian_eigenvalues"])
    print("  kinetic Hessian", result["kinetic_hessian_eigenvalues"])
    print("  site gradient", result["site_gradient"])
    print("  kinetic gradient", result["kinetic_gradient"])
    print("  site stationarity audit", result["site_gradient_steps"])
    print("  kinetic stationarity audit", result["kinetic_gradient_steps"])
    print("  site Hessian step audit", result["site_hessian_steps"])
    print("  kinetic Hessian step audit", result["kinetic_hessian_steps"])
    print("  site downhill certificate", result["site_downhill"])
    print("  kinetic downhill certificate", result["kinetic_downhill"])
    print("  quotient-invariance error", result["phase_permutation_error"])
    print("  random minimum", result["random_minimum"])
    print("  optimized runs", result["optimized"])
    print("  lowest cost", result["lowest_cost"])
    print("  endpoint gate", result["endpoint_gate"])
    print("  landscape gate", result["landscape_gate"])
    print(
        "  evaluations / objective seconds",
        result["evaluations"],
        result["objective_seconds"],
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--validate-only", action="store_true")
    parser.add_argument("--random-samples", type=int, default=24)
    parser.add_argument("--optimized-starts", type=int, default=4)
    parser.add_argument("--max-iterations", type=int, default=50)
    parser.add_argument("--seed", type=int, default=20260807)
    arguments = parser.parse_args()

    started = time.perf_counter()
    validation = validation_suite()
    print_validation(validation)
    if arguments.validate_only:
        print(f"elapsed seconds {time.perf_counter() - started:.3f}")
        return

    open_result = evaluate_boundary(
        False,
        arguments.random_samples,
        arguments.optimized_starts,
        arguments.max_iterations,
        arguments.seed,
    )
    print_boundary(open_result)
    periodic_result = evaluate_boundary(
        True,
        arguments.random_samples,
        arguments.optimized_starts,
        arguments.max_iterations,
        arguments.seed + 1,
    )
    print_boundary(periodic_result)

    if open_result["landscape_gate"] and periodic_result["landscape_gate"]:
        classification = (
            "FINITE SELECTOR SURVIVES THE FOUR-CELL LANDSCAPE GATE; proceed "
            "to deferred state and robustness controls without inferring a "
            "continuum or cosmological result."
        )
    else:
        classification = (
            "FOUR-CELL ROBUSTNESS FAILURE for the finite selector as currently "
            "defined; do not proceed to positive state diagnostics unless an "
            "implementation or predeclared-gate error is identified."
        )
    print("\nclassification")
    print(" ", classification)
    print(f"total elapsed seconds {time.perf_counter() - started:.3f}")


if __name__ == "__main__":
    main()
