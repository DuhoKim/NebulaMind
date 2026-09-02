POSITIVITY_HOLDS

# Third-seat adjudication: does the monopole-subtracted Reading-B spectrum go negative?

**Verdict: it does not.** `P_B(k) > 0` for every `k > 0`. agy's `min(P_B) ~ -2.8e-09` is a
numerical artefact of his own quadratures, reproduced here on demand and switched off on demand.
The construction is **not** excluded by a positivity violation.

**But codex is right for the wrong reason.** His script does not implement the window in the brief:
his `wtilde()` is the transform of a window supported on `2*chi_S = 28,030 Mpc`, twice the claimed
causal horizon. So his positivity PASS is a correct computation of a different construction, and his
`S_1/2 = 23,900 uK^4` is the `S_1/2` of that different construction, not of Reading B.

Script: `cutoffA_positivity_third.py` (run to completion, 103 s, exit 0; raw log `_tmp_third_out.txt`).
No CAMB, no `S_1/2`: this settles the SIGN question only.

---

## 1. Implementation differences between the two seats

| | codex `cutoffA_monopole.py` | agy `cutoffA_monopole_agy.py` |
|---|---|---|
| **Window support** | **`2*chi_S = 28,030 Mpc`** (`z = s*A` in `wtilde`, prefactor `4 pi A^3/3`) | `chi_S = 14,015 Mpc` — **correct** |
| Window representation | Fourier only: `W~(k) = (4 pi A^3/3)[3 j1(kA)/(kA)]^2` | Real space: `W = (1-x)^2(2+x)/2`, `x = r/L` |
| Where `xi` is built | never built; works with `P_LCDM` directly | `xi = simpson(Delta^2/q * sinc(qr), x=q)` on `q = geomspace(k_min, 20, 20000)` |
| Measure for `c` | `c = P_conv(0)/W~(0)` — algebraically identical to `<W xi>/<W>` | `c = simpson(r^2 W xi)/simpson(r^2 W)` — as specified |
| Subtraction | **Fourier**: `Delta^2_B = conv - k^3 c W~(k)/(2 pi^2)` | **Real space**: `xi_B = (xi - c) * W` |
| `k` grid | `1e-7 .. 6e-3` (225 pts) + `6e-3 .. 5` spliced | `geomspace(1e-7, 2.0, 2000)` |
| `r` grid | none | `linspace(1e-5, 14015, 20000)`, **linear**, Simpson |
| `q`/`mu` integration | `7200` log-`q` pts x `320`-node Gauss-Legendre in `mu` | Simpson in `q` (not `ln q`) |
| High-`k` normalisation | divides everything by `norm = median(db/primordial) = 1.04951` | splices to exact LCDM at `k = 0.1` |
| `k_max` | `2.0` | `20.0` |
| Negative handling | none needed | `Delta^2_B = maximum(Delta^2_B, 1e-30 As)` **after** `min_P` is recorded |

### Which of these can change the sign of `min(P_B)`

Ranked by whether they actually can:

1. **The window support (codex).** Decisive for *what is being computed*, and the single most
   important finding here. It does not by itself flip the sign — I verified positivity holds for
   both supports — but it means codex's numbers describe a 28,030 Mpc window.
2. **agy's `q`-quadrature for `xi`** — CAN and DOES flip the sign. Simpson on a `geomspace`
   `q`-grid up to `q = 20` gives `d(q r) = 268 radians per step` at `r = chi_S`. The resulting
   error in `xi` is tiny in the bulk (`1.8e-14` absolute on `xi ~ 2.3e-08`, i.e. `8e-07` relative
   for `r > 100 Mpc`) but it is *coherent and oscillatory in `r`*, and it beats against `sinc(kr)`
   at `k ~ 1.6-1.9 /Mpc` — exactly where his minimum sits.
3. **agy's linear `r` grid for the `r -> k` transform** — amplifies the above. `dr = 0.701 Mpc`
   against a half-period of `pi/2 = 1.571 Mpc` at `k = 2` is **2.24 Simpson points per half period**.
4. Fourier vs real-space subtraction: **not** sign-relevant. They are the same operation; I checked
   codex's `c` convention is algebraically correct (`P_conv(0)/W~(0) == <W xi>/<W>`).
5. codex's `norm = 1.04951` divide: **not** sign-relevant (a positive rescale). It is however
   physically wrong — see §5.
6. `k_max` (2 vs 20 vs infinity): **not** sign-relevant. Truncation perturbs `xi` only for
   `r <~ 1/k_max`, which the `r^2` measure suppresses.

**The `2 chi_S` window is provable, not inferred.** Two independent lines:
`codex_wtilde(k) == W~(k; chi = 2A)` to every digit printed; and codex's own reported `c` values
match the closed form for `chi = 2A` at two different `k_min`, and do not match `chi = A`:

