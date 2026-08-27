# DRAFTING BRIEF — R12. Reseat what R11 orphaned, and complete the Stage-C partition.

Subject: `SECTION6_DRAFT_AGY_R11.md`, sha256
`5daae51e7a195be46ec9e4bd6269fa0035dc1f7ca34af9edac2fcc72dfda17f0`.
Read `SECTION6_REVIEW_R11_GPT56.md` and `SECTION6_REVIEW_R11_CODEX.md` first.

**The round is close.** GPT56 logged one blocker; CODEX logged **zero blocking** — two HIGH and one
MEDIUM. Both confirm the dispatched identity now holds, the `< 962/1,000` failure is correctly seated
and reachable at pre-unblinding Row J, and the normative no-rerun passages agree. **All of that
stays.**

## Defect 1 — deleting Row P's power branch orphaned the VOID branch

R10B made any deviation from the pinned 1,000-trial protocol or frozen Stage-C implementation
terminate `VOID`. **R11 removed that from Row P and Part 2 item 4 without reseating it anywhere.** Row
P now binds a protocol digest and verifier result and states no consequence if either fails. A
protocol deviation is a reachable input with no stated outcome — clause 10 in the forward direction.
And Part 5 still asserts twice that the outcome exists, which is clause 10 in reverse.

**Repair — seat it where it executes:** **Row J must verify exactly `N_TRIALS = 1_000` and the frozen
Stage-C implementation/protocol digest *before* running or issuing BS-5f, and any deviation
terminates `VOID`.** BS-5f binds that verification. Row P stays limited to binding the
already-verified PASS and protocol digest. **Do not restore an unreachable post-unblinding Stage-C
FAIL branch in Row P** — that is what R11 correctly removed.

## Defect 2 — `< 962` is not the only executable Stage-C FAIL

Row J currently emits `INCONCLUSIVE-BY-POWER` only when the locked run yields fewer than 962 passing
trials. **The frozen implementation has an independent fail-closed branch:
`../ref/successor_ref_v9.py` lines 1275–1276 return `False` on any `refuted` or `nonconservative`
result regardless of the passing-trial count.** V15 lines 421–425 give every Stage-C FAIL the same
pre-unblinding consequence. So a self-verification FAIL at 962 or more passing trials is a reachable
path with no stated outcome.

**Repair:** state in Row J that **any** locked Stage-C FAIL emits `INCONCLUSIVE-BY-POWER` and halts,
explicitly including **(a)** fewer than 962 of 1,000 passing trials and **(b)** the self-verification
`refuted` or `nonconservative` fail-closed return at reference lines 1275–1276. State the
complementary PASS branch as **the sole route to BS-5f → BS-L**. Conform Part 3 C2 and Part 5 item 17
to describe the complete PASS/FAIL partition rather than only the count threshold.

**Read lines 1275–1276 yourself before writing this.** Do not reason from my description.

## Defect 3 — Part 5's repair map asserts mechanisms the text no longer has

Part 5 item 8 says Row P deterministically applies the `< 962` rule; item 16 says Row P and Part 2
item 4 retain the deviation-to-`VOID` rule. R11 moved the count decision to Row J and deleted those
branches. Both items are labelled `REPAIR`, so **the document claims two incompatible current
mechanisms** — and it defeats the reachability audit by advertising outcomes the normative text does
not contain.

**Repair — rewrite items 8 and 16 to say:** the ordinary Stage-C PASS/FAIL decision executes at Row
J; a verified PASS is required for BS-L and is therefore inherited by Row P; protocol or
frozen-implementation deviation terminates `VOID` at Row J before an acceptable BS-5f exists. Update
the referenced line locations.

## The lesson from this round, applied to yourself

R11 deleted a branch and orphaned another. Deletion is a repair, but it is not a local edit — **when
you remove a branch, check what depended on it, and check whether Part 5 still advertises it.** Run
clause 10 in both directions over your own draft before finishing: every path reaches exactly one
stated outcome, and every stated outcome is reachable.

## Not in scope

The attrition-intolerance design question is with the principal. Findings 1, 2, 2b and 3 stay
UNRESOLVED pending BS-2a. Do not weaken the fail-closed calibration rule.

## Deliverable

`SECTION6_DRAFT_AGY_R12.md` — complete, self-contained, five parts, not a diff. **Write it once,
completely, in a single write.** Do not create the file and continue editing it.

Do not modify the preregistration. Do not read `/Users/duhokim/NebulaMindData/`. Nothing is
authorised to fetch. No deadline.
