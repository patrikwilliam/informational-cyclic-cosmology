# Deep Mathematical Review of the Four-Cell Boundary-Phase Gate

Date: 7 August 2026

Status: internal adversarial review, not independent peer review. Numerical
strictness below means that the declared finite-difference tests pass; it is not
an exact or interval-arithmetic certificate.

Reviewed artifacts:

- [`research/ec_four_cell_boundary_phase.py`](../research/ec_four_cell_boundary_phase.py)
- [`research/four-cell-boundary-phase-gate.md`](../research/four-cell-boundary-phase-gate.md)
- [`research/ec_four_cell_selector.py`](../research/ec_four_cell_selector.py)
- [`research/ec_three_cell_selector.py`](../research/ec_three_cell_selector.py)

## Verdict

After correction, the calculation is mathematically coherent as a narrow
finite-dimensional numerical result. It supports a small-twist three-point pass
for one explicitly defined stationary branch and an analytic expression for its
retuned coexistence coupling. It also gives a decisive numerical curvature
failure before the antiperiodic endpoint.

The first implementation did not correctly follow one branch over the full
grid. That error has been removed. The surviving positive result is weaker than
the earlier phrase "nonzero interval" suggested: it is a discrete numerical
gate, not a certified continuum-in-$\phi$ theorem.

## Findings

### 1. Major error found and corrected: the old rule switched branches

The former algorithm optimized from the preceding representative and from an
exact kinetic seed, discarded non-strict candidates whenever any strict
candidate existed, and only then maximized overlap. This did not define branch
continuation.

At $\phi=\pi/2$:

- the descent initialized from the previous representative ended at cost
  0.52573937 with gradient norm $8.21\times10^{-4}$ and Hessian minimum
  $-0.01309$;
- the exact-kinetic initialization gave a different strict minimum at cost
  0.50898204; and
- the selected replacement had overlap only 0.747894 with the preceding branch.

The old output therefore could not support the claim that the periodic branch
first failed only at $11\pi/16$. It had silently changed identity at $\pi/2$.

The correction defines the branch directly as

$$
U_\phi=G(\phi)U_0,
\qquad
G(\phi)=\operatorname{diag}(e^{ix\phi/4})_{x=0}^3.
$$

No optimizer chooses its identity. The branch is stationary to below
$1.2\times10^{-11}$ on the complete grid and has consecutive matched overlap
0.997292. Its Hessian is positive at $7\pi/16$ and negative at $\pi/2$, so the
correct first failed prescribed point is $\pi/2$.

### 2. The twisted spectrum and gauge convention are exact

With $v_{x+4}=e^{i\phi}v_x$, plane waves give

$$
k_m=\frac{\phi+2\pi m}{4},
\qquad
\lambda_m=2\sin k_m.
$$

Direct diagonalization agrees with this formula to
$1.03\times10^{-15}$. Conjugation by $G(\phi)$ distributes the phase uniformly
over all links to $1.57\times10^{-16}$. These checks determine the sign of the
twist and rule out an accidental use of the opposite boundary convention.

At $\phi=\pi/16$, the former zero pair becomes approximately
$\pm0.098135$, so the small-twist result is not evaluated inside an exact
two-dimensional zero eigenspace.

### 3. The quotient Hessian is the correct local test, with one limitation

The 12 real and imaginary off-diagonal Hermitian generators are an orthonormal
horizontal basis for

$$
U(4)/U(1)^4.
$$

The omitted diagonal directions are column-phase gauge directions; permutations
are discrete and are handled by the matched-overlap comparison. Right
multiplication by $\exp(iH)$ is a valid local chart. At a stationary point, the
second derivative in this chart represents the intrinsic quotient Hessian, so
its positive definiteness is the relevant strict-local-minimum criterion.

This interpretation would fail at a nonstationary point. The corrected branch
gradient is small over all four steps, so that earlier mistake does not recur.
The calculation now requires the maximum, not merely one selected gradient
estimate, to be below $10^{-7}$.

### 4. The half-filled low-body formula has an independent direct check

Earlier validation compared the low-body partial-trace formulas with dense
matrices mainly at $N=3$. The review added an optional direct occupation-mask
audit at the actual $L=4,N=8$ filling. For a seeded Haar decomposition and the
twisted Hamiltonian at $\phi=\pi/16$:

- local projection overlaps agree within $1.89\times10^{-11}$;
- the sector Hilbert-Schmidt norm agrees at displayed precision; and
- the trace differs by $2.91\times10^{-10}$ on a value of magnitude
  approximately $4.13\times10^4$.

