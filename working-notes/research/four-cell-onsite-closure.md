# Four-Cell Onsite-Contact Closure

Date: 10 August 2026

Status: bounded analytic classification in the declared $L=4$, $N=8$ finite
CAR model

## Question

The matched axial and density calculations both produced

$$
R_{\mathrm{branch}}(\phi)
=
\left(A\sin^2\frac{\phi}{4},B,0\right).
$$

The remaining finite mathematical question was whether this law distinguished a
special subset of onsite interactions or followed from the common kinematics of
the entire onsite class.

## Interaction Class

Let the internal one-particle space at each cell be $\mathbb C^4$. The most
general Hermitian, number-preserving, normal-ordered onsite quartic contact with
the same coefficient at every cell is

$$
Q_q
=
\sum_{x=0}^{3}
\sum_{a<b}\sum_{c<d}
q_{ab,cd}\,
c_{x,a}^{\dagger}c_{x,b}^{\dagger}c_{x,d}c_{x,c},
$$

where

$$
q=q^\dagger\in
\operatorname{Herm}(\Lambda^2\mathbb C^4).
$$

Because $\dim_\mathbb C\Lambda^2\mathbb C^4=6$, this is a
36-real-dimensional interaction space. It includes diagonal density contacts,
the axial contact used in the EC-inspired truncation, and arbitrary complex
Hermitian pair-scattering terms.

The classification below assumes:

- four periodic cells and the half-filled sector
  $\mathcal H_{4,8}=\Lambda^8\mathbb C^{16}$;
- the fixed centered Hilbert-Schmidt projection onto the sum of number-preserving
  one-cell operator algebras;
- a translation-invariant contact, with the same $q$ at every cell;
- the prescribed transported branch $U_\phi=G_\phi U_0$; and
- the declared periodic rule that resolves the two-dimensional kinetic zero
  eigenspace by minimizing the contact residual before setting the coupling.

## Residual Notation

Let $\Pi_{\mathrm{loc}}$ be the fixed-sector orthogonal projection onto the
declared local Hamiltonian subspace, and define

$$
r_U(X)
=
(I-\Pi_{\mathrm{loc}})
\bigl(\Gamma(U)^\dagger X\Gamma(U)\bigr),
$$

where $\Gamma(U)$ is the number-preserving CAR lift of the cell unitary. The
three unnormalized residual components are

$$
R_U(K,Q)
=
\left(
\|r_U(K)\|_2^2,
\|r_U(Q)\|_2^2,
\operatorname{Re}\langle r_U(K),r_U(Q)\rangle
\right).
$$

## 1. Exact Transport Identity

Write $\vartheta=\phi/4$, let $K_0$ be the periodic current kinetic, and let
$S$ be the symmetric nearest-neighbor hopping with the same internal Dirac
matrix. Direct multiplication gives

$$
G_\phi^\dagger K_\phi G_\phi
=
\cos\vartheta\,K_0+\sin\vartheta\,S.
$$

Every $Q_q$ above is onsite and number preserving, so its four gauge phases
cancel:

$$
G_\phi^\dagger Q_qG_\phi=Q_q.
$$

If $U_0$ is any eigenbasis of $K_0$, then $r_{U_0}(K_0)=0$. Consequently,

$$
r_{U_\phi}(K_\phi)
=
\sin\vartheta\,r_{U_0}(S),
\qquad
r_{U_\phi}(Q_q)=r_{U_0}(Q_q).
$$

Thus the desired branch law is equivalent to

$$
\|r_{U_0}(S)\|_2^2=A,
\qquad
\operatorname{Re}\langle r_{U_0}(S),r_{U_0}(Q_q)\rangle=0,
$$

where $A=\|r_I(K_0)\|_2^2=109{,}824$.

## 2. Periodic Zero-Mode Family

Choose the ordered Fourier eigenbasis with momenta
$(-\pi/2,0,\pi,\pi/2)$. The two middle columns span the zero eigenspace. Up to
column phases, its nontrivial basis freedom can be written

