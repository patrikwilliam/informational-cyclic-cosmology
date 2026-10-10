# Kadison-Kastler Stability and Finite Restricted Entropy

Date: 9 October 2026.

Release supplement: v0.1.6. Section 5.4 of the [manuscript](../../PAPER.md)
summarizes the finite argument; this note retains its full scope and provenance.

Status: bounded internal AI-assisted analysis, not independent expert peer
review. The finite argument below is explicit; numerical checks are diagnostics,
not its proof. No novelty is claimed.

## Verdict

The useful result is a stability bound, not a selection rule. For equal-size
unital matrix factors in the same finite ambient matrix algebra, a small
Kadison-Kastler distance bounds the change of the fixed state's restricted
von Neumann entropy. A direct proof uses trace-preserving conditional
expectations and the established Audenaert continuity inequality. It does
not require the new universal stability theorem in OpenAI family 289.

This strengthens the description of sensitivity to algebra errors. It does
not explain why a physical observer changes algebra, supply ICC's relation
$\mathcal R$, or define cosmological $S_{\rm eff}$.

## Source and Formalization Scope

Catalogue snapshot: OpenAI `math`, revision
`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`, inspected 9 October 2026.

The family-289 manuscript states: for every $\varepsilon>0$ there is a
$\delta(\varepsilon)>0$, uniform over represented unital von Neumann
algebras, such that $d_{\rm KK}(A,B)<\delta(\varepsilon)$ implies
$B=uAu^*$ for a unitary satisfying $\|u-I\|<\varepsilon$.
The distance is the two-sided operator-norm Hausdorff distance between
closed unit balls. It is not agreement on a finite sample of observables.
[Theorem and introduction](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Universal-strong-Kadison-Kastler-stability-September-23-2026/build/sections/01-introduction.tex).

The [Lean scope note](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/289.md)
reports coverage of this uniform statement.
The [comparator configuration](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/ComparatorChallenges/StrongKadisonKastler.json)
targets `OAI.KadisonKastler.universal_strong_stability` in
`OAI.Analysis.KadisonKastler.StrongStability`, with the listed permitted axioms
`propext`, `Quot.sound`, and `Classical.choice`.
The comparator challenge's `sorry` is a target-statement placeholder, not
itself the solution. The solution entry point is a large import aggregator.
Neither its dependency closure nor its proof was compiled or independently
audited here. Thus the status is **reported formalization, not locally
reverified certification**.

