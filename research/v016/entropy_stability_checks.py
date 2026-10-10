"""Bounded finite-matrix diagnostics, not an exact KK-distance computation."""

import argparse
import json
import math
from pathlib import Path

import numpy as np


TOL = 2e-11
SEED = 20261009
I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)


def close(actual, expected):
    if not np.allclose(actual, expected, atol=TOL, rtol=0):
        raise AssertionError(f"Mismatch: {actual!r} != {expected!r}")


def at_most(actual, bound):
    if actual > bound + TOL:
        raise AssertionError(f"{actual} > {bound}")


def opnorm(matrix):
    return float(np.linalg.norm(matrix, ord=2))


def trace_distance(a, b):
    delta = (a - b + (a - b).conj().T) / 2
    return float(np.sum(np.abs(np.linalg.eigvalsh(delta))) / 2)


def entropy(matrix):
    close(matrix, matrix.conj().T)
    close(np.trace(matrix), 1)
    values = np.linalg.eigvalsh(matrix)
    if values.min() < -TOL:
        raise AssertionError("Nonpositive state")
    values = values[values > 0]
    return float(-np.sum(values * np.log2(values)))


def h2(p):
    if not 0 <= p <= 1:
        raise ValueError(p)
    return sum(-x * math.log2(x) for x in (p, 1 - p) if x > 0)


def modulus(d, upper_bound):
    if d < 1 or upper_bound < 0:
        raise ValueError((d, upper_bound))
    if d == 1:
        return 0.0
    t = min(upper_bound, 1 - 1 / d)
    return h2(t) + t * math.log2(d - 1)


def partial_trace(matrix, d, m):
    return np.trace(matrix.reshape(d, m, d, m), axis1=1, axis2=3)


def marginal(matrix, frame, d, m):
    return partial_trace(frame.conj().T @ matrix @ frame, d, m)


def expectation(matrix, frame, d, m):
    return frame @ np.kron(marginal(matrix, frame, d, m), np.eye(m) / m) @ frame.conj().T


def random_matrix(rng, n):
    return rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))


def random_unitary(rng, n, angle):
    raw = random_matrix(rng, n)
    generator = (raw + raw.conj().T) / 2
    generator /= opnorm(generator)
    values, basis = np.linalg.eigh(generator)
    return (basis * np.exp(-1j * angle * values)) @ basis.conj().T


def random_state(rng, n, pure):
    raw = random_matrix(rng, n)
    if pure:
        raw = raw[:, :1]
    state = raw @ raw.conj().T
    return state / np.trace(state)


