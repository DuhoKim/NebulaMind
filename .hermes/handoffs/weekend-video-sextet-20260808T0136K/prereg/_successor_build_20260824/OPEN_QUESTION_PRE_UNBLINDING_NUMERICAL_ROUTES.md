**STATUS: OPEN** — with the principal. Ruled option A 14:32; **A failed on its own terms** (no existing outcome honestly covers the branches), so it is back for a B-shaped decision.

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

---

# OPTION A HAS FAILED ON ITS OWN TERMS — 2026-08-29 14:3x

**The principal ruled option A: reuse an existing outcome if one honestly fits. Blanc's condition was
that A is a preference and not an instruction to succeed — if no existing code honestly covers the
branches, say so and stop rather than force the fit. Having done the work: no existing code covers
them, and the answer is B.**

## First, the question that was actually answerable

**Is `INCONCLUSIVE-BY-CALIBRATION`'s tie to `a_LB_b < 0.85` definitional or incidental? INCIDENTAL.**
The code already has **three** producers, and the third is independent of the threshold:

> produced by Row J pre-unblinding, pre-verdict validator post-unblinding removal, **or aggregate
> non-finite/degenerate failures excluding Row-I's missing allocated outputs — validated by
> `validate_calibration_aggregates` before the `< 0.85` comparison**

So the threshold is one producer among three, and the code already claims non-finite/degenerate
failures **evaluated before** it. That was the right question to ask, and it does not settle in A's
favour.

## Why it still fails

**The third producer is scoped to *aggregates*, not to bins or allocation.** §11's own item reads
*"Implement `validate_calibration_aggregates` to validate calibration **aggregates** as finite and
non-degenerate."* Aggregates are Row I's product at BS-8f. **Row F's failures are upstream of that**
— sealed boundaries and the hand-check allocation, at P3/BS-2f.

Applying the test — *a reader who knows only the outcome's definition would correctly predict this
branch produces it*:

| branch | verdict |
|---|---|
| **degenerate calibration bin** | **The name fits; the definition does not.** A reader told "inconclusive by calibration" would guess it; a reader told the *definition* — a named validator, operating on aggregates, before the `< 0.85` comparison — would not, because a bin is not an aggregate and P3 is not BS-8f. Covering it means widening the producer from aggregates to the whole calibration chain and from BS-8f back to P3. **That is stretching, which is precisely what was ruled out.** |
| **infeasible hand-check allocation** | **Fails outright.** It is not an aggregate, and it is not non-finite or degenerate. It is a feasibility failure. No reading of the definition predicts it. |
| checked and rejected | `INCONCLUSIVE-BY-POWER` fails on its face. `INCONCLUSIVE-BY-MISSING-ALLOCATED-OUTPUT` is Row I's *missing output after allocation*, not a *failed allocation*. The accounting refusals are Row P and post-unblinding. |

**So A fails on its own terms, and I am reporting that rather than forcing the fit. The answer is B.**

## Third: Row F is not alone, and the gap is systemic

The mechanical prose pass **cannot find Row F** — its failure modes are not in the row's prose at
all, they are in the code. That is the defect. So the honest axis is the executable one, and on that
axis the frozen reference says:

    111  raise sites in successor_ref_v9.py
      3  raise a TYPED outcome exception  (2 InconclusiveByPower, 1 InconclusiveByCalibration)
     69  raise a bare RuntimeError/ValueError
      2  exception classes correspond to a named outcome at all

**GPT56's finding generalises far past Stage C.** Almost nothing in the pinned code converts a raised
exception into a named outcome, so "the route is named in §5" and "the route is executable" come
apart across the whole reference, not at one row.

**What I am NOT claiming:** that all 69 untyped raises are §6.3(10) violations. Many guard
inadmissible input — a malformed mask, a wrong-shaped vector — which is a caller error rather than a
run outcome, and does not need an INCONCLUSIVE code. **Distinguishing the two requires reading each
site, which I have not done.** What is established is that the conversion layer is nearly absent, and
that Row F's branches are among the reachable ones — I triggered one myself today, unintentionally.

## What this means for the decision

**B, but scoped as a rule rather than as one code for Row F.** Adding a single outcome for Row F
would repair the instance the seats happened to name and leave the class open — the same mistake as
repairing findings one at a time instead of the defect generating them, which is the note this lane
has been carrying since the citation check.

**Still the principal's call**, and now materially different from the one he was given: A was ruled
against a two-branch problem, and the problem is a class with an unknown number of members.

## What I did that does not depend on the decision

**V48 adds the §11 conversion item.** A named outcome that nothing can produce is the defect a code
was deleted for this morning, one level down, and requiring the conversion is needed under A, B or
anything else.

---

# THE CLASS SIZED — 2026-08-29 14:4x. Row F alone is nine raise sites, not two branches.

I wrote that separating reachable failures from caller-error guards *"requires reading each site,
which I have not done"*, while asking the principal to choose against a class of unknown size. Done
now, to the extent it can be done without adjudicating each one.

