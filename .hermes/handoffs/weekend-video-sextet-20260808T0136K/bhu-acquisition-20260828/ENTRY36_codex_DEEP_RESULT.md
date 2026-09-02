AUDIT_HOLDS_CONSISTENCY_ONLY

## 1. Construction, theorems, and the allegedly unmeasured parameter

The construction is a spatially flat (`k=0`) FRW interior, with uncoupled radiation and pressureless matter after decoupling, matched across an outgoing spherical shock to a static TOV exterior. The paper itself describes the division as FRW inside and TOV outside (lines 81–87), fixes critical expansion at lines 90–93, and gives the post-decoupling matter/radiation assumptions at lines 108–125. Its equation of state is (Q=3\alpha/R^4+\beta/R^3), (P=\alpha/R^4); radiation therefore supplies the pressure while matter is pressureless.

The mathematical result is conditional existence, not uniqueness of the whole spacetime. Given a solution of the shock ODEs and positivity plus subluminal-speed hypotheses, Theorem 3 supplies a (C^{1,1}) coordinate transformation, Lipschitz matching, a weak Einstein solution, Rankine–Hugoniot conservation, and no delta-function surface source (lines 1118–1142). Separately, the phase-plane analysis selects a unique bounded **TOV-pressure orbit**; the introduction immediately warns that this orbit “does not constrain either the initial shock position or the TOV energy density” (lines 143–149). The paper invokes entropy increase as motivation (lines 76–80), but in this source it does not prove a separate Lax entropy inequality for the selected cosmological solution. The operational physical restrictions used for the estimates are positivity, (\bar Q>\bar P), outward evolution, and the conditional subluminal hypothesis.

There are two distinct starred quantities, and conflating them obscures the freedom:

- (R_*) is not a radius. It is the scale factor (hence starting epoch) at which the authors assume the settled shock model begins. It remains a freely chosen/unmeasured reference epoch within the stated range.
- (r_*=r(R_*)) is the shock’s initial FRW radial position. It is an integration constant. The paper says explicitly that “the only remaining piece of information missing is the initial condition for the shock-wave” (lines 2933–2935), and later explicitly introduces “the initial condition (r=r_*) at (R=R_*)” (lines 3440–3443). Physics bounds (r_*); it does not select it.

Thus the sweep’s substantive point survives, with a notation correction: the family is indexed by both a chosen start epoch (R_*) and an allowed initial position (r_*), while the paper’s evolution equation fixes only the increment once those are supplied.

## 2. What is actually computed from (H_0) and (T_0)

The strong introductory wording says that the model derives “precise estimates” at the epoch when (H_0) and (T_0) agree with observations and calls the resulting constraint free of adjustable parameters other than those observations (lines 94–104). The body qualifies that claim.

First, the observations normalize the FRW constants. With (R_0=1), the paper sets (Q_0=3\alpha+\beta=H_0^2) (lines 1785–1795). It then derives

\[
\alpha=\frac{\hat a}{3}T_0^4,\qquad \beta=H_0^2-\hat aT_0^4
\]

as equations (7.13)–(7.14) (lines 3138–3183), using the observed inputs (H_0=100h_0\,\mathrm{km\,s^{-1}\,Mpc^{-1}}) and (T_0=2.736\,\mathrm K) (lines 3197–3215).

Second, equation (7.31) predicts only the **squared propagation increment**:

\[
\frac{2.62\times10^{-7}T_0^4}{h_0^2H_0^2}\ln\frac1{R_*}
\le r^2-r_*^2\le
\frac{2.65\times10^{-7}T_0^4}{h_0^2H_0^2}\ln\frac1{R_*}.
\]

This is stated at lines 3377–3399, and the paper emphasizes that (r^2-r_*^2), not (r), is essentially independent of (r_*) (lines 3409–3411). For the illustrative choices (h_0=.55), (T_0=2.736\) K, and (R_*=2.7/4000=6.75\times10^{-4}), equation (7.33) gives (r^2-r_*^2\simeq(.019/H_0)^2) (lines 3412–3425), i.e. an extra distance of about (0.019H_0^{-1}) only if one takes the square-root increment in the special (r_*=0) case. Arithmetic from (7.31):

