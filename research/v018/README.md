# v0.1.8 Reproducibility Supplement

16 October 2026. Conditional finite measurement capabilities, not an ICC
selector or a reinterpretation of the core postulates.

## What Is Established

For the specified three-qubit apparatus, unread priming changes the retained
reference state. With one copy, the old input inaccessible, and the same
charge-symmetric processing class before and after, the attainable system
effect set is strictly smaller afterward. The implemented before score
`0.7197744539` exceeds even the broad after optimum `0.6813596618`.

This distinguishes genuine capability loss from a merely inefficient chosen
readout. It does not derive the access boundary. Both sets span the same `M_2`
algebra, and retaining the old input with arbitrary symmetric joint control
restores equality of the full capability sets.

## Contents and Evidence Levels

- [Three-qubit model](three-qubit-memory/README.md): fixed simultaneous
  interaction, exact propagator/effect formulas, unread priming and controls.
- [Capability derivation](measurement-capability/README.md): symmetric
  Helstrom optimum, analytic charge-coherence bound, full-set inclusion and
  witness, duration optimization and retained-resource comparison.
- [Model output](three-qubit-memory/checks-results.json) and
  [capability output](measurement-capability/checks-results.json): deterministic
  numerical cross-checks with source hashes, not exhaustive proofs.
- [Lean scope and reproduction](lean/README.md): checked operator lemmas and
  exact scalar gap, explicit analytic bridges, dependency audit and failing
  controls. This is not end-to-end formalization of the physical calculation.
- [Mathematical review](../../feedback/v0.1.8-mathematical-review.md) and
  [physics review](../../feedback/v0.1.8-physics-review.md): separate internal
  AI-assisted passes, not external expert certification.

The copied 15 October derivations/reviews preserve the earlier finite study.
The scripts' only integration change is the capability script's relative
import path. Its updated hash is recorded. Earlier comments that the numerical
scripts are not Lean proofs remain correct; the formal component is separate.
No OpenAI manuscript conjecture or unverified AI-generated theorem is used as
a mathematical premise.

## Run the Bounded Checks

From the repository root, with Python 3.10+ and NumPy:

```bash
python3 research/v018/run_checks.py --timeout 120
```

This runs both suites with Python optimization enabled, so correctness gates
cannot depend on removable `assert` statements. Fresh reports go to ignored
`verification-output/`, leaving the bundled outputs unchanged. The saved run
uses Python 3.12.14 and NumPy 2.3.5. Maximum equality residuals were approximately
`6.58e-15` for the model and `1.93e-15` for the capability suite, against a
`2e-10` tolerance. This is not a continuum limit, physical validation or a
new lattice campaign.

For formal checking, follow the separate Lean README. Its current verification
completed in 28.882 seconds with cached dependencies; this is not an estimate
for a fresh toolchain installation or a complete quantum-information library.

## Sources and Claim Boundary

The analytic methods are established reference-frame/asymmetry resource theory
and minimum-error discrimination. The derivation links Bartlett, Rudolph and
Spekkens (2007), Bartlett et al. (2006), Marvian and Spekkens (2012), and Barnett
and Croke (2008). Their role is prior art and mathematical tools, not endorsement
of ICC. The specific finite formulas are presented for checking without a
priority claim. The main missing problem remains an independently justified
physical access/algebra selector; measurement-strength loss alone does not
solve it.
