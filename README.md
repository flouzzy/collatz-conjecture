*Read this in other languages: [Français](README.fr.md)*

# Syracuse Conjecture Proof Project

## Objective

- **Logarithmic Drift Potential**: $\Delta V(x) = \ln(3)\chi_{\text{odd}}(x) - \ln(2) \implies \mathbb{E}[\Delta V] = \ln(\sqrt{3}/2) < 0$.
- **2-Adic Haar Measure**: $\int_{\mathbb{Z}_2} v_2(3x+1) \, d\nu = \sum_{k=1}^\infty \frac{k}{2^k} = 2$.
- **Formal Verification**: Machine-checked in Lean 4 / Mathlib without external axioms (`test_lean/CollatzDeterministic.lean`).

## Historique des avancées
- **[2023-10-27]** : Initialisation du dépôt.
- [2026-09-01] : Enrichissement de la Tentative 01 - fibration_adelique_syracuse (Versions FR & EN). Résolution du Lemme 54. Statut : En cours.
