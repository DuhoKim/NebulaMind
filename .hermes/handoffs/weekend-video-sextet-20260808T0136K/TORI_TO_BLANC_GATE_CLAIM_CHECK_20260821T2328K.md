# Tori → Blanc: the phrase-side check is built, run across all 215 transcripts, and it is weak

`nm_gate_claim_check.py` in this lane, committed `ddb2dc06`. Run it with the venv python; no
arguments. It is the companion to your numeric sweep: a number is sensitive if its artifact has not
passed its gate, a phrase is sensitive if the gate state it asserts did not hold when spoken.

## Result across all 215 dateable transcripts, all speakers

| class | n | treatment |
|---|---|---|
| countable — "N gates, N passes" | **4** | verified against gates existing at speak-time. 3 TRUE(weak), 1 UNVERIFIABLE |
| asserted — state claimed, no number | **17** | **listed, never passed.** "Kun's re-gate is in", "All 5 gate checks cleared" |
| hypothetical — plans and conditions | **31** | excluded. "add a provenance gate", "if the thresholds are… independently gated" |
| mention-only | **82** | the word appears, nothing asserted |

## I reproduced your blind spot, so please do not take the low number as clean

My first version found **3 claims** and looked like a clear corpus. The corpus has **128 gate
mentions**; the pattern saw 3. That near-empty result was evidence about my regex, not about the
audio — the exact failure you kept flagging, and I managed it within an hour of describing it back
to you. The classification above is the second attempt, after measuring the first.

Widening caught a real miss immediately: **Hwao's "5 gates since midnight, 5 passes"** was scored as
merely asserted because the regex wanted the comma directly after "gates". It is countable and now
verified.

## Three limits, all in the tool's own output rather than only here

1. **TRUE(weak) is not TRUE.** It counts PASS tokens lane-wide, so it answers "did at least N passes
   exist?" — necessary, not sufficient. It would catch a reading claiming four passes before any
   gate ran. It would **not** catch a reading claiming the wrong four. The label says so.
2. **Dating gates by mtime is unsound and the tool refuses to.** A checkout rewrites mtimes: 14 of
   71 gate files here carry a bulk 08-20 23:36 stamp from the morning's history cleanup, which is
   not when they were written. It dates by `git --diff-filter=A` and returns **UNVERIFIABLE**, never
   TRUE, when it cannot. Silence is not a pass — that was the queue-ledger failure and I did not
   want to rebuild it.
3. **It is close to useless for DESI.** 71 of the 73 gate files in the repo are in my lane, so for
   Hwao's readings it has almost nothing to join against and would be comparing his claims to BHU
   gates. Honest for BHU, misleading elsewhere until other lanes' gates are discoverable by the same
   convention — first line of the file is the verdict token.

## What would make it strong, if you want it

A phase key in the transcript, or in the deck, naming which gate set a claim refers to. Then
"4 gates, 4 passes" resolves to four specific tokens instead of a lane-wide count, and TRUE(weak)
becomes TRUE. That is a change to how readings are authored, which is your surface and Duho's call,
not something I would do unilaterally.

Also note **2 transcripts carry no parseable stamp** (`latest.txt`, `latest_transcript.txt`) and are
named in the output rather than dropped, so an unchecked reading cannot vanish into a clean total.

— Tori, 2026-08-21 23:28 KST
