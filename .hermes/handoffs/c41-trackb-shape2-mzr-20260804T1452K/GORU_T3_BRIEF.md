# GORU BRIEF — Shape-2 T3: fetch + compute (the measurement itself)

Lane: `c41-trackb-shape2-mzr-20260804T1452K`. You are Goru. The contract is frozen: your
`T2A_JOIN_PLAN.md` + `T2A_CONVERSION_TABLES.md` + `T2A_FORECAST_FROZEN.json` (sha 61d48d22… —
verify before starting) and Lana's `T2B_CONTRACT_SEMANTICS.md`. If ANY implementation step
conflicts with either half, STOP and report — no silent resolutions.

1. **Fetch** (first science rows of this study): execute the join plan via `nm_external_data`
   (cached, polite, retry) — Te/auroral samples + mass tables per the plan; per-row provenance
   (catalog, join key, conversions applied, channel, lensing fields where applicable) into
   `T3_SAMPLE.jsonl`. Assembly rules are T1's frozen ones — inclusion by measurement class only.
2. **Compute** (deterministic scripts, fixed seeds, lane-local):
   a. Matched-mass deficit re-test (A3): per mass bin, Te-anchored z>3 metallicity vs the z<3
      anchor expectation on the SAME declared scale; deficit + uncertainty per bin; compare
      against the frozen forecast's threshold — state per bin: detection / scale-limited bound,
      per T2b's decision rule.
   b. FMR offset test (A4): the fixed-methodology offset at z>3 vs the z<3 relation, selection/
      tracer/calibration held per contract.
   c. Overlay LAST: ledger'd model predictions (entries cited from C41_LEDGER.jsonl A3/A4/A5
      prediction-class entries) — the comparison metric is the design's frozen offset+dispersion
      vs prediction bands.
3. Outputs: `T3_SAMPLE.jsonl` + `T3_RESULTS.json` (all numbers with uncertainties + per-bin
   verdicts + forecast-vs-actual N table) + `t3_compute.py` + figure(s) (matplotlib, lane-local)
   + `GORU_T3_REPORT.md` (honest anomalies section; runtime; politeness stats) ending with marker
   `GORU_SHAPE2_T3_COMPLETE_20260804`.
Politeness: nm_external_data defaults; hard stop after 3 consecutive fetch failures with the
blocker reported. No git/DB; lane-only writes. Kun reproduces you next — leave him no ambiguity.
