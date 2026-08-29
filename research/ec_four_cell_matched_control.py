#!/usr/bin/env python3
"""Prospective four-cell EC axial versus non-axial density control gate.

Both interactions use the same fixed-sector selector, periodic zero-family
resolution, gauge-transported branch, phase grid, and numerical tolerances.
This is a finite interaction-specificity test, not a continuum or cosmological
calculation.
"""

from __future__ import annotations

import argparse
import math
import time
from dataclasses import dataclass

import numpy as np

import ec_four_cell_boundary_phase as phase_gate
import ec_four_cell_selector as four
import ec_three_cell_selector as dense


PHASE_SUBDIVISIONS = 16
LANDSCAPE_SAMPLES = 24
LANDSCAPE_DESCENTS = 4


@dataclass(frozen=True)
class ModelResult:
    label: str
    coupling: float
    periodic_representative: np.ndarray
    periodic_resolution: dict[str, float]
    rows: tuple[dict[str, object], ...]
    periodic_gate: bool
    small_twist_complete: bool
    small_twist_gate: bool
    full_grid_complete: bool
    full_grid_gate: bool
    first_failed_index: int | None
    component_identity_error: float


def density_low_body_operator() -> four.LowBodyOperator:
    two_particle_geometry = dense.FixedSectorGeometry(4, 2)
    density_two_body = dense.density_contact(two_particle_geometry)
    return four.LowBodyOperator(
        np.zeros((16, 16), dtype=complex), density_two_body
    )


def occupation_density(mask: int) -> float:
    return float(
        sum(
            (number := dense.local_state(mask, cell).bit_count())
            * (number - 1)
            for cell in range(4)
        )
    )


def validate_density_operator(
    contact: four.LowBodyOperator,
) -> dict[str, float]:
    small_geometry = dense.FixedSectorGeometry(4, 3)
    reconstructed = four.fixed_sector_matrix(small_geometry, contact)
    direct_small = dense.density_contact(small_geometry)

    geometry = dense.FixedSectorGeometry(4, 8)
    terms = four.sparse_terms(contact)
    actions = [
        four.apply_low_body(mask, contact, terms) for mask in geometry.masks
    ]
    expected_diagonal = np.asarray(
        [occupation_density(mask) for mask in geometry.masks]
    )
    diagonal_error = max(
        abs(action.get(mask, 0.0j) - expected)
        for action, mask, expected in zip(
            actions, geometry.masks, expected_diagonal
        )
    )
    off_diagonal_error = max(
        (
            abs(value)
            for action, mask in zip(actions, geometry.masks)
            for target, value in action.items()
            if target != mask
        ),
        default=0.0,
    )
    direct_overlaps = np.asarray(
        [
            sum(
                actions[column].get(geometry.masks[row], 0.0j)
                for row, column in zip(rows, columns)
            )
            for rows, columns in geometry.unit_supports
        ]
    )
    formula_overlaps = four.projection_overlaps(geometry, contact)
    direct_trace = float(np.sum(expected_diagonal))
    direct_norm = float(np.vdot(expected_diagonal, expected_diagonal).real)
    result = {
        "small_filling_reconstruction": float(
            np.max(np.abs(reconstructed - direct_small))
        ),
        "half_filled_diagonal": float(diagonal_error),
        "half_filled_off_diagonal": float(off_diagonal_error),
        "half_filled_projection_overlaps": float(
            np.max(np.abs(direct_overlaps - formula_overlaps))
        ),
        "half_filled_trace": float(
            abs(direct_trace - four.sector_trace(geometry, contact))
        ),
        "half_filled_norm": float(
            abs(
                direct_norm
                - four.sector_inner_product(
                    geometry, contact, contact
                ).real
            )
        ),
        "one_body_zero": float(np.max(np.abs(contact.one_body))),
        "two_body_hermiticity": float(
            np.max(np.abs(contact.two_body - contact.two_body.conj().T))
        ),
    }
    if max(result.values()) > 2e-8:
        raise AssertionError(f"density control validation failed: {result}")
    return result


