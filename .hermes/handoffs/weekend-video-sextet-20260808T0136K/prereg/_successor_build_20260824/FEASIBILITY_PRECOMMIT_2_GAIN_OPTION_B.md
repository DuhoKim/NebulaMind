# SECOND PRE-COMMITMENT — the option-B retry, written before the sweep

**Duho ruled 2026-08-29 20:20: retry it properly, with the positive control stated first.** The first
attempt's defects were in my harness, not in the question. This file is committed **before** the retry
runs; if it and the result disagree about meaning, this file was written blind.

## Answering the question Blanc asked, because it determines the design

At the real N with a null signal I found `|Â| + 3σ = 0.04152` against `A_LONGO = 0.0408`. Blanc read
that as correct — a null fixture *should* fail to reject. **That reading is half right, and the other
half matters.**

`REJECTED-AT-LONGO-AMPLITUDE` means *the measurement rules out Longo's amplitude*. **A null sky SHOULD
reject, if the measurement is precise enough** — that is what a rejection branch is for. At this N,
**`3σ = 0.0312`, comfortably below `A_LONGO = 0.0408`.** So rejection is reachable **by design**; that
particular draw missed only because its realised `|Â| = 0.0103` consumed the remaining margin.

**So the closeness of 0.04152 to 0.0408 is not a property of the design. It is one fluctuation.** The
design property is `3σ < A_LONGO`, which holds with ~24% headroom. **A null fixture whose realised
`|Â| < 0.0096` will reject**, and that is the positive control the retry needs.

## The positive control, fixed now

1. **Baseline: `REJECTED-AT-LONGO-AMPLITUDE`**, not the absorbing `INCONCLUSIVE`.
2. **Constructed from a NULL sky** (`A_inj = 0`) at the production N = 49,211 — not from a tuned
   signal.
3. **Seed selection rule, stated so it cannot be gamed:** take the **first** seed in ascending order
   whose baseline verdict is `REJECTED-AT-LONGO-AMPLITUDE`. **Selection is on the baseline criterion
   only and is blind to the sweep result.** I will report which seed and how many were tried.
4. **`n_perm = 5000` → p floor `1/5001 = 2.0e-4`.** `REPRODUCED-LONGO` needs `p < 0.001`, so the floor
   sits **5× below** the strictest threshold and **no verdict is foreclosed**. (First attempt:
   `n_perm = 400`, floor `2.5e-3`, which foreclosed `REPRODUCED-LONGO` outright.)

## The deletion probe, before the sweep is trusted

**A sweep never shown to fire is the same object as a control that cannot fail.** Before reading any
result, the harness must demonstrate it can report a verdict change:

> Evaluate the chosen baseline, then evaluate a fixture constructed to sit in a **different** verdict.
> **If the harness does not report two different verdicts, the retry is void and I stop.**

The first attempt could not have detected fragility however fragile the gate was, and nothing in the
run said so. This is the check that would have caught it.

## The reading, unchanged from the first pre-commitment

`f*` is the smallest adversarial flip fraction at which the verdict changes.

| outcome | reading |
|---|---|
| **f\* ≥ 0.10** | B is viable as a gate. |
| **0.01 ≤ f\* < 0.10** | MARGINAL — B is a gate but its passability depends on γ's bound, which must be measured before B is frozen. |
| **f\* < 0.01** | B is not a gate; A becomes the live candidate and its seed policy the next question. |
| **no change at f ≤ 0.50** | Report as such; **do not read as strength** — beyond half the signs the construction stops being adversarial. |

## If no valid baseline is constructible

**That is a result and I report it as one, and stop.** It would mean B's passability may not be
checkable before the study runs — making *"is B a gate?"* **undecidable at freeze** rather than merely
unanswered, which is a real argument about B. **I will not manufacture a cooperative fixture to avoid
saying that.**

**Unchanged:** the mapping is the principal's; A's seed policy is his if A becomes live; option C stays
rejected and visible; **v9 stays frozen at `6a9abbbd`**; BS-3g stays DESIGN/UNFILLED. **Not evidence
about the sky** — synthetic fixture, no real χ, γ̂ unmeasured.
