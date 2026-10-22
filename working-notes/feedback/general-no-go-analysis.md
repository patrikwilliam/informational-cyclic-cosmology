# General No-Go Analysis for the Interaction-Projection Selector

Date: 3 July 2026

M2 correction: 14 September 2026 (v0.1.4).

Status: preliminary mathematical argument with numerical checks, not peer
reviewed. The purity-based quotient-separation lemma below and all claimed
implications should be independently checked by a mathematical physicist before
this is presented as a theorem.

Related documents:

- [Main mathematical problem](./main-mathematical-problem.md)
- [Preliminary two-qubit analysis](./two-qubit-preliminary-analysis.md)
- [`2 x 3` numerical checks](../research/two_by_three_selector_analysis.py)

## Conclusion in brief

The interaction-projection selector proposed in the main mathematical problem
appears unable to select a strict local minimum at which an isolated stationary
pure state is entangled, in **any finite bipartite dimension**.

More precisely, under the assumptions below:

> At every strict local minimum of the interaction cost, every rank-one
> spectral projector associated with a nondegenerate Hamiltonian eigenvalue is
> a product state relative to the selected factorization.

Therefore two strict minima with a positive bipartite-entanglement-entropy
contrast cannot exist for this selector when the chosen stationary state is an
isolated eigenstate.

The proof does not exclude bipartite-entanglement contrast in degenerate
eigenspaces. Energy-degeneracy rotations preserve the Hamiltonian-only cost,
but changing the chosen state does not by itself separate classes under the
full factorization quotient. Such rotations obstruct strictness only when
arbitrarily nearby representatives are quotient-inequivalent. The explicit
entangled degenerate examples below have such flat directions; energy degeneracy
alone does not universally preclude a strict minimum. Selecting a particular
state inside a degenerate eigenspace still requires additional physical data.

This is a no-go result for one deliberately simple selector in the specified
finite-dimensional type-I entanglement test. It is not a no-go result for a
separately defined observational or subalgebra-relative entropy, quantum
mereology generally, or the cosmological hypothesis. The proportional Gaussian
scrambling cost inherits the same obstruction on this domain; a genuinely
different finite-time criterion would require separate analysis.

## 1. General finite-dimensional setup

Let

$$
\mathcal{H}=\mathcal{H}_A\otimes\mathcal{H}_B,
\qquad
\dim\mathcal{H}_A=d_A\geq2,
\qquad
\dim\mathcal{H}_B=d_B\geq2.
$$

For a candidate factorization represented by a unitary $U$, define

$$
K=U^\dagger H U.
$$

Let $P$ be the Hilbert-Schmidt orthogonal projection onto the real vector space
of non-interacting Hamiltonians

$$
\mathfrak{L}
=\{A\otimes I_B+I_A\otimes B:
A\in\mathrm{Herm}(d_A),\ B\in\mathrm{Herm}(d_B)\}.
$$

Write

$$
L=P(K),
\qquad
J=(I-P)(K)=K-L.
$$

The normalized selector is

$$
C_H([U])
=\frac{\lVert J\rVert_2^2}
{\left\lVert H-\frac{\operatorname{Tr}H}{d_A d_B}I\right\rVert_2^2}.
$$

The denominator is constant on the unitary orbit, so only the numerator matters
for local minimization.

Let

$$
\rho=|\Psi\rangle\langle\Psi|
$$

be a rank-one eigenprojector of $H$ whose eigenvalue is isolated and
nondegenerate. In the candidate factorization, write

$$
|\psi\rangle=U^\dagger|\Psi\rangle.
$$

The equivalence relation is the one stated in the main problem: local basis
changes, factor exchange where applicable, and global unitaries preserving
both $H$ and $\rho$ are quotiented out.

## 2. Critical-point equation

For a unitary variation

$$
U(t)=Ue^{tX},
\qquad X^\dagger=-X,
$$

one has

$$
\dot K(0)=[K,X].
$$

Orthogonality of $P$ gives

$$
\left.\frac{d}{dt}\lVert(I-P)K(t)\rVert_2^2\right|_{t=0}
=-2\operatorname{Re}\operatorname{Tr}([L,K]X).
$$

Thus every smooth critical point satisfies

$$
[K,L]=0.
$$

Because the eigenvalue of $K$ associated with $|\psi\rangle$ is nondegenerate,
$[K,L]=0$ implies

