# Residue report — C1r validator r3

Packet: `gemini-dr-c1r-validator-r3-implementation-20260713T034742Z`
Status: **diagnostic offline validator output only**

This report does not certify the C1r answer, validate its science, release any citation from quarantine, or retroactively accept the earlier Deep Research run. The unchanged artifact still fails the deterministic contract.

## Input custody

The r3 run reused the sealed C1r body and rendered DOM without editing them. T-CUST hashes remained GREEN:

- prompt: `fffac44fbf6e9abe3afb1f8f34f3a9e3e7688991f319c4927459fb29ac00e1ef`
- body: `8a130c5a6fc1b1f5d534888d3fb20806230b8b4c7737cb00f9bfb18ad0d6bc00`
- rendered DOM: `78ed129c47daf9300d9ed319aa1ffe95bbb0d1810a223733afaf48c4372f2bbc`
- v2 contract reference: `1b10b4538162e1f786e3e36b639448cbe0d4252282d236c88495272398062338`
- v2 structured-capture reference: `e26819dbc90a040ecc228639fbee3e2a68f8942fa9d26b9458aee71bbc65e3e9`
- v2 result reference: `ad4d035b291f6d64ad47f510811cc05826d822f449cf3d181974be2ce2473d52`

## Fresh r3 result

- overall: `FAIL`
- deterministic failures: **19**
- manual-review findings: **82**
- pass findings: **4**
- total findings: **105**
- `C4:UNCITED_CELL_CLAIM`: **0**

### Deterministic failures

| Clause/code | Count | Exact locus or mechanical evidence |
|---|---:|---|
| `C2:GAP_MULTIPLE_PER_PARAGRAPH` | 1 | parent paragraph `11` contains four GAP units |
| `C2:SENTINEL_FORMAT_DEFECT` | 1 | `table_row_7`, column 2 |
| `C6:MISSING_CALIBRATION_TARGET_PREFIX` | 9 | `table_row_4..11`, column 1; plus `table_row_11`, column 2 |
| `C6:UNLABELED_COMPARISON` | 6 | rows 5, 6, 9, 10, 11 column 3; plus `gap_line_1` |
| `C6:MISSING_QUALIFIER` | 1 | `table_row_6`, column 2 |
| `C7:C7_INTEGRITY_FAILURE` | 1 | 12 orphan indices, 9 duplicate rows, 46 blank short-name rows, no inline-only index |

Near-duplicate indices 14 and 29 are not part of the C7 hard failure. They are routed as one separate manual `C7_NEAR_DUPLICATE` finding.

### Manual queue

| Clause/code | Count |
|---|---:|
| `C3:UNCERTAINTY_CHECK` | 18 |
| `C4:CITATION_QUALITY_REVIEW` | 1 |
| `C4:CITED_CELL_CLAIM_REVIEW` | 48 |
| `C4:CITED_CLAIM_REVIEW` | 5 |
| `C4:SOURCE_FIDELITY_REVIEW` | 1 |
| `C6:COMPARISON_LABEL_REVIEW` | 8 |
| `C7:C7_NEAR_DUPLICATE` | 1 |
| **Total** | **82** |

The eight Section-2 Result-cell claims are manual reviews at `table_row_14..21`, column 2, with each row's Citation cell acting as the authoritative citation owner. Empty or unresolvable Citation cells hard-fail in the negative fixtures.

## Executable verification

- Python test suite: **14 passed**
- Node capture baseline: **passed**
- Python compile checks: passed
- Node syntax checks: passed
- independent regeneration: capture and validator outputs reproduced byte-for-byte

## Output hashes

- structured capture: `95f0fe7a3fe710a4599188c18a2c39717887e970f62b64e36d10804b6afffe76`
- validator result: `5fa0adb8a91ce3af7f19cfc88582cde8e0065e58f996c5c8370bc1f6d944bed0`

## Boundary statement

This was packet-local, offline implementation and diagnosis. No live Deep Research run, browser action, DB write, dashboard change, deploy, cron, git write, publication, trust update, or quarantine release occurred.

TORI_GATE_A_RESIDUE_REPORT_R3_DONE_20260713T034742Z
