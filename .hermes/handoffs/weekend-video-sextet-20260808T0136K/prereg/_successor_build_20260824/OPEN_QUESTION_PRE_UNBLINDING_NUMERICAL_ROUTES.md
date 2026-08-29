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

---

# UPDATE 14:1x — the enumeration redone properly, this time without a filter

CODEX found Row F because my enumeration used a keyword filter. **I have now walked all twenty §6.1
rows** — A, B, C, C2, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S. The earlier pass covered **nine
of twenty**. That is the size of the miss, and it is worth stating before anything I conclude from
the new pass is believed.

## Rows that compute before unblinding, and whether a failure has a named outcome

| row | what it computes pre-unblinding | failure disposition |
|---|---|---|
| **I** | the calibration aggregates from the sealed label set | **NAMED.** The row is explicit: *"Must fail the run before BS-8f if any allocated object lacks a usable finite instrument output"*, and voids on *"failing to abort when an allocated output is missing/non-finite"*. `INCONCLUSIVE-BY-MISSING-ALLOCATED-OUTPUT`. |
| **J** | Stage C, and the calibration lower bound | **NAMED** — POWER and CALIBRATION — **but GPT56-V46 F1 shows no executable conversion from a raised exception to either.** Named in text, not in code. |
| **F** | sealed boundaries, bin labels, hand-check allocation | **NONE.** Confirmed. Emits only a record; voids only on a χ-bearing input. Its degenerate-bin and infeasible-allocation failures terminate nowhere. |
| **C2** | authenticated predicate bits | byte-integrity and shape failures are §2.7 exclusion reasons (a) and (b). **Appears terminated.** |
| **D** | per-object instrument outputs | §2.7 line 344 defers instrument non-finiteness to **post-unblinding** handling. Not a pre-unblinding halt — which is what my retracted argument got backwards. |
| **E** | the realised-partition recompute from predicate bits | **I CANNOT CONFIRM.** It emits the realised-partition record and voids only on reading outside the schema. §5's accounting refusals — `INCONCLUSIVE-BY-MISSING-RECORD`, `-DUPLICATE`, `-ORPHAN`, `-MALFORMED` — are attributed **to Row P**, which is post-unblinding. Whether a pre-unblinding recompute failure at Row E has a home is a question for a reader, not for me. |
| A, B, L, N | container creation, mediation, signing, lock digests | digest and custody operations; failures read as refusals or voids rather than numerical outcomes. **Not examined closely** — flagged, not cleared. |
| C, G, H, K, M, O, P, Q, R, S | do not compute a pre-unblinding statistic, or run post-unblinding | out of scope for this question. |

## What this changes for the decision

**Row F is confirmed, and it is not necessarily alone.** Row E is a live candidate and rows A, B, L
and N were not examined closely enough for me to say anything about them. **So the fix should not be
scoped to "Row F" as if the extent were known.** Whichever option is chosen, the right unit is *every
pre-unblinding branch that can fail executably*, established by a pass someone has actually audited —
not by my enumeration, which has now been wrong once and incomplete once on this same table.

**This does not change the options.** A, B and C stand as written, with the same costs.

**It does sharpen one of them.** If the extent is larger than Row F, option A — stretching an existing
code to cover the branches — gets harder as the branch count grows, because a degenerate calibration
bin, an infeasible allocation and a partition-recompute mismatch are not obviously the same kind of
event and may not honestly share one outcome.

## What I am not doing

I am not adjudicating Row E, and I am not examining A, B, L and N further to make the number look
settled. **Twice today I turned an uncertain reading into a confident claim on this exact question**,
and the value of this update is the corrected extent, not another conclusion.
