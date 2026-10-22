import Mathlib.LinearAlgebra.LinearIndependent.Basic
import Mathlib.Tactic

noncomputable section
namespace IccTickSeparation

variable {K V : Type*} [Field K] [AddCommGroup V] [Module K V]

/-- The independence premise is not a formalized continuum field theorem. -/
theorem span_intersection (e u₁ v₁ u₂ v₂ : V)
    (h : LinearIndependent K ![e, u₁, v₁, u₂, v₂]) :
    Submodule.span K ({e, u₁, v₁} : Set V) ⊓
        Submodule.span K ({e, u₂, v₂} : Set V) =
      Submodule.span K ({e} : Set V) := by
  apply le_antisymm
  · intro x hx
    obtain ⟨a, b, c, h₁⟩ := Submodule.mem_span_triple.mp hx.1
    obtain ⟨d, f, g, h₂⟩ := Submodule.mem_span_triple.mp hx.2
    have heq : ∀ i : Fin 5, (![a, b, c, 0, 0] : Fin 5 → K) i =
        (![d, 0, 0, f, g] : Fin 5 → K) i := by
      apply Fintype.linearIndependent_iffₛ.mp h
      simpa [Fin.sum_univ_succ, add_assoc] using h₁.trans h₂.symm
    have hb : b = 0 := by simpa using heq 1
    have hc : c = 0 := by simpa using heq 2
    apply Submodule.mem_span_singleton.mpr
    exact ⟨a, by simpa [hb, hc] using h₁⟩
  · apply le_inf
    · exact Submodule.span_mono (by intro x hx; simp only [Set.mem_singleton_iff] at hx; simp [hx])
    · exact Submodule.span_mono (by intro x hx; simp only [Set.mem_singleton_iff] at hx; simp [hx])

end IccTickSeparation
