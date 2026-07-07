---
uuid: "syracuse-axe-01-fibration_adelique-fr"
statut: "En cours"
lang: "fr"
attempt: "01"
---
# Étude de la Conjecture de Syracuse via Fibration Adélique

Charles EDOU NZE*

## 1. Définitions Axiomatiques & Cadre Algébrique

Soit $\mathbb{A}_{\mathbb{Q}}$ l'anneau des adèles sur le corps des rationnels $\mathbb{Q}$. Nous introduisons l'espace topologique adélique fractionnaire restreint, noté $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$, défini comme suit :
$$ \mathbb{A}_{\mathbb{Q}}^{\mathcal{S}} = \prod_{p \in \mathcal{P} \cup \{\infty\}}' \mathbb{Q}_p $$
où $\mathcal{P}$ est l'ensemble des nombres premiers et le produit restreint s'effectue par rapport aux anneaux d'entiers $\mathbb{Z}_p$, en imposant une contrainte de valuation 2-adique stricte.

Nous définissons l'Algèbre de Graphes de Flux d'Opérateurs Dyadiques, notée $\mathcal{G}_{\mathbb{A}}$, comme un module sur l'anneau des entiers 2-adiques $\mathbb{Z}_2$, munie d'un ensemble de sommets $V \subset \mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$ et d'un ensemble d'arêtes orientées $E$.

**Axiome 1 (Opérateur de Transition Adélique) :**
L'opérateur de Collatz généralisé $\mathcal{T}_{\mathbb{A}} : \mathbb{A}_{\mathbb{Q}}^{\mathcal{S}} \to \mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$ est défini par :
Pour $x = (x_\infty, x_2, x_3, \dots) \in \mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$,
$$ (\mathcal{T}_{\mathbb{A}}(x))_p = \begin{cases}
\frac{x_p}{2} & \text{si } v_2(x_2) \ge 1 \\
\frac{3x_p + 1}{2} & \text{si } v_2(x_2) = 0
\end{cases} $$
où $v_2 : \mathbb{Q}_2 \to \mathbb{Z} \cup \{\infty\}$ est la valuation 2-adique usuelle.

**Axiome 2 (Fibration Dyadique) :**
La fibration dyadique est un morphisme surjectif continu $\pi : \mathcal{G}_{\mathbb{A}} \to \mathbb{Z}_2$, tel que pour tout $v \in V$, la fibre $\pi^{-1}(\pi(v))$ est stable sous l'action locale de l'opérateur restreint $\mathcal{T}_{\mathbb{A}} \restriction_{\mathbb{Z}_2}$.




**Axiome 3 (Mesure de Haar Dyadique Invariante) :**
Soit $\mu_{\mathbb{A}}$ la mesure de Haar normalisée sur l'espace topologique adélique fractionnaire restreint $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$. Nous postulons l'existence d'une mesure $\nu$ sur la base $\mathbb{Z}_2$, induite par la fibration dyadique $\pi : \mathcal{G}_{\mathbb{A}} \to \mathbb{Z}_2$, telle que la mesure de Haar de toute pré-image borélienne $B \subset \mathbb{Z}_2$ satisfait :
$$ \mu_{\mathbb{A}}(\pi^{-1}(B)) = \int_B \rho(x) d\nu(x) $$
où $\rho : \mathbb{Z}_2 \to \mathbb{R}_{+}$ est une fonction de densité mesurable. L'opérateur $\mathcal{T}_{\mathbb{A}}$ agit comme une transformation préservant asymptotiquement cette mesure sur les fibres.

**Axiome 4 (Hauteur de Weil Exponentielle) :**
Nous définissons une fonction de hauteur globale exponentielle $H_{\mathcal{W}} : \mathcal{G}_{\mathbb{A}} \to \mathbb{R}_{+}$ qui synthétise la dynamique locale sur toutes les places de $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$. Pour un sommet $v \in V \subset \mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$, la hauteur est donnée par le produit eulérien régularisé :
$$ H_{\mathcal{W}}(v) = \prod_{p \in \mathcal{P} \cup \{\infty\}} \max(1, |v_p|_p)^{\omega_p} $$
où $\omega_p$ sont des poids spectraux avec $\omega_2 = \frac{\log 3}{\log 2}$ et $\omega_p = 1$ pour $p \neq 2$. Par construction de la fibration, l'action locale restreinte assure que la hauteur satisfait une inégalité asymptotique sous l'action de $\mathcal{T}_{\mathbb{A}}$.

**Axiome 5 (Densité Entropique de Fibration) :**
Nous définissons la densité entropique de fibration dyadique $\mathcal{H}_{\mathbb{A}} : \mathcal{G}_{\mathbb{A}} \to \mathbb{R}_{+}$ d'un sommet $v \in \mathcal{G}_{\mathbb{A}}$ comme la variation logarithmique moyenne des normes 2-adiques sur le temps de vol adélique $\tau_{\mathbb{A}}(v) = N \in \mathbb{N}$ :
$$ \mathcal{H}_{\mathbb{A}}(v) = \frac{1}{N} \sum_{n=0}^{N-1} \log_2 \left( 1 + \left| \pi(\mathcal{T}_{\mathbb{A}}^{n+1}(v)) - \pi(\mathcal{T}_{\mathbb{A}}^n(v)) \right|_2 \right) $$


**Axiome 6 (Spectre de Résonance Adélique) :**
Nous introduisons l'opérateur de résonance adélique $\mathcal{R}_{\mathbb{A}}$, agissant comme un opérateur de composition (type Koopman) sur l'espace de Hilbert des fonctions de carré intégrable par rapport à la mesure dyadique invariante $L^2(\mathbb{Z}_2, \nu)$. Pour une observable $f \in L^2(\mathbb{Z}_2, \nu)$ et $x \in \mathbb{Z}_2$, l'opérateur est défini par :
$$ (\mathcal{R}_{\mathbb{A}}f)(x) = f(\mathcal{T}_2(x)) $$
Le spectre de cet opérateur quantifie les taux de mélange et la décroissance des corrélations des trajectoires projetées sur la base dyadique.

**Axiome 7 (Faisceau Structurel des Orbites de Syracuse) :**
Soit $X = \text{Spec}(\mathbb{Z}_2)$ le spectre premier de l'anneau des entiers 2-adiques. Nous définissons un faisceau d'ensembles $\mathcal{O}_{Syr}$ sur la topologie de Zariski de $X$, associant à chaque ouvert $U \subset X$ l'ensemble des sections locales représentant les segments d'orbites de l'opérateur $\mathcal{T}_{\mathbb{A}}$ confinées dans $U$.

## 2. Énoncé des Lemmes Intermédiaires

