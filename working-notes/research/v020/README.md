# v0.2.0 Reproducibility Supplement

19 October 2026. Conditional outcome-bearing ticks, not a microscopic
instrument derivation or an ICC algebra selector.

## Result and Boundary

[Appendix D of the manuscript](../../PAPER.md#appendix-d-conditional-outcome-bearing-ticks)
specifies a massive scalar field, a pure-dephasing detector and a fixed
effective clock/register law. Under its tetrahedral Luders instrument,
the two retained-record marginals have distinct operator systems. They are
compatible readouts of one archive; no difference of generated von Neumann
algebras, information erasure or cosmological transition is established.

An alternative instrument has the same first-outcome effects but resets the
detector, making the second field marginal scalar. Microscopic agreement must
therefore include the outcome-labelled state update, not only POVM effects
or an unlabelled master equation.

## Evidence Levels

- **Analytic:** the continuum Weyl-integral independence argument, finite-energy
  witness existence, complete record instrument and its marginal formulas are
  given in Appendix D. They are not machine-verified continuum theorems.
- **Numerical:** [jump-time quadrature](check.py) and a
  [record-block master-equation calculation](audit-check.py) check the same
  finite three-level field surrogate by different methods. They are not
  independent implementations of continuum QFT. The latter imports constants
  and a reference calculation from the former.
- **Formal:** [Lean coverage](lean/README.md) includes concrete qubit identities,
  the same-POVM counterexample and a conditional span-intersection lemma.
  All 32 declarations, including helpers, were checked. The full field-clock
  experiment and the continuum independence premise are not formalized.
- **Physical:** phase, energy, reservoir, preparation and memory resources
  remain open. No material realization is established by the calculations.

The two diagnostic source files and Lean proof source are copied unchanged
from the 19 October working study. The Lean record's source hashes therefore
remain valid. Neither numerical agreement nor separately prompted AI review
is external expert certification. No novel mathematical principle is claimed.

Separate PDF reviews are recorded for
[mathematics](../../feedback/v0.2.0-pdf-mathematical-review.md) and
[physics](../../feedback/v0.2.0-pdf-physics-review.md). They identify the reviewed
PDF by hash; the physics report also gives a small-perturbation counterexample
explaining why an approximation needs an operational acceptance criterion.

## Run the Diagnostics

With Python 3.10+ and NumPy, from the repository root:

```bash
python3 research/v020/run_checks.py --timeout 120
```

The runner enforces one shared deadline and launches both child processes
with assertions enabled, even if its parent Python was invoked with `-O`.
Do not run the diagnostic files directly with optimization: their original
gates use assertions. Fresh output goes to ignored `verification-output/`.
The [bundled numerical record](checks-results.json) includes source hashes.

The recorded generator/quadrature difference is about `6.1e-16`; the
finite-witness equality residuals are below `1.3e-13`. The exponential-series
tail bound is exact-arithmetic only and excludes floating-point roundoff.
The witness's small example-specific signal is not a uniform efficiency bound.
The coherent-apparatus control illustrates why stationarity matters to the
restricted conservation argument; it is not a tetrahedral-instrument realization.

For Lean, use the pinned project and commands in its README. The original
complete recheck took 41.805 seconds with cached dependencies; proof development
finished within the requested two-hour cap. A cold installation is not covered
by that timing, and no dependency cache belongs in a public release.

## Next Research Gate

Derive or approximate the labelled instrument from an independently motivated,
resource-accounted fixed microscopic law, with explicit errors and applicability
conditions. Specify the allowed error class and an operational success margin,
for example separation from classical postprocessing on stated finite-energy
preparations. Small effect errors alone do not guarantee preservation of the
exact scalar-only operator-system intersection. Do not infer new generated
algebras from the marginal operator systems, or use this result to resume the
closed EC/CAR or reference-phase-only
selector routes. Core ICC postulates and earlier negative results are unchanged.
