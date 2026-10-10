"""Small matrix checks for the transport applicability note, not a selector study."""

import math

import numpy as np


I2 = np.eye(2, dtype=complex)
I4 = np.eye(4, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
G = np.kron(X, Y)
bell = np.array([1, 0, 0, 1], dtype=complex) / math.sqrt(2)
rho = np.outer(bell, bell.conj())
TOL = 1e-12


def require_close(actual, expected):
    if not np.allclose(actual, expected, atol=TOL, rtol=0):
        raise AssertionError(f"Matrix mismatch: {actual!r} != {expected!r}")


def trace_b(matrix):
    return np.trace(matrix.reshape(2, 2, 2, 2), axis1=1, axis2=3)


def entropy(matrix):
    values = np.linalg.eigvalsh(matrix)
    if np.min(values) < -TOL:
        raise AssertionError("Negative eigenvalue beyond rounding tolerance")
    values = values[values > TOL]
    return float(-np.sum(values * np.log2(values)))


def unitary(theta):
    return math.cos(theta) * I4 - 1j * math.sin(theta) * G


def check_horizontal_generator():
    require_close(G @ G, I4)
    require_close(G, G.conj().T)
    for pauli in (I2, X, Y, Z):
        require_close(np.trace(np.kron(pauli, I2).conj().T @ G), 0)
        require_close(np.trace(np.kron(I2, pauli).conj().T @ G), 0)


def check_fixed_state_pullback():
    for theta in np.linspace(0, math.pi / 4, 17):
        U = unitary(theta)
        require_close(U.conj().T @ U, I4)
        reduced = trace_b(U.conj().T @ rho @ U)
        expected = np.diag([(1 + math.sin(2 * theta)) / 2,
                            (1 - math.sin(2 * theta)) / 2])
        require_close(reduced, expected)
    require_close(entropy(trace_b(rho)), 1)
    U = unitary(math.pi / 4)
    require_close(entropy(trace_b(U.conj().T @ rho @ U)), 0)


def check_co_transport():
    for theta in np.linspace(0, math.pi / 2, 17):
        U = unitary(theta)
        moved_state = U @ rho @ U.conj().T
        require_close(U.conj().T @ moved_state @ U, rho)
        require_close(entropy(trace_b(U.conj().T @ moved_state @ U)), 1)


def check_returned_algebra():
    U = unitary(math.pi / 2)
    require_close(U, -1j * G)
    for pauli in (I2, X, Y, Z):
        moved = U @ np.kron(pauli, I2) @ U.conj().T
        require_close(moved, np.kron(trace_b(moved) / 2, I2))
    require_close(entropy(trace_b(U.conj().T @ rho @ U)), 1)


def check_reparameterized_horizontal_lift():
    for r in np.linspace(0, 1, 17):
        theta = math.pi * (r + r * r) / 8
        speed = math.pi * (1 + 2 * r) / 8
        U = unitary(theta)
        derivative = speed * (-math.sin(theta) * I4 - 1j * math.cos(theta) * G)
        require_close(U.conj().T @ derivative, -1j * speed * G)


def check_generator_is_not_stationary_on_bell():
    commutator = G @ rho - rho @ G
    require_close(np.linalg.norm(commutator, "fro") ** 2, 2)


if __name__ == "__main__":
    checks = [check_horizontal_generator, check_fixed_state_pullback,
              check_co_transport, check_returned_algebra,
              check_reparameterized_horizontal_lift,
              check_generator_is_not_stationary_on_bell]
    for check in checks:
        check()
        print(f"PASS {check.__name__}")
    print(f"{len(checks)}/{len(checks)} bounded checks passed; not a theorem audit.")
