import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Tactic

noncomputable section
set_option maxHeartbeats 2000000
namespace IccOutcomeTick

open Matrix Complex
open scoped ComplexOrder

abbrev Qubit := Matrix (Fin 2) (Fin 2) ℂ

def r : ℝ := Real.sqrt (1 / 3)
def c : ℝ := Real.sqrt (1 / 8)

theorem r_sq : r ^ 2 = 1 / 3 := Real.sq_sqrt (by norm_num)
theorem c_sq : c ^ 2 = 1 / 8 := Real.sq_sqrt (by norm_num)

theorem rC_sq : (r : ℂ) ^ 2 = 1 / 3 := by
  rw [← Complex.ofReal_pow, r_sq]
  norm_num
theorem cC_sq : (c : ℂ) ^ 2 = 1 / 8 := by
  rw [← Complex.ofReal_pow, c_sq]
  norm_num

def sx : Fin 4 → ℂ := ![1, 1, -1, -1]
def sy : Fin 4 → ℂ := ![1, -1, 1, -1]
def sz : Fin 4 → ℂ := ![1, -1, -1, 1]

/-- I plus the tetrahedral Bloch vector dotted with the Pauli matrices. -/
def P (j : Fin 4) : Qubit :=
  !![1 + sz j * r, (sx j - Complex.I * sy j) * r;
     (sx j + Complex.I * sy j) * r, 1 - sz j * r]

def F (j : Fin 4) : Qubit := (1 / 4 : ℂ) • P j
def M (j : Fin 4) : Qubit := (c : ℂ) • P j

theorem M_hermitian (j : Fin 4) : (M j)ᴴ = M j := by
  fin_cases j <;> ext a b <;> fin_cases a <;> fin_cases b <;>
    simp [M, P, sx, sy, sz, Matrix.conjTranspose_apply]
  all_goals ring_nf
  all_goals simp

theorem kraus_effect (j : Fin 4) : (M j)ᴴ * M j = F j := by
  rw [M_hermitian]
  fin_cases j <;> ext a b <;> fin_cases a <;> fin_cases b <;>
    simp [M, F, P, sx, sy, sz, Matrix.mul_apply, Fin.sum_univ_two]
  all_goals ring_nf
  all_goals simp [rC_sq, cC_sq, Complex.I_sq]
  all_goals ring

theorem effects_sum : ∑ j : Fin 4, F j = 1 := by
  ext a b
  fin_cases a <;> fin_cases b <;>
    simp [F, P, sx, sy, sz, Fin.sum_univ_succ]
  all_goals ring

theorem kraus_normalization : ∑ j : Fin 4, (M j)ᴴ * M j = 1 := by
  simp_rw [kraus_effect]
  exact effects_sum

theorem effect_positive (j : Fin 4) : (F j).PosSemidef := by
  rw [← kraus_effect]
  exact Matrix.posSemidef_conjTranspose_mul_self (M j)

theorem M_rescale (j : Fin 4) : M j = (4 * c : ℝ) • F j := by
  ext a b
  simp [M, F, Complex.real_smul]
  ring

theorem M_positive (j : Fin 4) : (M j).PosSemidef := by
  rw [M_rescale]
  exact (effect_positive j).smul (by dsimp [c]; positivity)

/-- A positive square-root certificate for the declared Luders matrices. -/
theorem luders_square_root (j : Fin 4) :
    (M j).PosSemidef ∧ M j * M j = F j := by
  exact ⟨M_positive j, by simpa only [M_hermitian] using kraus_effect j⟩

def luders (X : Qubit) : Qubit := ∑ j : Fin 4, M j * X * (M j)ᴴ

theorem luders_formula (X : Qubit) :
    luders X = (1 / 3 : ℂ) • (X + Matrix.trace X • (1 : Qubit)) := by
  simp only [luders, M_hermitian]
  ext a b
  fin_cases a <;> fin_cases b <;>
    simp [M, P, sx, sy, sz, Matrix.mul_apply, Matrix.vecMul, dotProduct,
      Fin.sum_univ_succ, Matrix.trace, Matrix.diag]
  all_goals ring_nf
  all_goals simp [rC_sq, cC_sq, Complex.I_sq]
  all_goals ring

theorem luders_offdiagonal (X : Qubit) : luders X 0 1 = X 0 1 / 3 := by
  rw [luders_formula]
  simp [div_eq_mul_inv]
  ring

theorem luders_trace (X : Qubit) : Matrix.trace (luders X) = Matrix.trace X := by
  rw [luders_formula]
  simp [Matrix.trace_fin_two]
  ring

def down : Qubit := !![0, 0; 0, 1]

/-- Two unrecorded reset Kraus indices, not two additional recorded outcomes. -/
def R : Fin 2 → Qubit := ![!![0, 0; 1, 0], !![0, 0; 0, 1]]

def reset (X : Qubit) : Qubit := ∑ a : Fin 2, R a * X * (R a)ᴴ

