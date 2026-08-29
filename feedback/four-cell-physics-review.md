# Physicist Review of the Four-Cell Finite Selector Gate

Date: 7 August 2026

Status: internal adversarial review, not independent peer review.

Reviewed artifacts:

- [`research/ec_four_cell_selector.py`](../research/ec_four_cell_selector.py)
- [`research/four-cell-finite-gate.md`](../research/four-cell-finite-gate.md)
- [`research/einstein-cartan-circuit-selector.md`](../research/einstein-cartan-circuit-selector.md)

The numerical and algebraic implementation is assessed separately in
[`four-cell-mathematical-review.md`](./four-cell-mathematical-review.md). This
review asks what physical inference, if any, survives after accepting those
calculations as implemented.

## Verdict

The four-cell calculation is physically meaningful as a finite CAR-model
stress test. It does **not** support a positive periodic-only
Einstein-Cartan (EC) selector claim.

The open chain fails the predeclared endpoint gate, while the periodic ring
passes a restricted local and sampled numerical gate. Because the two
geometries differ by an order-one fraction of their links, because the passing
ring uses a naive derivative with an even-lattice doubler, because the coupling
is tuned rather than derived, and because analogous branch competition already
occurs for a non-EC onsite interaction, the passing ring is best classified as
a finite-model observation. It is not evidence that EC dynamics selects an
observable algebra, that the mechanism has a continuum limit, or that it
produces an aeonic transition.

The result is still worth publishing in v0.1.3. It is adverse evidence against
the boundary-independent version of this particular selector and prevents the
positive two-cell example from being overinterpreted. It does not test or
refute the core ICC proposal.

## Findings

### 1. Major: the predeclared physical robustness gate fails

The intended finite claim required the selector to survive both open and
periodic boundary conditions. At four cells, the open site endpoint is a
saddle and the open kinetic endpoint is not stationary. Consequently, no
downstream ground-state, gap, or entropy calculation can repair the tested
boundary-independent mechanism.

The repeated pattern at three and four cells,

$$
\text{open fail},\qquad \text{periodic pass},
$$

is evidence of boundary sensitivity, not convergence with system size. It is
also stronger and more informative than a single failed numerical search: the
failure is local at the proposed open endpoints.

Required claim boundary: this is a failure of one restricted finite selector,
not a no-go theorem for ICC, factorization selection in general, or EC
cosmology.

### 2. Major: the ring is not a small boundary variation at four cells

The open graph has three links and the ring has four. Closing the chain changes
one third of the open-chain bond count and restores exact translation
symmetry. At this size, the difference is an order-one modification of the
Hamiltonian rather than a boundary correction to a common bulk theory.

A periodic-only model is logically possible, but periodic topology and its
fermionic boundary phase would need independent physical motivation. A
one-dimensional four-site ring is not itself a model of three-dimensional
cosmic topology. Observational permission for some compact spatial topology
would not select this graph or this spin structure; Planck found no evidence
for a compact topology with a scale below the diameter of the last-scattering
surface.

### 3. Major: the passing kinetic operator contains the even-lattice doubler

For the periodic central-difference operator,

$$
\lambda_m=2\sin\left(\frac{2\pi m}{L}\right).
$$

At $L=4$ this gives $(-2,0,0,2)$. The $k=\pi$ zero is the additional zero of
the naive lattice derivative, not a second continuum low-momentum mode. The
calculation correctly removes the resulting arbitrary $U(2)$ eigenbasis before
testing the selector, but resolving the numerical basis ambiguity does not
remove the lattice species-doubling problem.

This does not explain the entire open/periodic pattern: the three-cell ring,
which does not sample $k=\pi$, also passed its restricted gate. It does mean
that the four-cell pass cannot be treated as an independent continuum
confirmation of the three-cell result. A Wilson, staggered, overlap, spectral,
or otherwise controlled fermion discretization would define a new physical
model and would need a prospectively stated test.

### 4. Major: the EC connection remains channel-level motivation

Eliminating nondynamical torsion in EC-type theories can generate local
four-fermion interactions, including an axial-axial channel. That justifies the
description **EC-inspired**. It does not derive the following ingredients:

- the one-dimensional nearest-neighbour lattice;
- the restricted $W\otimes I_4$ candidate family;
- the Hilbert-Schmidt projection selector;
- the choice of half filling;
- the equal-endpoint coupling; or
- a dynamical transition between factorizations.

