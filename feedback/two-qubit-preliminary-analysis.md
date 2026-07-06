# Preliminary Two-Qubit Analysis

Date: 3 July 2026

Status: preliminary derivation and numerical exploration, not peer reviewed.
The proof sketches and code should be independently checked before any result
is presented as a theorem.

Related problem:
[Hamiltonian-selected factorizations with a bipartite-entanglement contrast](./main-mathematical-problem.md).

Subsequent extension:
[General no-go analysis](./general-no-go-analysis.md).

Reproducible numerical checks:
[`research/two_qubit_selector_analysis.py`](../research/two_qubit_selector_analysis.py).

## Result in brief

For the specific interaction-norm selector $C_H$ proposed in the main
mathematical problem, the robust two-qubit problem appears to have a negative
answer:

> If a two-qubit Hamiltonian has a simple spectrum, every strict local minimum of
> $C_H$ has a product eigenbasis relative to the selected factorization.
> Therefore every rank-one stationary eigenprojector has zero bipartite
> entanglement entropy at such a minimum.

Consequently, two strict minima with a nonzero bipartite-entanglement contrast
cannot exist in the $2\times2$ case under these assumptions.

There is an exact degenerate example with bipartite-entanglement contrast
$\log 2$, but it has a continuous flat family of global minima and is destroyed
by generic degeneracy-lifting perturbations. It therefore fails the strictness
and robustness conditions for exactly the reasons those conditions were
included.

This two-qubit derivation was subsequently extended by a preliminary
arbitrary-dimension argument for the same selector. Neither result rules out a
minimal-scrambling selector, a selector using more than one distinguished
operator, or the broader cosmological proposal.

## 1. Notation

For a candidate factorization represented by $U\in U(4)$, write

$$
K=U^\dagger H U.
$$

Let $P_{\mathrm{loc}}$ denote the Hilbert-Schmidt orthogonal projection onto

$$
\mathfrak{L}
=\{A\otimes I+I\otimes B:A,B\in\mathrm{Herm}(2)\}.
$$

Explicitly,

$$
L=P_{\mathrm{loc}}(K)
=\frac{1}{2}\operatorname{Tr}_B(K)\otimes I
+I\otimes\frac{1}{2}\operatorname{Tr}_A(K)
-\frac{\operatorname{Tr}K}{4}I.
$$

With

$$
D=\left\lVert H-\frac{\operatorname{Tr}H}{4}I\right\rVert_2^2,
$$

the cost is

$$
C_H([U])=\frac{\lVert K-L\rVert_2^2}{D}.
$$

## 2. Critical-point condition

Consider a unitary variation

$$
U(t)=Ue^{tX},
\qquad X^\dagger=-X.
$$

Then

$$
\dot K(0)=[K,X].
$$

Because $P_{\mathrm{loc}}$ is an orthogonal projection, the first variation can
be written as

$$
\left.\frac{d}{dt}C_H([U(t)])\right|_{t=0}
=-\frac{2}{D}\operatorname{Re}\operatorname{Tr}([L,K]X).
$$

Therefore every smooth critical point satisfies

$$
[K,P_{\mathrm{loc}}(K)]=0.
$$

This equation is useful independently of the cosmological motivation. It says
that at a selected factorization, the full Hamiltonian must commute with its
best local, non-interacting approximation.

## 3. Exact two-qubit global cost

Let the eigenvalues of $H$ be
$\lambda_1,\lambda_2,\lambda_3,\lambda_4$, let

$$
\bar\lambda=\frac{1}{4}\sum_{i=1}^4\lambda_i,
\qquad
D=\sum_{i=1}^4(\lambda_i-\bar\lambda)^2,
$$

and define the three pair-sum contrasts

$$
\begin{aligned}
\delta_{12|34}&=\lambda_1+\lambda_2-\lambda_3-\lambda_4,\\
\delta_{13|24}&=\lambda_1+\lambda_3-\lambda_2-\lambda_4,\\
\delta_{14|23}&=\lambda_1+\lambda_4-\lambda_2-\lambda_3.
\end{aligned}
$$

The global minimum is

$$
C_{\min}(H)
=\frac{1}{4D}
\min\left\{
\delta_{12|34}^2,
\delta_{13|24}^2,
\delta_{14|23}^2
\right\}.
$$

### Proof sketch

