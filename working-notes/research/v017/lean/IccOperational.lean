import IccArithmetic
import Mathlib.Analysis.InnerProductSpace.Positive
import Mathlib.Analysis.NormedSpace.Normalize

noncomputable section
namespace IccOperational

open IccConcrete
open scoped ENNReal

theorem inner_basis_apply (i : Index) (x : H) : inner ℂ (basis i) x = x i := by
  simp [basis, lp.inner_single_left]

theorem op_ext_basis (a b : Op) (h : ∀ i, a (basis i) = b (basis i)) : a = b := by
  apply lp.ext_continuousLinearMap (by norm_num : (2 : ℝ≥0∞) ≠ ⊤)
  intro i
  apply ContinuousLinearMap.ext
  intro c
  change a (lp.single 2 i c) = b (lp.single 2 i c)
  have hs : (lp.single 2 i c : H) = c • basis i := by
    simpa [basis] using lp.single_smul (𝕜 := ℂ) (E := fun _ : Index => ℂ) 2 i c 1
  rw [hs, map_smul, map_smul, h]

theorem star_shift_zero (r : ℕ) : star shift (basis (0, r)) = 0 := by
  apply lp.ext
  funext i
  rw [← inner_basis_apply i]
  rw [ContinuousLinearMap.star_eq_adjoint, ContinuousLinearMap.adjoint_inner_right, shift_basis]
  rcases i with ⟨k, m⟩
  simp [basis_inner, shiftIndex]

theorem star_shift_succ (k r : ℕ) : star shift (basis (k + 1, r)) = basis (k, r) := by
  apply lp.ext
  funext i
  rw [← inner_basis_apply i, ← inner_basis_apply i (basis (k, r))]
  rw [ContinuousLinearMap.star_eq_adjoint, ContinuousLinearMap.adjoint_inner_right, shift_basis]
  rcases i with ⟨l, m⟩
  simp [basis_inner, shiftIndex]

def ground : Op := 1 - shift * star shift

@[simp] theorem ground_zero (r : ℕ) : ground (basis (0, r)) = basis (0, r) := by
  simp [ground, star_shift_zero]

@[simp] theorem ground_succ (k r : ℕ) : ground (basis (k + 1, r)) = 0 := by
  simp [ground, star_shift_succ, shiftIndex]

def levelSwapIndex : Index ≃ Index :=
  Equiv.prodCongr (Equiv.swap 0 1) (Equiv.refl ℕ)

def levelSwapIso : H →ₗᵢ[ℂ] H := embed levelSwapIndex levelSwapIndex.injective
def levelSwap : Op := levelSwapIso.toContinuousLinearMap

@[simp] theorem levelSwap_basis (i : Index) :
    levelSwap (basis i) = basis (levelSwapIndex i) :=
  embed_basis levelSwapIndex levelSwapIndex.injective i

theorem levelSwap_square : levelSwap * levelSwap = 1 := by
  apply op_ext_basis
  intro i
  simp only [ContinuousLinearMap.mul_apply, levelSwap_basis, ContinuousLinearMap.one_apply]
  congr 1
  rcases i with ⟨k, r⟩
  simp [levelSwapIndex]

theorem levelSwap_star : star levelSwap = levelSwap := by
  have h : star levelSwap * levelSwap = 1 :=
    (ContinuousLinearMap.norm_map_iff_adjoint_comp_self levelSwap).mp levelSwapIso.norm_map
  calc
    star levelSwap = star levelSwap * (levelSwap * levelSwap) := by rw [levelSwap_square, mul_one]
    _ = (star levelSwap * levelSwap) * levelSwap := (mul_assoc _ _ _).symm
    _ = levelSwap := by rw [h, one_mul]

theorem levelSwap_polynomial :
    levelSwap = shift * ground + ground * star shift + 1 - ground - shift * ground * star shift := by
  apply op_ext_basis
  rintro ⟨k, r⟩
  rcases k with _ | (_ | k)
  · simp [ContinuousLinearMap.mul_apply, star_shift_zero, levelSwapIndex, shiftIndex]
  · simp [ContinuousLinearMap.mul_apply, star_shift_succ, levelSwapIndex, shiftIndex]
  · simp [ContinuousLinearMap.mul_apply, star_shift_succ, levelSwapIndex,
      Equiv.swap_apply_of_ne_of_ne]