The type-I near-unitary-conjugacy result predates this collection:
Christensen, *Perturbations of Type I Von Neumann Algebras* (1975),
[DOI](https://doi.org/10.1112/jlms/s2-9.3.395).
The finite calculation below needs neither its quantitative constants nor
the new theorem's extension to arbitrary types.

## Fixed Domain and Entropy

Let $d\ge2$, $m\ge1$, $\mathcal H=\mathbb C^d\otimes\mathbb C^m$, and
let $A,B\subset\mathcal B(\mathcal H)$ be unital factors of type $M_d$.
Their multiplicity is the same $m$. Choose embeddings

$$
\iota_A(a)=W_A(a\otimes I_m)W_A^*,\qquad
\iota_B(a)=W_B(a\otimes I_m)W_B^*.
$$

For a fixed density matrix $\rho$, with no purity or stationarity assumption,
define

$$
\sigma_A=\operatorname{Tr}_m(W_A^*\rho W_A),\qquad
S_\rho(A)=-\operatorname{Tr}_d(\sigma_A\log_2\sigma_A),
$$

and similarly for $B$. Use the ordinary matrix trace and bits. Any two
identifications of the same factor differ by an inner automorphism, so this
entropy does not depend on a choice of local basis. For mixed global states,
it is restricted-state entropy, not an entanglement measure.

Write

$$
\delta=d_{\rm KK}(A,B)
=\max\left\{\sup_{a\in A_1}\inf_{b\in B_1}\|a-b\|,
\sup_{b\in B_1}\inf_{a\in A_1}\|b-a\|\right\}.
$$

Here $A_1,B_1$ are operator-norm unit balls, and $0\le\delta\le1$.
The finite trace-preserving conditional expectation is

$$
E_A(X)=W_A\left[\frac{\operatorname{Tr}_m(W_A^*XW_A)}{m}
\otimes I_m\right]W_A^*,
$$

and similarly for $E_B$. These maps are completely positive, unital,
trace-preserving, idempotent and operator-norm contractive. They are analytic
comparison tools here, not stipulated physical operations.

## Direct Finite Bound

For $x\ge0$, define the monotone modulus

$$
\omega_d(x)=h_2(t)+t\log_2(d-1),\qquad
t=\min\{x,1-1/d\}.
$$

Here $h_2(t)=-t\log_2t-(1-t)\log_2(1-t)$, with $0\log_2 0=0$.
It increases up to $\log_2d$ and then stays constant. For $d=1$, set
$\omega_1=0$. The cap is necessary: inserting only an upper bound on trace
distance into the uncapped binary-entropy formula is unsafe beyond its
increasing interval.

**Finite-factor conclusion:**

$$
\boxed{|S_\rho(A)-S_\rho(B)|\le\omega_d(\delta).}
$$

### Proof

1. For $a\in A_1$, select $b\in B_1$ with $\|a-b\|\le\delta$.
   Compactness permits this in the present finite domain. Since $E_B(b)=b$,

   $$
   \|a-E_B(a)\|\le\|a-b\|+\|E_B(b-a)\|\le2\delta.
   $$

2. Pull the restricted map back to $M_d$:
   $\Phi=\iota_B^{-1}\circ E_B\circ\iota_A$.
   It is completely positive and unital. It preserves the ordinary local
   trace because both embeddings multiply that trace by the same $m$ and
   $E_B$ preserves the ambient trace. Thus its trace adjoint $\Phi^*$ is
   also completely positive, trace-preserving and unital.

3. Set $\tau_A=\Phi^*(\sigma_B)$. For self-adjoint $a\in M_d$ with
   $\|a\|\le1$,

   $$
   |\operatorname{Tr}_d[(\sigma_A-\tau_A)a]|
   =|\operatorname{Tr}[\rho(\iota_A(a)-E_B(\iota_A(a))) ]|
   \le2\delta.
   $$

   Trace-norm duality gives
   $T(\sigma_A,\tau_A)=\tfrac12\|\sigma_A-\tau_A\|_1\le\delta$.

4. A unital trace-preserving positive map on $M_d$ cannot decrease
   von Neumann entropy. To see this here, diagonalize its input and output.
   The output eigenvalues equal $D\lambda$, where
   $D_{ij}=\langle i|\Phi^*(|j\rangle\langle j|)|i\rangle$.
   Positivity, unitality and trace preservation make $D$ doubly stochastic;
   concavity of $-x\log_2x$ gives $S(\tau_A)\ge S(\sigma_B)$.

5. Audenaert's inequality for $d$-dimensional states with actual trace
   distance $T$ is
   $|S(\sigma)-S(\tau)|\le h_2(T)+T\log_2(d-1)$.
   With the monotone envelope above,

   $$
   S_\rho(B)-S_\rho(A)
   \le S(\tau_A)-S(\sigma_A)\le\omega_d(\delta).
   $$

   Interchanging $A$ and $B$ proves the other direction. See Audenaert,
   *A sharp continuity estimate for the von Neumann entropy* (2007),
   [Theorem 1 of the preprint](https://arxiv.org/pdf/quant-ph/0610146),
   [DOI](https://doi.org/10.1088/1751-8113/40/28/S18).

This establishes the stated finite conclusion without constructing a
near-identity conjugating unitary. No optimality of this composite
algebra-distance bound is claimed.

### Supplied Unitary and Two Endpoint Errors

If $B=uAu^*$ and a particular implementing unitary is known, pull the
state on $B$ back to $A$. Partial-trace contractivity and the triangle
inequality imply

$$
T(\sigma_A,\sigma_B^{\rm pulled})
\le\tfrac12\|\rho-u^*\rho u\|_1\le\|u-I\|=\varepsilon.
$$

Consequently the same entropy gap is at most $\omega_d(\varepsilon)$.
This estimate is representation-dependent but valid for any supplied $u$;
a large local-basis rotation can make it unnecessarily loose.
Also $d_{\rm KK}(A,uAu^*)\le\min\{1,2\varepsilon\}$.
This is an upper bound, not an equality or an invertible estimate.

For a fixed-state contrast $\Delta=S_\rho(A)-S_\rho(B)$ and perturbed
factors $\widetilde A,\widetilde B$ of the same dimension,

$$
|\widetilde\Delta-\Delta|
\le\omega_d(d_{\rm KK}(A,\widetilde A))
+\omega_d(d_{\rm KK}(B,\widetilde B)).
$$

A positive gap exceeding this error budget retains its sign. The required
algebra-error bounds must be independently justified; sampling a few
observables does not certify a Kadison-Kastler distance.

For a qubit factor, $\delta\le0.01$ limits a single entropy change to
$h_2(0.01)\simeq0.080793$ bits. An exact $\log_2d$ contrast requires
$\delta\ge1-1/d$; this is only a necessary condition.

## Mathematical Re-review

- Equal local dimension is essential to the bistochastic-map argument.
  Different factor dimensions or trace calibrations are outside the claim.
- Both directions of the Kadison-Kastler distance are used to obtain an
  absolute entropy difference. A one-sided near inclusion alone does not
  establish this bound in both directions.
- The $1/m$ factor in $E_A$ is necessary. In fact
  $S(E_A(\rho))=S_\rho(A)+\log_2m$, not $S_\rho(A)$.
- The auxiliary channel may increase entropy; the proof does not claim
  coarse-graining creates a low-entropy state. Its two directions compare
  restrictions to two algebras while the original global state stays fixed.
- No purity, nondegenerate eigenstate, Hamiltonian, gap, or physical time
  occurs in the finite proof. These results do not remove or repair the
  selector-specific obstructions already recorded in ICC.
- At $A=B$, the intrinsic entropy difference is zero even if the chosen
  coordinate unitary is far from the identity. Co-transporting state and
  algebra also preserves the restricted entropy exactly.

### Why Fixed Dimension Cannot Be Dropped

There is no dimension-independent entropy modulus of this kind without
additional restrictions. In $\mathbb C^d\otimes\mathbb C^d$, hold
$\rho_d=|00\rangle\langle00|$ fixed within each comparison, set
$A_d=M_d\otimes I_d$, and let

$$
|\chi_d\rangle=\frac1{\sqrt{d-1}}\sum_{j=1}^{d-1}|jj\rangle.
$$

Let $u_d$ rotate the span of $|00\rangle,|\chi_d\rangle$ through
$\theta_d$ and act identically on its orthogonal complement. Take
$B_d=u_d A_d u_d^*$,
$p_d=1/\log_2(d-1)$, and $\theta_d=\arcsin\sqrt{p_d}$ for $d\ge4$.
The sign of the rotated component does not affect the marginal spectrum.
Then

$$
\|u_d-I\|=2\sin(\theta_d/2)\longrightarrow0,\qquad
d_{\rm KK}(A_d,B_d)\le2\|u_d-I\|\longrightarrow0,
$$

but

$$
S_{\rho_d}(A_d)=0,\qquad
S_{\rho_d}(B_d)=h_2(p_d)+p_d\log_2(d-1)=h_2(p_d)+1\longrightarrow1.
$$

This is a sequence of finite-dimensional comparisons, not a construction
of QFT algebras. It shows why the finite estimate cannot simply be made
dimension-free or passed to a continuum limit. Energy or other appropriate
controls would require separate theorems.

## Physics Applicability Review

The bound applies to the reduced-state entropy in the factorization
illustration and the finite transport note. It is **not** a continuity theorem
for the specific POVM observational entropy introduced in v0.1.5. Even on
one unchanged qubit algebra, Z and X measurements of $|0\rangle$ have
different outcome entropies. An algebra does not specify a complete protocol.
Compare the [existing operational definition](../v015/operational-entropy.md).

The result supplies an error-budget condition once a physical algebra,
state and error model have already been identified. It supplies none of those
inputs. A normalizer transformation is a change of local coordinates;
moving the algebra while keeping the state fixed is a different comparison.
The [Zanardi review](./transport-applicability.md)
still lacks an independently motivated path and compatible physical access.

There is no present extension to type-III entropies, type-II gravitational
trace calibrations, horizon contributions, or cosmological dynamics.
Operator-norm control of all bounded observables is also much stronger than
typical finite-resolution experimental access. Small norm distance is
sufficient here, not a claimed necessary condition for every stable entropy
comparison.

## Diagnostics and Disposition

[entropy_stability_checks.py](./entropy_stability_checks.py) uses deterministic NumPy calculations to check the
conditional expectations, bistochastic maps, trace-distance estimates,
entropy inequalities, normalizer and co-transport controls, the monotone
cap, and the explicit dimension-dependent example. Report:
[entropy_stability_checks_results.json](./entropy_stability_checks_results.json).

All seven diagnostic groups passed, including 60 fixed-dimension pure/mixed
comparisons and a 33-point Bell path. The mathematical re-review checked
trace normalization, adjoint orientation, the entropy-monotonicity direction,
the continuity cap and the growing-dimension counterexample. The separate
physics pass retained the protocol, selector and continuum limitations above.
Both review passes were internal, not independent expert validation.

The script uses certified analytic **upper bounds** on Kadison-Kastler
distance from supplied unitaries; it does not numerically compute the exact
unit-ball distance or certify a theorem by sampling. The matrix tests
corroborate the formulas only. No broad optimization or Lean build was run.

The bounded finite stability question is answered within its assumptions.
This release retains the full derivation as a separate robustness note, with
a compact manuscript summary. It does not adopt the universal theorem as an
ICC axiom or restart the closed lattice/selector campaigns. A further application is justified only
when an independently meaningful algebra-error bound or continuum domain
has been specified.
