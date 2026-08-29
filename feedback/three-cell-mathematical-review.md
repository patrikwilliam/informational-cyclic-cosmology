# Mathematical Review of the Three-Cell Finite Selector Gate

Date: 18 July 2026

Scope: independent audit of the finite-dimensional operator algebra,
factorization manifold, numerical Hessians, optimization evidence, spectra,
and reproducibility in
[`ec_three_cell_selector.py`](../research/ec_three_cell_selector.py) and
[`three-cell-finite-gate.md`](../research/three-cell-finite-gate.md).

## Verdict

The finite construction is mathematically coherent. No contradiction was found
in the fixed-sector Hilbert space, local-algebra projection, fermionic lift, or
six-dimensional quotient tangent calculation. The open-chain selector failure
is numerically decisive. The periodic result establishes two numerically strict
local minima and a failed search for a lower point; it is not a proof of global
minimality.

Two issues should be fixed before integration into v0.1.3:

1. the filling-Hessian statement in the report must be reproduced by the public
   script or removed; and
2. the projection must be described as an exact algebraic formula evaluated by
   a numerical Moore-Penrose pseudoinverse, not as an exact numerical
   projection.

Neither issue changes the reported three-cell classification.

## 1. Fixed-sector dimension and local subspace

The half-filled space is correctly identified as

$$
\mathcal H_{3,6}=\bigwedge^6\mathbb C^{12},
\qquad
\dim\mathcal H_{3,6}=\binom{12}{6}=924.
$$

A number-preserving one-cell operator has charge-block dimension

$$
\sum_{q=0}^{4}\binom{4}{q}^2=70.
$$

Three labelled cells therefore provide 210 matrix-unit generators before
relations are removed. There are three evident exact relations on the fixed
$N=6$ sector: equality of the three representations of the identity gives two
relations, and

$$
N_1+N_2+N_3=6I
$$

gives a third.

The integer Gram matrix was independently row-reduced modulo the prime
$1{,}000{,}003$. Its modular rank is 207. Because a nonzero 207-minor modulo a
prime is nonzero over the integers, this gives rank at least 207 over
$\mathbb Q$; the three exact relations give rank at most 207. Hence the local
subspace dimension is exactly 207.

The closed combinatorial Gram formula was also compared entry by entry with
the intersections of all 210 explicit matrix-unit supports. The maximum
difference was zero.

## 2. Orthogonal projection

Let $B$ map coefficient vectors for the 210 matrix units into
$\mathcal B(\mathcal H_{3,6})$, and let $G=B^\dagger B$. Then

$$
P_{\mathrm{loc}}=B G^+ B^\dagger
$$

is the Hilbert-Schmidt orthogonal projector onto the sum of the three one-cell
operator spaces. Using the Moore-Penrose inverse is correct even though the
generating family is linearly dependent.

The nonzero eigenvalues of the numerical Gram matrix lie between 24.91 and
186.02, so the nonzero subspace has condition number approximately 7.47. The
chosen pseudoinverse threshold is not close to discarding a physical singular
value.

Independent complex-Hermitian tests gave projection Hermiticity,
idempotence, and residual-orthogonality errors below $9\times10^{-14}$. The
Pythagorean identity held to approximately $1.4\times10^{-15}$ relative error.

Required wording: the projector is algebraically specified exactly and
evaluated in floating-point arithmetic. The numerical matrix itself is not an
exact symbolic object.

## 3. Fermionic lift

The blockwise implementation of $\Gamma(W\otimes I_4)$ was compared at 500
random matrix entries with the direct exterior-power formula

$$
\langle I|\Gamma(U)|J\rangle=\det U_{I,J}.
$$

The largest difference was $1.2\times10^{-16}$. The existing representation,
unitarity, and one-body covariance audits are therefore mutually independent
enough to support the lift convention. Exact reproduction of the separately
implemented two-cell Hamiltonians further checks the CAR signs and
normal-ordering convention.

## 4. Candidate manifold and tangent space

For labelled orthonormal cell factors, right multiplication by independent
column phases leaves the embedded local algebras unchanged, and column
permutations only relabel them. The candidate space is therefore

$$
U(3)/(U(1)^3\rtimes S_3),
$$

with real dimension $9-3=6$. The six off-diagonal Hermitian generators used by
the code are Hilbert-Schmidt orthonormal and span the horizontal tangent space.