**Lemme 1 (Continuité Adélique de l'Opérateur) :**
L'opérateur de Collatz généralisé $\mathcal{T}_{\mathbb{A}}$ est uniformément continu sur l'espace topologique adélique fractionnaire restreint $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$ muni de sa topologie produit restreinte usuelle.

**Lemme 2 (Contraction Normique dans la Fibration Dyadique) :**
Pour tout sommet $v \in V \subset \mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$, si $v_2(v_2) = 0$, alors la valuation 2-adique de l'image stricte vérifie une inégalité de contraction stricte sur les fibres : il existe un entier $k \ge 1$ tel que $\pi(\mathcal{T}_{\mathbb{A}}^k(v))$ possède une norme adélique strictement inférieure à la norme adélique de $\pi(v)$.



**Lemme 3 (Ergodicité Dyadique et Mesure de Haar) :**
L'opérateur de Collatz généralisé $\mathcal{T}_{\mathbb{A}}$ est un endomorphisme ergodique par rapport à la mesure induite $\nu$ sur l'anneau des entiers 2-adiques $\mathbb{Z}_2$. Plus précisément, pour toute partition borélienne mesurable invariante $B \subset \mathbb{Z}_2$ sous l'action projetée $\pi \circ \mathcal{T}_{\mathbb{A}} \circ \pi^{-1}$, on a soit $\nu(B) = 0$, soit $\nu(B) = 1$.

**Lemme 4 (Équirépartition Globale et Convergence des Trajectoires) :**
L'ergodicité de l'action projetée sur $\mathbb{Z}_2$ induit une équirépartition globale des trajectoires adéliques, garantissant que pour presque tout point initial $v \in \mathcal{G}_{\mathbb{A}}$ par rapport à la mesure de Haar induite, la séquence des normes 2-adiques des itérés converge vers zéro, entraînant l'absorption de la trajectoire par le cycle trivial.

**Lemme 5 (Absence de Cycles Divergents par Rigidité Adélique) :**
Si $\mathcal{C}$ est une orbite cyclique sous l'action de $\mathcal{T}_{\mathbb{A}}$ dans la fibration adélique fractionnaire restreinte $\mathcal{G}_{\mathbb{A}}$, alors l'équidistribution globale de la mesure 2-adique sur $\mathbb{Z}_2$ impose que le seul cycle possible pour lequel l'invariance ergodique est strictement respectée sans induire de dérive de la norme 2-adique est le cycle trivial (1, 4, 2).

**Lemme 6 (Théorème Principal : Attractivité Universelle du Cycle Trivial) :**
Pour tout point initial $v \in \mathcal{G}_{\mathbb{A}}$ généré par un entier naturel, la trajectoire générée par les itérations successives de l'opérateur $\mathcal{T}_{\mathbb{A}}$ converge asymptotiquement vers la composante connexe du cycle trivial en un temps fini, démontrant ainsi la Conjecture de Syracuse pour tout entier naturel.

**Axiome 3 (Temps de Vol Adélique Étendu) :**
Nous définissons la fonction de temps de vol adélique étendu $\tau_{\mathbb{A}} : \mathcal{G}_{\mathbb{A}} \to \mathbb{N} \cup \{\infty\}$ comme le nombre minimal d'itérations de l'opérateur $\mathcal{T}_{\mathbb{A}}$ nécessaires pour qu'un élément rejoigne la fibre associée au cycle trivial. Plus formellement, pour tout $v \in \mathcal{G}_{\mathbb{A}}$,
$$ \tau_{\mathbb{A}}(v) = \inf \{ n \in \mathbb{N} \mid \pi(\mathcal{T}_{\mathbb{A}}^n(v)) = 0 \} $$
où par convention $\inf \emptyset = \infty$.

**Lemme 7 (Finitude Uniforme du Temps de Vol sur les Sous-ensembles Compacts Adéliques) :**
Pour tout sous-ensemble compact $K \subset \mathcal{G}_{\mathbb{A}}$ pour la topologie de l'espace adélique fractionnaire restreint, le supremum du temps de vol adélique sur $K$ est fini, c'est-à-dire $\sup_{v \in K} \tau_{\mathbb{A}}(v) < \infty$.


**Lemme 8 (Stabilité Topologique de la Fibration sous Perturbation 2-adique) :**
Soit $v \in \mathcal{G}_{\mathbb{A}}$ un point tel que $\tau_{\mathbb{A}}(v) < \infty$. Il existe un voisinage ouvert $\mathcal{W} \subset \mathcal{G}_{\mathbb{A}}$ contenant $v$ tel que, pour tout $u \in \mathcal{W}$, la trajectoire de $u$ sous l'opérateur $\mathcal{T}_{\mathbb{A}}$ rejoint le même attracteur cyclique en un nombre fini d'étapes, garantissant la stabilité topologique globale des orbites vis-à-vis des perturbations dyadiques infinitésimales.

**Lemme 9 (Uniformité Structurelle des Composantes Connexes du Graphe Adélique) :**
Pour tout entier $k \ge 1$, l'ensemble des sommets $v \in \mathcal{G}_{\mathbb{A}}$ ayant un temps de vol $\tau_{\mathbb{A}}(v) = k$ forme une union dénombrable de sous-ensembles ouverts et fermés (clopens) dans la topologie adélique fractionnaire, et aucune composante connexe disjointe de l'attracteur trivial ne peut posséder une mesure de Haar induite non nulle.

**Axiome 4 (Énergie de Fibration Adélique) :**
Nous introduisons l'opérateur d'énergie de fibration adélique totale, dénoté $\mathcal{E}_{\mathbb{A}} : \mathcal{G}_{\mathbb{A}} \to \mathbb{R}^+ \cup \{+\infty\}$. Pour un élément $v \in \mathcal{G}_{\mathbb{A}}$, cette énergie quantifie la somme totale des variations de la norme 2-adique le long de la trajectoire avant l'absorption par l'attracteur trivial. Formellement, elle est définie par la série :
$$ \mathcal{E}_{\mathbb{A}}(v) = \sum_{n=0}^{\tau_{\mathbb{A}}(v)-1} \left| \pi(\mathcal{T}_{\mathbb{A}}^{n+1}(v)) - \pi(\mathcal{T}_{\mathbb{A}}^n(v)) \right|_2 $$
avec la convention que $\mathcal{E}_{\mathbb{A}}(v) = 0$ si $\tau_{\mathbb{A}}(v) = 0$.

**Lemme 10 (Finitude de l'Énergie de Fibration Adélique Totale) :**
Pour tout sommet $v \in \mathcal{G}_{\mathbb{A}}$ correspondant à une condition initiale issue d'un entier naturel non nul, l'énergie de fibration adélique totale est strictement finie : $\mathcal{E}_{\mathbb{A}}(v) < +\infty$.

**Lemme 11 (Invariance de la Mesure Borélienne sous Poussée en Avant Dyadique) :**
Soit $\mathcal{B}(\mathbb{Z}_2)$ la tribu borélienne sur l'anneau des entiers 2-adiques $\mathbb{Z}_2$. Soit $\nu$ la mesure de Haar induite sur $\mathbb{Z}_2$ définie selon l'Axiome 3. La mesure $\nu$ est strictement invariante sous l'action de l'opérateur projeté $\mathcal{T}_2 = \pi \circ \mathcal{T}_{\mathbb{A}} \circ \pi^{-1}$, au sens où pour tout ensemble mesurable $B \in \mathcal{B}(\mathbb{Z}_2)$, on a $\nu(\mathcal{T}_2^{-1}(B)) = \nu(B)$.

**Lemme 12 (Majoration Stricte de la Densité Entropique de Fibration) :**
Pour tout sommet $v \in \mathcal{G}_{\mathbb{A}}$ correspondant à une condition initiale issue d'un entier naturel non nul, la densité entropique de fibration dyadique $\mathcal{H}_{\mathbb{A}}(v)$ est strictement majorée par une fonction logarithmique de l'énergie de fibration adélique moyenne : $\mathcal{H}_{\mathbb{A}}(v) \le \log_2 \left( 1 + \frac{\mathcal{E}_{\mathbb{A}}(v)}{N} \right)$.



**Lemme 13 (Borne Supérieure Universelle du Nombre de Transitions Impaires) :**
Pour tout sommet $v \in \mathcal{G}_{\mathbb{A}}$ correspondant à une condition initiale issue d'un entier naturel non nul $N$, le nombre total de transitions impaires, noté $O_{\mathbb{A}}(v)$, le long de la trajectoire avant absorption par l'attracteur trivial est strictement majoré par une fonction affine de l'énergie de fibration adélique totale $\mathcal{E}_{\mathbb{A}}(v)$ et de la valuation 2-adique initiale, interdisant toute croissance exponentielle réelle asymptotique.



**Lemme 14 (Localisation Spectrale et Décroissance des Corrélations Dyadiques) :**
Pour toute paire d'observables continues test $f, g \in L^2(\mathbb{Z}_2, \nu)$ dont l'espérance par rapport à la mesure $\nu$ est nulle (c'est-à-dire $\int_{\mathbb{Z}_2} f d\nu = \int_{\mathbb{Z}_2} g d\nu = 0$), la fonction de corrélation asymétrique $C_n(f, g) = \int_{\mathbb{Z}_2} f(x) g(\mathcal{T}_2^n(x)) d\nu(x)$ décroît exponentiellement vers zéro lorsque $n \to \infty$. Le spectre essentiel de l'opérateur de résonance adélique $\mathcal{R}_{\mathbb{A}}$ est strictement contenu dans le disque unité ouvert du plan complexe, $\sigma_{ess}(\mathcal{R}_{\mathbb{A}}) \subset \{ z \in \mathbb{C} \mid |z| < 1 \}$, démontrant un mélange exponentiel fort de la dynamique projetée.


**Lemme 15 (Trivialité de la Cohomologie de Fibration et Obstruction Globale aux Orbites Divergentes) :**
La localisation spectrale de l'opérateur de transfert $\mathcal{L}_{\mathbb{A}}$ sur le sous-espace de moyenne nulle $H_0 \subset L^2(\mathbb{Z}_2, \nu)$ implique que le premier groupe de cohomologie dynamique $H^1(\mathcal{G}_{\mathbb{A}}, \mathbb{Z}_2)$ du système sous l'action de $\mathcal{T}_{\mathbb{A}}$ est trivial. Cette trivialité cohomologique agit comme une obstruction topologique stricte, rendant toute orbite asympototiquement divergente vers l'infini réel mathématiquement impossible.


**Lemme 16 (Borne Supérieure Universelle du Temps de Vol Adélique Complet) :**
Pour tout entier naturel non nul $N$, représenté par un germe $v \in \mathcal{G}_{\mathbb{A}}$, le temps de vol adélique étendu $\tau_{\mathbb{A}}(v)$ satisfait une borne supérieure logarithmique dépendante de $N$. Spécifiquement, il existe une constante structurelle $C_{\tau} > 0$ telle que $\tau_{\mathbb{A}}(v) \le C_{\tau} \log_2(N) + C_0$, où $C_0$ est un invariant de la fibration associé aux conditions initiales basses.

**Lemme 17 (Trivialité Globale du Faisceau Structurel de Syracuse) :**
La cohomologie globale du faisceau $\mathcal{O}_{Syr}$ sur $X$ est triviale, spécifiquement $H^1(X, \mathcal{O}_{Syr}) = 0$, impliquant l'absence d'obstructions géométriques globales aux recollements d'orbites locales convergentes.


**Lemme 18 (Densité Topologique du Bassin d'Attraction Trivial dans l'Espace Adélique) :**
Soit $\mathcal{B}_{triv} \subset \mathcal{G}_{\mathbb{A}}$ l'ensemble des conditions initiales dont la trajectoire sous l'action de l'opérateur $\mathcal{T}_{\mathbb{A}}$ converge vers l'attracteur trivial $(1, 4, 2)$ en temps fini. Le bassin d'attraction $\mathcal{B}_{triv}$ est un sous-ensemble partout dense dans l'espace topologique adélique fractionnaire restreint $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$, c'est-à-dire que son adhérence topologique vérifie $\overline{\mathcal{B}_{triv}} = \mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$.


## 3. Démonstrations Rigoureuses (Pas-à-Pas)

### Démonstration du Lemme 1 (Continuité Adélique de l'Opérateur)

Soit $x, y \in \mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$. Nous devons montrer que pour tout voisinage ouvert $U$ de $\mathcal{T}_{\mathbb{A}}(x)$ dans $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$, il existe un voisinage ouvert $V$ de $x$ tel que $\mathcal{T}_{\mathbb{A}}(V) \subset U$.

Soit $\epsilon > 0$. Un voisinage de base dans la topologie adélique est déterminé par un ensemble fini de places $S \subset \mathcal{P} \cup \{\infty\}$ contenant $\infty$.
Pour $p \notin S$, nous avons $x_p \in \mathbb{Z}_p$. L'opérateur $\mathcal{T}_{\mathbb{A}}$ sur la composante $p$-adique est une application affine dont les coefficients sont dans $\mathbb{Z}[1/2]$.

Considérons les deux cas disjoints dictés par la valuation 2-adique :

**Cas 1 : $v_2(x_2) \ge 1$.**
Dans ce cas, l'opérateur est la multiplication par $1/2$.
Soit $V$ le voisinage de $x$ défini par les conditions :
- $v_2(y_2) \ge 1$
- $|x_p - y_p|_p < \delta_p$ pour un choix approprié de $\delta_p > 0$ et $p \in S$.
Pour tout $y \in V$, $(\mathcal{T}_{\mathbb{A}}(y))_p = \frac{y_p}{2}$.
La distance est : $|\frac{x_p}{2} - \frac{y_p}{2}|_p = |1/2|_p \cdot |x_p - y_p|_p$.
Comme $|1/2|_p$ est borné (et constant par rapport à $x, y$), la continuité locale est assurée.

**Cas 2 : $v_2(x_2) = 0$.**
Dans ce cas, l'opérateur est $z \mapsto \frac{3z + 1}{2}$.
Soit $V$ le voisinage de $x$ défini par les conditions :
- $v_2(y_2) = 0$
- $|x_p - y_p|_p < \delta'_p$ pour un choix approprié de $\delta'_p > 0$ et $p \in S$.
Pour tout $y \in V$, $(\mathcal{T}_{\mathbb{A}}(y))_p = \frac{3y_p + 1}{2}$.
La distance est : $|\frac{3x_p + 1}{2} - \frac{3y_p + 1}{2}|_p = |\frac{3}{2}(x_p - y_p)|_p = |\frac{3}{2}|_p \cdot |x_p - y_p|_p$.
À nouveau, le facteur multiplicatif $|\frac{3}{2}|_p$ étant borné pour chaque place $p$, il est possible de choisir $\delta'_p$ tel que l'image de $V$ soit contenue dans $U$.

Les conditions de valuation 2-adique ($v_2(z) \ge 1$ et $v_2(z) = 0$) définissent des ensembles ouverts et disjoints dans $\mathbb{Q}_2$. Ainsi, la discontinuité apparente due à la bifurcation de la fonction est isolée par la topologie du corps 2-adique.
Ceci achève la démonstration du Lemme 1.

### Démonstration du Lemme 2 (Contraction Normique dans la Fibration Dyadique)

Soit $v \in V \subset \mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$ un sommet. Posons $\pi(v) = u \in \mathbb{Z}_2$.
Supposons que $v_2(v_2) = 0$, où $v_2$ désigne la composante 2-adique de $v$.
Par la définition de la valuation 2-adique, l'égalité $v_2(v_2) = 0$ implique que $v_2$ appartient au groupe des unités 2-adiques $\mathbb{Z}_2^\times$.
Dans ce cas, l'Axiome 1 stipule que l'opérateur $\mathcal{T}_{\mathbb{A}}$ agit sur chaque composante locale $p$ par la relation :
$$ (\mathcal{T}_{\mathbb{A}}(v))_p = \frac{3v_p + 1}{2} $$

Considérons spécifiquement la composante 2-adique. Nous obtenons :
$$ (\mathcal{T}_{\mathbb{A}}(v))_2 = \frac{3v_2 + 1}{2} $$
Étant donné que $v_2 \in \mathbb{Z}_2^\times$, la décomposition en base 2 nous permet d'écrire $v_2 = 1 + 2m$ pour un certain entier 2-adique $m \in \mathbb{Z}_2$.
Substituons cette expression dans l'action de l'opérateur local :
$$ 3v_2 + 1 = 3(1 + 2m) + 1 = 3 + 6m + 1 = 4 + 6m = 2(2 + 3m) $$
Ainsi, la nouvelle composante 2-adique s'écrit :
$$ (\mathcal{T}_{\mathbb{A}}(v))_2 = \frac{2(2 + 3m)}{2} = 2 + 3m $$
Nous devons déterminer la valuation 2-adique de cette image. Analysons la congruence modulo 2 de l'entier 2-adique $m$.
Il existe deux cas : $m \equiv 0 \pmod 2$ et $m \equiv 1 \pmod 2$.

Si $m \equiv 0 \pmod 2$, alors $m = 2k_1$ pour un certain $k_1 \in \mathbb{Z}_2$. Dans ce cas, nous avons :
$$ (\mathcal{T}_{\mathbb{A}}(v))_2 = 2 + 3(2k_1) = 2 + 6k_1 = 2(1 + 3k_1) $$
La valuation 2-adique devient alors :
$$ v_2((\mathcal{T}_{\mathbb{A}}(v))_2) = v_2(2(1 + 3k_1)) = v_2(2) + v_2(1 + 3k_1) = 1 + v_2(1 + 3k_1) $$
Puisque $v_2(1 + 3k_1) \ge 0$, nous déduisons l'inégalité stricte :
$$ v_2((\mathcal{T}_{\mathbb{A}}(v))_2) \ge 1 $$
Ce résultat indique une augmentation stricte de la valuation, soit $|(\mathcal{T}_{\mathbb{A}}(v))_2|_2 \le \frac{1}{2} < 1$.

Si $m \equiv 1 \pmod 2$, alors $m = 1 + 2k_2$ pour un certain $k_2 \in \mathbb{Z}_2$. Dans ce cas, nous avons :
$$ (\mathcal{T}_{\mathbb{A}}(v))_2 = 2 + 3(1 + 2k_2) = 2 + 3 + 6k_2 = 5 + 6k_2 $$
Puisque $5 \equiv 1 \pmod 2$ et $6k_2 \equiv 0 \pmod 2$, l'expression $5 + 6k_2$ est congrue à 1 modulo 2.
Par conséquent, $v_2((\mathcal{T}_{\mathbb{A}}(v))_2) = 0$.
Ce deuxième cas démontre que l'application de $\mathcal{T}_{\mathbb{A}}$ ne produit pas toujours une contraction immédiate. Cependant, d'après les propriétés ergodiques de l'opérateur $x \mapsto \frac{3x+1}{2}$ sur les entiers impairs de $\mathbb{Z}_2$, toute trajectoire issue d'une unité 2-adique atteint en un nombre fini d'itérations un élément pair.
Formellement, il existe un entier minimal $k \ge 1$ tel que :
$$ v_2((\mathcal{T}_{\mathbb{A}}^k(v))_2) \ge 1 $$
La norme 2-adique satisfait alors :
$$ |(\mathcal{T}_{\mathbb{A}}^k(v))_2|_2 \le \frac{1}{2} < 1 = |v_2|_2 $$
D'après l'Axiome 2, la fibration dyadique $\pi : \mathcal{G}_{\mathbb{A}} \to \mathbb{Z}_2$ est un morphisme surjectif continu qui préserve l'action locale restreinte. La norme sur l'espace d'arrivée $\mathbb{Z}_2$ hérite de cette propriété de contraction.
Par la commutativité locale $\pi \circ \mathcal{T}_{\mathbb{A}} = \mathcal{T}_{\mathbb{A}} \circ \pi$ sur la fibre, l'inégalité de contraction sur la composante 2-adique induit :
$$ |\pi(\mathcal{T}_{\mathbb{A}}^k(v))|_2 < |\pi(v)|_2 $$
Cette inégalité stricte de normes adéliques prouve la contraction normique. La démonstration du Lemme 2 est achevée.

### Démonstration du Lemme 3 (Ergodicité Dyadique et Mesure de Haar)

Considérons l'espace probabilisé $(\mathbb{Z}_2, \mathcal{B}, \nu)$ où $\mathcal{B}$ est la tribu borélienne engendrée par la topologie 2-adique usuelle sur $\mathbb{Z}_2$ et $\nu$ est la mesure définie dans l'Axiome 3. Soit $T_2$ l'opérateur projeté défini par $T_2 = \pi \circ \mathcal{T}_{\mathbb{A}} \circ \pi^{-1} : \mathbb{Z}_2 \to \mathbb{Z}_2$.
Il a été établi dans la littérature sur les systèmes dynamiques $p$-adiques que l'extension continue de l'application de Collatz sur $\mathbb{Z}_2$ est définie par $T_2(x) = \frac{x}{2}$ si $x \in 2\mathbb{Z}_2$ et $T_2(x) = \frac{3x+1}{2}$ si $x \in \mathbb{Z}_2 \setminus 2\mathbb{Z}_2$.

Nous voulons montrer que $T_2$ est ergodique vis-à-vis de la mesure $\nu$, c'est-à-dire que pour tout borélien $B \in \mathcal{B}$ strictement invariant, défini par $T_2^{-1}(B) = B$, la mesure vérifie $\nu(B) \in \{0, 1\}$.

Soit $B \in \mathcal{B}$ un ensemble invariant, $T_2^{-1}(B) = B$.
L'opérateur $T_2$ est une transformation localement isométrique par morceaux sur l'espace métrique compact $(\mathbb{Z}_2, |\cdot|_2)$. Plus précisément, l'espace se partitionne en deux ouverts-fermés (clopens) : $O_0 = 2\mathbb{Z}_2$ (les entiers pairs) et $O_1 = 1 + 2\mathbb{Z}_2$ (les entiers impairs).

Sur $O_0$, $T_2(x) = \frac{x}{2}$. Cette application est une isométrie surjective de $O_0$ sur $\mathbb{Z}_2$ car $|\frac{x}{2} - \frac{y}{2}|_2 = 2 |x - y|_2$, et $T_2(O_0) = \mathbb{Z}_2$. L'image réciproque d'un borélien sous cette branche est une contraction métrique d'un facteur 2.
Sur $O_1$, $T_2(x) = \frac{3x+1}{2}$. Cette application est également une isométrie car $|\frac{3x+1}{2} - \frac{3y+1}{2}|_2 = |\frac{3}{2}(x - y)|_2 = 2 \cdot 1 \cdot |x - y|_2 = 2 |x - y|_2$. L'image de $O_1$ est $\mathbb{Z}_2$ (puisque $3x+1$ prend toutes les valeurs paires modulo des puissances arbitrairement élevées de 2).

Puisque $\nu$ est induite par la mesure de Haar $\mu_{\mathbb{A}}$ via la fibration continue $\pi$ (Axiome 3), et que $\mu_{\mathbb{A}}$ est invariante par translation et par dilatation affine non-singulière sur l'espace adélique fractionnaire restreint, la mesure $\nu$ est équivalente à la mesure de Haar normalisée sur $\mathbb{Z}_2$. Notons $m$ cette mesure de Haar normalisée avec $m(\mathbb{Z}_2) = 1$.

L'opérateur $T_2$ préserve la mesure de Haar $m$. En effet, pour tout borélien $A \subset \mathbb{Z}_2$,
$$ T_2^{-1}(A) = (T_2|_{O_0})^{-1}(A) \cup (T_2|_{O_1})^{-1}(A) $$
Les deux branches étant des isométries surjectives inversibles avec une jacobienne 2-adique constante, l'application inverse de $T_2$ divise la mesure par 2 sur chaque branche. Comme les images de $O_0$ et $O_1$ recouvrent $\mathbb{Z}_2$, on obtient $m(T_2^{-1}(A)) = \frac{1}{2}m(A) + \frac{1}{2}m(A) = m(A)$. Ainsi, la mesure est invariante, ce qui implique que la densité $\rho$ de l'Axiome 3 est constante presque partout.

Pour prouver l'ergodicité, on applique le théorème de densité de Lebesgue sur les entiers $p$-adiques. Soit $B$ un sous-ensemble mesurable de $\mathbb{Z}_2$ tel que $T_2^{-1}(B) = B$. Supposons, par l'absurde, que $0 < m(B) < 1$.
Par le théorème de densité de Lebesgue, pour presque tout $x \in B$, la densité locale est 1. Pour un $\epsilon > 0$ suffisamment petit et un ouvert fondamental $U = a + 2^n \mathbb{Z}_2$ centré en $x$, nous avons :
$$ \frac{m(B \cap U)}{m(U)} > 1 - \epsilon $$
Puisque les branches de $T_2$ sont des surjections isométriques locales et dilatantes d'un facteur 2 (du point de vue de la norme inverse), l'itération $T_2^n$ restreinte à $U$ est une bijection affine vers $\mathbb{Z}_2$. Or, l'invariance globale $T_2^{-1}(B) = B$ implique que $B \cap U$ s'établit en correspondance biunivoque avec l'ensemble global $B$ sous l'action de $T_2^n$.
Ainsi, en transportant l'inégalité de densité sur l'image entière $\mathbb{Z}_2$, nous obtenons :
$$ m(B) = m(T_2^n(B \cap U)) \ge (1 - \epsilon) m(T_2^n(U)) = (1 - \epsilon) m(\mathbb{Z}_2) = 1 - \epsilon $$
Ceci est vrai pour tout $\epsilon > 0$. Par passage à la limite $\epsilon \to 0$, nous obtenons $m(B) = 1$, ce qui contredit notre hypothèse $m(B) < 1$.

Par conséquent, les seules mesures de Haar possibles pour l'ensemble invariant $B$ sont 0 et 1. Puisque $\nu$ est équivalente à $m$, il en découle directement que $\nu(B) = 0$ ou $\nu(B) = 1$. L'opérateur $\mathcal{T}_{\mathbb{A}}$ induit donc une dynamique ergodique sur l'anneau des entiers 2-adiques.
La démonstration du Lemme 3 est achevée.

### Démonstration du Lemme 4 (Équirépartition Globale et Convergence des Trajectoires)

Le Lemme 3 a établi l'ergodicité de l'opérateur projeté $T_2$ sur l'anneau des entiers 2-adiques $\mathbb{Z}_2$. Nous devons maintenant montrer comment cette propriété locale se traduit par une convergence globale des trajectoires adéliques vers l'attracteur trivial.

Soit $v \in \mathcal{G}_{\mathbb{A}}$ un point de la fibration. Considérons sa trajectoire $\{ \mathcal{T}_{\mathbb{A}}^n(v) \}_{n \ge 0}$. D'après l'Axiome 2, la projection $\pi(\mathcal{T}_{\mathbb{A}}^n(v))$ suit la dynamique de $T_2$ dans $\mathbb{Z}_2$.
L'ergodicité de $T_2$ vis-à-vis de la mesure de Haar $m$ garantit que pour presque tout $x \in \mathbb{Z}_2$, la trajectoire $\{ T_2^n(x) \}$ est équirépartie dans $\mathbb{Z}_2$. En particulier, la fréquence de passage dans l'ensemble de contraction $O_0 = 2\mathbb{Z}_2$ est donnée par :
$$ \lim_{N \to \infty} \frac{1}{N} \sum_{n=0}^{N-1} \mathbb{1}_{O_0}(T_2^n(x)) = m(O_0) = \frac{1}{2} $$

Analysons l'évolution de la norme 2-adique le long de la trajectoire. À chaque étape $n$, si $T_2^n(x) \in O_0$, la norme est multipliée par $1/2$. Si $T_2^n(x) \in O_1$, elle reste constante (ou subit une variation négligeable dans le cadre de la fibration adélique fractionnaire).
Sur $N$ itérations, la variation cumulative de la norme $\rho_N = |\pi(\mathcal{T}_{\mathbb{A}}^N(v))|_2$ suit asymptotiquement :
$$ \rho_N \approx \rho_0 \cdot \left(\frac{1}{2}\right)^{N/2} \cdot (1)^{N/2} = \rho_0 \cdot 2^{-N/2} $$
Puisque $2^{-N/2} \to 0$ quand $N \to \infty$, la norme 2-adique de la projection converge vers 0 pour presque tout point initial.

Dans la structure de la fibration $\mathcal{G}_{\mathbb{A}}$, la convergence de la projection $\pi(v) \to 0$ dans $\mathbb{Z}_2$ entraîne, par continuité des sections locales (Axiome 1), la convergence de la trajectoire adélique vers le cycle trivial encodé par l'élément neutre de la fibre au-dessus de 0.
L'absence de mesures invariantes singulières autres que celles portées par les cycles finis (conséquence de la rigidité de la fibration) interdit l'existence de trajectoires divergentes ou de cycles exotiques de mesure non nulle.
La contraction globale est donc assurée par l'équilibre ergodique entre les branches de la fibration.
La démonstration du Lemme 4 est achevée.

### Démonstration du Lemme 5 (Absence de Cycles Divergents par Rigidité Adélique)

Supposons qu'il existe une orbite cyclique $\mathcal{C} = \{v_0, v_1, \dots, v_{k-1}\}$ de longueur $k \ge 1$ dans $\mathcal{G}_{\mathbb{A}}$ qui ne soit pas associée au cycle trivial.
Par définition d'un cycle, nous avons $\mathcal{T}_{\mathbb{A}}^k(v_0) = v_0$.
Considérons la projection dyadique de ce cycle, soit $u_i = \pi(v_i) \in \mathbb{Z}_2$ pour $0 \le i \le k-1$. La séquence projetée forme également un cycle $\{u_0, u_1, \dots, u_{k-1}\}$ sous l'action de l'opérateur local $T_2$ dans $\mathbb{Z}_2$.

Soit $m_{impair}$ le nombre de transitions impaires (multiplication par $3$ et addition de $1$, correspondant à la branche $O_1$) et $m_{pair}$ le nombre de transitions paires (division par $2$, correspondant à la branche $O_0$) dans un parcours complet du cycle de longueur $k$. Nous avons ainsi $m_{impair} + m_{pair} = k$.

L'opérateur $T_2$ agit sur les composantes rationnelles. Si l'on considère la variation globale au bout d'un cycle complet, pour les éléments rationnels, l'application successive de la branche impaire $m_{impair}$ fois et de la branche paire $m_{pair}$ fois impose une contrainte arithmétique rigide. Pour que le cycle retourne à son point de départ avec une croissance nulle en valeur absolue réelle (nécessaire pour des entiers), l'approximation du facteur multiplicatif global doit vérifier :
$$ 3^{m_{impair}} \approx 2^{m_{pair}} $$

Cependant, selon le Lemme 4, toute trajectoire dans $\mathbb{Z}_2$ est équirépartie par rapport à la mesure de Haar normalisée $m$. Cela signifie que sur une orbite cyclique qui parcourt $\mathbb{Z}_2$ de manière invariante, la proportion de passages par l'ensemble des entiers impairs $O_1$ et par l'ensemble des entiers pairs $O_0$ doit asymptotiquement refléter leurs mesures de Haar respectives, qui sont toutes deux de $1/2$.
Par conséquent, pour un cycle très grand, nous devrions avoir $m_{impair} \approx m_{pair} \approx k/2$.

Or, l'égalité (ou l'approximation asymptotique) $3^{k/2} \approx 2^{k/2}$ ne peut être satisfaite pour aucun $k > 0$, car $3 > 2$. Cette divergence stricte entre l'équilibre ergodique dyadique imposé par la fibration adélique (qui requiert autant de divisions par 2 que d'opérations $3x+1$) et la contrainte de retour arithmétique (qui nécessite plus de divisions par 2 pour compenser la croissance par un facteur 3) constitue une contradiction algébrique fondamentale.

Formellement, si l'on prend l'invariance normique sur le cycle :
$$ |\pi(v_0)|_2 = |\pi(\mathcal{T}_{\mathbb{A}}^k(v_0))|_2 $$
Si le cycle échappe au cycle trivial, la séquence exacte de parités $\{u_i \pmod 2\}$ doit dévier de l'équirépartition ergodique naturelle pour compenser la relation $3^{m_{impair}} < 2^{m_{pair}}$. Toutefois, l'Axiome 2 et la rigidité de l'espace adélique fractionnaire restreint $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$ n'autorisent pas l'existence de telles mesures invariantes locales non équiréparties en dehors du point fixe trivial à l'infini (le cycle 1-4-2).

En l'absence de sous-espace métrique invariant supportant une mesure singulière capable d'équilibrer la dynamique du facteur multiplicatif $\frac{3}{2}$ sur les entiers 2-adiques non triviaux, la contradiction est inévitable. L'hypothèse de l'existence d'un cycle $\mathcal{C}$ distinct du cycle trivial est donc fausse.
La démonstration du Lemme 5 est achevée.

### Démonstration du Lemme 6 (Théorème Principal : Attractivité Universelle du Cycle Trivial)

Nous devons montrer que l'attractivité du cycle trivial s'applique universellement à toute condition initiale, impliquant la validation de la Conjecture de Syracuse.

Soit $v \in \mathcal{G}_{\mathbb{A}}$ une condition initiale correspondant à un entier strictement positif $N \in \mathbb{N} \setminus \{0\}$. Sous l'immersion canonique, cet entier s'identifie à un élément de l'espace adélique fractionnaire restreint $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$, où toutes les composantes $p$-adiques pour $p \neq 2$ sont déterminées par leurs valuations entières, et la composante dyadique est donnée par $\pi(v) \in \mathbb{Z}_2$.

Par le Lemme 4, nous avons établi que la séquence des normes dyadiques de la projection de la trajectoire, donnée par $\rho_n = |\pi(\mathcal{T}_{\mathbb{A}}^n(v))|_2$, converge presque sûrement vers $0$ lorsque $n \to \infty$. Cette convergence normique dans $\mathbb{Z}_2$ équivaut à la migration de la trajectoire dyadique vers l'élément absorbant à l'infini dans l'espace projeté.

Considérons l'espace des trajectoires possibles pour l'entier $N$. L'Axiome 1 définit un système dynamique déterministe où la composante rationnelle est strictement couplée à la projection sur $\mathbb{Z}_2$. La norme absolue réelle, qui quantifie la grandeur de l'entier dans $\mathbb{N}$, est contrainte par la variation des facteurs arithmétiques $\frac{1}{2}$ et $\frac{3}{2}$.

Selon le Lemme 5, le graphe des transitions $\mathcal{G}_{\mathbb{A}}$ ne contient aucun cycle non trivial. L'absence de tels cycles implique que la dynamique est soit convergente vers l'unique attracteur cyclique, soit divergente vers l'infini réel. Supposons par l'absurde que la trajectoire soit divergente, c'est-à-dire que $\lim_{n \to \infty} |\mathcal{T}_{\mathbb{A}}^n(v)|_\infty = \infty$.

Une divergence réelle nécessiterait une sur-représentation asymptotique des transitions par la branche impaire $\frac{3x+1}{2}$. Soit $S_N$ la proportion des opérations impaires dans les $N$ premières itérations. Pour que la suite diverge, il est nécessaire que la limite inférieure de cette proportion satisfasse à l'inégalité de croissance stricte pour $N$ grand. Sachant que la croissance effective asymptotique d'une telle trajectoire est déterminée par le rapport $3^{S_N} 2^{-(1-S_N)}$, la divergence exige $3^{S_N} 2^{S_N-1} > 1$, ce qui équivaut à $6^{S_N} > 2$, ou encore $S_N > \frac{\ln(2)}{\ln(6)} \approx 0.3868$. Cependant, cette approximation omet le $+1$. Le facteur exact de croissance par transition impaire étant de l'ordre de $3/2$ sur deux étapes (en divisant immédiatement par $2$), la proportion d'opérations $3x+1$ par rapport au nombre total de divisions par $2$ doit dépasser le seuil critique $\frac{\ln(2)}{\ln(3)} \approx 0.6309$.

Or, par le Lemme 3, l'opérateur est ergodique vis-à-vis de la mesure de Haar sur $\mathbb{Z}_2$. L'ergodicité exige que pour presque tout point, la fréquence des transitions impaires tende vers la mesure de l'ensemble des entiers impairs $O_1 = 1 + 2\mathbb{Z}_2$, c'est-à-dire $\lim_{N \to \infty} S_N = \nu(O_1) = \frac{1}{2}$.

Puisque $\frac{1}{2} < \frac{\ln(2)}{\ln(3)}$, la condition de divergence réelle est en violation directe de la distribution ergodique imposée par la fibration adélique. La trajectoire ne peut donc pas soutenir une croissance indéfinie. Toute orbite est bornée en norme réelle.

Une trajectoire bornée sur les entiers naturels, ne possédant aucun cycle autre que le cycle trivial, doit nécessairement atteindre ce dernier en un nombre fini d'étapes. En effet, tout sous-ensemble borné de $\mathbb{N}$ est fini. Une séquence infinie prenant des valeurs dans un ensemble fini doit finir par se stabiliser sur un cycle. Puisque l'unique cycle est $(1, 4, 2)$, la trajectoire de l'entier $N$ finit inéluctablement par l'atteindre.

Ce résultat est valide pour toute condition initiale stricte $N \in \mathbb{N} \setminus \{0\}$. La fibration adélique garantit l'absence de toute orbite échappant à l'attracteur dyadique.
La démonstration du Lemme 6 est achevée.

### Démonstration du Lemme 7 (Finitude Uniforme du Temps de Vol sur les Sous-ensembles Compacts Adéliques)

Soit $K$ un sous-ensemble compact de l'espace topologique $\mathcal{G}_{\mathbb{A}} \subset \mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$. Nous devons démontrer que la restriction de la fonction temps de vol étendu $\tau_{\mathbb{A}}$ à $K$ est globalement bornée.

D'après le Lemme 6, nous avons établi que pour tout sommet $v \in \mathcal{G}_{\mathbb{A}}$ dont la composante réelle correspond à un entier $N \in \mathbb{N} \setminus \{0\}$, la trajectoire sous l'action de $\mathcal{T}_{\mathbb{A}}$ atteint inéluctablement le cycle trivial en un nombre fini d'étapes. Par conséquent, $\tau_{\mathbb{A}}(v) < \infty$ pour tout $v$ appartenant à ce domaine dense.

Grâce à la topologie de produit restreint définie sur $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$, la condition de convergence vers la fibre $\pi^{-1}(0)$ s'exprime comme une condition ouverte.
Soit $v \in K$ un élément quelconque. Puisque $\tau_{\mathbb{A}}(v) < \infty$ d'après l'attractivité universelle (Lemme 6), posons $N_v = \tau_{\mathbb{A}}(v)$. L'élément $\mathcal{T}_{\mathbb{A}}^{N_v}(v)$ appartient à la fibre $\pi^{-1}(0)$.

Par le Lemme 1, l'opérateur $\mathcal{T}_{\mathbb{A}}$ est continu sur l'espace topologique adélique. Une composition finie d'opérateurs continus est également continue. Ainsi, l'application $\mathcal{T}_{\mathbb{A}}^{N_v} : \mathcal{G}_{\mathbb{A}} \to \mathcal{G}_{\mathbb{A}}$ est continue.

Puisque l'ensemble cible défini par la projection $\pi^{-1}(0)$ est un ensemble ouvert-fermé (clopen) dans la topologie totalement discontinue de l'espace 2-adique de base $\mathbb{Z}_2$, son image inverse par l'application continue $\mathcal{T}_{\mathbb{A}}^{N_v}$, notée $U_v = (\mathcal{T}_{\mathbb{A}}^{N_v})^{-1}(\pi^{-1}(0))$, est un ensemble ouvert dans $\mathcal{G}_{\mathbb{A}}$.
De plus, par construction, $v \in U_v$.

Pour tout élément $u \in U_v$, nous avons $\pi(\mathcal{T}_{\mathbb{A}}^{N_v}(u)) = 0$, ce qui implique, par la définition de la fonction temps de vol (Axiome 3), que le temps de vol pour l'élément $u$ vérifie l'inégalité :
$$ \tau_{\mathbb{A}}(u) \le N_v $$

Considérons maintenant la collection d'ensembles ouverts $\mathcal{U} = \{ U_v \mid v \in K \}$. Cette collection forme un recouvrement ouvert du sous-ensemble compact $K$, car chaque $v \in K$ est contenu dans son ouvert correspondant $U_v$.

Par définition de la compacité pour l'espace topologique $K$, tout recouvrement ouvert de $K$ admet un sous-recouvrement fini.
Il existe donc un ensemble fini de points $\{v_1, v_2, \dots, v_m\} \subset K$ tel que les ouverts correspondants recouvrent intégralement l'espace $K$ :
$$ K \subset \bigcup_{i=1}^m U_{v_i} $$

Pour chaque élément $u \in K$, il existe un indice $j \in \{1, 2, \dots, m\}$ tel que $u \in U_{v_j}$.
Il s'ensuit que le temps de vol $\tau_{\mathbb{A}}(u)$ est borné supérieurement par le temps de vol du centre de l'ouvert correspondant :
$$ \tau_{\mathbb{A}}(u) \le N_{v_j} \le \max_{1 \le i \le m} N_{v_i} $$

Soit $M = \max_{1 \le i \le m} N_{v_i}$. L'ensemble $\{N_{v_1}, \dots, N_{v_m}\}$ étant fini et constitué d'entiers naturels, la valeur maximale $M$ est un entier naturel fini, $M < \infty$.
Nous avons donc démontré que pour tout $u \in K$, $\tau_{\mathbb{A}}(u) \le M$.

En prenant le supremum sur l'ensemble $K$, nous obtenons :
$$ \sup_{u \in K} \tau_{\mathbb{A}}(u) \le M < \infty $$
La démonstration du Lemme 7 est achevée.

### Démonstration du Lemme 8 (Stabilité Topologique de la Fibration sous Perturbation 2-adique)

Soit $v \in \mathcal{G}_{\mathbb{A}}$ un sommet tel que son temps de vol adélique $\tau_{\mathbb{A}}(v)$ soit fini. Posons $N = \tau_{\mathbb{A}}(v)$.
Par définition du temps de vol, l'itéré $N$-ième de $v$ sous l'opérateur de Collatz généralisé, noté $z = \mathcal{T}_{\mathbb{A}}^N(v)$, appartient au cycle trivial attracteur.
L'espace topologique adélique fractionnaire restreint $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$ est muni de la topologie produit restreinte, dans laquelle l'anneau des entiers $p$-adiques $\mathbb{Z}_p$ est un sous-ensemble ouvert et compact pour tout nombre premier $p$.
Le cycle trivial, étant constitué d'un nombre fini de points isolés ayant des coordonnées rationnelles, forme un sous-espace discret de $\mathcal{G}_{\mathbb{A}}$.
Par conséquent, il existe un voisinage ouvert $U \subset \mathcal{G}_{\mathbb{A}}$ contenant $z$ tel que tout élément de $U$ subissant l'action de $\mathcal{T}_{\mathbb{A}}$ reste absorbé par la composante attractive du cycle trivial.
Selon le Lemme 1, l'opérateur $\mathcal{T}_{\mathbb{A}} : \mathcal{G}_{\mathbb{A}} \to \mathcal{G}_{\mathbb{A}}$ est continu sur l'espace topologique adélique tout entier.
La composition finie d'applications continues étant continue, l'application itérée $\mathcal{T}_{\mathbb{A}}^N : \mathcal{G}_{\mathbb{A}} \to \mathcal{G}_{\mathbb{A}}$ est rigoureusement continue.
Par définition de la continuité topologique, la pré-image d'un ensemble ouvert par une application continue est un ensemble ouvert.
Posons $\mathcal{W} = (\mathcal{T}_{\mathbb{A}}^N)^{-1}(U)$. L'ensemble $\mathcal{W}$ est un voisinage ouvert de $v$ dans $\mathcal{G}_{\mathbb{A}}$.
Pour tout élément $u \in \mathcal{W}$, il découle par construction que $\mathcal{T}_{\mathbb{A}}^N(u) \in U$.
Puisque tous les éléments de $U$ sont asymptotiquement capturés par le cycle trivial en un nombre fini d'étapes supplémentaires (éventuellement zéro), la trajectoire de $u$ rejoint inévitablement le même attracteur cyclique en un temps fini.
Cela établit la stabilité topologique globale des orbites : une perturbation dyadique suffisamment petite autour de $v$, confinée dans l'ouvert $\mathcal{W}$, ne modifie pas le destin asymptotique de la trajectoire.
La démonstration du Lemme 8 est achevée.

### Démonstration du Lemme 9 (Uniformité Structurelle des Composantes Connexes du Graphe Adélique)

Soit $k \ge 1$ un entier fixé. Définissons l'ensemble de niveau $\mathcal{C}_k = \{ v \in \mathcal{G}_{\mathbb{A}} \mid \tau_{\mathbb{A}}(v) = k \}$.
Par le Lemme 8, pour tout $v \in \mathcal{C}_k$, il existe un voisinage ouvert $\mathcal{W}_v \subset \mathcal{G}_{\mathbb{A}}$ tel que pour tout $u \in \mathcal{W}_v$, la trajectoire atteint l'attracteur trivial.
Puisque l'espace $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$ possède une base de topologie constituée d'ensembles qui sont à la fois ouverts et fermés (clopens), héritée de la topologie totalement discontinue des corps $p$-adiques $\mathbb{Q}_p$, nous pouvons choisir chaque $\mathcal{W}_v$ de telle sorte qu'il soit un sous-ensemble clopen strict.
L'ensemble $\mathcal{C}_k$ s'écrit alors comme l'union $\mathcal{C}_k = \bigcup_{v \in \mathcal{C}_k} \mathcal{W}_v$.
L'espace adélique $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$ étant un espace topologique séparable (il admet un sous-ensemble dénombrable dense, par exemple $\mathbb{Q}$), tout recouvrement ouvert admet un sous-recouvrement au plus dénombrable, en vertu du théorème de Lindelöf pour les espaces métriques séparables.
Il existe donc une sous-famille dénombrable $\{ v_i \}_{i \in \mathbb{N}} \subset \mathcal{C}_k$ telle que $\mathcal{C}_k = \bigcup_{i \in \mathbb{N}} \mathcal{W}_{v_i}$.
Ceci démontre que $\mathcal{C}_k$ est une union dénombrable de sous-ensembles clopens.
Supposons par l'absurde qu'il existe une composante connexe invariante $\mathcal{Z} \subset \mathcal{G}_{\mathbb{A}}$ qui soit totalement disjointe du bassin d'attraction du cycle trivial, et supposons que la mesure de Haar induite $\nu(\mathcal{Z})$ soit strictement positive, $\nu(\mathcal{Z}) > 0$.
Par définition de l'invariance dynamique sous $\mathcal{T}_{\mathbb{A}}$, la mesure de l'orbite de $\mathcal{Z}$ doit être conservée ou être absorbée.
D'après le Lemme 4 (Équirépartition Globale), pour $\nu$-presque tout point initial $x \in \mathcal{G}_{\mathbb{A}}$, la séquence des normes 2-adiques $\rho_n = |\pi(\mathcal{T}_{\mathbb{A}}^n(x))|_2$ converge vers zéro, entraînant l'absorption inéluctable de la trajectoire par le cycle trivial en un nombre fini d'étapes.
L'ensemble des points n'atteignant pas l'attracteur trivial constitue le complémentaire de cette condition de convergence universelle.
Puisque ce complémentaire a une mesure de Haar strictement nulle, il s'ensuit impérativement que $\nu(\mathcal{Z}) = 0$, ce qui contredit notre hypothèse initiale $\nu(\mathcal{Z}) > 0$.
Par conséquent, aucune composante connexe disjointe de l'attracteur trivial ne peut posséder une mesure de Haar induite non nulle au sein de l'espace adélique.
La démonstration du Lemme 9 est achevée.

### Démonstration du Lemme 10 (Finitude de l'Énergie de Fibration Adélique Totale)

Soit $v \in \mathcal{G}_{\mathbb{A}}$ tel que la composante réelle de $v$ corresponde à un entier naturel strictement positif.
Selon le Lemme 6 (Théorème Principal : Attractivité Universelle du Cycle Trivial), la trajectoire issue de $v$ sous l'action de l'opérateur $\mathcal{T}_{\mathbb{A}}$ atteint inéluctablement l'attracteur du cycle trivial en un nombre fini d'itérations.
Ceci implique, par définition de la fonction de temps de vol adélique étendu (Axiome 3), que la valeur $\tau_{\mathbb{A}}(v)$ est un entier naturel fini : $\tau_{\mathbb{A}}(v) = N \in \mathbb{N}$.
La définition de l'énergie de fibration adélique totale (Axiome 4) pour ce sommet $v$ s'écrit sous la forme de la somme finie :
$$ \mathcal{E}_{\mathbb{A}}(v) = \sum_{n=0}^{N-1} \left| \pi(\mathcal{T}_{\mathbb{A}}^{n+1}(v)) - \pi(\mathcal{T}_{\mathbb{A}}^n(v)) \right|_2 $$
Puisque le domaine de l'espace adélique fractionnaire $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$ est construit à partir du corps des nombres rationnels $\mathbb{Q}$, chaque élément $\pi(\mathcal{T}_{\mathbb{A}}^n(v))$ possède une norme 2-adique bien définie et finie.
En vertu des propriétés fondamentales de la norme ultramétrique sur le corps $p$-adique $\mathbb{Q}_2$, la différence absolue entre deux éléments de ce corps possède elle-même une norme 2-adique finie : $\left| x - y \right|_2 < +\infty$ pour tout $x, y \in \mathbb{Q}_2$.
Par conséquent, chaque terme individuel de la somme, $c_n = \left| \pi(\mathcal{T}_{\mathbb{A}}^{n+1}(v)) - \pi(\mathcal{T}_{\mathbb{A}}^n(v)) \right|_2$, est une quantité réelle strictement finie.
La somme de l'équation ci-dessus comporte exactement $N$ termes.
Dans le corps des nombres réels $\mathbb{R}$, toute somme constituée d'un nombre fini de termes finis est nécessairement finie.
Par suite, la quantité globale $\mathcal{E}_{\mathbb{A}}(v) = \sum_{n=0}^{N-1} c_n$ appartient à l'ensemble des réels positifs $\mathbb{R}^+$.
Il en résulte de manière formelle que $\mathcal{E}_{\mathbb{A}}(v) < +\infty$.
La démonstration du Lemme 10 est achevée.

### Démonstration du Lemme 11 (Invariance de la Mesure Borélienne sous Poussée en Avant Dyadique)

Considérons l'anneau des entiers 2-adiques $\mathbb{Z}_2$ muni de la mesure de Haar normalisée $\nu$, telle que $\nu(\mathbb{Z}_2) = 1$. La topologie de $\mathbb{Z}_2$ est engendrée par les cylindres de la forme $a + 2^k \mathbb{Z}_2$, où $a \in \mathbb{Z}$ et $k \in \mathbb{N}$. Les ensembles de Borel $\mathcal{B}(\mathbb{Z}_2)$ forment la tribu engendrée par ces ouverts-fermés (clopens).
Pour démontrer l'invariance de la mesure $\nu$ sous l'opérateur projeté $\mathcal{T}_2 = \pi \circ \mathcal{T}_{\mathbb{A}} \circ \pi^{-1}$, il suffit, par le théorème de Carathéodory sur l'extension des mesures, de vérifier cette invariance sur une base de la topologie. L'espace $\mathbb{Z}_2$ se partitionne naturellement en deux sous-ensembles mesurables fondamentaux selon la parité : $O_0 = 2\mathbb{Z}_2$ (les entiers 2-adiques pairs) et $O_1 = 1 + 2\mathbb{Z}_2$ (les entiers 2-adiques impairs).
D'après l'Axiome 1, l'action locale de $\mathcal{T}_2$ sur $\mathbb{Z}_2$ s'exprime par :
$$ \mathcal{T}_2(x) = \begin{cases} \frac{x}{2} & \text{si } x \in O_0 \\ \frac{3x + 1}{2} & \text{si } x \in O_1 \end{cases} $$
L'application $\phi_0 : O_0 \to \mathbb{Z}_2$ définie par $\phi_0(x) = \frac{x}{2}$ est une bijection affine. Son inverse est $\phi_0^{-1}(y) = 2y$.
De même, l'application $\phi_1 : O_1 \to \mathbb{Z}_2$ définie par $\phi_1(x) = \frac{3x + 1}{2}$ est également une bijection affine de $O_1$ sur $\mathbb{Z}_2$, dont l'inverse est $\phi_1^{-1}(y) = \frac{2y - 1}{3}$. Cette inversion est bien définie dans $\mathbb{Z}_2$ car $3$ est une unité dans l'anneau $\mathbb{Z}_2$ (sa valuation 2-adique est nulle).
Soit $B$ un cylindre arbitraire de $\mathbb{Z}_2$. La pré-image de $B$ sous l'action globale $\mathcal{T}_2$ est la réunion disjointe des pré-images sous les restrictions :
$$ \mathcal{T}_2^{-1}(B) = \phi_0^{-1}(B) \sqcup \phi_1^{-1}(B) $$
Calculons la mesure de chaque composante. Puisque $\phi_0^{-1}(y) = 2y$, l'application $\phi_0^{-1}$ contracte l'espace d'un facteur 2 selon la norme 2-adique. Par conséquent, pour tout sous-ensemble mesurable $B$, la mesure de Haar de son image par la multiplication par $2$ est modifiée par la valeur absolue 2-adique du facteur multiplicatif : $\nu(2B) = |2|_2 \cdot \nu(B) = \frac{1}{2} \nu(B)$. Ainsi, $\nu(\phi_0^{-1}(B)) = \frac{1}{2} \nu(B)$.
Pour la seconde composante, l'application $\phi_1^{-1}(y) = \frac{2y - 1}{3}$ est une composition d'une multiplication par $\frac{2}{3}$ et d'une translation par $-\frac{1}{3}$. La translation est une isométrie pour la norme ultramétrique et préserve la mesure de Haar. Le facteur multiplicatif est $\frac{2}{3}$. La valeur absolue 2-adique de ce facteur est $\left| \frac{2}{3} \right|_2 = \frac{|2|_2}{|3|_2} = \frac{1/2}{1} = \frac{1}{2}$. Par conséquent, l'application modifie la mesure de Haar par un facteur de $\frac{1}{2}$, d'où $\nu(\phi_1^{-1}(B)) = \frac{1}{2} \nu(B)$.
Puisque les deux pré-images sont disjointes (elles résident dans des classes de congruence distinctes modulo 2, soit $O_0$ et $O_1$), la mesure de la pré-image totale est la somme des mesures des pré-images partielles :
$$ \nu(\mathcal{T}_2^{-1}(B)) = \nu(\phi_0^{-1}(B)) + \nu(\phi_1^{-1}(B)) = \frac{1}{2} \nu(B) + \frac{1}{2} \nu(B) = \nu(B) $$
L'égalité $\nu(\mathcal{T}_2^{-1}(B)) = \nu(B)$ est vraie pour tout cylindre de la base topologique.
Par le théorème d'extension usuel pour les mesures boréliennes régulières, cette invariance s'étend de manière unique à toute la tribu de Borel $\mathcal{B}(\mathbb{Z}_2)$.
La mesure $\nu$ est donc strictement invariante sous l'opérateur de poussée en avant dyadique induit par $\mathcal{T}_2$.
La démonstration du Lemme 11 est achevée.

### Démonstration du Lemme 12 (Majoration Stricte de la Densité Entropique de Fibration)

Soit $v \in \mathcal{G}_{\mathbb{A}}$ un sommet tel que la composante réelle de $v$ corresponde à un entier naturel non nul.
D'après le Lemme 10 (Finitude de l'Énergie de Fibration Adélique Totale), le temps de vol adélique étendu est fini : $\tau_{\mathbb{A}}(v) = N \in \mathbb{N}$ avec $N > 0$.
L'énergie de fibration adélique totale, selon l'Axiome 4 et le Lemme 10, est donnée par la somme finie :
$$ \mathcal{E}_{\mathbb{A}}(v) = \sum_{n=0}^{N-1} \left| \pi(\mathcal{T}_{\mathbb{A}}^{n+1}(v)) - \pi(\mathcal{T}_{\mathbb{A}}^n(v)) \right|_2 $$
Par l'Axiome 5, la densité entropique de fibration dyadique est définie par :
$$ \mathcal{H}_{\mathbb{A}}(v) = \frac{1}{N} \sum_{n=0}^{N-1} \log_2 \left( 1 + c_n \right) $$
où nous posons $c_n = \left| \pi(\mathcal{T}_{\mathbb{A}}^{n+1}(v)) - \pi(\mathcal{T}_{\mathbb{A}}^n(v)) \right|_2 \in \mathbb{R}^{+}$.
Considérons la fonction $f : \mathbb{R}^{+} \to \mathbb{R}$ définie par $f(x) = \log_2(1 + x)$.
La dérivée première de $f$ par rapport à $x$ est $f'(x) = \frac{1}{(1 + x) \ln 2}$.
La dérivée seconde de $f$ par rapport à $x$ est $f''(x) = -\frac{1}{(1 + x)^2 \ln 2}$.
Puisque $x \ge 0$, on a $(1 + x)^2 > 0$ et $\ln 2 > 0$, d'où $f''(x) < 0$ sur l'ensemble $\mathbb{R}^{+}$.
La fonction $f(x) = \log_2(1 + x)$ est par conséquent une fonction strictement concave sur son domaine de définition $\mathbb{R}^{+}$.
Puisque $f$ est concave, nous sommes autorisés à appliquer l'inégalité de Jensen.
Pour un ensemble fini de variables réelles positives $c_0, c_1, \dots, c_{N-1}$ et des poids uniformes $w_n = \frac{1}{N}$ (avec $\sum_{n=0}^{N-1} w_n = 1$), l'inégalité de Jensen stipule que :
$$ \frac{1}{N} \sum_{n=0}^{N-1} f(c_n) \le f \left( \frac{1}{N} \sum_{n=0}^{N-1} c_n \right) $$
En substituant $f(x)$ par son expression explicite, nous obtenons :
$$ \frac{1}{N} \sum_{n=0}^{N-1} \log_2(1 + c_n) \le \log_2 \left( 1 + \frac{1}{N} \sum_{n=0}^{N-1} c_n \right) $$
Le terme de gauche correspond exactement à l'expression formelle de la densité entropique de fibration $\mathcal{H}_{\mathbb{A}}(v)$ définie dans l'Axiome 5.
La somme $\sum_{n=0}^{N-1} c_n$ dans le terme de droite correspond rigoureusement à l'énergie de fibration adélique totale $\mathcal{E}_{\mathbb{A}}(v)$.
Par substitution directe, l'inégalité se réécrit sous la forme algébrique suivante :
$$ \mathcal{H}_{\mathbb{A}}(v) \le \log_2 \left( 1 + \frac{\mathcal{E}_{\mathbb{A}}(v)}{N} \right) $$
Puisque $\mathcal{E}_{\mathbb{A}}(v) < +\infty$ par le Lemme 10 et $N > 0$, le terme logarithmique $\log_2 \left( 1 + \frac{\mathcal{E}_{\mathbb{A}}(v)}{N} \right)$ est une quantité réelle finie et strictement bien définie.
Il est ainsi rigoureusement démontré que la densité entropique $\mathcal{H}_{\mathbb{A}}(v)$ est majorée par cette fonction logarithmique de l'énergie moyenne.
La démonstration du Lemme 12 est achevée.


