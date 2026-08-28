# Pass 22 encoded-frame audit — native dark-tone floor followed by 360p

Status: `QA_ONLY_NOT_A_CANDIDATE_NOT_SCIENCE_ADJUDICATION`

Deepening pass: 22  
Extraction completed: `2026-08-08T13:03:49+09:00`  
Audit completed: `2026-08-08T13:09:21+09:00`

## Authority and custody

Before this pass I re-read:

- `HWAO_WEEKEND_ORDER.md`
- `COORDINATION_UPDATE.md`
- `lanes/spin/BRIEF.md`
- `STATUS.json`
- `SOURCE_STATUS_FREEZE.json`
- the preserved failed-candidate receipt, QA, hashes, and contact sheet
- sealed `STORYBOARD_PROPOSAL.json`, v8 render receipt, frames, and contact sheet
- the pass-21 immutable review snapshot, guard, encoded-frame audit, and lane receipt

Custody held:

- failed candidate SHA-256: `02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431`
- worker source-freeze SHA-256: `ecff0992015e0bea2b86c14fbf627b79348228bc387d4ad4523208f4925a56a1`
- sealed storyboard remains v8
- sealed v8, pass-7 proof, and pass-12 proof were read-only inputs
- no v9 or candidate was created

The sealed contact sheet still uses `GALAXY SPIN`, preserves method/status boundaries, and contains no audience-visible forbidden result/cosmology topics. The candidate remains dominated by result-bearing headlines, numbers, cards, plots, and conclusions without a persistent structural held boundary.

## Fresh representation boundary

Pass 22 tests an order-specific interaction not established by standalone pass 6 or pass 14:

1. decode a fresh native 1920×1080 RGB midpoint;
2. compute integer luma `Y=(54R+183G+19B+128)//256`;
3. apply native dark-tone floor/full-range remap `Y2=max(Y-f,0)×255/(255-f)` and hue-preserving `RGB2=RGB×Y2/Y`, both with integer round-half-up, with `Y=0` mapped to black;
4. downscale the complete transformed canvas to 640×360 with Pillow LANCZOS;
5. save static non-optimized RGB PNG evidence and independently recompute represented RGB pixels from native sources.

Operational compound variant:

- `floor16_then_360p`: native code-value floor 16, then 640×360

Reference:

- `downscale_360p`: lossless native-to-640×360 LANCZOS

Characterization only:

- `floor32_then_360p`
- `floor48_then_360p`

These are packet-specific representation stresses, not evidence about a named display, transfer function, codec, projector, player, browser, platform, service, room, viewer, or universal standard.

## Fresh extraction

`qa/extract_pass22_minimum_scale_dark_tone_frames.py` independently reran the ffmpeg 160×90 grayscale scene detector at score `>0.03`.

Result:

- cuts: `15/15`, exact pass-21 timestamps
- scenes: `16`
- fresh native midpoint frames byte-identical to pass 21: `16/16`
- candidate static frames: `80`
- variants per scene: `5`

The preserved candidate itself was not changed.

## Method derivatives

`qa/build_pass22_v8_minimum_scale_dark_tone.py` derived the same variants from three read-only method groups:

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
| native floor 16 then 360p | 0.894444 | 0.635932 | 0.256180 | 0.288889 | 0/16 | 16/16 |
| native floor 32 then 360p characterization | 0.894444 | 0.697719 | 0.395506 | 0.244444 | 0/16 | 16/16 |
| native floor 48 then 360p characterization | 0.905556 | 0.679658 | 0.352809 | 0.177778 | 0/16 | 16/16 |

The operational derivative has:

- mean incremental RGB PSNR: `23.432241 dB`
- mean incremental absolute RGB error: `16.031201`
- tolerant luma-edge recall: `0.998594`
- low-tone tolerant edge recall: `0.997481`
- mean luma retention: `0.405432`
- additional-black-pixel fraction: `0.647482`
- survival of represented nonzero dark pixels below luma 64: `0.308117`

