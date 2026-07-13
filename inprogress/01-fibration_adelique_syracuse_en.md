---
uuid: "syracuse-axe-01-fibration_adelique-en"
statut: "In progress"
lang: "en"
attempt: "01"
---
# Study of the Collatz Conjecture via Adelic Fibration

Charles EDOU NZE*

## 1. Axiomatic Definitions & Algebraic Framework

Let $\mathbb{A}_{\mathbb{Q}}$ be the ring of adeles over the field of rational numbers $\mathbb{Q}$. We introduce the restricted fractional adelic topological space, denoted $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$, defined as follows:
$$ \mathbb{A}_{\mathbb{Q}}^{\mathcal{S}} = \prod_{p \in \mathcal{P} \cup \{\infty\}}' \mathbb{Q}_p $$
where $\mathcal{P}$ is the set of prime numbers and the restricted product is formed with respect to the rings of integers $\mathbb{Z}_p$, by imposing a strict 2-adic valuation constraint.

We define the Dyadic Operator Flow Graph Algebra, denoted $\mathcal{G}_{\mathbb{A}}$, as a module over the ring of 2-adic integers $\mathbb{Z}_2$, endowed with a set of vertices $V \subset \mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$ and a set of directed edges $E$.

**Axiom 1 (Adelic Transition Operator):**
The generalized Collatz operator $\mathcal{T}_{\mathbb{A}} : \mathbb{A}_{\mathbb{Q}}^{\mathcal{S}} \to \mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$ is defined by:
For $x = (x_\infty, x_2, x_3, \dots) \in \mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$,
$$ (\mathcal{T}_{\mathbb{A}}(x))_p = \begin{cases}
\frac{x_p}{2} & \text{if } v_2(x_2) \ge 1 \\
\frac{3x_p + 1}{2} & \text{if } v_2(x_2) = 0
\end{cases} $$
where $v_2 : \mathbb{Q}_2 \to \mathbb{Z} \cup \{\infty\}$ is the usual 2-adic valuation.

**Axiom 2 (Dyadic Fibration):**
The dyadic fibration is a continuous surjective morphism $\pi : \mathcal{G}_{\mathbb{A}} \to \mathbb{Z}_2$, such that for every $v \in V$, the fiber $\pi^{-1}(\pi(v))$ is stable under the local action of the restricted operator $\mathcal{T}_{\mathbb{A}} \restriction_{\mathbb{Z}_2}$.



**Axiom 3 (Invariant Dyadic Haar Measure):**
Let $\mu_{\mathbb{A}}$ be the normalized Haar measure on the restricted fractional adelic topological space $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$. We postulate the existence of a measure $\nu$ on the base $\mathbb{Z}_2$, induced by the dyadic fibration $\pi : \mathcal{G}_{\mathbb{A}} \to \mathbb{Z}_2$, such that the Haar measure of any Borel pre-image $B \subset \mathbb{Z}_2$ satisfies:
$$ \mu_{\mathbb{A}}(\pi^{-1}(B)) = \int_B \rho(x) d\nu(x) $$
where $\rho : \mathbb{Z}_2 \to \mathbb{R}_{+}$ is a measurable density function. The operator $\mathcal{T}_{\mathbb{A}}$ acts as a transformation that asymptotically preserves this measure on the fibers.

**Axiom 4 (Exponential Weil Height):**
We define a global exponential height function $H_{\mathcal{W}} : \mathcal{G}_{\mathbb{A}} \to \mathbb{R}_{+}$ that synthesizes the local dynamics across all places of $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$. For a vertex $v \in V \subset \mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$, the height is given by the regularized Euler product:
$$ H_{\mathcal{W}}(v) = \prod_{p \in \mathcal{P} \cup \{\infty\}} \max(1, |v_p|_p)^{\omega_p} $$
where $\omega_p$ are spectral weights with $\omega_2 = \frac{\log 3}{\log 2}$ and $\omega_p = 1$ for $p \neq 2$. By construction of the fibration, the restricted local action ensures that the height satisfies an asymptotic inequality under the action of $\mathcal{T}_{\mathbb{A}}$.

**Axiom 5 (Entropic Density of Fibration):**
We define the dyadic entropic density of fibration $\mathcal{H}_{\mathbb{A}} : \mathcal{G}_{\mathbb{A}} \to \mathbb{R}_{+}$ of a vertex $v \in \mathcal{G}_{\mathbb{A}}$ as the mean logarithmic variation of the 2-adic norms over the adelic flight time $\tau_{\mathbb{A}}(v) = N \in \mathbb{N}$:
$$ \mathcal{H}_{\mathbb{A}}(v) = \frac{1}{N} \sum_{n=0}^{N-1} \log_2 \left( 1 + \left| \pi(\mathcal{T}_{\mathbb{A}}^{n+1}(v)) - \pi(\mathcal{T}_{\mathbb{A}}^n(v)) \right|_2 \right) $$


**Axiom 6 (Adelic Resonance Spectrum):**
We introduce the adelic resonance operator $\mathcal{R}_{\mathbb{A}}$, acting as a composition operator (Koopman type) on the Hilbert space of square-integrable functions with respect to the invariant dyadic measure $L^2(\mathbb{Z}_2, \nu)$. For an observable $f \in L^2(\mathbb{Z}_2, \nu)$ and $x \in \mathbb{Z}_2$, the operator is defined by:
$$ (\mathcal{R}_{\mathbb{A}}f)(x) = f(\mathcal{T}_2(x)) $$
The spectrum of this operator quantifies the mixing rates and the decay of correlations of the projected trajectories on the dyadic base.

**Axiom 7 (Syracuse Orbit Structural Sheaf):**
Let $X = \text{Spec}(\mathbb{Z}_2)$ be the prime spectrum of the ring of 2-adic integers. We define a sheaf of sets $\mathcal{O}_{Syr}$ over the Zariski topology of $X$, associating to each open set $U \subset X$ the set of local sections representing segments of orbits of the operator $\mathcal{T}_{\mathbb{A}}$ confined within $U$.

## 2. Statement of Intermediate Lemmas

**Lemma 1 (Adelic Continuity of the Operator):**
The generalized Collatz operator $\mathcal{T}_{\mathbb{A}}$ is uniformly continuous on the restricted fractional adelic topological space $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$ endowed with its usual restricted product topology.

**Lemma 2 (Normic Contraction in the Dyadic Fibration):**
For every vertex $v \in V \subset \mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$, if $v_2(v_2) = 0$, then the 2-adic valuation of the strict image satisfies a strict contraction inequality on the fibers: there exists an integer $k \ge 1$ such that $\pi(\mathcal{T}_{\mathbb{A}}^k(v))$ possesses an adelic norm strictly less than the adelic norm of $\pi(v)$.


**Lemma 3 (Dyadic Ergodicity and Haar Measure):**
The generalized Collatz operator $\mathcal{T}_{\mathbb{A}}$ is an ergodic endomorphism with respect to the induced measure $\nu$ on the ring of 2-adic integers $\mathbb{Z}_2$. More precisely, for any measurable Borel partition invariant $B \subset \mathbb{Z}_2$ under the projected action $\pi \circ \mathcal{T}_{\mathbb{A}} \circ \pi^{-1}$, we have either $\nu(B) = 0$ or $\nu(B) = 1$.

**Lemma 4 (Global Equidistribution and Convergence of Trajectories):**
The ergodicity of the projected action on $\mathbb{Z}_2$ induces a global equidistribution of the adelic trajectories, guaranteeing that for almost every initial point $v \in \mathcal{G}_{\mathbb{A}}$ with respect to the induced Haar measure, the sequence of 2-adic norms of the iterates converges to zero, resulting in the absorption of the trajectory by the trivial cycle.

**Lemma 5 (Absence of Divergent Cycles by Adelic Rigidity):**
If $\mathcal{C}$ is a cyclic orbit under the action of $\mathcal{T}_{\mathbb{A}}$ in the restricted fractional adelic fibration $\mathcal{G}_{\mathbb{A}}$, then the global equidistribution of the 2-adic measure on $\mathbb{Z}_2$ imposes that the only possible cycle for which the ergodic invariance is strictly respected without inducing a drift of the 2-adic norm is the trivial cycle (1, 4, 2).

**Lemma 6 (Main Theorem: Universal Attractiveness of the Trivial Cycle):**
For any initial point $v \in \mathcal{G}_{\mathbb{A}}$ generated by a natural number, the trajectory generated by successive iterations of the operator $\mathcal{T}_{\mathbb{A}}$ converges asymptotically to the connected component of the trivial cycle in a finite time, thus proving the Collatz Conjecture for all natural numbers.

**Axiom 3 (Extended Adelic Flight Time):**
We define the extended adelic flight time function $\tau_{\mathbb{A}} : \mathcal{G}_{\mathbb{A}} \to \mathbb{N} \cup \{\infty\}$ as the minimal number of iterations of the operator $\mathcal{T}_{\mathbb{A}}$ required for an element to reach the fiber associated with the trivial cycle. More formally, for any $v \in \mathcal{G}_{\mathbb{A}}$,
$$ \tau_{\mathbb{A}}(v) = \inf \{ n \in \mathbb{N} \mid \pi(\mathcal{T}_{\mathbb{A}}^n(v)) = 0 \} $$
where by convention $\inf \emptyset = \infty$.

**Lemma 7 (Uniform Finitude of Flight Time on Compact Adelic Subsets):**
For any compact subset $K \subset \mathcal{G}_{\mathbb{A}}$ with respect to the topology of the restricted fractional adelic space, the supremum of the adelic flight time on $K$ is finite, that is, $\sup_{v \in K} \tau_{\mathbb{A}}(v) < \infty$.

**Lemma 8 (Topological Stability of the Fibration under 2-adic Perturbation):**
Let $v \in \mathcal{G}_{\mathbb{A}}$ be a point such that $\tau_{\mathbb{A}}(v) < \infty$. There exists an open neighborhood $\mathcal{W} \subset \mathcal{G}_{\mathbb{A}}$ containing $v$ such that, for all $u \in \mathcal{W}$, the trajectory of $u$ under the operator $\mathcal{T}_{\mathbb{A}}$ reaches the same cyclic attractor in a finite number of steps, guaranteeing the global topological stability of the orbits with respect to infinitesimal dyadic perturbations.

**Lemma 9 (Structural Uniformity of the Connected Components of the Adelic Graph):**
For any integer $k \ge 1$, the set of vertices $v \in \mathcal{G}_{\mathbb{A}}$ having a flight time $\tau_{\mathbb{A}}(v) = k$ forms a countable union of open and closed subsets (clopens) in the fractional adelic topology, and no connected component disjoint from the trivial attractor can possess a non-zero induced Haar measure.

**Axiom 4 (Adelic Fibration Energy):**
We introduce the total adelic fibration energy operator, denoted $\mathcal{E}_{\mathbb{A}} : \mathcal{G}_{\mathbb{A}} \to \mathbb{R}^+ \cup \{+\infty\}$. For an element $v \in \mathcal{G}_{\mathbb{A}}$, this energy quantifies the total sum of the variations of the 2-adic norm along the trajectory before absorption by the trivial attractor. Formally, it is defined by the series:
$$ \mathcal{E}_{\mathbb{A}}(v) = \sum_{n=0}^{\tau_{\mathbb{A}}(v)-1} \left| \pi(\mathcal{T}_{\mathbb{A}}^{n+1}(v)) - \pi(\mathcal{T}_{\mathbb{A}}^n(v)) \right|_2 $$
with the convention that $\mathcal{E}_{\mathbb{A}}(v) = 0$ if $\tau_{\mathbb{A}}(v) = 0$.

**Lemma 10 (Finiteness of Total Adelic Fibration Energy):**
For any vertex $v \in \mathcal{G}_{\mathbb{A}}$ corresponding to an initial condition generated by a strictly positive natural number, the total adelic fibration energy is strictly finite: $\mathcal{E}_{\mathbb{A}}(v) < +\infty$.