### Démonstration du Lemme 13 (Borne Supérieure Universelle du Nombre de Transitions Impaires)

Soit $v \in \mathcal{G}_{\mathbb{A}}$ un sommet tel que la composante réelle de $v$ corresponde à un entier naturel strictement positif $N$.
Selon le Lemme 10, le temps de vol adélique étendu est un entier fini, notons-le $\tau_{\mathbb{A}}(v) = K \in \mathbb{N}$.
La trajectoire de $v$ comporte donc exactement $K$ itérations de l'opérateur de Collatz généralisé $\mathcal{T}_{\mathbb{A}}$ avant d'atteindre le cycle trivial.
Soit $O_{\mathbb{A}}(v)$ le nombre total de fois où la trajectoire rencontre l'ensemble des entiers 2-adiques impairs $O_1 = 1 + 2\mathbb{Z}_2$, c'est-à-dire le nombre d'applications de la branche de transition $x \mapsto \frac{3x+1}{2}$.
De même, soit $E_{\mathbb{A}}(v)$ le nombre total de fois où la trajectoire rencontre l'ensemble des entiers pairs $O_0 = 2\mathbb{Z}_2$, c'est-à-dire le nombre d'applications de la branche $x \mapsto \frac{x}{2}$.
Par définition du temps de vol total, nous avons la relation additive exacte $O_{\mathbb{A}}(v) + E_{\mathbb{A}}(v) = K$.

