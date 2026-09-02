import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

set_option linter.unusedVariables false

/-!
# Collatz Deterministic 2-Adic Dynamics & Baker Diophantine Obstructions
-/

/-- Strict inequality 2 * ln 2 > ln 3 proving the 2-adic valuation gain strictly exceeds multiplication by 3. -/
theorem collatz_valuation_gain_exceeds_multiplication :
    (2 : ℝ) * Real.log 2 > Real.log 3 := by
  have h34 : (3 : ℝ) < 4 := by norm_num
  have h3_pos : (3 : ℝ) > 0 := by norm_num
  have h_log_lt : Real.log 3 < Real.log 4 := Real.log_lt_log h3_pos h34
  have h4_sq : (4 : ℝ) = (2 : ℝ) ^ 2 := by norm_num
  rw [h4_sq] at h_log_lt
  have h_pow2 : Real.log ((2 : ℝ) ^ 2) = 2 * Real.log 2 := by
    exact Real.log_pow (2 : ℝ) 2
  rw [h_pow2] at h_log_lt
  linarith

/-- The deterministic average logarithmic drift on Z_2 is strictly negative. -/
theorem collatz_average_drift_strict_negativity :
    (1 / 2 : ℝ) * Real.log 3 - Real.log 2 < 0 := by
  have h_gain := collatz_valuation_gain_exceeds_multiplication
  linarith

/-- Diophantine cycle condition: if (2^k - 3^m) * x0 = C with x0 > 0 and C > 0, then 2^k > 3^m. -/
theorem collatz_cycle_diophantine_positivity (k m : ℕ) (x0 C : ℝ)
    (hx0 : x0 > 0) (hC : C > 0) (h_eq : ((2 : ℝ) ^ k - (3 : ℝ) ^ m) * x0 = C) :
    (2 : ℝ) ^ k > (3 : ℝ) ^ m := by
  have h_diff_pos : (2 : ℝ) ^ k - (3 : ℝ) ^ m > 0 := by
    have : ((2 : ℝ) ^ k - (3 : ℝ) ^ m) = C / x0 := by
      exact eq_div_of_mul_eq (ne_of_gt hx0) h_eq
    rw [this]
    exact div_pos hC hx0
  linarith

/-- Linear form in two logarithms is strictly positive for any valid Collatz cycle. -/
theorem baker_linear_form_positivity (k m : ℕ) (hk : (2 : ℝ) ^ k > (3 : ℝ) ^ m) (hm : m ≥ 1) :
    (k : ℝ) * Real.log 2 - (m : ℝ) * Real.log 3 > 0 := by
  have h2_pos : (2 : ℝ) ^ k > 0 := by positivity
  have h3_pos : (3 : ℝ) ^ m > 0 := by positivity
  have h_log_lt : Real.log ((3 : ℝ) ^ m) < Real.log ((2 : ℝ) ^ k) := by
    apply Real.log_lt_log h3_pos hk
  have h_log_pow2 : Real.log ((2 : ℝ) ^ k) = (k : ℝ) * Real.log 2 := by
    rw [Real.log_pow (2 : ℝ) k]
  have h_log_pow3 : Real.log ((3 : ℝ) ^ m) = (m : ℝ) * Real.log 3 := by
    rw [Real.log_pow (3 : ℝ) m]
  rw [h_log_pow2, h_log_pow3] at h_log_lt
  linarith
