# BS-2v defective-candidate repair

## Decision: B is mandated

The frozen V134 bytes classify BS-2v as a slot receipt and prohibit emission
until a successor-layer schema entry exists.  The deciding text is:

> **Every producer of a SLOT RECEIPT — that is, of an artefact whose slot
> appears in `SLOT_SCHEMA` — must construct it through `receipt_strict()` and
> through nothing else.**

> **Until an absent slot has a `SLOT_SCHEMA` entry, NO receipt may be emitted
> for it.**

The same clause expressly identifies the affected slot and when its entry is
created:

> BS-2v is UNRESOLVED, and **specifying a field set for a slot whose content is
> undecided would pin the wrong thing.** Each entry is written as part of
> filling its slot, under the same two constraints BS-3g met [...].

Section 7's BS-2v row binds `registry_digest` "in the slot schema".  Section 11
then fixes the canonical authenticated fields:

> The receipt must conform to a **canonical authenticated receipt schema**,
> including: registry digest, converter implementation digest, ordered
> normative IDs, exercised IDs, uniqueness and count closure, per-ID
> source/phase/failure-effect, and result classification (all authenticated).

The shipped converter's exact six producer fields implement that frozen list:
`registry_digest`, `converter_sha256`, `normative_ids`, `exercised_ids`,
`per_id`, and `classifications`.  Uniqueness and count closure are recomputed by
the independent gate rather than trusted as producer assertions.  Therefore A
is not permitted: the converter's own authentication remains a required inner
check, but it does not replace the mandated strict slot envelope.

## Implementation and validation

`run/receipt_strict.py` now pins `SLOT_SCHEMA_SUCCESSOR["BS-2v"]` to exactly
those six fields and emits schema `BS2V-V1`.  Frozen v9 was not modified and
`v9.receipt()` was not used.  `run/build_unbuilt_candidates_20260901.py` first
runs the converter's independently recomputing `gate()`, then emits the body
through `receipt_strict("BS-2v", body)`.

Produced `run/classp_candidates/BS-2v.json`:

- 60 ordered normative IDs and 60 exercised IDs
- strict envelope SHA-256:
  `92fe7a2192dfa7a152e9d87e9d05de0618ba86f9fe2f629216173257e17c8462`
- candidate file SHA-256:
  `a1ad1790161f63e7a09f994886b61a7b38b08ab6bb863c52fe5fee665de33696`
- converter SHA-256 (also authenticated in the body):
  `001cd94456449851a9d2f4cf0b7c857683c92129715bff5661ad5fd2a31338a4`
- frozen draft SHA-256:
  `9411fe3fa89915cca08d07da6573076af7c924d07e25416f9dd35be8eabb604f`
- successor strict-constructor SHA-256:
  `f50d8c1d9c4c3cf80bc6ba3a32a6aaa618d79092670cdac2c79cc8b9711ddef1`

Checks executed successfully:

- `run/receipt_strict.py`: 7/7 PASS
- `gates/bs2v_void_converter.py`: 13/13 green
- exact reconstruction equality through `receipt_strict()`
- converter `gate()` over the emitted strict envelope body

The superseded `run/classp_candidates/BS-2v.REJECTED-UNBUILT-V1.json` remains
unchanged as the audit record (SHA-256
`46602348b5eed37d0de3877b3eff6fe73b88b5a7cb102be1fba9751d40f57a28`).

SEAT: CODEX
VERSION: BS2VFIX-V1
VERDICT: FIXED
COUNT: 1
