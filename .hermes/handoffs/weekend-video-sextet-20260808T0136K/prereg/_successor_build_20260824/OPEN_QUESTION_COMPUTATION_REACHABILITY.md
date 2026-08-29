# OPEN QUESTION — `INCONCLUSIVE-BY-COMPUTATION` cannot fire, and I have failed twice on it

**Raised 2026-08-29 13:5x KST by Hwao. Two hard stops apply at once: this has now failed twice the
same way, and every remaining repair changes what an existing guard claims.**

## What happened, in order

- **V43, both seats (HIGH):** a pre-unblinding Stage-C numerical failure mapped to **both**
  `INCONCLUSIVE-BY-COMPUTATION` and Row J's POWER route, and the new code had no named producer.
- **My V44 repair:** made COMPUTATION **residual** — firing only where neither POWER nor CALIBRATION
  claims the failure — and added a §11 item requiring it be evaluated **after** both guards.
- **V44, both seats (HIGH), and they are right:** CODEX states it exactly — *"evaluating it after
  that guard makes the purported residual route unreachable on Stage-C numerical failures."*

**I did not resolve the overlap. I converted it into a dead branch.** §4 line 476 is universal:
Stage-C `FAIL → INCONCLUSIVE-BY-POWER declared before unblinding; the run halts`. Every Stage-C
failure is a FAIL, including a numerical one. So ordering COMPUTATION after the power guard means it
can never fire there.

**That is this lane's own defect class turned on an outcome instead of a check.** A control that
cannot fire proves nothing; an outcome that cannot be produced is a promise the document cannot keep.
The V43 finding and the V44 finding are the same problem, which is why I am stopping rather than
attempting a third repair.

## The options, and what each costs

**A. Narrow §4's Stage-C FAIL branch** so a numerical failure is excluded from POWER and reaches
COMPUTATION. *Cost:* changes what `INCONCLUSIVE-BY-POWER` claims — a §4 rule that has been stable
since well before this work, and one the power analysis depends on.

**B. Evaluate COMPUTATION before the power guard**, making POWER residual instead. *Cost:* inverts an
existing precedence. A Stage-C failure that today reports POWER would report COMPUTATION, changing
what previous reasoning about the power path means.

**C. Scope COMPUTATION to numerical failures outside Stage C** — the production runner's
permutation/statistic/protocol work — leaving Stage C wholly to POWER. *Cost:* needs someone to
confirm such a locus actually exists pre-unblinding; if it does not, C is A or B wearing a
narrower name, and I could not establish that from the document alone.

**D. Delete `INCONCLUSIVE-BY-COMPUTATION`.** Stage-C numerical failures already terminate the run
through POWER, and the principal's option C ruling asked that pre-unblinding numerical failures
*"route to an inconclusive code alongside the calibration one"* — POWER is such a code, and the route
already exists. *Cost:* it reads as walking back the option C ruling, and whether POWER is the code
the ruling meant is a judgement about the ruling, not about the text.

## My reading, not my decision

**D or C, and I lean D** — the ruling's requirement is that such a failure ends the run in a named
inconclusive outcome, which POWER already does. Adding a second code for a case an existing code
already claims is what created the overlap, then the dead branch. **But D is the option most likely
to be wrong about what the principal meant**, and that is precisely why it is not mine.

**What I am confident of:** the current text is defective either way. `INCONCLUSIVE-BY-COMPUTATION`
as written cannot be produced on the failures it names, and that must not be frozen.

## Status

- **V45** (`4fcc9c3460abfe2d`) repairs only the other V44 finding — §11's BS-3g item still called the
  completeness semantics open after the principal settled them. **F1 is untouched and V45 is not
  dispatched.**
- Checkers on V45: counts 16/8 prose-matched; trace 44 transitions, 0 problems; `void_registry`
  self-test 6/0; lint exits 0.
- **BS-6 and the first image byte remain blocked.**
