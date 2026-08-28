# Spin worker-Yui — isolated deepening pass 9 title-safe crop audit

Extraction completed: 2026-08-08T06:31:55.558928+09:00
Audit completed: 2026-08-08T06:40:17+09:00
Status: QA static PNG derivatives and proposal-only layout correction; not a candidate or science verdict

## Custody

- Candidate: `/Users/duhokim/HermesOps/cockpit/videos/spin-parity-census-narrated-20260808T0149.mp4`
- Candidate SHA-256: `02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431`
- Candidate bytes were read only and remain equal to the official worker freeze.
- Sealed-v8 storyboard, renderer, seven frames, contact sheet, and receipt were not changed.
- The pass-7 caption-safe proof was read and transformed into QA derivatives only; its source bytes were not changed.
- No MP4, audio, TTS, shared/public asset, runtime, publication, or Git operation occurred.

## Fresh encoded-frame method

Pass 9 independently reran the deterministic 30-fps 160×90 grayscale frame-difference detector. It reproduced all 15 pass-8 cut timestamps exactly. Sixteen fresh 1920×1080 RGB midpoint frames were decoded; all 16 hashes reproduce pass-8 color midpoints byte-for-byte.

Four crop-and-rescale presentation stress variants were generated from each clean midpoint:

1. symmetric 3%: remove 58 px left/right and 32 px top/bottom;
2. symmetric 5%: remove 96 px left/right and 54 px top/bottom;
3. horizontal 5%: remove 96 px left/right only;
4. vertical 5%: remove 54 px top/bottom only.

Every crop was resized back to 1920×1080 with deterministic Lanczos resampling. Together with clean, the fresh candidate census is 80 QA PNGs and five contact sheets. These are representation stress tests, not a claim that a named player, display, or projector applies such a crop.

## Encoded candidate finding

Human contact-sheet review and deterministic OCR agree that crop does not demote the held candidate's dominant result hierarchy. Large headlines, result numbers, bar plots, point/error-bar plots, matrices, and conclusion prose remain visibly dominant at both 3% and 5%. No structural `RESULT HELD`, `FRAME UNSTATED`, `OUTCOMES WITHHELD`, `NO OUTCOME SHOWN`, or `RESULT LOCKED` gate appears.

Across all 16 scenes:

| Variant | Headline OCR recall | Full OCR recall | Lower-support recall | Numeric recall | Structural gate scenes |
|---|---:|---:|---:|---:|---:|
| symmetric 3% | 1.000000 | 0.980399 | 0.987756 | 0.972159 | 0 |
| symmetric 5% | 0.995690 | 0.981884 | 0.994975 | 0.973861 | 0 |
| horizontal 5% | 0.993606 | 0.981868 | 0.994174 | 0.980586 | 0 |
| vertical 5% | 1.000000 | 0.985634 | 0.993373 | 0.977452 | 0 |

For held critical scenes 7, 9, 10, 11, and 16 under symmetric 5% crop:

- headline recall: `1.000000`;
- full-text recall: `0.965485`;
- numeric recall: `0.916356`;
- structural held gates: `0/5`.

Crop therefore neither hides the result presentation nor repairs the scientific-presentation failure.

## Sealed-v8 title-safe finding

Thirty-five QA derivatives tested seven sealed-v8 scenes in clean and four crop variants.

At symmetric 3% crop:

- no semantic loss was found on 7/7 scenes;
- `RESULT HELD` text remains visible on 7/7 scenes;
- full-text OCR recall is `0.939553`;
- headline OCR recall is `0.979692`.

At symmetric 5% crop:

- `RESULT HELD` words remain readable on 7/7 scenes, but every badge capsule is clipped at the frame edge;
- every left `GALAXY SPIN · METHOD-ONLY VISUAL PROPOSAL` header is clipped;
- edge content is visibly clipped in S1, S5, and S7: the first pipeline node/border, left source-column card/border, and left status-card/headline edge;
- 44 OCR-visible clean-frame tokens lie partly outside the inner-five-percent rectangle;
- full-text OCR recall falls to `0.899783`;
- headline recall is `0.946693`;
- numeric recall is `0.705597`.

The centered dominant method diagrams and gate words remain understandable, but complete semantic containers and audience headers do not. Sealed v8 therefore passes the tested 3% crop but does not satisfy a strict inner-5% title-safe contract.

## Pass-7 caption-safe proof compatibility

Thirty-five additional derivatives tested the pass-7 QA-only proof.

At symmetric 3% crop:

- 7/7 scene-specific top gate lines remain visible;
- 7/7 `RESULT HELD` words remain visible;
- full-text OCR recall is `0.932761`.

At symmetric 5% crop:

- all seven centered scene-specific gate lines remain visually and OCR-readable;
- all seven `RESULT HELD` words remain visually readable;
- all seven badge capsules and left headers are clipped;
- S1, S5, and S7 retain the same edge-content clipping as sealed v8;
- 44 clean-frame OCR tokens lie partly outside the inner-five-percent rectangle;
- full-text OCR recall is `0.896020`;
- headline recall is `0.957313`;
- numeric recall is `0.705597`.

This is a cumulative boundary finding: the pass-7 gate line survives bottom-quarter obstruction and remains centered under crop, but its surrounding frame still needs title-safe edge custody.

## Evidence-backed correction

`TITLE_SAFE_STORYBOARD_CORRECTION_PASS9.json` proposes one exact layout contract for any future Hwao-authored proposal iteration:

1. inner-5% safe rectangle at 1920×1080: `x=96..1824`, `y=54..1026`;
2. every semantic/audience-readable element and its complete border or marker must fit inside that rectangle;
3. outer 5% is decorative-only;
4. move the full header and complete `RESULT HELD` capsule inward;
5. retain the centered pass-7 scene-specific gate line above the pass-7 bottom-quarter obstruction zone;
6. specifically protect S1's first pipeline node, S5's left source-column card, and S7's first status card plus result-status headline;
7. keep audience-readable citations inside the safe rectangle; verification paths remain receipt-only;
8. rerun clean, 3%, symmetric/horizontal/vertical 5%, pass-8 color/monochrome, pass-7 obstruction, and pass-6 360p tests after any layout change.

This correction requests a future bounded pixel-layout change, but worker Yui did not create v9 or change sealed v8 because Hwao/Fable remains the sole integrator and proposal writer.

## Science blockers

Unchanged and binding:

1. no valid post-run independent A3.8 review for the frozen T4 artifact across the pass-5 all-209-file content proof;
2. `KUN_FRAME_REVIEW.md` remains `FRAME REVIEW: AGREES FRAME_UNSTATED`.

Therefore `video_reportable_now` remains `false`. Pass 9 performs no scientific adjudication and carries no T4 measured values.
