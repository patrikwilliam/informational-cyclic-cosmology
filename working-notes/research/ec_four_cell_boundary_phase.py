#!/usr/bin/env python3
"""Boundary-phase robustness gate for the four-cell EC-inspired selector.

The primary calculation holds the periodic coexistence coupling fixed and
audits the gauge-transported periodic branch on a prescribed boundary-twist
grid.  It uses the low-body fixed-sector implementation validated by
ec_four_cell_selector.py and never constructs a dense 12,870-dimensional
Hamiltonian.
"""

from __future__ import annotations

import argparse
import math
import time
from dataclasses import dataclass

import numpy as np

import ec_four_cell_selector as four
import ec_three_cell_selector as dense


PHASE_SUBDIVISIONS = 16
STATIONARITY_TOLERANCE = 1e-7
CURVATURE_TOLERANCE = 2e-5
DISTINCTNESS_TOLERANCE = 1e-6


@dataclass(frozen=True)
class BranchResult:
    unitary: np.ndarray
    cost: float
    gradient_norm: float
    hessian_minimum: float
    gradient_steps: dict[str, float]
    hessian_steps: dict[str, float]
    iterations: int
    newton_iterations: int

    @property
    def strict(self) -> bool:
        return (
            self.gradient_steps["maximum"] < STATIONARITY_TOLERANCE
            and self.hessian_minimum > CURVATURE_TOLERANCE
            and self.hessian_steps["minimum"] > CURVATURE_TOLERANCE
        )


def twisted_cell_kinetic(phase: float) -> np.ndarray:
    result = np.zeros((4, 4), dtype=complex)
    for cell in range(3):
        result[cell, cell + 1] = -1j
        result[cell + 1, cell] = 1j
    result[3, 0] = -1j * np.exp(1j * phase)
    result[0, 3] = 1j * np.exp(-1j * phase)
    if np.max(np.abs(result - result.conj().T)) > 1e-13:
        raise AssertionError("twisted kinetic matrix is not Hermitian")
    return result


def distributed_twist_gauge(phase: float) -> np.ndarray:
    """Gauge that distributes the closing-link phase uniformly over the ring."""

    return np.diag(np.exp(1j * np.arange(4) * phase / 4.0))


def transported_periodic_branch(
    periodic_representative: np.ndarray, phase: float
) -> np.ndarray:
    return distributed_twist_gauge(phase) @ periodic_representative


def twisted_operators(
    phase: float, contact: four.LowBodyOperator
) -> tuple[four.LowBodyOperator, np.ndarray, np.ndarray]:
    _, _, alpha = dense.two_cell.dirac_matrices()
    cell_kinetic = twisted_cell_kinetic(phase)
    one_body = np.kron(cell_kinetic, alpha[0])
    pair_count = math.comb(one_body.shape[0], 2)
    kinetic = four.LowBodyOperator(
        one_body,
        np.zeros((pair_count, pair_count), dtype=complex),
    )
    eigenvalues, eigenbasis = np.linalg.eigh(cell_kinetic)
    return kinetic, eigenvalues, eigenbasis


def degenerate_blocks(
    eigenvalues: np.ndarray, tolerance: float = 1e-9
) -> tuple[tuple[int, ...], ...]:
    blocks: list[list[int]] = []
    for index, value in enumerate(eigenvalues):
        if not blocks or abs(value - eigenvalues[blocks[-1][0]]) > tolerance:
            blocks.append([index])
        else:
            blocks[-1].append(index)
    return tuple(tuple(block) for block in blocks if len(block) > 1)


def objective_for(
    geometry: dense.FixedSectorGeometry,
    kinetic: four.LowBodyOperator,
    contact: four.LowBodyOperator,
    coupling: float,
) -> four.LowBodyObjective:
    statistics = four.invariant_statistics(geometry, kinetic, contact)
    hamiltonian = kinetic.scaled_add(contact, coupling)
    return four.LowBodyObjective(
        geometry,
        hamiltonian,
        statistics.norm(coupling),
        statistics.kinetic_trace + coupling * statistics.contact_trace,
    )


