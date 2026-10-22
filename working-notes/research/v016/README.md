# v0.1.6 Bounded Stability and Transport Supplement

Release date: 9 October 2026.

Status: internal AI-assisted mathematical and physical applicability checks,
not independent expert review. No novelty, new cosmological axiom or successful
physical selector is claimed.

## Contents

- [Finite restricted-entropy stability](./entropy-stability.md): assumptions,
  conditional-expectation proof, a supplied-unitary estimate, two-endpoint
  error budget and an explicit obstruction to a dimension-free extension.
- [Zanardi transport applicability](./transport-applicability.md): prescribed
  finite-factor paths, a horizontal Bell-state example, co-transport and
  returned-factor controls, and the missing physical-input boundary.
- [Entropy-stability checks](./entropy_stability_checks.py) and
  [recorded diagnostic results](./entropy_stability_checks_results.json).
- [Transport checks](./transport_checks.py).
- [One-command runner](./run_checks.py).

The main text contains a compact stability argument in Section 5.4 and a
conditional transport comparison in Section 6. The two full notes remain
separate so their assumptions are not mistaken for cosmological postulates.

## Reproduction

Requirements: Python 3.10 or later and NumPy. From the repository root:

```bash
python3 research/v016/run_checks.py
```

Run with assertions enabled, without `-O`, `-OO` or `PYTHONOPTIMIZE`. The runner
uses temporary output and leaves the bundled diagnostic record unchanged.
Both scripts can also be run directly. The entropy script accepts an optional
`--json PATH`; the transport script reports its checks on standard output.

The seven entropy-stability diagnostic groups use seed 20261009 and absolute
tolerance 2e-11. They include 60 pure/mixed finite comparisons and a 33-point
Bell path. The six transport groups use absolute tolerance 1e-12 and zero
relative tolerance. These are matrix diagnostics, not substitutes for the
analytic arguments. The exact unit-ball Kadison-Kastler distance is not
computed: the tests use certified analytic upper bounds from supplied
unitaries. The large-dimension sequence uses analytic spectra, not large
dense matrices.

## Source and Scope Boundaries

The finite stability argument uses established conditional expectations and
Audenaert's continuity inequality. It does not depend on the universal
Kadison-Kastler theorem reported in OpenAI catalogue family 289. The full note
preserves the pinned catalogue revision, source links and unverified Lean-build
status that motivated this bounded question.

The entropy is intrinsic restricted von Neumann entropy at fixed finite factor
dimension, not the v0.1.5 general-POVM quantity. No continuum entropy,
gravitational normalization, physical access change, relational dynamics or
selector is derived. The transport generator and stopping point are supplied,
not independently selected. Earlier EC/CAR and finite-time conclusions remain
unchanged; their searches are not restarted.

See the [release verification](../../feedback/v0.1.6-integration-verification.md)
for integration and packaging checks, distinct from mathematical proof.