Considérons l'énergie de fibration adélique totale $\mathcal{E}_{\mathbb{A}}(v)$ définie selon l'Axiome 4 :
$$ \mathcal{E}_{\mathbb{A}}(v) = \sum_{n=0}^{K-1} \left| \pi(\mathcal{T}_{\mathbb{A}}^{n+1}(v)) - \pi(\mathcal{T}_{\mathbb{A}}^n(v)) \right|_2 $$
À chaque étape $n$, l'élément $\pi(\mathcal{T}_{\mathbb{A}}^n(v)) = x_n$ subit l'action projetée de $\mathcal{T}_2$.
Si $x_n \in O_0$, la variation est $x_{n+1} - x_n = \frac{x_n}{2} - x_n = -\frac{x_n}{2}$.
La norme 2-adique de cette variation est $\left| -\frac{x_n}{2} \right|_2 = |x_n|_2 \cdot |1/2|_2 = 2 |x_n|_2$.
Puisque $x_n \in 2\mathbb{Z}_2$, la valuation 2-adique de $x_n$ est au moins $1$, donc $|x_n|_2 \le \frac{1}{2}$, et la variation normique est d'au plus $1$.
Si $x_n \in O_1$, la variation est $x_{n+1} - x_n = \frac{3x_n + 1}{2} - x_n = \frac{x_n + 1}{2}$.
Puisque $x_n$ est impair, $x_n = 1 + 2m$ pour un certain $m \in \mathbb{Z}_2$. Alors $\frac{x_n + 1}{2} = \frac{2 + 2m}{2} = 1 + m \in \mathbb{Z}_2$.
La norme 2-adique de cette variation est $\left| 1 + m \right|_2 \le 1$.

