# Longo-amplitude test — Yui BS-5 synthetic absolute-sign anchor

**Run date:** 2026-08-14  
**Verdict:** **PASS — known counter-clockwise synthetic spirals produced positive primary-estimator χ on 32/32 fixed probes, and their pixel mirrors produced negative χ on 32/32.**  
**Correction outcome:** **No estimator sign correction was required.** The uncorrected estimator multiplier remained `+1`; the frozen convention remained unchanged.  
**Gate boundary:** This receipt supplies synthetic BS-5 evidence only. It is not Duho acceptance, Kun's re-gate, a freeze, a real-image authorization, or publication.

## 1. Authority and frozen boundary

The executed brief is `prereg/_tmp_YUI_SIGN_ANCHOR_BRIEF.md`, SHA-256 `f8f0633a9e2bb513534ba721e79e573afd0e8e2d0e2ef3a11f6bcfee3be45602`.

The frozen preregistration was rehashed directly before execution:

- `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260814.md`: `da2c6a21d994b9af7395347bf881075f855826ff859dd0415f15042f80ed3308` — exact match to the authority brief;
- `LANA_BS5_LONGO_SIGN_20260814.md`: `b7c32dcf12d9e147e5dee6a8262d925b61011615f2ee1d75d687600abb0a72ca`;
- frozen weights file: `83008c1cbdae511af5d30020540e1e281c62c2bd95d3cb05527fc0687bf49e6d`;
- canonical little-endian float32 parameters after strict load: `1075a4d91c295d7f3256128534a0b8c4d097fb9d162169df1ac698843637a589`;
- frozen `τ`: `4.4006456017494235`;
- frozen null manifest: `1963132f2f36e7aa42b08012aad02d2c541d6c0973740a5bbce6a6e7a2904bd1`.

The model was reconstructed from the already-defined frozen architecture and loaded with `strict=True`. The training script was not imported. There was no retraining, re-export, fine-tuning, threshold recalibration, training/null-set regeneration, or parameter revision.

The sign convention stayed binding throughout:

> **counter-clockwise apparent winding, measured East-of-North on the analysis raster, means `χ > 0`; clockwise means `χ < 0`.**

No test outcome was allowed to revise that convention.

## 2. WCS parity was validated first

The parity-only validator has no model import and no image generator. It ran and wrote `wcs_parity.json` before the primary model was loaded or any anchor spiral was generated.

The binding PC-3 text, quoted from `PREREG_LONGO_AMPLITUDE_TEST_20260812.md:186-188` and carried unchanged by frozen preregistration §6, is:

> **Per-object WCS parity: CD/PC·CDELT determinant logged; row-order transform determinant logged; combined pixel→sky sign logged; handedness evaluated in sky coordinates (winding East-of-North).**

The position-free synthetic WCS template used only parity information—no `CRVAL`, coordinate, sky position, survey row, or image:

| Check | Measured result |
|---|---:|
| Raster | `128 × 128` |
| Logical pixel axes | column increases right; FITS-native logical row increases up |
| Sky tangent axes | East, North |
| `CD/PC·CDELT` | `[[-1/3600, 0], [0, +1/3600]]` deg/pixel |
| `det(CD/PC·CDELT)` | `-7.71604938271605e-08` |
| Row-order transform | identity |
| Row-order determinant | `+1.0` |
| Combined pixel→sky determinant | `-7.71604938271605e-08` |
| Combined parity | `REVERSING` |
| Raster orientation | North-up / East-left |
| Increasing position angle, North through East | counter-clockwise |
| Verdict | `PASS_WCS_PARITY_FIRST` |

Three parity contract tests passed. Two deliberate failures were also exercised: an East-right WCS and a silent row reversal were both rejected.

This validates the synthetic anchor raster's convention only. It explicitly does **not** substitute for the frozen future per-object PC-3 receipts on any separately authorized real-image run.

## 3. Fixed synthetic probe set

The anchor used **32 independent synthetic spirals** on the production `128 × 128 float32` raster. All were fixed before the model result:

- master seed: `LONGO-AMPLITUDE-BS5-ABSOLUTE-SIGN-V1`;
- synthetic source-index range: `5,000,000–5,000,031`;
- seed derivation: first eight bytes of `SHA-256(master_seed || source_index)`, reduced modulo `2^63`;
- pitch: fixed hash-derived values inside `12–38°`;
- inclination: fixed hash-derived values inside `0–55°`;
- S/N: fixed hash-derived values inside `35–50`;
- two arms, arm amplitude `0.9`, frozen-generator pixel phase `0.7`;
- pure pixel mirror: width-axis index reversal, no interpolation or resampling.