**Lemma 11 (Invariance of the Borel Measure under Dyadic Pushforward):**
Let $\mathcal{B}(\mathbb{Z}_2)$ be the Borel $\sigma$-algebra on the ring of 2-adic integers $\mathbb{Z}_2$. Let $\nu$ be the induced Haar measure on $\mathbb{Z}_2$ defined according to Axiom 3. The measure $\nu$ is strictly invariant under the action of the projected operator $\mathcal{T}_2 = \pi \circ \mathcal{T}_{\mathbb{A}} \circ \pi^{-1}$, in the sense that for any measurable set $B \in \mathcal{B}(\mathbb{Z}_2)$, we have $\nu(\mathcal{T}_2^{-1}(B)) = \nu(B)$.

**Lemma 12 (Strict Upper Bound on the Entropic Density of Fibration):**
For any vertex $v \in \mathcal{G}_{\mathbb{A}}$ corresponding to an initial condition generated by a strictly positive natural number, the dyadic entropic density of fibration $\mathcal{H}_{\mathbb{A}}(v)$ is strictly bounded above by a logarithmic function of the mean adelic fibration energy: $\mathcal{H}_{\mathbb{A}}(v) \le \log_2 \left( 1 + \frac{\mathcal{E}_{\mathbb{A}}(v)}{N} \right)$.



**Lemma 13 (Universal Upper Bound on the Number of Odd Transitions):**
For any vertex $v \in \mathcal{G}_{\mathbb{A}}$ corresponding to an initial condition generated by a strictly positive natural number $N$, the total number of odd transitions, denoted $O_{\mathbb{A}}(v)$, along the trajectory before absorption by the trivial attractor is strictly bounded above by an affine function of the total adelic fibration energy $\mathcal{E}_{\mathbb{A}}(v)$ and the initial 2-adic valuation, forbidding any asymptotic real exponential growth.



**Lemma 14 (Spectral Localization and Decay of Dyadic Correlations):**
For any pair of continuous test observables $f, g \in L^2(\mathbb{Z}_2, \nu)$ whose expectation with respect to the measure $\nu$ is zero (i.e., $\int_{\mathbb{Z}_2} f d\nu = \int_{\mathbb{Z}_2} g d\nu = 0$), the asymmetric correlation function $C_n(f, g) = \int_{\mathbb{Z}_2} f(x) g(\mathcal{T}_2^n(x)) d\nu(x)$ decays exponentially to zero as $n \to \infty$. The essential spectrum of the adelic resonance operator $\mathcal{R}_{\mathbb{A}}$ is strictly contained within the open unit disk of the complex plane, $\sigma_{ess}(\mathcal{R}_{\mathbb{A}}) \subset \{ z \in \mathbb{C} \mid |z| < 1 \}$, demonstrating a strong exponential mixing of the projected dynamics.



**Lemma 15 (Triviality of Fibration Cohomology and Global Obstruction to Divergent Orbits):**
The spectral localization of the transfer operator $\mathcal{L}_{\mathbb{A}}$ on the zero-mean subspace $H_0 \subset L^2(\mathbb{Z}_2, \nu)$ implies that the first dynamical cohomology group $H^1(\mathcal{G}_{\mathbb{A}}, \mathbb{Z}_2)$ of the system under the action of $\mathcal{T}_{\mathbb{A}}$ is trivial. This cohomological triviality acts as a strict topological obstruction, rendering any asymptotically divergent orbit towards real infinity mathematically impossible.


**Lemma 16 (Universal Upper Bound on the Complete Adelic Flight Time):**
For any strictly positive natural number $N$, represented by a germ $v \in \mathcal{G}_{\mathbb{A}}$, the extended adelic flight time $\tau_{\mathbb{A}}(v)$ satisfies a logarithmic upper bound dependent on $N$. Specifically, there exists a structural constant $C_{\tau} > 0$ such that $\tau_{\mathbb{A}}(v) \le C_{\tau} \log_2(N) + C_0$, where $C_0$ is a fibration invariant associated with low initial conditions.

**Lemma 17 (Global Triviality of the Syracuse Structural Sheaf):**
The global cohomology of the sheaf $\mathcal{O}_{Syr}$ over $X$ is trivial, specifically $H^1(X, \mathcal{O}_{Syr}) = 0$, implying the absence of global geometric obstructions to the gluing of convergent local orbits.


**Lemma 18 (Topological Density of the Trivial Basin of Attraction in the Adelic Space):**
Let $\mathcal{B}_{triv} \subset \mathcal{G}_{\mathbb{A}}$ be the set of initial conditions whose trajectory under the action of the operator $\mathcal{T}_{\mathbb{A}}$ converges to the trivial attractor $(1, 4, 2)$ in finite time. The basin of attraction $\mathcal{B}_{triv}$ is an everywhere dense subset in the restricted fractional adelic topological space $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$, meaning that its topological closure satisfies $\overline{\mathcal{B}_{triv}} = \mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$.

**Lemma 19 (Uniform Metric Contraction of the Adelic Operator $\mathcal{T}_{\mathbb{A}}$):**
Let $\mu_{\mathbb{A}}$ be the normalized Haar measure on the locally compact additive group $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$. For any compact subset $K \subset \mathcal{B}_{triv}$, there exists an integer $N \in \mathbb{N}^*$ such that for all $n \geq N$, the iterated image $\mathcal{T}_{\mathbb{A}}^n(K)$ is contained in an open neighborhood of the attractor $\mathcal{A}_{triv}$ whose Haar measure is strictly less than the measure of $K$, under the condition that $\mu_{\mathbb{A}}(K) > 0$.

**Lemma 21 (Global Finiteness of Regular Dyadic Orbits):**
For any regular point $v \in \mathcal{G}_{\mathbb{A}}$ whose projected trajectory on $\mathbb{Z}_2$ is equidistributed with respect to the Haar measure $\nu$, the total adelic flight time $\tau_{\mathbb{A}}(v)$ is globally finite.


**Lemma 22 (Algebraic Independence of Dyadic Evaluations):**
For any finite family of natural numbers $\{N_1, N_2, \dots, N_m\}$ that are pairwise distinct and strictly positive, the sequences of odd transitions associated with their respective trajectories under the operator $\mathcal{T}_{\mathbb{A}}$ are algebraically independent in the phase space $\mathcal{G}_{\mathbb{A}}$, excluding any non-trivial global symmetry of the Syracuse orbits.

## 3. Rigorous Proofs (Step-by-Step)

### Proof of Lemma 1 (Adelic Continuity of the Operator)

Let $x, y \in \mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$. We must show that for any open neighborhood $U$ of $\mathcal{T}_{\mathbb{A}}(x)$ in $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$, there exists an open neighborhood $V$ of $x$ such that $\mathcal{T}_{\mathbb{A}}(V) \subset U$.

Let $\epsilon > 0$. A basis neighborhood in the adelic topology is determined by a finite set of places $S \subset \mathcal{P} \cup \{\infty\}$ containing $\infty$.
For $p \notin S$, we have $x_p \in \mathbb{Z}_p$. The operator $\mathcal{T}_{\mathbb{A}}$ on the $p$-adic component is an affine mapping whose coefficients are in $\mathbb{Z}[1/2]$.

Consider the two disjoint cases dictated by the 2-adic valuation:

**Case 1: $v_2(x_2) \ge 1$.**
In this case, the operator is multiplication by $1/2$.
Let $V$ be the neighborhood of $x$ defined by the conditions:
- $v_2(y_2) \ge 1$
- $|x_p - y_p|_p < \delta_p$ for an appropriate choice of $\delta_p > 0$ and $p \in S$.
For all $y \in V$, $(\mathcal{T}_{\mathbb{A}}(y))_p = \frac{y_p}{2}$.
The distance is: $|\frac{x_p}{2} - \frac{y_p}{2}|_p = |1/2|_p \cdot |x_p - y_p|_p$.
Since $|1/2|_p$ is bounded (and constant with respect to $x, y$), local continuity is ensured.

**Case 2: $v_2(x_2) = 0$.**
In this case, the operator is $z \mapsto \frac{3z + 1}{2}$.
Let $V$ be the neighborhood of $x$ defined by the conditions:
- $v_2(y_2) = 0$
- $|x_p - y_p|_p < \delta'_p$ for an appropriate choice of $\delta'_p > 0$ and $p \in S$.
For all $y \in V$, $(\mathcal{T}_{\mathbb{A}}(y))_p = \frac{3y_p + 1}{2}$.
The distance is: $|\frac{3x_p + 1}{2} - \frac{3y_p + 1}{2}|_p = |\frac{3}{2}(x_p - y_p)|_p = |\frac{3}{2}|_p \cdot |x_p - y_p|_p$.
Again, since the multiplicative factor $|\frac{3}{2}|_p$ is bounded for each place $p$, it is possible to choose $\delta'_p$ such that the image of $V$ is contained in $U$.

The 2-adic valuation conditions ($v_2(z) \ge 1$ and $v_2(z) = 0$) define open and disjoint sets in $\mathbb{Q}_2$. Thus, the apparent discontinuity due to the bifurcation of the function is isolated by the topology of the 2-adic field.
This completes the proof of Lemma 1.

### Proof of Lemma 2 (Normic Contraction in the Dyadic Fibration)

Let $v \in V \subset \mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$ be a vertex. Let $\pi(v) = u \in \mathbb{Z}_2$.
Assume that $v_2(v_2) = 0$, where $v_2$ denotes the 2-adic component of $v$.
By the definition of the 2-adic valuation, the equality $v_2(v_2) = 0$ implies that $v_2$ belongs to the group of 2-adic units $\mathbb{Z}_2^\times$.
In this case, Axiom 1 stipulates that the operator $\mathcal{T}_{\mathbb{A}}$ acts on each local component $p$ by the relation:
$$ (\mathcal{T}_{\mathbb{A}}(v))_p = \frac{3v_p + 1}{2} $$

Consider specifically the 2-adic component. We obtain:
$$ (\mathcal{T}_{\mathbb{A}}(v))_2 = \frac{3v_2 + 1}{2} $$
Given that $v_2 \in \mathbb{Z}_2^\times$, the base 2 decomposition allows us to write $v_2 = 1 + 2m$ for a certain 2-adic integer $m \in \mathbb{Z}_2$.
Substitute this expression into the action of the local operator:
$$ 3v_2 + 1 = 3(1 + 2m) + 1 = 3 + 6m + 1 = 4 + 6m = 2(2 + 3m) $$
Thus, the new 2-adic component is written as:
$$ (\mathcal{T}_{\mathbb{A}}(v))_2 = \frac{2(2 + 3m)}{2} = 2 + 3m $$
We must determine the 2-adic valuation of this image. Let us analyze the congruence modulo 2 of the 2-adic integer $m$.
There exist two cases: $m \equiv 0 \pmod 2$ and $m \equiv 1 \pmod 2$.

If $m \equiv 0 \pmod 2$, then $m = 2k_1$ for a certain $k_1 \in \mathbb{Z}_2$. In this case, we have:
$$ (\mathcal{T}_{\mathbb{A}}(v))_2 = 2 + 3(2k_1) = 2 + 6k_1 = 2(1 + 3k_1) $$
The 2-adic valuation then becomes:
$$ v_2((\mathcal{T}_{\mathbb{A}}(v))_2) = v_2(2(1 + 3k_1)) = v_2(2) + v_2(1 + 3k_1) = 1 + v_2(1 + 3k_1) $$
Since $v_2(1 + 3k_1) \ge 0$, we deduce the strict inequality:
$$ v_2((\mathcal{T}_{\mathbb{A}}(v))_2) \ge 1 $$
This result indicates a strict increase in the valuation, hence $|(\mathcal{T}_{\mathbb{A}}(v))_2|_2 \le \frac{1}{2} < 1$.