theorem levelSwap_mem : levelSwap ∈ algebra := by
  have hS : shift ∈ algebraBundled := shift_mem
  have hG : ground ∈ algebraBundled := sub_mem (one_mem _) (mul_mem hS (star_mem hS))
  rw [levelSwap_polynomial]
  exact sub_mem (sub_mem (add_mem (add_mem (mul_mem hS hG) (mul_mem hG (star_mem hS)))
    (one_mem _)) hG) (mul_mem (mul_mem hS hG) (star_mem hS))

def effect : Op := (1 / 2 : ℂ) • (1 + levelSwap)

theorem effect_mem : effect ∈ algebra := by
  have h : 1 + levelSwap ∈ algebraBundled.toStarSubalgebra := add_mem (one_mem _) levelSwap_mem
  exact algebraBundled.toStarSubalgebra.smul_mem h (1 / 2 : ℂ)

theorem effect_projection : IsStarProjection effect := by
  constructor
  · change effect * effect = effect
    apply ContinuousLinearMap.ext
    intro x
    have hL : levelSwap (levelSwap x) = x :=
      congrArg (fun T : Op => T x) levelSwap_square
    simp [effect, ContinuousLinearMap.mul_apply, hL]
    module
  · change star effect = effect
    simp [effect, star_smul, star_add, levelSwap_star]

theorem effect_positive : effect.IsPositive :=
  ContinuousLinearMap.IsPositive.of_isStarProjection effect_projection

theorem complement_positive : (1 - effect).IsPositive := by
  apply ContinuousLinearMap.IsPositive.of_isStarProjection
  exact effect_projection.one_sub

theorem conjugate_positive (r : ℕ) (a : Op) (ha : a.IsPositive) :
    (conjugate r a).IsPositive := by
  have h := ha.conj_adjoint (phaseFlip r : Op)
  change ((phaseFlip r : Op) * a * star (phaseFlip r : Op)).IsPositive at h
  simpa [phaseFlip_star] using h

theorem conjugate_one (r : ℕ) : conjugate r 1 = 1 := by
  apply ContinuousLinearMap.ext
  intro x
  simp [conjugate, ContinuousLinearMap.mul_apply, phaseFlip]

theorem flipped_effect_valid (r : ℕ) :
    (conjugate r effect).IsPositive ∧ (1 - conjugate r effect).IsPositive := by
  refine ⟨conjugate_positive r effect effect_positive, ?_⟩
  have h := conjugate_positive r (1 - effect) complement_positive
  have heq : conjugate r (1 - effect) = 1 - conjugate r effect := by
    simp only [conjugate, mul_sub, sub_mul]
    rw [← conjugate, conjugate_one]
  rwa [heq] at h

def ray (r : ℕ) : H := basis (0, r) + basis (1, r)

theorem ray_inner_self (r : ℕ) : inner ℂ (ray r) (ray r) = 2 := by
  norm_num [ray, inner_add_left, inner_add_right, basis_inner]

theorem ray_norm_sq (r : ℕ) : ‖ray r‖ ^ 2 = 2 := by
  have h := congrArg Complex.re (ray_inner_self r)
  simpa [inner_self_eq_norm_sq_to_K, pow_two, Complex.mul_re] using h

def probability (a : Op) (r : ℕ) : ℝ := (inner ℂ (ray r) (a (ray r))).re / 2

theorem probability_range (a : Op) (ha : a.IsPositive) (hc : (1 - a).IsPositive)
    (r : ℕ) : 0 ≤ probability a r ∧ probability a r ≤ 1 := by
  have h0 := ha.re_inner_nonneg_right (ray r)
  have h1 := hc.re_inner_nonneg_right (ray r)
  simp only [ContinuousLinearMap.sub_apply, ContinuousLinearMap.one_apply,
    inner_sub_right, map_sub, ray_inner_self] at h1
  change 0 ≤ 2 - (inner ℂ (ray r) (a (ray r))).re at h1
  change 0 ≤ (inner ℂ (ray r) (a (ray r))).re at h0
  dsimp [probability]
  constructor <;> linarith

