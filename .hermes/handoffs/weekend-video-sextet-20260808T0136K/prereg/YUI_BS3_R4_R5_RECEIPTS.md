# Yui — BS-3 production-estimator R4/R5 receipts

**Run completed 2026-08-13 KST. Synthetic instrument probes only.** This receipt supplies the two production runs missing from `GORU_BS3_INVENTORY.md`: R4, the interpolating-mirror canary, and R5, the per-object paired outputs / raw-trunk flip imbalance. It is evidence for Kun's BS-3 re-gate, not a freeze or acceptance decision.

## Result first

- **R4: PASS — canary detects the forbidden interpolating mirror.** On the frozen 200-object production probe set, all **200 / 200** probes violated the bad-input identity by more than the preregistered `0.01` threshold. The absolute violation ranged from **0.0105876923** to **1.5070748329**; mean **0.3970843741**. The pass rule required at least one probe above `0.01`.
- **R5: dA_raw = +0.015.** Using the appendix formula `mean((sign(f(x)) + sign(f(mirror(x)))) / 2)`, the contribution sum was `+3.0` over 200 probes. Contributions were `0.0` for 197 objects and `+1.0` for 3 objects; there were no negative contributions. The complete paired raw outputs and derived fields are in `prereg/yui_bs3_r4_r5_20260813/paired_probe_records.jsonl`.
- **Production path remained exact:** pure index-reversal mirror involution was byte-exact **200 / 200**; production antisymmetry was value-exact and bit-exact on all **200 / 200** nonzero pairs; maximum `abs(chi(mirror(x)) + chi(x))` was exactly `0.0`; paired acceptance mismatches at frozen tau were **0 / 200**.

## Frozen-object preflight and closeout

The runner hashed the files themselves before loading the instrument and again after writing the new receipts. Every pin matched both times:

| Frozen object | Directly measured / verified value |
|---|---|
| Generator `spike/yui_identity/w_chi.py` | SHA-256 `89da33ec6260e75e06eadb0f171da4c52f1478b59ff5e543d363dbf56fefcd75` |
| Weights `prereg/weights_frozen.pt` | SHA-256 `83008c1cbdae511af5d30020540e1e281c62c2bd95d3cb05527fc0687bf49e6d` |
| Canonical little-endian float32 parameter serialization | SHA-256 `1075a4d91c295d7f3256128534a0b8c4d097fb9d162169df1ac698843637a589` |
| Frozen tau | `4.4006456017494235` |
| Null-set manifest | `null-8000`, N = 8,000, SHA-256 `1963132f2f36e7aa42b08012aad02d2c541d6c0973740a5bbce6a6e7a2904bd1` |
| Master seed | `LONGO-AMPLITUDE-FREEZE-M1` |
| `prereg/train_results.json` | SHA-256 `c36cd33001e432c60df786da8c0ff95b8ef5ab350a458b29d71ff084178a41fd` |
| Existing `prereg/receipt_results.json` | SHA-256 `d5d4a8bc005b031ed523e64a672237536896f37030722fd5cf71ff44a3405a04` |
| Corrected-retention machine result | SHA-256 `414fbc5cb6fa050390f0a6bca69e02e81795ed2a3585928be19767f4cb3a59e2` |

The state dict was loaded strictly into the original architecture without importing `yui_train_measure.py`, whose import would retrain. No frozen file was rewritten. There was **no retraining, no tau recalibration or retuning, and no training-set regeneration**.

## Probe-set identity

R4 and R5 used the same deterministic production probe set already used for R1/R2 in `yui_train_measure.py`:

- N = 200
- source indices = `3,000,000` through `3,000,199`, inclusive
- raster = `128 x 128`
- inference dtype = `float32`
- parameter and noise seeds = `SHA-256(M || index) mod 2^63`, with frozen master seed M above
- concatenated float32 image-hash manifest SHA-256 = `ab75d5f2ec08ad44fbcf1198d1612c23759f8d3aac29db044a181346ac43f9b2`

This run regenerated only these specified synthetic **probe images** from the frozen generator and seed policy; it did not regenerate or alter the frozen training set, null set, weights, or threshold.

## R4 — interpolating-mirror canary

The canary reproduced the appendix's deliberately forbidden mirror:

- `scipy.ndimage.affine_transform`
- reflection displaced `0.25` pixel from the array centreline
- bilinear interpolation, `order=1`
- `mode="nearest"`

For this canary only, define `m_bad` as that transform. As in the feasibility spike, the frozen production chi function retains its pure index-reversal mirror internally; the affine transform is supplied only as the deliberately bad input. The tested residual was:

`abs(chi_production(m_bad(x)) + chi_production(x))`.

The preregistered canary condition is satisfied if the residual exceeds `0.01` on at least one probe. Machine result:

| Quantity | Result |
|---|---:|
| Probes | 200 |
| Residual > 0.01 | 200 |
| Minimum residual | 0.010587692260742188 |
| Maximum residual | 1.5070748329162598 |
| Mean residual | 0.3970843741297722 |
| Verdict | `PASS_CANARY_DETECTS_INTERPOLATING_MIRROR` |

