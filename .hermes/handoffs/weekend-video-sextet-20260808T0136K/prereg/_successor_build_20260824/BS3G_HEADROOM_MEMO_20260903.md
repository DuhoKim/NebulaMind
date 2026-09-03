# BS-3g — would a fixture with more headroom let the control test a real-size tilt? (Hwao, 2026-09-03 17:5x KST)
Answer to Duho's question via Blanc. Measured, not extrapolated: the ruled 99 × 51 sweep was re-run on synthetic
fixtures differing from the frozen one ONLY in injected calibration accuracy (gates/bs3g_headroom_experiment/,
marked NOT A RECEIPT; nothing pinned or signed was touched). Digits below are the experiment's.

**Short answer: YES. With the fixture's accuracy at 0.95 instead of 0.88, the control can probe a tilt of
|γ| ≈ 0.12, about 2.5 times the estimator's resolution (σ_γ ≈ 0.048), without tripping the 0.85 floor.
At 0.88 it can probe only 0.01, about 0.18 σ — no real test.**

| fixture accuracy a_hat | widest tilt that holds (measured) | in units of σ_γ | cells inconclusive over ±0.25 | verdict of the full ±0.25 sweep |
|---:|---:|---:|---:|:---|
| 0.88 (frozen fixture) | 0.01 | 0.18 | 94 % (4,752 / 5,049) | FAILED |
| 0.90 | 0.04 | 0.74 | 82 % | FAILED |
| 0.92 | 0.07 | 1.36 | 71 % | FAILED |
| 0.95 | 0.12 | 2.51 | 51 % | FAILED |
| 0.98 | 0.16 | 3.56 | 35 % | FAILED |

The measured edges match the mapping arithmetic a(c) = a₀ + γ(c − c̄) to within one grid step (analytic
0.015 / 0.045 / 0.076 / 0.121 / 0.167). Two facts follow. First, NO realistic fixture supports the ratified
±0.25: even at 0.98 the sweep fails above 0.16, so the ±0.25 range was a ruling made before the arithmetic
existed, on any fixture. Second, the floor is the binding constraint, not the estimator: γ̂ is 0 to machine
precision on every fixture (the verdict is tilt-invariant where the floor lets it run), so the control's
question is answerable wherever the floor admits a real-size tilt.

## What the fixture would be
The same frozen generator, same sample, same c-spread, same seed/draws, with the injected calibration
accuracy set to 0.95 instead of 0.88 — one parameter. The frozen fixture battery of the instrument
(successor_ref_v9 --fixtures) is untouched; BS-3g's fixture is the control's own synthetic sky.

## Is it legitimate under the frozen text?
The BS-3g slot is a DESIGN slot being filled now, not a P0-signed value. Its "fixture a_hat" is one of the four
conventions the principal "Confirmed as committed" on 08-29 for the fixture-scoped fill. Changing it is therefore
a design choice that belongs to you, made in the same amendment that sets Γ (V137), with the same disclosed diff
and referee — not a successor-design item. What it does NOT change: the real instrument's accuracy (~0.88 on the
frozen fixture), the real run's calibration floor (checked at BS-8f / Stage C, unchanged), the blind, any pin.

## What the control then actually tests
With a_hat = 0.95 and Γ = 0.10 (2 σ_γ, inside the measured 0.12 edge with margin), BS-3g tests whether the
frozen decision is invariant to a sky-gradient in sensitivity of a size the estimator can actually resolve — the
threat §1 names. It tests the pipeline's response to a tilt, not the real instrument's floor headroom; that
headroom is precisely what the FAILED receipt on the 0.88 fixture already documents, and it stays on the record.

## Cost
One text round (V137 variant: Γ = 0.10, Δγ = 0.004 at n_steps 50, fixture accuracy 0.95, nothing else), one
fresh sweep (~10 min, then the PINNABLE verifier), one dispatcher referee, your one sentence: ~1 h.

## Options
(i) sign V137 as it stands (Γ = 0.01, fixture 0.88): honest but nearly toothless — a 0.18 σ test.
(ii) V137-H: fixture accuracy 0.95, Γ = 0.10: a real-size tilt test. Recommended.
(iii) both: sign (i) now, add (ii) as V138 later. Costs a second signature for no scientific gain.
V137 stays HELD at SIGNABLE until you choose; (ii) is a re-draft of the same amendment, not a new chain.

## Provenance precision (added after reading the experiment record)
The frozen fixture is built by `ref/gain_counterfactual_path.py::_fixture(n=240, seed=7)`, a P0-SIGNED file
(sha 92cbbdf8…) that stays byte-untouched under every option. The headroom variant does not edit it: the
unpinned BS-3g producer supplies the calibration accuracy a₀ used by the mapping a(c) = a₀ + γ(c − c̄) (the
experiment copy applied exactly that shift, sha 708da93d…). V137-H would state a₀ = 0.95 as a BS-3g design
parameter with its derivation, and the PINNABLE verifier recomputes the matrix from it. Experiment runtime:
56.5 min for the five fixtures (the 0.95 sweep alone took 16.6 min).
