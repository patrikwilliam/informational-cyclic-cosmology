# Main Mathematical Problem

> **Preliminary result:** the interaction-projection selector now appears to
> have a negative answer in every finite bipartite dimension when the selected
> stationary state is an isolated eigenstate and the minimum is strict. The
> $2\times3$ search agrees with the general argument. See the
> [general no-go analysis](./general-no-go-analysis.md) and the earlier
> [two-qubit analysis](./two-qubit-preliminary-analysis.md).

## Hamiltonian-selected factorizations with a bipartite-entanglement contrast

### One-sentence question

Can one fixed finite-dimensional Hamiltonian non-circularly select two stable,
physically inequivalent tensor-product structures for the same stationary pure
state, such that the state has high entanglement entropy in one structure and
low entanglement entropy in the other?

The desired answer may be either an explicit construction or a no-go theorem.

## Why this is the first problem

It is already known that the entanglement of a pure state can be changed by an
arbitrary change of observables or tensor-product structure. That fact alone
does not help the cosmological proposal, because choosing a factorization only
because it gives the desired entropy would be circular.

The missing step is a criterion that depends on independently specified
physics, such as the Hamiltonian, and not on the desired entropy. This problem
asks whether even a finite-dimensional proof of principle of that stronger
claim exists.

This is not yet a problem about cosmology, quantum field theory, type-III
algebras, or thermodynamic entropy. It is a deliberately smaller test of the
selection mechanism required by the hypothesis.

## Mathematical setup

Let

$$
\mathcal{H}=\mathbb{C}^{d_A}\otimes\mathbb{C}^{d_B},
\qquad d=d_A d_B,
$$

with $2\leq d_A\leq d_B$. Fix:

- a non-scalar Hermitian operator $H\in\mathcal{B}(\mathcal{H})$;
- a pure state $\rho=|\Psi\rangle\langle\Psi|$ satisfying
  $[H,\rho]=0$.

The reference subsystem algebras are

$$
\mathcal{A}_0=\mathcal{B}(\mathbb{C}^{d_A})\otimes I_B,
\qquad
\mathcal{B}_0=I_A\otimes\mathcal{B}(\mathbb{C}^{d_B}).
$$

Every unitary $U\in U(d)$ defines a candidate tensor-product structure, or
equivalently a pair of commuting factor algebras,

$$
\mathcal{A}_U=U\mathcal{A}_0U^\dagger,
\qquad
\mathcal{B}_U=U\mathcal{B}_0U^\dagger.
$$

Right multiplication of $U$ by $V_A\otimes V_B$ changes only the local bases
and therefore defines the same subsystem structure. When $d_A=d_B$, exchange
of the two factors may also be quotiented out.

In addition, two structures should not count as physically distinct if they
are related by a global unitary $W$ that preserves both supplied data:

$$
W H W^\dagger=H,
\qquad
W\rho W^\dagger=\rho.
$$

Thus the relevant variable is an equivalence class $[U]$, not a particular
matrix representative.

## A concrete Hamiltonian-only selector

For each $U$, write the Hamiltonian in the candidate factorization:

$$
K_U=U^\dagger H U.
$$

Define its normalized one-factor parts and scalar part by

$$
K_A(U)=\frac{1}{d_B}\operatorname{Tr}_B K_U,
\qquad
K_B(U)=\frac{1}{d_A}\operatorname{Tr}_A K_U,
\qquad
c=\frac{\operatorname{Tr}H}{d}.
$$

The interaction component relative to this factorization is

$$
K_{\mathrm{int}}(U)
=K_U-K_A(U)\otimes I_B-I_A\otimes K_B(U)+cI_{AB}.
$$

Using the Hilbert-Schmidt norm, define the dimensionless interaction cost

$$
C_H([U])=
\frac{\lVert K_{\mathrm{int}}(U)\rVert_2^2}
{\lVert H-cI\rVert_2^2}.
$$

This cost is independent of $\rho$, invariant under local basis changes, and
unchanged by adding a scalar multiple of the identity to $H$. It vanishes
exactly when $H$ is non-interacting in the selected bipartite structure:

$$
U^\dagger H U=H_A\otimes I_B+I_A\otimes H_B+c'I.
$$

The local, one-factor, and interaction components are orthogonal in the
Hilbert-Schmidt inner product, so

$$
0\leq C_H([U])\leq 1.
$$

Let

$$
C_{\min}(H)=\min_{[U]} C_H([U]).
$$

