import IccWitness
import Mathlib.Analysis.InnerProductSpace.l2Space
import Mathlib.Analysis.InnerProductSpace.Adjoint
import Mathlib.Analysis.InnerProductSpace.Projection.Reflection
import Mathlib.Algebra.Group.Center
import Mathlib.Analysis.VonNeumannAlgebra.Basic

noncomputable section
namespace IccConcrete

open scoped ENNReal Topology Pointwise
open Filter

abbrev Index := ℕ × ℕ
abbrev H := ℓ²(Index, ℂ)
abbrev Op := H →L[ℂ] H

def basis (i : Index) : H := lp.single 2 i 1

@[simp] theorem basis_norm (i : Index) : ‖basis i‖ = 1 := by
  simp [basis, lp.norm_single]

@[simp] theorem basis_inner (i j : Index) :
    inner ℂ (basis i) (basis j) = if i = j then 1 else 0 := by
  dsimp [basis]
  rw [lp.inner_single_left]
  by_cases h : i = j
  · subst j; simp
  · rw [lp.single_apply_ne 2 j 1 h]
    simp [h]

def singleIso (i : Index) : ℂ →ₗᵢ[ℂ] H :=
  { lp.lsingle (𝕜 := ℂ) (E := fun _ : Index => ℂ) 2 i with
    norm_map' := by
      intro x
      exact lp.norm_single (E := fun _ : Index => ℂ) (p := 2) (by norm_num) i x }

theorem embedded_orthogonal (f : Index → Index) (hf : Function.Injective f) :
    OrthogonalFamily ℂ (fun _ : Index => ℂ) (fun i => singleIso (f i)) := by
  intro i j hij a b
  change inner ℂ (lp.single (E := fun _ : Index => ℂ) 2 (f i) a)
    (lp.single 2 (f j) b) = 0
  rw [lp.inner_single_left,
    lp.single_apply_ne (E := fun _ : Index => ℂ) 2 (f j) b (hf.ne hij)]
  simp

def embed (f : Index → Index) (hf : Function.Injective f) : H →ₗᵢ[ℂ] H :=
  (embedded_orthogonal f hf).linearIsometry

@[simp] theorem embed_single (f : Index → Index) (hf : Function.Injective f)
    (i : Index) (c : ℂ) :
    embed f hf (lp.single 2 i c) = lp.single 2 (f i) c := by
  exact (embedded_orthogonal f hf).linearIsometry_apply_single c

@[simp] theorem embed_basis (f : Index → Index) (hf : Function.Injective f)
    (i : Index) : embed f hf (basis i) = basis (f i) := embed_single f hf i 1

def shiftIndex (i : Index) : Index := (i.1 + 1, i.2)

theorem shiftIndex_injective : Function.Injective shiftIndex := by
  intro i j h
  cases i; cases j
  simp_all [shiftIndex, Prod.mk.injEq]

def shiftIso : H →ₗᵢ[ℂ] H := embed shiftIndex shiftIndex_injective
def shift : Op := shiftIso.toContinuousLinearMap

@[simp] theorem shift_single (i : Index) (c : ℂ) :
    shift (lp.single 2 i c) = lp.single 2 (shiftIndex i) c :=
  embed_single shiftIndex shiftIndex_injective i c

@[simp] theorem shift_basis (i : Index) : shift (basis i) = basis (shiftIndex i) :=
  shift_single i 1

def swapIndex (r s : ℕ) : Index ≃ Index :=
  Equiv.prodCongr (Equiv.refl ℕ) (Equiv.swap r s)

def swapIso (r s : ℕ) : H →ₗᵢ[ℂ] H :=
  embed (swapIndex r s) (swapIndex r s).injective

def swapOp (r s : ℕ) : Op := (swapIso r s).toContinuousLinearMap

@[simp] theorem swap_single (r s : ℕ) (i : Index) (c : ℂ) :
    swapOp r s (lp.single 2 i c) = lp.single 2 (swapIndex r s i) c :=
  embed_single (swapIndex r s) (swapIndex r s).injective i c

@[simp] theorem swap_basis (r s : ℕ) (i : Index) :
    swapOp r s (basis i) = basis (swapIndex r s i) := swap_single r s i 1

theorem swap_square (r s : ℕ) : swapOp r s * swapOp r s = 1 := by
  apply lp.ext_continuousLinearMap (by norm_num : (2 : ℝ≥0∞) ≠ ⊤)
  intro i
  apply ContinuousLinearMap.ext
  intro c
  change swapOp r s (swapOp r s (lp.single 2 i c)) = lp.single 2 i c
  rw [swap_single, swap_single]
  congr 1
  rcases i with ⟨k, m⟩
  simp [swapIndex]