theorem reset_formula (X : Qubit) : reset X = Matrix.trace X • down := by
  ext a b
  fin_cases a <;> fin_cases b <;>
    simp [reset, R, down, Matrix.conjTranspose_apply, Matrix.mul_apply,
      Matrix.vecMul, dotProduct, Fin.sum_univ_two, Matrix.trace_fin_two]

theorem reset_normalization : ∑ a : Fin 2, (R a)ᴴ * R a = 1 := by
  ext a b
  fin_cases a <;> fin_cases b <;>
    simp [R, Matrix.conjTranspose_apply, Matrix.mul_apply, Fin.sum_univ_two]

def K (j : Fin 4) (a : Fin 2) : Qubit := R a * M j

theorem composed_effect (A : Qubit) :
    (∑ a : Fin 2, (R a * A)ᴴ * (R a * A)) = Aᴴ * A := by
  simp only [Matrix.conjTranspose_mul, ← Matrix.mul_assoc]
  simp_rw [Matrix.mul_assoc Aᴴ]
  rw [← Finset.mul_sum]
  rw [← Finset.sum_mul, reset_normalization, one_mul]

/-- Equality of effects is per recorded outcome, not just after summing j. -/
theorem same_effect (j : Fin 4) : ∑ a : Fin 2, (K j a)ᴴ * K j a = F j := by
  unfold K
  rw [composed_effect, kraus_effect]

theorem alternative_normalization :
    ∑ j : Fin 4, ∑ a : Fin 2, (K j a)ᴴ * K j a = 1 := by
  simp_rw [same_effect]
  exact effects_sum

def resetOutcome (j : Fin 4) (X : Qubit) : Qubit :=
  ∑ a : Fin 2, K j a * X * (K j a)ᴴ

theorem resetOutcome_composition (j : Fin 4) (X : Qubit) :
    resetOutcome j X = reset (M j * X * (M j)ᴴ) := by
  simp only [resetOutcome, reset, K, Matrix.conjTranspose_mul]
  apply Finset.sum_congr rfl
  intro a _
  simp only [Matrix.mul_assoc]

theorem resetOutcome_formula (j : Fin 4) (X : Qubit) :
    resetOutcome j X = Matrix.trace (F j * X) • down := by
  rw [resetOutcome_composition, reset_formula, Matrix.trace_mul_cycle, kraus_effect]

theorem same_outcome_probability (j : Fin 4) (X : Qubit) :
    Matrix.trace (resetOutcome j X) = Matrix.trace (M j * X * (M j)ᴴ) := by
  rw [resetOutcome_composition, reset_formula, Matrix.trace_smul]
  simp [down, Matrix.trace_fin_two]

def alternative (X : Qubit) : Qubit := ∑ j : Fin 4, resetOutcome j X

theorem alternative_formula (X : Qubit) :
    alternative X = Matrix.trace X • down := by
  simp only [alternative, resetOutcome_formula]
  rw [← Finset.sum_smul, ← Matrix.trace_sum, ← Finset.sum_mul, effects_sum, one_mul]

/-- All subsequent qubit effect statistics depend only on the input trace. -/
theorem reset_readout (X E : Qubit) :
    Matrix.trace (E * alternative X) = Matrix.trace X * E 1 1 := by
  rw [alternative_formula]
  simp [down, Matrix.trace_fin_two, Matrix.mul_apply, Fin.sum_univ_two]
  ring

theorem down_effect (j : Fin 4) : (F j) 1 1 = (1 - sz j * r) / 4 := by
  simp [F, P, div_eq_mul_inv]
  ring

theorem second_detector_statistics (j : Fin 4) (X : Qubit) :
    Matrix.trace (F j * alternative X) =
      Matrix.trace X * ((1 - sz j * r) / 4) := by
  rw [reset_readout, down_effect]

theorem instruments_differ : luders (1 : Qubit) ≠ alternative (1 : Qubit) := by
  intro h
  have he := congrArg (fun A : Qubit => A 0 0) h
  rw [luders_formula, alternative_formula] at he
  norm_num [down, Matrix.trace_fin_two] at he

def maximallyMixed : Qubit := (1 / 2 : ℝ) • (1 : Qubit)

theorem maximallyMixed_density :
    maximallyMixed.PosSemidef ∧ Matrix.trace maximallyMixed = 1 := by
  constructor
  · exact (Matrix.PosSemidef.one : (1 : Qubit).PosSemidef).smul (by norm_num : (0 : ℝ) ≤ 1 / 2)
  · norm_num [maximallyMixed, Matrix.trace_fin_two]

theorem density_outputs :
    luders maximallyMixed = maximallyMixed ∧ alternative maximallyMixed = down := by
  constructor
  · rw [luders_formula, maximallyMixed_density.2]
    ext a b
    fin_cases a <;> fin_cases b <;> norm_num [maximallyMixed]
  · rw [alternative_formula, maximallyMixed_density.2, one_smul]

theorem density_outputs_differ : luders maximallyMixed ≠ alternative maximallyMixed := by
  rw [density_outputs.1, density_outputs.2]
  intro h
  have he := congrArg (fun A : Qubit => A 0 0) h
  norm_num [maximallyMixed, down] at he

end IccOutcomeTick
