# Scoped Lean Verification for Appendix B

Version 0.1.7, 10 October 2026. These AI-assisted proof scripts check selected
mathematical components, not the complete reconstruction or the ICC proposal.
No external OpenAI manuscript theorem is imported or used as an axiom.

## Checked Statements

The model is the actual infinite Hilbert space ell^2(N_0 x N_0, C), not a
finite matrix truncation. Let S shift the first coordinate, A = {S,S*}'',
and D_r flip the sign of basis vector (0,r).

- `IccWitness.lean` proves a two-fiber unit-ball Hausdorff lemma with explicit
  common-coefficient and witness assumptions.
- `IccConcrete.lean` supplies the concrete von Neumann algebra, discharges
  those assumptions, proves distance exactly 1 and shift difference norm 2,
  and proves that D_r c tends to c in vector norm for every c as r grows.
- `IccArithmetic.lean` proves that (k,r) maps bijectively to 2^k(2r+1) and
  intertwines the coordinate shift with multiplication by 2.
- `IccOperational.lean` proves the projection witness's algebra membership,
  validity of its phase conjugate as an effect, probe normalization,
  probability bounds, the two-fixed-probe obstruction, and the scalar estimate
  ||normalize(z)-normalize(w)|| <= 2||z-w||/||z|| for nonzero z,w.

The unitary identification induced by the arithmetic bijection is an analytic
interpretation, not an additional formal theorem here. The algebra uses
mathlib's bicommutant definition; no separate closure-equivalence theorem is
proved in this project.

## Unformalized Bridges

The reference-to-algebra polar reconstruction, semigroup classification,
stationary-state entropy result, infinite reference normalization and energy
sums, and pure-state trace-distance formula remain analytic. So do the exact
compressed effect-set Hausdorff theorem and the assembled finite-window local
continuity bound. The scalar/probe statements are not substitutes for those
bridges. No continuum-QFT or physical-selection claim is certified.

See the [analytic supplement](../operational-stability.md) and the
[original reconstruction](../arithmetic-reconstruction.md) for those arguments.
No optimality or mathematical novelty is claimed for the local-bound constant.

## Reproduce

Prerequisites: Lean/Elan and Python 3.10+. The pinned toolchain is Lean 4.24.0;
mathlib v4.24.0 is pinned to `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`, with
transitive revisions in `lake-manifest.json`. Dependency downloads are separate
from the bounded proof check and may require several GB.

From this directory:

```sh
lake exe cache get
python3 verify.py --timeout 300
```

Use `--lake /absolute/path/to/lake` and the appropriate `ELAN_HOME` for an
isolated toolchain. The verifier shares a five-minute cap across build, axiom
audit and two deliberately failing controls; it terminates child processes on
timeout. The controls are excluded from normal Lake targets. They intentionally
try to use a distance-one result as a zero-distance proof and a lower bound as
an incompatible upper-bound proof.

`Audit.lean` prints theorem types and the axiom inventories of 16 declarations.
The verifier allows only `propext`, `Classical.choice`, and `Quot.sound` and
rejects unfinished proofs, project axioms and native-evaluation shortcuts.
The checked Lean runtime and cached dependencies remain trusted software; no
independent compiler verification or full library rebuild is claimed.

The bundled `verification-record.json` records the release check. New runs
write only to ignored `verification-output/`; they do not alter that record.
No toolchain, dependency checkout, cache or compiled library is distributed.
