#!/usr/bin/env python3
"""Analytic closure of the four-cell transported-branch residual law.

The calculation classifies every nonzero, translation-invariant,
number-preserving onsite quartic contact in the declared L=4, N=8 model.  A
local contact is represented by a Hermitian operator q on the six-dimensional
pair space Lambda^2 C^4 and is repeated identically on all four cells.

The script checks finite matrix identities on a real orthonormal basis of
Herm(Lambda^2 C^4).  It is a bounded finite-CAR result, not a continuum or
cosmological statement.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from fractions import Fraction

import numpy as np

import ec_four_cell_boundary_phase as phase_gate
import ec_four_cell_selector as four
import ec_three_cell_selector as dense


CELL_COUNT = 4
PARTICLE_NUMBER = 8
INTERNAL_DIMENSION = 4
PAIR_DIMENSION = math.comb(INTERNAL_DIMENSION, 2)
CONTACT_DIMENSION = PAIR_DIMENSION**2
TOLERANCE = 2e-7


@dataclass(frozen=True)
class ClosureResult:
    kinetic_identity_error: float
    contact_identity_error: float
    cross_identity_error: float
    direct_branch_error: float
    commutator_error: float
    p_spectrum: tuple[tuple[Fraction, int], ...]
    r_spectrum: tuple[tuple[Fraction, int], ...]
    irrep_checks: tuple[
        tuple[str, Fraction, Fraction, Fraction, Fraction], ...
    ]


def hermitian_pair_basis() -> tuple[np.ndarray, ...]:
    """Real Hilbert-Schmidt orthonormal basis of Herm(C^6)."""

    result: list[np.ndarray] = []
    for row in range(PAIR_DIMENSION):
        matrix = np.zeros((PAIR_DIMENSION, PAIR_DIMENSION), dtype=complex)
        matrix[row, row] = 1.0
        result.append(matrix)
    for row in range(PAIR_DIMENSION):
        for column in range(row + 1, PAIR_DIMENSION):
            real = np.zeros((PAIR_DIMENSION, PAIR_DIMENSION), dtype=complex)
            real[row, column] = real[column, row] = 1.0 / math.sqrt(2.0)
            result.append(real)

            imaginary = np.zeros(
                (PAIR_DIMENSION, PAIR_DIMENSION), dtype=complex
            )
            imaginary[row, column] = -1j / math.sqrt(2.0)
            imaginary[column, row] = 1j / math.sqrt(2.0)
            result.append(imaginary)

    if len(result) != CONTACT_DIMENSION:
        raise AssertionError("Hermitian pair basis has the wrong dimension")
    gram = np.asarray(
        [
            [float(np.vdot(left, right).real) for right in result]
            for left in result
        ]
    )
    if np.max(np.abs(gram - np.eye(CONTACT_DIMENSION))) > 1e-13:
        raise AssertionError("Hermitian pair basis is not orthonormal")
    return tuple(result)


def onsite_contact(local_pair_matrix: np.ndarray) -> four.LowBodyOperator:
    """Repeat one Hermitian two-particle operator on every spatial cell."""

    if local_pair_matrix.shape != (PAIR_DIMENSION, PAIR_DIMENSION):
        raise ValueError("local pair matrix must be 6 by 6")
    if np.max(np.abs(local_pair_matrix - local_pair_matrix.conj().T)) > 1e-12:
        raise ValueError("local pair matrix must be Hermitian")

    mode_count = CELL_COUNT * INTERNAL_DIMENSION
    global_pairs = four.pair_basis(mode_count)
    pair_position = {pair: index for index, pair in enumerate(global_pairs)}
    local_pairs = four.pair_basis(INTERNAL_DIMENSION)
    global_matrix = np.zeros(
        (len(global_pairs), len(global_pairs)), dtype=complex
    )
    for cell in range(CELL_COUNT):
        offset = cell * INTERNAL_DIMENSION
        indices = tuple(
            pair_position[(offset + left, offset + right)]
            for left, right in local_pairs
        )
        global_matrix[np.ix_(indices, indices)] = local_pair_matrix
    return four.LowBodyOperator(
        np.zeros((mode_count, mode_count), dtype=complex), global_matrix
    )


def periodic_fourier_basis() -> np.ndarray:
    """Eigenbasis of the periodic current kinetic in ascending eigenvalue order."""

    momenta = (-math.pi / 2.0, 0.0, math.pi, math.pi / 2.0)
    basis = np.asarray(
        [
            [np.exp(1j * momentum * cell) / 2.0 for momentum in momenta]
            for cell in range(CELL_COUNT)
        ],
        dtype=complex,
    )
    kinetic = dense.cell_kinetic_matrix(CELL_COUNT, True)
    expected = np.diag((-2.0, 0.0, 0.0, 2.0))
    if np.max(np.abs(basis.conj().T @ basis - np.eye(CELL_COUNT))) > 1e-13:
        raise AssertionError("Fourier basis is not unitary")
    if np.max(np.abs(basis.conj().T @ kinetic @ basis - expected)) > 2e-13:
        raise AssertionError("Fourier basis does not diagonalize the kinetic")
    return basis


def zero_family_basis(beta: float, chi: float) -> np.ndarray:
    """Rotate only the k=0, pi zero eigenspace of the periodic kinetic."""

    rotation = np.eye(CELL_COUNT, dtype=complex)
    rotation[np.ix_((1, 2), (1, 2))] = four.zero_mode_unitary(beta, chi)
    return periodic_fourier_basis() @ rotation


def low_body_one_particle(cell_matrix: np.ndarray) -> four.LowBodyOperator:
    _, _, alpha = dense.two_cell.dirac_matrices()
    one_body = np.kron(cell_matrix, alpha[0])
    return four.LowBodyOperator(
        one_body,
        np.zeros((math.comb(one_body.shape[0], 2),) * 2, dtype=complex),
    )


def symmetric_cell_hopping() -> np.ndarray:
    result = np.zeros((CELL_COUNT, CELL_COUNT), dtype=complex)
    for cell in range(CELL_COUNT):
        neighbor = (cell + 1) % CELL_COUNT
        result[cell, neighbor] = 1.0
        result[neighbor, cell] = 1.0
    return result


def projection_quadratic_matrix(
    geometry: dense.FixedSectorGeometry,
    contacts: tuple[four.LowBodyOperator, ...],
    unitary: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    """Return contact overlaps and their projected-norm quadratic form."""

    overlaps = np.column_stack(
        [
            four.projection_overlaps(geometry, contact.transformed(unitary))
            for contact in contacts
        ]
    )
    matrix = np.real(
        overlaps.conj().T @ geometry.gram_pseudoinverse @ overlaps
    )
    return overlaps, (matrix + matrix.T) / 2.0


def residual_norm(
    geometry: dense.FixedSectorGeometry,
    operator: four.LowBodyOperator,
    unitary: np.ndarray,
) -> float:
    transformed = operator.transformed(unitary)
    overlap = four.projection_overlaps(geometry, transformed)
    projection = float(
        np.vdot(overlap, geometry.gram_pseudoinverse @ overlap).real
    )
    invariant = float(
        four.sector_inner_product(geometry, operator, operator).real
    )
    value = invariant - projection
    return 0.0 if abs(value) < 1e-8 else value


def rational_spectrum(
    matrix: np.ndarray,
    expected: tuple[tuple[Fraction, int], ...],
) -> tuple[tuple[Fraction, int], ...]:
    values = np.linalg.eigvalsh(matrix)
    cursor = 0
    for rational, multiplicity in expected:
        block = values[cursor : cursor + multiplicity]
        error = float(np.max(np.abs(block - float(rational))))
        if error > TOLERANCE:
            raise AssertionError(
                f"spectrum differs from {rational} with multiplicity "
                f"{multiplicity}: error={error}"
            )
        cursor += multiplicity
    if cursor != len(values):
        raise AssertionError("expected spectrum has the wrong dimension")
    return expected


def irrep_representatives() -> tuple[tuple[str, np.ndarray], ...]:
    """Normalized representatives of 1 + 15 + 20 in Herm(Lambda^2 C^4)."""

    scalar = np.eye(PAIR_DIMENSION, dtype=complex) / math.sqrt(PAIR_DIMENSION)
    adjoint = np.diag((0.0, 1.0, 1.0, -1.0, -1.0, 0.0)) / 2.0
    twenty = np.diag((1.0, -1.0, 0.0, 0.0, -1.0, 1.0)) / 2.0
    result = (("1", scalar), ("15", adjoint), ("20", twenty))
    for _, matrix in result:
        if abs(float(np.vdot(matrix, matrix).real) - 1.0) > 1e-13:
            raise AssertionError("irrep representative is not normalized")
    return result


def run(seed: int) -> ClosureResult:
    geometry = dense.FixedSectorGeometry(CELL_COUNT, PARTICLE_NUMBER)
    pair_basis = hermitian_pair_basis()
    contacts = tuple(onsite_contact(matrix) for matrix in pair_basis)

    kinetic_zero = low_body_one_particle(
        dense.cell_kinetic_matrix(CELL_COUNT, True)
    )
    symmetric = low_body_one_particle(symmetric_cell_hopping())
    site = np.eye(CELL_COUNT, dtype=complex)
    kinetic_residual = residual_norm(geometry, kinetic_zero, site)

    sample_orientations = (
        (0.0, 0.0),
        (math.pi / 4.0, 0.0),
        (math.pi / 2.0, 0.0),
        (math.pi / 3.0, math.pi / 5.0),
        (0.73 * math.pi, 0.37 * math.pi),
        (math.pi / 2.0, math.pi / 2.0),
    )

    matrices: dict[tuple[float, float], tuple[np.ndarray, np.ndarray]] = {}
    kinetic_identity_error = 0.0
    for beta, chi in sample_orientations:
        unitary = zero_family_basis(beta, chi)
        matrices[(beta, chi)] = projection_quadratic_matrix(
            geometry, contacts, unitary
        )
        symmetric_residual = residual_norm(geometry, symmetric, unitary)
        kinetic_identity_error = max(
            kinetic_identity_error,
            abs(
                symmetric_residual
                - kinetic_residual * math.sin(beta) ** 2
            ),
        )
        if residual_norm(geometry, kinetic_zero, unitary) > 2e-7:
            raise AssertionError("periodic kinetic is not local in its eigenbasis")

    zero_key = (0.0, 0.0)
    half_key = (math.pi / 4.0, 0.0)
    one_key = (math.pi / 2.0, 0.0)
    _, matrix_zero = matrices[zero_key]
    _, matrix_half = matrices[half_key]
    _, matrix_one = matrices[one_key]
    difference_half = matrix_half - matrix_zero
    difference_one = matrix_one - matrix_zero
    p_matrix = 4.0 * difference_half - difference_one
    r_matrix = 2.0 * difference_one - 4.0 * difference_half
    p_matrix = (p_matrix + p_matrix.T) / 2.0
    r_matrix = (r_matrix + r_matrix.T) / 2.0

    p_expected = (
        (Fraction(231, 4), 1),
        (Fraction(231, 2), 15),
        (Fraction(231, 1), 20),
    )
    r_expected = (
        (Fraction(231, 2), 20),
        (Fraction(539, 4), 15),
        (Fraction(693, 4), 1),
    )
    p_spectrum = rational_spectrum(p_matrix, p_expected)
    r_spectrum = rational_spectrum(r_matrix, r_expected)

    expected_irrep_data = {
        "1": (
            Fraction(14784, 5),
            Fraction(10857, 4),
            Fraction(231, 4),
            Fraction(693, 4),
        ),
        "15": (
            Fraction(10032, 1),
            Fraction(11473, 4),
            Fraction(231, 2),
            Fraction(539, 4),
        ),
        "20": (
            Fraction(3696, 1),
            Fraction(6237, 2),
            Fraction(231, 1),
            Fraction(231, 2),
        ),
    }
    irrep_checks = []
    balanced = zero_family_basis(math.pi / 2.0, 0.0)
    for label, local_matrix in irrep_representatives():
        contact = onsite_contact(local_matrix)
        invariant_norm = float(
            four.sector_inner_product(geometry, contact, contact).real
        )
        trace = four.sector_trace(geometry, contact)
        denominator = invariant_norm - abs(trace) ** 2 / geometry.dimension
        selected_residual = residual_norm(geometry, contact, balanced)
        coordinates = np.asarray(
            [float(np.vdot(item, local_matrix).real) for item in pair_basis]
        )
        p_value = float(coordinates @ p_matrix @ coordinates)
        r_value = float(coordinates @ r_matrix @ coordinates)
        expected_values = expected_irrep_data[label]
        actual_values = (denominator, selected_residual, p_value, r_value)
        if max(
            abs(actual - float(expected))
            for actual, expected in zip(actual_values, expected_values)
        ) > TOLERANCE:
            raise AssertionError(
                f"{label} irrep coefficient audit failed: {actual_values}"
            )
        irrep_checks.append((label, *expected_values))

    contact_identity_error = 0.0
    cross_identity_error = 0.0
    for beta, chi in sample_orientations:
        overlaps, matrix = matrices[(beta, chi)]
        x = math.sin(beta) ** 2 * math.cos(chi) ** 2
        predicted = matrix_zero + x * p_matrix + x**2 * r_matrix
        contact_identity_error = max(
            contact_identity_error, float(np.max(np.abs(matrix - predicted)))
        )

        symmetric_overlap = four.projection_overlaps(
            geometry, symmetric.transformed(zero_family_basis(beta, chi))
        )
        projected_crosses = np.real(
            symmetric_overlap.conj()
            @ geometry.gram_pseudoinverse
            @ overlaps
        )
        # Before projection, an inter-cell hop is orthogonal to every onsite
        # number-preserving contact because the latter preserves each cell's
        # occupation.  Hence these projected values are the negative residual
        # cross coefficients.
        cross_identity_error = max(
            cross_identity_error,
            float(np.max(np.abs(projected_crosses))),
        )

    # Extra seeded orientations test the matrix identities away from the points
    # used to reconstruct P and R.
    random = np.random.default_rng(seed)
    for _ in range(8):
        beta = float(random.uniform(0.0, math.pi))
        chi = float(random.uniform(0.0, 2.0 * math.pi))
        unitary = zero_family_basis(beta, chi)
        overlaps, matrix = projection_quadratic_matrix(
            geometry, contacts, unitary
        )
        x = math.sin(beta) ** 2 * math.cos(chi) ** 2
        predicted = matrix_zero + x * p_matrix + x**2 * r_matrix
        contact_identity_error = max(
            contact_identity_error, float(np.max(np.abs(matrix - predicted)))
        )
        symmetric_overlap = four.projection_overlaps(
            geometry, symmetric.transformed(unitary)
        )
        projected_crosses = np.real(
            symmetric_overlap.conj()
            @ geometry.gram_pseudoinverse
            @ overlaps
        )
        cross_identity_error = max(
            cross_identity_error,
            float(np.max(np.abs(projected_crosses))),
        )

    # The distributed gauge gives G^dagger K_phi G = cos(theta) K_0 +
    # sin(theta) S with theta=phi/4, while every onsite contact is gauge
    # invariant.  Validate that identity directly on representative phases.
    gauge_error = 0.0
    for phase in (0.0, math.pi / 16.0, math.pi / 3.0, math.pi):
        gauge = phase_gate.distributed_twist_gauge(phase)
        twisted = phase_gate.twisted_cell_kinetic(phase)
        theta = phase / CELL_COUNT
        expected = (
            math.cos(theta) * dense.cell_kinetic_matrix(CELL_COUNT, True)
            + math.sin(theta) * symmetric_cell_hopping()
        )
        gauge_error = max(
            gauge_error,
            float(np.max(np.abs(gauge.conj().T @ twisted @ gauge - expected))),
        )
    kinetic_identity_error = max(kinetic_identity_error, gauge_error)

    generic_coefficients = random.normal(size=CONTACT_DIMENSION)
    generic_coefficients /= np.linalg.norm(generic_coefficients)
    generic_local = sum(
        coefficient * matrix
        for coefficient, matrix in zip(generic_coefficients, pair_basis)
    )
    generic_contact = onsite_contact(generic_local)
    generic_statistics = four.invariant_statistics(
        geometry, kinetic_zero, generic_contact
    )
    generic_b = residual_norm(geometry, generic_contact, balanced)
    direct_branch_error = 0.0
    for phase in (0.0, math.pi / 16.0, math.pi / 3.0, math.pi):
        kinetic, _, _ = phase_gate.twisted_operators(phase, generic_contact)
        branch = phase_gate.transported_periodic_branch(balanced, phase)
        components = four.residual_components(
            geometry,
            generic_statistics,
            kinetic,
            generic_contact,
            branch,
        )
        expected = (
            kinetic_residual * math.sin(phase / CELL_COUNT) ** 2,
            generic_b,
            0.0,
        )
        direct_branch_error = max(
            direct_branch_error,
            max(abs(actual - target) for actual, target in zip(components, expected)),
        )

    commutator = p_matrix @ r_matrix - r_matrix @ p_matrix
    commutator_error = float(np.linalg.norm(commutator, ord=2))
    errors = {
        "kinetic identity": kinetic_identity_error,
        "contact identity": contact_identity_error,
        "cross identity": cross_identity_error,
        "direct branch": direct_branch_error,
        "P-R commutator": commutator_error,
    }
    if max(errors.values()) > TOLERANCE:
        raise AssertionError(f"onsite closure audit failed: {errors}")
    if np.min(np.linalg.eigvalsh(p_matrix)) <= 0.0:
        raise AssertionError("P is not positive definite")
    if np.min(np.linalg.eigvalsh(r_matrix)) <= 0.0:
        raise AssertionError("R is not positive definite")

    return ClosureResult(
        kinetic_identity_error=kinetic_identity_error,
        contact_identity_error=contact_identity_error,
        cross_identity_error=cross_identity_error,
        direct_branch_error=direct_branch_error,
        commutator_error=commutator_error,
        p_spectrum=p_spectrum,
        r_spectrum=r_spectrum,
        irrep_checks=tuple(irrep_checks),
    )


def format_spectrum(
    spectrum: tuple[tuple[Fraction, int], ...]
) -> str:
    return ", ".join(
        f"{value} (multiplicity {multiplicity})"
        for value, multiplicity in spectrum
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=2026081001)
    arguments = parser.parse_args()
    result = run(arguments.seed)

    print("four-cell onsite-contact closure")
    print("  contact space Herm(Lambda^2 C^4): real dimension", CONTACT_DIMENSION)
    print("  kinetic identity max error", result.kinetic_identity_error)
    print("  contact matrix identity max error", result.contact_identity_error)
    print("  residual cross max error", result.cross_identity_error)
    print("  direct generic-branch max error", result.direct_branch_error)
    print("  ||[P,R]||_2", result.commutator_error)
    print("  spectrum(P):", format_spectrum(result.p_spectrum))
    print("  spectrum(R):", format_spectrum(result.r_spectrum))
    print("  irrep coefficients (denominator, B, p, r):")
    for label, denominator, residual, p_value, r_value in result.irrep_checks:
        print(
            f"    {label}: {denominator}, {residual}, "
            f"{p_value}, {r_value}"
        )
    print("  P and R positive definite: True")
    print(
        "  classification: every nonzero Hermitian translation-invariant "
        "onsite quartic contact selects the balanced zero-mode decomposition"
    )
    print(
        "  branch law: R_branch(phi) = "
        "(A sin^2(phi/4), B, 0)"
    )
    print("  bounded finite-model closure: PASS")


if __name__ == "__main__":
    main()
