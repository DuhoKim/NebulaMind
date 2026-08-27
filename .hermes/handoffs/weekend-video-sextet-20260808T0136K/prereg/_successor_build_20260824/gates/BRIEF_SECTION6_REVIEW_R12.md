# REFEREE BRIEF — §6 twelfth pass. Reseated, partitioned, and the repair map corrected.

Subject: **`SECTION6_DRAFT_AGY_R12.md`**. Its sha256 is pinned in `runner_s6r12_round.log` **after
the drafting seat exited**, confirmed stable across two reads, with a post-review check that the
bytes did not move. **Verify the file you open matches that digest and record what you found.**

Your digest verification last round worked exactly as intended — both of you independently confirmed
`5daae51e…` and the post-check showed the subject unchanged throughout. Keep doing it.

## What R12 repairs, all three from your R11 reports

**1. The orphaned `VOID` branch is reseated at Row J** (CODEX 1, GPT56 1). R11 deleted the
protocol-deviation rule from Row P and Part 2 item 4 without putting it anywhere. Row J now verifies
`N_TRIALS = 1_000` and the frozen Stage-C implementation/protocol digest **before running or issuing
BS-5f**, with any deviation terminating `VOID`; BS-5f binds that verification; Row P stays limited to
binding the already-verified PASS and protocol digest. **No unreachable post-unblinding FAIL branch
has been restored to Row P.**

**2. The Stage-C FAIL partition is completed** (CODEX 2). You found that
`../ref/successor_ref_v9.py` lines 1275–1276 return `False` on any `refuted` or `nonconservative`
result regardless of passing-trial count, so a self-verification FAIL at ≥962 was unterminated. Row J
should now state that **any** locked Stage-C FAIL emits `INCONCLUSIVE-BY-POWER` and halts —
explicitly covering both the count threshold and the self-verification return — with the
complementary PASS branch as the sole route to BS-5f → BS-L. Part 3 C2 and Part 5 item 17 conformed.

**3. Part 5 items 8 and 16 rewritten** (CODEX 3, GPT56 2). They asserted Row P mechanisms the text no
longer has, both labelled `REPAIR`, so the document claimed two incompatible current mechanisms.

## What to judge

1. **Verify the digest first.** Record it. A mismatch is a finding and outranks content.
2. **Clause 10 in both directions, over the whole table.** R11 deleted a branch and orphaned another;
   R12 reseats one and adds a FAIL condition. Both operations can create new orphans. Every path
   reaches exactly one stated outcome; every stated outcome is reachable.
3. **Check the Row J seating actually executes there.** Is the protocol verification genuinely before
   BS-5f is issued, and does BS-5f bind it? A check placed after the artifact it should gate is the
   same defect in a new position.
4. **Read lines 1275–1276 and confirm the partition is complete** — not merely that two cases are now
   named, but that they exhaust the FAIL space.
5. **Whole-document consistency and a numeric sweep.** Part 5's repair map must describe the
   mechanisms the normative text actually contains. Four clean numeric sweeps do not retire the class.

## Not in scope

The attrition-intolerance design question is with the principal. Do not accept a draft that weakens
the fail-closed calibration rule. Findings 1, 2, 2b and 3 stay UNRESOLVED pending BS-2a; BS-2a is
REFUSED; rows C2 and E cannot run; BS-6 and the first image byte stay blocked.

Do not read `/Users/duhokim/NebulaMindData/`. Nothing is authorised to fetch. No deadline.

## Verdict

`SECTION6_REVIEW_R12_<YOURSEAT>.md`. Numbered findings with severity, row/clause, why it fails,
smallest sufficient repair. Unverified assertions under `Testimony`. Final line exactly `**CLEAR**`
or `**NOT CLEAR**`.

CODEX returned zero blocking last round. **If §6 is now sound as prose and the remainder is genuinely
the BS-2a mechanism, say so plainly** — that is the answer I will act on, and twelve rounds of
narrowing has to be allowed to end somewhere. But say it only if it is true; a thirteenth finding is
more use than a courtesy pass.
