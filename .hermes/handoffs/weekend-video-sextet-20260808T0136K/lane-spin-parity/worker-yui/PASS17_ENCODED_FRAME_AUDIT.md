# Pass 17 encoded-frame audit — 360p plus JPEG 4:2:0 interaction

Status: `QA_ONLY_NOT_A_CANDIDATE_NOT_SCIENCE_ADJUDICATION`

Deepening pass: 17  
Extraction completed: see `qa/pass17_minimum_scale_recompression_audit/extraction_receipt.json`  
Audit completed: `2026-08-08T11:03:06+09:00`

## Authority and custody

Before this pass I re-read:

- `HWAO_WEEKEND_ORDER.md`
- `COORDINATION_UPDATE.md`
- `lanes/spin/BRIEF.md`
- `STATUS.json`
- `SOURCE_STATUS_FREEZE.json`
- the preserved failed-candidate `RECEIPT.md`, `QA.md`, `hashes.txt`, and contact sheet
- sealed `STORYBOARD_PROPOSAL.json`, the v8 render receipt, frames, and contact sheet
- the pass-16 immutable review snapshot and encoded-frame audit
- `LANE_RECEIPT.md`

Custody held:

- failed candidate SHA-256: `02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431`
- worker source freeze SHA-256: `ecff0992015e0bea2b86c14fbf627b79348228bc387d4ad4523208f4925a56a1`
- sealed storyboard remains v8
- sealed v8, pass-7 proof, and pass-12 proof were read-only inputs
- no v9 or candidate was created

The sealed contact sheet still uses `GALAXY SPIN`, preserves graphics-first method/status boundaries, and contains no audience-visible forbidden result/cosmology topics. The candidate contact sheet remains dominated by result-bearing headlines, numbers, cards, plots, and conclusions without a persistent structural held boundary.

## Fresh representation boundary

Pass 17 tests an order-specific interaction not established by standalone pass 6 or pass 11:

1. decode a fresh native 1920×1080 RGB midpoint;
2. downscale the full canvas to 640×360 with Pillow LANCZOS;
3. encode the represented 360p pixels as Pillow JPEG with `subsampling=2` (4:2:0), `optimize=false`, and `progressive=false`;
4. decode the exact JPEG byte stream to RGB;
5. save decoded pixels as non-optimized PNG for static QA.

Operational compound variant:

- `jpeg_q60_420_360p`

Reference:

- `downscale_360p` lossless RGB PNG

Characterization only:

- `jpeg_q35_420_360p`
- `jpeg_q20_420_360p`

This is a packet-specific representation stress. Pillow quality values are library parameters, not evidence about a named codec ladder, display, player, browser, platform, upload route, delivery service, room, viewer, or universal standard.

## Fresh extraction

`qa/extract_pass17_minimum_scale_recompression_frames.py` independently reran the ffmpeg 160×90 grayscale scene detector at score `>0.03`.

Result:

- cuts: `15/15`, exact pass-16 timestamps
- scenes: `16`
- fresh native midpoint frames byte-identical to pass 16: `16/16`
- candidate static frames: `80`
- variants per scene: `5`

The preserved candidate itself was not changed.

## Method derivatives

`qa/build_pass17_v8_minimum_scale_recompression.py` derived the same five variants from three read-only method groups:

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
| lossless 360p reference | 0.957977 | 0.762310 | 0.355206 | 0.508145 | 0/16 |
| q60 4:2:0 at 360p | 0.936728 | 0.752200 | 0.340235 | 0.480409 | 0/16 |
| q35 4:2:0 at 360p | 0.936728 | 0.733435 | 0.332694 | 0.458181 | 0/16 |
| q20 4:2:0 at 360p | 0.944572 | 0.680946 | 0.290992 | 0.458181 | 0/16 |

Operational diagnostics:

- q60 combined backprojected RGB PSNR: `28.174973 dB`
- q60 combined tolerant luma-edge recall: `0.858432`
- q60 mean JPEG byte count: `16,983`

These values characterize represented-pixel loss only. OCR is non-monotonic under segmentation changes and does not validate any scientific claim.

### Held-critical scenes 7, 9, 10, 11, and 16

| Variant | Headline recall | Full-text recall | Lower-support recall | Numeric recall | Structural gates |
|---|---:|---:|---:|---:|---:|
| lossless 360p reference | 0.913804 | 0.533821 | 0.533146 | 0.466065 | 0/5 |
| q60 4:2:0 at 360p | 0.879137 | 0.515556 | 0.523977 | 0.417308 | 0/5 |
| q20 characterization | 0.877804 | 0.435024 | 0.441690 | 0.372846 | 0/5 |

Human encoded-frame review agrees with the hierarchy finding:

- large result headlines, numbers, bars, matrices, plots, and conclusions remain primary through q60 and q20 at 360p;
- no structural `RESULT HELD`, `FRAME UNSTATED`, `OUTCOMES WITHHELD`, `NO OUTCOME SHOWN`, or `RESULT LOCKED` boundary appears;
- fine axes, tick labels, error bars, caveats, citations, and provenance weaken first and are not uniformly acceptance-readable at q60 360p;
- the compound transform deepens the assertion-versus-support imbalance and does not repair or authorize the candidate.

## Method-proof result

Human review of represented q60 360p pixels:

| Proof | Exact scene gates | `RESULT HELD` badges | Major status boundaries | Clipping/overlap/ambiguity |
|---|---:|---:|---:|---:|
| sealed v8 | not a top-gate proof | 7/7 | 7/7 | none |
| pass-7 caption-safe | 7/7 | 7/7 | 7/7 | none |
| pass-12 strengthened | 7/7 | 7/7 | 7/7 | none |

Mapped pass-12 gate-crop character similarity:

| Variant | Mean best-of-PSM 6/7/11/13 similarity | Gates passing ≥0.80 |
|---|---:|---:|
| lossless 360p | 1.000000 | 7/7 |
| q60 4:2:0 at 360p | 1.000000 | 7/7 |
| q35 4:2:0 at 360p | 1.000000 | 7/7 |
| q20 4:2:0 at 360p | 0.988874 | 7/7 |

The recognizer maps the pass-12 native gate box to represented 360p pixels, adds four represented-pixel padding, enlarges that crop fourfold with LANCZOS for recognition only, and uses a predeclared fixed PSM set. It stores scores, not recognized text.

Global full-frame OCR under-counts small visibly readable gates and badges at 360p. It is not used as the acceptance oracle. Exact mapped crops plus human review of represented pixels and complete containers are decisive.

## Evidence-backed action

Action: `INTEGRATION_GUARD_NOT_PIXEL_CORRECTION`

`MINIMUM_SCALE_RECOMPRESSION_GUARD_PASS17.json` adds the minimum-scale plus recompression boundary for future Hwao-authored layouts:

- q60 4:2:0 after 640×360 LANCZOS downscale is the packet's operational compound transform;
- q35 and q20 remain characterization only;
- required status, interpretation, uncertainty, branch, and result-held boundaries must remain direct readable text at represented q60 360p pixels;
- required meaning may not depend only on fine chroma detail, one-pixel lines, tiny axes, small error bars, citations, provenance footers, or low-contrast caveats;
- required axes, units, values, thresholds, branches, and equation terms need direct readable labels;
- exact mapped crops and represented-pixel human review are required; global OCR alone is insufficient.

A new visual or copy correction is not evidence-justified because the pass-12 proof retains all seven exact gates and badges at operational q60 without clipping, overlap, or ambiguity. It also retains all seven exact gates under q20 characterization.

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
