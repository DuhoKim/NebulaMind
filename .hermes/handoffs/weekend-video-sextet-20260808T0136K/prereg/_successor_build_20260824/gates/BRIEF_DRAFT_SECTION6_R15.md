# DRAFTING BRIEF — R15. Part 2 shrank while §6 grew. Restore it, completely, once.

Subject: `SECTION6_DRAFT_AGY_R14.md`, sha256
`d151824355006d9e97f17f465d4321d19f3b478f239d5432fc85d0997245d5e9`.
Read `SECTION6_REVIEW_R14_GPT56.md` and `SECTION6_REVIEW_R14_CODEX.md` in full first.

## What is settled — do not touch any of it

**Both seats adjudicated route (b) as correct and route (a) as not better.** GPT56: route (b)
"avoids trusting a producer-authored PASS field and lets the independent lock verifier recompute the
predicate from authenticated BS-8f bytes… It becomes fully specified once Finding 1's BS-L/slot-schema
seam is added to Part 2."

The §6 body is done. The partition, the seating, the thresholds, the ten clauses, the twenty rows,
the Row-J calibration guard, the `verify_lock()` route — **all credited by both seats. Change none of
it.** This pass edits **Part 2 only**.

## The defect, and its cause

Part 2 asserts it lists **every** conforming edit outside §6. It does not — and R14's three additions
did not close it, because **the list has been shrinking across rounds while §6 grew**.

CODEX establishes this directly: items that were **explicit in `SECTION6_DRAFT_AGY_R5.md` Part 2
lines 187–192 have disappeared** from the list now claiming completeness. This is not an omission you
need to re-derive from scratch. **Open R5's Part 2 and recover what was lost**, then add what is new.

## The complete set of missing items, from both seats

**A. `SLOT_SCHEMA` entries** (GPT56 finding 1; CODEX second bullet). §6.1 line 21 calls BS-2a, BS-2k
and BS-L slot receipts "under the pinned `SLOT_SCHEMA` as conformed by this revision's code items,"
but the pinned `SLOT_SCHEMA` (`../ref/successor_ref_v9.py` lines 185–205) **has no entry for any of
the three** — GPT56 confirmed by programmatic set comparison. Add one explicit Part 2 code-side item
requiring exact pinned `SLOT_SCHEMA` entries and canonical receipt fields for **BS-L and BS-2k**, and
naming the **BS-2a schema addition as required work deferred with the already-refused BS-2a design**.
Bind those schema bytes into the implementation/schema digest item 7 already requires. **Do not change
BS-5f** — route (b) stands.

**B. §7 count and DESIGN inventory** (CODEX, first bullet; and this was in R5 Part 2 line 187). V15
§7 lines 595–600 still says "One of twelve class-P slots is filled" and lists BS-2f, BS-5p, BS-8p,
BS-9 as DESIGN slots. CODEX independently parsed the tables: **14 class-P and 6 class-E now**, and
applying items 5–6 yields **14 class-P and 7 class-E**. The prose would still say twelve, would omit
DESIGN slots BS-2a and BS-2k, and would retain BS-2f despite V15 lines 341–342 and 624 calling it
value-only. Add the count/inventory replacement **and the lint assertion** that prose count equals
parsed table count.

**C. §5 guard seam** (CODEX, third bullet). Item 3 adds adequacy-receipt and final-mask verification
but does not conform §5 and the pinned production symbol to **require and verify the canonical BS-L
artifact and the one-use unblinding receipt** that Row P and Clause 3 make mandatory. A literal
application leaves §5's declared guard surface incomplete.

**D. The remaining literal seams** (CODEX, fourth bullet). §2.5's producer-checksum narrowing to
source images; the **§10 repair-trace edit** that Clause 10 and V15 §6.3/§10 require; and the code
items that were in R5 and are now absent — `verify_unblinding_receipt`, `verify_archive_seal`, the
opening-authorization / replay verifier, `recompute_acceptance_ledger`, the enforceable-mediation gate
checks, and the general `SLOT_SCHEMA` update.

## How to do this so it does not recur

**Derive the list, do not recall it.** Walk your own Part 1 top to bottom — every row, every clause,
every sentence in §6.1's closed list — and for each thing it requires outside §6, write the edit
down. GPT56 did exactly this walk and produced eight items; seven were listed and one was not. Do the
walk yourself and **state in Part 2 that it was derived by walking Part 1**, so the next reader knows
what kind of list it is.

Then state plainly, in Part 2, that **implementation is not claimed** — every code item is required
work, marked UNRESOLVED alongside findings 1, 2, 2b and 3, pending the refused BS-2a design.

## Not in scope

The §6 body. The attrition-intolerance design question, which is with the principal. Writing any
code. Do not weaken the fail-closed calibration rule.

## Deliverable

`SECTION6_DRAFT_AGY_R15.md` — complete, self-contained, five parts, single write.

Do not modify the preregistration. Do not read `/Users/duhokim/NebulaMindData/`. Nothing is
authorised to fetch. No deadline.

**A list that says "this is everything" and is missing one item is the same defect as one missing
six.** This is the fourth round in which a completeness claim has been the blocker. Close it by
construction — by walking the section — not by adding the items you were just told about.
