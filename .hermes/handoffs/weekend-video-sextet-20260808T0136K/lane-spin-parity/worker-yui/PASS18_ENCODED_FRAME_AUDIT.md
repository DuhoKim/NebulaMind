# Pass 18 encoded-frame audit — 360p plus bottom-obstruction interaction

Status: `QA_ONLY_NOT_A_CANDIDATE_NOT_SCIENCE_ADJUDICATION`

Deepening pass: 18  
Extraction completed: see `qa/pass18_minimum_scale_obstruction_audit/extraction_receipt.json`  
Audit completed: `2026-08-08T11:27:07+09:00`

## Authority and custody

Before this pass I re-read:

- `HWAO_WEEKEND_ORDER.md`
- `COORDINATION_UPDATE.md`
- `lanes/spin/BRIEF.md`
- `STATUS.json`
- `SOURCE_STATUS_FREEZE.json`
- the preserved failed-candidate `RECEIPT.md`, `QA.md`, `hashes.txt`, and contact sheet
- sealed `STORYBOARD_PROPOSAL.json`, the v8 render receipt, frames, and contact sheet
- the pass-17 immutable review snapshot and encoded-frame audit
- `LANE_RECEIPT.md`

Custody held:

- failed candidate SHA-256: `02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431`
- worker source freeze SHA-256: `ecff0992015e0bea2b86c14fbf627b79348228bc387d4ad4523208f4925a56a1`
- sealed storyboard remains v8
- sealed v8, pass-7 proof, and pass-12 proof were read-only inputs
- no v9 or candidate was created

The sealed contact sheet still uses `GALAXY SPIN`, preserves graphics-first method/status boundaries, and contains no audience-visible forbidden result/cosmology topics. The candidate contact sheet remains dominated by result-bearing headlines, numbers, cards, plots, and conclusions without a persistent structural held boundary.

## Fresh representation boundary

Pass 18 tests an order-specific interaction not established by standalone pass 6 or pass 7:

1. decode a fresh native 1920×1080 RGB midpoint;
2. downscale the full canvas to 640×360 with Pillow LANCZOS;
3. apply an opaque black bottom mask to represented 360p pixels;
4. prove every pixel above the mask boundary remains byte-identical to the lossless 360p downscale;
5. save static non-optimized RGB PNG evidence.

Operational compound variants:

- `caption15_360p`: mask rows `306..359`
- `player_ui25_360p`: mask rows `270..359`

Reference:

- `downscale_360p`

Characterization only:

- `heavy35_360p`: mask rows `234..359`

This is a packet-specific representation stress. The masks are not evidence about a named caption renderer, player, browser, platform, service, display, room, viewer, or universal standard.

## Fresh extraction

`qa/extract_pass18_minimum_scale_obstruction_frames.py` independently reran the ffmpeg 160×90 grayscale scene detector at score `>0.03`.

Result:

- cuts: `15/15`, exact pass-17 timestamps
- scenes: `16`
- fresh native midpoint frames byte-identical to pass 17: `16/16`
- candidate static frames: `80`
- variants per scene: `5`

The preserved candidate itself was not changed.

## Method derivatives

`qa/build_pass18_v8_minimum_scale_obstruction.py` derived the same variants from three read-only method groups:

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
| lossless 360p reference | 0.894444 | 0.668251 | 0.328090 | 0.288889 | 0/16 |
| caption 15% at 360p | 0.894444 | 0.565589 | 0.089888 | 0.244444 | 0/16 |
| player UI 25% at 360p | 0.894444 | 0.548479 | 0.049438 | 0.233333 | 0/16 |
| heavy 35% characterization | 0.894444 | 0.527567 | 0.006742 | 0.166667 | 0/16 |

The opaque masks remove all OCR tokens whose centers were in the masked downscale zones:

- caption 15%: `124 → 0`
- player UI 25%: `148 → 0`
- heavy 35%: `188 → 0`

These are token-occlusion diagnostics, not semantic scores.

### Held-critical scenes 7, 9, 10, 11, and 16

| Variant | Headline recall | Full-text recall | Lower-support recall | Numeric recall | Structural gates |
|---|---:|---:|---:|---:|---:|
| lossless 360p reference | 0.881720 | 0.425532 | 0.280323 | 0.242857 | 0/5 |
| caption 15% at 360p | 0.881720 | 0.247582 | 0.040431 | 0.200000 | 0/5 |
| player UI 25% at 360p | 0.881720 | 0.241779 | 0.029650 | 0.200000 | 0/5 |
| heavy 35% characterization | 0.881720 | 0.220503 | 0.000000 | 0.114286 | 0/5 |

Human represented-pixel review agrees with the hierarchy finding:

- large result headlines, numbers, bars, matrices, plots, and conclusions remain primary above the operational masks;
- no structural `RESULT HELD`, `FRAME UNSTATED`, `OUTCOMES WITHHELD`, `NO OUTCOME SHOWN`, or `RESULT LOCKED` boundary appears;
- axes, error bars, caveats, citations, provenance, and lower explanatory support are occluded first;
- the interaction deepens the assertion-versus-support imbalance and does not repair or authorize the candidate.

## Method-proof result

Human review at operational player-UI 25% obstruction:

| Proof | Exact top gates | `RESULT HELD` badges | Scene-specific status complete | Clipping/overlap/ambiguity |
|---|---:|---:|---:|---:|
| sealed v8 | not a top-gate proof | 7/7 | no; lower boundaries S2–S6 occluded | no ambiguity in surviving generic hold, but exact scope incomplete |
| pass-7 caption-safe | 7/7 | 7/7 | yes | none |
| pass-12 strengthened | 7/7 | 7/7 | yes | none |

The sealed-v8 generic hold survives, but a generic badge alone is not a complete scene-specific boundary. This reconfirms the need for the existing pass-7/pass-12 top-gate correction rather than creating another pixel change.

Pass-12 mapped gate-crop character similarity:

| Variant | Mean best-of-PSM 6/7/11/13 similarity | Gates passing ≥0.80 | Exact top-pixel identity |
|---|---:|---:|---:|
| lossless 360p | 0.985159 | 7/7 | reference |
| caption 15% at 360p | 0.985159 | 7/7 | 7/7 |
| player UI 25% at 360p | 0.985159 | 7/7 | 7/7 |
| heavy 35% characterization | 0.985159 | 7/7 | 7/7 |

The recognizer uses the predeclared mapped 360p gate crop and PSM set. It stores scores, not recognized text. Global OCR remains a diagnostic only; represented-pixel human review and complete-container visibility are decisive.

## Evidence-backed action

Action: `INTEGRATION_GUARD_NOT_PIXEL_CORRECTION`

`MINIMUM_SCALE_OBSTRUCTION_GUARD_PASS18.json` adds the compound minimum-scale plus obstruction boundary for future Hwao-authored layouts:

- all seven exact status gates and complete `RESULT HELD` capsules must remain above the bottom 25% boundary at represented 640×360 pixels;
- locked inputs, archive-frame uncertainty, outcomes withheld, unavailable rungs, and separate-authorization conditions must remain direct readable text outside the mask;
- no required qualifier, uncertainty, branch distinction, axis, unit, value, error bar, threshold, equation term, provenance fact, or interpretation limit may live only in the lower 25%;
- the 35% mask remains characterization only;
- exact upper-pixel identity and human represented-pixel review are required.

A new visual or copy correction is not evidence-justified. The latest pass-12 proof preserves all seven exact gates and badges under both operational masks without clipping, overlap, or ambiguity. Its strengthened top gate also survives the 35% characterization mask, while lower scientific support is deliberately unavailable.

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
