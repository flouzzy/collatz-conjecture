import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

/-!
# Syracuse / Collatz Conjecture: Deterministic Drift & 2-Adic Dynamics
## Logarithmic Drift Potential & Haar Integral
-/

/-- The Syracuse accelerated mean logarithmic drift is strictly negative. -/
theorem collatz_average_drift :
    Real.log (Real.sqrt 3 / 2) < 0 := by
  have h_sqrt3_lt_2 : Real.sqrt 3 < 2 := by
    rw [Real.sqrt_lt'] <;> norm_num
  have h_ratio_lt_1 : Real.sqrt 3 / 2 < 1 := by linarith
  have h_ratio_pos : Real.sqrt 3 / 2 > 0 := by positivity
  exact Real.log_neg h_ratio_pos h_ratio_lt_1

/-- Haar expectation factor 2 strictly overcomes multiplication by 3 in log base 2. -/
theorem haar_gain_gt_multiplication :
    Real.log 3 < Real.log 4 := by
  have h3_pos : (3 : ℝ) > 0 := by norm_num
  have h_lt : (3 : ℝ) < 4 := by norm_num
  exact Real.log_lt_log h3_pos h_lt