def interaction_independence(
    axial: four.LowBodyOperator,
    density: four.LowBodyOperator,
) -> dict[str, object]:
    """Check that centering and rescaling do not identify the two contacts."""

    geometry = dense.FixedSectorGeometry(4, 8)
    dimension = geometry.dimension
    axial_trace = four.sector_trace(geometry, axial)
    density_trace = four.sector_trace(geometry, density)
    axial_norm = (
        four.sector_inner_product(geometry, axial, axial).real
        - abs(axial_trace) ** 2 / dimension
    )
    density_norm = (
        four.sector_inner_product(geometry, density, density).real
        - abs(density_trace) ** 2 / dimension
    )
    centered_inner = (
        four.sector_inner_product(geometry, axial, density)
        - axial_trace.conjugate() * density_trace / dimension
    )
    centered_cosine = abs(centered_inner) / math.sqrt(
        axial_norm * density_norm
    )
    best_scale = float(centered_inner.real / axial_norm)
    residual_squared = (
        density_norm
        - 2.0 * best_scale * centered_inner.real
        + best_scale**2 * axial_norm
    )
    relative_residual = math.sqrt(max(residual_squared, 0.0) / density_norm)

    pairs = four.pair_basis(axial.mode_count)
    local_pair_indices = tuple(
        index for index, pair in enumerate(pairs) if pair[1] < 4
    )
    axial_local = axial.two_body[
        np.ix_(local_pair_indices, local_pair_indices)
    ]
    density_local = density.two_body[
        np.ix_(local_pair_indices, local_pair_indices)
    ]
    result: dict[str, object] = {
        "centered_cosine": float(centered_cosine),
        "best_centered_scale": best_scale,
        "relative_centered_residual": float(relative_residual),
        "axial_local_spectrum": tuple(
            float(value) for value in np.linalg.eigvalsh(axial_local)
        ),
        "density_local_spectrum": tuple(
            float(value) for value in np.linalg.eigvalsh(density_local)
        ),
    }
    if relative_residual < 1e-3:
        raise AssertionError(
            "density control is affinely equivalent to the axial contact"
        )
    return result


def contact_objective_for(
    geometry: dense.FixedSectorGeometry,
    contact: four.LowBodyOperator,
) -> four.LowBodyObjective:
    zero = four.LowBodyOperator(
        np.zeros_like(contact.one_body), np.zeros_like(contact.two_body)
    )
    statistics = four.invariant_statistics(geometry, zero, contact)
    return four.LowBodyObjective(
        geometry,
        contact,
        statistics.contact_norm,
        statistics.contact_trace,
    )


def scan_model(
    label: str,
    contact: four.LowBodyOperator,
    max_index: int,
) -> ModelResult:
    geometry = dense.FixedSectorGeometry(4, 8)
    generators = dense.off_diagonal_generators(4)
    identity = np.eye(4, dtype=complex)
    contact_objective = contact_objective_for(geometry, contact)

    kinetic_zero, _, basis_zero = phase_gate.twisted_operators(0.0, contact)
    representative_zero, resolution = four.periodic_kinetic_representative(
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
    branch_components = four.residual_components(
        geometry,
        statistics_zero,
        kinetic_zero,
        contact,
        representative_zero,
    )
    coupling = four.endpoint_coupling(site_components, branch_components)
    periodic_cost = phase_gate.objective_for(
        geometry, kinetic_zero, contact, coupling
    )(identity)
    expected_site_kinetic_residual = site_components[0]
    expected_branch_contact_residual = branch_components[1]

    rows: list[dict[str, object]] = []
    previous = representative_zero
    component_identity_error = 0.0
    for index in range(max_index + 1):
        phase = index * math.pi / PHASE_SUBDIVISIONS
        kinetic, spectrum, _ = phase_gate.twisted_operators(phase, contact)
        statistics = four.invariant_statistics(geometry, kinetic, contact)
        hamiltonian = kinetic.scaled_add(contact, coupling)
        objective = four.LowBodyObjective(
            geometry,
            hamiltonian,
            statistics.norm(coupling),
            statistics.kinetic_trace
            + coupling * statistics.contact_trace,
        )
        branch_unitary = phase_gate.transported_periodic_branch(
            representative_zero, phase
        )
        site = phase_gate.audit_branch(objective, identity, generators)
        branch = phase_gate.audit_branch(
            objective, branch_unitary, generators
        )
        overlap = dense.best_decomposition_overlap(
            site.unitary, branch.unitary
        )
        tracking_overlap = dense.best_decomposition_overlap(
            previous, branch.unitary
        )
        distinct = overlap < 1.0 - phase_gate.DISTINCTNESS_TOLERANCE
        current_site_components = four.residual_components(
            geometry,
            statistics,
            kinetic,
            contact,
            identity,
        )
        current_branch_components = four.residual_components(
            geometry,
            statistics,
            kinetic,
            contact,
            branch_unitary,
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
            *(
                abs(left - right)
                for left, right in zip(
                    current_site_components, expected_site_components
                )
            ),
            *(
                abs(left - right)
                for left, right in zip(
                    current_branch_components, expected_branch_components
                )
            ),
            abs(branch.cost - expected_branch_cost),
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
                "site": site,
                "branch": branch,
                "site_components": current_site_components,
                "branch_components": current_branch_components,
                "component_identity_error": row_identity_error,
                "overlap": overlap,
                "tracking_overlap": tracking_overlap,
                "distinct": distinct,
                "pass": site.strict and branch.strict and distinct,
            }
        )
        previous = branch_unitary

    periodic_gate = bool(rows[0]["pass"])
    small_twist_complete = len(rows) >= 3
    small_twist_gate = small_twist_complete and all(
        bool(rows[index]["pass"]) for index in (0, 1, 2)
    )
    full_grid_complete = len(rows) == PHASE_SUBDIVISIONS + 1
    full_grid_gate = full_grid_complete and all(
        bool(row["pass"]) for row in rows
    )
    first_failed = next(
        (int(row["index"]) for row in rows if not row["pass"]), None
    )
    if component_identity_error > 1e-6:
        raise AssertionError(
            "transported-branch component identity failed: "
            f"{component_identity_error:.3e}"
        )
    return ModelResult(
        label=label,
        coupling=coupling,
        periodic_representative=representative_zero,
        periodic_resolution=resolution,
        rows=tuple(rows),
        periodic_gate=periodic_gate,
        small_twist_complete=small_twist_complete,
        small_twist_gate=small_twist_gate,
        full_grid_complete=full_grid_complete,
        full_grid_gate=full_grid_gate,
        first_failed_index=first_failed,
        component_identity_error=component_identity_error,
    )


