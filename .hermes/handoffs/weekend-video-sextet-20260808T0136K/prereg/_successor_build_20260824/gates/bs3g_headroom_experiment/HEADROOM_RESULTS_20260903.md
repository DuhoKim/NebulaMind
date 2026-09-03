# BS-3g synthetic headroom experiment — NOT A RECEIPT

**EXPERIMENT ONLY. NOT PINNED. NOT A RECEIPT.** No science pixels or network were used. No frozen, signed, or pinnable file was edited.

## Method and provenance

The experiment used the untouched pinnable `gates/bs3g_producer.py` (SHA-256 `618767cd41e5283bdf736e30249ce2f0bdb180b4f0257e58e690bea58d3a18e6`) and its ruled values: Γ = 0.25, Δγ = 0.01 (51 grid points), 99 common-random draws, master seed 20260830, mapping A worst case, and option (b) real gate with 20,000 permutations. The pinned replay loader, counterfactual path, mapping, estimator, kernel, and verifier were used unchanged; the run completed its loaded-object census and post-run root re-verification.

The frozen fixture is made by `ref/gain_counterfactual_path.py::_fixture(n=240, seed=7)`, SHA-256 `92cbbdf89bd2a494c9cfb9f19fb12a46cf59a16731246cea2e74c56d2454a9b7`. It constructs the fixed 240-object sample with `c = linspace(-0.98, 0.98, 240)`, the seed-7 signs, and production tertile calibration bins. Its frozen `_CAL` has `a_hat = a_b = 0.88`, `a_lb = a_lb_b = 0.86`, and `cov_a = diag(0.0004)`.

The experiment copy is `gates/bs3g_headroom_experiment/headroom_experiment.py`, SHA-256 `708da93d40e302eec9cc88012c9816a7dc599329747773d8e4bfcf23195902ce`. For each requested `a_hat`, it applied the same additive shift to `a_hat`, every `a_b`, `a_lb`, and every `a_lb_b`. Thus it varied only injected calibration accuracy while preserving the frozen 0.02 lower-bound margins, zero c-profile spread, covariance, sample, c values, signs, boundaries, and bin labels.

The actual c range is [-0.98, 0.98], sample mean `c_bar = -1.1842378929335003e-16`, and per-bin means are `[-0.6519665271966528, 0.008200836820083586, 0.6601673640167361]`. The mapping's per-bin lower bounds therefore obey, before any irrelevant upper-side clipping,

`min_b a_lb_b'(γ) = a_hat - 0.02 - |γ| max_b |c_bar_b - c_bar|`,

with the actual bin-mean radius `0.6601673640167363`. Setting this equal to the frozen floor 0.85 predicts `|γ| <= (a_hat - 0.87) / 0.6601673640167363`, capped at Γ = 0.25. “Analytic” below is that continuous prediction; “measured” is the widest ruled grid magnitude for which both signs and all 99 draws avoid `INCONCLUSIVE-BY-CALIBRATION`. The sub-grid differences (0.00118–0.00662) are exactly the expected downward quantization to Δγ = 0.01, not extrapolated measurements.

## Results

| a_hat | admissible \|γ\| measured (analytic) | measured / σ_γ | inconclusive cells | min a_lb_b at γ=0 / at measured edge | γ_hat | σ_γ | invariance_outcome |
|---:|---:|---:|---:|---:|---:|---:|:---|
| 0.88 | 0.01 (0.015147674) | 0.176287 | 0.941176471 (4752/5049) | 0.860000000 / 0.853398326 | -1.114842498e-16 | 0.056725772 | FAILED |
| 0.90 | 0.04 (0.045443022) | 0.742260 | 0.823529412 (4158/5049) | 0.880000000 / 0.853593305 | -2.740546649e-19 | 0.053889484 | FAILED |
| 0.92 | 0.07 (0.075738370) | 1.363902 | 0.705882353 (3564/5049) | 0.900000000 / 0.853788285 | -2.542874166e-17 | 0.051323318 | FAILED |
| 0.95 | 0.12 (0.121181392) | 2.505127 | 0.509803922 (2574/5049) | 0.930000000 / 0.850779916 | -1.375288504e-18 | 0.047901763 | FAILED |
| 0.98 | 0.16 (0.166624414) | 3.562847 | 0.352941176 (1782/5049) | 0.960000000 / 0.854373222 | -8.831545916e-17 | 0.044907903 | FAILED |

All inconclusive cells were `INCONCLUSIVE-BY-CALIBRATION`; there were no other inconclusive tokens. Every full-grid `invariance_outcome` is `FAILED` because each ±0.25 sweep includes calibration-inconclusive cells, while the admissible values above report the requested largest symmetric, all-99-draw adjudicated sub-grid. The edge minimum is the smaller of the two signs at that magnitude.

Total measured wall runtime: **3391.570216 s (56 min 31.570 s)**. Per-fixture runtimes were 120.139 s, 361.924 s, 595.194 s, 993.984 s, and 1320.304 s in ascending `a_hat` order. Raw experimental output is `headroom_raw_NOT_A_RECEIPT.json` in this directory.

SEAT: CODEX
VERSION: BS3G-HEADROOM-EXPERIMENT-V1
ADMISSIBLE_GAMMA: 0.88=0.01 0.90=0.04 0.92=0.07 0.95=0.12 0.98=0.16
SIGMA_GAMMA_FROZEN: 0.05672577217492736
