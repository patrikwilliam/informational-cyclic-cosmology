# Scoped Lean Verification: Measurement Capability

16 October 2026. Lean 4.24.0; mathlib v4.24.0, pinned commit
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7` in `lake-manifest.json`.

## Result and Limit

The [source](IccCapability.lean) passes Lean's kernel checking. The
[record](verification-record.json) contains source hashes, toolchain version,
the dependency inventory for 13 declarations and expected rejections of two
false test statements. The recorded combined verification took 28.882 seconds
using an already installed toolchain and cached dependencies. Proof development
and testing were completed within the requested two-hour cap; a cold dependency
installation is not included in that verification timing.

**This is partial formal verification, not a Lean proof of the entire
three-qubit experiment or the ICC hypothesis.** The bridges listed below are
analytic and numerically cross-checked, not silently assumed proved by Lean.
No external expert review or new mathematical principle is claimed.

## Checked Statements

Operators are actual bounded complex-linear maps on complete inner-product
spaces. `Effect e` means that both `e` and `1-e` are positive operators using
mathlib's Hilbert-space positivity, not a freely assigned Boolean label.

| Declarations | Formal content | Explicit boundary |
|---|---|---|
| `kraus_positive`, `kraus_unital`, `krausPullback` | A finite map `L(E) = sum_j V_j^* E V_j` is positive, and unital when `sum_j V_j^* V_j = I` | Concrete Kraus matrices and covariance are not instantiated |
| `pullback_effect`, `pullback_invariant` | A positive unital linear pullback preserves effects; covariance preserves fixed points of a supplied action | Positivity must hold on the whole joint system, not only on a resource factor |
| `capability_inclusion` | After capabilities are a subset of before capabilities | Assumes the pullback properties and `oldExtract(L(E)) = newExtract(E)` |
| `finite_povm_pullback` | Every effect remains valid and invariant; the finite sum remains identity | A finite family with normalized sum is supplied |
| `reversible_capabilities` | Compatible simulation maps in both directions imply equality | Does not construct the retained-resource unitary |
| `strict_inclusion_from_witness` | Inclusion plus a separating score witness implies proper inclusion | Membership and the universal score bound are premises |
| `squared_gap`, `strict_scalar_separation` | For `1/2 <= x <= 3/4`, the squared gap is at least `1/80`, hence nonnegative roots are strictly separated | Assumes the displayed formulas for the two squares |
| `primary_interval`, `primary_scalar_gap` | At `x = sin(pi sqrt(5)/8)^2`, the interval and strict square-root inequality hold exactly | Identification with the physical effects remains analytic |

The covariance interface uses a family of actions and proves a fixed-point
implication; group laws are unnecessary for that implication. In the physical
application the action is total-charge conjugation. The extraction maps have
a generic codomain; to apply the inclusion theorem to POVM effects, the
all-input Born identity must be established separately. The theorem does not
infer this identity from agreement on two test states.

The exact scalar certificate is

$$
x=\sin^2(\pi\sqrt5/8),\quad \frac12\le x\le\frac34,\qquad
\frac{x(1-x)}5-\frac{1-4x/5}{16}\ge\frac1{80}.
$$

It proves `sqrt(1-4*x/5)/4 < sqrt(x*(1-x)/5)` without floating-point
approximations. The latter expression equals the original transverse
magnitude for the analytically derived primary effect. Lean does not evaluate
or certify the manuscript's displayed decimal digits.

## Not Formalized Here

- Construction of `exp(-i H T)`, the partial trace and concrete priming channel.
- The tensor extension of that channel, its concrete covariance, and its
  Born-pairing identity. Complete positivity of the resource channel is needed
  to justify positivity after tensoring with the identity; mere positivity
  on the resource alone is not asserted sufficient.
- Helstrom optimization, the trace-norm/charge-block formula, identification of
  the concrete witness, duration optimization, and the operator-norm distance
  bound or full-algebra-span result.
- The unitary forward/inverse instantiation for retained old-input access.
- Physical justification of the resource boundary, symmetry, clock, interaction,
  factorization or any ICC cosmological interpretation.

Consequently the full concrete strict-inclusion claim remains an analytic
derivation supported by numerical checks and these formal components, not an
end-to-end machine-verified theorem.

## Reproduce

With the pinned toolchain and dependencies available:

```bash
cd research/v018/lean
python3 verify.py --timeout 300
```

An isolated installation can be selected with `--lake /path/to/lake` and its
`ELAN_HOME`. A new checkout may first require `lake update` and
`lake exe cache get`; retain the pinned manifest and inspect any dependency
changes. The 300-second runner timeout is shared by all verification commands,
not reset for every step. It cannot promise a cold installation in that time.

The runner checks forbidden proof escapes, builds the positive target, audits
the named declarations, and requires both negative controls to fail for their
intended reason. `NegativeControl.lean` reverses the proved inequality;
`NegativeControlInterval.lean` tries the interval theorem at `x=0`. These files
are intentionally not default build targets. Their rejection is a sanity check,
not independent evidence for the physical model.

The audited logical dependencies are exactly within `propext`,
`Classical.choice`, and `Quot.sound`, the usual classical mathlib foundations.
There are no added scientific assumptions hidden as custom Lean axioms, no
`sorry`/`admit` placeholders, and no `native_decide` or unsafe proof shortcut.
The scientific premises remain visible theorem arguments and documented
unformalized bridges.

Fresh logs go to ignored `verification-output/`; the bundled record is not
overwritten. `.lake/`, cached packages and local toolchains are not publication
content. Rechecking the Lean files does not modify v0.1.7's proof project.
