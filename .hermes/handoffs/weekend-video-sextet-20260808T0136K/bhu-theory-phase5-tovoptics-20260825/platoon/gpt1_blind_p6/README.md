# GPT1 blind P6 — independent TOV optical transfer

## Blindness and scope

This calculation used only `BRIEF_GPT1_BLIND_P6.md` and the gated orbit table named there, `a1_results.csv` (40,001 rows; SHA-256 `c00b26b0244b3cd649b45b117e9e95732972cb0fc256fb7b11bfddac5c8985c7`). I did not read any withdrawn P5/P6 implementation or receipt. The calculation writes only in this directory and makes no commit.

The pinned equations determine gravitational and kinematic transfer but do not supply a microscopic opacity or emissivity. I therefore do not invent a unique optical depth. I report a dimensionless grey-opacity family `lambda=10^-4...10^4`, plus the strict opaque limit. `lambda` is defined below so the results can be reinterpreted for any microphysical opacity.

## Centre crossing and geometry

At zero offset the crossing obeys

`chi_0 = r_*(eta_0) = 2-eta_0`.

PCHIP interpolation in log time of the gated table gives

- `eta_0 = 0.563388685460245`
- `chi_0 = R_cross = 1.436611314539755` (comoving)
- `t_cross = 0.0793517027261557`
- `sqrt(N_s) = 2.549947046533522`, `N_s = 6.502229940125031`
- `u_s = 0.105622785334128`, `v_s = 0.429999338539215`
- junction `w=u_s/v_s = 0.245634762353234`
- `r_*'(eta_0)=0.525179023758149`.

For `mu = n dot xhat` and small comoving offset `x`, differentiating

`sqrt(x^2+chi^2+2 x chi mu)=r_*(2-chi)`

gives

`delta eta = mu x/(1+r_*')`.

If `Q(eta,w,lambda)` is the crossing temperature factor, then

`T(mu)/<T> = 1 + a1 (x/R_cross) mu + O(x^2)`

with

`a1 = [R_cross/(1+r_*')] d ln Q/d eta`.

The numerical factor multiplying `d ln Q/d eta` is `0.941929630660566`.

## The five decisions

### 1. What the past-directed sight line terminates on

I choose the black-hole-interior time orientation required by the brief: future-directed TOV matter moves to smaller areal radius, so a past-directed ray from the shock follows increasing `rbar` until `N -> 1`, the past horizon. It does not run to the `rbar=0` future singularity.

For constant `p=w rho`, the pressure equation integrates exactly:

`rho/rho_s = [(N-1)/(N_s-1)]^q`,  `q=(1+w)/(2w)`.

Set `z=ln(rbar/rbar_s)`, `C=kappa rho rbar^2`, and `L=ln(|B|/|B_s|)`. The equations used in the script are

`dN/dz = -N-wC`,

`C = C_s exp(2z)[(N-1)/(N_s-1)]^q`,  `C_s=3 v_s N_s`,

`dL/dz = -(N+C)/(N-1)`.

Near the horizon, `x=N-1 -> 0`, `dx/dz -> -1`, and `C -> 0`. Therefore `|B| proportional x`. A collisionless comoving photon has `omega proportional 1/sqrt(|B|)`, so transfer from a horizon-side emitter to the shock is

`g = omega_s/omega_e = sqrt(|B_e|/|B_s|) proportional sqrt(x) -> 0`.

By Liouville invariance, bolometric incident intensity is weighted by `g^4 proportional x^2`; radiation from beyond the TOV horizon reaches the shock with zero strength in this limiting comoving transfer. The finite numerical horizon cutoff confirms `g<4.26e-6` across the full w sweep, so the largest residual intensity weight is below about `3.3e-22`.

### 2. Whether depth matters, and the role of B

Yes. A comoving LTE source with zero chemical potential has `T_fluid proportional rho^[w/(1+w)]`. Combined with the geodesic redshift,

`T_source,seen_at_shock / T_source,s = g (rho/rho_s)^[w/(1+w)]`,

and its bolometric source weight is the fourth power. Near the horizon, the thermodynamic factor is proportional to `sqrt(x)` and `g` is also proportional to `sqrt(x)`, so the observed source temperature is proportional to `x` and source intensity to `x^4`. Deeper (horizon-ward) layers are therefore much dimmer; B is essential.

Because no opacity coefficient was pinned, I define

