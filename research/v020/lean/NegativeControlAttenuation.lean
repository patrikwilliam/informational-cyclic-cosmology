import IccOutcomeTick

open IccOutcomeTick

-- Deliberately false: removing the attenuation changes the result.
example (X : Qubit) : luders X 0 1 = X 0 1 := by
  exact luders_offdiagonal X
