# Yui — BS-4 frozen secondary instrument and receipts

**Run:** 2026-08-14 KST  
**Slot:** BS-4, deterministic secondary instrument  
**Validity verdict:** **PASS — identity is bit-exact and abstention is published.**  
**Scientific-utility warning:** the frozen secondary instrument is an extremely high-abstention cross-check, not a high-yield substitute for the primary.

This fills the slot at `PREREG_LONGO_AMPLITUDE_TEST_20260812.md:222`: frozen algorithm description plus the primary-style identity receipts; validity requires bit-exact identity and a published abstention rate.

## 1. Frozen algorithm description

### Reproducibility object

The secondary instrument is the deterministic code in `spike/yui_identity/w_chi.py`, directly measured SHA-256:

`89da33ec6260e75e06eadb0f171da4c52f1478b59ff5e543d363dbf56fefcd75`.

There are no trained weights. The frozen production acceptance tuple is:

- algorithm code hash above;
- 128 x 128 final analysis raster;
- float32 production wrapper;
- pure width-axis pixel-index mirror;
- `chi_secondary(x) = (float32(w(x)) - float32(w(mirror(x)))) / float32(2)`;
- accept iff `abs(chi_secondary) > 5.916292121766702` by ordered numeric comparison;
- null calibration: 99.5th percentile of `abs(chi_secondary)` on the frozen 8,000-null manifest `1963132f2f36e7aa42b08012aad02d2c541d6c0973740a5bbce6a6e7a2904bd1` under master seed `LONGO-AMPLITUDE-FREEZE-M1`.

The production receipt runner `prereg/yui_receipt_run.py` has SHA-256 `eb41680c8425135662bf9d18cad1a12a4c752c137672f179e3e140f48656a028`.

### Exact source anchors

The mirror is frozen by the source itself (`w_chi.py:27-29`):

> `return np.fliplr(x)`

The estimator body is frozen at `w_chi.py:51-67`. Its operative sequence is:

1. fixed annulus **6–56 pixels**;
2. **25 radial bins** and **90 azimuthal bins** (`w_chi.py:22-24`);
3. nearest-neighbour assignment of pixels to that fixed polar grid, with no image interpolation;
4. mean intensity per polar cell;
5. deterministic first-maximum `argmax` azimuth at each radius (`w_chi.py:53-56`);
6. arm-agnostic period-pi unwrap (`w_chi.py:57-63`);
7. fixed-order least-squares slope of tracked angle against `ln(radius)` (`w_chi.py:64-67`).

The antisymmetrization is the exact source expression at `w_chi.py:70-71`:

> `return (w(x) - w(mirror(x))) / 2.0`

The production float32 wrapper is at `yui_receipt_run.py:46-50`; it casts the two raw `w` outputs to float32 before subtraction and halving. Tau calibration and held-out retention are implemented at `yui_receipt_run.py:25-44` and landed in `prereg/receipt_results.json:18-40`.

The source docstring defines the sign on the analysis pixel grid. Mapping that pixel-grid sign through survey WCS parity is a separate preregistration custody problem and was not exercised here.

## 2. Identity receipts on the promised production probes

BS-4 used the same one-shot 1,000-probe production extension as the repaired BS-3 witness:

- source indices **3,000,000–3,000,999**;
- 128 x 128 float32;
- probe manifest SHA-256 `35d679d4955d3657866bd64fe309a9a42b30ff8a61d1952d2a3795ee59231024`;
- first-200 prefix manifest `ab75d5f2ec08ad44fbcf1198d1612c23759f8d3aac29db044a181346ac43f9b2`, matching the landed production receipts.

| Receipt | Result |
|---|---:|
| R1 mirror involution byte-exact | **1,000/1,000** |
| R2 antisymmetry value-exact | **1,000/1,000** |
| R2 antisymmetry float32 bit-exact | **1,000/1,000** |
| Nonzero R2 cases | **1,000** |
| Zero R2 cases in the 1,000-probe grid | **0** |
| Maximum `abs(chi(mirror(x)) + chi(x))` | **0.0 exactly** |

**BS-4 identity validity: PASS.** No failing probe was removed, replaced, or rerun.

### R3 signed zero

An exactly mirror-symmetric float32 probe produced `chi = +0.0`; its mirrored value had bits `0x00000000`, while `-chi` had bits `0x80000000`. They are value-equal, bit-different, and both abstain because the frozen acceptance path is the ordered test `abs(chi) > tau`. No sign-bit branch is permitted.

### R4 forbidden-transform canary

Production `chi_secondary` remained unchanged internally. A 0.25-pixel-displaced bilinear affine mirror was applied only to the canary input, and the receipt measured:

`abs(chi_secondary(m_bad(x)) + chi_secondary(x))`.

- N = 1,000;
- threshold = strictly greater than 0.01 on at least one probe;
- exceeding threshold = **939/1,000**;
- minimum residual = `0.0000591278076171875`;
- maximum residual = `6.3714709877967834`;
- mean residual = `0.7186069953221013`;
- verdict: **PASS**.

The minimum being below 0.01 is reported, not hidden; the preregistered canary validity rule requires at least one exceedance, not 1,000/1,000.

### R5 raw flip imbalance

Using

`dA_raw = mean((sign(w(x)) + sign(w(mirror(x)))) / 2)`,

all 1,000 per-probe contributions were `0.0`, giving sum `0.0` and **dA_raw = 0.0 exactly**. This is a synthetic pre-antisymmetrization diagnostic, not a sky statistic.