def classify_specificity(
    axial: ModelResult, density: ModelResult
) -> tuple[str, bool]:
    if not axial.small_twist_complete or not density.small_twist_complete:
        return (
            "NOT EVALUATED: the run did not include all three primary "
            "small-twist points.",
            False,
        )
    if not axial.periodic_gate or not axial.small_twist_gate:
        return (
            "INCONCLUSIVE: the axial candidate does not pass its own primary "
            "small-twist gate.",
            False,
        )
    if density.periodic_gate and density.small_twist_gate:
        return (
            "EC-SPECIFICITY FAIL: the matched non-axial density control passes "
            "the same periodic and small-twist gates.",
            False,
        )
    return (
        "EC-SPECIFICITY PASS: the axial candidate passes while the validated "
        "density control fails the prospective primary gate.",
        True,
    )


def conditional_diagnostics(
    model: ModelResult,
    contact: four.LowBodyOperator,
    seed: int,
) -> tuple[dict[str, object], ...]:
    if not model.small_twist_gate:
        return ()
    geometry = dense.FixedSectorGeometry(4, 8)
    generators = dense.off_diagonal_generators(4)
    results: list[dict[str, object]] = []
    for phase_index in (1, 2):
        row = model.rows[phase_index]
        phase = float(row["phase"])
        site_components = np.asarray(row["site_components"], dtype=float)
        branch_components = np.asarray(
            row["branch_components"], dtype=float
        )
        delta = site_components - branch_components
        roots = phase_gate.positive_polynomial_roots(
            (float(delta[1]), float(2.0 * delta[2]), float(delta[0]))
        )
        allowed = tuple(
            root
            for root in roots
            if 0.70 * model.coupling <= root <= 1.05 * model.coupling
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
        coupling = min(
            allowed, key=lambda value: abs(value - model.coupling)
        )
        kinetic, _, _ = phase_gate.twisted_operators(phase, contact)
        objective = phase_gate.objective_for(
            geometry, kinetic, contact, coupling
        )
        site = phase_gate.audit_branch(
            objective, row["site"].unitary, generators
        )
        branch = phase_gate.audit_branch(
            objective, row["branch"].unitary, generators
        )
        overlap = dense.best_decomposition_overlap(
            site.unitary, branch.unitary
        )
        random = np.random.default_rng(seed + phase_index)
        samples = [
            (float(objective(candidate)), candidate)
            for candidate in (
                dense.haar_unitary(4, random)
                for _ in range(LANDSCAPE_SAMPLES)
            )
        ]
        samples.sort(key=lambda item: item[0])
        optimized = [
            phase_gate.optimize_stationary(
                objective,
                candidate,
                generators,
                max_iterations=100,
            )[0]
            for _, candidate in samples[:LANDSCAPE_DESCENTS]
        ]
        polynomial_residual = float(
            delta[0] + 2.0 * coupling * delta[2]
            + coupling**2 * delta[1]
        )
        crossing_slope = float(
            2.0 * delta[2] + 2.0 * coupling * delta[1]
        )
        predicted_coupling = model.coupling * math.cos(phase / 4.0)
        endpoint_minimum = min(site.cost, branch.cost)
        optimized_minimum = min(optimized)
        landscape_pass = optimized_minimum >= endpoint_minimum - 2e-7
        equal = abs(site.cost - branch.cost) < 1e-8
        distinct = overlap < 1.0 - phase_gate.DISTINCTNESS_TOLERANCE
        results.append(
            {
                "phase_index": phase_index,
                "phase_over_pi": phase / math.pi,
                "root_found": True,
                "roots": roots,
                "coupling": coupling,
                "polynomial_residual": polynomial_residual,
                "crossing_slope": crossing_slope,
                "predicted_coupling": predicted_coupling,
                "prediction_error": abs(coupling - predicted_coupling),
                "site": site,
                "branch": branch,
                "overlap": overlap,
                "random_minimum": samples[0][0],
                "optimized_minimum": optimized_minimum,
                "equal": equal,
                "distinct": distinct,
                "landscape_pass": landscape_pass,
                "pass": (
                    equal
                    and distinct
                    and site.strict
                    and branch.strict
                    and landscape_pass
                    and abs(polynomial_residual) < 1e-7
                    and abs(crossing_slope) > 1e-6
                ),
            }
        )
    return tuple(results)


def print_model(model: ModelResult) -> None:
    print(f"\n{model.label.upper()}")
    print("coupling", model.coupling)
    print("periodic resolution", model.periodic_resolution)
    print("analytic component/cost identity error", model.component_identity_error)
    print(
        "phase/pi site_cost branch_cost site_grad branch_grad "
        "site_hmin branch_hmin overlap tracking pass"
    )
    for row in model.rows:
        site = row["site"]
        branch = row["branch"]
        print(
            f"{row['phase_over_pi']:8.5f} "
            f"{site.cost:9.7f} {branch.cost:11.7f} "
            f"{site.gradient_norm:9.2e} {branch.gradient_norm:11.2e} "
            f"{site.hessian_minimum:10.6f} "
            f"{branch.hessian_minimum:11.6f} "
            f"{row['overlap']:8.6f} {row['tracking_overlap']:8.6f} "
            f"{row['pass']}"
        )
    print("periodic endpoint gate", model.periodic_gate)
    print(
        "small-twist gate",
        model.small_twist_gate if model.small_twist_complete else "not evaluated",
    )
    print(
        "full phase-grid gate",
        model.full_grid_gate if model.full_grid_complete else "not evaluated",
    )
    print("first failed index", model.first_failed_index)


def print_conditional(
    label: str, results: tuple[dict[str, object], ...]
) -> None:
    print(f"\n{label.upper()} CONDITIONAL DIAGNOSTICS")
    if not results:
        print("skipped: small-twist gate failed")
        return
    for result in results:
        if not result["root_found"]:
            print(
                f"phase/pi={result['phase_over_pi']:.5f} "
                f"roots={result['roots']} pass=False"
            )
            continue
        site = result["site"]
        branch = result["branch"]
        print(
            f"phase/pi={result['phase_over_pi']:.5f} "
            f"g={result['coupling']:.10f} "
            f"costs=({site.cost:.10f},{branch.cost:.10f}) "
            f"grad=({site.gradient_norm:.2e},{branch.gradient_norm:.2e}) "
            f"hmin=({site.hessian_minimum:.6f},"
            f"{branch.hessian_minimum:.6f}) "
            f"poly={result['polynomial_residual']:.2e} "
            f"slope={result['crossing_slope']:.3e} "
            f"g_error={result['prediction_error']:.2e} "
            f"random={result['random_minimum']:.8f} "
            f"optimized={result['optimized_minimum']:.8f} "
            f"pass={result['pass']}"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-index", type=int, default=PHASE_SUBDIVISIONS)
    parser.add_argument("--conditional", action="store_true")
    parser.add_argument("--seed", type=int, default=2026080901)
    arguments = parser.parse_args()
    if not 0 <= arguments.max_index <= PHASE_SUBDIVISIONS:
        raise ValueError(
            f"max-index must be between 0 and {PHASE_SUBDIVISIONS}"
        )

    started = time.perf_counter()
    _, axial_contact, _ = four.low_body_operators(4, True)
    density_contact = density_low_body_operator()
    density_validation = validate_density_operator(density_contact)
    independence = interaction_independence(axial_contact, density_contact)
    twist_validation = phase_gate.validate_twist_construction(axial_contact)
    print("density validation", density_validation)
    print("interaction independence", independence)
    print("shared twist validation", twist_validation)

    axial = scan_model("EC axial contact", axial_contact, arguments.max_index)
    density = scan_model(
        "non-axial density control", density_contact, arguments.max_index
    )
    print_model(axial)
    print_model(density)

    specificity, passed = classify_specificity(axial, density)
    print("\nPRIMARY SPECIFICITY VERDICT", specificity)
    print("EC-specificity gate", passed)

    if arguments.conditional:
        axial_conditional = conditional_diagnostics(
            axial, axial_contact, arguments.seed + 100
        )
        density_conditional = conditional_diagnostics(
            density, density_contact, arguments.seed + 200
        )
        print_conditional(axial.label, axial_conditional)
        print_conditional(density.label, density_conditional)

    print(f"total elapsed seconds {time.perf_counter() - started:.3f}")


if __name__ == "__main__":
    main()
