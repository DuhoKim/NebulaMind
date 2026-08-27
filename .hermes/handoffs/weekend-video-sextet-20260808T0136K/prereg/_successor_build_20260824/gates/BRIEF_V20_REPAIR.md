# REPAIR BRIEF — V20. Stop claiming capability the code does not have. Say what it actually returns.

Base: `../PREREG_SUCCESSOR_DRAFT_V19_20260827.md`, sha256
`b7deb106eb81b3e13376e7049263b355ba90982656f7de30964c0d3bfda5e63b`. **Verify before starting.**
Read `V19_WHOLE_REVIEW_GPT56.md` and `V19_WHOLE_REVIEW_CODEX.md` in full first — both traced the
pinned implementation line by line, and their line numbers are the specification for this pass.

**Write `../PREREG_SUCCESSOR_DRAFT_V20_20260827.md`.** Do not edit V19 in place. **Do not touch V15
through V18** — all checked immutable.

## Credited — do not disturb

The lifecycle rename **did** fix the impossible claim that one late function owns every earlier halt.
Numeric outcomes are correctly assigned to the numeric helper. Per-attempt states remain separate,
zero-or-more and disjoint. **All three §10 trace entries are now accurate against their mechanical
diffs** (CODEX), and the threshold contract holds.

## The blocker — names without capability

CODEX: *"V19 now has textual names, but executable returns, prose phase ownership, and the claimed
runner set disagree in both directions."* §0 makes the pinned code the definition, so this is a defect
by the document's own rule. Five distinct failures:

**A. The narrowed runner claim is factually inverted.** Line 473 says `run_production_verdict()` can
return numeric verdicts, post-unblinding accounting refusals, post-unblinding calibration halts and
`VOID`. The pinned function (lines 1591–1625) returns the three numeric outcomes via `_decide_from()`
and `INCONCLUSIVE-BY-POWER` at 1610–1616. **It contains no accounting join, no accounting-refusal
return, no post-unblinding attrition validator, no `VOID` return, and no catch converting
`InconclusiveByCalibration` into an emitted verdict.**

**B. The power producer is not exhaustive.** Line 469 names Row J for `INCONCLUSIVE-BY-POWER`, but §5
lines 486–487 and the pinned runner at 1610–1616 make the **production runner** emit the same category
for a failed Stage-C receipt or `N_eq < 100,000`. A category with an omitted producer contradicts
V19's own promise.

**C. Several named producers are promises, not capabilities.** The Row-J calibration guard is
**explicitly still required work** at §11 line 806. The accounting/adequacy validator and its
schemas/verifiers likewise (§11 804–810). `INCONCLUSIVE-BY-MISSING-ALLOCATED-OUTPUT` occurs **only in
the registry** — Row I mandates an abort with no emission mechanism. **A draft may honestly specify
required work; it may not simultaneously name that work as a current producer.**

**D. `VOID` has no producing phase or process.** Line 471 lists triggers and admits permutation and
statistic failures currently raise **uncategorised exceptions**. **A trigger condition is not an
emitter.** Reverse reachability stops at an abstract label.

**E. The non-finite split is not disjoint by phase and cause.** Row I (line 529) treats an allocated
object's missing **or non-finite** output as the pre-BS-8f abort mapping to
`INCONCLUSIVE-BY-MISSING-ALLOCATED-OUTPUT`. Line 469 also maps "calibration-input
non-finite/degenerate failures" to `INCONCLUSIVE-BY-CALIBRATION`. Those instrument outputs **are** Row
I's calibration inputs, so **one antecedent yields two run outcomes.**

## The repair — an honest capability statement, not more naming

1. **Replace line 473 with an exact present-tense inventory of what the pinned function really
   returns**: the numeric outcomes plus its two power branches. **Separately label as unresolved
   required implementation**: accounting, post-unblinding calibration return, Row-I emission, the
   Row-J calibration guard, per-attempt emission, and `VOID` conversion.
2. **List all producers per category** in the lifecycle registry, including the production runner's
   `N_eq` and Stage-C power guard.
3. **Name a fixed validator or process and phase for `VOID`, or state explicitly that the category is
   not yet executable.** Either is acceptable. Silence is not.
4. **Define "calibration-input non-finite/degenerate" so it excludes the Row-I case**, and name the
   producer that validates calibration aggregates as finite and non-degenerate **before** the `< 0.85`
   comparison, with its emitted authenticated outcome. Add that implementation and its fixture to §11.
5. **Correct the V16→V17 trace row** (GPT56 2) to: *"Repaired the Class E count in §7 from 7 to 8; the
   already-correct Class P count remained 14."* Verify that against V16 line 636 and V17 line 669
   yourself before writing it.
6. Add the **V19→V20** trace entry.

**Do not invent an orchestration symbol** unless its contract is actually specified. Both seats say
so independently, and it remains forbidden.

**The honest move here is subtraction.** Where the document claims a capability the pinned code does
not have, remove the claim and mark the work unresolved. This lane has repeatedly found that refusing
is a result: BS-2a refused rather than composed, reason (c) refused rather than invented, a threshold
declared missing rather than fabricated. Do the same here.

## Then audit your own result

Clause 10 across §§0–11, both directions. Every threshold: value, phase, failure effect. Check nothing
adjacent broke.

## Standing state

Findings 1, 2, 2b and 3 **UNRESOLVED**; **BS-2a REFUSED**; rows C2 and E cannot run; **BS-6 and the
first image byte blocked**.

## Deliverable

`../PREREG_SUCCESSOR_DRAFT_V20_20260827.md`, complete, single write, titled **V20**.

Do not read `/Users/duhokim/NebulaMindData/`. Nothing is authorised to fetch. No deadline.
