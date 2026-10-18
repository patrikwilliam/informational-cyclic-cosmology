import IccOperational

open IccConcrete IccOperational

-- Deliberately wrong: a lower bound is not a proof of this strict upper bound.
example (a : Op) (ha : a ∈ algebra) :
    max |probability (conjugate 1 effect) 0 - probability a 0|
      |probability (conjugate 1 effect) 1 - probability a 1| ≤ 1 / 4 := by
  exact fixed_two_probe_obstruction a ha