def audit_branch(
    objective: four.LowBodyObjective,
    unitary: np.ndarray,
    generators: tuple[np.ndarray, ...],
) -> BranchResult:
    gradient, gradient_steps = four.stationarity_step_audit(
        objective, unitary, generators
    )
    hessian, hessian_steps = four.hessian_step_audit(
        objective, unitary, generators
    )
    return BranchResult(
        unitary=unitary,
        cost=float(objective(unitary)),
        gradient_norm=float(np.linalg.norm(gradient)),
        hessian_minimum=float(np.min(np.linalg.eigvalsh(hessian))),
        gradient_steps=gradient_steps,
        hessian_steps=hessian_steps,
        iterations=0,
        newton_iterations=0,
    )


def refine_branch(
    objective: four.LowBodyObjective,
    initial: np.ndarray,
    generators: tuple[np.ndarray, ...],
    max_iterations: int,
) -> BranchResult:
    value, unitary, iterations, newton_iterations = optimize_stationary(
        objective, initial, generators, max_iterations
    )
    gradient, gradient_steps = four.stationarity_step_audit(
        objective, unitary, generators
    )
    hessian, hessian_steps = four.hessian_step_audit(
        objective, unitary, generators
    )
    return BranchResult(
        unitary=unitary,
        cost=float(value),
        gradient_norm=float(np.linalg.norm(gradient)),
        hessian_minimum=float(np.min(np.linalg.eigvalsh(hessian))),
        gradient_steps=gradient_steps,
        hessian_steps=hessian_steps,
        iterations=iterations,
        newton_iterations=newton_iterations,
    )


def optimize_stationary(
    objective: four.LowBodyObjective,
    initial: np.ndarray,
    generators: tuple[np.ndarray, ...],
    max_iterations: int,
) -> tuple[float, np.ndarray, int, int]:
    value, unitary, iterations, _ = dense.optimize_unitary(
        objective,
        initial,
        generators,
        max_iterations=max_iterations,
    )
    value = float(objective(unitary))
    newton_iterations = 0
    for newton_iterations in range(1, 9):
        gradient = four.numerical_gradient(
            objective, unitary, generators, 2e-5
        )
        if float(np.linalg.norm(gradient)) < 5e-10:
            newton_iterations -= 1
            break
        hessian = dense.numerical_hessian(
            objective, unitary, generators, 5e-4
        )
        if float(np.min(np.linalg.eigvalsh(hessian))) <= 1e-7:
            newton_iterations -= 1
            break
        displacement = -np.linalg.solve(hessian, gradient)
        displacement_norm = float(np.linalg.norm(displacement))
        if displacement_norm > 0.25:
            displacement *= 0.25 / displacement_norm
        direction = sum(
            displacement[index] * generator
            for index, generator in enumerate(generators)
        )
        accepted = False
        for scale in (1.0, 0.5, 0.25, 0.125, 0.0625):
            candidate = dense.unitary_chart(unitary, scale * direction)
            candidate_value = float(objective(candidate))
            if candidate_value < value:
                unitary = candidate
                value = candidate_value
                accepted = True
                break
        if not accepted:
            newton_iterations -= 1
            break
    return value, unitary, iterations, newton_iterations


