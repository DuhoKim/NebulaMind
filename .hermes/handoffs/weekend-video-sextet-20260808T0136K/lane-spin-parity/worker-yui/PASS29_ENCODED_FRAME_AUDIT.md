# Pass 29 encoded-frame audit — color/monochrome → 360p → represented vertical smear w3

Status: `QA_ONLY_NOT_A_CANDIDATE_NOT_SCIENCE_ADJUDICATION`

Deepening pass: 29  
Extraction started: `2026-08-08T15:47:50+09:00`  
Audit packet written: `2026-08-08T15:52:34+09:00`

## Authority and custody

Re-read the current Hwao order, coordination update, spin brief, worker status and receipt, source/status freeze, sealed storyboard and v8 receipt, failed candidate 0149 receipt/QA/hashes, and pass-28 snapshot/audit.

- Candidate 0149 SHA-256 remains `02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431`.
- Source/status freeze remains `ecff0992015e0bea2b86c14fbf627b79348228bc387d4ad4523208f4925a56a1` with `video_reportable_now=false`.
- Candidate 0149 was decoded read-only and preserved. No candidate or v9 was created.
- Sealed v8 and pass-7/pass-12 proof sources were not modified.

## Fresh transform

Order for each of five presentation variants:

1. native full color, native linear-light BT.709 grayscale, or one fixed packet-specific Machado severity-100 presentation matrix;
2. full-canvas Pillow LANCZOS reduction to 640×360;
3. centered vertical width-3 box smear on represented pixels, with edge replication, uint64 accumulation, and integer round-half-up division.

This is a fresh packet-specific ordered presentation stress. Pass 28 used a horizontal width-3 represented-pixel smear; pass 29 uses a vertical kernel. It is not asserted to equal a native-resolution kernel, clinical view, named display, player, projector, browser, platform, service, room, viewer, or universal standard.

## Deterministic extraction and custody

- Fresh ffmpeg scene detection reproduced 15/15 cuts.
- Fresh native midpoint decodes: 16/16 byte-identical to pass 28.
- Pass-23 640×360 presentation baselines reproduced pixel-exactly:
  - candidate: 80/80;
  - sealed-v8/pass-7/pass-12 method proofs: 105/105.
- Centered vertical width-3 smear recomputation: 185/185 exact.
- PNG output only; no audio or video encoded.

## Candidate 0149 quantitative aid

OCR values are aids only. They compare each smeared represented frame with its exact pass-23 no-smear baseline.

| variant | headline recall | full recall | lower-support recall | numeric recall | PSNR dB | MAE | tolerant edge recall | horizontal gradient ratio | vertical gradient ratio |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| color | 0.986207 | 0.876304 | 0.647887 | 0.500000 | 29.747925 | 1.932636 | 0.960106 | 0.883723 | 0.577560 |
| grayscale | 0.965753 | 0.660911 | 0.118812 | 0.636364 | 29.829991 | 1.904916 | 0.961113 | 0.883852 | 0.577354 |
| protanopia | 0.993007 | 0.808752 | 0.320000 | 0.416667 | 29.707663 | 1.941225 | 0.958644 | 0.883980 | 0.577294 |
| deuteranopia | 0.993103 | 0.826021 | 0.489051 | 0.562500 | 29.757066 | 1.929627 | 0.959793 | 0.883724 | 0.577670 |
| tritanopia | 0.954545 | 0.786136 | 0.391608 | 0.307692 | 29.866496 | 1.903311 | 0.958889 | 0.883976 | 0.577853 |

The directional metric behaves as expected: vertical gradient energy falls to about 0.577 while horizontal gradient energy remains about 0.884. This describes the ordered transform, not a scientific defect.

## Encoded-pixel review

Candidate 0149:

- Large result headlines, numbers, plots, bars, matrices, and conclusions remain primary.
- Horizontal glyph strokes and separators, fine horizontal grid rules and axes, error-bar caps, small units/legends, caveats, citations, provenance, and small qualifiers soften first.
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

The inherited fixed gate crop, nearest-neighbour enlargement, four-PSM Tesseract aid passed the unchanged 0.80 heuristic for 4/7 color, 4/7 grayscale, 4/7 protanopia, 3/7 deuteranopia, and 4/7 tritanopia gates. Mean similarities were 0.797493, 0.765234, 0.806685, 0.779427, and 0.772629 respectively; the minimum individual score was 0.516129.

Direct review of the encoded contact sheets confirms all 7/7 top lines in every variant. The OCR undercount is retained transparently rather than reclassified as a semantic defect or used to alter the inherited threshold.

## Evidence-backed action

Adopt `COLOR_MINIMUM_SCALE_REPRESENTED_VERTICAL_SMEAR_GUARD_PASS29.json`; do not make a pixel or copy correction.

The pass-7/pass-12 correction remains sufficient. A later separately authored iteration must keep status and required meaning in direct text plus complete non-color geometry and may not place sole meaning in hue or vertical-smear-fragile horizontal detail.

## Blockers

`BLOCKER_PACKET_PASS29.json` preserves the exact blockers:

1. no valid independent post-run A3.8 verdict record bound to the exact frozen all-209-file T4 artifact;
2. `KUN_FRAME_REVIEW.md` remains `FRAME REVIEW: AGREES FRAME_UNSTATED`;
3. `video_reportable_now` remains false.

No blocker was repaired, weakened, or invented. Hwao remains sole integrator.
