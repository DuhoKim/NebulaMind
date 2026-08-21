# Build spec — the verdict estimator. Must be written and FROZEN before the sample completes.

Hwao, 2026-08-21 15:41 KST.

## Why this is urgent rather than merely pending

Searched the lane for any implementation of F-3 through F-7. **There is none.** The decision
regions REPRODUCED-LONGO, REJECTED-AT-LONGO-AMPLITUDE, INCONCLUSIVE and INCONCLUSIVE-BY-POWER
exist **only in Markdown** — in the frozen preregistration and the gate files. `spike/sim_power.py`
simulates power; nothing computes a verdict.

So the single piece of code that turns 208,407 chirality values into an answer does not exist,
five days before the values are all there.

**It must be written now, and the reason is not scheduling.** Writing analysis code after the data
is available is precisely what preregistration exists to prevent. Right now we are in the only
window where it can be written honestly: the values exist but the authorization forbids anyone
computing any aggregate over them, so the code can be built and validated against synthetic sky
realizations with no possibility of contamination. That window closes the moment the sample
completes.

**Therefore the deliverable is not just working code. It is code frozen at mode 444 with its
SHA-256 recorded before the first aggregate is ever computed** — the hash is the evidence that the
analysis predates the data, and it is worth more to a referee than the code's elegance.

## Frozen inputs (quoted from PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md — do not restate from memory)

- **F-3 Null.** Label-permutation, **N_perm = 100,000** over fixed positions and footprint.
  One-sided p at Longo's sign.
- **F-4 sigma definitions.** sigma_D = sqrt(1/(3*N_accepted)); sigma_ours = 3*sigma_D/(2a-1);
  sigma_comb = sqrt(sigma_pub^2 + sigma_ours^2) with sigma_pub = 0.011.
- **F-5 Sign.** In our East-of-North winding convention the target is **A(n_L) = +0.0408**.
  The mandatory synthetic absolute-sign anchor is already satisfied
  (`YUI_BS5_SIGN_ANCHOR_20260814.md`, gated `KUN_BS5_ANCHOR_GATE_20260814.md`, both 14 Aug —
  verified today as predating K-8).
- **F-6 Decision regions.**
  - REPRODUCED-LONGO: p < 0.001 AND sign per F-5 AND |A_c - 0.0408| <= 3*sigma_comb
  - REJECTED-AT-LONGO-AMPLITUDE: p > 0.05 AND (|A_c| + 3*sigma_ours) < 0.0408
  - INCONCLUSIVE: any other numeric outcome, or any triggered INCONCLUSIVE rule in section 4/6
  - INCONCLUSIVE-BY-POWER: declared **before unblinding** if the power gate fails; no run
- **F-7 Effective detection floor.** One-sided floor 3.09*sigma_ours on A_c. No A_c below the
  **evaluated** floor may be called REPRODUCED regardless of the band, and the evaluated floor is
  printed in the results table.
- **Power gate.** N_accepted >= 100,000, a >= 0.85.
- Axis: Longo's, frozen, (RA, Dec) = (216.9844, +32.0606).

## What to build

`_verdict_20260821/verdict_runner.py`, following the gating pattern of
`_inference_20260820/inference_runner.py` exactly:

1. **Refuses real data without `--authorization`** pinned to a SHA-256, same as the inference
   runner. A separate authorization will be required to run it, and that authorization does not
   exist yet and must not be written yet.
2. **Refuses to run at all unless the sample is complete** — every one of the 208,407 parent
   objects must have a chi receipt. A partial run is not a smaller run; it is a different
   experiment, and the authorization's condition 1 forbids it.
3. Acceptance is `|chi| > tau` with tau = 4.4006456017494235, read from the frozen receipt, never
   hardcoded a second time.
4. Computes A_c at the fixed axis, the 100,000-permutation one-sided p, all three sigmas, the
   evaluated floor, and emits **exactly one** of the four verdicts. No verdict may be computed by
   a human reading a number off a table.
5. Emits the F-10 aggregate artifact set (P1-P10, S1-S5). Per-object files stay hash-committed and
   undistributed.

## Validation, before any gate

Synthetic sky realizations only, with injected amplitudes, at the frozen N and a:

- A = 0 must return REJECTED-AT-LONGO-AMPLITUDE or INCONCLUSIVE, and must **never** return
  REPRODUCED. Run this many times; a single false REPRODUCED is a build failure, not a tuning
  problem.
- A = +0.0408 must return REPRODUCED-LONGO at the frozen power.
- A = -0.0408 must **not** return REPRODUCED. This is the sign test, and it is the one most likely
  to be silently wrong — an inverted convention passes every other check in this list.
- A just below the evaluated floor must not return REPRODUCED even when the band would allow it.
- N_accepted = 99,999 must return INCONCLUSIVE-BY-POWER and refuse to proceed.

## Gate

Adversarial, by an engine that did not write it, against the frozen preregistration text rather
than against this spec — this spec is a convenience and carries no authority. One deliverable per
gate; the 67-minute combined gate on 20 Aug is the reason.

On PASS: chmod 444, record the SHA-256 in a freeze note, and state in that note that no aggregate
over chi had been computed at the time of freezing. Then it sits untouched until the hand-check is
done.

## What this spec does NOT authorize

Running it on real chi. Computing any aggregate, tertile or summary. Writing the run
authorization. Those are separate, later, and Duho's.