def validate_twist_construction(contact: four.LowBodyOperator) -> dict[str, float]:
    periodic = dense.cell_kinetic_matrix(4, True)
    phase_zero = twisted_cell_kinetic(0.0)
    closure_error = float(np.max(np.abs(periodic - phase_zero)))
    cycle_error = float(
        np.max(np.abs(phase_zero - twisted_cell_kinetic(2.0 * math.pi)))
    )

    spectrum_error = 0.0
    distributed_gauge_error = 0.0
    reconstruction_error = 0.0
    contact_error = 0.0
    geometry = dense.FixedSectorGeometry(4, 3)
    _, _, alpha = dense.two_cell.dirac_matrices()
    for phase in (0.0, math.pi / 16.0, math.pi / 8.0, math.pi / 3.0, math.pi):
        cell_kinetic = twisted_cell_kinetic(phase)
        exact_spectrum = np.sort(
            np.asarray(
                [
                    2.0 * math.sin((phase + 2.0 * math.pi * mode) / 4.0)
                    for mode in range(4)
                ]
            )
        )
        spectrum_error = max(
            spectrum_error,
            float(
                np.max(
                    np.abs(np.linalg.eigvalsh(cell_kinetic) - exact_spectrum)
                )
            ),
        )
        gauge = distributed_twist_gauge(phase)
        gauged = gauge.conj().T @ cell_kinetic @ gauge
        uniform = np.zeros((4, 4), dtype=complex)
        for cell in range(4):
            uniform[cell, (cell + 1) % 4] = -1j * np.exp(1j * phase / 4.0)
            uniform[(cell + 1) % 4, cell] = 1j * np.exp(-1j * phase / 4.0)
        distributed_gauge_error = max(
            distributed_gauge_error,
            float(np.max(np.abs(gauged - uniform))),
        )
        kinetic, _, _ = twisted_operators(phase, contact)
        direct = dense.second_quantized_one_body(
            geometry, np.kron(twisted_cell_kinetic(phase), alpha[0])
        )
        reconstruction_error = max(
            reconstruction_error,
            float(
                np.max(
                    np.abs(four.fixed_sector_matrix(geometry, kinetic) - direct)
                )
            ),
        )
        contact_error = max(
            contact_error,
            float(
                np.max(
                    np.abs(
                        four.fixed_sector_matrix(geometry, contact)
                        - dense.axial_contact(geometry)
                    )
                )
            ),
        )
    result = {
        "periodic_closure": closure_error,
        "two_pi_cycle": cycle_error,
        "exact_spectrum": spectrum_error,
        "distributed_gauge": distributed_gauge_error,
        "kinetic_reconstruction": reconstruction_error,
        "contact_reconstruction": contact_error,
    }
    if max(result.values()) > 2e-10:
        raise AssertionError(f"twist validation failed: {result}")
    return result


def validate_half_filled_projection(seed: int) -> dict[str, float]:
    """Independent sparse N=8 check of the low-body partial-trace formulas."""

    geometry = dense.FixedSectorGeometry(4, 8)
    _, contact, _ = four.low_body_operators(4, True)
    kinetic, _, _ = twisted_operators(math.pi / 16.0, contact)
    random = np.random.default_rng(seed)
    unitary = dense.haar_unitary(4, random)
    operator = kinetic.scaled_add(contact, 0.4298279138553384).transformed(
        unitary
    )
    terms = four.sparse_terms(operator)
    actions = [
        four.apply_low_body(mask, operator, terms) for mask in geometry.masks
    ]
    direct_overlaps = np.asarray(
        [
            sum(
                actions[column].get(geometry.masks[row], 0.0j)
                for row, column in zip(rows, columns)
            )
            for rows, columns in geometry.unit_supports
        ]
    )
    formula_overlaps = four.projection_overlaps(geometry, operator)
    direct_norm = sum(
        sum(abs(value) ** 2 for value in action.values())
        for action in actions
    )
    direct_trace = sum(
        actions[index].get(mask, 0.0j)
        for index, mask in enumerate(geometry.masks)
    )
    result = {
        "projection_overlaps": float(
            np.max(np.abs(direct_overlaps - formula_overlaps))
        ),
        "sector_norm": float(
            abs(
                direct_norm
                - four.sector_inner_product(
                    geometry, operator, operator
                ).real
            )
        ),
        "sector_trace": float(
            abs(direct_trace - four.sector_trace(geometry, operator))
        ),
    }
    if (
        result["projection_overlaps"] > 1e-8
        or result["sector_norm"] > 1e-7
        or result["sector_trace"] > 1e-7
    ):
        raise AssertionError(f"half-filled sparse validation failed: {result}")
    return result