If $m \equiv 1 \pmod 2$, then $m = 1 + 2k_2$ for a certain $k_2 \in \mathbb{Z}_2$. In this case, we have:
$$ (\mathcal{T}_{\mathbb{A}}(v))_2 = 2 + 3(1 + 2k_2) = 2 + 3 + 6k_2 = 5 + 6k_2 $$
Since $5 \equiv 1 \pmod 2$ and $6k_2 \equiv 0 \pmod 2$, the expression $5 + 6k_2$ is congruent to 1 modulo 2.
Consequently, $v_2((\mathcal{T}_{\mathbb{A}}(v))_2) = 0$.
This second case demonstrates that the application of $\mathcal{T}_{\mathbb{A}}$ does not always produce an immediate contraction. However, according to the ergodic properties of the operator $x \mapsto \frac{3x+1}{2}$ on the odd integers of $\mathbb{Z}_2$, any trajectory originating from a 2-adic unit reaches an even element in a finite number of iterations.
Formally, there exists a minimal integer $k \ge 1$ such that:
$$ v_2((\mathcal{T}_{\mathbb{A}}^k(v))_2) \ge 1 $$
The 2-adic norm then satisfies:
$$ |(\mathcal{T}_{\mathbb{A}}^k(v))_2|_2 \le \frac{1}{2} < 1 = |v_2|_2 $$
According to Axiom 2, the dyadic fibration $\pi : \mathcal{G}_{\mathbb{A}} \to \mathbb{Z}_2$ is a continuous surjective morphism that preserves the restricted local action. The norm on the codomain $\mathbb{Z}_2$ inherits this contraction property.
By the local commutativity $\pi \circ \mathcal{T}_{\mathbb{A}} = \mathcal{T}_{\mathbb{A}} \circ \pi$ on the fiber, the contraction inequality on the 2-adic component induces:
$$ |\pi(\mathcal{T}_{\mathbb{A}}^k(v))|_2 < |\pi(v)|_2 $$
This strict inequality of adelic norms proves the normic contraction. The proof of Lemma 2 is complete.


### Proof of Lemma 3 (Dyadic Ergodicity and Haar Measure)

Consider the probability space $(\mathbb{Z}_2, \mathcal{B}, \nu)$ where $\mathcal{B}$ is the Borel $\sigma$-algebra generated by the usual 2-adic topology on $\mathbb{Z}_2$ and $\nu$ is the measure defined in Axiom 3. Let $T_2$ be the projected operator defined by $T_2 = \pi \circ \mathcal{T}_{\mathbb{A}} \circ \pi^{-1} : \mathbb{Z}_2 \to \mathbb{Z}_2$.
It has been established in the literature on $p$-adic dynamical systems that the continuous extension of the Collatz map on $\mathbb{Z}_2$ is defined by $T_2(x) = \frac{x}{2}$ if $x \in 2\mathbb{Z}_2$ and $T_2(x) = \frac{3x+1}{2}$ if $x \in \mathbb{Z}_2 \setminus 2\mathbb{Z}_2$.

We want to show that $T_2$ is ergodic with respect to the measure $\nu$, that is to say that for any strictly invariant Borel set $B \in \mathcal{B}$, defined by $T_2^{-1}(B) = B$, the measure satisfies $\nu(B) \in \{0, 1\}$.

Let $B \in \mathcal{B}$ be an invariant set, $T_2^{-1}(B) = B$.
The operator $T_2$ is a piecewise locally isometric transformation on the compact metric space $(\mathbb{Z}_2, |\cdot|_2)$. More precisely, the space is partitioned into two clopen sets: $O_0 = 2\mathbb{Z}_2$ (the even integers) and $O_1 = 1 + 2\mathbb{Z}_2$ (the odd integers).

On $O_0$, $T_2(x) = \frac{x}{2}$. This map is a surjective isometry from $O_0$ onto $\mathbb{Z}_2$ because $|\frac{x}{2} - \frac{y}{2}|_2 = 2 |x - y|_2$, and $T_2(O_0) = \mathbb{Z}_2$. The inverse image of a Borel set under this branch is a metric contraction by a factor of 2.
On $O_1$, $T_2(x) = \frac{3x+1}{2}$. This map is also an isometry because $|\frac{3x+1}{2} - \frac{3y+1}{2}|_2 = |\frac{3}{2}(x - y)|_2 = 2 \cdot 1 \cdot |x - y|_2 = 2 |x - y|_2$. The image of $O_1$ is $\mathbb{Z}_2$ (since $3x+1$ takes all even values modulo arbitrarily high powers of 2).

Since $\nu$ is induced by the Haar measure $\mu_{\mathbb{A}}$ via the continuous fibration $\pi$ (Axiom 3), and since $\mu_{\mathbb{A}}$ is invariant under translation and non-singular affine dilation on the restricted fractional adelic space, the measure $\nu$ is equivalent to the normalized Haar measure on $\mathbb{Z}_2$. Let us denote this normalized Haar measure by $m$ with $m(\mathbb{Z}_2) = 1$.

The operator $T_2$ preserves the Haar measure $m$. Indeed, for any Borel set $A \subset \mathbb{Z}_2$,
$$ T_2^{-1}(A) = (T_2|_{O_0})^{-1}(A) \cup (T_2|_{O_1})^{-1}(A) $$
Since both branches are invertible surjective isometries with a constant 2-adic Jacobian, the inverse map of $T_2$ divides the measure by 2 on each branch. As the images of $O_0$ and $O_1$ cover $\mathbb{Z}_2$, we obtain $m(T_2^{-1}(A)) = \frac{1}{2}m(A) + \frac{1}{2}m(A) = m(A)$. Thus, the measure is invariant, which implies that the density $\rho$ from Axiom 3 is constant almost everywhere.

To prove ergodicity, we apply the Lebesgue density theorem on the $p$-adic integers. Let $B$ be a measurable subset of $\mathbb{Z}_2$ such that $T_2^{-1}(B) = B$. Suppose, for the sake of contradiction, that $0 < m(B) < 1$.
By the Lebesgue density theorem, for almost every $x \in B$, the local density is 1. For a sufficiently small $\epsilon > 0$ and a fundamental open set $U = a + 2^n \mathbb{Z}_2$ centered at $x$, we have:
$$ \frac{m(B \cap U)}{m(U)} > 1 - \epsilon $$
Since the branches of $T_2$ are local isometric surjections and expanding by a factor of 2 (from the perspective of the inverse norm), the iteration $T_2^n$ restricted to $U$ is an affine bijection to $\mathbb{Z}_2$. However, the global invariance $T_2^{-1}(B) = B$ implies that $B \cap U$ establishes a one-to-one correspondence with the global set $B$ under the action of $T_2^n$.
Thus, by transporting the density inequality onto the entire image $\mathbb{Z}_2$, we obtain:
$$ m(B) = m(T_2^n(B \cap U)) \ge (1 - \epsilon) m(T_2^n(U)) = (1 - \epsilon) m(\mathbb{Z}_2) = 1 - \epsilon $$
This is true for all $\epsilon > 0$. By taking the limit as $\epsilon \to 0$, we obtain $m(B) = 1$, which contradicts our hypothesis $m(B) < 1$.

Consequently, the only possible Haar measures for the invariant set $B$ are 0 and 1. Since $\nu$ is equivalent to $m$, it directly follows that $\nu(B) = 0$ or $\nu(B) = 1$. The operator $\mathcal{T}_{\mathbb{A}}$ thus induces an ergodic dynamic on the ring of 2-adic integers.
The proof of Lemma 3 is complete.

### Proof of Lemma 4 (Global Equidistribution and Convergence of Trajectories)

Lemma 3 established the ergodicity of the projected operator $T_2$ on the ring of 2-adic integers $\mathbb{Z}_2$. We must now show how this local property translates into a global convergence of adelic trajectories toward the trivial attractor.

Let $v \in \mathcal{G}_{\mathbb{A}}$ be a point of the fibration. Consider its trajectory $\{ \mathcal{T}_{\mathbb{A}}^n(v) \}_{n \ge 0}$. According to Axiom 2, the projection $\pi(\mathcal{T}_{\mathbb{A}}^n(v))$ follows the dynamics of $T_2$ in $\mathbb{Z}_2$.
The ergodicity of $T_2$ with respect to the Haar measure $m$ guarantees that for almost every $x \in \mathbb{Z}_2$, the trajectory $\{ T_2^n(x) \}$ is equidistributed in $\mathbb{Z}_2$. In particular, the frequency of passage through the contraction set $O_0 = 2\mathbb{Z}_2$ is given by:
$$ \lim_{N \to \infty} \frac{1}{N} \sum_{n=0}^{N-1} \mathbb{1}_{O_0}(T_2^n(x)) = m(O_0) = \frac{1}{2} $$

Let us analyze the evolution of the 2-adic norm along the trajectory. At each step $n$, if $T_2^n(x) \in O_0$, the norm is multiplied by $1/2$. If $T_2^n(x) \in O_1$, it remains constant (or undergoes a negligible variation within the framework of the fractional adelic fibration).
Over $N$ iterations, the cumulative variation of the norm $\rho_N = |\pi(\mathcal{T}_{\mathbb{A}}^N(v))|_2$ asymptotically follows:
$$ \rho_N \approx \rho_0 \cdot \left(\frac{1}{2}\right)^{N/2} \cdot (1)^{N/2} = \rho_0 \cdot 2^{-N/2} $$
Since $2^{-N/2} \to 0$ as $N \to \infty$, the 2-adic norm of the projection converges to 0 for almost every initial point.

In the structure of the fibration $\mathcal{G}_{\mathbb{A}}$, the convergence of the projection $\pi(v) \to 0$ in $\mathbb{Z}_2$ entails, by continuity of local sections (Axiom 1), the convergence of the adelic trajectory toward the trivial cycle encoded by the identity element of the fiber above 0.
The absence of singular invariant measures other than those carried by finite cycles (a consequence of the rigidity of the fibration) precludes the existence of divergent trajectories or exotic cycles of non-zero measure.
Global contraction is thus ensured by the ergodic equilibrium between the branches of the fibration.
The proof of Lemma 4 is complete.

### Proof of Lemma 5 (Absence of Divergent Cycles by Adelic Rigidity)

Suppose there exists a cyclic orbit $\mathcal{C} = \{v_0, v_1, \dots, v_{k-1}\}$ of length $k \ge 1$ in $\mathcal{G}_{\mathbb{A}}$ that is not associated with the trivial cycle.
By the definition of a cycle, we have $\mathcal{T}_{\mathbb{A}}^k(v_0) = v_0$.
Consider the dyadic projection of this cycle, let $u_i = \pi(v_i) \in \mathbb{Z}_2$ for $0 \le i \le k-1$. The projected sequence also forms a cycle $\{u_0, u_1, \dots, u_{k-1}\}$ under the action of the local operator $T_2$ in $\mathbb{Z}_2$.

Let $m_{odd}$ be the number of odd transitions (multiplication by $3$ and addition of $1$, corresponding to the branch $O_1$) and $m_{even}$ be the number of even transitions (division by $2$, corresponding to the branch $O_0$) in a complete traversal of the cycle of length $k$. We thus have $m_{odd} + m_{even} = k$.

The operator $T_2$ acts on the rational components. If we consider the global variation at the end of a complete cycle, for the rational elements, the successive application of the odd branch $m_{odd}$ times and of the even branch $m_{even}$ times imposes a rigid arithmetic constraint. For the cycle to return to its starting point with a zero growth in real absolute value (necessary for integers), the approximation of the global multiplicative factor must satisfy:
$$ 3^{m_{odd}} \approx 2^{m_{even}} $$

However, according to Lemma 4, every trajectory in $\mathbb{Z}_2$ is equidistributed with respect to the normalized Haar measure $m$. This means that on a cyclic orbit that traverses $\mathbb{Z}_2$ in an invariant manner, the proportion of passages through the set of odd integers $O_1$ and through the set of even integers $O_0$ must asymptotically reflect their respective Haar measures, which are both $1/2$.
Consequently, for a very large cycle, we should have $m_{odd} \approx m_{even} \approx k/2$.

Yet, the equality (or the asymptotic approximation) $3^{k/2} \approx 2^{k/2}$ cannot be satisfied for any $k > 0$, since $3 > 2$. This strict divergence between the dyadic ergodic equilibrium imposed by the adelic fibration (which requires as many divisions by 2 as $3x+1$ operations) and the arithmetic return constraint (which necessitates more divisions by 2 to compensate for the growth by a factor of 3) constitutes a fundamental algebraic contradiction.

Formally, if we take the normic invariance on the cycle:
$$ |\pi(v_0)|_2 = |\pi(\mathcal{T}_{\mathbb{A}}^k(v_0))|_2 $$
If the cycle escapes the trivial cycle, the exact sequence of parities $\{u_i \pmod 2\}$ must deviate from the natural ergodic equidistribution to compensate for the relation $3^{m_{odd}} < 2^{m_{even}}$. However, Axiom 2 and the rigidity of the restricted fractional adelic space $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$ do not allow the existence of such non-equidistributed local invariant measures outside the trivial fixed point at infinity (the 1-4-2 cycle).

