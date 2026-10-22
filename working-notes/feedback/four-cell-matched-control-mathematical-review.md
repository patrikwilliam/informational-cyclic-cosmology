# Deep Mathematical Review of the Four-Cell Matched-Control Gate

Date: 9 August 2026

Status: internal adversarial review, not independent peer review. Numerical
strictness means that the declared finite-difference audits pass; it is not an
interval-arithmetic or symbolic certificate.

**10 August 2026 addendum:** This review correctly treated the original
two-contact calculation as insufficient to prove an all-onsite statement. A
subsequent bounded calculation now classifies every nonzero Hermitian,
translation-invariant, number-preserving onsite quartic contact in the same
$L=4$, $N=8$ model. That later result supersedes only the unresolved
universality item below; it does not alter this review's audit of the prospective
matched gate. See the
[closure report](../research/four-cell-onsite-closure.md) and its separate
[mathematical review](./four-cell-onsite-closure-mathematical-review.md).

Reviewed artifacts:

- [`research/four-cell-matched-control-gate.md`](../research/four-cell-matched-control-gate.md)
- [`research/ec_four_cell_matched_control.py`](../research/ec_four_cell_matched_control.py)
- [`research/ec_four_cell_boundary_phase.py`](../research/ec_four_cell_boundary_phase.py)
- [`research/ec_four_cell_selector.py`](../research/ec_four_cell_selector.py)
- [`research/ec_three_cell_selector.py`](../research/ec_three_cell_selector.py)

## Verdict

No release-blocking mathematical error was found in the matched-control
calculation. The density operator is reconstructed exactly under the declared
CAR convention, is not an affine rescaling of the axial contact after sector
centering, and is evaluated with the same quotient, branch rule, coupling rule,
phase grid, and tolerances.

The prospective EC-specificity gate fails: the axial contact and the independent
density control both pass the periodic and three-point small-twist gates. The
full-grid and conditional calculations strengthen the negative interpretation
but do not alter that predeclared verdict.

## Findings

### 1. The primary comparison was fixed before the control result

The local protocol fixes one control,

$$
Q_{\mathrm{dens}}=\sum_x N_x(N_x-1),
$$

and specifies the filling, quotient, branch transport, coupling rule, phase
points, tolerances, and decision rule. In particular, later differences in
curvature or critical phase cannot rescue EC specificity if both interactions
pass the first three points. This blocks the most obvious post-result selection
of a favorable control or threshold.

The protocol was recorded locally rather than in an external preregistration
service. Its prospective status is therefore a documented workflow fact, not an
independently timestamped guarantee.

### 2. The density low-body operator is exact at the tested filling

The operator is constructed from its two-particle matrix and then checked
without constructing a dense $12{,}870\times12{,}870$ half-filled Hamiltonian.
The audit verifies:

- equality with the direct density operator in a small fixed-number sector;
- the diagonal action $\sum_x n_x(n_x-1)$ on every $L=4,N=8$ occupation mask;
- absence of every off-diagonal action at $N=8$;
- equality of direct and combinatorial local-projection overlaps;
- fixed-sector trace and Hilbert-Schmidt norm; and
- Hermiticity with an exactly zero one-body coefficient matrix.

Every reported discrepancy is zero at double-precision output. This is a much
stronger check than inferring the $N=8$ action from the $N=2$ construction alone.

### 3. The control is not a centered affine copy of the axial contact

Because the selector removes the identity component and normalizes by the
centered sector norm, ordinary coefficient-space independence is insufficient.
The relevant centered $N=8$ audit gives

$$
\frac{|\langle Q_{\mathrm{ax},c},Q_{\mathrm{dens},c}\rangle|}
{\|Q_{\mathrm{ax},c}\|\,\|Q_{\mathrm{dens},c}\|}
=0.2119995760.
$$

After the best real rescaling of the centered axial contact, the relative
residual in the density contact is $0.9772697579$. Their one-cell two-particle
spectra also differ:

$$
\operatorname{spec}Q_{\mathrm{ax},x}=(-4,-4,-4,4,8,8),
\qquad
\operatorname{spec}Q_{\mathrm{dens},x}=(2,2,2,2,2,2).
$$

The matched result is therefore not caused by feeding the same operator to the
selector under a new normalization or identity shift.

### 4. The endpoint construction is internally consistent

For each contact, the same numerical rule resolves the two-dimensional zero-mode
freedom of the periodic kinetic basis. The resolved representatives have
unitarity errors below $1.2\times10^{-14}$. Their zero-family gradient norms and
minimum Hessian eigenvalues are, respectively,

| Contact | Gradient norm | Minimum zero-family Hessian |
|---|---:|---:|
| Axial | $8.78\times10^{-12}$ | 0.502107 |
| Density | $1.16\times10^{-10}$ | 0.546875 |

