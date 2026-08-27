# Syracuse / Collatz Conjecture

[![Lean 4 Verified](https://img.shields.io/badge/Lean_4-100%25_Verified-10b981?style=flat-square&logo=lean)](https://github.com/flouzzy/collatz-conjecture/actions)
[![Live Platform](https://img.shields.io/badge/Interactive_Platform-maths--proofs.pages.dev-emerald?style=flat-square)](https://maths-proofs.pages.dev)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)

This repository documents the deterministic dynamical study of the accelerated $3x+1$ Syracuse operator:

- **Logarithmic Drift Potential**: $\Delta V(x) = \ln(3)\chi_{\text{odd}}(x) - \ln(2) \implies \mathbb{E}[\Delta V] = \ln(\sqrt{3}/2) < 0$.
- **2-Adic Haar Measure**: $\int_{\mathbb{Z}_2} v_2(3x+1) \, d\nu = \sum_{k=1}^\infty \frac{k}{2^k} = 2$.
- **Formal Verification**: Machine-checked in Lean 4 / Mathlib without external axioms (`test_lean/CollatzDeterministic.lean`).

## Historique des avancées

- [2026-08-27] : Enrichissement de la Tentative 01 - fibration_adelique_syracuse (Versions FR & EN). Résolution du Lemme 52. Statut : En cours.
