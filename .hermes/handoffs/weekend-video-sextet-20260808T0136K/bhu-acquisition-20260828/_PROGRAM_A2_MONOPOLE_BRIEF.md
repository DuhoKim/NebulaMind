# Does monopole subtraction rescue Reading B? — the referee's first objection, tested

## Where this stands

Reading B of the causal condition is `ξ(r) = 0` for `r > χ_§` on the primordial field, built as
`ξ_B = ξ_ΛCDM · W` with `W` a positive-definite window compactly supported on `[0, χ_§]`,
`χ_§ = 14,015 Mpc`. Two independent seats computed it and both found **`S₁/₂` depends on the IR
regulator and does not converge** — codex 252,066 → 900,646 μK⁴ over three decades of `k_min`, agy
diverging, 553,328 at `k_min = 10⁻⁸`.

**The mechanism both identified:** `ξ(r) = ∫ dk/k Δ²(k) sinc(kr)` is log-divergent in the IR, and the
divergent piece is `r`-independent — an unobservable **monopole**. Windowing converts that constant
into physical low-k power, because `c·W̃(k)` is concentrated at `k ≲ 2π/χ_§`, exactly the multipoles
that dominate `S₁/₂`. Observed scaling fits `S₁/₂ ∝ c²`.

## THE OBJECTION YOU ARE TESTING

**A referee will say: "that constant is unobservable — just subtract the monopole."** If so, the
divergence is an artifact of the construction rather than a property of the model, and Reading B may
give a perfectly stable number. **Both prior seats used the same construction, so their agreement
does not exclude a shared error of exactly this kind.** Settle it.

## The condition to impose

Impose **no zero mode**: choose the subtraction constant `c` so that the windowed correlation carries
no monopole, i.e.

    P_B(k → 0) = 0,   equivalently   ∫ d³r W(r) [ ξ_ΛCDM(r) − c ] = 0

so `c = ∫d³r W ξ / ∫d³r W`. This is physically motivated, not a convenience: a causally bounded
region should carry no net super-horizon power, so `P_B(0)=0` is what the causal picture actually
demands. Then rebuild `ξ_B = (ξ_ΛCDM − c)·W` and recompute.

**Positivity is no longer automatic.** `ξ − c` need not be positive-definite, so `P_B ≥ 0` must be
**checked numerically on the grid and reported**, not assumed. If `P_B` goes negative anywhere, that
is itself a finding — it would mean the no-zero-mode condition is incompatible with a valid power
spectrum under this construction, which is a *stronger* no-go.

## What to compute and report

1. `S₁/₂` for monopole-subtracted Reading B, full-sky unlensed, same pipeline as before
   (CAMB `set_initial_power_table`, `effective_ns_for_nonlinear=ns`, `NonLinear_none`,
   `lens_potential_accuracy=0`, ℓ_max ≥ 100), normalized to unchanged ΛCDM above `k ≈ 0.006 /Mpc`.
2. **The `k_min` sensitivity table again**, same decades as before. This is the decisive output:
   - **If `S₁/₂` now converges** as `k_min → 0`, then Reading B *does* have a prediction, the earlier
     "no number" conclusion is **overturned**, and you must say so plainly.
   - **If it still diverges**, the no-go survives its first serious objection.
3. `min(P_B)` on the grid, i.e. whether positivity survives subtraction.
4. The comparison line: `ΛCDM 34,924 · Reading A 6,897 · Reading B (subtracted) ? · observed ~1,150`.

## Rules

- Cosmology: H0=67.36, ombh2=0.02237, omch2=0.1200, tau=0.0544, As=2.1e-9, ns=0.9649, mnu=0.06.
- Write a runnable script, **run it to completion**, paste its ACTUAL output. No claimed numbers
  without execution.
- Do not fit anything to low-ℓ data; do not tune `χ_§`.
- **Report the result that the computation gives, including one that overturns the previous
  finding.** The previous finding is mine, not yours, and I would rather lose it now than at review.