def check_finite_comparisons():
    rng = np.random.default_rng(SEED)
    cases = 0
    largest_gap = 0.0
    for d, m in ((2, 2), (2, 3), (3, 2), (3, 3), (4, 2)):
        n = d * m
        identity = np.eye(n)
        for pure in (False, True):
            for angle in (0.0, 0.001, 0.01, 0.05, 0.2, 0.9):
                rho = random_state(rng, n, pure)
                u = random_unitary(rng, n, angle)
                close(u.conj().T @ u, identity)
                sa = marginal(rho, identity, d, m)
                sb = marginal(rho, u, d, m)
                ea = expectation(rho, identity, d, m)
                eb = expectation(rho, u, d, m)
                close(np.trace(eb), 1)
                close(expectation(eb, u, d, m), eb)
                close(entropy(eb), entropy(sb) + math.log2(m))
                close(expectation(identity, u, d, m), identity)

                def phi(a):
                    return partial_trace(u.conj().T @ np.kron(a, np.eye(m)) @ u, d, m) / m

                def phi_adjoint(b):
                    return partial_trace(u @ np.kron(b, np.eye(m)) @ u.conj().T, d, m) / m

                close(phi(np.eye(d)), np.eye(d))
                close(phi_adjoint(np.eye(d)), np.eye(d))
                a, b = random_matrix(rng, d), random_matrix(rng, d)
                close(np.trace(phi(a)), np.trace(a))
                close(np.trace(phi_adjoint(b)), np.trace(b))
                close(np.trace(b.conj().T @ phi(a)), np.trace(phi_adjoint(b).conj().T @ a))
                choi = np.zeros((d * d, d * d), dtype=complex)
                for i in range(d):
                    for j in range(d):
                        eij = np.zeros((d, d), dtype=complex)
                        eij[i, j] = 1
                        choi += np.kron(eij, phi(eij))
                at_most(-float(np.linalg.eigvalsh(choi).min()), 0)

                ta = marginal(eb, identity, d, m)
                tb = marginal(ea, u, d, m)
                close(ta, phi_adjoint(sb))
                close(tb, phi(sa))
                at_most(entropy(sb), entropy(ta))
                at_most(entropy(sa), entropy(tb))

                eps = opnorm(u - identity)
                # A proven upper bound on the full unit-ball distance, not a sample estimate.
                kk_upper = min(1.0, 2 * eps)
                at_most(trace_distance(sa, ta), kk_upper)
                at_most(trace_distance(sb, tb), kk_upper)
                at_most(trace_distance(sa, sb), eps)
                gap = abs(entropy(sa) - entropy(sb))
                at_most(gap, modulus(d, kk_upper))
                at_most(gap, modulus(d, eps))

                observable = np.kron(a / opnorm(a), np.eye(m))
                at_most(opnorm(observable - expectation(observable, u, d, m)), 2 * kk_upper)
                frame = random_unitary(rng, n, 1.3)
                moved_rho = frame @ rho @ frame.conj().T
                close(marginal(moved_rho, frame @ u, d, m), sb)
                largest_gap = max(largest_gap, gap)
                cases += 1
    return {"cases": cases, "largest_tested_entropy_gap_bits": largest_gap}


def check_normalizer_and_cotransport():
    rng = np.random.default_rng(SEED + 1)
    rho = random_state(rng, 6, False)
    u = np.kron(random_unitary(rng, 2, 2.0), random_unitary(rng, 3, 1.4))
    close(expectation(rho, u, 2, 3), expectation(rho, np.eye(6), 2, 3))
    close(entropy(marginal(rho, u, 2, 3)), entropy(partial_trace(rho, 2, 3)))
    if opnorm(u - np.eye(6)) < 0.1:
        raise AssertionError("Normalizer control should not be a tiny rotation")
    v = random_unitary(rng, 6, 0.7)
    close(marginal(v @ rho @ v.conj().T, v, 2, 3), partial_trace(rho, 2, 3))


def check_bell_path():
    bell = np.array([1, 0, 0, 1], dtype=complex) / math.sqrt(2)
    rho = np.outer(bell, bell.conj())
    g = np.kron(X, Y)
    for theta in np.linspace(0, math.pi / 2, 33):
        u = math.cos(theta) * np.eye(4) - 1j * math.sin(theta) * g
        sb = marginal(rho, u, 2, 2)
        close(sb, np.diag([(1 + math.sin(2 * theta)) / 2, (1 - math.sin(2 * theta)) / 2]))
        gap = abs(1 - entropy(sb))
        at_most(gap, modulus(2, opnorm(u - np.eye(4))))
    u = (np.eye(4) - 1j * g) / math.sqrt(2)
    close(entropy(marginal(rho, u, 2, 2)), 0)
    close(entropy(marginal(rho, -1j * g, 2, 2)), 1)


def check_monotone_cap():
    for d in (2, 3, 4, 16):
        values = [modulus(d, x) for x in np.linspace(0, 2, 401)]
        at_most(-min(np.diff(values)), 0)
        close(values[-1], math.log2(d))
        for t in (0, 0.01, 0.1, 1 - 1 / d):
            a = np.diag([1 - t] + [t / (d - 1)] * (d - 1))
            pure = np.diag([1.0] + [0.0] * (d - 1))
            close(trace_distance(a, pure), t)
            close(entropy(a), modulus(d, t))
    close(modulus(2, 0.75), 1)
    close(modulus(1, 0.7), 0)
    return {"qubit_bound_at_kk_upper_0_01_bits": modulus(2, 0.01)}


