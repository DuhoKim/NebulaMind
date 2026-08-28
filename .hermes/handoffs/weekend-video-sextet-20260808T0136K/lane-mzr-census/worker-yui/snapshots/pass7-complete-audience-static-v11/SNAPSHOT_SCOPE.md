# Exact review-packet scope — pass-7 v11

This file distinguishes the immutable review packet from the larger live worker lane.

## Packet authority

`MANIFEST.json` is the complete and authoritative inventory of this exact snapshot. Every listed entry is included, hashed, and mode-enforced. No unlisted live-lane artifact is claimed to be inside the packet.

## Included evidence classes

- Exact v8 storyboard, complete-audience projection over narration/screen/citations, neutral-question audience packet, proposal validation, approved contract, validator, visual-v9-aligned preparers, mutation suite, and v11 local-check receipt.
- `NUMERIC_SOURCE_AUDIT.json` and the eight-file snapshot-local frozen source set.
- All 43 exact candidate frame PNGs, frame hashes, boundary-continuity evidence, OCR evidence, and contact sheets.
- Static-v9 proposal and its snapshot-local renderer/full-resolution QA; renderer `--check` is byte-exact and write-free; earlier visuals are excluded from current acceptance.
- Integrator request, citation ledger, display citations, diagnosis, candidate notes, and explicit external-candidate custody receipt.

## Deliberate exclusions

- Prior paper-naive and adversarial answer/result artifacts, including v1–v8 review outputs, so the closed-book packet contains no review answer key.
- Historical pass-2 through pass-6 QA packets. They remain preserved in the live lane but are neither dependencies nor asserted members of this exact packet.
- The external MP4 candidate itself. It is referenced and hash-checked at both review boundaries but not copied.

## External candidate boundary

The candidate is mode `0644` and owner-writable. “Read-only” means worker authorization and handling policy, not filesystem enforcement. Snapshot `0444`/`0555` guarantees apply only to the immutable snapshot tree. `qa/EXTERNAL_CANDIDATE_CUSTODY.json` records the exact distinction.

## Gate boundary

Packet or proposal PASS cannot clear the failed encoded candidate, assert future MP4 timing, run T2 eligibility, produce an eligible-table count, invoke TTS, integrate, publish, or write shared/public/Git state.
