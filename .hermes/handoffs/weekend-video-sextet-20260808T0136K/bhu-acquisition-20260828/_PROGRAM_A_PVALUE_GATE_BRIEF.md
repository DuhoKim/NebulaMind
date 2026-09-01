# GATE — attack the re-aimed Program (A) result

Everything needed is inline. Do not open large files. Your job is to REFUTE. Default to refuted if
uncertain. This result has never been gated and will be shown to the principal at 07:00.

## What was computed

Question: does the Gaztañaga causal-horizon cutoff explain the CMB large-angle correlation deficit?

Statistic: `S₁/₂ = ∫_{-1}^{1/2} [C(θ)]² d(cos θ)` — integrates over exactly θ ∈ (60°,180°).
Observed ≈ 1150 μK⁴. Operator validated: reproduces ΛCDM `S₁/₂` = 34,924 μK⁴ against an independent
reference of ~34,900 (0.1%), and is exact to 1e-14 against independent quadrature.

Model: hard IR cut on the primordial spectrum, `P(k)=0` for `k < k_§`, `P = P_ΛCDM` above. `k_§`
comes from the paper's own Eq. 23, `χ_§ = (3.149 ± 0.006) c/H₀` = 14,015 Mpc; `k_§ = 2π/χ_§` =
4.483e-4 /Mpc. Unlensed, nonlinear off, full sky. CAMB 1.6.0.

Reported (Monte Carlo, 100k–200k skies, `Ĉ_ℓ = C_ℓ·χ²_(2ℓ+1)/(2ℓ+1)`):

| spectrum | S₁/₂ (mean spectrum) | P(Ŝ ≤ 1150) |
|---|---|---|
| ΛCDM | 34,924 | ~0.1% |
| hard cut, `k_§=2π/χ_§` | 6,897 | ~3.3% |
| hard cut, `k_§=π/χ_§` | 14,000 | ~0.35% |
| smoothed cut, 0.3 k_§ | 6,113 | ~3.1% |
| smoothed cut, 1.0 k_§ | 8,713 | ~1.9% |
| excess power below k_§ | 157,151 | ~0.001% |

Two claims drawn:
- **C1.** The cutoff moves the anomaly from p ≈ 0.1% to **at most ~3%** — a real improvement that
  does not make the observation typical. Claimed as an upper bound because no tested alternative
  suppresses more than the hard cut.
- **C2.** The paper asserts (its L457) "CMB temperature should not be correlated above θ > 60 deg",
  i.e. `S₁/₂ = 0`. The hard cut leaves `S₁/₂ = 6,897` — **6× the observed 1150**, only 5.1× below
  ΛCDM. So the causal cut gives a partial suppression, not the vanishing correlation asserted.

## Attack these

1. **Is C2 a fair reading of the paper?** The paper says elsewhere that its estimate "does not take
   into account the foreground (late) ISW and lensing effects … which add non primordial
   correlations to the largest scales." Does that caveat rescue the 6× overshoot — i.e. could
   ISW+lensing account for the gap between 6,897 and 1150? Note 6,897 is ABOVE 1150, so the model
   OVERSHOOTS; would including ISW push it further up (making C2 stronger) or is there a mechanism
   that reduces it? Get the SIGN right and say so explicitly.
2. **Is the cut placement right?** `k_§ = 2π/χ_§` vs `π/χ_§` swings the p-value ~9×. Is either
   defensible? Should the cut instead be applied to the projected scale, or to modes with
   wavelength ≥ χ_§ in a different convention? Is a sharp cut in `k` even the right object given
   that the causal statement is about a finite region in real space?
3. **Is the MC right?** `Ĉ_ℓ = C_ℓ χ²_(2ℓ+1)/(2ℓ+1)` assumes full sky, Gaussianity, no noise, no
   mask. The observed 1150 is a CUT-SKY value. Does the cut sky change the comparison enough to
   overturn C1 — in which direction, and by roughly how much?
4. **Is C1's upper-bound status justified?** It rests on: Paley–Wiener forces a compact-correlation
   spectrum to be entire, hence smooth at the cut, so smoothed cuts are the relevant family, and
   none beat the hard cut. Is there an admissible spectrum that suppresses `S₁/₂` MORE than the hard
   cut while remaining a valid (non-negative) power spectrum? If you can construct one, C1 falls.
5. **Is any of this circular?** The spectrum above the cut is ΛCDM's, fixed by high-ℓ data; the
   low-ℓ data sets nothing. Is that actually non-circular, or does using ΛCDM's transfer functions
   and parameters smuggle in the answer?
6. **Anything else that kills it.**

## Output

First line: one token — `PVALUE_RESULT_SOUND`, `PVALUE_RESULT_SOUND_WITH_REPAIRS`, or
`PVALUE_RESULT_REFUTED`. Then C1 and C2 each HOLDS or FAILS with reasons, then points 1–6, then the
minimum repairs. Be specific and quantitative where you can. Do not be agreeable.