def check_endpoint_error_budget():
    rng = np.random.default_rng(SEED + 2)
    rho = random_state(rng, 6, True)
    a, b = np.eye(6), random_unitary(rng, 6, 0.8)
    va, vb = random_unitary(rng, 6, 0.003), random_unitary(rng, 6, 0.007)
    delta = entropy(marginal(rho, a, 2, 3)) - entropy(marginal(rho, b, 2, 3))
    changed = entropy(marginal(rho, va @ a, 2, 3)) - entropy(marginal(rho, vb @ b, 2, 3))
    budget = sum(modulus(2, min(1.0, 2 * opnorm(v - np.eye(6)))) for v in (va, vb))
    at_most(abs(changed - delta), budget)


def check_dimension_dependence():
    for d in (4, 8):
        n = d * d
        zero = np.zeros(n, dtype=complex)
        zero[0] = 1
        chi = np.zeros(n, dtype=complex)
        chi[[j * d + j for j in range(1, d)]] = 1 / math.sqrt(d - 1)
        p = 1 / math.log2(d - 1)
        theta = math.asin(math.sqrt(p))
        projector = np.outer(zero, zero.conj()) + np.outer(chi, chi.conj())
        rotation = np.outer(chi, zero.conj()) - np.outer(zero, chi.conj())
        u = np.eye(n) + (math.cos(theta) - 1) * projector + math.sin(theta) * rotation
        close(u.conj().T @ u, np.eye(n))
        close(opnorm(u - np.eye(n)), 2 * math.sin(theta / 2))
        sb = marginal(np.outer(zero, zero.conj()), u, d, d)
        close(sb, np.diag([1 - p] + [p / (d - 1)] * (d - 1)))
        close(entropy(sb), 1 + h2(p))
    # Analytic spectra only: these rows do not allocate exponentially large matrices.
    rows = []
    for log_dimension_minus_one in (4, 16, 64, 256, 1024):
        p = 1 / log_dimension_minus_one
        eps = 2 * math.sin(math.asin(math.sqrt(p)) / 2)
        rows.append({"log2_d_minus_one": log_dimension_minus_one,
                     "kk_upper": min(1.0, 2 * eps), "entropy_gap_bits": 1 + h2(p)})
    return {"analytic_growing_dimension_sequence": rows}


def check_protocol_not_algebra_entropy():
    rho = np.diag([1.0, 0.0])
    hadamard = (X + Z) / math.sqrt(2)
    z_probs = np.diag(rho)
    x_probs = np.diag(hadamard @ rho @ hadamard.conj().T).real
    close(h2(float(z_probs[0])), 0)
    close(h2(float(x_probs[0])), 1)
    close(entropy(rho), 0)
    close(entropy(hadamard @ rho @ hadamard.conj().T), 0)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    checks = [check_finite_comparisons, check_normalizer_and_cotransport,
              check_bell_path, check_monotone_cap, check_endpoint_error_budget,
              check_dimension_dependence, check_protocol_not_algebra_entropy]
    report = {"seed": SEED, "absolute_tolerance": TOL, "numpy_version": np.__version__,
              "scope": "Finite diagnostics; no exact KK-distance computation, selector search, or Lean audit",
              "checks": []}
    for check in checks:
        detail = check()
        report["checks"].append({"name": check.__name__, "passed": True, "detail": detail})
        print(f"PASS {check.__name__}")
    report["passed"] = len(checks)
    if args.json:
        args.json.write_text(json.dumps(report, indent=2) + "\n")
    print(f"{len(checks)}/{len(checks)} bounded checks passed; numerical diagnostics, not a theorem audit.")


if __name__ == "__main__":
    main()
