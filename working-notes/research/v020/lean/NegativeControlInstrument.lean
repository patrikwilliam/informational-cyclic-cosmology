import IccOutcomeTick

open IccOutcomeTick

-- Deliberately false: equal POVM effects do not force equal state updates.
example : luders maximallyMixed = alternative maximallyMixed := by
  exact density_outputs_differ