The functional is only a simple test selector. It may later be replaced by a
better-motivated Hamiltonian criterion based on minimal scrambling,
quasi-classicality, or pointer-state stability. The important restriction is
that the selector must not contain the entropy target below.

## Entropy relative to a candidate factorization

For the same $U$, define

$$
\rho_A(U)=\operatorname{Tr}_B(U^\dagger\rho U)
$$

and

$$
S_\rho([U])
=-\operatorname{Tr}\!\left[\rho_A(U)\log\rho_A(U)\right].
$$

Because $\rho$ is pure,

$$
0\leq S_\rho([U])\leq \log d_A.
$$

This is bipartite entanglement entropy only. It is not being identified with
thermodynamic, gravitational, or cosmological entropy.

## The construction-or-no-go problem

Determine the smallest pair $(d_A,d_B)$, if one exists, for which there are
$H$, $\rho$, and two equivalence classes $[U_{\mathrm{hi}}]$ and
$[U_{\mathrm{lo}}]$ satisfying all of the following:

1. **Stationarity:** $[H,\rho]=0$ and $\rho$ is pure.
2. **Independent selection:** both classes are strict local minima of $C_H$ on
   the quotient space of factorizations. A positive-definite Hessian transverse
   to the equivalence orbit would be sufficient.
3. **Physical inequivalence:** the two classes are not related by local basis
   changes, a factor swap, or a global symmetry preserving both $H$ and $\rho$.
4. **Entropy contrast:** for some nonzero $\Delta$,

   $$
   S_\rho([U_{\mathrm{hi}}])-S_\rho([U_{\mathrm{lo}}])\geq\Delta.
   $$

   The strongest target would approach
   $S_\rho([U_{\mathrm{hi}}])=\log d_A$ and
   $S_\rho([U_{\mathrm{lo}}])=0$.
5. **Dynamical relevance:** for a specified $\varepsilon>0$,

   $$
   \max\{C_H([U_{\mathrm{hi}}]),C_H([U_{\mathrm{lo}}])\}
   \leq C_{\min}(H)+\varepsilon.
   $$

   Of particular interest is whether examples exist for arbitrarily small
   $\varepsilon$.
6. **Robustness:** the two local-minimum classes and a nonzero entropy gap
   survive sufficiently small perturbations of $H$, with $\rho$ continued as a
   corresponding isolated eigenprojector, or under controlled perturbations of
   a protected eigenspace, modulo the stated equivalences.

The **strong form** asks whether the two classes can both be global minimizers
of $C_H$. A useful **weaker form** asks for two isolated, low-lying local minima
that satisfy the $\varepsilon$-near-minimum condition. The weaker form supplies
only candidate structures; an additional intrinsic rule would still be needed
to select or order them.

An equally useful answer would prove that such a pair cannot exist under
clearly stated assumptions, or derive an inequality relating $C_H$, the
spectrum of $H$, and $S_\rho$ that obstructs the requested
bipartite-entanglement contrast.

## First finite case

Start with

$$
d_A=d_B=2,
\qquad
H\in\mathrm{Herm}(4).
$$

Questions for this case are:

1. Can a $4\times4$ Hamiltonian produce two inequivalent strict minima of
   $C_H$ with different values of $S_\rho$ for one stationary eigenstate?
2. If not, can impossibility be proved for $2\times2$ factorizations?
3. Is the first possible example instead $2\times3$, $2\times4$, or larger?

This version is suitable for analytic work or a numerical search over
Hermitian matrices and the unitary quotient.

## Known triviality and immediate obstruction

The problem is not solved merely by finding two unitaries that give different
entropies. Arbitrary observables can tailor the entanglement of a pure state;
that freedom is exactly what the Hamiltonian-only cost is intended to remove.

There is also an immediate obstruction at zero interaction cost. If
$C_H([U])=0$ and the additive Hamiltonian has a nondegenerate spectrum, its
energy eigenvectors are product vectors in that factorization. A stationary
nondegenerate eigenstate therefore has $S_\rho([U])=0$. A positive construction
may consequently require nonzero interaction, a protected degeneracy, or a
richer selector. Determining whether any of those possibilities can satisfy
the robustness condition is part of the problem.

Two minima generated only by a symmetry of $(H,\rho)$ do not count. Nor does a
functional defined by minimizing $S_\rho$ itself, because that would assume the
desired conclusion.

## What would count as progress

Any of the following would materially advance the project:

- an explicit smallest-dimensional example with matrices for $H$, $\rho$,
  $U_{\mathrm{hi}}$, and $U_{\mathrm{lo}}$;
