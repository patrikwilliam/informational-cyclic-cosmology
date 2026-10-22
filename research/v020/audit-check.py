"""Second-pass checks using the record-block generator, not jump-time quadrature."""

import json
import math

import numpy as np

import check as original


def norm(value):
    return float(np.linalg.norm(value))


def evolve_records(measurement, coupling=0.35, fault_rate=0.0, degree=80):
    nf, gamma, horizon, omega = 3, 0.7, 1.3, 0.8
    hf = np.diag([0.0, 0.9, 2.2])
    q = np.array([[0.2, 0.6, 0.1j], [0.6, -0.3, 0.4], [-0.1j, 0.4, 0.1]])
    h = np.kron(hf, original.I2) + np.kron(np.eye(nf), omega * original.Z / 2)
    h += coupling * np.kron(q, original.Z)
    m = np.array([np.kron(np.eye(nf), item) for item in measurement])
    count = 22 if fault_rate else 21
    injection = np.kron(np.eye(nf), np.array([[1], [1]]) / np.sqrt(2))
    basis = np.eye(nf * nf).reshape(nf * nf, nf, nf)
    initial = np.zeros((nf * nf, count, 2 * nf, 2 * nf), dtype=complex)
    initial[:, 0] = injection @ basis @ injection.conj().T

    def generator(rho):
        result = -1j * (h @ rho - rho @ h)
        result[:, :5] -= gamma * rho[:, :5]
        for j in range(4):
            result[:, 1 + j] += gamma * (m[j] @ rho[:, 0] @ m[j].conj().T)
            for k in range(4):
                result[:, 5 + 4 * j + k] += gamma * (m[k] @ rho[:, 1 + j] @ m[k].conj().T)
        if fault_rate:
            result[:, :21] -= fault_rate * rho[:, :21]
            result[:, 21] += fault_rate * rho[:, :21].sum(axis=1)
        return result

    result = initial.copy()
    term = initial.copy()
    for n in range(1, degree + 1):
        term = horizon / n * generator(term)
        result += term
    probabilities = np.trace(result, axis1=-2, axis2=-1)
    effects = probabilities.reshape(nf, nf, count).transpose(2, 1, 0)

    # Bound the Taylor remainder in the sum-of-block Frobenius norm per input.
    bound = horizon * (2 * np.linalg.norm(h, ord=2) + 3 * gamma + 2 * fault_rate)
    tail = math.exp(bound + (degree + 1) * math.log(bound) - math.lgamma(degree + 2))
    return effects, tail


def marginals(records):
    pairs = records[5:21].reshape(4, 4, 3, 3)
    return records[1:5] + pairs.sum(axis=1), pairs.sum(axis=0)


def real_vector(matrix):
    return np.concatenate([matrix.real.ravel(), matrix.imag.ravel()])