$$
L|\psi\rangle=\ell|\psi\rangle
$$

for some $\ell$.

## 3. Degeneracy lemma

Every operator $L\in\mathfrak{L}$ can be written as

$$
L=A\otimes I_B+I_A\otimes B.
$$

Choose eigenbases

$$
A|a_i\rangle=\alpha_i|a_i\rangle,
\qquad
B|b_j\rangle=\beta_j|b_j\rangle.
$$

Then $L$ has product eigenvectors

$$
|a_i\rangle\otimes|b_j\rangle
$$

with eigenvalues $\alpha_i+\beta_j$.

If the eigenvalue $\ell$ is nondegenerate, its eigenspace is spanned by one
product vector and $|\psi\rangle$ is separable.

Therefore an entangled $|\psi\rangle$ requires a degenerate eigenspace

$$
E_\ell=\ker(L-\ell I)
$$

containing at least two product-basis cells whose superpositions can have
Schmidt rank greater than one.

## 4. Degenerate-block variation

Assume that $|\psi\rangle$ is entangled and hence that $E_\ell$ is degenerate.
Let $R$ be any unitary supported inside $E_\ell$ and equal to the identity on
$E_\ell^\perp$. Then

$$
[R,L]=0.
$$

At the critical point,

$$
K=L+J,
\qquad
P(J)=0.
$$

Under the candidate-factorization variation $U\mapsto UR$,

$$
K_R=R^\dagger K R=L+R^\dagger J R.
$$

Using orthogonality of $P$ and $I-P$,

$$
\begin{aligned}
\lVert(I-P)K_R\rVert_2^2
&=\lVert(I-P)(R^\dagger J R)\rVert_2^2\\
&=\lVert J\rVert_2^2
-\lVert P(R^\dagger J R)\rVert_2^2\\
&\leq\lVert J\rVert_2^2.
\end{aligned}
$$

Thus every sufficiently small rotation inside the degenerate eigenspace either
lowers the interaction cost or leaves it unchanged. To exclude a strict minimum
on the quotient, it remains to show that arbitrarily small rotations of this
kind are not all equivalence transformations.

### Quotient separation by reduced-state purity

Define the reduced-state purity

$$
Q_\rho(U)
=\operatorname{Tr}\!\left[
\left(\operatorname{Tr}_B(U^\dagger\rho U)\right)^2
\right].
$$

For a pure global state, $Q_\rho(U)=1$ exactly when
$U^\dagger|\Psi\rangle$ is a product vector, while an entangled vector has
$Q_\rho(U)<1$.

This purity is invariant under every stated equivalence:

1. right multiplication by $V_A\otimes V_B$ conjugates the reduced state by
   $V_A$ and leaves its purity unchanged;
2. factor exchange, where applicable, preserves the nonzero Schmidt spectrum of
   a pure state;
3. left multiplication by a global unitary $W$ preserving $\rho$ gives
   $U^\dagger W^\dagger\rho WU=U^\dagger\rho U$.

Therefore $Q_\rho$ is a well-defined function on the quotient space.

The eigenspace $E_\ell$ contains product eigenvectors of $L$. Choose one such
unit vector $|\phi\rangle\in E_\ell$. Because the unitary group of $E_\ell$ acts
transitively on its unit sphere, there is a unitary $R_1$, supported inside
$E_\ell$, such that

$$
R_1^\dagger|\psi\rangle=|\phi\rangle.
$$

Choose an anti-Hermitian logarithm $X$ of $R_1$ supported in $E_\ell$ and set

$$
R(t)=e^{tX},
\qquad 0\leq t\leq1.
$$

Every $R(t)$ commutes with $L$, so the interaction-cost inequality above holds
along the entire path. The function

$$
q(t)=Q_\rho(UR(t))
$$

is real analytic in finite dimension. It satisfies

$$
q(0)<1,
\qquad
q(1)=1,
$$

and is therefore nonconstant. A nonconstant real-analytic function cannot be
constant on any neighborhood of $t=0$. Hence there are arbitrarily small
$t>0$ for which

$$
Q_\rho(UR(t))\neq Q_\rho(U).
$$

Because equivalent representatives have equal purity, these rotations define
genuinely distinct points of the quotient arbitrarily close to $[U]$. Their
interaction cost is no greater than the cost at $[U]$. Consequently an
entangled isolated eigenvector cannot occur at a strict local minimum.

