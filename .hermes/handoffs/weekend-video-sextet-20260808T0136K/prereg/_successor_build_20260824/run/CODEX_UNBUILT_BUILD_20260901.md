# Unbuilt Class-P candidate build — 2026-09-01

Boundary: read-only use of frozen v9 and lane artifacts. No image was found,
opened, hashed, or transported; no χ was measured; no live store was written.
Candidates were written as each completed, and this report was written last.

## BS-2v — PRODUCED

Candidate: `run/classp_candidates/BS-2v.json` (file sha256
`46602348b5eed37d0de3877b3eff6fe73b88b5a7cb102be1fba9751d40f57a28`).
BS-2v is absent from frozen v9 `SLOT_SCHEMA`, so the converter's authenticated
schema applies. Its frozen code clause is: “The receipt schema is the item's own
list, verbatim fields: (registry_digest, converter_sha256, normative_ids
ordered, exercised_ids, per_id rows, result classifications).”

The candidate binds §7.1 registry digest
`315ef0195d047bf22ff3164b98f7ec036d04f18869f8ab67b349fdede5ed9053`,
on-disk converter sha256
`001cd94456449851a9d2f4cf0b7c857683c92129715bff5661ad5fd2a31338a4`,
and authenticated receipt sha256
`da87d01bb5e159319402295d21784ee57f46e679665f6fbd72e038aa7350ce78`.
The converter's fresh battery was 13/13 green and its gate returned PASS over
the emitted body and frozen V134 text.

## BS-1b — PRODUCED

Candidate: `run/classp_candidates/BS-1b.json` (file sha256
`690d1c14587c75ab7df0cb3665408482f14b2ef548721b0f52e9b5c59200b9c5`).
Frozen `v9.receipt()` accepted exactly `(photoz_product, columns, join_keys,
provenance)`, producing body sha256
`2035966fab9d5b910e02ba8116e1d89052c6c7b7bfdf45de2216412abcd85f53`
and envelope sha256
`d0328354a27fb00be97bad53b31a589849b16a1d3c6289f84bc8bf0227767563`.

Field provenance: `photoz_product=ls_dr10.photo_z` comes from frozen
`BRANCH_CONFIG["B_DR10_1"]`; product columns
`ls_id,release,brickid,objid,z_phot_median` and join keys
`ls_id,release,brickid,objid` occur literally in both on-disk acquisition ADQL
queries. The provenance field binds the Branch-B config digest, both query-file
digests, both acquisition-receipt-file digests, and their authenticated output
digests (`425a42c3…` positions and `61214b59…` quality).

## BS-8p — STOP-AND-BLOCKED

Exact missing value: the realized 3 × 9 cell counts from the verified BS-SI
stratum-index artifact. Frozen §7 says the BS-SI artifact is χ-derived and
fills only at P2–P3, its schema is pending, and “until then no stratum-index
artifact may be emitted, which blocks BS-2f's allocation and BS-8p.” Therefore
`allocate_handcheck` cannot produce a real allocation pre-image. The v9 schema
requires a nonempty `allocation`; substituting a prose method would not be the
frozen row's required “3 × 9 allocation.” No candidate was emitted.

The applicable carried plan remains v9 `allocate_handcheck`: proportional
integer allocation over 3 × 9 cells, per-bin floor 10, inherited-stratum floor
30, total fixed real-label budget `HC_REAL_LABELS=500`, with deterministic
largest-remainder completion. It does not supply the missing realized counts.

## BS-2a — STOP-AND-BLOCKED

The quality thresholds are real and consistent:
`flux_ivar_r > 8.4000532`, `psfsize_r < 1.5699703`, and `nobs_r >= 3`, quoted
identically in frozen §7 and `acquire/quality_cut_receipt.json`. The existing
quality component is already pinned as `ref/bs2a_quality_gate.py` sha256
`dfbd63d146b472f194f74d01b313874f23c9a4264f26903b22837ae32aa18508`.

Exact missing design is named by the frozen BS-2a row: an exact v9 `SLOT_SCHEMA`
entry/canonical receipt fields; `verify_cutout_integrity` (Row C2); the
confidence threshold; retry and failure semantics; the ledger schema; and
§6.3(9) adversarial producer fixtures under transformed cutouts. The row also
states those fixtures need cutouts, which BS-6 blocks, and that the quality
component is “not a fill authorization.” Frozen §7 further says filling a DESIGN
slot requires a new text revision and fresh text gate, not receipt insertion.
Accordingly no partial threshold-only predicate or candidate was fabricated.

## BS-9 — STOP-AND-BLOCKED

The derivable branch values are only Branch B, band `r`, HDU `1`, from frozen
`BRANCH_CONFIG`. Exact missing design/code: the production single-band
HDU/plane input-function contract (including required source array shape,
normalization/dtype/channel ordering and tensor layout), the gated replacement
runner, and the definitions/implementation of the five R1–R5 checks that must
run through that function. Frozen `successor_ref_v9.py` contains the BS-9
receipt field names but no R1, R2, R3, R4 or R5 machinery and no BS-9 input or
replacement-runner symbol. Predecessor `nm_acquire_cutouts.py` remains expressly
prohibited and predecessor receipts cannot supply this run's evidence. Without
the missing definitions, an `r1_r5_receipt` digest+verdict and production
function hash would be synthetic, so no function, fixtures, or candidate was
emitted.

## Build artifact

`run/build_unbuilt_candidates_20260901.py` sha256
`21169c26b482f8d2bbb02a7cf45caca16800fdd41620f7445ff8f74d9f7025f3`
is the offline reproducible builder for the two produced candidates.

SEAT: CODEX
VERSION: UNBUILT-V1
VERDICT: 2-PRODUCED-3-BLOCKED
COUNT: 2
