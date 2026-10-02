"""Exact-coefficient and rational-bound audit of the fixed Bell candidate.

H0 = XX + 2 YY + 3 ZZ; T0 = 8/sqrt(14).
Only finite 4D algebra. NumPy object arrays hold arbitrary-precision integers.
Trigonometric bounds use Fraction arithmetic, not floating-point quadrature.
"""

import argparse
from fractions import Fraction
import json
from pathlib import Path

import numpy as np


ZERO = np.zeros((8, 8), dtype=object)
I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
PAULIS = (I2, X, Y, Z)
PAIRS = ((1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (3, 2))
LABELS = ("XY", "YX", "XZ", "ZX", "YZ", "ZY")


def encode_literal(matrix):
    # Initial Pauli entries are literal Gaussian integers only.
    assert np.all(matrix.real == np.rint(matrix.real))
    assert np.all(matrix.imag == np.rint(matrix.imag))
    real = np.array(matrix.real.astype(int), dtype=object)
    imag = np.array(matrix.imag.astype(int), dtype=object)
    return np.block([[real, -imag], [imag, real]])


def realign(matrix):
    real = matrix[:4, :4].reshape(2, 2, 2, 2).transpose(0, 2, 1, 3).reshape(4, 4)
    imag = matrix[4:, :4].reshape(2, 2, 2, 2).transpose(0, 2, 1, 3).reshape(4, 4)
    return np.block([[real, -imag], [imag, real]])


def compact(polynomial):
    return {n: a for n, a in polynomial.items() if np.any(a != 0)}


def add(*polynomials):
    result = {}
    for polynomial in polynomials:
        for n, coefficient in polynomial.items():
            result[n] = result.get(n, ZERO) + coefficient
    return compact(result)


def scale(polynomial, factor):
    return compact({n: factor * a for n, a in polynomial.items()})


def multiply(left, right):
    result = {}
    for n, a in left.items():
        for m, b in right.items():
            result[n + m] = result.get(n + m, ZERO) + a @ b
    return compact(result)


def adjoint(polynomial):
    return {(-n): a.T for n, a in polynomial.items()}


def commutator(matrix, generator):
    return matrix @ generator - generator @ matrix


def real_trace(polynomial, denominator, sign=1):
    result = {}
    for n, a in polynomial.items():
        assert sum(a[4 + i, i] for i in range(4)) == 0
        coefficient = Fraction(sign * int(sum(a[i, i] for i in range(4))), denominator)
        if coefficient:
            result[n] = coefficient
    return result


def scalar_add(left, right, sign=1):
    result = dict(left)
    for n, coefficient in right.items():
        result[n] = result.get(n, Fraction(0)) + sign * coefficient
    return {n: c for n, c in result.items() if c}


def sinc_bounds(frequency, terms=192):
    q = Fraction(32 * frequency * frequency, 7)
    term = Fraction(1)
    total = term
    for m in range(terms):
        term *= -q / ((2 * m + 2) * (2 * m + 3))
        total += term
    following = term * -q / ((2 * terms + 2) * (2 * terms + 3))
    assert q < (2 * terms + 2) * (2 * terms + 3)
    # The remaining alternating tail decreases monotonically from this index.
    return min(total, total + following), max(total, total + following)


def integrate(polynomial):
    for n, c in polynomial.items():
        assert polynomial.get(-n, Fraction(0)) == c
    lower = upper = Fraction(0)
    for n, coefficient in polynomial.items():
        lo, hi = sinc_bounds(n)
        if coefficient >= 0:
            lower += coefficient * lo
            upper += coefficient * hi
        else:
            lower += coefficient * hi
            upper += coefficient * lo
    assert upper - lower < Fraction(1, 10**80)
    return lower, upper


def cost_coefficients(projector_numerators):
    m = {e: realign(p) for e, p in projector_numerators.items()}
    q = multiply(m, adjoint(m))
    return scalar_add({0: Fraction(1)}, real_trace(multiply(q, q), 4096), sign=-1)


def serialize(polynomial):
    return {str(n): str(c) for n, c in sorted(polynomial.items())}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    identity = encode_literal(np.eye(4))
    xx, yy, zz = [encode_literal(np.kron(p, p)) for p in (X, Y, Z)]
    patterns = ((1, -1, 1), (-1, 1, 1), (1, 1, -1), (-1, -1, -1))
    projectors = {sx + 2 * sy + 3 * sz: identity + sx * xx + sy * yy + sz * zz
                  for sx, sy, sz in patterns}
    assert sorted(projectors) == [-6, 0, 2, 4]
    assert np.array_equal(sum(projectors.values()), 4 * identity)
    for e, p in projectors.items():
        assert np.array_equal(p @ p, 4 * p)
        assert np.array_equal((xx + 2 * yy + 3 * zz) @ p, e * p)

    generators = [encode_literal(-1j * np.kron(PAULIS[a], PAULIS[b])) for a, b in PAIRS]
    m = {e: realign(p) for e, p in projectors.items()}  # denominator 4
    md = adjoint(m)
    q = multiply(m, md)  # denominator 16
    raw_a = [{e: commutator(p, g) for e, p in projectors.items()} for g in generators]
    a = [{e: realign(p) for e, p in polynomial.items()} for polynomial in raw_a]  # denominator 8
    qi = [add(multiply(ai, md), multiply(m, adjoint(ai))) for ai in a]  # denominator 32
    for term in qi:
        assert not real_trace(multiply(q, term), 4096, sign=-1)

    hessian = [[None] * 6 for _ in range(6)]
    for i, gi in enumerate(generators):
        for j in range(i + 1):
            gj = generators[j]
            b = {e: realign(commutator(raw_a[i][e], gj)
                           + commutator(raw_a[j][e], gi)) for e in projectors}  # denominator 32
            qij = add(multiply(b, md), multiply(m, adjoint(b)),
                      scale(multiply(a[i], adjoint(a[j])), 2),
                      scale(multiply(a[j], adjoint(a[i])), 2))  # denominator 128
            numerator = add(scale(multiply(qi[i], qi[j]), 2), multiply(q, qij))
            hessian[i][j] = hessian[j][i] = real_trace(numerator, 16384, sign=-1)

    eigenvalues = []
    for i in (0, 2, 4):
        assert hessian[i][i] == hessian[i + 1][i + 1]
        for j in range(6):
            if j not in (i, i + 1):
                assert hessian[i][j] == hessian[i + 1][j] == {}
        for sign in (-1, 1):
            polynomial = scalar_add(hessian[i][i], hessian[i][i + 1], sign)
            lower, upper = integrate(polynomial)
            assert lower > Fraction(7, 100)
            eigenvalues.append({"direction": f"({LABELS[i]}{'+' if sign == 1 else '-'}{LABELS[i+1]})/sqrt(2)",
                                "fourier_coefficients": serialize(polynomial),
                                "decimal_display": float((lower + upper) / 2),
                                "certified_lower_bound": "7/100",
                                "interval_width_less_than": "1e-80"})

    bell_cost = cost_coefficients(projectors)
    bell_lower, bell_upper = integrate(bell_cost)
    product_projectors = {}
    for i, energy in enumerate((-6, 0, 2, 4)):
        p = np.zeros((4, 4), dtype=int)
        p[i, i] = 4
        product_projectors[energy] = encode_literal(p)
    basis_numerator = encode_literal(np.array(
        [[0, 0, 1, 1], [1, 1, 0, 0], [-1, 1, 0, 0], [0, 0, 1, -1]], dtype=int))
    assert np.array_equal(basis_numerator.T @ basis_numerator, 2 * identity)
    for energy, projector in projectors.items():
        assert np.array_equal(basis_numerator.T @ projector @ basis_numerator,
                              2 * product_projectors[energy])
    product_cost = cost_coefficients(product_projectors)
    product_lower, product_upper = integrate(product_cost)
    assert bell_lower - product_upper > Fraction(3, 10)
    result = {"status": "exact integer coefficients and rational Taylor enclosures passed",
              "H0": "XX + 2 YY + 3 ZZ", "T0": "8/sqrt(14)",
              "generator_normalization": "-i sigma_a tensor sigma_b / 2",
              "horizontal_gradient_coefficients": "exactly zero",
              "normal_hessian_eigenvalues": eigenvalues,
              "bell_cost_fourier_coefficients": serialize(bell_cost),
              "bell_cost_decimal_display": float((bell_lower + bell_upper) / 2),
              "product_cost_decimal_display": float((product_lower + product_upper) / 2),
              "product_basis_map": "Explicit Bell-basis columns verified by integer matrix identities",
              "gap_above_one_product_competitor_greater_than": "3/10",
              "scope": "Requires analytic quotient and criticality argument; "
                       "not an ICC mechanism or global-minimum certificate."}
    if args.output:
        args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
