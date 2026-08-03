# Verdict memo — z>7 mass–metallicity run (updated 2026-07-20 10:00 KST, P7)

## Status: DESCRIPTIVE — a BOUNDED, SELECTION-ROBUST deficit (upgraded from unbounded upper bound)
Upgrade over P5: the JWST emission-line selection function is now **forward-modelled and bounded**
(two independent methods), and the deficit **survives** the correction — selection cannot explain it away.
- Automated referee (qwen3.6:27b-nvfp4, 126 s): **REJECT** — but every objection (calibration transfer,
  Te-vs-strong-line tension, small-N, 2× method spread) is one the paper **already concedes** as a caveat;
  it judges against a "detection" bar the paper explicitly does not claim.
- Honesty gate (P7 audit + pre-registration): **MINOR** — holds as an honest, selection-bounded descriptive
  paper. Title/abstract/conclusion claim only a bounded, selection-corrected deficit, not a detection.
**Still NOT to be presented as a validated measurement of z>7 MZR evolution.**

## The result (all trace to results.json / selection_results.json / RECONCILIATION.md)
- Matched deficit **Δ = 0.45 dex**, bootstrap 95% CI **[0.28, 0.62]** (excludes 0).
- Selection forward-model (Test 4): strong-line **Δ_sel ≈ 0.10 dex (range 0.04–0.20)**; Te/auroral is the
  **more** selection-biased channel (0.04–0.35) → Te quoted as corroboration only, not the safe anchor.
- **Selection-corrected deficit = 0.25–0.41 dex (central ~0.35)**, CI excludes 0; selection ≈ 10–45%, ≥55% residual.
- Two independent estimates (Tori MC + Goru first-principles/empirical), cross-checked, differ ~2×.
- Mechanism: **truncation bias** — median EW(Hβ)=124 Å, within-sample flat (Δ-vs-EW r=+0.09) → must be forward-modelled.
- Sample: SDSS N=203,599; JWST z>7 **N=16** overlap (4 Te + 12 strong-line), Nakajima+23 via VizieR TAP.
- Pre-registered systematics: **7/7 PASS in the bounded sense** (Test 4 upgraded FAIL-unbounded → PASS-bounded).

## What is now defensible (upgraded)
1. The calibration-controlled framework + SDSS anchor (reproduces prior fit).
2. The matched-scale offset exceeds the calibration floor and survives 7 systematics + LOO.
3. **NEW: the selection bias is bounded (Δ_sel ≈ 0.04–0.20 dex strong-line) and the deficit survives it** —
   emission-line selection cannot account for the deficit (≈10–45% only).

## What still needs human sign-off / to become a validated detection
1. ~~Selection function~~ **DONE (bounded).** Forward-modelled two independent ways; Test 4 now PASS-bounded.
2. **Independent multi-survey z>7 sample** — add Curti+24 (not in VizieR TAP) & Heintz+23; N=16 single-survey is thin.
3. **z>7 simulation comparator** — TNG on disk stops at z=6 (~0.13 dex); need a z>7 sim.
4. **Tighter / Te-independent calibration transfer** — with selection bounded, the residual leans on the
   strong-line KE08 transfer; the Te channel is itself more selection-biased and does not independently confirm.

## One-line honest status
A bounded, selection-robust z>7 gas-phase O/H deficit of ~0.25–0.41 dex (central ~0.35, CI excludes 0)
that emission-line selection **cannot explain away** — still descriptive, awaiting an independent multi-survey
sample, a z>7 simulation, and a tighter Te-independent calibration before it is a validated detection.
