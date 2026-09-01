UNDETERMINED_NEEDS_LINEAR_ECSK_PERTURBATION_ACTION

# RQ-B codex result — Popławski Einstein–Cartan interior transfer

## Verdict

The strict Popławski model in the cited papers fixes a **homogeneous background bounce**, not a perturbation transfer function. The papers do not determine whether a parent perturbation survives with finite amplitude or is erased. In particular, the present-day number \(\Omega_S=-8.6\times10^{-70}\) is **not** an exponential transfer suppression: the torsion contribution grows relative to radiation as \(a^{-2}\) and is order unity at the bounce.

Therefore neither `NEW_FALSIFIER_CANDIDATE` nor `CONSISTENCY_ONLY_BY_DERIVATION` follows. The missing resource is a published or explicitly supplied **second-order/linearized ECSK spin-fluid (or Dirac-field) perturbation action, including a microscopic spin-correlation closure and bounce matching/junction prescription**. With particle production retained, its Riemann–Cartan quantum production functional is also required. No tier is changed.

## 0. Source-identity correction

The brief's entry-10 pin is wrong. `1111.1017_clean.txt` is Fullana i Alfonso and Alfonso-Faus, “Quantization of the Universe as a Black Hole,” not Popławski and not PRD 85, 107502. The actual Popławski paper is arXiv `1111.4595v2`, DOI `10.1103/PhysRevD.85.107502`. I independently pinned it as:

- `../bhu-reading-20260823/sources/1111.4595v2_poplawski_prd85.pdf`, SHA-256 `dce45dbb6c4d625f828252ad354717be94cda7ebda940489873548991c1463d0`;
- extracted text `1111.4595v2_poplawski_prd85_clean.txt`, SHA-256 `2d1c7fbf9e99f30bc9cc9797e55c7e77738a6b8ab4eb1b85efbea07f0aaa3f54`.

I also pinned entry 12, arXiv `2509.11468v2`, DOI `10.1142/S0217751X25440075`:

- `2509.11468v2_poplawski_ijmpa40.pdf`, SHA-256 `1fa609e5f1d32eceda0908c34bae418344cb147301ad17acceda77c5e272c5ac`;
- extracted text `2509.11468v2_poplawski_ijmpa40_clean.txt`, SHA-256 `8297f879829f430baab68b3f8b917e8889ef878386b46f505592c71ad807b9ad`.

## 1. Field equations actually supplied

The Cartan equation is algebraic,

\[
S_{jik}-S_i g_{jk}+S_k g_{ji}=-{\kappa\over2}s_{ikj},
\]

so torsion has no independent vacuum propagation in this minimal ECSK model. Eliminating it produces corrections quadratic in the spin tensor in the Einstein equation. For an unpolarized Weyssenhoff spin fluid,

\[
s^2={1\over8}(\hbar c n_f)^2,
\qquad
\tilde\epsilon=\epsilon-\alpha n_f^2,
\qquad
\tilde p=p-\alpha n_f^2,
\qquad
\alpha={\kappa(\hbar c)^2\over32}.
\]

For the closed FLRW ansatz, the background equations are

\[
{\dot a^2\over c^2}+1={\kappa\over3}(\epsilon-\alpha n_f^2)a^2,
\]

\[
{\dot a^2+2a\ddot a\over c^2}+1=-\kappa(p-\alpha n_f^2)a^2,
\]

and

\[
{d\over dt}\left[(\epsilon-\alpha n_f^2)a^3\right]
 +(p-\alpha n_f^2){d(a^3)\over dt}=0.
\]

For ultrarelativistic matter, \(\epsilon\propto a^{-4}\), \(n_f\propto a^{-3}\), hence

\[
\epsilon_S=-\alpha n_f^2\propto-a^{-6}.
\]

These are background equations only. They contain no Fourier mode \(k\), no scalar/vector/tensor decomposition, and no equation for \(\delta s_{ij}\) or its correlations.

