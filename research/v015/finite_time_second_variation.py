"""Bounded 4D finite-time derivative checks; no optimization or certification.

Requires NumPy. Protocol: finite-time-second-variation-2026-09-29.md.
"""

import argparse
import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss


I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
PAULIS = (I, X, Y, Z)
PAIRS = [(a, b) for a in range(4) for b in range(4) if (a, b) != (0, 0)]
HERMITIAN = np.array([np.kron(PAULIS[a], PAULIS[b]) / 2 for a, b in PAIRS])
GENERATORS = -1j * HERMITIAN
LOCAL = [i for i, (a, b) in enumerate(PAIRS) if a == 0 or b == 0]
HORIZONS = (0.25, 0.5, 1.0, 2.0, 4.0, 8.0)


def adjoint(matrix):
    return matrix.conj().swapaxes(-1, -2)


def realign(matrix):
    return matrix.reshape(-1, 2, 2, 2, 2).transpose(0, 1, 3, 2, 4).reshape(-1, 4, 4)


def trace_product(left, right):
    return np.einsum("...ij,...ji->...", left, right).real


def propagators(k, horizon, count):
    nodes, weights = leggauss(count)
    times = horizon * (nodes + 1) / 2
    eigenvalues, eigenvectors = np.linalg.eigh(k)
    phase = np.exp(-1j * times[:, None] * eigenvalues)
    matrices = (eigenvectors[None] * phase[:, None, :]) @ eigenvectors.conj().T
    return matrices, weights / 2


def value(k, horizon, count=128):
    w, weights = propagators(k, horizon, count)
    m = realign(w)
    q = m @ adjoint(m)
    return float(weights @ (1 - trace_product(q, q) / 16))


def derivatives(k, horizon, count=128):
    w, weights = propagators(k, horizon, count)
    m = realign(w)
    md = adjoint(m)
    q = m @ md
    commutators = [w @ x - x @ w for x in GENERATORS]
    a = [realign(commutator) for commutator in commutators]
    qi = [term @ md + m @ adjoint(term) for term in a]
    gradient = np.array([-weights @ trace_product(q, term) / 8 for term in qi])
    hessian = np.empty((15, 15))
    for i, xi in enumerate(GENERATORS):
        for j in range(i + 1):
            xj = GENERATORS[j]
            second = ((commutators[i] @ xj - xj @ commutators[i])
                      + (commutators[j] @ xi - xi @ commutators[j])) / 2
            b = realign(second)
            qij = b @ md + m @ adjoint(b) + a[i] @ adjoint(a[j]) + a[j] @ adjoint(a[i])
            integrand = trace_product(qi[i], qi[j]) + trace_product(q, qij)
            hessian[i, j] = hessian[j, i] = -weights @ integrand / 8
    return float(weights @ (1 - trace_product(q, q) / 16)), gradient, hessian


def normal_slice(k):
    _, vectors = np.linalg.eigh(k)
    projectors = [np.outer(vector, vector.conj()) for vector in vectors.T]
    columns = [np.eye(15)[:, index] for index in LOCAL]
    for projector in projectors[:-1]:
        central = (projector - projectors[-1]) / math.sqrt(2)
        columns.append(np.array([np.trace(g @ central).real for g in HERMITIAN]))
    left, singular, _ = np.linalg.svd(np.column_stack(columns), full_matrices=True)
    rank = int(np.count_nonzero(singular > 1e-9))
    return left[:, rank:], left[:, :rank], singular


def conjugate(k, direction, step):
    g = np.einsum("i,ijk->jk", direction, HERMITIAN)
    eigenvalues, eigenvectors = np.linalg.eigh(g)
    u = (eigenvectors * np.exp(-1j * step * eigenvalues)) @ eigenvectors.conj().T
    return u.conj().T @ k @ u


def entropy_bits(k):
    _, vectors = np.linalg.eigh(k)
    state = vectors[:, 0].reshape(2, 2)
    spectrum = np.linalg.eigvalsh(state @ state.conj().T)
    positive = spectrum[spectrum > 1e-13]
    return float(-np.sum(positive * np.log2(positive)))