This PASS means the test suite detects the intended failure mode. It does **not** permit an interpolating mirror in production. The production chi path continued to use pure width-axis pixel-index reversal and independently re-passed exact R1/R2 on the same probes.

## R5 — paired raw outputs and flip imbalance

For each probe, the row artifact records:

- source index and float32 image SHA-256;
- parity, pitch, inclination, and S/N parameters;
- raw trunk outputs `f(x)` and `f(mirror(x))`;
- each raw sign and the per-object `dA_raw` contribution;
- `chi(x)` and `chi(mirror(x))`, including float32 bit patterns;
- acceptance of each paired chi at frozen tau;
- pure-mirror identity residual and pairwise `abs(chi)` delta;
- R4 affine-mirrored input output, its pure-index-reversed partner output, production chi on that bad input, and the canary residual.

The independent reduction from those 200 rows found:

- `sum((sign(f(x)) + sign(f(mirror(x)))) / 2) = 3.0`
- `dA_raw = 3.0 / 200 = +0.015`
- contribution `0.0`: 197 rows
- contribution `+1.0`: 3 rows, at source indices `3,000,014`, `3,000,061`, and `3,000,170`
- accepted production pairs: 191; unaccepted production pairs: 9
- acceptance mismatch between x and its pure mirror: 0

`dA_raw` is the raw trunk's pre-antisymmetrization flip imbalance on this frozen synthetic probe set. It is **not** a sky statistic, not a real-galaxy result, and not a failure of the antisymmetrized production estimator. The architectural production output remained exactly antisymmetric for all 200 nonzero pairs.

## Corrected operative retention — carried forward

The old **96.44% central / 96.15% lower-bound** figures are not operative for the `b/a > 0.4` population. They were measured on synthetics sampled uniformly in inclination only over `0–60 degrees`.

The operative result is the full admitted-range remeasurement, using the unchanged frozen estimator and tau and sampling uniformly in `cos(i)` over `0–69.3 degrees`:

- accepted = **10,349 / 12,000**
- retention = **86.24%**
- one-sided lower 95% Wilson bound = **85.72%** (`z = 1.6448536269514722`)

Any freeze candidate must carry **86.24% / 85.72%**, not the superseded narrow-support values.

## Machine artifacts and hashes

Workspace: `prereg/yui_bs3_r4_r5_20260813/`

| Artifact | SHA-256 |
|---|---|
| `run_bs3_r4_r5.py` | `de0f35355902f25497e240a413a087a1413d365342419b0be3fc15a7e5117914` |
| `test_run_bs3_r4_r5.py` | `046f9993e632446d854edad91ec06ce9be4ca72c3307f6a42830e8f387c44154` |
| `results.json` | `bb4eef8798893a0ce8e06c09768e20d683ca771c5b7dfb396fd7747a86efea78` |
| `paired_probe_records.jsonl` (200 rows) | `8f8b973abe4685f76049de16b907e16bbc8e3be7c9061f7d349b655bd55b7e82` |
| `run_stdout.log` | `bb4eef8798893a0ce8e06c09768e20d683ca771c5b7dfb396fd7747a86efea78` |
| `run_stderr.log` (empty) | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `independent_verify.py` | `af5a70c70f4d7ec60995b0e957c4cbdef59c1950acc55737772cef7135b26b3a` |
| `test_independent_verify.py` | `5747804c93361c77dbe988cfc183d17ec37b943315fc6dbd74c334c40f3cf9fc` |
| `independent_verification.json` | `c1b81faed8a39d1e7d77cedaade111a446ffd62b949159bbc9de24f8510f2d27` |
| `independent_stdout.log` | `c1b81faed8a39d1e7d77cedaade111a446ffd62b949159bbc9de24f8510f2d27` |
| `independent_stderr.log` (empty) | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

Environment: Python 3.9.6; NumPy 1.26.4; PyTorch 2.8.0; SciPy 1.13.1; macOS 26.6.1 arm64; single-thread CPU inference; deterministic PyTorch algorithms enabled.

Focused tests: **6 / 6 PASS**. The independent verifier did not import the model runner, Torch, SciPy, or training code. It reparsed all 200 JSONL rows, recomputed every contribution from the two raw outputs, reproduced `dA_raw`, R4 count/min/max/mean, exact source-index sequence, probe image manifest, production identity and acceptance-pair counts, corrected retention, records hash, and all frozen-file hashes. Verdict: `PASS_INDEPENDENT_R4_R5_REDUCTION`.

## Boundary held

No survey image, catalogue row, sky coordinate, or real galaxy was read. No sky handedness or anisotropy statistic was computed. Nothing was accepted, frozen, published, committed, uploaded, deployed, or promoted. This receipt closes only Yui's two missing synthetic instrument-run artifacts. **Kun alone re-gates BS-3.**
