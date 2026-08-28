# Pass 20 encoded-frame audit — native defocus followed by 360p

Status: `QA_ONLY_NOT_A_CANDIDATE_NOT_SCIENCE_ADJUDICATION`

Deepening pass: 20  
Extraction completed: `2026-08-08T12:12:58+09:00`  
Audit completed: `2026-08-08T12:18:40+09:00`

## Authority and custody

Before this pass I re-read:

- `HWAO_WEEKEND_ORDER.md`
- `COORDINATION_UPDATE.md`
- `lanes/spin/BRIEF.md`
- `STATUS.json`
- `SOURCE_STATUS_FREEZE.json`
- the preserved failed-candidate receipt, QA, hashes, and contact sheet
- sealed `STORYBOARD_PROPOSAL.json`, v8 render receipt, frames, and contact sheet
- the pass-19 immutable review snapshot, guard, and encoded-frame audit
- `LANE_RECEIPT.md`

Custody held:

- failed candidate SHA-256: `02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431`
- worker source-freeze SHA-256: `ecff0992015e0bea2b86c14fbf627b79348228bc387d4ad4523208f4925a56a1`
- sealed storyboard remains v8
- sealed v8, pass-7 proof, and pass-12 proof were read-only inputs
- no v9 or candidate was created

The sealed contact sheet still uses `GALAXY SPIN`, preserves method/status boundaries, and contains no audience-visible forbidden result/cosmology topics. The candidate remains dominated by result-bearing headlines, numbers, cards, plots, and conclusions without a persistent structural held boundary.

## Fresh representation boundary

Pass 20 tests an order-specific interaction not established by standalone pass 6 or pass 12:

1. decode a fresh native 1920×1080 RGB midpoint;
2. apply Pillow `ImageFilter.GaussianBlur(radius)` at the native canvas;
3. downscale the full blurred canvas to 640×360 with Pillow LANCZOS;
4. save static non-optimized RGB PNG evidence;
5. independently recompute the exact compound transform from the native source and compare represented RGB pixels.

Operational compound variant:

- `defocus_r1_50_then_360p`: native Gaussian radius 1.5 pixels, then 640×360

Reference:

- `downscale_360p`: lossless native-to-640×360 LANCZOS

Characterization only:

- `defocus_r2_50_then_360p`
- `defocus_r4_00_then_360p`

These are packet-specific representation stresses, not evidence about a named lens, projector, display, player, browser, platform, service, room, viewer, or universal standard.

## Fresh extraction

`qa/extract_pass20_minimum_scale_defocus_frames.py` independently reran the ffmpeg 160×90 grayscale scene detector at score `>0.03`.

Result:

- cuts: `15/15`, exact pass-19 timestamps
- scenes: `16`
- fresh native midpoint frames byte-identical to pass 19: `16/16`
- candidate static frames: `80`
- variants per scene: `5`

The preserved candidate itself was not changed.

## Method derivatives

`qa/build_pass20_v8_minimum_scale_defocus.py` derived the same variants from three read-only method groups:

- sealed v8
- pass-7 caption-safe proof
- pass-12 sharpness-safe proof

Result:

- groups: `3`
- source scenes: `21`
- static derivative frames: `105`

## Candidate quantitative result

OCR recall is measured against each fresh native clean frame. Incremental pixel metrics compare the represented derivative with the lossless 360p reference.

| Variant | Headline recall | Full-text recall | Lower-support recall | Numeric recall | Structural gates | Exact transform |
|---|---:|---:|---:|---:|---:|---:|
| lossless 360p reference | 0.894444 | 0.668251 | 0.328090 | 0.288889 | 0/16 | reference |
| native r1.5 then 360p | 0.877778 | 0.675856 | 0.375281 | 0.177778 | 0/16 | 16/16 |
| native r2.5 then 360p characterization | 0.866667 | 0.601711 | 0.211236 | 0.111111 | 0/16 | 16/16 |
| native r4.0 then 360p characterization | 0.727778 | 0.366920 | 0.029213 | 0.133333 | 0/16 | 16/16 |

