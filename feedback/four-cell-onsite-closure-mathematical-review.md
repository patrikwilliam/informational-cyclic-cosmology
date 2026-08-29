# Mathematical Review: Four-Cell Onsite-Contact Closure

Date: 10 August 2026

Reviewed artifacts:

- [`research/four-cell-onsite-closure.md`](../research/four-cell-onsite-closure.md)
- [`research/ec_four_cell_onsite_closure.py`](../research/ec_four_cell_onsite_closure.py)
- the fixed-sector projection and transport conventions used by the earlier
  four-cell scripts

## Verdict

**Pass as a bounded finite-model classification.** No blocking algebraic error
was found in the conclusion that every nonzero interaction in the declared
36-real-dimensional onsite quartic class produces the transported residual law
under the stated periodic resolver.

This is not a continuum theorem, a global landscape theorem, or evidence for an
Einstein-Cartan selector. It closes only the explicitly stated $L=4$, $N=8$
onsite-contact question.

## Findings

### 1. No blocking inconsistency in the transport reduction

With $\vartheta=\phi/4$, direct multiplication confirms

$$
G_\phi^\dagger K_\phi G_\phi
=\cos\vartheta K_0+\sin\vartheta S.
$$

An onsite number-preserving quartic contact is invariant under $G_\phi$. Since
the chosen $U_0$ diagonalizes $K_0$, its $K_0$ residual is zero. The reduction
of the full branch identity to the residual of $S$ and the fixed contact is
therefore correct.

### 2. The basis condition and the resolver conclusion are correctly separated

In the ordered Fourier basis, the zero block of $S$ is $2\sigma_z$. Rotation by
$V(\beta,\chi)$ gives

$$
\|r(S)\|_2^2=A\sin^2\beta.
$$

Thus an externally supplied periodic kinetic eigenbasis satisfies the required
kinetic coefficient if and only if $\sin^2\beta=1$. This condition alone does
not fix $\chi$.

The contact resolver supplies the stronger restriction. Its exact form

$$
B_q=B_q(0,0)-p(q)x-r(q)x^2,
\qquad
x=\sin^2\beta\cos^2\chi,
$$

with positive-definite $p$ and $r$, forces $x=1$ for every $q\neq0$. Hence
$\beta=\pi/2$ and $\chi=0$ or $\pi$. Conflating these two steps would have been
an error; the report does not do so.

### 3. The full onsite class is represented

A Hermitian operator on $\Lambda^2\mathbb C^4\simeq\mathbb C^6$ has 36 real
parameters. The script spans all of them with six diagonal, 15 real
off-diagonal, and 15 imaginary off-diagonal Hilbert-Schmidt-orthonormal basis
elements. The embedding repeats the same local pair matrix on all four cells,
which is exactly the translation-invariant number-preserving onsite class
claimed in the report.

The result does not classify cell-dependent, inter-cell, or number-changing
quartic terms. Those exclusions are explicit.

### 4. The positivity argument is sufficient

The internal decomposition

$$
\operatorname{Herm}(\Lambda^2\mathbb C^4)
=\mathbf1\oplus\mathbf{15}\oplus\mathbf{20}
$$

has real dimensions $1+15+20=36$. Internal $U(4)$ covariance makes the relevant
quadratic forms scalar on these summands. Evaluation on one normalized
representative per summand gives

$$
\operatorname{spec}(p)
=\left\{\frac{231}{4},\frac{231}{2},231\right\},
$$

with multiplicities $1,15,20$, and

$$
\operatorname{spec}(r)
=\left\{\frac{693}{4},\frac{539}{4},\frac{231}{2}\right\}
$$

on the same respective summands. Every coefficient is positive. The reported
normalization $D(q)$ and selected residual $B(q)$ are also positive on each
summand, so no nonzero interaction makes the selector undefined or creates a
hidden zero-residual exception.

### 5. The cross term vanishes for the required representative

The unprojected fixed-sector Hilbert-Schmidt contraction of $S$ with $Q_q$ is
zero: the former changes cell occupation and the latter preserves it. At
$\beta=\pi/2$, $U_0^\dagger S U_0$ is purely off-cell, so its local projection is
zero. The residual cross term is therefore zero exactly for the representative
selected by every nonzero contact. This is enough for the theorem. The stronger
all-$(\beta,\chi)$ cancellation is also reproduced on the complete contact
basis by the supplied partial-trace calculation.

### 6. Earlier special cases are recovered

For the density contact, the local coefficient is $q=2I_6$, so
$\|q_1\|_2^2=24$. The general formulas give

$$
p=1386,
\qquad
r=4158,
\qquad
B=65142,
$$

and hence $B(0,0)=70686$, exactly matching the prior density calculation.

For the axial contact, the squared components are

$$
\|q_1\|_2^2=\frac{32}{3},
\qquad
\|q_{15}\|_2^2=0,
\qquad
\|q_{20}\|_2^2=\frac{544}{3}.
$$

The same formulas give $p=42504$, $r=22792$, and $B=594440$, reproducing the
prior axial values. These independent substitutions strongly constrain sign,
normalization, and representation-label errors.

### 7. Numerical certification is appropriately bounded

The script uses floating-point pseudoinversion of the already audited local
Gram matrix. It is therefore not a machine-checked exact proof by itself. The
reported conclusion instead rests on the finite algebraic reduction and exact
rational coefficients; the script checks those identities on a spanning basis.

Observed worst errors are $3.73\times10^{-11}$ for a direct generic branch,
$1.10\times10^{-11}$ for the contact quadratic identity, and
$2.51\times10^{-12}$ for the cross identity. The reconstructed $p$ and $r$
spectra are separated from zero by at least $231/4$, far beyond numerical
uncertainty. A fully symbolic rational implementation could strengthen formal
certification but is not needed to support the bounded manuscript wording.

## Mathematical Claim Boundary

Supported:

> In the declared periodic four-cell, half-filled, centered Hilbert-Schmidt CAR
> selector, every nonzero Hermitian translation-invariant number-preserving
> onsite quartic contact makes the prescribed periodic resolver choose the
> balanced kinetic zero modes and consequently satisfies
> $R_{\mathrm{branch}}(\phi)=(A\sin^2(\phi/4),B(q),0)$.

Not supported:

- universality under other interactions, fillings, graphs, norms, or resolvers;
- persistence of strict local minima for all $\phi$;
- global optimality away from the resolved periodic zero family;
- an EC-specific interaction selection;
- a continuum-QFT/AQFT extension; or
- a cosmological transition.

## Recommendation

Integrate the result as the final bounded closure of the four-cell side branch.
It strengthens the adverse interpretation: sampling additional contacts from
the same onsite class cannot restore EC specificity. Further finite work on
this selector should stop unless an independently motivated interaction,
projection, norm, or dynamical selection rule falls outside the classified
assumptions.