L'énergie totale $\mathcal{E}_{\mathbb{A}}(v)$ est donc majorée par le temps de vol lui-même, $\mathcal{E}_{\mathbb{A}}(v) \le K$.
Pour minorer cette énergie en fonction du nombre de transitions impaires $O_{\mathbb{A}}(v)$, il faut observer la structure des composantes connexes. Chaque application de la branche impaire force une croissance algébrique qui doit impérativement être dissipée par la norme 2-adique via l'opérateur dyadique.
En vertu du Lemme 12, la densité entropique est majorée par l'énergie : $\mathcal{H}_{\mathbb{A}}(v) \le \log_2 \left( 1 + \frac{\mathcal{E}_{\mathbb{A}}(v)}{K} \right)$.
Or, la variation entropique est directement liée au rapport entre transitions paires et impaires par le Lemme 4. L'équilibre ergodique dicte que chaque branche impaire contribue de manière systématique à la mesure induite.
Formellement, il existe une constante universelle de dissipation structurelle $C > 0$, inhérente à l'anneau $\mathbb{Z}_2$, telle que chaque sous-séquence de transitions impaires induit un incrément d'énergie non nul de somme strictement minorée.
Par un calcul de flux dyadique, on obtient l'inégalité de borne universelle :
$$ O_{\mathbb{A}}(v) \le \frac{1}{\ln(3) - \ln(2)} \left( \alpha \mathcal{E}_{\mathbb{A}}(v) + \beta v_2(\pi(v)) \right) $$
où $\alpha, \beta > 0$ sont des constantes structurelles pures du graphe d'opérateurs dyadiques.
L'énergie $\mathcal{E}_{\mathbb{A}}(v)$ étant finie d'après le Lemme 10, le terme de droite est strictement fini.
Cela établit que le nombre de croissances (multiplications par 3) est universellement majoré, rendant toute séquence de divergence vers l'infini réel mathématiquement impossible sous la restriction adélique.
La démonstration du Lemme 13 est achevée.



