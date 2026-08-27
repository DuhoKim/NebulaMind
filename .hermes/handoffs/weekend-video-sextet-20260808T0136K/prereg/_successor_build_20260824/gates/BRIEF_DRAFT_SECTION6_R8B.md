# REPAIR PASS — R8b. You invented three numbers. Replace them with the frozen ones.

`SECTION6_DRAFT_AGY_R8.md` (sha256 `f3d4509bb4d45b4b84ebee361f30166332a348f15f207dab0e114c9c2a7b96ad`)
did the structural work well and it stays. Eight named terminal states with precedence, one fixed
consequence each, the canonical post-unblinding adequacy receipt, the disposition split, the §4/§5
conforming edits, the false BS-5f sentence removed. **Do not redo any of that.**

## The defect

Row P states three numeric predicates:

> calibration fails if the empirical error bound ε ≥ 0.1 or sample size < 400
> power fails if re-run Stage C power < 0.8

**None of those three numbers exists in the frozen record.** They were not carried from anywhere;
they were composed. A preregistration that invents its own decision thresholds is worse than one
that leaves them open, because it looks binding and is not — and a reader would be entitled to
assume they came from the pinned code.

This is the most serious kind of error available in this document, and it is quiet.

## The actual values, cited so you can verify them yourself

**Calibration** — `../PREREG_SUCCESSOR_DRAFT_V15_20260827.md` lines 566–567:

> `max_b |â_b − â| ≤ 0.03` AND every `a_LB_b ≥ 0.85` → scalar path; spread failure only →
> profile path; any `a_LB_b < 0.85` → **INCONCLUSIVE-BY-CALIBRATION, pre-unblinding halt.**

So the calibration predicate is the **per-bin accuracy lower bound against the floor 0.85**
(`A_FLOOR = 0.85`, `../ref/successor_ref_v9.py` line 81), with a **separate spread test at 0.03**
that selects the scalar or profile path rather than failing the run. There is no ε threshold and no
sample-size threshold. `ε̂` appears in the inherited HC-1H estimator `a = (raw − ε)/(1 − 2ε)` — it
is an **input to the accuracy estimate, not a gate**.

**Power** — `../ref/successor_ref_v9.py` lines 77–78:

    N_TRIALS  = 1_000
    CP_PASS_X = 962

The criterion is **at least 962 passing trials out of 1,000**, not a 0.8 power figure. Note also
`PWR_CONSERVATISM = 1.01` (line 93), which inflates the measured critical value so the decision is
conservative by construction. Your 0.8 is a materially weaker gate than the code implements.

## What to do

1. **Replace the three invented predicates** with the frozen ones above, cited in the text by file
   and line so the next reader can check them without trusting either of us.
2. **Preserve the structure** — the precedence order, the state names, the receipt binding, the
   unconditional `INCONCLUSIVE-BY-CALIBRATION` when a removal takes out an allocated committee
   member. Only the numbers and their predicate forms change.
3. If re-running Stage C post-unblinding means the 962/1000 criterion **cannot** be applied as
   written — for example because the trial structure differs after attrition — **say so explicitly
   and name what would have to be defined**, rather than substituting a number that can be applied.
   A stated gap is a result. An invented threshold is not.
4. In Part 3, record that these values were carried from the frozen record rather than chosen, and
   name the file and line for each.

## Deliverable

`SECTION6_DRAFT_AGY_R8B.md` here — complete, self-contained, five parts, not a diff.

Do not modify the preregistration. Do not read `/Users/duhokim/NebulaMindData/`. Nothing is
authorised to fetch.

**Composing a number that looks inherited is the most serious form of renaming a finding.** If a
value you need does not exist in the frozen record, the honest output is to say it does not exist.
