# REPAIR BRIEF — V23. Undo an error I introduced, and make BS-2v actually gateable.

Base: `../PREREG_SUCCESSOR_DRAFT_V22_20260827.md`, sha256
`9b09416685e966cc9ffbbca12f5e67e94d853c69b0da552b380f2bd54be2a8f3`. **Verify before starting.**
Read `V22_WHOLE_REVIEW_GPT56.md` and `V22_WHOLE_REVIEW_CODEX.md` in full first.

**Write `../PREREG_SUCCESSOR_DRAFT_V23_20260827.md`.** Do not edit V22. **Do not touch V15–V21.**

## Blocker 1 — the class-E count. The error is mine, not yours.

**§7's class-E table has 8 data rows and always has.** The eighth is
`| Unblinding receipt | Unsealing service | … |` — a row whose first cell is a phrase, not a `BS-`
identifier. **Count the rows yourself and confirm 8 before writing anything.**

I instructed the V22 pass to change the prose from 8 to 7. That instruction was wrong. My linter keys
rows by identifier and never saw the `Unblinding receipt` row, so it reported 7; my cross-check used
the same pattern and so confirmed nothing. **You executed a correct instruction badly stated. The
defect is mine.**

**Repair:** restore the class-E prose to **8**. Leave class-P at **15** — that count is correct, and
V22 fixed it properly by giving the `VOID` converter the ID `BS-2v`.

## Blocker 2 — two trace rows are materially inaccurate, and I caused both

CODEX diffed all six transitions and recomputed every predecessor digest pin; four entries agree with
their diffs. These two do not:

1. **V16→V17 (line 780)** says V17 changed class-E prose from 7 to 8 "while the table held 7,"
   introducing an error. **False.** The table held **8** in both V16 and V17. **V17's edit was
   correct** — it made the prose match the table. **V16's 7 was the error.**
2. **V21→V22 (lines 820–821)** says the class-E count was corrected "to match the table" and that
   `BS-2v` was upgraded to an enforceable gate. **Neither is true**: the table has 8, and blockers 3
   and 4 below show the gate is not yet enforceable.

**Repair — write the truth in both rows:** V16's class-E prose of 7 was wrong; **V17 corrected it to
8**; V18–V21 carried 8 correctly; **V22 changed it to 7 and introduced the present mismatch, on a
wrong instruction from the coordinator**; V23 restores 8. And state that `BS-2v` was **given a slot ID
and a stated intent, not yet an enforceable gate.**

Do not soften either. This is the third and fourth trace row tonight to misdescribe its own change,
and a repair trace that flatters the repairs is worth less than none.

## Blocker 3 — BS-2v's set equality has no independent reference set (both seats)

The coverage test compares the converter against itself. GPT56 calls it self-referential; CODEX says
it establishes implementation/fixture agreement, not coverage of the preregistration's complete
`VOID` antecedent universe.

**Repair:** put the **canonical stable-ID antecedent registry into the preregistration** — or pin a
separately gated immutable registry by digest — with **one row per antecedent**, each carrying its
**exact source row or clause, phase, and failure effect**. Then require **independently**:
1. converter IDs **equal** normative registry IDs;
2. exercised fixture IDs **equal** normative registry IDs.

Equality against a set the converter does not author is what makes this a gate.

## Blocker 4 — BS-2v is not receiptable under §6.1's own closed list (CODEX 3)

§6.1 declares its non-χ-bearing receipt list closed and exhaustive, and the slot-receipt list at line
505 **omits BS-2v** — so by the document's own default rule, BS-2v's receipt is χ-bearing and cannot
lawfully be inspected by a gate.

**Repair:** add **BS-2v** to the exhaustive non-χ-bearing slot-receipt list **and** to §11's exact
`SLOT_SCHEMA` additions, specifying authenticated fields: document/registry digest, converter
implementation digest, ordered normative IDs, exercised IDs, uniqueness and count closure, per-ID
source/phase/failure-effect, and result classification.

## Also

Add the **V22→V23** trace entry. Read the neighbours of every change. Re-count both classes after any
row edit.

## Standing state

Findings 1, 2, 2b and 3 **UNRESOLVED**; **BS-2a REFUSED**; rows C2 and E cannot run; **BS-6 and the
first image byte blocked**, including on unfilled `BS-2v`.

## Deliverable

`../PREREG_SUCCESSOR_DRAFT_V23_20260827.md`, complete, single write, titled **V23**.

Do not read `/Users/duhokim/NebulaMindData/`. Nothing is authorised to fetch. No deadline.
