# Spin worker-Yui — isolated deepening pass 8 monochrome/color-vision audit

Extraction completed: 2026-08-08T06:02:28.375412+09:00
Audit completed: 2026-08-08T06:12:59+09:00
Status: QA static PNG derivatives and proposal-only integration guard; not a candidate or science verdict

## Custody

- Candidate: `/Users/duhokim/HermesOps/cockpit/videos/spin-parity-census-narrated-20260808T0149.mp4`
- Candidate SHA-256: `02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431`
- Candidate bytes were read only and remain equal to the official worker freeze.
- Sealed-v8 storyboard, renderer, seven frames, contact sheet, and receipt were not changed.
- The pass-7 caption-safe proof was read and transformed into QA derivatives only; its source bytes were not changed.
- No MP4, audio, TTS, shared/public asset, runtime, publication, or Git operation occurred.

## Fresh encoded-frame method

Pass 8 independently reran the deterministic 30-fps 160×90 grayscale frame-difference detector. It reproduced all 15 pass-7 cut timestamps exactly. Sixteen fresh 1920×1080 RGB midpoint frames were decoded; all 16 hashes reproduce pass-7 clean midpoints byte-for-byte.

Four presentation stress transforms were generated from each color midpoint:

1. linear-light BT.709 grayscale;
2. Machado severity-100 protanopia simulation;
3. Machado severity-100 deuteranopia simulation;
4. Machado severity-100 tritanopia simulation.

Together with color, the fresh candidate census is 80 QA PNGs and five contact sheets. These transforms are deterministic presentation stress tests, not clinical diagnostics.

## Encoded candidate finding

Human full-sheet review and deterministic OCR/edge metrics agree: removing or changing hue does not demote the candidate's dominant assertion layer. Large headlines, result numbers, bars, point/error-bar plots, matrix cells, and plot silhouettes persist. Color distinctions weaken in plot legends and series, especially in grayscale, but text labels, axis position, and geometry still carry enough structure to preserve the result presentation.

Across all 16 scenes:

| Variant | Headline OCR retention | Full OCR retention | Lower-support retention | Numeric retention | Edge recall |
|---|---:|---:|---:|---:|---:|
| grayscale | 1.000000 | 0.933301 | 0.877063 | 0.910233 | 0.999942 |
| protanopia | 1.000000 | 0.979962 | 0.979505 | 0.959358 | 0.999953 |
| deuteranopia | 1.000000 | 0.939980 | 0.926533 | 0.962081 | 0.999950 |
| tritanopia | 1.000000 | 0.982433 | 0.978786 | 0.952005 | 0.999839 |

For chart/matrix scenes 5, 7, 9, 10, and 11 in grayscale:

- headline OCR retention: `1.000000`;
- full OCR retention: `0.808086`;
- lower-support retention: `0.739935`;
- numeric retention: `0.779412`;
- edge recall: `0.999998`;
- chroma retention: `0.000000`.

Critical held scenes 7, 9, 10, 11, and 16 contain zero structural `RESULT HELD`, `FRAME UNSTATED`, `OUTCOMES WITHHELD`, `NO OUTCOME SHOWN`, or `RESULT LOCKED` gates in all five variants. Monochrome and color-vision transforms therefore do not repair the scientific-presentation failure.

## Sealed-v8 finding

Thirty-five QA derivatives tested seven sealed-v8 scenes in the same five variants. Full-sheet review found:

- `RESULT HELD` readable on 7/7 scenes in all five variants;
- zero semantic distinctions carried by hue alone;
- all seven scenes preserve meaning through direct labels, distinct boxes/glyphs/connectors, line treatment, and stable position;
- grayscale full-text OCR retention: `0.962894`;
- grayscale edge recall: `1.000000`.

Specific redundancy remains visible without hue:

- S1: numbered nodes, arrows, and locked-result words;
- S2: three labelled readout boxes, equal branch arrows, and containment words;
- S3: labelled CW/ACW/tie bins, equation, and separate tie tray;
- S4: mirrored glyph geometry, two direct branch labels, and `FRAME UNSTATED`;
- S5: direct column labels, connector geometry, numerical cards, and named zero states;
- S6: condition names, separate cards, solid available rails, dashed blocked rail, and `OUTCOMES WITHHELD`;
- S7: titled columns, bullet position, and full-text authorization boundary.

No new sealed-v8 pixel correction is justified.

## Pass-7 correction compatibility

Thirty-five further QA derivatives stress-tested the pass-7 caption-safe proof. Human review and auxiliary OCR found, in every color/monochrome/CVD variant:

- 7/7 scene-specific top gate lines readable;
- 7/7 `RESULT HELD` badges readable;
- 7/7 scene-specific gate phrases detected by OCR;
- 7/7 badges detected by OCR;
- mean top-gate-line token retention versus color: `1.000000`;
- zero hue-only meaning, overlap, or ambiguity;
- grayscale full-text retention: `0.952297`;
- grayscale edge recall: `1.000000`.

The amber styling is emphasis only; words and the bordered capsule carry the gate. Pass 8 therefore keeps the pass-7 correction intact rather than creating another mockup.

## Evidence-backed correction

`REDUNDANT_ENCODING_GUARD_PASS8.json` adds a bounded acceptance contract for any future Hwao-authored proposal iteration:

1. no method, scope, status, availability, unresolved state, or authorization distinction by hue alone;
2. direct labels plus distinct shape, line style, marker, or stable position for every branch/condition/column/rail;
3. text and border—not amber hue—must carry `RESULT HELD` and scene-specific caption-safe gates;
4. unavailable rails require both explicit copy and non-solid/blocked treatment;
5. any separately authorized future result figure requires direct labels and distinct marker/line patterns, not a color legend alone;
6. human contact-sheet review in color, grayscale, protanopia, deuteranopia, and tritanopia simulations;
7. retain pass-7 bottom-quarter obstruction and pass-6 360p tests.

This is a non-pixel storyboard/integration correction. Sealed v8 and the pass-7 proof already satisfy it, so a cosmetic v9 would add custody risk without repairing an observed defect.

## Science blockers

Unchanged and binding:

1. no valid post-run independent A3.8 review for the frozen T4 artifact across the pass-5 all-209-file content proof;
2. `KUN_FRAME_REVIEW.md` remains `FRAME REVIEW: AGREES FRAME_UNSTATED`.

Therefore `video_reportable_now` remains `false`. Pass 8 performs no scientific adjudication and carries no T4 measured values.