$$
V(\beta,\chi)
=
\begin{pmatrix}
\cos(\beta/2)&-e^{-i\chi}\sin(\beta/2)\\
e^{i\chi}\sin(\beta/2)&\cos(\beta/2)
\end{pmatrix}.
$$

Let $U_0(\beta,\chi)$ denote the Fourier basis with this rotation in the zero
block. Since $S$ has zero-block matrix $2\sigma_z$, direct evaluation of the
off-cell part gives

$$
\|r_{U_0(\beta,\chi)}(S)\|_2^2
=
A\sin^2\beta.
$$

The residual cross contraction vanishes identically for the full onsite class:

$$
\operatorname{Re}\langle
r_{U_0(\beta,\chi)}(S),r_{U_0(\beta,\chi)}(Q_q)
\rangle=0
$$

for every Hermitian $q$, $\beta$, and $\chi$. Before projection the contraction
is zero because $S$ changes cell occupation whereas $Q_q$ preserves it.
Substitution into the exact fixed-sector partial-trace formula also makes the
projected contraction zero. At the selected value $\beta=\pi/2$, the argument
is especially direct: the zero block of $U_0^\dagger S U_0$ is purely
off-diagonal, so $\Pi_{\mathrm{loc}}(U_0^\dagger S U_0)=0$; unitary invariance
then reduces the residual cross term to the already-zero unprojected
contraction.

It follows that, for an externally chosen periodic kinetic eigenbasis, the
target law holds if and only if

$$
\sin^2\beta=1.
$$

The phase $\chi$ does not affect this kinetic condition.

## 3. Which Basis the Contact Resolver Selects

Define

$$
x=\sin^2\beta\cos^2\chi,
\qquad 0\leq x\leq1,
$$

and let

$$
B_q(\beta,\chi)=\|r_{U_0(\beta,\chi)}(Q_q)\|_2^2.
$$

Expanding the finite CAR contractions gives the exact quadratic identity

$$
B_q(\beta,\chi)
=
B_q(0,0)-p(q)x-r(q)x^2.
$$

Under the internal $U(4)$ action, the real Hermitian pair-operator space
decomposes orthogonally as

$$
\operatorname{Herm}(\Lambda^2\mathbb C^4)
=
\mathbf1\oplus\mathbf{15}\oplus\mathbf{20}.
$$

Writing $q=q_1+q_{15}+q_{20}$, the two quadratic forms are

$$
\begin{aligned}
p(q)
&=\frac{231}{4}\|q_1\|_2^2
+\frac{231}{2}\|q_{15}\|_2^2
+231\|q_{20}\|_2^2,\\
r(q)
&=\frac{693}{4}\|q_1\|_2^2
+\frac{539}{4}\|q_{15}\|_2^2
+\frac{231}{2}\|q_{20}\|_2^2.
\end{aligned}
$$

All six coefficients are strictly positive. Therefore, for every $q\neq0$,
$B_q$ is strictly decreasing as a function of $x$ and its unique minimum in
$x$ is at $x=1$. In the stated parameter range this requires

$$
\beta=\frac\pi2,
\qquad
\chi=0\ \text{or}\ \pi.
$$

The two solutions differ only by phases and permutation of the resulting
even- and odd-sublattice zero modes, so they define the same quotient
factorization. In particular, the contact resolver forces the kinetic condition
$\sin^2\beta=1$ for every nonzero member of the interaction class.

The centered contact norm that normalizes the selector is also positive for all
$q\neq0$:

$$
D(q)
=
\frac{14784}{5}\|q_1\|_2^2
+10032\|q_{15}\|_2^2
+3696\|q_{20}\|_2^2.
$$

At the selected balanced representative,

$$
B(q)
=
\frac{10857}{4}\|q_1\|_2^2
+\frac{11473}{4}\|q_{15}\|_2^2
+\frac{6237}{2}\|q_{20}\|_2^2,
$$