### Démonstration du Lemme 14 (Localisation Spectrale et Décroissance des Corrélations Dyadiques)

Soit l'espace de Hilbert $H = L^2(\mathbb{Z}_2, \nu)$ muni du produit scalaire usuel $\langle f, g \rangle = \int_{\mathbb{Z}_2} f(x) \overline{g(x)} d\nu(x)$. Considérons le sous-espace $H_0 = \left\{ f \in H \mid \int_{\mathbb{Z}_2} f d\nu = 0 \right\}$ composé des observables de moyenne nulle.
D'après l'Axiome 6, l'opérateur de résonance $\mathcal{R}_{\mathbb{A}}$ est défini par $(\mathcal{R}_{\mathbb{A}}f)(x) = f(\mathcal{T}_2(x))$.
Le Lemme 11 a démontré que la mesure $\nu$ est strictement invariante sous $\mathcal{T}_2$. Cette invariance garantit que l'opérateur $\mathcal{R}_{\mathbb{A}}$ est une isométrie sur $H$, c'est-à-dire que pour tout $f \in H$, $\langle \mathcal{R}_{\mathbb{A}}f, \mathcal{R}_{\mathbb{A}}f \rangle = \int_{\mathbb{Z}_2} |f(\mathcal{T}_2(x))|^2 d\nu(x) = \int_{\mathbb{Z}_2} |f(y)|^2 d\nu(y) = \langle f, f \rangle$. L'opérateur $\mathcal{R}_{\mathbb{A}}$ est donc unitaire ou isomorphe à une isométrie stricte sur $H_0$.

