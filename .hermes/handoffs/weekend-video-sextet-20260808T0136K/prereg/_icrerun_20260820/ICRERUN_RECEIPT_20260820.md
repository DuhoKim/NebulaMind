# IC R1–R5 rerun receipt — 2026-08-20

## Verdict

**PASS_ICRERUN.** The complete synthetic R1–R5 series and full-support retention remeasurement ran through the imported production IC code in `_cutout_runner_20260820/cutout_runner.py` (SHA-256 `ccb9b8fed457333669e54fa9f0a3dac645dc866a56c6cd8dc665ffd4d93b1bcc`). The rerun called that module's `apply_input_contract` for IC-1…IC-6 and `mirror_tensor` for IC-7; neither function was copied or reimplemented.

The authority was verified directly: `LANA_PC1_INPUT_AMENDMENT_20260815.md` SHA-256 `519ab5ba33c5e9d670b5654fb41f6941293c5d969c5515fb0284ebe8d52d70fb`. This receipt supplies the synthetic evidence required by §3 A3 and §4 consequence 1. It does not itself authorize sky access: Kun must gate it.

## Binding slots filled

`_cutout_runner_20260820/ic_slots.json` is now filled and pinned at SHA-256:

`10d24a6e1c5dd64eef8e1ada7e3d222f2e168bab288b1438792db7ff6a848372`

### IC-4 — invalid-fraction cap

- Frozen cap: **0.0**.
- Selection evidence: all **13,000/13,000** natural frozen-generator images in the identity and full-support retention populations had invalid fraction exactly **0.0**; total natural invalid pixels: **0**.
- Rule: no synthetic evidence supported a nonzero tolerance, so the conservative fail-closed cap is zero.
- Synthetic edge fixture: zero-invalid raster passed at fraction `0.0`; one NaN pixel produced fraction `1/16384 = 0.00006103515625` and failed with `FAILED_IC4_INVALID_FRACTION_CAP`.
- Replacement order remains the production implementation's amendment-ordered behavior: scaling first, replacement second. With cap 0.0, any object needing replacement abstains rather than entering the model.

### IC-5 — fixed scaling map

- Function: **`tensor = float32(nanomaggy)`**.
- Form: fixed monotone identity affine map.
- Gain: **1.0**.
- Offset: **0.0**.
- Per-object normalization: **none**.
- Data-dependent constants: **none**.
- Frozen scaler: `_icrerun_20260820/ic5_scaler.py`, SHA-256 `21b66eda899b5e48034be2b2d92ee2c77f262b156eb59d680eb1b80763d12621`.
- Synthetic validation: order preserved on a monotone 16,384-value grid; output bytes equaled input float32 bytes on the grid and on **13,000/13,000** frozen-generator images.
- Justification: the weights and tau were frozen on the generator's float32 scale. The identity map is the fixed monotone zero-change choice that preserves that scale and permits a direct bit witness; no real image or real-data statistic was used to choose it.

IC-2/IC-3 equivalence was exercised rather than assumed: each synthetic raster entered the production scaler whole, with no unit conversion, background estimate, subtraction, or normalization. Exact old/new raster-byte equality on 13,000/13,000 images proves the new IC path added none of those operations on the tested synthetic population.

## Frozen input custody

Direct hashes verified before and after the successful run:

