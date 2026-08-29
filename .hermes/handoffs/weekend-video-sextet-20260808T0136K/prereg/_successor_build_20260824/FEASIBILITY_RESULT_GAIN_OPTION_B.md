**STATUS: RUN, AND THE CHECK IS INVALID AS CONSTRUCTED.** The passability question is **not**
answered. Read with `FEASIBILITY_PRECOMMIT_GAIN_OPTION_B.md`, committed blind at `950bcee34`.

# Option B feasibility — the pre-registered outcome, and why it cannot be read

## The pre-registered outcome, reported first and exactly as written

**No verdict change at any adversarial flip fraction f ≤ 0.50.** That is the fourth case of the
pre-commitment, whose reading was fixed in advance as: *"Report as such and do not read it as
strength."* I am reporting it as such, and it is not strength.

    baseline           INCONCLUSIVE   A_L = -0.05293   p = 0.6434
    f = 0.002 … 0.50   INCONCLUSIVE throughout; A_L drifts -0.053 → -2.005, p → 1.0000

## Why the number cannot be read at all — two defects, both in my harness

**1. The baseline verdict was the absorbing outcome.** `INCONCLUSIVE` is defined as *"any other
numeric outcome"* — the catch-all. An adversarial flip drives the estimate **further** into it. There
was nowhere to flip *to*, so the sweep could not have detected a change however fragile the gate is.
**A feasibility test whose baseline cannot change has no positive control**, which is the same defect
this lane spent two days removing from its checkers, arriving in an experiment instead.

**2. `n_perm = 400` made `REPRODUCED-LONGO` structurally unreachable.** Its exact one-sided p floor is
`1/(1+400) = 0.00249`, and `REPRODUCED-LONGO` requires **p < 0.001**. **The outcome was foreclosed by
a harness parameter before any data was involved.** Production uses `N_PERM = 100,000`. This is
precisely the mistake the seats caught six hours ago — I froze `budget` and read non-observation as
unreachability — repeated in a different parameter of a different harness on the same day.

## What I tried next, and what it establishes

I searched for a fixture with a **decisive** baseline, so the test would have a positive control:
N from 240 to 49,211, injected A from 0 to 0.08, several seeds, `n_perm` up to 4,000. **Every one
returned `INCONCLUSIVE`.** At the real N = 49,211 with a null signal, `|A| + 3σ = 0.04152` against
`A_LONGO = 0.0408` — **REJECTED-AT-LONGO-AMPLITUDE misses by 0.0007**. At A = 0.0408 the p-value is
≈ 0.012 with an adequate permutation count, well short of the 0.001 that `REPRODUCED-LONGO` needs.

**This is a limited search and I am not claiming decisive verdicts are unreachable.** What it
establishes is narrower and still useful: **a synthetic fixture that exercises the adversarial gate is
not trivially constructible**, and every attempt here landed in the absorbing outcome.

## What this means for the pending decision — and what it does not

**It does not answer whether B can pass.** The question I raised, and which the principal authorised
checking, is **still open**. Nothing here supports or undermines B.

**It does add one thing worth having:** if a valid positive control cannot be built without real
calibration and a real χ vector, then **B's passability may not be checkable before the study runs** —
which would make "is B a gate?" undecidable at freeze time, not merely unanswered. That would be a
real argument about B's viability, and I am flagging it as a possibility rather than asserting it,
because one afternoon's fixture search is not a proof.

**A valid attempt needs:** a baseline verdict that is **not** `INCONCLUSIVE`; `n_perm` large enough
that no verdict is foreclosed by the p floor; and both stated before the sweep, as the pre-commitment
required and as I failed to check.

## Standing

**Not evidence about the sky.** Synthetic fixtures, no real χ, γ̂ unmeasured. **v9 untouched at
`6a9abbbd`.** **The mapping choice remains the principal's**, as does A's seed or quantile policy if A
becomes live. **Option C stays rejected and stays visible.** BS-3g stays DESIGN/UNFILLED; BS-6 and
the first image byte remain blocked.