The operational derivative has:

- mean incremental RGB PSNR: `32.688459 dB`
- mean incremental absolute RGB error: `1.597248`
- tolerant luma-edge recall: `0.975758`
- luma-gradient-energy ratio: `0.467665`

OCR is non-monotonic: modest blur can merge fragments into tokens that the lossless 360p segmentation missed. This does not indicate semantic repair.

### Held-critical scenes 7, 9, 10, 11, and 16

| Variant | Headline recall | Full-text recall | Lower-support recall | Numeric recall | Structural gates |
|---|---:|---:|---:|---:|---:|
| lossless 360p reference | 0.881720 | 0.425532 | 0.280323 | 0.242857 | 0/5 |
| native r1.5 then 360p | 0.849462 | 0.446809 | 0.331536 | 0.171429 | 0/5 |
| native r2.5 then 360p characterization | 0.827957 | 0.344294 | 0.199461 | 0.085714 | 0/5 |
| native r4.0 then 360p characterization | 0.591398 | 0.168279 | 0.029650 | 0.100000 | 0/5 |

Human represented-pixel review agrees with the hierarchy finding:

- large result headlines, numbers, bars, matrices, plots, and conclusions remain primary through the operational transform and remain the recognizable hierarchy at the severe characterization;
- no structural `RESULT HELD`, `FRAME UNSTATED`, `OUTCOMES WITHHELD`, `NO OUTCOME SHOWN`, `RESULT LOCKED`, or `RESULT STATUS · HELD` boundary appears;
- fine axes, error bars, caveats, citations, provenance, and lower explanatory support weaken first;
- the interaction deepens the assertion-versus-support imbalance and does not repair or authorize the candidate.

## Method-proof result

Human represented-pixel review at operational native r1.5 followed by 360p:

| Proof | Exact top gates | `RESULT HELD` badges | Major status boundaries | Clipping/overlap/ambiguity |
|---|---:|---:|---:|---:|
| sealed v8 | not a top-gate proof | 7/7 | 7/7 | none |
| pass-7 caption-safe | 7/7 | 7/7 | 7/7 | none |
| pass-12 strengthened | 7/7 | 7/7 | 7/7 | none |

Pass-12 mapped gate-crop character similarity:

| Variant | Mean best-of-PSM 6/7/11/13 similarity | Gates passing ≥0.80 | Exact transform |
|---|---:|---:|---:|
| lossless 360p | 0.985159 | 7/7 | reference |
| native r1.5 then 360p | 0.954273 | 7/7 | 7/7 |
| native r2.5 then 360p characterization | 0.782872 | 5/7 | 7/7 |
| native r4.0 then 360p characterization | 0.260468 | 0/7 | 7/7 |

At r2.5 and r4.0 characterization, the seven top gate containers and status hierarchy remain recognizable, but exact wording is not uniformly acceptance-reliable. At r4.0, fine axes, citations, provenance, and lower-support text are also not acceptance-reliable. Those severe variants are not promoted to acceptance thresholds.

## Evidence-backed action

Action: `INTEGRATION_GUARD_NOT_PIXEL_CORRECTION`

`MINIMUM_SCALE_DEFOCUS_GUARD_PASS20.json` adds the compound native-defocus plus minimum-scale boundary for future Hwao-authored layouts:

- all seven exact scene-specific gates and complete `RESULT HELD` capsules must remain directly readable after native radius-1.5 Gaussian defocus followed by 640×360 LANCZOS downscale;
- every required qualifier, uncertainty, branch, axis, unit, value, error bar, threshold, equation term, interpretation limit, and provenance fact must survive through direct high-contrast text plus a complete border, capsule, connector, marker, or stable geometry channel;
- no required meaning may live only in blur-fragile fine print, tiny axes or error bars, one-pixel lines, narrow glyph spacing, citations, provenance footers, subtle grids, low-contrast caveats, or global OCR;
- native radii 2.5 and 4.0 followed by 360p remain characterization only;
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