## Row F is not two branches. It is at least nine raise sites.

    calibration_bins      L1369  degenerate calibration bins {sizes} — FAIL
    allocate_handcheck    L1397  stratum {j} needs {n} labels but only ...
    allocate_handcheck    L1401  inherited floors need {n} labels, budget {b} — FAIL
    allocate_handcheck    L1403  budget {b} exceeds available objects {n} — FAIL
    allocate_handcheck    L1411  floors exceed budget after the stratum lift — FAIL
    allocate_handcheck    L1435  no headroom remains to place the budget — FAIL
    allocate_handcheck    L1437  allocation {n} != budget {b} — FAIL
    allocate_handcheck    L1439  allocation exceeds available objects in a cell — FAIL
    allocate_handcheck    L1442  stratum {j} below floor after apportionment — FAIL

**All nine raise a bare `RuntimeError`. None converts to a named outcome.** "Infeasible hand-check
allocation" is not one condition — it is **eight distinct feasibility failures**, each with its own
cause: a stratum short of labels, floors exceeding budget, budget exceeding available objects, no
headroom, a cell over-allocated, a stratum under floor.

**This settles the A-versus-B question further than my last note could.** No single existing outcome
can honestly cover eight distinct feasibility conditions plus a degenerate-bin failure. Even a new
code would need to decide whether these are one outcome or several.

## The class, sized as honestly as a heuristic allows

Classifying the 108 untyped raise sites by what the guard tests:

    caller / input guard — a caller error, needs no run outcome     29
    reachable run-time failure — needs a named outcome              31
    UNCLEAR, requires reading                                       48

**Read these as bounds, not counts.** The classifier keys on the raise message, and the largest
bucket is the one it could not decide — so **the class is at least 31 and at most 79.** I am stating
it that way rather than picking the middle, because a confident number is exactly what I produced
twice today and had to retract.

## Two things visible in the residue that the pre-unblinding framing does not cover

- **`accuracy_from_handcheck`** (L1462–1468): empty calibration bin, agreement count out of range,
  epsilon out of range — Row I's calibration path, same pattern.
- **The decision path itself** — `_finite` (L1503), `w_profile` (L1513, L1517), `sigma_ours_scalar`
  (L1537), `sigma_ours_profile` (L1548, L1554) — raises bare errors on a non-finite decision
  quantity, a degenerate `c`, a vanishing profile factor, `2a−1 ≤ 0`, a negative quadratic form.
  **These are post-unblinding**, inside `_decide_from`, and equally unconverted. The question was
  framed as pre-unblinding; the defect is not confined to that phase.

## What I am not doing

Not adjudicating the 48, and not deciding whether the nine Row F sites are one outcome or several.
**Both are the substance of the pending decision, not inputs to it.**

---

# CORRECTION 15:1x — "nine raise sites" was raise-sites, not reachable branches

I wrote that **Row F is at least nine raise sites** and let that number stand as the scale of the
problem. It is the count of `raise` statements. **It is not the count of branches shown to fire**,
and the principal is being asked to decide against a scale, so the difference matters.

## What was actually tested

`allocate_handcheck` executed against **60,000 generated cell-count tables** at nine density scales,
with dead strata and dead bins injected, at the frozen constants (`N_CAL_BINS=3`, `N_HC_STRATA=9`,
`HC_MIN_PER_CELL=10`, `HC_MIN_PER_STRATUM=30`, budget `HC_REAL_LABELS=500`):

| site | status |
|---|---|
| `stratum {j} needs {n} labels but only {m} objects exist` | **REACHED** |
| `budget {b} exceeds available objects {n}` | **REACHED** |
| `stratum {j} below floor after apportionment` | **REACHED** |
| `inherited floors need {n} labels, budget {b}` | not reached |
| `floors exceed budget after the stratum lift` | not reached |
| `no headroom remains to place the budget` | not reached |
| `allocation {n} != budget {b}` | not reached |
| `allocation exceeds available objects in a cell` | not reached |

Plus `calibration_bins` → `degenerate calibration bins`, **reached** — I tripped that one by accident
earlier today, which is how Row F entered this question at all.

## The corrected number, and its limit

**4 branches are demonstrated reachable. 5 were not reached.**

**"Not reached in 60,000 random tables" is not "unreachable."** That is the absence direction, and
this document has been wrong in it repeatedly today. The five may be genuinely dead defensive checks,
or reachable only under structured inputs a random search does not produce — the function's own
docstring says feasibility is *decided before allocating*, which is exactly the design that would
make later guards hard to reach. **The search has a positive control** — three of the eight did fire,
so it is capable of finding these — but that makes "not reached" weakly informative, not conclusive.

## What this does and does not change

**It does not rescue option A.** The three reachable allocation failures are *different causes* — a
stratum short of objects, a budget exceeding total availability, and a stratum falling below floor
after apportionment. Together with a degenerate calibration bin that is **four distinct conditions**,
and no existing outcome honestly covers four distinct conditions any better than it covered nine.

**It does correct the scale I gave.** The honest statement is **"at least four demonstrated, with
five more of unknown status in this function alone"** — not "nine". I am correcting it before it is
decided from, because I have now had to retract two confident numbers today and would rather not
supply a third.
