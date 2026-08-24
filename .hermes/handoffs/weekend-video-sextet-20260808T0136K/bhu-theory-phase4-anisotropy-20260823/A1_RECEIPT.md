# A1 receipt — Tori's implementation (2026-08-24, ~09:40 KST)

Script: `a1_shock_trajectory.py`; output `a1_results.csv` (40,001 rows). Written BLIND to
platoon/gpt1_blind_a1/ — that dir was not opened until this receipt was written (the comparison
below is timestamped after it).

## Hand derivations feeding the script (mine, from the pinned equations)

1. **Seed at S→0 (σ=1/3):** substituting u = 1/3 − w into (5.4) and balancing at leading order:
   prefactor → 1/(3S); numerator → −3w² + (8/3)S; denominator → w + (4/3)S. The ansatz
   w = a√S closes with −a/2 = (8/3 − 3a²)/(3a) → a² = 16/9, a = 4/3:
   **u(S) ≈ 1/3 − (4/3)√S**. (Also gives shock-speed approach rate s = 1 − O(√S), used to
   calibrate the Thm3 check tolerance.)
2. **Regular endpoint at S=1:** u(1) = 0 exactly (5.7); (5.4) there gives
   du/dS = −σ/(2(1+σ)) = −1/8. Confirms (4.3) yields v(1) = 0 identically at u=0.
3. **Time mapping (FRW side, σ=1/3):** H = 1/(2t), r̄ = R·r, N = (r̄H)² (§6's "number of
   Hubble lengths √N"), s = Rṙ (4.5) ⇒ dr̄/dt = Hr̄ + s ⇒ **d√N/dt = (s−√N)/(2t)** ⇒
   d ln t/d√N = 2/(s−√N), anchored t = t₀ at √N = 1.

## Integration decisions, including the failure

- **First attempt failed loudly:** forward shooting from S₀ = 1e-10 with the asymptotic seed
  diverged (den → 0, NaNs; 2/12 checks) — the orbit is a saddle connection and the S=0 end is
  a repeller in forward S. Kept on the record: exit-code-1 run, RuntimeWarnings in the log.
- **Fix:** integrate BACKWARD from the regular S=1 endpoint (seed u = δ/8 at S = 1−δ,
  δ = 1e-8), LSODA rtol 1e-11/atol 1e-13. The S→0 limit then lands on 1/3 − (4/3)√S₀ to 8
  digits WITHOUT being told to — the asymptotic seed derivation and the integration confirm
  each other from opposite ends.

## Verification: 12/12 checks

Every theorem in the pinned §5 verified on the solution: Thm 1 limits (both ends), positivity,
both entropy conditions (4.6), physical bound (5.5), admissibility (5.6), Thm 2 subluminality
(max s = 0.999959 < 1), Thm 3 s→1 at the Big Bang at the analytically expected O(√S) rate,
plus an internal consistency check the paper doesn't require: r̄ from ODE (4.2) against the
FRW-side identity r̄ = 2t√N — ratio constant to 6.8e-7 over ten decades of S after grid
densification (4001 → 40001; the 4001-row run showed 6.8e-5, pure trapezoid error, recorded).

## Physical summary of the A1 result (σ = 1/3 branch)

The shock starts at the Big Bang at the speed of light infinitely many Hubble lengths out
(in the N-measure), decelerates monotonically (u: 1/3 → 0, s < 1 throughout), and reaches one
Hubble length (N = 1) — the white-hole crossing — at t = t₀ with the TOV side gone dust-like
(p̄, ρ̄ → 0), matching the paper's OS-limit asymptotics. t(√N) spans t/t₀ = 2.8e-11 at
√N = 1e5 to 1 at √N = 1.

## Addendum (2026-08-24 A2 opening): anchor label corrected

The receipt above says the shock "reaches one Hubble length (N = 1) … at t = t₀". The anchor is
right; the LABEL is wrong against the paper's notation: §6's t₀ is the FIRST-VISIBILITY time
(photon from the Big Bang shock reaching the FRW center), and the N = 1 white-hole crossing is
t_crit, with 1.8 ≤ t_crit/t₀ ≤ 4.5 (6.3). My tabulated t is in units of t_crit (as is gpt1's —
their "N=1 horizon event has t=1"). A2 computes t_vis from the A1 solution and checks it lands
inside (6.3)'s band; results in A2_RECEIPT.md.