- a certified numerical example followed by analytic bounds;
- a no-go theorem for $2\times2$ or for all nondegenerate Hamiltonians;
- a classification of the critical points of $C_H$ on the factorization
  quotient;
- a proof that the robustness and entropy-contrast requirements are
  incompatible for this selector;
- a replacement selector from quantum mereology that makes the problem better
  posed while remaining independent of the desired entropy.

A positive result would still not prove an entropy reset or a cosmological
cycle. It would establish only that non-circular dynamical selection and a
factorization-relative bipartite-entanglement contrast can coexist in a finite
system. A negative result would identify precisely what additional structure
the cosmological hypothesis would require.

## Closest prior work

- [Harshman and Ranade, *Observables can be tailored to change the entanglement
  of any pure state*](https://arxiv.org/abs/1102.0955) proves that arbitrary
  observable choices can tailor pure-state entanglement. This makes an
  independent selector essential.
- [Carroll and Singh, *Quantum Mereology: Factorizing Hilbert Space into
  Subsystems with Quasi-Classical Dynamics*](https://arxiv.org/abs/2005.12938)
  proposes selecting factorizations through limited entanglement growth and
  quasi-classical dynamics.
- [Zanardi et al., *Operational Quantum Mereology and Minimal
  Scrambling*](https://arxiv.org/abs/2212.14340) formulates generalized tensor
  product structures using an algebra and its commutant, and proposes minimal
  short-time scrambling as a dynamical selector.
- [Safranek, Deutsch, and Aguirre, *Quantum coarse-grained entropy and
  thermalization in closed systems*](https://arxiv.org/abs/1803.00665) develops
  observational entropy. That is relevant later, but the present finite problem
  intentionally uses only bipartite entanglement entropy.

## Copy-ready community question

### Title

Can one Hamiltonian select two inequivalent tensor-product structures with a
large entanglement-entropy contrast?

### Question

Let $\mathcal{H}=\mathbb{C}^{d_A}\otimes\mathbb{C}^{d_B}$ with
$2\leq d_A\leq d_B$, let $H$ be a fixed
non-scalar Hermitian operator, and let
$\rho=|\Psi\rangle\langle\Psi|$ be a stationary pure state. A unitary $U$
defines a candidate factorization through
$\mathcal{A}_U=U(\mathcal{B}(\mathbb{C}^{d_A})\otimes I)U^\dagger$.

For $K_U=U^\dagger H U$, define

$$
K_A=\frac{1}{d_B}\operatorname{Tr}_B K_U,
\qquad
K_B=\frac{1}{d_A}\operatorname{Tr}_A K_U,
\qquad
c=\frac{\operatorname{Tr}H}{d_A d_B},
$$

and

$$
K_{\mathrm{int}}(U)
=K_U-K_A\otimes I_B-I_A\otimes K_B+cI_{AB}.
$$

Define

$$
C_H([U])=
\frac{\lVert K_{\mathrm{int}}(U)\rVert_2^2}
{\lVert H-(\operatorname{Tr}H/d)I\rVert_2^2},
$$

and define the factorization-relative entropy

$$
S_\rho([U])=
S\!\left(\operatorname{Tr}_B(U^\dagger\rho U)\right).
$$

Classes are quotiented by local basis changes, factor exchange when applicable,
and global symmetries preserving both $H$ and $\rho$.

Does there exist, preferably in the smallest possible dimension, a pair of
physically inequivalent, robust strict local minima, both global or
$\varepsilon$-close to
$C_{\min}(H)=\min_{[U]}C_H([U])$,
$[U_{\mathrm{hi}}]$ and $[U_{\mathrm{lo}}]$ of $C_H$ for which

$$
S_\rho([U_{\mathrm{hi}}])-S_\rho([U_{\mathrm{lo}}])>0?
$$

Can the gap approach $\log d_A$, with one state nearly maximally entangled and
the other nearly separable? If this is impossible for $d_A=d_B=2$, is there a
proof or a lower bound on the required dimension?

I am not asking whether arbitrary refactorization can change entanglement; that
is known. The point is whether a state-independent Hamiltonian criterion can
select the candidate structures without putting the desired entropy into the
definition. A no-go theorem, an explicit construction, or a better established
non-circular selector would all answer the question.

The cosmological motivation is described in
[*Informational Cyclic Cosmology*](https://doi.org/10.5281/zenodo.21115416),
but the finite-dimensional problem above stands independently of it.
