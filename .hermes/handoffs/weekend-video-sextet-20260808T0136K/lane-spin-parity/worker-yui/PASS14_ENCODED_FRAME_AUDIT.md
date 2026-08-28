# Spin worker-Yui — isolated deepening pass 14 dark-tone-floor audit

Extraction completed: 2026-08-08T09:25:29.355659+09:00
Audit completed: 2026-08-08T09:28:29+09:00
Status: QA static PNG derivatives and proposal-only integration guard; not a candidate or science verdict

## Custody

- Candidate: `/Users/duhokim/HermesOps/cockpit/videos/spin-parity-census-narrated-20260808T0149.mp4`
- Candidate SHA-256: `02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431`
- Candidate bytes were read only and remain equal to the official worker freeze.
- Sealed-v8 storyboard, renderer, seven frames, contact sheet, and receipt were not changed.
- Pass-7 and pass-12 proof bytes were not changed.
- No MP4, audio, TTS, shared/public asset, runtime, publication, browser, or Git operation occurred.

## Fresh encoded-frame method

Pass 14 independently reran the 30-fps, 160×90 grayscale frame-difference detector with fixed 30-frame nonmaximum separation. It reproduced all 15 pass-13 cuts exactly. Sixteen fresh 1920×1080 RGB midpoints were decoded; all 16 are byte-identical to the pass-13 clean midpoints.

Each frame was transformed with a deterministic integer-luma-preserving dark-tone floor and full-range remap. Integer luma uses weights 54/256, 183/256, and 19/256 for R, G, and B. For floor `f`, luma is mapped as `Y2 = max(Y − f, 0) × 255 / (255 − f)` with integer round-half-up, then each RGB channel is scaled by `Y2/Y` with integer round-half-up. Four code-value floors were tested:

1. 8/255;
2. 16/255;
3. 32/255;
4. 48/255.

Together with clean, the candidate census is 80 QA frames and five contact sheets. Canvas, RGB mode, frame timing, and frame boundaries do not change.

The floor values are packet parameters, not claims about a named display, transfer function, codec, player, platform, service, room, projector, viewer, camera, or perception standard. Floor 16 is the operational review floor in this packet. Floors 32 and 48 are characterization only.

## Encoded candidate finding

Human contact-sheet review and deterministic metrics show that dark background texture, gridlines, axes, error bars, legends, caveats, citations, provenance, and low-luminance context weaken or disappear before white result headlines, large blue numbers, bright bars, matrices, plot silhouettes, and the conclusion hierarchy. No structural `RESULT HELD`, `FRAME UNSTATED`, `OUTCOMES WITHHELD`, `NO OUTCOME SHOWN`, or `RESULT LOCKED` gate appears in any candidate variant.

Across all 16 scenes:

| Variant | Headline OCR recall | Full OCR recall | Lower-support recall | Numeric recall | RGB PSNR dB | Mean luma retention | Added black pixels | Dark-pixel survival below 64 | Low-tone edge recall | Structural gates |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| floor 8 | 0.993606 | 0.980337 | 0.978874 | 0.974653 | 29.105795 | 0.685204 | 0.001427 | 0.998402 | 0.999786 | 0 |
| floor 16 | 0.997845 | 0.978241 | 0.974119 | 0.967361 | 23.322732 | 0.393058 | 0.689215 | 0.267620 | 0.998334 | 0 |
| floor 32 | 0.993534 | 0.944125 | 0.934223 | 0.859776 | 22.458567 | 0.325960 | 0.928856 | 0.017867 | 0.967069 | 0 |
| floor 48 | 0.995690 | 0.900701 | 0.879442 | 0.644551 | 22.093857 | 0.303405 | 0.942483 | 0.003571 | 0.866807 | 0 |

At operational floor 16, 68.9% of pixels that were non-black in the clean frames become black, but headline recall is 0.997845 and no held/status gate appears. This high black-pixel fraction reflects the candidate's mostly near-black canvas; it is not a display prevalence claim.

For held-critical scenes 7, 9, 10, 11, and 16 at floor 16:

- headline recall: `1.000000`;
- full-text recall: `0.961609`;
- lower-support recall: `0.952503`;
- numeric recall: `0.895556`;
- mean luma retention: `0.441212`;
- additional black-pixel fraction: `0.796146`;
- nonzero dark-pixel survival below luma 64: `0.134594`;
- structural held gates: `0/5`.