## 5. Preliminary arbitrary-dimension proposition

### Proposition

Let $H$ be a non-scalar finite-dimensional bipartite Hamiltonian, and let
$\rho$ be a rank-one projector onto an isolated, nondegenerate eigenvalue of
$H$. For the interaction-projection selector $C_H$, every strict local minimum
$[U]$ satisfies

$$
S\!\left(\operatorname{Tr}_B(U^\dagger\rho U)\right)=0.
$$

### Proof summary

1. A local minimum is critical, so $[K,P(K)]=0$.
2. Nondegeneracy of the selected eigenvalue makes $|\psi\rangle$ an eigenvector
   of $P(K)$.
3. A one-dimensional eigenspace of a Kronecker-sum operator is spanned by a
   product vector.
4. If the relevant eigenvalue of $P(K)$ is degenerate and $|\psi\rangle$ is
   entangled, the reduced-state-purity lemma supplies arbitrarily nearby,
   quotient-inequivalent rotations inside that eigenspace along which the cost
   cannot increase.
5. The point is therefore not a strict local minimum.

This contradicts the assumption of an entangled stationary state at a strict
minimum.

## 6. What happens when the energy is degenerate

If $\rho$ lies in a degenerate energy eigenspace, a Hamiltonian-only selector
does not identify that particular rank-one state. A unitary $R$ acting inside
the energy eigenspace commutes with $H$, so $U\mapsto RU$ leaves $C_H$
unchanged, although $R^\dagger\rho R$ can differ from $\rho$.

Changing $\rho$ rules out treating $R$ itself as a left symmetry preserving
both $H$ and $\rho$. It does not rule out a right local-basis equivalence,
factor exchange, or a combination with an allowed left symmetry. Failure of
strictness requires arbitrarily nearby, distinct classes under this **full
quotient**, not merely different selected-state representatives. A nonconstant
reduced-state purity along a real-analytic constant-cost path supplies the
needed separation, by the argument in Section 4; a state change alone does not.

### Counterexample to the degenerate-energy inference

Let $X,Z$ be Pauli matrices and set

$$
H=Z\otimes I_2,\qquad
\rho=|00\rangle\langle00|,\qquad
P_j=|j\rangle\langle j|,\qquad B_\theta=e^{-i\theta X}.
$$

Even a local rotation $I_2\otimes B_\theta$ preserves $H$ and changes $\rho$
for generic small nonzero $\theta$, yet represents $[I]$. More strongly, define

$$
\begin{aligned}
R_\theta&=P_0\otimes B_\theta+P_1\otimes I_2,\\
W_\theta&=P_0\otimes I_2+P_1\otimes B_\theta^\dagger,\\
V_\theta&=I_2\otimes B_\theta.
\end{aligned}
$$

Here $R_\theta$ is generically nonlocal, commutes with $H$, and changes
$\rho$. Nevertheless $R_\theta=W_\theta V_\theta$, with $W_\theta$
preserving both $H$ and $\rho$ and $V_\theta$ local. Thus
$[R_\theta]=[I]$ under the full quotient. Along this path $C_H=0$ and
$Q_\rho=1$: the state stays product and no quotient flat direction is produced.

In fact, $[I]$ is a strict global minimum for this pair when factor exchange
is included. To see this, any zero-cost $K=U^\dagger H U$ has the form
$K=A\otimes I_2+I_2\otimes B$ with traceless Hermitian qubit operators $A,B$.
Writing $A^2=a^2I_2$ and $B^2=b^2I_2$, the identity $K^2=I_4$ gives

$$
(a^2+b^2)I_4+2A\otimes B=I_4.
$$

Taking the trace yields $a^2+b^2=1$, hence $A\otimes B=0$. Thus $K$ acts on
only one factor and its selected $+1$ eigenvector is product. Local bases and,
if needed, factor exchange can simultaneously bring $K$ and $U^\dagger\rho U$
to $H$ and $\rho$: the unused factor's basis can align the selected vector.
Explicitly, choose such a right equivalence $V$; then $W=UV$ preserves both
$H$ and $\rho$, so $U=WV^\dagger$ represents $[I]$. Every zero-cost
representative is therefore in that single class; all other classes have
positive cost. Degenerate energy does not universally preclude strictness.

