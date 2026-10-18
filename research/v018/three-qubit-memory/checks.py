#!/usr/bin/env python3
"""Bounded simultaneous S-D exchange and D-M recording diagnostics."""

import argparse
import hashlib
import json
from pathlib import Path
import platform

import numpy as np


TOL = 2e-10
SEED = 20261015
I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], complex)
Y = np.array([[0, -1j], [1j, 0]], complex)
Z = np.diag([1, -1]).astype(complex)
N = (I - Z) / 2
ZERO = I - N
PLUS = (I + X) / 2
T = np.pi / 4


def tensor(*args):
    result = np.ones((1, 1), complex)
    for a in args:
        result = np.kron(result, a)
    return result


Q = tensor(N, I, I) + tensor(I, N, I)
PD = tensor(I, N, I)
PM = tensor(I, I, N)
XM = tensor(I, I, X)
EXCHANGE = (tensor(X, X, I) + tensor(Y, Y, I)) / 2
RECORD = tensor(I, N, X)


def require(condition, label):
    if not condition:
        raise RuntimeError(label)


def close(actual, expected, label, errors):
    error = float(np.max(np.abs(np.asarray(actual) - np.asarray(expected))))
    require(np.isfinite(error) and error < TOL, f"{label}: {error}")
    errors[label] = max(errors.get(label, 0.0), error)


def comm(a, b):
    return a @ b - b @ a


def hamiltonian(g=1.0, k=1.0, omega=0.0):
    return omega * Q + g * EXCHANGE + k * RECORD


def unitary(h, time):
    values, vectors = np.linalg.eigh(h)
    return (vectors * np.exp(-1j * values * time)) @ vectors.conj().T


def analytic_unitary(time, g=1.0, k=1.0, omega=0.0):
    """Solve the conserved memory-X sectors and 0/1/2 excitation blocks."""
    result = np.zeros((8, 8), complex)
    radius = np.hypot(g, k / 2)
    cosine = np.cos(radius * time)
    sinc = time if radius == 0 else np.sin(radius * time) / radius
    for mu in [-1, 1]:
        block = np.zeros((4, 4), complex)
        block[0, 0] = 1
        block[3, 3] = np.exp(-1j * (2 * omega + mu * k) * time)
        generator = np.array([[mu * k / 2, g], [g, -mu * k / 2]])
        block[1:3, 1:3] = (np.exp(-1j * (omega + mu * k / 2) * time)
                           * (cosine * I - 1j * sinc * generator))
        result += tensor(block, (I + mu * X) / 2)
    return result


def reduced(rho, keep, dimensions=(2, 2, 2)):
    """Partial trace retaining factors in their original order."""
    dimensions = list(dimensions)
    result = rho.reshape(dimensions + dimensions)
    for axis in reversed(range(len(dimensions))):
        if axis not in keep:
            result = np.trace(result, axis1=axis, axis2=axis + len(dimensions))
            dimensions.pop(axis)
    size = int(np.prod(dimensions))
    return result.reshape(size, size)


def effect(u, apparatus, pointer=PD):
    evolved = (u.conj().T @ pointer @ u).reshape(2, 4, 2, 4)
    return np.einsum("ab,ibja->ij", apparatus, evolved)


def evolve(u, system, apparatus):
    return u @ tensor(system, apparatus) @ u.conj().T


def prime(u, apparatus):
    return reduced(evolve(u, I / 2, apparatus), [1, 2])


def distance(a, b):
    return float(np.sum(np.abs(np.linalg.eigvalsh(a - b))) / 2)


def qfi(rho, generator):
    values, vectors = np.linalg.eigh(rho)
    matrix = vectors.conj().T @ generator @ vectors
    return float(sum(2 * (a - b) ** 2 * abs(matrix[i, j]) ** 2 / (a + b)
                     for i, a in enumerate(values) for j, b in enumerate(values)
                     if a + b > 1e-12))


def random_density(rng, dimension):
    a = rng.normal(size=(dimension, dimension)) + 1j * rng.normal(size=(dimension, dimension))
    result = a @ a.conj().T
    return result / np.trace(result)


def bloch_coefficients(a):
    return [float(np.trace(a @ basis).real / 2) for basis in [I, X, Y, Z]]


def phase_success(f):
    return float((1 + abs(np.trace(f @ Y))) / 2)


