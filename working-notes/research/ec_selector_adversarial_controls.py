#!/usr/bin/env python3
"""Adversarial controls for the finite EC/CAR selector increment.

The script tests whether the fixed-sector stationary result is special to N=4
and whether a non-EC onsite density contact produces the same qualitative
selector geometry.
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research"))

import ec_axial_selector_analysis as model  # noqa: E402


LOCAL_INDICES = {
    particle_number: tuple(
        index
        for index in range(model.FACTOR_DIMENSION)
        if index.bit_count() == particle_number
    )
    for particle_number in range(model.SPINOR_DIMENSION + 1)
}


@dataclass(frozen=True)
class SectorGeometry:
    particle_number: int
    indices: tuple[int, ...]
    block_positions: dict[int, tuple[int, ...]]

    @property
    def dimension(self) -> int:
        return len(self.indices)


def build_sector_geometry(particle_number: int) -> SectorGeometry:
    indices = tuple(
        index
        for index in range(model.FOCK_DIMENSION)
        if index.bit_count() == particle_number
    )
    positions = {index: position for position, index in enumerate(indices)}
    blocks: dict[int, tuple[int, ...]] = {}
    lower = max(0, particle_number - model.SPINOR_DIMENSION)
    upper = min(model.SPINOR_DIMENSION, particle_number)
    for first_particles in range(lower, upper + 1):
        second_particles = particle_number - first_particles
        blocks[first_particles] = tuple(
            positions[first * model.FACTOR_DIMENSION + second]
            for first in LOCAL_INDICES[first_particles]
            for second in LOCAL_INDICES[second_particles]
        )
    return SectorGeometry(particle_number, indices, blocks)


def rectangular_local_projection(
    matrix: np.ndarray,
    first_dimension: int,
    second_dimension: int,
) -> np.ndarray:
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


def sector_local_projection(
    matrix: np.ndarray,
    geometry: SectorGeometry,
) -> np.ndarray:
    result = np.zeros_like(matrix)
    total = geometry.particle_number
    for first_particles, positions in geometry.block_positions.items():
        second_particles = total - first_particles
        first_dimension = len(LOCAL_INDICES[first_particles])
        second_dimension = len(LOCAL_INDICES[second_particles])
        block = matrix[np.ix_(positions, positions)]
        result[np.ix_(positions, positions)] = rectangular_local_projection(
            block,
            first_dimension,
            second_dimension,
        )
    return result


def restrict(matrix: np.ndarray, geometry: SectorGeometry) -> np.ndarray:
    return matrix[np.ix_(geometry.indices, geometry.indices)]


def residual_components(
    kinetic: np.ndarray,
    contact: np.ndarray,
    orientation: np.ndarray,
    geometry: SectorGeometry | None = None,
) -> tuple[float, float, float]:
    lift = model.lifted_cell_unitary(orientation)
    transformed_kinetic = lift.conj().T @ kinetic @ lift
    transformed_contact = lift.conj().T @ contact @ lift
    if geometry is None:
        projected_kinetic = model.local_projection(transformed_kinetic)
        projected_contact = model.local_projection(transformed_contact)
    else:
        transformed_kinetic = restrict(transformed_kinetic, geometry)
        transformed_contact = restrict(transformed_contact, geometry)
        projected_kinetic = sector_local_projection(transformed_kinetic, geometry)
        projected_contact = sector_local_projection(transformed_contact, geometry)
    residual_kinetic = transformed_kinetic - projected_kinetic
    residual_contact = transformed_contact - projected_contact
    return (
        model.squared_norm(residual_kinetic),
        model.squared_norm(residual_contact),
        float(np.vdot(residual_kinetic, residual_contact).real),
    )


def critical_sector_state(
    kinetic: np.ndarray,
    contact: np.ndarray,
    coupling: float,
    geometry: SectorGeometry,
) -> dict[str, float]:
    sector_hamiltonian = restrict(kinetic + coupling * contact, geometry)
    eigenvalues, eigenvectors = np.linalg.eigh(sector_hamiltonian)
    sector_state = eigenvectors[:, 0]
    full_state = np.zeros(model.FOCK_DIMENSION, dtype=complex)
    full_state[list(geometry.indices)] = sector_state
    momentum = model.lifted_cell_unitary(np.array([0.0, 1.0, 0.0]))
    return {
        "energy": float(eigenvalues[0]),
        "gap": float(eigenvalues[1] - eigenvalues[0])
        if geometry.dimension > 1
        else float("nan"),
        "site_entropy": model.pure_state_entropy_bits(full_state),
        "momentum_entropy": model.pure_state_entropy_bits(
            momentum.conj().T @ full_state
        ),
    }


def endpoint_hessians(
    kinetic: np.ndarray,
    contact: np.ndarray,
    coupling: float,
    geometry: SectorGeometry | None,
    epsilon: float = 1e-4,
) -> tuple[tuple[float, float], tuple[float, float]]:
    def cost(orientation: np.ndarray) -> float:
        k, q, cross = residual_components(
            kinetic, contact, orientation, geometry
        )
        return k + coupling * coupling * q + 2.0 * coupling * cross

    def curvature(center: np.ndarray, tangent: np.ndarray) -> float:
        plus = center * math.cos(epsilon) + tangent * math.sin(epsilon)
        minus = center * math.cos(epsilon) - tangent * math.sin(epsilon)
        return (cost(plus) - 2.0 * cost(center) + cost(minus)) / epsilon**2

    y = np.array([0.0, 1.0, 0.0])
    z = np.array([0.0, 0.0, 1.0])
    x = np.array([1.0, 0.0, 0.0])
    return (
        (curvature(y, x), curvature(y, z)),
        (curvature(z, x), curvature(z, y)),
    )


def density_contact() -> np.ndarray:
    diagonal = np.zeros(model.FOCK_DIMENSION, dtype=float)
    for index in range(model.FOCK_DIMENSION):
        first = index // model.FACTOR_DIMENSION
        second = index % model.FACTOR_DIMENSION
        n_first = first.bit_count()
        n_second = second.bit_count()
        diagonal[index] = n_first * (n_first - 1) + n_second * (n_second - 1)
    return np.diag(diagonal).astype(complex)


def binomial_or_zero(upper: int, lower: int) -> int:
    if lower < 0 or lower > upper:
        return 0
    return math.comb(upper, lower)


def predicted_axial_sector_components(
    particle_number: int,
    orientation: np.ndarray,
) -> tuple[float, float, float]:
    orientation = orientation / np.linalg.norm(orientation)
    _, y, z = orientation
    kinetic = 8.0 * binomial_or_zero(6, particle_number - 1) * (1.0 - y * y)
    contact = (
        4.0
        * binomial_or_zero(4, particle_number - 2)
        * (1.0 - z * z)
        * (71.0 + 25.0 * z * z)
    )
    return kinetic, contact, 0.0


def scan_sphere_minimum(
    kinetic: np.ndarray,
    contact: np.ndarray,
    coupling: float,
    geometry: SectorGeometry | None,
    samples: int = 24,
) -> tuple[float, np.ndarray]:
    random = np.random.default_rng(20260717)
    endpoints = [
        np.array([0.0, 1.0, 0.0]),
        np.array([0.0, 0.0, 1.0]),
    ]
    orientations = endpoints + [
        vector / np.linalg.norm(vector)
        for vector in random.normal(size=(samples, 3))
    ]
    best = (float("inf"), orientations[0])
    for orientation in orientations:
        k, q, cross = residual_components(
            kinetic, contact, orientation, geometry
        )
        value = k + coupling * coupling * q + 2.0 * coupling * cross
        if value < best[0]:
            best = (value, orientation)
    return best


def sector_scan(kinetic: np.ndarray, contact: np.ndarray) -> None:
    print("EC axial contact: all fixed-number sectors")
    print(
        "N dim K_site Q_momentum r_c y_hess_min z_hess_min gap dS "
        "random_excess"
    )
    y = np.array([0.0, 1.0, 0.0])
    z = np.array([0.0, 0.0, 1.0])
    formula_error = 0.0
    random = np.random.default_rng(20260718)
    for particle_number in range(1, model.MODE_COUNT):
        geometry = build_sector_geometry(particle_number)
        test_orientations = [y, z, *random.normal(size=(3, 3))]
        for orientation in test_orientations:
            numerical = np.asarray(
                residual_components(kinetic, contact, orientation, geometry)
            )
            predicted = np.asarray(
                predicted_axial_sector_components(particle_number, orientation)
            )
            formula_error = max(
                formula_error, float(np.max(np.abs(numerical - predicted)))
            )
        site = residual_components(kinetic, contact, z, geometry)
        momentum = residual_components(kinetic, contact, y, geometry)
        if site[0] < 1e-10 or momentum[1] < 1e-10:
            print(
                particle_number,
                geometry.dimension,
                f"{site[0]:.9g}",
                f"{momentum[1]:.9g}",
                "no-transition",
            )
            continue
        coupling = math.sqrt(site[0] / momentum[1])
        y_hessian, z_hessian = endpoint_hessians(
            kinetic, contact, coupling, geometry
        )
        state = critical_sector_state(kinetic, contact, coupling, geometry)
        minimum, orientation = scan_sphere_minimum(
            kinetic, contact, coupling, geometry
        )
        endpoint_cost = site[0]
        print(
            particle_number,
            geometry.dimension,
            f"{site[0]:.9g}",
            f"{momentum[1]:.9g}",
            f"{coupling:.9g}",
            f"{min(y_hessian):.9g}",
            f"{min(z_hessian):.9g}",
            f"{state['gap']:.9g}",
            f"{state['site_entropy'] - state['momentum_entropy']:.9g}",
            f"{minimum - endpoint_cost:.3g}",
            np.round(orientation, 3),
        )
    print("largest all-sector closed-form error", formula_error)
    if formula_error > 1e-8:
        raise AssertionError("all-sector axial formula failed")


def null_control(kinetic: np.ndarray) -> None:
    contact = density_contact()
    y = np.array([0.0, 1.0, 0.0])
    z = np.array([0.0, 0.0, 1.0])
    print("\nNon-EC onsite density contact control")
    for label, geometry in (
        ("full Fock", None),
        ("N=4", build_sector_geometry(4)),
    ):
        site = residual_components(kinetic, contact, z, geometry)
        momentum = residual_components(kinetic, contact, y, geometry)
        coupling = math.sqrt(site[0] / momentum[1])
        y_hessian, z_hessian = endpoint_hessians(
            kinetic, contact, coupling, geometry
        )
        minimum, orientation = scan_sphere_minimum(
            kinetic, contact, coupling, geometry, samples=80
        )
        sector_state = critical_sector_state(
            kinetic,
            contact,
            coupling,
            build_sector_geometry(4),
        )
        print(label)
        print("  components site", site, "momentum", momentum)
        print("  equal-endpoint coupling", coupling)
        print("  endpoint Hessians y", y_hessian, "z", z_hessian)
        print(
            "  random minimum excess/orientation",
            minimum - site[0],
            np.round(orientation, 6),
        )
        print(
            "  N=4 critical state gap/dS",
            sector_state["gap"],
            sector_state["site_entropy"] - sector_state["momentum_entropy"],
        )
        if min(*y_hessian, *z_hessian) <= 0.0:
            raise AssertionError("density-contact endpoint lost strictness")
        if minimum < site[0] - 1e-8:
            raise AssertionError("random scan found a lower non-endpoint cost")
        if sector_state["gap"] <= 0.0:
            raise AssertionError("density-contact N=4 ground state is degenerate")


def main() -> None:
    kinetic, contact = model.build_hamiltonians()
    sector_scan(kinetic, contact)
    null_control(kinetic)


if __name__ == "__main__":
    main()