theorem swap_commutes_shift (r s : ℕ) : shift * swapOp r s = swapOp r s * shift := by
  apply lp.ext_continuousLinearMap (by norm_num : (2 : ℝ≥0∞) ≠ ⊤)
  intro i
  apply ContinuousLinearMap.ext
  intro c
  change shift (swapOp r s (lp.single 2 i c)) = swapOp r s (shift (lp.single 2 i c))
  rw [swap_single, shift_single, shift_single, swap_single]
  rfl

theorem swap_star (r s : ℕ) : star (swapOp r s) = swapOp r s := by
  have h : star (swapOp r s) * swapOp r s = 1 := by
    exact (ContinuousLinearMap.norm_map_iff_adjoint_comp_self (swapOp r s)).mp
      (swapIso r s).norm_map
  calc
    star (swapOp r s) = star (swapOp r s) * (swapOp r s * swapOp r s) := by rw [swap_square, mul_one]
    _ = (star (swapOp r s) * swapOp r s) * swapOp r s := (mul_assoc _ _ _).symm
    _ = swapOp r s := by rw [h, one_mul]

def generators : Set Op := {shift, star shift}
def algebra : Set Op := Set.centralizer (Set.centralizer generators)

theorem algebra_as_starSubalgebra :
    algebra = (StarSubalgebra.centralizer ℂ
      (StarSubalgebra.centralizer ℂ ({shift} : Set Op) : Set Op) : Set Op) := by
  rw [StarSubalgebra.coe_centralizer_centralizer]
  simp [algebra, generators, Set.star_singleton, Set.pair_comm]

/-- Concrete von Neumann algebra, in mathlib's bicommutant definition. -/
def algebraBundled : VonNeumannAlgebra H where
  toStarSubalgebra := (StarSubalgebra.centralizer ℂ
    (StarSubalgebra.centralizer ℂ ({shift} : Set Op) : Set Op)).copy
      algebra algebra_as_starSubalgebra
  centralizer_centralizer' := by
    change Set.centralizer (Set.centralizer algebra) = algebra
    simp [algebra]

@[simp] theorem algebraBundled_carrier : (algebraBundled : Set Op) = algebra := rfl

theorem shift_mem : shift ∈ algebra :=
  Set.subset_centralizer_centralizer (by simp [generators])

theorem zero_mem : (0 : Op) ∈ algebra := by
  intro a ha
  simp

theorem swap_mem_commutant (r s : ℕ) : swapOp r s ∈ Set.centralizer generators := by
  intro a ha
  rcases (show a = shift ∨ a = star shift by simpa [generators] using ha) with rfl | rfl
  · exact swap_commutes_shift r s
  · have h := congrArg star (swap_commutes_shift r s)
    simpa only [star_mul, swap_star] using h.symm

theorem common_coefficient (a : Op) (ha : a ∈ algebra) (r s : ℕ) :
    inner ℂ (basis (1, r)) (a (basis (0, r))) =
      inner ℂ (basis (1, s)) (a (basis (0, s))) := by
  have hc := ha (swapOp r s) (swap_mem_commutant r s)
  have happly := congrArg (fun T : Op => T (basis (0, r))) hc
  simp only [ContinuousLinearMap.mul_apply, swap_basis] at happly
  have hinner := (swapIso r s).inner_map_map (basis (1, r)) (a (basis (0, r)))
  change inner ℂ (swapOp r s (basis (1, r))) (swapOp r s (a (basis (0, r)))) = _ at hinner
  rw [happly, swap_basis] at hinner
  simpa [swapIndex] using hinner.symm

def phaseFlip (r : ℕ) : H ≃ₗᵢ[ℂ] H :=
  (ℂ ∙ basis (0, r))ᗮ.reflection

theorem phaseFlip_star (r : ℕ) : star (phaseFlip r : Op) = (phaseFlip r : Op) := by
  rw [LinearIsometryEquiv.star_eq_symm]
  rfl

theorem phaseFlip_apply (r : ℕ) (x : H) :
    phaseFlip r x = x - (2 * inner ℂ (basis (0, r)) x) • basis (0, r) := by
  rw [phaseFlip, Submodule.reflection_orthogonal_apply,
    Submodule.reflection_singleton_apply, basis_norm]
  module

@[simp] theorem phaseFlip_basis (r : ℕ) (i : Index) :
    phaseFlip r (basis i) = if i = (0, r) then -basis i else basis i := by
  rw [phaseFlip_apply, basis_inner]
  by_cases h : i = (0, r)
  · subst i; simp; module
  · simp [h, Ne.symm h]

def conjugate (r : ℕ) (a : Op) : Op :=
  (phaseFlip r : Op) * a * (phaseFlip r : Op)

def flippedAlgebra (r : ℕ) : Set Op := conjugate r '' algebra

theorem flipped_zero_mem (r : ℕ) : (0 : Op) ∈ flippedAlgebra r := by
  exact ⟨0, zero_mem, by simp [conjugate]⟩

theorem witness_mem (r : ℕ) : conjugate r shift ∈ flippedAlgebra r :=
  ⟨shift, shift_mem, rfl⟩

