#!/usr/bin/env python3
"""Operational entanglement diagnostics under local fermionic SSRs."""

from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "research"))

import ec_axial_selector_analysis as model  # noqa: E402


def entropy_bits(matrix: np.ndarray) -> float:
    eigenvalues = np.linalg.eigvalsh(matrix)
    eigenvalues = eigenvalues[eigenvalues > 1e-14]
    return float(-np.sum(eigenvalues * np.log2(eigenvalues)))


def local_ssr_entropies(state: np.ndarray) -> dict[str, float]:
    """Return mode entropy and sector-resolved pure-state SSR diagnostics.

    The states tested below have fixed total particle number, so the local
    reduced state is block diagonal in local number. The returned accessible
    terms exclude the Shannon entropy of the local sector label.
    """

    if abs(float(np.vdot(state, state).real) - 1.0) > 1e-10:
        raise AssertionError("state is not normalized")
    coefficients = state.reshape(model.FACTOR_DIMENSION, model.FACTOR_DIMENSION)
    reduced = coefficients @ coefficients.conj().T
    number_groups = {
        number: np.array(
            [
                index
                for index in range(model.FACTOR_DIMENSION)
                if index.bit_count() == number
            ],
            dtype=int,
        )
        for number in range(model.SPINOR_DIMENSION + 1)
    }

    def accessible(groups: list[np.ndarray]) -> tuple[float, float]:
        result = 0.0
        probabilities = []
        for indices in groups:
            block = reduced[np.ix_(indices, indices)]
            probability = float(np.trace(block).real)
            if probability <= 1e-14:
                continue
            probabilities.append(probability)
            result += probability * entropy_bits(block / probability)
        probabilities_array = np.asarray(probabilities)
        if abs(float(np.sum(probabilities_array)) - 1.0) > 1e-10:
            raise AssertionError("SSR sector probabilities do not sum to one")
        classical = float(
            -np.sum(probabilities_array * np.log2(probabilities_array))
        )
        return result, classical

    number_accessible, number_shannon = accessible(list(number_groups.values()))
    even = np.concatenate([number_groups[0], number_groups[2], number_groups[4]])
    odd = np.concatenate([number_groups[1], number_groups[3]])
    parity_accessible, parity_shannon = accessible([even, odd])
    mode = entropy_bits(reduced)
    if abs(mode - number_accessible - number_shannon) > 1e-10:
        raise AssertionError("local-number entropy decomposition failed")
    if abs(mode - parity_accessible - parity_shannon) > 1e-10:
        raise AssertionError("local-parity entropy decomposition failed")
    return {
        "mode": mode,
        "number_accessible": number_accessible,
        "number_shannon": number_shannon,
        "parity_accessible": parity_accessible,
        "parity_shannon": parity_shannon,
    }


def ground_state(kinetic: np.ndarray, contact: np.ndarray, coupling: float) -> np.ndarray:
    _, eigenvectors = np.linalg.eigh(kinetic + coupling * contact)
    return eigenvectors[:, 0]


def density_contact() -> np.ndarray:
    diagonal = np.zeros(model.FOCK_DIMENSION, dtype=float)
    for index in range(model.FOCK_DIMENSION):
        first = index // model.FACTOR_DIMENSION
        second = index % model.FACTOR_DIMENSION
        n_first = first.bit_count()
        n_second = second.bit_count()
        diagonal[index] = n_first * (n_first - 1) + n_second * (n_second - 1)
    return np.diag(diagonal).astype(complex)


def report(label: str, state: np.ndarray) -> None:
    momentum = model.lifted_cell_unitary(np.array([0.0, 1.0, 0.0]))
    site = local_ssr_entropies(state)
    transformed = momentum.conj().T @ state
    momentum_values = local_ssr_entropies(transformed)
    print(label)
    for name in site:
        print(
            f"  {name:18s} site={site[name]:.12f} "
            f"momentum={momentum_values[name]:.12f} "
            f"contrast={site[name] - momentum_values[name]:.12f}"
        )
    if label.startswith("EC axial"):
        for name in ("number_accessible", "parity_accessible"):
            if site[name] <= momentum_values[name]:
                raise AssertionError(
                    f"the {name} EC entanglement contrast was lost"
                )


def main() -> None:
    kinetic, axial = model.build_hamiltonians()
    report("EC axial, full-Fock selector critical point", ground_state(kinetic, axial, 1 / 3))
    report(
        "EC axial, fixed-N=4 selector critical point",
        ground_state(kinetic, axial, math.sqrt(20 / 213)),
    )
    density = density_contact()
    report(
        "Density-contact null, full-Fock selector critical point",
        ground_state(kinetic, density, math.sqrt(8 / 9)),
    )


if __name__ == "__main__":
    main()
