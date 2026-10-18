# Informational Cyclic Cosmology

## A Conceptual Hypothesis of Relational Time, Algebra-Relative Entropy, and Aeonic Readability

Author: Patrik William Pustejovsky

ORCID: [0009-0008-1618-6619](https://orcid.org/0009-0008-1618-6619)

DOI (all versions): [10.5281/zenodo.21115416](https://doi.org/10.5281/zenodo.21115416)

Version: 0.1.8

Release date: 16 October 2026

Status: speculative hypothesis, not a completed physical theory.

Revision note: version 0.1.8 adds a finite reference-resource study. With fixed
symmetry restrictions and the old input inaccessible, unread priming strictly
reduces the attainable measurement set. Both sets still span the same qubit
algebra. Selected operator lemmas and the exact scalar separation are
Lean-checked; the concrete channel and discrimination derivations remain
analytic. Earlier results and core postulates are unchanged; no physical
selector or aeonic transition is derived.

## Abstract

This note explores whether an aeonic boundary could change the physically
privileged local observable algebra of one globally conserved informational
state, rather than restart evolution in external time. No selection mechanism,
distinct quantitative cosmological prediction, or new general theorem about
factorization or observational entropy is supplied.

Finite studies constrain the proposal. An unrestricted interaction-projection
selector encounters a preliminary obstruction; restricted Einstein-Cartan-inspired
CAR examples fail robustness and specificity tests. A finite-time scrambling
example has an internally certified entangled strict local minimum, but a
product competitor has lower cost and better recovery in the stated task.

On a fixed Bell state, reduced-state entropies of one and zero bits coexist
with observational entropies of two and five-thirds bits under a specified
measurement protocol. On arbitrary inputs at nonzero sharpness, its statistics
require access beyond the first original qubit; their implementation does not
supply coherent subsystem control or a physical entropy reset.

A fixed-interaction reference example gives strictly smaller attainable effect
sets after unread priming under fixed symmetry restrictions and loss of old-input
access. Retaining that input restores equivalence under full symmetric control.
Both reduced sets span the same qubit algebra: measurement strength changes,
not the algebra.

Finite stability and prescribed-transport results remain conditional.
Arithmetic reconstruction with supplied reference data encounters stationary
entropy equality and full-norm instability; finite-access stability requires
additional conditioning. Selected proof components are Lean-checked, not the
complete constructions. Physical algebra selection, cosmological entropy,
relational dynamics, repeatability and observational tests remain open.
Reported reviews are internal and LLM-assisted, not independent expert review.

## Scope and Claimed Contribution

The mathematical ingredients used in this note are drawn from existing work on
relational time, observable algebras, factorization-dependent entanglement,
quantum mereology, observational entropy, and Einstein-Cartan fermion dynamics.
The original finite-dimensional refactorization example is not presented as a
new mathematical result. The selector-specific no-go argument added in version
0.1.2 and the restricted EC/CAR finite example and stress tests added in version
0.1.3 are presented for independent checking, not as established general
theorems or as a derived cosmological mechanism. Version 0.1.5 adds a bounded
finite-time counterexample and an operational elaboration of the original
two-qubit illustration. These are different tasks with different inputs, not
components already joined into a cosmological mechanism.

Version 0.1.6 adds finite stability and prescribed-transport comparisons using
established tools; no novelty or independent expert certification is claimed.
Version 0.1.7 adds the conditional arithmetic construction and its bounded
limitations in Appendix B. It does not introduce a prime-number cosmological
postulate or adopt an unverified AI-generated theorem.

Version 0.1.8 adds the conditional measurement-capability example in Appendix C,
using established finite-reference and state-discrimination methods. It does
not claim a new resource-theoretic principle. A scoped Lean supplement checks
general pullback lemmas and the primary scalar inequality, not an end-to-end
formalization of the experiment or its physical assumptions.

The narrower claim explored here is that these ingredients may admit a distinct
cosmological application. In this interpretation, successive aeons are not
fundamentally successive global states. They are different locally readable
descriptions associated with different physically privileged observable
algebras and clock decompositions of one global state.

This is presently a research question, not an established mechanism. For the
proposal to acquire physical content, it must explain what selects the local
algebra, in what sense the selection constitutes an aeonic transition rather
than a change of notation, and what observable consequence distinguishes it
from existing cosmological models.

A non-exhaustive literature review found close prior art for the mathematical
ingredients, cosmological observable-algebra embeddings, and relationally
induced subsystem algebras. It did not identify the same aeonic interpretation,
but that does not establish priority. The claimed contribution is therefore
limited to the proposed synthesis and research question.

### Results and Limits

| Study | Result within its stated domain | What does not follow |
|---|---|---|
| Interaction-projection selector | Preliminary unrestricted strict-minimum obstruction | A no-go theorem for all selectors or ICC |
| Restricted EC/CAR examples | Finite competing minima; robustness and specificity failures | An EC-specific or scalable selector |
| Finite-time scrambling | Entangled strict local minimum, outperformed by a product competitor | Global preference or physical selection |
| Fixed measurement entropy | 2 versus 5/3 bits under declared measurements | Thermodynamic or cosmological entropy reset |
| Measurement access | Exact local implementation with classical communication | Coherent subsystem control or a derived change of access |
| Finite algebra perturbations | Fixed-dimension restricted-entropy continuity bound | POVM or cosmological entropy stability without further assumptions |
| Prescribed algebra transport | Horizontal paths can realize a fixed-state entropy contrast | A selected path, physical transition, or thermodynamic arrow |
| Arithmetic reconstruction | Stationary entropy equality; full-norm instability; conditional finite-access stability | An independently derived selector, uniform energy-only guarantee, or ICC no-go |
| Finite reference redistribution | Strictly smaller attainable effect set under fixed symmetry and reduced access | A different generated algebra, derived access boundary, or ICC transition |

The [v0.1.5 reproducibility supplement](./research/v015/README.md) separates
analytic identities, exact-arithmetic certificates, numerical checks and
assumed physical resources. None is presented as external peer review.
The [v0.1.6 supplement](./research/v016/README.md) adds the bounded stability
and transport analyses without reopening the closed selector searches.
The [v0.1.7 supplement](./research/v017/README.md) contains the arithmetic
derivation, finite-access analysis, diagnostics, scoped Lean proofs, and separate
internal mathematics and physics reviews. These are conditional results and
limitations, not a new physical mechanism.
The [v0.1.8 supplement](./research/v018/README.md) adds the three-qubit
derivation, capability bounds, numerical controls and scoped Lean verification.
Its access restrictions remain explicit inputs.

## 1. Core Postulates

### Foundational postulate: Primacy of the global informational structure

Fundamental reality is hypothesized to be a global informational structure.
Time, space, particles, causality, and the thermodynamic arrow are treated as
emergent features of how this structure is locally decomposed and read from
within.

In the present ansatz, "informational structure" is not an additional substance
or a numerical information measure. It is represented provisionally by a
Hilbert space, a global observable algebra, a state on that algebra, and a
Hamiltonian or constraint. The emergence claims are programmatic and are not
derived in this note.

### 1. Global unitarity

Information is postulated never to be fundamentally destroyed. Apparent
information loss is local, coarse-grained, or observer-dependent. In this
version, black-hole evaporation must ultimately preserve information.

Because the proposal does not assume a fundamental external time, "global
unitarity" does not mean evolution of the universe against an external clock.
It means that the fundamental formulation contains no information-destroying
non-unitary law and that any relational dynamics recovered within an aeon must
be compatible with unitary quantum mechanics.

### 2. Entropy as loss of local readability

Within the hypothesis, growth of the relevant effective entropy does not mean
destruction of the global state. It is interpreted as information becoming
increasingly delocalized, correlated, or difficult to reconstruct relative to a
specified local algebra and coarse-graining. This is not asserted as a
definition of every thermodynamic or information-theoretic entropy.

### 3. Cyclicity as a property of reading, not temporal restart

The "end" and "beginning" of the universe are not necessarily two events
separated by external time. They may be two candidate boundary descriptions of
the same global informational structure. What appears as maximal disorder in one
local decomposition may correspond to a differently embedded or refactored
observable algebra for which a specified effective entropy is low.

### 4. Low effective entropy through changed distinguishability

The low entropy of a new cosmic phase is not produced by erasing information.
It would require a differently embedded or refactored local observable algebra
whose induced restricted state has low entropy under a specified entropy
functional. Merely discarding observables or coarse-graining more strongly does
not guarantee lower entropy and commonly increases observational entropy. This
is therefore not the claim that many microstates merely look identical under
fixed macro-observables, which would normally correspond to high Boltzmann
entropy. The required claim is narrower: the physically selected subsystem
structure changes, and the same global state has high effective entropy in one
embedded algebra but low effective entropy in the other. The selection and the
entropy decrease are not derived here.

### 5. Cyclicity as a repeatability requirement

A single association between end-of-aeon and beginning-of-aeon descriptions is
only a boundary proposal, not yet a cyclic cosmology. Calling the completed
model cyclic requires an intrinsically selected, repeatable family of such
associations together with conditional histories that run from a low-effective-
entropy boundary toward a high-effective-entropy regime within each aeon. This
does not require exact periodic recurrence of the same local state or algebra.
Repeatability is a requirement of the hypothesis, not a result derived here.
A fixed selection rule evaluated on identical global and relational input data
would select the same physical algebra again; a sequence of distinct aeonic
descriptions therefore requires intrinsically defined relational data that
differ between the relevant conditional regimes.

## 2. Speculative Cosmological Extensions

The following conjectures are motivated by the informational framework but are
not logical requirements of the aeonic boundary proposal. Each may be modified
or falsified independently without by itself falsifying the central claim about
local observable algebras.

### 2.1 Informational dark-sector conjecture

In this extension, the phenomena conventionally attributed to dark matter are
conjectured not to arise from an additional particle species. They are instead
the gravitationally accessible signature of correlations retained in the
global informational state but inaccessible to the observable algebra of
ordinary matter. Those correlations may encode structure associated with
matter-like degrees of freedom in another aeonic decomposition while appearing
in the current description only through gravity.

Because the central proposal has no fundamental external time, this should not
yet be described as a signal propagating from a temporally earlier universe.
It is instead a candidate residual pattern in the global state. Calling that
pattern a wave would require a propagation equation, characteristic speed, and
physical observables that have not been supplied.

At an effective level, one possible implementation would be

$$
G_{\mu\nu}+\Lambda g_{\mu\nu}
=8\pi G\left(
T_{\mu\nu}^{\mathrm{visible}}+T_{\mu\nu}^{\mathrm{info}}
\right),
$$

with total covariant conservation,

$$
\nabla^{\mu}\left(
T_{\mu\nu}^{\mathrm{visible}}+T_{\mu\nu}^{\mathrm{info}}
\right)=0.
$$

Here $T_{\mu\nu}^{\mathrm{info}}$ is only a placeholder. Calling it
"information" does not explain why it gravitates. A completed extension must
derive it from the global state and selected observable algebra, or replace it
with a precise modification of the gravitational field equations. It must also
reproduce the empirical successes normally attributed to cold dark matter.

### 2.2 Emergent rest-mass and scale conjecture

The algebraic boundary ansatz does not by itself require all massive particles
to decay. The fate of rest mass becomes compulsory only if the aeonic
identification also requires conformal scale invariance, as in conformal cyclic
constructions. In that case, the extension must specify whether massive degrees
of freedom disappear dynamically or become locally inaccessible under the
selected new algebra while their information remains global.
Local inaccessibility alone does not establish conformal scale invariance:
mass scales may remain in the effective dynamics or gravitational backreaction.
A conformal extension must show that those scales become irrelevant to the
effective equations and observables used in the aeonic identification.

### 2.3 Dark energy as possible boundary data

Dark energy may drive extreme dilution and thereby contribute to the intrinsic
boundary data $\lambda$ used by the algebra selector. A dynamical dark-energy
component might instead participate directly in selecting a new local
description. Neither possibility is currently derived. If the cosmological
constant remains positive and fixed, the extension must explain why an
asymptotic de Sitter regime produces an aeonic algebra change rather than only
continued expansion.

## 3. Algebraic Boundary Ansatz and Missing Selection Rule

For the present type-I ansatz, let $\mathcal{H}$ be a Hilbert space,
$\mathcal{M}=\mathcal{B}(\mathcal{H})$ the global observable algebra,
$H$ a Hamiltonian or global constraint, and
$\rho=|\Psi\rangle\langle\Psi|$ a pure stationary global state. In a Hamiltonian
description stationarity means $[H,\rho]=0$; in a constrained description it may
instead take the form $H|\Psi\rangle=0$. The expectation functional is

$$
\omega(X)=\mathrm{Tr}(\rho X),
\qquad X\in\mathcal{M}.
$$

Purity and stationarity are assumptions of this version; neither follows from
unitarity alone. The proposed aeonic identification is not represented by
replacing one global state with another:

$$
|\Psi_{\mathrm{old}}\rangle \rightarrow |\Psi_{\mathrm{new}}\rangle
$$

At the schematic level, it instead associates two embedded local descriptions
of the same state:

$$
(\rho, \iota_{\mathrm{old}}(\mathcal{A}_{\mathrm{old}}))
\;\mathrel{\mathcal{R}}\;
(\rho, \iota_{\mathrm{new}}(\mathcal{A}_{\mathrm{new}}))
$$

Here:

```text
rho = assumed pure, stationary global state
A_old = abstract local observable algebra in the old aeon
A_new = abstract local observable algebra in the new aeon
iota = embedding of an abstract local algebra into the global algebra
```

The proposal concerns the embedding and factorization of local observables
inside the same global algebra, not a replacement of the underlying state. Two
local algebras may be abstractly isomorphic while being embedded differently in
the global algebra and therefore carrying different restricted states. The
$\mathcal{B}(\mathcal{H})$ notation is schematic and type-I; it is not asserted
to describe local algebras in continuum QFT.

At the present stage, let $\mathcal{R}$ be an unspecified relation contained in
the product of the relevant embedding spaces. The symbol $T_n$ labels one
candidate pair in that relation:

$$
\iota_n^{\infty}:\mathcal{A}_n^{\infty}\hookrightarrow\mathcal{M},
\qquad
\iota_{n+1}^{0}:\mathcal{A}_{n+1}^{0}\hookrightarrow\mathcal{M},
$$

$$
T_n:=\left(\iota_n^{\infty},\iota_{n+1}^{0}\right)\in\mathcal{R}.
$$

Here:

```text
A_n^infty = candidate algebra assigned to the end-boundary regime of aeon n
A_{n+1}^0 = candidate algebra assigned to the start-boundary regime of aeon n+1
M = B(H) = schematic type-I global algebra
iota = embedding of a local algebra into the global algebra
R = proposed boundary relation, not yet a physical law
T_n = one candidate pair of related embeddings
```

The superscripts $\infty$ and $0$ are mnemonic boundary labels in this version.
They do not denote values of an external time parameter or limits already
defined in a topology on states, algebras, or embeddings. If a completed model
interprets either boundary as a genuine asymptotic limit, it must specify an
intrinsic relational parameter, the relevant topology, and a convergence
criterion. The same qualification applies to $\lambda_n^{\infty}$ and
$\lambda_{n+1}^{0}$ below.

This notation does not define $T_n$ as a unitary operator on $\mathcal{H}$, a
completely positive trace-preserving map on states, a homomorphism from the old
algebra to the new one, or evolution in an external time parameter. It records
the proposed aeonic association and nothing more. The index $n$ labels the
candidate aeonic descriptions; it is not an external time coordinate. A full
theory must replace $\mathcal{R}$ with an intrinsic rule that selects the two
embeddings and relates their operational meanings.

One candidate pair $T_n$ describes only one proposed boundary. A cyclic model
would require an intrinsically selected family

$$
\{T_n\}_{n\in\mathcal{I}},
\qquad
T_n=\left(\iota_n^{\infty},\iota_{n+1}^{0}\right)\in\mathcal{R},
$$

for an aeonic index set $\mathcal{I}$, plus compatible relational histories
within the aeons. The index remains bookkeeping for relationally ordered
descriptions, not a fundamental external time. Neither the existence nor the
repeatability of this family is established here.

The global state is assumed to be the same on both sides:

$$
\rho_{n+1}=\rho_n=\rho.
$$

For any embedding $\iota:\mathcal{A}\hookrightarrow\mathcal{M}$, the induced
state on the abstract local algebra is

$$
\omega_{\iota}(a):=\omega(\iota(a)),
\qquad a\in\mathcal{A}.
$$

Because $\rho$ is assumed pure, its global von Neumann entropy is

$$
S_{\mathrm{vN}}(\rho)=0.
$$

The hypothesis requires, rather than derives, a target inequality of the form

$$
S_{\mathrm{eff}}(
\omega_{\iota_n^{\infty}};\mathcal{A}_n^{\infty})
\gg
S_{\mathrm{eff}}(
\omega_{\iota_{n+1}^{0}};\mathcal{A}_{n+1}^{0}).
$$

Thus the beginning of a new aeon is not caused by information erasure. It is
hypothesized to correspond to a change in which distinctions are locally
readable. The equations above do not explain why that change occurs or establish
the inequality.

Here $S_{\mathrm{eff}}$ should not be read as ordinary global von Neumann
entropy, which is invariant under unitary evolution. It is a placeholder for an
observational or subalgebra-relative entropy and must be specified together with
the embedded algebra and coarse-graining. In a finite-dimensional bipartite
matrix factor, the restricted state can be represented by a reduced density
matrix. For a pure global state, its von Neumann entropy is the bipartite
entanglement entropy $S_{\mathrm{ent}}$ used in Section 5; it is not automatically
the cosmological $S_{\mathrm{eff}}$. More general subalgebras, algebras with
centers, and type-III algebras require different constructions. A specified
quantum channel could model an operational coarse-graining only after its input
algebra, output algebra, and physical meaning are fixed; an arbitrary channel is
not a definition of local restriction. None of these entropy constructions defines
the relation $\mathcal{R}$ or selects a candidate pair $T_n$. The current
version does not choose a unique entropy construction for the full
cosmological case.

### Required form of a physical selection rule

Let $\mathfrak{E}_{\lambda}$ denote a physically admissible family of embeddings
of candidate local algebras into $\mathcal{M}$, and let $\sim_{\mathrm{phys}}$
identify embeddings that represent the same operational physics. The label
$\lambda$ must be intrinsic: for example, relational clock data, asymptotic
observables, or boundary conditions. It must not be an external time coordinate
introduced only to make the aeons consecutive.

A completed model would need a selector of schematic form:

$$
\bigl[\iota_{\star}(\lambda)\bigr]
\in
\operatorname*{arg\,min}_{[\iota]\in
\mathfrak{E}_{\lambda}/\!\sim_{\mathrm{phys}}}
\mathcal{F}([\iota];\rho,H,\lambda),
$$

where $H$ may be a Hamiltonian or global constraint and $\mathcal{F}$ is an
operationally defined criterion that must be invariant under
$\sim_{\mathrm{phys}}$. Existing quantum-mereology programs suggest criteria
based on quasi-classicality, limited entanglement growth, pointer-state
stability, locality, or minimal scrambling. The selector must not be defined
merely by choosing whichever factorization makes $\rho$ low entropy; that would
build the desired conclusion into the premise.

For fixed $\rho$, $H$, and $\lambda$, a selector with a unique physical minimum
would return the same equivalence class of embeddings. Distinct aeonic
descriptions therefore require a family of intrinsic relational data, such as
$\lambda_n^{\infty}$ and $\lambda_{n+1}^{0}$, for which schematically

$$
\bigl[\iota_n^{\infty}\bigr]
=\bigl[\iota_{\star}(\lambda_n^{\infty})\bigr],
\qquad
\bigl[\iota_{n+1}^{0}\bigr]
=\bigl[\iota_{\star}(\lambda_{n+1}^{0})\bigr].
$$

These data must be derived from relational observables, records, conditional
states, or boundary structure already encoded in the global theory. They cannot
be supplied by the aeon index $n$, an external time variable, or the desired
low-entropy conclusion. Because the clock decomposition is itself selected, a
completed model may need a joint consistency condition for the embedding,
clock, and relational boundary data rather than treating $\lambda$ as an
independent input. No such derivation or joint condition is provided here.
If the selector instead has degenerate physical minima, the theory must derive
a branch-selection or consistency rule; degeneracy alone does not generate an
ordered aeonic sequence.

For physical content, the selector must identify a unique or physically
equivalent class of embeddings, remain stable under small perturbations, and
distinguish operationally meaningful observables from global unitary
relabelings. The hypothesis does not yet supply such a functional or prove that
its end-of-aeon and beginning-of-aeon solutions exist.

### A tested selector and a preliminary entanglement no-go result

Version 0.1.2 investigates one deliberately simple Hamiltonian-only criterion.
This is a diagnostic test of the selection problem, not an additional
postulate. On a finite bipartite Hilbert space
$\mathcal{H}_A\otimes\mathcal{H}_B$, let a unitary $U$ represent a candidate
factorization and write

$$
K_U=U^\dagger H U.
$$

Let $P_{\mathrm{loc}}$ be the Hilbert-Schmidt orthogonal projection onto
Kronecker-sum Hamiltonians $A\otimes I_B+I_A\otimes B$. Explicitly,

$$
P_{\mathrm{loc}}(K)
=
\frac{1}{d_B}\operatorname{Tr}_B(K)\otimes I_B
+I_A\otimes\frac{1}{d_A}\operatorname{Tr}_A(K)
-\frac{\operatorname{Tr}K}{d_A d_B}I.
$$

For a non-scalar $H$, define the normalized interaction cost

$$
C_H([U])
=
\frac{\left\|(I-P_{\mathrm{loc}})K_U\right\|_2^2}
{\left\|H-\frac{\operatorname{Tr}H}{d_A d_B}I\right\|_2^2}.
$$

This functional asks which candidate factorizations make the fixed Hamiltonian
as close as possible to non-interacting. It does not include the target entropy
and is therefore non-circular in that limited sense.

This is also the finite factor-algebra Gaussian minimal-scrambling criterion,
up to normalization. Set $d=d_A d_B$ and
$\mathcal A_U=U(\mathcal B(\mathcal H_A)\otimes I_B)U^\dagger$,
with commutant $\mathcal A_U'$. In units $\hbar=1$, equations (14) and (16) of
[Zanardi et al. (2024)](https://arxiv.org/abs/2212.14340) give

$$
\begin{aligned}
\tau_s^{-2}(H,\mathcal A_U)
&=\frac{\|(I-P_{\mathcal A_U+\mathcal A_U'})H\|_2^2}{d},\\
C_H([U])&=
\frac{d\,\tau_s^{-2}(H,\mathcal A_U)}
{\|H-(\operatorname{Tr}H/d)I\|_2^2}.
\end{aligned}
$$

where $P_{\mathcal A_U+\mathcal A_U'}$ projects onto the sum of the two
operator subspaces, not their generated algebra. For fixed non-scalar $H$, the
positive multiplier is independent of $U$: minimizing the squared Gaussian
rate gives the same minima and local stability on the same candidate domain.
This is direct prior art and operational motivation for the cost, not a
different selector that evades the argument below. The bounded finite-time
follow-up later in this section uses a different functional and a declared
time-window protocol; its physical timing justification remains absent.
The displayed Gaussian identification is not assumed for charge-sector
algebras or continuum QFT.

The preliminary result is negative. Assume that $\rho$ is a rank-one projector
onto an isolated, nondegenerate eigenvalue of $H$, and quotient candidate
factorizations by local basis changes, factor exchange where applicable, and
global symmetries preserving both $H$ and $\rho$. Then the current argument
gives

> At every strict local minimum $[U]$ of $C_H$, the state
> $U^\dagger\rho U$ is a product state, and hence its bipartite entanglement
> entropy is zero.

The key steps are short. At a smooth critical point,

$$
[K_U,P_{\mathrm{loc}}(K_U)]=0.
$$

The eigenvector of $K_U$ associated with the selected nondegenerate eigenvalue
is therefore also an eigenvector of the local operator
$L=P_{\mathrm{loc}}(K_U)=A\otimes I+I\otimes B$. If its eigenvalue as
an eigenvector of this Kronecker sum is nondegenerate, the eigenvector is a
product vector. An entangled eigenvector consequently requires a degenerate
eigenspace of $L$. Writing
$K_U=L+J$, with $P_{\mathrm{loc}}(J)=0$, and rotating by any unitary $R$ inside
that degenerate eigenspace gives

$$
\left\|(I-P_{\mathrm{loc}})(R^\dagger K_U R)\right\|_2^2
=
\|J\|_2^2
-\left\|P_{\mathrm{loc}}(R^\dagger J R)\right\|_2^2
\leq
\|J\|_2^2.
$$

To show that this is a genuine quotient direction, define the reduced-state
purity

$$
Q_\rho(U)
=\operatorname{Tr}\!\left[
\left(\operatorname{Tr}_B(U^\dagger\rho U)\right)^2
\right].
$$

This quantity is invariant under local basis changes, factor exchange for a pure
state, and global symmetries preserving $\rho$. It therefore descends to the
stated quotient. The degenerate eigenspace of $L$ contains a product eigenvector
$|\phi\rangle$. A unitary $R_1$ supported in that eigenspace can be chosen so
that $R_1^\dagger|\psi\rangle=|\phi\rangle$, and it can be joined to the identity
by an analytic path $R(t)$ inside the same block. Along this path the cost never
exceeds its value at $t=0$, while $Q_\rho(UR(t))$ is a nonconstant real-analytic
function changing from a value below one to one. Consequently every
neighborhood of $[U]$ contains a quotient-inequivalent point of no greater cost,
which excludes a strict local minimum. This purity-based quotient argument is
the step for which independent mathematical review is most important.

Exact two-qubit calculations, explicit degenerate and resonant examples, and
numerical $2\times3$ searches support the argument. The tested degenerate
examples display bipartite-entanglement contrast along flat families that fail
strictness and robustness. This is not a general exclusion of strict minima
for degenerate energies: state-changing rotations must also be shown
inequivalent under the full quotient. Details and reproducible scripts
are supplied in
[`feedback/general-no-go-analysis.md`](./feedback/general-no-go-analysis.md),
[`feedback/two-qubit-preliminary-analysis.md`](./feedback/two-qubit-preliminary-analysis.md),
and the [`research`](./research) directory. The numerics are supporting checks,
not a proof.

If independently confirmed, this result retires $C_H$ as a solution to the
specified finite-dimensional type-I entanglement-contrast problem under these
assumptions. It does not determine whether algebras selected by this or another
criterion could exhibit a contrast in a separately defined observational or
subalgebra-relative $S_{\mathrm{eff}}$. The Gaussian scrambling criterion
inherits the same obstruction on this domain by the identity above. Genuinely
different criteria, such as a specified finite-time scrambling or
quasi-classicality functional, selectors acting on a family of observables,
field-theoretic algebras, mixed or nonstationary states, and the central
cosmological proposal require separate analysis.

### Bounded finite-time follow-up

Version 0.1.5 tests a genuinely different finite-horizon functional. For a
candidate embedding U, let $W_{U,t}=e^{-itU^\dagger HU}$, set $\hbar=1$, and
define the channel

$$
\mathcal E_{U,t}(X)=\operatorname{Tr}_B\left[
W_{U,t}(X\otimes I_B/d_B)W_{U,t}^\dagger\right].
$$

Let $J_{U,t}$ be its trace-one Choi state, ordered as output tensor reference.
The algebraic scrambling quantity and its finite-time average are

$$
G_U(t)=1-\operatorname{Tr}(J_{U,t}^2),\qquad
F_T([U])=\frac1T\int_0^T G_U(t)\,dt.
$$

This channel interpretation is established prior art
([Styliaris, Anand & Zanardi](https://arxiv.org/abs/2007.08570)), not a new
entropy definition. Its operational use presupposes preparation of arbitrary
A probes, a reset maximally mixed B, and specified timing. The Choi purity is
not the reduced-state entropy of the selected stationary ground state. T is
fixed independently of the candidate algebra and the desired entropy.

For $H=(XX+2YY+3ZZ)/\sqrt{14}$ and T = 8, the reference algebra has a
quotient-strict local minimum with the nondegenerate singlet ground state
$|\Psi^-\rangle$. Here $PQ$ denotes $P\otimes Q$. Exact stationarity and
rational enclosures of all six normal-slice Hessian eigenvalues give
$\kappa_i>7/100$ in the normalization of the
[technical derivation](./research/v015/finite-time-analysis.md).
This internally checked counterexample excludes a universal product-state
strict-local-minimum claim for this finite-time functional. It is not a
counterexample to the original cost-specific argument.

Crucially, the entangled local minimum is not a global minimizer. A
product-eigenbasis embedding of the same H and selected state gives

$$
F_8(\mathcal A_{\mathrm{Bell}})\simeq0.552031754,\qquad
F_8(\mathcal A_{\mathrm{prod}})\simeq0.227611851.
$$

The exact-arithmetic certificate bounds their difference strictly above 3/10.
This particular branch therefore fails any near-global tolerance at most 0.3;
neither a global optimizer nor a physically metastable algebra has been found.
Its simple energies have repeated gaps. Finite-time local strictness does not
contradict infinite-time global-minimizer results under nonresonance assumptions
([Andreadakis, Dallas & Zanardi](https://arxiv.org/abs/2312.13386)).

The operational comparison is also unfavorable to this Bell candidate. For
the stated unital channel, put $P=\operatorname{Tr}J^2$ and let $f_*$ denote
optimal entanglement fidelity with an A-only CPTP decoder and maximally mixed
input. The adjoint decoder and a spectral bound give $P\leq f_*\leq\sqrt P$,
a specialization of transpose recovery
([Barnum & Knill](https://arxiv.org/abs/quant-ph/0004088)). For uniformly sampled,
recorded time and a decoder allowed to depend on that time, the supplement
certifies average optimal fidelities below 0.670 for the Bell candidate and
above 0.772 for its product competitor. Unrecorded time defines a different
channel and task; these bounds do not supply a cosmological clock or window.

This bounded follow-up is closed without promoting the branch to an ICC
selector. Unitary transport generated by the same H stays in its centralizer
orbit and thus in the same stipulated factorization class. A physical
preference principle, timing prescription and transition between inequivalent
classes remain additional inputs. The argument does not exclude other
physically motivated selectors, and no such replacement is proposed here.

### Restricted follow-up: an Einstein-Cartan-inspired CAR selector

Version 0.1.3 tests whether the negative result above still blocks the same
cost after the admissible family is restricted by specified fermionic
structure. Consider two spatial cells with four Dirac components per
cell. At one-particle level require candidate transformations to preserve
fermion number and normalize the internal matrix algebra

$$
\mathfrak D=I_2\otimes M_4(\mathbb C),
\qquad
V\mathfrak D V^\dagger=\mathfrak D.
$$

Every such unitary has the form $V=W\otimes S$, where $S$ is a common internal
basis change that does not alter the cell split. The induced unordered cell
decompositions form

$$
U(2)/\left((U(1)\times U(1))\rtimes S_2\right)
\simeq \mathbb{RP}^2
\simeq S^2/\{\pm1\}.
$$

They are therefore represented by an unoriented Bloch axis $\mathbf n$. This
restriction is a defining structural assumption of the finite model, not a
consequence of the EC contact term; a completed theory would have to derive it
independently.

For a massless one-link Dirac kinetic term and the normal-ordered axial-current
contact channel induced when non-propagating Einstein-Cartan torsion is
eliminated, the full-Fock interaction cost becomes

$$
C(\mathbf n;r)=
\frac{
(1-n_y^2)+3r^2(1-n_z^2)(3+n_z^2)
}{1+16r^2},
\qquad r=\frac gt.
$$

For $1/\sqrt{12}<|r|<1/\sqrt6$, it has two strict local endpoint minima,
at the momentum split
$\mathbf n=\pm\hat{\mathbf y}$ and site split
$\mathbf n=\pm\hat{\mathbf z}$, which exchange global stability at
$|r|=1/3$. On the tested positive-coupling branch, $r=1/3$, the Hamiltonian has
an exactly certified isolated ground state and a numerically evaluated
$1.80367$-bit difference between its site- and momentum-factor entanglement
entropies. The selector geometry depends only on $r^2$, but the stationary-state
calculation is not asserted here for $r=-1/3$.

As a weighting gate, the calculation was repeated in the fixed four-particle
sector rather than using the trace on the entire Fock space. In the full-Fock
trace, sectors contribute through their sector traces and hence in proportion
to their dimensions when expressed as normalized sector averages. The
restricted cost is then

$$
C_4(\mathbf n;r)=
\frac{
160(1-n_y^2)+24r^2(1-n_z^2)(71+25n_z^2)
}{160+(15744/7)r^2}.
$$

The two strict selector branches and finite barrier survive, with transition
$|r_c|=\sqrt{20/213}$. On the tested positive branch
$r=+\sqrt{20/213}$, the numerically isolated ground state remains in the
four-particle sector and has a $2.00732$-bit site-versus-momentum entanglement
contrast. Appendix A states the construction,
checks, and limitations, with reproducible code in the
[`research`](./research) directory.

This is not a counterexample to the unrestricted no-go argument: strictness is
obtained only on a narrower candidate manifold from which the general descent
directions have been removed. Its relevance therefore depends on whether the
Dirac/CAR restriction follows from physical structure already present in a
continuum theory. If it is imposed only to avoid the no-go directions, the
escape is circular. The result establishes finite mathematical possibility
under the stated restriction, not an aeonic transition, a cosmological entropy
reset, or Einstein-Cartan cosmology.

A null control replacing the axial-current contact by a spin-independent onsite
density contact reproduces the same two-minimum geometry. The finite transition
should therefore be interpreted as generic competition between a hopping term
that is local in momentum variables and an onsite interaction that is local in
site variables, not as evidence for Einstein-Cartan dynamics. Conversely, the
ground-state entropy contrast remains positive after imposing local-number or
local-parity superselection, so it is not entirely a particle-number-fluctuation
artifact. Appendix A gives the numerical controls and their limitations.

A first larger finite test replaces the two cells by three and admits the full
restricted cell-mixing family $U(3)/(U(1)^3\rtimes S_3)$. In the half-filled
$N=6$ sector, the open-chain kinetic endpoint has a negative Hessian direction
and an explicit lower mixed factorization. The periodic ring retains two
numerically strict endpoints, and a strengthened multi-start search found no
lower candidate, but this is not a proof of global minimality. At three cells,
changing the boundary also changes two bonds into three and changes the
discrete-derivative spectrum at order one. The combined result therefore fails
a boundary-independent robustness gate. The periodic branch is recorded as a
finite numerical observation, not as support for an EC-derived selector.
Appendix A and the
[three-cell technical report](./research/three-cell-finite-gate.md) give the
construction, exact rank certificate, controls, and limitations.

A four-cell periodic ring then tests the full
$U(4)/(U(1)^4\rtimes S_4)$ cell-mixing family in the half-filled $N=8$ sector.
Both periodic endpoints are numerically strict. An explicit gauge-transported
branch stays stationary and strict at the prescribed small twists $\pi/16$ and
$\pi/8$, but loses positive curvature at $\pi/2$. This removes the narrow
objection that the three-cell periodic observation was purely an odd-size
effect, while still failing full periodic-to-antiperiodic persistence.

More decisively, a prospectively fixed spinor-blind density contact
$Q_{\mathrm{dens}}=\sum_xN_x(N_x-1)$ passes the same periodic and small-twist
gates. The two contacts are not equivalent after fixed-sector centering, yet
both obey the same transported residual law and retuned coexistence relation
$g_*(\phi)=g_0\cos(\phi/4)$. The finite behavior is therefore not an
EC-specific signature. Appendix A, the
[matched-control report](./research/four-cell-matched-control-gate.md), and its
separate [mathematical](./feedback/four-cell-matched-control-mathematical-review.md)
and [physics](./feedback/four-cell-matched-control-physics-review.md) reviews
state the result and limits.

In compact form:

```text
same global state rho
+ old embedded algebra -> high specified effective entropy
+ new embedded algebra -> low specified effective entropy
```

## 4. Relational Clock Time, the Thermodynamic Arrow, and Clock Ambiguity

The Page-Wootters mechanism addresses how conditional dynamics may be encoded
in a globally stationary state. It does not by itself explain why one temporal
orientation is thermodynamically distinguished. Relational clock time and the
thermodynamic arrow are therefore treated as separate problems in this note.

### Idealized conditional dynamics

In the idealized construction, the accessible Hilbert space and observable
algebra admit compatible clock/rest decompositions:

$$
\mathcal{H} \simeq \mathcal{H}_C\otimes\mathcal{H}_R,
\qquad
\mathcal{A}_n \simeq \mathcal{A}_n^C\otimes\mathcal{A}_n^R.
$$

The stationary global state must also satisfy an appropriate constraint. In the
ideal non-interacting form,

$$
H_{\mathrm{tot}}|\Psi\rangle=0,
\qquad
H_{\mathrm{tot}}=H_C\otimes I_R+I_C\otimes H_R.
$$

The zero eigenvalue is conventional; a stationary energy eigenvalue can be
shifted to zero. A nonzero constrained state also requires compatible clock and
rest energy support, so that contributing energy eigenvalues can sum to the
chosen total eigenvalue. Interactions, imperfect clocks, and more general
constraints require extensions of this ideal form.

Let the clock states be generated by $H_C$,

$$
|t\rangle_C=e^{-iH_Ct}|0\rangle_C,
\qquad
E_t=|t\rangle_C\langle t|.
$$

For $\rho=|\Psi\rangle\langle\Psi|$, the state of the remaining degrees of
freedom relative to the clock reading $t$ is

$$
\rho_R(t)=
\frac{\mathrm{Tr}_C[(E_t\otimes I_R)\rho]}{p(t)},
\qquad
p(t)=\mathrm{Tr}[(E_t\otimes I_R)\rho].
$$

The formula applies where $p(t)>0$. Each $E_t$ is treated as a rank-one positive
effect and, for normalized $|t\rangle$, an individual rank-one projection. A
continuous family of such effects in a finite-dimensional clock is generally
non-orthogonal and is not a projection-valued time observable; a normalized
clock POVM requires an appropriate measure and normalization. Actual
measurement updates additionally require a specified instrument. The
conditional state above is instead a relative-state assignment and does not
require an actual measurement of the clock. Under the ideal constraint and
spectral-compatibility assumptions above, it satisfies, in units with
$\hbar=1$,

$$
\frac{\partial\rho_R(t)}{\partial t}
=-i[H_R,\rho_R(t)].
$$

Thus $t$ is an internal label for correlations between a selected clock and the
rest, not a fundamental external parameter. The construction recovers
reversible conditional dynamics; it does not yet select a preferred clock or a
direction of time.

### The separate arrow-of-time requirement

The ideal conditional evolution above is unitary. If $\rho_R(t)$ is pure, its
von Neumann entropy remains zero. A thermodynamic arrow therefore requires
additional structure: a physically selected coarse-graining or accessible
subalgebra, a low-observational-entropy boundary condition, and conditional
dynamics that produce records and typical entropy growth away from that
boundary.

The Page-Wootters construction does not by itself identify either orientation
of the clock label as the thermodynamic future. A thermodynamic arrow would
orient the clock readings in the direction of typical entropy increase away
from the selected low-entropy boundary.

Schematically, for a selected observational algebra
$\mathcal{A}_R^{\mathrm{obs}}$, an arrow would require behavior such as

$$
S_{\mathrm{obs}}(\rho_R(t_2)\mid\mathcal{A}_R^{\mathrm{obs}})
\gtrsim
S_{\mathrm{obs}}(\rho_R(t_1)\mid\mathcal{A}_R^{\mathrm{obs}}),
\qquad t_2>t_1,
$$

for typical conditional histories over an appropriate regime. This is not
asserted as exact monotonicity: finite systems can fluctuate or recur. Here
$S_{\mathrm{obs}}$ is a placeholder for a specified observational or
coarse-grained entropy, not the global von Neumann entropy. The proposed
low-effective-entropy restricted state relative to the new aeon's algebra could
serve as a boundary condition only if that algebra is selected non-circularly
and its conditional dynamics actually generate the required asymmetry.
Refactorization alone does not do so.

### Clock ambiguity

A stationary global state generally admits many candidate clock/rest
decompositions. Different choices can encode different conditional histories
and even different effective dynamical laws. This is the clock ambiguity. It is
especially important here because the proposal already allows the physically
privileged observable algebra to differ between aeons.

The status of the ambiguity is disputed. Marletto and Vedral argue that fixing
the global Hamiltonian and requiring an ideal non-interacting clock can select a
unique suitable decomposition. Recent work by Stoica argues that
non-interaction alone is insufficient and that the physical meaning of the
observables must also be supplied. This note does not assume that the dispute is
settled.

The selector introduced in Section 3 must therefore select not only an embedded
local algebra, but also a compatible clock subalgebra and rest algebra, and it
must relate them to the fixed global Hamiltonian or constraint and to a physical
record structure. It must not choose a clock merely because that clock
reproduces the desired history. Across the aeonic boundary relation, a
different selected clock may define a different relational time coordinate,
but it does not by itself define a new thermodynamic arrow.

## 5. Finite-Dimensional Illustration

This section first illustrates an established kinematic fact: the entanglement and
reduced-state entropy assigned to a pure state depend on the chosen subsystem
factorization or observable algebra. Sections 5.2 and 5.3 then specify an
observational-entropy comparison and the measurements that realize it. None
models cosmology, derives an aeonic transition, or claims a new general theorem.

The operational role of observable algebras in selecting quantum subsystems was
developed by [Zanardi](https://arxiv.org/abs/quant-ph/0103030). Explicit
constructions show that observables can induce a tensor-product structure in
which an arbitrary pure state has a chosen Schmidt decomposition
([Harshman & Ranade](https://arxiv.org/abs/1102.0955)), and that a state may
appear entangled or separable under different factorizations of its observable
algebra
([Thirring et al.](https://arxiv.org/abs/1106.3047)). The calculation below is
a two-qubit specialization of this known factorization dependence, included to
make the proposed cosmological interpretation concrete.

### 5.1 Factorization-relative entanglement

For this illustration only, define the bipartite entanglement entropy
$S_{\mathrm{ent}}$ as the von Neumann entropy of the reduced state obtained from
the assumed pure global state. This quantity depends on the chosen
tensor-product factorization. It is not identified here with the cosmological
$S_{\mathrm{eff}}$ of Section 3 or the observational entropy used for the
thermodynamic arrow in Section 4.

Let the global Hilbert space be finite-dimensional:

$$
\mathcal{H} \simeq \mathbb{C}^4.
$$

In the old aeon, choose a two-qubit factorization:

$$
\mathcal{H} = \mathcal{H}_A \otimes \mathcal{H}_B,
\qquad
\dim \mathcal{H}_A = \dim \mathcal{H}_B = 2.
$$

Let the globally conserved state be a Bell state with respect to this
factorization:

$$
|\Psi\rangle =
\frac{1}{\sqrt{2}}
\left(
|0_A0_B\rangle + |1_A1_B\rangle
\right).
$$

The old local observable algebra is:

$$
\mathcal{A}_n^\infty =
\mathcal{B}(\mathcal{H}_A) \otimes I_B.
$$

An observer restricted to this algebra traces over the inaccessible subsystem
$B$:

$$
\rho_A =
\mathrm{Tr}_B(|\Psi\rangle\langle\Psi|)
=
\frac{I_A}{2}.
$$

The entanglement entropy relative to the old factorization is:

$$
S_{\mathrm{ent}}(\rho \mid \mathcal{A}_n^\infty)
=
S(\rho_A)
=
-\mathrm{Tr}(\rho_A \log_2 \rho_A)
=
1.
$$

Thus, relative to the old factorization, the locally accessible state is
maximally mixed.

Now choose a second factorization of the same global Hilbert space, intended
only to represent the candidate local description assigned to a new aeon:

$$
\mathcal{H} =
\mathcal{H}_{A'} \otimes \mathcal{H}_{B'}.
$$

Because the tensor-product structure is not fixed by the abstract
four-dimensional Hilbert space alone, one may choose a new factorization in
which the same vector $|\Psi\rangle$ is separable:

$$
|\Psi\rangle = |0_{A'}\rangle \otimes |0_{B'}\rangle.
$$

Explicitly, one may define a new product basis by setting:

$$
|0_{A'}0_{B'}\rangle =
\frac{1}{\sqrt{2}}
\left(
|0_A0_B\rangle + |1_A1_B\rangle
\right),
$$

$$
|0_{A'}1_{B'}\rangle =
\frac{1}{\sqrt{2}}
\left(
|0_A0_B\rangle - |1_A1_B\rangle
\right),
$$

$$
|1_{A'}0_{B'}\rangle = |0_A1_B\rangle,
\qquad
|1_{A'}1_{B'}\rangle = |1_A0_B\rangle.
$$

This defines a valid tensor-product structure
$\mathcal{H}_{A'} \otimes \mathcal{H}_{B'}$ on the same abstract
four-dimensional Hilbert space, with the original Bell state now appearing as a
product state in the primed factorization.

Equivalently, let $U$ be the global unitary that maps the original computational
product basis, in order, to the four primed basis vectors above. Then

$$
|\Psi\rangle=U|0_A0_B\rangle,
\qquad
\mathcal{A}_{n+1}^{0}=U\mathcal{A}_n^{\infty}U^{\dagger}.
$$

This makes explicit that the two finite-dimensional factorizations are related
by a global unitary. The illustration supplies no physical reason to privilege
one embedding over the other.

The new local observable algebra is:

$$
\mathcal{A}_{n+1}^{0} =
\mathcal{B}(\mathcal{H}_{A'}) \otimes I_{B'}.
$$

The reduced state seen by the new local observer is:

$$
\rho_{A'} =
\mathrm{Tr}_{B'}(|\Psi\rangle\langle\Psi|)
=
|0_{A'}\rangle\langle 0_{A'}|.
$$

Therefore:

$$
S_{\mathrm{ent}}(\rho \mid \mathcal{A}_{n+1}^{0})
=
S(\rho_{A'})
=
0.
$$

The assumed global state has not changed:

$$
\rho_{n+1}=\rho_n=\rho.
$$

The global von Neumann entropy remains zero throughout:

$$
S_{\mathrm{vN}}(\rho) = 0.
$$

The two descriptions differ only in their chosen local factorization and
accessible observable algebra.

The values above are entanglement entropies of reduced density matrices. They
are not calculations of Boltzmann entropy, observational entropy, horizon or
gravitational entropy, or the entropy of a cosmological heat-death state. The
illustration therefore does not establish the target inequality for
$S_{\mathrm{eff}}$ in Section 3; it only demonstrates that one
factorization-relative entropy can differ for the same pure vector.

The illustration reproduces the following standard factorization dependence:

```text
same global pure state
+ old factorization
-> locally maximally mixed state

same global pure state
+ new factorization
-> locally pure state
```

The calculation does not show that a refactorization occurs, nor that either
factorization is physically privileged. In finite-dimensional Hilbert space,
an arbitrary refactorization can make entanglement entropy appear or disappear
by construction. A physical theory must therefore provide a selection principle
for the factorization and separately connect the selected algebra to a
thermodynamically relevant entropy. One possible route is quantum
mereology: the preferred factorization is not arbitrary, but selected by a
Hamiltonian, locality, robustness of pointer states, or quasi-classical
dynamics. The interaction-projection cost tested in Section 3 is one simple
Hamiltonian-locality proxy, and its preliminary no-go result shows that this
particular route does not supply the bipartite-entanglement contrast used in the
finite-dimensional illustration. It does not settle the paper's distinct,
still-unspecified cosmological $S_{\mathrm{eff}}$. More sophisticated selectors
still need independent, non-circular motivation. In the cosmological hypothesis,
the missing task is to explain why extreme dilution, dark-energy dominance, or
a boundary condition at an aeonic transition would naturally select the new
algebra $\mathcal{A}_{n+1}^{0}$.

There is also a field-theoretic limitation. The illustration uses a
finite-dimensional type-I Hilbert-space factorization, where partial traces and
reduced density matrices are well-defined. Local algebras in nongravitational
relativistic quantum field theory are typically type-III von Neumann algebras,
where a spatial tensor-product factorization and ordinary reduced density
matrices are not available in the same way
([Witten](https://arxiv.org/abs/1803.04993)). Gravitationally dressed observable
algebras need not have that type: a de Sitter static-patch construction yields a
type-II$_1$ algebra with a corresponding entropy
([Chandrasekaran et al.](https://arxiv.org/abs/2206.10780)), while clock-defined
algebras in semiclassical cosmological spacetimes can be type-II$_\infty$
([Chen & Penington](https://arxiv.org/abs/2406.02116)). A full extension must
therefore identify the physically relevant algebraic class and define locality,
entropy, and restriction without relying on naive partial tracing.

Comparing entropies of different gravitational algebras also requires a common,
physically justified reference and compatible normalization and renormalization
conventions. A type-II$_1$ factor has a canonical normalized trace, whereas a
type-II$_\infty$ factor's semifinite trace is defined only up to a positive
rescaling, which shifts its state entropy by an additive constant
([Chen & Penington](https://arxiv.org/abs/2406.02116)). Where algebra entropy
represents generalized entropy, the comparison must consistently include the
horizon contribution and matter entropy. In the cited de Sitter static-patch
construction, empty de Sitter space is the maximum-entropy state, not a
low-entropy initial state
([Chandrasekaran et al.](https://arxiv.org/abs/2206.10780)). Thus dilution alone
does not establish the proposed entropy contrast, and independently chosen
entropy offsets cannot establish it either. This additional continuum
requirement does not change the declared conventions or results of the finite
examples.

### 5.2 A fixed measurement-relative entropy

Keep the state $\rho=|\Phi^+\rangle\langle\Phi^+|$ and the original U above,
whose columns are $(\Phi^+,\Phi^-,01,10)$. This is a separate example from
Section 3's singlet/Hamiltonian calculation. Neither the state nor its two
embeddings is selected by that finite-time criterion.

For a specified POVM $\mathcal C=\{E_i\}$, use the established observational
entropy, in bits,

$$
S_{\mathcal C}(\rho)=-\sum_i p_i\log_2(p_i/V_i),\qquad
p_i=\operatorname{Tr}(\rho E_i),\quad V_i=\operatorname{Tr}E_i.
$$

All traces defining volume use the same global four-dimensional space;
zero-probability terms vanish. This applies the definition of
[Buscemi, Schindler & Safranek](https://arxiv.org/abs/2209.03803).
The protocol chooses one of X,Y,Z uniformly, measures its binary outcome
$s=\pm1$, and retains both axis and sign. It is not a serial measurement of
three incompatible observables. With $W=I_4$ or U for the two embeddings,

$$
E_{j,s}^{W,\eta}=\frac16W[(I_2+s\eta\sigma_j)\otimes I_2]W^\dagger,
\qquad 0\leq\eta\leq1.
$$

Each effect has volume 2/3. The axis weights, frame, retained records and
volume convention are fixed before the comparison. For the stipulated
white-noise family $\rho_p=(1-p)\rho+pI_4/4$, $0\leq p\leq1$, put
$x=\eta(1-p)$ and let $h_2$ be the binary Shannon entropy. Direct evaluation gives

$$
S_{\mathcal C_I}(\rho_p)=2,\qquad
S_{\mathcal C_U}(\rho_p)=\frac53+\frac13h_2\left(\frac{1+x}{2}\right).
$$

At ideal purity and sharpness the contrast is 1/3 bit. It stays positive for
$p<1$ and $\eta>0$ in this family, tending to zero at complete mixing or zero
sharpness. This is not a general apparatus-noise or finite-sample robustness
claim. X or Y alone yields two bits in both descriptions; Z alone yields two
versus one at the ideal point. The definition is therefore explicitly
measurement-relative, not fixed by the algebra alone.

This state-specific contrast does not establish a measurement ordering valid
for every input, or superior performance on every information-processing task.
For general POVMs, classical-postprocessing, measured-relative-entropy and
observational-entropy orderings are inequivalent:
[Teixido-Bonfill, Schindler & Safranek (2025)](https://arxiv.org/abs/2310.14086v3).
Accordingly, "readability" here refers only to the declared state family and
measurement protocol, not universal information access or a physical selection
principle.

| Quantity at the ideal point | Old description | New description |
|---|---|---|
| Global von Neumann entropy | 0 bits | 0 bits |
| Reduced-state entropy, equal to entanglement entropy for this pure input | 1 bit | 0 bits |
| Fixed XYZ observational entropy | 2 bits | 5/3 bits |
| Cosmological $S_{\mathrm{eff}}$ | Not supplied | Not supplied |

The inaccessible factor contributes one bit through global trace volumes;
subtracting it would change the defined quantity. The six effects span the
embedded qubit algebra for $\eta>0$, but tomography of its marginal is not
the same entropy calculation. For mixed inputs reduced-state entropy is not
an entanglement measure. A generic POVM's observational entropy is also not
the von Neumann entropy of its Petz reconstruction or postmeasurement state.

Simultaneous conjugation of state and effects preserves all probabilities and
volumes. Here the effects change relative to a fixed state. Consequently the
lower value is a comparison of measurement descriptions, not a trajectory
of decreasing entropy. The detailed formulas, controls and fixed-grid checks
are in the [operational supplement](./research/v015/operational-entropy.md).

### 5.3 Physical access and closure

The new observables have the explicit original-factor form

$$
X'=\frac{X\otimes I+Z\otimes X}{\sqrt2},\quad
Y'=\frac{I\otimes Y+Y\otimes Z}{\sqrt2},\quad Z'=Z\otimes Z.
$$

Their outcome statistics can be implemented by local operations and classical
communication (LOCC), assuming both original qubits are addressable:

| Setting | Local implementation |
|---|---|
| $X'$ | Measure X on B, send result b to A, then measure $(X+bZ)/\sqrt2$ on A. |
| $Y'$ | Measure Y on A, send result a to B, then measure $(Y+aZ)/\sqrt2$ on B. |
| $Z'$ | Measure Z on both and report the product of signs. |

Retain only the chosen axis and final sign. The branch effects in the supplement
sum to the target POVM effects, including the axis probability 1/3. This operator
identity holds for every input, not only the Bell state. An independent sign
flip of probability $(1-\eta)/2$ realizes
the same unsharp effects. No inter-qubit gate, quantum communication between
the original subsystems or additional shared entangled ancilla is needed for
these statistics. This is a sufficient
protocol, not an optimum in communication, time, energy or apparatus cost.

A-only access is insufficient for $\eta>0$: $|00\rangle$ and $|01\rangle$ have the same A
marginal but different parity statistics. At $\eta=0$ the outputs are
state-independent. The construction thus exposes an added access assumption;
ICC has not derived why both-factor access becomes available. Equal outcome
counts and trace volumes do not establish equal physical resources.

These measurements do not implement arbitrary coherent operations on the new
subsystem. On $|++\rangle$, ideal coherence-preserving parity measurement has a Bell
state as its normalized even-parity output, whereas separate local Z readouts
give $(|00\rangle\langle00|+|11\rangle\langle11|)/2$. The outcome probabilities
agree, but the instruments differ. Unassisted LOCC cannot realize the ideal
instrument with its quantum outputs on the original A and B, because that
would create entanglement from a product input; see
[Chitambar et al.](https://arxiv.org/abs/1210.4583) for the operational classes.

Intermediate local results also exist even when omitted from the final
record. Retaining them defines a refined POVM, whose entropy need not equal
the six-outcome value. Omitting a record is not a modeled thermodynamic
erasure or restoration of coherence. No physical entropy reset, selected
algebra, field-theoretic extension or cosmological transition follows.
The finite-example sequence is closed at this operational boundary.

### 5.4 Stability under finite algebra perturbations

A separate robustness question concerns the restricted von Neumann entropy
used in Section 5.1, not the POVM entropy in Section 5.2. Let
$\mathcal H=\mathbb C^d\otimes\mathbb C^m$, $d\ge2$, and let
$A,B\subset\mathcal B(\mathcal H)$ be unital factors of the same type $M_d$
and multiplicity $m$. For any fixed density matrix $\rho$, choose embeddings
$\iota_A(a)=W_A(a\otimes I_m)W_A^\dagger$ and define

$$
\sigma_A=\operatorname{Tr}_m(W_A^\dagger\rho W_A),\qquad
S_\rho(A)=-\operatorname{Tr}_d(\sigma_A\log_2\sigma_A),
$$

with the analogous definition for $B$. This uses ordinary local matrix trace
and bits and is independent of local basis. For mixed global states it is not
an entanglement measure.

Let $\delta=d_{\rm KK}(A,B)$ be the two-sided operator-norm Hausdorff distance
between their entire closed unit balls, following
[Kadison and Kastler (1972)](https://doi.org/10.2307/2373592). Define

$$
\omega_d(x)=h_2(t)+t\log_2(d-1),\qquad
t=\min\{x,1-1/d\},
$$

where $h_2$ is binary entropy. Then the direct finite-factor bound is

$$
|S_\rho(A)-S_\rho(B)|\le\omega_d(\delta).
$$

To see this, the trace-preserving conditional expectation $E_B$ obeys
$\|a-E_B(a)\|\le2\delta$ on $A$'s unit ball. The pulled-back map
$\Phi=\iota_B^{-1}E_B\iota_A$ is completely positive, unital and
trace-preserving because the multiplicities agree. Its trace adjoint has
the same properties. For $\tau_A=\Phi^*(\sigma_B)$, trace-norm duality gives
$\tfrac12\|\sigma_A-\tau_A\|_1\le\delta$, while bistochasticity gives
$S(\tau_A)\ge S(\sigma_B)$. Applying
[Audenaert's continuity inequality](https://arxiv.org/abs/quant-ph/0610146)
and then interchanging $A$ and $B$ proves the bound. The cap in $\omega_d$
is essential when substituting an upper bound on trace distance.

For example, $d=2$ and $\delta\le0.01$ limit the change to approximately
0.080793 bits. A two-endpoint comparison has the sum of the two corresponding
error bounds. These are conditional guarantees: a finite sample of observables
does not certify the required unit-ball distance. The proof does not select
an algebra, require a pure or stationary state, or construct a physical
operation changing access.

The [full derivation and checks](./research/v016/entropy-stability.md) also
give an explicit growing-dimension sequence whose algebra distances tend to
zero while its entropy gaps tend to one bit. Thus this estimate cannot become
dimension-independent without additional restrictions. It is not a type-III,
gravitational, or continuum entropy theorem, and it does not control the
entropy of an unspecified measurement protocol. No new universal
Kadison-Kastler stability theorem is assumed or certified here.

## 6. Relation to Existing Frameworks

### LambdaCDM

The standard model remains the observational baseline. Planck 2018 found strong
consistency with six-parameter flat LambdaCDM and no compelling evidence for
extensions: [Planck 2018](https://arxiv.org/abs/1807.06209). This hypothesis
differs by treating the cosmic endpoint as informationally continuous with an
effective new beginning.

### DESI and dark energy

DESI DR2 BAO measurements are well described by flat LambdaCDM on their own.
When combined with CMB and supernova data, however, they favor a time-varying
dark-energy equation of state at a significance that depends on the supernova
sample, with unknown systematics still a possible qualification:
[DESI DR2](https://arxiv.org/abs/2503.14738). This matters because the fate of
expansion determines whether dilution, boundary formation, or another
transition mechanism is possible.

### Penrose CCC

Penrose's conformal cyclic cosmology joins the future conformal infinity of one
aeon to the conformally stretched Big Bang of the next across a crossover
surface: [Meissner & Penrose](https://arxiv.org/abs/2503.24263). Its defining
transition is conformal-geometric; it does not identify successive aeons as
different locally readable observable algebras of one fixed global quantum
state. Proposed CMB Hawking-point evidence remains contested. An et al. claim a
detection, while Jow and Scott and Bodnia et al. report no statistically
significant evidence: [An et al.](https://arxiv.org/abs/1808.01740),
[Jow & Scott](https://arxiv.org/abs/1909.09672),
[Bodnia et al.](https://arxiv.org/abs/2208.06021).

### Exactly periodic quantum cyclic cosmology

Carroll, Diachenko, and Dulani propose an exactly periodic cosmology in a
finite-dimensional Hilbert space and discuss quantum mereology as a still
preliminary route to a semiclassical interpretation. Their mechanism relies on
unitary state evolution, commensurable energy gaps, and a distinguished
low-entropy excursion associated with a Crunch/Bounce/Big-Bang phase:
[Carroll, Diachenko & Dulani](https://philsci-archive.pitt.edu/29823/).

The present hypothesis shares the use of finite-dimensional quantum mereology
as a possible route to emergent subsystem structure, but proposes a different
mechanism. It does not identify the cycle primarily with periodic evolution of
the global state. Instead, it asks whether an effectively new aeon can arise
through a change in the locally accessible observable algebra or factorization
of a globally conserved state. Whether that distinction can be made physically
meaningful, rather than merely redescribing the same dynamics, is an open
question.

### Black-hole information

Recent Page-curve and island results support the possibility that black-hole
evaporation can preserve information in quantum gravity models:
[Almheiri et al.](https://arxiv.org/abs/1908.10996),
[Raju review](https://arxiv.org/abs/2012.05770).

### Emergent spacetime and holography

AdS/CFT supplies a concrete gauge/gravity duality, the Ryu-Takayanagi proposal
relates boundary entanglement entropy to bulk minimal-surface area, and Van
Raamsdonk argues that bulk connectivity is tied to entanglement:
[Maldacena](https://arxiv.org/abs/hep-th/9711200),
[Ryu-Takayanagi](https://arxiv.org/abs/hep-th/0603001),
[Van Raamsdonk](https://arxiv.org/abs/1005.3035). These results motivate
information-theoretic approaches to geometry in specific holographic settings;
they do not establish the present cosmological proposal.

### Relational time and clock ambiguity

The hypothesis is related to Page-Wootters-style relational time, where a
stationary constrained state can encode conditional dynamics relative to an
internal clock: [Page & Wootters](https://doi.org/10.1103/PhysRevD.27.2885),
[Moreva et al.](https://arxiv.org/abs/1310.4691),
[Marletto & Vedral](https://arxiv.org/abs/1610.04773). The ideal construction
requires a compatible clock/rest decomposition and constraint; interactions or
mixed global states can modify the resulting conditional dynamics:
[Rijavec](https://arxiv.org/abs/2204.11740).

The non-uniqueness of the clock choice can underdetermine the effective history
and laws:
[Albrecht & Iglesias](https://arxiv.org/abs/0708.2743). Whether ideal
non-interaction removes this ambiguity is contested by a recent analysis that
instead requires physical meaning to be assigned to the observables:
[Stoica](https://arxiv.org/abs/2604.21805). None of these constructions derives
a thermodynamic arrow from relational time alone. An extended finite-dimensional
Page-Wootters model obtains an informational arrow only after adding
inaccessible auxiliary degrees of freedom and effective noisy dynamics:
[Jesni Shamsul Shaari](https://doi.org/10.1016/j.physleta.2026.131456). This
provides an example of the additional coarse-graining needed, not a derivation
of a macroscopic cosmological arrow from the clock mechanism itself.

### Relational and cosmological observable algebras

Quantum-reference-frame work demonstrates that different relational
perspectives can induce different subsystem observable algebras and therefore
different notions of subsystem locality and entanglement
([Ahmad et al.](https://arxiv.org/abs/2103.01232)). This is close kinematic prior
art for the present proposal, but it does not identify those perspectives with
successive aeons or supply an entropy-reset mechanism.

Observable-algebra embeddings have also been used to extract a cosmological
sector from full loop quantum gravity
([Koslowski](https://arxiv.org/abs/0711.1098)). More recent constructions use
physical clocks or observer dressing to define type-II gravitational observable
algebras in de Sitter and other cosmological settings
([Chandrasekaran et al.](https://arxiv.org/abs/2206.10780),
[Chen & Penington](https://arxiv.org/abs/2406.02116)). These results are relevant
to the missing definitions of physical accessibility and effective entropy, but
none provides the aeonic boundary relation or repeatable selector proposed here.

### Factorization-relative entanglement

The finite-dimensional illustration uses the established fact that subsystem
structure, entanglement, and reduced-state entropy depend on the observable
algebra or tensor-product structure. This operational and algebraic relativity
is developed in [Zanardi](https://arxiv.org/abs/quant-ph/0103030),
[Harshman & Ranade](https://arxiv.org/abs/1102.0955), and
[Thirring et al.](https://arxiv.org/abs/1106.3047). The present note does not
extend those mathematical results; it asks whether they admit a physically
selected aeonic interpretation.

### Transport of observable algebras

[Zanardi (2026)](https://arxiv.org/html/2609.28662v1) develops a canonical
connection and holonomic transport on finite observable-algebra orbits of
fixed block structure. This supplies transport along a specified path, not
the path itself. The [bounded applicability review](./research/v016/transport-applicability.md)
exhibits a horizontal two-qubit path with a one-to-zero-bit restricted-entropy
contrast for a fixed Bell state. Co-transporting the state and algebra instead
preserves that entropy. The path and stopping point are prescribed, not
selected by independent physical data. Geometric reparameterization invariance
does not supply a relational clock or remove the control and gap requirements
of an adiabatic implementation. This is conditional geometric prior art, not
an ICC selector, cosmological transition, or extension to continuum algebras.

### Quantum mereology and observational entropy

Quantum mereology studies how preferred subsystem decompositions might be
selected rather than assumed in advance. Carroll and Singh propose selecting
quasi-classical factorizations by limiting entanglement growth and internal
spreading:
[Carroll & Singh](https://arxiv.org/abs/2005.12938). Operational quantum
mereology instead represents generalized subsystem structures by an observable
algebra and its commutant, and uses minimal algebraic scrambling as a dynamical
criterion:
[Zanardi et al.](https://arxiv.org/abs/2212.14340). Its Gaussian criterion is
equivalent to the interaction-projection cost on the finite bipartite
factor-algebra domain, as shown above; it is not an independent replacement
for that tested selector. A related toy-universe model
jointly selects Hamiltonian structure, subsystem decomposition, and a
low-entropy state through a variational principle:
[Shokrian Zini, Brown & Freedman](https://arxiv.org/abs/2208.00944).

None of these results supplies the aeonic boundary relation proposed here, but
they constrain what a non-arbitrary selector $\mathcal{F}$ could mean. The
proposed cosmological entropy remains unspecified. Section 5.2 uses an explicit
POVM-relative instance of established observational entropy, without identifying
it with that cosmological quantity or with global von Neumann entropy:
[Safranek, Deutsch & Aguirre](https://arxiv.org/abs/1803.00665),
[Buscemi, Schindler & Safranek](https://arxiv.org/abs/2209.03803).

For specified accessible algebras, the recent preprint by
[Rignon-Bret & Elouard (2026)](https://arxiv.org/abs/2607.09242v1)
develops entropy accounting based on maximum-entropy completions and specified
microscopic dynamics. This algebra-dependent construction is not automatically
the general-POVM entropy used in Section 5.2. It provides conditional
thermodynamic context, not a derivation of ICC's proposed boundary relation.
Changing an algebraic description alone does not establish a physical
transition, thermodynamic entropy reduction, or cosmological cycle; the
selection mechanism, operational dynamics and cosmological entropy remain
unresolved here.

In quantum field theory, entanglement is more naturally treated as a property
of local observable algebras rather than only as a property of states on
tensor-product factors:
[Witten](https://arxiv.org/abs/1803.04993).

### Constraints on the informational dark-sector extension

The extension's strongest empirical challenge is dark matter phenomenology.
Observations such as the
Bullet Cluster show gravitational lensing mass separated from the dominant
baryonic X-ray gas, strongly favoring some unseen gravitating component:
[Clowe, Randall & Markevitch](https://arxiv.org/abs/astro-ph/0611496). Any
informational-gravitational replacement must reproduce galaxy rotation curves,
lensing, CMB acoustic peaks, BAO, cluster collisions, and structure growth at
least as well as cold dark matter. The CMB spectra provide an independent
precision constraint: a replacement must reproduce the successful base-LambdaCDM
fit to the acoustic structure, not only late-time galaxy dynamics
([Planck 2018](https://arxiv.org/abs/1807.06209)).

## 7. Failure Criteria and Missing Physical Content

The central proposal's first vulnerability is the algebra-selection rule. In
this version, $\mathcal{R}$ is only an unspecified boundary relation and $T_n$
is one candidate pair of embeddings in that relation, not a quantum channel or
time-evolution map. The proposal must define the admissible family
$\mathfrak{E}_{\lambda}$, the intrinsic data $\lambda$, and a selector
$\mathcal{F}$ that chooses a stable physical equivalence class without assuming
the desired entropy decrease. It must also explain how relationally derived
data such as $\lambda_n^{\infty}$ and $\lambda_{n+1}^{0}$ can differ while the
global state and constraint remain fixed; otherwise repeated evaluation selects
the same algebra and no aeonic change occurs.

Over the unrestricted finite bipartite factorization space, the simple
interaction-projection selector tested in Section 3 appears to fail the
entanglement-contrast test: under the stated assumptions, its strict local
minima cannot support an entangled isolated stationary eigenstate. This result
should be independently checked, especially its quotient-space step based on
reduced-state purity. The restricted EC/CAR calculation does not refute it; it
removes the relevant descent directions by limiting the admissible manifold.
That finite construction passes the full-Fock and fixed-$N=4$ tests, but its
physical relevance now depends on deriving the restriction independently in a
continuum theory. Neither result addresses a separately specified
observational or subalgebra-relative $S_{\mathrm{eff}}$.

The separate finite-time example shows why the cost-specific obstruction
cannot simply be generalized to every finite-time strict local minimum. It
does not supply physical selection: its entangled branch is outperformed by
the stated product competitor. Likewise, Section 5 supplies a concrete
measurement-relative entropy and an all-input measurement implementation, not
an independently motivated selection or change of access. These tasks remain
separate; their partial results do not jointly constitute a transition law.

Appendix B supplies another bounded limitation. For its exact simple-spectrum
logarithmic Hamiltonian, compatible multiplication families differ by diagonal
unitaries preserving any normal stationary state. Their corresponding
restricted entropies therefore agree. An independently specified coherent
reference fixes an embedding but does not evade this obstruction; unrestricted
operator-norm stability of that reconstruction also fails. A separate fixed-window
analysis gives local continuity at each full-support reference, but no uniform
guarantee from an energy budget alone. These conclusions do not apply
automatically to a different constraint, a nonstationary target, or other
energy-restricted error criteria.

The boundary labels are also not yet mathematical limits. Any asymptotic
interpretation of the superscripts $\infty$ and $0$ requires a relational
parameter, topology, and convergence law; otherwise they remain labels for the
two sides of the proposed association.

The second vulnerability is physical equivalence. If the old and new embeddings
differ only by a global unitary relabeling, with no intrinsic operational
criterion distinguishing them, the proposal has no physical content beyond a
change of description.

The third vulnerability is temporal orientation. Page-Wootters conditioning
can recover relational dynamics, but the proposal must separately derive a
low-entropy boundary, typical observational-entropy growth, and stable records.
It must also show that the algebra selector chooses a physically meaningful
clock/rest decomposition rather than one engineered to encode the desired
history.

The fourth vulnerability is the field-theoretic and gravitational extension.
The finite-dimensional illustration uses type-I tensor-product factorization
and partial traces. A realistic version must identify the appropriate local or
gravitational observable algebras, which may involve type-III algebras in local
QFT or type-II algebras after gravitational dressing, and must define effective
entropy without relying on the naive finite-dimensional reduced density matrix.

The fifth vulnerability is observational uniqueness. The hypothesis must
predict something different from LambdaCDM, Penrose CCC, exactly periodic
finite-dimensional quantum cyclic cosmology, and existing emergent-gravity
models.

The sixth vulnerability is cyclicity itself. One admissible boundary pair does
not establish a cycle. The proposal must show that its intrinsic selection rule
can generate a repeatable family of compatible aeonic boundaries and
within-aeon relational histories without inserting each new low-entropy
description by hand.

### Extension-specific failure conditions

The informational dark-sector extension fails in its present form if it cannot
derive a covariantly consistent gravitational source and reproduce CMB acoustic
peaks, BAO, lensing, cluster collisions, halo phenomenology, and structure
growth. A direct particle detection that accounts for the dark-matter
phenomenology without a residual informational component would falsify the
extension's stated non-particle interpretation, not automatically the central
aeonic proposal.

Stable massive particles are fatal only to versions that require a conformal
loss of scale. They do not by themselves falsify the more general algebraic
boundary relation.

The dark-energy extension remains unsupported until a fixed cosmological
constant or a dynamical dark-energy field is shown to provide intrinsic
boundary data or a selection mechanism for the new observable algebra.

## 8. Working Summary

This is not yet a complete physical theory. It is a structured hypothesis:

> The universe may be one globally conserved informational structure. Time,
> entropy, matter, and cosmic history are local readings of that structure. A
> cosmic cycle would not be a restart in external time, but a change in local
> readability: the same global information that appears maximally disordered at
> the end of one description may induce a low-effective-entropy state on a
> differently embedded or refactored local observable algebra at the beginning
> of another.

The proposed contribution is this aeonic interpretation of a change in the
physically privileged local observable algebra. The note does not claim a new
general factorization theorem, and it does not yet derive an aeonic transition
from a Hamiltonian, boundary condition, or other dynamical principle. One
simple Hamiltonian-only selector fails the stated unrestricted
finite-dimensional entanglement test, while an Einstein-Cartan-inspired
restriction of its admissible CAR family yields a bounded finite example with
strict competing minima and stationary entanglement contrast at two cells. Its
first three-cell extension fails boundary-independent robustness. A four-cell
periodic extension has a locally robust small-twist branch, but a matched
non-axial density contact reproduces the primary gate and the same branch-cost
law. The final bounded classification shows that every nonzero contact in the
declared translation-invariant onsite quartic class shares that law. The
construction is therefore retained only as a bounded example of generic
kinetic-versus-onsite competition rather than a scalable or EC-specific
selector candidate. The restriction is not yet derived from continuum physics,
and none of these results decides whether a physically defined cosmological
$S_{\mathrm{eff}}$ could exhibit the proposed contrast.

The finite-time follow-up admits an entangled strict local minimum but does
not make it globally preferred, operationally superior in the specified
recovery task, or physically selected. Independently, the two-qubit
measurement protocol gives a fixed-state observational-entropy contrast of
1/3 bit and an explicit local implementation with classical communication.
Neither comparison is a physical entropy-reducing process. The finite studies
clarify operational meaning and limitations; they do not derive algebra
selection, relational transition dynamics, or cosmological cycling. This
version closes these finite examples rather than extending their scope.

The arithmetic follow-up in Appendix B likewise identifies missing physical
input rather than supplying it. Its conditional reconstruction cannot produce
the proposed contrast for a fixed stationary state in the stated model, and
small reference errors need not give small full operator-norm algebra errors.
At fixed finite access, an independently certified reference-amplitude floor
provides a conditional robustness bound; energy restriction alone does not.
The reference-phase-only route is therefore closed as an ICC transition
candidate under these assumptions. The reconstruction and stability results
remain useful as conditional mathematical results, not a transition mechanism.
The broader physical selector question remains open; these limitations are not
a universal no-go theorem for ICC.

Appendix C separates a genuine loss of attainable measurement capability from
an inefficient chosen readout. The loss follows under a supplied access
boundary and fixed symmetry restriction; it disappears under unrestricted
symmetric access to the retained old input. Both reduced capability sets span
the same operator algebra. This identifies a finite operational distinction,
not the missing physical algebra selector or a cosmological entropy change.

To become a physical theory, the hypothesis needs:

1. a rigorous definition of the admissible observable algebras and their
   embeddings, including a relational definition of the boundary regimes and a
   topology if genuine limits are claimed,
2. a precise relation $\mathcal{R}$ and a criterion selecting the candidate pair
   $T_n$ independently of the desired entropy conclusion,
3. an intrinsic, non-circular rule that jointly determines the physically
   privileged algebra and the relational data $\lambda_n$ that can distinguish
   successive conditional regimes,
4. a demonstration that the selected construction is repeatable across aeonic
   boundaries rather than specifying only one pair,
5. a physically justified cosmological definition of effective entropy
   `S_eff` and its target contrast, rather than an inference from either toy
   entanglement entropy or the stipulated finite measurement protocol,
6. a field-theoretic version that can handle local operator algebras beyond the
   finite-dimensional illustration,
7. a compatible relational-clock construction and a separate derivation of the
   thermodynamic arrow,
8. at least one observational prediction that differs from LambdaCDM, Penrose
   CCC, exactly periodic quantum cyclic cosmology, and emergent-gravity models.

The optional cosmological extensions additionally require a derivation of
$T_{\mu\nu}^{\mathrm{info}}$ or another precise gravitational modification, a
clear statement of whether conformal scale loss is required, and a mechanism by
which dark energy supplies boundary data rather than merely cosmic dilution.

## Appendix A. Restricted Einstein-Cartan-Inspired CAR Selector

This appendix summarizes a finite follow-up to the selector problem in Section
3. It is supplementary to the central ICC hypothesis. The complete derivation,
additional perturbation checks, and executable calculations are supplied in
[the companion derivation](./research/einstein-cartan-circuit-selector.md),
[the full-Fock calculation](./research/ec_axial_selector_analysis.py),
[the exact spectral certificate](./research/ec_ground_state_certificate.py),
[the fixed-sector gate](./research/ec_fixed_sector_selector.py),
[the adversarial controls](./research/ec_selector_adversarial_controls.py),
and
[the superselection controls](./research/ec_superselection_controls.py). The
first larger finite stress test is supplied in
[the three-cell report](./research/three-cell-finite-gate.md) and
[its executable calculation](./research/ec_three_cell_selector.py).
The ranked internal critique is
[the v0.1.3 adversarial review](./feedback/v0.1.3-adversarial-review.md).
The proof-level follow-up is
[the v0.1.3 mathematical audit](./feedback/v0.1.3-mathematical-audit.md). The
three-cell increment received separate
[physics](./feedback/three-cell-physics-review.md) and
[mathematics](./feedback/three-cell-mathematical-review.md) reviews before
integration. The four-cell extension is supplied in the
[finite gate](./research/four-cell-finite-gate.md),
[boundary-phase report](./research/four-cell-boundary-phase-gate.md), and
[matched-control report](./research/four-cell-matched-control-gate.md), with
separate
[mathematical](./feedback/four-cell-matched-control-mathematical-review.md) and
[physics](./feedback/four-cell-matched-control-physics-review.md) reviews. The
full onsite class is treated in the
[analytic closure](./research/four-cell-onsite-closure.md), its
[reproducibility script](./research/ec_four_cell_onsite_closure.py), and the
separate [mathematical review](./feedback/four-cell-onsite-closure-mathematical-review.md).

### A.1 Finite fermionic model

Take two spatial cells and four Dirac components per cell:

$$
\mathfrak h=\mathbb C^2_{\mathrm{cell}}\otimes
\mathbb C^4_{\mathrm{Dirac}},
\qquad
\mathcal H=\mathcal F(\mathfrak h),
\qquad
\dim\mathcal H=2^8=256.
$$

With the link spacing absorbed into the coefficients, define

$$
H(t,g)=tK+gQ,
$$

$$
K=-i\left(\psi_1^\dagger\alpha^1\psi_2
-\psi_2^\dagger\alpha^1\psi_1\right),
$$

and

$$
Q=\sum_{x=1}^{2}
\left[
:\!\left(\psi_x^\dagger\gamma^5\psi_x\right)^2\!:
-\sum_{i=1}^{3}
:\!\left(\psi_x^\dagger\alpha^i\gamma^5\psi_x\right)^2\!:
\right].
$$

The contact term is the finite-mode axial-axial channel corresponding to
$J_5^\mu J^5_\mu$. Eliminating algebraic, non-propagating torsion in
Einstein-Cartan fermion theory produces a local four-fermion interaction that
includes this channel. Its sign and coefficient depend on conventions and on
possible non-minimal couplings
([Diakonov, Tumanov & Vladimirov](https://arxiv.org/abs/1104.2432)). Only $g^2$
enters the selector branch diagram. For comparison,
[Khanapurkar et al.](https://arxiv.org/abs/1804.04434) derive a
non-relativistic limit directly from the Einstein-Cartan-Dirac field equations.
The present finite-mode truncation is neither a discretized solution of those
equations nor such a controlled limit.

A microscopic Einstein-Cartan cosmology with torsion-induced effective
four-fermion interactions can produce a bounce
([Lucat & Prokopec](https://arxiv.org/abs/1512.06074)), but that construction
does not derive the algebra selector used here.

### A.2 Restricted candidate factorizations

Arbitrary factorizations of the 256-dimensional Fock space belong to the
unrestricted setting of the no-go argument. The number-preserving Fock-space
lifts $\Gamma(V)$ of one-particle $U(8)$ transformations form a proper subgroup
of $U(256)$, not the unrestricted domain. We restrict to these
one-particle transformations and further require normalization of the internal
Dirac matrix algebra

$$
\mathfrak D=I_2\otimes M_4(\mathbb C),
\qquad
V\mathfrak D V^\dagger=\mathfrak D.
$$

Because every automorphism of $M_4(\mathbb C)$ is inner, every such unitary has
the form

$$
V=W\otimes S,
\qquad W\in U(2),\quad S\in U(4).
$$

The common $S$ acts only as an internal basis change inside each candidate
cell, so it does not alter the factorization. The induced unordered cell
decompositions form

$$
U(2)/\left((U(1)\times U(1))\rtimes S_2\right)
\simeq\mathbb{RP}^2.
$$

Equivalently, the candidate split is represented by

$$
\mathbf n=(n_x,n_y,n_z)\in S^2,
\qquad \mathbf n\sim-\mathbf n.
$$

Fermionic mode factors use a graded tensor product. The finite implementation
fixes a Jordan-Wigner ordering and works with parity-even Hamiltonians and
number-preserving candidate unitaries. The normalizer condition is the defining
restriction of this proof of concept. Its physical derivation is not supplied.

### A.3 Full-Fock selector and branch diagram

Lift $W$ to Fock space and project the transformed Hamiltonian onto one-factor
Kronecker-sum Hamiltonians using the Hilbert-Schmidt projection from Section 3.
The denominator in Section 3 removes the scalar component of the Hamiltonian.
Here $\operatorname{Tr}K=0$ and $\operatorname{Tr}Q/256=4$. Define
$\widetilde Q=Q-4I$. Direct CAR traces give

$$
\lVert K\rVert_2^2=512,
\qquad
\lVert \widetilde Q\rVert_2^2=8192,
\qquad
\langle K,\widetilde Q\rangle_{\mathrm{HS}}=0,
$$

$$
\lVert K_{\mathrm{int}}(\mathbf n)\rVert_2^2
=512(1-n_y^2),
$$

$$
\lVert Q_{\mathrm{int}}(\mathbf n)\rVert_2^2
=1536(1-n_z^2)(3+n_z^2),
$$

and a vanishing residual cross term. Therefore, with $r=g/t$,

$$
C(\mathbf n;r)=
\frac{
(1-n_y^2)+3r^2(1-n_z^2)(3+n_z^2)
}{1+16r^2}.
$$

For fixed $n_z$, minimization sets $n_x=0$. Writing $u=n_z^2$, the numerator is

$$
N(u;r)=u+3r^2(1-u)(3+u),
$$

a concave quadratic for $r\neq0$. Hence every global minimum is an endpoint
class. The momentum factorization $\mathbf n=\pm\hat{\mathbf y}$ is
global for $|r|<1/3$, the site factorization
$\mathbf n=\pm\hat{\mathbf z}$ is global for $|r|>1/3$, and they are co-global
at $|r|=1/3$. Both remain locally stable in the interval

$$
\frac1{\sqrt{12}}<|r|<\frac1{\sqrt6}.
$$

At the transition,

$$
C_{\min}=\frac9{25},
\qquad
C_{\mathrm{barrier}}=\frac{39}{100},
\qquad
\Delta C=\frac3{100}.
$$

Along the shortest $yz$ path
$\mathbf n(\alpha)=(0,\sin2\alpha,\cos2\alpha)$, four equal fermionic beam
splitters give the finite Grassmannian line element

$$
ds_{\mathrm{CAR}}^2=4\,d\alpha^2,
\qquad
d_{\mathrm{CAR}}(\mathrm{site},\mathrm{momentum})=\frac\pi2.
$$

This metric and the finite barrier permit a circuit-penalized update model, but
they do not derive a unique circuit action, transition rate, or relational
clock law. The geometric language follows the general circuit-geometry program
([Nielsen](https://arxiv.org/abs/quant-ph/0502070)) and its fermionic
developments ([Hackl & Myers](https://arxiv.org/abs/1803.10638)); no complexity
functional from those works is claimed to select this cosmological model.

### A.4 Fixed-particle-number gate

The full-Fock Hilbert-Schmidt inner product uses the trace on the entire Fock
space:

$$
\operatorname{Tr}_{\mathcal H}(X)
=\sum_{N=0}^{8}\operatorname{Tr}_{\mathcal H_N}(P_NXP_N).
$$

It therefore weights orthonormal Fock-space basis states equally, not
particle-number sectors equally. In a normalized-trace decomposition, sector
$N$ carries weight $\binom{8}{N}/256$. The primary weighting gate restricts
instead to

$$
\mathcal H_{N=4}
=\bigoplus_{k=0}^{4}
\left(\wedge^k\mathfrak h_+\right)\otimes
\left(\wedge^{4-k}\mathfrak h_-\right),
\qquad
\dim\mathcal H_{N=4}=70.
$$

Let $P_4$ be the total-number projector and let $N_\pm$ be the two local number
operators. Fix the local Hamiltonian subspace before selecting $H$ or
$\mathbf n$:

$$
\mathfrak L_4=
\left\{
P_4(A_+\widehat\otimes I+I\widehat\otimes A_-)P_4:
[A_+,N_+]=[A_-,N_-]=0
\right\}.
$$

It has dimension $135$. In the charge block with dimensions
$d_k=\binom4k$ and $d_{4-k}$, the orthogonal projection is

$$
\Pi_k(X)=
\frac{\operatorname{Tr}_{-}X}{d_{4-k}}\otimes I
+I\otimes\frac{\operatorname{Tr}_{+}X}{d_k}
-\frac{\operatorname{Tr}X}{d_kd_{4-k}}I,
$$

and off-diagonal charge blocks project to zero. This handles the common
particle-number center without counting its parametrization kernel as an extra
local direction.

In this sector $\operatorname{Tr}K=0$ and
$\operatorname{Tr}Q/70=24/7$. With
$\widetilde Q_4=Q-(24/7)I_{70}$, the centered sector traces give

$$
\lVert K\rVert_{2,4}^2=160,
\qquad
\lVert \widetilde Q_4\rVert_{2,4}^2=\frac{15744}{7},
\qquad
\langle K,\widetilde Q_4\rangle_{2,4}=0,
$$

$$
\lVert K_{\mathrm{int}}(\mathbf n)\rVert_{2,4}^2
=160(1-n_y^2),
$$

$$
\lVert Q_{\mathrm{int}}(\mathbf n)\rVert_{2,4}^2
=24(1-n_z^2)(71+25n_z^2),
$$

again with zero residual cross term. The normalized fixed-sector selector is

$$
C_4(\mathbf n;r)=
\frac{
160(1-n_y^2)+24r^2(1-n_z^2)(71+25n_z^2)
}{160+(15744/7)r^2}.
$$

It retains the same two strict branches. Their exchange and coexistence window
are

$$
|r_c|=\sqrt{\frac{20}{213}}\simeq0.3064257065,
$$

$$
\sqrt{\frac5{72}}<|r|<\sqrt{\frac{10}{69}}.
$$

At the transition,

$$
C_{4,\min}=\frac{497}{1153},
\qquad
C_{4,\mathrm{barrier}}=\frac{2163}{4612},
\qquad
\Delta C_4=\frac{175}{4612}.
$$

Thus the two-branch result is not confined to the unrestricted full-Fock
weighting. Gibbs and other state-weighted norms have not been tested.

### A.5 Stationarity and certificate boundaries

At the positive-coupling full-Fock co-global point $H_c=K+Q/3$, numerical
diagonalization gives

$$
E_0\simeq-4.11560796875,
\qquad
E_1-E_0\simeq0.620514177337.
$$

The supplied exact certificate constructs $3H_c$ directly from
Gaussian-integer CAR data. Conserved particle-number, chirality, and link-spin
labels split it into $65$ blocks of maximum dimension $18$. Exact rational
$LDL^\mathsf{T}$ inertia and the spectral factor

$$
p(\lambda)=
\lambda^4-20\lambda^3-144\lambda^2+3008\lambda-1792
$$

prove that the ground state is simple and

$$
E_1-E_0>\frac{923}{1500}.
$$

Its mode-entanglement entropies are evaluated numerically:

$$
S_{\mathrm{site}}\simeq3.01251822001\ \text{bits},
\qquad
S_{\mathrm{mom}}\simeq1.20884898928\ \text{bits},
$$

so $\Delta S_{\mathrm{mode}}\simeq1.80366923073$ bits. At the fixed-sector
transition $r=\sqrt{20/213}$, the numerically isolated ground state remains in
$N=4$ and has

$$
E_1-E_0\simeq0.678109892996,
\qquad
\Delta S_{\mathrm{mode}}\simeq2.00731779928\ \text{bits}.
$$

Because these ground states have fixed total particle number, their reduced
states are block diagonal in local particle number. Resolving the reduced state
into sectors allowed by local fermionic superselection reduces but does not
remove this contrast. The reported quantity is the probability-weighted
within-sector entropy; it excludes the Shannon entropy of the sector label. At
the positive-coupling full-Fock exchange point, the site-minus-momentum contrast
is numerically $0.698734$ bits
under local-number superselection and $0.995665$ bits under local-parity
superselection. At the positive fixed-$N=4$ exchange point the corresponding
values are $0.800293$ and $1.162493$ bits. These are operationally stricter
fermionic pure-state diagnostics, not a general mixed-state entanglement
measure or thermodynamic entropy. The local-number construction follows the
standard particle-entanglement decomposition
([Wiseman and Vaccaro](https://arxiv.org/abs/quant-ph/0210002)); fermionic
subsystems and parity superselection are reviewed by
[Szalay et al.](https://arxiv.org/abs/2006.03087).

A 121-point scan across the fixed-sector bistability interval found a minimum
sampled gap of $0.5359112$ and a minimum sampled entropy contrast of
$1.4856425$ bits. The fixed-sector spectral and entropy claims are numerical,
not interval-certified.

### A.6 Three-cell finite-size stress test

The first size extension uses three cells, four Dirac modes per cell, and the
half-filled sector

$$
\mathcal H_{3,6}=\bigwedge^6\mathbb C^{12},
\qquad
\dim\mathcal H_{3,6}=\binom{12}{6}=924.
$$

The admissible cell factorizations form
$U(3)/(U(1)^3\rtimes S_3)$ and have six continuous tangent directions. The
fixed-sector one-cell Hamiltonian space has 210 matrix-unit generators. Two
relations identify the three copies of the identity and a third is
$N_1+N_2+N_3=6I$. Row reduction of the integer Gram matrix modulo the prime
$1{,}000{,}003$ gives rank 207; together with those three exact relations, this
certifies the local-subspace dimension over $\mathbb Q$.

At each boundary condition the positive coupling is tuned to make the site and
kinetic-eigenmode endpoint costs equal. The primary numerical result is:

| Quantity | Open chain | Periodic ring |
|---|---:|---:|
| $g_c$ | 0.3501691221 | 0.4129483210 |
| Normalized endpoint cost | 0.4529794648 | 0.4717832957 |
| Minimum site Hessian eigenvalue | 0.1222247 | 0.4866812 |
| Minimum kinetic Hessian eigenvalue | **-0.0465277** | 0.2433404 |
| Lowest optimized cost found | **0.4413803** | 0.4717832957 |
| Ground-space multiplicity | **3** | 1 |
| Gap above the ground space | 0.5688714 | 0.2033920 |
| Mode-entropy contrast | not evidential | 1.7508546 bits |
| Local-number-SSR contrast | not evidential | 0.6380137 bits |
| Local-parity-SSR contrast | not evidential | 0.9787055 bits |

The open kinetic endpoint is not a local minimum. Direct motion along its
negative Hessian eigenvector lowers the cost, independently of optimizer
convergence. The periodic endpoints are numerically strict; 32 Haar samples
and optimization from eight random starts found no lower point, but do not
prove global minimality on the flag manifold.

The normalized endpoint-Hessian pattern is the same at the tested fillings
$N=4,5,6,7,8$: the open kinetic endpoint fails and both periodic endpoints are
locally strict. Periodic even fillings $N=4,6,8$ have isolated positive-contrast
ground states; the odd fillings have fourfold numerical ground-space
degeneracy and their arbitrary eigenvector entropies are not used. A non-axial
onsite density contact also produces strict competing endpoints, so the result
is not specific evidence for torsion dynamics.

The boundary comparison is not a bulk-limit test. At $L=3$, the open chain has
two links while the periodic ring has three, and the periodic
central-difference kinetic spectrum is $\{-\sqrt3,0,+\sqrt3\}$. Both the graph
and the naive-derivative spectrum therefore change at order one. The combined
result is classified as a boundary-independent robustness failure, with the
periodic branch retained only as a restricted finite numerical observation. No
conclusion about larger size follows from the three-cell comparison alone.

### A.7 Four-cell phase and matched-control gate

The even-size follow-up uses

$$
\mathcal H_{4,8}=\bigwedge^8\mathbb C^{16},
\qquad
\dim\mathcal H_{4,8}=\binom{16}{8}=12{,}870,
$$

and the 12-dimensional quotient
$U(4)/(U(1)^4\rtimes S_4)$. Exact combinatorial partial traces evaluate the
centered Hilbert-Schmidt selector without constructing a dense
$12{,}870\times12{,}870$ Hamiltonian. The implementation is checked against
dense low-filling matrices, sparse half-filled occupation-mask actions,
projection overlaps, traces, norms, quotient invariance, and finite-difference
step convergence.

At periodic boundary conditions, the kinetic operator has a two-dimensional
zero eigenspace. A fixed grid-plus-refinement rule resolves its basis freedom
using the interaction selector before the endpoint coupling is set. At the
equal-endpoint axial coupling $g_0=0.4298279139$, the site and resolved periodic
representatives have minimum quotient-Hessian eigenvalues 0.177740 and
0.122137. A prescribed gauge transport

$$
U_\phi=G(\phi)U_0,
\qquad
G_{xx}(\phi)=e^{ix\phi/4},
$$

is stationary across the 17-point grid. It remains strict at $\pi/16$ and
$\pi/8$, then first fails the grid at $\pi/2$ with minimum Hessian
$-0.010441$. Thus the small-twist gate passes while the complete
periodic-to-antiperiodic gate fails.

The prospectively selected comparison replaces the axial contact by the
spinor-blind onsite density interaction
$Q_{\mathrm{dens}}=\sum_xN_x(N_x-1)$ and changes nothing else in the gate. The
control is reconstructed exactly on every $N=8$ occupation mask. After
fixed-sector centering, its cosine with the axial contact is 0.2119995760 and it
retains relative residual 0.9772697579 after the best axial rescaling, so it is
not an affine copy under the selector.

At its equal-endpoint coupling $g_0=1.2984286349$, the density control passes the
same periodic, $\pi/16$, and $\pi/8$ tests. It remains strict at $\pi/2$ and
first loses positive curvature at $9\pi/16$. For both interactions the audited
residuals satisfy

$$
R_{\mathrm{site}}=(A,0,0),
\qquad
R_{\mathrm{branch}}=
\left(A\sin^2\frac{\phi}{4},B,0\right),
\qquad
g_0^2B=A,
$$

to errors below $7.0\times10^{-10}$. The corresponding retuned equal-cost root
is $g_*(\phi)=g_0\cos(\phi/4)$ for both contacts. Finite seeded searches at the
first two nonzero twists find no lower candidate but do not prove global
minimality.

The remaining onsite question admits a bounded analytic closure. Write the most
general translation-invariant, number-preserving onsite quartic contact as
$Q_q=\sum_x Q_x(q)$, with
$q=q^\dagger\in\operatorname{Herm}(\Lambda^2\mathbb C^4)$. This is a
36-real-dimensional space. If $(\beta,\chi)$ parameterizes the periodic kinetic
zero-mode basis and $x=\sin^2\beta\cos^2\chi$, exact fixed-sector contractions
give

$$
B_q(\beta,\chi)=B_q(0,0)-p(q)x-r(q)x^2.
$$

Under
$\operatorname{Herm}(\Lambda^2\mathbb C^4)=\mathbf1\oplus\mathbf{15}\oplus\mathbf{20}$,
the spectra of $p$ are $231/4$, $231/2$, and $231$, while those of $r$ are
$693/4$, $539/4$, and $231/2$ on the respective summands. Both forms are
positive definite. Every nonzero contact therefore makes the declared periodic
resolver choose $x=1$, including $\beta=\pi/2$. At that balanced representative,
the symmetric-hopping residual has squared Hilbert-Schmidt norm $A$, and its
residual cross contraction
with every $Q_q$ vanishes. Hence

$$
R_{\mathrm{branch}}(\phi)
=\left(A\sin^2\frac{\phi}{4},B(q),0\right)
$$

for the complete nonzero interaction class just defined. This is a theorem only
inside the fixed four-cell model and resolver; it does not cover disordered or
inter-cell contacts, other fillings or norms, or a continuum limit.

The prospective EC-specificity gate therefore fails. Here "non-axial" means
only that the control is not the axial-current contraction used for the minimal
EC-inspired channel; it does not assert that no generalized torsion effective
theory can contain density-like interactions. The result tests one finite
selector and does not simulate EC field dynamics.

The complete artifacts are the
[boundary-phase report](./research/four-cell-boundary-phase-gate.md),
[matched-control report](./research/four-cell-matched-control-gate.md),
[reproducibility script](./research/ec_four_cell_matched_control.py), and the
separate [mathematical](./feedback/four-cell-matched-control-mathematical-review.md)
and [physics](./feedback/four-cell-matched-control-physics-review.md) reviews.
The full onsite classification is supplied in the
[closure report](./research/four-cell-onsite-closure.md),
[closure script](./research/ec_four_cell_onsite_closure.py), and its separate
[mathematical review](./feedback/four-cell-onsite-closure-mathematical-review.md).

### A.8 Interpretation and stop condition

The two-cell calculation demonstrates only the following finite statement: on a
specified Dirac-algebra-normalizing, number-preserving CAR manifold, an
Einstein-Cartan-inspired Hamiltonian supplies a non-entropic interaction cost
with two strict minima, a finite barrier, and an isolated stationary state with
factorization-dependent mode entanglement. The structure survives one
physically motivated charge-sector weighting. The three-cell result shows that
this statement is not boundary-independent at the first change in lattice size.
The four-cell result supplies a locally robust periodic branch but shows that
its mechanism is reproduced by an independent non-axial onsite control. The
final bounded classification strengthens this from a two-contact observation to
every nonzero interaction in the declared translation-invariant onsite quartic
class.

Two adversarial controls narrow that statement. Direct traces in all fixed
number sectors retain the two-minimum geometry for $2\leq N\leq6$, but the
sector ground state at the equal-endpoint coupling is numerically degenerate for
$N=2,3,5,6$; only $N=4$ passes the isolated-state gate. More importantly, the
non-axial contact $Q_{\mathrm{dens}}=\sum_xN_x(N_x-1)$ produces the same qualitative
selector geometry and a positive stationary contrast. Hence the finite geometry
is generic kinetic-versus-onsite locality competition. The axial-current
channel supplies one realization but no EC-specific explanatory evidence. The
two-cell controls are reproduced by
[the adversarial-control calculation](./research/ec_selector_adversarial_controls.py)
and
[the superselection calculation](./research/ec_superselection_controls.py).
The four-cell matched comparison strengthens this stop condition by applying
the same branch and phase protocol to both interactions. The onsite closure
shows that testing additional contacts from that same finite class cannot
restore specificity.

It does not derive the admissible manifold from continuum field equations,
establish validity at the Planckian coupling where the contact term competes
with the kinetic term, extend the construction to type-III local QFT algebras,
define cosmological observational entropy, produce a Page-Wootters boundary
transition, demonstrate repeatable aeons, or predict a cosmological observable.
It also does not show persistence at arbitrary cell count or that
Einstein-Cartan dynamics selects this factorization family. These are required
before the finite result can support the central ICC proposal.

## Appendix B. Arithmetic Reconstruction and Its Limits

This is a separate bounded test of whether arithmetic dynamics can determine
observable algebras. Multiplication shifts occur in Bost-Connes representations
([Marcolli, 2008](https://www.its.caltech.edu/~matilde/BCF1slides.pdf)). Their
presence in that mathematical framework does not derive them from cosmology.
[Kubota and Takeishi](https://arxiv.org/abs/1709.03281v2) reconstruct semigroup
actions up to conjugacy from algebras already in the number-field Bost-Connes
class; their theorem does not identify that class from an arbitrary Hamiltonian.
The full derivation, controls and applicability review are in the
[v0.1.7 supplement](./research/v017/arithmetic-reconstruction.md). No novelty
or dependence on new OpenAI mathematics manuscripts is claimed.

### B.1 Conditional reconstruction

Assume, rather than derive, the represented ambient algebra
$\mathcal B(\mathcal H)$ and the nondegenerate Hamiltonian

$$
\mathcal H=\ell^2(\mathbb N_{>0}),\qquad
H|n\rangle=(\log n)|n\rangle,\qquad P_n=|n\rangle\langle n|.
$$

The energy zero and units are fixed. If isometries $T_m$, for positive integers
$m$, satisfy

$$
e^{itH}T_m e^{-itH}=m^{it}T_m,\qquad T_mT_n=T_{mn},\qquad T_1=I,
$$

simple spectrum gives $T_m|n\rangle=\alpha_m(n)|mn\rangle$, with
$|\alpha_m(n)|=1$. The semigroup identity acting on $|1\rangle$ implies

$$
\alpha_m(n)=\eta_{mn}\overline{\eta_n},\qquad
T_m=D S_mD^*,\qquad S_m|n\rangle=|mn\rangle,
$$

where $\eta_n=\alpha_n(1)$ and $D|n\rangle=\eta_n|n\rangle$. Thus the
compatible families form one diagonal-unitary orbit, not a uniquely determined
physical embedding. The covariance and semigroup conditions are additional
assumptions, not consequences of the spectrum alone.

A specified normalized reference $|r\rangle=\sum_n c_n|n\rangle$, with every
$c_n\ne0$, fixes one family through the polar decomposition of

$$
B_m=\sum_{n\ge1}P_{mn}|r\rangle\langle r|P_n,\qquad
V_m^{(r)}|n\rangle=
e^{i(\arg c_{mn}-\arg c_n)}|mn\rangle.
$$

The bounded weighted-shift sum converges strongly, and its polar factor is an
isometry even when its weights approach zero. The resulting
$\mathcal A_p^{(r)}=W^*(V_p^{(r)})$ is a diagonal-unitary conjugate of the
prime-occupation factor obtained from $n=p^k q$, $p\nmid q$:
$\mathcal B(\ell^2(\mathbb N_0))\otimes I$. Distinct primes give commuting
factors. These are type-I factors in a specified representation, not spatially
local QFT algebras.

Reference coherence is a physical resource in quantum-information theory
([Bartlett, Rudolph and Spekkens, 2007](https://arxiv.org/abs/quant-ph/0610030)),
but this construction does not explain why ICC supplies this particular
reference or makes the polar operations accessible. In particular,
$(V_m^{(r)})^*H V_m^{(r)}=H+\log m$ on the energy domain requires energy
exchange in an implementation. A general probe need not obey the compatible
phase relations; the supplement supplies a failing control.

### B.2 Stationary-state obstruction

Let $\rho$ be a fixed normal density operator invariant under $e^{-itH}$.
Nondegeneracy makes it diagonal. Every $D$ above preserves $\rho$, so for
each fixed prime $p$ and any two full-support references,

$$
S_\rho(\mathcal A_p^{(r)})=S_\rho(\mathcal A_p^{(s)}).
$$

Here $S_\rho$ is ordinary type-I restricted-state entropy, possibly infinite;
no subtraction of divergent quantities or gravitational interpretation is made.
Also $r(t)=e^{-itH}r$ gives
$V_m^{(r(t))}=m^{-it}V_m^{(r)}$, leaving each algebra unchanged. Thus changing
only these reference phases does not yield a stationary entropy contrast, and
free reference evolution does not generate an algebra transition. This is a
limited statement about the specified model, not about every possible ICC
constraint or every arithmetic algebra.

Accordingly, we discontinue the reference-phase-only route as an ICC transition
mechanism under these assumptions. This closes that proposed use, not the
conditional reconstruction or stability analyses retained here. The broader
selector question remains open. A different candidate would need to identify
and physically justify which assumptions it changes; improved reconstruction
stability alone cannot remove the stationary-state obstruction.

### B.3 Full-norm instability

Take $c_n=\sqrt6/(\pi n)>0$ and $D_j=I-2P_j$ for odd $j\to\infty$.
The reference has finite mean energy, and the trace distance obeys

$$
\tfrac12\bigl\||c\rangle\langle c|
-D_j|c\rangle\langle c|D_j^*\bigr\|_1
=2|c_j|\sqrt{1-|c_j|^2}\longrightarrow0.
$$

Nevertheless, for $\mathcal A_2=W^*(S_2)$ in this fixed ambient representation,

$$
d_{\rm KK}(\mathcal A_2,D_j\mathcal A_2D_j^*)=1.
$$

The distance is the full unit-ball Hausdorff distance in operator norm used in
Section 5.4. Indeed, an element of $\mathcal A_2$ has the same matrix element
from occupation zero to one in every odd-$q$ fiber of $n=2^k q$. The unit-ball
witness $D_jS_2D_j^*$ has that element $-1$ in the $j$-fiber and $+1$ in any
other fiber. Its distance from $\mathcal A_2$ is therefore at least
$\min_z\max\{|z-1|,|z+1|\}=1$, and zero in the unit ball supplies the upper
bound. This is not a failure of the earlier finite entropy bound: its small
algebra-distance premise is absent here.

Energy-restricted or state-weighted criteria require separate analysis. The
following subsection addresses one hard-cutoff comparison, not every such
criterion.

### B.4 Fixed access and conditional stability

Keep the doubling algebra $\mathcal A=\mathcal A_2$ and write
$\mathcal A_c=D_c\mathcal A D_c^*$ for a full-support reference, with
$D_c|n\rangle=c_n|c_n|^{-1}|n\rangle$. Fix a spectral window
$\Pi_N=\sum_{n=1}^N P_n$, independently of reference phases. Define

$$
\begin{aligned}
\mathcal E_N(\mathcal A_c)&=\{\Pi_N a\Pi_N:a\in\mathcal A_c,\ 0\le a\le I\},\\
d_N(\mathcal A_c,\mathcal A_d)&=d_{\rm H}^{\|\cdot\|}
(\mathcal E_N(\mathcal A_c),\mathcal E_N(\mathcal A_d)).
\end{aligned}
$$

The norm is on $\Pi_N\mathcal H$. It measures worst-case probability error
over test states supported there; the Hausdorff comparison concerns ideal
binary-effect approximation, not a channel, instrument, or reconstruction
algorithm. Coherent test-state preparation and a fixed external phase standard
are supplied. Candidate measurements remain exactly the sets $\mathcal E_N$;
external preparation resources do not enlarge them to unrestricted laboratory
measurement sets. No implementation cost or back-action bound is established.

Every compressed effect is within $1/2$ of the common midpoint $\Pi_N/2$,
so $d_N\le1/2$. This differs from the unit-ball normalization in B.3.
If $j>N$, then $\Pi_N D_j=\Pi_N$: the old high-index flip is invisible.
Uniform continuity nevertheless fails for every fixed $N\ge6$. Set

$$
u_3=0,\quad u_n=\sqrt{192/61}\,2^{-n}\ (n\ne3),\qquad
c_\epsilon^\pm=\sqrt{1-\epsilon^2}\,u\pm\epsilon|3\rangle,
\quad 0<\epsilon<1/2.
$$

Since $\sum_{n\ne3}4^{-n}=61/192$, both references are normalized and
full-support. Their trace distance is $2\epsilon\sqrt{1-\epsilon^2}\to0$.
Also $\langle u,Hu\rangle\le\sum_n n|u_n|^2=229/183<2$ and $\log3<2$,
so both satisfy the same mean-energy budget $\langle H\rangle<2$.
This reference budget is separate from the test-state hard cutoff $\log N$.
Their reconstructed algebras are $\mathcal A$ and $D_3\mathcal A D_3$.

To see the exact separation, let $L\in\mathcal A$ swap occupations $k=0,1$
in every odd fiber of $n=2^kq$, fixing higher occupations. Then
$Q=(I+L)/2$ is a projection. The effect $Q'=D_3QD_3$ gives probabilities
1 and 0 on the fixed preparations

$$
\psi_0=(|1\rangle+|2\rangle)/\sqrt2,\qquad
\psi_1=(|3\rangle+|6\rangle)/\sqrt2.
$$

Every effect in $\mathcal A$ has one common expectation $z$ on these
preparations. Hence its error against $Q'$ is at least
$\max\{|1-z|,|z|\}\ge1/2$, proving $d_N=1/2$ for $N\ge6$.
This disproves uniform continuity over the stated reference class, not
continuity at each full-support reference: the limiting $u$ is outside that
domain.

Indeed, for fixed finite $N$, put
$\mu_N(c)=\min_{n\le N}|c_n|>0$ and
$\delta=\min_{|\lambda|=1}\|c-\lambda d\|$. The scalar estimate
$\left|\frac z{|z|}-\frac w{|w|}\right|\le\frac{2|z-w|}{|z|}$
for nonzero $z,w$, and centering effects at $\Pi_N/2$, give

$$
d_N(\mathcal A_c,\mathcal A_d)
\le\min\left\{\frac12,\frac{2\delta}{\mu_N(c)}\right\}.
$$

A common certified amplitude floor gives a uniform bound on that restricted
class; the mean-energy budget alone supplies none. This is a pure-reference
perturbation statement, not a bound for mixed noise, spectral errors, finite
frequency resolution, or a continuum limit. Energy-diagonal test states cannot
detect the phase-conjugation distinction; co-transporting states and apparatus
also preserves probabilities. Neither comparison produces a selector.

The [operational supplement](./research/v017/operational-stability.md) gives
the full proof and controls. The [Lean project](./research/v017/lean/README.md)
checks the infinite-dimensional B.3 witness and vector limit, and B.4's effect
witness, two-probe bound and scalar phase estimate. Reconstruction, reference
sums, trace distance, and the assembled compressed-set and continuity theorems
remain analytic, not end-to-end formalized. B.2 is unchanged: coherent external
probes do not create stationary entropy contrast or free-evolution transitions.
No physical selector, cosmological reset, continuum QFT construction, or
general ICC no-go follows. Reviews remain internal and AI-assisted.

## Appendix C. Finite Reference Resources and Measurement Capability

### C.1 Fixed interaction and declared access

This example asks whether unchanged allowed operations can yield genuinely
different measurement capabilities after a finite reference resource is
redistributed. It uses the established resource perspective on symmetry and
reference frames (Bartlett, Rudolph, and Spekkens, 2007; Marvian and Spekkens,
2012) and finite-reference degradation (Bartlett et al., 2006). These sources
motivate the operational framework, not the particular Hamiltonian or ICC.
The tensor factors, interaction, charge, exposure time and access restrictions
below are supplied apparatus data, not derived cosmological inputs.

Take an input qubit $S$, detector/reference qubit $D$, and charge-neutral
logical memory qubit $M$. With $n=(I-Z)/2$, identity factors suppressed, and
$\hbar=1$, fix

$$
H=\frac12(X_SX_D+Y_SY_D)+n_DX_M,\qquad
Q=n_S+n_D,\qquad T=\frac\pi4,\qquad U_T=e^{-iHT}.
$$

The memory's two logical states carry the same charge and its bare Hamiltonian
is zero in this idealization. It is an ordinary additional degree of freedom,
not a new spatial dimension. Both couplings act simultaneously; their
noncommutativity precludes replacing $U_T$ by two sequential gates. The
interaction conserves $Q$. Initially the retained apparatus $R=DM$ has state
$\tau_0=|+\rangle\langle+|_D\otimes|0\rangle\langle0|_M$.
Unread priming with an invariant old input gives

$$
\tau_1=\Phi(\tau_0),\qquad
\Phi(\tau)=\operatorname{Tr}_{S_{\rm old}}
\left[U_T\left(\frac{I_{S_{\rm old}}}{2}\otimes\tau\right)U_T^\dagger\right].
$$

No intermediate readout, reset or postselection occurs. The old input and any
preparation label or purification of its mixed state are then inaccessible;
the correlated $DM$ state is retained and a fresh independent input is supplied.
This access boundary and input replacement are assumptions, not an autonomous
transport mechanism. Each trial uses one apparatus and one unknown input,
without additional asymmetric references, coherent training probes or
many-copy processing. The original readout is $n_D$ after another exposure to
the same $H$ for the same duration $T$.

For a broader benchmark, allow all joint binary effects obeying
$0\le E\le I$ and $[E,n_S+Q_R]=0$, where $Q_R=n_D\otimes I_M$.
Define the induced system effect and the attainable set by

$$
\operatorname{Tr}[\rho F_\tau(E)]
=\operatorname{Tr}[(\rho\otimes\tau)E],\qquad
\mathcal C_{\rm sym}(\tau)
=\{F_\tau(E):0\le E\le I,\ [E,n_S+Q_R]=0\}.
$$

Exactly the same processing class is used before and after priming. It contains
the original hardware effects but need not be implementable in full by that
hardware. It includes effective POVMs obtained from symmetric operations with
invariant ancillas and invariant readouts. Conservation of $Q$ alone would not
exclude an experimenter supplying a new asymmetric reference; that additional
resource is explicitly excluded here.

### C.2 Exact capability bound and strict inclusion

Use equal-prior test inputs $\rho_\pm=(I\pm Y)/2$, with their phase defined
relative to the initial reference; their preparator is not an accessible extra
resource. Let $\mathcal G$ delete coherences between distinct total-charge
sectors. The Helstrom optimization (Barnett and Croke, 2008) reduces to

$$
p_{\rm sym}^\star(\tau)
=\frac12+\frac14\|\mathcal G(Y\otimes\tau)\|_1
=\frac12+\frac12\|B\|_1,\qquad
\tau=\begin{pmatrix}A&B\\B^\dagger&C\end{pmatrix},
$$

where the entries are $M$ operators in the $D$-charge basis. The only nonzero
twirled block is $\left(\begin{smallmatrix}0&-iB^\dagger\\iB&0\end{smallmatrix}\right)$;
its eigenvalues are the positive and negative singular values of $B$.
The positive spectral effect attains the optimum and is charge invariant.
Equivalently every attainable effect has
$|[F_\tau(E)]_{01}|\le\|B\|_1/2$. This transverse bound does not characterize
the entire effect set, whose bias and longitudinal constraints also matter.

Put $\theta=\pi\sqrt5/8$, $s=\sin\theta$, $c=\cos\theta$, and $u=4s^2/5$.
Direct block evolution of the specified Hamiltonian gives

$$
\|B_0\|_1=\frac12,\qquad
\|B_1\|_1=\frac12\sqrt{1-u},\qquad
p_{\rm sym}^\star(\tau_1)=\frac12+\frac14\sqrt{1-u}.
$$

The original before-priming effect is
$F_0=I/2+(sc/\sqrt5)Y-(u/2)Z$. Its transverse magnitude
$y_0=sc/\sqrt5$ exceeds the after-priming ceiling
$b_1=\sqrt{1-u}/4$. Numerically, $y_0\simeq0.2197744539$ and
$b_1\simeq0.1813596618$. Thus an effect actually implemented before priming
is unavailable afterward even in the larger symmetric benchmark.

| Fixed access and processing class | Before | After |
|---|---:|---:|
| Original $H,n_D,T$ protocol | 0.7197744539 | 0.5341235815 |
| Same $H,n_D$, optimized duration allowed on both sides | 0.7236067977 | 0.6731277438 |
| All charge-symmetric measurements on fresh $S$ and retained $DM$ | 0.7500000000 | 0.6813596618 |
| Old input retained; all charge-symmetric joint measurements | 0.7500000000 | 0.7500000000 |
| Unrestricted direct system measurement, abandoning the charge restriction | 1.0000000000 | 1.0000000000 |

All entries are unconditional equal-prior discrimination success probabilities,
not entropy values. The duration row uses the same timing menu on both sides
with priming fixed at $T$, and does not construct an autonomous clock.
The [derivation](./research/v018/measurement-capability/README.md) gives the
charge-block calculation and analytic duration maxima.

There is also a full-set statement. The reduced channel $\Phi$ is completely
positive, trace preserving and covariant. For any allowed after effect,
$E'=(\mathrm{id}_S\otimes\Phi^*)(E)$ is a valid invariant before effect
with the same Born probabilities on every input. The dual map preserves finite
POVM normalization. This proves inclusion, while $F_0$ proves strictness:

$$
\mathcal C_{\rm sym}(\tau_1)\subsetneq\mathcal C_{\rm sym}(\tau_0),\qquad
\inf_{F\in\mathcal C_{\rm sym}(\tau_1)}\|F_0-F\|_{\rm op}
\ge y_0-b_1\simeq0.0384147921.
$$

The distance expression is a lower bound, not a computed exact nearest-effect
distance. Any unchanged hardware class containing the original protocol and
contained in the symmetric class also has different before/after attainable
sets; nesting of those smaller hardware sets is not asserted. Universal
inclusion follows from the dual-channel argument, not from random sampling.

### C.3 Controls and physical limit

If the old input remains coherently accessible, the apparatus transformation
is unitary on the larger resource. Forward and inverse conjugation give a
bijection of invariant effects, so the full symmetric capability sets are
equal, not just their scores on this task. This comparison assumes arbitrary
symmetric joint control, not availability of the inverse in the smaller
fixed-$H$ hardware menu. If direct asymmetric system measurements are instead
allowed, both discrimination scores are one.

A maximally mixed memory produces the same original detector effects and the
same optimum for this phase task without a locally readable preparation-label
record. That single-score equality does not establish equality of its whole
capability set with the pure-memory case. The model therefore does not show
that record formation drives the change.

Crucially, both reduced capability sets span $M_2(\mathbb C)$: diagonal effects
remain sharp and nonzero charge coherence permits both transverse directions.
Taking the linear span does not grant arbitrary sharp measurements. This is a
quantitative measurement-strength loss within a fixed algebra, not a new
observable algebra, factorization, global information loss, or entropy reset.
The supplied charge, interaction, access boundary and timing remain the missing
physical input in any proposed ICC application. No core postulate or aeonic
interpretation is changed by this example.

### C.4 Verification scope

The [Lean supplement](./research/v018/lean/README.md) checks operator-level
effect preservation by positive unital pullbacks, invariance under a specified
covariant action, capability inclusion conditional on the Born-pairing
identity, finite-POVM normalization, and equality under mutual simulation.
Kraus positivity and normalization are proved for general finite families.
It also certifies the exact scalar strict inequality above: for
$x=\sin^2(\pi\sqrt5/8)$, it proves $1/2\le x\le3/4$ and

$$
\frac{x(1-x)}5-\frac{1-4x/5}{16}\ge\frac1{80}>0.
$$

These are the squares of $y_0$ and $b_1$. The certificate does not rely on
rounded decimal evaluations. However, identifying these scalar quantities
with the concrete Hamiltonian's effects, constructing its tensor-extended
channel, proving its covariance and Born pairing, and deriving the Helstrom
and trace-norm formulas remain analytic, not end-to-end Lean-verified.
The formal mutual-simulation lemma does not itself instantiate the retained
resource unitary. No physical assumption is validated by a proof checker.

The pinned Lean 4.24.0/mathlib project passes its build, a dependency audit of
13 named declarations and two deliberately failing controls. Its checked
declarations use only the standard logical dependencies recorded in the
supplement, with no proof placeholders. Two deterministic NumPy suites
cross-check the model and capability formulas, including arbitrary-input Born
identities, explicit dual-channel simulations and retained-resource controls.
Numerical checks, scoped formal proofs and internal LLM-assisted mathematics
and physics reviews are reported separately; none is independent peer review.

## References

- Ahmad, S. A., Galley, T. D., Hoehn, P. A., Lock, M. P. E., and Smith, A. R. H.
  (2022). [Quantum Relativity of
  Subsystems](https://arxiv.org/abs/2103.01232). *Physical Review Letters* 128, 170401.
- Albrecht, A., and Iglesias, A. (2008). [The clock ambiguity and the emergence
  of physical laws](https://arxiv.org/abs/0708.2743). *Physical Review D* 77, 063506.
- Almheiri, A., Mahajan, R., Maldacena, J., and Zhao, Y. (2020). [The Page curve
  of Hawking radiation from semiclassical
  geometry](https://arxiv.org/abs/1908.10996). *Journal of High Energy Physics* 2020, 149.
- An, D., Meissner, K. A., Nurowski, P., and Penrose, R. (2018). [Apparent
  evidence for Hawking points in the CMB
  Sky](https://arxiv.org/abs/1808.01740). arXiv:1808.01740.
- Andreadakis, F., Dallas, E., and Zanardi, P. (2024). [Long-time Quantum
  Scrambling and Generalized Tensor Product
  Structures](https://arxiv.org/abs/2312.13386). *Physical Review A* 109, 052424.
- Audenaert, K. M. R. (2007). [A sharp continuity estimate for the von Neumann
  entropy](https://doi.org/10.1088/1751-8113/40/28/S18). *Journal of Physics A:
  Mathematical and Theoretical* 40, 8127-8136.
- Barnett, S. M., and Croke, S. (2008). [Quantum state
  discrimination](https://arxiv.org/abs/0810.1970). arXiv:0810.1970, Section 3.1.
- Barnum, H., and Knill, E. (2002). [Reversing quantum dynamics with near-optimal
  quantum and classical fidelity](https://arxiv.org/abs/quant-ph/0004088v2).
  *Journal of Mathematical Physics* 43, 2097-2106. Revised arXiv version, 2026.
- Bartlett, S. D., Rudolph, T., Spekkens, R. W., and Turner, P. S. (2006).
  [Degradation of a quantum reference frame](https://arxiv.org/abs/quant-ph/0602069).
  *New Journal of Physics* 8, 58.
- Bartlett, S. D., Rudolph, T., and Spekkens, R. W. (2007). [Reference frames,
  superselection rules, and quantum information](https://arxiv.org/abs/quant-ph/0610030).
  *Reviews of Modern Physics* 79, 555-609.
- Bodnia, E., Isenbaev, V., Colburn, K., Swearngin, J., and Bouwmeester, D.
  (2022). [The quest for CMB signatures of Conformal Cyclic
  Cosmology](https://arxiv.org/abs/2208.06021). arXiv:2208.06021.
- Buscemi, F., Schindler, J., and Safranek, D. (2023). [Observational entropy,
  coarse quantum states, and Petz recovery: information-theoretic properties
  and bounds](https://arxiv.org/abs/2209.03803). *New Journal of Physics* 25, 053002.
- Carroll, S. M., Diachenko, N., and Dulani, S. (2026). [Toward a
  Phenomenologically Acceptable Quantum Cyclic
  Universe](https://philsci-archive.pitt.edu/29823/). PhilSci-Archive preprint.
- Carroll, S. M., and Singh, A. (2021). [Quantum Mereology: Factorizing Hilbert
  Space into Subsystems with Quasi-Classical
  Dynamics](https://arxiv.org/abs/2005.12938). *Physical Review A* 103, 022213.
- Chandrasekaran, V., Longo, R., Penington, G., and Witten, E. (2023). [An
  Algebra of Observables for de Sitter
  Space](https://arxiv.org/abs/2206.10780). *Journal of High Energy Physics* 2023(02), 082.
- Chen, C.-H., and Penington, G. (2024). [A clock is just a way to tell the time:
  gravitational algebras in cosmological
  spacetimes](https://arxiv.org/abs/2406.02116). arXiv:2406.02116.
- Chitambar, E., Leung, D., Mancinska, L., Ozols, M., and Winter, A. (2014).
  [Everything You Always Wanted to Know About LOCC (But Were Afraid to
  Ask)](https://arxiv.org/abs/1210.4583). *Communications in Mathematical
  Physics* 328, 303-326.
- Clowe, D., Randall, S. W., and Markevitch, M. (2007). [Catching a bullet:
  direct evidence for the existence of dark
  matter](https://arxiv.org/abs/astro-ph/0611496). *Nuclear Physics B -
  Proceedings Supplements* 173, 28-31.
- DESI Collaboration (2025). [DESI DR2 Results II: Measurements of Baryon
  Acoustic Oscillations and Cosmological
  Constraints](https://arxiv.org/abs/2503.14738). *Physical Review D* 112, 083515.
- Diakonov, D., Tumanov, A. G., and Vladimirov, A. A. (2011). [Low-energy
  general relativity with torsion: a systematic derivative
  expansion](https://arxiv.org/abs/1104.2432). *Physical Review D* 84, 124042.
- Hackl, L., and Myers, R. C. (2018). [Circuit complexity for free
  fermions](https://arxiv.org/abs/1803.10638). *Journal of High Energy Physics*
  2018(07), 139.
- Harshman, N. L., and Ranade, K. S. (2011). [Observables can be tailored to
  change the entanglement of any pure state](https://arxiv.org/abs/1102.0955).
  *Physical Review A* 84, 012303.
- Jow, D. L., and Scott, D. (2020). [Re-evaluating evidence for Hawking points in
  the CMB](https://arxiv.org/abs/1909.09672). *Journal of Cosmology and
  Astroparticle Physics* 2020(03), 021.
- Kadison, R. V., and Kastler, D. (1972). [Perturbations of von Neumann
  Algebras. I. Stability of Type](https://doi.org/10.2307/2373592).
  *American Journal of Mathematics* 94, 38-54.
- Khanapurkar, S., Pradhan, A., Dhruv, A., and Singh, T. P. (2018).
  [Non-relativistic limit of Einstein-Cartan-Dirac
  equations](https://arxiv.org/abs/1804.04434). *Physical Review D* 98, 104027.
- Koslowski, T. A. (2007). [A Cosmological Sector in Loop Quantum
  Gravity](https://arxiv.org/abs/0711.1098). arXiv:0711.1098.
- Kubota, Y., and Takeishi, T. (2018). [Reconstructing the Bost-Connes semigroup
  actions from K-theory](https://arxiv.org/abs/1709.03281v2).
  arXiv:1709.03281v2; first submitted 2017.
- Lucat, S., and Prokopec, T. (2017). [Cosmological singularities and bounce in
  Cartan-Einstein theory](https://arxiv.org/abs/1512.06074). *Journal of
  Cosmology and Astroparticle Physics* 2017(10), 047.
- Maldacena, J. M. (1998). [The Large N Limit of Superconformal Field Theories
  and Supergravity](https://arxiv.org/abs/hep-th/9711200). *Advances in
  Theoretical and Mathematical Physics* 2, 231-252.
- Marcolli, M. (2008). [Bost-Connes, F1,
  3-manifolds](https://www.its.caltech.edu/~matilde/BCF1slides.pdf).
  Author-hosted lecture slides, slides 1-2.
- Marletto, C., and Vedral, V. (2017). [Evolution without evolution, and without
  ambiguities](https://arxiv.org/abs/1610.04773). *Physical Review D* 95, 043510.
- Marvian, I., and Spekkens, R. W. (2012). [An information-theoretic account of
  the Wigner-Araki-Yanase theorem](https://arxiv.org/abs/1212.3378).
  arXiv:1212.3378.
- Meissner, K. A., and Penrose, R. (2025). [The Physics of Conformal Cyclic
  Cosmology](https://arxiv.org/abs/2503.24263). arXiv:2503.24263.
- Moreva, E., et al. (2014). [Time from quantum entanglement: an experimental
  illustration](https://arxiv.org/abs/1310.4691). *Physical Review A* 89, 052122.
- Nielsen, M. A. (2006). [A geometric approach to quantum circuit lower
  bounds](https://arxiv.org/abs/quant-ph/0502070). *Quantum Information &
  Computation* 6, 213-262.
- Page, D. N., and Wootters, W. K. (1983). [Evolution without evolution:
  Dynamics described by stationary
  observables](https://doi.org/10.1103/PhysRevD.27.2885). *Physical Review D* 27, 2885-2892.
- Planck Collaboration (2020). [Planck 2018 results. VI. Cosmological
  parameters](https://arxiv.org/abs/1807.06209). *Astronomy & Astrophysics* 641,
  A6.
- Raju, S. (2020). [Lessons from the Information
  Paradox](https://arxiv.org/abs/2012.05770). arXiv:2012.05770.
- Rijavec, S. (2023). [Robustness of the Page-Wootters construction across
  different pictures, states of the universe and system-clock
  interactions](https://arxiv.org/abs/2204.11740). *Physical Review D* 108, 063507.
- Rignon-Bret, A., and Elouard, C. (2026). [Quantum stochastic thermodynamics of
  macroscopic systems: an algebraic approach](https://arxiv.org/abs/2607.09242v1).
  arXiv:2607.09242v1, preprint.
- Ryu, S., and Takayanagi, T. (2006). [Holographic Derivation of Entanglement
  Entropy from AdS/CFT](https://arxiv.org/abs/hep-th/0603001). *Physical Review
  Letters* 96, 181602.
- Safranek, D., Deutsch, J. M., and Aguirre, A. (2019). [Quantum coarse-grained
  entropy and thermalization in closed systems](https://arxiv.org/abs/1803.00665).
  *Physical Review A* 99, 012103.
- Shaari, J. S. (2026). [Informational arrow of time in an extended two-qubit
  Page-Wooters model](https://doi.org/10.1016/j.physleta.2026.131456). *Physics
  Letters A* 577, 131456.
- Shokrian Zini, M., Brown, A. R., and Freedman, M. (2023). [The Smallest
  Interacting Universe](https://arxiv.org/abs/2208.00944). *Journal of High
  Energy Physics* 2023, 82.
- Stoica, O. C. (2026). [The clock ambiguity problem: extended or
  extinguished?](https://arxiv.org/abs/2604.21805). arXiv:2604.21805.
- Styliaris, G., Anand, N., and Zanardi, P. (2021). [Information Scrambling over
  Bipartitions: Equilibration, Entropy Production, and
  Typicality](https://arxiv.org/abs/2007.08570). *Physical Review Letters* 126, 030601.
- Szalay, S., Zimboras, Z., Mate, M., Barcza, G., Schilling, C., and Legeza, O.
  (2021). [Fermionic systems for quantum information
  people](https://arxiv.org/abs/2006.03087). *Journal of Physics A: Mathematical
  and Theoretical* 54, 393001.
- Teixido-Bonfill, A., Schindler, J., and Safranek, D. (2025). [Entropic partial
  orderings of quantum measurements](https://arxiv.org/abs/2310.14086v3).
  *Physica Scripta*. [DOI: 10.1088/1402-4896/ad977c](https://doi.org/10.1088/1402-4896/ad977c).
- Thirring, W., Bertlmann, R. A., Kohler, P., and Narnhofer, H. (2011).
  [Entanglement or separability: The choice of how to factorize the algebra of a
  density matrix](https://arxiv.org/abs/1106.3047). *European Physical Journal
  D* 64, 181-196.
- Van Raamsdonk, M. (2010). [Building up spacetime with quantum
  entanglement](https://arxiv.org/abs/1005.3035). *General Relativity and
  Gravitation* 42, 2323-2329.
- Wiseman, H. M., and Vaccaro, J. A. (2003). [The entanglement of
  indistinguishable particles shared between two
  parties](https://arxiv.org/abs/quant-ph/0210002). *Physical Review Letters*
  91, 097902.
- Witten, E. (2018). [Notes on Some Entanglement Properties of Quantum Field
  Theory](https://arxiv.org/abs/1803.04993). *Reviews of Modern Physics* 90, 045003.
- Zanardi, P. (2001). [Virtual Quantum
  Subsystems](https://arxiv.org/abs/quant-ph/0103030). *Physical Review Letters* 87, 077901.
- Zanardi, P. (2026). [Universal holonomic control of algebras of
  observables](https://arxiv.org/abs/2609.28662v1). arXiv:2609.28662v1, preprint.
- Zanardi, P., Dallas, E., Andreadakis, F., and Lloyd, S. (2024). [Operational
  Quantum Mereology and Minimal Scrambling](https://arxiv.org/abs/2212.14340).
  *Quantum* 8, 1406.

## Conceptual Provenance and AI-Assistance Disclosure

The originating cosmological intuition is the author's. It developed from
questions about Maxwell's demon, statistical entropy, heat death, and whether
the apparent end and beginning of a cosmic cycle must describe different
universes at all. In particular, the author proposed that the universe remains
one and the same global informational reality through the putative cycle, while
the apparent succession of an end and a beginning reflects how that information
is organized or described. The later formulation in terms of local readability
and physically privileged observable algebras was developed with LLM
assistance. The informational interpretation of the dark sector also originated
in the author's brainstorming, but is retained here only as a separate
speculative extension.

Multiple large language models were used extensively during the subsequent
development of the manuscript. Their contributions included criticism and
counterarguments; development and revision of the operator-algebraic notation,
the boundary ansatz, relational-time connections, the finite-dimensional
illustrations, the EC/CAR candidate calculation, the finite-time selector
study, the measurement-entropy and access analyses, and the finite
entropy-stability, transport, conditional arithmetic-reconstruction and
finite-access analyses, and the finite reference-resource and measurement-
capability study; scoped Lean proof development and review;
literature discovery and
comparison; code drafting and review; manuscript organization; English drafting
and rewriting; and preparation of publication metadata. Much of the present
wording, formal presentation, and exploratory code was generated or revised
with LLM assistance.
Some AI outputs made incorrect or overstated claims and were removed or
qualified during revision.

No independent expert validation is claimed. The author directed the revisions,
selected the claims retained in this version, and accepts responsibility for
the final text, citations, errors, and omissions. LLMs are not listed as authors
because they cannot verify the work, consent to publication, or assume
responsibility for it.
