# Citation Audit

Initial audit date: 2026-07-01

Version 0.1.3 update: 2026-07-18

Version 0.1.4 targeted check: 2026-09-14. Equations (14) and (16) of
[Zanardi et al. (2024)](https://arxiv.org/html/2212.14340) were checked against
the Gaussian-rate normalization now displayed alongside $C_H$. On the declared
finite bipartite factor-algebra domain, the squared rate and cost differ by a
positive, candidate-independent multiplier. The updated discussion credits
direct prior art and does not describe this criterion as a new selector. This
targeted check is not a new exhaustive citation audit.

## Version 0.1.5 Targeted Addition

Date: 2026-10-01. This checks the added citations and the existing source reused
for the measurement-entropy definition; it is not a repeat of the full audit.

| Source | Use and limit in v0.1.5 |
|---|---|
| [Styliaris, Anand, and Zanardi (2021)](https://arxiv.org/abs/2007.08570), *Physical Review Letters* 126, 030601 | Channel/operator-entanglement interpretation of bipartite scrambling. This does not identify that quantity with ground-state or cosmological entropy. |
| [Andreadakis, Dallas, and Zanardi (2024)](https://arxiv.org/abs/2312.13386), *Physical Review A* 109, 052424 | Long-time results with spectral assumptions. These are distinguished from the finite-window local-minimum calculation; the latter is not a refutation of the cited result. |
| [Barnum and Knill (2002)](https://arxiv.org/abs/quant-ph/0004088v2), *Journal of Mathematical Physics* 43, 2097-2106 | Recovery bounds under the stated channel/input task. The revised arXiv proof is dated 2026; the journal article remains a 2002 citation. |
| [Chitambar et al. (2014)](https://arxiv.org/abs/1210.4583), *Communications in Mathematical Physics* 328, 303-326 | LOCC resource classes and the statistics/instrument distinction. The concrete protocols and witness are worked out in the supplement. |
| [Buscemi, Schindler, and Safranek (2023)](https://arxiv.org/abs/2209.03803), *New Journal of Physics* 25, 053002 | Existing POVM observational-entropy definition, classical postprocessing and Petz comparison. The fixed-protocol calculation is not a new entropy definition or a cosmological application established by this source. |

Author lists, publication metadata and claim scope were checked against primary
arXiv records and the source-based derivations used for the finite supplements.
No citation is used as evidence for an ICC cosmological transition.

## Version 0.1.5 Pre-publication Source Additions

Date: 2026-10-02. Two scoped additions to the manuscript and references are
included in the final v0.1.5 source, PDF and archive. The version number and
release metadata are unchanged. The earlier document-only snapshot is
superseded by this pre-publication package.
This is a targeted source-use check, not a new exhaustive audit or external
peer review.

| Source | Verified use and boundary |
|---|---|
| [Rignon-Bret and Elouard (2026), v1](https://arxiv.org/abs/2607.09242v1) | Section 2.2, Eqs. (2.19)-(2.22), defines algebra-dependent maximum-entropy completion; Section 5 conditions entropy accounting on specified dynamics and includes nonequilibrium corrections. Cited as a recent preprint and conditional thermodynamic context, not as an ICC selector or a derivation of a cosmological reset. Its algebra-completion entropy is explicitly distinguished from Section 5.2's general-POVM entropy. |
| [Teixido-Bonfill, Schindler, and Safranek (2025), v3](https://arxiv.org/abs/2310.14086v3) | The published-version text establishes inequivalent postprocessing, measured-relative-entropy and observational-entropy orderings for general POVMs. It supports distinguishing Section 5.2's state-specific comparison from universal measurement superiority. No all-ensemble mutual-information theorem, ICC-specific counterexample or cosmological mechanism is attributed to this source. |

The primary arXiv records and relevant full-text statements were checked.
The Rignon-Bret/Elouard record lists v1 only and no journal reference as checked
on this date. The Teixido-Bonfill et al. record labels v3 the published version
and links [the journal DOI](https://doi.org/10.1088/1402-4896/ad977c); the
publisher page was not retrievable in this check. Its arXiv v3 PDF identifies
the authors and March 2025 text. The reference retains the journal DOI without
adding volume or page metadata not verified from the accessible primary record.
The relevant definitions, source locations and claim boundaries are summarized
in the table above; this audit does not require unpublished working notes.
Neither citation is presented as external validation of ICC itself.

Initial PDF-only rebuild check on 2026-10-02: 33 pages, 93 rendered display equations, four tables,
and 197 HTTPS link annotations. The new boundary appears on page 17, the
algebraic-thermodynamics paragraph on page 20, and both reference entries on
page 32. All pages were inspected as contact sheets, with detailed inspection
of the changed pages and page 8's norm symbols. The latter retain the known
extracted-font-metric anomaly but render correctly. MathJax reported no errors
or unresolved placeholders. The root PDF and `output/pdf/` copy match; no ZIP
was rebuilt at that stage and no upload was performed. No mathematical
computation or complete release test suite was rerun for that document-only
update. The subsequent final package checks are recorded in the
[integration verification](./v0.1.5-integration-verification.md).

## Earlier Audits

Initial audit scope: every scholarly source then linked from `PAPER.md`, plus foundational sources
that were missing where the manuscript directly invoked a named framework. Each
source was checked against its abstract or full text and against the exact claim
made in the manuscript.

1. **Zanardi (2001), _Virtual Quantum Subsystems_ - Correct.** Supports the
   claim that operationally relevant observable algebras can select a preferred
   tensor-product subsystem structure.
2. **Harshman and Ranade (2011) - Correct.** Explicitly constructs observables
   that give an arbitrary finite-dimensional pure state a chosen Schmidt
   decomposition.
3. **Thirring et al. (2011) - Correct.** Supports the dependence of entanglement
   versus separability on the chosen factorization of the observable algebra.
4. **Planck Collaboration (2020) - Correct.** Supports both the strong fit of
   six-parameter flat LambdaCDM and the use of precise CMB spectra as a
   constraint on alternatives.
5. **DESI Collaboration DR2 (2025) - Corrected.** The source says BAO alone is
   well described by flat LambdaCDM; the dynamical-dark-energy preference
   arises in combinations with CMB and supernova data. The manuscript now makes
   that distinction.
6. **Meissner and Penrose (2025) - Added and correct.** This is direct support
   for CCC's conformal joining of future infinity to the next aeon's stretched
   Big Bang.
7. **An et al. (2018) - Correct.** Cited specifically as the paper claiming CMB
   Hawking-point evidence.
8. **Jow and Scott (2020) - Correct.** Cited as a reanalysis finding no
   statistically significant Hawking-point evidence.
9. **Bodnia et al. (2022) - Correct.** Cited as a Planck/WMAP search finding no
   statistically significant low-variance circles or Hawking points.
10. **Carroll, Diachenko, and Dulani (2026) - Corrected.** Correctly supports an
    exactly periodic, finite-dimensional unitary model with commensurable energy
    gaps and a distinguished low-entropy excursion. The manuscript no longer
    implies that the paper has already derived its semiclassical spacetime.
11. **Almheiri et al. (2020) - Correct.** Supports Page-curve and island
    calculations in a semiclassical holographic gravity model.
12. **Raju (2020) - Correct.** Appropriately used as a review of information
    preservation proposals and recent Page-curve constructions.
13. **Maldacena (1998) - Correct after qualification.** Supports the AdS/CFT
    gauge/gravity duality, not a general theorem that all geometry emerges from
    information.
14. **Ryu and Takayanagi (2006) - Correct.** Supports the relation between
    boundary entanglement entropy and bulk minimal-surface area in AdS/CFT.
15. **Van Raamsdonk (2010) - Correct.** Supports the argument connecting bulk
    spacetime connectivity with quantum entanglement.
16. **Page and Wootters (1983) - Added and correct.** This is the foundational
    source for describing dynamics by correlations with internal clock readings
    in a globally stationary system.
17. **Moreva et al. (2014) - Correct.** Supports the experimental illustration
    of Page-Wootters conditional dynamics using entangled photons.
18. **Marletto and Vedral (2017) - Correct.** Supports the non-interacting
    clock/rest construction and the authors' claimed resolution of clock
    ambiguity under their assumptions.
19. **Rijavec (2023) - Correct.** Supports the discussion of mixed global states,
    clock interactions, and possible non-unitary conditional dynamics.
20. **Albrecht and Iglesias (2008) - Correct.** Supports the claim that clock
    choice can underdetermine histories and effective laws.
21. **Stoica (2026) - Correct.** Supports the counterclaim that non-interaction
    alone does not remove clock ambiguity and that observables need physical
    meaning.
22. **Shaari (2026) - Correct.** Supports a finite-dimensional informational
    arrow obtained by adding inaccessible auxiliary degrees of freedom and
    effective noise. The manuscript correctly states that this is not a
    cosmological thermodynamic-arrow derivation.
23. **Carroll and Singh (2021) - Correct.** Supports selecting quasi-classical
    factorizations by minimizing entanglement growth and internal spreading.
24. **Zanardi et al. (2024) - Correct.** Supports generalized subsystem
    structures defined by an algebra/commutant pair and selected by minimal
    short-time scrambling.
25. **Shokrian Zini, Brown, and Freedman (2023) - Correct.** Supports a toy
    variational model in which Hamiltonian locality, subsystem factorization,
    and a low-entropy initial state co-emerge.
26. **Safranek, Deutsch, and Aguirre (2019) - Correct.** Supports observational
    entropy as a coarse-grained quantum entropy that can rise toward a
    thermodynamic value in isolated systems.
27. **Buscemi, Schindler, and Safranek (2023) - Correct.** Supports the
    information-theoretic interpretation and bounds for observational entropy
    and coarse-grained states.
28. **Witten (2018) - Correct and moved closer to the claim.** Supports treating
    QFT entanglement algebraically and the type-III obstruction to naive local
    tensor factors and reduced density matrices.
29. **Clowe, Randall, and Markevitch (2007) - Correct.** Supports the separation
    of weak-lensing mass from the dominant baryonic X-ray plasma in the Bullet
    Cluster and the inference of an unseen gravitating component.
30. **Ahmad et al. (2022) - Added and correct.** Demonstrates that different
    quantum-reference-frame perspectives can induce different subsystem
    observable algebras and frame-dependent notions of entanglement and
    subsystem locality.
31. **Koslowski (2007) - Added and correct.** Uses an observable-algebra
    embedding to extract a cosmological sector from full loop quantum gravity.
    It is adjacent prior art for cosmological algebra embeddings, not an aeonic
    transition model.
32. **Chandrasekaran et al. (2023) - Added and correct.** Constructs a
    type-II$_1$ algebra of gravitationally dressed observables for a de Sitter
    static patch and a corresponding entropy.
33. **Chen and Penington (2024) - Added and correct.** Constructs clock-defined
    type-II$_\infty$ gravitational observable algebras in semiclassical
    cosmological backgrounds and relates their entropy to generalized entropy.
34. **Diakonov, Tumanov, and Vladimirov (2011/2012) - Added and correct.**
    Supports the limited statement that integrating out torsion can yield local
    vector-vector, axial-vector, and axial-axial four-fermion interactions. It
    does not derive the finite selector or its candidate manifold.
35. **Khanapurkar et al. (2018) - Added and correct.** Derives a specific
    non-relativistic limit of the Einstein-Cartan-Dirac equations. The
    manuscript now presents it explicitly as a comparison with, rather than an
    assessment of, the finite-mode truncation.
36. **Nielsen (2005/2006) - Added and correct.** Supports geometric approaches
    to quantum-circuit cost through geodesic length. The manuscript explicitly
    does not attribute its candidate selector or circuit action to this work.
37. **Hackl and Myers (2018) - Added and correct.** Develops geodesic circuit
    complexity for fermionic Gaussian states and free fermionic field theories.
    It is contextual support for the finite CAR metric, not a derivation of it.
38. **Szalay et al. (2021) - Added and correct.** Supports the distinction
    between qubit tensor products and fermionic mode subsystems, the role of
    Jordan-Wigner representations, and the necessity of parity superselection
    for a local-operation interpretation.
39. **Wiseman and Vaccaro (2003) - Added and correct.** Supplies the standard
    operational particle-entanglement construction under local particle-number
    restrictions. The manuscript uses its probability-weighted within-sector
    entropy only for fixed-total-number pure states.
40. **Lucat and Prokopec (2017) - Added and correct.** Studies an
    Einstein-Cartan cosmological bounce driven by gravitational-strength
    four-fermion interactions. It is now cited inline only as a bounded bounce
    example, not as a derivation of the selector.

## Corrections Made

- Replaced the unsupported statement that CCC is generally compatible with
  information loss.
- Distinguished DESI BAO-only results from combined CMB and supernova results.
- Qualified the semiclassical status of the 2026 exactly periodic model.
- Narrowed the holography paragraph to what the cited papers actually establish.
- Added the original Page-Wootters paper and a direct modern CCC source.
- Moved Witten next to the type-III claim and Planck next to the CMB constraint.
- Added direct prior art on relational subsystem algebras, cosmological algebra
  embeddings, and type-II gravitational observable algebras.
- Added and bounded the v0.1.3 sources for torsion-induced contact terms,
  circuit geometry, fermionic subsystems, and superselection-resolved
  entanglement.
- Added a complete reference list to `PAPER.md`.
