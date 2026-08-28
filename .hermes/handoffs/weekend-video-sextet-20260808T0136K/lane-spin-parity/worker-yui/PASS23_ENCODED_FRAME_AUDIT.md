# Pass 23 encoded-frame audit — native monochrome/color-vision transforms followed by 360p

Status: `QA_ONLY_NOT_A_CANDIDATE_NOT_SCIENCE_ADJUDICATION`

Deepening pass: 23  
Extraction completed: `2026-08-08T13:28:02+09:00`  
Audit completed: `2026-08-08T13:36:15+09:00`

## Authority and custody

Before this pass I re-read:

- `HWAO_WEEKEND_ORDER.md`
- `COORDINATION_UPDATE.md`
- `lanes/spin/BRIEF.md`
- `STATUS.json`
- `SOURCE_STATUS_FREEZE.json`
- the preserved failed candidate receipt, QA, hashes, and contact sheet
- sealed `STORYBOARD_PROPOSAL.json`, v8 render receipt, frames, and contact sheet
- the pass-22 immutable review snapshot, guard, encoded-frame audit, and lane receipt

Custody held:

- failed candidate SHA-256: `02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431`
- worker source-freeze SHA-256: `ecff0992015e0bea2b86c14fbf627b79348228bc387d4ad4523208f4925a56a1`
- sealed storyboard remains v8
- sealed v8, pass-7 proof, and pass-12 proof were read-only inputs
- no v9 or candidate was created

The sealed method contact sheet still uses `GALAXY SPIN`, preserves method/status boundaries, and contains no audience-visible forbidden result/cosmology topics. The candidate remains dominated by result-bearing headlines, numbers, plots, matrices, and conclusions without a persistent structural held boundary.

## Fresh representation boundary

Pass 23 tests an order-specific interaction not established by standalone pass 8 or pass 6:

1. decode a fresh native 1920×1080 RGB midpoint;
2. preserve a full-color reference;
3. at native size apply either linear-light BT.709 grayscale or one fixed Machado severity-100 color-vision presentation matrix in float64;
4. clip, sRGB-encode, and round with NumPy `rint` to RGB uint8;
5. downscale the complete transformed canvas to 640×360 using Pillow LANCZOS;
6. independently recompute every represented derivative from its native source.

Represented variants:

- `color_360p` — lossless represented reference
- `grayscale_bt709_then_360p`
- `protanopia_machado100_then_360p`
- `deuteranopia_machado100_then_360p`
- `tritanopia_machado100_then_360p`

All four transforms are packet-specific operational presentation stresses. They are not clinical diagnostics and do not claim a named display, player, browser, projector, codec, platform, service, room, viewer, or universal standard.

## Fresh extraction and method derivatives

`qa/extract_pass23_minimum_scale_color_vision_frames.py` independently reran the ffmpeg 160×90 grayscale scene-score detector at threshold `>0.03`.

Result:

- cuts: `15/15`, exact pass-22 timestamps
- scenes: `16`
- fresh native midpoint frames byte-identical to pass 22: `16/16`
- candidate static derivatives: `80`
- variants per scene: `5`

`qa/build_pass23_v8_minimum_scale_color_vision.py` applied the same five represented variants to three read-only method groups:

- sealed v8
- pass-7 caption-safe proof
- pass-12 sharpness-safe proof

Result:

- groups: `3`
- source scenes: `21`
- method static derivatives: `105`

## Candidate quantitative result

OCR retention and pixel/chroma metrics compare each compound transform with the exact full-color 640×360 scene.

| Variant | Headline | Full text | Lower support | Numeric | Edge recall | Chroma retention | Structural gates |
|---|---:|---:|---:|---:|---:|---:|---:|
| full-color 360p reference | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0/16 |
| BT.709 grayscale → 360p | 0.988533 | 0.930353 | 0.732388 | 0.828125 | 0.999991 | 0.000000 | 0/16 |
| protanopia matrix → 360p | 0.988533 | 0.939875 | 0.759153 | 0.848958 | 0.999921 | 0.818706 | 0/16 |
| deuteranopia matrix → 360p | 0.985408 | 0.954081 | 0.851875 | 0.880208 | 0.999977 | 0.907247 | 0/16 |
| tritanopia matrix → 360p | 0.988533 | 0.947530 | 0.787202 | 0.854167 | 0.999942 | 1.065977 | 0/16 |