The Dirac-field paper uses a different averaged source. Its equations (11)–(17) yield a finite minimum \(a_{\rm cr}\), but its solution is a **cusp**: the parameter jumps from \(-\eta_{\rm cr}\) to \(+\eta_{\rm cr}\), and \(\dot a\) jumps from \(-v\) to \(+v\). Continuation of timelike background geodesics does not specify continuation of gauge-invariant perturbations through that discontinuity.

### Parent-to-background map

Entry 12 does retain finite parent dependence at the homogeneous level. For a fluid sphere,

\[
r_g={2GM\over c^2}=\kappa\int_0^{R_0}\tilde\epsilon,r^2r'\,dR,
\]

and its homogeneous ansatz gives

\[
\sin R_0=\sqrt{r_g/r_0},
\qquad
a_0=\sqrt{r_0^3/r_g},
\qquad
Mc^2={4\pi\over3}r_0^3h_*T_0^4.
\]

Thus the papers do **not** prove that all parent information is zero. They map parent mass/radius into daughter homogeneous initial data. But they never map a parent perturbation \(\delta_{\rm in}(k)\) into an observable daughter perturbation, and \(r_0\), \(R_0\), and the parent \(M\) are not independently observable from within the late daughter in the supplied model.

## 2. Why \(\Omega_S\) is not a transfer factor

Entry 9 writes

\[
H^2=H_0^2\left(\Omega_R\hat a^{-4}+\Omega_S\hat a^{-6}\right)
\]

in the early regime, with \(\Omega_R=8.8\times10^{-5}\) and \(\Omega_S=-8.6\times10^{-70}\). Therefore the magnitude ratio of the torsion background term to radiation is

\[
q(\hat a)={|\Omega_S|\hat a^{-6}\over\Omega_R\hat a^{-4}}
={|\Omega_S|\over\Omega_R\hat a^2}
=\left({\hat a_m\over\hat a}\right)^2,
\]

where

\[
\hat a_m=\sqrt{-\Omega_S/\Omega_R}=3.1\times10^{-33}.
\]

At the curvature-neglected bounce, \(q(\hat a_m)=1\). The tiny present coefficient is exactly compensated by the faster \(a^{-6}\) growth. It cannot be inserted as \(T\sim10^{-70}\), nor exponentiated into an erasure claim. Conversely, order-unity torsion at the bounce does not prove \(T\sim1\); that requires perturbation dynamics.

## 3. Transfer-function derivation and where it stops

Choose the gauge-invariant comoving curvature perturbation \({\cal R}_k\) and its canonical momentum \(\Pi_k\). A linear bounce map would have the form

\[
X_k^+={\cal M}_k X_k^-,
\qquad
X_k=({\cal R}_k,\Pi_k)^T,
\]

and the requested scalar transfer would be one projection of \({\cal M}_k\), for example

\[
T_{\cal R}(k)={{\cal R}_k^+\over{\cal R}_k^-}
\]

only after specifying the independent incoming momentum/mode or its state.

To calculate \({\cal M}_k\), one needs the quadratic action or equivalent closed linear system. Schematically a single adiabatic degree of freedom would require coefficients in

\[
v_k''+\left[c_s^2(k,\eta)k^2-{z''\over z}\right]v_k=0,
\qquad v_k=z{\cal R}_k.
\]

None of the six specified sources provides \(v\), \(z\), \(c_s^2\), \(\delta n_f\), \(\delta s_{ij}\), nonadiabatic pressure, anisotropic spin stress, or matching conditions at the bounce. The background replacement \((\epsilon,p)\mapsto(\tilde\epsilon,\tilde p)\) is insufficient: entry 9 itself warns that treating the negative spin term as an independent exotic fluid is “purely formal” and not a physical equation of state.

The missing information is not cosmetic. Distinct closures sharing exactly the same background give distinct \({\cal M}_k\):