This independently checks the fixed-number combinatorial multiplicities without
allocating the dense $12{,}870^2$ matrix. It does not constitute a formal proof
for arbitrary low-body operators, but it directly exercises the filling used by
the reported result.

### 5. The transported branch has an explicit residual polynomial

For the interaction residual

$$
R_U(g)=A_U+2gC_U+g^2B_U,
$$

the two branches satisfy numerically

$$
(A_{\rm site},B_{\rm site},C_{\rm site})=(109824,0,0)
$$

and

$$
(A_\phi,B_\phi,C_\phi)=
\left(109824\sin^2\frac{\phi}{4},594440,0\right).
$$

The maximum discrepancy in these raw identities over the full grid is
$4.66\times10^{-10}$. Since both decompositions share the same invariant
normalization denominator, equal cost reduces to a quadratic numerator equation.
Its positive root is

$$
g_*(\phi)=g_0\cos\frac{\phi}{4}.
$$

Thus the conditional roots are not artifacts of discontinuous optimizer output.
At the two reported roots, the polynomial residual is
$1.46\times10^{-11}$ in magnitude, the crossing slope is nonzero, and both
full quotient Hessians are positive.

### 6. The fixed-coupling curvature failure is robust

The transported branch remains stationary while its minimum Hessian eigenvalue
changes from 0.015917 at $7\pi/16$ to -0.010441 at $\pi/2$. The sign at each
endpoint is unchanged across finite-difference steps from $2\times10^{-3}$ to
$2.5\times10^{-4}$.

A post-review bisection using the $5\times10^{-4}$ Hessian brackets a
sign-changing zero at

$$
0.4756011963 < \phi/\pi < 0.4756164551.
$$

This is a reproducible numerical bracket. It is not an interval proof, and it
does not exclude an unobserved earlier sign change followed by recovery between
coarse samples. The safe conclusion is simply that the explicit branch is not
strict at $\pi/2$ and therefore fails the declared full gate.

### 7. Small-twist survival is expected from nondegenerate perturbation theory

If the exact objective is smooth in $(U,\phi)$ and the periodic critical point
has an invertible positive Hessian, the implicit-function theorem already gives
a unique nearby critical branch for sufficiently small $|\phi|$. Continuity of
the Hessian then preserves strictness on some unspecified neighborhood.

Accordingly, survival at the first small twists is not an independent mechanism
or a surprising consequence of the boundary calculation. It numerically shows
that the persistence reaches at least the two prescribed sample points with
large curvature margins. The more informative new quantity is where the
explicit branch loses stability, not the mere existence of an infinitesimal
continuation.

### 8. Three points are not a proof of a closed phase interval

The points $0$, $\pi/16$, and $\pi/8$ lie on one explicit smooth representative
path and all have comfortable positive Hessian margins. Smoothness plus a
nonsingular Hessian gives local continuation in neighborhoods through the
implicit-function principle. The numerical calculation does not bound those
neighborhoods or prove that they cover every phase in $[0,\pi/8]$.

The defensible label is therefore "small-twist three-point gate," not "proof of
robustness on a nonzero interval." A certified interval claim would require
interval arithmetic or another rigorous lower bound on the Hessian over the
whole phase range.

### 9. The landscape search remains nonrigorous

At each conditional root, 24 Haar samples and four local descents find no lower
value. This can only be stated as failure to find a lower point under the fixed
budget. Compactness of the quotient ensures a global minimum exists, but finite
random sampling does not identify it or prove that only two minima occur.

The additional exact-kinetic stationary branch seen at intermediate twists also
shows that the landscape contains more structure than a two-state picture. It
does not affect the explicit transported-branch audit, but it precludes a claim
of exhaustive branch classification.

## Claim Boundary

Mathematically defensible:

> In the declared four-cell fixed-sector model, the gauge-transported periodic
> representative is numerically stationary on the whole twist grid and remains
> a strict local minimum at $0$, $\pi/16$, and $\pi/8$. Its residual coefficients
> yield analytic retuned coexistence roots. Its quotient Hessian is negative at
> $\pi/2$, so full periodic-to-antiperiodic persistence fails.

Not established:

- strictness at every real phase through $\pi/8$;
- a global-minimum or uniqueness theorem;
- an exhaustive classification of stationary branches;
- persistence for other fillings, interactions, norms, or lattice sizes;
- a continuum/AQFT limit; or
- a physical or cosmological selection law.

## Recommendation

Retain the corrected result as a finite robustness refinement. It weakens the
narrow exact-zero-basis-artifact objection but does not rescue the previously
failed boundary-independent selector. Further work on this particular branch
should begin with a prospective non-EC interaction control or a controlled
lattice discretization, not more random searches on the same four-site model.
