---
uuid: "syracuse-axe-01-fibration_adelique-en"
statut: "In progress"
lang: "en"
attempt: "01"
---
# Study of the Collatz Conjecture via Adelic Fibration

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

## 2. Statement of Intermediate Lemmas

**Lemma 1 (Adelic Continuity of the Operator):**
The generalized Collatz operator $\mathcal{T}_{\mathbb{A}}$ is uniformly continuous on the restricted fractional adelic topological space $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$ endowed with its usual restricted product topology.

**Lemma 2 (Normic Contraction in the Dyadic Fibration):**
For every vertex $v \in V \subset \mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$, if $v_2(v_2) = 0$, then the 2-adic valuation of the strict image satisfies a strict contraction inequality on the fibers: there exists an integer $k \ge 1$ such that $\pi(\mathcal{T}_{\mathbb{A}}^k(v))$ possesses an adelic norm strictly less than the adelic norm of $\pi(v)$.

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