import IccConcrete

-- This file MUST fail: it deliberately asks the checked distance-one
-- theorem to prove the incompatible conclusion zero.
example (r : ℕ) :
    Metric.hausdorffDist (IccWitness.unitPart IccConcrete.algebra)
      (IccWitness.unitPart (IccConcrete.flippedAlgebra r)) = 0 := by
  exact IccConcrete.concrete_distance_one r
