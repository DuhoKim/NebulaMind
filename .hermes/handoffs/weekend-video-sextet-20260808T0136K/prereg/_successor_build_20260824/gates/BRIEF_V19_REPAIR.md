# REPAIR BRIEF — V19. One convergent blocker, one trace completion. The narrowest pass yet.

Base: `../PREREG_SUCCESSOR_DRAFT_V18_20260827.md`, sha256
`ce144dc23ba8605df1a3b7590464fc3de09c313a597168f91c80d4b29ab302f4`. **Verify before starting.**
Read `V18_WHOLE_REVIEW_GPT56.md` and `V18_WHOLE_REVIEW_CODEX.md` in full first.

**Write `../PREREG_SUCCESSOR_DRAFT_V19_20260827.md`.** Do not edit V18 in place. **Do not touch V15,
V16 or V17** — all checked immutable before and after.

## Credited — do not disturb

Both seats confirm: the digest matches; **the registry's two namespaces are disjoint by construction
and by type** — CODEX tried to place an `EXCLUDED-BY-*` or `ACCEPTED-FINITE` label in the run-level set
and failed; the **§2.7 confidence-authority repair holds**; the **§3 calibration-precedence repair
holds**; the **V17→V18 trace is ACCURATE**, every substantive hunk represented; and **the unbriefed
Row-I abort is accepted by both.**

## Blocker — the registry is disjoint in prose but not executable by its named producer

Both seats, independently. §5 claims `run_production_verdict()` "emits exactly one outcome from the
canonical registry" — but the run-level registry contains **pre-verdict lifecycle outcomes that
function cannot return**, because they occur before it runs. §0 makes the pinned code the definition
and prose disagreement a defect, so a prose set can be disjoint while its asserted producer cannot
emit it.

**Repair — take the naming route, not the new-code route:**

- Define the list as the **canonical study-run lifecycle outcome registry** — exactly one outcome per
  **run**, not per function call.
- **Name the producing phase or process for each category**: Row I, Row J, Row P or the pre-verdict
  validator, or the numeric decision helper.
- **Narrow `run_production_verdict()`'s emitter claim to the outcomes it can actually return.**
- Keep the per-attempt registry separate and unchanged.

Do **not** invent an orchestration symbol that owns every terminal phase — that is new machinery,
and this document does not get to claim code it has not specified.

GPT56 adds one thing to fix while you are here: **split non-finite and degenerate failures by phase
and cause.** A calibration-input failure may map to calibration inconclusive, but
permutation/statistic/protocol failures need their own honest fail-closed category or a precisely
defined `VOID` rule. **If the branch is not implementable in the pinned code, list it as unresolved
required work rather than claiming executable closure.**

## Trace completion (CODEX 2)

The **V16→V17** entry is not a complete finding→change map. Expand its §6.3 finding row to include
**Row P's V15-citation replacement**, and add the **still-unrepaired historical §10 claim** to the
"Partial repairs" row. **No prose outside §10 needs to change.**

Then add the **V18→V19** entry for this pass, as §6.3 now requires.

## Then audit your own result

Clause 10 across §§0–11, both directions, against both registry sets. Every threshold: value, phase,
failure effect. And check nothing adjacent broke — five of the last six rounds introduced a defect
while fixing one.

## Standing state

Findings 1, 2, 2b and 3 **UNRESOLVED**; **BS-2a REFUSED**; rows C2 and E cannot run; **BS-6 and the
first image byte blocked**; `verify_lock()` and the unblinding-receipt schema required work, not
implemented.

## Deliverable

`../PREREG_SUCCESSOR_DRAFT_V19_20260827.md`, complete, single write, titled **V19**.

Do not read `/Users/duhokim/NebulaMindData/`. Nothing is authorised to fetch. No deadline.