```
k_min=4.483186e-10 : codex c=4.05905805e-08 | closed form chi=2A -> 4.05905805e-08 | chi=A -> 4.23706726e-08
k_min=4.483186e-09 : codex c=3.16890163e-08 | closed form chi=2A -> 3.16890163e-08 | chi=A -> 3.34691084e-08
```

agy's `c`, by contrast, is right: his `2.26e-09, 8.40e-09, 1.52e-08, 2.26e-08, 3.05e-08` match my
closed form `2.132859e-09, 8.396647e-09, 1.518770e-08, 2.255040e-08, 3.053286e-08`.

---

## 2. The key simplification: the IR regulator can be removed exactly

With `Delta^2 = As (k/k0)^(ns-1)` a pure power law, `alpha = 1 - ns`:

```
xi(r; k_min) = As k0^alpha [ r^alpha * G  +  k_min^(-alpha)/alpha ] ,
G = Gamma(ns-2) sin(pi (ns-2)/2) = -28.07351802     (analytic continuation)
```

The `k_min`-dependent term is **`r`-independent**, so `c` annihilates it exactly. Hence, with no
regulator at all and no extrapolation:

```
xi(r) - c = B (r^alpha - m),  B = As k0^alpha G = -5.3070109201e-08 ,  m = <r^alpha>_mu = 1.361965595
```

Validated against 40-digit mpmath integration of `int dk k^(ns-2) sinc(kr)` at 8 `(r, k_min)` points,
worst relative error `1.8e-14`. This is why both seats correctly saw convergence as `k_min -> 0`.

---

## 3. My numbers

### Mandated zero-mode check (task 3a)

`P_B(k_S = 4.483186e-04) = 5.00278041e+02 Mpc^3` is the reference scale.

```
     k [1/Mpc]       P_B(k) [Mpc^3]   |P_B|/P_B(k_S)        P_B/k^2 [Mpc^5]
    1.0000e-12    -8.5562994846e-11       1.7103e-13      -8.5562994846e+13
    1.0000e-11    -8.4561279013e-11       1.6903e-13      -8.4561279013e+11
    1.0000e-10     6.8627300567e-12       1.3718e-14       6.8627300567e+08
    1.0000e-09     9.1598430398e-09       1.8310e-11       9.1598430398e+09
    1.0000e-08     9.2445715970e-07       1.8479e-09       9.2445715970e+09
    1.0000e-07     9.2454181904e-05       1.8481e-07       9.2454181904e+09
    1.0000e-06     9.2453695027e-03       1.8480e-05       9.2453695027e+09
    4.4832e-04     5.0027804109e+02       1.0000e+00       2.4890745718e+09
```

**`|P_B(1e-09)| / P_B(k_S) = 1.8310e-11`. The requirement is `< 1e-3`. PASS.**

I state the trap explicitly, because the previous attempt fell into it: `P_B(k_tiny)` **is** the
minimum of the curve on any grid reaching down to `k_tiny`. That is forced by `P_B(0) = 0` and is
expected, not a silent failure. What makes it a real check is the third column: `P_B/k^2` settles on
the **positive** constant `9.2454e+09`, which is exactly the analytic `P_B''(0)/2 = 9.245427e+09`
from §4. Agreement to 5 digits over three decades of `k`.

Honest caveat, disclosed: below `k ~ 1e-10` the direct real-space sum hits its double-precision
cancellation floor (`~1e-10 Mpc^3` absolute), which is why `k = 1e-12, 1e-11` come out slightly
negative. Those two entries are roundoff, not physics; the analytic `k^2` law of §4 governs that
region and is positive.

### Mandated grid convergence (task 3b)

Level `L` uses `1500*L` Gauss-Legendre panels (16 nodes each) in `r` and `1000*L` log-`k` points on
`k in [1e-9, 2.0]`:

```
  lev  r-panels   k-pts  N_r nodes   min P_B [Mpc^3]      k at min  #(P_B<0)    min P_B/P_LCDM
    1      1500    1000      24000    4.55489567e-09   2.00000e+00         0    1.00057971e+00
    2      3000    2000      48000    4.55514588e-09   2.00000e+00         0    1.00063467e+00
    4      6000    4000      96000    4.55517669e-09   2.00000e+00         0    1.00063320e+00
    8     12000    8000     192000    4.55518043e-09   2.00000e+00         0    1.00063437e+00
```

Sign is stable under 1x/2x/4x/8x; `min(P_B)` converges monotonically to 6 digits; **zero negative
grid points at every level.** The grid minimum sits at the top of the `k` range and is just the
natural `k^(ns-4)` decay, not a dip.

Because a log grid can step over a narrow dip, I added dense **linear** scans:

