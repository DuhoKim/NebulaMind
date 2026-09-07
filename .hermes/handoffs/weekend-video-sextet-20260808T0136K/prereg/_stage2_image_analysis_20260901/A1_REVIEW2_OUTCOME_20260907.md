# A1 — FINAL INDEPENDENT PASS: **VERDICT: REVIEWABLE-AND-SOUND** (2026-09-07 14:32 KST)
Reviewer **agy / Gemini**, wrapper pid 38415, ACCESS PROVEN for the final bytes `61e253cef941de58…`. **Exit artefacts read before the report counted**: stderr 0 bytes, stdout 4,653 bytes, rc 0 — a completed seat, not a timeout. Same reviewer as the first pass, which REFUSED this proposal; still not the author of any change (all changes were written by Codex workers). Report retained as `AGY_A1_REVIEW2_20260907.md`.

| its own earlier finding | now |
|---|---|
| FATAL 1–2, unwitnessed clock / ten minutes insufficient | **CLOSED** — the anchor is third-party and strictly precedes the round being named, so the clock cannot be backdated and the seed is unknowable when the inputs lock |
| best-of-many via a locally-held attempts register (found by MY sweep, not its review) | **CLOSED** — an attempt anchored before first holdout access leaves a visible gap if abandoned |
| deferring the control gates and `verify_split` | **JUSTIFIED** — anchored inputs + anchored code + anchored seed make the split deterministic, so an outsider's honestly derived id hashes would not match manipulated ones |
| MAJOR: clause disposition / T_sign | resolved by the anchor replacing the removed NIST clock |
| MAJOR: the ledger's separate listing of two losses | resolved by the compounded-loss entry and the pairwise sweep |
| MAJOR: selection code | **VERIFIED IN THE CODE**: exact sizes or `ValueError`; no reference to the floors remains |
| its own Q3 answer (`/2000`, unscored as misses) | **THE REVIEWER OVERTURNED ITSELF.** It read `miniprereg_pins/validation_gate.py` lines 67–75, found `m = n − r` with `wilson_lower(…, m)`, and states: "The lane owner is exactly right, and my first review's claim was wrong." |
| two-stage freeze, manifest placeholders, adoption clause, regressions | sound; no invented digest; the clause marks itself unadopted on its face |

## WHAT THIS IS AND IS NOT
**IS**: a prepared amendment whose changed bytes have passed one independent review by a non-authoring, different-engine seat, with every earlier finding dispositioned and the two FATALs closed.
**IS NOT**: adopted. Duho has made no decision. Two manifest entries are still NAMED PLACEHOLDERS — the eligible-id file and the derived failed-set file — and both must be produced and pinned to REAL digests **before** the input freeze is anchored. No draw, split or holdout has occurred or is permitted; the unseen evaluation data remain UNOPENED; drand-only stands; round 6440756 cannot seed this run.

## WHAT REMAINS, AND WHO ACTS
1. **Duho** — decide on the amendment (the one-page sheet is the document for that; A1 carries the digest he would state).
2. **The lane owner (me)** — produce the eligible-id file and the derived failed-set file, pin their real digests, then anchor the input freeze.
3. **Nobody** — until 1 and 2, nothing else proceeds.
