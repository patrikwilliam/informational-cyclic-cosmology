# Scoped Lean Verification: Outcome-Bearing Ticks

19 October 2026. Scoped formal supplement for v0.2.0, not a replacement for
the paper's mathematical and physics reviews. The checked source is copied
unchanged from the bounded working proof project.

The integrated release-folder recheck also passed in **47.688 seconds** with
the same cached dependencies. Its [separate record](release-verification-record.json)
preserves the new command paths and source hashes without replacing the
original development record below. The proof scope is unchanged.

## Result

**32 theorem declarations pass Lean's kernel checking.** These include helper
identities as well as the main results; they are not 32 new scientific results.
Three deliberately false controls are rejected for the intended reasons.

The [verification record](verification-record.json) includes source hashes,
the toolchain, each command's exit status, and every theorem's logical
dependencies. The full recorded recheck took **41.805 seconds** with the
existing toolchain and cached dependencies. This is not the time to develop
the proofs or install dependencies. The work was carried out within the
user's two-hour development cap, starting at 12:43:54 UTC on 19 October 2026.

Lean 4.24.0 and mathlib v4.24.0 are pinned. The checked mathlib commit is
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`; the runner also checked that its
tracked source was unmodified. No new installation was needed.

## Concrete Detector Results

[IccOutcomeTick.lean](IccOutcomeTick.lean) uses actual complex 2-by-2 matrices,
their conjugate transposes and the usual matrix trace. Positivity is mathlib's
positive-semidefinite matrix predicate, not an assigned label.

The tetrahedral vectors have the sign patterns
`(+++)`, `(+--)`, `(-+-)`, `(--+)`, with magnitude `r = sqrt(1/3)` in each
coordinate. The source defines `c = sqrt(1/8)`, so its matrices
`M_j = c (I + v_j dot sigma)` have the paper's positive square-root coefficient
`1/(2 sqrt(2))`. The corresponding effects are `F_j = (I + v_j dot sigma)/4`.

| Formal result | What it checks |
| --- | --- |
| `kraus_effect`, `effects_sum`, `kraus_normalization` | Each `M_j^* M_j = F_j`, and both normalization sums equal identity. |
| `effect_positive`, `M_positive`, `luders_square_root` | Effects are positive; each `M_j` is positive and squares to `F_j`. This is a positive square-root certificate, not just a Hermitian factor. |
| `luders_formula` | For every complex qubit matrix `X`, `sum_j M_j X M_j^* = (X + tr(X) I)/3`. |
| `luders_offdiagonal`, `luders_trace` | The detector off-diagonal entry is divided by three, and the trace is preserved. |
| `same_effect`, `same_outcome_probability` | The alternative instrument has the same effect and probability for each recorded outcome, for every qubit input matrix. |
| `resetOutcome_formula`, `alternative_formula` | Its outcome maps are `tr(F_j X) P_down`, and their sum is `tr(X) P_down`. |
| `reset_readout`, `second_detector_statistics` | Immediate subsequent detector statistics depend only on the input trace; the tetrahedral readout coefficient is `(1-v_jz)/4`. |
| `maximallyMixed_density`, `density_outputs`, `density_outputs_differ` | `I/2` is positive with trace one; its two nonselective outputs are respectively `I/2` and `P_down`, and these differ. |

These are exact symbolic results, not checks of selected floating-point inputs.
They do not establish a new mathematical principle or a physical realization.

### How the Counterexample Is Represented

The [manuscript, Appendix D.4](../../../PAPER.md#d4-same-effects-different-instrument) uses one
rank-one Kraus matrix `N_j = |-z><v_j|/sqrt(2)` per recorded outcome.
The formalization avoids square-root spinor coordinates by giving the same
outcome map a two-Kraus representation:

```text
R_0 = |-z><+z|,  R_1 = |-z><-z|,
K_{j,a} = R_a M_j,
sum_a K_{j,a} X K_{j,a}^* = tr(F_j X) P_down.
```

The index `a` is unrecorded; this is still a four-outcome instrument, not an
eight-outcome measurement. Equality of the outcome maps follows from the
displayed formula and the analytic rank-one expression for `F_j`. The
particular eigenvectors `|v_j>` and their single-Kraus representation are not
constructed in Lean. The concrete two-Kraus counterexample itself is checked.

**Same POVM does not mean same sequential instrument.** The result verifies
that distinction; it does not refute the explicitly specified Luders model
or show that its response is destroyed by every small perturbation.

## Conditional Separation Result

[IccTickSeparation.lean](IccTickSeparation.lean) proves, over any field and
vector space, that linear independence of `e,u1,v1,u2,v2` implies

```text
span{e,u1,v1} intersect span{e,u2,v2} = span{e}.
```

For the proposed application the inputs would be
`I,Z1,Z1*,Z2,Z2*` over the complex numbers. Their independence is an explicit
theorem premise, **not a new axiom and not proved for the continuum model in
this Lean project**. Nor does this generic lemma prove that the record effects
span these particular operator systems. Those remain analytic bridges in the
[construction, Appendix D.3](../../../PAPER.md#d3-conditional-continuum-separation).

## Boundaries After Formalization

The following remain outside the machine-checked scope:

- The field-detector tensor extension, its operator-valued block action, and
  evolution under the unbounded continuum Hamiltonian.
- The clock/register Lindblad dynamics, exponential wait weights, and
  normalization of the full 21-effect retained-record POVM.
- Preservation of the reset detector sector under the full field interaction,
  integration over the second tick time, and the formula for the complete
  field effect `B_k^reset = q2 (1-v_kz) I/4`.
- The Weyl-integral independence argument, finite-energy witnesses, operational
  preparation costs and retention faults.
- Differences between generated von Neumann algebras, a physical selector,
  an entropy reset, or an ICC cosmological transition.

In particular, `second_detector_statistics` does not formalize intervening
field evolution or the time factor `q2`, despite its short declaration name.
Extending the qubit channel formula to field-valued blocks remains an analytic
step here. The [physical limitations in Appendix D.5](../../../PAPER.md#d5-physical-implementation-and-the-next-gate) still apply: phase,
energy, reservoir and hardware resources are not supplied by a formal proof.

The appropriate release claim is **selected detector-instrument identities,
a same-POVM counterexample, and a conditional linear-algebra lemma formally
verified**. It is not an end-to-end formal verification of the outcome-tick
construction or of ICC. This is AI-assisted development and scope review,
not external peer review.

## Reproduce and Audit

With the pinned toolchain and cached dependencies available, run from this
directory:

```bash
python3 verify.py --timeout 300
```

An isolated Lake executable can be selected with `--lake /path/to/lake` and
the appropriate `ELAN_HOME`. A clean checkout needs the pinned dependencies
first; the 300-second verification cap is not a promise for cold setup.
The runner shares one timeout across its subprocesses and terminates their
process groups if it expires.

The runner builds both modules, checks their source directly, and audits
every theorem with `#print axioms`. Dependencies are limited to `propext`,
`Classical.choice` and `Quot.sound`, the usual classical mathlib foundations.
There are no added axioms, proof placeholders, or native-computation proof
shortcuts in the new source. Standard compiled Lean/mathlib dependencies are
trusted; the entire dependency library was not rebuilt from scratch.

The negative controls attempt to equate the different instruments, remove
the attenuation factor, and drop the separation lemma's independence
condition. Their rejection is a regression sanity check, not evidence of
physical applicability. They are intentionally excluded from default targets.

Fresh logs go to ignored `verification-output/`; the bundled record is not
overwritten. `.lake/` and the reused dependency cache are not publication
content. Older Lean projects and the original working proof files are
unchanged. Proof source hashes in the record remain valid after integration;
only this explanatory README's links and release context were updated.