### Scope of the remaining flat-direction conclusions

The explicit entangled $2\times2$ and $2\times3$ degenerate examples retain
their individually verified conclusions. Their constant-cost rotations connect
an entangled state to a product state, changing reduced-state purity; the
analytic-path argument supplies arbitrarily nearby inequivalent classes.
Additional data, such as another conserved operator or a specified relational
algebra, would still be needed to select a state inside a degenerate eigenspace.
This qualification does not change the nondegenerate-energy proposition in
Section 5 or its separate purity-based argument for degeneracy of $P(K)$.

## 7. Explicit `2 x 3` checks

### Degenerate near-example

Take one-factor energy spectra

$$
A=\operatorname{diag}(0,1),
\qquad
B=\operatorname{diag}(0,1,3),
$$

and

$$
H_0=A\otimes I_3+I_2\otimes B.
$$

The product states $|0,1\rangle$ and $|1,0\rangle$ both have energy $1$.
Therefore

$$
|\psi^+\rangle
=\frac{|0,1\rangle+|1,0\rangle}{\sqrt2}
$$

is stationary and has entropy $\log2$ in the reference factorization. Rotating
the degenerate subspace maps it to a product basis vector while preserving
$H_0$. Both descriptions have $C_{H_0}=0$, but the connecting rotations form a
flat family. This fails strictness and robustness.

### Attempted stabilization

Add a resonant coupling

$$
V=g\left(
|0,1\rangle\langle1,0|
+|1,0\rangle\langle0,1|
\right).
$$

This isolates the entangled symmetric and antisymmetric states. However, a
rotation in their two-dimensional resonant subspace converts part of $V$ into
local diagonal terms. With $g=0.2$, the numerical values are

$$
C_H(0)=0.0073304826,
\qquad
C_H\left(\frac{\pi}{4}\right)=0.0012217471,
$$

and

$$
C_H''(0)\approx-0.04886988.
$$

The entangled critical factorization is again a saddle.

## 8. `2 x 3` random search

Riemannian gradient descent was run from 64 Haar-random unitaries for each of
two simple spectra. Multiple local-cost clusters were found, but every cluster
had product eigenvectors within numerical tolerance.

For spectrum

$$
(-3.2,-1.7,-0.4,0.8,2.1,4.6),
$$

five cost clusters were found. Their largest final eigenstate entropy was below
$9.4\times10^{-11}$.

For spectrum

$$
(-4.1,-2.0,-0.3,1.2,2.8,5.7),
$$

five cost clusters were found. Their largest final eigenstate entropy was below
$5.8\times10^{-11}$.

The largest final critical-point residual was approximately
$6.3\times10^{-6}$. These calculations are consistent with the general
argument but do not prove it.

## 9. Scope and consequence

If the proposition is confirmed, the interaction-projection functional should
be retired as a solution to the paper's finite-dimensional type-I
entanglement-contrast test. Increasing the finite dimension does not repair that
construction under the isolated-state and strict-minimum requirements.

This proposition does not evaluate the paper's placeholder $S_{\mathrm{eff}}$.
A future observational or subalgebra-relative entropy need not equal the
reduced-state entanglement entropy used here. Whether the same selector has any
relevance after such an entropy and its physical coarse-graining are specified
is a separate question not answered by this analysis.

The remaining scientifically defensible directions for this proof-of-principle
are not further entanglement searches with the same cost. They are:

1. distinguish genuinely different protocols: in the finite bipartite setting,
   the squared Gaussian scrambling rate $\tau_s^{-2}$ is proportional to $C_H$
   for fixed $H$ and dimensions ([Eqs. (14), (16)](https://arxiv.org/html/2212.14340)),
   so it inherits the same obstruction on the same quotient, not a new escape;
   finite-time scrambling or quasi-classicality needs a separately specified
   physical protocol before its selector can be assessed;
2. determine whether a selector acting on an algebra or a family of operators,
   rather than one Hamiltonian, can be non-circular;
3. specify intrinsic relational data $\lambda$ before attempting to select
   different aeonic algebras;
4. retain a negative theorem if the broader selector classes also fail.

The immediate expert request should be to check the degenerate-block variation,
the invariance of $Q_\rho$ on the stated quotient, and the analytic-path argument
that supplies arbitrarily nearby inequivalent rotations.
