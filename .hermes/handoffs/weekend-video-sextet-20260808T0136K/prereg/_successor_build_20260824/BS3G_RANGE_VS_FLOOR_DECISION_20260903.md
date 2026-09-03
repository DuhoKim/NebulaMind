# BS-3g — THE RULED SWEEP RANGE MEETS THE CALIBRATION FLOOR (Hwao, 2026-09-03 15:2x KST)
For Duho, via Blanc. Plain words; digits. Evidence first, options last. Nothing here changes frozen text.

## What happened
BS-3g is the sensitivity-gradient control: it re-runs the frozen decision 99 times per gradient value across
51 gradient values (−0.25 … +0.25 in steps of 0.01), on the FROZEN FIXTURES, and asks whether the verdict
stays what it was at gradient 0. You ruled every parameter of this sweep on 08-29/30 (range ±0.25 in 50
steps; 99 draws; "real gate"; worst case over draws). The build ran it today, exactly as ruled.

**Result: a verifier-valid FAILED receipt** (`run/classp_candidates/BS-3g.json`, deterministic across two
runs, committed 6f49416c7).

| quantity | value |
|---|---:|
| cells in the sweep | 5,049 (99 draws × 51 gradients) |
| cells that stop with INCONCLUSIVE-BY-CALIBRATION | 4,752 (99 × 48 columns) |
| gradient columns that hold the gradient-0 verdict | 3 of 51 (gradient 0 and its two neighbours, ±0.01) |
| lowest calibration lower bound reached | 0.6950 (floor is 0.85) |

Why: under the ruled mapping the per-bin accuracy becomes a(c) = a₀ + γ·(c − c̄). With the fixture's own
accuracy sitting near the floor and c spanning about 1, any |γ| ≥ 0.02 pushes at least one bin below 0.85,
and the frozen text then halts that cell as INCONCLUSIVE-BY-CALIBRATION before any statistic. So 48 of 51
columns cannot hold, and the invariance test reduces to FAILED. This is not a bug: the second seat read the
frozen text and confirmed an inconclusive cell is a recordable outcome (reading (i), ACCESS PROVEN); the
text also says a FAILED BS-3g receipt "is a TRUE RECORD THAT BLOCKS … and goes to the principal". Here it is.

## What it means
The ratified ±0.25 range and the 0.85 calibration floor were never compatible with each other on these
fixtures: the range asks the control to probe gradients ten times larger than the floor permits. BS-3g
therefore blocks BS-6 (the first image byte) as written. The flagship data, the instrument, the blind: all
unaffected. What is affected is one control's parameter, ruled before the arithmetic was run.

## Your options
(a) **Narrow the sweep range to what the floor admits** — an amendment (V137) re-ratifying Γ (the receipt
    says ±0.01 holds; the referee will state the admissible bound); n_steps stays 50; everything else as
    ruled. Cost: one text round + referee + your sentence. Keeps the control real.
(b) **Keep ±0.25 and change what an inconclusive cell counts as** (e.g. treat calibration-halted cells as
    "not evidence against invariance"). Cost: a design amendment to §11's reduction; a hostile referee
    will call it softening the gate. Not recommended.
(c) **Accept the FAILED receipt as the control's verdict** — BS-3g stays blocked; the flagship image half
    does not start until a successor design. Cost: the flagship waits.
(d) **Hold** — decide after seeing the referee's hand-computed admissible bound (running now).
Recommendation: (a), with the exact bound taken from the referee's report, not from me.

## Status of the tooling
The producer/verifier/receipt are under hostile referee through nm_referee_dispatch.sh (verdict pending);
V137 is NOT drafted until that referee returns and you rule. No pixel opened. Pinned/signed files unchanged
(P0 manifest 30/30).

## Referee update (15:18 KST, ACCESS PROVEN — AGY_BS3G_BUILD_REFEREE_20260903.md)
Tooling: **PINNABLE**. Receipt: **VALID-FAILED-RECORD**, 55/55 tests. The referee recomputed the evidence by
hand from the fixture's own accuracy (a_hat = 0.88) and spread: at γ = ±0.01 the lowest bin bound is 0.8534
/ 0.8535 (holds, above 0.85); at γ = ±0.02 it is 0.8468 (fails). So on these fixtures the admissible sweep
range is exactly **|γ| ≤ 0.01 — 3 of the 51 ruled columns** — a property of the fixture's accuracy sitting
0.03 above the floor, not a bug. Option (a) with Γ = 0.01 and n_steps = 50 would sweep Δγ = 0.0004; whether
that still tests what §1 wants the control to test (a sky-gradient in sensitivity of the size the estimator
can resolve, σ_γ = 0.057 in this receipt) is the scientific question your ruling decides.
