# Shared parent-sample and selection-function module — 20260708T204717Z

Marker: `SHARED_SELECTION_MODULE_20260708T204717Z`

## What changed

Built a reusable local module for all nine active AAS-style pilot papers: a data dictionary, selection-function counts, sSFR-retention table, paper-use contract, and an AASTeX fragment smoke-tested with Tectonic. This is a paper-quality improvement because it gives every draft the same front-loaded denominator disclosure instead of letting each paper restate the SDSS sample differently.

## Grounding from actual artifacts

- Cached row-level SDSS CSV read: `runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv`.
- Selection-function packet read: `overnight-9-papers-20260708/lanes/tori/selection-function-attrition/20260708T155514Z/selection_function_attrition_summary_20260708T155514Z.json` plus stage and sSFR CSV tables.
- Goru regression/bin-sensitivity summary read for cross-checks: `overnight-9-papers-20260708/lanes/goru/artifacts/goru_regression_bin_sensitivity_20260708T183643Z.json`.
- Cached rows: 60,000; duplicate `specObjID`: 0; `specObjID` nondecreasing: True.
- Public strict four-line S/N>=3 eligible rows: 249,917; cached coverage: 24.0%.
- BPT counts from the cached CSV: star-forming 39,553, intermediate 12,234, optical AGN 8,146, unclassified 67.
- S/N-threshold counts recomputed from the cached CSV: >=3 60,000, >=5 42,446, >=10 22,311.
- High-excitation optical AGN proxy (`bpt_label == agn` and `log_oiii_hb > 0.25`): 4,440 rows.
- sSFR-dependent line-selection warning preserved: 33.6% S/N>=3 retention for -12<log sSFR<-11 versus 94.9% for -10<log sSFR<-9.5.

## Files changed / written

- `overnight-9-papers-20260708/lanes/tori/shared-selection-module/20260708T204717Z/shared_selection_data_dictionary_20260708T204717Z.json`
- `overnight-9-papers-20260708/lanes/tori/shared-selection-module/20260708T204717Z/tables/column_dictionary_20260708T204717Z.csv`
- `overnight-9-papers-20260708/lanes/tori/shared-selection-module/20260708T204717Z/tables/paper_use_contracts_20260708T204717Z.csv`
- `overnight-9-papers-20260708/lanes/tori/shared-selection-module/20260708T204717Z/tables/selection_stage_counts_verified_20260708T204717Z.csv`
- `overnight-9-papers-20260708/lanes/tori/shared-selection-module/20260708T204717Z/tables/ssfr_retention_verified_20260708T204717Z.csv`
- `overnight-9-papers-20260708/lanes/tori/shared-selection-module/20260708T204717Z/aastex/shared_parent_sample_selection_fragment_20260708T204717Z.tex`
- `overnight-9-papers-20260708/lanes/tori/shared-selection-module/20260708T204717Z/aastex/selection_module_smoke_test_20260708T204717Z.tex`
- `overnight-9-papers-20260708/lanes/tori/shared-selection-module/20260708T204717Z/SHARED_SELECTION_MODULE_20260708T204717Z.md`
- `overnight-9-papers-20260708/lanes/tori/shared-selection-module/20260708T204717Z/shared_selection_module_manifest_20260708T204717Z.json`
- `overnight-9-papers-20260708/ticks/TICK_20260708T204717Z.md`
- `overnight-9-papers-20260708/scripts/shared_selection_module_tick.py`
- `overnight-9-papers-20260708/lanes/tori/shared-selection-module/20260708T204717Z/aastex/compile.log`
- `overnight-9-papers-20260708/lanes/tori/shared-selection-module/20260708T204717Z/aastex/selection_module_smoke_test_20260708T204717Z.pdf`

## Verification

- JSON/CSV/TEX artifacts written: 13.
- Tectonic smoke-test exit code: 0.
- Smoke-test PDF starts with `%PDF`: True.
- Smoke-test PDF SHA256: `b70c811a8b9652890b6458cbe4ad805a1644c603485d9eef7d53b5b08fd1bbbd`.
- Fatal LaTeX markers found in compile log: [].
- Count checks passed: {'rows_eq_60000': True, 'bpt_counts_match_goru': True, 'sn_ge_3_eq_60000': True, 'sn_ge_5_matches_goru': True, 'sn_ge_10_matches_goru': True, 'strict_public_count_eq_249917': True, 'duplicate_specobjid_zero': True, 'specobjid_nondecreasing': True}.

## Blockers / cautions

- This module is not a public-linked manuscript replacement. It is a local integration primitive that should be included before any future local merge of the nine drafts.
- It does not authorize prose publication, public mirroring, DB/API writes, deploy/restart, git actions, or external submission.
- The central scientific caution is unchanged: the cached sample is a capped optical emission-line denominator, not a complete/random SDSS parent and not a causal feedback/gas/simulation measurement.

## Next recommended tick

Use this shared module to assemble a local integration draft for either RP-1 flagship or the eight-paper denominator suite, then recompile/hash locally and run Kun-style reproducibility checks. Do not overwrite public-linked PDFs without a separate approval gate.

## Safety

Read cached SDSS/local overnight artifacts only; wrote local artifacts under overnight-9-papers-20260708/lanes/tori/shared-selection-module plus the required tick report and ledger append. No product DB/API/page_versions/wiki publish/live mirror/deploy/restart/git/extra-cron/billing/OAuth/external submission changes.
