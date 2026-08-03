# Kun Packet A Receipt

Dispatch marker: OVERNIGHT_PAPER_BOARD_PACKET_A_KUN_BRIEF_V1

## Files Produced

| file | sha256 |
|---|---|
| packets/A-mzr-reconciliation/kun/REPRODUCIBILITY_AUDIT.md | d238904392ad66d6c0d1fbf4c188025793537bd5b5e047e9fb03e0ce66f059e0 |
| packets/A-mzr-reconciliation/kun/DUPLICATION_ANALYSIS.md | 2a2529e4672c47346995b4f825a980a78c2c25581c89c5a73af8c287dd8715f3 |
| packets/A-mzr-reconciliation/kun/DUPLICATION_ANALYSIS.csv | c59e6641c374ac612f18cf49d80cbec33d7562acce18035bb863870339b1a1ff |
| packets/A-mzr-reconciliation/kun/CANONICAL_RECOMMENDATION.md | 7da1f40c069d02644745c6bb46926815541e7bdc61cd7c41c2901fc320f5880e |

Receipt file SHA256 is not self-listed because the receipt content would change its own hash.

## Traceability Findings

Source hash check passed for all 38 baseline source files. This was a documentary traceability audit only; no runner was run and no SDSS/TNG data was re-pulled.

| run_id | traceability summary |
|---|---|
| `2958462772b2` | SDSS `120,000`, review cycle `1`, and `MINOR` review are traceable to own JSON/draft/history. SDSS O/H calibration/scale is absent. |
| `d8de519cb9c9` | TNG `23,722` and SDSS `120,000` are traceable to own summary/spec/log. It is figure/summary-only; draft/PDF are absent and the result says the full draft is queued. TNG solar-scaled O/H is stated; SDSS scale is absent. |
| `e2f3b038f8dd` | SDSS `80,000`, `oh_at_logM9=8.572`, and `oh_at_logM10p5=9.05` are traceable to own result fields and log. Method/topic labels do not match MZR content. SDSS calibration/scale is absent. |
| `gated-e2e-demo` | TNG `23,722`, SDSS `120,000`, review cycle `1`, expected-value `TENSION`, and citation gate `2 unsupported of 4 checked` are traceable to own JSON/draft/log/gates. TNG solar-scaled O/H is stated; SDSS scale is absent. |

Open reconciliation gap: a common TNG-vs-SDSS O/H scale is not established. No dex offset was invented or applied.

## Duplication Classifications

| run pair | classification |
|---|---|
| `d8de519cb9c9` vs `gated-e2e-demo` | `superset-subset` |
| `2958462772b2` vs `d8de519cb9c9` | `superset-subset` |
| `2958462772b2` vs `gated-e2e-demo` | `superset-subset` |
| `2958462772b2` vs `e2f3b038f8dd` | `near-duplicate-different-sample` |
| `d8de519cb9c9` vs `e2f3b038f8dd` | `near-duplicate-different-sample` |
| `e2f3b038f8dd` vs `gated-e2e-demo` | `near-duplicate-different-sample` |

No pair was classified as `exact-duplicate`.

## Canonical Recommendation

Recommend `gated-e2e-demo` as the canonical TNG+SDSS MZR representative and recommend Packet C build from `gated-e2e-demo` rather than directly from `d8de519cb9c9`, provided citation repairs and the O/H-scale caveat remain explicit. Treat `d8de519cb9c9` as the redundant figure/summary precursor, `2958462772b2` as SDSS-only context, and `e2f3b038f8dd` as a separate SDSS 80,000-galaxy MZR-family output with label/provenance gaps.

## STOP Notes

None. No source drift, `CONTRADICTS` expected-value verdict, payment/overage/top-up prompt, runner/data-pull need, source edit, public/DB/wiki/git/cron/browser/account/deploy action, or write outside the listed Kun roots occurred.

## Completion State

DONE

OVERNIGHT_PAPER_BOARD_PACKET_A_KUN_DUPLICATION_COMPLETE_V1