def scan_fixed_coupling(
    subdivisions: int,
    max_iterations: int,
    seed: int,
    max_index: int | None = None,
) -> dict[str, object]:
    del max_iterations, seed
    if subdivisions != PHASE_SUBDIVISIONS:
        raise ValueError(
            f"the declared gate requires subdivisions={PHASE_SUBDIVISIONS}"
        )
    geometry = dense.FixedSectorGeometry(4, 8)
    _, contact, _ = four.low_body_operators(4, True)
    validation = validate_twist_construction(contact)
    contact_statistics = four.invariant_statistics(
        geometry,
        four.LowBodyOperator(
            np.zeros_like(contact.one_body), np.zeros_like(contact.two_body)
        ),
        contact,
    )
    contact_objective = four.LowBodyObjective(
        geometry,
        contact,
        contact_statistics.contact_norm,
        contact_statistics.contact_trace,
    )
    generators = dense.off_diagonal_generators(4)
    identity = np.eye(4, dtype=complex)

    kinetic_zero, spectrum_zero, basis_zero = twisted_operators(0.0, contact)
    representative_zero, degeneracy_zero = four.periodic_kinetic_representative(
        contact_objective, basis_zero
    )
    statistics_zero = four.invariant_statistics(
        geometry, kinetic_zero, contact
    )
    site_components = four.residual_components(
        geometry,
        statistics_zero,
        kinetic_zero,
        contact,
        identity,
    )
    kinetic_components = four.residual_components(
        geometry,
        statistics_zero,
        kinetic_zero,
        contact,
        representative_zero,
    )
    coupling = four.endpoint_coupling(site_components, kinetic_components)

    expected_site_kinetic_residual = site_components[0]
    expected_branch_contact_residual = kinetic_components[1]
    periodic_cost = objective_for(
        geometry, kinetic_zero, contact, coupling
    )(identity)

    previous_kinetic = representative_zero
    rows: list[dict[str, object]] = []
    component_identity_error = 0.0
    final_index = subdivisions if max_index is None else min(max_index, subdivisions)
    for index in range(final_index + 1):
        phase = index * math.pi / subdivisions
        kinetic, spectrum, _ = twisted_operators(phase, contact)
        statistics = four.invariant_statistics(geometry, kinetic, contact)
        hamiltonian = kinetic.scaled_add(contact, coupling)
        objective = four.LowBodyObjective(
            geometry,
            hamiltonian,
            statistics.norm(coupling),
            statistics.kinetic_trace + coupling * statistics.contact_trace,
        )
        branch_unitary = transported_periodic_branch(
            representative_zero, phase
        )
        site = audit_branch(objective, identity, generators)
        kinetic_branch = audit_branch(objective, branch_unitary, generators)

        overlap = dense.best_decomposition_overlap(
            site.unitary, kinetic_branch.unitary
        )
        tracking_overlap = dense.best_decomposition_overlap(
            previous_kinetic, kinetic_branch.unitary
        )
        distinct = overlap < 1.0 - DISTINCTNESS_TOLERANCE
        phase_pass = site.strict and kinetic_branch.strict and distinct
        current_site_components = four.residual_components(
            geometry, statistics, kinetic, contact, identity
        )
        current_branch_components = four.residual_components(
            geometry, statistics, kinetic, contact, branch_unitary
        )
        expected_site_components = (
            expected_site_kinetic_residual,
            0.0,
            0.0,
        )
        expected_branch_components = (
            expected_site_kinetic_residual * math.sin(phase / 4.0) ** 2,
            expected_branch_contact_residual,
            0.0,
        )
        expected_branch_cost = periodic_cost * (
            1.0 + math.sin(phase / 4.0) ** 2
        )
        row_identity_error = max(
            *(abs(left - right) for left, right in zip(
                current_site_components, expected_site_components
            )),
            *(abs(left - right) for left, right in zip(
                current_branch_components, expected_branch_components
            )),
            abs(kinetic_branch.cost - expected_branch_cost),
        )
        component_identity_error = max(
            component_identity_error, row_identity_error
        )
        rows.append(
            {
                "index": index,
                "phase": phase,
                "phase_over_pi": phase / math.pi,
                "spectrum": spectrum,
                "degenerate_blocks": degenerate_blocks(spectrum),
                "site": site,
                "kinetic": kinetic_branch,
                "overlap": overlap,
                "tracking_overlap": tracking_overlap,
                "site_components": current_site_components,
                "kinetic_components": current_branch_components,
                "component_identity_error": row_identity_error,
                "distinct": distinct,
                "pass": phase_pass,
                "objective_evaluations": objective.evaluations,
                "objective_seconds": objective.elapsed,
            }
        )
        previous_kinetic = kinetic_branch.unitary

    small_twist_complete = len(rows) >= 3
    small_twist_gate = small_twist_complete and all(
        bool(rows[index]["pass"]) for index in (0, 1, 2)
    )
    full_gate = len(rows) == subdivisions + 1 and all(
        bool(row["pass"]) for row in rows
    )
    if component_identity_error > 1e-6:
        raise AssertionError(
            "transported-branch residual identities failed: "
            f"{component_identity_error:.3e}"
        )
    return {
        "validation": validation,
        "subdivisions": subdivisions,
        "coupling": coupling,
        "periodic_degeneracy": degeneracy_zero,
        "periodic_representative": representative_zero,
        "rows": rows,
        "small_twist_complete": small_twist_complete,
        "small_twist_gate": small_twist_gate,
        "full_gate": full_gate,
        "component_identity_error": component_identity_error,
        "contact_evaluations": contact_objective.evaluations,
        "contact_seconds": contact_objective.elapsed,
    }


