# PAPER_CHANGELOG — ANCHOR_GAP_PAPER.tex source → section map

Lane: `c41-trackb-shape2-mzr-20260804T1452K` · Author: Lana · 2026-08-04 (KST, via `date`)

Rule enforced while drafting: every number in the .tex traces to a receipted lane artifact.
This file is the map. "§" = paper section; artifacts are lane-relative unless noted.

## Number-by-number provenance

| Number / claim in paper | Where in paper | Source artifact (field) |
|---|---|---|
| 5 contract-grade anchors | Abstract, §4.1, §4.3, §7 | `T3_REAL_RESULTS.json` `forecast_vs_actual.actual_usable_anchors_total`; `T3_REAL_SAMPLE.jsonl` rows with `exclusion:null`; `T5_RECEIPTS.md` check 1 |
| Anchor table values (z, S/N, E(B−V), Te, O/H, logM per object) | Table 1 | `T3_REAL_SAMPLE.jsonl` (verbatim per-row fields); reproduced-to-digit table in `KUN_T4_REAL_FORENSICS.md` §1 |
| z range 4.015–8.496; O/H 7.109–8.032; Te 14,307–24,847 K | Abstract, §4.1, §7 | min/max over the 5 `T3_REAL_SAMPLE.jsonl` anchor rows |
| E(B−V) list incl. flagged zero-reddening GLASS_150029 (obs Hγ/Hβ 0.471 ≥ 0.468) | §4.1, Table 1 note a, §6.7 | `T3_REAL_SAMPLE.jsonl` row GLASS_150029 `flag_dustcorr_skipped`; `KUN_T4_REAL_FORENSICS.md` §1 + Uncertainties |
| 79 tables with 4363-class column; 23 candidates; 12 unreachable / 11 tables (8 catalogs) fetched | Abstract, §3.2, §5.1(4), §6.1 | `T3_REAL_LOG.txt` run-7 block (S1 lines; 12 `S2 SKIP … HTTPError` lines; fetch lines); catalog count per `KUN_T4_REAL_FORENSICS.md` §2 |
| 95 z>3 rows; per-table split 10/9/32/6/38 | Abstract, §3.2, Table 2 | `T3_REAL_SAMPLE.jsonl` (recounted this session: totals close 5+64+12+6+8=95); `T3_REAL_LOG.txt` "S2 done: 95" |
| Exclusion taxonomy: 64 S/N-floor (14 zero-flux; 5 near-miss 4.76–4.84), 12 no-Hβ, 6 missing-flux, 8 Te-failure | Table 2, §4.2 | `T3_REAL_SAMPLE.jsonl` `exclusion` strings, recounted this session (see note below); audit basis `KUN_T4_REAL_FORENSICS.md` §2 |
| Near-miss identities ERO_06355 (8.7/1.8=4.83), GLASS_10021 (19.8/4.1=4.83) with masses 8.77/8.51 | §4.2, §5.1(2) | `T3_REAL_SAMPLE.jsonl` rows; arithmetic confirmed in `KUN_T4_REAL_FORENSICS.md` §2 |
| JADES 85/95 rows; auroral S/N up to 8.5 at z=9.43; all z>9 survivors die at no-Hβ/missing flux | §4.2, §5.1(1), §5.3 | `T3_REAL_SAMPLE.jsonl` (gsprism id 2115 z=9.432791 sn 8.5 no-Hβ; 2427 z=9.4327 sn 7.12 no-Hβ; 1207/230/272 z=9.69–10.61 missing flux); split per `KUN_T4_REAL_FORENSICS.md` §2 |
| Te-failure physicality example f4363 > f5007 | Table 2 comment | `T3_REAL_SAMPLE.jsonl` id 949 (4.373 > 3.214); `KUN_T4_REAL_FORENSICS.md` §2 |
| Flags: 20 no-dustcorr, 1 dustcorr-skipped, 0 Class-X-no-SNR, 0 ICF-fallback, 0 no-mass | Table 2 comment | `T3_REAL_RESULTS.json` `per_class_counts` (flag counts recounted from sample file, match) |
| Bins 2/1/0; below_bin_floor 2 (ERO_04590 @7.60, ERO_10612 @7.78); 3+2=5 closure | §4.3, Fig. 1 | `T3_REAL_RESULTS.json` `bins`, `per_class_counts.below_bin_floor`, `below_bin_floor_note`; closure check `T5_RECEIPTS.md` check 1 |
| Forecast v1 10/12/3 = 25, 0.25 dex precision, 0.30 dex threshold, sha 61d48d22… | §2.3, §4.3, Fig. 1b | `T2A_FORECAST_FROZEN.json`; sha in `T2A_FORECAST_FROZEN_V2.json.v1_sha256` + `T5_RECEIPTS.md` |
| Forecast v2 35/42/10 = 87, 0.12/0.15 dex, revision cause | §2.3, Fig. 1b | `T2A_FORECAST_FROZEN_V2.json` |
| v2 precision flagged unachievable (F-T4-1); null stated against v1 as more conservative | §2.3 | `T3_REAL_RESULTS.json` `supersession_disclosure`; `KUN_T4_REAL_FORENSICS.md` Correction 2 |
| Null statement (verbatim quotation) | §4.3 | `T3_REAL_RESULTS.json` `forecast_vs_actual.null_statement_T2b_s6` (verbatim; template authority `T2B_CONTRACT_SEMANTICS.md` §6) |
| 3-anchor per-bin minimum; Rule S; 0.15 dex Te-anchor class floor; 0.24 dex class; no-retro-shrinking | §2.1, §4.3, Fig. 1 caption | `T2B_CONTRACT_SEMANTICS.md` §2/§3/§6; `T2A_CONVERSION_TABLES.md` §2; `t3_real.py` `TE_CLASS_FLOOR` |
| Class A′ definition, S/N≥5 floor rationale ([Fe II] λ4360), lensing ruling, one licensed re-freeze | §2.2, §2.3 | `T2B_AMENDMENT_RULING.md` Rulings 1–3 |
| A′ pipeline components (Izotov 2006, PyNeb, ICF(O)=1, CCM89 R_V=3.1, Case B 0.468, ne=100, T(OII)=0.7Te+3000, MC seed/draws) | §3.3 | `APRIME_PIPELINE_FROZEN.md`; implemented form in reviewed `t3_real.py` (S3) |
| Review chain: APPROVED_WITH_EDITS, B1–B3 / R1–R4 / A1–A3 substance; 6 micro-deltas; 7 runs (3 honest failures, 1 incomplete, 748→0 run, 2 completions) | §3.1 | `KUN_SCRIPT_REVIEW.md` (initial + deltas); `T3_REAL_LOG.txt` (7 START blocks; run-5 "748 z>3 rows" + "S3 done: 0"); run disposition `T5_RECEIPTS.md` check 4 |
| Forensics: SOUND_WITH_CORRECTIONS; all 5 reproduced to the digit; flux rows char-matched; masses/z spot-verified live; C1/C2 change no numbers | §3.1, §4.1, Table 1 comment | `KUN_T4_REAL_FORENSICS.md` (verdict, §1, §3–4); `T5_RECEIPTS.md` check 3 |
| Mass sibling table tabled1: 182 rows / 180 joined | §3.2, Table 1 comment | `KUN_T4_REAL_FORENSICS.md` §1 (182 rows); `T3_REAL_LOG.txt` run-7 "180 masses" |
| AM13 eq.5 form + anchor-frame discrepancy note (quoted verbatim) | §3.3, §5.2, Fig. 1 | `T3_REAL_RESULTS.json` `anchor_frame` (form, table, `anchor_frame_discrepancy_note`) |
| A4 FMR not-computable-v1 + reason | §4.4, §5.3 | `T3_REAL_RESULTS.json` `A4_FMR` |
| Predictions: 11 entries → 7 not-numeric-in-span, 4 no-measured-bins | §4.4 | `T3_REAL_RESULTS.json` `predictions_confrontation` (counted) |
| z9–10 differentiation: sign established, −0.69±0.03 stat, ±0.16 dex total (Te-scale 0.15 dominant), 95% CI [−0.82,−0.55], z≈9.3–10.6 incl. GN-z11, "systematic-limited, NOT a detection"; FMR untouched there | §5.3 | `KUN_DESIGN_REFUTATION.md` F2 (+F1 lens-contamination precedent); design F2 block in `MEASUREMENT_DESIGN_V1.md` |
| A3 motivation: 22 entries, c41_037 holder, c41_043 vs c41_033/035/044/045, c41_012 ~25 galaxies, dispersion figures (0.05–0.1 dex; 0.35±0.28 dex), settle-line wording | §1, §5.4 | `../c41-baseline-restart-20260803T1253Z/C41_STATUS_DEBATE_MAP_V1.md` axis A3 |
| Mock retired / no agent-typed numbers protocol | §3.1 | `KUN_T4_FORENSICS.md` (mock rejection), `t3_real.py` docstring, `T3_REAL_RESULTS.json` `protocol` |
| PyNeb version seam 1.1.18 (freeze doc) vs 1.1.32 (runtime/forensics) | §6.5 | `APRIME_PIPELINE_FROZEN.md` vs `KUN_SCRIPT_REVIEW.md`/`KUN_T4_REAL_FORENSICS.md` headers |
| Per-object MC uncertainties not tabulated in v1 outputs | §6.4 | `T3_REAL_SAMPLE.jsonl` (no per-row O/H error fields) vs `APRIME_PIPELINE_FROZEN.md` MC spec |
| Anchors toward SMACS J0723 / Abell 2744 sightlines; no μ column in archived table | §6.6 | Anchor IDs (ERO_*, GLASS_*) in `T3_REAL_SAMPLE.jsonl`; program identities + lens precedent per `KUN_DESIGN_REFUTATION.md` F1; §5 semantics `T2B_CONTRACT_SEMANTICS.md` |