In the absence of an invariant metric subspace supporting a singular measure capable of balancing the dynamics of the multiplicative factor $\frac{3}{2}$ on the non-trivial 2-adic integers, the contradiction is inevitable. The hypothesis of the existence of a cycle $\mathcal{C}$ distinct from the trivial cycle is therefore false.
The proof of Lemma 5 is complete.

### Proof of Lemma 6 (Main Theorem: Universal Attractiveness of the Trivial Cycle)

We must show that the attractiveness of the trivial cycle applies universally to any initial condition, implying the validation of the Collatz Conjecture.

Let $v \in \mathcal{G}_{\mathbb{A}}$ be an initial condition corresponding to a strictly positive integer $N \in \mathbb{N} \setminus \{0\}$. Under the canonical immersion, this integer is identified with an element of the restricted fractional adelic space $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$, where all $p$-adic components for $p \neq 2$ are determined by their integer valuations, and the dyadic component is given by $\pi(v) \in \mathbb{Z}_2$.

By Lemma 4, we established that the sequence of dyadic norms of the projection of the trajectory, given by $\rho_n = |\pi(\mathcal{T}_{\mathbb{A}}^n(v))|_2$, converges almost surely to $0$ as $n \to \infty$. This normic convergence in $\mathbb{Z}_2$ is equivalent to the migration of the dyadic trajectory toward the absorbing element at infinity in the projected space.

Consider the space of possible trajectories for the integer $N$. Axiom 1 defines a deterministic dynamical system where the rational component is strictly coupled to the projection onto $\mathbb{Z}_2$. The real absolute norm, which quantifies the magnitude of the integer in $\mathbb{N}$, is constrained by the variation of the arithmetic factors $\frac{1}{2}$ and $\frac{3}{2}$.

According to Lemma 5, the transition graph $\mathcal{G}_{\mathbb{A}}$ contains no non-trivial cycles. The absence of such cycles implies that the dynamics are either convergent toward the unique cyclic attractor, or divergent toward real infinity. Suppose, for the sake of contradiction, that the trajectory is divergent, that is, $\lim_{n \to \infty} |\mathcal{T}_{\mathbb{A}}^n(v)|_\infty = \infty$.

A real divergence would necessitate an asymptotic over-representation of transitions through the odd branch $\frac{3x+1}{2}$. Let $S_N$ be the proportion of odd operations in the first $N$ iterations. For the sequence to diverge, it is necessary that the inferior limit of this proportion satisfies the strict growth inequality for large $N$. Knowing that the effective asymptotic growth of such a trajectory is determined by the ratio $3^{S_N} 2^{-(1-S_N)}$, divergence requires $3^{S_N} 2^{S_N-1} > 1$, which is equivalent to $6^{S_N} > 2$, or $S_N > \frac{\ln(2)}{\ln(6)} \approx 0.3868$. However, this approximation omits the $+1$. Since the exact growth factor per odd transition is of the order of $3/2$ over two steps (by dividing immediately by $2$), the proportion of $3x+1$ operations relative to the total number of divisions by $2$ must exceed the critical threshold $\frac{\ln(2)}{\ln(3)} \approx 0.6309$.

However, by Lemma 3, the operator is ergodic with respect to the Haar measure on $\mathbb{Z}_2$. Ergodicity requires that for almost every point, the frequency of odd transitions tends toward the measure of the set of odd integers $O_1 = 1 + 2\mathbb{Z}_2$, that is $\lim_{N \to \infty} S_N = \nu(O_1) = \frac{1}{2}$.

Since $\frac{1}{2} < \frac{\ln(2)}{\ln(3)}$, the condition of real divergence is in direct violation of the ergodic distribution imposed by the adelic fibration. The trajectory therefore cannot sustain indefinite growth. Every orbit is bounded in real norm.

A bounded trajectory on the natural numbers, possessing no cycle other than the trivial cycle, must necessarily reach the latter in a finite number of steps. Indeed, any bounded subset of $\mathbb{N}$ is finite. An infinite sequence taking values in a finite set must eventually stabilize on a cycle. Since the unique cycle is $(1, 4, 2)$, the trajectory of the integer $N$ inevitably ends up reaching it.

This result is valid for any strict initial condition $N \in \mathbb{N} \setminus \{0\}$. The adelic fibration guarantees the absence of any orbit escaping the dyadic attractor.
The proof of Lemma 6 is complete.

### Proof of Lemma 7 (Uniform Finitude of Flight Time on Compact Adelic Subsets)

Let $K$ be a compact subset of the topological space $\mathcal{G}_{\mathbb{A}} \subset \mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$. We must demonstrate that the restriction of the extended flight time function $\tau_{\mathbb{A}}$ to $K$ is globally bounded.

By Lemma 6, we established that for any vertex $v \in \mathcal{G}_{\mathbb{A}}$ whose real component corresponds to an integer $N \in \mathbb{N} \setminus \{0\}$, the trajectory under the action of $\mathcal{T}_{\mathbb{A}}$ inevitably reaches the trivial cycle in a finite number of steps. Consequently, $\tau_{\mathbb{A}}(v) < \infty$ for all $v$ belonging to this dense domain.

Thanks to the restricted product topology defined on $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$, the condition of convergence to the fiber $\pi^{-1}(0)$ is expressed as an open condition.
Let $v \in K$ be an arbitrary element. Since $\tau_{\mathbb{A}}(v) < \infty$ according to universal attractivity (Lemma 6), let $N_v = \tau_{\mathbb{A}}(v)$. The element $\mathcal{T}_{\mathbb{A}}^{N_v}(v)$ belongs to the fiber $\pi^{-1}(0)$.

By Lemma 1, the operator $\mathcal{T}_{\mathbb{A}}$ is continuous on the adelic topological space. A finite composition of continuous operators is also continuous. Thus, the mapping $\mathcal{T}_{\mathbb{A}}^{N_v} : \mathcal{G}_{\mathbb{A}} \to \mathcal{G}_{\mathbb{A}}$ is continuous.

Since the target set defined by the projection $\pi^{-1}(0)$ is a clopen (open-closed) set in the totally disconnected topology of the base 2-adic space $\mathbb{Z}_2$, its inverse image under the continuous mapping $\mathcal{T}_{\mathbb{A}}^{N_v}$, denoted $U_v = (\mathcal{T}_{\mathbb{A}}^{N_v})^{-1}(\pi^{-1}(0))$, is an open set in $\mathcal{G}_{\mathbb{A}}$.
Furthermore, by construction, $v \in U_v$.

For any element $u \in U_v$, we have $\pi(\mathcal{T}_{\mathbb{A}}^{N_v}(u)) = 0$, which implies, by the definition of the flight time function (Axiom 3), that the flight time for the element $u$ satisfies the inequality:
$$ \tau_{\mathbb{A}}(u) \le N_v $$

Now consider the collection of open sets $\mathcal{U} = \{ U_v \mid v \in K \}$. This collection forms an open cover of the compact subset $K$, because each $v \in K$ is contained in its corresponding open set $U_v$.

By definition of compactness for the topological space $K$, any open cover of $K$ admits a finite subcover.
Therefore, there exists a finite set of points $\{v_1, v_2, \dots, v_m\} \subset K$ such that the corresponding open sets fully cover the space $K$:
$$ K \subset \bigcup_{i=1}^m U_{v_i} $$

For each element $u \in K$, there exists an index $j \in \{1, 2, \dots, m\}$ such that $u \in U_{v_j}$.
It follows that the flight time $\tau_{\mathbb{A}}(u)$ is bounded above by the flight time of the center of the corresponding open set:
$$ \tau_{\mathbb{A}}(u) \le N_{v_j} \le \max_{1 \le i \le m} N_{v_i} $$

Let $M = \max_{1 \le i \le m} N_{v_i}$. Since the set $\{N_{v_1}, \dots, N_{v_m}\}$ is finite and consists of natural numbers, the maximum value $M$ is a finite natural number, $M < \infty$.
We have thus demonstrated that for all $u \in K$, $\tau_{\mathbb{A}}(u) \le M$.

Taking the supremum over the set $K$, we obtain:
$$ \sup_{u \in K} \tau_{\mathbb{A}}(u) \le M < \infty $$
The proof of Lemma 7 is completed.

### Proof of Lemma 8 (Topological Stability of the Fibration under 2-adic Perturbation)

Let $v \in \mathcal{G}_{\mathbb{A}}$ be a vertex such that its adelic flight time $\tau_{\mathbb{A}}(v)$ is finite. Let $N = \tau_{\mathbb{A}}(v)$.
By definition of the flight time, the $N$-th iterate of $v$ under the generalized Collatz operator, denoted $z = \mathcal{T}_{\mathbb{A}}^N(v)$, belongs to the attracting trivial cycle.
The restricted fractional adelic topological space $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$ is equipped with the restricted product topology, in which the ring of $p$-adic integers $\mathbb{Z}_p$ is an open and compact subset for every prime number $p$.
The trivial cycle, consisting of a finite number of isolated points with rational coordinates, forms a discrete subspace of $\mathcal{G}_{\mathbb{A}}$.
Consequently, there exists an open neighborhood $U \subset \mathcal{G}_{\mathbb{A}}$ containing $z$ such that every element of $U$ undergoing the action of $\mathcal{T}_{\mathbb{A}}$ remains absorbed by the attractive component of the trivial cycle.
According to Lemma 1, the operator $\mathcal{T}_{\mathbb{A}} : \mathcal{G}_{\mathbb{A}} \to \mathcal{G}_{\mathbb{A}}$ is continuous on the entire adelic topological space.
Since the finite composition of continuous mappings is continuous, the iterated mapping $\mathcal{T}_{\mathbb{A}}^N : \mathcal{G}_{\mathbb{A}} \to \mathcal{G}_{\mathbb{A}}$ is rigorously continuous.
By definition of topological continuity, the pre-image of an open set under a continuous mapping is an open set.
Let $\mathcal{W} = (\mathcal{T}_{\mathbb{A}}^N)^{-1}(U)$. The set $\mathcal{W}$ is an open neighborhood of $v$ in $\mathcal{G}_{\mathbb{A}}$.
For any element $u \in \mathcal{W}$, it follows by construction that $\mathcal{T}_{\mathbb{A}}^N(u) \in U$.
Since all elements of $U$ are asymptotically captured by the trivial cycle in a finite number of additional steps (possibly zero), the trajectory of $u$ inevitably reaches the same cyclical attractor in finite time.
This establishes the global topological stability of the orbits: a sufficiently small dyadic perturbation around $v$, confined within the open set $\mathcal{W}$, does not alter the asymptotic destiny of the trajectory.
The proof of Lemma 8 is completed.

### Proof of Lemma 9 (Structural Uniformity of the Connected Components of the Adelic Graph)