`d tau/dz = lambda (rho/rho_s)(rbar/rbar_s) sqrt[(N_s-1)/(N-1)]`.

This is density times the comoving photon path element, normalized so `d tau/dz=lambda` at the shock. The dimensionless column with `lambda=1` is `H`; across w, `H_total=0.01705...0.55855`.

With no incident horizon beam, the formal grey LTE solution is

`I_ext/I_s = integral_0^Htotal S(H) exp(-lambda H) lambda dH`.

This explicit family is preferable to pretending the pinned hydrodynamics specifies a unique microscopic opacity.

### 3. Observable normalization

All directions share a potentially large monopole, including the Doppler factor and mean grey transfer. I divide the directional temperature by its all-sky mean before extracting the Legendre dipole. Equivalently, the linear coefficient is a derivative of `ln Q`, not of Q. This removes any common calibration or source-temperature factor while retaining the crossing-time anisotropy.

The exterior fluid is inward-moving relative to the FRW observer and the relevant photons propagate forward, inward toward the observer. I therefore use the forward Doppler temperature factor

`D = gamma(1+beta) = sqrt[(1+beta)/(1-beta)]`,  `beta=1/sqrt(N_s)`.

At the centre crossing, `D=1.5131`. The transfer used in the anisotropy is

`Q = D (I_ext/I_s)^(1/4)`.

### 4. Radius used to normalize x_off

I normalize with the **comoving shock radius at the zero-offset light-cone crossing**, `R_cross=r_*(eta_0)=chi_0=1.436611314539755`. Both `x_off` and the crossing equation are comoving. The areal TOV radius has different units/slicing, and the shock radius at observer time is not the surface actually sampled by the light cone.

### 5. Behavior as opacity increases

The exterior intensity itself strengthens monotonically from zero in the transparent/no-emission limit to the local shock source in the strict opaque limit. The crossing temperature relative to an unshocked FRW direction likewise rises monotonically. It is dim for small lambda, becomes comparable at `lambda approximately 2.43...13.83` (depending on w), and is bright in the opaque limit because the inward Doppler boost remains: `Q -> D=1.5131`.

The **normalized dipole is not universally monotone**. Twenty-eight of the 100 sampled w values have a resolved interior turning point across the opacity grid. For example, near the junction closure it rises to a shallow maximum near `lambda about 5` and then falls to the opaque asymptote; at large w it weakens monotonically from its thin-limit value; at very small w it strengthens toward the opaque value. I report the computed surface rather than fitting a trend.

## Results

The observational fractional limit is

`3.7 mK / 2.7255 K = 0.00135754907356448`.

The bound is

`x_off/R_cross < 0.00135754907356448 / |a1|`.

Key results:

- Strict opaque limit (independent of w because the photosphere is at the shock): `a1=0.615243275680`; `x_off/R_cross < 0.00220652403241`; `x_off < 0.00316991739076` in the pinned comoving units.
- Strongest anisotropy on the sampled `(w,lambda)` surface: at `w=0.999`, `lambda=1e-4`, `a1=0.700762047791`; `x_off/R_cross < 0.00193724685554`; `x_off < 0.00278307075172`.
- Across the entire sampled surface, `a1=0.50256...0.70076`, giving `x_off/R_cross < 0.001937...0.002701`.
- At the exact junction closure and `lambda=1`: `I_ext/I_s=0.0865932526`, `Q=0.820962879` (dimmer), `a1=0.627060377`, and `x_off/R_cross < 0.00216494157`.

Thus the plain brightness answer is conditional but unambiguous: a transparent or moderately thin crossing is **dimmer** because horizon-side radiation is killed by the B redshift and little local source is accumulated; a sufficiently opaque crossing becomes **comparable and then brighter**, saturating at the Doppler-boosted shock photosphere.

## Deliverables

- `p6_blind_transfer.py` — independent calculation.
- `p6_w_sweep.csv` — one row per w, selected opacity values, each w's strongest sampled dipole, and opaque limit.
- `p6_opacity_surface.csv` — all 8,100 `(w,lambda)` results.
- `p6_summary.json` — centre crossing, headline extrema, bound, and nonlinear check.
- `horizon_diagnostics.json` — horizon convergence diagnostics for every w.
- `LIMITING_CASE_CHECKS.md` — explicit checks.
- `RUN_RECEIPT.json` — hashes and row counts.

No publication, repository commit, or mutation outside this directory was performed.