```
  k in [1.0e-05,  0.01]  dk=8.317e-08 (5390.5 pts per 2pi/chi_S) : min P_B=+3.829094e-01  #neg=0
  k in [5.0e-03,  0.20]  dk=4.875e-06 (   92.0 pts per 2pi/chi_S) : min P_B=+4.957114e-06  #neg=0
  k in [2.0e-01,  2.00]  dk=6.000e-05 (    7.5 pts per 2pi/chi_S) : min P_B=+4.555180e-09  #neg=0
  k in [2.0e+00, 10.00]  dk=4.000e-04 (    1.1 pts per 2pi/chi_S) : min P_B=+3.442286e-11  #neg=0
```

### Mandated positive controls (task 3c) — all PASS

- **A.** My transform reproduces the closed form `W~(k) = (pi chi^3/6)[3 j1(k chi/2)/(k chi/2)]^2`
  to `3.7e-15` of its peak, and returns `min W~ = +1.29e-06 >= 0`. (Pointwise *relative* error
  reaches `5.7e-03` at one `k` — that `k` sits on a zero of `W~`, where `W~` is `9e-19` of its peak;
  no double-precision real-space quadrature can be relatively accurate there. I state the control as
  absolute error over the peak. This is a corrected metric, not a loosened tolerance.)
- **B1.** **The exact control the task asked for**: no `c` subtraction, sharp IR cut. Bochner
  guarantees `>= 0`, and I get `min P_unsub = +3.372e-04` with `#neg = 0` at `k_min = 1e-4, 1e-5, 1e-6`.
- **B2.** Delta-shell control: `xi = sinc(k_a r)` is p.d., `W` is p.d., so the product's transform
  must be `>= 0`. `min = +3.97e+02, +4.01e+02, +4.34e+02` for three `k_a`; `#neg = 0`.
- **C.** Closed-form `xi` vs 40-digit mpmath integration, worst rel. err `1.8e-14`.
- **QAWO.** Fully independent oscillatory quadrature (`scipy` QAWO) at 12 `k` values agrees with the
  composite Gauss-Legendre to `1e-15 .. 1e-07`; all values positive.

### A physical check neither seat performed

`P_B(k)/P_LCDM(k) -> 1` at high `k` **with no splice and no renormalisation applied**:
`1.0533` at `k = 0.01`, `1.0184` at `0.03`, `1.0074` at `0.1`, `1.0014` at `1.0`, `1.0006` at `2.0`.
The construction recovers unmodified LCDM on its own.

---

## 4. The analytic curvature result (task 4) — this is the decisive part

`P_B(k) = 4 pi int r^2 f(r) [1 - (kr)^2/6 + ...] dr` with `f = (xi - c) W`. `P_B(0) = 0` is imposed
and `P_B'(0) = 0` because `P_B` is even in `k`, so the sign just above `k = 0` is fixed by

```
P_B''(0) = -(4 pi/3) M4 ,      M4 = int_0^chi_S r^4 [xi(r) - c] W(r) dr
```

With `d mu = r^2 W dr` and `c = <xi>_mu`, this is exactly a covariance:

```
M4 = int d mu  r^2 (xi - c) = Cov_mu( r^2 , xi )
```

**`xi` is a decreasing function of `r`, so `Cov_mu(r^2, xi) < 0`, so `M4 < 0`, so `P_B''(0) > 0`.**
`P_B` leaves the origin **upward**. Closed form for the stated parameters:

```
  int_0^1 x^(4+a) W dx  = 0.012286760636 ,  chi^a * that = 0.017178404132
  int_0^1 x^4     W dx  = 0.012500000000 ,  m * that     = 0.017024569937
  D = 1.538341952101e-04   (a 0.896% cancellation)
  M4       = -4.41436638e+09   (NEGATIVE: B<0 and D>0)
  P_B''(0) = +1.84908547e+10 Mpc^5   -> POSITIVE
```

Reproduced numerically to `9.4e-14` relative. So `P_B(k) ~ 9.245427e+09 * k^2` for `k << k_S` — the
positive constant confirmed in the `P_B/k^2` column above. **This is grid-independent: no refinement
can change it.** It is also robust in `ns` — `B` and `D` flip sign together at `ns = 1`, so the
product does not:

```
        ns   alpha=1-ns       B (sign)         D (sign)         P_B''(0)
    0.9000       0.1000    -1.4934e-08       7.7145e-04     2.609358e+10 POSITIVE
    0.9649       0.0351    -5.3070e-08       1.5383e-04     1.849085e+10 POSITIVE
    0.9900       0.0100    -2.0294e-07       3.5227e-05     1.619212e+10 POSITIVE
    1.0100      -0.0100     2.1730e-07      -2.9602e-05     1.456937e+10 POSITIVE
    1.0500      -0.0500     4.9840e-08      -1.0454e-04     1.180081e+10 POSITIVE
    1.1000      -0.1000     2.9583e-08      -1.3545e-04     9.075306e+09 POSITIVE
```

Generality worth recording: the argument needs only `W >= 0` and a **monotonically decreasing `xi`**.
It never uses the specific window shape or `chi_S`. So *no* no-zero-mode subtraction of this form,
applied to any ordinary decreasing correlation function, can be excluded by negativity near `k = 0`.
The "stronger no-go" agy hoped for cannot be obtained at small `k` at all.