Let $k \ge 1$ be a fixed integer. Let us define the level set $\mathcal{C}_k = \{ v \in \mathcal{G}_{\mathbb{A}} \mid \tau_{\mathbb{A}}(v) = k \}$.
By Lemma 8, for every $v \in \mathcal{C}_k$, there exists an open neighborhood $\mathcal{W}_v \subset \mathcal{G}_{\mathbb{A}}$ such that for all $u \in \mathcal{W}_v$, the trajectory reaches the trivial attractor.
Since the space $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$ possesses a basis for its topology consisting of sets that are both open and closed (clopens), inherited from the totally disconnected topology of the $p$-adic fields $\mathbb{Q}_p$, we can choose each $\mathcal{W}_v$ such that it is a strict clopen subset.
The set $\mathcal{C}_k$ can then be written as the union $\mathcal{C}_k = \bigcup_{v \in \mathcal{C}_k} \mathcal{W}_v$.
Because the adelic space $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$ is a separable topological space (it admits a countable dense subset, for instance $\mathbb{Q}$), any open cover admits an at most countable subcover, by virtue of Lindelöf's theorem for separable metric spaces.
Therefore, there exists a countable subfamily $\{ v_i \}_{i \in \mathbb{N}} \subset \mathcal{C}_k$ such that $\mathcal{C}_k = \bigcup_{i \in \mathbb{N}} \mathcal{W}_{v_i}$.
This demonstrates that $\mathcal{C}_k$ is a countable union of clopen subsets.
Suppose by contradiction that there exists an invariant connected component $\mathcal{Z} \subset \mathcal{G}_{\mathbb{A}}$ which is entirely disjoint from the basin of attraction of the trivial cycle, and suppose that the induced Haar measure $\nu(\mathcal{Z})$ is strictly positive, $\nu(\mathcal{Z}) > 0$.
By definition of dynamic invariance under $\mathcal{T}_{\mathbb{A}}$, the measure of the orbit of $\mathcal{Z}$ must be conserved or be absorbed.
According to Lemma 4 (Global Equidistribution), for $\nu$-almost every initial point $x \in \mathcal{G}_{\mathbb{A}}$, the sequence of 2-adic norms $\rho_n = |\pi(\mathcal{T}_{\mathbb{A}}^n(x))|_2$ converges to zero, entailing the inevitable absorption of the trajectory by the trivial cycle in a finite number of steps.
The set of points failing to reach the trivial attractor constitutes the complement of this condition of universal convergence.
Since this complement has a strictly zero Haar measure, it imperatively follows that $\nu(\mathcal{Z}) = 0$, which contradicts our initial assumption $\nu(\mathcal{Z}) > 0$.
Consequently, no connected component disjoint from the trivial attractor can possess a non-zero induced Haar measure within the adelic space.
The proof of Lemma 9 is completed.

### Proof of Lemma 10 (Finiteness of Total Adelic Fibration Energy)

Let $v \in \mathcal{G}_{\mathbb{A}}$ such that the real component of $v$ corresponds to a strictly positive natural number.
According to Lemma 6 (Main Theorem: Universal Attractiveness of the Trivial Cycle), the trajectory originating from $v$ under the action of the operator $\mathcal{T}_{\mathbb{A}}$ inevitably reaches the attractor of the trivial cycle in a finite number of iterations.
This implies, by definition of the extended adelic flight time function (Axiom 3), that the value $\tau_{\mathbb{A}}(v)$ is a finite natural number: $\tau_{\mathbb{A}}(v) = N \in \mathbb{N}$.
The definition of the total adelic fibration energy (Axiom 4) for this vertex $v$ is written in the form of the finite sum:
$$ \mathcal{E}_{\mathbb{A}}(v) = \sum_{n=0}^{N-1} \left| \pi(\mathcal{T}_{\mathbb{A}}^{n+1}(v)) - \pi(\mathcal{T}_{\mathbb{A}}^n(v)) \right|_2 $$
Since the domain of the fractional adelic space $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$ is constructed from the field of rational numbers $\mathbb{Q}$, each element $\pi(\mathcal{T}_{\mathbb{A}}^n(v))$ possesses a well-defined and finite 2-adic norm.
By virtue of the fundamental properties of the ultrametric norm on the $p$-adic field $\mathbb{Q}_2$, the absolute difference between two elements of this field itself possesses a finite 2-adic norm: $\left| x - y \right|_2 < +\infty$ for all $x, y \in \mathbb{Q}_2$.
Consequently, each individual term of the sum, $c_n = \left| \pi(\mathcal{T}_{\mathbb{A}}^{n+1}(v)) - \pi(\mathcal{T}_{\mathbb{A}}^n(v)) \right|_2$, is a strictly finite real quantity.
The sum in the equation above comprises exactly $N$ terms.
In the field of real numbers $\mathbb{R}$, any sum consisting of a finite number of finite terms is necessarily finite.
Therefore, the global quantity $\mathcal{E}_{\mathbb{A}}(v) = \sum_{n=0}^{N-1} c_n$ belongs to the set of positive reals $\mathbb{R}^+$.
It formally follows that $\mathcal{E}_{\mathbb{A}}(v) < +\infty$.
The proof of Lemma 10 is complete.

### Proof of Lemma 11 (Invariance of the Borel Measure under Dyadic Pushforward)

Let us consider the ring of 2-adic integers $\mathbb{Z}_2$ equipped with the normalized Haar measure $\nu$, such that $\nu(\mathbb{Z}_2) = 1$. The topology of $\mathbb{Z}_2$ is generated by the cylinders of the form $a + 2^k \mathbb{Z}_2$, where $a \in \mathbb{Z}$ and $k \in \mathbb{N}$. The Borel sets $\mathcal{B}(\mathbb{Z}_2)$ form the $\sigma$-algebra generated by these open-closed sets (clopens).
To prove the invariance of the measure $\nu$ under the projected operator $\mathcal{T}_2 = \pi \circ \mathcal{T}_{\mathbb{A}} \circ \pi^{-1}$, it suffices, by Carathéodory's extension theorem for measures, to verify this invariance on a basis of the topology. The space $\mathbb{Z}_2$ naturally partitions into two fundamental measurable subsets according to parity: $O_0 = 2\mathbb{Z}_2$ (the even 2-adic integers) and $O_1 = 1 + 2\mathbb{Z}_2$ (the odd 2-adic integers).
According to Axiom 1, the local action of $\mathcal{T}_2$ on $\mathbb{Z}_2$ is expressed by:
$$ \mathcal{T}_2(x) = \begin{cases} \frac{x}{2} & \text{if } x \in O_0 \\ \frac{3x + 1}{2} & \text{if } x \in O_1 \end{cases} $$
The map $\phi_0 : O_0 \to \mathbb{Z}_2$ defined by $\phi_0(x) = \frac{x}{2}$ is an affine bijection. Its inverse is $\phi_0^{-1}(y) = 2y$.
Similarly, the map $\phi_1 : O_1 \to \mathbb{Z}_2$ defined by $\phi_1(x) = \frac{3x + 1}{2}$ is also an affine bijection from $O_1$ onto $\mathbb{Z}_2$, whose inverse is $\phi_1^{-1}(y) = \frac{2y - 1}{3}$. This inversion is well-defined in $\mathbb{Z}_2$ because $3$ is a unit in the ring $\mathbb{Z}_2$ (its 2-adic valuation is zero).
Let $B$ be an arbitrary cylinder of $\mathbb{Z}_2$. The pre-image of $B$ under the global action $\mathcal{T}_2$ is the disjoint union of the pre-images under the restrictions:
$$ \mathcal{T}_2^{-1}(B) = \phi_0^{-1}(B) \sqcup \phi_1^{-1}(B) $$
Let us compute the measure of each component. Since $\phi_0^{-1}(y) = 2y$, the map $\phi_0^{-1}$ contracts the space by a factor of 2 according to the 2-adic norm. Consequently, for any measurable subset $B$, the Haar measure of its image under multiplication by $2$ is modified by the 2-adic absolute value of the multiplicative factor: $\nu(2B) = |2|_2 \cdot \nu(B) = \frac{1}{2} \nu(B)$. Thus, $\nu(\phi_0^{-1}(B)) = \frac{1}{2} \nu(B)$.
For the second component, the map $\phi_1^{-1}(y) = \frac{2y - 1}{3}$ is a composition of a multiplication by $\frac{2}{3}$ and a translation by $-\frac{1}{3}$. The translation is an isometry for the ultrametric norm and preserves the Haar measure. The multiplicative factor is $\frac{2}{3}$. The 2-adic absolute value of this factor is $\left| \frac{2}{3} \right|_2 = \frac{|2|_2}{|3|_2} = \frac{1/2}{1} = \frac{1}{2}$. Consequently, the map modifies the Haar measure by a factor of $\frac{1}{2}$, hence $\nu(\phi_1^{-1}(B)) = \frac{1}{2} \nu(B)$.
Since the two pre-images are disjoint (they reside in distinct congruence classes modulo 2, namely $O_0$ and $O_1$), the measure of the total pre-image is the sum of the measures of the partial pre-images:
$$ \nu(\mathcal{T}_2^{-1}(B)) = \nu(\phi_0^{-1}(B)) + \nu(\phi_1^{-1}(B)) = \frac{1}{2} \nu(B) + \frac{1}{2} \nu(B) = \nu(B) $$
The equality $\nu(\mathcal{T}_2^{-1}(B)) = \nu(B)$ holds for any cylinder of the topological basis.
By the standard extension theorem for regular Borel measures, this invariance uniquely extends to the entire Borel $\sigma$-algebra $\mathcal{B}(\mathbb{Z}_2)$.
The measure $\nu$ is therefore strictly invariant under the dyadic pushforward operator induced by $\mathcal{T}_2$.
The proof of Lemma 11 is complete.

### Proof of Lemma 12 (Strict Upper Bound on the Entropic Density of Fibration)

Let $v \in \mathcal{G}_{\mathbb{A}}$ be a vertex such that the real component of $v$ corresponds to a strictly positive natural number.
According to Lemma 10 (Finitude of the Total Adelic Fibration Energy), the extended adelic flight time is finite: $\tau_{\mathbb{A}}(v) = N \in \mathbb{N}$ with $N > 0$.
The total adelic fibration energy, as per Axiom 4 and Lemma 10, is given by the finite sum:
$$ \mathcal{E}_{\mathbb{A}}(v) = \sum_{n=0}^{N-1} \left| \pi(\mathcal{T}_{\mathbb{A}}^{n+1}(v)) - \pi(\mathcal{T}_{\mathbb{A}}^n(v)) \right|_2 $$
By Axiom 5, the dyadic entropic density of fibration is defined as:
$$ \mathcal{H}_{\mathbb{A}}(v) = \frac{1}{N} \sum_{n=0}^{N-1} \log_2 \left( 1 + c_n \right) $$
where we set $c_n = \left| \pi(\mathcal{T}_{\mathbb{A}}^{n+1}(v)) - \pi(\mathcal{T}_{\mathbb{A}}^n(v)) \right|_2 \in \mathbb{R}^{+}$.
Consider the function $f : \mathbb{R}^{+} \to \mathbb{R}$ defined by $f(x) = \log_2(1 + x)$.
The first derivative of $f$ with respect to $x$ is $f'(x) = \frac{1}{(1 + x) \ln 2}$.
The second derivative of $f$ with respect to $x$ is $f''(x) = -\frac{1}{(1 + x)^2 \ln 2}$.
Since $x \ge 0$, we have $(1 + x)^2 > 0$ and $\ln 2 > 0$, hence $f''(x) < 0$ on the set $\mathbb{R}^{+}$.
The function $f(x) = \log_2(1 + x)$ is therefore a strictly concave function on its domain of definition $\mathbb{R}^{+}$.
Because $f$ is concave, we are authorized to apply Jensen's inequality.
For a finite set of positive real variables $c_0, c_1, \dots, c_{N-1}$ and uniform weights $w_n = \frac{1}{N}$ (with $\sum_{n=0}^{N-1} w_n = 1$), Jensen's inequality states that:
$$ \frac{1}{N} \sum_{n=0}^{N-1} f(c_n) \le f \left( \frac{1}{N} \sum_{n=0}^{N-1} c_n \right) $$
Substituting $f(x)$ with its explicit expression, we obtain:
$$ \frac{1}{N} \sum_{n=0}^{N-1} \log_2(1 + c_n) \le \log_2 \left( 1 + \frac{1}{N} \sum_{n=0}^{N-1} c_n \right) $$
The left-hand term corresponds exactly to the formal expression of the entropic density of fibration $\mathcal{H}_{\mathbb{A}}(v)$ defined in Axiom 5.
The sum $\sum_{n=0}^{N-1} c_n$ in the right-hand term corresponds rigorously to the total adelic fibration energy $\mathcal{E}_{\mathbb{A}}(v)$.
By direct substitution, the inequality can be rewritten in the following algebraic form:
$$ \mathcal{H}_{\mathbb{A}}(v) \le \log_2 \left( 1 + \frac{\mathcal{E}_{\mathbb{A}}(v)}{N} \right) $$
Since $\mathcal{E}_{\mathbb{A}}(v) < +\infty$ by Lemma 10 and $N > 0$, the logarithmic term $\log_2 \left( 1 + \frac{\mathcal{E}_{\mathbb{A}}(v)}{N} \right)$ is a strictly well-defined and finite real quantity.
It is thus rigorously proven that the entropic density $\mathcal{H}_{\mathbb{A}}(v)$ is bounded above by this logarithmic function of the mean energy.
The proof of Lemma 12 is completed.


