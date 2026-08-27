# DRAFTING BRIEF — R9. Two reachable branches need a consequence decided NOW. Small pass.

Subject: `SECTION6_DRAFT_AGY_R8B.md`, sha256
`5a407225ec21792cfe4c342d2dec681943eb00a7a376f90053f297e56a03f2a2`.
Read `SECTION6_REVIEW_R8B_GPT56.md` and `SECTION6_REVIEW_R8B_CODEX.md` first.

**This is a small pass. Almost everything in R8b is confirmed and stays.**

## What both referees verified and credited

- **Both independently checked the two numeric thresholds against the frozen files and confirmed
  them.** CODEX traced `a_LB_b < 0.85` to V15 566–567, `A_FLOOR` to `successor_ref_v9.py` line 81
  and its enforcement at 1492–1496; and the 1,000-trial rule to V15 390–391, `N_TRIALS`/`CP_PASS_X`
  at lines 77–78 and the comparison `succ >= CP_PASS_X` at line 1277. Your "fewer than 962" wording
  is exact.
- **Both swept the whole document for further composed numbers and found none.** The remaining
  numeric literals — 208,405 and 65,060 — trace to V15. The invented ε ≥ 0.1, n < 400 and power <
  0.8 are gone.
- The exact-parent terminal-state partition is credited as materially more decidable.
- Row I's halt reveals aggregate completeness, not handedness or direction — the leakage cost is
  acceptable.
- Unconditional refusal on removal of an allocated committee member is a conservative, determinate
  choice and is credited.
- Refusing an entire 65,060-object run for any single unusable row was correctly declined as
  operationally brittle.

**Do not touch any of that.**

## Defect 1 — my instruction was wrong, and it created this blocker

I told you that if the 962/1,000 criterion cannot be applied post-attrition, declaring a stated gap
was an acceptable output. **That was wrong, and both referees caught it.** CODEX gives the reason:

> V15 lines 570–573 void any post-first-real-χ change to a decision threshold, and post-read
> amendments cannot cure a void.

The branch is reached **after unblinding**. So a threshold defined at that point would void the run,
and the gap therefore **cannot lawfully be filled later**. A named gap is candid, but candor is not
a terminal state — a gate reaching that branch still cannot decide whether to emit
`INCONCLUSIVE-BY-POWER`, void the run, or wait for a number that may never lawfully exist.

**Assign the consequence now.** My reading is that it should emit **`INCONCLUSIVE-BY-POWER`**: the
study cannot demonstrate adequacy on the analysed population, and the defined state for inadequate
power already exists. Voiding is harsher than the situation warrants — nothing was tampered with,
the sample simply attrited. **If you think voiding is the correct call, argue it in Part 3 and take
it.** What is not available is leaving the branch open.

Say explicitly in the text that the consequence is fixed **before any real χ is read**, and cite
V15 lines 570–573 as the reason it must be.

## Defect 2 — `calibration applicability` is undefined for non-committee attrition

Row P binds a `calibration applicability` field into the post-unblinding adequacy receipt, and
defines the predicate only for the committee-member case (unconditional
`INCONCLUSIVE-BY-CALIBRATION`). For **non-committee attrition** there is no predicate at all, so the
field's value is post-unblinding policy.

Define it, from frozen quantities only. `a_LB_b < 0.85` is V15's **pre-unblinding halt** predicate —
GPT56's finding 2 warns that re-using it post-unblinding is numerically correct but its
**applicability must itself be a frozen predicate**, and §6 must make the dependency and the
fail-closed consequence explicit. If a needed quantity does not exist in the frozen record, **do not
compose one** — say which quantity is missing and make the branch fail closed to
`INCONCLUSIVE-BY-CALIBRATION`.

## Defect 3 — a false claim about your own diff (both, LOW)

R8b says only the thresholds changed. Both referees diffed it: four regions changed — the title, the
governing-brief name, row P's thresholds, and a new Part 3 choice C2. No lifecycle, custody, actor,
terminal-state or BS-2a disposition rule changed, so the *normative* claim holds and the literal one
does not. Restate it accurately.

## After this pass

Both referees say §6 is not yet sound as prose **but that these repairs are bounded**. GPT56: once
they are made, the remaining channel-closure mechanism "can genuinely stay in BS-2a rather than
trigger another broad §6 rewrite." So write this pass to close §6, not to open it.

## Deliverable

`SECTION6_DRAFT_AGY_R9.md` — complete, self-contained, five parts, not a diff.

Do not modify the preregistration. Do not read `/Users/duhokim/NebulaMindData/`. Nothing is
authorised to fetch. No deadline.

**A branch without a consequence is a decision deferred to whoever runs it.** That is the freedom
this document exists to remove.
