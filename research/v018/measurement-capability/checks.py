#!/usr/bin/env python3
"""Exact symmetry-constrained capability bounds for the existing finite model."""

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import platform

import numpy as np


BASE_PATH = Path(__file__).resolve().parent.parent / "three-qubit-memory" / "checks.py"
SPEC = importlib.util.spec_from_file_location("icc_three_qubit", BASE_PATH)
BASE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BASE)
I, X, Y, Z, N = BASE.I, BASE.X, BASE.Y, BASE.Z, BASE.N
TOL = 2e-10
SEED = 20261015


def require(condition, label):
    if not condition:
        raise RuntimeError(label)


def close(a, b, label, errors):
    error = float(np.max(np.abs(np.asarray(a) - np.asarray(b))))
    require(np.isfinite(error) and error < TOL, f"{label}: {error}")
    errors[label] = max(errors.get(label, 0.), error)


def trace_norm(a):
    return float(np.sum(np.linalg.svd(a, compute_uv=False)))


def total_charges(resource_charges):
    return (np.array([0, 1])[:, None] + resource_charges[None, :]).reshape(-1)


def twirl(a, charges):
    return a * (charges[:, None] == charges[None, :])


def induced_effect(e, tau):
    d = len(tau)
    return np.einsum("ab,ibja->ij", tau, e.reshape(2, d, 2, d))


def feasible(e, charges, label, errors):
    close(e, e.conj().T, label + "_Hermitian", errors)
    close(e, twirl(e, charges), label + "_invariant", errors)
    spectrum = np.linalg.eigvalsh(e)
    require(spectrum.min() >= -TOL and spectrum.max() <= 1 + TOL, label + "_effect_bounds")


def phase_optimum(tau, resource_charges):
    delta = twirl(np.kron(Y, tau), total_charges(resource_charges))
    values, vectors = np.linalg.eigh(delta)
    # Half weight on the kernel is also Helstrom optimal and yields a valid POVM.
    weights = np.where(values > 1e-12, 1., np.where(values < -1e-12, 0., .5))
    effect = (vectors * weights) @ vectors.conj().T
    return .5 + trace_norm(delta) / 4, effect


def adjacent_mode_norm(tau, charges):
    result = 0.
    for q in np.unique(charges):
        rows, cols = np.flatnonzero(charges == q), np.flatnonzero(charges == q + 1)
        if len(cols):
            result += trace_norm(tau[np.ix_(rows, cols)])
    return result


def support_optimum(w, tau, resource_charges):
    matrix = twirl(np.kron(w, tau), total_charges(resource_charges))
    values, vectors = np.linalg.eigh(matrix)
    effect = (vectors * (values > 0)) @ vectors.conj().T
    return float(np.maximum(values, 0).sum()), effect


def random_invariant_effect(rng, charges):
    size = len(charges)
    result = np.zeros((size, size), complex)
    for q in np.unique(charges):
        indices = np.flatnonzero(charges == q)
        a = rng.normal(size=(len(indices), len(indices))) + 1j * rng.normal(size=(len(indices), len(indices)))
        vectors, _ = np.linalg.qr(a)
        block = (vectors * rng.uniform(size=len(indices))) @ vectors.conj().T
        result[np.ix_(indices, indices)] = block
    return result


def analytic_charge_block(time, g=1., k=1.):
    radius = np.hypot(g, k / 2)
    alpha = 0. if radius == 0 else k / (2 * radius)
    s, c = np.sin(radius * time), np.cos(radius * time)
    delta = k * time / 2
    rotation = np.cos(delta) * I - 1j * np.sin(delta) * X
    a_dagger = rotation.conj().T @ (c * I + 1j * alpha * s * X)
    d_block = rotation @ (c * I + 1j * alpha * s * X)
    e_block = np.cos(2 * delta) * I - 1j * np.sin(2 * delta) * X
    b = (BASE.ZERO @ a_dagger + d_block @ BASE.ZERO @ e_block.conj().T) / 4
    norm = .5 * np.sqrt(c ** 2 + alpha ** 2 * s ** 2)
    return b, norm


def channel_kraus(u):
    blocks = u.reshape(2, 4, 2, 4)
    return [blocks[a, :, b, :] / np.sqrt(2) for a in range(2) for b in range(2)]