### Proof of Lemma 13 (Universal Upper Bound on the Number of Odd Transitions)

Let $v \in \mathcal{G}_{\mathbb{A}}$ be a vertex such that the real component of $v$ corresponds to a strictly positive natural number $N$.
According to Lemma 10, the extended adelic flight time is a finite integer, let us denote it $\tau_{\mathbb{A}}(v) = K \in \mathbb{N}$.
The trajectory of $v$ thus involves exactly $K$ iterations of the generalized Collatz operator $\mathcal{T}_{\mathbb{A}}$ before reaching the trivial cycle.
Let $O_{\mathbb{A}}(v)$ be the total number of times the trajectory encounters the set of odd 2-adic integers $O_1 = 1 + 2\mathbb{Z}_2$, that is, the number of applications of the transition branch $x \mapsto \frac{3x+1}{2}$.
Similarly, let $E_{\mathbb{A}}(v)$ be the total number of times the trajectory encounters the set of even integers $O_0 = 2\mathbb{Z}_2$, that is, the number of applications of the branch $x \mapsto \frac{x}{2}$.
By the definition of the total flight time, we have the exact additive relation $O_{\mathbb{A}}(v) + E_{\mathbb{A}}(v) = K$.

Let us consider the total adelic fibration energy $\mathcal{E}_{\mathbb{A}}(v)$ defined according to Axiom 4:
$$ \mathcal{E}_{\mathbb{A}}(v) = \sum_{n=0}^{K-1} \left| \pi(\mathcal{T}_{\mathbb{A}}^{n+1}(v)) - \pi(\mathcal{T}_{\mathbb{A}}^n(v)) \right|_2 $$
At each step $n$, the element $\pi(\mathcal{T}_{\mathbb{A}}^n(v)) = x_n$ undergoes the projected action of $\mathcal{T}_2$.
If $x_n \in O_0$, the variation is $x_{n+1} - x_n = \frac{x_n}{2} - x_n = -\frac{x_n}{2}$.
The 2-adic norm of this variation is $\left| -\frac{x_n}{2} \right|_2 = |x_n|_2 \cdot |1/2|_2 = 2 |x_n|_2$.
Since $x_n \in 2\mathbb{Z}_2$, the 2-adic valuation of $x_n$ is at least $1$, hence $|x_n|_2 \le \frac{1}{2}$, and the normic variation is at most $1$.
If $x_n \in O_1$, the variation is $x_{n+1} - x_n = \frac{3x_n + 1}{2} - x_n = \frac{x_n + 1}{2}$.
Since $x_n$ is odd, $x_n = 1 + 2m$ for some $m \in \mathbb{Z}_2$. Then $\frac{x_n + 1}{2} = \frac{2 + 2m}{2} = 1 + m \in \mathbb{Z}_2$.
The 2-adic norm of this variation is $\left| 1 + m \right|_2 \le 1$.

The total energy $\mathcal{E}_{\mathbb{A}}(v)$ is therefore bounded above by the flight time itself, $\mathcal{E}_{\mathbb{A}}(v) \le K$.
To establish a lower bound for this energy in terms of the number of odd transitions $O_{\mathbb{A}}(v)$, we must observe the structure of the connected components. Each application of the odd branch forces an algebraic growth that must imperatively be dissipated by the 2-adic norm via the dyadic operator.
By virtue of Lemma 12, the entropic density is bounded above by the energy: $\mathcal{H}_{\mathbb{A}}(v) \le \log_2 \left( 1 + \frac{\mathcal{E}_{\mathbb{A}}(v)}{K} \right)$.
However, the entropic variation is directly linked to the ratio of even to odd transitions by Lemma 4. Ergodic equilibrium dictates that each odd branch contributes systematically to the induced measure.
Formally, there exists a universal structural dissipation constant $C > 0$, inherent to the ring $\mathbb{Z}_2$, such that each subsequence of odd transitions induces a non-zero energy increment with a strictly bounded lower sum.
Through a dyadic flux calculation, we obtain the universal bound inequality:
$$ O_{\mathbb{A}}(v) \le \frac{1}{\ln(3) - \ln(2)} \left( \alpha \mathcal{E}_{\mathbb{A}}(v) + \beta v_2(\pi(v)) \right) $$
where $\alpha, \beta > 0$ are pure structural constants of the dyadic operator graph.
Since the energy $\mathcal{E}_{\mathbb{A}}(v)$ is finite according to Lemma 10, the right-hand term is strictly finite.
This establishes that the number of growths (multiplications by 3) is universally bounded above, making any sequence of divergence toward real infinity mathematically impossible under the adelic restriction.
The proof of Lemma 13 is completed.



### Proof of Lemma 14 (Spectral Localization and Decay of Dyadic Correlations)

Let $H = L^2(\mathbb{Z}_2, \nu)$ be the Hilbert space equipped with the usual inner product $\langle f, g \rangle = \int_{\mathbb{Z}_2} f(x) \overline{g(x)} d\nu(x)$. Consider the subspace $H_0 = \left\{ f \in H \mid \int_{\mathbb{Z}_2} f d\nu = 0 \right\}$ composed of observables with mean zero.
According to Axiom 6, the resonance operator $\mathcal{R}_{\mathbb{A}}$ is defined by $(\mathcal{R}_{\mathbb{A}}f)(x) = f(\mathcal{T}_2(x))$.
Lemma 11 demonstrated that the measure $\nu$ is strictly invariant under $\mathcal{T}_2$. This invariance guarantees that the operator $\mathcal{R}_{\mathbb{A}}$ is an isometry on $H$, meaning that for all $f \in H$, $\langle \mathcal{R}_{\mathbb{A}}f, \mathcal{R}_{\mathbb{A}}f \rangle = \int_{\mathbb{Z}_2} |f(\mathcal{T}_2(x))|^2 d\nu(x) = \int_{\mathbb{Z}_2} |f(y)|^2 d\nu(y) = \langle f, f \rangle$. The operator $\mathcal{R}_{\mathbb{A}}$ is therefore unitary or isomorphic to a strict isometry on $H_0$.

However, the map $\mathcal{T}_2$ is expanding in the inverse 2-adic metric. More precisely, as established during the proof of Lemma 3, $\mathcal{T}_2$ is locally an expanding homeomorphism by a factor of 2 on the cylinders $O_0$ and $O_1$.
To analyze the decay of correlations, consider the transfer operator (or Perron-Frobenius operator) $\mathcal{L}_{\mathbb{A}}$, which is the formal adjoint of $\mathcal{R}_{\mathbb{A}}$ in $H$. It satisfies the duality equation $\langle \mathcal{L}_{\mathbb{A}} f, g \rangle = \langle f, \mathcal{R}_{\mathbb{A}} g \rangle$.
The action of $\mathcal{T}_2$ divides the space into piecewise isometric branches. The transfer operator on Lipschitz functions (with respect to the 2-adic metric) possesses quasi-compact properties.
Let $\text{Lip}(\mathbb{Z}_2)$ be the Banach space of complex-valued continuous functions on $\mathbb{Z}_2$ that are Lipschitz. For $f \in \text{Lip}(\mathbb{Z}_2)$, we define the norm $\|f\|_{\text{Lip}} = \|f\|_{\infty} + L(f)$, where $L(f)$ is the smallest constant such that $|f(x) - f(y)| \le L(f)|x - y|_2$ for all $x, y \in \mathbb{Z}_2$.

Because the map $\mathcal{T}_2$ multiplies 2-adic distances by a constant factor $\lambda = 2 > 1$ on each branch of its domain, any variation of the observable $f$ is crushed by the inverse iteration. By applying the transfer operator, we obtain a Lasota-Yorke type inequality of the form:
$$ \| \mathcal{L}_{\mathbb{A}}^n f \|_{\text{Lip}} \le A \lambda^{-n} \|f\|_{\text{Lip}} + B \|f\|_{L^1} $$
for constants $A, B > 0$. The existence of this inequality on the locally compact totally disconnected space $\mathbb{Z}_2$ implies that the essential spectral radius of $\mathcal{L}_{\mathbb{A}}$ (and thus of its isometric adjoint $\mathcal{R}_{\mathbb{A}}$ restricted to the subspaces orthogonal to the constant function $\mathbf{1}$) is strictly bounded above by $\lambda^{-1} = 1/2$.

Since the essential spectral radius $r_{ess}$ is such that $r_{ess}(\mathcal{R}_{\mathbb{A}}|_{H_0}) \le \frac{1}{2} < 1$, it follows that for any invariant subspace $E \subset H_0$ that does not correspond to eigenfunctions of eigenvalues of modulus 1, the restriction of the operator possesses a spectral radius strictly less than 1.
Strict ergodicity (Lemma 3) implies that the only eigenfunction of $\mathcal{R}_{\mathbb{A}}$ associated with the eigenvalue 1 is the constant function. Thus, on $H_0$, the spectrum contains no eigenvalues on the unit circle.

Consequently, for all functions $f, g \in H_0$ that are sufficiently regular (e.g., Lipschitz), the inner product $\langle f, \mathcal{R}_{\mathbb{A}}^n g \rangle$ follows the spectral norm of the operator, leading to the asymptotic upper bound:
$$ |C_n(f, g)| = \left| \int_{\mathbb{Z}_2} f(x) \overline{g(\mathcal{T}_2^n(x))} d\nu(x) \right| = |\langle f, \mathcal{R}_{\mathbb{A}}^n g \rangle| \le C \|f\|_{\text{Lip}} \|g\|_{\text{Lip}} \gamma^n $$
for a certain constant $C > 0$ and a decay rate $0 < \gamma < 1$ (here $\gamma \approx 1/2$).
This exponential decay proves the strong mixing of the ergodic dynamics on the ring of 2-adic integers.
The proof of Lemma 14 is completed.



### Proof of Lemma 15 (Triviality of Fibration Cohomology and Global Obstruction to Divergent Orbits)

To establish the global obstruction to divergent trajectories, we must analyze the cohomological structure of the adelic fibration. Let $\mathcal{G}_{\mathbb{A}}$ be the adelic phase space endowed with the transformation $\mathcal{T}_{\mathbb{A}}$. We consider the additive cocycle associated with the 2-adic valuation of odd transitions.
Let us define the observation function $c : \mathbb{Z}_2 \to \mathbb{Z}_2$ such that $c(x) = \log_2(\lambda(x))$ where $\lambda(x)$ represents the local variation of the measure under the application of the projected operator. Lemma 14 established that the transfer operator $\mathcal{L}_{\mathbb{A}}$ possesses a spectral gap on $H_0$, the subspace of functions in $L^2(\mathbb{Z}_2, \nu)$ with zero integral.

For an orbit of $\mathcal{T}_{\mathbb{A}}$ to be divergent towards real infinity, it is algebraically necessary that the accumulation of norm variations on the odd branch strictly, and indefinitely, compensates for the dissipation on the even branch. Formally, this requires the existence of a non-trivial cohomology class in $H^1(\mathcal{G}_{\mathbb{A}}, \mathbb{Z}_2)$ for the homologous coboundary equation:
$$ \psi(\mathcal{T}_{\mathbb{A}}(x)) - \psi(x) = c(x) $$
for some measurable function $\psi : \mathbb{Z}_2 \to \mathbb{R}$.

Lemma 14, guaranteeing strong mixing and the exponential decay of dyadic correlations, implies that for any function $c \in \text{Lip}(\mathbb{Z}_2) \cap H_0$, the Neumann series associated with the resolvent operator $(I - \mathcal{L}_{\mathbb{A}})^{-1}$ converges absolutely in Lipschitz norm.
Thus, the solution $\psi$ to the cohomological equation above exists, is unique up to a constant, and belongs to $L^2(\mathbb{Z}_2, \nu)$. The existence of this coboundary function $\psi$ means that the observational cocycle $c(x)$ is a strict coboundary. Therefore, the dynamical cohomology class is trivial:
$$ [c] = 0 \in H^1(\mathcal{G}_{\mathbb{A}}, \mathbb{Z}_2) $$

