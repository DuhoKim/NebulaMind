**B6 — Applicability of the flat-geometry results to the source's KS scenario**  
2026-09-07 · Weyssenhoff FLUID only · Report only

The exact KS shear evolution is generally not a pure power law: it is an $a^{-6}$ factor times a curvature-dependent, time-dependent coefficient. During contraction on the positive-source branch described after the source's Eq. (30), shear grows faster than $a^{-6}$. Thus B1's constant-comparison argument does not transfer. The number-density mechanism used in B3 does transfer, but its guaranteed bounce result is undetermined in KS by this applicability check.

The governing source read here is Nikodem J. Popławski, *A nonsingular, anisotropic universe in a black hole with torsion and particle production*, *General Relativity and Gravitation* **53**, article 18 (2021), [saved publisher HTML](b4_springer_access.html), DOI [10.1007/s10714-021-02790-7](https://link.springer.com/article/10.1007/s10714-021-02790-7). All quotations below come directly from that saved publisher HTML; none comes from arXiv or an APS PDF. Equation text is copied from its MathJax payload with its printed number; prose is copied with HTML formatting removed. Publisher source SHA256: `fb94da36db11823ed1081fd39226a7134dec64883a7811c4011a1ea7234efc88`.

The existing FLUID claims were identified from the lane's B1 result, criterion and scope qualification and B3 rescue and reconciliation records, particularly [B1's scope statement](B1_SCOPE_QUALIFICATION_20260907.md) and [B3's scaling and theorem](B3_RESCUE_20260907.md). They are treated as the established flat-geometry inputs. This report performs the requested equation-level applicability derivation; it selects no closure, integrates no new model, revises no earlier result and files no class. No excluded data were used.

**(a) The printed KS shear law and its neighbours.**

Use the source's Eq. (6) geometry and Eqs. (15)–(16) definitions, on a regular patch with positive scale factors:

$$
a^3=XY^2,\qquad H=\frac{\dot a}{a}=\frac{H_X+2H_Y}{3},\qquad
H_X=\frac{\dot X}{X},\quad H_Y=\frac{\dot Y}{Y},\quad
\Delta=H_X-H_Y,\quad K=Y^{-2}>0.
$$

Write $S=\sigma^2$ for the source's shear scalar (not its square root). Eqs. (24)–(25) give $\sigma^1{}_1=2\Delta/3$, $\sigma^2{}_2=\sigma^3{}_3=-\Delta/3$ and $S=\Delta^2/3$.

**Verbatim quotation — publisher HTML, Eq. (27), `Equ27`; read directly, not arXiv:**

> $$\begin{aligned} \dot{\sigma }^{1}_1=\frac{2}{3}\Bigl (\frac{X\ddot{X}-\dot{X}^{2}}{X^{2}} -\frac{Y\ddot{Y}-\dot{Y}^{2}}{Y^{2}}\Bigr ). \end{aligned}$$
>
> (27)

**Verbatim quotation — publisher HTML, immediately before Eq. (28); read directly, not arXiv:**

> Using this equation with (11) and (16) gives

**Verbatim quotation — publisher HTML, Eq. (28), `Equ28`; read directly, not arXiv:**

> $$\begin{aligned} \dot{\sigma }^{1}_1+3H\sigma ^{1}_1=\frac{2}{3Y^{2}}. \end{aligned}$$
>
> (28)

**Verbatim quotation — publisher HTML, immediately before Eq. (29); read directly, not arXiv:**

> Similarly, the rates of the other components satisfy

**Verbatim quotation — publisher HTML, Eq. (29), `Equ29`; read directly, not arXiv:**

> $$\begin{aligned} \dot{\sigma }^{2}_{2}+3H\sigma ^{2}_{2}=\dot{\sigma }^{3}_{3}+3H\sigma ^{3}_{3} =-\frac{1}{3Y^{2}}. \end{aligned}$$
>
> (29)

**Verbatim quotation — publisher HTML, immediately before Eq. (30); read directly, not arXiv:**

> Consequently, the rate of the shear scalar \(d(\sigma ^{2})/dt=\dot{\sigma }^{\mu }_\nu \sigma ^\nu _\mu \) satisfies

**Verbatim quotation — publisher HTML, Eq. (30), `Equ30`; read directly, not arXiv:**

> $$\begin{aligned} \frac{d(\sigma ^{2})}{dt}+6H\sigma ^{2}=\frac{2}{3Y^{2}}\Bigl (\frac{\dot{X}}{X} -\frac{\dot{Y}}{Y}\Bigr ). \end{aligned}$$
>
> (30)

**Verbatim quotation — publisher HTML, immediately after Eq. (30); read directly, not arXiv:**

> The right-hand side in this equation is positive, which indicates that the shear scalar grows with decreasing a faster than \(\sim a^{-6}\).


The next numbered equation is the Raychaudhuri equation:

**Verbatim quotation — publisher HTML, Eq. (31), `Equ31`; read directly, not arXiv:**

> $$\begin{aligned} \frac{d\theta }{ds}=-\frac{1}{3}\theta ^{2}-2(\sigma ^{2}-\omega ^{2}) +w^{\mu }{}_{;\mu }-R_{\mu \nu }u^{\mu } u^\nu , \end{aligned}$$
>
> (31)


From Eq. (28) and $\sigma^1{}_1=2\Delta/3$, the exact signed-anisotropy equation is

$$
\dot\Delta+3H\Delta=K.
$$

Multiplying by the integrating factor $a^3$ gives

$$
\frac{d(a^3\Delta)}{dt}=a^3K,\qquad
I(t)=\int_{t_0}^{t}a^3(t')K(t')\,dt',\qquad
C=a(t_0)^3\Delta(t_0).
$$

Consequently, the **exact derived scaling** is

$$
\boxed{\Delta(t)=a(t)^{-3}[C+I(t)],\qquad
\sigma^2(t)=\frac{[C+I(t)]^2}{3a(t)^6}.}
$$

Since $a^3K=X$ on this patch, the same integral is $I(t)=\int_{t_0}^{t}X(t')\,dt'$. This is an exact integral identity for the printed equations, not a specification of $X(t)$ or a new solution. Equivalently, Eq. (30) gives

$$
\boxed{\frac{d(a^6S)}{dt}=\frac23a^6K\Delta,}
$$

which exhibits precisely why the flat conserved shear coefficient is lost.

Where $H\ne0$ and $\Delta\ne0$, the instantaneous logarithmic slope is

$$
\boxed{\frac{d\ln S}{d\ln a}=-6+\frac{2K}{H\Delta}.}
$$

For **contraction with $H<0$ and $\Delta>0$**, this is less than $-6$: $S$ grows faster than $a^{-6}$ as $a$ decreases, agreeing with the quoted sentence after Eq. (30). It does not supply a fixed exponent $p>6$ with $S\propto a^{-p}$; $K/(H\Delta)$ need not be constant. Thus “faster” describes relative growth on that branch, while “generally not a power law” describes the exact functional dependence.

The sign qualification matters. The right-hand side of Eq. (30) is positive **iff $\Delta>0$**, not merely because the geometry is KS or the volume is contracting. If $H<0$ and $\Delta<0$, the slope is greater than $-6$ and $a^6S$ decreases; $S$ need not even grow throughout such an interval. The source's suggested data after Eq. (37) include $\dot Y_0=0$, which gives $\Delta_0=3H_0$; if that instant is volume-contracting, its $\Delta_0$ is negative. This algebraic observation precludes treating the prose's positivity claim as a theorem for every KS datum. At $\Delta=0$ the logarithmic formula is undefined, but the integral law remains regular and $\dot\Delta=K$; shear cannot remain zero on an interval at finite $Y$. No universal fixed shear power follows from the printed equations alone.

**(b) Does the $a^{-6}$ degeneracy hold?**

With no production, the source's number equation (34) at $\beta=0$ gives

$$
N_0=a^3n_{\rm f}=\text{constant},\qquad
\alpha n_{\rm f}^2=\alpha N_0^2a^{-6}.
$$

Here $\alpha$ is the positive, constant coefficient in the source's FLUID Eq. (1), $\tilde\epsilon=\epsilon-\alpha n_{\rm f}^2$ and $\tilde p=p-\alpha n_{\rm f}^2$. No value or additional matter relation is chosen.

The spin term retains exact $a^{-6}$ scaling, but the KS shear has the additional coefficient $[C+I(t)]^2/3$. Therefore the **exact shear–spin $a^{-6}$ degeneracy does not hold in finite-curvature KS**. Within the two geometries being compared, it is the flat Bianchi I result, recovered when the curvature source is absent ($K=0$, so $I=0$). A small curvature contribution might permit an approximation on a specified interval; it does not restore exact conservation.

For $S>0$, the dimensionless torsion/shear ratio makes the difference explicit:

$$
R=\frac{\kappa\alpha n_{\rm f}^2}{S}
 =\frac{3\kappa\alpha N_0^2}{[C+I(t)]^2},\qquad
\dot R=-\frac{2K}{\Delta}R\quad(\beta=0).
$$

**(c) What transfers from B1?**

B1 compared $\kappa\alpha N_0^2$ with a conserved $a^6S=\Sigma^2$. In KS, the latter is not conserved. Also, the source's first field equation (10), rewritten using the definitions above and Eq. (1), is

$$
3H^2=\kappa(\epsilon-\alpha n_{\rm f}^2)+S-K.
$$

Thus the flat constraint and its constant-only bounce criterion cannot simply be imported either.

There is nevertheless a precise surviving directional statement: on an interval with $\Delta>0$ and no production, $R$ is nonincreasing (strictly decreasing for positive number density), so data with $R\le1$ cannot evolve to $R>1$ while that sign holds. The source's printed Eq. (32), $2\kappa\alpha n_{\rm f}^2>2S+\kappa\epsilon$, requires $R>1$ when $\epsilon>0$, so those data cannot reach that inequality on this interval. This is a curvature-driven monotonicity argument, not a comparison of constants. For $\Delta<0$, $R$ instead increases; that fact alone proves neither threshold crossing nor a bounce. The failure of the flat argument supplies no contrary KS solution and no general KS bounce classification.

**B1 — FAILS as a transfer of the comparison-of-constants conclusion, because KS curvature makes $a^6\sigma^2$ and the torsion/shear ratio evolve, although initially subdominant torsion still cannot overtake shear without production on the source's $\Delta>0$ branch.**

**(d) What transfers from B3's production mechanism and result?**

**Verbatim quotation — publisher HTML, Eq. (34), `Equ34`; read directly, not arXiv:**

> $$\begin{aligned} \dot{n}_{\text {f}}+3Hn_{\text {f}}=\beta H^{4},\quad \frac{d(n^{2}_{\text {f}})}{dt} +6Hn^{2}_{\text {f}}=2\beta n_{\text {f}}H^{4}. \end{aligned}$$
>
> (34)

**Verbatim quotation — publisher HTML, immediately before Eq. (35); read directly, not arXiv:**

> To avoid a singularity, the rate of \(n^{2}_{\text {f}}\) must exceed the rate of \(\sigma ^{2}\). Comparing (34) with (30) gives

**Verbatim quotation — publisher HTML, Eq. (35), `Equ35`; read directly, not arXiv:**

> $$\begin{aligned} \frac{2\beta n_{\text {f}}}{81}\Bigl (\frac{\dot{X}}{X} +\frac{2\dot{Y}}{Y}\Bigr )^{4}>\frac{2}{3Y^{2}}\Bigl (\frac{\dot{X}}{X} -\frac{\dot{Y}}{Y}\Bigr ). \end{aligned}$$
>
> (35)

**Verbatim quotation — publisher HTML, immediately after Eq. (35); read directly, not arXiv:**

> After the formation of the event horizon, at the instant when (32) is reached, this inequality must be satisfied to ensure that (32) continues to hold.


Eq. (34) is already a KS equation. With $\Psi=\beta H^4$ and $N=a^3n_{\rm f}$ it gives, without a thermal closure,

$$
\dot N=a^3\Psi,\qquad
N(t)=N(t_0)+\int_{t_0}^{t}a^3(t')\Psi(t')\,dt',\qquad
\alpha n_{\rm f}^2=\alpha a^{-6}N(t)^2.
$$

For $n_{\rm f}>0$ and $H\ne0$,

$$
\frac{d\ln n_{\rm f}}{d\ln a}=-3+\frac{\Psi}{Hn_{\rm f}},\qquad
\frac{d\ln(\alpha n_{\rm f}^2)}{d\ln a}
=-6+\frac{2\Psi}{Hn_{\rm f}}.
$$

With positive production, these slopes are greater than $-3$ and $-6$ during expansion (slower dilution, or growth), and less than $-3$ and $-6$ during contraction (faster compression-driven growth). For the collapse in question, **number density grows faster than $a^{-3}$** is the appropriate wording. At $n_{\rm f}=0$ or $H=0$, use the integral and time-derivative equations rather than these logarithms.

**Number-density mechanism — TRANSFERS:** the same volume balance makes $a^3n_{\rm f}$ increase and changes the coefficient of the spin term in KS. There is, however, no pre-existing exact KS shear–spin degeneracy for production to break; both coefficients can now evolve.

The exact comparison with shear, wherever $n_{\rm f}>0$ and $S>0$, is

$$
R(t)=\frac{3\kappa\alpha N(t)^2}{[C+I(t)]^2},\qquad
\boxed{\frac{\dot R}{R}
=2\left(\frac{\Psi}{n_{\rm f}}-\frac{K}{\Delta}\right).}
$$

In flat Bianchi I the second term vanishes and every positive source increases $R$. In KS on the positive-source branch, increasing $R$ requires the additional comparison

$$
\frac{\Psi}{n_{\rm f}}>\frac{K}{\Delta}\qquad(\Delta>0).
$$

Production therefore contributes in the same helpful direction, but positivity of $\Psi$ alone does not fix the net ratio's sign. On a $\Delta<0$ interval the curvature contribution also increases $R$; that conditional sign does not settle the later evolution. The quoted Eq. (35) explicitly displays the source's intended competition between production and curvature-sourced shear. The fractional-rate identity above keeps the normalization of the actual torsion/shear ratio explicit; no standalone sufficient bounce theorem is inferred from Eq. (35).

B3's flat-geometry theorem required its particular dynamical system as well as number production. The changing KS shear coefficient and the curvature term in the constraint prevent transferring that proof merely by retaining Eq. (34). This report establishes the production contribution, not that it necessarily wins throughout a KS collapse; no failed KS rescue is inferred from this unresolved comparison.

**B3 — UNDETERMINED for transfer of its guaranteed bounce result, because the number-production mechanism transfers exactly but must compete with KS curvature-sourced shear, whose growth is not bounded by number balance alone.**