## 3. Abstention — pathology carried, not laundered

### Frozen production held-out receipt

The landed production secondary receipt at `prereg/receipt_results.json:18-40`, SHA-256 `d5d4a8bc005b031ed523e64a672237536896f37030722fd5cf71ff44a3405a04`, reports at frozen tau `5.916292121766702`:

- accepted: **16/12,000**;
- retention: **0.133333%**;
- abstention: **99.866667%**;
- one-sided lower 95% retention bound: **0.088646%**.

By S/N:

| Peak S/N | Accepted / N | Retention | Abstention |
|---|---:|---:|---:|
| 2–5 | 14 / 3,452 | 0.405562% | 99.594438% |
| 5–10 | 2 / 2,594 | 0.077101% | 99.922899% |
| 10–20 | 0 / 2,592 | 0% | 100% |
| 20–50 | 0 / 3,362 | 0% | 100% |

That is the secondary tracer's pathology: near-total abstention and retention that decreases rather than improves with S/N under this frozen calibration. It is a sensitivity failure, not an antisymmetry failure.

### Fresh 1,000-probe check

On the same promised production identity set used above, without changing tau:

- accepted: **1/1,000**;
- retention: **0.1%**;
- abstention: **99.9%**;
- the sole acceptance was in the 2–5 S/N bin; the 5–10, 10–20, and 20–50 bins had zero acceptances.

This independently reproduces the high-abstention shape. No parameter was changed to improve it.

### Why 92.2% also appears in the older spike

The original feasibility grid in `spike/yui_identity/results.json`, SHA-256 `9e95861f8e02113ae97681f572b93a8dcbc27f16fa22214fb7971d3a0becab61`, reports **92.2% abstention at tau 4.198004717066903** on a different 1,000-image factorial grid and a 240-null calibration. It is historical spike evidence, not the frozen production abstention rate.

Its runner used the process-salted Python tuple-hash function for spiral noise seeds (`run_identity_test.py:46-47` and `133-134`) without recording `PYTHONHASHSEED`. The landed result is hash-pinned, but those exact historical noise seeds are not reconstructible from source alone. This limitation is published here rather than silently treating 92.2% as the production value.

## 4. The primary caveat, interpreted accurately

`YUI_PRODUCTION_ESTIMATOR_RECEIPT_20260812.md:12-17` says:

> “No S/N inversion: retention RISES with S/N … The secondary tracer's pathology does not appear.”

That sentence describes the **primary classifier's** narrow-support retention study. It means the primary did not reproduce the secondary's falling-with-S/N retention. It does **not** say the secondary instrument is healthy. The secondary's own frozen production receipt is the 99.866667% abstention result above.

The operative primary full-range retention remains 86.24%, lower bound 85.72%; that number must not be assigned to the secondary.

## 5. Validity versus utility and support limit

The BS-4 table gives two validity requirements only:

1. identity bit-exact;
2. abstention published.

Both are satisfied, so **BS-4 validity PASS**. The pass does not claim useful yield. At the frozen production threshold the secondary is only a sparse training-free cross-check.

The 12,000-object production secondary abstention receipt sampled inclination only over **0–60 degrees**. It is not a remeasurement over the full **0–69.3-degree** support admitted by `b/a > 0.4`, and this document does not represent it as one. BS-4 specifies no minimum secondary retention, but any later yield statement over the full admitted population needs a separately gated full-support measurement or must retain this limitation.

## 6. Machine artifacts and verification

Workspace: `prereg/yui_bs34_20260814/`

| Artifact | SHA-256 |
|---|---|
| `run_bs34.py` | `264ff3b7a3904baea1e022433645da535cef10a6a7b22aaa39e92c4947cc9f8f` |
| `test_run_bs34.py` | `784febfe6eb9d7a3b915048e543211e019252d66611083b14fb4399576286b27` |
| `results.json` | `cfd11391f123e0caa054f0a3bdfab76b20eb7293c457bafd70563e90af07df33` |
| `identity_probe_records.jsonl` (synthetic probes only) | `b5ddea6397947f74156cdb9bf62038d72f983b765b4ba54a8e00052eb6550380` |
| `independent_verify.py` | `75e6af0cecb7f63fdf9b835891bf02c6fd222b070e73a2b6d743e74db666c9e4` |
| `test_independent_verify.py` | `83dff437d512d048ee4b4b335cbd2d515df1145a4316ec9670697e03e0ddd83d` |
| `independent_verification.json` | `2a51aed8307e9ab3140d91eb74fdd2b0b973bb85d7c5db11157be23d5efcfeb3` |
| `run_stderr.log` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` (empty) |
| `independent_stderr.log` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` (empty) |

Focused tests: **5/5 PASS**. The independent verifier imported no model runner, training code, Torch, SciPy, or secondary algorithm. It reparsed all 1,000 rows and recomputed the bit comparisons, source-index custody, manifests, ordered acceptance, S/N abstention bins, R4 reduction, R5 contributions, direct frozen hashes, and historical receipt numbers. Verdict: `PASS_INDEPENDENT_BS34_REDUCTION`.

## 7. Boundary

No survey data, real-object row, coordinate, real image, morphology/chirality label, or sky statistic was read or computed. No tuning, retry-to-pass, retraining, recalibration, acceptance, freeze, publication, commit, or push occurred. This is a slot receipt for Kun's re-gate; **Duho owns acceptance.**
