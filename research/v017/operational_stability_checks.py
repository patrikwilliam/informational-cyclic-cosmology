#!/usr/bin/env python3
"""Small diagnostics, not a proof of an infinite-dimensional optimization."""

import argparse
import json
from pathlib import Path
import sys

import numpy as np


def level_and_fiber(n):
    level = 0
    while n % 2 == 0:
        level += 1
        n //= 2
    return level, n


def compress(level_matrix, n):
    """Compress X tensor I from the infinite model, not W*(a truncated shift)."""
    labels = [level_and_fiber(i) for i in range(1, n + 1)]
    return np.array([
        [level_matrix[k, l] if r == s else 0 for l, s in labels]
        for k, r in labels
    ], dtype=complex)


def norm(a):
    return float(np.linalg.norm(a, ord=2))


def probability(a, psi):
    return float(np.vdot(psi, a @ psi).real)


def random_effect(size, rng):
    q, _ = np.linalg.qr(rng.normal(size=(size, size)) + 1j * rng.normal(size=(size, size)))
    return (q * rng.uniform(size=size)) @ q.conj().T


def run():
    rng = np.random.default_rng(10102026)
    tol = 2e-12
    checks = []
    results = []
    for n in (6, 12):
        levels = n.bit_length()
        swap = np.eye(levels)
        swap[:2, :2] = [[0, 1], [1, 0]]
        q = compress((np.eye(levels) + swap) / 2, n)
        d = np.eye(n)
        d[2, 2] = -1
        flipped = d @ q @ d
        psi0 = np.zeros(n, dtype=complex)
        psi1 = np.zeros(n, dtype=complex)
        psi0[[0, 1]] = 1 / np.sqrt(2)
        psi1[[2, 5]] = 1 / np.sqrt(2)
        ev = np.linalg.eigvalsh(flipped)
        assert ev.min() >= -tol and ev.max() <= 1 + tol
        assert abs(probability(flipped, psi0) - 1) < tol
        assert abs(probability(flipped, psi1)) < tol
        assert abs(norm(flipped - np.eye(n) / 2) - 0.5) < tol
        common_error = 0.0
        diagonal_error = 0.0
        cotransport_error = 0.0
        for _ in range(40):
            a = compress(random_effect(levels, rng), n)
            common_error = max(common_error, abs(probability(a, psi0) - probability(a, psi1)))
            assert max(abs(1 - probability(a, psi0)), abs(probability(a, psi1))) >= 0.5 - tol
            weights = rng.dirichlet(np.ones(n))
            diagonal_error = max(diagonal_error, abs(np.dot(weights, np.diag(a - d @ a @ d))))
            v = rng.normal(size=n) + 1j * rng.normal(size=n)
            v /= np.linalg.norm(v)
            cotransport_error = max(cotransport_error, abs(probability(a, v) - probability(d @ a @ d, d @ v)))
        assert max(common_error, diagonal_error, cotransport_error) < tol

        # A flip beyond the access window is the identity after compression.
        larger_n = n + 3
        larger_a = compress(random_effect(larger_n.bit_length(), rng), larger_n)
        tail_d = np.eye(larger_n)
        tail_d[-1, -1] = -1
        tail_error = norm((tail_d @ larger_a @ tail_d)[:n, :n] - larger_a[:n, :n])
        assert tail_error == 0
        results.append({
            "window": n,
            "witness_probabilities": [probability(flipped, psi0), probability(flipped, psi1)],
            "witness_midpoint_distance": norm(flipped - np.eye(n) / 2),
            "sampled_common_probability_error": common_error,
            "diagonal_state_control_error": float(diagonal_error),
            "cotransport_control_error": cotransport_error,
            "outside_window_control_error": tail_error,
        })
    checks.extend(["positive_effect_witness", "two_fixed_probe_obstruction", "midpoint_upper_bound_witness",
                   "fiber_symmetry_samples", "diagonal_access_control", "cotransport_control", "cutoff_control"])

    # The exact infinite normalization and energy bound are in the supplement.
    indices = np.arange(1, 65)
    u = np.sqrt(192 / 61) * 2.0 ** (-indices)
    u[2] = 0
    assert abs(np.linalg.norm(u) - 1) < tol
    reference_results = []
    for epsilon in (0.1, 0.01, 0.0001, 0.000001):
        c = np.sqrt(1 - epsilon**2) * u.astype(complex)
        c[2] = epsilon
        other = c.copy()
        other[2] *= -1
        vector_error = float(np.linalg.norm(c - other))
        rho_difference = np.outer(c, c.conj()) - np.outer(other, other.conj())
        trace_distance = float(np.abs(np.linalg.eigvalsh(rho_difference)).sum() / 2)
        expected_trace_distance = 2 * epsilon * np.sqrt(1 - epsilon**2)
        energy = float(np.dot(np.abs(c)**2, np.log(indices)))
        assert abs(vector_error - 2 * epsilon) < tol
        assert abs(trace_distance - expected_trace_distance) < tol
        assert energy < 2
        reference_results.append({"epsilon": epsilon, "vector_error": vector_error,
                                  "trace_distance": trace_distance, "truncated_mean_energy": energy})
    checks.append("reference_error_and_energy_diagnostics")

    # Independently sampled small perturbations check, but do not prove, the bound.
    c = np.sqrt(0.99) * u.astype(complex)
    c[2] = 0.1
    worst_excess = 0.0
    for n in (6, 12):
        mu = float(np.abs(c[:n]).min())
        for _ in range(40):
            other = c + 1e-5 * (rng.normal(size=64) + 1j * rng.normal(size=64))
            other /= np.linalg.norm(other)
            overlap = np.vdot(c, other)
            other *= overlap.conjugate() / abs(overlap)
            delta = float(np.linalg.norm(c - other))
            phase_c = c[:n] / np.abs(c[:n])
            phase_other = other[:n] / np.abs(other[:n])
            eta = float(np.abs(phase_c - phase_other).max())
            assert eta <= 2 * delta / mu + tol
            a = compress(random_effect(n.bit_length(), rng), n)
            old_a = phase_c[:, None] * a * phase_c.conj()[None, :]
            new_a = phase_other[:, None] * a * phase_other.conj()[None, :]
            excess = norm(old_a - new_a) - eta
            worst_excess = max(worst_excess, excess)
            assert excess < tol
    checks.append("conditional_phase_and_centered_effect_bound_samples")
    return {"status": "passed", "seed": 10102026, "tolerance": tol, "checks": checks,
            "windows": results, "reference_diagnostics": reference_results,
            "conditional_bound_worst_excess": worst_excess,
            "limits": "Finite diagnostics only; no optimization proof or physical selector."}


if __name__ == "__main__":
    if sys.flags.optimize:
        raise SystemExit("Assertions must be enabled; do not use -O/-OO.")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = json.dumps(run(), indent=2) + "\n"
    if args.output:
        args.output.write_text(result, encoding="utf-8")
    print(result)
