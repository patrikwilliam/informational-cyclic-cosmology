import Mathlib.Analysis.Normed.Operator.Basic
import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.Topology.MetricSpace.HausdorffDistance
import Mathlib.Tactic

namespace IccWitness

open scoped InnerProductSpace

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℂ E]

/-- A unit-vector matrix element is bounded by the operator norm. -/
theorem matrix_element_le (T : E →L[ℂ] E) (u v : E)
    (hu : ‖u‖ = 1) (hv : ‖v‖ = 1) :
    ‖inner ℂ u (T v)‖ ≤ ‖T‖ := by
  calc
    ‖inner ℂ u (T v)‖ ≤ ‖u‖ * ‖T v‖ := norm_inner_le_norm _ _
    _ = ‖T v‖ := by rw [hu, one_mul]
    _ ≤ ‖T‖ * ‖v‖ := T.le_opNorm v
    _ = ‖T‖ := by rw [hv, mul_one]

/-- The two-fiber lower bound in Appendix B, with its matrix-element
    hypotheses explicit. No tensor-product identification is assumed proved. -/
theorem two_fiber_lower_bound (a b : E →L[ℂ] E) (u₀ v₀ u₁ v₁ : E)
    (hu₀ : ‖u₀‖ = 1) (hv₀ : ‖v₀‖ = 1)
    (hu₁ : ‖u₁‖ = 1) (hv₁ : ‖v₁‖ = 1)
    (ha : inner ℂ u₀ (a v₀) = inner ℂ u₁ (a v₁))
    (hb₀ : inner ℂ u₀ (b v₀) = 1)
    (hb₁ : inner ℂ u₁ (b v₁) = -1) :
    1 ≤ ‖b - a‖ := by
  have h₀ := matrix_element_le (b - a) u₀ v₀ hu₀ hv₀
  have h₁ := matrix_element_le (b - a) u₁ v₁ hu₁ hv₁
  simp only [ContinuousLinearMap.sub_apply, inner_sub_right, hb₀, hb₁] at h₀ h₁
  rw [ha] at h₀
  have htri := norm_sub_le
    (1 - inner ℂ u₁ (a v₁)) (-1 - inner ℂ u₁ (a v₁))
  have heq : (1 - inner ℂ u₁ (a v₁)) - (-1 - inner ℂ u₁ (a v₁)) = (2 : ℂ) := by ring
  rw [heq] at htri
  norm_num at htri
  linarith

/-- Intersection with the closed operator-norm unit ball. -/
def unitPart (A : Set (E →L[ℂ] E)) : Set (E →L[ℂ] E) :=
  {a | a ∈ A ∧ ‖a‖ ≤ 1}

theorem unitPart_bounded (A : Set (E →L[ℂ] E)) :
    Bornology.IsBounded (unitPart A) := by
  apply (Metric.isBounded_closedBall (x := (0 : E →L[ℂ] E)) (r := (1 : ℝ))).subset
  intro a ha
  simpa only [Metric.mem_closedBall, dist_zero_right] using ha.2

/-- The paper's unit-ball Hausdorff normalization has upper bound one,
    as soon as both ambient sets contain zero. -/
theorem unitPart_hausdorff_le_one (A B : Set (E →L[ℂ] E))
    (hA : 0 ∈ A) (hB : 0 ∈ B) :
    Metric.hausdorffDist (unitPart A) (unitPart B) ≤ 1 := by
  have hA₀ : (0 : E →L[ℂ] E) ∈ unitPart A := ⟨hA, by simp⟩
  have hB₀ : (0 : E →L[ℂ] E) ∈ unitPart B := ⟨hB, by simp⟩
  apply Metric.hausdorffDist_le_of_mem_dist (by norm_num)
  · intro a ha
    exact ⟨0, hB₀, by simpa using ha.2⟩
  · intro b hb
    exact ⟨0, hA₀, by simpa using hb.2⟩

/-- Exact distance-one conclusion from an actual unit-ball witness with
    opposite coefficients and a common coefficient on the comparison set. -/
theorem two_fiber_hausdorff_eq_one (A B : Set (E →L[ℂ] E))
    (hA : 0 ∈ A) (hB : 0 ∈ B) (b : E →L[ℂ] E)
    (hbB : b ∈ B) (hb_norm : ‖b‖ ≤ 1) (u₀ v₀ u₁ v₁ : E)
    (hu₀ : ‖u₀‖ = 1) (hv₀ : ‖v₀‖ = 1)
    (hu₁ : ‖u₁‖ = 1) (hv₁ : ‖v₁‖ = 1)
    (hcommon : ∀ a ∈ A, inner ℂ u₀ (a v₀) = inner ℂ u₁ (a v₁))
    (hb₀ : inner ℂ u₀ (b v₀) = 1)
    (hb₁ : inner ℂ u₁ (b v₁) = -1) :
    Metric.hausdorffDist (unitPart A) (unitPart B) = 1 := by
  apply le_antisymm (unitPart_hausdorff_le_one A B hA hB)
  have hAne : (unitPart A).Nonempty := ⟨0, hA, by simp⟩
  have hBne : (unitPart B).Nonempty := ⟨0, hB, by simp⟩
  have hfin := Metric.hausdorffEdist_ne_top_of_nonempty_of_bounded
    hBne hAne (unitPart_bounded B) (unitPart_bounded A)
  have hinf : 1 ≤ Metric.infDist b (unitPart A) := by
    apply (Metric.le_infDist hAne).mpr
    intro a ha
    simpa only [dist_eq_norm] using
      two_fiber_lower_bound a b u₀ v₀ u₁ v₁ hu₀ hv₀ hu₁ hv₁
        (hcommon a ha.1) hb₀ hb₁
  have hle := Metric.infDist_le_hausdorffDist_of_mem
    (show b ∈ unitPart B from ⟨hbB, hb_norm⟩) hfin
  rw [Metric.hausdorffDist_comm] at hle
  exact hinf.trans hle

#print axioms two_fiber_lower_bound
#print axioms two_fiber_hausdorff_eq_one

end IccWitness