| Object | SHA-256 |
|---|---|
| Amendment | `519ab5ba33c5e9d670b5654fb41f6941293c5d969c5515fb0284ebe8d52d70fb` |
| Old estimator appendix | `331a941a807eef2f02e821086230655505b332b90ff1e47ff128d034334f9fc3` |
| Production cutout/IC module | `ccb9b8fed457333669e54fa9f0a3dac645dc866a56c6cd8dc665ffd4d93b1bcc` |
| Frozen BS-3 generator | `89da33ec6260e75e06eadb0f171da4c52f1478b59ff5e543d363dbf56fefcd75` |
| Frozen weights file | `83008c1cbdae511af5d30020540e1e281c62c2bd95d3cb05527fc0687bf49e6d` |
| Canonical float32 weights after strict load | `1075a4d91c295d7f3256128534a0b8c4d097fb9d162169df1ac698843637a589` |
| `train_results.json` | `c36cd33001e432c60df786da8c0ff95b8ef5ab350a458b29d71ff084178a41fd` |
| `receipt_results.json` | `d5d4a8bc005b031ed523e64a672237536896f37030722fd5cf71ff44a3405a04` |
| Old 1,000-probe machine result | `cfd11391f123e0caa054f0a3bdfab76b20eb7293c457bafd70563e90af07df33` |
| Old retention machine result | `414fbc5cb6fa050390f0a6bca69e02e81795ed2a3585928be19767f4cb3a59e2` |
| Old R4/R5 machine result | `bb4eef8798893a0ce8e06c09768e20d683ca771c5b7dfb396fd7747a86efea78` |

Frozen master seed: `LONGO-AMPLITUDE-FREEZE-M1`. Frozen primary tau: `4.4006456017494235`. No training, retraining, threshold recalibration, retuning, or probe replacement occurred.

## R1–R3 and identity witness

Population: source indices **3,000,000–3,000,999**, N = **1,000**. The regenerated float32 image-manifest SHA-256 was `35d679d4955d3657866bd64fe309a9a42b30ff8a61d1952d2a3795ee59231024`, exactly the old 1,000-probe pin. Its 200-row prefix was `ab75d5f2ec08ad44fbcf1198d1612c23759f8d3aac29db044a181346ac43f9b2`, exactly the old R4/R5 pin.

| Test | New full-IC result | Old-path quantity | Comparison |
|---|---:|---:|---|
| R1 mirror involution, byte-exact | **1,000/1,000** | 1,000/1,000 | exact reproduction |
| R2 antisymmetry, value-exact | **1,000/1,000** | 1,000/1,000 | exact reproduction |
| R2 antisymmetry, float32-bit-exact | **1,000/1,000** | 1,000/1,000 | exact reproduction |
| max `abs(chi(mirror(x)) + chi(x))` | **0.0** | 0.0 | exact reproduction |
| old-path chi vs new-path chi bits | **1,000/1,000 identical** | binding witness newly required | **PASS identity witness** |
| IC-7 placement: mirror-after-IC equals IC(raw mirror) bytes | **1,000/1,000** | not previously an IC-path quantity | PASS |

R3 exactly symmetric fixture:

- `chi = +0.0`, bits `0x00000000`;
- `chi(mirror(x)) = +0.0`, bits `0x00000000`;
- `-chi` bits `0x80000000`;
- value equality: true;
- bit equality for the signed-zero edge: false, as expected;
- ordered acceptance `abs(chi) > tau`: false;
- input bytes equal to the old path: true.

This is the appendix's signed-zero rule, not an R2 failure: the 1,000 production probes were nonzero and flipped sign bit-exactly.

## R4 — forbidden interpolating-mirror canary

The old canary transform was reused: `scipy.ndimage.affine_transform`, reflection displaced 0.25 pixel from the grid centreline, bilinear `order=1`, `mode="nearest"`. The bad transform was applied to the canary input only; both original and bad inputs then passed through the production IC function, and production chi retained the pure IC-7 index mirror internally.

Formula: `abs(chi_production_full_path(m_bad(x)) + chi_production_full_path(x))`.

| Quantity | New full-IC result | Old-path result |
|---|---:|---:|
| N | 200 | 200 |
| residual > 0.01 | **200** | 200 |
| minimum | **0.010587692260742188** | 0.010587692260742188 |
| maximum | **1.5070748329162598** | 1.5070748329162598 |
| mean | **0.3970843741297722** | 0.3970843741297722 |
| verdict | **PASS** | PASS |

