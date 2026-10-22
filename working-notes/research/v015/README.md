# ICC v0.1.5: Finite Operational Supplements

These supplements consolidate the completed 29 September to 1 October 2026
finite calculations. They do not introduce a new selector, parameter search,
lattice calculation, or cosmological mechanism.

- [Finite-time analysis](finite-time-analysis.md): the full normal-slice proof,
  exact coefficient certificate, lower-cost competitor, conditional recovery
  comparison, and unresolved physical window and selection assumptions.
- [Operational entropy and access](operational-entropy.md): the fixed POVM,
  analytic entropy formulas, all-input local implementation, and distinction
  between outcome statistics and coherent measurement instruments.

The Bell example is a non-global entangled strict local minimum, not a
preferred structure. The separate entropy example gives a measurement-relative
contrast of 1/3 bit, not a physical reset. Neither is a universal selector
no-go, evidence for ICC cosmology, or a novelty claim.

## Reproduction

Use Python 3.10+ with NumPy installed in that interpreter. No SciPy, optimizer,
network access, external data, or lattice package is required. From the
repository root:

```sh
python3 research/v015/run_checks.py
```

The runner invokes all six scripts sequentially with `sys.executable`,
captures their output, and prints a compact pass summary. It rejects `-O`,
`-OO`, and an active `PYTHONOPTIMIZE` setting because the checks use assertions.
Child processes disable bytecode writing and run in an automatically removed
temporary directory; generated JSON never replaces the bundled records.
On failure it prints the captured diagnostic and exits nonzero.

The certificate is regenerated before the operational selector check.
The runner compares its exact Bell-cost and all six normal-Hessian Fourier
coefficient dictionaries, plus normalization metadata, with the bundled
certificate reference. This explicitly checks the inherited coefficient
dependency; rounded numerical displays are not the certificate.

The individual checks can also be run directly, without modifying records:

```sh
python3 -B research/v015/finite_time_ranking_check.py
python3 -B research/v015/finite_time_second_variation.py
python3 -B research/v015/finite_time_bell_certificate.py
python3 -B research/v015/operational_selector_checks.py
python3 -B research/v015/observational_entropy_checks.py
python3 -B research/v015/measurement_access_checks.py
```

All except the ranking script accept `--output /tmp/chosen-result.json`.
Do not use optimized Python for direct runs either.

## Files and Coverage

| Script stem (add `.py`) | Bounded coverage | Bundled record |
|---|---|---|
| `finite_time_ranking_check` | Two fixed rankings, commutator/realignment identity | stdout only; no historical JSON |
| `finite_time_second_variation` | Six Hamiltonians, six horizons, derivatives and normal slices | `finite_time_second_variation_results.json` |
| `finite_time_bell_certificate` | Exact integer coefficients, rational curvature and competitor bounds | `finite_time_bell_certificate_results.json` |
| `operational_selector_checks` | Channel normalization, timing, recovery identities and scalar bounds | `operational_selector_checks_results.json` |
| `observational_entropy_checks` | 24 noise/sharpness/embedding cases, 168 POVMs and controls | `observational_entropy_checks_results.json` |
| `measurement_access_checks` | Product Kraus effects, 288 spanning-input probability checks, disturbance witness | `measurement_access_checks_results.json` |

The six verification scripts and five JSON records are unchanged copies of
the completed working-note artifacts. Recorded numerical runs report NumPy
2.3.5 where a version field is present. A current runner pass means the
assertions passed in the printed Python/NumPy environment, not that every
floating-point digit or version field matches the historical records.
Quadrature comparisons and finite grids are consistency checks, not rigorous
integration bounds or proofs for all inputs.

Keep the files together: `operational_selector_checks.py` imports
`finite_time_bell_certificate.integrate` and reads the neighboring
`finite_time_bell_certificate_results.json`; `measurement_access_checks.py`
imports constants and entropy helpers from `observational_entropy_checks.py`.
Original working-note filenames in unchanged script docstrings are provenance,
not runtime dependencies. The release supplements above contain the analytical
arguments needed beyond code, without requiring the internal working notes.

## Evidence Boundary

The exact certificate uses integer matrices and rational interval arithmetic;
the quotient argument and all-input measurement proofs are given analytically.
These are internally AI-assisted derivations and checks, not a proof-assistant
formalization, external peer review, experiment, or independent human validation.
Separate derivations and matrix evaluations reduce shared-error risk but do not
remove it; helper imports and inherited coefficients are disclosed above.
The human author remains responsible for the claims and any errors.

The entropy grid does not independently assert every probability or spectrum;
single-axis Petz formulas lack dedicated analytic assertions, completion entropy
is computed as `1 + reduced entropy`, and equal marginals limit A/B-swap
detection. Access numerics test the even-parity disturbance witness; both
branches are covered analytically. Physical measurement access, a justified
clock/window, preference between inequivalent algebras, transition dynamics,
and a thermodynamic interpretation remain additional requirements.
