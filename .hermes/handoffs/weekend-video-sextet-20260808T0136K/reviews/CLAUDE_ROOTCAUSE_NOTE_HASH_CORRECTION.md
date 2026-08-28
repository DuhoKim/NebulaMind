# Note to Hwao — the stale-hash root cause was supersession, not a mid-write read

Filed 2026-08-09 13:08 KST by the **Claude-macbook** seat (Directors board, pane %30), on Duho's
direct instruction in that pane: *"tell hwao the root cause was staleness, not mid-write."*

Re: `reviews/HWAO_HASH_CORRECTION_20260809.md`.

**Your correction and your fix are both right.** `d940a7e8…` was the wrong hash to dispatch,
`0496435a…` is correct, and cross-checking each lane's own `POST_ENCODE_FREEZE.json` is the right
remedy. Only the *cause* is misdiagnosed, and it changes what the standing lesson should say.

## `d940a7e8…` was a complete artifact, not a partial write

From `encoded_qa.HOLD1.json`, which records that exact hash:

- probe: **9,192,680 bytes, full duration 224.233333 s**
- **27 OCR frames** swept at 2 fps
- motion measured: longest near-unchanged run **13.5 s**
- **25 of 27** checks executed, returning a substantive `HOLD`

A partially-written MP4 cannot full-decode, cannot yield a 2 fps OCR sweep across its runtime, and
cannot produce motion statistics. The integrator also preserved it as a finished attempt at
`rejected-attempts/d940a7e8-freeze-hold/`.

## What actually happened

`d940a7e8…` was the **first complete encode**. It failed `no_eight_second_freeze` at 13.5 s. The
integrator then re-rendered, producing `0496435a…` at **02:26:40**, and the lane's freeze recorded
that at 02:27:20.

Your watcher read the first encode **correctly**. It then never re-read after the rebuild. The hash
went stale because the artifact was superseded, not because it was caught half-written.

Independent corroboration from this seat's own timeline: my waiter reported `d940a7e8…` at
**02:22:36** when it was the current artifact, the QA ran on it at 02:22:47, and I reported
`0496435a…` after the 02:26:40 re-render. Both reads were accurate at the time they were taken.

## Why the distinction matters

The lesson as written — *"a size-stability check can pass mid-write"* — points at wait duration.
**A longer wait would not have prevented this.** The first encode was finished and stable; waiting
another minute would have returned the same hash. Only re-reading after the re-render would have
caught it.

The accurate lesson is narrower and more useful: **a hash is a claim about a moment, not about a
candidate.** Any hash held across a rebuild is stale by default. That is why your fix works —
`POST_ENCODE_FREEZE.json` is re-written on every rebuild, so comparing against it re-reads by
construction, whereas a watcher variable does not.

Worth noting the two seats that avoided this did the same thing independently: Lana hashed 62
governing inputs at audit start and rehashed all 62 before writing; Goru took tree digests at open
and replayed them at close. Both bracket their work rather than trusting a single earlier read.

## Not disputed

Kun was right to refuse the lane and mark his section diagnostic-only. Goru's `mzr-census` section
still needs re-stamping. Nothing here touches any candidate, verdict, or gate; this note is
read-only and changes no artifact.
