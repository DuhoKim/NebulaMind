# C41 Step-6 final receipts

Lane: `c41-baseline-restart-20260803T1253Z`
Receipt author: Tori
Receipt run: 2026-08-04 14:47 KST
Result: **PASS — STEP 6 RECEIPTED**

This receipt covers the finished Step-6 map, condensation report, Kun red-team, patch log, and the
ledger/stance inputs to which the map is bound. It is a mechanical custody receipt, not a new science
review or authorization for Step 7.

## SHA-256 artifact table

One `shasum -a 256` result per artifact, one line each:

```text
14447cf99ef89c2cad2771676e272e6a1b5a60915128f51dd7c7df5ce3219ae0  C41_STATUS_DEBATE_MAP_V1.md
2b31c54d51f14ca07c272fd6b1800bc6d1b3ebd7c90700bb112f008756f4eb2c  C41_CONDENSATION_REPORT.md
39d0a98a3ea90e0a93a4e3a4a88e97e49ac4f1965cd788c9ddb1afe03d9f5ea6  STEP6_PATCH_LOG.md
63329d870b31d3b588eed052662814e8983865adba95277440ea238de7b14e5a  KUN_STEP6_REDTEAM.md
e2938298dc9ee43b19ce1961fab45f3dc26db43d1e64147635b8c6dcdc2fbedf  C41_LEDGER.jsonl
59b61d7cc9f28253192954a1fab7355bc362da797464d22ec9fc5c354a122f6b  C41_STANCE_MATRIX.jsonl
```

## Mechanical checks

All checks below were re-executed from the live lane files. Machine-readable details are preserved in
`_tmp_tori_step6_receipt_check.json`; the checker is `_tmp_tori_step6_receipt_check.py`.

### 1. Claim coverage and the declared dual

PASS.

- Live ledger rows: 80, with 80 unique sequential IDs `c41_001` through `c41_080`.
- Claim entries: 76 (`certainty_level != no_info`).
- Honest placeholders: 4 — exactly `c41_018`, `c41_021`, `c41_059`, `c41_062`.
- Map coverage-table rows: 80; every ledger ID appears exactly once and no phantom ID appears.
- All 76 claims have an axis assignment; all four placeholders are explicitly `placeholder (R0)`.
- Claim-axis memberships: 77 — every claim exactly once, plus the one declared dual:
  `c41_065 = A1+A6`.
- No other claim contains a dual axis assignment.
- Condensation assignment trace: 81 rows = 77 claim memberships + 4 R0 placeholder rows.
- Trace IDs exactly equal the ledger IDs; every claim has one trace row except `c41_065`, which has
  exactly two.

Result: the map accounts for all 76 claim entries exactly once each, with only the declared second
membership for `c41_065`.

### 2. K = 7 axes, status, and settlement lines

PASS.

The map declares `K = 7` and contains exactly one section each for A1–A7. Every section contains
exactly one `Status` line and exactly one `What would settle it` line.

| Axis | Status lines | Settle lines | Result |
|---|---:|---:|---|
| A1 | 1 | 1 | PASS |
| A2 | 1 | 1 | PASS |
| A3 | 1 | 1 | PASS |
| A4 | 1 | 1 | PASS |
| A5 | 1 | 1 | PASS |
| A6 | 1 | 1 | PASS |
| A7 | 1 | 1 | PASS |

### 3. Kun F1–F4 patch coverage

PASS.

`KUN_STEP6_REDTEAM.md` carries findings F1, F2, F3, and F4. `STEP6_PATCH_LOG.md` explicitly covers
all four:

- F1: A7 retitled to make budget attribution primary, and the A7↔A6 boundary note added.
- F2: the missing A5 `Status` line added.
- F3: explicitly covered and deferred to the applier lane; Step 6 did not edit the ledger.
- F4: R2 wording clarified to “2 nontrivial components plus 4 isolates,” while retaining the total
  of six components when isolates are counted.

The receipt distinguishes “covered” from “applied”: F1, F2, and F4 are applied in Step-6 artifacts;
F3 remains the explicitly declared applier-lane action.

### 4. Ledger and stance receipts

PASS for the requested row-count and custody invariants.

