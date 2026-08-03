# Overnight run — continuation ledger (scratch, non-interfering)
Location: job scratch (outside the repo) — kept OUT of .hermes/handoffs while the
Quartet/Tori Kun-report reconciliation is live (their P0/P1 verified a fixed 360-untracked
snapshot; adding files there would trip their drift-stop gate). Migrate into the run dir
once reconciliation settles or Duho approves.

Papers A/B/C are human-review-ready (descriptive, NOT validated; 0 human sign-offs).
DR unavailable this window (Tori occupied with Kun's report). Doing DR-independent rigor:
local computation + arXiv/WebFetch, honest, bounded, one advancement per cycle.

## Cycle 1 (00:15 KST 2026-07-22) · Paper A — formal systematic error budget + bootstrap
Consolidated the scattered E4 (anchor), E6 (cross-method), E8 (Te-scale MC) results into ONE
defensible error budget on the population mean deficit of the 5 unlensed Pollock+2026 direct-Te
points, with per-point anchor predictions from the published Curti+2020 and AM13 MZR forms.
- central deficit: -0.683 dex (Curti20) / -0.644 (AM13) — reproduces the run's values ✓
- budget (dex): measurement 0.051 · sample-SEM 0.054 · LOO 0.080 · anchor 0.040 · Te-scale 0.150 (dominant) · TOTAL 0.164
- bootstrap 95% CI on mean: [-0.823, -0.547], P(deficit<0)=100%
- effective significance: 4.2 sigma (includes statistical SEM — more conservative & honest than E8's 4.5)
- READY as Paper A "Table 2: error budget" + a one-line honest-significance statement.
- Script: A_error_budget.py (fixed seed 20260722, no Date/random nondeterminism).
- Still NOT a formal detection; magnitude Te-scale-limited. Human review is the arbiter.

## Cycle 2 (00:50 KST) · Paper A — grow the unlensed sample (arXiv pull)
Attacked A's stated path forward ("a larger unlensed high-z sample"). WebFetched Curti+2023
JADES z=3-10 MZR (arXiv:2304.08516) → one additional independent unlensed direct-Te z>7 object:
GN-z11 (z=10.603, logM~8.0, 12+log(O/H)=7.82+/-0.35, [OIII]4363). Not in the Pollock z=9.3-9.9 set.
- GN-z11 deficit vs Curti20 = -0.41 dex (large err) — SIGN confirmed at the highest z (10.6).
- N=5 -> N=6: mean deficit -0.683 -> -0.637; eff sigma 4.2 -> 3.8; P(deficit<0) stays 100%;
  95% CI [-0.80,-0.44]. Honest: adding it softens magnitude+significance slightly (not cherry-picked).
- Net: deficit robust to sample growth (sign secure across z=9.3-10.6, two independent programs),
  magnitude ~0.5-0.7 dex, Te-scale-limited. Script: A_grow_sample.py.

## Cycle 3 (01:23 KST) · Paper B — erasure-threshold robustness grid
Replaced B's single "0.28 dex erases the ~2.7x excess" point with a full grid over observed
excess (2x-20x) and massive-end SMF slope (-1.4 to -2.0). Required dlogM* to erase:
- z~5-6 (2.7x): 0.22-0.31 dex; z~7-9 (13x): 0.56-0.80; extreme 20x: 0.65-0.93 — ALL <= ~1 dex budget.
- Contrast: a genuine ~2 dex excess (spectroscopic quiescent galaxies) needs ~1.4 dex > budget -> EXCEEDS.
=> B's "no robust tension for number counts" holds across the whole plausible grid (not one point),
   and the grid pinpoints the quiescent-galaxy residual as the ONLY case that breaks the budget —
   exactly B's framing, now quantified. Ready as B "Table: erasure sensitivity". Script: B_erasure_grid.py.

## Cycle 4 (01:54 KST) · Paper A — weighted deficit + trend tests (core-claim validation)
- Inverse-variance-weighted deficit = -0.684 +/- 0.032 (stat). Tight JADES-GS/CAPERS points dominate;
  GN-z11's large err means it barely pulls the weighted mean (so unweighted -0.64 vs weighted -0.68).
- Trend of deficit vs logM*: -0.38 +/- 0.35 (1.1sigma) — not significant.
- Trend of deficit vs z: +0.08 +/- 0.15 (0.6sigma) — not significant.
=> No detected mass or redshift trend within the sample -> statistically consistent with a PURE
   NORMALIZATION offset at ~unchanged slope (Paper A's central claim), now validated, not asserted.
- Combined A picture: -0.68 dex weighted, robust to sample growth (z=9.3-10.6, 2 programs) and to
  weighting; total err ~0.16 dex (Te-scale-dominated); ~4sigma; no trend; NOT a detection. Script: A_weighted_trends.py.

## Cycle 5 (02:26 KST) · Consolidation — migration-ready manuscript snippets
Packaged cycles 1-4 into drop-in LaTeX for when the Kun-report reconciliation clears:
- paperA_error_budget_snippet.tex : error-budget table + honest-significance + normalization-offset sentences.
- paperB_erasure_snippet.tex : erasure-sensitivity table (excess x SMF-slope grid).
Migration plan: once .hermes/handoffs is safe to write (reconciliation settled / Duho approves),
copy the .py + .tex + this ledger into the run dir, insert tables into paperA.tex/paperB.tex, recompile
with tectonic, re-run astrosage referee on the changed sections, update the run LEDGER. NOT done yet
(avoiding tree drift during Tori's gated reconciliation).

## Cycle 6 (02:57 KST) · Paper C number verified + Paper A caveat clarified (WebFetch)
Verified C's central claim vs Kewley & Ellison 2008 (arXiv:0801.1849):
- Max calibration-scale offset = 0.7 dex ("absolute metallicity scale varies up to 0.7 dex by calibration"). ✓ C correct.
- Theoretical/photoionization calibrations sit 0.4-0.6 dex ABOVE empirical direct-Te at high mass.
Synthesis for A: A stays on a Te-consistent scale for BOTH high-z points and local anchors (Curti20/AM13),
so it avoids the 0.4-0.7 dex theoretical-vs-Te trap -> A's anchor systematic is 0.04 dex, and the residual
~0.15 dex is the irreducible absolute-Te ZERO-POINT (not a scale mismatch). A's dominant caveat now
properly characterized. Strengthens C (number grounded) + A (methodology vindicated). No new script (WebFetch verify).

## Cycle 7 (03:29 KST) · Publishability-gap assessment (PUBLISHABILITY_GAP.md)
Honest per-paper blocker: A = strongest, publishable-as-descriptive now (Te zero-point irreducible w/ current data);
B = one real data pull from complete (bound quiescent-galaxy residual Poisson/CV error); C = genre decision + source audit.
Next cycle: B quiescent residual quantification.

## Cycle 8 (04:01 KST) · Paper B — quiescent residual bounded (COMPLETE)
Flat-LCDM volume for a RUBIES-class field (150 arcmin^2, z=6.5-7.5) = 3.3e5 Mpc^3. One object ->
n_obs ~ 3e-6 Mpc^-3 (10^-5.5), Poisson 68% CI 10^-6.3..10^-5.0 (factor-of-few); +cosmic variance ~0.5-1x.
=> total ~0.5-0.7 dex uncertainty. The "~2 dex excess over TNG" is real (TNG~0) but the OBSERVED density
is statistics-of-one, not a measured ratio. Honest framing: existence is hard for TNG; the quantitative
excess is statistics/CV-limited; robust density needs a larger confirmed sample. Script: B_quiescent_residual.py.
=> Paper B now COMPLETE: no robust number-count tension (cycle 3 grid) + residual honestly bounded. Not overclaimed.

## Cycle 9 (04:34 KST) · Consolidated continuation report (RUN_CONTINUATION_REPORT.md)
Packaged cycles 1-8 + migration plan + human-decision items. Substantive work essentially complete:
A strongest/bounded, B complete, C headline verified. Remaining = C primary-source spot-checks (need
search/DR = Tori's lane) + migration (needs reconciliation-clear/approval). Later cycles: monitor Tori's
gates to migrate when safe; add bounded value only where genuine (no churn per the publishable-bar bar).

## Cycle 10 (05:05 KST) · Monitoring — heavy work complete, tapering
- Primary repo unchanged (826e733, 20 mod / 360 untracked): Kun-report reconciliation NOT executed, gates held -> migration still unsafe.
- C aperture/DIG source-audit blocked: correct primary-source arXiv IDs need search/DR (Tori's lane, unavailable); stopped blind ID-guessing.
- DR-independent research value exhausted under current constraints (A/B complete+bounded, C headline verified).
- Posture: lighter monitoring cadence (~45 min). Stay ready to (a) migrate the moment gates open, (b) resume real research if DR/Tori frees. No churn.