## Figure

`ANCHOR_GAP_FIGURE.png/.pdf` generated by `make_paper_figure.py` from
`T3_REAL_SAMPLE.jsonl` + `T3_REAL_RESULTS.json` only (asserts the 5-anchor count and the
frozen AM13 form string before drawing). Palette = reference categorical slots 1–3,
validated colorblind-safe (all-pairs) with the dataviz validator; forecasts hatched +
all bars direct-labeled (contrast relief). Rendered and visually checked for collisions.

## Recount note (disclosed, not hidden)

`KUN_T4_REAL_FORENSICS.md` §2 prose says "S/N-floor exclusions (58 rows)"; a direct recount
of `T3_REAL_SAMPLE.jsonl` this session gives **64** S/N-floor exclusion rows (and the totals
only close at 64: 5+64+12+6+8=95). The paper's Table 2 uses the archived per-row file as
authoritative (the same file Kun's audit sampled; his other counts — 14 zero-flux, 12 no-Hβ,
6 missing-flux, 8 Te-fail, 5 near-misses — all reproduce exactly). Flagged for Kun/T4 as a
prose-count nit in his report, not a data defect.

## Style/modality decisions

- Title per brief: "The Public-Archive Direct-Te Anchor Gap at z>3: A Contract-Grade Census".
- Census + null modality enforced: no sentence claims a deficit, an evolution, or their
  absence; Fig. 1a caption explicitly de-licenses the visual offset; per-object offsets from
  Kun's evidence ledger are referenced as provenance-only and not printed as results.
