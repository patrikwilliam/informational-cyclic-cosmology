import IccConcrete
import Mathlib.Data.Nat.Factorization.Basic

noncomputable section
namespace IccArithmetic

open IccConcrete

/-- The paper's integer label for a level and an odd fiber. -/
def label (i : Index) : ℕ := 2 ^ i.1 * (2 * i.2 + 1)

theorem label_positive (i : Index) : 0 < label i := by
  dsimp [label]
  positivity

theorem label_exponent (i : Index) : (label i).factorization 2 = i.1 := by
  have hodd : ¬2 ∣ 2 * i.2 + 1 := by omega
  rw [label, Nat.factorization_mul (by positivity) (by omega), Finsupp.add_apply,
    Nat.factorization_pow_self Nat.prime_two,
    Nat.factorization_eq_zero_of_not_dvd hodd, add_zero]

theorem label_injective : Function.Injective label := by
  intro i j h
  have hk := congrArg (fun n : ℕ => n.factorization 2) h
  simp only [label_exponent] at hk
  apply Prod.ext hk
  dsimp [label] at h
  rw [hk] at h
  have hm := Nat.eq_of_mul_eq_mul_left (by positivity : 0 < 2 ^ j.1) h
  omega

theorem label_surjective_positive (n : ℕ) (hn : 0 < n) : ∃ i : Index, label i = n := by
  obtain ⟨k, m, hm, hn'⟩ := Nat.exists_eq_two_pow_mul_odd hn.ne'
  obtain ⟨r, hr⟩ := hm
  refine ⟨(k, r), ?_⟩
  have heq : m = 2 * r + 1 := by omega
  simp only [label]
  rw [← heq]
  exact hn'.symm

def positiveLabels : Index ≃ {n : ℕ // 0 < n} :=
  Equiv.ofBijective (fun i => ⟨label i, label_positive i⟩)
    ⟨fun i j h => label_injective (congrArg Subtype.val h), by
      intro n
      obtain ⟨i, hi⟩ := label_surjective_positive n.val n.property
      exact ⟨i, Subtype.ext hi⟩⟩

theorem label_shift (i : Index) : label (shiftIndex i) = 2 * label i := by
  simp only [label, shiftIndex, pow_succ]
  ring

theorem label_flipped_coordinate (r : ℕ) : label (0, r) = 2 * r + 1 := by
  simp [label]

#print axioms positiveLabels
#print axioms label_shift

end IccArithmetic