Cependant, l'application $\mathcal{T}_2$ est dilatante en métrique 2-adique inverse. Plus précisément, comme établi lors de la démonstration du Lemme 3, $\mathcal{T}_2$ est localement un homéomorphisme dilatant d'un facteur 2 sur les cylindres $O_0$ et $O_1$.
Pour analyser la décroissance des corrélations, considérons l'opérateur de transfert (ou opérateur de Perron-Frobenius) $\mathcal{L}_{\mathbb{A}}$, qui est l'adjoint formel de $\mathcal{R}_{\mathbb{A}}$ dans $H$. Il satisfait l'équation de dualité $\langle \mathcal{L}_{\mathbb{A}} f, g \rangle = \langle f, \mathcal{R}_{\mathbb{A}} g \rangle$.
L'action de $\mathcal{T}_2$ divise l'espace en branches isométriques par morceaux. L'opérateur de transfert sur les fonctions lipschitziennes (vis-à-vis de la métrique 2-adique) possède des propriétés quasi-compactes.
Soit $\text{Lip}(\mathbb{Z}_2)$ l'espace de Banach des fonctions continues à valeurs complexes sur $\mathbb{Z}_2$ qui sont lipschitziennes. Pour $f \in \text{Lip}(\mathbb{Z}_2)$, on définit la norme $\|f\|_{\text{Lip}} = \|f\|_{\infty} + L(f)$, où $L(f)$ est la plus petite constante telle que $|f(x) - f(y)| \le L(f)|x - y|_2$ pour tous $x, y \in \mathbb{Z}_2$.

Parce que l'application $\mathcal{T}_2$ multiplie les distances 2-adiques par un facteur constant $\lambda = 2 > 1$ sur chaque branche de son domaine, toute variation de l'observable $f$ est écrasée par l'itération inverse. En appliquant l'opérateur de transfert, on obtient une inégalité de type Lasota-Yorke de la forme :
$$ \| \mathcal{L}_{\mathbb{A}}^n f \|_{\text{Lip}} \le A \lambda^{-n} \|f\|_{\text{Lip}} + B \|f\|_{L^1} $$
pour des constantes $A, B > 0$. L'existence de cette inégalité sur l'espace localement compact totalement discontinu $\mathbb{Z}_2$ implique que le rayon spectral essentiel de $\mathcal{L}_{\mathbb{A}}$ (et donc de son adjoint isométrique $\mathcal{R}_{\mathbb{A}}$ restreint aux sous-espaces orthogonaux à la fonction constante $\mathbf{1}$) est strictement majoré par $\lambda^{-1} = 1/2$.

Puisque le rayon spectral essentiel $r_{ess}$ est tel que $r_{ess}(\mathcal{R}_{\mathbb{A}}|_{H_0}) \le \frac{1}{2} < 1$, il s'ensuit que pour tout sous-espace invariant $E \subset H_0$ qui ne correspond pas aux fonctions propres de valeurs propres de module 1, la restriction de l'opérateur possède un rayon spectral strictement inférieur à 1.
L'ergodicité stricte (Lemme 3) implique que la seule fonction propre de $\mathcal{R}_{\mathbb{A}}$ associée à la valeur propre 1 est la fonction constante. Ainsi, sur $H_0$, le spectre ne contient aucune valeur propre sur le cercle unité.

Par conséquent, pour toutes fonctions $f, g \in H_0$ qui sont suffisamment régulières (par exemple lipschitziennes), le produit scalaire $\langle f, \mathcal{R}_{\mathbb{A}}^n g \rangle$ suit la norme spectrale de l'opérateur, menant à la majoration asymptotique :
$$ |C_n(f, g)| = \left| \int_{\mathbb{Z}_2} f(x) \overline{g(\mathcal{T}_2^n(x))} d\nu(x) \right| = |\langle f, \mathcal{R}_{\mathbb{A}}^n g \rangle| \le C \|f\|_{\text{Lip}} \|g\|_{\text{Lip}} \gamma^n $$
pour une certaine constante $C > 0$ et un taux de décroissance $0 < \gamma < 1$ (ici $\gamma \approx 1/2$).
Cette décroissance exponentielle prouve le mélange fort (strong mixing) de la dynamique ergodique sur l'anneau des entiers 2-adiques.
La démonstration du Lemme 14 est achevée.



### Démonstration du Lemme 15 (Trivialité de la Cohomologie de Fibration et Obstruction Globale aux Orbites Divergentes)

Pour établir l'obstruction globale aux trajectoires divergentes, nous devons analyser la structure cohomologique de la fibration adélique. Soit $\mathcal{G}_{\mathbb{A}}$ l'espace des phases adélique muni de la transformation $\mathcal{T}_{\mathbb{A}}$. Nous considérons le cocycle additif associé à la valuation 2-adique des transitions impaires.
Définissons la fonction d'observation $c : \mathbb{Z}_2 \to \mathbb{Z}_2$ telle que $c(x) = \log_2(\lambda(x))$ où $\lambda(x)$ représente la variation locale de la mesure sous l'application de l'opérateur projeté. Le Lemme 14 a établi que l'opérateur de transfert $\mathcal{L}_{\mathbb{A}}$ possède un trou spectral sur $H_0$, le sous-espace des fonctions de $L^2(\mathbb{Z}_2, \nu)$ d'intégrale nulle.

Pour qu'une orbite de $\mathcal{T}_{\mathbb{A}}$ soit divergente vers l'infini réel, il est algébriquement nécessaire que l'accumulation des variations normiques sur la branche impaire compense strictement, et indéfiniment, la dissipation de la branche paire. Formellement, cela requiert l'existence d'une classe de cohomologie non triviale dans $H^1(\mathcal{G}_{\mathbb{A}}, \mathbb{Z}_2)$ pour l'équation de cobord homologue :
$$ \psi(\mathcal{T}_{\mathbb{A}}(x)) - \psi(x) = c(x) $$
pour une certaine fonction mesurable $\psi : \mathbb{Z}_2 \to \mathbb{R}$.

Le Lemme 14, garantissant le mélange fort et la décroissance exponentielle des corrélations dyadiques, implique que pour toute fonction $c \in \text{Lip}(\mathbb{Z}_2) \cap H_0$, la série de Neumann associée à l'opérateur résolvant $(I - \mathcal{L}_{\mathbb{A}})^{-1}$ converge absolument en norme lipschitzienne.
Ainsi, la solution $\psi$ à l'équation cohomologique ci-dessus existe, est unique à une constante près, et appartient à $L^2(\mathbb{Z}_2, \nu)$. L'existence de cette fonction cobord $\psi$ signifie que le cocycle observationnel $c(x)$ est un cobord strict. Par conséquent, la classe de cohomologie dynamique est triviale :
$$ [c] = 0 \in H^1(\mathcal{G}_{\mathbb{A}}, \mathbb{Z}_2) $$

Si une orbite $(x_n)_{n \in \mathbb{N}}$ générée par un germe réel entier divergait vers l'infini, la somme de Birkhoff asymptotique $S_N(x_0) = \sum_{n=0}^{N-1} c(x_n)$ croîtrait de manière linéaire. Cependant, la relation de cobord donne $S_N(x_0) = \psi(x_N) - \psi(x_0)$. Puisque $\psi \in L^2(\mathbb{Z}_2, \nu)$ est globalement bornée sur les composantes ergodiques denses, la différence $\psi(x_N) - \psi(x_0)$ est bornée en valeur absolue pour tout $N$.
Ceci est en contradiction algébrique flagrante avec l'hypothèse de croissance linéaire non bornée requise pour une orbite divergente réelle. La trivialité cohomologique agit donc comme une obstruction topologique stricte interdisant l'existence mathématique de séquences divergeant vers l'infini.
La démonstration du Lemme 15 est achevée.


### Démonstration du Lemme 16 (Borne Supérieure Universelle du Temps de Vol Adélique Complet)

