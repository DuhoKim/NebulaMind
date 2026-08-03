# KUN Step 9D Reproducibility Report

Verdict: PASS

Reviewed packet: `docs/baseline_step9d_insert_heavy_exact_diff_prep_20260703T1500Z`

## Scope

Read-only reproducibility review of packet artifacts only. No SQL was executed, no DB/API/product/git mutations were performed, and no packet artifact was modified.

## JSON / JSONL Parse Recompute

All packet `.json` and `.jsonl` artifacts parsed successfully.

Key recomputed counts:

- `proposed/step9d_candidate_source_entities_25.jsonl`: 25 rows; 25 unique `source_num` values.
- `proposed/step9d_claim_evidence_use_matrix_35_design.jsonl`: 35 rows; references 25 unique `source_num` values.
- `proposed/step9d_citation_anchor_replacement_design.jsonl`: 16 rows.
- `artifacts/step9d_candidate_claim_skeletons.jsonl`: 6 rows.
- `go_no_go_checklist.jsonl`: 12 rows; 6 `GO`, 6 `NO_GO`.

Additional packet design-row files also parse and align with the same distinction:

- `artifacts/step9d_source_insert_candidate_mapping.jsonl`: 25 rows.
- `artifacts/step9d_proposed_evidence_candidate_rows_design.jsonl`: 35 rows.
- `artifacts/step9d_proposed_page_citation_link_rows_design.jsonl`: 35 rows.

## Validator Consistency

`validation/step9d_packet_validation.json` is internally consistent with the recomputed artifact counts:

- Source entities: validator 25; recomputed 25.
- Claim-use design rows: validator 35; recomputed 35.
- Claim skeletons: validator 6; recomputed 6.
- Citation anchors: validator 16; recomputed 16.
- Unresolved refs: validator 0.
- Cross-claim review refs: validator 35.
- Hard stops: validator `hard_stops_zero: true`; `summary.json` and the snapshot summary show all hard-stop counters at 0.
- Validator status: `PASS`; validator errors: `[]`.

## SQL / Execution Boundary

No executable `.sql` files were found under the packet directory.

No active execution phrase was found. The packet text explicitly states it is preparation-only, says no executable SQL was generated, says no active execution phrase exists, and marks execution/apply authorization as false. The `APPROVE ...` strings present in `summary.json` and `APPROVAL_PACKET.md` are bounded as preparation-only or next recommended approval text, with explicit no-write/no-apply/no-mutation clauses.

## 25-Source vs 35-Claim-Use Distinction

The distinction is clearly represented:

- `APPROVAL_PACKET.md` lists "Source-level insert candidates: 25" separately from "Claim-use design rows: 35".
- `summary.json` separately records `source_entity_count: 25` and `claim_use_row_count_design: 35`.
- `validation/step9d_packet_validation.json` separately records `source_entity_count: 25` and `claim_use_row_count_design: 35`.
- The claim-use matrix contains 35 rows across the same 25 source entities, with some sources intentionally mapped to more than one claim.

Patch requests: none.

KUN_STEP9D_REPRO_DONE
