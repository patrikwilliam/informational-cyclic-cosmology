# Physics Review of the Four-Cell Matched-Control Gate

Date: 9 August 2026

Status: internal adversarial physics review, not independent peer review.

**10 August 2026 addendum:** The original matched comparison could not establish
universality from two contacts. A subsequent bounded mathematical closure proves
that every nonzero contact in the declared Hermitian, translation-invariant,
number-preserving onsite quartic class shares the residual law under the same
periodic resolver. This strengthens the finite kinematic interpretation and
leaves the negative EC-specificity verdict unchanged. It does not extend the
claim to other interactions, selectors, or continuum physics. See the
[closure report](../research/four-cell-onsite-closure.md) and its
[mathematical review](./four-cell-onsite-closure-mathematical-review.md).

Reviewed artifacts:

- [`research/four-cell-matched-control-gate.md`](../research/four-cell-matched-control-gate.md)
- [`research/ec_four_cell_matched_control.py`](../research/ec_four_cell_matched_control.py)
- [`four-cell-matched-control-mathematical-review.md`](./four-cell-matched-control-mathematical-review.md)
- [`research/four-cell-boundary-phase-gate.md`](../research/four-cell-boundary-phase-gate.md)
- [`research/einstein-cartan-circuit-selector.md`](../research/einstein-cartan-circuit-selector.md)

## Verdict

The calculation is physically useful as a negative control on the restricted
finite selector. It does not distinguish the Einstein-Cartan-motivated axial
contact from generic onsite interaction locality. The density control passes
the same periodic and small-twist gates and satisfies the same transported-
branch cost law. The finite branch phenomenon must therefore not be presented
as evidence that EC dynamics selects a factorization.

This result does not refute Einstein-Cartan theory and does not refute the main
ICC hypothesis. It rejects one proposed finite EC-specific signature inside a
highly restricted lattice model.

## Findings

### 1. One independent counterexample is enough for this specificity claim

The primary physical question is not whether the axial contact can produce two
strict finite selector branches. It can. The question is whether that behavior
is characteristic of the axial channel rather than ordinary competition between
a hopping term and an onsite interaction.

The spinor-blind density control is structurally independent of the axial
contact after fixed-sector centering, yet it passes the same primary gate with
larger small-twist curvature margins. This single counterexample is sufficient
to reject the proposed **specificity** inference. It is not sufficient to prove
that every onsite interaction behaves identically, so the narrower phrase
"reproduced by a matched non-axial control" is preferable to a universality
claim.

### 2. "Non-axial" is more accurate than "non-EC"

The control

$$
Q_{\mathrm{dens}}=\sum_xN_x(N_x-1)
$$

is not the normal-ordered axial-current contraction chosen to model the minimal
EC-induced channel. That makes it a valid non-axial control for this paper.

