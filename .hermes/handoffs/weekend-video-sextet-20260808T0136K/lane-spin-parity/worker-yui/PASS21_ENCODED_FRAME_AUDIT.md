# Pass 21 encoded-frame audit — native directional smear followed by 360p

Status: `QA_ONLY_NOT_A_CANDIDATE_NOT_SCIENCE_ADJUDICATION`

Deepening pass: 21  
Extraction completed: `2026-08-08T12:36:41+09:00`  
Audit completed: `2026-08-08T12:45:34+09:00`

## Authority and custody

Before this pass I re-read:

- `HWAO_WEEKEND_ORDER.md`
- `COORDINATION_UPDATE.md`
- `lanes/spin/BRIEF.md`
- `STATUS.json`
- `SOURCE_STATUS_FREEZE.json`
- the preserved failed-candidate receipt, QA, hashes, and contact sheet
- sealed `STORYBOARD_PROPOSAL.json`, v8 render receipt, frames, and contact sheet
- the pass-20 immutable review snapshot, guard, and encoded-frame audit
- `LANE_RECEIPT.md`

Custody held:

- failed candidate SHA-256: `02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431`
- worker source-freeze SHA-256: `ecff0992015e0bea2b86c14fbf627b79348228bc387d4ad4523208f4925a56a1`
- sealed storyboard remains v8
- sealed v8, pass-7 proof, and pass-12 proof were read-only inputs
- no v9 or candidate was created

The sealed contact sheet still uses `GALAXY SPIN`, preserves method/status boundaries, and contains no audience-visible forbidden result/cosmology topics. The candidate remains dominated by result-bearing headlines, numbers, cards, plots, and conclusions without a persistent structural held boundary.

## Fresh representation boundary

Pass 21 tests an order-specific interaction not established by standalone pass 6 or pass 13:

1. decode a fresh native 1920×1080 RGB midpoint;
2. apply a centered horizontal box smear at the native canvas using edge replication, `uint64` channel sums, and integer round-half-up division;
3. downscale the full smeared canvas to 640×360 with Pillow LANCZOS;
4. save static non-optimized RGB PNG evidence;
5. independently recompute the exact compound transform from the native source and compare represented RGB pixels.

Operational compound variant:

- `smear_w07_then_360p`: native horizontal width 7 pixels, then 640×360

Reference:

- `downscale_360p`: lossless native-to-640×360 LANCZOS

Characterization only:

- `smear_w13_then_360p`
- `smear_w21_then_360p`

These are packet-specific representation stresses, not evidence about a named camera, lens, motion, exposure, projector, display, player, browser, platform, service, room, viewer, or universal standard.

## Fresh extraction

`qa/extract_pass21_minimum_scale_directional_smear_frames.py` independently reran the ffmpeg 160×90 grayscale scene detector at score `>0.03`.

Result:

- cuts: `15/15`, exact pass-20 timestamps
- scenes: `16`
- fresh native midpoint frames byte-identical to pass 20: `16/16`
- candidate static frames: `80`
- variants per scene: `5`

The preserved candidate itself was not changed.

## Method derivatives

`qa/build_pass21_v8_minimum_scale_directional_smear.py` derived the same variants from three read-only method groups:

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
| native width 7 then 360p | 0.850000 | 0.620722 | 0.265169 | 0.122222 | 0/16 | 16/16 |
| native width 13 then 360p characterization | 0.633333 | 0.332700 | 0.022472 | 0.144444 | 0/16 | 16/16 |
| native width 21 then 360p characterization | 0.216667 | 0.066540 | 0.011236 | 0.055556 | 0/16 | 16/16 |

The operational derivative has:

- mean incremental RGB PSNR: `30.957814 dB`
- mean incremental absolute RGB error: `1.789840`
- tolerant luma-edge recall: `0.983109`
- x-gradient-energy ratio: `0.357208`
- y-gradient-energy ratio: `0.736968`
- x-to-y gradient-retention ratio: `0.484240`

The anisotropic loss is expected from the declared transform: horizontal averaging suppresses vertical strokes and x-direction gradients more strongly. These diagnostics characterize the represented pixels only; they do not model a named physical or delivery system.

### Held-critical scenes 7, 9, 10, 11, and 16