theorem witness_norm_le (r : ℕ) : ‖conjugate r shift‖ ≤ 1 := by
  apply ContinuousLinearMap.opNorm_le_bound _ (by norm_num)
  intro x
  change ‖phaseFlip r (shiftIso (phaseFlip r x))‖ ≤ 1 * ‖x‖
  simp only [LinearIsometryEquiv.norm_map, LinearIsometry.norm_map, one_mul, le_refl]

theorem witness_negative (r : ℕ) :
    inner ℂ (basis (1, r)) (conjugate r shift (basis (0, r))) = -1 := by
  simp [conjugate, ContinuousLinearMap.mul_apply, shiftIndex]

theorem witness_positive (r s : ℕ) (hrs : s ≠ r) :
    inner ℂ (basis (1, s)) (conjugate r shift (basis (0, s))) = 1 := by
  simp [conjugate, ContinuousLinearMap.mul_apply, shiftIndex, hrs]

theorem concrete_distance_one (r : ℕ) :
    Metric.hausdorffDist (IccWitness.unitPart algebra)
      (IccWitness.unitPart (flippedAlgebra r)) = 1 := by
  exact IccWitness.two_fiber_hausdorff_eq_one algebra (flippedAlgebra r)
    zero_mem (flipped_zero_mem r) (conjugate r shift) (witness_mem r) (witness_norm_le r)
    (basis (1, r + 1)) (basis (0, r + 1)) (basis (1, r)) (basis (0, r))
    (basis_norm _) (basis_norm _) (basis_norm _) (basis_norm _)
    (fun a ha => common_coefficient a ha (r + 1) r)
    (witness_positive r (r + 1) (by omega)) (witness_negative r)

theorem shift_difference_norm (r : ℕ) : ‖conjugate r shift - shift‖ = 2 := by
  apply le_antisymm
  · have h := norm_sub_le (conjugate r shift) shift
    have hS : ‖shift‖ ≤ 1 := shiftIso.norm_toContinuousLinearMap_le
    linarith [witness_norm_le r]
  · have h := (conjugate r shift - shift).le_opNorm (basis (0, r))
    have heval : (conjugate r shift - shift) (basis (0, r)) =
        -(2 : ℂ) • basis (1, r) := by
      simp [conjugate, shiftIndex]
      module
    rw [heval, basis_norm, mul_one, norm_smul, basis_norm, mul_one] at h
    simpa using h

theorem phaseFlip_difference_norm (r : ℕ) (c : H) :
    ‖phaseFlip r c - c‖ = 2 * ‖c (0, r)‖ := by
  have heq : phaseFlip r c - c = -(2 * inner ℂ (basis (0, r)) c) • basis (0, r) := by
    rw [phaseFlip_apply]
    module
  rw [heq, norm_smul, basis_norm, mul_one, norm_neg, norm_mul]
  simp [basis, lp.inner_single_left]

theorem reference_coefficients_tendsto_zero (c : H) :
    Tendsto (fun r : ℕ => ‖c (0, r)‖) atTop (𝓝 0) := by
  have hc := (lp.hasSum_single (by norm_num : (2 : ℝ≥0∞) ≠ ⊤) c).summable.tendsto_cofinite_zero.norm
  have hinj : Function.Injective (fun r : ℕ => (0, r)) := by
    intro i j h
    exact congrArg Prod.snd h
  simpa [Function.comp_def, Nat.cofinite_eq_atTop, lp.norm_single] using
    hc.comp hinj.tendsto_cofinite

theorem phaseFlip_tendsto_identity (c : H) :
    Tendsto (fun r : ℕ => phaseFlip r c) atTop (𝓝 c) := by
  rw [tendsto_iff_norm_sub_tendsto_zero]
  simp_rw [phaseFlip_difference_norm]
  simpa using (reference_coefficients_tendsto_zero c).const_mul 2

/-- A concrete infinite-dimensional separation of vector-norm convergence
    from the fixed-representation unit-ball Hausdorff metric. -/
theorem arbitrarily_close_vectors_distance_one (c : H) (ε : ℝ) (hε : 0 < ε) :
    ∃ r : ℕ, ‖phaseFlip r c - c‖ < ε ∧
      Metric.hausdorffDist (IccWitness.unitPart algebra)
        (IccWitness.unitPart (flippedAlgebra r)) = 1 := by
  have hlim : Tendsto (fun r : ℕ => 2 * ‖c (0, r)‖) atTop (𝓝 0) := by
    simpa using (reference_coefficients_tendsto_zero c).const_mul 2
  obtain ⟨r, hr⟩ := (hlim.eventually_lt_const hε).exists
  exact ⟨r, by simpa only [phaseFlip_difference_norm] using hr, concrete_distance_one r⟩

#print axioms concrete_distance_one
#print axioms phaseFlip_tendsto_identity
#print axioms algebraBundled
#print axioms shift_difference_norm
#print axioms arbitrarily_close_vectors_distance_one

end IccConcrete
