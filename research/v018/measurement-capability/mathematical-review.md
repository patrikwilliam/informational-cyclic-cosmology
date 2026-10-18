# Mathematical Review: Capability-Set Comparison

15 October 2026. Internal AI-assisted derivation and computational review.
No Lean proof or independent expert certification is claimed.

## Verdict

The finite result is stronger than a changed readout: the full invariant-effect
benchmark has a proper inclusion after priming. An actual before-priming
hardware effect lies outside the after-priming benchmark, so even the original
hardware cannot reproduce that effect afterward without changing the declared
resources or symmetry conditions. The enlarged benchmark is not silently
identified with the smaller hardware menu.

## Proof Audit

1. **Measurement definition.** The allowed joint effects obey 0 <= E <= I and
   commute with n_S+Q_R. The induced effect is defined by all-input Born
   probabilities; it is not inferred from the two favored diagnostic states.
2. **Helstrom factors.** The signal difference is rho_+-rho_- = Y, not Y/2.
   Equal-prior optimal success is 1/2 + ||G(Y tensor tau)||_1/4. The only
   nonzero sector has off-diagonal blocks -i B^dagger and i B, with trace norm
   2||B||_1. Thus p* = 1/2+||B||_1/2, attaining 3/4, not 1, for tau_0.
3. **Attainability and upper bound.** The positive spectral effect is invariant.
   Giving eigenvalue 1/2 to its kernel remains a valid optimum. The transverse
   effect bound |F_01| <= ||B||_1/2 follows alternatively from the operator
   norm bound 1/2 on off-diagonal blocks of any positive contraction, followed
   by trace-norm duality. A singular-vector choice attains it.
4. **Primed block.** Block evolution gives B_1 W = (P D+D P)/4, with W unitary
   and D = d_0 I+i d_1 X. Computing the sum of two singular values yields
   ||B_1||_1 = sqrt(d_0^2+d_1^2)/2 = sqrt(1-u)/2. This is checked against
   the full 8x8 evolution and partial trace, including negative diagnostic
   coupling values. It is not inferred from the dephased memory alone.
5. **Strict separation.** F_0's off-diagonal magnitude exceeds the after bound
   by 0.0384147921. Operator norm dominates the magnitude of a matrix element,
   yielding the displayed lower bound on distance to the entire after set.
   The bound is a lower bound, not a claimed exact nearest-effect distance.
6. **Full inclusion.** Phi is CPTP and covariant. Its adjoint, tensored with
   the identity on the new input, maps every allowed after effect to a valid
   invariant before effect with identical statistics on every input. It also
   preserves POVM normalization. This proves inclusion; the one task proves
   strictness. Sampling alone would prove neither universal inclusion nor
   completeness of a measurement family.
7. **Global control.** If the old input is retained, the channel is unitary
   on the larger apparatus. Conjugation of effects is a bijection in the
   invariant class. Full capability sets are then equal. The inverse need
   not be implementable by the narrower fixed-H hardware; the equality is
   explicitly for the maximal invariant class.
8. **Duration optimization.** After priming, the original hardware's transverse
   coefficient is one sinusoid plus a constant. Its exact maximum absolute
   value is beta(sqrt(a^2+d^2)+|d|)/4. The two claimed maxima are attained
   at the displayed times. The same duration menu and outcome relabeling are
   allowed on both sides; randomization cannot increase a linear task score.
9. **No algebra change inferred.** Both resources have nonzero B. The invariant
   benchmark includes nonzero transverse effects and charge-diagonal effects;
   applying a charge-commuting phase rotation gives the other transverse
   direction. The explicit effects span M_2 before and after. Strict effect-set
   inclusion is therefore not a different linear operator algebra.

## Numerical Verification

The deterministic script uses NumPy and the prior finite model read-only:

- 80 arbitrary apparatus states: spectral optimum, adjacent-charge formula,
  optimal invariant-effect feasibility and attainment, and arbitrary-effect
  upper bounds;
- 320 Born comparisons covering all four system matrix units;
- 60 finite evolutions comparing the analytic charge block, its trace norm,
  the symmetric optimum and the mixed-memory control;
- 80 explicit dual-channel simulations of after effects before priming,
  covariance checks, and support-function comparisons;
- 20 invertible global effect transformations with the old input retained;
- 33 times checking the duration formula, plus exact maximizing-time checks.

The largest equality residual in the saved run is below 2e-15, against tolerance
2e-10. Formula proofs and the dual-channel argument carry the general claims;
the finite checks are cross-checks, not an exhaustive proof by computation.

## Limits

Only a single-copy effect-set comparison under the declared symmetry/access
conditions is established. No exact classification of the entire small hardware
set, general nesting of that smaller set, state-independent loss across all
tasks, many-copy distillation bound, postselected advantage bound, monotonicity
in continuous time, or cosmological selector is claimed. Equality of one
discrimination optimum for pure and mixed memory does not imply equality of
their full attainable sets.