The additional-black fraction is specific to this mostly black packet and is not evidence about real-world display prevalence. Non-monotonic OCR changes at floors 32 and 48 are segmentation effects, not semantic repair.

### Held-critical scenes 7, 9, 10, 11, and 16

| Variant | Headline recall | Full-text recall | Lower-support recall | Numeric recall | Structural gates |
|---|---:|---:|---:|---:|---:|
| lossless 360p reference | 0.881720 | 0.425532 | 0.280323 | 0.242857 | 0/5 |
| native floor 16 then 360p | 0.881720 | 0.352031 | 0.191375 | 0.242857 | 0/5 |
| native floor 32 then 360p characterization | 0.881720 | 0.481625 | 0.363881 | 0.200000 | 0/5 |
| native floor 48 then 360p characterization | 0.903226 | 0.479691 | 0.355795 | 0.171429 | 0/5 |

Human represented-pixel review agrees with the hierarchy finding:

- bright result headlines, large numbers, bars, matrices, plots, and conclusion framing remain primary;
- no structural `RESULT HELD`, `FRAME UNSTATED`, `OUTCOMES WITHHELD`, `NO OUTCOME SHOWN`, `RESULT LOCKED`, or `RESULT STATUS · HELD` boundary appears;
- dark background texture, grids, fine axes, error bars, dividers, caveats, citations, provenance, and lower support weaken before the bright assertion hierarchy;
- no clipping or overlap creates a held boundary;
- the interaction deepens assertion-versus-context imbalance and does not repair or authorize the candidate.

## Method-proof result

Human represented-pixel review at operational native floor 16 followed by 360p:

| Proof | Exact top gates | `RESULT HELD` badges | Major status boundaries | Clipping/overlap/ambiguity |
|---|---:|---:|---:|---:|
| sealed v8 | not a top-gate proof | 7/7 | 7/7 | none |
| pass-7 caption-safe | 7/7 | 7/7 | 7/7 | none |
| pass-12 strengthened | 7/7 | 7/7 | 7/7 | none |

Pass-12 mapped gate-crop character similarity:

| Variant | Mean best-of-PSM 6/7/11/13 similarity | Gates passing ≥0.80 | Exact transform |
|---|---:|---:|---:|
| lossless 360p | 0.985159 | 7/7 | reference |
| native floor 16 then 360p | 0.967458 | 7/7 | 7/7 |
| native floor 32 then 360p characterization | 0.989766 | 7/7 | 7/7 |
| native floor 48 then 360p characterization | 0.994129 | 7/7 | 7/7 |

All operational gates retain exact wording, complete borders, badges, connectors, rails, status columns, and separated header/gate/headline layers. The severe variants keep exact top-gate/status hierarchy, but dark grids, subtle dividers, citations, provenance, and fine support are not uniformly acceptance-reliable. Higher severe-variant OCR similarity is explicitly non-monotonic and does not promote floors 32 or 48 to acceptance thresholds.

## Evidence-backed action

Action: `INTEGRATION_GUARD_NOT_PIXEL_CORRECTION`

`MINIMUM_SCALE_DARK_TONE_GUARD_PASS22.json` adds the compound native-dark-tone-floor plus minimum-scale boundary for future Hwao-authored layouts:

- all seven exact scene gates and complete `RESULT HELD` capsules must remain directly readable after native floor 16 followed by 640×360;
- every required qualifier, uncertainty, branch, axis, unit, value, error bar, threshold, equation term, interpretation limit, and provenance fact must survive through direct high-contrast text plus complete borders, capsules, connectors, markers, rails, status columns, or stable geometry;
- no required meaning may live only at source-luma values at or below code value 16, in dark texture, subtle grids, fine axes/error bars, one-pixel dividers/connectors, low-contrast caveats, citations, provenance footers, or global OCR;
- floors 32 and 48 followed by 360p remain characterization only;
- exact transform recomputation and represented-pixel human review are required.

A new visual or copy correction is not evidence-justified. The latest pass-12 proof preserves all seven exact gates, badges, and redundant geometry under the operational interaction without clipping, overlap, or ambiguity.

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
