# DRAFTING BRIEF — R10b. One finding I missed, and it reverses an instruction I gave you.

Subject: `SECTION6_DRAFT_AGY_R10.md` (just written by you under `BRIEF_DRAFT_SECTION6_R10.md`).
**Keep everything in it.** This adds one repair the R10 brief should have carried and did not.

## Why it was missing

I built the R10 brief from GPT56's report. CODEX writes findings in a different format that my
extraction did not match, so I worked from one seat's list and missed CODEX's finding 3. That is my
error, not a new referee round. The finding is in `SECTION6_REVIEW_R9C_CODEX.md`, item 3.

## The finding — and it reverses what I told you in R9

In R9 I instructed: if the exact 962/1,000 criterion cannot be applied post-attrition, emit
`INCONCLUSIVE-BY-POWER`. **CODEX shows that instruction was wrong.**

The pinned code (`../ref/successor_ref_v9.py` lines 77–78 and 1275–1277) fixes `N_TRIALS = 1_000` and
`CP_PASS_X = 962`, returns a boolean pass/fail whenever `n_trials == N_TRIALS`, and returns `None`
when the trial count differs. Your text says the criterion may be inapplicable "e.g., because the
trial structure differs." But **a changed trial count or structure is a departure from the frozen
protocol, and V15 lines 570–573 make any post-first-real-χ deviation from a binding rule, algorithm
or threshold contract VOID — not inconclusive.**

So the branch as written either **downgrades a void to an inconclusive**, or is unreachable. Both are
defects. `INCONCLUSIVE-BY-POWER` is a scientific outcome; `VOID` is a protocol failure. Emitting the
gentler one for a protocol breach is the document excusing its own violation.

## The repair — split the causes

1. **Any deviation from the pinned 1,000-trial protocol or the frozen Stage-C implementation
   terminates `VOID`.** State it in row P and in Part 2 item 4.
2. **`INCONCLUSIVE-BY-POWER` may remain only for a specifically named inapplicability state produced
   by the *unchanged* frozen protocol.** If such a lawful state exists, name the predicate and the
   receipt field that carries it.
3. **If no such lawful state exists — delete the inapplicability branch entirely and apply the pinned
   `< 962` rule alone.** Do not keep a branch alive to be safe. An unreachable branch is exactly what
   clause 10 forbids, and deleting it is the honest outcome if nothing can reach it.

Decide 2 or 3 on what the frozen code actually admits, and say in Part 3 which you chose and why.
Read lines 1275–1277 before deciding; do not reason from the description alone.

## Also carry forward

Everything from the R10 brief stands: the four join-anomaly branches keep their named
`INCONCLUSIVE-BY-*` refusals with the void column made to agree; the ordered adequacy decision tree
with Part 2 and R3 conformed; and clause 8's retrospective-custody branch terminated rather than
deferred to a later judgement.

**Not in scope:** the attrition-intolerance design question is with the principal. Do not weaken the
fail-closed calibration rule.

## Deliverable

`SECTION6_DRAFT_AGY_R10B.md` — complete, self-contained, five parts, not a diff.

Do not modify the preregistration. Do not read `/Users/duhokim/NebulaMindData/`. Nothing is
authorised to fetch. No deadline.

**Emitting a softer terminal state for a protocol breach is renaming a finding.** If the honest
answer is VOID, write VOID.