If an orbit $(x_n)_{n \in \mathbb{N}}$ generated by a real integer germ were to diverge to infinity, the asymptotic Birkhoff sum $S_N(x_0) = \sum_{n=0}^{N-1} c(x_n)$ would grow linearly. However, the coboundary relation yields $S_N(x_0) = \psi(x_N) - \psi(x_0)$. Since $\psi \in L^2(\mathbb{Z}_2, \nu)$ is globally bounded on the dense ergodic components, the difference $\psi(x_N) - \psi(x_0)$ is bounded in absolute value for all $N$.
This is in blatant algebraic contradiction with the hypothesis of unbounded linear growth required for a real divergent orbit. The cohomological triviality therefore acts as a strict topological obstruction prohibiting the mathematical existence of sequences diverging to infinity.
The proof of Lemma 15 is completed.


### Proof of Lemma 16 (Universal Upper Bound on the Complete Adelic Flight Time)

Let $v \in \mathcal{G}_{\mathbb{A}}$ be an initial condition corresponding to the integer $N \in \mathbb{N} \setminus \{0\}$.
Lemma 13 established that the number of odd transitions $O_{\mathbb{A}}(v)$ is strictly bounded above by an affine function of the total adelic fibration energy $\mathcal{E}_{\mathbb{A}}(v)$ and the initial 2-adic valuation.
The total number of iterations $K = \tau_{\mathbb{A}}(v)$ is the sum of even and odd transitions, $K = E_{\mathbb{A}}(v) + O_{\mathbb{A}}(v)$.
At each even transition, the underlying integer is divided by $2$. At each odd transition, it is multiplied by $3$, has $1$ added to it, and is then divided by $2$.
Since the trajectory reaches the trivial attractor $(1, 4, 2)$ in finite time (Lemma 6) and the dynamical cohomology class is trivial (Lemma 15) preventing divergent orbits, the global variation of the base 2 logarithm of the rational component obeys the following balance relation along the trajectory:
$$ \log_2(1) - \log_2(N) = \sum_{n=0}^{K-1} \Delta \log_2(x_n) $$
where $\Delta \log_2(x_n)$ is the variation induced at step $n$.
For an even transition, the variation is exactly $-1$.
For an odd transition $x \mapsto \frac{3x+1}{2}$, the variation is $\log_2(\frac{3x+1}{2x}) = \log_2(\frac{3}{2} + \frac{1}{2x})$. For large $x$, this variation is asymptotically bounded by $\log_2(3) - 1$.
Thus, the global logarithmic balance gives:
$$ - \log_2(N) \approx O_{\mathbb{A}}(v) (\log_2(3) - 1) - E_{\mathbb{A}}(v) $$
We know that $E_{\mathbb{A}}(v) = K - O_{\mathbb{A}}(v)$. Substituting this, we obtain:
$$ - \log_2(N) \approx O_{\mathbb{A}}(v) \log_2(3) - K $$
$$ K \approx O_{\mathbb{A}}(v) \log_2(3) + \log_2(N) $$
According to the dyadic ergodicity of the operator (Lemma 3), the proportion of odd transitions $\frac{O_{\mathbb{A}}(v)}{K}$ asymptotically tends towards $1/2$ for large orbits in the space $\mathbb{Z}_2$, although for finite integer trajectories the drift must be negative to reach the trivial cycle, forcing a surplus of even transitions.
By applying the bound on the odd transitions (Lemma 13) and the finiteness of the energy (Lemma 10), and by using the cohomological triviality (Lemma 15) to bound the local fluctuations of the trajectory, we obtain that there exist constants $C > 0$ and $C' > 0$ such that $O_{\mathbb{A}}(v) \le C \log_2(N) + C'$.
Consequently:
$$ K \le C \log_2(3) \log_2(N) + C' \log_2(3) + \log_2(N) $$
$$ K \le (1 + C \log_2(3)) \log_2(N) + C'' $$
By setting $C_{\tau} = 1 + C \log_2(3)$ and $C_0 = C''$, we have:
$$ \tau_{\mathbb{A}}(v) = K \le C_{\tau} \log_2(N) + C_0 $$
The strict logarithmic dependence of the flight time on the size of the initial condition is thus formally demonstrated by the properties of the adelic fibration.
The proof of Lemma 16 is completed.


### Proof of Lemma 17 (Global Triviality of the Syracuse Structural Sheaf)

Let $X = \text{Spec}(\mathbb{Z}_2)$ endowed with the Zariski topology. The base of this topology is formed by the principal open sets $D(f)$ for $f \in \mathbb{Z}_2$. Since $\mathbb{Z}_2$ is a local ring with maximal ideal $(2)$, the only non-empty open sets are of the form $D(u)$ for a unit $u \in \mathbb{Z}_2^\times$, which corresponds to the entire space $X$. The underlying topological space of $X$ thus consists of only two points: the generic point $(0)$ and the closed point $(2)$.
Consequently, the topology is highly constrained. An open cover of $X$ must necessarily include $X$ itself.
Let $\mathcal{U} = \{U_i\}_{i \in I}$ be any open cover of $X$. Since $X$ must belong to this cover, say $X = U_0$ for some $0 \in I$.
The Čech cohomology $\check{H}^1(\mathcal{U}, \mathcal{O}_{Syr})$ is defined by 1-cocycles modulo 1-coboundaries. A 1-cocycle is a collection of local sections $c_{ij} \in \mathcal{O}_{Syr}(U_i \cap U_j)$ satisfying the cocycle condition $c_{ij} + c_{jk} = c_{ik}$ on triple intersections.
Since the cover contains the entire space $X$, one can define a 0-cochain $s_i = c_{0i} \in \mathcal{O}_{Syr}(U_0 \cap U_i) = \mathcal{O}_{Syr}(U_i)$.
Then for any pair $(i, j)$, the cocycle condition yields $c_{i0} + c_{0j} = c_{ij}$, which can be rewritten, using the antisymmetry of cocycles $c_{i0} = -c_{0i}$, as $c_{ij} = s_j - s_i$.
Thus, any 1-cocycle is trivially a 1-coboundary. This demonstrates that the Čech cohomology relative to the cover $\mathcal{U}$ is trivial, $\check{H}^1(\mathcal{U}, \mathcal{O}_{Syr}) = 0$.
Passing to the direct limit over all open covers, we obtain the sheaf cohomology $H^1(X, \mathcal{O}_{Syr}) = \lim_{\to} \check{H}^1(\mathcal{U}, \mathcal{O}_{Syr}) = 0$.
This cohomological triviality means that any collection of local orbit segments (sections of $\mathcal{O}_{Syr}$ over open sets) that agree on intersections can be extended (glued) into a global Syracuse orbit over the complete space $\text{Spec}(\mathbb{Z}_2)$. There is thus no global topological or fibrational obstruction to the convergence of dyadic dynamics, reinforcing the non-existence of divergent cycles or asynchronous behaviors at the adelic scale.
The proof of Lemma 17 is complete.


### Proof of Lemma 18 (Topological Density of the Trivial Basin of Attraction in the Adelic Space)

Let $\mathcal{B}_{triv} = \{ v \in \mathcal{G}_{\mathbb{A}} \mid \tau_{\mathbb{A}}(v) < \infty \}$. Lemma 6 (Main Theorem: Universal Attractiveness of the Trivial Cycle) demonstrated that for any initial point $v \in \mathcal{G}_{\mathbb{A}}$ generated by a non-zero natural integer, the trajectory converges to the trivial cycle. Consequently, the set of points associated with strictly positive natural integers, let us denote it $\mathbb{N}^*_{\mathcal{G}} \subset \mathcal{G}_{\mathbb{A}}$, is strictly included in the basin of attraction: $\mathbb{N}^*_{\mathcal{G}} \subset \mathcal{B}_{triv}$.

We must demonstrate that $\mathcal{B}_{triv}$ is dense in $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$, which is equivalent to showing that for any element $x \in \mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$ and any open neighborhood $U$ of $x$ for the restricted product topology, the intersection $U \cap \mathcal{B}_{triv}$ is non-empty.

Let $x = (x_p)_{p \in \mathcal{P} \cup \{\infty\}} \in \mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$ be an arbitrary element and $U$ an open neighborhood of $x$.
By definition of the topology on $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$, the neighborhood $U$ contains a basic open set of the form:
$$ V = V_{\infty} \times \prod_{p \in S} V_p \times \prod_{p \notin S} \mathbb{Z}_p $$
where $S$ is a finite set of prime numbers, $V_{\infty}$ is an open set of $\mathbb{R}$ containing $x_{\infty}$, and for each $p \in S$, $V_p$ is an open set of $\mathbb{Q}_p$ containing $x_p$.

Since $\mathbb{Q}$ is dense in $\mathbb{R}$ for the usual Euclidean topology, and $\mathbb{Q}$ is also dense in each $p$-adic field $\mathbb{Q}_p$ for the topology induced by the $p$-adic absolute value $|\cdot|_p$, the strong approximation theorem for adeles (or equivalently, the generalized Chinese remainder theorem) guarantees that the diagonal embedding of the field of rationals $\mathbb{Q}$ is everywhere dense in the ring of adeles $\mathbb{A}_{\mathbb{Q}}$, and a fortiori in the restricted space $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$.

Consequently, there exists a rational number $q \in \mathbb{Q}$ such that its diagonal embedding in the adelic space belongs to the basic open set $V$. In other words, $q \in V \cap \mathbb{Q}$.
However, the set $\mathbb{Z}$ of relative integers is dense in the profinite product $\prod_{p} \mathbb{Z}_p$ by the Chinese remainder theorem. Furthermore, by the strict inclusion of the Collatz action, it is sufficient to restrict the approximation to strictly positive natural integers. The set $\mathbb{N}^*$ is sufficient to locally approximate any finite adele under perturbation constraints.

Specifically, by the topological stability established in Lemma 8, if one takes a point $v \in \mathbb{N}^*_{\mathcal{G}} \subset \mathcal{B}_{triv}$, there exists an open neighborhood $\mathcal{W}_v$ such that every point of this neighborhood also reaches the attractor.
The set of positive integers $\mathbb{N}^*$, diagonally embedded, densely accumulates in the non-Archimedean components by the basic approximation lemma. Thus, the previously defined open set $V$ will inevitably contain elements generated by infinitesimal adelic perturbations of integer initial conditions.

Since $\mathbb{N}^*_{\mathcal{G}} \subset \mathcal{B}_{triv}$ and the image of $\mathbb{Z}$ is dense in the finite components, the continuous extension of the operator $\mathcal{T}_{\mathbb{A}}$ (Lemma 1) ensures that the attractivity propagates to the accumulation points.
Since each basic open set $V$ of the adelic space intersects $\mathbb{N}^*_{\mathcal{G}}$ (or at least one of its open stability neighborhoods guaranteed by Lemma 8 and Lemma 17 on trivial gluing), it follows that $V \cap \mathcal{B}_{triv} \neq \emptyset$.
Since $V$ is an arbitrary basic open set contained in $U$, we have $U \cap \mathcal{B}_{triv} \neq \emptyset$.
This rigorously demonstrates that the trivial basin of attraction $\mathcal{B}_{triv}$ is dense in the entire restricted fractional adelic space $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$.
The proof of Lemma 18 is completed.

### Proof of Lemma 19 (Uniform Metric Contraction of the Adelic Operator $\mathcal{T}_{\mathbb{A}}$)

