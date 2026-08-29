# OPEN QUESTION — a pre-unblinding permutation failure is voided by the prose and by no antecedent

**Raised 2026-08-29 10:5x KST by Hwao, from CODEX-V38 F2 (HIGH). Hard stops: every available repair
changes what voids a run, and the authorship record does not determine which was meant. I checked the
record first — that is now the rule here — and it does not settle this one.**

## The finding, verified against the document

**§5 line 493** states the VOID trigger with **no phase qualifier**:

> **VOID:** triggered by forbidden acts, protocol/digest deviation, or permutation/statistic/protocol
> non-finite/degenerate failures.

**§7.1** scopes the matching antecedents to `Post-unblinding`: `VOID-5-NONFINITE` (present since V24)
and `VOID-5-DEGENERATE` (added in V37 under the authorised option A, inheriting its sibling's phase).

**The pre-unblinding case is not covered by the inconclusive path either.** §5 line 491's
`INCONCLUSIVE-BY-CALIBRATION` covers *"aggregate non-finite/degenerate failures"* — **calibration
aggregates**. §5 line 493's trigger is broader: **permutation**, **statistic**, **protocol**.

**And the gap is reachable, not theoretical.** The §6 conduct table's Row J runs Stage C
**pre-unblinding**, injecting synthetic signs and permuting, and never reads a real χ. A non-finite or
degenerate *permutation* result there is voided by §5's prose, is not an aggregate calibration
failure, and matches no antecedent phase.

**CODEX found this; GPT56 did not.** That asymmetry is not evidence against it — I verified each step
above against the document's own bytes — but it is worth recording that it rests on one seat.

## Why I did not repair it

It is **not** a defect V37 introduced: `VOID-5-NONFINITE` has carried `Post-unblinding` since V24
(commit `96c3469a2`), whose message introduces the registry requirement but gives **no rationale for
the phase**. So the record does not tell me what was meant, and this is not recoverable the way the
§2.7 instant was.

Every repair changes what voids a run:

**A. Broaden the phases to `Any`.** The prose and the registry agree, and every non-finite/degenerate
failure voids whenever it happens. *Cost:* a transient pre-unblinding numerical failure — in a stage
that runs on **synthetic** signs and reads no real χ — would kill the entire run rather than halt it
recoverably. That is a harsh reading of a stage designed to be rerunnable, and it is the option most
likely to destroy a run for a reason nobody intended.

**B. Add distinct pre-unblinding antecedents** (e.g. `VOID-5-NONFINITE-PRE`), so the pre-unblinding
case is named and can carry its own effect. *Cost:* two more normative antecedents, and it still
requires deciding whether their effect is VOID or INCONCLUSIVE — the same question, one level down.

**C. Qualify §5's prose** so the trigger reads post-unblinding, and route pre-unblinding
permutation/statistic failures to an inconclusive code alongside the calibration one. *Cost:*
**narrows VOID**, which is the dangerous direction if a genuine protocol deviation can occur
pre-unblinding — and forbidden acts and protocol deviation are already `Any` in the registry,
suggesting the authors did think about pre-unblinding misconduct.

## My reading, not my decision

**C for the numerical conditions, and leave the misconduct conditions alone.** A non-finite
permutation on synthetic signs is a *computation that failed*, not a *protocol that was broken*, and
the document already separates those: forbidden acts and protocol/digest deviation are `Any`, while
the numerical failures sit `Post-unblinding`. That split looks deliberate rather than accidental, and
C makes the prose say what the registry already does.

**But I am not confident**, which is the stopping condition. The V24 record is silent, and B is the
option that concedes least while still closing the hole. **A pre-unblinding failure is also exactly
where an operator would most want a rerun rather than a void**, so the choice has consequences for
how the study behaves under a bad night, not merely for what it says.

## Status

- **V39 (`221c6a08cd794e5b`) records this as OPEN in §7.1** and does not resolve it. Registry digest
  unchanged at `a4d1d745…`; class counts 16/8; all checkers pass.
- The three other V38 findings are repaired in V39 (both seats' agreed BS-3g omission, and CODEX's
  two citation-accuracy findings).
- **BS-6 and the first image byte remain blocked.**
