# v0.1.7 Arithmetic Reconstruction Supplement

Release date: 10 October 2026.

This bounded study records a conditional reconstruction and its limitations,
not a successful physical selector. It does not change ICC's core postulates.
All reviews and checks are internal and AI-assisted, not independent expert
certification. No mathematical novelty is claimed.

## Contents

- [Full derivation and source scope](./arithmetic-reconstruction.md).
- [Finite diagnostic script](./arithmetic_checks.py) and
  [recorded results](./arithmetic_checks_results.json).
- [One-command runner](./run_checks.py).
- [Fixed-access derivation](./operational-stability.md),
  [nine additional diagnostics](./operational_stability_checks.py), and
  [recorded results](./operational_stability_results.json).
- [Scoped Lean proof project](./lean/README.md), including reproducible sources,
  pinned dependencies and a verification record; the toolchain is not bundled.
- [Mathematical review](../../feedback/v0.1.7-mathematical-review.md).
- [Physics review](../../feedback/v0.1.7-physics-review.md).
- [Release verification](../../feedback/v0.1.7-integration-verification.md).

Appendix B of the manuscript contains the compact argument. The supplement
separates the explicit derivations from the known source results and the
unresolved physical assumptions.

## Reproduction and Limits

Use Python 3.10 or later with NumPy, from the repository root:

```bash
python3 research/v017/run_checks.py
```

The runner executes 24 diagnostic groups, leaves bundled records unchanged and rejects optimized Python for
consistency with earlier runners. The checks themselves raise explicit errors.
Seed: 20261010. Default absolute residual tolerance: 1e-10. Finite-window
shifts are checked as partial isometries, not full infinite-space isometries.
The script also tests generic-basis covariance, semigroup identities,
incompatible probes, stationary entropy invariance, reference free evolution,
non-product reference amplitudes, and an instability witness. Extra review
controls check missing transitions, energy-exchange identities on the allowed
finite domain, and the full stationary density-matrix spectrum.

The finite rectangle is supplied as a diagnostic window; it is not a derived
physical factorization. These tests do not prove the infinite statements,
whose explicit arguments are provided separately. They do not implement a
clock, a work source, continuum QFT, or a cosmological transition. No new
OpenAI mathematics theorem or Riemann-hypothesis claim is used.

The independent physical origin of the logarithmic spectrum and reference is
unresolved. Reference-phase changes preserve the target restricted entropy in
the stationary model; free reference evolution leaves the algebra unchanged.
We therefore close the reference-phase-only route as an ICC transition
candidate under these assumptions, while retaining the conditional
reconstruction and stability results. The broader selector question stays
open; any replacement must identify and physically justify changed assumptions.
The full operator-norm instability does not decide every energy-restricted or
state-weighted criterion. The separate hard-cutoff effect-set analysis removes
the old high-index witness but still disproves uniform continuity over the
fixed-energy reference class. At each fixed full-support reference, local
continuity holds, with a bound conditioned on accessible reference amplitudes.
External coherent preparation/calibration is supplied, not physically derived.
Historical selector results are unchanged. Lean checks selected components,
not the complete reconstruction or the assembled operational theorem.