- imposing adiabatic \(\delta n_f/n_f=(3/4)\delta\epsilon/\epsilon\), allowing spin-isocurvature, or keeping microscopic spin correlations changes \(\delta p_{\rm nad}\) and hence super-horizon \({\cal R}'\);
- the PRD cusp has a discontinuous \(\dot a\), so a mode equation contains distributional matching data not fixed by the two Friedmann equations;
- the smooth spin-fluid turning point is a different bounce realization and does not supply the missing spin perturbation closure;
- particle creation changes \(n_f(a)\) and the background itself. Entry 11 posits \(K=\beta(\kappa\tilde\epsilon)^2\) as the “simplest form,” calls \(\beta\) an undetermined constant, and says \(K\) ultimately must be derived from quantum field theory in Riemann–Cartan spacetime. Entry 12 likewise retains an unspecified \(\beta\).

Therefore an infinite family of transfer matrices—including finite transmission, mode mixing, amplification, and special closures with cancellation—shares the pinned background equations. Assigning \({\cal M}_k=0\) is an extra boundary condition, not a derivation. Assigning finite nonzero transmission is equally extra.

## 4. Direct textual cross-check

Entry 11 closes the issue explicitly: after presenting its homogeneous particle-production model, it says, “Finally, we need to derive primordial density fluctuations generated in the early universe formed in a black hole and compare them with the observed spectrum” (`1410.3881_clean.txt:364`). That is the calculation requested here, acknowledged as unfinished by the source itself. The 2025 synthesis still supplies only homogeneous collapse plus shear scaling and particle-production background equations; it adds no perturbation system.

Entry 9's preferred-axis remark also does not rescue a calibrated observable. It says a rotating parent “should” imprint small FLRW corrections containing the Kerr radius, but gives neither their metric components nor a mapping to a daughter observable. That is a prospect, not a finite transfer amplitude.

Entry 51 and its erratum do not close this gap. The VoR derives nonsingularity/finite Cartan size for Dirac matter and estimates a density/mass floor. The erratum corrects statements around equations (21), (26), and (29) in the Papapetrou section; neither contains cosmological perturbation evolution or bounce matching.

## 5. Required calculation to resolve the verdict

A determinate ruling needs all of the following in one consistent branch:

1. A matter action for either microscopic Dirac fields or a covariantly defined spin fluid, expanded to second order about the contracting and expanding closed background.
2. A closure for spin two-point functions and perturbations of the algebraic Cartan equation.
3. Gauge-invariant scalar/vector/tensor mode equations, including nonadiabatic and anisotropic-spin terms.
4. A regular bounce solution and derived junction conditions. For the PRD cusp, a distributional completion or smoothing prescription is mandatory.
5. If particle production is essential, the Riemann–Cartan quantum production functional \(K[g,S]\), not the phenomenological free \(\beta\) ansatz.
6. Initial parent perturbation data and an explicit late-time daughter observable.

Only then can one integrate a fundamental matrix \({\cal M}_k\), quote \(T(k)\), and test parent-parameter dependence. The pinned literature proves neither suppression nor survival.

## Receipts

- `1007.0587_clean.txt:72-130`: spin-fluid effective source and Friedmann equations; `:134-153`: \(a^{-6}\), \(\Omega_S\), and \(a_m\); `:244-246`: unquantified inherited rotation-axis prospect.
- `1111.4595v2_poplawski_prd85_clean.txt:141-194`: Dirac averaged source and Friedmann system; `:251-264,287-339`: cusp and discontinuous expansion; `:342-374`: numerical background results only.
- `1410.3881_clean.txt:82-119`: effective density/pressure and closed Friedmann background; `:293-319`: phenomenological \(K\) and \(\beta\); `:357-364`: explicitly unfinished density-fluctuation derivation.
- `2509.11468v2_poplawski_ijmpa40_clean.txt:165-206`: parent collapse and three arbitrary background functions; `:241-259`: parent-to-closed-FLRW map and bounce; `:268-323`: shear and phenomenological particle-production continuation.
- `0902.1994_clean.txt`: Einstein–Rosen radial geodesics and horizon identification only; no cosmological perturbation equation.
- `poplawski_plb690_vor_clean.txt:620-680` and `poplawski_plb690_erratum_clean.txt`: Cartan-density discussion and the exact erratum scope; no transfer calculation.

No tier was changed.
