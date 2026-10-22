# Physics Review of the Four-Cell Boundary-Phase Gate

Date: 7 August 2026

Status: internal adversarial review, not independent peer review.

Reviewed artifacts:

- [`research/four-cell-boundary-phase-gate.md`](../research/four-cell-boundary-phase-gate.md)
- [`research/ec_four_cell_boundary_phase.py`](../research/ec_four_cell_boundary_phase.py)
- [`four-cell-boundary-phase-mathematical-review.md`](./four-cell-boundary-phase-mathematical-review.md)

## Verdict

The phase scan strengthens one narrow finite-model statement: the periodic
four-cell minimum is not created solely by the arbitrary basis freedom of its
exact two-dimensional zero eigenspace. The two-minimum structure survives when
a small twist splits that zero.

It does not cure lattice fermion doubling, establish robustness across spin
structures, add Einstein-Cartan specificity, or provide continuum evidence.
The EC/CAR construction remains an exploratory side branch rather than the ICC
dynamical selector.

## Findings

### 1. The exact-degeneracy objection is weakened, not removed wholesale

At $\phi=\pi/16$, the periodic zero pair has split to approximately
$\pm0.0981$, yet the site branch and the explicitly gauge-transported periodic
branch remain strict at fixed $g_0$. Retuning the coupling slightly also
restores equal costs. Therefore the positive
$\phi=0$ result is not solely a consequence of choosing a favorable basis in
an exactly degenerate zero subspace.

This is the main positive information supplied by the follow-up.

It should not be overstated. Once the resolved periodic point is a strict
nondegenerate minimum of a smooth finite objective, sufficiently small
perturbations are expected to preserve a nearby minimum. The scan estimates a
finite range and locates a later failure; it does not reveal a new physical
stabilization mechanism.

### 2. A boundary twist is a robustness probe, not automatically a spin structure

Periodic and antiperiodic fermionic boundary conditions represent the two spin
structures on a spatial circle. A generic continuous phase additionally
resembles a $U(1)$ holonomy or flux. The present Hamiltonian does not contain a
dynamical gauge field that derives such a holonomy. The continuous scan is
therefore best understood as a controlled perturbation test of the finite
ring, not as a model of cosmological topology.

### 3. Twisting does not solve the continuum doubler problem

A finite twist moves the allowed momenta and removes the exact $k=0$ and
$k=\pi$ zeros at generic $\phi$. It does not change the sine dispersion of the
naive central derivative or remove its extra continuum species as the lattice
is enlarged. The Nielsen-Ninomiya concern raised in the four-cell physics
review therefore remains.

The result rules against the narrow **exact-zero-basis artifact** explanation;
it does not validate the discretization.

### 4. The small-twist grid passes but the full path fails

The three prescribed points $0$, $\pi/16$, and $\pi/8$ pass, while the full
periodic-to-antiperiodic grid fails when the transported stationary branch
develops negative curvature at $\phi=\pi/2$. The earlier implementation's
apparent strict antiperiodic representative belonged to a different branch and
is not evidence of recovery.

This is stronger than an exactly periodic-only observation and weaker than
boundary-condition-independent behavior. The three-point gate is not a
certified statement about every continuous phase between its samples.

### 5. The coexistence line remains tuned

The conditional roots obey the finite-model identity
$g_*(\phi)=g_0\cos(\phi/4)$ and shift from $g_0=0.4298279139$ to 0.4293101673
and 0.4277581750. This removes an optimizer-tracking ambiguity, but every value
still comes from enforcing equal selector cost. No EC field equation predicts
this curve or identifies $\phi$ as a cosmological control variable.

### 6. No EC-specific evidence has been added

The interaction remains one axial-axial contact channel motivated by
integrating out nondynamical torsion. The twist scan does not compare the axial
contact against a matched non-EC onsite control. Since the earlier density
contact produced analogous competing branches, robustness under $\phi$ cannot
be attributed specifically to torsion without that comparison.

The sign-blind, approximately additive kinetic/contact selector structure also
remains unchanged.

### 7. No thermodynamic or cosmological statement follows

The calculation concerns local minima of an operator-locality functional in a
four-cell half-filled CAR model. Boundary-phase robustness is not robustness of
heat-death entropy, an aeonic transition, a cosmological bounce, or relational
time. There is still no metric dynamics, backreaction, continuum local algebra,
or physical factorization-selection law.

## Publication wording

The defensible addition is:

> A prescribed four-cell boundary-phase scan shows that the site branch and an
> explicitly gauge-transported periodic branch remain strict at fixed coupling
> at the first two nonzero grid points. Their residual polynomial gives nearby
> retuned coexistence roots, which survive a finite seeded search. The
> transported branch loses positive curvature at $\phi=\pi/2$, so full
> periodic-to-antiperiodic robustness is absent. This disfavors an explanation
> based solely on the exact periodic zero-eigenspace ambiguity but does not cure
> fermion doubling or establish an EC-specific, continuum, or cosmological
> selector.

Do not describe the result as confirmation of periodic cosmology, removal of
the doubler, or restoration of the failed boundary-independent selector.

## Next physical gate

If the finite side branch is pursued, the next informative calculation is a
prospectively specified controlled lattice-fermion discretization, with the
same axial interaction and a matched non-EC onsite control. Boundary twists
should then be applied to both models under the same selector norm.

That test asks whether local phase robustness belongs to the EC channel or to
generic kinetic-versus-onsite locality competition. Increasing the number of
cells while retaining the same naive derivative would add cost without
answering this objection.

## Physical references used for scope

- H. B. Nielsen and M. Ninomiya, [A no-go theorem for regularizing chiral
  fermions](https://doi.org/10.1016/0370-2693(81)91026-1), *Physics Letters B*
  105, 219-223 (1981). General species-doubling context; the finite spectra in
  this test are computed directly.
- C. T. Sachrajda and G. Villadoro, [Twisted Boundary Conditions in Lattice
  Simulations](https://arxiv.org/abs/hep-lat/0411033), *Physics Letters B* 609,
  73-85 (2005). Supports interpreting continuous twists as momentum-shifting
  finite-volume boundary conditions, not as a cure for the lattice action.
- T. Misumi and T. Kanazawa, [Adjoint QCD on $\mathbb R^3\times S^1$ with
  twisted fermionic boundary
  conditions](https://arxiv.org/abs/1405.3113), *Journal of High Energy
  Physics* 06, 181 (2014). Illustrates that a generic fermionic twist is a
  physical control parameter only inside a specified compactified field
  theory; no such derivation is supplied by the finite selector.
