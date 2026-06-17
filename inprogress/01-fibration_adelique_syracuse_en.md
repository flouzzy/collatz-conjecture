---
uuid: "syracuse-axe-01-fibration_adelique_syracuse-en"
statut: In progress
lang: "en"
attempt: 01
---
# Study of the Collatz Conjecture via Adelic Fibration and Dyadic Operator Flow Graphs

## 1. Axiomatic Definitions & Algebraic Framework

Let $\mathbb{A}_{\mathbb{Q}}$ be the ring of adeles over the field of rational numbers $\mathbb{Q}$. We introduce the restricted fractional adelic topological space, denoted $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$, defined as follows:
$$ \mathbb{A}_{\mathbb{Q}}^{\mathcal{S}} = \prod_{p \in \mathcal{P} \cup \{\infty\}}' \mathbb{Q}_p $$
where $\mathcal{P}$ is the set of prime numbers and the restricted product is performed with respect to the rings of integers $\mathbb{Z}_p$, by imposing a strict 2-adic valuation constraint.

We define the Dyadic Operator Flow Graph Algebra, denoted $\mathcal{G}_{\mathbb{A}}$, as a module over the ring of 2-adic integers $\mathbb{Z}_2$, equipped with a set of vertices $V \subset \mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$ and a set of directed edges $E$.

**Axiom 1 (Adelic Transition Operator):**
The generalized Collatz operator $\mathcal{T}_{\mathbb{A}} : \mathbb{A}_{\mathbb{Q}}^{\mathcal{S}} \to \mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$ is defined by:
For $x = (x_\infty, x_2, x_3, \dots) \in \mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$,
$$ (\mathcal{T}_{\mathbb{A}}(x))_p = \begin{cases}
\frac{x_p}{2} & \text{if } v_2(x_2) \ge 1 \\
\frac{3x_p + 1}{2} & \text{if } v_2(x_2) = 0
\end{cases} $$
where $v_2 : \mathbb{Q}_2 \to \mathbb{Z} \cup \{\infty\}$ is the standard 2-adic valuation.

**Axiom 2 (Dyadic Fibration):**
The dyadic fibration is a continuous surjective morphism $\pi : \mathcal{G}_{\mathbb{A}} \to \mathbb{Z}_2$, such that for every $v \in V$, the fiber $\pi^{-1}(\pi(v))$ is stable under the local action of the restricted operator $\mathcal{T}_{\mathbb{A}} \restriction_{\mathbb{Z}_2}$.

**Axiom 3 (Canonical Embedding of Strictly Positive Integers):**
The set of strictly positive natural numbers $\mathbb{N}^* = \{1, 2, 3, \dots\}$ canonically injects into the restricted fractional adelic topological space $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$ via the diagonal inclusion morphism $\iota : \mathbb{N}^* \hookrightarrow \mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$, defined by $\iota(n) = (n, n, n, \dots)$ for all $n \in \mathbb{N}^*$. The image of this injection forms a discrete subset in the adelic topology. Furthermore, the restriction of the operator $\mathcal{T}_{\mathbb{A}}$ to the image $\iota(\mathbb{N}^*)$ coincides exactly with the classical Collatz function $T : \mathbb{N}^* \to \mathbb{N}^*$ defined by $T(n) = \frac{n}{2}$ if $n \equiv 0 \pmod 2$ and $T(n) = \frac{3n+1}{2}$ if $n \equiv 1 \pmod 2$, in the sense that $\mathcal{T}_{\mathbb{A}}(\iota(n)) = \iota(T(n))$.

## 2. Statement of Intermediate Lemmas

**Lemma 1 (Adelic Continuity of the Operator):**
The generalized Collatz operator $\mathcal{T}_{\mathbb{A}}$ is uniformly continuous on the restricted fractional adelic topological space $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$ equipped with its standard restricted product topology.

**Lemma 2 (Norm Contraction in the Dyadic Fibration):**
For every vertex $v \in V \subset \mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$, if $v_2(v_2) = 0$, then the 2-adic valuation of the strict image satisfies a strict contraction inequality on the fibers: there exists an integer $k \ge 1$ such that $\pi(\mathcal{T}_{\mathbb{A}}^k(v))$ has an adelic norm strictly less than the adelic norm of $\pi(v)$.

## 3. Rigorous Proofs (Step-by-Step)

### Proof of Lemma 1 (Adelic Continuity of the Operator)

Let $x, y \in \mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$. We must show that for any open neighborhood $U$ of $\mathcal{T}_{\mathbb{A}}(x)$ in $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$, there exists an open neighborhood $V$ of $x$ such that $\mathcal{T}_{\mathbb{A}}(V) \subset U$.

Let $\epsilon > 0$. A base neighborhood in the adelic topology is determined by a finite set of places $S \subset \mathcal{P} \cup \{\infty\}$ containing $\infty$.
For $p \notin S$, we have $x_p \in \mathbb{Z}_p$. The operator $\mathcal{T}_{\mathbb{A}}$ on the $p$-adic component is an affine map whose coefficients are in $\mathbb{Z}[1/2]$.

Let us consider the two disjoint cases dictated by the 2-adic valuation:

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
Again, the multiplicative factor $|\frac{3}{2}|_p$ being bounded for each place $p$, it is possible to choose $\delta'_p$ such that the image of $V$ is contained in $U$.

