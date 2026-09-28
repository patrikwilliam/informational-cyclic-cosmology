# Informational Cyclic Cosmology v0.1.4

Release date: 14 September 2026

## Purpose

This is a correction and clarification release following the separate internal
[mathematical](./feedback/v0.1.3-final-mathematical-review-2026-09-10.md) and
[physics](./feedback/v0.1.3-final-physics-review-2026-09-10.md) reviews of v0.1.3.
Those dated reports are retained as historical records, not human peer review.
The [verification note](./feedback/v0.1.4-correction-verification.md) records
the bounded rechecks of the corrections.

## Corrections

1. **Candidate domain (M1).** A number-preserving one-particle $U(8)$ map
   lifts to a proper subgroup of $U(256)$ on Fock space. Dropping the internal
   Dirac normalizer condition does not recover all Fock-space factorizations.
2. **Degenerate energies (M2).** Rotations changing the selected state need
   not change the factorization class under the full quotient. The supporting
   no-go analysis now requires an actual separation argument; its proposition
   for a simple selected energy eigenvalue is unchanged.
3. **Endpoint stability (M3).** The full-Fock two-cell summary specifies the
   simultaneous strict-local-minimum window
   $1/\sqrt{12}<|r|<1/\sqrt6$, with coexistence at $|r|=1/3$.
4. **Residual coefficient (M4).** The four-cell coefficient $A$ is labeled a
   squared Hilbert-Schmidt norm, consistently with its definition and code.
5. **Optional trajectory law (F1).** The companion note's positive functional
   is a trajectory penalty of Euclidean form, not a stable real-time action.
   Its overdamped downhill law requires a separate dissipative assumption.
6. **Density interpretation (F2).** The cutoff estimate $r\sim\kappa/\ell^2$
   implies an increasing-density trend only after identifying physical cells
   and fixing their mean occupation. Regulator refinement alone is not density
   evolution or a relational clock.
7. **Direct prior art (F3).** For the finite bipartite factor algebras, the
   tested cost is proportional to the squared Gaussian scrambling rate of
   Zanardi et al. (2024). The paper and research agenda now state this
   equivalence, including its domain and normalization. No finite-time
   scrambling calculation is claimed or resumed in this release.
8. **Current status (F4).** The open questions and historical three-cell note
   now acknowledge the later four-cell gates and onsite closure. Active
   metadata and the formatted PDF are synchronized to v0.1.4.

## Unchanged Results and Limits

No numerical coefficient, lattice calculation, spectral certificate, or
entropy diagnostic is changed by this release. The three-cell
boundary-independent robustness gate and the four-cell EC-specificity gate
still fail. The finite branch remains generic kinetic-versus-onsite locality
competition in the declared model, not evidence for a cosmological transition.

The central ICC proposal remains a speculative research program without a
derived physical algebra selector, cosmological entropy functional, continuum
limit, repeatable aeonic dynamics, or quantitative observational prediction.
Those questions remain open; this release does not claim to solve them.

Author, ORCID, and the CC BY 4.0 license are unchanged. The manuscript retains
the [all-versions DOI](https://doi.org/10.5281/zenodo.21115416); no unassigned
version-specific DOI is invented. Preparing this package does not publish it
or create a GitHub release or Zenodo record.
