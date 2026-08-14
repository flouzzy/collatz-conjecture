# Blueprint Formel : Conjecture de Collatz / Syracuse (3x+1)

## 1. Énoncé Formel
Soit $T : \mathbb{N}_{>0} \to \mathbb{N}_{>0}$ défini par :
$$T(n) = \begin{cases} n/2 & \text{si } n \text{ est pair} \\ (3n+1)/2 & \text{si } n \text{ est impair} \end{cases}$$
Pour tout entier $n \ge 1$, il existe $k \in \mathbb{N}$ tel que $T^k(n) = 1$.

## 2. Déconstruction des Barrières
1. **Théorème de Tao (2019) :** Pour toute fonction $f(N) \to \infty$ arbitrairement lente, presque tous les entiers $N \in \mathbb{N}$ (au sens de la densité logarithmique) vérifient $\min_{k \ge 0} T^k(N) < f(N)$.
2. **Indécidabilité des Systèmes de Collatz Généralisés (Conway 1972) :** La généralisation des fonctions affines par morceaux modulo $m$ est indécidable au sens de Turing.
3. **Obstacle de la Mesure 2-adique :** La convergence sous la mesure de Haar sur $\mathbb{Z}_2$ ne garantit pas la convergence sur le sous-ensemble discret de mesure nulle $\mathbb{N} \subset \mathbb{Z}_2$.

## 3. Redressement Méthodologique
* Formaliser l'opérateur $T$ et ses itérés en Lean 4.
* Prouver formellement l'absence de cycles non triviaux de petite longueur (cycles de longueur $1, 2, \dots, 68$ via le théorème de Simons-de Weger).
* Formaliser les extensions $2$-adiques continues sur $\mathbb{Z}_2$.

## 4. Graphe de Décomposition Modulaire (Lean 4)
- [ ] Définition de l'application de Collatz $T : \mathbb{N} \to \mathbb{N}$ et de la relation d'accessibilité inductive.
- [ ] Preuve formelle de l'attractivité du cycle trivial $\{1, 2\}$.
- [ ] Preuve formelle de l'absence de 1-cycles non triviaux ($3n+1 = 2^k n$).
- [ ] Formalisation des temps d'arrêt et de l'arbre généalogique inverse de Syracuse.
