# Limiting-case and regression checks

1. **Centre crossing identity:** `chi_0`, `r_*(eta_0)`, and `2-eta_0` agree to the root solver tolerance. Exactly one crossing root was found on the gated time interval.

2. **Shock-state algebra:** the dimensionless initial TOV density is formed as `C_s=kappa rho_s r_s^2=3 v_s N_s`, directly from the pinned definitions.

3. **Integrated pressure equation:** the numerical solver uses the exact first integral `rho/rho_s=[(N-1)/(N_s-1)]^[(1+w)/(2w)]`; density is positive and tends to zero at the past horizon for all `0.01<=w<=0.999`.

4. **Horizon transfer:** the integration stops at `N-1=1e-10`. Across 100 w values, the largest remaining frequency factor is `g=4.2572e-6`; the largest local source intensity at the cutoff is `1.0850e-43`. This confirms the analytic limits `g->0`, horizon incident intensity `g^4 I_h->0`, and local source `S->0`.

5. **Transparent limit:** with no incident horizon beam, `I_ext = lambda integral S dH + O(lambda^2)`, so `I_ext->0` and the crossing is dark as `lambda->0`. The smallest sampled crossing temperature is `0.05330` of the unshocked reference.

6. **Opaque limit:** after changing variable to `y=lambda H`, `I_ext=integral S(y/lambda)e^-y dy -> S(0)=1`. At `lambda=1e4`, the crossing factor is `1.51299...1.51310` across w, approaching the analytic Doppler-only value `D=1.5131`. The dipole approaches `a1=0.615243275680`.

7. **Monotone intensity but not necessarily monotone dipole:** every one of the 100 w tracks has monotonically increasing `I_ext(lambda)`. The dipole has an interior turning point for 28 tracks; these are retained rather than smoothed away.

8. **Brightness transition:** all 100 w tracks cross `Q=1` once on the sampled opacity range. Log-lambda interpolation places the transition in `lambda=2.43...13.83`.

9. **Nonlinear angular regression:** for the junction closure, `lambda=1`, and `x_off/R_cross=1e-4`, solving the full crossing equation at 41 values of mu and integrating the Legendre coefficient gives `a1=0.6278442`. The derivative prediction on the nearest w grid is `0.6279711`, a relative difference `2.02e-4`; the difference is dominated by using the nearest tabulated w rather than the exact junction w.

10. **Finite-output check:** `p6_opacity_surface.csv` has exactly 8,100 data rows (`100 w x 81 lambda`), all numerical entries are finite, and `p6_w_sweep.csv` has exactly 100 data rows.
