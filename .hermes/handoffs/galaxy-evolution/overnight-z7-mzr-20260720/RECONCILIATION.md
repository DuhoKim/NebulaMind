# Selection forward-model — reconciliation (captain, 2026-07-20 08:55 KST)

Two independent P6 estimates of the JWST z>7 emission-line selection bias Δ_sel.

## The two estimates
| | strong-line Δ_sel | Te/auroral Δ_sel | method |
|---|---|---|---|
| Tori (MC forward model) | 0.01–0.11 (fid 0.04) | 0.04–0.35 (fid 0.22) | mock parent → line lums → NIRSpec detection → recover MZR; 48-run grid |
| Goru (independent) | 0.05–0.20 (central 0.10–0.15) | 0.05–0.15 (central 0.10) | FMR-route + measured Te-vs-strong-line gap in the real sample (0.17–0.19 dex) |

## Reconciled position (adopt the conservative synthesis)
- **Δ_sel is now BOUNDED** — both methods agree. The original Test-4 failure (unbounded selection) is **resolved**.
- **Strong-line Δ_sel ≈ 0.10 dex, range 0.04–0.20** (adopt Goru's central; Tori's 0.04 fiducial is below Goru's floor, flagged).
- **Te/auroral is the MORE selection-biased channel** (auroral [OIII]4363 detectability itself selects low-Z/high-Te) — both now agree. The Te-only "calibration-free" 0.33 dex does **not** survive on its own (corrected → ~0.09–0.23, CI can include 0). Quote Te as corroboration only, NOT the conservative anchor.
- **Selection-corrected matched offset = 0.45 − (0.04–0.20) = 0.25–0.41 dex** (central ~0.35), CI excludes 0 across both methods → **selection cannot explain the deficit away** (selection ≈ 10–45%; ≥55% residual).

## Test 4
FAIL (unbounded) → **PASS as a bounded systematic.** Scorecard is now 7/7 in the bounded sense.

## Honest verdict for the paper (the upgrade, stated honestly)
Upgrade from *"unbounded upper limit"* to **"a bounded, selection-robust ~0.25–0.41 dex z>7 mass–metallicity deficit that emission-line selection cannot account for."** This is materially stronger than P5.
It is **NOT yet a clean/validated detection**, because:
1. the two independent selection estimates differ by ~2× (correction itself uncertain);
2. the residual signal now leans on the strong-line **calibration transfer** (KE08) — the Te channel that was meant to bypass calibration does not independently confirm (small N=4, its own selection);
3. single-survey (Nakajima+23 only), N=16 in overlap;
4. no z>7 simulation comparator.

**Label: DESCRIPTIVE — bounded / selection-robust** (upgraded from unbounded upper limit). Title drops "upper bound" for "selection-bounded"; abstract states selection accounts for ~10–45% and the deficit survives; conclusion keeps the 4 caveats.
