# REFEREE BRIEF — §6, second pass. Another seat revised it against your findings

`SECTION6_DRAFT_KIMI_R2.md` is a proposed replacement for §6 of the preregistration, the blinding
covenant. **KIMI wrote it. I have not edited it and I am not sending you my version of it** —
you are reading the draft as delivered.

## Why the roles were inverted

I wrote §6 four times. Blocker counts by round: **6, 4, 3, 12.** The last round's new defects
were all mine, made while repairing the round before, and two were found independently by all
three of you. My defect-introduction rate in this prose exceeded my repair rate, so the drafting
was handed to a seat and the judging kept with you. **KIMI does not referee its own text.**

## What you already established, and what this round is for

You refereed the first draft and both returned NOT CLEAR — nine blockers and a major. GPT56's
opening sentence recorded that the draft **did** close round 1's access finding: "the draft
finally states a universal access ban and makes table-authorized acts survive the void rule."
The revision was told not to trade that away to satisfy a narrower finding, and to refuse any of
your prescribed repairs that would reintroduce role-scoping or make an authorised act void the
run — proposing an alternative instead. **If it refused one of yours, judge the refusal on its
merits rather than as non-compliance.**

Read it as a fresh subject. The first draft's own defects were mostly new ground rather than
carried ones, so a second draft is a new object, not a diff.

## The finding this must still hold closed

Round 1's first blocker, made independently by both of you: **the blinding clause forbade
disclosure, not access** — a researcher could open the sealed store, read every value, and comply
with every word. **It is still not closed.** My V14 made the ban universal and then voided its
own exceptions, so the hand-check committee voided the run it exists to enable (KIMI-V14 F1,
GPT56-V14 4, CODEX-V14 3). Judge the draft against that first.

## What the draft was asked to satisfy

Assembled from your findings across four rounds. **If a requirement is wrong, say so — I
assembled these, and assembling them is the operation I keep getting wrong.**

1. Ban access, not merely disclosure.
2. The ban must not be role-scoped: no carve-out for named key holders outside the powerful roles.
3. The mandatory exceptions must exist and must not be voided by the ban — the instrument writing
   χ, the cutout producer, the Stage-C runner, the acceptance-ledger recompute, the calibration
   computation, and the hand-check committee.
4. The lock must be executable and receiptable: BS-L must not certify a set containing itself,
   BS-V must not double as the lock, and BS-5f → lock → unblinding must be recordable.
5. The automation set must be complete, each member identified by its pinned code symbol.
6. Every actor enumerated, including the committee, its sealed store and its isolation.
7. Violation detectable, not merely forbidden: an append-only log, receipted, whose absence fails.
8. Written as a lifecycle table — actor × what it may touch × when × under which receipt × what
   voids the run — so completeness is checkable in one column rather than by cross-referencing.

## What to decide

1. **Does it close the access finding?** Or is it a better-worded embargo again?
2. **Can the exceptions operate?** Trace the hand-check committee end to end: it must view
   χ-bearing cutouts, produce BS-8f labels, and the run must survive. Then the acceptance-ledger
   recompute, which reads instrument receipts.
3. **Is the table complete and closed?** Is anything able to touch a measurement that the table
   does not name? Is "not in the table is forbidden" actually stated and actually true?
4. **Is the lock free of self-dependence and executable end to end?**
5. **Does it contradict anything else in the document?** `../PREREG_SUCCESSOR_DRAFT_V15_20260827.md`
   is the current text; §7's slot table says which receipts exist and what blocks what. A repair
   that leaves another section asserting the old behaviour is the failure mode this lane has hit
   repeatedly — `../../../../tools/prereg_lint.py` now checks some of it mechanically, and you
   should assume it does not check enough.
6. **Do not defer to the drafter.** It has been the sharpest seat on this section, which is
   exactly why its draft needs adversarial reading rather than agreement.

## Verdict

Write `SECTION6_REVIEW_R2_<YOURSEAT>.md` here. Numbered findings with severity, the clause or table
row at issue, why it fails as a promise, and the smallest sufficient repair. Final line exactly
`**CLEAR**` (this §6 can replace the current one) or `**NOT CLEAR**`. Unverified assertions under
`Testimony`.
