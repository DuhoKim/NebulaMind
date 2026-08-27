# CUSTODY NOTE — the R10B dispatch record attested a digest the seat had not finished writing

**2026-08-27, ~20:55 KST. Raised by Blanc on Duho's instruction; verified here from the artifacts.**

## The two digests are not two drafts

    4e36683e33cb8c69d13583b6d4bd271c3b0b78a06c7463f5d57b32d5112f263f  SECTION6_DRAFT_AGY_R10.md
    ef35a8b1aad1b023ded0cb42b3632dfa1d14036d65b6bca788c8c772def88383  SECTION6_DRAFT_AGY_R10B.md

The digest my log pinned, `4e36683e`, **is R10's content.** The agy seat created R10B by copying R10
and then editing it in place. My dispatcher hashed the file during that window, so it recorded R10's
bytes under R10B's name — which is also why the same log says "changed lines R10 -> R10B: 0". The
self-contradiction Blanc identified is a single fact stated twice.

**There is no ambiguity about which bytes were meant.** `ef35a8b1` is the finished R10B and is the
artifact of record. `4e36683e` is not a discarded draft of R10B; it is R10, which exists under its own
name and is unaffected. Nothing needs discarding.

## What was actually refereed — and why the content findings stand

Both referees recorded the digest of what they opened. GPT56 printed `ef35a8b1…` in its finding and
compared it against the `4e36683e…` in my log; CODEX did the same. Between them the finished digest
appears four times across the two reports.

**So the reviewed bytes are knowable, and they were the correct ones.** This was not a review of
unknown bytes. It was a correct review of the right artifact under a dispatch record that attested
the wrong digest — a record failure, not an identity failure. That distinction matters for what
survives: **both seats' substantive findings are about `ef35a8b1` and remain valid.** Their first
blocker is against my record-keeping, and it is upheld.

Also not in question, and not to be redone: **both seats independently confirmed the
power-inapplicability repair is substantively correct against the pinned code.**

## Root cause

Two defects in my dispatcher, compounding:

1. **It treated "file exists and is non-empty" as "the seat has finished writing."** It then slept 40
   seconds and hashed. The seat was still editing.
2. **The confinement gate was wrong-signed.** It aborted above 30 changed lines and said nothing
   about zero. A pass that appeared to change nothing sailed through the guard whose entire purpose
   was to catch a pass that did nothing.

## Fix, applied from R11 onward

- **Hash only after the seat process has exited.** No hashing a file that something else holds open.
- **Require the digest to be stable across two reads five seconds apart**, and abort if it moves.
- **Abort on a zero-line diff** as well as an oversized one. A repair pass that produces a
  byte-identical file is a failed pass, not a clean one.

## Why this is worth a note rather than a fix in silence

Blanc records this as the second instance today, after the PHASE5B_FREEZE pin mismatch on the Tori
lane at 19:42 KST — a record pointing at bytes that no longer exist.

It happened during round ten of hardening a section about custody and access control. The document
now requires that no artifact judging the manifest be nominated by its presenter, that verification
bind the bytes rather than re-resolve filenames, and that every branch terminate in one stated
outcome. My own dispatch process met none of that standard while enforcing it on the text.

**A hash taken from a file another process is still writing certifies nothing.** That is the same
failure the closure mechanism spent five rounds removing from the code, arriving in the harness that
carries it.
