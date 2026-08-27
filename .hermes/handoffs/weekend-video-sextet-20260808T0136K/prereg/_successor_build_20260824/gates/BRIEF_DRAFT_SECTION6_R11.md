# DRAFTING BRIEF — R11. Delete the dead branch. Conform two passages. Nothing else.

Subject: `SECTION6_DRAFT_AGY_R10B.md`, sha256
`ef35a8b1aad1b023ded0cb42b3632dfa1d14036d65b6bca788c8c772def88383`.
Read `SECTION6_REVIEW_R10B_GPT56.md` and `SECTION6_REVIEW_R10B_CODEX.md` first.

**Your R10B power-inapplicability repair was judged substantively correct by both seats.** The VOID
split you wrote stands. So do all R10 repairs, the twenty rows, the ten clauses, and the thresholds.
Findings 1, 2, 2b and 3 stay UNRESOLVED pending BS-2a. **Do not reopen any of it.**

Note: both seats' first blocker was a dispatch-custody failure of mine — the send-time log pinned
the wrong digest because my script hashed your file while you were still writing it. That is fixed
and is not your defect.

## Defect 1 — the Stage-C power branch in Row P is unreachable. Delete it.

Both seats, independently, from the document's own structure:

- Row P is authorised only after unblinding and **requires a verified BS-L**.
- Clause 3(c): `verify_lock()` checks **BS-5f's PASS**. Clause 3(d) requires that verified lock on the
  only verdict path. Row J forbids continuing after a Stage-C FAIL.
- V15 lines 421–425 freeze Stage C **before** unblinding, and a FAIL emits `INCONCLUSIVE-BY-POWER`,
  halts the run, and prevents any real-sky statistic.

Therefore **a Row-P invocation can only ever inherit a locked Stage-C PASS.** It cannot lawfully
encounter a result below 962. Once R10 removed the post-attrition rerun, the third branch of Row P's
adequacy tree became dead code — and clause 10 forbids exactly that.

**Repair:**
- **Delete the Stage-C power branch from Row P's post-unblinding adequacy tree and from Part 2 item 4.**
- **Keep the `< 962/1,000 → INCONCLUSIVE-BY-POWER` decision where it executes: pre-unblinding, Row J /
  BS-5f.** It is not being removed from the study, only from the place it cannot run.
- The post-unblinding adequacy receipt may **bind the already-verified locked PASS and the protocol
  digest**, but must not branch on a FAIL that BS-L excludes.

This retires the branch I have had you rewrite three times. The correct answer was that it does not
belong in Row P at all — deletion, not another consequence.

## Defect 2 — two passages still assert the behaviour you removed

Row P, Part 2, R3 and Part 5 item 13 all correctly say any removal ends in
`INCONCLUSIVE-BY-CALIBRATION` with no Stage-C rerun. But:

- **Part 3 C1** still says the design relies on the post-unblinding confidence-cut consequence
  "recomputing power and potentially failing the verdict." Replace with the actual consequence: any
  post-unblinding removal emits `INCONCLUSIVE-BY-CALIBRATION` **without rerunning Stage C**.
- **Part 5 finding 5** still says the adequacy receipt binds a "re-evaluated Stage-C result." Replace
  with the **locked BS-5f Stage-C inputs/result**, wording that plainly means carried and bound, not
  recomputed.

These are assertions of old behaviour, not historical description. A repair in the row that leaves
Part 3 asserting the old rule is the failure this document keeps producing.

## Then check your own draft against clause 10

Before you finish, walk every row's consequence column and every clause and ask: does each path reach
exactly one stated outcome, and is each stated outcome reachable? **Both directions.** Two outcomes
for one branch is a defect; a branch no execution can reach is also a defect. That test has now
caught something in three consecutive rounds — run it on yourself before the referees do.

## Not in scope

The attrition-intolerance design question is with the principal. Do not weaken the fail-closed
calibration rule.

## Deliverable

`SECTION6_DRAFT_AGY_R11.md` — complete, self-contained, five parts, not a diff.
**Write it once, completely, before you stop.** Do not create the file and then continue editing it.

Do not modify the preregistration. Do not read `/Users/duhokim/NebulaMindData/`. Nothing is
authorised to fetch. No deadline.