- Null quoted verbatim from the receipted result file (§6-template instantiation with v1/v2
  supersession disclosure), per Kun Correction 2.
- External bibliography kept to the four safe method citations (AM13, CCM89, Izotov+2006,
  PyNeb); source catalogs cited by VizieR identifier with a comment that bib entries are
  completed at submission prep (no network in-lane to verify bibcodes).

LANA_PAPER_CHANGELOG_COMPLETE_20260804

## Referee fixes (Kun MINOR verdict, F-R1…F-R4) — applied 2026-08-04 21:32 KST

Source: `KUN_ANCHORGAP_REFEREE.md` (verdict MINOR — accept after edits). Exactly the four
listed fixes applied by Lana; no numbers changed. Kun's "no fix required" observations
(the "two objects, three rows" parenthetical and all §3 items) deliberately not applied —
nothing beyond his list.

- **F-R1 (Table 2)**: S/N-floor row "Dominant source" corrected "JADES prism/grating" →
  "JADES prism + compilation" (Kun's recount: 28 gnprism + 31 gsprism + 5 compilation;
  zero grating rows in the class).
- **F-R2 (§5.3)**: "the $z\geq9.7$ candidates lack the nebular flux" → "$z>9.6$"
  (gsprism id 230 sits at z = 9.686 < 9.7; substance unchanged).
- **F-R3 (§4.2)**: attribution clause reworded to credit the direct recount of the
  archived per-row file ("all 64 exclusions were recomputed directly from the archived
  per-row fluxes, confirming every stated reason") instead of ascribing "all 64" to the
  audit document whose own prose says 58 (the slip already disclosed in the Recount note
  above). Number unchanged.
- **F-R4 (§6.5)**: one added disclosure — the freeze doc's dust input (Hα/Hβ primary,
  source $A_V$ fallback) vs the executed pipeline's exclusive Hγ/Hβ decrement (B2's
  approved fix; only physically available Balmer pair at z>4; primary branch vacuous,
  fallback never fired). Documentation seam, same class as the PyNeb version seam;
  not a numeric defect.

LANA_ANCHORGAP_FIXES_LOGGED_20260804
