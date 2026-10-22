# Mathematical Review: Simultaneous Three-Qubit Model

15 October 2026. Internal AI-assisted review, not expert or Lean certification.

## Verdict

The displayed finite-dimensional identities and bounded computational checks
are consistent. The positive result is a changed induced POVM after unread
priming at unchanged coupling, duration, and readout. The exact mixed-memory
control rules out necessity of a LOCAL memory record for that change in this
model. Neither statement is a general selector theorem.

## Independent Derivation Pass

1. Resolve the conserved X_M sectors. In each, the one-excitation S,D block
   is [[mu k,g],[g,0]]. Subtracting mu k I/2 leaves a matrix squaring to
   (g^2+k^2/4)I, which proves the analytic propagator in the README.
2. The n_D Heisenberg effect in that block has off-diagonal entry
   beta s (mu alpha s-i c). Multiplying by the initial detector coherence
   1/2 and averaging mu gives y_0 = beta sc/2.
3. For S = I/2, the normalized primed detector state in memory-X sector mu
   has populations 1/2 and coherence exp(i mu delta)(c+i mu alpha s)/2.
   Its product with the block effect is
   -i beta s exp(i mu delta)(c+i mu alpha s)^2/2.
   Averaging over mu proves the stated y_1. Cross-sector memory coherences
   do not contribute to the detector pointer, but within-sector DM
   correlations MUST be retained.
4. For the two initial D labels, memory overlap-factor difference is
   i exp(-ikT)[sin(kT)+2 alpha sc]. Dividing by two gives the density-matrix
   off-diagonal difference. Its eigenvalues yield D_tr; taking the real
   component gives D_pop. These are different attainable-measurement claims.
5. Dephasing the apparatus only between X_M sectors cannot change a D-only
   outcome: both the propagator and pointer commute with X_M. The same is
   true after partial tracing a used S, by blockwise linearity. This proves
   the mixed/pure memory equivalence for further unread fresh-input trials.
   It is not restricted to the four repetitions checked numerically.

## Numerical Cross-Checks

The script independently constructs the 8x8 Hamiltonian using tensor products
and exponentiates it by Hermitian eigendecomposition. The analytic solution
instead exponentiates the 2x2 excitation blocks. They agree in 80 seeded cases.
The effect contraction is compared to full Born probabilities on all four
system matrix units, for each of two pointers and arbitrary apparatus states:
640 comparisons. This avoids checking only the favored input pair.

Sixty additional seeded cases compare the closed before/after formulas,
memory distances, primed X blocks, and dephasing equivalence. Matrix positivity,
unitarity, conservation, zero-coupling limits, and invalid sequential-gate
shortcuts are also checked. Largest equality residual in the saved run is
below 7e-15, against tolerance 2e-10. Numerical agreement supports the written
derivation; it is not a replacement for it or a machine-checked proof.

## Pitfalls Explicitly Excluded

- Simultaneous U is not U_record U_exchange or its reverse: the interactions
  do not commute. At the primary setting the operator-norm discrepancy from
  either sequential product is about 0.28297.
- Discarding DM correlations changes the second effect by about 0.06660 in
  operator norm. The actual calculation keeps the full joint state.
- No intermediate population measurement is inserted. Adding one would be
  a different instrument and produce a different apparatus update.
- Nonzero [F_0,F_1] excludes binary classical postprocessing equivalence, not
  general joint measurability of arbitrary unsharp POVMs.
- The memory is neutral under Q. Including n_M in Q would invalidate the
  conservation assertion for n_D X_M.
- [H,Q] = 0 establishes conservation during each closed exposure, not during
  input replacement or terminal measurement.

## Remaining Limits

Finite, supplied factors and a specified Hamiltonian; no continuum limit,
observable-algebra selection, entropy reset, autonomous input transport,
relational clock, or irreversible record. The arithmetic is not evidence for
either successive aeons or a timeless global ontology.