At severe floor 48, 94.2% additional source-nonblack pixels become black and dark-pixel survival below luma 64 falls to 0.003571. Yet major result headlines, large numbers, bright bars, matrices, plot silhouettes, and conclusion hierarchy remain visually primary; headline recall remains 0.995690. Exact minor axes, grids, error bars, small labels, citations, provenance, and dark context are no longer reliable carriers. Structural gates remain `0/16`. Dark-tone loss therefore cannot authorize or repair the candidate.

## Sealed-v8 dark-tone finding

Thirty-five QA derivatives test the seven sealed-v8 scenes.

At operational floor 16:

- `RESULT HELD` remains visually readable on 7/7 scenes;
- large method/status boundaries remain readable on 7/7 scenes;
- direct labels, arrows, borders, connectors, rails, and status columns remain distinguishable;
- no required meaning becomes ambiguous;
- headline OCR recall is `1.000000`;
- full-text OCR recall is `0.980620`;
- lower-support OCR recall is `0.972143`;
- numeric OCR recall is `1.000000`.

At severe floor 48, the same seven badges, large status boundaries, labels, borders, arrows, connectors, rails, and status columns remain readable. Headline recall remains 1.000000 and full-text recall is 0.961706. Dark card fills and background texture collapse toward black, while tiny citations and provenance are reduced; none is the sole carrier of required method or status meaning.

## Pass-7 caption-safe proof compatibility

Thirty-five derivatives test the existing pass-7 proof.

At floor 16:

- all seven scene-specific top gate lines remain visually exact;
- all seven `RESULT HELD` badges remain visually readable;
- full-text OCR recall is `0.973567`;
- headline OCR recall is `1.000000`;
- lower-support OCR recall is `0.958450`;
- the single global regex OCR aid detects six of seven exact gate lines.

The global OCR miss does not overrule readable pixels. It is consistent with global OCR ordering limitations already recorded in pass 13.

## Pass-12 strengthened title-safe proof compatibility

Thirty-five derivatives test the pass-12 strengthened proof without changing it.

At operational floor 16:

- all seven exact scene-specific gate lines remain visually readable;
- all seven complete `RESULT HELD` badges remain visually readable;
- cropped multi-PSM character-similarity acceptance remains 7/7 at threshold `0.85`;
- mean best-of-PSM gate similarity is `1.000000`;
- full-text OCR recall is `0.973210`;
- headline OCR recall is `1.000000`;
- no overlap, clipping, or semantic ambiguity appears.

Even at characterization floor 48, visual exact-gate count remains 7/7, character-similarity acceptance remains 7/7 with mean 1.000000, and all seven badges and required status boundaries remain readable. Dark fill and texture loss does not erase a required label or geometry channel.

## Evidence-backed action

`DARK_TONE_RESILIENCE_GUARD_PASS14.json` adds a non-pixel future-integration guard:

1. use the exact floor-16 integer transform as a packet-specific operational review floor;
2. require 7/7 exact strengthened scene-gate lines visually and at the recorded `0.85` cropped character threshold;
3. require 7/7 complete `RESULT HELD` capsules and large scene-status boundaries;
4. preserve header/gate/badge/headline separation without clipping or semantic ambiguity;
5. retain direct labels plus arrows, borders, connectors, rails, and stable positions;
6. carry no required scientific qualifier, unresolved boundary, unavailable rung, interpretation limit, branch distinction, axis, error bar, or provenance fact only in pixels at or below source-luma code value 16;
7. use dark fill and background texture as decoration only, not as the sole boundary channel;
8. keep human full-sheet and full-resolution review decisive;
9. treat floors 32 and 48 as characterization only;
10. rerun the dark-tone test cumulatively with directional smear, spatial defocus, JPEG recompression, black lift, title-safe crop, color/monochrome, obstruction, and 360p review.

No further pixel or copy correction is justified. The pass-12 strengthened proof already passes the operational floor and preserves all required meaning at the severe characterization. Sealed v8 and both proofs remain unchanged; no v9 was created. Hwao/Fable remains the sole integrator and proposal writer.

## Science blockers

Unchanged and binding:

1. no valid post-run independent A3.8 review for the frozen T4 artifact across the all-209-file content proof;
2. `KUN_FRAME_REVIEW.md` remains `FRAME REVIEW: AGREES FRAME_UNSTATED`.

Therefore `video_reportable_now` remains `false`. Pass 14 performs no scientific adjudication and carries no T4 measured values.