Every reported R4 quantity reproduced exactly. This PASS means the suite detects the forbidden transform; it does not permit interpolation in production.

## R5 — paired raw-output flip imbalance

Formula: `mean((sign(f(x)) + sign(f(mirror_full_path(x)))) / 2)` over the same pinned 200-row prefix.

| Quantity | New full-IC result | Old-path result |
|---|---:|---:|
| contribution sum | **3.0** | 3.0 |
| `dA_raw` | **+0.015** | +0.015 |
| contribution 0.0 | **197** | 197 |
| contribution +1.0 | **3** | 3 |
| negative contributions | **0** | 0 |
| paired acceptance mismatches | **0** | 0 |

Every R5 quantity reproduced exactly. This is a synthetic raw-trunk, pre-antisymmetrization diagnostic, not a sky statistic.

## Full-support retention remeasurement

Population: N = **12,000**, source indices **2,000,000–2,011,999**, uniform in `cos(i)` over `0 <= i <= 69.3°`. Generator manifest `bb60b69b17b24424af47667367312c1915cd0b8986336865a741fe70f80933d0` exactly matched the old full-support receipt. All 12,000 production-IC tensors were byte-identical to their old-path float32 images.

Overall:

- accepted: **10,349/12,000**;
- retention: **0.8624166666666667 = 86.24%**;
- one-sided 95% Wilson lower bound: **0.8571626782674123 = 85.72%**;
- accepted-sign accuracy: **10,349/10,349 = 1.0**.

Old-path quantities were 10,349/12,000, 0.8624166666666667, 0.8571626782674123, and 1.0 respectively: every overall quantity reproduced exactly.

Inclination bins:

| Inclination | Accepted/N | Retention | Lower 95% | Accepted-sign accuracy |
|---|---:|---:|---:|---:|
| 0–15° | 602/630 | 0.9555555555555556 | 0.9399913956399034 | 1.0 |
| 15–30° | 1,785/1,831 | 0.9748771163298744 | 0.9681244113355228 | 1.0 |
| 30–45° | 2,909/2,970 | 0.9794612794612795 | 0.9747238195819057 | 1.0 |
| 45–60° | 3,652/3,842 | 0.950546590317543 | 0.9444693134261581 | 1.0 |
| 60–65° | 1,072/1,427 | 0.7512263489838823 | 0.7319391366831476 | 1.0 |
| 65–69.3° | 329/1,300 | 0.2530769230769231 | 0.23376928784859147 | 1.0 |

S/N bins:

| S/N | Accepted/N | Retention | Lower 95% | Accepted-sign accuracy |
|---|---:|---:|---:|---:|
| 2–5 | 2,591/3,452 | 0.7505793742757821 | 0.7382731582361939 | 1.0 |
| 5–10 | 2,310/2,594 | 0.8905165767154973 | 0.8800226298695049 | 1.0 |
| 10–20 | 2,347/2,592 | 0.9054783950617284 | 0.8955992721825667 | 1.0 |
| 20–50 | 3,101/3,362 | 0.9223676383105295 | 0.9144324208557847 | 1.0 |

The old 96.44% / 96.15% narrow-support quantities remain superseded. The operative result remains 86.24% / 85.72% on the full admitted synthetic support.

## Independent reduction

`_icrerun_20260820/independent_verify.py` uses the Python standard library only and imports no runner, model code, Torch, NumPy, SciPy, generator, or production IC module. It reparsed all 13,000 rows, verified both exact source-index sequences and manifests, recomputed R1, R2 bits, the old/new identity witness, IC-7 placement, R4 count/min/max/mean, R5 histogram/sum/mean, retention, and the Wilson lower bound, and rehashed the frozen objects and slot file.

Verdict: **`PASS_INDEPENDENT_ICRERUN_REDUCTION`**; all **32/32** recorded predicates are true.

## Artifact pins

