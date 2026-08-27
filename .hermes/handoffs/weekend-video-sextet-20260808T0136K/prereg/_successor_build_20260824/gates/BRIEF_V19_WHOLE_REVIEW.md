# REFEREE BRIEF — V19, whole document. Fourth assembled round.

Subject: **`../PREREG_SUCCESSOR_DRAFT_V19_20260827.md`**, sha256
`b7deb106eb81b3e13376e7049263b355ba90982656f7de30964c0d3bfda5e63b`. **Verify before opening, and
record the result.** 30 lines changed from V18 — the narrowest pass so far.

## What your V18 round produced

Both NOT CLEAR, one blocker each, reached independently and identically: **the registry was disjoint
in prose but named a producer that could not emit it.** §5 claimed `run_production_verdict()` emits
exactly one outcome from a set containing pre-verdict lifecycle outcomes that occur before it runs.

V19 takes the **naming** route you both proposed, not new machinery:

- the list is now the **canonical study-run lifecycle outcome registry** — exactly one outcome per
  **run**, not per function call;
- **the producing phase or process is named for each category** — Row I, Row J, Row P, the pre-verdict
  validator, or the numeric decision helper;
- **`run_production_verdict()`'s emitter claim is narrowed** to outcomes it can actually return;
- the per-attempt registry is unchanged.

**No orchestration symbol was invented.** I forbade it explicitly — a document does not get to claim
code it has not specified — and the check confirms none appears. If you think one is genuinely
required, say so as a finding rather than assuming it was an oversight.

GPT56's second point is also addressed: **non-finite and degenerate failures split by phase and
cause**, with anything unimplementable in the pinned code listed as unresolved required work rather
than claimed closed.

CODEX's trace completion: the **V16→V17** entry now includes Row P's V15-citation replacement, the
still-unrepaired historical §10 claim moved to "Partial repairs", and a **V18→V19** entry added.

## What both of you credited in V18 — do not disturb

The two registry namespaces are **disjoint by construction and by type** (CODEX confirmed
adversarially by trying to place `EXCLUDED-BY-*` and `ACCEPTED-FINITE` in the run-level set and
failing). The §2.7 confidence-authority repair. The §3 calibration-precedence repair. The **accurate
V17→V18 trace.** The **Row-I abort**, which you both accepted despite it being unbriefed.

## What to judge

1. **Digest first**, recorded.
2. **Does the renaming actually fix it, or relocate it?** For every category in the lifecycle
   registry, check the named producer can in fact emit it at that phase. **The failure mode this
   whole sequence keeps producing is a correct-sounding name over an unchanged capability.**
3. **Clause 10 across §§0–11, both directions, against both registries.**
4. **Every threshold: value, phase, failure effect.**
5. **Are all three §10 trace entries accurate** — V16→V17, V17→V18, V18→V19? Compare each against
   what actually changed.
6. **Did anything adjacent break?** Six of the last seven rounds introduced a defect while fixing one.
7. **Does the document overclaim?**

## Standing state

Findings 1, 2, 2b and 3 **UNRESOLVED**; **BS-2a REFUSED**; rows C2 and E cannot run; **BS-6 and the
first image byte blocked**; `verify_lock()` and the unblinding-receipt schema required work, not
implemented. V15 through V18 held at their reviewed digests, verified immutable across this run.

Do not read `/Users/duhokim/NebulaMindData/`. Nothing is authorised to fetch. No deadline.

## Verdict

`V19_WHOLE_REVIEW_<YOURSEAT>.md`. Numbered findings with severity, section and line, why it fails,
smallest sufficient repair. Unverified assertions under `Testimony`. Final line exactly `**CLEAR**`
or `**NOT CLEAR**`.

Blockers have fallen every assembled round: four and five, three and four, one and two. **Do not let
that trend influence your verdict.** If it is sound, say so; if something is wrong, say what. A
finding at this stage is worth more than a clear, and neither of you should converge toward the other.
