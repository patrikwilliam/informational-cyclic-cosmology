#!/usr/bin/env python3
"""Three-cell finite gate for the restricted EC-inspired CAR selector.

The calculation generalizes the v0.1.3 two-cell fixed-charge construction to
three cells with four Dirac modes per cell.  It tests the half-filled N=6
sector for open and periodic spatial links.  The admissible factorizations are
the number-preserving Dirac-algebra normalizer represented by W in U(3), modulo
column phases and permutations.

This is a finite feasibility gate.  It is not a continuum limit, an arbitrary-
size result, or a cosmological calculation.
"""

from __future__ import annotations

import argparse
import itertools
import math
import time
from dataclasses import dataclass

import numpy as np

import ec_axial_selector_analysis as two_cell


SPINOR_DIMENSION = 4
LOCAL_FOCK_DIMENSION = 1 << SPINOR_DIMENSION


def binomial_or_zero(upper: int, lower: int) -> int:
    if lower < 0 or lower > upper:
        return 0
    return math.comb(upper, lower)


def annihilate(mask: int, mode: int) -> tuple[int, int] | None:
    if not (mask >> mode) & 1:
        return None
    sign = -1 if (mask & ((1 << mode) - 1)).bit_count() % 2 else 1
    return mask & ~(1 << mode), sign


def create(mask: int, mode: int) -> tuple[int, int] | None:
    if (mask >> mode) & 1:
        return None
    sign = -1 if (mask & ((1 << mode) - 1)).bit_count() % 2 else 1
    return mask | (1 << mode), sign


def apply_number_conserving_monomial(
    mask: int,
    annihilation_modes: tuple[int, ...],
    creation_modes: tuple[int, ...],
) -> tuple[int, int] | None:
    """Apply operators in the supplied right-to-left order."""

    result = mask
    sign = 1
    for mode in annihilation_modes:
        applied = annihilate(result, mode)
        if applied is None:
            return None
        result, factor = applied
        sign *= factor
    for mode in creation_modes:
        applied = create(result, mode)
        if applied is None:
            return None
        result, factor = applied
        sign *= factor
    return result, sign


def local_state(mask: int, cell: int) -> int:
    return (mask >> (SPINOR_DIMENSION * cell)) & (LOCAL_FOCK_DIMENSION - 1)


@dataclass(frozen=True)
class LocalMatrixUnit:
    cell: int
    particles: int
    row: int
    column: int


