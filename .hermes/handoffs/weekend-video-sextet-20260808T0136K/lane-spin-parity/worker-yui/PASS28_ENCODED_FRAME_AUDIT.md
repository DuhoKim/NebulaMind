# Pass 28 encoded-frame audit — color/monochrome → 360p → represented horizontal smear w3

Status: `QA_ONLY_NOT_A_CANDIDATE_NOT_SCIENCE_ADJUDICATION`

Deepening pass: 28  
Extraction started: `2026-08-08T15:26:20+09:00`  
Audit packet written: `2026-08-08T15:32:30+09:00`

## Authority and custody

Re-read the current Hwao order, coordination update, spin brief, worker status and receipt, source/status freeze, sealed storyboard and v8 receipt, failed candidate 0149 receipt/QA/hashes, and pass-27 snapshot/audit.

- Candidate 0149 SHA-256 remains `02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431`.
- Source/status freeze remains `ecff0992015e0bea2b86c14fbf627b79348228bc387d4ad4523208f4925a56a1` with `video_reportable_now=false`.
- Candidate 0149 was decoded read-only and preserved. No candidate or v9 was created.
- Sealed v8 and pass-7/pass-12 proof sources were not modified.

## Fresh transform

Order for each of five presentation variants:

1. native full color, native linear-light BT.709 grayscale, or one fixed packet-specific Machado severity-100 presentation matrix;
2. full-canvas Pillow LANCZOS reduction to 640×360;
3. centered horizontal width-3 box smear on represented pixels, with edge replication, uint64 accumulation, and integer round-half-up division.

This is a packet-specific ordered presentation stress. It is not asserted to equal a native-resolution kernel, clinical view, named display, player, projector, browser, platform, service, room, viewer, or universal standard.

## Deterministic extraction and custody

- Fresh ffmpeg scene detection reproduced 15/15 cuts.
- Fresh native midpoint decodes: 16/16 byte-identical to pass 27.
- Pass-23 640×360 presentation baselines reproduced pixel-exactly:
  - candidate: 80/80;
  - sealed-v8/pass-7/pass-12 method proofs: 105/105.
- Centered horizontal width-3 smear recomputation: 185/185 exact.
- PNG output only; no audio or video encoded.

## Candidate 0149 quantitative aid

OCR values are aids only. They compare each smeared represented frame with its exact pass-23 no-smear baseline.

| variant | headline recall | full recall | lower-support recall | numeric recall | PSNR dB | MAE | tolerant edge recall | horizontal gradient ratio | vertical gradient ratio |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| color | 0.924138 | 0.736215 | 0.105634 | 0.444444 | 28.246489 | 2.467715 | 0.968532 | 0.536725 | 0.842925 |
| grayscale | 0.910959 | 0.706436 | 0.099010 | 0.454545 | 28.364668 | 2.434963 | 0.969556 | 0.536574 | 0.842648 |
| protanopia | 0.944056 | 0.810373 | 0.250000 | 0.666667 | 28.182392 | 2.486796 | 0.967930 | 0.536956 | 0.842697 |
| deuteranopia | 0.903448 | 0.762481 | 0.233577 | 0.562500 | 28.259909 | 2.465003 | 0.968096 | 0.536409 | 0.843128 |
| tritanopia | 0.850649 | 0.696165 | 0.258741 | 0.384615 | 28.429974 | 2.417746 | 0.967345 | 0.535701 | 0.843326 |

The directional metric behaves as expected: horizontal gradient energy falls to about 0.536 while vertical gradient energy remains about 0.843. This describes the ordered transform, not a scientific defect.

## Encoded-pixel review

Candidate 0149:

- Large result headlines, numbers, plots, bars, matrices, and conclusions remain primary.
- Narrow glyph strokes, thin vertical separators, fine axes/ticks, small error bars, units/legends, caveats, citations, provenance, and small qualifiers soften first.
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

The inherited fixed gate crop, nearest-neighbour enlargement, four-PSM Tesseract aid passed the 0.80 heuristic for 7/7 color, 5/7 deuteranopia, 4/7 grayscale, 5/7 protanopia, and 5/7 tritanopia gates. Mean similarities were 0.911576, 0.843920, 0.827568, 0.864051, and 0.830960 respectively; the minimum individual score was 0.545455.

Direct review of the encoded contact sheets confirms all 7/7 top lines in every variant. The OCR undercount is retained transparently rather than reclassified as a semantic defect or used to alter the inherited threshold.

## Evidence-backed action

Adopt `COLOR_MINIMUM_SCALE_REPRESENTED_SMEAR_GUARD_PASS28.json`; do not make a pixel or copy correction.

The pass-7/pass-12 correction remains sufficient. A later separately authored iteration must keep status and required meaning in direct text plus complete non-color geometry and may not place sole meaning in hue or horizontal-smear-fragile detail.

## Blockers

`BLOCKER_PACKET_PASS28.json` preserves the exact blockers:

1. no valid independent post-run A3.8 verdict record bound to the exact frozen all-209-file T4 artifact;
2. `KUN_FRAME_REVIEW.md` remains `FRAME REVIEW: AGREES FRAME_UNSTATED`;
3. `video_reportable_now` remains false.

No blocker was repaired, weakened, or invented. Hwao remains sole integrator.