theorem common_probability (a : Op) (ha : a ∈ algebra) (r s : ℕ) :
    probability a r = probability a s := by
  have hc := ha (swapOp r s) (swap_mem_commutant r s)
  have hx := congrArg (fun T : Op => T (ray r)) hc
  have hu : swapOp r s (ray r) = ray s := by simp [ray, swapIndex]
  have hi := (swapIso r s).inner_map_map (ray r) (a (ray r))
  change inner ℂ (swapOp r s (ray r)) (swapOp r s (a (ray r))) = _ at hi
  simp only [ContinuousLinearMap.mul_apply, hu] at hx
  rw [hu, hx] at hi
  exact congrArg (fun z : ℂ => z.re / 2) hi.symm

theorem effect_ray (r : ℕ) : effect (ray r) = ray r := by
  simp [effect, ray, levelSwapIndex]
  module

theorem flipped_effect_ray_same (r : ℕ) : conjugate r effect (ray r) = 0 := by
  simp [conjugate, ContinuousLinearMap.mul_apply, effect, ray, levelSwapIndex]
  module

theorem flipped_effect_ray_other (r s : ℕ) (hrs : s ≠ r) :
    conjugate r effect (ray s) = ray s := by
  simp [conjugate, ContinuousLinearMap.mul_apply, effect, ray, levelSwapIndex, hrs]
  module

theorem witness_probabilities :
    probability (conjugate 1 effect) 0 = 1 ∧ probability (conjugate 1 effect) 1 = 0 := by
  constructor
  · rw [probability, flipped_effect_ray_other 1 0 (by decide), ray_inner_self]
    norm_num
  · rw [probability, flipped_effect_ray_same]
    simp

theorem two_probability_lower_bound (z : ℝ) : 1 / 2 ≤ max |1 - z| |z| := by
  have h₁ : 1 - z ≤ |1 - z| := le_abs_self _
  have h₂ : z ≤ |z| := le_abs_self _
  have h₃ := le_max_left |1 - z| |z|
  have h₄ := le_max_right |1 - z| |z|
  linarith

theorem fixed_two_probe_obstruction (a : Op) (ha : a ∈ algebra) :
    1 / 2 ≤ max |probability (conjugate 1 effect) 0 - probability a 0|
      |probability (conjugate 1 effect) 1 - probability a 1| := by
  rw [witness_probabilities.1, witness_probabilities.2, common_probability a ha 0 1]
  simpa using two_probability_lower_bound (probability a 1)

/-- Conditioning of the scalar phase, with a denominator that cannot be
discarded when reference amplitudes are allowed to approach zero. -/
theorem phase_perturbation_bound (z w : ℂ) (hz : z ≠ 0) (hw : w ≠ 0) :
    ‖NormedSpace.normalize z - NormedSpace.normalize w‖ ≤ 2 * ‖z - w‖ / ‖z‖ := by
  have hzpos : 0 < ‖z‖ := norm_pos_iff.mpr hz
  have hnw : ‖NormedSpace.normalize w‖ = 1 := NormedSpace.norm_normalize hw
  have hid : ‖z‖ • (NormedSpace.normalize z - NormedSpace.normalize w) =
      (z - w) + (‖w‖ - ‖z‖) • NormedSpace.normalize w := by
    rw [smul_sub, sub_smul, NormedSpace.norm_smul_normalize,
      NormedSpace.norm_smul_normalize]
    abel
  have h := norm_add_le (z - w) ((‖w‖ - ‖z‖) • NormedSpace.normalize w)
  rw [← hid, norm_smul, norm_smul, hnw, mul_one, Real.norm_eq_abs,
    abs_of_pos hzpos] at h
  rw [Real.norm_eq_abs] at h
  have hr : |‖w‖ - ‖z‖| ≤ ‖z - w‖ := by
    simpa [norm_sub_rev] using abs_norm_sub_norm_le w z
  apply (le_div_iff₀ hzpos).mpr
  simpa [mul_comm] using (show ‖z‖ * ‖NormedSpace.normalize z - NormedSpace.normalize w‖ ≤
    2 * ‖z - w‖ by linarith)

#print axioms effect_mem
#print axioms effect_projection
#print axioms ray_norm_sq
#print axioms flipped_effect_valid
#print axioms probability_range
#print axioms fixed_two_probe_obstruction
#print axioms phase_perturbation_bound

end IccOperational
