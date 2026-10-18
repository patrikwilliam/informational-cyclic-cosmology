"""Independent implementation of the finite Appendix C bridges.

No imports from the release tests. Linear identities are checked on complete
matrix-unit bases at the primary parameters; this is floating-point evidence,
not an exact proof or a test of physical assumptions.
"""

import hashlib
import json
from pathlib import Path
import platform

import numpy as np


TOL = 1e-11
residuals = {}


def check(name, actual, expected):
    error = float(np.max(np.abs(np.asarray(actual) - np.asarray(expected))))
    if not np.isfinite(error) or error > TOL:
        raise RuntimeError(f"{name}: {error}")
    residuals[name] = max(error, residuals.get(name, 0.0))


def unit(d, i, j):
    result = np.zeros((d, d), complex)
    result[i, j] = 1
    return result


def extract(effect, resource):
    """Recover every effect entry directly from its trace pairing."""
    return np.array([[np.trace(np.kron(unit(2, j, i), resource) @ effect)
                      for j in range(2)] for i in range(2)])


def trace_old(matrix):
    return matrix[:4, :4] + matrix[4:, 4:]


def twirl(matrix, charges):
    return np.where(charges[:, None] == charges[None, :], matrix, 0)


def optimum(resource, charges):
    difference = twirl(np.kron(Y, resource), charges)
    values, vectors = np.linalg.eigh(difference)
    effect = (vectors * (values > 1e-13)) @ vectors.conj().T
    probability = 0.5 + np.abs(values).sum() / 4
    check("positive_spectral_effect_attains", probability,
          0.5 + np.trace(extract(effect, resource) @ Y).real / 2)
    return float(probability), effect


I2 = np.eye(2)
Y = np.array([[0, -1j], [1j, 0]])
H = np.zeros((8, 8), complex)
charges = np.zeros(8, int)
for s in range(2):
    for d in range(2):
        for m in range(2):
            j = 4 * s + 2 * d + m
            charges[j] = s + d
            if s != d:
                H[4 * d + 2 * s + m, j] += 1
            if d:
                H[4 * s + 2 * d + (1 - m), j] += 1
Q = np.diag(charges)
QR = np.diag([0, 0, 1, 1])
check("hermitian_H", H, H.conj().T)
check("charge_conservation", H @ Q, Q @ H)

# Taylor exponential rather than the eigensolver used in the release tests.
T = np.pi / 4
U = np.eye(8, dtype=complex)
term = U.copy()
for order in range(1, 81):
    term = term @ (-1j * T * H) / order
    U += term
check("Taylor_final_term", term, 0)
check("unitarity", U.conj().T @ U, np.eye(8))
check("U_charge_conservation", U @ Q, Q @ U)

ks = []
for i in range(2):
    for j in range(2):
        k = U[4 * i:4 * (i + 1), 4 * j:4 * (j + 1)] / np.sqrt(2)
        ks.append(k)
        check("Kraus_definite_charge_shift", QR @ k - k @ QR, (j - i) * k)
check("Kraus_trace_preservation", sum(k.conj().T @ k for k in ks), np.eye(4))


def channel(r):
    return sum(k @ r @ k.conj().T for k in ks)


def pullback(e):
    return sum(np.kron(I2, k).conj().T @ e @ np.kron(I2, k) for k in ks)


tau0 = np.kron(np.ones((2, 2)) / 2, unit(2, 0, 0))
tau1 = channel(tau0)
check("joint_dual_unital", pullback(np.eye(8)), np.eye(8))
matrix_units = [unit(4, i, j) for i in range(4) for j in range(4)]
for r in matrix_units:
    check("channel_all_matrix_units", channel(r),
          trace_old(U @ np.kron(I2 / 2, r) @ U.conj().T))
    check("channel_covariance_generator", channel(QR @ r - r @ QR),
          QR @ channel(r) - channel(r) @ QR)

