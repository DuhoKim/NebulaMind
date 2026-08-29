**STATUS: VALID RUN. f\* ≈ 0.0007 → by the pre-registered reading, B IS NOT A GATE.** Read with
`FEASIBILITY_PRECOMMIT_2_GAIN_OPTION_B.md`, committed blind at `13e48e3c4`.

# Option B feasibility, retried properly — the result, then the reading

## The positive control held, and the deletion probe passed

- **Baseline `REJECTED-AT-LONGO-AMPLITUDE`** — not the absorbing outcome. Null sky (`A_inj = 0`) at
  the production **N = 49,211**. **Seed 1, the first tried**, by the pre-committed ascending rule;
  selection was on the baseline criterion alone and blind to the sweep.
- **`n_perm = 5000`, p floor `2.0e-4`** — five times below `REPRODUCED-LONGO`'s 0.001, so **no verdict
  was foreclosed.** (First attempt: floor `2.5e-3`, which foreclosed it outright.)
- **Deletion probe PASSED before anything was read:** baseline `REJECTED-AT-LONGO-AMPLITUDE`, probe
  fixture `INCONCLUSIVE` — the harness demonstrably reports verdict changes. The first attempt never
  showed this and could not have.

## The result

    k       f          verdict                        |Â|+3σ
    0       0          REJECTED-AT-LONGO-AMPLITUDE    0.03531
    20      0.000406   REJECTED-AT-LONGO-AMPLITUDE    0.03859
    49      0.000996   INCONCLUSIVE                   0.04333   <- verdict changes

**f\* lies between 0.000406 and 0.000996 — between 20 and 49 flipped signs out of 49,211.**

## The reading, as pre-registered

**`f* < 0.01` → "B is not a gate; A becomes the live candidate, and its seed or quantile policy
becomes the next question."** f\* is **roughly ten times smaller** than that threshold. The reading is
not close to a boundary and does not depend on where in the 20–49 interval f\* falls.

**Twenty to forty-nine signs out of forty-nine thousand overturn the verdict.** An adversarial
construction defeats this gate at any bound on γ that is not essentially zero, so B cannot discharge
the control it was selected to carry.

## Why this happens, since the number alone is not the finding

The rejection branch requires `|Â| + 3σ < A_LONGO`, and the baseline sits at **0.0353 against 0.0408
— a margin of 0.0055**. The adversarial flip attacks exactly that margin, and each flipped sign moves
`|Â|` by roughly `2/(N·Var(c))` in the worst direction. **The margin is thin because the design is
close to its own rejection threshold, which is the same closeness Blanc asked about earlier today.**

**So the two observations are one observation.** The near-miss at `0.04152` vs `0.0408` was not a
fluke of one draw: it is the same small margin that makes an adversarial construction cheap. **A gate
built on that margin is fragile by construction, not by accident.**

## What this does and does not license

**Does:** by the pre-registered table, **B is not a gate**, and **A is the live candidate**.

**Does not:** select A. **The mapping choice remains the principal's**, and if A becomes live its
**seed or quantile policy** is the next question — the thing I called innocuous-looking and
outcome-deciding, and still is.

**Not evidence about the sky.** Synthetic null fixture, no real χ, γ̂ unmeasured. This is a property of
the **gate design**. **v9 untouched at `6a9abbbd`.** **Option C stays rejected and visible.** BS-3g
stays DESIGN/UNFILLED; BS-6 and the first image byte remain blocked.

## One caveat I will not leave implicit

**This is one fixture at one calibration.** The margin `A_LONGO − 3σ` depends on N and on the
calibration accuracy; a different calibration widens or narrows it. The conclusion that B is not a
gate follows from a margin thin enough that ~30 signs cross it, and **that margin should be
re-derived at the real calibration before B is finally discarded.** The result is decisive as
pre-registered; it is not the last word on the design.