For fixed $L\in\mathfrak{L}$, minimizing
$\lVert U^\dagger H U-L\rVert_2$ over $U$ is an instance of the
Hoffman-Wielandt spectral matching problem. A minimum is attained when $K$ and
$L$ commute and their eigenvalues are optimally matched.

A two-qubit non-interacting Hamiltonian has four additive eigenvalues that can
be placed in a $2\times2$ grid. For any placement of the four $\lambda_i$, the
least-squares residual from the additive row-plus-column subspace is

$$
\frac{\delta}{4}(1,-1,-1,1),
$$

where $\delta$ is the difference between the sums on the two opposite-corner
pairs. Its squared norm is $\delta^2/4$. There are three inequivalent ways to
partition four eigenvalues into two opposite-corner pairs, giving the formula
above.

The minimizing representative can always be chosen diagonal in a product
basis. For generic spectra, its local part is nondegenerate, so every global
minimizer has a product eigenbasis up to the stated equivalences.

## 4. Preliminary two-qubit no-go proposition

### Proposition

Let $H\in\mathrm{Herm}(4)$ have four distinct eigenvalues. Let
$\rho$ be any rank-one eigenprojector of $H$. At every strict local minimum of
$C_H$,

$$
S\!\left(\operatorname{Tr}_B(U^\dagger\rho U)\right)=0.
$$

Hence the requested pair of local minima with a positive
bipartite-entanglement contrast does not exist for a simple-spectrum two-qubit
Hamiltonian and this selector.

### Proof sketch

At a critical point, $[K,L]=0$. Local basis changes can diagonalize the two
one-qubit terms in $L$, so, after subtracting a scalar,

$$
L=aZ\otimes I+bI\otimes Z.
$$

There are four cases.

1. If $L$ has a simple spectrum, $K$ has the same product eigenbasis.
2. If a degeneracy consists of states in one row or one column of the product
   basis, every vector in that degenerate subspace still has one fixed tensor
   factor. Eigenvectors of $K$ in that block are therefore product vectors.
3. Cross-factor degeneracy occurs when $a=b$ or $a=-b$. The degenerate subspace
   is then either
   $\operatorname{span}\{|01\rangle,|10\rangle\}$ or
   $\operatorname{span}\{|00\rangle,|11\rangle\}$. Because
   $P_{\mathrm{loc}}(K)=L$, the two diagonal entries of $K$ in that block are
   equal. If $K$ has a simple spectrum, its block must have a nonzero
   off-diagonal entry $z$, producing Bell-type eigenvectors.

   A rotation $R(\theta)$ inside that block converts part of the off-diagonal
   term into a diagonal difference. In a $2\times2$ product grid, that diagonal
   difference is a local operator:

   $$
   |01\rangle\langle01|-|10\rangle\langle10|
   =\frac{1}{2}(Z\otimes I-I\otimes Z),
   $$

   or analogously

   $$
   |00\rangle\langle00|-|11\rangle\langle11|
   =\frac{1}{2}(Z\otimes I+I\otimes Z).
   $$

   Along the rotation,

   $$
   C_H(\theta)
   =C_H(0)-\frac{2|z|^2}{D}\sin^2(2\theta).
   $$

   Thus $C_H''(0)<0$ whenever $z\neq0$: every entangled cross-degenerate
   critical point is a saddle, not a local minimum.
4. If $L$ is scalar, then $C_H=1$, the maximum possible cost. Such a point
   cannot be a strict local minimum.

The remaining strict-local-minimum cases have product eigenvectors. Since $H$ has a
simple spectrum, every rank-one stationary state is one of those eigenvectors,
and its bipartite entropy is zero.

The main point requiring expert review is whether any quotient-space
singularity or exceptional critical manifold invalidates this case analysis.
The later general analysis addresses quotient separation with a
reduced-state-purity invariant.

## 5. Exact degenerate near-example

Let

$$
H_0=Z\otimes I+I\otimes Z
=\operatorname{diag}(2,0,0,-2)
$$

and

$$
|\Psi\rangle=|\psi^+\rangle
=\frac{|01\rangle+|10\rangle}{\sqrt{2}}.
$$

Because $|\psi^+\rangle$ lies in the zero-energy eigenspace,
$[H_0,\rho]=0$. In the reference factorization,

$$
C_{H_0}([I])=0,
\qquad
S_\rho([I])=\log 2.
$$

Now define $U_{\mathrm{prod}}$ by its columns:

