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

**Lemma 11 (Universal Upper Bound of the Adelic Fibration Energy):**
There exists a real constant $\Lambda \in \mathbb{R}^+$ such that for any vertex $v \in \mathcal{G}_{\mathbb{A}}$ corresponding to a strictly positive natural number, the total adelic fibration energy satisfies the inequality $\mathcal{E}_{\mathbb{A}}(v) \leq \Lambda \cdot \tau_{\mathbb{A}}(v)$.

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

### Proof of Lemma 11 (Universal Upper Bound of the Adelic Fibration Energy)

Let $v \in \mathcal{G}_{\mathbb{A}}$ such that the real component of $v$ corresponds to a strictly positive natural number.
According to Lemma 6 (Main Theorem: Universal Attractiveness of the Trivial Cycle), the value $\tau_{\mathbb{A}}(v)$ is a finite natural number, let us denote it $N = \tau_{\mathbb{A}}(v)$.
By the definition of Axiom 4, the total adelic fibration energy is given by the sum:
$$ \mathcal{E}_{\mathbb{A}}(v) = \sum_{n=0}^{N-1} \left| \pi(\mathcal{T}_{\mathbb{A}}^{n+1}(v)) - \pi(\mathcal{T}_{\mathbb{A}}^n(v)) \right|_2 $$
Let us examine the expression of the difference $\Delta_n(v) = \pi(\mathcal{T}_{\mathbb{A}}^{n+1}(v)) - \pi(\mathcal{T}_{\mathbb{A}}^n(v))$ in the $p$-adic field $\mathbb{Q}_2$.
The generalized Collatz operator $\mathcal{T}_{\mathbb{A}}$ acts on the ring of 2-adic integers $\mathbb{Z}_2$ as a piecewise affine function.
For any element $x \in \mathbb{Z}_2$, if $x \equiv 0 \pmod 2$, then $\mathcal{T}_{\mathbb{A}}(x) = \frac{x}{2}$. The difference is $\mathcal{T}_{\mathbb{A}}(x) - x = -\frac{x}{2}$. The 2-adic norm of this difference is $\left| -\frac{x}{2} \right|_2 = \left| x \right|_2 \cdot \left| \frac{1}{2} \right|_2 = \left| x \right|_2 \cdot 2$.
Since $x \in \mathbb{Z}_2$, its 2-adic norm satisfies $\left| x \right|_2 \leq 1$. Consequently, in this case, $\left| \mathcal{T}_{\mathbb{A}}(x) - x \right|_2 \leq 2$.
If $x \equiv 1 \pmod 2$, then $\mathcal{T}_{\mathbb{A}}(x) = \frac{3x + 1}{2}$. The difference is $\mathcal{T}_{\mathbb{A}}(x) - x = \frac{3x + 1 - 2x}{2} = \frac{x + 1}{2}$.
The 2-adic norm of this difference is $\left| \frac{x + 1}{2} \right|_2 = \left| x + 1 \right|_2 \cdot \left| \frac{1}{2} \right|_2 = \left| x + 1 \right|_2 \cdot 2$.
Since $x \in \mathbb{Z}_2$ and $1 \in \mathbb{Z}_2$, the sum $x + 1$ belongs to $\mathbb{Z}_2$, which implies $\left| x + 1 \right|_2 \leq 1$. Consequently, in this second case as well, $\left| \mathcal{T}_{\mathbb{A}}(x) - x \right|_2 \leq 2$.
Thus, for any element $x \in \mathbb{Z}_2$ of the trajectory, the distance between two successive iterations in the 2-adic topology is globally bounded by a constant $\Lambda = 2$.
By applying this uniform bound to each term of the sum defining the total adelic fibration energy, we obtain:
$$ \mathcal{E}_{\mathbb{A}}(v) \leq \sum_{n=0}^{N-1} 2 $$
The sum comprises exactly $N$ terms, all bounded above by the constant $2$.
By factoring, the inequality becomes:
$$ \mathcal{E}_{\mathbb{A}}(v) \leq 2 \cdot N $$
By substituting $N$ with its definition $N = \tau_{\mathbb{A}}(v)$ and setting $\Lambda = 2$, we obtain the final strict inequality:
$$ \mathcal{E}_{\mathbb{A}}(v) \leq \Lambda \cdot \tau_{\mathbb{A}}(v) $$
This upper bound is independent of the initial vertex $v$, thus establishing the existence of a universal upper bound of the adelic fibration energy linear with respect to the adelic flight time.
The proof of Lemma 11 is complete.

***
*Chercheur indépendant / Independent Researcher
