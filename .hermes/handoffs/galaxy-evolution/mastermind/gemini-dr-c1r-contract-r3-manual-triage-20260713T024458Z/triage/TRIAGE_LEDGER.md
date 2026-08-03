# TRIAGE_LEDGER — 73-entry manual-queue classification (P2)

Packet: `gemini-dr-c1r-contract-r3-manual-triage-20260713T024458Z` · Lane: Lana (P2). Coordinator: Hwao.
Source of record: `triage/GORU_MANUAL_QUEUE_TABLE.json` (sha256 `ae5aac74ff85f6ba66652dd4e4f023dc435740e4b19713753ac94f380d95ad06`), extracted verbatim from `../gemini-dr-c1r-chip-validator-repair-20260713T010203Z/readjudication/validator_result_v2.json` (upstream validator-result sha256 `ad4d035b291f6d64ad47f510811cc05826d822f449cf3d181974be2ce2473d52`).
Classification is **routing, not scientific adjudication**. No source retrieval, no source-fidelity conclusion. Exactly one pinned lane per entry; source order M001–M073 preserved; ties break toward a `VERIFY_*` lane.
Per Amendment A3, the eight deterministic Section-2 Result-cell `UNCITED_CELL_CLAIM` findings that D3 re-types are **not** in this queue and do not appear below; the deterministic D1–D5 crosswalk lives in `design/CONTRACT_R3_DRAFT.md` §9.

## Lane arithmetic (reconciles to 73)

| Lane | Count |
|---|---:|
| `VERIFY_SOURCE_FIDELITY` | 47 |
| `VERIFY_SCIENTIFIC_COMPARABILITY` | 8 |
| `VERIFY_UNCERTAINTY_OR_SCOPE` | 18 |
| `CONTRACT_R3_CHANGE` | 0 |
| `IGNORE_FOR_THIS_CONTRACT_TEST` | 0 |
| **Total** | **73** |

## clause:code arithmetic (reconciles to 73)

| clause:code | Count | Lane |
|---|---:|---|
| `C3:UNCERTAINTY_CHECK` | 18 | `VERIFY_UNCERTAINTY_OR_SCOPE` |
| `C4:CITED_CELL_CLAIM_REVIEW` | 40 | `VERIFY_SOURCE_FIDELITY` |
| `C4:CITED_CLAIM_REVIEW` | 5 | `VERIFY_SOURCE_FIDELITY` |
| `C4:CITATION_QUALITY_REVIEW` | 1 | `VERIFY_SOURCE_FIDELITY` |
| `C4:SOURCE_FIDELITY_REVIEW` | 1 | `VERIFY_SOURCE_FIDELITY` |
| `C6:COMPARISON_LABEL_REVIEW` | 8 | `VERIFY_SCIENTIFIC_COMPARABILITY` |
| **Total** | **73** | |

## All 73 entries (source order)

