# KUN Step 9B Reproducibility Report

Marker: `KUN_STEP9B_REPRO_DONE_20260703T1329Z`

## Scope and Method

Reviewed only the Step 9B packet at `docs/baseline_step9b_claim_evidence_continuity_20260703T1329Z` per the saved brief. I did not apply product/wiki/content changes, did not run DB/API mutations, did not use git commit/push/merge, and did not patch files. This report was produced from read-only inspection of packet artifacts plus the requested report write.

Recomputed from JSON/JSONL artifacts and manifest file hashes, and reran the local packet validator script.

## Recomputed Counts

- Claim continuity rows: 6
- Current claim object rows: 6
- Claim IDs present: 2913, 2915, 2917, 2921, 2924, 2929
- Captured evidence rows: 54
- Sum of per-claim captured evidence counts: 54
- Step 9 source rows: 26
- Publicly resolved source rows: 1
- Unresolved source rows: 25
- Public resolved product evidence IDs: 6651
- Citation marker plan rows: 16
- GO checklist rows: 5
- NO-GO checklist rows: 5

## Validator and Manifest

Validator status is PASS.

Validator rerun summary returned:

```json
{"claim_count": 6, "evidence_row_count": 54, "go_count": 5, "insert_heavy_gate": "TRIGGERED", "no_go_count": 5, "resolved_source_count": 1, "status": "PASS", "step9_source_count": 26, "unresolved_source_count": 25}
```

All manifest-listed SHA-256 hashes match the current packet files:

- `APPROVAL_PACKET.md`: `80554aa45aa71e1bb1842156d52686c639fb894e65f70de6f7de04c329456b9e`
- `artifacts/citation_marker_resolution_plan.jsonl`: `8e3df14ac0bdb20258b51dab28d74c6ca4b0b4234f47f45db3814046aebd56a4`
- `artifacts/claim_continuity_resolution.jsonl`: `173aa28a70a99105ebd5dc8d8a1252e291bb78b4f948fbcd762fbd07075b4b4e`
- `artifacts/six_claim_evidence_rows.jsonl`: `966576772bb242e35c97ec2e238a45764bb3f1adbe30218c2854ea798f2c4aa0`
- `artifacts/six_current_claim_objects.jsonl`: `13e0e76bb31ae470cb073c5a43ee56f66a7bf8e392adc29cc71b833d7f7e859d`
- `artifacts/step9_source_to_product_evidence_match.jsonl`: `9b612d8d52e85c213bdb748e50d6e1e39c4fff9c36d31bb7218aa1d312b467ea`
- `go_no_go_checklist.jsonl`: `56bce43d68991f479821205a772630aa8339dc00f55834ddc0ea171e4d800eea`
- `reports/STEP9_SOURCE_TO_PRODUCT_EVIDENCE_MATCH.md`: `39fc9449916b2eae10bab911351145bfc1ff038f1612bad7c76454f256bf73b8`
- `scripts/validate_step9b_packet.py`: `9f26a8859fbd56337d615adb7a746a11638092bed041bd6b10059b11356188dc`
- `summary.json`: `8044d40da694fddd4da169bacfcd95c59cebd389093902cccee05a038a5aa1cb`

## Claim Continuity Decisions

- 2913: `DO_NOT_CARRY_FORWARD_IN_AGN_SECTION`
- 2915: `CARRY_FORWARD_COMPATIBLE_EXISTING_CLAIM_CHIP`
- 2917: `CARRY_FORWARD_COMPATIBLE_EXISTING_CLAIM_CHIP`
- 2921: `DO_NOT_CARRY_FORWARD_IN_AGN_SECTION_BY_DEFAULT`
- 2924: `REPLACE_FLAT_CLAIM_WITH_MODEL_BOUNDED_WORDING_DO_NOT_CARRY_CURRENT_CHIP_AS_IS`
- 2929: `SUPERSEDE_WITH_STEP9_SCOPED_SYNTHESIS_DO_NOT_REUSE_AS_IS`

The default carry-forward set is therefore exactly 2915 and 2917. The packet blocks/desurfaces/requires later workflow decisions for 2913, 2921, 2924, and 2929. This is mechanically present and gate-wise sane for a packet-only Step 9B review.

## Evidence-ID Resolution

The source-to-product evidence map has 26 rows. Only source 14 resolves to a public existing product evidence row, evidence ID 6651. The remaining 25 rows have `NO_PUBLIC_MATCH_FOUND_REQUIRES_DB_SEARCH_OR_INSERT_CANDIDATE`.

This supports the packet's insert-heavy gate: `TRIGGERED`. I found no evidence-ID laundering in the Step 9B packet: unresolved sources are not assigned invented product evidence IDs, and current product evidence attached to removed/current claim chips is not reused as Step 9 source evidence without an explicit later audit.

## Execute/Apply Phrase and Hard Stops

The packet contains negative/locked references to apply/execute only, including the explicit statement that it has no valid execute/apply phrase. I found no valid positive execute/apply phrase.

Hard stops are zero in both `summary.json` and `manifest.json`:

- API mutations: 0
- DB writes: 0
- SQL mutations: 0
- migrations: 0
- product publish: 0
- deploy/restart: 0
- exact-diff apply: 0
- git commit/push/merge: 0

## Review Answers

1. The six claim-chip decisions are mechanically present and scientifically/gate-wise sane for packet-only continuity resolution.
2. It is correct for this packet to carry forward only 2915 and 2917 by default, while blocking/desurfacing/retiring/superseding 2913, 2921, 2924, and 2929 pending later operator decisions or claim workflow.
3. The evidence-ID mapping is honest: only evidence 6651 is publicly resolved for the Step 9 source list, 25 of 26 sources remain unresolved, and the insert-heavy gate is triggered.
4. The packet avoids evidence-ID laundering and does not invent product evidence IDs.
5. The packet avoids a valid execute/apply phrase and keeps DB/API/product/git/deploy hard stops at zero.
6. Step 9B should be marked complete as `PACKET_ONLY_NOT_EXECUTED`; no patches are needed.

## Final Stance

PASS
