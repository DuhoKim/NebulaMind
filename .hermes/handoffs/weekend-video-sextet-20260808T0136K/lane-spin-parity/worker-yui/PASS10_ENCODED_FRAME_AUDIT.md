# Spin worker-Yui — isolated deepening pass 10 ambient-contrast audit

Extraction completed: 2026-08-08T06:57:44.449200+09:00
Audit completed: 2026-08-08T07:05:07+09:00
Status: QA static PNG derivatives and proposal-only integration guard; not a candidate or science verdict

## Custody

- Candidate: `/Users/duhokim/HermesOps/cockpit/videos/spin-parity-census-narrated-20260808T0149.mp4`
- Candidate SHA-256: `02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431`
- Candidate bytes were read only and remain equal to the official worker freeze.
- Sealed-v8 storyboard, renderer, seven frames, contact sheet, and receipt were not changed.
- The pass-7 caption-safe proof was transformed into QA derivatives only; its source bytes were not changed.
- No MP4, audio, TTS, shared/public asset, runtime, publication, or Git operation occurred.

## Fresh encoded-frame method

Pass 10 independently reran the deterministic 30-fps 160×90 grayscale frame-difference detector. It reproduced all 15 pass-9 cut timestamps exactly. Sixteen fresh 1920×1080 RGB midpoint frames were decoded; all 16 hashes reproduce pass-9 clean midpoints byte-for-byte.

Four deterministic uniform black-lift variants were generated from each clean midpoint. The transform decodes sRGB to linear light, applies `output = lift + (1 − lift) × input`, then re-encodes sRGB with float64 arithmetic and nearest-integer uint8 output:

1. 10% black lift, ideal white-to-black ratio capped at 7.0:1;
2. 20% black lift, ratio capped at 4.2:1;
3. 30% black lift, ratio capped at 3.0:1;
4. 40% black lift, ratio capped at 2.333333:1.

Together with clean, the fresh candidate census is 80 QA PNGs and five contact sheets. These are presentation stress tests, not a claim about a named projector, room, display, or viewer. The 20% variant is the operational integration floor in this packet; 30% and 40% are characterization only.

## Encoded candidate finding

Human contact-sheet review and deterministic OCR agree that uniform black lift does not demote the held candidate's dominant result hierarchy. Large headlines, result numbers, bar plots, point/error-bar plots, matrices, and conclusion prose survive while small caveats, axes, legends, citations, and provenance weaken first. No structural `RESULT HELD`, `FRAME UNSTATED`, `OUTCOMES WITHHELD`, `NO OUTCOME SHOWN`, or `RESULT LOCKED` gate appears.

Across all 16 scenes:

| Variant | Headline OCR recall | Full OCR recall | Lower-support recall | Numeric recall | Structural gate scenes |
|---|---:|---:|---:|---:|---:|
| 10% black lift | 0.995690 | 0.888670 | 0.480083 | 0.660251 | 0 |
| 20% black lift | 0.997845 | 0.875962 | 0.467116 | 0.648508 | 0 |
| 30% black lift | 0.997845 | 0.877310 | 0.467199 | 0.652584 | 0 |
| 40% black lift | 0.995761 | 0.849285 | 0.438828 | 0.647242 | 0 |

For held critical scenes 7, 9, 10, 11, and 16 under the operational 20% stress:

- headline recall: `1.000000`;
- full-text recall: `0.810953`;
- lower-support recall: `0.786754`;
- numeric recall: `0.768558`;
- structural held gates: `0/5`.

At severe 40% stress, the same critical scenes retain `0.993333` headline recall but only `0.725587` full-text recall and `0.696233` lower-support recall, with zero structural gates. Ambient wash therefore neither hides the result presentation nor repairs the scientific-presentation failure; it preferentially strips context and increases the imbalance.

## Sealed-v8 contrast finding

Thirty-five QA derivatives tested seven sealed-v8 scenes in clean and four black-lift variants.

At the operational 20% stress:

- `RESULT HELD` words remain visually readable on 7/7 scenes;
- large method/status boundaries remain readable on 7/7 scenes;
- full-text OCR recall is `0.961405`;
- headline OCR recall is `1.000000`;
- lower-support OCR recall is `0.980952`;
- numeric OCR recall is `1.000000`;
- mean robust p99/p01 luminance ratio is `3.726047`.

At the severe 40% characterization:

- `RESULT HELD` words remain visually readable on 7/7 scenes;
- large status boundaries remain readable on 7/7 scenes;
- full-text OCR recall is `0.959852`;
- headline OCR recall is `0.983894`;
- lower-support OCR recall is `0.980952`;
- numeric OCR recall is `1.000000`.

Small qualifiers and citations become visually faint under heavy lift, but deterministic OCR does not show a method-level collapse. The large `RESULT LOCKED`, `FRAME UNSTATED`, `OUTCOMES WITHHELD`, and `RESULT STATUS · HELD` structures remain primary. Sealed v8 therefore supports a non-pixel contrast-floor guard rather than a new cosmetic iteration.

## Pass-7 caption-safe proof compatibility

Thirty-five additional derivatives tested the pass-7 QA-only proof.

At the operational 20% stress:

- all seven scene-specific top gate lines remain visually readable and OCR-detectable;
- all seven `RESULT HELD` words remain visually readable;
- full-text OCR recall is `0.952633`;
- headline OCR recall is `1.000000`;
- lower-support OCR recall is `0.945022`;
- numeric OCR recall is `1.000000`.

At severe 40% characterization:

- all seven scene-specific gate lines remain visually readable and OCR-detectable;
- all seven `RESULT HELD` words remain visually readable;
- full-text OCR recall is `0.951405`;
- headline OCR recall is `0.986385`;
- lower-support OCR recall is `0.945022`;
- numeric OCR recall is `1.000000`.

The pass-7 proof therefore remains the correct scene-specific status correction under ambient-contrast stress.

## Evidence-backed action

`AMBIENT_CONTRAST_GUARD_PASS10.json` adds one cumulative non-pixel integration contract:

1. the operational acceptance transform is 20% uniform linear-light black lift;
2. 7/7 complete `RESULT HELD` capsules and 7/7 pass-7 scene-specific gate lines must remain readable;
3. large unresolved/status boundaries must remain primary or be paired with the scene-specific top gate;
4. no scientific qualifier, unresolved boundary, unavailable rung, or interpretation limit may live only in low-contrast footer, citation, axis, or tiny body copy;
5. direct labels, borders, line styles, markers, and status columns must remain distinguishable;
6. 30% and 40% remain characterization, not assumed viewing environments or mandatory thresholds;
7. the guard is cumulative with pass-6 360p, pass-7 obstruction, pass-8 color/monochrome, and pass-9 title-safe tests.

No new pixel correction is evidenced because sealed v8 and the pass-7 proof pass the operational stress. Worker Yui created no v9 and changed no sealed pixel because Hwao/Fable remains the sole integrator and proposal writer.

## Science blockers

Unchanged and binding:

1. no valid post-run independent A3.8 review for the frozen T4 artifact across the pass-5 all-209-file content proof;
2. `KUN_FRAME_REVIEW.md` remains `FRAME REVIEW: AGREES FRAME_UNSTATED`.

Therefore `video_reportable_now` remains `false`. Pass 10 performs no scientific adjudication and carries no T4 measured values.