Seeds, in probe order:

`2473273849244718098, 8789019505398510286, 1526912716211634484, 9072892516473193307, 8540587544735610435, 3479233177003602006, 2206455257116269984, 7915581451605460104, 7967478538437203672, 8327766093791237161, 6567860936143578748, 2094551303266628906, 1618592970158951944, 1532065566840713327, 4881465317377269483, 1555784974855130691, 7554151867994230338, 2292959223475340082, 4632702592972026775, 1725246391710917466, 922424052922638712, 3643598945665468368, 3687420998031907456, 8636501273444800728, 7253894412676643749, 4438494391256111696, 3671490285313508610, 2558166004466253871, 7987164651420205480, 996386341571357895, 925931966215780766, 3812471434965937345`.

The generator was written in sky coordinates. With East left and North up, each two-arm ridge obeys positive `d(PA)/d(ln r)`, where PA increases North through East. It is algebraically the frozen generator's parity `+1` branch expressed in those sky axes. A direct byte comparison against the frozen generator confirmed **32/32 byte-identical float32 images, with maximum absolute difference `0.0`**. An independent rendered-pixel two-arm phase measurement—not the model output—confirmed:

- original-image slope positive: **32/32**, range `+1.2954932761243938` to `+3.836324656923356`;
- mirrored-image slope negative: **32/32**, range `-3.836324656923356` to `-1.2954932761243938`;
- mirror involution byte-exact: **32/32**.

The ordered image-and-mirror float32 manifest SHA-256 is `d0f8ffab5a941add19bb1b9adef74e944bd8973bf7d48f89c677e48f74a71293`.

## 4. Absolute-sign result

The frozen primary wrapper was evaluated as

`χ_base(x) = [f(x) − f(pixel_mirror(x))] / 2`

with an explicit estimator-side multiplier. The pre-correction multiplier was `+1`.

| Predicate | Result |
|---|---:|
| Rendered originals independently verified CCW | **32/32** |
| Rendered pixel mirrors independently verified CW | **32/32** |
| Uncorrected `χ_base(CCW) > 0` | **32/32** |
| Uncorrected `χ_base(mirror(CCW)) < 0` | **32/32** |
| Estimator `χ(CCW) > 0` | **32/32** |
| Estimator `χ(mirror(CCW)) < 0` | **32/32** |
| `χ(mirror(x)) = −χ(x)` by float32 value | **32/32** |
| Accepted at frozen `τ` | **32/32** |

For CCW originals, estimator χ ranged from `+4.513615131378174` to `+10.054704666137695`, with mean `+7.576760560274124`.

**BS-5 synthetic absolute-sign anchor: PASS.** The base estimator already agreed with the frozen convention. Therefore:

- estimator sign multiplier remained `+1`;
- no estimator code-side polarity correction was applied;
- the documented convention was not changed;
- no post-correction run exists or was needed.

The `32/32` accepted-at-τ count is reported as an instrument detail. The BS-5 pass predicate is the absolute sign pair, not a retuned acceptance criterion.

## 5. Execution-history disclosure

The first execution attempt reached construction of the first synthetic record but failed while serializing a NumPy `bool_` to JSON. It emitted no sign value, wrote no JSONL row, and produced no model-result receipt that could be inspected or used. The preserved partial JSONL is zero bytes. The stderr is preserved verbatim.

A focused RED test reproduced the serialization failure. The serializer was minimally corrected to emit native Python booleans, the test turned GREEN, and the same unchanged 32-probe schedule was executed. No probe, seed, parameter, threshold, sign convention, weight, or acceptance rule was replaced or tuned. This was a disclosed technical pre-result rerun, not a result-driven retry.

## 6. Independent verification

`independent_verify.py` imports neither the model runner, training code, NumPy, Torch, nor SciPy. It reparsed the 32 landed JSONL records and independently recomputed:

- exact probe-index/source-index sequences and all 32 seeds;
- ordered image/mirror manifest;
- analytic and rendered winding-sign counts;
- base and estimator sign-pair counts;
- float-value antisymmetry;
- frozen-τ acceptance count;
- χ min/max/mean;
- WCS receipt hash, determinant signs, and North-up/East-left predicates;
- stage/result/record hashes;
- all frozen input hashes;
- the disclosed first-attempt failure and zero-byte partial record;
- every no-real-data/no-tuning/no-acceptance boundary.

