# REFEREE BRIEF — V23, whole document. Eighth assembled round.

Subject: **`../PREREG_SUCCESSOR_DRAFT_V23_20260827.md`**. Its sha256 is pinned in
`runner_v23_chain.log` after the drafting seat exited. **Verify it, and state what you compared.**

## The coordinator introduced an error and this round undoes it

CODEX was right: §7's class-E table has **8** data rows and always has — the eighth is
`| Unblinding receipt | Unsealing service | … |`, whose first cell is a phrase rather than a `BS-`
identifier. **V17's 7→8 prose edit was correct. V16's 7 was the error. V22's 8→7 edit — made on my
instruction — introduced the mismatch you found.**

My linter keyed rows by identifier and never saw that row; my cross-check used the same pattern, so
it confirmed nothing. **Two checks that agree because they share an assumption are one check.** The
tool now counts data rows and prints both numbers so the gap is visible. It immediately found a
second undercount the old matcher hid — V21's class-P prose said 14 over 15 rows, which is the count
error GPT56 reported and V22 fixed correctly by assigning `BS-2v`.

**Count both classes yourself. Do not accept 15 and 8 from me.** That instruction is not ceremonial:
accepting my number is exactly what produced this.

## What V23 changes

1. **Class-E prose restored to 8**; class-P stays 15.
2. **Both inaccurate trace rows corrected** — the V16→V17 row no longer accuses V17 of introducing an
   error it fixed, and the V21→V22 row no longer claims the count was corrected "to match the table"
   or that `BS-2v` became enforceable. The trace now records that **V22 introduced the mismatch on a
   wrong coordinator instruction.** Check that it says so plainly.
3. **`BS-2v` gets an independent canonical antecedent registry** — stable IDs, one row per antecedent
   with source clause, phase and failure effect — with converter IDs and exercised fixture IDs each
   required to **equal that normative set**, which the converter does not author.
4. **`BS-2v` added to §6.1's exhaustive non-χ-bearing slot-receipt list and §11's `SLOT_SCHEMA`
   additions**, with authenticated fields specified. Without this it was not lawfully inspectable by
   any gate under the document's own default rule.

## What to judge

1. **Digest first**, with the comparison stated.
2. **Count both classes of §7 data row yourself**, including rows whose first cell is not a `BS-` ID.
3. **Is the registry genuinely independent?** Can a gate decide coverage using a set the converter
   does not produce? GPT56 called the previous test self-referential; check the new one is not.
4. **Is `BS-2v` now lawfully inspectable** under §6.1's closed list, with enough schema to fail a
   non-conforming receipt?
5. **Are all seven trace entries accurate?** CODEX diffed all six transitions last round and
   recomputed every predecessor digest pin — all matched. **Do that again for V22→V23**, and confirm
   the two corrected rows are now true.
6. **Clause 10 across §§0–11, both directions**, still expected unresolved at `VOID`.
7. **Every threshold: value, phase, failure effect.** **Read the neighbours** of every change.

## Standing state

Findings 1, 2, 2b and 3 **UNRESOLVED**; **BS-2a REFUSED**; rows C2 and E cannot run; **BS-6 and the
first image byte blocked**, including on unfilled `BS-2v`.

Do not read `/Users/duhokim/NebulaMindData/`. Nothing is authorised to fetch. No deadline.

## Verdict

`V23_WHOLE_REVIEW_<YOURSEAT>.md`. Numbered findings with severity, section and line, why it fails,
smallest sufficient repair. Unverified assertions under `Testimony`. Final line exactly `**CLEAR**`
or `**NOT CLEAR**`.

**Judge independently; do not converge.** If V23 is a correct preregistration honest about being an
unfinished programme, say so in those words.