class FixedSectorGeometry:
    """Fixed-charge space and exact projection onto one-cell Hamiltonians."""

    def __init__(self, cell_count: int, particle_number: int) -> None:
        self.cell_count = cell_count
        self.particle_number = particle_number
        self.mode_count = SPINOR_DIMENSION * cell_count
        self.masks = tuple(
            sum(1 << mode for mode in occupied)
            for occupied in itertools.combinations(
                range(self.mode_count), particle_number
            )
        )
        self.position = {mask: index for index, mask in enumerate(self.masks)}
        self.dimension = len(self.masks)
        self.local_states = {
            particles: tuple(
                state
                for state in range(LOCAL_FOCK_DIMENSION)
                if state.bit_count() == particles
            )
            for particles in range(SPINOR_DIMENSION + 1)
        }
        self.units = tuple(
            LocalMatrixUnit(cell, particles, row, column)
            for cell in range(cell_count)
            for particles, states in self.local_states.items()
            for row in states
            for column in states
        )
        self.unit_supports = tuple(
            self._unit_support(unit) for unit in self.units
        )
        self.gram = self._gram_matrix()
        self.gram_pseudoinverse = np.linalg.pinv(self.gram, rcond=1e-12)
        self.local_subspace_dimension = int(
            np.linalg.matrix_rank(self.gram, tol=1e-10)
        )
        self._unitary_blocks = self._build_unitary_blocks()

    def _unit_support(
        self, unit: LocalMatrixUnit
    ) -> tuple[np.ndarray, np.ndarray]:
        shift = SPINOR_DIMENSION * unit.cell
        cell_mask = (LOCAL_FOCK_DIMENSION - 1) << shift
        rows: list[int] = []
        columns: list[int] = []
        for column_position, mask in enumerate(self.masks):
            if local_state(mask, unit.cell) != unit.column:
                continue
            target = (mask & ~cell_mask) | (unit.row << shift)
            rows.append(self.position[target])
            columns.append(column_position)
        return np.asarray(rows, dtype=int), np.asarray(columns, dtype=int)

    def _gram_matrix(self) -> np.ndarray:
        count = len(self.units)
        gram = np.zeros((count, count), dtype=float)
        remaining_modes_same = SPINOR_DIMENSION * (self.cell_count - 1)
        remaining_modes_distinct = SPINOR_DIMENSION * (self.cell_count - 2)
        for left_index, left in enumerate(self.units):
            for right_index in range(left_index, count):
                right = self.units[right_index]
                value = 0.0
                if left.cell == right.cell:
                    if left.row == right.row and left.column == right.column:
                        value = float(
                            binomial_or_zero(
                                remaining_modes_same,
                                self.particle_number - left.particles,
                            )
                        )
                elif (
                    left.row == left.column
                    and right.row == right.column
                ):
                    value = float(
                        binomial_or_zero(
                            remaining_modes_distinct,
                            self.particle_number
                            - left.particles
                            - right.particles,
                        )
                    )
                gram[left_index, right_index] = value
                gram[right_index, left_index] = value
        return gram

    def local_projection_data(
        self, matrix: np.ndarray
    ) -> tuple[np.ndarray, np.ndarray, float]:
        if matrix.shape != (self.dimension, self.dimension):
            raise ValueError("matrix has the wrong fixed-sector dimension")
        overlaps = np.asarray(
            [
                np.sum(matrix[rows, columns])
                for rows, columns in self.unit_supports
            ],
            dtype=complex,
        )
        coefficients = self.gram_pseudoinverse @ overlaps
        projection_norm = float(np.vdot(coefficients, overlaps).real)
        return overlaps, coefficients, projection_norm

    def local_projection(self, matrix: np.ndarray) -> np.ndarray:
        _, coefficients, _ = self.local_projection_data(matrix)
        result = np.zeros_like(matrix)
        for coefficient, (rows, columns) in zip(
            coefficients, self.unit_supports
        ):
            result[rows, columns] += coefficient
        return result

    def interaction_norm(self, matrix: np.ndarray) -> float:
        _, _, projection_norm = self.local_projection_data(matrix)
        value = float(np.vdot(matrix, matrix).real) - projection_norm
        if value < 0.0 and abs(value) < 1e-8:
            return 0.0
        return value

    def residual_components(
        self, first: np.ndarray, second: np.ndarray
    ) -> tuple[float, float, float]:
        first_overlap, first_coefficients, first_projection_norm = (
            self.local_projection_data(first)
        )
        second_overlap, second_coefficients, second_projection_norm = (
            self.local_projection_data(second)
        )
        first_norm = float(np.vdot(first, first).real) - first_projection_norm
        second_norm = float(np.vdot(second, second).real) - second_projection_norm
        projected_cross = np.vdot(first_coefficients, second_overlap)
        cross = float((np.vdot(first, second) - projected_cross).real)
        del first_overlap, second_coefficients
        return first_norm, second_norm, cross

    def projection_audit(self, seed: int = 20260718) -> dict[str, float]:
        random = np.random.default_rng(seed)
        matrix = random.normal(size=(self.dimension, self.dimension))
        matrix = matrix + matrix.T
        projection = self.local_projection(matrix.astype(complex))
        repeated = self.local_projection(projection)
        residual = matrix - projection
        overlaps = np.asarray(
            [
                np.sum(residual[rows, columns])
                for rows, columns in self.unit_supports
            ]
        )

        local_coefficients = random.normal(size=len(self.units))
        local_matrix = np.zeros_like(projection)
        for coefficient, (rows, columns) in zip(
            local_coefficients, self.unit_supports
        ):
            local_matrix[rows, columns] += coefficient
        local_residual = local_matrix - self.local_projection(local_matrix)
        return {
            "idempotence": float(np.max(np.abs(repeated - projection))),
            "orthogonality": float(np.max(np.abs(overlaps))),
            "local_reproduction": float(np.max(np.abs(local_residual))),
        }

    def _build_unitary_blocks(
        self,
    ) -> tuple[tuple[tuple[int, ...], np.ndarray, tuple[int, ...]], ...]:
        subsets = {
            number: tuple(itertools.combinations(range(self.cell_count), number))
            for number in range(self.cell_count + 1)
        }
        patterns: dict[tuple[int, ...], list[int]] = {}
        for mask in self.masks:
            pattern = tuple(
                sum(
                    (mask >> (cell * SPINOR_DIMENSION + spinor)) & 1
                    for cell in range(self.cell_count)
                )
                for spinor in range(SPINOR_DIMENSION)
            )
            patterns.setdefault(pattern, []).append(mask)

        blocks = []
        for pattern in sorted(patterns):
            product_subsets = tuple(
                itertools.product(*(subsets[number] for number in pattern))
            )
            positions = []
            signs = []
            for flavor_subsets in product_subsets:
                mask = 0
                flavor_ranks = []
                for spinor, occupied_cells in enumerate(flavor_subsets):
                    for cell in occupied_cells:
                        mask |= 1 << (cell * SPINOR_DIMENSION + spinor)
                for cell in range(self.cell_count):
                    for spinor in range(SPINOR_DIMENSION):
                        if (mask >> (cell * SPINOR_DIMENSION + spinor)) & 1:
                            flavor_ranks.append(spinor * self.cell_count + cell)
                inversions = sum(
                    flavor_ranks[left] > flavor_ranks[right]
                    for left in range(len(flavor_ranks))
                    for right in range(left + 1, len(flavor_ranks))
                )
                positions.append(self.position[mask])
                signs.append(-1 if inversions % 2 else 1)
            if set(positions) != set(self.position[mask] for mask in patterns[pattern]):
                raise AssertionError("unitary block enumeration is inconsistent")
            blocks.append((pattern, np.asarray(positions, dtype=int), tuple(signs)))
        return tuple(blocks)

    def lifted_cell_unitary(self, cell_unitary: np.ndarray) -> np.ndarray:
        if cell_unitary.shape != (self.cell_count, self.cell_count):
            raise ValueError("cell unitary has the wrong dimension")
        exterior_powers: dict[int, np.ndarray] = {}
        for number in range(self.cell_count + 1):
            subsets = tuple(itertools.combinations(range(self.cell_count), number))
            power = np.zeros((len(subsets), len(subsets)), dtype=complex)
            for target_index, target in enumerate(subsets):
                for source_index, source in enumerate(subsets):
                    power[target_index, source_index] = np.linalg.det(
                        cell_unitary[np.ix_(target, source)]
                    )
            exterior_powers[number] = power

        result = np.zeros((self.dimension, self.dimension), dtype=complex)
        for pattern, positions, signs_tuple in self._unitary_blocks:
            block = np.array([[1.0 + 0.0j]])
            for number in pattern:
                block = np.kron(block, exterior_powers[number])
            signs = np.asarray(signs_tuple, dtype=float)
            block = signs[:, None] * block * signs[None, :]
            result[np.ix_(positions, positions)] = block
        return result


def rank_modulo(integer_matrix: np.ndarray, prime: int) -> int:
    """Return the exact matrix rank over the finite field with `prime` elements."""

    matrix = [
        [int(value) % prime for value in row]
        for row in integer_matrix.tolist()
    ]
    row_count = len(matrix)
    column_count = len(matrix[0])
    rank = 0
    for column in range(column_count):
        pivot = next(
            (
                row
                for row in range(rank, row_count)
                if matrix[row][column] != 0
            ),
            None,
        )
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = pow(matrix[rank][column], prime - 2, prime)
        for row in range(rank + 1, row_count):
            if matrix[row][column] == 0:
                continue
            factor = matrix[row][column] * inverse % prime
            matrix[row] = [
                (left - factor * right) % prime
                for left, right in zip(matrix[row], matrix[rank])
            ]
        rank += 1
        if rank == row_count:
            break
    return rank


