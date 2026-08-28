# REPAIR BRIEF — V22. A false count five drafts old, and a prerequisite that must become receiptable.

Base: `../PREREG_SUCCESSOR_DRAFT_V21_20260827.md`, sha256
`8386d5f0b3cdc8ed4161545dbcf2f8e4898c9c68942ddfc117b3103ef6ea10e5`. **Verify before starting.**
Read `V21_WHOLE_REVIEW_GPT56.md` and `V21_WHOLE_REVIEW_CODEX.md` in full first.

**Write `../PREREG_SUCCESSOR_DRAFT_V22_20260827.md`.** Do not edit V21. **Do not touch V15–V20.**

## Blocker 1 — the class-E count is wrong, and has been since V17

§7's prose says **"There are 8 class-E slots."** The table holds **7**. Verify this yourself by
counting rows under `**Class E`.

**This is not V21's defect. It is five drafts old:**

    V16   prose 7   table 7   correct
    V17   prose 8   table 7   regression introduced here
    V18   prose 8   table 7   inherited
    V19   prose 8   table 7   inherited
    V20   prose 8   table 7   inherited
    V21   prose 8   table 7   inherited

**Repair:** change the prose to **7 class-E slots**, matching the table. Confirm the class-P count of
fourteen is correct against the table before leaving it alone.

## Blocker 2 — the repair trace records the regression as a repair

V20's §10 trace row reads *"Repaired the Class E count in §7 from 7 to 8; the already-correct Class P
count remained 14."* The **class-P half is correct** — no class-P repair ever happened, and saying so
was right. The **class-E half describes the introduction of the error as its repair.**

**Repair:** rewrite that row to state plainly that **V17 changed the class-E prose from 7 to 8 while
the table held 7, introducing a count error that V18–V21 inherited, and V22 corrects the prose to 7.**
Do not soften it. The trace is the document's own account of its history and this is the second time
tonight a trace row has misdescribed its own change.

## Blocker 3 — the `VOID` pre-BS-6 dependency is not receiptable (both seats)

Both seats accept that placing the dependency was right, and both find it **not yet enforceable**:

- **It is not specified as a receiptable slot.** A prerequisite nothing can produce a receipt against
  is a sentence, not a gate. Give it a slot with a producer, inputs, schema and what it blocks — the
  same shape as every other §7 row.
- **"Branch-complete fixtures" is not defined tightly enough for a gate to fail an incomplete one.**
  State what "branch-complete" means: which enumerated void antecedents the fixture set must cover,
  and what a gate compares to decide the set is complete. If that cannot be specified without the
  converter existing, say so and mark it unresolved rather than leaving the phrase to be interpreted
  at gate time.

## Blocker 4 — the unresolved implementation inventory still omits an item (GPT56 3)

§5 lines 462–474 and §11 lines 824–833. You added two items last round after CODEX found them
missing; GPT56 now finds another. **Read its finding and add what it names.** Then walk §5 and §11
against each other and confirm nothing else is missing — this is the third round in which the
"complete" list was incomplete.

## Also

Add the **V21→V22** trace entry. Re-run the neighbour check: read the sentences either side of every
change you make.

## A standing instruction from this round

**When a finding says a value was changed, check whether the new value is correct** — not merely that
the change occurred. The class-E error survived five drafts and two referee reviews because everyone
verified the edit had happened and nobody counted the rows.

## Standing state

Findings 1, 2, 2b and 3 **UNRESOLVED**; **BS-2a REFUSED**; rows C2 and E cannot run; **BS-6 and the
first image byte blocked** for two separately named reasons.

## Deliverable

`../PREREG_SUCCESSOR_DRAFT_V22_20260827.md`, complete, single write, titled **V22**.

Do not read `/Users/duhokim/NebulaMindData/`. Nothing is authorised to fetch. No deadline.