Independent verdict: **`PASS_INDEPENDENT_BS5_SIGN_ANCHOR_REDUCTION` — 28/28 checks.**

Focused/full contract suite: **11/11 PASS**. Python compilation passed. Runner stderr, parity stderr, and final independent-verifier stderr are empty.

## 7. Machine-artifact SHA-256 ledger

### Core code and receipts

| Artifact | SHA-256 |
|---|---|
| `validate_wcs_parity.py` | `7bf0201917e7722ee9545c9c11b6cc1cbdec345504e3f29fa1aeb01e58edaa55` |
| `test_validate_wcs_parity.py` | `75b19826bc658229fd0977c905613c596a6f94ec75f55a6141d91860dd75fd9f` |
| `wcs_parity.json` | `14deff60b3462f99ec2daae6412e9d370313990e9303a2186f4faf48242e6169` |
| `run_bs5_sign_anchor.py` | `3ee8c684e5712fd24d31e1d4ce5b7257e2c9491519ce9d39d95b96d2dc1e8150` |
| `test_run_bs5_sign_anchor.py` | `8b7e692c0b119767501315eb9c47a867da552beee0bd85f747ebe747b0865fad` |
| `pre_correction_results.json` | `20eee087c4f5abc8c0dcf2ce75640d52ded0858629f8fead252d1fb7d4d0c6cc` |
| `results.json` | `7c98eea5dbc92301b0900fa9b3ce09f1ed31c3e9751b599944008e35e91e0038` |
| `pre_correction_probe_records.jsonl` | `cd02451070f0bbd16326439ed963dc07a5593da7b1505ef277307d4571019dc2` |
| `independent_verify.py` | `08d9aa33307d387acfed1d22f8eafe4724f74aaf55f586d4bf34924dd69a9a41` |
| `test_independent_verify.py` | `d82ad062e7e483d637764a4cb96d6586806051a7357ff41deee757c0fbf76982` |
| `independent_verification.json` | `deeb88646c15a6d10fc01602cc6366f4550b17e89c762e0256ba51332288436b` |

### Execution and test logs

| Artifact | SHA-256 |
|---|---|
| `parity_test_stdout.log` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `parity_test_stderr.log` | `4011b427ba11d54ee13b62d3b6f1d417e018a1ff8e05f46164ceed79d881ae15` |
| `parity_stdout.log` | `14deff60b3462f99ec2daae6412e9d370313990e9303a2186f4faf48242e6169` |
| `parity_stderr.log` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `pre_correction_stdout.log` | `7c98eea5dbc92301b0900fa9b3ce09f1ed31c3e9751b599944008e35e91e0038` |
| `pre_correction_stderr.log` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `attempt1_pre_correction_stdout.log` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `attempt1_pre_correction_stderr.log` | `4753ae9d8806d56a98adff5fe9c008a512f0843faae2d95f71a58809e8cd508d` |
| `attempt1_partial_probe_records.jsonl` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `independent_test_stdout.log` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `independent_test_stderr.log` | `64d416fbbd554236371d030242ef68b03dc3b8d7abc3a39d62f82abcc9f753ce` |
| `independent_stdout.log` | `deeb88646c15a6d10fc01602cc6366f4550b17e89c762e0256ba51332288436b` |
| `independent_stderr.log` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `full_test_stdout.log` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `full_test_stderr.log` | `1df5885be22ab114237ad05fafd1cbc1dfa15196bb57a852be70374eb40fc2ce` |
| `generator_equivalence.log` | `8deb25efbdde802d4699d478b778888a88560ae2185f81bcd4bba1ff2c76b54c` |

The SHA-256 of this prose receipt is intentionally measured only after the final write and is supplied at closeout.

## 8. Absolute boundary

Real sky data: **0**. Real galaxy images: **0**. Survey cutouts: **0**. Object rows: **0**. Coordinates or positions: **0**. Real chirality labels: **0**. Sky statistics: **0**. Network access: **0**. Retraining/re-export/fine-tuning: **0**. Threshold or probe tuning: **0**. Convention changes: **0**. Publication, acceptance, freeze, commit, or push: **0**.

The next step that would touch a real galaxy remains a STOP. This receipt returns to Kun for the BS-5 gate; Duho owns acceptance.