The endpoint residual identities justify the positive equal-cost couplings

$$
g_{0,\mathrm{ax}}=0.4298279139,
\qquad
g_{0,\mathrm{dens}}=1.2984286349.
$$

The zero-family search is still a grid plus local refinement, not an analytic
global minimization over that family. The reported representatives are,
however, well-resolved strict stationary points, and the adverse comparison
does not depend on proving them globally unique.

### 5. Both interactions pass the primary gate with large margins

At $\phi=0,\pi/16,\pi/8$, both the site representative and the explicitly
transported representative are distinct and strict. The decomposition overlap
is 0.375, far from the identity threshold $1-10^{-6}$. Across all four
finite-difference steps, the largest branch-gradient norms on these points are
below $6.0\times10^{-12}$ for the axial contact and
$6.5\times10^{-11}$ for density.

At the least favorable primary point, $\phi=\pi/8$, the minimum transported-
branch Hessian values across the step audit are

$$
0.11188395\quad\text{(axial)},
\qquad
0.18143311\quad\text{(density)},
$$

compared with the declared threshold $2\times10^{-5}$. The result is not a
rounding-level classification. Since both contacts pass, the prospective
specificity gate fails by its own rule.

### 6. The same residual identity explains both branch diagrams

For each contact, let $A$ be the site kinetic residual and $B$ the transported
periodic contact residual. The full-grid audit finds

$$
R_{\mathrm{site}}(g)=(A,0,0),
$$

and

$$
R_{\mathrm{branch}}(g,\phi)
=\left(A\sin^2\frac{\phi}{4},B,0\right),
\qquad
g_0^2B=A.
$$

The maximum component-and-cost identity errors over all 17 points are
$4.66\times10^{-10}$ for the axial contact and
$6.98\times10^{-10}$ for density. Hence the fixed-coupling branch costs obey

$$
C_{\mathrm{branch}}(\phi)
=C_{\mathrm{site}}\left(1+\sin^2\frac{\phi}{4}\right)
$$

for both tested interactions to the reported precision. This common identity is
post-result analysis, not an additional prospective success criterion. It
shows that the shared cost behavior is controlled by the finite ring,
gauge-transport, and onsite-locality structure rather than by the axial matrix
coefficients alone.

It does not prove the identity for every onsite quartic contact. That would
require a separate all-contact algebraic derivation.

### 7. The full-grid difference is quantitative, not specific

The transported axial branch first fails the prescribed grid at
$\phi=8\pi/16$, where its minimum Hessian is $-0.010441$. The density branch is
still strict there with minimum Hessian $0.004766$ and first fails at
$9\pi/16$, where its minimum Hessian is $-0.064837$. Both full-grid gates
therefore fail.

The density control surviving one point longer cannot be read as an axial
advantage. The protocol correctly treats these as interaction-dependent
stability details after the already-shared primary mechanism.

### 8. Conditional coexistence is algebraically shared

Solving the fixed-representative quadratic at $\pi/16$ and $\pi/8$ gives

$$
g_*(\phi)=g_0\cos\frac{\phi}{4}
$$

for both contacts. The direct root errors are at most $1.11\times10^{-16}$ for
the axial contact and $5.33\times10^{-15}$ for density. Polynomial residuals
have magnitude $1.46\times10^{-11}$, crossing slopes are nonzero, and both
representatives remain strict at the four retuned roots.

The 24 seeded Haar samples and four descents at each root find no lower value.
This is a reproducible finite search, not a proof of global minimality or an
exhaustive stationary-point classification. Global minimality is not required
for the primary local-specificity failure.

## Claim Boundary

Mathematically defensible:

> In the declared $L=4,N=8$ centered Hilbert-Schmidt selector, one independently
> reconstructed onsite density contact passes the same periodic and prescribed
> small-twist local-minimum gates as the axial contact. Both contacts obey the
> same transported-branch residual law to numerical precision. The declared
> EC-specificity gate therefore fails.

Not established:

- that every non-axial onsite interaction has the same branch law;
- a global-minimum or uniqueness theorem for either landscape;
- strictness on continuous phase intervals between grid points;
- an exact global solution of the periodic zero-mode family;
- persistence at larger lattice size or different filling;
- a continuum-QFT or AQFT limit; or
- any physical or cosmological selection law.

## Recommendation

Record the result as a successful adverse control and stop using the four-cell
branch as evidence for an EC-specific selector. The finite construction remains
mathematically valid as an example of generic kinetic-versus-onsite locality
competition. A larger lattice would not repair interaction specificity unless a
new, independently derived selector or coupling rule distinguished the axial
channel before its outcome was known.