| manual_id | ord | clause:code | source_refs | lane |
|---|---:|---|---|---|
| M001 | 4 | `C3:UNCERTAINTY_CHECK` | `table_row_4:3` | `VERIFY_UNCERTAINTY_OR_SCOPE` |
| M002 | 5 | `C3:UNCERTAINTY_CHECK` | `table_row_5:1` | `VERIFY_UNCERTAINTY_OR_SCOPE` |
| M003 | 6 | `C3:UNCERTAINTY_CHECK` | `table_row_5:2` | `VERIFY_UNCERTAINTY_OR_SCOPE` |
| M004 | 7 | `C3:UNCERTAINTY_CHECK` | `table_row_5:3` | `VERIFY_UNCERTAINTY_OR_SCOPE` |
| M005 | 8 | `C3:UNCERTAINTY_CHECK` | `table_row_6:2` | `VERIFY_UNCERTAINTY_OR_SCOPE` |
| M006 | 9 | `C3:UNCERTAINTY_CHECK` | `table_row_6:3` | `VERIFY_UNCERTAINTY_OR_SCOPE` |
| M007 | 10 | `C3:UNCERTAINTY_CHECK` | `table_row_8:1` | `VERIFY_UNCERTAINTY_OR_SCOPE` |
| M008 | 11 | `C3:UNCERTAINTY_CHECK` | `table_row_8:2` | `VERIFY_UNCERTAINTY_OR_SCOPE` |
| M009 | 12 | `C3:UNCERTAINTY_CHECK` | `table_row_9:1` | `VERIFY_UNCERTAINTY_OR_SCOPE` |
| M010 | 13 | `C3:UNCERTAINTY_CHECK` | `table_row_9:2` | `VERIFY_UNCERTAINTY_OR_SCOPE` |
| M011 | 14 | `C3:UNCERTAINTY_CHECK` | `table_row_10:1` | `VERIFY_UNCERTAINTY_OR_SCOPE` |
| M012 | 15 | `C3:UNCERTAINTY_CHECK` | `table_row_11:1` | `VERIFY_UNCERTAINTY_OR_SCOPE` |
| M013 | 16 | `C3:UNCERTAINTY_CHECK` | `table_row_14:2` | `VERIFY_UNCERTAINTY_OR_SCOPE` |
| M014 | 17 | `C3:UNCERTAINTY_CHECK` | `table_row_15:2` | `VERIFY_UNCERTAINTY_OR_SCOPE` |
| M015 | 18 | `C3:UNCERTAINTY_CHECK` | `table_row_16:2` | `VERIFY_UNCERTAINTY_OR_SCOPE` |
| M016 | 19 | `C3:UNCERTAINTY_CHECK` | `table_row_19:2` | `VERIFY_UNCERTAINTY_OR_SCOPE` |
| M017 | 20 | `C3:UNCERTAINTY_CHECK` | `bullet_25` | `VERIFY_UNCERTAINTY_OR_SCOPE` |
| M018 | 21 | `C3:UNCERTAINTY_CHECK` | `gap_line_4` | `VERIFY_UNCERTAINTY_OR_SCOPE` |
| M019 | 22 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_4:1` | `VERIFY_SOURCE_FIDELITY` |
| M020 | 23 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_4:2` | `VERIFY_SOURCE_FIDELITY` |
| M021 | 24 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_4:3` | `VERIFY_SOURCE_FIDELITY` |
| M022 | 25 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_4:4` | `VERIFY_SOURCE_FIDELITY` |
| M023 | 26 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_5:1` | `VERIFY_SOURCE_FIDELITY` |
| M024 | 27 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_5:2` | `VERIFY_SOURCE_FIDELITY` |
| M025 | 28 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_5:3` | `VERIFY_SOURCE_FIDELITY` |
| M026 | 29 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_5:4` | `VERIFY_SOURCE_FIDELITY` |
| M027 | 30 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_6:1` | `VERIFY_SOURCE_FIDELITY` |
| M028 | 31 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_6:2` | `VERIFY_SOURCE_FIDELITY` |
| M029 | 32 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_6:3` | `VERIFY_SOURCE_FIDELITY` |
| M030 | 33 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_6:4` | `VERIFY_SOURCE_FIDELITY` |
| M031 | 34 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_7:1` | `VERIFY_SOURCE_FIDELITY` |
| M032 | 35 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_7:3` | `VERIFY_SOURCE_FIDELITY` |
| M033 | 36 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_7:4` | `VERIFY_SOURCE_FIDELITY` |
| M034 | 37 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_8:1` | `VERIFY_SOURCE_FIDELITY` |
| M035 | 38 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_8:2` | `VERIFY_SOURCE_FIDELITY` |
| M036 | 39 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_8:3` | `VERIFY_SOURCE_FIDELITY` |
| M037 | 40 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_8:4` | `VERIFY_SOURCE_FIDELITY` |
| M038 | 41 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_9:1` | `VERIFY_SOURCE_FIDELITY` |
| M039 | 42 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_9:2` | `VERIFY_SOURCE_FIDELITY` |
| M040 | 43 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_9:3` | `VERIFY_SOURCE_FIDELITY` |
| M041 | 44 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_9:4` | `VERIFY_SOURCE_FIDELITY` |
| M042 | 45 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_10:1` | `VERIFY_SOURCE_FIDELITY` |
| M043 | 46 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_10:2` | `VERIFY_SOURCE_FIDELITY` |
| M044 | 47 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_10:3` | `VERIFY_SOURCE_FIDELITY` |
| M045 | 48 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_10:4` | `VERIFY_SOURCE_FIDELITY` |
| M046 | 49 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_11:1` | `VERIFY_SOURCE_FIDELITY` |
| M047 | 50 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_11:2` | `VERIFY_SOURCE_FIDELITY` |
| M048 | 51 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_11:3` | `VERIFY_SOURCE_FIDELITY` |
| M049 | 52 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_11:4` | `VERIFY_SOURCE_FIDELITY` |
| M050 | 61 | `C4:CITED_CLAIM_REVIEW` | `bullet_23` | `VERIFY_SOURCE_FIDELITY` |
| M051 | 62 | `C4:CITED_CLAIM_REVIEW` | `bullet_24` | `VERIFY_SOURCE_FIDELITY` |
| M052 | 63 | `C4:CITED_CLAIM_REVIEW` | `bullet_25` | `VERIFY_SOURCE_FIDELITY` |
| M053 | 64 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_28:1` | `VERIFY_SOURCE_FIDELITY` |
| M054 | 65 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_28:5` | `VERIFY_SOURCE_FIDELITY` |
| M055 | 66 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_29:1` | `VERIFY_SOURCE_FIDELITY` |
| M056 | 67 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_29:5` | `VERIFY_SOURCE_FIDELITY` |
| M057 | 68 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_30:1` | `VERIFY_SOURCE_FIDELITY` |
| M058 | 69 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_30:5` | `VERIFY_SOURCE_FIDELITY` |
| M059 | 70 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_31:3` | `VERIFY_SOURCE_FIDELITY` |
| M060 | 71 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_34:4` | `VERIFY_SOURCE_FIDELITY` |
| M061 | 72 | `C4:CITED_CELL_CLAIM_REVIEW` | `table_row_35:4` | `VERIFY_SOURCE_FIDELITY` |
| M062 | 73 | `C4:CITED_CLAIM_REVIEW` | `gap_line_1` | `VERIFY_SOURCE_FIDELITY` |
| M063 | 74 | `C4:CITED_CLAIM_REVIEW` | `gap_line_3` | `VERIFY_SOURCE_FIDELITY` |
| M064 | 75 | `C4:CITATION_QUALITY_REVIEW` | `(document-level)` | `VERIFY_SOURCE_FIDELITY` |
| M065 | 76 | `C4:SOURCE_FIDELITY_REVIEW` | `(document-level)` | `VERIFY_SOURCE_FIDELITY` |
| M066 | 78 | `C6:COMPARISON_LABEL_REVIEW` | `table_row_14:3` | `VERIFY_SCIENTIFIC_COMPARABILITY` |
| M067 | 79 | `C6:COMPARISON_LABEL_REVIEW` | `table_row_15:3` | `VERIFY_SCIENTIFIC_COMPARABILITY` |
| M068 | 80 | `C6:COMPARISON_LABEL_REVIEW` | `table_row_16:3` | `VERIFY_SCIENTIFIC_COMPARABILITY` |
| M069 | 81 | `C6:COMPARISON_LABEL_REVIEW` | `table_row_17:3` | `VERIFY_SCIENTIFIC_COMPARABILITY` |
| M070 | 82 | `C6:COMPARISON_LABEL_REVIEW` | `table_row_18:3` | `VERIFY_SCIENTIFIC_COMPARABILITY` |
| M071 | 83 | `C6:COMPARISON_LABEL_REVIEW` | `table_row_19:3` | `VERIFY_SCIENTIFIC_COMPARABILITY` |
| M072 | 84 | `C6:COMPARISON_LABEL_REVIEW` | `table_row_20:3` | `VERIFY_SCIENTIFIC_COMPARABILITY` |
| M073 | 85 | `C6:COMPARISON_LABEL_REVIEW` | `table_row_21:3` | `VERIFY_SCIENTIFIC_COMPARABILITY` |

Per-lane reason (uniform by clause:code; see JSON per-entry `reason`):
- `C3:UNCERTAINTY_CHECK` → UNCERTAINTY_NOT_QUOTED_BY_SOURCE / quoted-value / redshift-selection-scope faithfulness in this unit is an uncertainty-scope review.
- `C4:CITED_CELL_CLAIM_REVIEW` → Cited claim cell (same-cell citation resolved); needs source-fidelity check that the source supports the claim.
- `C4:CITED_CLAIM_REVIEW` → Cited bullet/GAP claim; needs source-fidelity check that the cited source supports the stated claim.
- `C4:CITATION_QUALITY_REVIEW` → Resolved-citation quality (aggregator / shared-source risk) is a source-resolution question; tie broken toward VERIFY_SOURCE_FIDELITY.
- `C4:SOURCE_FIDELITY_REVIEW` → Explicit source-fidelity review of the resolved-citation set.
- `C6:COMPARISON_LABEL_REVIEW` → Semantic correctness of the COMPARABILITY token is a scientific-comparability judgment.

## Zero lanes (Amendment A1 — valid outcomes, not forced)

ZERO_LANE CONTRACT_R3_CHANGE: no entry fit because Every finding an r3 D-item resolves (D1 6 UNLABELED_COMPARISON, D2 SIMBA MISSING_QUALIFIER, D3 8 Section-2 Result-cell UNCITED_CELL_CLAIM, D4 C7 integrity, D5 GAP granularity) is a deterministic FAIL outside the 73-entry manual queue per Amendment A3; no manual entry exists solely because of an r3-resolved contract pressure.
ZERO_LANE IGNORE_FOR_THIS_CONTRACT_TEST: no entry fit because All 73 manual entries carry a genuine uncertainty, source-fidelity, or comparability review need; none is a duplicate flag on the same defect or a formatting-only review with no scientific content, so none meets the ignore definition (ignore never means scientifically accepted).

## Notes
- `IGNORE_FOR_THIS_CONTRACT_TEST` is zero; had any entry qualified it would carry a one-clause residual-risk note. None did — ignore never means scientifically accepted.
- `CONTRACT_R3_CHANGE` is zero; its cross-map requirement applies only to manual entries in that lane (none). Deterministic r3-absorbed findings are crosswalked in `design/CONTRACT_R3_DRAFT.md` §9, not here.
- All disposition of resolvability/support/semantic-correctness is deferred to the later, separately gated manual verification pass; every citation remains QUARANTINED_PENDING_LOCAL_CHECK.

LANA_R3_TRIAGE_CLASSIFICATION_DONE_20260713T024458Z
