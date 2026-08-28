# Pass 31 encoded-frame audit — color/monochrome → 360p → represented main-diagonal smear w3

Status: `QA_ONLY_NOT_A_CANDIDATE_NOT_SCIENCE_ADJUDICATION`

Deepening pass: 31  
Extraction started: `2026-08-08T16:28:24+09:00`  
Audit packet written: `2026-08-08T16:32:39+09:00`

## Authority and custody

Re-read the current Hwao order, coordination update, spin brief, worker status and receipt, source/status freeze, sealed storyboard and v8 receipt, failed candidate 0149 receipt/QA/hashes, and pass-30 snapshot/audit.

- Candidate 0149 SHA-256 remains `02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431`.
- Source/status freeze remains `ecff0992015e0bea2b86c14fbf627b79348228bc387d4ad4523208f4925a56a1` with `video_reportable_now=false`.
- Candidate 0149 was decoded read-only and preserved. No candidate or v9 was created.
- Sealed v8 and pass-7/pass-12 proof sources were not modified.

## Fresh transform

Order for each of five presentation variants:

1. native full color, native linear-light BT.709 grayscale, or one fixed packet-specific Machado severity-100 presentation matrix;
2. full-canvas Pillow LANCZOS reduction to 640×360;
3. represented-pixel centered main-diagonal NW-SE width-3 box smear using offsets (−1,−1), (0,0), and (+1,+1), edge replication on both axes, uint64 accumulation, and integer round-half-up division.

This is a fresh diagonal-direction representation stress. Pass 28 used a horizontal kernel, pass 29 a vertical kernel, and pass 30 an isotropic bilinear resampling round trip. Pass 31 specifically suppresses gradients along the NW-SE sampling direction and stresses anti-diagonal/oblique edges and connectors. It is not a native-resolution equivalence or named lens, motion, display, player, platform, service, room, viewer, or universal standard.

## Deterministic extraction and custody

- Fresh ffmpeg scene detection reproduced 15/15 cuts.
- Fresh native midpoint decodes: 16/16 byte-identical to pass 30.
- Pass-23 640×360 presentation baselines reproduced pixel-exactly:
  - candidate: 80/80;
  - sealed-v8/pass-7/pass-12 method proofs: 105/105.
- Centered main-diagonal width-3 smear recomputation: 185/185 exact.
- PNG output only; no audio or video encoded.

## Candidate 0149 quantitative aid

OCR values are aids only. They compare each smeared represented frame with its exact pass-23 no-smear baseline.

| variant | headline recall | full recall | lower-support recall | numeric recall | PSNR dB | MAE | tolerant edge recall | horizontal gradient | vertical gradient | main-diagonal gradient | anti-diagonal gradient |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| color | 0.944828 | 0.721311 | 0.183099 | 0.388889 | 26.169420 | 3.433393 | 0.946403 | 0.627436 | 0.664549 | 0.511647 | 0.671406 |
| grayscale | 0.917808 | 0.667190 | 0.079208 | 0.272727 | 26.270356 | 3.385109 | 0.947606 | 0.627017 | 0.664212 | 0.511778 | 0.671028 |
| protanopia | 0.930070 | 0.755267 | 0.170000 | 0.416667 | 26.112598 | 3.458074 | 0.945233 | 0.627338 | 0.664096 | 0.511956 | 0.671221 |
| deuteranopia | 0.937931 | 0.736762 | 0.182482 | 0.437500 | 26.181189 | 3.429453 | 0.945753 | 0.627325 | 0.664800 | 0.511232 | 0.671263 |
| tritanopia | 0.902597 | 0.703540 | 0.209790 | 0.307692 | 26.329640 | 3.365927 | 0.944843 | 0.626804 | 0.664981 | 0.510747 | 0.670961 |

The main-diagonal gradient ratio falls to about 0.511 while the anti-diagonal ratio remains about 0.671. This is consistent with the declared kernel and describes presentation damage, not a scientific defect.

## Encoded-pixel review

Candidate 0149:

- Large result headlines, numbers, plots, bars, matrices, and conclusions remain primary.
- Anti-diagonal and oblique strokes, diagonal connectors and arrowheads, small glyph joins/counters, fine axes and grids, sloped markers and error-bar caps, units, legends, caveats, citations, provenance, and small qualifiers soften first.
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

The inherited fixed gate crop, nearest-neighbour enlargement, four-PSM Tesseract aid passed the unchanged 0.80 heuristic for 1/7 color, 1/7 grayscale, 1/7 protanopia, 1/7 deuteranopia, and 1/7 tritanopia gates. Mean similarities were 0.607436, 0.647995, 0.602912, 0.654189, and 0.595801 respectively; the minimum individual score was 0.307692.

Direct review of the represented contact sheets confirms all 7/7 top lines in every variant. The severe OCR segmentation undercount is retained transparently rather than reclassified as a semantic defect or used to alter the inherited threshold.

## Evidence-backed action

Adopt `COLOR_MINIMUM_SCALE_REPRESENTED_DIAGONAL_SMEAR_GUARD_PASS31.json`; do not make a pixel or copy correction.

The pass-7/pass-12 correction remains sufficient. A later separately authored iteration must keep status and required meaning in direct text plus complete non-color geometry and may not place sole meaning in hue or diagonal-smear-fragile oblique/fine support.

## Blockers

`BLOCKER_PACKET_PASS31.json` preserves the exact blockers:

1. no valid independent post-run A3.8 verdict record bound to the exact frozen all-209-file T4 artifact;
2. `KUN_FRAME_REVIEW.md` remains `FRAME REVIEW: AGREES FRAME_UNSTATED`;
3. `video_reportable_now` remains false.

No blocker was repaired, weakened, or invented. Hwao remains sole integrator.
