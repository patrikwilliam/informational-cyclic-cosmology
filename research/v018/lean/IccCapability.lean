import Mathlib.Analysis.InnerProductSpace.Positive
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic

noncomputable section
namespace IccCapability

variable {H K : Type*}
  [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
  [NormedAddCommGroup K] [InnerProductSpace ℂ K] [CompleteSpace K]

abbrev Op (H : Type*) [NormedAddCommGroup H] [InnerProductSpace ℂ H] := H →L[ℂ] H

def Effect (e : Op H) : Prop := e.IsPositive ∧ (1 - e).IsPositive

def Invariant {G : Type*} (action : G → Op H → Op H) (e : Op H) : Prop :=
  ∀ g, action g e = e

/-- The needed Heisenberg properties. Tensor-extension positivity must be
established for the actual map, not inferred from positivity on a factor. -/
structure Pullback {G : Type*} (oldAction : G → Op H → Op H)
    (newAction : G → Op K → Op K) where
  map : Op K →ₗ[ℂ] Op H
  positive : ∀ e, e.IsPositive → (map e).IsPositive
  unital : map 1 = 1
  covariant : ∀ g e, map (newAction g e) = oldAction g (map e)

variable {G : Type*} {oldAction : G → Op H → Op H}
  {newAction : G → Op K → Op K}

def krausMap {J : Type*} [Fintype J] (v : J → Op H) : Op H →ₗ[ℂ] Op H where
  toFun e := ∑ j, star (v j) * e * v j
  map_add' e f := by simp [mul_add, add_mul, Finset.sum_add_distrib]
  map_smul' z e := by simp [Finset.smul_sum]

theorem kraus_positive {J : Type*} [Fintype J] (v : J → Op H)
    (e : Op H) (he : e.IsPositive) : (krausMap v e).IsPositive := by
  classical
  have hterm : ∀ j, (star (v j) * e * v j).IsPositive := by
    intro j
    exact he.adjoint_conj (v j)
  change (∑ j, star (v j) * e * v j).IsPositive
  induction (Finset.univ : Finset J) using Finset.induction_on with
  | empty => simpa using (ContinuousLinearMap.isPositive_zero (E := H) (𝕜 := ℂ))
  | @insert j s hjs ih =>
    rw [Finset.sum_insert hjs]
    exact (hterm j).add ih

theorem kraus_unital {J : Type*} [Fintype J] (v : J → Op H)
    (hn : ∑ j, star (v j) * v j = 1) : krausMap v 1 = 1 := by
  simpa [krausMap] using hn

/-- Kraus positivity and normalization discharge two operator hypotheses.
The concrete tensor extension, covariance, and Born pairing remain to be
instantiated separately for a particular experiment. -/
def krausPullback {J : Type*} [Fintype J] (v : J → Op H)
    (oldAction newAction : G → Op H → Op H)
    (hn : ∑ j, star (v j) * v j = 1)
    (hc : ∀ g e, krausMap v (newAction g e) = oldAction g (krausMap v e)) :
    Pullback oldAction newAction where
  map := krausMap v
  positive := kraus_positive v
  unital := kraus_unital v hn
  covariant := hc

theorem pullback_effect (L : Pullback oldAction newAction) (e : Op K)
    (he : Effect e) : Effect (L.map e) := by
  refine ⟨L.positive e he.1, ?_⟩
  have hc := L.positive (1 - e) he.2
  simpa only [map_sub, L.unital] using hc

theorem pullback_invariant (L : Pullback oldAction newAction) (e : Op K)
    (he : Invariant newAction e) : Invariant oldAction (L.map e) := by
  intro g
  rw [← L.covariant, he g]

def Capabilities {F : Type*} (action : G → Op H → Op H) (extract : Op H → F) : Set F :=
  {f | ∃ e, Effect e ∧ Invariant action e ∧ extract e = f}

/-- The compatibility equation is the Born-pairing bridge; it is an explicit
hypothesis here, not a formal construction of a partial trace or channel. -/
theorem capability_inclusion {F : Type*} (L : Pullback oldAction newAction)
    (oldExtract : Op H → F) (newExtract : Op K → F)
    (compatible : ∀ e, oldExtract (L.map e) = newExtract e) :
    Capabilities newAction newExtract ⊆ Capabilities oldAction oldExtract := by
  rintro f ⟨e, he, hi, hf⟩
  exact ⟨L.map e, pullback_effect L e he, pullback_invariant L e hi,
    (compatible e).trans hf⟩

theorem finite_povm_pullback {J : Type*} [Fintype J]
    (L : Pullback oldAction newAction) (es : J → Op K)
    (he : ∀ j, Effect (es j) ∧ Invariant newAction (es j))
    (hsum : ∑ j, es j = 1) :
    (∀ j, Effect (L.map (es j)) ∧ Invariant oldAction (L.map (es j))) ∧
      (∑ j, L.map (es j)) = 1 := by
  constructor
  · intro j
    exact ⟨pullback_effect L (es j) (he j).1,
      pullback_invariant L (es j) (he j).2⟩
  · rw [← map_sum, hsum, L.unital]

/-- Mutual simulation suffices for equality; in the retained-resource control
the analytic instantiation is forward and inverse unitary conjugation. -/
theorem reversible_capabilities {F : Type*}
    (L : Pullback oldAction newAction) (R : Pullback newAction oldAction)
    (oldExtract : Op H → F) (newExtract : Op K → F)
    (hL : ∀ e, oldExtract (L.map e) = newExtract e)
    (hR : ∀ e, newExtract (R.map e) = oldExtract e) :
    Capabilities newAction newExtract = Capabilities oldAction oldExtract := by
  exact Set.Subset.antisymm
    (capability_inclusion L oldExtract newExtract hL)
    (capability_inclusion R newExtract oldExtract hR)

theorem strict_inclusion_from_witness {F : Type*} {oldSet newSet : Set F}
    (hsub : newSet ⊆ oldSet) (score : F → ℝ) (bound : ℝ) (witness : F)
    (hw : witness ∈ oldSet) (hbound : ∀ f ∈ newSet, score f ≤ bound)
    (hgap : bound < score witness) : newSet ⊂ oldSet := by
  refine ⟨hsub, ?_⟩
  intro hreverse
  exact (not_lt_of_ge (hbound witness (hreverse hw))) hgap

/-- A rational interval certificate for the scalar comparison at g = k = 1.
The bridge from the Hamiltonian and trace norm to these squares is analytic. -/
theorem squared_gap (x : ℝ) (hx : 1 / 2 ≤ x) (hx' : x ≤ 3 / 4) :
    1 / 80 ≤ x * (1 - x) / 5 - (1 - 4 * x / 5) / 16 := by
  have h := mul_nonneg (sub_nonneg.mpr hx) (sub_nonneg.mpr hx')
  nlinarith

theorem strict_scalar_separation (x y b : ℝ)
    (hx : 1 / 2 ≤ x) (hx' : x ≤ 3 / 4) (hy : 0 ≤ y) (hb : 0 ≤ b)
    (hy2 : y ^ 2 = x * (1 - x) / 5)
    (hb2 : b ^ 2 = (1 - 4 * x / 5) / 16) : b < y := by
  have hg := squared_gap x hx hx'
  by_contra h
  have hby : y ≤ b := le_of_not_gt h
  have hm := mul_nonneg (sub_nonneg.mpr hby) (add_nonneg hb hy)
  nlinarith

def primaryAngle : ℝ := Real.pi * Real.sqrt 5 / 8
def primaryX : ℝ := Real.sin primaryAngle ^ 2

theorem primary_interval : 1 / 2 ≤ primaryX ∧ primaryX ≤ 3 / 4 := by
  have hp := Real.pi_pos
  have hsq := Real.sq_sqrt (by norm_num : (0 : ℝ) ≤ 5)
  have hr := Real.sqrt_nonneg (5 : ℝ)
  have hrlo : (2 : ℝ) ≤ Real.sqrt 5 := by nlinarith
  have hrhi : Real.sqrt 5 ≤ (8 : ℝ) / 3 := by nlinarith
  have hθlo : Real.pi / 4 ≤ primaryAngle := by
    dsimp [primaryAngle]
    nlinarith [mul_nonneg hp.le (sub_nonneg.mpr hrlo)]
  have hθhi : primaryAngle ≤ Real.pi / 3 := by
    dsimp [primaryAngle]
    nlinarith [mul_nonneg hp.le (sub_nonneg.mpr hrhi)]
  have hlo := Real.sin_le_sin_of_le_of_le_pi_div_two
    (by linarith : -(Real.pi / 2) ≤ Real.pi / 4)
    (by linarith : primaryAngle ≤ Real.pi / 2) hθlo
  have hhi := Real.sin_le_sin_of_le_of_le_pi_div_two
    (by linarith : -(Real.pi / 2) ≤ primaryAngle)
    (by linarith : Real.pi / 3 ≤ Real.pi / 2) hθhi
  have htwo := Real.sq_sqrt (by norm_num : (0 : ℝ) ≤ 2)
  have htwo0 := Real.sqrt_nonneg (2 : ℝ)
  have hthree := Real.sq_sin_pi_div_three
  rw [Real.sin_pi_div_four] at hlo
  have hs0 : 0 ≤ Real.sin primaryAngle := by linarith
  have ht0 : 0 ≤ Real.sin (Real.pi / 3) := le_trans hs0 hhi
  dsimp [primaryX]
  constructor
  · nlinarith
  · nlinarith

theorem primary_scalar_gap :
    Real.sqrt (1 - 4 * primaryX / 5) / 4 <
      Real.sqrt (primaryX * (1 - primaryX) / 5) := by
  obtain ⟨hx, hx'⟩ := primary_interval
  apply strict_scalar_separation primaryX _ _ hx hx'
  · exact Real.sqrt_nonneg _
  · positivity
  · apply Real.sq_sqrt
    have hx0 : 0 ≤ primaryX := by linarith
    have hx1 : 0 ≤ 1 - primaryX := by linarith
    positivity
  · rw [div_pow, Real.sq_sqrt (by linarith : 0 ≤ 1 - 4 * primaryX / 5)]
    norm_num

end IccCapability
