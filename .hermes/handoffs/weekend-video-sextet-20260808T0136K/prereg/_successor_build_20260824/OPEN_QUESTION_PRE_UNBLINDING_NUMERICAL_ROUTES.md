# OPEN QUESTION — a pre-unblinding numerical failure may have no executable route at all

**Raised 2026-08-29 14:1x KST by Hwao from the V46 round. Both seats, HIGH, converging. Naming an
outcome for an unterminated branch changes what the study claims, so it stops here.**

## What the seats found, and they are right

I asked both seats to attack the completeness argument I had written into §5. They broke it in two
places, and the second is a genuine pre-existing defect rather than a flaw in my prose.

**1. The §2.7 premise was simply false (both seats).** My argument said a per-object non-finite
instrument output is disposed of by §2.7's exclusion reason (c). **Reason (c) is *catalogue
quality*.** §2.7 line 344 says the opposite of what I claimed: *"Instrument absence/non-finiteness
and confidence threshold exclusions are **deferred to post-unblinding handling**."* I quoted reason
(c) from the V11 diff I had read that morning, not from the current text, which had changed. My own
operating rule is to verify an anchor claim from the source at the moment of use.

**2. The enumeration missed Row F (CODEX).** **Row F, calibration-bin sealing, runs pre-unblinding at
P3** and writes sealed boundaries, bin labels and the hand-check allocation. Its **degenerate-bin and
infeasible-allocation FAIL branches are executable and carry no named outcome.** So §6.1's row table
does not close the set the way my argument needed, and §6.3(10) — *every branch of every row must
terminate in one stated outcome* — is violated independently of anything I wrote.

**I hit Row F's degenerate-bin failure myself earlier the same day**, probing the gain path, where
`calibration_bins` refused with `degenerate calibration bins [60, 0, 0] — FAIL`. I still left Row F
out, because I built the enumeration with a keyword filter (`pre-unblind|permut|stage`) and Row F's
line contains none of those words. **A narrow pattern, in the absence direction, inside the argument
about when absence may be asserted.**

**3. And the route is not executable (GPT56).** The normative Stage-C code propagates numerical
exceptions, and §11 names no conversion from an exception to `INCONCLUSIVE-BY-POWER`. So even where
the document says POWER claims a Stage-C failure, nothing yet turns a raised exception into that
outcome.

## What this does and does not disturb

**It does not disturb the principal's option D ruling.** Deleting `INCONCLUSIVE-BY-COMPUTATION` was
ruled on the ground that POWER is the code the earlier ruling meant, and a second claimant on the
same route was redundant. **That remains true.** What is now in doubt is whether the route it was
redundant with is *complete and executable* — a different question, and one nobody has answered.

**The retracted argument is not load-bearing for the deletion.** V47 records the retraction in §5 and
says the deletion stands on the ruling, not on my reasoning.

## The options

**A. Name outcomes for Row F's FAIL branches**, and add a §11 item requiring the Stage-C exception →
outcome conversion. *Cost:* deciding *which* outcome. `INCONCLUSIVE-BY-POWER` is a power statement
and a degenerate calibration bin is not a power failure; `INCONCLUSIVE-BY-CALIBRATION` is closer but
is currently tied to the `a_LB_b < 0.85` test. Either choice stretches an existing code's meaning.

**B. Introduce one named outcome for pre-unblinding numerical failure**, covering Row F and the
Stage-C exception path. *Cost:* this is very close to the code just deleted under option D, and would
read as reversing that ruling three drafts after making it — **though on a different ground, since
the defect is now a real unterminated branch rather than a redundant claimant.** That distinction is
exactly the kind a future reader will not reconstruct, so it would have to be recorded loudly.

**C. Leave both branches unterminated and record the gap.** *Cost:* §6.3(10) is violated in the text
and the document knows it, which is honest but leaves clause 10 unexecutable — and clause 10 gates
BS-6.

## My reading, not my decision

**A if a single existing code can honestly cover both branches; otherwise B.** I lean A, because
adding a code so soon after deleting one invites exactly the misreading the V46 record was written to
prevent. **But I do not know which existing code is honest here**, and choosing one because it is
cheaper is the failure mode I have already produced twice today on this exact question.

**What I am confident of:** Row F's FAIL branches are unterminated, that is a real §6.3(10) violation,
and it predates all of this work.

## Status

- **V47** (`bc0fd1f0aa9537f2`) retracts the false argument and records the gap as UNRESOLVED. It does
  **not** repair the branches. Checkers: 16/8 prose-matched, trace 46 transitions 0 problems,
  `void_registry` 6/0, lint exits 0.
- **BS-6 and the first image byte remain blocked.**
