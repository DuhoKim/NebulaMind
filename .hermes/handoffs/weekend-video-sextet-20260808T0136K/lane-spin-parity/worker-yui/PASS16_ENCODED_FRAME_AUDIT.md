# Pass 16 encoded-frame audit — compound anisotropic geometry at 360p

Status: `QA_ONLY_NOT_A_CANDIDATE_NOT_SCIENCE_ADJUDICATION`

Deepening pass: 16  
Extraction completed: `2026-08-08T10:24:21.907298+09:00`  
Audit completed: `2026-08-08T10:34:16+09:00`

## Authority and custody

Before this pass I re-read:

- `HWAO_WEEKEND_ORDER.md`
- `COORDINATION_UPDATE.md`
- `lanes/spin/BRIEF.md`
- `STATUS.json`
- `SOURCE_STATUS_FREEZE.json`
- the preserved failed-candidate `RECEIPT.md`, `QA.md`, `hashes.txt`, and contact sheet
- sealed `STORYBOARD_PROPOSAL.json`, the v8 render receipt, frames, and contact sheet
- the pass-15 immutable review snapshot and encoded-frame audit
- `LANE_RECEIPT.md`

Custody held:

- failed candidate SHA-256: `02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431`
- worker source freeze SHA-256: `ecff0992015e0bea2b86c14fbf627b79348228bc387d4ad4523208f4925a56a1`
- sealed storyboard remains v8
- sealed v8, pass-7 proof, and pass-12 proof were read-only inputs
- no v9 or candidate was created

## Fresh representation boundary

Pass 16 tests an interaction not covered by either prior boundary alone:

1. native centered anisotropic LANCZOS resampling;
2. centered black padding back to 1920×1080;
3. full-canvas LANCZOS downscale to 640×360.

Operational pair:

- `x90_360p`: native x scale 0.90, y scale 1.00, then 640×360
- `y90_360p`: native x scale 1.00, y scale 0.90, then 640×360

Characterization only:

- `x80_360p`
- `y80_360p`

This is a packet-specific compound representation stress. It is not evidence about a named display, player, projector, codec, browser, delivery platform, service, room, viewer, or pixel-aspect standard.

## Fresh extraction

`qa/extract_pass16_minimum_scale_geometry_frames.py` independently re-ran the ffmpeg 160×90 grayscale scene detector at score `>0.03`.

Result:

- cuts: `15/15`
- scenes: `16`
- fresh midpoint frames byte-identical to pass 15: `16/16`
- candidate static frames: `80`
- variants per scene: `5`

The preserved candidate itself was not changed.

## Method derivatives

`qa/build_pass16_v8_minimum_scale_geometry.py` derived the same five variants from three read-only method groups:

- sealed v8
- pass-7 caption-safe proof
- pass-12 sharpness-safe proof

Result:

- groups: `3`
- source scenes: `21`
- static derivative frames: `105`

## Candidate quantitative result

| Variant | Headline recall | Full-text recall | Lower-support recall | Numeric recall | Structural gates |
|---|---:|---:|---:|---:|---:|
| x90_360p | 0.920550 | 0.726070 | 0.682688 | 0.449145 | 0/16 |
| y90_360p | 0.912103 | 0.757360 | 0.717162 | 0.461298 | 0/16 |
| x80_360p | 0.910056 | 0.673028 | 0.618756 | 0.437099 | 0/16 |
| y80_360p | 0.898030 | 0.729645 | 0.687699 | 0.438835 | 0/16 |

Backprojected operational diagnostics:

| Variant | RGB PSNR dB | Tolerant luma-edge recall |
|---|---:|---:|
| x90_360p | 28.553735 | 0.911660 |
| y90_360p | 28.926930 | 0.914089 |

These diagnostics characterize represented-pixel loss only. They do not validate any scientific claim.

### Held-critical scenes 7, 9, 10, 11, and 16

| Variant | Headline recall | Full-text recall | Lower-support recall | Numeric recall | Structural gates |
|---|---:|---:|---:|---:|---:|
| x90_360p | 0.814727 | 0.480969 | 0.403528 | 0.324445 | 0/5 |
| y90_360p | 0.857394 | 0.516210 | 0.439766 | 0.363333 | 0/5 |

Human encoded-frame review agrees with the metrics:

- large result headlines, numbers, bars, matrices, plots, and conclusions remain primary;
- no `RESULT HELD`, `FRAME UNSTATED`, `OUTCOMES WITHHELD`, `NO OUTCOME SHOWN`, or `RESULT LOCKED` structural boundary appears;
- small axes, tick labels, error bars, caveats, citations, and provenance are not uniformly acceptance-readable at represented 360p pixels;
- required meaning cannot safely depend on those fine elements.

This deepens the preserved candidate failure. It does not create a new science finding.

## Method-proof result

Human review of represented output pixels:

| Proof | x90_360p | y90_360p | x80_360p | y80_360p |
|---|---:|---:|---:|---:|
| sealed-v8 `RESULT HELD` badges | 7/7 | 7/7 | not acceptance axis | not acceptance axis |
| sealed-v8 major status boundaries | 7/7 | 7/7 | not acceptance axis | not acceptance axis |
| pass-7 exact scene-specific gates | 7/7 | 7/7 | characterization only | characterization only |
| pass-7 `RESULT HELD` badges | 7/7 | 7/7 | characterization only | characterization only |
| pass-12 exact scene-specific gates | 7/7 | 7/7 | 7/7 | 7/7 |
| pass-12 `RESULT HELD` badges | 7/7 | 7/7 | 7/7 | 7/7 |

Mapped pass-12 gate-crop character similarity:

| Variant | Mean best-of-PSM 6/7/11/13 similarity | Exact gates passing ≥0.80 |
|---|---:|---:|
| x90_360p | 1.000000 | 7/7 |
| y90_360p | 0.973463 | 7/7 |
| x80_360p | 1.000000 | 7/7 |
| y80_360p | 0.979486 | 7/7 |

The crop recognizer maps the clean gate box through each compound transform, adds four output-pixel padding, enlarges the represented crop fourfold with LANCZOS for recognition only, and compares normalized alphanumeric sequences. It stores no recognized text.

Global full-frame OCR under-counts small badges and some pass-7 gate lines at 360p. It is therefore not used as the acceptance oracle. Exact mapped gate crops plus human review of represented pixels are decisive.

No clipping, overlap, or semantic ambiguity was observed. Fine source/provenance lines and some tertiary labels remain present but are not uniformly acceptance-readable; pass-12 acceptance does not depend on them.

## Evidence-backed action

Action: `INTEGRATION_GUARD_NOT_PIXEL_CORRECTION`

`MINIMUM_SCALE_GEOMETRY_GUARD_PASS16.json` adds the compound minimum-scale/geometry boundary for future Hwao-authored layouts:

- required status and interpretation boundaries must remain direct readable text after both operational transforms;
- required meaning may not depend only on geometry, color, or tiny fine print;
- required axes, units, values, error bars, thresholds, branches, and equation terms need direct readable labels at represented 360p pixels;
- future gate lines should meet or exceed the demonstrated pass-12 high-contrast bold 28 px / 1 px stroke contract at 1080p authoring scale;
- exact mapped crops and represented-pixel human review are required; global OCR alone is insufficient.

A new correction is not evidence-justified because the pass-12 proof retains all seven exact gates and badges under the operational pair and both severe characterization variants.

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