It should not be described as impossible in every theory with torsion. General
torsion effective actions can generate vector-vector, axial-vector, and
axial-axial four-fermion structures after torsion is integrated out; see
[Diakonov, Tumanov, and Vladimirov](https://arxiv.org/abs/1104.2432). The review
therefore uses "non-axial density control" and defines precisely what is being
contrasted.

### 3. The tested Hamiltonian is EC-inspired, not EC dynamics

The calculation contains a one-dimensional four-cell kinetic matrix and a local
four-fermion operator. It does not contain a dynamical tetrad, spin connection,
torsion field, curvature, gravitational constraints, or an EC cosmological
solution. Eliminating nondynamical torsion motivates an axial contact channel,
but that motivation does not derive the selector functional, the admissible
$U(4)/(U(1)^4\rtimes S_4)$ family, or the branch transition.

Moreover, each contact coupling is tuned to equalize two selector costs. In a
physical EC effective theory, the induced coupling is fixed by the gravitational
and fermionic action, subject to convention and possible nonminimal terms. An
equal-selector-cost coupling is therefore a diagnostic construction, not a
prediction of EC theory.

### 4. The common branch law points to kinematics

Both interactions satisfy, to numerical precision,

$$
C_{\mathrm{branch}}(\phi)
=C_{\mathrm{site}}\left(1+\sin^2\frac{\phi}{4}\right),
\qquad
g_*(\phi)=g_0\cos\frac{\phi}{4}.
$$

The natural interpretation is that the law comes from the four-site ring,
onsite gauge invariance, the chosen Hilbert-Schmidt projection, and the explicit
gauge transport of the basis. The axial coefficients change the coupling and
Hessian spectrum, but not the qualitative mechanism.

This is exactly the behavior expected of a useful adverse control: it identifies
which part of the prior positive result was supplied by shared construction
rather than by EC-specific physics.

### 5. Small-twist persistence is not a physical selection mechanism

A strict stationary minimum of a smooth finite objective normally persists
under sufficiently small perturbations. The three prescribed points show that
the numerical continuation remains strict through $\pi/8$ with comfortable
margins. They do not explain why nature would choose that factorization, why an
aeon boundary would implement the transport, or why the selector should govern
relational observables.

The boundary phase is a finite-ring flux/twist parameter. It is not cosmic time,
an aeonic order parameter, torsion, or dark-energy evolution. The loss of
positive Hessian curvature at a later twist is likewise a finite selector
instability, not a cosmological phase transition.

### 6. The lattice remains physically uncontrolled

The kinetic term is a naive finite-difference Dirac construction on four sites.
Such discretizations do not by themselves supply a controlled chiral continuum
fermion theory; the standard doubling obstruction and the need to specify a
continuum prescription remain relevant. A concise modern discussion of the
assumptions behind the doubling problem appears in
[Guo, Ma, and Zhang](https://arxiv.org/abs/2105.10977).

No lattice-spacing sequence, renormalization prescription, continuum scaling of
the contact, or recovery of EC field equations is provided. Four-cell survival
therefore cannot be extrapolated to continuum QFT, and the present negative
specificity result does not require such an extrapolation.

### 7. The landscape diagnostics do not change the physical verdict

At retuned couplings, finite Haar searches and local descents find no lower
factorization than the two audited representatives. Even if future work proved
those representatives globally minimizing in the finite model, the density
control would still exhibit the same coexistence. Global optimization could
strengthen the finite mathematical statement but could not restore EC
specificity.

The one-grid-step difference in loss of branch stability also has no known EC
meaning. The density branch survives farther, so it cannot even be used as a
qualitative robustness advantage for the axial channel.

### 8. Consequence for the ICC research program

The matched-control failure concerns the optional route

$$
\text{finite EC-inspired Hamiltonian}
\longrightarrow
\text{factorization selector}.
$$

It does not address ICC's central unresolved requirements: a physically derived
algebra selector, a defined algebra-relative entropy in QFT/AQFT, a relational
transition law, repeatable aeons, and a cosmological observable. The main paper
should present this result as a reason not to promote the EC side calculation,
not as evidence against global informational or relational-time ideas in
general.

## Defensible Physical Statement

> In the declared four-cell, half-filled CAR selector, the axial-current contact
> and a structurally independent spinor-blind onsite density contact both support
> the same prescribed small-twist pair of strict local minima and the same
> transported-branch cost law. The observed finite branch structure is therefore
> not an EC-specific signature and is best interpreted as kinetic-versus-onsite
> locality competition within this model.

## Not Established

- a discretization or simulation of Einstein-Cartan field dynamics;
- a gravitationally fixed coexistence coupling;
- an EC-derived factorization manifold or selector;
- robustness under a continuum limit or renormalization;
- a physical phase transition associated with the boundary twist;
- a QFT/AQFT algebra transition;
- an entropy reset, repeated aeons, or a cosmological prediction.

## Recommendation

Include the matched-control result because it materially improves the honesty
and diagnostic value of the finite appendix. Treat it as a stop condition for
using this branch geometry as EC-specific support. Do not spend further lattice
sizes on the same specificity claim unless a new selector, admissible family, or
coupling rule is first derived from physical EC structure and fixed before
controls are evaluated.

The generic finite selector geometry may still be studied as mathematics, but
that would be a separate question from whether Einstein-Cartan dynamics supplies
ICC's missing selector.