def cases():
    zi, iz = np.kron(Z, I), np.kron(I, Z)
    xx, yy, zz = (np.kron(p, p) for p in (X, Y, Z))
    return {
        "additive": zi + math.sqrt(2) * iz,
        "diagonal": 2 * zi + 0.5 * iz + zz,
        "bell_123": xx + 2 * yy + 3 * zz,
        "bell_radicals": xx + math.sqrt(2) * yy + math.sqrt(3) * zz,
        "bell_pi": xx + math.sqrt(2) * yy + math.pi * zz,
        "generic": zi + 0.7 * np.kron(I, X) + 0.3 * xx + 0.5 * np.kron(Y, Z) + 0.2 * zz,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    directions = [np.arange(1, 16, dtype=float), np.cos(np.arange(1, 16, dtype=float))]
    directions = [v / np.linalg.norm(v) for v in directions]
    rows = []
    checks = {"quadrature": 0.0, "gradient_difference": 0.0,
              "curvature_difference": 0.0, "vertical_gradient": 0.0,
              "critical_vertical_hessian": 0.0}

    for name, original in cases().items():
        centered = original - np.trace(original) * np.eye(4) / 4
        scale = math.sqrt(float(np.trace(centered @ centered).real) / 4)
        k = centered / scale
        assert np.min(np.diff(np.linalg.eigvalsh(k))) > 1e-8
        normal, vertical, singular = normal_slice(k)
        state_entropy = entropy_bits(k)
        for horizon in HORIZONS:
            f, gradient, hessian = derivatives(k, horizon)
            f64, gradient64, hessian64 = derivatives(k, horizon, count=64)
            checks["quadrature"] = max(checks["quadrature"], abs(f - f64),
                float(np.max(abs(gradient - gradient64))), float(np.max(abs(hessian - hessian64))))
            checks["vertical_gradient"] = max(checks["vertical_gradient"],
                float(np.linalg.norm(vertical.T @ gradient)))
            stationary = np.linalg.norm(gradient) < 1e-9
            if stationary:
                checks["critical_vertical_hessian"] = max(checks["critical_vertical_hessian"],
                    float(np.linalg.norm(hessian @ vertical)))
            curvature = np.linalg.eigvalsh(normal.T @ hessian @ normal)
            for direction in directions:
                for step in (1e-3, 5e-4):
                    plus = value(conjugate(k, direction, step), horizon)
                    minus = value(conjugate(k, direction, -step), horizon)
                    df = (plus - minus) / (2 * step)
                    ddf = (plus + minus - 2 * f) / step**2
                    checks["gradient_difference"] = max(checks["gradient_difference"],
                        abs(df - gradient @ direction))
                    checks["curvature_difference"] = max(checks["curvature_difference"],
                        abs(ddf - direction @ hessian @ direction))
            row = {"case": name, "tau": horizon, "cost": f,
                   "gradient_norm": float(np.linalg.norm(gradient)),
                   "numerically_stationary": bool(stationary),
                   "normal_slice_dimension": int(normal.shape[1]),
                   "normal_hessian_eigenvalues": curvature.tolist(),
                   "vertical_span_singular_values": singular.tolist(),
                   "ground_state_entropy_bits": state_entropy}
            rows.append(row)
            print(f"{name:15s} tau={horizon:4g} F={f:.9f} "
                  f"grad={np.linalg.norm(gradient):.2e} "
                  f"slice={normal.shape[1]} hmin={curvature[0]:+.6e} "
                  f"hmax={curvature[-1]:+.6e} S={state_entropy:.6f}")

    assert checks["quadrature"] < 1e-9, checks
    assert checks["gradient_difference"] < 1e-5, checks
    assert checks["curvature_difference"] < 1e-5, checks
    assert checks["vertical_gradient"] < 1e-9, checks
    assert checks["critical_vertical_hessian"] < 1e-9, checks
    result = {"status": "bounded diagnostic, not a strict-minimum certificate",
              "numpy_version": np.__version__, "checks": checks, "rows": rows}
    if args.output:
        args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(checks, indent=2))


if __name__ == "__main__":
    main()