\[
\sqrt{2.62\times10^{-7}}\,\frac{2.736^2}{.55}\sqrt{\ln(4000/2.7)}=0.0188.
\]

Third, physical admissibility gives an **upper bound**, not a selected initial radius: equation (7.34) bounds (r_*^2) through (\bar Q>\bar P) (lines 3440–3469). Consequently the present maximum (r_{\max}) remains an explicit function of (R_*) in equations (7.35)–(7.36) (lines 3473–3530), and the final present-position result is a lower/upper window, equations (7.37)–(7.38), conditional on (R_*) and the admissibility assumptions (lines 3533–3591). There is no unique present radius in Hubble lengths or Mpc from (H_0,T_0) alone.

For scale, the paper’s Hubble length is (H_0^{-1}\simeq(0.98/h_0)\times10^{10}) light-years (lines 3400–3408). With (h_0=.55), (0.019H_0^{-1}\simeq3.39\times10^8) light-years, about (104) Mpc. That is the propagation increment for the illustrative start epoch, not a determined center-to-shock radius.

## 3. Observability

The source does not place the shock unambiguously relative to our past light cone. Nor does it derive a CMB temperature edge, density-jump image, anisotropy amplitude, angular scale, spectral sign, or any other detection statistic. The only location claims are geometric scale statements: the abstract says the present center-to-shock distance is “comparable to the Hubble distance” (lines 8–14), while the actual estimates are the conditional family above. The model also places the observer in a special position and acknowledges conflict with the Copernican principle and the observed directional uniformity of the CMB/redshifts (lines 59–69), but gives no magnitude or threshold for that anisotropy.

The closing discussion merely asks whether distant observed objects could be other explosions and whether similar explosions beyond our own shock might be observable; it presents those as questions, not signatures or predictions (lines 318–333). Therefore the paper provides no observable with a stated sign and magnitude by which its own shock could be tested.

## 4. Meaning of “accounts for” (H_0) and (T_0)

(H_0) and (T_0) are inputs. The authors choose “present time” to mean the model epoch at which those quantities agree with their observed values (lines 97–101), choose (R_0=1), impose (Q_0=H_0^2) (lines 1785–1795), and use (T_0) to fix (\alpha) and (H_0) to fix (\beta) via (7.13)–(7.14) (lines 3138–3183). Hence “accounts for” means that the FRW side adopts the standard post-decoupling equation of state and is normalized to the measured present expansion and radiation temperature. Neither (H_0) nor (T_0) is an output or an independent success. A radius expressed in the borrowed unit (H_0^{-1}), with its coefficients also fixed using (H_0,T_0), is not calibration against independent data.

## 5. Tier consequence

The tier remains **CONSISTENCY-ONLY (A(a))**. The paper establishes a mathematically interesting, conditionally admissible FRW–TOV shock construction and derives a narrow bound on the shock’s accumulated motion after a chosen start epoch. But it does not fix the start epoch, does not fix the initial shock radius, does not return a unique present shock position from (H_0,T_0), and does not map its conditional geometric window to a measurable signature with sign, magnitude, or comparison threshold. The lane may own a missing threshold, never a missing number; here both the independently predicted number and the observational mapping are missing.

The 2026-08-28 **QUALITATIVE-DIRECTIONAL flag does not survive adjudication**. “Comparable to the Hubble length” is qualitative prose attached to a family constrained by physical inequalities, not a directional observable. There is therefore no genuine present-shock prediction to forward to Duho as a tier-adjacent candidate. The strongest defensible quantitative statement is conditional: for (h_0=.55), (T_0=2.736\) K, and the assumed (R_*=2.7/4000), the shock advances about (0.019H_0^{-1}\approx104) Mpc beyond comoving freefall, while its absolute present radius still depends on (r_*) (and its allowed maximum on (R_*)).

In plain language: the paper proves that a flat expanding FRW region can be joined consistently to a static TOV exterior by a real shock and that reasonable exterior matter limits how far that shock could be. It does not tell us where the shock is today from the Hubble constant and CMB temperature alone. Those measured quantities are fed into the model, and an assumed start time plus an unfixed starting radius remain. Since the paper also supplies no concrete sky signature, its result is a consistency construction with conditional scale estimates, not an observational prediction.
