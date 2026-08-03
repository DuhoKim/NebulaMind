# REFEREE_REPORT — z>7 MZR upper-bound paper

**Run:** overnight-z7-mzr-20260720 (Trikitear) · **Phase 4 (referee -> revise)** · Goru · 2026-07-20 01:53 KST

## Step 1 — Automated referee (local model)
- Model: `qwen3.6:27b-nvfp4` via ollama. Ran to completion (~a few min; `timeout` unavailable on macOS so run was monitored, not hard-capped). Prompt: abstract + key numbers. Raw output in `_referee_out.txt`.
- **Model VERDICT: REJECT.** Top risks it raised:
  1. Selection failure invalidates the "upper bound": the unbounded ~0.1–0.2 dex same-sign bias overlaps the lower CI edge (0.283), so the offset could be entirely selection — calling it a "strong upper bound" is a semantic overclaim masking a non-detection.
  2. Significance rests on unvalidated KE08 calibration transfer to z>7; the calibration-free Te-direct subset (N=4) is "close to zero."
  3. Small-N (N=16) single-survey bootstrap may understate uncertainty; no independent JWST comparator.
- Its "most important next step": confirm the offset in an independent z>7 sample selected orthogonally to emission-line/UV (lensed / deep-continuum) to break the selection–evolution degeneracy.

### My assessment of the model verdict
- **Risk 1 is a semantic disagreement, not a caught overclaim.** The paper never claims a detection; it explicitly labels the deficit a *ceiling on evolution*. When a same-sign bias is unbounded, the measured deficit IS the correct upper bound (a ceiling, not a floor) — that is the honest label the pre-registration demands, not an overclaim. The model's own reasoning ("consistent with no evolution... not a detection") agrees with the paper's conclusion.
- **Risk 2 contains a factual error:** the model states the Te-direct CI [0.075, 0.535] is "fully consistent with zero." It is **not** — the lower bound 0.075 > 0, so it excludes zero (marginally). However, the *adjacent* valid point — that the plausible selection bias (0.1–0.2 dex) exceeds the Te-only lower CI edge (0.08) — is a real honesty improvement and I acted on it.
- **Risk 3** is already caveated in the draft (single-survey, N=16, no z>7 sim), but I confirmed the framing is honest.

## Step 2 — Non-circularity & honesty audit (against PREREGISTRATION.md + results.json)
1. **Only an upper bound, never "detection"/"measurement of evolution"?** PASS. Title = "Upper Bound"; abstract = "descriptive result --- not a validated measurement", "strong upper bound... not a detection"; conclusion = "not a validated detection"; caveats = "descriptive, automated result, not a validated measurement". No word implies validated evolution. (Intro's "normalization is observed to fall with redshift" is correctly attributed to established low-z literature, Sanders+21.)
2. **Failed selection test honest & prominent?** PASS. Bold **FAIL** in the scorecard, a dedicated paragraph in Systematics, and repeated in abstract, conclusion, and caveats. Not buried.
3. **Every number matches results.json?** One genuine mismatch found and FIXED (see Step 3). All headline numbers verified exact: Δ=0.449→0.45; Te-only 0.332→0.33 (CI [0.075,0.535]→[0.08,0.54]); bootstrap CI [0.283,0.622]→[0.28,0.62]; N=16; 6/7; naive T04 0.565→0.57; per-grid 0.545/0.396/0.439/0.427 (N=4/10/7/2); strong-line 0.488 CI[0.351,0.615]; z7 fit 5.539+0.268; test-5 CI [0.328,0.560], LOO [0.428,0.481], excl-extreme [0.372,0.586]; TNG z=6 ~0.13.
4. **KE08 + "~0.12 dex" claim correct?** PASS. 0.565 − 0.449 = 0.116 ≈ 0.12 dex; cubic coefficients (a=230.782, b=−75.79752, c=8.526986, d=−0.3162894, valid 8.05–9.2) match results.json exactly.
5. **Circular reasoning?** NONE. Calibration is reconciled first, thresholds are pre-registered, and the offset is not assumed anywhere it is later "found." Both a surviving offset and a vanishing null were admissible.
6. **Self-label in abstract AND caveats section?** PASS. Present in both (plus conclusion).

## Step 3 — Revisions I made (via python, numbers never invented)
1. **Fixed number mismatch:** Data section said "6 direct-Te" for the N=16 overlap. Per `_p2_intermediate.json` `calib_breakdown` (direct=4, R23=7, R3=5) and `_p2_tests.json` (Te-direct N=4, strong-line N=12), the overlap has **4 direct-Te + 12 strong-line**; the "6" is the count in the broader 26-galaxy z>7 census. Corrected to "4 direct-Te and 12 R23/R3 strong-line," with the census figure noted parenthetically. Confirmed by direct count of `z7_metallicity.csv` (only 4 `direct` rows fall in [8.0,9.5] and are non-limits).
2. **Hardened the selection caveat** (addressing the referee's one valid quantitative point): added that the plausible selection amplitude (~0.1–0.2 dex) is comparable to the lower CI edge, and that on the calibration-free Te-direct subset (lower bound 0.08 dex) the selection bias lies *within* the interval, so on the most conservative reading selection could account for much or all of the Te-only signal — only the strong-line-inclusive offset sits clearly above the selection band. Reinforces "ceiling, not measurement."
- Recompiled `draft.pdf` with tectonic after each edit (clean; only benign underfull-hbox warnings).

## VERDICTS
- **Automated model:** REJECT (partly on a semantic objection that agrees with the paper's own non-detection stance, and one factual error about the Te CI).
- **My initial audit:** MINOR (honest, well-caveated upper-bound paper; one number mismatch).
- **FINAL after revision: MINOR.** The paper is an honest upper-bound result: it never claims detection, presents the failed selection test prominently, all numbers now match results.json, and the selection ceiling is now quantitatively tied to the CI. The residual limitations (single-survey, N=16, no z>7 sim, uncorrected selection) are inherent to the data on disk and are fully disclosed — they cap what can be claimed but do not constitute overclaiming. Forcing this to ACCEPT would require independent-sample confirmation the data cannot provide; hiding the selection caveat to do so would be the real failure.
