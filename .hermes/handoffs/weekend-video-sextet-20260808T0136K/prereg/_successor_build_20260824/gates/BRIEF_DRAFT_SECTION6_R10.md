# DRAFTING BRIEF — R10. Clause 10 caught three branches, including one in your own clause list.

Subject: `SECTION6_DRAFT_AGY_R9C.md`, sha256
`ad2b23f058a4304025a1b267d8790ec563a4a61c5384a8017185ab6b7300c576`.
Read `SECTION6_REVIEW_R9C_GPT56.md` and `SECTION6_REVIEW_R9C_CODEX.md` first.

**Clause 10 worked.** The referees applied it to the whole table as a test and it found three
branches that do not terminate — one of them in the clause list itself. That is the rule doing its
job, not a failure of the round.

**What is confirmed and stays:** both numeric thresholds re-verified against the pinned files by both
seats, with a full comparison-operator and numeric-literal sweep finding no further composed value.
The terminal-state partition, the exact-parent join, the ban on silent inner-join loss and on
discretionary retry, twenty rows, the three protected properties. Findings 1, 2, 2b and 3 stay
UNRESOLVED pending BS-2a. **Do not reopen any of it.**

## Defect 1 — four branches each reach two different outcomes

Row P's partition emits `INCONCLUSIVE-BY-MISSING-RECORD`, `-DUPLICATE`, `-ORPHAN` and `-MALFORMED`
for zero, duplicate, extra and malformed records. **The same row's final column then lists
"missing/duplicate/extra/malformed records" under what voids the run.** Inconclusive and void are not
interchangeable, so each of those four branches terminates twice.

**Repair:** keep the named `INCONCLUSIVE-BY-*` refusals and **delete missing/duplicate/extra/malformed
from row P's void column**, reserving void for prohibited execution outside the symbol, silent
inner-join loss, and discretionary retry.

## Defect 2 — calibration and power have no precedence, and one makes the other dead

Committee attrition emits `INCONCLUSIVE-BY-CALIBRATION`. Non-committee attrition also emits it,
because the applicability predicate is absent. **Those two cases exhaust attrition.** Yet the same
row also requires Stage-C re-evaluation and emits `INCONCLUSIVE-BY-POWER` below 962/1,000.

Two problems. There is no precedence: for a mask that fails both, the prose does not say which
terminates, whether both are emitted, or whether power runs at all. And if "emits" means immediate
termination, **the fail-closed calibration rule makes every post-attrition Stage-C branch
unreachable** — contradicting Part 2's promise to re-evaluate Stage C and residual risk R3's "strict
recomputation protocol." R3 compounds it by saying post-unblinding failure "would void the run,"
where row P says inconclusive.

**Repair:** freeze an ordered adequacy decision tree. If calibration is first, say plainly that any
attrition immediately emits `INCONCLUSIVE-BY-CALIBRATION`, that **no Stage-C rerun is performed**,
and fix Part 2 and R3 to match — including replacing R3's "void" language. If both must run, define
one deterministic outcome for simultaneous failure. **Do not leave the executor to choose which
failure names the result.**

## Defect 3 — clause 8 defers to a judgement made later, which clause 10 forbids

Clause 8 says the retrospective-custody question is "open" and "its resolution is a freeze-level
decision for the principal." **Clause 10 says a consequence depending on a judgement made later is
not a termination.** Naming the decision-maker does not terminate the branch.

The prose may remain candid that the history is unknowable. What it may not do is leave the
*consequence* of that uncertainty unstated.

**Repair — write this:** the retrospective-custody question must be resolved before freeze, and **if
it is unresolved at freeze time the run is refused.** That terminates the branch without pre-empting
what the principal decides on the substance; he retains the whole pre-freeze window to decide, and
the document stops depending on a decision that might never come. If you think the honest
alternative is that retrospective uncertainty has no effect on execution and is purely a fixed
disclosure limitation, argue that in Part 3 — but pick one and state it.

## Not in scope

GPT56's finding 4 and CODEX's finding 4 — that any single removal now forces
`INCONCLUSIVE-BY-CALIBRATION` — is a **design** question, not prose, and is with the principal.
Do not attempt to solve it. Do not weaken the fail-closed rule to avoid it.

One correction for your Part 4: my brief told the referees attrition is "near-certain" at 65,060
objects. **Neither seat would assert that**, because no attrition rate exists in the authorised
files. GPT56 gave sensitivity only — a per-object rate of 1.07e-5 makes at least one attrition 50%
likely, 4.6e-5 makes it 95%. If your residual risks repeat "near-certain", correct it to the
structural statement: **any one removal is sufficient**, and the rate is unknown.

## Deliverable

`SECTION6_DRAFT_AGY_R10.md` — complete, self-contained, five parts, not a diff.

Do not modify the preregistration. Do not read `/Users/duhokim/NebulaMindData/`. Nothing is
authorised to fetch. No deadline.