def analytic_effects(time, g=1., k=1.):
    radius = np.hypot(g, k / 2)
    if radius == 0:
        return I / 2, I / 2
    alpha, beta = k / (2 * radius), g / radius
    s, c = np.sin(radius * time), np.cos(radius * time)
    delta = k * time / 2
    population = beta ** 2 * s ** 2
    y0 = beta * s * c / 2
    y1 = beta * s * ((c ** 2 - alpha ** 2 * s ** 2) * np.cos(delta)
                     - 2 * alpha * s * c * np.sin(delta)) / 2
    return I / 2 + y0 * Y - population * Z / 2, I / 2 + y1 * Y - population * Z / 2


def analytic_record(time, g=1., k=1.):
    radius = np.hypot(g, k / 2)
    cross = 0. if radius == 0 else k / radius * np.sin(radius * time) * np.cos(radius * time)
    trace_distance = abs(np.sin(k * time) + cross) / 2
    return trace_distance, trace_distance * abs(np.sin(k * time))


def analytic_primed_X_blocks(time, g=1., k=1.):
    radius = np.hypot(g, k / 2)
    alpha = 0 if radius == 0 else k / (2 * radius)
    s, c = np.sin(radius * time), np.cos(radius * time)
    blocks = []
    for mu in [-1, 1]:
        coherence = np.exp(1j * mu * k * time / 2) * (c + 1j * mu * alpha * s) / 2
        blocks.append(np.array([[.5, coherence], [coherence.conjugate(), .5]]))
    return blocks


def record_diagnostics(u, memory=ZERO):
    states = [reduced(evolve(u, I / 2, tensor(d, memory)), [2]) for d in [ZERO, N]]
    population_distance = float(abs(np.trace(N @ (states[0] - states[1]))))
    return {"trace_distance": distance(*states),
            "fixed_population_distance": population_distance,
            "fixed_population_success": (1 + population_distance) / 2}, states