def locate_curvature_zero(
    primary: dict[str, object], iterations: int = 12
) -> dict[str, float]:
    """Bracket a Hessian zero between the last pass and first failed grid point."""

    geometry = dense.FixedSectorGeometry(4, 8)
    _, contact, _ = four.low_body_operators(4, True)
    generators = dense.off_diagonal_generators(4)
    representative = primary["periodic_representative"]
    coupling = float(primary["coupling"])

    def minimum_curvature(phase: float) -> float:
        kinetic, _, _ = twisted_operators(phase, contact)
        objective = objective_for(geometry, kinetic, contact, coupling)
        unitary = transported_periodic_branch(representative, phase)
        hessian = dense.numerical_hessian(
            objective, unitary, generators, 5e-4
        )
        return float(np.min(np.linalg.eigvalsh(hessian)))

    left = 7.0 * math.pi / 16.0
    right = math.pi / 2.0
    left_value = minimum_curvature(left)
    right_value = minimum_curvature(right)
    if left_value <= 0.0 or right_value >= 0.0:
        raise AssertionError("the declared curvature-zero bracket is invalid")
    for _ in range(iterations):
        midpoint = 0.5 * (left + right)
        midpoint_value = minimum_curvature(midpoint)
        if midpoint_value > 0.0:
            left = midpoint
            left_value = midpoint_value
        else:
            right = midpoint
            right_value = midpoint_value
    return {
        "left_phase_over_pi": left / math.pi,
        "left_hessian_minimum": left_value,
        "right_phase_over_pi": right / math.pi,
        "right_hessian_minimum": right_value,
    }


def positive_polynomial_roots(
    coefficients: tuple[float, float, float]
) -> tuple[float, ...]:
    quadratic, linear, constant = coefficients
    if abs(quadratic) < 1e-12:
        if abs(linear) < 1e-12:
            return ()
        roots = np.asarray([-constant / linear], dtype=complex)
    else:
        roots = np.roots((quadratic, linear, constant))
    return tuple(
        float(root.real)
        for root in roots
        if abs(root.imag) < 1e-10 and root.real > 0.0
    )


