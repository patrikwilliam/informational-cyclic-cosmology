import IccTickSeparation

-- Deliberately false without independence: both spans can coincide.
example :
    Submodule.span ℝ ({(0 : ℝ), 1, 1} : Set ℝ) ⊓
        Submodule.span ℝ ({(0 : ℝ), 1, 1} : Set ℝ) =
      Submodule.span ℝ ({(0 : ℝ)} : Set ℝ) := by
  simp
