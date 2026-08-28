# REPAIR BRIEF — V21. The inventory is true. The sentence three lines above it is not.

Base: `../PREREG_SUCCESSOR_DRAFT_V20_20260827.md`, sha256
`607df3dd5b022a299162dac501b9c5766dda87bac8b3ba1cea11a105efa00261`. **Verify before starting.**
Read `V20_WHOLE_REVIEW_GPT56.md` and `V20_WHOLE_REVIEW_CODEX.md` in full first.

**Write `../PREREG_SUCCESSOR_DRAFT_V21_20260827.md`.** Do not edit V20. **Do not touch V15–V19.**

## What worked — and it worked exactly where it was applied

**Both seats parsed the pinned source and confirmed line 473's capability inventory is TRUE.** CODEX
compared every return site in code lines 1591–1625 and the decision helper at 1561–1588 against your
sentence; GPT56 did the same by AST against source sha `6a9abbbd…`. **The subtraction repair is
correct and stays exactly as written.** Keep that sentence.

## Blocker 1 — the guard inventory three lines above is still present-tense and false

§5 lines **458–461** describe guards in the present tense as though implemented. They are not. The
repair you applied at 473 was not applied to its own neighbour.

**Repair (both seats agree):**
- At **line 461**, replace the present-tense statement with an **explicit required-but-unimplemented
  guard**.
- Add **BS-L verification** and **authenticated one-use unblinding-receipt verification** to line
  473's unresolved implementation list — CODEX found the unresolved list itself incomplete.
- **Keep the exact return-value sentence at 473 unchanged.**

This is the same defect in the adjacent sentence. **When you fix a present-tense overclaim, check its
neighbours in the same paragraph** — that is now three rounds in a row where a repair was correct and
local while an identical defect sat beside it.

## Blocker 2 — `VOID` is honestly non-executable, and clause 10 still cannot resolve it

Declaring `VOID` not yet executable was right. But reverse reachability now stops there, and the
document does not say so. Both seats converge on stating it rather than papering over it:

**Repair:**
- Add a **direct clause-10 status sentence**: *`VOID` reverse reachability is unresolved; therefore
  clause 10 is not yet executable, and **BS-6 and the first image byte remain blocked** until a pinned
  producer or conversion handles **every enumerated void antecedent**.*
- Add that **converter and its branch-complete fixtures to §11**, and make it a **pre-BS-6
  dependency** in §7.
- **Do not invent a producer name as if implemented.** Keep "not yet executable" until those bytes
  pass a gate.

Note what this does: it converts an unresolved clause-10 branch into **a named prerequisite for the
first image byte.** That is the honest structure — the study cannot start until the branch closes,
and the document now says which branch and why.

## Repair 3 — the V19→V20 trace overstates what the changed prose names (GPT56 LOW)

§10 lines 797–805, the aggregate-validation row. Correct it to what actually changed. **State what
you compared.**

Then add the **V20→V21** entry.

## Then audit your own result

Clause 10 across §§0–11, both directions — and expect it to be **explicitly unresolved at `VOID`**;
that is the intended state, not a failure. Every threshold: value, phase, failure effect. **And read
the neighbouring sentences of everything you change.**

## Standing state

Findings 1, 2, 2b and 3 **UNRESOLVED**; **BS-2a REFUSED**; rows C2 and E cannot run; **BS-6 and the
first image byte blocked** — now for a second, separately named reason.

## Deliverable

`../PREREG_SUCCESSOR_DRAFT_V21_20260827.md`, complete, single write, titled **V21**.

Do not read `/Users/duhokim/NebulaMindData/`. Nothing is authorised to fetch. No deadline.