def conditional_coexistence(
    primary: dict[str, object],
    max_iterations: int,
    seed: int,
) -> tuple[dict[str, object], ...]:
    del max_iterations
    if not primary["small_twist_gate"]:
        return ()
    geometry = dense.FixedSectorGeometry(4, 8)
    _, contact, _ = four.low_body_operators(4, True)
    generators = dense.off_diagonal_generators(4)
    coupling_zero = float(primary["coupling"])
    results: list[dict[str, object]] = []

    for phase_index in (1, 2):
        row = primary["rows"][phase_index]
        phase = float(row["phase"])
        kinetic, _, _ = twisted_operators(phase, contact)
        site_unitary = row["site"].unitary
        kinetic_unitary = row["kinetic"].unitary
        site_components = np.asarray(row["site_components"], dtype=float)
        kinetic_components = np.asarray(
            row["kinetic_components"], dtype=float
        )
        delta = site_components - kinetic_components
        roots = positive_polynomial_roots(
            (float(delta[1]), float(2.0 * delta[2]), float(delta[0]))
        )
        allowed = tuple(
            root
            for root in roots
            if 0.70 * coupling_zero <= root <= 1.05 * coupling_zero
        )
        if not allowed:
            results.append(
                {
                    "phase_index": phase_index,
                    "phase_over_pi": phase / math.pi,
                    "root_found": False,
                    "roots": roots,
                    "pass": False,
                }
            )
            continue
        coupling = min(allowed, key=lambda value: abs(value - coupling_zero))
        final_objective = objective_for(
            geometry, kinetic, contact, coupling
        )
        site = audit_branch(final_objective, site_unitary, generators)
        kinetic_branch = audit_branch(
            final_objective, kinetic_unitary, generators
        )
        overlap = dense.best_decomposition_overlap(
            site.unitary, kinetic_branch.unitary
        )
        random = np.random.default_rng(seed + phase_index)
        sampled = []
        for _ in range(24):
            candidate = dense.haar_unitary(4, random)
            sampled.append((float(final_objective(candidate)), candidate))
        sampled.sort(key=lambda item: item[0])
        optimized = [
            optimize_stationary(
                final_objective,
                candidate,
                generators,
                max_iterations=100,
            )[0]
            for _, candidate in sampled[:4]
        ]
        lowest = min(
            [site.cost, kinetic_branch.cost]
            + [value for value, _ in sampled]
            + optimized
        )
        equal = abs(site.cost - kinetic_branch.cost) < 1e-8
        distinct = overlap < 1.0 - DISTINCTNESS_TOLERANCE
        landscape_pass = lowest >= min(site.cost, kinetic_branch.cost) - 2e-7
        polynomial_residual = float(
            delta[0] + 2.0 * coupling * delta[2] + coupling**2 * delta[1]
        )
        crossing_slope = float(2.0 * delta[2] + 2.0 * coupling * delta[1])
        predicted_coupling = coupling_zero * math.cos(phase / 4.0)
        results.append(
            {
                "phase_index": phase_index,
                "phase_over_pi": phase / math.pi,
                "root_found": True,
                "roots": roots,
                "coupling": coupling,
                "predicted_coupling": predicted_coupling,
                "prediction_error": abs(coupling - predicted_coupling),
                "polynomial_residual": polynomial_residual,
                "crossing_slope": crossing_slope,
                "cost_difference": float(site.cost - kinetic_branch.cost),
                "site": site,
                "kinetic": kinetic_branch,
                "overlap": overlap,
                "random_minimum": sampled[0][0],
                "optimized_minimum": min(optimized),
                "lowest": lowest,
                "equal": equal,
                "distinct": distinct,
                "landscape_pass": landscape_pass,
                "pass": (
                    equal
                    and distinct
                    and site.strict
                    and kinetic_branch.strict
                    and landscape_pass
                    and abs(polynomial_residual) < 1e-7
                    and abs(crossing_slope) > 1e-6
                    and abs(coupling - predicted_coupling) < 1e-10
                ),
            }
        )
    return tuple(results)