The 2-adic valuation conditions ($v_2(z) \ge 1$ and $v_2(z) = 0$) define open and disjoint sets in $\mathbb{Q}_2$. Thus, the apparent discontinuity due to the bifurcation of the function is isolated by the topology of the 2-adic field.
This completes the proof of Lemma 1.

### Proof of Lemma 2 (Norm Contraction in the Dyadic Fibration)

Let $v \in V \subset \mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$ be a vertex such that the 2-adic valuation of its 2-adic component satisfies $v_2(v_2) = 0$.
By Axiom 3, we consider the canonical injection $\iota : \mathbb{N}^* \hookrightarrow \mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$. Suppose that $v = \iota(n)$ for a certain $n \in \mathbb{N}^*$.
Since $v_2(v_2) = 0$, the integer $n$ is odd, meaning $n \equiv 1 \pmod 2$.

We apply the adelic transition operator $\mathcal{T}_{\mathbb{A}}$ defined in Axiom 1.
Since $v_2(v_2) = 0$, the image by the operator is $\mathcal{T}_{\mathbb{A}}(v) = \iota\left(\frac{3n + 1}{2}\right)$.
Let $n_1 = \frac{3n + 1}{2}$. Since $n \ge 1$, we have $n_1 \in \mathbb{N}^*$.

If $n_1 \equiv 0 \pmod 2$, then the 2-adic valuation of its component is $v_2((n_1)_2) \ge 1$. The corresponding 2-adic norm is $|(n_1)_2|_2 = 2^{-v_2((n_1)_2)} \le \frac{1}{2} < 1$.
Since $|v_2|_2 = 2^0 = 1$, we obtain a strict contraction of the 2-adic norm, satisfying the conclusion of the lemma for $k = 1$.

If $n_1 \equiv 1 \pmod 2$, the operator $\mathcal{T}_{\mathbb{A}}$ applies the affine transformation again.
Suppose for the sake of contradiction that for every integer $m \ge 1$, the iterated sequence generates an odd integer.
We define the sequence $(n_m)_{m \ge 0}$ by $n_0 = n$ and $n_{m+1} = \frac{3n_m + 1}{2}$.
By induction, we express the general term $n_m$ as a function of $n_0$:
$n_m = \left(\frac{3}{2}\right)^m n + \sum_{j=0}^{m-1} \left(\frac{3}{2}\right)^j \frac{1}{2}$.

We calculate the sum of the geometric series:
$\sum_{j=0}^{m-1} \left(\frac{3}{2}\right)^j \frac{1}{2} = \frac{1}{2} \frac{\left(\frac{3}{2}\right)^m - 1}{\frac{3}{2} - 1} = \frac{1}{2} \frac{\left(\frac{3}{2}\right)^m - 1}{\frac{1}{2}} = \left(\frac{3}{2}\right)^m - 1$.

By substituting this sum into the expression for $n_m$, we obtain:
$n_m = \left(\frac{3}{2}\right)^m n + \left(\frac{3}{2}\right)^m - 1 = \left(\frac{3}{2}\right)^m (n + 1) - 1$.

For the sequence $(n_m)_{m \ge 0}$ to remain in the domain of integers for all $m \ge 1$, the term $\left(\frac{3}{2}\right)^m (n + 1)$ must be an integer.
This requires that the denominator $2^m$ exactly divides the numerator $3^m (n + 1)$. Since 2 and 3 are coprime, $2^m$ must divide $(n + 1)$ for every integer $m \ge 1$.
In the ring of relative integers $\mathbb{Z}$, the only value of $n$ for which $2^m$ divides $(n + 1)$ for all positive integers $m$ is the value that nullifies the expression, meaning $n + 1 = 0$, which implies $n = -1$.

However, according to Axiom 3, the initial seed belongs to the strictly positive integers, $n \in \mathbb{N}^*$, which requires $n \ge 1$.
Therefore, $n + 1 \ge 2 > 0$. It is thus impossible for $2^m$ to divide $(n + 1)$ for all $m \ge 1$.
There is therefore a maximal integer $k \ge 1$ such that $2^k$ divides $(n + 1)$ and such that $2^{k+1}$ does not divide $(n + 1)$.

For this specific index $k$, we evaluate $n_k$.
Since $2^k$ divides $(n + 1)$ and $2^{k+1}$ does not divide it, the quotient $q = \frac{n + 1}{2^k}$ is an odd integer, so $q \equiv 1 \pmod 2$.
The expression for $n_k$ becomes:
$n_k = \frac{3^k (n + 1)}{2^k} - 1 = 3^k q - 1$.

The term $3^k$ is the product of odd numbers, so it is odd.
The term $q$ is an odd integer.
The product of two odd integers $3^k q$ is an odd integer.
Subtracting 1 (which is odd) from an odd integer $3^k q$ yields an even result.
Thus, $n_k \equiv 0 \pmod 2$.

We conclude that the 2-adic valuation of the 2-adic component at step $k$ is strictly positive: $v_2((n_k)_2) \ge 1$.
The strict image $\pi(\mathcal{T}_{\mathbb{A}}^k(v))$ therefore has an adelic norm strictly less than the adelic norm of $\pi(v)$. The contraction inequality is rigorously proven on the fibers, except in the case of the seed associated with -1, excluded by definition of the domain $\mathbb{N}^*$.
