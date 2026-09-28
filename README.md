# Informational Cyclic Cosmology

Status: speculative hypothesis, not a completed physical theory.

Author: Patrik William Pustejovsky
([ORCID 0009-0008-1618-6619](https://orcid.org/0009-0008-1618-6619)).

DOI (all versions):
[10.5281/zenodo.21115416](https://doi.org/10.5281/zenodo.21115416).

This repository contains version 0.1.4 of a conceptual research note on emergent
time, informational conservation, entropy as local readability, and cyclic
cosmology. It includes a minimal finite-dimensional illustration showing how the
same global pure state can have different bipartite entanglement entropies under
different local observable algebras, plus a restricted Einstein-Cartan-inspired
CAR selector as a separate finite example. Its first three-cell robustness test
is boundary-sensitive. At four cells, the transported residual law is shared by
every nonzero contact in the declared translation-invariant onsite quartic
class, so the periodic branch is not EC specific.

Release date: 14 September 2026.

This is version 0.1.4. Its purpose is to be broken.

The goal is not to defend this formulation, but to expose it to serious
criticism, identify where it fails, and use those failure modes to build a
stronger version.

## TL;DR

The text presents a structured speculative hypothesis in which the universe is
treated as a globally conserved informational structure, and cosmological cycles
correspond to changes in local information readability rather than temporal
restarts. It connects this idea to quantum-gravity-adjacent concepts such as
emergent spacetime, holographic entropy, black-hole unitarity, and
Page-Wootters-style relational time. It treats the thermodynamic arrow as a
separate problem and acknowledges the ambiguity in selecting a clock. Its main
failure points are factorization selection, physical equivalence, and the lack
of an intrinsic algebra-selection rule. It also leaves the repeatability needed
for a genuinely cyclic model as an open requirement. A
finite-dimensional example illustrates the established dependence of
entanglement and reduced-state entropy on subsystem factorization. It does not
derive an aeonic transition, demonstrate a thermodynamic entropy reset, or
identify the correct field-theoretic or gravitational observable algebra.
The proposal is suitable for preliminary academic discussion as a conceptual
physical hypothesis, but not yet as a completed theory.

Version 0.1.4 retains the preliminary no-go result for the unrestricted
Hamiltonian interaction-projection selector and the restricted finite
follow-up introduced in v0.1.3. On the number-preserving CAR manifold that
normalizes the internal Dirac matrix algebra, an Einstein-Cartan-inspired
two-cell Hamiltonian develops two strict competing factorization minima in its
coexistence window and an isolated stationary ground state with nonzero
mode-entanglement contrast. The result survives restriction
to the fixed four-particle sector. It does not contradict the unrestricted
argument, because the latter's descent directions are not all admissible on the
restricted manifold. The physical derivation of that manifold, its continuum
extension, and any cosmological interpretation remain open. A three-cell
extension fails boundary-independent robustness: the open-chain kinetic
endpoint is unstable, while the periodic ring passes only a restricted
numerical gate. The periodic result is not treated as a rescue or as evidence
for EC dynamics. A four-cell periodic follow-up passes a prescribed small-twist
gate but fails the full phase grid. More importantly, a structurally independent
non-axial onsite density control passes the same primary gate and obeys the same
transported-branch cost law. A bounded analytic classification extends that law
to every nonzero Hermitian translation-invariant onsite quartic contact in the
declared four-cell class. This is a stop result for EC specificity, not a
positive extension of the main ICC proposal.

## What Changed in 0.1.4

- Corrected the distinction between one-particle $U(8)$ transformations and
  arbitrary transformations of the 256-dimensional Fock space.
- Qualified the energy-degeneracy discussion: state-changing rotations need
  not be distinct in the full factorization quotient. The nondegenerate
  strict-minimum proposition is unchanged.
- Made the two-cell coexistence window explicit and corrected a squared-norm
  label in the four-cell closure.
- Identified Gaussian minimal scrambling as the same optimization criterion
  on the finite bipartite factor-algebra domain, not a separate escape from the
  tested selector's limitations. No finite-time follow-up result is included.
- Distinguished the companion note's positive trajectory penalty from a
  real-time action and its separately assumed dissipative law. Made the density
  scaling conditional on a physical cell and occupation prescription.
- Updated the supplementary status, PDF, citation metadata, and release
  package. No finite calculation or central cosmological postulate changes.

See the [release notes](./RELEASE_NOTES-v0.1.4.md) and
[correction verification](./feedback/v0.1.4-correction-verification.md).

## Finite Results Added in 0.1.3

- Preserved and clarified the v0.1.2 no-go argument on the unrestricted
  factorization space.
- Added an Einstein-Cartan-inspired two-cell CAR Hamiltonian on a structurally
  restricted candidate manifold.
- Derived closed full-Fock and fixed-$N=4$ selector branch diagrams with two
  strict minima, coexistence windows, and finite barriers.
- Added an exact spectral certificate for the full-Fock critical ground state
  and numerical stationary-state checks at the fixed-sector transition.
- Corrected the selector normalization to remove the scalar Hamiltonian
  component consistently with the v0.1.2 definition; this changes normalized
  cost values but not minima, transition couplings, states, gaps, or entropies.
- Added all-sector, non-axial onsite-contact, and fermionic-superselection controls.
  They show that the entropy contrast survives operational restrictions but the
  two-minimum geometry is not specific to Einstein-Cartan dynamics.
- Added a math-only audit of the projection, quotient argument, normalizer,
  optimizer geometry, spectral certificate, and superselection calculation.
- Added a three-cell finite-size stress test with an exact local-subspace rank
  certificate, full $U(3)/(U(1)^3\rtimes S_3)$ endpoint Hessians, filling
  controls, and separate physics and mathematics reviews. The combined result
  fails boundary-independent robustness.
- Added a four-cell periodic phase gate and a prospectively matched non-axial
  density control. Both contacts pass the same three-point small-twist gate and
  share the same transported residual law, so the EC-specificity gate fails.
- Closed the remaining onsite-contact question analytically. The complete
  36-real-dimensional Hermitian onsite quartic class selects the same balanced
  periodic zero modes and satisfies the same residual law.
- Added a companion technical note and reproducibility scripts while
  keeping the result separate from the central cosmological postulates.

## Claimed Contribution

This project does not claim a new theorem about Hilbert-space factorization,
entanglement relativity, or observational entropy. Its proposed contribution is
a speculative cosmological interpretation: an aeonic boundary may correspond
to a change in the physically privileged local observable algebra of a
stationary global informational state, rather than to a new global state or an
externally timed restart.

The novelty claim is limited to this proposed synthesis and remains subject to
correction if closer prior art is identified.

The physical principle selecting the new algebra is not yet known. Determining
whether this proposal describes a real transition rather than a relabeling of
observables is one of the main open questions. A fixed selector acting on the
same global state, constraint, and relational data would select the same algebra;
the model must therefore derive intrinsic relational data that distinguish the
candidate aeonic regimes without introducing external time.

In the current notation, $\mathcal{R}$ is a placeholder relation between
embedded local observable algebras, and $T_n$ labels one candidate pair in that
relation. Neither is a unitary transformation, a quantum channel, or evolution
in external time. A physical model must supply an intrinsic and non-circular
rule that selects a stable equivalence class of local algebras.

The interaction-projection cost introduced in version 0.1.2 was one attempt to
make this requirement concrete. It appears to fail for isolated stationary
pure states at strict minima on the unrestricted finite factorization space
when the target is bipartite entanglement entropy. Version 0.1.3 shows that the
same form of cost can support strict competing minima and stationary
entanglement on a narrower Dirac-algebra-normalizing CAR manifold. This does
not refute the unrestricted result. The restricted family must be derived from
independent physical structure rather than chosen to remove the no-go
directions. Its first three-cell extension is boundary-sensitive and therefore
does not establish a selector that persists with system size. The four-cell
periodic branch survives small twists, but the same result for a matched
non-axial density control shows that this behavior is generic to the tested
kinetic-versus-onsite construction rather than EC specific. The final onsite
classification strengthens this conclusion from two controls to every nonzero
contact in the declared translation-invariant quartic class.

The superscripts $\infty$ and $0$ are currently mnemonic labels for the proposed
end- and start-boundary regimes. They are not values of external time or
mathematically defined limits. A limit interpretation would require a relational
parameter, topology, and convergence criterion.

## Speculative Cosmological Extensions

The manuscript also explores an informational dark sector, emergent rest-mass
scales, and dark energy as possible boundary data. These extensions are
motivated by the central framework but are not required by it. In particular,
failure of the proposed non-particle dark-matter interpretation would not by
itself falsify the central aeonic boundary proposal.

## Main Document

- [PAPER.md](./PAPER.md)
- [Formatted PDF (v0.1.4)](./Informational-Cyclic-Cosmology-v0.1.4.pdf)
- [Release notes for v0.1.4](./RELEASE_NOTES-v0.1.4.md)
- [Correction verification for v0.1.4](./feedback/v0.1.4-correction-verification.md)
- [Final v0.1.3 mathematical review](./feedback/v0.1.3-final-mathematical-review-2026-09-10.md)
- [Final v0.1.3 physics review](./feedback/v0.1.3-final-physics-review-2026-09-10.md)
- [Historical release notes for v0.1.3](./RELEASE_NOTES-v0.1.3.md)
- [Adversarial review of the v0.1.3 increment](./feedback/v0.1.3-adversarial-review.md)
- [Mathematical audit of the v0.1.3 increment](./feedback/v0.1.3-mathematical-audit.md)
- [EC/CAR companion technical note](./research/einstein-cartan-circuit-selector.md)
- [Full-Fock EC/CAR analysis](./research/ec_axial_selector_analysis.py)
- [Exact critical spectral certificate](./research/ec_ground_state_certificate.py)
- [Fixed-particle-number selector gate](./research/ec_fixed_sector_selector.py)
- [All-sector and non-axial adversarial controls](./research/ec_selector_adversarial_controls.py)
- [Fermionic-superselection controls](./research/ec_superselection_controls.py)
- [Three-cell finite-size report](./research/three-cell-finite-gate.md)
- [Three-cell reproducibility script](./research/ec_three_cell_selector.py)
- [Three-cell physicist review](./feedback/three-cell-physics-review.md)
- [Three-cell mathematical review](./feedback/three-cell-mathematical-review.md)
- [Four-cell finite gate](./research/four-cell-finite-gate.md)
- [Four-cell boundary-phase report](./research/four-cell-boundary-phase-gate.md)
- [Four-cell matched-control report](./research/four-cell-matched-control-gate.md)
- [Four-cell matched-control script](./research/ec_four_cell_matched_control.py)
- [Four-cell matched-control mathematical review](./feedback/four-cell-matched-control-mathematical-review.md)
- [Four-cell matched-control physics review](./feedback/four-cell-matched-control-physics-review.md)
- [Four-cell full onsite-contact closure](./research/four-cell-onsite-closure.md)
- [Four-cell onsite-contact closure script](./research/ec_four_cell_onsite_closure.py)
- [Four-cell onsite-contact mathematical review](./feedback/four-cell-onsite-closure-mathematical-review.md)
- [Main mathematical problem](./feedback/main-mathematical-problem.md)
- [General no-go analysis](./feedback/general-no-go-analysis.md)
- [Preliminary two-qubit analysis](./feedback/two-qubit-preliminary-analysis.md)
- [`2 x 3` numerical checks](./research/two_by_three_selector_analysis.py)
- [Two-qubit reproducibility script](./research/two_qubit_selector_analysis.py)
- [Open questions](./feedback/open-questions.md)
- [Citation audit](./feedback/citation-audit.md)
- [Technical-validity audit](./feedback/technical-validity-audit.md)

## Reproducing the Finite Calculations

The finite calculations introduced in v0.1.3 are unchanged in v0.1.4. They
require Python 3.10 or later and NumPy. From the
repository root, run:

```bash
python3 research/ec_axial_selector_analysis.py
python3 research/ec_ground_state_certificate.py
python3 research/ec_fixed_sector_selector.py
python3 research/ec_selector_adversarial_controls.py
python3 research/ec_superselection_controls.py
python3 research/ec_three_cell_selector.py
python3 research/ec_four_cell_selector.py
python3 research/ec_four_cell_boundary_phase.py --deep-validation --curvature-root --conditional
python3 research/ec_four_cell_matched_control.py --max-index 16 --conditional
python3 research/ec_four_cell_onsite_closure.py
```

The scripts exit with a nonzero status when a stated internal gate fails. The
second supplies the exact rational spectral certificate described in Appendix
A. Scientific gate failures are reported as results while the scripts exit
successfully when implementation and reproducibility audits pass. The four-cell
matched-control command takes several minutes on a recent laptop; the final
onsite closure takes seconds.

## Feedback Wanted

Strong objections are preferred over general encouragement.

I am especially interested in criticism of:

1. the unrestricted arbitrary-dimension no-go argument and whether the
   Dirac-algebra-normalizing CAR restriction is physically defensible rather
   than an imposed removal of its descent directions,
2. the boundary relation, missing replacement algebra-selection rule, and
   missing intrinsic source of relational variation between aeonic regimes,
3. the entropy/readability distinction,
4. the finite-dimensional illustration and whether its refactorization move has
   any physically meaningful cosmological analogue beyond changing bipartite
   entanglement entropy,
5. extension from finite-dimensional Hilbert spaces to the appropriate QFT or
   gravitational observable algebras,
6. the optional informational dark-sector extension, especially its effective
   gravitational source, CMB acoustic peaks, and structure formation,
7. compatibility with black-hole unitarity,
8. the Page-Wootters-inspired treatment of relational time, its clock
   ambiguity, and the separate derivation of a thermodynamic arrow,
9. whether the hypothesis makes any testable prediction distinct from
   LambdaCDM, Penrose CCC, exactly periodic quantum cyclic cosmology, or
   emergent-gravity models,
10. whether an intrinsic rule can generate repeatable aeonic boundaries rather
   than only one selected pair.

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
illustrations, and the EC/CAR candidate calculation; literature discovery and
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

This version is expected to contain weaknesses. The purpose of publishing it
openly is to expose those weaknesses, invite criticism, and build a stronger
version.

## License

This project is released under the Creative Commons Attribution 4.0
International license (CC BY 4.0). You may use, copy, modify, criticize, fork,
or republish it for any purpose, including commercially, provided that you give
appropriate credit, link to the license, and indicate whether changes were
made.