def exact_local_rank_audit() -> dict[str, int]:
    """Certify the three-cell local-subspace rank using integer arithmetic."""

    geometry = FixedSectorGeometry(3, 6)
    rounded_gram = np.rint(geometry.gram).astype(np.int64)
    if np.max(np.abs(geometry.gram - rounded_gram)) != 0.0:
        raise AssertionError("the local Gram matrix is not integer-valued")

    def identity_coefficients(cell: int) -> np.ndarray:
        return np.asarray(
            [
                int(unit.cell == cell and unit.row == unit.column)
                for unit in geometry.units
            ],
            dtype=np.int64,
        )

    def number_coefficients(cell: int) -> np.ndarray:
        return np.asarray(
            [
                unit.particles
                if unit.cell == cell and unit.row == unit.column
                else 0
                for unit in geometry.units
            ],
            dtype=np.int64,
        )

    identities = tuple(identity_coefficients(cell) for cell in range(3))
    relations = (
        identities[0] - identities[1],
        identities[0] - identities[2],
        sum(number_coefficients(cell) for cell in range(3))
        - geometry.particle_number * identities[0],
    )
    relation_residual = max(
        int(np.max(np.abs(rounded_gram @ relation)))
        for relation in relations
    )
    prime = 1_000_003
    modular_rank = rank_modulo(rounded_gram, prime)
    if relation_residual != 0 or modular_rank != 207:
        raise AssertionError("the exact three-cell local-rank audit failed")
    if len(geometry.units) - len(relations) != modular_rank:
        raise AssertionError("the stated relations do not certify the rank")
    return {
        "generator_count": len(geometry.units),
        "exact_relation_count": len(relations),
        "modular_prime": prime,
        "modular_rank": modular_rank,
        "relation_residual": relation_residual,
    }


def second_quantized_one_body(
    geometry: FixedSectorGeometry, one_particle: np.ndarray
) -> np.ndarray:
    terms = [
        (row, column, coefficient)
        for row in range(geometry.mode_count)
        for column in range(geometry.mode_count)
        if abs((coefficient := one_particle[row, column])) > 1e-14
    ]
    result = np.zeros((geometry.dimension, geometry.dimension), dtype=complex)
    for source_position, source in enumerate(geometry.masks):
        for row, column, coefficient in terms:
            applied = apply_number_conserving_monomial(
                source, (column,), (row,)
            )
            if applied is None:
                continue
            target, sign = applied
            result[geometry.position[target], source_position] += coefficient * sign
    return result


def axial_contact(geometry: FixedSectorGeometry) -> np.ndarray:
    _, gamma_5, alpha = two_cell.dirac_matrices()
    axial_matrices = [gamma_5, *(matrix @ gamma_5 for matrix in alpha)]
    signatures = (1.0, -1.0, -1.0, -1.0)
    combined_terms: dict[tuple[int, int, int, int], complex] = {}
    for cell in range(geometry.cell_count):
        offset = cell * SPINOR_DIMENSION
        for signature, matrix in zip(signatures, axial_matrices):
            for first_row in range(SPINOR_DIMENSION):
                for first_column in range(SPINOR_DIMENSION):
                    first = matrix[first_row, first_column]
                    if abs(first) <= 1e-14:
                        continue
                    for second_row in range(SPINOR_DIMENSION):
                        for second_column in range(SPINOR_DIMENSION):
                            second = matrix[second_row, second_column]
                            if abs(second) <= 1e-14:
                                continue
                            key = (
                                offset + first_row,
                                offset + second_row,
                                offset + first_column,
                                offset + second_column,
                            )
                            combined_terms[key] = combined_terms.get(key, 0.0j) - (
                                signature * first * second
                            )

    terms = [
        (*key, coefficient)
        for key, coefficient in combined_terms.items()
        if abs(coefficient) > 1e-14
    ]
    result = np.zeros((geometry.dimension, geometry.dimension), dtype=complex)
    for source_position, source in enumerate(geometry.masks):
        for first_row, second_row, first_column, second_column, coefficient in terms:
            applied = apply_number_conserving_monomial(
                source,
                (second_column, first_column),
                (second_row, first_row),
            )
            if applied is None:
                continue
            target, sign = applied
            result[geometry.position[target], source_position] += coefficient * sign
    return result


def density_contact(geometry: FixedSectorGeometry) -> np.ndarray:
    diagonal = np.asarray(
        [
            sum(
                (number := local_state(mask, cell).bit_count()) * (number - 1)
                for cell in range(geometry.cell_count)
            )
            for mask in geometry.masks
        ],
        dtype=float,
    )
    return np.diag(diagonal).astype(complex)


def cell_kinetic_matrix(cell_count: int, periodic: bool) -> np.ndarray:
    result = np.zeros((cell_count, cell_count), dtype=complex)
    for cell in range(cell_count - 1):
        result[cell, cell + 1] = -1j
        result[cell + 1, cell] = 1j
    if periodic:
        if cell_count < 3:
            raise ValueError("periodic orientation requires at least three cells")
        result[cell_count - 1, 0] = -1j
        result[0, cell_count - 1] = 1j
    return result


