# Spin worker-Yui — isolated deepening pass 11 recompression audit

Extraction completed: 2026-08-08T07:27:26.851432+09:00
Audit completed: 2026-08-08T07:34:28+09:00
Status: QA static PNG derivatives and proposal-only integration guard; not a candidate or science verdict

## Custody

- Candidate: `/Users/duhokim/HermesOps/cockpit/videos/spin-parity-census-narrated-20260808T0149.mp4`
- Candidate SHA-256: `02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431`
- Candidate bytes were read only and remain equal to the official worker freeze.
- Sealed-v8 storyboard, renderer, seven frames, contact sheet, and receipt were not changed.
- The pass-7 caption-safe proof was used only as the clean source of QA derivatives; its bytes were not changed.
- No MP4, audio, TTS, shared/public asset, runtime, publication, browser, or Git operation occurred.

## Fresh encoded-frame method

Pass 11 independently reran the 30-fps, 160×90 grayscale frame-difference detector with a fixed 30-frame nonmaximum separation. It reproduced all 15 pass-10 cuts exactly. Sixteen fresh 1920×1080 RGB midpoints were decoded; all 16 are byte-identical to the pass-10 clean midpoints.

Each clean midpoint was deterministically encoded and decoded through Pillow JPEG with RGB input, 4:2:0 chroma subsampling (`subsampling=2`), `optimize=False`, and `progressive=False`. Four library quality values were tested:

1. quality 85;
2. quality 60;
3. quality 35;
4. quality 20.

The decoded RGB pixels were stored as non-optimized PNGs for static QA. The receipt pins each transient JPEG byte-stream hash and size as well as every decoded PNG hash. Together with clean, the candidate census is 80 QA frames and five contact sheets.

These are deterministic representation stress tests. Pillow quality values are library parameters, not claims about a named platform, codec ladder, upload path, or delivery system. Quality 60 is the operational floor in this packet; quality 35 and 20 are characterization only.

## Encoded candidate finding

Human contact-sheet review and deterministic metrics agree that recompression does not demote the held candidate's substantive result hierarchy. Major headlines, result numbers, plots, matrices, and conclusion prose remain dominant. Fine axes, legends, citations, provenance, and small qualifiers soften first. No structural `RESULT HELD`, `FRAME UNSTATED`, `OUTCOMES WITHHELD`, `NO OUTCOME SHOWN`, or `RESULT LOCKED` gate appears in any variant.

Across all 16 scenes:

| Variant | Headline OCR recall | Full OCR recall | Lower-support recall | Numeric recall | RGB PSNR dB | Tolerant luma-edge recall | Structural gate scenes |
|---|---:|---:|---:|---:|---:|---:|---:|
| JPEG q85 4:2:0 | 0.997845 | 0.986743 | 0.994005 | 0.980930 | 42.968679 | 0.998170 | 0 |
| JPEG q60 4:2:0 | 0.995690 | 0.970333 | 0.976472 | 0.958996 | 38.545696 | 0.993255 | 0 |
| JPEG q35 4:2:0 | 0.995690 | 0.961609 | 0.935222 | 0.938275 | 36.255712 | 0.994454 | 0 |
| JPEG q20 4:2:0 | 0.995690 | 0.954311 | 0.954819 | 0.951323 | 33.716193 | 0.989097 | 0 |

OCR response is not monotonic across all quality values, as expected for segmentation and recognition after block/ringing changes. Full-sheet and full-resolution human review therefore remains decisive.

For held-critical scenes 7, 9, 10, 11, and 16 at operational q60:

- headline recall: `1.000000`;
- full-text recall: `0.942037`;
- lower-support recall: `0.946331`;
- numeric recall: `0.882119`;
- structural held gates: `0/5`.

At severe q20, the same critical scenes retain `1.000000` headline recall while full-text recall falls to `0.892398`; structural gates remain `0/5`. Recompression therefore neither hides the dominant result presentation nor repairs its missing scientific boundary.

## Sealed-v8 recompression finding

Thirty-five QA derivatives tested seven sealed-v8 scenes in clean and four recompression variants.

At operational q60 4:2:0:

- `RESULT HELD` remains visually readable on 7/7 scenes;
- large method/status boundaries remain readable on 7/7 scenes;
- no required meaning becomes ambiguous;
- full-text OCR recall is `0.973906`;
- headline OCR recall is `0.979692`;
- lower-support OCR recall is `1.000000`;
- numeric OCR recall is `1.000000`;
- mean RGB PSNR is `33.368965` dB;
- tolerant luma-edge recall is `1.000000`.

At severe q20 characterization:

- `RESULT HELD` remains visually readable on 7/7 scenes;
- `RESULT LOCKED`, `FRAME UNSTATED`, `OUTCOMES WITHHELD`, and `RESULT STATUS · HELD` remain primary;
- direct diagram labels and status columns remain recoverable;
- full-text OCR recall is `0.963908`;
- headline OCR recall is `0.979692`;
- numeric OCR recall is `1.000000`.

Small footer and citation copy softens under severe recompression, but no required method or status meaning becomes ambiguous. No sealed pixel correction is supported.

## Pass-7 caption-safe proof compatibility

Thirty-five additional derivatives tested the pass-7 QA-only proof.

At operational q60 4:2:0:

- all seven scene-specific top gate lines remain visually readable and OCR-detectable;
- all seven `RESULT HELD` badges remain visually readable;
- full-text OCR recall is `0.964362`;
- headline OCR recall is `0.982814`;
- lower-support OCR recall is `0.954545`;
- numeric OCR recall is `1.000000`;
- tolerant luma-edge recall is `1.000000`.

At severe q20 characterization:

- all seven scene-specific gate lines remain visually readable and OCR-detectable;
- all seven badges remain visually readable;
- full-text OCR recall is `0.955538`;
- headline OCR recall is `0.982814`;
- numeric OCR recall is `1.000000`.

The pass-7 proof remains the correct scene-specific status correction under recompression stress.

## Evidence-backed action

`RECOMPRESSION_RESILIENCE_GUARD_PASS11.json` adds one cumulative non-pixel integration contract:

1. operational review uses the exact Pillow JPEG q60 4:2:0 transform recorded above;
2. 7/7 complete `RESULT HELD` capsules and 7/7 scene-specific gate lines remain readable;
3. large unresolved/status boundaries remain primary or are paired with the scene-specific top gate;
4. no scientific qualifier, unresolved boundary, unavailable rung, or interpretation limit may live only in fine chroma detail, a one-pixel line, a tiny axis label, a citation, or a footer;
5. direct labels, borders, arrows, line styles, markers, and status columns remain distinguishable;
6. q35 and q20 remain characterization, not universal delivery requirements;
7. recompression review remains cumulative with 360p, obstruction, color/monochrome, title-safe, and ambient-contrast tests.

No new pixel correction is evidenced because sealed v8 and the pass-7 proof pass the operational stress. Worker Yui created no v9 and changed no sealed pixel because Hwao/Fable remains the sole integrator and proposal writer.

## Science blockers

Unchanged and binding:

1. no valid post-run independent A3.8 review for the frozen T4 artifact across the all-209-file content proof;
2. `KUN_FRAME_REVIEW.md` remains `FRAME REVIEW: AGREES FRAME_UNSTATED`.

Therefore `video_reportable_now` remains `false`. Pass 11 performs no scientific adjudication and carries no T4 measured values.