def apply_channel(tau, kraus):
    return sum((k @ tau @ k.conj().T for k in kraus), np.zeros_like(tau))


def dual_effect(e, kraus):
    lifted = [np.kron(I, k) for k in kraus]
    return sum((k.conj().T @ e @ k for k in lifted), np.zeros_like(e))


def score(f):
    return float((1 + abs(np.trace(f @ Y))) / 2)


def run_checks():
    errors = {}
    rng = np.random.default_rng(SEED)
    q_r = np.array([0, 0, 1, 1])
    q_total = total_charges(q_r)
    u = BASE.unitary(BASE.hamiltonian(), BASE.T)
    tau0 = np.kron(BASE.PLUS, BASE.ZERO)
    tau1 = BASE.prime(u, tau0)
    p0, e0 = phase_optimum(tau0, q_r)
    p1, e1 = phase_optimum(tau1, q_r)
    f0, f1 = BASE.effect(u, tau0), BASE.effect(u, tau1)
    before_score, after_score = score(f0), score(f1)
    feasible(e0, q_total, "optimal_before", errors)
    feasible(e1, q_total, "optimal_after", errors)
    close(score(induced_effect(e0, tau0)), p0, "optimal_before_attained", errors)
    close(score(induced_effect(e1, tau1)), p1, "optimal_after_attained", errors)
    close(p0, .75, "initial_optimum", errors)
    require(before_score > p1 + .03, "before hardware beats EVERY symmetric after measurement")
    close(abs(f0[0, 1]) - trace_norm(tau1[:2, 2:]) / 2,
          before_score - p1, "unattainable_effect_distance_lower_bound", errors)
    phase_rotation = np.diag([1., 1j])
    lifted_rotation = np.kron(phase_rotation, np.eye(4))
    span_dimensions = []
    for tau, optimal_y in [(tau0, e0), (tau1, e1)]:
        optimal_x = lifted_rotation @ optimal_y @ lifted_rotation.conj().T
        feasible(optimal_x, q_total, "rotated_phase_effect", errors)
        fy, fx = induced_effect(optimal_y, tau), induced_effect(optimal_x, tau)
        diagonal_effect = np.kron(N, np.eye(4))
        feasible(diagonal_effect, q_total, "diagonal_system_effect", errors)
        close(induced_effect(diagonal_effect, tau), N, "diagonal_effect_attained", errors)
        dimension = int(np.linalg.matrix_rank(np.column_stack([a.reshape(-1) for a in [I, N, fx, fy]])))
        require(dimension == 4, "both capability sets span the same full qubit algebra")
        span_dimensions.append(dimension)

    # Optional enlargement of the ORIGINAL hardware menu: allow any exposure
    # duration, but still only this H and the n_D pointer, with no added pulses.
    radius = np.sqrt(1.25)
    alpha, beta = .5 / radius, 1 / radius
    s0, c0 = np.sin(radius * BASE.T), np.cos(radius * BASE.T)
    delta0 = BASE.T / 2
    a0 = c0 * np.cos(delta0) - alpha * s0 * np.sin(delta0)
    b0 = c0 * np.sin(delta0) + alpha * s0 * np.cos(delta0)
    d0 = alpha * b0
    orbit_p0 = .5 + beta / 4
    orbit_p1 = .5 + beta * (np.hypot(a0, d0) + abs(d0)) / 4
    orbit_t0 = np.pi / (4 * radius)
    orbit_t1 = (np.arctan2(-a0, -d0) % (2 * np.pi)) / (2 * radius)
    close(score(BASE.effect(BASE.unitary(BASE.hamiltonian(), orbit_t0), tau0)),
          orbit_p0, "hardware_time_optimum_before_attained", errors)
    close(score(BASE.effect(BASE.unitary(BASE.hamiltonian(), orbit_t1), tau1)),
          orbit_p1, "hardware_time_optimum_after_attained", errors)
    for time in np.linspace(0, np.pi / radius, 33):
        test_u = BASE.unitary(BASE.hamiltonian(), time)
        y_after = beta * (a0 * np.sin(2 * radius * time)
                          + d0 * np.cos(2 * radius * time) - d0) / 4
        close(BASE.bloch_coefficients(BASE.effect(test_u, tau1))[2], y_after,
              "hardware_orbit_analytic_phase_coefficient", errors)
        require(score(BASE.effect(test_u, tau0)) <= orbit_p0 + TOL
                and score(BASE.effect(test_u, tau1)) <= orbit_p1 + TOL,
                "hardware_orbit_bounds")

    # Exact Helstrom optimization, compared to the adjacent-charge block formula
    # and tested using independent Born probabilities on all system matrix units.
    matrix_units = [np.outer(I[:, i], I[:, j]) for i in range(2) for j in range(2)]
    for _ in range(80):
        tau = BASE.random_density(rng, 4)
        optimum, e = phase_optimum(tau, q_r)
        feasible(e, q_total, "random_optimal", errors)
        f = induced_effect(e, tau)
        close(optimum, .5 + adjacent_mode_norm(tau, q_r) / 2, "charge_block_Helstrom_identity", errors)
        close(score(f), optimum, "random_optimal_attainment", errors)
        close(abs(f[0, 1]), trace_norm(tau[:2, 2:]) / 2,
              "offdiagonal_bound_attained", errors)
        for a in matrix_units:
            close(np.trace(f @ a), np.trace(e @ np.kron(a, tau)), "all_input_Born_rule", errors)
        trial = random_invariant_effect(rng, q_total)
        trial_f = induced_effect(trial, tau)
        require(abs(trial_f[0, 1]) <= trace_norm(tau[:2, 2:]) / 2 + TOL,
                "offdiagonal bound for arbitrary effect")
        require(score(trial_f) <= optimum + TOL, "trial does not beat optimum")

    for _ in range(60):
        time = rng.uniform(0, 3)
        g, k = rng.uniform(-2, 2, 2)
        test_u = BASE.unitary(BASE.hamiltonian(g, k), time)
        post = BASE.prime(test_u, tau0)
        b, bnorm = analytic_charge_block(time, g, k)
        close(post[:2, 2:], b, "analytic_charge_coherence_matrix", errors)
        close(trace_norm(b), bnorm, "analytic_charge_coherence_norm", errors)
        close(phase_optimum(post, q_r)[0], .5 + bnorm / 2, "analytic_capacity", errors)
        mixed_post = BASE.prime(test_u, np.kron(BASE.PLUS, I / 2))
        close(phase_optimum(mixed_post, q_r)[0], .5 + bnorm / 2,
              "mixed_memory_same_phase_capacity", errors)

    # Construct the simulation map for full effect-set inclusion, not merely
    # the one discrimination witness: pull any after effect through Phi*.
    kraus = channel_kraus(u)
    close(sum((k.conj().T @ k for k in kraus), np.zeros((4, 4), complex)),
          np.eye(4), "priming_channel_trace_preserving", errors)
    close(apply_channel(tau0, kraus), tau1, "priming_Kraus_matches_partial_trace", errors)
    for _ in range(80):
        post_effect = random_invariant_effect(rng, q_total)
        pre_effect = dual_effect(post_effect, kraus)
        feasible(pre_effect, q_total, "pulled_back_effect", errors)
        close(induced_effect(pre_effect, tau0), induced_effect(post_effect, tau1),
              "full_effect_inclusion_constructive_witness", errors)
        w = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
        w = (w + w.conj().T) / 2
        sup0, opt0 = support_optimum(w, tau0, q_r)
        sup1, opt1 = support_optimum(w, tau1, q_r)
        close(np.trace(w @ induced_effect(opt0, tau0)), sup0, "support_before_attained", errors)
        close(np.trace(w @ induced_effect(opt1, tau1)), sup1, "support_after_attained", errors)
        require(sup1 <= sup0 + TOL, "support_function_inclusion")
        arbitrary = BASE.random_density(rng, 4)
        angle = rng.uniform(-np.pi, np.pi)
        rotation = np.diag(np.exp(-1j * angle * q_r))
        close(apply_channel(rotation @ arbitrary @ rotation.conj().T, kraus),
              rotation @ apply_channel(arbitrary, kraus) @ rotation.conj().T,
              "priming_channel_covariance", errors)

    # Retain the OLD input as part of the reference, without adding a new
    # dynamical model. A fresh test input gives a 16x16 measurement comparison.
    all0 = np.kron(I / 2, tau0)
    all1 = u @ all0 @ u.conj().T
    q_all = np.diag(BASE.Q).real.astype(int)
    full_p0, _ = phase_optimum(all0, q_all)
    full_p1, _ = phase_optimum(all1, q_all)
    close(full_p0, .75, "retained_global_capacity_before", errors)
    close(full_p1, .75, "retained_global_capacity_after", errors)
    lifted_u = np.kron(I, u)
    full_charges = total_charges(q_all)
    for _ in range(20):
        after_e = random_invariant_effect(rng, full_charges)
        before_e = lifted_u.conj().T @ after_e @ lifted_u
        feasible(before_e, full_charges, "global_pullback", errors)
        close(induced_effect(before_e, all0), induced_effect(after_e, all1),
              "retained_global_effect_set_unitary_equivalence", errors)
        close(lifted_u @ before_e @ lifted_u.conj().T, after_e,
              "global_pullback_has_inverse", errors)

    d0 = BASE.reduced(tau0, [0], (2, 2))
    d1 = BASE.reduced(tau1, [0], (2, 2))
    d_p0, _ = phase_optimum(d0, np.array([0, 1]))
    d_p1, _ = phase_optimum(d1, np.array([0, 1]))
    close(d_p1, .5 + abs(d1[0, 1]) / 2, "detector_only_capacity", errors)
    require(d_p1 < p1, "accessible memory correlations help")

    # With an unrestricted phase-sensitive apparatus, the resource is not
    # needed: directly measure Y. This violates the declared Q symmetry.
    unrestricted_e = np.kron((I + Y) / 2, np.eye(4))
    require(np.linalg.norm(unrestricted_e - twirl(unrestricted_e, q_total), 2) > .1,
            "unrestricted_control_is_not_symmetric")
    for tau in [tau0, tau1]:
        close(score(induced_effect(unrestricted_e, tau)), 1., "unrestricted_perfect_control", errors)
    for time in [0., BASE.T, np.pi / 2]:
        control_post = BASE.prime(BASE.unitary(BASE.hamiltonian(g=0), time), tau0)
        close(phase_optimum(control_post, q_r)[0], .75, "no_exchange_no_capability_loss", errors)

    return {
        "status": "passed", "seed": SEED, "tolerance": TOL,
        "python": platform.python_version(), "numpy": np.__version__,
        "fixed_hardware_success_before_after": [before_score, after_score],
        "same_H_pointer_arbitrary_duration_optimum_before_after": [orbit_p0, orbit_p1],
        "same_H_pointer_optimizing_durations": [orbit_t0, orbit_t1],
        "symmetric_DM_optimum_before_after": [p0, p1],
        "symmetric_D_only_optimum_before_after": [d_p0, d_p1],
        "symmetric_retained_old_input_optimum_before_after": [full_p0, full_p1],
        "unrestricted_optimum_before_after": [1., 1.],
        "primary_resource_charge_coherence_norm_before_after": [trace_norm(tau0[:2, 2:]), trace_norm(tau1[:2, 2:])],
        "symmetric_effect_linear_span_dimensions_before_after": span_dimensions,
        "before_fixed_hardware_minus_after_symmetric_ceiling": before_score - p1,
        "after_optimization_recovers_over_fixed_readout": p1 - after_score,
        "random_state_optimization_cases": 80, "Born_matrix_unit_checks": 320,
        "analytic_charge_block_cases": 60, "constructive_inclusion_checks": 80,
        "global_equivalence_checks": 20, "support_direction_checks": 80,
        "max_residuals": errors,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "model_source_sha256": hashlib.sha256(BASE_PATH.read_bytes()).hexdigest(),
        "scope": "Single-copy, deterministic measurement statistics; fixed Q-invariant "
                 "measurement class before and after. Full symmetric controls are a "
                 "benchmark upper envelope, not derived hardware access. Old input "
                 "unavailable except in the explicit retained-resource control. "
                 "No fresh phase reference, postselection advantage, entropy calculation, "
                 "cosmological selector, or Lean proof."
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    encoded = json.dumps(run_checks(), sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.write_text(encoded, encoding="utf-8")
    print(encoded, end="")


if __name__ == "__main__":
    main()
