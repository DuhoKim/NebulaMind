# Tori pre-classification queue-shape note

The mechanically verified 73-entry queue contains only findings whose status is `MANUAL_REVIEW_REQUIRED`:

- 18 × `C3:UNCERTAINTY_CHECK`
- 40 × `C4:CITED_CELL_CLAIM_REVIEW`
- 5 × `C4:CITED_CLAIM_REVIEW`
- 1 × `C4:CITATION_QUALITY_REVIEW`
- 1 × `C4:SOURCE_FIDELITY_REVIEW`
- 8 × `C6:COMPARISON_LABEL_REVIEW`

Important scope fact: the eight Section-2 `UNCITED_CELL_CLAIM` findings that D3 re-types are deterministic FAIL findings, not members of the 73-entry manual queue. They therefore cannot be inserted into `TRIAGE_LEDGER.*` without violating the exactly-73 source-order custody rule.

Possible plan tension: `HWAO_PLAN.md:38` requires Tori to sample ≥2 entries from every lane, while §0 does not require every lane to be non-empty. The evidence may legitimately yield zero `CONTRACT_R3_CHANGE` and/or zero `IGNORE_FOR_THIS_CONTRACT_TEST` entries. No entry should be forced into a lane merely to satisfy the sampling quota.

Requested coordinator clarification before P2:

- confirm that zero-count lanes are valid when no source entry fits;
- amend P3 sampling to ≥2 from every **non-empty** lane, with zero lanes explicitly audited as zero;
- confirm the eight deterministic D3 failures stay in the r3 change record/residue crosswalk, outside the 73-entry manual ledger.

No classification was performed in this note.

TORI_PRECLASSIFICATION_SHAPE_NOTE_20260713T024458Z
