import IccCapability

-- Deliberately false extension of the interval certificate to x = 0.
example : (1 : ℝ) / 80 ≤ (0 : ℝ) * (1 - 0) / 5 - (1 - 4 * 0 / 5) / 16 := by
  exact IccCapability.squared_gap 0 (by norm_num) (by norm_num)