invariant_units = [unit(8, i, j) for i in range(8) for j in range(8)
                   if charges[i] == charges[j]]
for e in invariant_units:
    ep = pullback(e)
    check("dual_preserves_full_commutant", Q @ ep, ep @ Q)
    for r in matrix_units:
        check("full_Born_bridge", extract(ep, r), extract(e, channel(r)))

theta = np.pi * np.sqrt(5) / 8
s, c = np.sin(theta), np.cos(theta)
u = 4 * s * s / 5
B = tau1[:2, 2:]
bnorm = float(np.linalg.svd(B, compute_uv=False).sum())
check("coherence_block_formula", bnorm, np.sqrt(1 - u) / 2)
p0, e0 = optimum(tau0, charges)
p1, e1 = optimum(tau1, charges)
check("initial_optimum", p0, 0.75)
check("final_optimum", p1, 0.5 + bnorm / 2)

pointer = np.diag([0, 0, 1, 1, 0, 0, 1, 1])
hardware = U.conj().T @ pointer @ U
f0 = extract(hardware, tau0)
f1 = extract(hardware, tau1)
expected_f0 = I2 / 2 + s * c / np.sqrt(5) * Y - u / 2 * np.diag([1, -1])
check("hardware_formula", f0, expected_f0)
gap = float(abs(f0[0, 1]) - bnorm / 2)
if not gap > 0.0384:
    raise RuntimeError("Strict witness missing")
check("exact_scalar_identity", (s * c / np.sqrt(5)) ** 2 - (bnorm / 2) ** 2,
      1 / 80 + (s * s - 0.5) * (0.75 - s * s) / 5)

# The old input is now part of the retained resource; check the entire
# invariant operator basis under reversible conjugation.
large0 = np.kron(I2 / 2, tau0)
large1 = U @ large0 @ U.conj().T
V = np.kron(I2, U)
large_charges = np.array([fresh + old for fresh in range(2) for old in charges])
largeQ = np.diag(large_charges)
retained_units = [unit(16, i, j) for i in range(16) for j in range(16)
                  if large_charges[i] == large_charges[j]]
for e in retained_units:
    ep = V.conj().T @ e @ V
    check("retained_invariant", largeQ @ ep, ep @ largeQ)
    check("retained_inverse", V @ ep @ V.conj().T, e)
    check("retained_Born_bridge", extract(ep, large0), extract(e, large1))
retained0, _ = optimum(large0, large_charges)
retained1, _ = optimum(large1, large_charges)
check("retained_optima", [retained0, retained1], [0.75, 0.75])

# Genuine phase directions plus sharp populations span M_2 on both sides.
phase = np.diag([1, 1j])
fullphase = np.kron(phase, np.eye(4))
for resource, optimal in [(tau0, e0), (tau1, e1)]:
    f = extract(optimal, resource)
    frot = extract(fullphase.conj().T @ optimal @ fullphase, resource)
    span = np.array([unit(2, 0, 0).ravel(), unit(2, 1, 1).ravel(),
                     f.ravel(), frot.ravel()])
    if np.linalg.matrix_rank(span, tol=1e-10) != 4:
        raise RuntimeError("Full algebra span missing")

result = {
    "status": "passed",
    "scope": "Primary finite setting; numerical linear-basis checks, not formal or physical validation",
    "python": platform.python_version(),
    "numpy": np.__version__,
    "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "resource_matrix_units": len(matrix_units),
    "joint_commutant_matrix_units": len(invariant_units),
    "retained_commutant_matrix_units": len(retained_units),
    "max_residuals": residuals,
    "scores": {"symmetric_before": p0, "symmetric_after": p1,
               "hardware_before": float(0.5 + abs(np.trace(f0 @ Y)) / 2),
               "hardware_after": float(0.5 + abs(np.trace(f1 @ Y)) / 2),
               "retained_before": retained0, "retained_after": retained1},
    "distance_lower_bound": gap,
}
print(json.dumps(result, indent=2))
