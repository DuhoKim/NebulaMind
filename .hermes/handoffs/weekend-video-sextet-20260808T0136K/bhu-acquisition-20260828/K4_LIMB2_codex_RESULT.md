LIMB2_UNDETERMINED

# Codex blind limb-2 result

## Decision

The perturbed Darmois junction is neither F1 nor F2. It is a transmission/matching system. It does not, without an additional exterior radiation-state condition, define a closed spectral boundary condition for the interior. The unfixed freedom is: for every `ell >= 2` and `-ell <= m <= ell`, the Schwarzschild exterior admits arbitrary real finite-energy polar Zerilli Cauchy data—two functions per `(ell,m)`, subject to the usual reality and regularity conditions. This is a functional space, not a scalar parameter with a numerical interval. Manufacturing “no incoming radiation,” a reflecting wall, or a regularity condition at a second boundary would violate the brief. The required class is therefore `LIMB2_UNDETERMINED`.

## Background and gauge

The perturbed background is K2's B1 cell: a `k=0`, `Lambda=0` pressureless FLRW top-hat at fixed comoving `chi*`, with `R=a chi*` and `M=(4/3) pi chi*^3 rho0`, smoothly matched to Schwarzschild, class `J_SMOOTH_EXPANDING` (governing prereg section 1; `K2_RESULT_20260903.md` sections 2–4; source `gaztanaga_mass_mnras_clean.txt` line 143, whose OCR renders the fraction and cube incorrectly).

The script declares, before computation, boundary-adapted Gaussian-normal gauge: the timelike surface is `n=0`, `n` is proper normal distance, and `h_nn=h_na=0` on the surface. Scalar interior perturbations match even-parity Schwarzschild perturbations; the latter can equivalently be represented by the gauge-invariant Zerilli master field.

Script receipts:

```text
GAUGE=boundary-adapted Gaussian-normal at Sigma (n=0; h_nn=h_na=0); exterior polar modes represented by the Zerilli variable
NO_PIXEL_INPUT=TRUE
BACKGROUND=k=0, Lambda=0, dust, comoving chi*=constant, R=a chi*, M=(4/3) pi chi*^3 rho0, Schwarzschild exterior, J_SMOOTH_EXPANDING
```

## Linear Darmois conditions, multipole by multipole

On the three-dimensional timelike junction, expand the even-parity induced metric as

`h_tt=A_lm Y_lm`, `h_tA=B_lm Y_A`, and `h_AB=R^2(K_lm Omega_AB Y_lm+G_lm Y_AB)`.

Continuity of the first fundamental form gives `[A_lm]=[B_lm]=[K_lm]=[G_lm]=0`. In Gaussian-normal gauge, `delta K_ab=(1/2) d_n h_ab`, so continuity of the second fundamental form gives the same four equations for the normal derivatives. Only harmonics that exist at a given `ell` are retained (`Y_A` is absent at `ell=0`; the trace-free tensor harmonic is absent for `ell<2`). Spherical symmetry of the background diagonalizes these equations in `(ell,m)`; it does not delete nonspherical sectors.

```text
JUNCTION_DECOMPOSITION=h_tt=A_lm Y_lm; h_tA=B_lm Y_A; h_AB=R^2[K_lm Omega_AB Y_lm+G_lm Y_AB]
DARMOIS_FIRST_FORM=[A_lm]=[B_lm]=[K_lm]=[G_lm]=0 (retain only harmonics existing at that ell)
DARMOIS_SECOND_FORM=[d_n A_lm]=[d_n B_lm]=[d_n K_lm]=[d_n G_lm]=0 in Gaussian-normal gauge (same harmonic qualifications)
MULTIPOLE_STRUCTURE=rotational symmetry makes every (ell,m) match independently; it does not project onto ell=0
```

For `ell=0`, matching relates the spherical perturbation to a constant exterior mass perturbation `delta M`. For `ell=1`, the even vacuum mode is center-of-mass/gauge data. For every `ell>=2`, Schwarzschild vacuum has physical polar gravitational perturbations governed by the Zerilli equation. Its two functional Cauchy data supply exterior boundary value and normal derivative data to which the interior amplitudes are matched. Darmois continuity relates those data; it does not select them.

Birkhoff's theorem controls only the exactly spherical sector: it makes the unperturbed exterior Schwarzschild and makes its monopole mass constant. It does not say that nonspherical linear vacuum perturbations vanish.

```text
ELL_GE_2=Schwarzschild vacuum has a polar Zerilli master field with two real functional Cauchy data per (ell,m); Darmois relates its boundary value/normal derivative to the interior mode
BIRKHOFF=Birkhoff fixes only the exactly spherical exterior (ell=0) to Schwarzschild with constant mass; it says nothing that removes ell>=2 vacuum gravitational perturbations
FREE_MODE=for every ell>=2 and -ell<=m<=ell, arbitrary real finite-energy exterior Zerilli incoming/Cauchy data (two functions, subject to reality and regularity) remain unspecified
```

## F1/F2 and spectral comparison

This is not F1 because the junction acts separately at every multipole, including `ell>=2`, rather than imposing one spherical average. It is not F2 because it equates boundary data across the surface; it does not impose `W_tilde(k) delta_tilde(k)=0` and does not annihilate a continuous power spectrum (`PROGRAM_C_FLUX_RESULT_20260902.md` lines 15–22).

No radial discretization follows. A spacing `Delta k` near `pi/chi*` would arise only after adding a homogeneous reflecting/cavity condition. At the recorded causal scale `chi_section=3.149 c/H0=14,015 Mpc` (governing prereg section 2), the script computes that conditional—not derived—number as `pi/chi*=2.241593045729e-04 Mpc^-1`.

```text
SPECTRUM=without an exterior state/no-incoming-radiation condition, Darmois supplies transmission data, not a homogeneous reflecting eigencondition; k remains continuous and no Delta-k is derived
CONDITIONAL_CAVITY_SPACING=pi/chi*; if chi*=chi_section=14015 Mpc then pi/chi*=2.241593045729e-04 Mpc^-1, but this spacing is NOT implied by Darmois
F1_COMPARISON=NO: the conditions act mode-by-mode, including ell>=2, rather than only on ell=0
F2_COMPARISON=NO: they equate boundary data across Sigma and do not impose W_tilde(k) delta_tilde(k)=0 or P=0
CLASS=LIMB2_UNDETERMINED
```

Inherited limits: dust only; exact spherical symmetry of the background; `0 <= Lambda <= Lambda_c`, with the selected B1 cell at `Lambda=0` (`K2_RESULT_20260903.md` section 4). No tier, warrant token, standing, or stamp is moved.