The mean saturated-reference-pixel fraction is `0.035618`. Chroma retention above one is possible because a fixed matrix may increase RGB max-minus-min distance on some reference-saturated pixels; it is not a clinical or perceptual score.

Exact transform recomputation passes `16/16` for each variant.

### Held-critical scenes 7, 9, 10, 11, and 16

| Variant | Headline | Full text | Lower support | Numeric | Structural gates |
|---|---:|---:|---:|---:|---:|
| full-color 360p reference | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 0/5 |
| BT.709 grayscale → 360p | 0.973304 | 0.869521 | 0.791643 | 0.566667 | 0/5 |
| protanopia matrix → 360p | 0.973304 | 0.899252 | 0.877291 | 0.650000 | 0/5 |
| deuteranopia matrix → 360p | 0.963304 | 0.921284 | 0.899332 | 0.700000 | 0/5 |
| tritanopia matrix → 360p | 0.973304 | 0.912636 | 0.867047 | 0.650000 | 0/5 |

Human represented-pixel review finds:

- large result headlines, numbers, bars, matrices, plots, and conclusions remain primary across all transforms;
- no structural `RESULT HELD`, `FRAME UNSTATED`, `OUTCOMES WITHHELD`, `NO OUTCOME SHOWN`, `RESULT LOCKED`, or `RESULT STATUS · HELD` boundary appears;
- fine axes, error bars, legends, caveats, citations, provenance, and small support are less uniformly reliable at 360p;
- plot and matrix colors remain visually salient in color-vision variants, but labels, geometry, and position remain present;
- grayscale removes all chroma without adding a held boundary;
- there is no clipping or overlap that repairs the candidate;
- the interaction preserves the result hierarchy and does not repair or authorize the candidate.

## Method-proof result

Human represented-pixel review across all five represented variants:

| Proof | Exact top gates | Complete badges | Major status boundaries | Hue-only required meaning | Clipping/overlap/ambiguity |
|---|---:|---:|---:|---:|---:|
| sealed v8 | not a top-gate proof | 7/7 each | 7/7 each | 0 | none |
| pass-7 caption-safe | 7/7 each | 7/7 each | 7/7 each | 0 | none |
| pass-12 strengthened | 7/7 each | 7/7 each | 7/7 each | 0 | none |

Pass-12 mapped gate-crop OCR aid:

- threshold: `0.80`
- full-color 360p: mean `1.000000`, `7/7`
- grayscale then 360p: mean `1.000000`, `7/7`
- protanopia matrix then 360p: mean `1.000000`, `7/7`
- deuteranopia matrix then 360p: mean `1.000000`, `7/7`
- tritanopia matrix then 360p: mean `1.000000`, `7/7`
- exact transform recomputation: `7/7` per variant

All required method distinctions remain directly labelled and paired with non-color geometry: complete borders, arrows, connectors, line styles, positions, markers, unavailable rails, status columns, or separate cards. Header, gate, badge, headline, and diagram layers remain separated. No required scientific/status meaning depends on hue alone.

## Evidence-backed action

Action: `INTEGRATION_GUARD_NOT_PIXEL_CORRECTION`

`MINIMUM_SCALE_COLOR_REDUNDANCY_GUARD_PASS23.json` adds a cumulative compound guard:

- all seven exact gates and complete `RESULT HELD` badges must remain directly readable after each declared native monochrome/color-vision transform followed by 640×360;
- every required status, branch, comparison, equation term, axis, unit, value, error bar, threshold, unavailable rung, uncertainty, qualifier, provenance fact, and interpretation boundary must have a direct label plus at least one non-color shape, line style, marker, border, connector, stable position, pattern, or status-column channel;
- hue may reinforce but may not solely carry category, sign, direction, threshold crossing, availability, unresolved state, result status, or authorization;
- legends and matrices must directly name categories;
- exact transform recomputation and represented-pixel human review are required.

A new visual or copy correction is not evidence-justified. The pass-12 proof preserves every exact gate, badge, and redundant geometry channel under the operational suite without clipping, overlap, ambiguity, or hue-only required meaning.

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
