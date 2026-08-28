# Pass 30 encoded-frame audit — color/monochrome → 360p → represented bilinear resampling round trip

Status: `QA_ONLY_NOT_A_CANDIDATE_NOT_SCIENCE_ADJUDICATION`

Deepening pass: 30  
Extraction started: `2026-08-08T16:06:12+09:00`  
Audit packet written: `2026-08-08T16:13:54+09:00`

## Authority and custody

Re-read the current Hwao order, coordination update, spin brief, worker status and receipt, source/status freeze, sealed storyboard and v8 receipt, failed candidate 0149 receipt/QA/hashes, and pass-29 snapshot/audit.

- Candidate 0149 SHA-256 remains `02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431`.
- Source/status freeze remains `ecff0992015e0bea2b86c14fbf627b79348228bc387d4ad4523208f4925a56a1` with `video_reportable_now=false`.
- Candidate 0149 was decoded read-only and preserved. No candidate or v9 was created.
- Sealed v8 and pass-7/pass-12 proof sources were not modified.

## Fresh transform

Order for each of five presentation variants:

1. native full color, native linear-light BT.709 grayscale, or one fixed packet-specific Machado severity-100 presentation matrix;
2. full-canvas Pillow LANCZOS reduction to 640×360;
3. represented-pixel Pillow BILINEAR reduction to 512×288;
4. represented-pixel Pillow BILINEAR restoration to 640×360.

This is a fresh isotropic resampling-chain stress. Pass 29 used a vertical width-3 represented-pixel smear and pass 28 used a horizontal one; pass 30 instead tests a two-stage bilinear representation round trip. It is not asserted to equal a named display, player, browser, projector, platform, service, room, viewer, scaling policy, delivery route, or universal standard.

## Deterministic extraction and custody

- Fresh ffmpeg scene detection reproduced 15/15 cuts.
- Fresh native midpoint decodes: 16/16 byte-identical to pass 29.
- Pass-23 640×360 presentation baselines reproduced pixel-exactly:
  - candidate: 80/80;
  - sealed-v8/pass-7/pass-12 method proofs: 105/105.
- Two-stage bilinear round-trip recomputation: 185/185 exact.
- PNG output only; no audio or video encoded.

## Candidate 0149 quantitative aid

OCR values are aids only. They compare each restored frame with its exact pass-23 no-round-trip baseline.

| variant | headline recall | full recall | lower-support recall | numeric recall | PSNR dB | MAE | tolerant edge recall | horizontal gradient ratio | vertical gradient ratio |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| color | 0.965517 | 0.870343 | 0.443662 | 0.611111 | 28.543495 | 2.640403 | 0.951756 | 0.569166 | 0.580139 |
| grayscale | 0.952055 | 0.835165 | 0.267327 | 0.545455 | 28.636154 | 2.606439 | 0.951706 | 0.569134 | 0.579754 |
| protanopia | 0.979021 | 0.880065 | 0.330000 | 0.666667 | 28.493605 | 2.657990 | 0.950065 | 0.569618 | 0.579697 |
| deuteranopia | 0.972414 | 0.877458 | 0.459854 | 0.625000 | 28.551660 | 2.639625 | 0.951041 | 0.569330 | 0.580768 |
| tritanopia | 0.961039 | 0.856932 | 0.391608 | 0.692308 | 28.681935 | 2.595054 | 0.950162 | 0.568743 | 0.580992 |

Both gradient directions fall to about 0.57–0.58, as expected for an isotropic two-stage resampling chain. This describes the ordered transform, not a scientific defect.

## Encoded-pixel review

Candidate 0149:

- Large result headlines, numbers, plots, bars, matrices, and conclusions remain primary.
- One-pixel rules and connectors, small glyph counters and narrow spacing, fine axes and grid rules, error bars, small units/legends, caveats, citations, provenance, and small qualifiers soften first.
- Structural held/status gates: 0/16 under every variant.
- Held-critical scenes 7, 9, 10, 11, and 16: 0/5 under every variant.
- No transform-specific clipping, overlap, or meaning-changing ambiguity was observed.
- The transform does not repair or authorize the candidate.

Method proofs:

- Sealed v8 complete RESULT HELD badges: 7/7 under every variant.
- Sealed v8 major method/status boundaries and GALAXY SPIN headers: 7/7 under every variant.
- Pass-7 exact top gate lines and complete badges: 7/7 under every variant.
- Pass-12 exact top gate lines, complete containers, badges, and separated header/gate/badge/headline layers: 7/7 under every variant.
- Direct labels and non-color geometry remain load-bearing; hue-only required meaning: 0.
- No clipping, overlap, or meaning-changing ambiguity was observed.

## OCR-aid boundary

The inherited fixed gate crop, nearest-neighbour enlargement, four-PSM Tesseract aid passed the unchanged 0.80 heuristic for 4/7 color, 4/7 grayscale, 5/7 protanopia, 4/7 deuteranopia, and 4/7 tritanopia gates. Mean similarities were 0.758973, 0.783481, 0.841171, 0.755511, and 0.795360 respectively; the minimum individual score was 0.285714.

Direct review of the represented contact sheets confirms all 7/7 top lines in every variant. The OCR undercount and low segmentation score are retained transparently rather than reclassified as semantic defects or used to alter the inherited threshold.

## Evidence-backed action

Adopt `COLOR_MINIMUM_SCALE_REPRESENTED_RESAMPLING_ROUNDTRIP_GUARD_PASS30.json`; do not make a pixel or copy correction.

The pass-7/pass-12 correction remains sufficient. A later separately authored iteration must keep status and required meaning in direct text plus complete non-color geometry and may not place sole meaning in hue or resampling-fragile one-pixel/fine support.

## Blockers

`BLOCKER_PACKET_PASS30.json` preserves the exact blockers:

1. no valid independent post-run A3.8 verdict record bound to the exact frozen all-209-file T4 artifact;
2. `KUN_FRAME_REVIEW.md` remains `FRAME REVIEW: AGREES FRAME_UNSTATED`;
3. `video_reportable_now` remains false.

No blocker was repaired, weakened, or invented. Hwao remains sole integrator.