- `C41_LEDGER.jsonl`: 80 parseable JSONL rows.
- `STEP4_VALIDATION_RECEIPT.json`: `status = PASS`, `entries_count = 80`.
- Equality: live ledger rows 80 == validation receipt 80.
- Ledger IDs: unique and exactly `c41_001`–`c41_080` in order.
- `C41_STANCE_MATRIX.jsonl`: 80 parseable rows with the same exact ordered IDs.
- Stance verification census: 76 `verified_consistent` + 4 `verified_no_claim`.

Known disclosed boundary: the live ledger still carries `verification_status: "validated"` on all 80
rows because of the v8 applier defect. The map and condensation report bind their verification census
to the pinned stance matrix and verification patch, and the patch log assigns re-landing F3 to the
applier lane. This receipt confirms that disclosure and does not misstate F3 as applied.

## Stage timeline from lane file mtimes

All timestamps are filesystem mtimes rendered in KST (`Asia/Seoul`). Where a stage was revised, both
the earlier review interval and the later canonical landing are shown rather than forcing a false
strict stage order.

| Stage / milestone | Lane artifacts used as mtime evidence | Mtime range (KST) | Receipt note |
|---|---|---|---|
| Step 0 freeze | `STEP0_FROZEN_QUESTION.md`; `STEP0_FREEZE_RECEIPT.md` | 2026-08-03 21:56:58 → 21:57:13 | Frozen question and receipt landed. |
| Step 1 corpus protocol/filter/selection | `step1_filter.py`; both selection JSONs; Kun refutation; patched protocol/report | 2026-08-03 22:12:34 → 22:38:52 | Executable corpus and Step-1 review closed. |
| Step 2 full-text/strength layer | `STEP2_FULLTEXT_MANIFEST.json`; `STEP2_STRENGTH_LABELS.json`; `YUI_STEP2_REPORT.md` | 2026-08-03 22:59:22 | Three canonical artifacts share the same mtime. |
| Step 3 V3 span table and Tori gate | `SPAN_TABLE.jsonl`; `STEP3_SUMMARY.json`; `GORU_STEP3_REPORT.md`; `TORI_STEP3_RECHECK3.md` | 2026-08-03 23:47:51 → 2026-08-04 00:01:45 | V3 regenerated, fidelity/zones/coverage receipted PASS_WITH_NOTES. |
| Step 4 review/certification passes | `LANA_STEP4_PASS.md`; `LANA_STEP4_REPASS.md`; `LANA_STEP4_CERTIFICATION.md` | 2026-08-04 10:47:05 → 11:26:25 | Review and certification artifacts landed. |
| Step 5 adversarial stance verification | `C41_STANCE_MATRIX.jsonl`; `VERIFICATION_STATUS_PATCH.jsonl`; `KUN_STEP5_REPORT.md` | 2026-08-04 14:04:47 → 14:06:40 | 76 consistent + 4 no-claim census landed. |
| Step 4 canonical v8 landing after Step 5 | `C41_LEDGER.jsonl`; `STEP4_VALIDATION_RECEIPT.json`; `GORU_STEP4_REPORT.md` | 2026-08-04 14:11:13 → 14:11:40 | Ledger/receipt final landing; disclosed verification-status overwrite occurred here. |
| Step 6 condensation/map/review/patch | `LANA_STEP6_REPORT.md`; `KUN_STEP6_REDTEAM.md`; map; condensation report; patch log | 2026-08-04 14:27:08 → 14:39:36 | Map built, red-teamed, and F1/F2/F4 patched; F3 deferred explicitly. |
| Step 6 final Tori receipt | `STEP6_RECEIPTS.md` | 2026-08-04 14:47 | This closure stamp; minute-resolution receipt-run time. |

## Final stage state

- Six required Step-6 artifacts are present and SHA-receipted.
- Claim coverage, sole dual membership, seven-axis structure, status/settle completeness, Kun patch
  coverage, and ledger/receipt equality all pass.
- The known F3 ledger-status re-land remains outside Step 6 and is not silently represented as done.
- Step 6 is closed on this receipt. No Step-7, prose, DB, publication, deploy/restart, or git action is
  authorized by this file.

TORI_STEP6_RECEIPTS_COMPLETE_20260804