More general torsion-effective actions can contain vector-vector and
axial-vector channels as well. The toy model also retains all three spatial
components of $J_5^\mu J^5_\mu$ while using a kinetic derivative in only one
spatial direction, so it is not a controlled dimensional reduction of the
EC-Dirac field equations.

An exploratory four-cell diagnostic sampled 24 Haar factorizations for each
boundary condition using seed `20260807`. In all 48 cases, the code returned a
zero residual kinetic-contact cross component at its $10^{-8}$ cleanup
threshold. Together with the exact two-cell result, the tested landscape
therefore behaves as

$$
R(W;g)=R_K(W)+g^2R_Q(W)
$$

within the reported numerical precision. The gate supplies no evidence that
the sign of the EC contact or EC-specific kinetic-contact interference matters.
An exact all-$W$ four-cell identity was not proved in this review.

### 5. Major: coexistence is tuned, not predicted

For each geometry, $g_c$ is solved from the condition that the site and kinetic
endpoint costs are equal. The periodic value $g_c=0.4298279139$ is therefore a
coexistence parameter chosen by construction, not a value predicted by EC
gravity or ICC. This is legitimate for asking whether two competing branches
can exist, but it cannot establish naturalness or a physical transition scale.

With the companion note's dimensional estimate

$$
t\sim \ell^{-1},\qquad g\sim\kappa\ell^{-3},\qquad
\frac{g}{t}\sim\frac{\kappa}{\ell^2},
$$

an order-one ratio points to a Planckian cell scale up to convention-dependent
coefficients. That is precisely where the low-energy EC contact truncation and
the four-cell lattice are least controlled. A finite equality at normalized
$t=1$ is not a predicted cosmological density or reset condition.

### 6. Major: the positive periodic result is not interaction-specific

The earlier non-EC onsite density contact produces analogous strict site and
kinetic branches under the same selector construction. Translation-invariant
hopping naturally favors its eigenmode basis, while any onsite contact
naturally favors the site basis. The periodic result is therefore consistent
with generic competition between kinetic and onsite locality.

No four-cell non-EC ensemble was required after the predeclared combined gate
failed. Its absence is methodologically acceptable for a negative report, but
it prevents any positive claim that the surviving ring branch diagnoses
torsion or the axial channel.

### 7. Moderate: the selector norm and state sector are modeling assumptions

The centered fixed-$N=8$ Hilbert-Schmidt norm weights all vectors in the
half-filled sector equally. It is an operator-locality measure, not a vacuum,
ground-state, thermal, path-integral, or cosmological weighting derived from
EC dynamics. A Gibbs-weighted, ground-state-weighted, modular, or other
state-sensitive inner product could change the landscape.

Half filling was fixed before the four-cell calculation, so this is not
post-selection of a successful filling. It nevertheless has no stated
continuum or cosmological interpretation. The three-cell filling controls do
not establish filling independence at four cells.

The admissible $U(4)$ cell transformations are also deliberately restricted:
they preserve fermion number and act trivially on the common internal Dirac
factor. Bogoliubov transformations, gauge constraints, spatially dependent
spin frames, and general AQFT subalgebras are outside the gate. Strict minima
within this quotient are not strict minima in a continuum theory's unknown
admissible space.

### 8. Moderate: the periodic minimum is numerical and finite, not a phase

The full tangent Hessians establish strict local minima within the tested
finite manifold, and the strengthened multistart search found no lower point.
This is good evidence for a finite periodic branch. It is not a proof of the
global minimum, and four sites cannot establish a thermodynamic phase or a
large-$L$ scaling law.

The term "transition" should therefore mean only equality and exchange of
finite selector minima as a parameter is varied. It must not imply a derived
real-time process, quantum phase transition, or aeonic boundary dynamics.

### 9. Major for ICC interpretation: no cosmological bridge has been supplied

The calculation contains no dynamical metric or torsion field, scale factor,
constraint equations, stress-energy backreaction, relational clock,
transition probability, or map between aeonic observable algebras. It does not
calculate thermodynamic, Boltzmann, horizon, or observational entropy.

EC cosmological models can produce nonsingular behavior under additional
matter and state assumptions, but that does not derive this factorization
selector. The finite gate remains a side branch of the ICC research program,
not a validation of its central cosmological mechanism.

## Next decisive periodic-only test

Do not advance directly from this result to a larger periodic lattice. First
test whether the ring minimum survives the arbitrary boundary phase. Replace
the closing link by

