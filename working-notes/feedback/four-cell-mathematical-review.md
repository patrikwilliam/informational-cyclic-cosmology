# Mathematical Review of the Four-Cell Finite Gate

Date: 7 August 2026

Status: internal adversarial review, not independent peer review.

Reviewed artifacts:

- [`research/ec_four_cell_selector.py`](../research/ec_four_cell_selector.py)
- [`research/four-cell-finite-gate.md`](../research/four-cell-finite-gate.md)

## Findings

### 1. Major presentation error found and corrected: stationarity was missing

The first version checked endpoint cost equality and second derivatives but did
not separately test first derivatives. That omission mattered. The open kinetic
endpoint has stable gradient norm 0.0613668, so it is not a critical point. Its
chart second-derivative matrix cannot be treated as an intrinsic Hessian, and
the endpoint must not be called a saddle.

The calculation and report now include a four-step stationarity audit and a
$10^{-7}$ gradient gate. The corrected statement is:

- the open site endpoint is stationary and has a negative Hessian direction;
- the open kinetic endpoint is nonstationary and has an explicit descent
  direction;
- the periodic site endpoint is stationary;
- after one zero-family Newton correction, the periodic kinetic endpoint has
  full gradient norm approximately $5\times10^{-12}$ and a positive Hessian.

This correction does not change the open-fail/periodic-pass classification, but
it is mathematically necessary.

### 2. No remaining internal algebraic contradiction was found

The low-body representation is appropriate for a number-preserving Hamiltonian
of body order at most two. The transformations

$$
h\mapsto U^\dagger hU,
\qquad
V\mapsto \Gamma_2(U)^\dagger V\Gamma_2(U)
$$

agree with the dense exterior-power representation in every validation case.
The fixed-number partial-trace multiplicities correctly separate local,
one-environment-contraction, and two-environment-trace contributions.

For nonorthogonal local matrix units with Gram matrix $G$ and overlap vector
$b$, the projected squared norm $b^\dagger G^+b$ is correct. The numerator may
be evaluated before or after subtracting the global trace because the sector
identity lies in the local subspace. At the two endpoints, the contact residual
vanishes exactly in the site basis and the kinetic residual vanishes exactly in
the kinetic basis, so equal endpoint cost gives
$g_c=\sqrt{A_{\rm site}/B_{\rm kin}}$ as used in the script.

### 3. The implementation is anchored to separately evaluated dense code

The script reconstructs all tested dense Hamiltonians exactly. At seeded Haar
factorizations it checks the exterior lift, all local projection overlaps,
residual components, and invariant sector norms. This includes open and
periodic $L=4,N=3$ cases, so the four-cell combinatorial code is not inferred
solely from lower cell count.

A generic random Hermitian one-plus-two-body operator at $L=4,N=3$ gives local
projection-overlap error $2.84\times10^{-14}$ and exactly matching displayed
trace. This exercises coefficient patterns beyond the structured kinetic and
contact operators.

The largest reported residual-component discrepancy is
$1.7\times10^{-9}$ in the $L=3,N=6$ periodic comparison. This is negligible
relative to the decisive four-cell gradient and curvature margins and is also
separated from the objective evaluations used in those derivatives.

### 4. The local-subspace rank has an exact certificate

The 280-generator integer Gram matrix has four displayed exact rational null
relations. Its rank modulo $1{,}000{,}003$ is 276. A nonzero rank-276 minor over
that finite field gives rank at least 276 over $\mathbb Q$, while the four exact
relations give rank at most 276. Therefore the rational rank is exactly 276.

The nonzero Gram spectrum has condition number approximately 6.88. The
Moore-Penrose projector identities hold to about $2\times10^{-12}$ or better,
so the numerical pseudoinverse is not ill-conditioned in this calculation.

### 5. The open-boundary failure is numerically decisive

The open site gradient is zero at displayed precision, while its minimum
Hessian eigenvalue remains between -0.02949085 and -0.02949084 over four chart
steps. A finite perturbation lowers its objective. The open kinetic gradient
norm remains between 0.06136674 and 0.06136681, and a finite negative-gradient
step lowers its objective. Neither failure depends on optimization convergence.

### 6. The periodic zero-mode quotient is handled coherently

For the two-dimensional zero eigenspace, orthonormal decompositions modulo
column phases are parameterized by $U(2)/U(1)^2$, equivalently a two-sphere up
to the discrete column swap. The deterministic sphere scan and two-generator
refinement therefore cover the continuous ambiguity relevant to the declared
quotient. Minimizing the contact residual within that family is equivalent to
minimizing the full endpoint selector because the kinetic residual vanishes
throughout the degenerate kinetic family.

This is a selector-based convention, not a derivation of a physical basis. The
paper correctly treats the missing dynamical selection principle as unresolved.

A denser $49\times96$ sphere scan returns the same sampled extrema. Sixteen
additional random zero-family starts all descend to the same value within
$10^{-12}$ before the final Newton correction. This is strong finite numerical
evidence for the chosen representative, not an analytic proof of the global
minimum on the sphere.

### 7. The periodic global claim remains numerical

Positive endpoint Hessians prove only strict local minimality within the tested
smooth chart. The default search now optimizes the lowest-cost sampled starts.
A supplemental 64-point search followed by eight 100-step descents also finds
no lower value, but finite random sampling cannot prove global minimality on the
compact quotient. The wording “sampled landscape gate” is therefore
appropriate; “global minimum” would not be.

## Verdict

After the stationarity correction, the calculation is mathematically suitable
as a reproducible negative finite stress test. It supports the precise statement
that the open site endpoint is a saddle, the open kinetic endpoint is
nonstationary, and the periodic endpoints pass the declared local and sampled
tests. It does not prove behavior at arbitrary lattice size, a continuum limit,
or a general no-go theorem.