def run_math():
    _, reference = original.evaluate(24, 0.35)
    records, tail = evolve_records(original.M)
    coarse, _ = evolve_records(original.M, degree=64)
    first, second = marginals(records)

    # Same POVM, but a different fixed instrument prepares the lower Z level.
    down = np.array([0, 1], dtype=complex)
    reset = []
    for effect in original.F:
        _, eigenvectors = np.linalg.eigh(effect)
        reset.append(np.outer(down, eigenvectors[:, -1].conj()) / np.sqrt(2))
    reset = np.array(reset)
    reset_effects = np.array([m.conj().T @ m for m in reset])
    reset_records, _ = evolve_records(reset)
    reset_first, reset_second = marginals(reset_records)
    q2 = 1 - np.exp(-0.7 * 1.3) * (1 + 0.7 * 1.3)
    reset_prediction = np.array([q2 * effect[1, 1] * np.eye(3) for effect in original.F])

    # Verify the finite-compression separation argument in this surrogate.
    matrices = [np.eye(3), *first]
    design = np.column_stack([real_vector(item) for item in matrices])
    coefficients = np.linalg.lstsq(design, real_vector(second[0]), rcond=None)[0]
    residual = second[0] - sum(c * item for c, item in zip(coefficients, matrices))
    residual = (residual + residual.conj().T) / 2
    size = np.linalg.norm(residual, ord=2)
    assert size > 1e-8
    offset = residual / (6 * size)
    plus, minus = np.eye(3) / 3 + offset, np.eye(3) / 3 - offset
    first_gap = max(abs(np.trace(a @ (plus - minus))) for a in first)
    second_gap = abs(np.trace(second[0] @ (plus - minus)))

    eta = 0.09
    failed, fault_tail = evolve_records(original.M, fault_rate=eta)
    survival = np.exp(-eta * 1.3)
    _, zero_reference = original.evaluate(16, 0.0)
    zero_records, _ = evolve_records(original.M, coupling=0.0)
    errors = {
        "generator_vs_quadrature": norm(records - reference),
        "taylor_64_vs_80": norm(records - coarse),
        "record_normalization": norm(records.sum(axis=0) - np.eye(3)),
        "same_povm_under_reset": norm(reset_effects - original.F),
        "reset_first_marginal": norm(reset_first - first),
        "reset_second_scalar_formula": norm(reset_second - reset_prediction),
        "finite_witness_first_gap": float(first_gap),
        "finite_witness_trace": max(abs(np.trace(plus) - 1), abs(np.trace(minus) - 1)),
        "retention_survival": norm(failed[:21] - survival * records),
        "retention_failure": norm(failed[21] - (1 - survival) * np.eye(3)),
        "zero_coupling_generator": norm(zero_records - zero_reference),
    }
    assert max(errors.values()) < 1e-10, errors
    minimum = float(min(np.linalg.eigvalsh(plus).min(), np.linalg.eigvalsh(minus).min()))
    assert minimum > 0 and second_gap > 1e-7
    return {
        "status": "passed",
        "errors": {k: float(v) for k, v in errors.items()},
        "finite_witness_second_gap": float(second_gap),
        "finite_witness_minimum_eigenvalue": minimum,
        "analytic_truncation_bound_per_basis_input": tail,
        "fault_truncation_bound_per_basis_input": fault_tail,
        "scope": "Finite-generator diagnostics and instrument counterexample; not a numerical continuum proof.",
    }


def run_physics_control():
    i, x, y, z = original.I2, original.X, original.Y, original.Z
    exchange = (np.kron(x, x) + np.kron(y, y)) / 2
    additive_energy = (np.kron(z, i) + np.kron(i, z)) / 2
    values, vectors = np.linalg.eigh(exchange)
    unitary = (vectors * np.exp(-1j * values * 0.6)) @ vectors.conj().T
    pointer = (i + z) / 2
    joint_effect = unitary.conj().T @ np.kron(i, pointer) @ unitary

    def induced(apparatus):
        return np.einsum("ba,satb->st", apparatus, joint_effect.reshape(2, 2, 2, 2))

    stationary = induced(np.diag([0.37, 0.63]))
    coherent = induced((i + x) / 2)
    energy_error = norm(unitary @ additive_energy - additive_energy @ unitary)
    stationary_error = norm(stationary @ z - z @ stationary)
    coherent_signal = norm(coherent @ z - z @ coherent)
    assert energy_error < 1e-14 and stationary_error < 1e-14 and coherent_signal > 0.1
    return {
        "status": "passed",
        "additive_energy_commutator": energy_error,
        "stationary_apparatus_effect_commutator": stationary_error,
        "coherent_apparatus_effect_commutator": coherent_signal,
        "scope": "Control of the restricted symmetry argument only; not a realization of the tetrahedral tick instrument.",
    }


if __name__ == "__main__":
    print(json.dumps({"mathematics": run_math(), "physics_control": run_physics_control()}, indent=2))
