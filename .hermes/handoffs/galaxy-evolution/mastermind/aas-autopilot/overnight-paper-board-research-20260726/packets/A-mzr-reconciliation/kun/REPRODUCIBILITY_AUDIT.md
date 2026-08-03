# Reproducibility Audit

AI_DRAFT_NOT_HUMAN_GOLD

Marker: OVERNIGHT_PAPER_BOARD_PACKET_A_KUN_REPRODUCIBILITY_AUDIT_V1

This audit is documentary traceability only. I did not run the live runner, re-pull SDSS/TNG catalogs, recompute values, or edit source runs.

Source hash check: PASS. `shasum -a 256 -c baseline/INPUT_SHA256.txt` returned OK for all 38 captured files. No scoped `expected_value` verdict is `CONTRADICTS`; only `gated-e2e-demo` has an `expected_value` gate among the four runs, with verdict `TENSION`.

## Run-Level Findings

| run_id | traceability status | stated numeric results / N-counts | own-run trace | contradictions | O/H calibration or scale |
|---|---|---|---|---|---|
| `2958462772b2` | traceable-with-gap | SDSS `120,000` galaxies; review cycle `1`; review verdict `MINOR` | `result.summary` states SDSS `(120,000 gals)`; `draft.tex` abstract/data/result repeat approximately `120,000`; `result.review_cycles=1`; `history.json` and `result.review_verdict` record `MINOR`; log records SDSS pull, draft, review, PDF compile | none found inside own fields | SDSS O/H calibration/scale: `ABSENT`. Draft explicitly says measurements were uncalibrated, but no named SDSS metallicity calibration or common O/H scale is provided. |
| `d8de519cb9c9` | traceable-with-gap | TNG100 `23,722` galaxies; SDSS `120,000` galaxies | `result.summary` states both counts; `spec.data_sources` and `result.data_sources` are `tng, sdss`; `result.method=mass-metallicity`; log records loading TNG `gasZ` and pulling SDSS; artifacts are only `result.png` and `history.json`; no draft/PDF exists | none found inside own fields; however `spec.outputs` asks for `aastex-draft` while `result.note` says full draft is queued, so the run is not a completed draft build | TNG scale stated: `SF-weighted gas metallicity -> O/H (solar-scaled)`. SDSS O/H calibration/scale: `ABSENT`. Common TNG-vs-SDSS O/H scale is not established. |
| `e2f3b038f8dd` | traceable-with-gap | SDSS `80,000` galaxies; `oh_at_logM9=8.572`; `oh_at_logM10p5=9.05`; summary rounded values `8.57` at `logM*=9.0` and `9.05` at `logM*=10.5` | `result.N=80000`; `result.oh_at_logM9=8.572`; `result.oh_at_logM10p5=9.05`; summary repeats the same values with expected rounding; log records `pulled 80000 galaxies; computing MZR`; artifact is `mzr.png` | no numeric contradiction; metadata/content gap exists because `spec.method=scaling-relation-evolution` and `topic=main-sequence-quenching` while result text and artifact report MZR | SDSS O/H calibration/scale: `ABSENT`. The output is in `12+log(O/H)`, but the SDSS calibration basis is not stated. |
| `gated-e2e-demo` | traceable-with-gap | TNG100 `23,722` galaxies; SDSS `120,000` galaxies; citation gate `2 unsupported of 4 checked`; review cycle `1`; expected-value `n_values=41`, `TENSION`; novelty top similarity `0.774`, `NOVEL` | `result.summary` states both counts; `draft.tex` abstract/result repeat both counts; `spec.data_sources` and `result.data_sources` are `tng, sdss`; log records TNG `gasZ`, SDSS pull, expected-value gate, lit grounding, draft/review/citation gates, PDF compile; `gates.citation_entailment.checked=4`, `n_unsupported=2`; `result.review_cycles=1`; `gates.expected_value.n_values=41` | no numeric contradiction; citation-integrity gap exists because citation gate records `2 unsupported of 4 checked` | TNG scale stated: `SF-weighted gas metallicity -> O/H (solar-scaled)`. SDSS O/H calibration/scale: `ABSENT`. Common TNG-vs-SDSS O/H scale is not established. |

## Cross-Run Numeric Consistency

| field | values found | audit finding |
|---|---|---|
| SDSS N-count | `120,000` in `2958462772b2`, `d8de519cb9c9`, `gated-e2e-demo`; `80,000` in `e2f3b038f8dd` | Not contradictory within any single run, but cross-run SDSS sample definitions differ. Treat `e2f3b038f8dd` as a different SDSS sample/selection unless source provenance later proves otherwise. |
| TNG N-count | `23,722` in `d8de519cb9c9` and `gated-e2e-demo`; absent in the two SDSS-only runs | Internally consistent between the two TNG+SDSS runs and repeated in `gated-e2e-demo` draft. |
| O/H values | `8.572`/`9.05` only in `e2f3b038f8dd`; no equivalent ordinate values in other run JSONs | Traceable to own result fields only for `e2f3b038f8dd`; cannot reconcile with other runs from captured fields alone. |
| O/H calibration/scale | TNG solar-scaled wording in `d8de519cb9c9` and `gated-e2e-demo`; SDSS calibration absent in all four | Reconciliation gap. A common O/H scale is required before treating TNG and SDSS metallicity curves as directly comparable. No dex offset is provided or applied here. |

## Gaps That Remain Open

- SDSS metallicity calibration is absent across all four runs.
- `d8de519cb9c9` lacks a draft/PDF despite `spec.outputs=["aastex-draft"]`; its own result note says the full draft is queued.
- `e2f3b038f8dd` reports MZR values while its method/topic labels point to `scaling-relation-evolution` and `main-sequence-quenching`.
- `gated-e2e-demo` has citation gate failures; this does not break numeric traceability, but it is a publication-readiness gap.

