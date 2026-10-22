# Informational Cyclic Cosmology

Status: speculative hypothesis, not a completed physical theory.

Author: Patrik William Pustejovsky
([ORCID 0009-0008-1618-6619](https://orcid.org/0009-0008-1618-6619)).

DOI (all versions):
[10.5281/zenodo.21115416](https://doi.org/10.5281/zenodo.21115416).

This repository contains version 0.2.0 of a conceptual research note on emergent
time, informational conservation, entropy as local readability, and cyclic
cosmology. It includes a minimal finite-dimensional illustration showing how the
same global pure state can have different bipartite entanglement entropies under
different local observable algebras, plus a restricted Einstein-Cartan-inspired
CAR selector as a separate finite example. Its first three-cell robustness test
is boundary-sensitive. At four cells, the transported residual law is shared by
every nonzero contact in the declared translation-invariant onsite quartic
class, so the periodic branch is not EC specific. Version 0.1.8's finite
reference-resource study changes measurement capability within one algebra.
The current update adds a conditional continuum field-detector study: two
retained-record marginals have different operator systems under a specified
instrument, but different generated algebras are not established. A same-POVM
counterexample and scoped Lean proofs clarify the dependence on the state
update. No microscopic instrument or physical selection mechanism is derived.

Release date: 19 October 2026.

This is version 0.2.0. Its purpose is to be broken.

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

The current version retains the preliminary no-go result for the unrestricted
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

## What Changed in 0.2.0

- Appendix D specifies one massive scalar field, one pure-dephasing detector,
  and a fixed effective tick-and-record law with all 21 archive outcomes retained.
- Under its stated Luders instrument, the two marginal operator systems
  intersect only in scalars. They remain compatible readouts of one archive;
  this is not a result about different generated von Neumann algebras.
- A fixed alternative instrument has the same first-outcome POVM but a
  field-independent second marginal. The state update matters, not only the
  probabilities. The example does not show the Luders model is impossible.
- The [new Lean package](./research/v020/lean/README.md) checks concrete
  detector identities, a same-POVM counterexample and a conditional
  span-intersection lemma. Its 32 declarations include helpers; the continuum
  independence premise and full field-clock dynamics are not Lean-proved.
- The [supplement](./research/v020/README.md) separates analytic arguments,
  two finite diagnostic methods, proof coverage and physical assumptions.
  The next gate is a resource-accounted labelled-instrument derivation.
- Core postulates, older results, license, author ORCID and all-versions DOI
  are unchanged. The version bump marks a new branch, not a solved selector.

See the [release notes](./RELEASE_NOTES-v0.2.0.md) and
[release instructions](./RELEASE_INSTRUCTIONS-v0.2.0.md).

## Historical Changes in 0.1.8

- Appendix C fixes one simultaneous three-qubit interaction and compares the
  same charge-symmetric measurement class before and after unread priming.
  When the old input is inaccessible, the full attainable effect set is
  strictly smaller afterward, not merely worse for one chosen readout.
- The original implemented before score, `0.7197744539`, exceeds the optimum
  over all symmetric after measurements, `0.6813596618`. The broad benchmark
  is not silently identified with the fixed Hamiltonian's hardware controls.
- With the old input retained and arbitrary symmetric joint access, the full
  capability sets are equal. Both reduced sets span the same `M_2` algebra.
  The example does not derive an access boundary, algebra selector, entropy
  reset or aeonic transition; core postulates and interpretation are unchanged.
- The [Lean project](./research/v018/lean/README.md) checks pullback/effect
  lemmas and the exact scalar separation, with a dependency audit and two
  failing controls. The concrete Hamiltonian, channel instantiation and
  Helstrom derivation remain analytic and numerically cross-checked.
- The [v0.1.8 supplement](./research/v018/README.md) provides the derivations,
  two bounded numerical suites, proof scope and separate internal reviews.
  Established reference-resource and discrimination work is cited as prior
  art, not new support for ICC or independent expert endorsement.

See the [release notes](./RELEASE_NOTES-v0.1.8.md) and
[integration verification](./feedback/v0.1.8-integration-verification.md).

## Historical Changes in 0.1.7

- Appendix B tests arithmetic reconstruction with a specified logarithmic
  Hamiltonian and coherent reference. These inputs recover multiplication
  operations but are not derived from ICC.
- Compatible embeddings preserve the restricted entropy of a fixed normal
  stationary state in this model. Free reference evolution leaves the algebras
  unchanged. We therefore close the reference-phase-only route as an ICC
  transition candidate under these assumptions, retaining its reconstruction
  and stability results. The broader selector question remains open; this is
  not a no-go for every selector.
- Arbitrarily small reference errors can give maximal full operator-norm
  algebra distance. The earlier finite entropy-continuity bound is not contradicted.
- Appendix B.4 fixes one finite-access measurement comparison. A hard cutoff
  hides high-energy flips but an energy budget alone still gives no uniform
  stability. At each fixed full-support reference, local stability holds with
  an explicit reference-amplitude conditioning bound.
- The bundled [Lean project](./research/v017/lean/README.md) checks selected
  infinite-dimensional witness and phase-bound components, not the entire
  reconstruction, operational theorem, or ICC hypothesis. The combined numeric
  runner includes 24 diagnostic groups.
- The [v0.1.7 supplement](./research/v017/README.md) includes the derivation,
  reproducible diagnostics, and separate internal mathematical and physical
  reviews. No new OpenAI theorem, Riemann-hypothesis claim, prime-number
  cosmological postulate or independent expert endorsement is introduced.

See the [release notes](./RELEASE_NOTES-v0.1.7.md) and
[integration verification](./feedback/v0.1.7-integration-verification.md).

## Historical Changes in 0.1.6

- A direct finite-dimensional bound controls restricted von Neumann entropy
  under small Kadison-Kastler algebra perturbations at fixed factor dimension.
  It applies to pure or mixed global states, not to unspecified POVMs or
  cosmological entropy. A growing-dimension example explains the limit.
- A bounded review of Zanardi's transport framework shows geometric
  compatibility along a prescribed path, not a physical path-selection rule.
  Co-transporting state and algebra preserves their restricted entropy.
- The manuscript now explicitly separates mass inaccessibility from conformal
  invariance and requires common calibration and horizon accounting for
  cross-algebra gravitational entropy comparisons.
- The [v0.1.6 supplement](./research/v016/README.md) contains the full bounded
  arguments, two scripts with 13 diagnostic groups and a one-command runner.
  The proof does not depend on the new universal stability theorem reported
  in the OpenAI mathematics collection, whose Lean build was not audited here.
- Earlier selector failures, the physical-selection gap, the operational
  measurement boundaries and the closed status of the finite searches remain
  unchanged. No new cosmological postulate or prediction is introduced.

See the [release notes](./RELEASE_NOTES-v0.1.6.md) and
[integration verification](./feedback/v0.1.6-integration-verification.md).

## Historical Changes in 0.1.5

- A bounded finite-time scrambling study supplies an internally certified
  entangled strict local minimum. It is not globally preferred: a product
  competitor has lower cost and better recovery in the specified operational
  task. This is not a counterexample to the interaction-cost-specific argument.
- A separate fixed Bell-state measurement example has observational entropies
  of 2 and 5/3 bits, with explicit white-noise and measurement-sharpness formulas.
  Reduced-state entropy, measurement entropy and cosmological S_eff remain
  distinct; the last is still not supplied.
- The complete new measurement statistics have an exact local implementation
  on both original qubits with classical communication. First-qubit-only
  access cannot implement the informative POVM on arbitrary inputs. Matching
  statistics does not provide coherent control of the new subsystem.
- The abstract, results-and-limits table, conclusions, source attribution and
  AI-assistance disclosure now reflect these distinct studies. No physical
  entropy reset, cosmological selection law or transition is derived.
- The [reproducibility supplement](./research/v015/README.md) supplies the
  derivations, six checked scripts, recorded outputs and one-command runner.
  The finite-example sequence is closed; the earlier EC/CAR results are unchanged.

See the [v0.1.5 release notes](./RELEASE_NOTES-v0.1.5.md).

## Historical Changes in 0.1.4

- Corrected the distinction between one-particle $U(8)$ transformations and
  arbitrary transformations of the 256-dimensional Fock space.
- Qualified the energy-degeneracy discussion: state-changing rotations need
  not be distinct in the full factorization quotient. The nondegenerate
  strict-minimum proposition is unchanged.
- Made the two-cell coexistence window explicit and corrected a squared-norm
  label in the four-cell closure.
- Identified Gaussian minimal scrambling as the same optimization criterion
  on the finite bipartite factor-algebra domain, not a separate escape from the
  tested selector's limitations. No finite-time follow-up result was included
  in v0.1.4.
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
- [Formatted PDF (v0.2.0)](./Informational-Cyclic-Cosmology-v0.2.0.pdf)
- [Release notes for v0.2.0](./RELEASE_NOTES-v0.2.0.md)
- [Release instructions](./RELEASE_INSTRUCTIONS-v0.2.0.md)
- [v0.2.0 reproducibility supplement](./research/v020/README.md)
- [v0.2.0 PDF mathematical review](./feedback/v0.2.0-pdf-mathematical-review.md)
- [v0.2.0 PDF physics review](./feedback/v0.2.0-pdf-physics-review.md)
- [v0.2.0 integration verification](./feedback/v0.2.0-integration-verification.md)
- [Historical release notes for v0.1.8](./RELEASE_NOTES-v0.1.8.md)
- [v0.1.8 reproducibility supplement](./research/v018/README.md)
- [v0.1.8 mathematical review](./feedback/v0.1.8-mathematical-review.md)
- [v0.1.8 physics review](./feedback/v0.1.8-physics-review.md)
- [v0.1.8 integration verification](./feedback/v0.1.8-integration-verification.md)
- [Historical release notes for v0.1.7](./RELEASE_NOTES-v0.1.7.md)
- [v0.1.7 reproducibility supplement](./research/v017/README.md)
- [v0.1.7 mathematical review](./feedback/v0.1.7-mathematical-review.md)
- [v0.1.7 physics review](./feedback/v0.1.7-physics-review.md)
- [v0.1.7 integration verification](./feedback/v0.1.7-integration-verification.md)
- [Historical release notes for v0.1.6](./RELEASE_NOTES-v0.1.6.md)
- [v0.1.6 reproducibility supplement](./research/v016/README.md)
- [v0.1.6 integration verification](./feedback/v0.1.6-integration-verification.md)
- [Historical release notes for v0.1.5](./RELEASE_NOTES-v0.1.5.md)
- [v0.1.5 reproducibility supplement](./research/v015/README.md)
- [v0.1.5 integration verification](./feedback/v0.1.5-integration-verification.md)
- [Historical release notes for v0.1.4](./RELEASE_NOTES-v0.1.4.md)
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

For the v0.2.0 tick diagnostics, with Python 3.10+ and NumPy:

```bash
python3 research/v020/run_checks.py --timeout 120
```

The [v0.2.0 Lean instructions](./research/v020/lean/README.md) give the pinned
toolchain and exact scope. Neither the matrix surrogate nor these selected
proof components certifies the continuum construction or its physical realization.

For the bounded v0.1.8 reference-resource and capability checks, use Python
3.10 or later with NumPy:

```bash
python3 research/v018/run_checks.py --timeout 120
```

The separate [Lean instructions](./research/v018/lean/README.md) document the
pinned toolchain, verification command and partial proof coverage. Numerical
checks do not replace the analytic arguments or establish physical selection.

For the v0.1.7 arithmetic diagnostics, use Python 3.10 or later with NumPy:

```bash
python3 research/v017/run_checks.py
```

These are bounded matrix checks and counterexample witnesses, not validation
of infinite-dimensional theorems or physical access. The analytic arguments
are in the supplement and Appendix B. No older search is restarted.

For the bounded v0.1.6 stability and transport checks, use Python 3.10 or later
with NumPy and run:

```bash
python3 research/v016/run_checks.py
```

The runner checks 13 finite diagnostic groups without changing bundled output.
It does not compute the exact Kadison-Kastler distance, compile Lean, rerun a
selector search, or certify the full source theorems. The analytic arguments
and their assumptions are in the supplement.

For the bounded v0.1.5 additions, use Python 3.10 or later with NumPy and run:

```bash
python3 research/v015/run_checks.py
```

This checks the declared finite examples, not a physical selection mechanism.
The supplement explains the exact-arithmetic certificate, numerical tolerances,
recorded outputs and limits. It does not rerun the older lattice campaign.

The finite calculations introduced in v0.1.3 are unchanged in v0.1.8. They
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
4. whether the finite measurement-relative comparison has any cosmological
   analogue once its assumed access and the absence of transition dynamics
   are made explicit,
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
illustrations, the EC/CAR candidate calculation, the finite-time selector
follow-up, the measurement-entropy and access analyses, and the finite
entropy-stability, transport, and conditional arithmetic-reconstruction
analyses; the finite reference-resource and capability study; the conditional
field-detector and outcome-bearing tick construction, instrument counterexample
and diagnostics; scoped Lean proof development and review; literature discovery and
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
