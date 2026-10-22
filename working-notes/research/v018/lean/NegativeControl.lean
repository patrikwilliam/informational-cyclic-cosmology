import IccCapability

-- Deliberately false reversal of the certified strict inequality.
example :
    Real.sqrt (IccCapability.primaryX * (1 - IccCapability.primaryX) / 5) <
      Real.sqrt (1 - 4 * IccCapability.primaryX / 5) / 4 := by
  exact IccCapability.primary_scalar_gap