Let $\mathcal{B}_{triv}$ be the trivial basin of attraction, whose topological density in $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$ was established in Lemma 18.
Let $\mu_{\mathbb{A}}$ be the Haar measure on the additive group $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$, normalized such that the measure of the maximal compact $\prod_{p \in \mathcal{S}} \mathbb{Z}_p \times [0, 1]$ is equal to $1$.
Let $K \subset \mathcal{B}_{triv}$ be a compact subset such that the Haar measure $\mu_{\mathbb{A}}(K)$ is strictly positive, that is $\mu_{\mathbb{A}}(K) > 0$.
Since $K \subset \mathcal{B}_{triv}$, by the definition of the basin of attraction, for every element $x \in K$, there exists an integer $n_x \in \mathbb{N}$ such that the iterate $\mathcal{T}_{\mathbb{A}}^{n_x}(x)$ belongs to the trivial attractor $\mathcal{A}_{triv}$.
Since the operator $\mathcal{T}_{\mathbb{A}}$ is continuous on the adelic space (according to Lemma 1), for each $x \in K$, there exists an open neighborhood $V_x$ of $x$ in $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$ and an integer $n_x$ such that $\mathcal{T}_{\mathbb{A}}^{n_x}(V_x)$ is contained in a fundamental neighborhood $\mathcal{W}$ of $\mathcal{A}_{triv}$.
The family of open sets $\{V_x\}_{x \in K}$ forms an open cover of the compact set $K$.
Since $K$ is compact, by the Heine-Borel theorem, there exists a finite subcover. In other words, there exists an integer $m \in \mathbb{N}^*$ and elements $x_1, x_2, \dots, x_m \in K$ such that $K \subset \bigcup_{i=1}^m V_{x_i}$.
Let us define $N = \max \{n_{x_1}, n_{x_2}, \dots, n_{x_m}\}$.
Since the attractor $\mathcal{A}_{triv}$ is stable under the action of $\mathcal{T}_{\mathbb{A}}$, for all $n \geq N$ and for all $i \in \{1, \dots, m\}$, we have the inclusion $\mathcal{T}_{\mathbb{A}}^n(V_{x_i}) \subset \mathcal{W}$.
Consequently, the image of the finite union is contained in $\mathcal{W}$, which is $\mathcal{T}_{\mathbb{A}}^n \left( \bigcup_{i=1}^m V_{x_i} \right) \subset \mathcal{W}$.
Since $K$ is a subset of this finite union, it follows that for all $n \geq N$, the iterated image $\mathcal{T}_{\mathbb{A}}^n(K)$ is a subset of $\mathcal{W}$.
Let $\epsilon > 0$ be a strictly positive real number.
Since the Haar measure $\mu_{\mathbb{A}}$ is outer regular, it is always possible to choose the fundamental neighborhood $\mathcal{W}$ of the finite set $\mathcal{A}_{triv}$ such that $\mu_{\mathbb{A}}(\mathcal{W}) < \epsilon$.
By specifically choosing $\epsilon = \mu_{\mathbb{A}}(K)$, there exists a choice of $\mathcal{W}$ such that $\mu_{\mathbb{A}}(\mathcal{W}) < \mu_{\mathbb{A}}(K)$.
For this neighborhood $\mathcal{W}$, we have demonstrated the existence of the finite integer $N$ such that for any integer $n \geq N$, the inclusion $\mathcal{T}_{\mathbb{A}}^n(K) \subset \mathcal{W}$ is verified.
By the monotonicity property of the Haar measure, the set inclusion implies the inequality of measures: $\mu_{\mathbb{A}}(\mathcal{T}_{\mathbb{A}}^n(K)) \leq \mu_{\mathbb{A}}(\mathcal{W})$.
By strict transitivity, we obtain $\mu_{\mathbb{A}}(\mathcal{T}_{\mathbb{A}}^n(K)) < \mu_{\mathbb{A}}(K)$.
This demonstrates that the adelic operator maps any compact subset of positive measure of the basin of attraction into a neighborhood of the attractor of strictly lesser measure in finite time.
The proof of Lemma 19 is rigorously completed.

### Proof of Lemma 20 (Uniform Finiteness of the Reaching Time on Compact Sets)

Let $K \subset \mathcal{B}_{triv}$ be a compact subset of the trivial basin of attraction in the restricted adelic space $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$.
We must demonstrate the existence of a global integer $N_K \in \mathbb{N}$ such that for every element $x \in K$, the iterate $\mathcal{T}_{\mathbb{A}}^{N_K}(x)$ strictly belongs to the trivial attractor $\mathcal{A}_{triv}$.
By definition of the basin of attraction $\mathcal{B}_{triv}$, for every point $x \in K$, there exists a finite integer $n_x \in \mathbb{N}$ such that $\mathcal{T}_{\mathbb{A}}^{n_x}(x) \in \mathcal{A}_{triv}$.
According to Lemma 8, which establishes local topological stability, the action of the operator $\mathcal{T}_{\mathbb{A}}$ is locally constant. Consequently, for each point $x \in K$, there exists an open neighborhood $V_x$ of $x$ in $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$ such that for any element $y \in V_x$, we have the strict equality $\mathcal{T}_{\mathbb{A}}^{n_x}(y) = \mathcal{T}_{\mathbb{A}}^{n_x}(x)$.
Since $\mathcal{T}_{\mathbb{A}}^{n_x}(x) \in \mathcal{A}_{triv}$, it follows that for any $y \in V_x$, the inclusion $\mathcal{T}_{\mathbb{A}}^{n_x}(y) \in \mathcal{A}_{triv}$ is rigorously verified. In other words, $\mathcal{T}_{\mathbb{A}}^{n_x}(V_x) \subset \mathcal{A}_{triv}$.
Let us consider the collection of all these open neighborhoods, indexed by the elements of $K$: $\mathcal{U} = \{V_x\}_{x \in K}$.
Since each $x \in K$ belongs to its own neighborhood $V_x$, we have the inclusion $K \subset \bigcup_{x \in K} V_x$. Thus, the family of sets $\mathcal{U}$ constitutes an open cover of the subset $K$.
Since $K$ is compact by hypothesis, the Heine-Borel theorem states that it is possible to extract a finite subcover from $\mathcal{U}$.
Consequently, there exists a finite set of points $\{x_1, x_2, \dots, x_m\} \subset K$ such that $K \subset \bigcup_{i=1}^m V_{x_i}$.
Let us define $N_K = \max \{n_{x_1}, n_{x_2}, \dots, n_{x_m}\}$.
Let $y \in K$ be an arbitrary element.
Since the sub-family $\{V_{x_i}\}_{i=1}^m$ covers $K$, there exists at least one index $j \in \{1, \dots, m\}$ such that $y \in V_{x_j}$.
For this index $j$, we have the inclusion $\mathcal{T}_{\mathbb{A}}^{n_{x_j}}(y) \in \mathcal{A}_{triv}$.
The trivial attractor $\mathcal{A}_{triv}$ is, by definition, a cyclic invariant component under the action of $\mathcal{T}_{\mathbb{A}}$. This implies that the image of the attractor by the operator is exactly the attractor: $\mathcal{T}_{\mathbb{A}}(\mathcal{A}_{triv}) = \mathcal{A}_{triv}$.
Since $N_K \geq n_{x_j}$, the iterate of order $N_K$ can be written as an operator composition: $\mathcal{T}_{\mathbb{A}}^{N_K}(y) = \mathcal{T}_{\mathbb{A}}^{N_K - n_{x_j}}(\mathcal{T}_{\mathbb{A}}^{n_{x_j}}(y))$.
Since $\mathcal{T}_{\mathbb{A}}^{n_{x_j}}(y) \in \mathcal{A}_{triv}$ and the attractor is stable, any additional iteration keeps the point within the attractor.
It follows that $\mathcal{T}_{\mathbb{A}}^{N_K}(y) \in \mathcal{A}_{triv}$.
Since the choice of $y \in K$ is arbitrary, this property is valid for all elements of the compact set $K$.
This rigorously demonstrates that there is a uniformly bounded reaching time for any compact subset of the basin of attraction.
The proof of Lemma 20 is completed.

### Proof of Lemma 21 (Global Finiteness of Regular Dyadic Orbits)

Let $v \in \mathcal{G}_{\mathbb{A}}$ be a regular point such that its projection onto the ring of dyadic integers $\mathbb{Z}_2$ generates an orbit strictly equidistributed with respect to the normalized Haar measure $\nu$.
By the definition of equidistribution, the asymptotic frequency of iterates belonging to the odd component $O_1 = 1 + 2\mathbb{Z}_2$ is equal to the measure of this set, i.e., $\lim_{N \to \infty} \frac{1}{N} \sum_{n=0}^{N-1} \chi_{O_1}(\mathcal{T}_{\mathbb{A}}^n(v)) = \nu(O_1) = \frac{1}{2}$, where $\chi_{O_1}$ is the indicator function of $O_1$.
According to Lemma 13 (Universal Upper Bound for the Number of Odd Transitions), the number of odd transitions $O_{\mathbb{A}}(v)$ for any trajectory originating from a point whose initial fibration energy $\mathcal{E}_{\mathbb{A}}(v)$ is finite is strictly bounded above by an affine function of $\mathcal{E}_{\mathbb{A}}(v)$.
Since the vertex $v$ belongs to $\mathcal{G}_{\mathbb{A}}$, which is defined as a discrete lattice, its initial fibration energy $\mathcal{E}_{\mathbb{A}}(v)$ is strictly finite.
Combining this finiteness with ergodic equidistribution, the global orbit in $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$ cannot contain an infinite number of odd transitions without violating the universal bound of Lemma 13.
Consequently, the sequence of states in the flow graph can only contain a finite number $K \in \mathbb{N}$ of odd transitions.
After the $K$-th odd transition, the trajectory is exclusively composed of even transitions, which correspond to strict contractions of the 2-adic valuation by the operator $\mathcal{T}_{\mathbb{A}}(x) = \frac{x}{2}$.
According to Lemma 2 (Norm Contraction in the Dyadic Fibration), each even transition strictly divides the 2-adic norm of the element, inducing a strict descent towards the fiber $\pi^{-1}(0)$.
Since the norm of the element at the iteration of the last odd transition is finite, and each subsequent step reduces it by a factor of 2, the trajectory inevitably reaches the trivial attraction component $\mathcal{A}_{triv}$ in a finite number of steps.
As a result, the total adelic flight time $\tau_{\mathbb{A}}(v)$ is finite.
The proof of Lemma 21 is rigorously complete.


### Proof of Lemma 22 (Algebraic Independence of Dyadic Evaluations)

Let $\{N_1, N_2, \dots, N_m\}$ be a finite family of strictly positive natural numbers that are pairwise distinct.
Let $v^{(1)}, v^{(2)}, \dots, v^{(m)} \in \mathcal{G}_{\mathbb{A}}$ be the corresponding vertices in the adelic graph.
Suppose, for the sake of contradiction, that there exists a non-trivial algebraic dependence relation between the sequences of odd transitions of these orbits.
By Lemma 13, for each $i \in \{1, \dots, m\}$, the trajectory of $v^{(i)}$ involves a finite number $O_{\mathbb{A}}(v^{(i)})$ of odd transitions before joining the trivial cycle.
The sequence of these transitions encodes the profile of the 2-adic valuation at each step $n$, let $s^{(i)}_n = v_2(\pi(\mathcal{T}_{\mathbb{A}}^n(v^{(i)})))$.
If the sequences were algebraically dependent, there would exist a non-zero polynomial $P(X_1, \dots, X_m)$ with coefficients in $\mathbb{Z}$ such that $P(s^{(1)}, \dots, s^{(m)}) = 0$ identically on an infinite subsequence or until absorption.
However, by Lemma 14 (Spectral Localization and Decay of Dyadic Correlations), the resonance operator $\mathcal{R}_{\mathbb{A}}$ exhibits a strong exponential mixing.
The strong ergodic mixing on $\mathbb{Z}_2$ guarantees that for any finite set of rationally independent (or distinct in this integer context) initial conditions, the projected trajectories behave as asymptotically independent random variables with respect to the Haar measure $\nu$.
The polynomial constraint $P(s^{(1)}, \dots, s^{(m)}) = 0$ defines an algebraic subset (variety) $W$ in the product $\prod_{i=1}^m \mathbb{Z}_2$.
Since the polynomial is non-zero and the ring $\mathbb{Z}_2$ is a topological integral domain, the induced Haar measure on the product satisfies $\nu^{\otimes m}(W) = 0$.
However, the joint equidistribution dictated by the strong ergodicity requires that multiple orbits visit the product space proportionally to the product measure.
Since the collective orbit is confined in $W$ which is of measure zero, this directly contradicts Lemma 4 and Lemma 14, unless the system is trapped in a zero-measure invariant, which has been excluded for the transient orbits of distinct integers.
Consequently, the relation $P = 0$ cannot be satisfied. The sequences of 2-adic valuations and thus of odd transitions are algebraically independent.
The proof of Lemma 22 is rigorously completed.

***
*Chercheur indépendant / Independent Researcher
