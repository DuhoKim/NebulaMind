# DESIGNATION STOPPED — two concrete conflicts, no round collected (2026-09-07 20:06:39 KST)
**No beacon was collected. 6444945 was NOT used. 6444942 was NOT collected.** No protected data touched, no seed obtained.

## FIRST, MY OWN ERROR, PRESERVED NOT DELETED
`INPUT_ANCHOR_RECORD_20260907.md` declared **round 6444945 at 11:09:30Z** using a "later of the two timestamps" base. **That rule is mine, not A1's.** The adopted formula, implemented in the reviewed `run_path.designate()`, is `r = 1 + ceil((A + 600 − GENESIS) / PERIOD)` on the anchor's `third_party_utc`. With the real GitHub anchor A = `2026-09-07T10:57:47Z` it gives **6444942 at 11:08:00Z**. I substituted my own judgement — "more conservative" — for an adopted, reviewed rule. Being stricter is still a deviation, and an unreviewed one. **That declaration is SUPERSEDED and stays on the record**; nothing about it is deleted.

## WHY THE CONFORMING DESIGNATION ALSO COULD NOT COMPLETE
I ran the tested gate rather than writing another prose designation. It refused, twice over, for reasons that are correct:
**(a) `MISSING-CORE-ENTRY`** — importing the run path in a fresh process caused macOS to write a bytecode cache for `_optionA_dev/agreement_run/bytecode_correspondence.py` that CORE does not register. Under the correspondence rule adopted this evening, an unregistered loadable artefact must refuse. Registering it is legitimate — **but that changes CORE's digest.**
**(b) `ANCHOR-DIGEST`** — the tested gate requires `anchor.published_sha256 == C.sha256` where **C is the CORE INPUT MANIFEST** (`e9222abf13485a36…`). The anchor Codex actually published binds the **input-freeze record** (`bbc08cd696150f9a…`). **The published anchor therefore does not bind the artefact the adopted code checks.** This is not a wording quibble: the anchor's whole purpose is to fix, in third-party time, the exact object the run path will consume.
Either fix invalidates the current anchor — (a) changes CORE's digest, and (b) requires anchoring a different digest — and round 6444942 was 2 minutes away. **I did not race it, and I did not weaken either check to fit the window.**

## WHAT IS NEEDED, EXACTLY
1. Register the new bytecode artefact in CORE under the existing correspondence rule (code equality verified), yielding a new CORE digest.
2. Re-issue the input freeze so C references that CORE, and **publish an anchor that binds the CORE manifest digest** — the artefact `designate()` actually checks — with the input-freeze digest carried alongside it.
3. Then run `designate()` against the fresh anchor while its computed round is still future, and proceed to collection.
**No alternative seed is being chosen, no attempt is being reset, and no completed valid designation exists to alter.** There is no valid designation on record — only my superseded prose note.