def build_hamiltonians(
    geometry: FixedSectorGeometry, periodic: bool
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    _, _, alpha = two_cell.dirac_matrices()
    cell_kinetic = cell_kinetic_matrix(geometry.cell_count, periodic)
    kinetic = second_quantized_one_body(
        geometry, np.kron(cell_kinetic, alpha[0])
    )
    contact = axial_contact(geometry)
    _, kinetic_basis = np.linalg.eigh(cell_kinetic)
    return kinetic, contact, density_contact(geometry), kinetic_basis


def centered_norm(matrix: np.ndarray) -> float:
    dimension = matrix.shape[0]
    centered = matrix - np.trace(matrix) / dimension * np.eye(dimension)
    return float(np.vdot(centered, centered).real)


def transformed_components(
    geometry: FixedSectorGeometry,
    kinetic: np.ndarray,
    contact: np.ndarray,
    cell_unitary: np.ndarray,
) -> tuple[float, float, float]:
    lift = geometry.lifted_cell_unitary(cell_unitary)
    transformed_kinetic = lift.conj().T @ kinetic @ lift
    transformed_contact = lift.conj().T @ contact @ lift
    return geometry.residual_components(transformed_kinetic, transformed_contact)


def off_diagonal_generators(dimension: int) -> tuple[np.ndarray, ...]:
    result = []
    for left in range(dimension):
        for right in range(left + 1, dimension):
            real = np.zeros((dimension, dimension), dtype=complex)
            real[left, right] = real[right, left] = 1.0 / math.sqrt(2.0)
            imaginary = np.zeros((dimension, dimension), dtype=complex)
            imaginary[left, right] = -1j / math.sqrt(2.0)
            imaginary[right, left] = 1j / math.sqrt(2.0)
            result.extend((real, imaginary))
    return tuple(result)


def unitary_chart(cell_unitary: np.ndarray, generator: np.ndarray) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(generator)
    update = (eigenvectors * np.exp(1j * eigenvalues)) @ eigenvectors.conj().T
    return cell_unitary @ update


def haar_unitary(dimension: int, random: np.random.Generator) -> np.ndarray:
    matrix = random.normal(size=(dimension, dimension)) + 1j * random.normal(
        size=(dimension, dimension)
    )
    unitary, triangular = np.linalg.qr(matrix)
    phases = np.diag(triangular)
    phases = np.where(np.abs(phases) > 0.0, phases / np.abs(phases), 1.0)
    return unitary @ np.diag(phases.conj())


def best_decomposition_overlap(first: np.ndarray, second: np.ndarray) -> float:
    overlaps = np.abs(first.conj().T @ second) ** 2
    return float(
        max(
            sum(overlaps[row, permutation[row]] for row in range(first.shape[0]))
            / first.shape[0]
            for permutation in itertools.permutations(range(first.shape[0]))
        )
    )


class SelectorObjective:
    def __init__(
        self,
        geometry: FixedSectorGeometry,
        hamiltonian: np.ndarray,
    ) -> None:
        self.geometry = geometry
        self.hamiltonian = hamiltonian
        self.denominator = centered_norm(hamiltonian)
        self.evaluations = 0
        self.elapsed = 0.0

    def __call__(self, cell_unitary: np.ndarray) -> float:
        started = time.perf_counter()
        lift = self.geometry.lifted_cell_unitary(cell_unitary)
        transformed = lift.conj().T @ self.hamiltonian @ lift
        value = self.geometry.interaction_norm(transformed) / self.denominator
        self.evaluations += 1
        self.elapsed += time.perf_counter() - started
        return value


def numerical_hessian(
    objective: SelectorObjective,
    cell_unitary: np.ndarray,
    generators: tuple[np.ndarray, ...],
    epsilon: float,
) -> np.ndarray:
    count = len(generators)
    hessian = np.zeros((count, count), dtype=float)
    center = objective(cell_unitary)
    for index, generator in enumerate(generators):
        plus = objective(unitary_chart(cell_unitary, epsilon * generator))
        minus = objective(unitary_chart(cell_unitary, -epsilon * generator))
        hessian[index, index] = (plus - 2.0 * center + minus) / epsilon**2
    for left in range(count):
        for right in range(left + 1, count):
            values = []
            for left_sign, right_sign in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
                direction = epsilon * (
                    left_sign * generators[left] + right_sign * generators[right]
                )
                values.append(objective(unitary_chart(cell_unitary, direction)))
            value = (values[0] - values[1] - values[2] + values[3]) / (
                4.0 * epsilon**2
            )
            hessian[left, right] = hessian[right, left] = value
    return hessian


def optimize_unitary(
    objective: SelectorObjective,
    initial: np.ndarray,
    generators: tuple[np.ndarray, ...],
    max_iterations: int,
    derivative_step: float = 2e-4,
) -> tuple[float, np.ndarray, int, float]:
    current = initial
    value = objective(current)
    gradient_norm = float("inf")
    for iteration in range(1, max_iterations + 1):
        derivatives = []
        for generator in generators:
            plus = objective(unitary_chart(current, derivative_step * generator))
            minus = objective(unitary_chart(current, -derivative_step * generator))
            derivatives.append((plus - minus) / (2.0 * derivative_step))
        gradient_norm = float(np.linalg.norm(derivatives))
        if gradient_norm < 1e-8:
            return value, current, iteration, gradient_norm
        gradient = sum(
            derivative * generator
            for derivative, generator in zip(derivatives, generators)
        )
        accepted = False
        step = min(0.5, 0.15 / max(gradient_norm, 1e-12))
        for _ in range(12):
            candidate = unitary_chart(current, -step * gradient)
            candidate_value = objective(candidate)
            if candidate_value < value - 1e-12:
                current = candidate
                value = candidate_value
                accepted = True
                break
            step *= 0.5
        if not accepted:
            return value, current, iteration, gradient_norm
    return value, current, max_iterations, gradient_norm


def entropy_bits(matrix: np.ndarray) -> float:
    eigenvalues = np.linalg.eigvalsh(matrix)
    eigenvalues = eigenvalues[eigenvalues > 1e-14]
    return float(-np.sum(eigenvalues * np.log2(eigenvalues)))


def state_tensor(
    geometry: FixedSectorGeometry, state: np.ndarray
) -> np.ndarray:
    tensor = np.zeros((LOCAL_FOCK_DIMENSION,) * geometry.cell_count, dtype=complex)
    for amplitude, mask in zip(state, geometry.masks):
        tensor[tuple(local_state(mask, cell) for cell in range(geometry.cell_count))] = (
            amplitude
        )
    return tensor


def one_cell_diagnostics(
    geometry: FixedSectorGeometry, state: np.ndarray
) -> dict[str, float]:
    tensor = state_tensor(geometry, state)
    number_groups = [
        np.asarray(geometry.local_states[number], dtype=int)
        for number in range(SPINOR_DIMENSION + 1)
    ]
    even = np.concatenate((number_groups[0], number_groups[2], number_groups[4]))
    odd = np.concatenate((number_groups[1], number_groups[3]))
    values = {"mode": [], "number_accessible": [], "parity_accessible": []}

    for cell in range(geometry.cell_count):
        coefficients = np.moveaxis(tensor, cell, 0).reshape(
            LOCAL_FOCK_DIMENSION, -1
        )
        reduced = coefficients @ coefficients.conj().T
        mode_entropy = entropy_bits(reduced)

        def accessible(groups: list[np.ndarray]) -> tuple[float, float]:
            accessible_entropy = 0.0
            probabilities = []
            for indices in groups:
                block = reduced[np.ix_(indices, indices)]
                probability = float(np.trace(block).real)
                if probability <= 1e-14:
                    continue
                probabilities.append(probability)
                accessible_entropy += probability * entropy_bits(
                    block / probability
                )
            probabilities_array = np.asarray(probabilities)
            shannon = float(
                -np.sum(probabilities_array * np.log2(probabilities_array))
            )
            return accessible_entropy, shannon

        number_accessible, number_shannon = accessible(number_groups)
        parity_accessible, parity_shannon = accessible([even, odd])
        if abs(mode_entropy - number_accessible - number_shannon) > 1e-9:
            raise AssertionError("local-number entropy identity failed")
        if abs(mode_entropy - parity_accessible - parity_shannon) > 1e-9:
            raise AssertionError("local-parity entropy identity failed")
        values["mode"].append(mode_entropy)
        values["number_accessible"].append(number_accessible)
        values["parity_accessible"].append(parity_accessible)
    return {name: float(np.mean(entries)) for name, entries in values.items()}


def stationary_diagnostic(
    geometry: FixedSectorGeometry,
    kinetic: np.ndarray,
    contact: np.ndarray,
    coupling: float,
    kinetic_basis: np.ndarray,
) -> dict[str, float]:
    hamiltonian = kinetic + coupling * contact
    eigenvalues, eigenvectors = np.linalg.eigh(hamiltonian)
    ground_multiplicity = int(
        np.sum(np.abs(eigenvalues - eigenvalues[0]) < 1e-10)
    )
    gap_above_ground = (
        float(eigenvalues[ground_multiplicity] - eigenvalues[0])
        if ground_multiplicity < len(eigenvalues)
        else float("nan")
    )
    state = eigenvectors[:, 0]
    result = {
        "energy": float(eigenvalues[0]),
        "gap": float(eigenvalues[1] - eigenvalues[0]),
        "ground_multiplicity": float(ground_multiplicity),
        "gap_above_ground": gap_above_ground,
        "residual": float(
            np.linalg.norm(hamiltonian @ state - eigenvalues[0] * state)
        ),
    }
    names = ("mode", "number_accessible", "parity_accessible")
    if ground_multiplicity == 1:
        momentum_lift = geometry.lifted_cell_unitary(kinetic_basis)
        transformed_state = momentum_lift.conj().T @ state
        site = one_cell_diagnostics(geometry, state)
        momentum = one_cell_diagnostics(geometry, transformed_state)
        for name in names:
            result[f"site_{name}"] = site[name]
            result[f"momentum_{name}"] = momentum[name]
            result[f"contrast_{name}"] = site[name] - momentum[name]
    else:
        for name in names:
            result[f"site_{name}"] = float("nan")
            result[f"momentum_{name}"] = float("nan")
            result[f"contrast_{name}"] = float("nan")
    return result


def filling_controls(seed: int) -> dict[str, object]:
    random = np.random.default_rng(seed)
    test_unitaries = tuple(haar_unitary(3, random) for _ in range(8))
    generators = off_diagonal_generators(3)
    rows = []
    landscapes = []
    for particle_number in range(4, 9):
        geometry = FixedSectorGeometry(3, particle_number)
        hessian_minima = {}
        periodic_coupling = float("nan")
        stationary = None
        for periodic in (False, True):
            kinetic, contact, _, kinetic_basis = build_hamiltonians(
                geometry, periodic
            )
            site = transformed_components(
                geometry, kinetic, contact, np.eye(3, dtype=complex)
            )
            momentum = transformed_components(
                geometry, kinetic, contact, kinetic_basis
            )
            coupling = math.sqrt(site[0] / momentum[1])
            objective = SelectorObjective(
                geometry, kinetic + coupling * contact
            )
            site_hessian = numerical_hessian(
                objective, np.eye(3, dtype=complex), generators, 1e-3
            )
            momentum_hessian = numerical_hessian(
                objective, kinetic_basis, generators, 1e-3
            )
            label = "periodic" if periodic else "open"
            hessian_minima[label] = (
                float(np.min(np.linalg.eigvalsh(site_hessian))),
                float(np.min(np.linalg.eigvalsh(momentum_hessian))),
            )
            if periodic:
                periodic_coupling = coupling
                landscapes.append(
                    [objective(unitary) for unitary in test_unitaries]
                )
                stationary = stationary_diagnostic(
                    geometry, kinetic, contact, coupling, kinetic_basis
                )
        if stationary is None:
            raise AssertionError("periodic filling control was not evaluated")
        rows.append(
            {
                "particle_number": particle_number,
                "dimension": geometry.dimension,
                "coupling": periodic_coupling,
                "open_site_hessian_minimum": hessian_minima["open"][0],
                "open_momentum_hessian_minimum": hessian_minima["open"][1],
                "periodic_site_hessian_minimum": hessian_minima["periodic"][0],
                "periodic_momentum_hessian_minimum": hessian_minima[
                    "periodic"
                ][1],
                "ground_multiplicity": int(stationary["ground_multiplicity"]),
                "gap_above_ground": stationary["gap_above_ground"],
                "contrast_mode": stationary["contrast_mode"],
                "contrast_number_accessible": stationary[
                    "contrast_number_accessible"
                ],
                "contrast_parity_accessible": stationary[
                    "contrast_parity_accessible"
                ],
            }
        )
    landscape_array = np.asarray(landscapes)
    maximum_spread = float(np.max(np.ptp(landscape_array, axis=0)))
    if maximum_spread > 1e-9:
        raise AssertionError("periodic normalized selector changed across fillings")
    for row in rows:
        if row["open_site_hessian_minimum"] <= 0.0:
            raise AssertionError("an open site endpoint lost strictness")
        if row["open_momentum_hessian_minimum"] >= 0.0:
            raise AssertionError("an open kinetic endpoint no longer fails")
        if min(
            row["periodic_site_hessian_minimum"],
            row["periodic_momentum_hessian_minimum"],
        ) <= 0.0:
            raise AssertionError("a periodic endpoint lost strictness")
        if row["particle_number"] % 2 == 0:
            if row["ground_multiplicity"] != 1:
                raise AssertionError("an even filling lost its isolated ground state")
            if min(
                row["contrast_mode"],
                row["contrast_number_accessible"],
                row["contrast_parity_accessible"],
            ) <= 0.0:
                raise AssertionError("an even filling lost its entropy contrast")
    return {"rows": rows, "maximum_landscape_spread": maximum_spread}


def density_controls(seed: int) -> tuple[dict[str, object], ...]:
    rows = []
    generators = off_diagonal_generators(3)
    for periodic in (False, True):
        geometry = FixedSectorGeometry(3, 6)
        kinetic, _, density, kinetic_basis = build_hamiltonians(geometry, periodic)
        site = transformed_components(
            geometry, kinetic, density, np.eye(3, dtype=complex)
        )
        momentum = transformed_components(
            geometry, kinetic, density, kinetic_basis
        )
        coupling = math.sqrt(site[0] / momentum[1])
        objective = SelectorObjective(geometry, kinetic + coupling * density)
        site_hessian = numerical_hessian(
            objective, np.eye(3, dtype=complex), generators, 1e-3
        )
        momentum_hessian = numerical_hessian(
            objective, kinetic_basis, generators, 1e-3
        )
        endpoint_cost = objective(np.eye(3, dtype=complex))
        random = np.random.default_rng(seed + int(periodic))
        random_costs = [objective(haar_unitary(3, random)) for _ in range(24)]
        row = {
            "boundary": "periodic" if periodic else "open",
            "coupling": coupling,
            "endpoint_cost": endpoint_cost,
            "minimum_site_hessian": float(np.min(np.linalg.eigvalsh(site_hessian))),
            "minimum_momentum_hessian": float(
                np.min(np.linalg.eigvalsh(momentum_hessian))
            ),
            "smallest_random_cost": min(random_costs),
        }
        if min(
            row["minimum_site_hessian"], row["minimum_momentum_hessian"]
        ) <= 0.0:
            raise AssertionError("density control lost endpoint strictness")
        if row["smallest_random_cost"] < endpoint_cost - 1e-8:
            raise AssertionError("density control found a lower random factorization")
        rows.append(row)
    return tuple(rows)


def reproduce_two_cell() -> dict[str, float]:
    geometry = FixedSectorGeometry(2, 4)
    kinetic, contact, _, kinetic_basis = build_hamiltonians(geometry, periodic=False)
    old_kinetic, old_contact = two_cell.build_hamiltonians()
    old_indices = tuple(
        sum(
            ((mask >> mode) & 1) << (geometry.mode_count - 1 - mode)
            for mode in range(geometry.mode_count)
        )
        for mask in geometry.masks
    )
    old_kinetic = old_kinetic[np.ix_(old_indices, old_indices)]
    old_contact = old_contact[np.ix_(old_indices, old_indices)]
    matrix_error = max(
        float(np.max(np.abs(kinetic - old_kinetic))),
        float(np.max(np.abs(contact - old_contact))),
    )
    site = transformed_components(
        geometry, kinetic, contact, np.eye(2, dtype=complex)
    )
    momentum = transformed_components(
        geometry, kinetic, contact, kinetic_basis
    )
    expected_site = np.asarray((160.0, 0.0, 0.0))
    expected_momentum = np.asarray((0.0, 1704.0, 0.0))
    component_error = max(
        float(np.max(np.abs(np.asarray(site) - expected_site))),
        float(np.max(np.abs(np.asarray(momentum) - expected_momentum))),
    )
    stationary = stationary_diagnostic(
        geometry, kinetic, contact, math.sqrt(20.0 / 213.0), kinetic_basis
    )
    expected_stationary = {
        "gap": 0.6781098929961402,
        "contrast_mode": 2.0073177992767834,
        "contrast_number_accessible": 0.800292623385306,
        "contrast_parity_accessible": 1.1624926813828704,
    }
    stationary_error = max(
        abs(stationary[name] - expected)
        for name, expected in expected_stationary.items()
    )
    audit = geometry.projection_audit()
    if matrix_error > 1e-10 or component_error > 1e-8 or stationary_error > 1e-10:
        raise AssertionError("generalized implementation does not reproduce L=2")
    if max(audit.values()) > 1e-8 or geometry.local_subspace_dimension != 135:
        raise AssertionError("generalized L=2 local projection failed")
    return {
        "matrix_error": matrix_error,
        "component_error": component_error,
        "stationary_error": stationary_error,
        "projection_error": max(audit.values()),
        "local_subspace_dimension": float(geometry.local_subspace_dimension),
    }


def representation_audit(
    geometry: FixedSectorGeometry, seed: int
) -> dict[str, float]:
    random = np.random.default_rng(seed)
    first = haar_unitary(geometry.cell_count, random)
    second = haar_unitary(geometry.cell_count, random)
    first_lift = geometry.lifted_cell_unitary(first)
    second_lift = geometry.lifted_cell_unitary(second)
    product_lift = geometry.lifted_cell_unitary(first @ second)
    representation_error = float(
        np.max(np.abs(product_lift - first_lift @ second_lift))
    )

    _, _, alpha = two_cell.dirac_matrices()
    cell_matrix = random.normal(size=(geometry.cell_count, geometry.cell_count))
    cell_matrix = cell_matrix + 1j * random.normal(
        size=(geometry.cell_count, geometry.cell_count)
    )
    cell_matrix = 0.5 * (cell_matrix + cell_matrix.conj().T)
    one_particle = np.kron(cell_matrix, alpha[0])
    transformed_one_particle = (
        np.kron(first, np.eye(SPINOR_DIMENSION)).conj().T
        @ one_particle
        @ np.kron(first, np.eye(SPINOR_DIMENSION))
    )
    covariance_left = second_quantized_one_body(
        geometry, transformed_one_particle
    )
    covariance_right = first_lift.conj().T @ second_quantized_one_body(
        geometry, one_particle
    ) @ first_lift
    covariance_error = float(
        np.max(np.abs(covariance_left - covariance_right))
    )
    return {
        "representation": representation_error,
        "one_body_covariance": covariance_error,
    }


def evaluate_boundary(
    periodic: bool,
    particle_number: int,
    random_samples: int,
    optimization_starts: int,
    max_iterations: int,
    seed: int,
) -> dict[str, object]:
    label = "periodic" if periodic else "open"
    started = time.perf_counter()
    geometry = FixedSectorGeometry(3, particle_number)
    built_geometry = time.perf_counter()
    kinetic, contact, density, kinetic_basis = build_hamiltonians(geometry, periodic)
    built_operators = time.perf_counter()
    hermiticity_error = max(
        float(np.max(np.abs(kinetic - kinetic.conj().T))),
        float(np.max(np.abs(contact - contact.conj().T))),
        float(np.max(np.abs(density - density.conj().T))),
    )
    unitary_error = float(
        np.max(
            np.abs(
                geometry.lifted_cell_unitary(kinetic_basis).conj().T
                @ geometry.lifted_cell_unitary(kinetic_basis)
                - np.eye(geometry.dimension)
            )
        )
    )
    projection_audit = geometry.projection_audit(seed)
    lift_audit = representation_audit(geometry, seed + 31)
    if hermiticity_error > 1e-10 or unitary_error > 1e-10:
        raise AssertionError(f"{label} operator/unitary audit failed")
    if max(projection_audit.values()) > 1e-8 or max(lift_audit.values()) > 1e-8:
        raise AssertionError(f"{label} local projection audit failed")

    identity = np.eye(3, dtype=complex)
    site = transformed_components(geometry, kinetic, contact, identity)
    momentum = transformed_components(
        geometry, kinetic, contact, kinetic_basis
    )
    if site[0] <= 1e-10 or momentum[1] <= 1e-10:
        raise AssertionError(f"{label} endpoint competition is undefined")
    coupling = math.sqrt(site[0] / momentum[1])
    hamiltonian = kinetic + coupling * contact
    objective = SelectorObjective(geometry, hamiltonian)
    site_cost = objective(identity)
    momentum_cost = objective(kinetic_basis)
    endpoint_cost = 0.5 * (site_cost + momentum_cost)
    endpoint_mismatch = abs(site_cost - momentum_cost)

    generators = off_diagonal_generators(3)
    site_hessian = numerical_hessian(objective, identity, generators, 8e-4)
    momentum_hessian = numerical_hessian(
        objective, kinetic_basis, generators, 8e-4
    )
    site_hessian_eigenvalues = np.linalg.eigvalsh(site_hessian)
    momentum_hessian_eigenvalues = np.linalg.eigvalsh(momentum_hessian)

    random = np.random.default_rng(seed + (1 if periodic else 0))
    phase = np.diag(np.exp(1j * random.uniform(0.0, 2.0 * np.pi, 3)))
    permutation = np.eye(3, dtype=complex)[:, random.permutation(3)]
    invariance_error = max(
        abs(objective(identity @ phase) - site_cost),
        abs(objective(identity @ permutation) - site_cost),
    )
    invariance_random = np.random.default_rng(seed + 700 + int(periodic))
    for _ in range(8):
        unitary = haar_unitary(3, invariance_random)
        phase = np.diag(
            np.exp(1j * invariance_random.uniform(0.0, 2.0 * np.pi, 3))
        )
        permutation = np.eye(3, dtype=complex)[
            :, invariance_random.permutation(3)
        ]
        base_cost = objective(unitary)
        invariance_error = max(
            invariance_error,
            abs(objective(unitary @ phase) - base_cost),
            abs(objective(unitary @ permutation) - base_cost),
        )
    random_results = []
    random_unitaries = []
    for _ in range(random_samples):
        unitary = haar_unitary(3, random)
        random_unitaries.append(unitary)
        random_results.append(objective(unitary))
    smallest_random = min(random_results) if random_results else float("inf")

    starts = [identity, kinetic_basis]
    starts.extend(random_unitaries[:optimization_starts])
    optimized = []
    for initial in starts:
        value, unitary, iterations, gradient_norm = optimize_unitary(
            objective,
            initial,
            generators,
            max_iterations,
        )
        optimized.append(
            {
                "cost": value,
                "iterations": iterations,
                "gradient_norm": gradient_norm,
                "site_overlap": best_decomposition_overlap(identity, unitary),
                "momentum_overlap": best_decomposition_overlap(
                    kinetic_basis, unitary
                ),
            }
        )
    smallest_optimized = min(item["cost"] for item in optimized)
    stationary = stationary_diagnostic(
        geometry, kinetic, contact, coupling, kinetic_basis
    )

    density_site = transformed_components(geometry, kinetic, density, identity)
    density_momentum = transformed_components(
        geometry, kinetic, density, kinetic_basis
    )

    tolerance = 2e-6
    strict_endpoints = (
        float(np.min(site_hessian_eigenvalues)) > tolerance
        and float(np.min(momentum_hessian_eigenvalues)) > tolerance
    )
    no_lower_candidate = (
        smallest_random >= endpoint_cost - tolerance
        and smallest_optimized >= endpoint_cost - tolerance
    )
    stationary_gate = (
        stationary["gap"] > 1e-8
        and stationary["residual"] < 1e-8
        and stationary["contrast_mode"] > tolerance
        and stationary["contrast_number_accessible"] > tolerance
        and stationary["contrast_parity_accessible"] > tolerance
    )
    selector_gate = (
        endpoint_mismatch < tolerance
        and invariance_error < tolerance
        and strict_endpoints
        and no_lower_candidate
    )
    passed = selector_gate and stationary_gate
    finished = time.perf_counter()
    return {
        "label": label,
        "particle_number": particle_number,
        "geometry": geometry,
        "coupling": coupling,
        "site_components": site,
        "momentum_components": momentum,
        "endpoint_cost": endpoint_cost,
        "endpoint_mismatch": endpoint_mismatch,
        "site_hessian_eigenvalues": site_hessian_eigenvalues,
        "momentum_hessian_eigenvalues": momentum_hessian_eigenvalues,
        "invariance_error": invariance_error,
        "smallest_random": smallest_random,
        "smallest_optimized": smallest_optimized,
        "optimized": optimized,
        "stationary": stationary,
        "density_site_components": density_site,
        "density_momentum_components": density_momentum,
        "passed": passed,
        "selector_gate": selector_gate,
        "strict_endpoints": strict_endpoints,
        "no_lower_candidate": no_lower_candidate,
        "stationary_gate": stationary_gate,
        "timing": {
            "geometry": built_geometry - started,
            "operators": built_operators - built_geometry,
            "analysis": finished - built_operators,
            "total": finished - started,
            "objective_evaluations": objective.evaluations,
            "objective_seconds": objective.elapsed,
        },
        "audits": {
            "hermiticity": hermiticity_error,
            "unitarity": unitary_error,
            **projection_audit,
            **lift_audit,
        },
    }


def print_boundary(result: dict[str, object]) -> None:
    geometry = result["geometry"]
    assert isinstance(geometry, FixedSectorGeometry)
    print(f"\nTHREE-CELL {str(result['label']).upper()} GATE")
    print("  particle number", result["particle_number"])
    print("  sector dimension", geometry.dimension)
    print("  local-subspace dimension", geometry.local_subspace_dimension)
    print("  coupling", result["coupling"])
    print("  site components", result["site_components"])
    print("  momentum components", result["momentum_components"])
    print("  normalized endpoint cost", result["endpoint_cost"])
    print("  endpoint mismatch", result["endpoint_mismatch"])
    print("  site Hessian eigenvalues", result["site_hessian_eigenvalues"])
    print("  momentum Hessian eigenvalues", result["momentum_hessian_eigenvalues"])
    print("  phase/permutation invariance error", result["invariance_error"])
    print("  smallest random cost", result["smallest_random"])
    print("  smallest optimized cost", result["smallest_optimized"])
    print("  optimized runs")
    for item in result["optimized"]:
        print("   ", item)
    print("  stationary diagnostic")
    for name, value in result["stationary"].items():
        print(f"    {name}: {value:.15g}")
    print("  non-EC density endpoint components")
    print("    site", result["density_site_components"])
    print("    momentum", result["density_momentum_components"])
    print("  audits", result["audits"])
    print("  timing", result["timing"])
    print("  strict endpoint gate", result["strict_endpoints"])
    print("  no-lower-candidate gate", result["no_lower_candidate"])
    print("  selector gate", result["selector_gate"])
    print("  stationary contrast gate", result["stationary_gate"])
    print(
        "  RESTRICTED NUMERICAL VERDICT",
        "PASS" if result["passed"] else "FAIL",
    )


def classify(open_result: dict[str, object], periodic_result: dict[str, object]) -> str:
    open_selector = bool(open_result["selector_gate"])
    periodic_selector = bool(periodic_result["selector_gate"])
    open_stationary = bool(open_result["stationary_gate"])
    periodic_stationary = bool(periodic_result["stationary_gate"])
    if open_selector and periodic_selector and open_stationary and periodic_stationary:
        return (
            "PASS: the predeclared half-filled three-cell gate survives both "
            "tested boundary conditions; proceed to broader fillings and controls."
        )
    if not open_selector and not periodic_selector:
        return (
            "STRUCTURAL SELECTOR FAILURE: both open and periodic selector gates fail; "
            "retire this selector unless the failure is traced to an implementation "
            "or definition error. Do not run four cells as an untargeted rescue."
        )
    if open_selector != periodic_selector:
        passing_stationary = periodic_stationary if periodic_selector else open_stationary
        stationary_text = (
            "The passing selector also passes the isolated-state gate."
            if passing_stationary
            else "The passing selector still fails the isolated-state gate."
        )
        return (
            "BOUNDARY-INDEPENDENT ROBUSTNESS FAILURE: exactly one three-cell "
            f"boundary condition passes the restricted numerical gate. {stationary_text} "
            "A four-cell or analytic large-size calculation would be required to "
            "adjudicate the boundary/odd-lattice dependence; neither is performed here."
        )
    if not open_stationary and not periodic_stationary:
        return (
            "STATIONARY-STATE FAILURE: both selector gates pass, but neither has "
            "the required isolated stationary state."
        )
    return (
        "BOUNDARY-SENSITIVE STATIONARY STATE: both selector gates pass, but the "
        "isolated-state gate depends on the boundary condition."
    )


def run(
    particle_number: int,
    boundary: str,
    extended_controls: bool,
    random_samples: int,
    optimization_starts: int,
    max_iterations: int,
    seed: int,
) -> None:
    total_started = time.perf_counter()
    reproduction = reproduce_two_cell()
    print("TWO-CELL REPRODUCTION")
    for name, value in reproduction.items():
        print(f"  {name}: {value:.15g}")

    rank_audit = exact_local_rank_audit()
    print("\nTHREE-CELL EXACT LOCAL-RANK AUDIT")
    for name, value in rank_audit.items():
        print(f"  {name}: {value}")

    results = {}
    for periodic in (
        (False, True) if boundary == "both" else (boundary == "periodic",)
    ):
        result = evaluate_boundary(
            periodic,
            particle_number,
            random_samples,
            optimization_starts,
            max_iterations,
            seed,
        )
        results["periodic" if periodic else "open"] = result
        print_boundary(result)
    if boundary == "both":
        print("\nFINAL THREE-CELL CLASSIFICATION")
        print(" ", classify(results["open"], results["periodic"]))
    if extended_controls:
        print("\nPERIODIC FILLING CONTROLS")
        filling_result = filling_controls(seed + 101)
        print(
            "  maximum normalized-landscape spread",
            filling_result["maximum_landscape_spread"],
        )
        for row in filling_result["rows"]:
            print(" ", row)
        print("\nNON-EC DENSITY CONTROLS")
        for row in density_controls(seed + 202):
            print(" ", row)
    print("  total wall time", time.perf_counter() - total_started)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--particle-number", type=int, default=6)
    parser.add_argument(
        "--boundary", choices=("both", "open", "periodic"), default="both"
    )
    parser.add_argument("--skip-extended-controls", action="store_true")
    parser.add_argument("--random-samples", type=int, default=12)
    parser.add_argument("--optimization-starts", type=int, default=4)
    parser.add_argument("--max-iterations", type=int, default=24)
    parser.add_argument("--seed", type=int, default=20260718)
    arguments = parser.parse_args()
    run(
        arguments.particle_number,
        arguments.boundary,
        not arguments.skip_extended_controls,
        arguments.random_samples,
        arguments.optimization_starts,
        arguments.max_iterations,
        arguments.seed,
    )


if __name__ == "__main__":
    main()