$$
U_{\mathrm{prod}}
=\bigl(|00\rangle,|\psi^+\rangle,|\psi^-\rangle,|11\rangle\bigr).
$$

Then

$$
U_{\mathrm{prod}}^\dagger H_0U_{\mathrm{prod}}=H_0,
\qquad
U_{\mathrm{prod}}^\dagger|\psi^+\rangle=|01\rangle,
$$

so

$$
C_{H_0}([U_{\mathrm{prod}}])=0,
\qquad
S_\rho([U_{\mathrm{prod}}])=0.
$$

The two classes cannot be equivalent under transformations preserving
$(H_0,\rho)$ and local basis changes, because such equivalences preserve the
entropy while these values differ.

This looks like the requested bipartite-entanglement contrast, but it is not a
valid robust solution. Every rotation inside the two-dimensional zero-energy
eigenspace commutes with $H_0$, producing a continuous flat family with
$C_{H_0}=0$.
The minima are therefore not strict. Moreover, $\rho$ is not an isolated
eigenprojector, and a generic perturbation that lifts the degeneracy destroys
the construction.

## 6. Failed attempt to stabilize the Bell state

A natural attempted repair is

$$
H(a,g,j)
=a(Z\otimes I+I\otimes Z)
+g(X\otimes X+Y\otimes Y)
+jZ\otimes Z.
$$

For $g\neq0$, $|\psi^+\rangle$ is an isolated Bell eigenstate in generic
parameter ranges. The reference factorization is a critical point because
$H$ commutes with its local projection. Its cost is

$$
C_H(0)=
\frac{8g^2+4j^2}{8a^2+8g^2+4j^2}.
$$

However, the same rotation in the
$\{|01\rangle,|10\rangle\}$ subspace gives

$$
C_H(\theta)=
\frac{4j^2+8g^2\cos^2(2\theta)}
{8a^2+8g^2+4j^2},
$$

and therefore

$$
C_H''(0)=
-\frac{64g^2}{8a^2+8g^2+4j^2}<0.
$$

The interaction that makes the Bell state an isolated eigenvector also turns
the high-entropy factorization into a saddle. Adding $Z\otimes Z$ does not cure
the negative direction.

## 7. Numerical checks

The accompanying NumPy script performs finite-difference quotient Hessians and
Riemannian gradient descent on $U(4)$.

The exploratory run used 160 random starts for each of three generic spectra:

| Spectrum | Exact $C_{\min}$ | Largest final eigenstate entropy |
| --- | ---: | ---: |
| $(-2.3,-0.7,0.4,3.8)$ | $0.0404595405$ | $2.1\times10^{-11}$ |
| $(-3.0,-1.0,1.5,2.2)$ | $0.0247546507$ | $2.9\times10^{-14}$ |
| $(-4.0,-0.2,0.9,5.1)$ | $0.0009512485$ | $8.4\times10^{-11}$ |

All 480 runs converged numerically to the exact spectral global cost and to
product eigenvectors within tolerance.

For the first spectrum, all 24 product-diagonal eigenvalue arrangements were
also checked. The eight arrangements realizing the minimum pairing had no
negative quotient-Hessian directions. The next eight had two negative
directions, and the final eight had four.

A grid of 1,215 resonant Hamiltonians $H(a,g,j)$ was checked over multiple
$g/a$ and $j/a$ values. Every Bell-state critical point had at least one
negative Hessian direction, consistent with the analytic rotation above.

These calculations support the proof sketch but are not a substitute for it.

## 8. Interpretation and next questions

The first finite-dimensional problem did useful work: it rejected a tempting
but unstable degenerate construction and exposed a structural limitation of the
interaction-norm selector.

The later general analysis and $2\times3$ checks give preliminary negative
answers to the first two questions posed by this two-qubit study. The remaining
mathematically useful questions are:

1. Is the arbitrary-dimension degenerate-block argument, including its
   purity-based quotient-separation lemma, correct on the stated quotient space?
2. Does the minimal-scrambling functional of operational quantum mereology
   evade this no-go result?
3. Would a selector based on a distinguished algebra or a jointly specified
   family of operators $(H,Q_1,\ldots,Q_k)$ be mathematically better posed than
   one based on $H$ alone?
4. Can an intrinsic relational datum $\lambda$ select between candidate minima
   without encoding the desired entropy?

For expert feedback, the most valuable immediate request is to verify or break
the general no-go proof, especially its purity-based quotient-separation step.