---

## 5. Where agy's negative number comes from — reproduced and switched off

I re-ran agy's pipeline with his numerics substituted in one stage at a time.

**Stage 1 — his `r -> k` Simpson transform alone, fed an EXACT `xi - c`:** no negatives.
`min P_B = +5.166e-09` vs converged `+4.555e-09` (13% high at `k = 2`, no sign change).

**Stage 2 — add his `q`-grid Simpson for `xi`:** the negatives appear, and they reproduce his
reported values:

```
  k_min=1.0e-06 : min P_B = -2.004887e-09 at k=1.901586e+00 ; #neg=1
  k_min=1.0e-07 : min P_B = -2.878305e-09 at k=1.648262e+00 ; #neg=3   (he reported -2.77e-09)
  k_min=1.0e-08 : min P_B = -8.028834e-10 at k=1.719047e+00 ; #neg=1
```

**Attribution, `k` in `[1.0, 2.0]`:**

```
  (i)   agy xi + agy Simpson r->k    : min = -5.953056e-09   #neg =  15
  (ii)  agy xi + converged r->k      : min = -1.701237e-09   #neg =   4
  (iii) exact xi + converged r->k    : min = +4.555180e-09   #neg =   0
  at k = 1.6900 : (i) -5.953056e-09   (ii) -1.701237e-09   (iii) +7.596200e-09
```

Both of his numerical stages push `P_B` down; neither is physics. Three further tells:

- His negatives all sit at `k = 1.6 - 1.9 /Mpc` — the extreme top of his `k` range, at `ell ~ 20,000`
  in CMB terms. They are nowhere near the low-`k` region that carries `S_1/2`.
- His `min(P_B)` **flips sign erratically with `k_min`** (`+6.27e-10, -2.17e-09, -2.09e-09,
  -2.77e-09, +2.19e-10`) while `S_1/2` converges to 5 digits. A physical negativity would not
  come and go with an IR regulator that the construction is provably insensitive to.
- His `min_P` is recorded *before* `Delta^2_B = maximum(Delta^2_B, 1e-30 As)` clips it, so the
  clip did not mask anything — but it also means the number never influenced his `S_1/2`.

---

## 6. Which seat I believe

**On positivity: codex's conclusion, not agy's.** `P_B(k) > 0` everywhere. agy's negativity is
numerical, demonstrated by construction and removal.

**On the computation: agy's setup, not codex's.** agy's window and `c` are the ones the brief
specifies; codex's are for a window twice as wide.

So neither report should be adopted as it stands:

- **codex** should re-run with `z = s*chi_S/2` and prefactor `pi chi_S^3/6`. His positivity claim
  will survive; his `S_1/2 = 23,900 uK^4` will not — it is the `S_1/2` of a 28,030 Mpc window, and a
  wider window keeps more large-scale power, which is the expected direction of his excess over
  agy's `10,063`.
- **codex's `norm = 1.04951` renormalisation is itself an artefact.** My direct calculation shows
  `P_B/P_LCDM = 1.053` at `k = 0.01` falling to `1.0006` at `k = 2` — a real, `k`-dependent feature
  of the construction. Dividing by a single constant erases it and mis-scales everything else.
  The brief's "normalise to unchanged LCDM above `k ~ 0.006`" instruction is not needed: the
  construction reaches LCDM on its own.
- **agy** should drop the sentence "Positivity Failure" and the Schur/Bochner claim built on it.
  His `S_1/2 ~ 10,063 uK^4` is the more likely of the two to survive, because his window is right
  and his aliasing lives at `k >~ 1`, far above the modes that set `S_1/2` — but I did not verify
  that number and it is outside this adjudication.

**Scope of this verdict.** It settles the sign of `P_B` for the construction exactly as written in
the brief (`chi_S = 14,015 Mpc`, `W = (1-x)^2(2+x)/2`, `c = <W xi>/<W>`, pure power-law `Delta^2`,
`k_min -> 0`). It does not re-derive `S_1/2` and does not touch the physics of Reading B otherwise.

---

## Actual script output

