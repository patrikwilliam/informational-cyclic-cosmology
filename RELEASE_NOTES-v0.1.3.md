# Informational Cyclic Cosmology v0.1.3

Release date: 10 August 2026

## Purpose

Version 0.1.3 records a bounded follow-up to the algebra-selection problem in
v0.1.2. It preserves the preliminary no-go argument for the unrestricted
interaction-projection selector and adds a finite Einstein-Cartan-inspired CAR
calculation on a restricted admissible manifold.

## Main Result

For a two-cell, eight-mode fermionic model, candidate transformations are
restricted to number-preserving CAR transformations that normalize the internal
Dirac matrix algebra. On this manifold:

- the Hamiltonian interaction cost has strict momentum- and site-factorization
  minima separated by a finite barrier;
- an isolated stationary ground state has nonzero factorization-dependent mode
  entanglement at the tested positive-coupling co-global point;
- the branch structure and stationary contrast survive replacement of the
  full-Fock Hilbert-Schmidt trace by the fixed four-particle-sector trace.

The normalized selector consistently removes the scalar Hamiltonian component
in both full-Fock and fixed-sector denominators. This normalization does not
affect the candidate minima, transition couplings, Hamiltonian spectrum, or
entanglement diagnostics.

Adversarial controls further show that local-number and local-parity
superselection reduce but do not eliminate the stationary contrast. A non-axial
onsite density contact reproduces the same qualitative two-minimum geometry,
so that geometry is not claimed as an Einstein-Cartan-specific effect.

This is not a counterexample to the v0.1.2 no-go argument because the latter is
defined on a larger candidate space. The physical derivation of the restricted
manifold remains open.

The first finite-size extension tests three cells in the half-filled $N=6$
sector over the full restricted cell-factorization manifold
$U(3)/(U(1)^3\rtimes S_3)$. It does not pass a boundary-independent robustness
gate. The open-chain kinetic endpoint has a negative Hessian direction and a
lower mixed factorization; the periodic ring retains numerically strict
endpoints and an isolated positive-contrast state. Because the two three-cell
graphs and their discrete-derivative spectra differ at order one, the periodic
branch is recorded only as a restricted numerical observation. No larger-size
conclusion follows from that comparison alone.

The four-cell periodic follow-up has strict site and resolved kinetic endpoints.
An explicitly gauge-transported branch passes the prescribed three-point
small-twist gate and later loses positive curvature at $\phi=\pi/2$. A
prospectively matched, structurally independent onsite density control passes
the same primary gate, obeys the same transported residual law, and remains
strict one grid point farther. The declared EC-specificity gate therefore
fails. The four-cell result is retained as generic kinetic-versus-onsite
locality competition, not support for EC dynamics.

A final analytic closure classifies the complete 36-real-dimensional space of
nonzero Hermitian, translation-invariant, number-preserving onsite quartic
contacts. Every member makes the declared periodic resolver select the balanced
zero modes and obeys
$R_{\mathrm{branch}}(\phi)=(A\sin^2(\phi/4),B(q),0)$. This removes the remaining
possibility that another contact in the same finite class could restore EC
specificity.

## Added Material

- Appendix A in `PAPER.md`, summarizing the finite model and its limitations.
- `feedback/v0.1.3-adversarial-review.md`, the ranked internal kill-test review.
- `feedback/v0.1.3-mathematical-audit.md`, the final math-only review of the
  finite claims and their wording boundaries.
- `research/einstein-cartan-circuit-selector.md`, the companion technical note.
- `research/ec_axial_selector_analysis.py`, the full-Fock calculation and
  operator-convention audits.
- `research/ec_ground_state_certificate.py`, the exact spectral certificate.
- `research/ec_fixed_sector_selector.py`, the fixed-particle-number gate.
- `research/ec_selector_adversarial_controls.py`, the all-sector and non-axial
  null-model controls.
- `research/ec_superselection_controls.py`, the local-number and local-parity
  entanglement controls.
- `research/three-cell-finite-gate.md`, the reviewed finite-size stress-test
  report.
- `research/ec_three_cell_selector.py`, the three-cell calculation, exact
  local-rank certificate, filling Hessians, and non-axial controls.
- `feedback/three-cell-physics-review.md`, the physical interpretation review.
- `feedback/three-cell-mathematical-review.md`, the separate internal algebraic
  and numerical review.
- `research/four-cell-finite-gate.md` and
  `research/ec_four_cell_selector.py`, the four-cell finite feasibility gate.
- `research/four-cell-boundary-phase-gate.md` and
  `research/ec_four_cell_boundary_phase.py`, the corrected explicit-branch
  phase calculation.
- `research/four-cell-matched-control-gate.md` and
  `research/ec_four_cell_matched_control.py`, the prospective axial-versus-
  density specificity test.
- `feedback/four-cell-matched-control-mathematical-review.md`, the separate
  mathematical review of the matched comparison.
- `feedback/four-cell-matched-control-physics-review.md`, the separate physical
  interpretation review.
- `research/four-cell-onsite-closure.md` and
  `research/ec_four_cell_onsite_closure.py`, the bounded analytic classification
  of the full translation-invariant onsite quartic class.
- `feedback/four-cell-onsite-closure-mathematical-review.md`, the separate review
  of that classification.

## Unchanged Scope

Version 0.1.3 does not provide a continuum Einstein-Cartan derivation, a
field-theoretic algebra selector, a Page-Wootters transition, a definition of
cosmological observational entropy, repeatable aeons, or an observational
prediction. The central ICC proposal remains a speculative research program.
The three-cell robustness failure and four-cell specificity failure change no
central ICC postulate; they limit only the exploratory EC/CAR selector branch.
