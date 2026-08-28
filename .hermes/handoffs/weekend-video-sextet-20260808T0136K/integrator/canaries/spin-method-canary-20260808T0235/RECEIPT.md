# RECEIPT — spin-method-canary-20260808T0235 (v2)

Seat: `yui-video-integration`. Rendered 2026-08-08 02:35–02:40 KST (stamps from `date`).
Freeze in force: unchanged — `spin-method-canary-pass1-20260808T0153K`,
`video_reportable_now: false`, `BLOCK_SUBSTANTIVE_RESULT_RENDER; ALLOW_METHOD_ONLY_CANARY`.

## What this is

Version 2 of the silent, method-only spin-parity visual canary. **v1
(`spin-method-canary-20260808T0204/`) is preserved unchanged** — never overwritten, per
`HWAO_WEEKEND_ORDER.md` §5.

## The one change, and its evidence

v1's funnel card asserted "each rung only narrows it" and drew the counts as a descending
sequential funnel. That nesting is **not stated by the cited artifact**: `T1_FUNNEL.json` records
`SPIRAL_FLAG`, `0.60`, and `0.80` as sibling readouts under `funnel.zooSpec`, each with its own
pass/classified/tie accounting. The spin worker lane's independently validated static proposal
(`lane-spin-parity/worker-yui`, `STATIC_PROPOSAL_QA.md`, 12/12 claim-traceability PASS) renders
the same counts as parallel branches labelled `PARALLEL READOUTS — NOT A SEQUENTIAL FUNNEL`.

Correction applied (card 5 only; all other cards byte-identical in text to v1):

- heading → "Three predeclared readouts of one frozen source";
- figure → `figures/readouts_method.png`, a parallel-branch diagram drawn deterministically from
  the pinned `T1_FUNNEL.json` (sha `ed97758a…`, identical to the freeze), adopting the worker
  lane's parallel-readouts structure with credit;
- body states the readouts are parallel, not nested; tie accounting and the "no asymmetry
  computed" statement are retained.

The handedness schematic is unchanged from v1. No quarantined figure was read or reused.

## Verification

- Numeric-source guard: PASS 11/11 twice (`--check`, then pre-render); evidence single-hit and
  on-topic (`667944 → rows_parsed`, `29053 → N_tie`, `36 → probed`).
- Machine QA (`reviews/yui/audit_canary.py`): PASS — 11/11 states, all expected cuts, none
  unexpected, single silent H.264 video stream, sha matches this receipt's `hashes.txt`,
  +6.000 s concat close hold (same benign behavior as v1).
- Encoded-frame QA: corrected card decodes cleanly; full contact sheet in `contact-sheet.jpg`.

## Gates untouched

No TTS, no Git, no upload/publication, no shared-tool or public-asset writes. Sibling-lane
rendering unaffected; this is the same lane and scope as the v1 First Task.