def print_result(result: dict[str, object]) -> None:
    print("twist construction validation", result["validation"])
    print("analytic component identity error", result["component_identity_error"])
    print("fixed periodic coupling", result["coupling"])
    print("periodic degeneracy resolution", result["periodic_degeneracy"])
    print(
        "phase/pi  site_cost  kinetic_cost  site_grad  kinetic_grad  "
        "site_hmin  kinetic_hmin  overlap  tracking  pass"
    )
    for row in result["rows"]:
        site = row["site"]
        kinetic = row["kinetic"]
        print(
            f"{row['phase_over_pi']:8.5f} "
            f"{site.cost:10.8f} {kinetic.cost:12.8f} "
            f"{site.gradient_norm:9.2e} {kinetic.gradient_norm:12.2e} "
            f"{site.hessian_minimum:10.6f} {kinetic.hessian_minimum:13.6f} "
            f"{row['overlap']:8.6f} {row['tracking_overlap']:9.6f} "
            f"{row['pass']}"
        )
        if not row["pass"]:
            print("  site gradient steps", site.gradient_steps)
            print("  kinetic gradient steps", kinetic.gradient_steps)
            print("  site Hessian steps", site.hessian_steps)
            print("  kinetic Hessian steps", kinetic.hessian_steps)
            print("  spectrum", row["spectrum"])
            print("  degenerate blocks", row["degenerate_blocks"])

    print(
        "small-twist three-point gate",
        result["small_twist_gate"]
        if result["small_twist_complete"]
        else "not evaluated",
    )
    complete = len(result["rows"]) == int(result["subdivisions"]) + 1
    print(
        "full periodic-to-antiperiodic gate",
        result["full_gate"] if complete else "not evaluated",
    )
    if not result["small_twist_complete"]:
        classification = (
            "PARTIAL PHASE SCAN: the small-twist three-point gate was not "
            "evaluated."
        )
    elif not result["small_twist_gate"]:
        classification = (
            "BOUNDARY-PHASE FAILURE: the periodic branch is locally fragile; "
            "do not run phase-retuned or sampled positive diagnostics."
        )
    elif not complete:
        classification = (
            "SMALL-TWIST GRID PASS: the requested partial run did not evaluate "
            "the full periodic-to-antiperiodic grid."
        )
    elif not result["full_gate"]:
        classification = (
            "SMALL-TWIST ROBUSTNESS ONLY: the first two nonzero grid points "
            "survive, but the transported branch does not remain strict at all "
            "tested twists."
        )
    else:
        classification = (
            "FINITE LOCAL PHASE ROBUSTNESS: both branches persist from periodic "
            "to antiperiodic boundary conditions at fixed coupling; this is not "
            "a global, continuum, EC-specific, or cosmological result."
        )
    print("classification", classification)


def print_conditional(results: tuple[dict[str, object], ...]) -> None:
    if not results:
        print("conditional coexistence skipped: small-twist gate failed")
        return
    print("\nconditional phase-retuned coexistence")
    for result in results:
        if not result["root_found"]:
            print(
                f"  phase/pi={result['phase_over_pi']:.5f} no positive root; "
                f"roots={result['roots']} pass=False"
            )
            continue
        site = result["site"]
        kinetic = result["kinetic"]
        print(
            f"  phase/pi={result['phase_over_pi']:.5f} "
            f"g={result['coupling']:.10f} "
            f"costs=({site.cost:.10f},{kinetic.cost:.10f}) "
            f"grad=({site.gradient_norm:.2e},{kinetic.gradient_norm:.2e}) "
            f"hmin=({site.hessian_minimum:.6f},"
            f"{kinetic.hessian_minimum:.6f}) "
            f"overlap={result['overlap']:.6f} "
            f"poly={result['polynomial_residual']:.2e} "
            f"slope={result['crossing_slope']:.3e} "
            f"random={result['random_minimum']:.8f} "
            f"optimized={result['optimized_minimum']:.8f} "
            f"pass={result['pass']}"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--subdivisions", type=int, default=PHASE_SUBDIVISIONS)
    parser.add_argument("--max-iterations", type=int, default=120)
    parser.add_argument("--max-index", type=int)
    parser.add_argument("--conditional", action="store_true")
    parser.add_argument("--curvature-root", action="store_true")
    parser.add_argument("--deep-validation", action="store_true")
    parser.add_argument("--seed", type=int, default=2026080713)
    arguments = parser.parse_args()
    if arguments.subdivisions < 2:
        raise ValueError("subdivisions must be at least two")
    if arguments.max_index is not None and arguments.max_index < 0:
        raise ValueError("max-index must be nonnegative")

    started = time.perf_counter()
    result = scan_fixed_coupling(
        arguments.subdivisions,
        arguments.max_iterations,
        arguments.seed,
        arguments.max_index,
    )
    print_result(result)
    if arguments.deep_validation:
        print(
            "half-filled sparse validation",
            validate_half_filled_projection(arguments.seed + 1000),
        )
    if arguments.curvature_root:
        print("curvature-zero bracket", locate_curvature_zero(result))
    if arguments.conditional:
        conditional = conditional_coexistence(
            result,
            arguments.max_iterations,
            arguments.seed + 100,
        )
        print_conditional(conditional)
    print(f"total elapsed seconds {time.perf_counter() - started:.3f}")


if __name__ == "__main__":
    main()
