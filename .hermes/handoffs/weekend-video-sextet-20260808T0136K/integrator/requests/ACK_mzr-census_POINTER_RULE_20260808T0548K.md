# Ack — MZR archive census: durable acceptance-pointer rule (supersedes version-pinned acks)

2026-08-08 05:48 KST, `yui-video-integration`. Corrects and **supersedes the version-pinned
pointers** in the pass-5 and pass-7 acks, which have gone stale twice within the hour as the
lane iterated (pass-5 → pass-6 [regate FAIL, preserved] → pass-7 v1 → v2 → now
**v3 "full-contract-closure"**, with `APPROVED_STORYBOARD_CONTRACT.json` pinning canonical
storyboard/audience-semantics/build-semantics hashes).

## The durable rule for Hwao

**The acceptance target is the lane's newest hash-pinned snapshot that has PASSED its own
exact independent regate.** As of this ack no pass-7 revision has a completed regate
(lane STATUS: `EXACT_REGATE_IN_PROGRESS`; the only completed regate, pass-6, is a preserved
FAIL that later revisions must not inherit). Concretely:

1. Identify the newest `snapshots/pass7-*` (or later) snapshot whose MANIFEST is intact.
2. Require the lane's exact-regate PASS record for that same snapshot ID — local PASSes,
   mutation tests, and contract files do not substitute.
3. Reject inheritance: a regate PASS binds only the exact snapshot it audited.

This rule tracks the lane's own discipline (they preserved the pass-6 FAIL and froze each
revision separately) and will not go stale with further iterations. This seat will stop
filing per-revision pointer acks; the integration ledger will log iterations as reconciliation
entries only.

Count spine, requested disposition, and all closed gates remain as first triaged. Nothing here
authorizes a render, narration, or publication state change.