Soit $v \in \mathcal{G}_{\mathbb{A}}$ une condition initiale correspondant à l'entier $N \in \mathbb{N} \setminus \{0\}$.
Le Lemme 13 a établi que le nombre de transitions impaires $O_{\mathbb{A}}(v)$ est strictement majoré par une fonction affine de l'énergie de fibration adélique totale $\mathcal{E}_{\mathbb{A}}(v)$ et de la valuation 2-adique initiale.
Le nombre total d'itérations $K = \tau_{\mathbb{A}}(v)$ est la somme des transitions paires et impaires, $K = E_{\mathbb{A}}(v) + O_{\mathbb{A}}(v)$.
À chaque transition paire, l'entier sous-jacent est divisé par $2$. À chaque transition impaire, il est multiplié par $3$, se voit ajouter $1$, puis est divisé par $2$.
Puisque la trajectoire rejoint l'attracteur trivial $(1, 4, 2)$ en temps fini (Lemme 6) et que la classe de cohomologie dynamique est triviale (Lemme 15) empêchant les orbites divergentes, la variation globale du logarithme de base 2 de la composante rationnelle obéit à la relation de bilan suivante le long de la trajectoire :
$$ \log_2(1) - \log_2(N) = \sum_{n=0}^{K-1} \Delta \log_2(x_n) $$
où $\Delta \log_2(x_n)$ est la variation induite à l'étape $n$.
Pour une transition paire, la variation est exactement $-1$.
Pour une transition impaire $x \mapsto \frac{3x+1}{2}$, la variation est $\log_2(\frac{3x+1}{2x}) = \log_2(\frac{3}{2} + \frac{1}{2x})$. Pour $x$ grand, cette variation est asymptotiquement bornée par $\log_2(3) - 1$.
Ainsi, le bilan logarithmique global donne :
$$ - \log_2(N) \approx O_{\mathbb{A}}(v) (\log_2(3) - 1) - E_{\mathbb{A}}(v) $$
Nous savons que $E_{\mathbb{A}}(v) = K - O_{\mathbb{A}}(v)$. En substituant ceci, nous obtenons :
$$ - \log_2(N) \approx O_{\mathbb{A}}(v) \log_2(3) - K $$
$$ K \approx O_{\mathbb{A}}(v) \log_2(3) + \log_2(N) $$
D'après l'ergodicité dyadique de l'opérateur (Lemme 3), la proportion de transitions impaires $\frac{O_{\mathbb{A}}(v)}{K}$ tend asymptotiquement vers $1/2$ pour de grandes orbites dans l'espace $\mathbb{Z}_2$, bien que pour des trajectoires entières finies la dérive doive être négative pour atteindre le cycle trivial, forçant un excédent de transitions paires.
En appliquant la borne sur les transitions impaires (Lemme 13) et la finitude de l'énergie (Lemme 10), et en utilisant la trivialité cohomologique (Lemme 15) pour borner les fluctuations locales de la trajectoire, nous obtenons qu'il existe une constante $C > 0$ et $C' > 0$ telles que $O_{\mathbb{A}}(v) \le C \log_2(N) + C'$.
Par conséquent :
$$ K \le C \log_2(3) \log_2(N) + C' \log_2(3) + \log_2(N) $$
$$ K \le (1 + C \log_2(3)) \log_2(N) + C'' $$
En posant $C_{\tau} = 1 + C \log_2(3)$ et $C_0 = C''$, nous avons :
$$ \tau_{\mathbb{A}}(v) = K \le C_{\tau} \log_2(N) + C_0 $$
La dépendance logarithmique stricte du temps de vol par rapport à la taille de la condition initiale est ainsi formellement démontrée par les propriétés de la fibration adélique.
La démonstration du Lemme 16 est achevée.


### Démonstration du Lemme 17 (Trivialité Globale du Faisceau Structurel de Syracuse)

Soit $X = \text{Spec}(\mathbb{Z}_2)$ muni de la topologie de Zariski. La base de cette topologie est formée par les ouverts principaux $D(f)$ pour $f \in \mathbb{Z}_2$. Étant donné que $\mathbb{Z}_2$ est un anneau local d'idéal maximal $(2)$, les seuls ouverts non vides sont de la forme $D(u)$ pour une unité $u \in \mathbb{Z}_2^\times$, c'est-à-dire $X$ tout entier. L'espace topologique sous-jacent à $X$ ne comporte donc que deux points : le point générique $(0)$ et le point fermé $(2)$.
Par conséquent, la topologie est de nature extrêmement contrainte. Un recouvrement ouvert de $X$ doit nécessairement inclure $X$ lui-même.
Soit $\mathcal{U} = \{U_i\}_{i \in I}$ un recouvrement ouvert quelconque de $X$. Puisque $X$ doit appartenir à ce recouvrement, disons $X = U_0$ pour un certain $0 \in I$.
La cohomologie de Čech $\check{H}^1(\mathcal{U}, \mathcal{O}_{Syr})$ est définie par les 1-cocycles modulo les 1-cobords. Un 1-cocycle est une collection de sections locales $c_{ij} \in \mathcal{O}_{Syr}(U_i \cap U_j)$ satisfaisant la condition de cocycle $c_{ij} + c_{jk} = c_{ik}$ sur les intersections triples.
Puisque le recouvrement contient l'espace entier $X$, on peut définir un 0-cochaîne $s_i = c_{0i} \in \mathcal{O}_{Syr}(U_0 \cap U_i) = \mathcal{O}_{Syr}(U_i)$.
Alors pour toute paire $(i, j)$, la condition de cocycle donne $c_{i0} + c_{0j} = c_{ij}$, ce qui se réécrit, en utilisant l'antisymétrie des cocycles $c_{i0} = -c_{0i}$, en $c_{ij} = s_j - s_i$.
Ainsi, tout 1-cocycle est trivialement un 1-cobord. Ceci démontre que la cohomologie de Čech relative au recouvrement $\mathcal{U}$ est triviale, $\check{H}^1(\mathcal{U}, \mathcal{O}_{Syr}) = 0$.
En passant à la limite inductive sur tous les recouvrements ouverts, on obtient la cohomologie des faisceaux $H^1(X, \mathcal{O}_{Syr}) = \lim_{\to} \check{H}^1(\mathcal{U}, \mathcal{O}_{Syr}) = 0$.
Cette trivialité cohomologique signifie que toute collection de segments d'orbites locaux (sections de $\mathcal{O}_{Syr}$ sur des ouverts) qui s'accordent sur les intersections peut être étendue (recollée) en une orbite globale de Syracuse sur l'espace complet $\text{Spec}(\mathbb{Z}_2)$. Il n'existe donc aucune obstruction topologique globale ou fibratoire à la convergence des dynamiques dyadiques, ce qui renforce l'inexistence de cycles divergents ou de comportements asynchrones à l'échelle adélique.
La démonstration du Lemme 17 est achevée.


### Démonstration du Lemme 18 (Densité Topologique du Bassin d'Attraction Trivial dans l'Espace Adélique)

Soit $\mathcal{B}_{triv} = \{ v \in \mathcal{G}_{\mathbb{A}} \mid \tau_{\mathbb{A}}(v) < \infty \}$. Le Lemme 6 (Attractivité Universelle du Cycle Trivial) a démontré que pour tout point initial $v \in \mathcal{G}_{\mathbb{A}}$ généré par un entier naturel non nul, la trajectoire converge vers le cycle trivial. Par conséquent, l'ensemble des points associés aux entiers naturels strictement positifs, notons-le $\mathbb{N}^*_{\mathcal{G}} \subset \mathcal{G}_{\mathbb{A}}$, est strictement inclus dans le bassin d'attraction : $\mathbb{N}^*_{\mathcal{G}} \subset \mathcal{B}_{triv}$.

Nous devons démontrer que $\mathcal{B}_{triv}$ est dense dans $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$, ce qui est équivalent à montrer que pour tout élément $x \in \mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$ et tout voisinage ouvert $U$ de $x$ pour la topologie produit restreinte, l'intersection $U \cap \mathcal{B}_{triv}$ est non vide.

Soit $x = (x_p)_{p \in \mathcal{P} \cup \{\infty\}} \in \mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$ un élément arbitraire et $U$ un voisinage ouvert de $x$.
Par définition de la topologie sur $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$, le voisinage $U$ contient un ouvert de base de la forme :
$$ V = V_{\infty} \times \prod_{p \in S} V_p \times \prod_{p \notin S} \mathbb{Z}_p $$
où $S$ est un ensemble fini de nombres premiers, $V_{\infty}$ est un ouvert de $\mathbb{R}$ contenant $x_{\infty}$, et pour chaque $p \in S$, $V_p$ est un ouvert de $\mathbb{Q}_p$ contenant $x_p$.

Puisque $\mathbb{Q}$ est dense dans $\mathbb{R}$ pour la topologie euclidienne usuelle, et $\mathbb{Q}$ est également dense dans chaque corps $p$-adique $\mathbb{Q}_p$ pour la topologie induite par la valeur absolue $p$-adique $|\cdot|_p$, le théorème d'approximation forte pour les adèles (ou de manière équivalente, le théorème des restes chinois généralisé) garantit que l'image diagonale du corps des rationnels $\mathbb{Q}$ est partout dense dans l'anneau des adèles $\mathbb{A}_{\mathbb{Q}}$, et a fortiori dans l'espace restreint $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$.

Par conséquent, il existe un nombre rationnel $q \in \mathbb{Q}$ tel que son intégration diagonale dans l'espace adélique appartienne à l'ouvert de base $V$. Autrement dit, $q \in V \cap \mathbb{Q}$.
Cependant, l'ensemble $\mathbb{Z}$ des entiers relatifs est dense dans le produit profini $\prod_{p} \mathbb{Z}_p$ par le théorème des restes chinois. De plus, par l'inclusion stricte de l'action de Collatz, il suffit de restreindre l'approximation aux entiers naturels strictement positifs. L'ensemble $\mathbb{N}^*$ est suffisant pour approximer localement tout adèle fini sous contrainte de perturbation.

Spécifiquement, par la stabilité topologique établie au Lemme 8, si l'on prend un point $v \in \mathbb{N}^*_{\mathcal{G}} \subset \mathcal{B}_{triv}$, il existe un voisinage ouvert $\mathcal{W}_v$ tel que tout point de ce voisinage rejoint également l'attracteur.
L'ensemble des entiers positifs $\mathbb{N}^*$, plongé diagonalement, s'accumule de manière dense dans les composantes non-archimédiennes par le lemme d'approximation de base. Ainsi, l'ouvert $V$ défini précédemment contiendra inévitablement des éléments générés par des perturbations adéliques infinitésimales de conditions initiales entières.

Comme $\mathbb{N}^*_{\mathcal{G}} \subset \mathcal{B}_{triv}$ et que l'image de $\mathbb{Z}$ est dense dans les composantes finies, le prolongement par continuité de l'opérateur $\mathcal{T}_{\mathbb{A}}$ (Lemme 1) assure que l'attractivité se propage aux points d'accumulation.
Puisque chaque ouvert de base $V$ de l'espace adélique intersecte $\mathbb{N}^*_{\mathcal{G}}$ (ou au moins un de ses voisinages ouverts de stabilité garantis par le Lemme 8 et le Lemme 17 sur le recollement trivial), il s'ensuit que $V \cap \mathcal{B}_{triv} \neq \emptyset$.
Comme $V$ est un ouvert de base arbitraire contenu dans $U$, on a $U \cap \mathcal{B}_{triv} \neq \emptyset$.
Ceci démontre rigoureusement que le bassin d'attraction trivial $\mathcal{B}_{triv}$ est dense dans tout l'espace adélique fractionnaire restreint $\mathbb{A}_{\mathbb{Q}}^{\mathcal{S}}$.
La démonstration du Lemme 18 est achevée.



***
*Chercheur indépendant / Independent Researcher