| Variant | Headline recall | Full-text recall | Lower-support recall | Numeric recall | Structural gates |
|---|---:|---:|---:|---:|---:|
| lossless 360p reference | 0.881720 | 0.425532 | 0.280323 | 0.242857 | 0/5 |
| native width 7 then 360p | 0.795699 | 0.384913 | 0.266846 | 0.085714 | 0/5 |
| native width 13 then 360p characterization | 0.440860 | 0.133462 | 0.024259 | 0.128571 | 0/5 |
| native width 21 then 360p characterization | 0.086022 | 0.023211 | 0.005391 | 0.000000 | 0/5 |

Human represented-pixel review agrees with the hierarchy finding:

- large result headlines, large numbers, bars, matrices, plot silhouettes, and conclusions remain the primary hierarchy at width 7 and remain recognizable at width 21;
- no structural `RESULT HELD`, `FRAME UNSTATED`, `OUTCOMES WITHHELD`, `NO OUTCOME SHOWN`, `RESULT LOCKED`, or `RESULT STATUS · HELD` boundary appears;
- thin vertical edges, small labels, axes, error bars, legends, caveats, citations, provenance, and lower explanatory support weaken first;
- the interaction deepens the assertion-versus-support imbalance and does not repair or authorize the candidate.

No clipping or overlap creates a new held boundary. The severe characterization variants make exact small copy unreliable and are not acceptance thresholds.

## Method-proof result

Human represented-pixel review at operational native width 7 followed by 360p:

| Proof | Exact top gates | `RESULT HELD` badges | Major status boundaries | Clipping/overlap/ambiguity |
|---|---:|---:|---:|---:|
| sealed v8 | not a top-gate proof | 7/7 | 7/7 | none |
| pass-7 caption-safe | 7/7 | 7/7 | 7/7 | none |
| pass-12 strengthened | 7/7 | 7/7 | 7/7 | none |

Pass-12 mapped gate-crop character similarity:

| Variant | Mean best-of-PSM 6/7/11/13 similarity | Gates passing ≥0.80 | Exact transform |
|---|---:|---:|---:|
| lossless 360p | 0.985159 | 7/7 | reference |
| native width 7 then 360p | 0.945953 | 6/7 | 7/7 |
| native width 13 then 360p characterization | 0.212419 | 0/7 | 7/7 |
| native width 21 then 360p characterization | 0.161198 | 0/7 | 7/7 |

At operational width 7, scene 4 scores `0.780488`, below the disclosed `0.80` mapped-crop OCR threshold. Direct represented-pixel review nevertheless reads the complete exact gate `FRAME UNSTATED · RESULT HELD`, with its border, badge, and status hierarchy intact and no clipping, overlap, or semantic ambiguity. This aid result is reported rather than silently rounded up. An arbitrary OCR threshold alone neither proves semantic loss nor repairs a hierarchy.

At width 13 and width 21 characterization, all seven gate containers and status hierarchy remain recognizable, but exact wording and fine scientific support are not uniformly acceptance-reliable. Fine axes, citations, provenance, lower-support text, and narrow glyph detail are especially fragile. Those severe variants are not promoted to acceptance thresholds.

## Evidence-backed action

Action: `INTEGRATION_GUARD_NOT_PIXEL_CORRECTION`

`MINIMUM_SCALE_DIRECTIONAL_SMEAR_GUARD_PASS21.json` adds the compound native-directional-smear plus minimum-scale boundary for future Hwao-authored layouts:

- all seven exact scene-specific gates and complete `RESULT HELD` capsules must remain directly readable after native width-7 centered horizontal box smear followed by 640×360 LANCZOS downscale;
- every required qualifier, uncertainty, branch, axis, unit, value, error bar, threshold, equation term, interpretation limit, and provenance fact must survive through direct high-contrast text plus a complete border, capsule, connector, marker, or stable geometry channel;
- no required meaning may live only in thin vertical strokes, tiny axes/error bars, one-pixel connectors, narrow glyph spacing, fine legends, citations, provenance footers, subtle grids, low-contrast caveats, or global OCR;
- native widths 13 and 21 followed by 360p remain characterization only;
- exact transform recomputation and represented-pixel human review are required, with mapped-crop OCR aid failures disclosed.

A new visual or copy correction is not evidence-justified. The latest pass-12 proof preserves all seven directly readable exact gates and badges under the operational interaction without clipping, overlap, or ambiguity. The one near-threshold mapped OCR miss is evidence for keeping human represented-pixel review decisive, not evidence for mutating sealed pixels or inventing copy.

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
