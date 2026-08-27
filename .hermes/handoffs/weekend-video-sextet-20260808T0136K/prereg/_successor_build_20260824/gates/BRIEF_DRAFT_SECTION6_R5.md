# DRAFTING BRIEF — §6, fifth pass. Build the property. Do not name it.

You wrote `SECTION6_DRAFT_AGY_R4.md`. Both referees returned NOT CLEAR
(`SECTION6_REVIEW_R4_GPT56.md`, `SECTION6_REVIEW_R4_CODEX.md`). Revise into
`SECTION6_DRAFT_AGY_R5.md`.

## The instruction, from the principal

**Make the acceptance-evidence projection outcome-free BY CONSTRUCTION, not by declaration.**

Both referees converged on this independently:

- GPT56: *"the acceptance-evidence projection is declared outcome-free, not made outcome-free."*
- CODEX: *"not sign-blind by construction"* — and specifically that keeping the serialized
  measurement receipt away from row E is **necessary but not sufficient, because row D still sees
  enough.**

The test: **a reviewer looking at the acceptance evidence must be unable to infer the answer
because of what the projection structurally contains — not because the text says they must not.**

## The diagnosis, and it is mine

Round 3 established a rule: **renaming a finding counts as refusing it.** R4 then renamed the
property to "outcome-free" without making it so. That is the same move, one round later, inside
the mechanism written to prevent it.

This is the fourth consecutive round where the objection has the same shape: **you said it, you
did not build it.** It matches a check in another lane that could not fail, a probe that asserted
on its own outdated wording, and a brief citing a change record that did not exist. **Name this
failure mode explicitly in the draft**, so the next reader knows the author knew it. A document
that admits its programme's characteristic defect is easier to audit than one that quietly
repeats it.

## The design principle you are given

**A narrower projection you can prove is worth more than a wide one you have to promise about.**
If the honest construction is that some evidence cannot be shown at all before unblinding, say
so and lose the convenience.

Consider these candidates and either adopt or refute each with reasons — they are mine, and
assembling requirements is the operation that keeps going wrong here:

1. **Change the writer, not the fields.** A projection written by a process that has seen the
   sign can always encode it. Cutout integrity, tensor shape and completion are properties of
   image bytes, computable by a process that never invokes the classifier. If the acceptance
   evidence is produced by such a process, no channel exists to encode an outcome.
2. **Drop confidence-based exclusion before unblinding.** Confidence comes from the classifier
   and is the channel both referees named. Options: exclude only on integrity failures pre-lock;
   or apply a confidence rule after unblinding, by pinned code, with no human in the loop and the
   threshold frozen beforehand. Say what this costs.
3. **If a field must come from an outcome-aware process, it cannot be in the pre-lock
   projection.** State that as a rule and apply it to every field, rather than case by case.

## What must not regress — confirmed held by both referees across four passes

- The universal access ban stays closed: every person and process, table as the sole pre-unblinding
  exception surface, a conforming table-authorized act surviving the void rule.
- The hand-check committee completes G → H → I without voiding the run.
- The BS-5f chain works.

**Do not trade any of these away chasing the projection.** If a construction for the projection
would break one, refuse it and say so.

## Structure

Part 1 replacement §6, Part 2 conforming edits outside §6, Part 3 choices and rejected
alternatives, Part 4 residual risks, Part 5 each finding REPAIR or REFUSE — never a bare
"Accepted", and **never a repair whose mechanism is a promise about behaviour rather than a
constraint on capability.**

Do not modify the preregistration. Do not read `/Users/duhokim/NebulaMindData/`.
