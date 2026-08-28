# Pass 19 encoded-frame audit — 360p plus linear-light black-lift interaction

Status: `QA_ONLY_NOT_A_CANDIDATE_NOT_SCIENCE_ADJUDICATION`

Deepening pass: 19  
Extraction completed: see `qa/pass19_minimum_scale_black_lift_audit/extraction_receipt.json`  
Audit completed: `2026-08-08T11:49:42+09:00`

## Authority and custody

Before this pass I re-read:

- `HWAO_WEEKEND_ORDER.md`
- `COORDINATION_UPDATE.md`
- `lanes/spin/BRIEF.md`
- `STATUS.json`
- `SOURCE_STATUS_FREEZE.json`
- the preserved failed-candidate receipt, QA, hashes, and contact sheet
- sealed `STORYBOARD_PROPOSAL.json`, v8 render receipt, frames, and contact sheet
- the pass-18 immutable review snapshot, guard, and encoded-frame audit
- `LANE_RECEIPT.md`

Custody held:

- failed candidate SHA-256: `02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431`
- worker source-freeze SHA-256: `ecff0992015e0bea2b86c14fbf627b79348228bc387d4ad4523208f4925a56a1`
- sealed storyboard remains v8
- sealed v8, pass-7 proof, and pass-12 proof were read-only inputs
- no v9 or candidate was created

The sealed contact sheet still uses `GALAXY SPIN`, preserves graphics-first method/status boundaries, and contains no audience-visible forbidden result/cosmology topics. The candidate contact sheet remains dominated by result-bearing headlines, numbers, cards, plots, and conclusions without a persistent structural held boundary.

## Fresh representation boundary

Pass 19 tests an order-specific interaction not established by standalone pass 6 or pass 10:

1. decode a fresh native 1920×1080 RGB midpoint;
2. downscale the full canvas to 640×360 with Pillow LANCZOS;
3. decode represented sRGB values to linear-light float64;
4. apply `L_out = a + (1-a) × L_in` to every RGB channel;
5. encode to sRGB, clip to `[0,1]`, round with NumPy `rint`, and save static non-optimized RGB PNG evidence;
6. independently recompute the represented output from the lossless 360p baseline and compare exact RGB pixels.

Operational compound variant:

- `black_lift20_360p`: `a=0.20`, maximum ideal white-to-black ratio `4.2:1`

Reference:

- `downscale_360p`

Characterization only:

- `black_lift30_360p`: `a=0.30`, maximum ideal ratio `3.0:1`
- `black_lift40_360p`: `a=0.40`, maximum ideal ratio `2.333333:1`

This is a packet-specific representation stress. It is not evidence about a named display, projector, room, player, browser, platform, service, viewer, or universal standard.

## Fresh extraction

`qa/extract_pass19_minimum_scale_black_lift_frames.py` independently reran the ffmpeg 160×90 grayscale scene detector at score `>0.03`.

Result:

- cuts: `15/15`, exact pass-18 timestamps
- scenes: `16`
- fresh native midpoint frames byte-identical to pass 18: `16/16`
- candidate static frames: `80`
- variants per scene: `5`

The preserved candidate itself was not changed.

## Method derivatives

`qa/build_pass19_v8_minimum_scale_black_lift.py` derived the same variants from three read-only method groups:

- sealed v8
- pass-7 caption-safe proof
- pass-12 sharpness-safe proof

Result:

- groups: `3`
- source scenes: `21`
- static derivative frames: `105`

## Candidate quantitative result

| Variant | Headline recall | Full-text recall | Lower-support recall | Numeric recall | Structural gates | Exact transform |
|---|---:|---:|---:|---:|---:|---:|
| lossless 360p reference | 0.894444 | 0.668251 | 0.328090 | 0.288889 | 0/16 | reference |
| 20% black lift at 360p | 0.883333 | 0.621673 | 0.289888 | 0.155556 | 0/16 | 16/16 |
| 30% characterization | 0.877778 | 0.576046 | 0.262921 | 0.166667 | 0/16 | 16/16 |
| 40% characterization | 0.877778 | 0.511407 | 0.235955 | 0.155556 | 0/16 | 16/16 |

Mean robust p99/p01 luminance ratio is `10.194278` for lossless 360p, `2.522387` at 20%, `1.956003` at 30%, and `1.633905` at 40%. These ratios are diagnostics, not named viewing-condition claims.