| Artifact | SHA-256 |
|---|---|
| `_cutout_runner_20260820/ic_slots.json` | `10d24a6e1c5dd64eef8e1ada7e3d222f2e168bab288b1438792db7ff6a848372` |
| `_icrerun_20260820/ic5_scaler.py` | `21b66eda899b5e48034be2b2d92ee2c77f262b156eb59d680eb1b80763d12621` |
| `_icrerun_20260820/run_icrerun.py` | `65014032cce0578db8f18c11d9ab037d241874ba0407457ff8186e3119485d1a` |
| `_icrerun_20260820/independent_verify.py` | `596151e6890d363773b49f719eb67e12151d2e57bdc76743a4b22809baf25140` |
| `_icrerun_20260820/R1_R5_RECEIPT.json` | `8a3d70102b37ed5981cf569ce15f4badcc5e2176c8589681c160940a8aa6a64f` |
| `_icrerun_20260820/RETENTION_RECEIPT.json` | `41e50d90070c7a87f9b62d2f015c4b55319e85379ad4ee2fdf6038d32b2f956f` |
| `_icrerun_20260820/IC_SLOT_VALIDATION_RECEIPT.json` | `120dc3bd27d34f4a4a30106037c03622b58090c373ea702a283af245fe76f71e` |
| `_icrerun_20260820/ICRERUN_RESULTS.json` | `c5f4356d20e583819700b8f727501be5bb83892f51fc3eedfa0f02b1a9ede1ad` |
| `_icrerun_20260820/INDEPENDENT_VERIFICATION.json` | `bca40882b4efb62955ff40c4bf99f478acfb09c29ffb58d749c0da51df736acd` |
| `_icrerun_20260820/r1_r5_records.jsonl` (1,000 rows) | `65fa6dfe8ab43ea28053c3840126c98406a10ce137329446d1a3e5d38747ef1a` |
| `_icrerun_20260820/retention_records.jsonl` (12,000 rows) | `d96f641d2f3bad058967ab72e6e781930b0acc0e8942e556d1e2badced75d49f` |
| `_icrerun_20260820/run_stdout.log` | `c5b3098f20575f3049b456535373cf32c5ad1ef19057c2cf57c636bd8724e0ce` |
| `_icrerun_20260820/run_stderr.log` (empty) | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `_icrerun_20260820/independent_stdout.log` | `bca40882b4efb62955ff40c4bf99f478acfb09c29ffb58d749c0da51df736acd` |
| `_icrerun_20260820/independent_stderr.log` (empty) | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

The successful run took 416.44 seconds under Python 3.9.6, NumPy 1.26.4, PyTorch 2.8.0, macOS 26.6.2 arm64, one Torch intra-op thread, one inter-op thread, and deterministic algorithms enabled.

## Attempt custody

Two pre-verdict attempts are preserved, not overwritten:

1. `attempt1_terminated/`: the background-process wrapper left a defunct process after the 1,000-row write with no exit code or traceback. No aggregate receipt existed.
2. `attempt2_code_error/`: the unchanged sequence exposed a wrong module namespace for the R3 `synth_disk` symbol after the 1,000-row write. The traceback is preserved. The minimal repair imported the same hash-pinned generator directly; no scientific definition changed.

Both partial row files have SHA-256 `65fa6dfe8ab43ea28053c3840126c98406a10ce137329446d1a3e5d38747ef1a`, matching the final deterministic 1,000-row record exactly. No row was selected, dropped, replaced, or retried under a different definition.

## Boundary

Only analytic BS-3 synthetics and frozen local estimator artifacts were read. The runner has no network, FITS, catalogue, coordinate, acquisition, or selection import. No real survey raster, real object row, sky coordinate, morphology label, handedness label, or sky statistic was read or computed. No network was used. Nothing was trained, recalibrated, tuned, accepted, published, committed, pushed, deployed, or promoted.

This receipt clears the demanded synthetic rerun evidence only. **Sky access remains closed until Kun gates this receipt and the other preregistration conditions are satisfied.**