```text
==============================================================================
STAGE 0 -- setup
==============================================================================
window identity  max|(1-x)^2(2+x)/2 - (1-1.5x+0.5x^3)| = 2.220e-16
chi_S = 14015.0 Mpc     k_S = 2pi/chi_S = 4.483186091e-04 /Mpc
alpha = 1-ns = 0.035100    G = Gamma(ns-2)sin(pi(ns-2)/2) = -28.07351802
B = As k0^alpha G = -5.3070109201e-08   (B < 0  =>  xi decreasing in r)
int r^2 W dr        = 1.1470122722e+11  (exact chi^3/24 = 1.1470122722e+11)
int r^2 W r^a dr    = 1.5621912517e+11
m = <r^alpha>_mu    = 1.361965594926

==============================================================================
STAGE 1 -- MACHINERY CONTROL A: numeric W~(k) vs its closed form (Bochner >= 0)
==============================================================================
W~(0): numeric 1.44137813e+12   analytic 1.44137813e+12
max ABSOLUTE error / W~(0)           : 3.726e-15   <-- the meaningful metric
min numeric W~(k)                    : +1.291181e-06   (must be >= 0)
worst POINTWISE-RELATIVE error       : 5.679e-03 at k=1.667515e+00 (z=kA/2=11685.1, j1(z)=3.70e-06)
   -- that k sits essentially ON a zero of W~ (W~ there = 1.299e-06 = 9.0e-19 of the peak).
   Pointwise relative accuracy is unattainable at the exact zeros of W~ for ANY
   double-precision real-space quadrature: the cancellation floor is ~1e-16*W~(0).
   The control is therefore stated as absolute error relative to W~(0).
CONTROL A: PASS

==============================================================================
STAGE 1b -- what window does codex's wtilde() actually implement?
==============================================================================
codex code:  z = s*A ;  wtilde = (4 pi A^3/3) [3 j1(z)/z]^2
correct   :  z = s*A/2 ; W~     = (  pi A^3/6) [3 j1(z)/z]^2

     k [1/Mpc]       codex wtilde       W~ for chi=A      W~ for chi=2A
   1.00000e-06    1.153057207e+13    1.441363975e+12    1.153057207e+13
   6.30957e-06    1.151300346e+13    1.440814673e+12    1.151300346e+13
   3.98107e-05    1.083195700e+13    1.419091804e+12    1.083195700e+13
   2.51189e-04    4.588258024e+11    7.525183774e+11    4.588258024e+11
   1.58489e-03    3.976406911e+08    3.404787013e+07    3.976406911e+08
   1.00000e-02    3.272252790e+04    1.698347688e+05    3.272252790e+04

=> codex's wtilde IS EXACTLY W~ for a window of support 2*chi_S = 28030 Mpc.
k_min=4.483186e-10 : codex c=4.05905805e-08 | closed form chi=2A -> 4.05905805e-08 | chi=A -> 4.23706726e-08
k_min=4.483186e-09 : codex c=3.16890163e-08 | closed form chi=2A -> 3.16890163e-08 | chi=A -> 3.34691084e-08

==============================================================================
STAGE 2 -- CONTROL C: validate the closed-form xi against direct integration
==============================================================================
  r [Mpc]     k_min   mpmath direct integral              closed form      rel.err
    300.0     1e-06    2.263423910683243e-08    2.263423910683224e-08    8.186e-15
    300.0     1e-08    3.797940274361909e-08    3.797940274361894e-08    3.833e-15
   3000.0     1e-06    1.717681441217826e-08    1.717681441217805e-08    1.233e-14
   3000.0     1e-08    3.252197572896488e-08    3.252197572896469e-08    5.697e-15
   7000.0     1e-06    1.505497735926212e-08    1.505497735926190e-08    1.451e-14
   7000.0     1e-08    3.040012826079741e-08    3.040012826079723e-08    5.877e-15
  14015.0     1e-06    1.326886580688510e-08    1.326886580688487e-08    1.758e-14
  14015.0     1e-08    2.861397832313132e-08    2.861397832313113e-08    6.591e-15
=> xi(r) - c = B (r^alpha - m) exactly, with NO IR regulator, since the
   k_min-dependent term k_min^(-alpha)/alpha is r-independent.
CONTROL C: PASS

==============================================================================
STAGE 3 -- the zero-mode condition, checked exactly
==============================================================================
By construction  int r^2 W (xi - c) dr = B [ int r^2 W r^a dr - m int r^2 W dr ] = 0
analytic residual = -0.000000e+00   (relative to |B| int r^2 W r^a dr : 0.000e+00)

c(k_min) for the CORRECT window chi_S = 14015 Mpc:
   k_min= 1.0e-04 -> c = 2.132859e-09
   k_min= 1.0e-05 -> c = 8.396647e-09
   k_min= 1.0e-06 -> c = 1.518770e-08
   k_min= 1.0e-07 -> c = 2.255040e-08
   k_min= 1.0e-08 -> c = 3.053286e-08
   (agy reported c = 2.26e-09, 8.40e-09, 1.52e-08, 2.26e-08, 3.05e-08 -- compare)

==============================================================================
STAGE 4 -- ANALYTIC CURVATURE AT k=0  (the decisive test)
==============================================================================
P_B(k) = 4pi int r^2 f(r) [1 - (kr)^2/6 + ...] dr  with f = (xi-c) W
  P_B(0)   = 4pi int r^2 f dr = 0                    (imposed)
  P_B'(0)  = 0                                       (P_B even in k)
  P_B''(0) = -(4pi/3) M4 ,  M4 = int_0^chi r^4 (xi-c) W dr

M4 = B [ int r^4 W r^a dr - m int r^4 W dr ] = B * chi^5 * D
  int_0^1 x^(4+a) W dx  = 0.012286760636 ,  chi^a * that = 0.017178404132
  int_0^1 x^4     W dx  = 0.012500000000 ,  m * that     = 0.017024569937  (= 1/80 * m)
  D = 1.538341952101e-04   (a 0.896% cancellation)
  M4       = -4.41436638e+09   (sign NEGATIVE, because B<0 and D>0)
  P_B''(0) = 1.84908547e+10 Mpc^5   -> POSITIVE

Interpretation: D = Cov_mu(r^2, r^alpha) > 0 identically (both factors
increase with r), and B < 0 because xi decreases with r.  Hence
P_B''(0) > 0 for ANY chi_S and any ns < 1: P_B leaves k=0 UPWARD.
P_B(k) ~ (1/2) P_B''(0) k^2 = 9.245427e+09 * k^2 for k << k_S
numeric  int r^2 (xi-c) W dr = -6.812328e-12  (target 0; = 6.81e-14 of int r^2 |xi-c| W dr)
numeric  M4 = int r^4 (xi-c) W dr = -4.41436638e+09  (analytic -4.41436638e+09 ; rel.diff 9.40e-14)

STAGE 4b -- how general is this?  M4 = int d mu r^2 (xi - c) = Cov_mu(r^2, xi),
because c = <xi>_mu.  xi is DECREASING in r, so Cov_mu(r^2, xi) < 0, so
P_B''(0) = -(4pi/3) M4 > 0.  This needs no property of the window beyond
W >= 0, and no property of the spectrum beyond a monotone xi.  Scan over ns:
        ns   alpha=1-ns       B (sign)         D (sign)         P_B''(0)
    0.9000       0.1000    -1.4934e-08       7.7145e-04     2.609358e+10 POSITIVE
    0.9649       0.0351    -5.3070e-08       1.5383e-04     1.849085e+10 POSITIVE
    0.9900       0.0100    -2.0294e-07       3.5227e-05     1.619212e+10 POSITIVE
    1.0100      -0.0100     2.1730e-07      -2.9602e-05     1.456937e+10 POSITIVE
    1.0500      -0.0500     4.9840e-08      -1.0454e-04     1.180081e+10 POSITIVE
    1.1000      -0.1000     2.9583e-08      -1.3545e-04     9.075306e+09 POSITIVE
B and D flip sign together at ns=1, so P_B''(0) > 0 on both sides.

==============================================================================
STAGE 5 -- P_B(k) by direct real-space integration, with grid refinement
==============================================================================
refinement: level L uses 1500*L r-panels (x16 GL nodes) and 1000*L log-k points
  lev  r-panels   k-pts  N_r nodes   min P_B [Mpc^3]      k at min  #(P_B<0)    min P_B/P_LCDM
                              (ratio min taken over k>=1e-3, where it is O(1))
    1      1500    1000      24000    4.55489567e-09   2.00000e+00         0    1.00057971e+00
    2      3000    2000      48000    4.55514588e-09   2.00000e+00         0    1.00063467e+00
    4      6000    4000      96000    4.55517669e-09   2.00000e+00         0    1.00063320e+00
    8     12000    8000     192000    4.55518043e-09   2.00000e+00         0    1.00063437e+00

Sign structure at each level (the mandated stability test):
  lev 1 : min P_B over k>=1e-6 = +4.55489567e-09 at k=2.00000e+00 ; ALL P_B > 0 ? True
  lev 2 : min P_B over k>=1e-6 = +4.55514588e-09 at k=2.00000e+00 ; ALL P_B > 0 ? True
  lev 4 : min P_B over k>=1e-6 = +4.55517669e-09 at k=2.00000e+00 ; ALL P_B > 0 ? True
  lev 8 : min P_B over k>=1e-6 = +4.55518043e-09 at k=2.00000e+00 ; ALL P_B > 0 ? True

DENSE LINEAR k scans (log grids can step over a narrow dip; these cannot).
Oscillation scale of the window transform is 2pi/chi_S = 4.483e-04 /Mpc.
  k in [1.0e-05,  0.01]  dk=8.317e-08 (5390.5 pts per 2pi/chi_S) : min P_B=+3.829094e-01  min P_B/P_LCDM=0.000000  #neg=0
  k in [5.0e-03,  0.20]  dk=4.875e-06 (92.0 pts per 2pi/chi_S) : min P_B=+4.957114e-06  min P_B/P_LCDM=1.004236  #neg=0
  k in [2.0e-01,  2.00]  dk=6.000e-05 (7.5 pts per 2pi/chi_S) : min P_B=+4.555180e-09  min P_B/P_LCDM=1.000626  #neg=0
  k in [2.0e+00, 10.00]  dk=4.000e-04 (1.1 pts per 2pi/chi_S) : min P_B=+3.442286e-11  min P_B/P_LCDM=1.000020  #neg=0

==============================================================================
STAGE 5b -- MANDATED ZERO-MODE CHECK   |P_B(k_tiny)| / P_B(k_S)  <  1e-3 ?
==============================================================================
P_B(k_S = 4.483186e-04) = 5.00278041e+02 Mpc^3   (this is the reference scale)
     k [1/Mpc]       P_B(k) [Mpc^3]   |P_B|/P_B(k_S)        P_B/k^2 [Mpc^5]
    1.0000e-12    -8.5562994846e-11       1.7103e-13      -8.5562994846e+13
    1.0000e-11    -8.4561279013e-11       1.6903e-13      -8.4561279013e+11
    1.0000e-10     6.8627300567e-12       1.3718e-14       6.8627300567e+08
    1.0000e-09     9.1598430398e-09       1.8310e-11       9.1598430398e+09
    1.0000e-08     9.2445715970e-07       1.8479e-09       9.2445715970e+09
    1.0000e-07     9.2454181904e-05       1.8481e-07       9.2454181904e+09
    1.0000e-06     9.2453695027e-03       1.8480e-05       9.2453695027e+09
    4.4832e-04     5.0027804109e+02       1.0000e+00       2.4890745718e+09

RATIO |P_B(1e-09)| / P_B(k_S) = 1.8310e-11   -- required < 1e-3 -> PASS
NOTE, explicitly: P_B(k_tiny) IS the minimum of the curve on any grid
that reaches down to k_tiny, because P_B(0)=0 is imposed and P_B rises
from it.  That is expected, NOT a silent failure.  The content of the
check is (i) the RATIO above, and (ii) that P_B/k^2 tends to the
POSITIVE constant P_B''(0)/2 = 9.245427e+09, which it does.

==============================================================================
STAGE 6 -- MACHINERY CONTROL B: Bochner-guaranteed cases must come out >= 0
==============================================================================
B1: NO subtraction, sharp IR cut -- P_unsub(k) = 4pi int r^2 W xi dr must be >= 0
   k_min= 1.0e-04 : min P_unsub = +3.37203177e-04  (peak 3.258563e+03, ratio 1.03e-07) ; #neg=0
   k_min= 1.0e-05 : min P_unsub = +3.37420290e-04  (peak 1.210478e+04, ratio 2.79e-08) ; #neg=0
   k_min= 1.0e-06 : min P_unsub = +3.37469769e-04  (peak 2.189124e+04, ratio 1.54e-08) ; #neg=0
   -> PASS

B2: delta-shell control -- xi_ctrl(r)=sinc(k_a r) is p.d.; W p.d.;
    so 4pi int r^2 W sinc(k_a r) sinc(kr) dr must be >= 0 for every k.
   k_a= 3.0e-04 : min = +3.96554560e+02 , max = 5.583248e+11 , ratio = +7.10e-10
   k_a= 1.0e-03 : min = +4.00693522e+02 , max = 3.364904e+10 , ratio = +1.19e-08
   k_a= 5.0e-03 : min = +4.34062368e+02 , max = 1.313446e+09 , ratio = +3.30e-07
   -> PASS

==============================================================================
STAGE 7 -- independent high-accuracy reference (QAWO oscillatory quadrature)
==============================================================================
P_B(k) = (4 pi B / k) int_0^chi r W(r) (r^a - m) sin(kr) dr, via scipy QAWO
     k [1/Mpc]             P_B (QAWO)          P_B (GL lev4)     rel.diff
   1.00000e-06     9.245369502313e-03     9.245369502828e-03    5.572e-11
   1.00000e-05     9.239655061263e-01     9.239655061272e-01    9.241e-13
   1.00000e-04     8.684462804507e+01     8.684462804507e+01    9.818e-16
   4.48319e-04     5.002780410898e+02     5.002780410898e+02    6.817e-16
   1.00000e-03     5.674346416478e+01     5.674346416478e+01    4.132e-15
   3.00000e-03     1.877112111258e+00     1.877112111258e+00    2.129e-15
   1.00000e-02     4.619863949508e-02     4.619863949508e-02    2.508e-14
   3.00000e-02     1.591879310520e-03     1.591879310519e-03    2.543e-13
   1.00000e-01     4.075525185400e-05     4.075525185344e-05    1.374e-11
   3.00000e-01     1.446411933734e-06     1.446411933150e-06    4.041e-10
   1.00000e+00     3.736695101262e-08     3.736695058452e-08    1.146e-08
   2.00000e+00     4.555180964127e-09     4.555180429569e-09    1.174e-07
all QAWO values positive ? True
agreement with composite GL: PASS

High-k physical check: P_B(k)/P_LCDM(k) must -> 1 with no hand-applied splice
   k=  0.010 : P_B=4.619864e-02  P_LCDM=4.386144e-02  ratio=1.053286
   k=  0.030 : P_B=1.591879e-03  P_LCDM=1.563047e-03  ratio=1.018446
   k=  0.100 : P_B=4.075525e-05  P_LCDM=4.045599e-05  ratio=1.007397
   k=  0.300 : P_B=1.446412e-06  P_LCDM=1.441691e-06  ratio=1.003275
   k=  1.000 : P_B=3.736695e-08  P_LCDM=3.731495e-08  ratio=1.001394
   k=  2.000 : P_B=4.555181e-09  P_LCDM=4.552257e-09  ratio=1.000642

==============================================================================
STAGE 8 -- diagnosis: reproduce agy's numerical scheme and locate his minimum
==============================================================================
agy: r = linspace(1e-5, chi_S, 20000) [linear, dr = 0.701 Mpc], Simpson;
     k_out = geomspace(1e-7, 2.0, 2000).  Half-period of sin(kr) at k=2 is
     pi/2 = 1.571 Mpc -> only 2.24 Simpson points per HALF period.

On agy's own grid (with an EXACT xi-c, so the only defect is the transform):
   min P_B = +5.166190e-09 at k = 2.000000e+00   ; #(P_B<0) = 0 of 2000
   converged value at that same k = +4.555181e-09
   first k where agy's grid goes negative: nan
   converged min over the same k range   = +4.555181e-09 at k=2.000000e+00
   max |agy - converged| for k > 0.05    = 6.110096e-10  (scale P_LCDM(2)=4.552e-09)
   max |agy - converged| for k < 0.01    = 3.269633e-10
   => his r->k Simpson transform alone does NOT produce negatives.

8b -- now also reproduce agy's xi QUADRATURE (his q-grid), the remaining difference
     agy: q = geomspace(k_min, 20, 20000), Simpson in q (not in ln q).
     At q=20 the step is dq=0.0191, so d(q r)=268 radians per Simpson step at r=chi_S.
  k_min=1.0e-06 : c_agy=1.518771e-08 (exact 1.518770e-08, rel 1.01e-06) ; max|xi_agy-xi_exact|=1.305e-08
               min P_B = -2.004887e-09 at k=1.901586e+00 ; #neg=1 ; first neg k=1.9016e+00
               converged P_B at that k = +5.309828e-09 ; |agy-conv| there = 7.315e-09
  k_min=1.0e-07 : c_agy=2.255040e-08 (exact 2.255040e-08, rel 7.38e-09) ; max|xi_agy-xi_exact|=1.305e-08
               min P_B = -2.878305e-09 at k=1.648262e+00 ; #neg=3 ; first neg k=1.6345e+00
               converged P_B at that k = +8.195582e-09 ; |agy-conv| there = 1.107e-08
  k_min=1.0e-08 : c_agy=3.053286e-08 (exact 3.053286e-08, rel 5.08e-11) ; max|xi_agy-xi_exact|=1.305e-08
               min P_B = -8.028834e-10 at k=1.719047e+00 ; #neg=1 ; first neg k=1.7190e+00
               converged P_B at that k = +7.213360e-09 ; |agy-conv| there = 8.016e-09

8c -- ATTRIBUTION: swap agy's two numerical stages in and out, k in [1.0, 2.0]
     (his reported minimum, -2.77e-09, lives in exactly this band)
     his xi is accurate to 1.76e-14 absolute for r>100 Mpc (xi itself ~ 2.31e-08);
     the whole 1.3e-08 headline error sits at his first node r=1e-05 Mpc and is
     just his k_max=20 UV truncation, which the r^2 measure makes irrelevant.
  (i)   agy xi + agy Simpson r->k    : min = -5.953056e-09   #neg =  15
  (ii)  agy xi + converged r->k      : min = -1.701237e-09   #neg =   4
  (iii) exact xi + converged r->k    : min = +4.555180e-09   #neg =   0
  at k = 1.6900 : (i) -5.953056e-09   (ii) -1.701237e-09   (iii) +7.596200e-09
  => BOTH of agy's numerical stages push P_B down; neither is physics.

==============================================================================
SUMMARY
==============================================================================
CONTROL A (W~ closed form)          : PASS
CONTROL C (xi power-law reduction)  : PASS
DENSE LINEAR k scans all positive   : PASS
CONTROL B (Bochner positive cases)  : PASS
CONTROL QAWO (independent quadrature): PASS
ZERO-MODE ratio < 1e-3              : PASS (1.831e-11)
SIGN STABLE under 1x/2x/4x/8x       : PASS
min P_B per level                   : 4.5549e-09, 4.5551e-09, 4.5552e-09, 4.5552e-09
P_B''(0)                            : +1.849085e+10 Mpc^5 (POSITIVE)

VERDICT TOKEN: POSITIVITY_HOLDS
```

---

*Third seat, 2026-09-02 KST. Files written: `cutoffA_positivity_third.py`, this verdict, and the raw
run log `_tmp_third_out.txt`. No other file touched.*