$$
K_{L-1,0}=-i e^{i\phi},\qquad
K_{0,L-1}=i e^{-i\phi},
$$

and predeclare a scan including periodic ($\phi=0$), antiperiodic
($\phi=\pi$), and generic twisted values. Keep the interaction, filling,
selector norm, candidate family, stationarity tolerance, and search budget
fixed.

A defensible pass would require either:

1. persistence of the two strict branches over a nonzero interval of $\phi$;
   or
2. an independent derivation selecting $\phi=0$ before inspecting the
   landscape.

If the branch survives only at the exactly periodic, translation-symmetric
point, classify it as a boundary/symmetry artifact and retire the periodic-only
mechanism. If it survives generic twists, the next gate should replace the
naive derivative with a controlled lattice-fermion discretization and repeat
the test with at least one state-weighted norm and a matched non-EC interaction
control.

This sequence is more discriminating than immediately computing five or more
cells with the same assumptions.

## Publication recommendation

Include the four-cell result and both internal reviews in v0.1.3 as an adverse
finite-size update. The defensible summary is:

> At four cells, the restricted EC-inspired selector again fails the
> boundary-independent robustness gate: the open-chain proposed endpoints do
> not both survive, while the periodic ring retains two strict sampled minima.
> The periodic result depends on a tuned coupling, a naive even-lattice
> derivative, a fixed Hilbert-Schmidt norm, and modeling choices not derived
> from EC dynamics; analogous competition is not EC-specific. It is therefore
> a finite periodic observation, not evidence for a continuum, dynamical, or
> cosmological selector.

Do not place the periodic pass among the paper's positive headline results.
Do not describe it as EC confirmation, continuum evidence, or a rescue of the
selector. Retain it because the negative boundary-robustness result is useful
and reproducible.

## Resolution of the proposed boundary-phase test

Completed and mathematically re-audited on 7 August 2026. The prescribed
fixed-coupling scan passes its small-twist three-point gate at
$\phi=0,\pi/16,\pi/8$. The explicitly transported branch has analytic retuned
coexistence roots at the two nonzero points, which survive the stated finite
search. It acquires negative curvature at $\phi=\pi/2$, so the complete
periodic-to-antiperiodic gate fails. The earlier optimizer-based scan had
silently switched branches at that point; the corrected result no longer uses
optimizer basin selection to define continuation.

This narrows Finding 3: the periodic pass is not solely an artifact of the
exact four-cell zero-eigenspace basis freedom. It does not remove the naive
derivative's continuum doubling problem or alter the EC/cosmology claim
boundary above.

Full calculation and reviews:

- [`four-cell-boundary-phase-gate.md`](../research/four-cell-boundary-phase-gate.md)
- [`ec_four_cell_boundary_phase.py`](../research/ec_four_cell_boundary_phase.py)
- [`four-cell-boundary-phase-mathematical-review.md`](./four-cell-boundary-phase-mathematical-review.md)
- [`four-cell-boundary-phase-physics-review.md`](./four-cell-boundary-phase-physics-review.md)

## Physical references used for scope

- D. Diakonov, A. G. Tumanov, and A. A. Vladimirov, [Low-energy general
  relativity with torsion: a systematic derivative
  expansion](https://arxiv.org/abs/1104.2432), *Physical Review D* 84,
  124042 (2011). Supports torsion-induced local four-fermion channels, not the
  selector or its finite lattice realization.
- H. B. Nielsen and M. Ninomiya, [A no-go theorem for regularizing chiral
  fermions](https://doi.org/10.1016/0370-2693(81)91026-1), *Physics Letters B*
  105, 219-223 (1981). General lattice-fermion context; the four-cell doubled
  zero follows directly from the spectrum of the operator used here.
- P. A. R. Ade et al. (Planck Collaboration), [Planck 2015 results. XVIII.
  Background geometry and
  topology](https://arxiv.org/abs/1502.01593), *Astronomy & Astrophysics* 594,
  A18 (2016). Constrains compact cosmic topology but does not motivate the
  finite ring or select its fermionic boundary condition.
- F. Lucat and T. Prokopec,
  [Cosmological singularities and bounce in Cartan-Einstein
  theory](https://arxiv.org/abs/1512.06074), derives torsion-induced
  four-fermion effects in a specified microscopic cosmological model rather
  than an algebra selector. It illustrates the additional dynamical input that
  the finite gate does not provide.