At 20 independent Haar points for each boundary condition, right-phase and
right-permutation invariance held to $8.7\times10^{-14}$. The production audit
currently checks this only at the site endpoint; it should check a generic Haar
point as well.

## 5. Endpoint coupling and Hessians

The endpoint coupling is well defined because the site contact residual and
kinetic-basis hopping residual vanish to numerical precision, while the two
competing residual norms are positive. The direct objective agrees with the
quadratic residual reconstruction

$$
A(W)+g^2B(W)+2gC(W)
$$

to below $10^{-13}$ at independent Haar points.

Endpoint gradient norms are below $9\times10^{-11}$. Recomputing all endpoint
Hessians with chart steps $2\times10^{-3}$, $10^{-3}$, $5\times10^{-4}$, and
$2.5\times10^{-4}$ gives stable signs:

| Boundary | Endpoint | Smallest eigenvalue range |
|---|---|---:|
| Open | site | $0.1222236$ to $0.1222249$ |
| Open | kinetic | $-0.0465285$ to $-0.0465275$ |
| Periodic | site | $0.4866789$ to $0.4866815$ |
| Periodic | kinetic | $0.2433372$ to $0.2433405$ |

Moving directly along the open kinetic endpoint's lowest Hessian eigenvector
reduces the normalized cost from $0.4529794648$ to $0.4529207581$ at tangent
step 0.05 and to $0.4519231869$ at step 0.2. The open failure therefore does
not depend on convergence of the multi-start optimizer.

The Hessians remain floating-point finite-difference results rather than
interval-certified signs, but their margins and step stability make a sign
error implausible at the reported precision.

## 6. Periodic search and logical status

Positive-definite endpoint Hessians prove only strict local minimality within
the chosen coordinates, assuming the stationary-point calculation. Haar
sampling and multi-start descent add numerical evidence but cannot prove that
no lower point exists on the compact flag manifold.

The report currently states this limitation correctly. It should consistently
use “passes the restricted numerical gate” rather than an unqualified “passes.”
The fixed random seed makes the calculation reproducible, not statistically
certified.

## 7. Spectra and entropy

The even-filling periodic ground states are numerically isolated by gaps much
larger than the eigensolver tolerance. The odd-filling ground spaces are
fourfold degenerate. Suppressing entropy contrasts for degenerate ground spaces
is mathematically conservative because a numerical eigensolver chooses an
arbitrary basis in such a space.

The reduced density matrices have unit trace, and the local-number and
local-parity decompositions satisfy their entropy identities to the asserted
tolerance. These are finite factorization-dependent von Neumann entropies; no
thermodynamic interpretation follows mathematically.

## 8. Reproducibility gap

The report says that endpoint Hessians have the same open-fail/periodic-pass
pattern for $N=4,5,6,7,8$. An independent run confirms that claim: the open
kinetic minimum lies between $-0.0465276$ and $-0.0465274$, while the periodic
endpoint minima remain approximately 0.486681 and 0.243340 at every tested
filling.

However, `filling_controls()` currently evaluates shared Haar landscapes and
stationary spectra only; it does not compute these filling-dependent Hessians.
The public reproduction command therefore does not reproduce that sentence.
The calculation should be added to the script and its output included in the
control table.

## 9. Required changes before manuscript integration

1. Add an exact modular-rank audit or include the rank proof in the report.
2. Test quotient invariance at generic Haar points, not only the endpoint.
3. Add the claimed filling Hessians to `filling_controls()`.
4. Replace ambiguous uses of “exact projection” with the precise
   algebraic-versus-floating-point distinction.
5. Preserve the explicit lack of a global minimum proof and the numerical
   nature of all three-cell spectral and entropy claims.

After these changes, the calculation is suitable for inclusion as an adverse,
boundary-sensitive finite test. It does not establish a selector valid at
arbitrary cell count.

## 10. Resolution in v0.1.3

Resolved on 20 July 2026:

- the production script now certifies rank 207 by exact modular row reduction
  together with the three exact null relations;
- phase/permutation invariance is tested at generic Haar points;
- all claimed $N=4,5,6,7,8$ open and periodic endpoint Hessians are reproduced
  by `filling_controls()`;
- the report distinguishes the exact projector formula and rank certificate
  from their floating-point realization; and
- the manuscript consistently labels the periodic result a restricted
  numerical gate and states that no global minimum proof is supplied.

The full default reproduction completed successfully after these changes. No
review finding required changing the numerical classification.
