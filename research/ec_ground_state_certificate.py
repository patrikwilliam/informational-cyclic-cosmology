#!/usr/bin/env python3
"""Exact spectral certificate for the critical two-cell EC/CAR model.

The matrix of 3 H_c is constructed directly from exact Gaussian-integer CAR
data in a simultaneous chirality/spin basis.  An exact Fock-basis phase gauge
then makes it a real integer symmetric matrix.  The spectral calculations use
only Python integers and fractions.Fraction.  A separate floating-point
cross-check verifies agreement with the companion numerical implementation.

The certificate proves that the critical Hamiltonian has a unique ground state
and gives a rigorous lower bound on its gap.  Entropy values are checked in the
companion numerical script and are not certified here.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from typing import TypeAlias

import numpy as np

import ec_axial_selector_analysis as model


CHIRALITY_LABELS = (-1, -1, 1, 1)
SPIN_X_LABELS = (-1, 1, -1, 1)

GaussianInteger: TypeAlias = tuple[int, int]
SparseMatrix: TypeAlias = dict[tuple[int, int], GaussianInteger]

ZERO = (0, 0)
ONE = (1, 0)
I = (0, 1)


def gaussian_add(left: GaussianInteger, right: GaussianInteger) -> GaussianInteger:
    return left[0] + right[0], left[1] + right[1]


def gaussian_multiply(
    left: GaussianInteger, right: GaussianInteger
) -> GaussianInteger:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def gaussian_conjugate(value: GaussianInteger) -> GaussianInteger:
    return value[0], -value[1]


def add_entry(
    matrix: SparseMatrix,
    row: int,
    column: int,
    value: GaussianInteger,
) -> None:
    updated = gaussian_add(matrix.get((row, column), ZERO), value)
    if updated == ZERO:
        matrix.pop((row, column), None)
    else:
        matrix[row, column] = updated


def sparse_scale(matrix: SparseMatrix, scalar: GaussianInteger) -> SparseMatrix:
    result: SparseMatrix = {}
    for (row, column), value in matrix.items():
        add_entry(result, row, column, gaussian_multiply(scalar, value))
    return result


def sparse_sum(*matrices: SparseMatrix) -> SparseMatrix:
    result: SparseMatrix = {}
    for matrix in matrices:
        for (row, column), value in matrix.items():
            add_entry(result, row, column, value)
    return result


def sparse_adjoint(matrix: SparseMatrix) -> SparseMatrix:
    return {
        (column, row): gaussian_conjugate(value)
        for (row, column), value in matrix.items()
    }


def sparse_multiply(left: SparseMatrix, right: SparseMatrix) -> SparseMatrix:
    right_rows: dict[int, list[tuple[int, GaussianInteger]]] = defaultdict(list)
    for (row, column), value in right.items():
        right_rows[row].append((column, value))

    result: SparseMatrix = {}
    for (row, inner), left_value in left.items():
        for column, right_value in right_rows.get(inner, []):
            add_entry(
                result,
                row,
                column,
                gaussian_multiply(left_value, right_value),
            )
    return result


def apply_annihilation(state: int, mode: int) -> tuple[int, int] | None:
    bit = model.MODE_COUNT - 1 - mode
    if not (state >> bit) & 1:
        return None
    occupied_before = sum(
        (state >> (model.MODE_COUNT - 1 - earlier)) & 1
        for earlier in range(mode)
    )
    return state & ~(1 << bit), -1 if occupied_before % 2 else 1


def apply_creation(state: int, mode: int) -> tuple[int, int] | None:
    bit = model.MODE_COUNT - 1 - mode
    if (state >> bit) & 1:
        return None
    occupied_before = sum(
        (state >> (model.MODE_COUNT - 1 - earlier)) & 1
        for earlier in range(mode)
    )
    return state | (1 << bit), -1 if occupied_before % 2 else 1


def exact_bilinear(
    internal_matrix: tuple[tuple[GaussianInteger, ...], ...],
    left_cell: int,
    right_cell: int,
) -> SparseMatrix:
    """Return psi_left^dagger M psi_right using exact CAR signs."""

    result: SparseMatrix = {}
    for source in range(model.FOCK_DIMENSION):
        for column in range(model.SPINOR_DIMENSION):
            annihilated = apply_annihilation(
                source, right_cell * model.SPINOR_DIMENSION + column
            )
            if annihilated is None:
                continue
            intermediate, annihilation_sign = annihilated
            for row in range(model.SPINOR_DIMENSION):
                coefficient = internal_matrix[row][column]
                if coefficient == ZERO:
                    continue
                created = apply_creation(
                    intermediate, left_cell * model.SPINOR_DIMENSION + row
                )
                if created is None:
                    continue
                target, creation_sign = created
                sign = annihilation_sign * creation_sign
                add_entry(
                    result,
                    target,
                    source,
                    sparse_scale_value(coefficient, sign),
                )
    return result


def sparse_scale_value(value: GaussianInteger, scalar: int) -> GaussianInteger:
    return value[0] * scalar, value[1] * scalar


def diagonal_internal(*values: int) -> tuple[tuple[GaussianInteger, ...], ...]:
    return tuple(
        tuple((values[row], 0) if row == column else ZERO for column in range(4))
        for row in range(4)
    )


def exact_internal_matrices() -> tuple[
    tuple[tuple[GaussianInteger, ...], ...],
    tuple[tuple[tuple[GaussianInteger, ...], ...], ...],
]:
    """Return alpha^1 and J_5 matrices in the exact certificate basis."""

    alpha_1 = diagonal_internal(1, -1, -1, 1)
    gamma_5 = diagonal_internal(-1, -1, 1, 1)
    alpha_1_gamma_5 = diagonal_internal(-1, 1, -1, 1)
    alpha_2_gamma_5 = (
        (ZERO, (0, -1), ZERO, ZERO),
        ((0, 1), ZERO, ZERO, ZERO),
        (ZERO, ZERO, ZERO, (0, -1)),
        (ZERO, ZERO, (0, 1), ZERO),
    )
    alpha_3_gamma_5 = (
        (ZERO, ONE, ZERO, ZERO),
        (ONE, ZERO, ZERO, ZERO),
        (ZERO, ZERO, ZERO, ONE),
        (ZERO, ZERO, ONE, ZERO),
    )
    return alpha_1, (
        gamma_5,
        alpha_1_gamma_5,
        alpha_2_gamma_5,
        alpha_3_gamma_5,
    )


def simultaneous_internal_basis() -> np.ndarray:
    """Floating copy of the exact basis, used only for an implementation check."""

    columns = []
    for chirality, spin_x in zip(CHIRALITY_LABELS, SPIN_X_LABELS):
        columns.append(
            np.array(
                [1, spin_x, chirality, chirality * spin_x],
                dtype=float,
            )
            / 2.0
        )
    return np.column_stack(columns).astype(complex)


def exact_integer_critical_matrix() -> list[list[int]]:
    """Return the exact integer matrix unitarily equivalent to 3(K+Q/3)."""

    alpha_1, axial_matrices = exact_internal_matrices()
    identity_4 = diagonal_internal(1, 1, 1, 1)

    forward = exact_bilinear(alpha_1, 0, 1)
    kinetic = sparse_scale(
        sparse_sum(forward, sparse_scale(sparse_adjoint(forward), (-1, 0))),
        (0, -1),
    )

    contact: SparseMatrix = {}
    for cell in range(model.CELL_COUNT):
        number = exact_bilinear(identity_4, cell, cell)
        normal_squares = []
        for axial_matrix in axial_matrices:
            current = exact_bilinear(axial_matrix, cell, cell)
            normal_squares.append(
                sparse_sum(
                    sparse_multiply(current, current),
                    sparse_scale(number, (-1, 0)),
                )
            )
        contact = sparse_sum(
            contact,
            normal_squares[0],
            *(sparse_scale(term, (-1, 0)) for term in normal_squares[1:]),
        )

    critical = sparse_sum(sparse_scale(kinetic, (3, 0)), contact)
    phases = []
    powers_of_i = (ONE, I, (-1, 0), (0, -1))
    for basis_index in range(model.FOCK_DIMENSION):
        second_cell_particles = sum(
            (basis_index >> (model.MODE_COUNT - 1 - mode)) & 1
            for mode in range(model.SPINOR_DIMENSION, model.MODE_COUNT)
        )
        phases.append(powers_of_i[second_cell_particles % 4])

    gauged: SparseMatrix = {}
    for (row, column), value in critical.items():
        transformed = gaussian_multiply(
            gaussian_conjugate(phases[row]),
            gaussian_multiply(value, phases[column]),
        )
        if transformed[1] != 0:
            raise AssertionError("exact critical matrix did not become real")
        add_entry(gauged, row, column, transformed)

    return [
        [gauged.get((row, column), ZERO)[0] for column in range(model.FOCK_DIMENSION)]
        for row in range(model.FOCK_DIMENSION)
    ]


def numerical_model_equivalence_error(matrix: list[list[int]]) -> float:
    """Cross-check the exact construction against the companion NumPy model."""

    kinetic, contact = model.build_hamiltonians()
    internal = simultaneous_internal_basis()
    one_particle = np.kron(np.eye(model.CELL_COUNT), internal)
    fock_unitary = model.fock_lift(one_particle)
    transformed = fock_unitary.conj().T @ (3.0 * kinetic + contact) @ fock_unitary

    phases = []
    for basis_index in range(model.FOCK_DIMENSION):
        second_cell_particles = sum(
            (basis_index >> (model.MODE_COUNT - 1 - mode)) & 1
            for mode in range(model.SPINOR_DIMENSION, model.MODE_COUNT)
        )
        phases.append(1j**second_cell_particles)
    gauge = np.diag(phases)
    real_form = gauge.conj().T @ transformed @ gauge
    return float(np.max(np.abs(real_form - np.asarray(matrix, dtype=float))))


def occupation_labels(basis_index: int) -> tuple[int, int, int]:
    occupations = [
        (basis_index >> (model.MODE_COUNT - 1 - mode)) & 1
        for mode in range(model.MODE_COUNT)
    ]
    particle_number = sum(occupations)
    chirality = sum(
        occupations[mode] * CHIRALITY_LABELS[mode % model.SPINOR_DIMENSION]
        for mode in range(model.MODE_COUNT)
    )
    spin_x = sum(
        occupations[mode] * SPIN_X_LABELS[mode % model.SPINOR_DIMENSION]
        for mode in range(model.MODE_COUNT)
    )
    return particle_number, chirality, spin_x


def conserved_blocks() -> dict[tuple[int, int, int], list[int]]:
    result: dict[tuple[int, int, int], list[int]] = defaultdict(list)
    for basis_index in range(model.FOCK_DIMENSION):
        result[occupation_labels(basis_index)].append(basis_index)
    return dict(result)


def submatrix(matrix: list[list[int]], indices: list[int]) -> list[list[int]]:
    return [[matrix[row][column] for column in indices] for row in indices]


def exact_inertia_without_pivoting(
    matrix: list[list[int]],
    diagonal_shift: Fraction,
) -> tuple[int, int, int]:
    """Return inertia of matrix + shift I using exact LDL^T elimination."""

    dimension = len(matrix)
    lower = [
        [Fraction(0) for _ in range(dimension)] for _ in range(dimension)
    ]
    diagonal: list[Fraction] = []
    for column in range(dimension):
        pivot = Fraction(matrix[column][column]) + diagonal_shift
        pivot -= sum(
            lower[column][earlier] ** 2 * diagonal[earlier]
            for earlier in range(column)
        )
        if pivot == 0:
            raise ArithmeticError("zero LDL pivot; a symmetric pivot is required")
        diagonal.append(pivot)
        lower[column][column] = 1
        for row in range(column + 1, dimension):
            numerator = Fraction(matrix[row][column])
            numerator -= sum(
                lower[row][earlier]
                * lower[column][earlier]
                * diagonal[earlier]
                for earlier in range(column)
            )
            lower[row][column] = numerator / pivot
    return (
        sum(value < 0 for value in diagonal),
        sum(value == 0 for value in diagonal),
        sum(value > 0 for value in diagonal),
    )


def polynomial_divide(
    dividend: list[int], divisor: list[int]
) -> tuple[list[int], list[int]]:
    """Divide descending integer coefficients by a monic divisor."""

    remainder = dividend[:]
    quotient = []
    steps = len(dividend) - len(divisor) + 1
    for index in range(steps):
        coefficient = remainder[index]
        quotient.append(coefficient)
        for offset, divisor_coefficient in enumerate(divisor):
            remainder[index + offset] -= coefficient * divisor_coefficient
    return quotient, remainder[steps:]


def characteristic_polynomial(matrix: list[list[int]]) -> list[int]:
    """Return descending coefficients using exact Newton identities."""

    dimension = len(matrix)

    def multiply(
        left: list[list[int]], right: list[list[int]]
    ) -> list[list[int]]:
        return [
            [
                sum(
                    left[row][inner] * right[inner][column]
                    for inner in range(dimension)
                )
                for column in range(dimension)
            ]
            for row in range(dimension)
        ]

    power = [row[:] for row in matrix]
    traces = []
    for exponent in range(1, dimension + 1):
        traces.append(sum(power[index][index] for index in range(dimension)))
        if exponent < dimension:
            power = multiply(power, matrix)

    coefficients = [1]
    for degree in range(1, dimension + 1):
        numerator = sum(
            coefficients[degree - exponent] * traces[exponent - 1]
            for exponent in range(1, degree + 1)
        )
        if numerator % degree:
            raise ArithmeticError("Newton identity failed to produce an integer")
        coefficients.append(-numerator // degree)
    return coefficients


def quartic_value(argument: Fraction) -> Fraction:
    return (
        argument**4
        - 20 * argument**3
        - 144 * argument**2
        + 3008 * argument
        - 1792
    )


def run_certificate() -> None:
    matrix = exact_integer_critical_matrix()
    equivalence_error = numerical_model_equivalence_error(matrix)
    if equivalence_error > 1e-10:
        raise AssertionError("exact and numerical Hamiltonian constructions disagree")
    blocks = conserved_blocks()
    if max(map(len, blocks.values())) != 18:
        raise AssertionError("unexpected conserved-block dimensions")
    if any(
        matrix[row][column] != matrix[column][row]
        for row in range(model.FOCK_DIMENSION)
        for column in range(model.FOCK_DIMENSION)
    ):
        raise AssertionError("critical integer matrix is not symmetric")
    labels_by_index = [
        occupation_labels(index) for index in range(model.FOCK_DIMENSION)
    ]
    if any(
        matrix[row][column] != 0
        for row in range(model.FOCK_DIMENSION)
        for column in range(model.FOCK_DIMENSION)
        if labels_by_index[row] != labels_by_index[column]
    ):
        raise AssertionError("claimed conserved sectors are not block diagonal")

    total_below_minus_ten_and_half = 0
    negative_blocks = []
    for labels, indices in blocks.items():
        inertia = exact_inertia_without_pivoting(
            submatrix(matrix, indices), Fraction(21, 2)
        )
        total_below_minus_ten_and_half += inertia[0]
        if inertia[0]:
            negative_blocks.append((labels, inertia))

    if total_below_minus_ten_and_half != 1:
        raise AssertionError("critical Hamiltonian did not have one low eigenvalue")
    if negative_blocks != [((4, 0, 0), (1, 0, 17))]:
        raise AssertionError("the low eigenvalue moved to an unexpected block")

    ground_indices = blocks[(4, 0, 0)]
    ground_block = submatrix(matrix, ground_indices)
    quartic = [1, -20, -144, 3008, -1792]
    block_polynomial = characteristic_polynomial(ground_block)
    _, remainder = polynomial_divide(block_polynomial, quartic)
    if any(remainder):
        raise AssertionError("ground-state quartic was not a spectral factor")

    lower = Fraction(-12347, 1000)
    upper = Fraction(-6173, 500)
    lower_value = quartic_value(lower)
    upper_value = quartic_value(upper)
    if not (lower_value > 0 and upper_value < 0):
        raise AssertionError("quartic root was not bracketed")

    energy_lower = lower / 3
    energy_upper = upper / 3
    gap_lower_bound = (Fraction(-21, 2) - upper) / 3

    print("exact critical spectral certificate")
    print("  numerical implementation cross-check error", equivalence_error)
    print("  integer matrix dimension", len(matrix))
    print("  conserved blocks", len(blocks))
    print("  largest block dimension", max(map(len, blocks.values())))
    print("  blocks with eigenvalues below -10.5", negative_blocks)
    print("  ground-block spectral quartic", quartic)
    print("  quartic at lower endpoint", lower_value)
    print("  quartic at upper endpoint", upper_value)
    print("  ground eigenvalue of 3 H_c lies in", (lower, upper))
    print("  ground energy lies in", (energy_lower, energy_upper))
    print("  exact spectral-gap lower bound", gap_lower_bound)
    print("  decimal gap lower bound", float(gap_lower_bound))


if __name__ == "__main__":
    run_certificate()