which is likewise strictly positive for $q\neq0$.

The rational coefficients can be obtained without diagonalizing a generic
36-dimensional matrix. Internal $U(4)$ covariance makes each quadratic form a
scalar on the three irreducible summands. It is therefore sufficient to insert
one normalized representative from each summand into the exact fixed-$N$
partial-trace formula. In the pair order
$(01,02,03,12,13,23)$, convenient choices and the resulting coefficients are:

| sector | normalized representative | $D$ | $B$ | $p$ | $r$ |
| --- | --- | ---: | ---: | ---: | ---: |
| $\mathbf1$ | $I_6/\sqrt6$ | $14784/5$ | $10857/4$ | $231/4$ | $693/4$ |
| $\mathbf{15}$ | $\operatorname{diag}(0,1,1,-1,-1,0)/2$ | $10032$ | $11473/4$ | $231/2$ | $539/4$ |
| $\mathbf{20}$ | $\operatorname{diag}(1,-1,0,0,-1,1)/2$ | $3696$ | $6237/2$ | $231$ | $231/2$ |

This also supplies a direct positivity check for the normalization and selected
contact residual, not only for the two basis-selection forms $p$ and $r$.

## Classification Result

Within the assumptions stated above:

> Every nonzero Hermitian, translation-invariant, number-preserving onsite
> quartic contact satisfies
> $$
> R_{\mathrm{branch}}(\phi)
> =\left(A\sin^2\frac{\phi}{4},B(q),0\right)
> $$
> when $U_0$ is chosen by the declared periodic contact-locality resolver.

The zero interaction $q=0$ is exceptional only because its centered selector
denominator vanishes and it cannot resolve the kinetic zero space. If a balanced
zero basis were supplied externally, the same identity would hold with $B=0$.

This closes the finite question negatively for interaction specificity. The law
does not characterize the axial channel, the density channel, or any proper
nonzero subset of the allowed onsite contacts. It is a universal consequence of
the four-cell transport, zero-mode degeneracy, local projection, and periodic
resolver used here.

## Reproducibility Certificate

[`ec_four_cell_onsite_closure.py`](./ec_four_cell_onsite_closure.py) constructs a
real Hilbert-Schmidt orthonormal basis of all 36 Hermitian contact directions and
checks the matrix identities directly. The audit reports:

- maximum kinetic identity error: $2.91\times10^{-11}$;
- maximum contact quadratic-form error: $1.10\times10^{-11}$;
- maximum residual cross error: $2.51\times10^{-12}$;
- maximum direct generic-branch error: $3.73\times10^{-11}$;
- $P$ spectrum:
  $231/4$ (multiplicity 1), $231/2$ (15), and $231$ (20);
- $R$ spectrum:
  $693/4$ (1), $539/4$ (15), and $231/2$ (20); and
- spectral norm $\|[P,R]\|_2=1.67\times10^{-9}$.

The rational coefficients follow from the finite CAR trace expansion and the
$\mathbf1\oplus\mathbf{15}\oplus\mathbf{20}$ decomposition. The floating-point
script is a reproducibility check of that derivation, not a replacement for the
algebraic positivity argument.

## Scope Boundary

This classification does not cover:

- cell-dependent or disordered onsite coefficients $q_x$;
- inter-cell quartic interactions;
- number-nonconserving contacts;
- a different local algebra, norm, filling, lattice size, or boundary graph;
- a different rule for resolving the periodic kinetic degeneracy;
- interval-wide local-minimum persistence of the full selector landscape;
- a continuum QFT or AQFT limit; or
- an Einstein-Cartan or cosmological selection mechanism.

The result strengthens the existing stop condition: further sampling of
translation-invariant onsite quartic controls cannot recover EC specificity in
this finite gate. Any useful next selector would have to add independently
derived structure outside the class just classified.
