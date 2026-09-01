# AGY Unbuilt Candidate Verify — 2026-09-01

## BS-2v — DEFECTIVE
[F-1] The candidate fails multiple requirements set by frozen texts:
1. It violates the text rule from `PREREG_SUCCESSOR_DRAFT_V134_20260831.md`: "Until an absent slot has a `SLOT_SCHEMA` entry, NO receipt may be emitted for it." Since `BS-2v` is absent from `SLOT_SCHEMA` in `successor_ref_v9.py`, no candidate can be emitted.
2. It bypasses `v9.receipt()`. It was manually built via `conv.build_receipt()` and does not pass `v9.receipt()`. Submitting its fields to `v9.receipt()` with proper bytes encoding produces an envelope SHA that does not match the candidate's `receipt_sha256`. 
3. Because it is absent from `SLOT_SCHEMA`, it does not "carry EXACTLY its v9 `SLOT_SCHEMA` field set" as required.

## BS-1b — SOUND
Candidate carries exactly the `SLOT_SCHEMA` fields (`photoz_product`, `columns`, `join_keys`, `provenance`) and passes `v9.receipt()` with correct bytes encoding. Fields are verbatim quoted from `BRANCH_CONFIG` and `acquire` ADQL queries. SHAs in the provenance are derived properly from on-disk facts.

## BS-8p — STOP-AND-BLOCKED
The block is REAL. As specified in the draft, the BS-SI stratum-index artifact schema is pending, and "until then no stratum-index artifact may be emitted, which blocks BS-2f's allocation and BS-8p." It requires realized counts that cannot be derived without the filled artifact.

## BS-2a — STOP-AND-BLOCKED
The block is REAL. The design elements (evidence schema, ledger schema, recomputation code, verify_cutout_integrity) are marked as DESIGN/UNFILLED in the draft, blocking partial thresholds from acting as a fill authorization.

## BS-9 — STOP-AND-BLOCKED
The block is REAL. The production input function contract and R1-R5 checks are missing, and `nm_acquire_cutouts.py` is expressly prohibited in the draft. No valid input function or hash can be produced without them.

SEAT: AGY
VERSION: UNBUILT-VERIFY-V1
VERDICT: DEFECTIVE
COUNT: 1
F-lines: 9-23