def run_checks():
    errors = {}
    rng = np.random.default_rng(SEED)
    h, u = hamiltonian(), unitary(hamiltonian(), T)
    apparatus = tensor(PLUS, ZERO)
    close(comm(h, Q), 0, "charge_conservation", errors)
    close(comm(h, XM), 0, "memory_X_conservation", errors)
    close(comm(PD, Q), 0, "detector_readout_symmetric", errors)
    close(comm(PM, Q), 0, "memory_readout_symmetric", errors)
    require(np.linalg.norm(comm(h, PD), 2) > 0, "not a QND measurement of D")
    require(np.linalg.norm(comm(EXCHANGE, RECORD), 2) > 0,
            "simultaneous interactions do not commute")
    units = [np.outer(I[:, i], I[:, j]) for i in range(2) for j in range(2)]

    for _ in range(80):
        time, g, k, omega = rng.uniform(0, 3, 4)
        full_u = unitary(hamiltonian(g, k, omega), time)
        close(full_u, analytic_unitary(time, g, k, omega),
              "sector_propagator", errors)
        close(full_u.conj().T @ full_u, np.eye(8), "unitarity", errors)
        tau = random_density(rng, 4)
        for pointer in [PD, PM]:
            f = effect(full_u, tau, pointer)
            close(f, f.conj().T, "effect_hermiticity", errors)
            eigs = np.linalg.eigvalsh(f)
            require(eigs.min() >= -TOL and eigs.max() <= 1 + TOL, "effect positivity")
            for matrix_unit in units:
                direct = np.trace(pointer @ evolve(full_u, matrix_unit, tau))
                close(np.trace(f @ matrix_unit), direct, "all_input_Born_rule", errors)
    close(analytic_unitary(T, 0, 0), np.eye(8), "zero_coupling_propagator", errors)

    for _ in range(60):
        time, g, k = rng.uniform(0, 3, 3)
        test_u = unitary(hamiltonian(g, k), time)
        primed = prime(test_u, apparatus)
        f0, f1 = analytic_effects(time, g, k)
        close(effect(test_u, apparatus), f0, "analytic_before_effect", errors)
        close(effect(test_u, primed), f1, "analytic_reuse_effect", errors)
        record, _ = record_diagnostics(test_u)
        td, pd = analytic_record(time, g, k)
        close(record["trace_distance"], td, "analytic_record_trace_distance", errors)
        close(record["fixed_population_distance"], pd, "analytic_record_population_distance", errors)
        for mu, expected in zip([-1, 1], analytic_primed_X_blocks(time, g, k)):
            projector = tensor(I, (I + mu * X) / 2)
            block = reduced(projector @ primed @ projector, [0], (2, 2))
            close(2 * block, expected, "analytic_primed_memory_X_blocks", errors)

        # Dephasing only the unobserved X sectors does not change D readout.
        arbitrary_tau = random_density(rng, 4)
        xdm = tensor(I, X)
        dephased_tau = (arbitrary_tau + xdm @ arbitrary_tau @ xdm) / 2
        close(effect(test_u, arbitrary_tau), effect(test_u, dephased_tau),
              "arbitrary_apparatus_X_dephasing_equivalence", errors)
        close(effect(test_u, prime(test_u, arbitrary_tau)),
              effect(test_u, prime(test_u, dephased_tau)),
              "reuse_X_dephasing_equivalence", errors)

    after = prime(u, apparatus)
    before_effect, after_effect = effect(u, apparatus), effect(u, after)
    records, _ = record_diagnostics(u)
    require(records["fixed_population_distance"] > 1e-3, "readable initial-D record")
    require(np.linalg.norm(comm(before_effect, after_effect), 2) > 1e-3,
            "same_duration_effect_change")
    product_after = tensor(reduced(after, [0], (2, 2)), reduced(after, [1], (2, 2)))
    product_effect = effect(u, product_after)
    initial = tensor(I / 2, apparatus)
    final = u @ initial @ u.conj().T
    close(qfi(initial, Q), 1, "initial_global_QFI", errors)
    close(qfi(final, Q), 1, "preserved_global_QFI", errors)
    close(np.trace(Q @ initial), np.trace(Q @ final), "preserved_charge_mean", errors)
    close(np.trace(h @ initial), np.trace(h @ final), "preserved_total_energy", errors)

    # A mixed memory has the same conserved-X diagonal blocks but no local record
    # of the detector preparation. Keep full DM correlations during every reuse.
    mixed = tensor(PLUS, I / 2)
    mixed_record, mixed_states = record_diagnostics(u, I / 2)
    for memory_state in mixed_states:
        close(memory_state, I / 2, "mixed_memory_no_local_record", errors)
    close(effect(u, mixed, PM), I / 2, "mixed_memory_no_record_of_any_system_input", errors)
    tau_blank, tau_mixed = apparatus.copy(), mixed.copy()
    for _ in range(4):
        close(effect(u, tau_blank), effect(u, tau_mixed),
              "record_not_necessary_for_detector_effect", errors)
        close(effect(u, tau_mixed, PM), I / 2, "reused_mixed_memory_no_local_input_record", errors)
        tau_blank, tau_mixed = prime(u, tau_blank), prime(u, tau_mixed)

    controls = {}
    for name, g, k, reference in [
            ("no_memory_coupling", 1., 0., PLUS),
            ("no_exchange", 0., 1., PLUS),
            ("incoherent_reference", 1., 1., I / 2)]:
        control_u = unitary(hamiltonian(g, k), T)
        tau = tensor(reference, ZERO)
        f0, f1 = effect(control_u, tau), effect(control_u, prime(control_u, tau))
        record, _ = record_diagnostics(control_u)
        controls[name] = {"effect_before": bloch_coefficients(f0),
                          "effect_after": bloch_coefficients(f1),
                          "phase_success_before_after": [phase_success(f0), phase_success(f1)],
                          "record": record}
        if name == "no_memory_coupling":
            close(record["trace_distance"], 0, "no_coupling_no_record", errors)
            close(f0, I / 2 + Y / 4 - Z / 4, "two_qubit_before_limit", errors)
            close(f1, I / 2 + Y / (4 * np.sqrt(2)) - Z / 4,
                  "two_qubit_without_intermediate_readout_limit", errors)
        elif name == "no_exchange":
            close(f0, I / 2, "no_exchange_before_uninformative", errors)
            close(f1, I / 2, "no_exchange_after_uninformative", errors)
        else:
            close(comm(f0, N), 0, "incoherent_before_no_phase_access", errors)
            close(comm(f1, N), 0, "incoherent_after_no_phase_access", errors)

    times = []
    for time in [0.9 * T, T, 1.1 * T]:
        timed_u = unitary(h, time)
        f0 = effect(timed_u, apparatus)
        f1 = effect(timed_u, prime(timed_u, apparatus))
        record, _ = record_diagnostics(timed_u)
        contrast = float(np.linalg.norm(comm(f0, f1), 2))
        require(contrast > 1e-3 and record["fixed_population_distance"] > 1e-3,
                "nearby time witness")
        times.append({"time": float(time), "commutator_norm": contrast, "record": record})

    # This represents one uncertain duration per exposure, with independent
    # uncertainty on the calibration and subsequent test exposures.
    nodes, weights = np.polynomial.legendre.leggauss(32)
    jitter_us = [unitary(h, T * (1 + .1 * node)) for node in nodes]
    averaged_after = sum((w * prime(ju, apparatus) for ju, w in zip(jitter_us, weights)),
                         np.zeros((4, 4), complex)) / 2
    averaged_before_effect = sum((w * effect(ju, apparatus) for ju, w in zip(jitter_us, weights)),
                                 np.zeros((2, 2), complex)) / 2
    averaged_after_effect = sum((w * effect(ju, averaged_after) for ju, w in zip(jitter_us, weights)),
                                np.zeros((2, 2), complex)) / 2
    averaged_memory = [sum((w * reduced(evolve(ju, I / 2, tensor(d, ZERO)), [2])
                           for ju, w in zip(jitter_us, weights)), np.zeros((2, 2), complex)) / 2
                       for d in [ZERO, N]]
    jitter_record_distance = float(abs(np.trace(N @ (averaged_memory[0] - averaged_memory[1]))))
    jitter_norm = float(np.linalg.norm(comm(averaged_before_effect, averaged_after_effect), 2))
    require(jitter_record_distance > 1e-3 and jitter_norm > 1e-3, "averaged timing witness")

    # Negatively test a common erroneous shortcut: simultaneous evolution is
    # not either time ordering of two separately applied equal-duration gates.
    sequential_a = unitary(RECORD, T) @ unitary(EXCHANGE, T)
    sequential_b = unitary(EXCHANGE, T) @ unitary(RECORD, T)
    sequence_errors = [float(np.linalg.norm(u - seq, 2)) for seq in [sequential_a, sequential_b]]
    require(min(sequence_errors) > 1e-3, "must not replace simultaneous U by sequential gates")

    return {"status": "passed", "seed": SEED, "tolerance": TOL,
            "python": platform.python_version(), "numpy": np.__version__,
            "random_propagator_cases": 80, "Born_matrix_unit_comparisons": 640,
            "analytic_reuse_and_record_cases": 60,
            "primary": {"g": 1, "k": 1, "omega": 0, "time": float(T),
                        "effect_before_I_X_Y_Z": bloch_coefficients(before_effect),
                        "effect_after_I_X_Y_Z": bloch_coefficients(after_effect),
                        "phase_success_before_after": [phase_success(before_effect), phase_success(after_effect)],
                        "commutator_norm": float(np.linalg.norm(comm(before_effect, after_effect), 2)),
                        "initial_D_record": records,
                        "memory_readout_effect_on_S_I_X_Y_Z": bloch_coefficients(effect(u, apparatus, PM)),
                        "product_replacement_effect_error": float(np.linalg.norm(after_effect - product_effect, 2)),
                        "DM_correlation_distance": distance(after, product_after),
                        "detector_coherence_after": float(2 * abs(reduced(after, [0], (2, 2))[0, 1]))},
            "mixed_memory_record": mixed_record,
            "controls": controls, "nearby_times": times, "max_residuals": errors,
            "uniform_10_percent_timing_uncertainty": {
                "quadrature_nodes": 32, "independent_exposures": True,
                "commutator_norm": jitter_norm, "record_population_distance": jitter_record_distance,
                "phase_success_before_after": [phase_success(averaged_before_effect), phase_success(averaged_after_effect)]},
            "simultaneous_vs_sequential_unitary_errors": sequence_errors,
            "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "scope": "One simultaneous, time-independent three-qubit model. Fresh input "
                     "replacement and readout remain supplied. No entropy, selector, "
                     "autonomous classical memory, broad search, or Lean claim."}


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