### Held-critical scenes 7, 9, 10, 11, and 16

| Variant | Headline recall | Full-text recall | Lower-support recall | Numeric recall | Structural gates |
|---|---:|---:|---:|---:|---:|
| lossless 360p reference | 0.881720 | 0.425532 | 0.280323 | 0.242857 | 0/5 |
| 20% black lift at 360p | 0.860215 | 0.406190 | 0.274933 | 0.142857 | 0/5 |
| 30% characterization | 0.849462 | 0.379110 | 0.239892 | 0.142857 | 0/5 |
| 40% characterization | 0.849462 | 0.353965 | 0.207547 | 0.114286 | 0/5 |

Human represented-pixel review agrees with the hierarchy finding:

- large result headlines, numbers, bars, matrices, plots, and conclusions remain primary through the operational and characterization transforms;
- no structural `RESULT HELD`, `FRAME UNSTATED`, `OUTCOMES WITHHELD`, `NO OUTCOME SHOWN`, `RESULT LOCKED`, or `RESULT STATUS · HELD` boundary appears;
- fine axes, error bars, caveats, citations, provenance, and lower explanatory support weaken first;
- the interaction deepens the assertion-versus-support imbalance and does not repair or authorize the candidate.

## Method-proof result

Human review at operational 20% black lift after 360p downscale:

| Proof | Exact top gates | `RESULT HELD` badges | Major status boundaries | Clipping/overlap/ambiguity |
|---|---:|---:|---:|---:|
| sealed v8 | not a top-gate proof | 7/7 | 7/7 | none |
| pass-7 caption-safe | 7/7 | 7/7 | 7/7 | none |
| pass-12 strengthened | 7/7 | 7/7 | 7/7 | none |

Pass-12 mapped gate-crop character similarity:

| Variant | Mean best-of-PSM 6/7/11/13 similarity | Gates passing ≥0.80 | Exact transform |
|---|---:|---:|---:|
| lossless 360p | 0.985159 | 7/7 | reference |
| 20% black lift at 360p | 0.996825 | 7/7 | 7/7 |
| 30% characterization | 0.990873 | 7/7 | 7/7 |
| 40% characterization | 0.996825 | 7/7 | 7/7 |

OCR similarity is non-monotonic under black lift and is an auxiliary aid only. It stores scores rather than recognized text. Represented-pixel human review and complete-container visibility remain decisive.

At 40% characterization, the strengthened gate/status hierarchy still survives, but fine axes, citations, provenance, and lower-support text are not acceptance-reliable. That characterization does not promote 40% to an acceptance threshold.

## Evidence-backed action

Action: `INTEGRATION_GUARD_NOT_PIXEL_CORRECTION`

`MINIMUM_SCALE_BLACK_LIFT_GUARD_PASS19.json` adds the compound minimum-scale plus black-lift boundary for future Hwao-authored layouts:

- all seven exact scene-specific gates and complete `RESULT HELD` capsules must remain directly readable at represented 640×360 pixels under the exact 20% linear-light black-lift transform;
- every required qualifier, uncertainty, branch, axis, unit, value, error bar, threshold, equation term, interpretation limit, and provenance fact must survive through direct high-contrast text plus a complete shape, border, connector, or stable geometry channel;
- no required meaning may live only in dark fill, a low-contrast footer, tiny axis, one-pixel line, subtle grid, citation, provenance footer, or global OCR;
- the 30% and 40% transforms remain characterization only;
- exact transform recomputation and represented-pixel human review are required.

A new visual or copy correction is not evidence-justified. The latest pass-12 proof preserves all seven exact gates and badges under the operational interaction without clipping, overlap, or ambiguity.

## Blockers unchanged

- no valid post-run independent A3.8 review exists for the exact frozen all-209-file T4 artifact;
- `KUN_FRAME_REVIEW.md` still ends `FRAME REVIEW: AGREES FRAME_UNSTATED`;
- the archive storage convention required for interpretation remains unresolved;
- `video_reportable_now` remains `false`.

## Safety

- no TTS invoked
- no audio generated
- no video encoded
- no publication
- no shared/public asset modification
- no Git action
- all writes stayed in `lane-spin-parity/worker-yui`
