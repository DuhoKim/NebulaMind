# Spin worker-Yui — isolated deepening pass 7 caption/UI-obstruction audit

Extraction completed: 2026-08-07T20:39:18.002837+00:00 (2026-08-08T05:39:18.002837+09:00)
Audit completed: 2026-08-08T05:45:48+09:00
Status: QA static PNGs and proposal-only correction; not a candidate or science verdict

## Custody

- Candidate: `/Users/duhokim/HermesOps/cockpit/videos/spin-parity-census-narrated-20260808T0149.mp4`
- Candidate SHA-256: `02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431`
- Candidate bytes were read only and remain equal to the official worker freeze.
- Sealed v8 storyboard, renderer, seven frames, contact sheet, and receipt were not changed.
- No MP4, audio, TTS, shared/public asset, runtime, publication, or Git operation occurred.

## Fresh encoded-frame method

The current FFmpeg scene-expression filter returned no selected frames despite the hash-stable candidate. Pass 7 therefore used a deterministic independent detector: 30-fps 160×90 grayscale decode, frame-to-frame mean absolute difference, top 15 peaks with one-second non-maximum separation. This reproduced all 15 pass-6 cut timestamps exactly.

Sixteen clean 1920×1080 RGB midpoint frames were decoded freshly. Their hashes reproduce pass 6 16/16. Two deterministic obstruction variants were then made from each clean frame:

1. caption obstruction: opaque bottom 15%;
2. player-UI obstruction: opaque bottom 25%.

Total: 48 QA PNGs and three contact sheets. The area above each mask remains pixel-identical to the clean frame in 16/16 scenes.

## Encoded candidate finding

Clean frames reproduce the already-held hierarchy: dominant assertion headlines, large numerical cards, matrix cells, and plot silhouettes; caveats, citations, provenance, axes, and explanatory boundaries are subordinate and often bottom-aligned. No clean critical scene contains a structural `RESULT HELD`, `FRAME UNSTATED`, `OUTCOMES WITHHELD`, or `NO OUTCOME SHOWN` phrase.

### Caption obstruction — bottom 15%

- mean full-text retention: `0.866911`
- mean headline retention: `0.966250`
- mean middle retention: `0.928813`
- mean lower-support retention: `0.295149`
- 14/16 clean scenes contain OCR-visible copy in the masked zone;
- all 161 tokens in those occupied zones are removed;
- structural-gate scenes: `0/16`.

### Player-UI obstruction — bottom 25%

- mean full-text retention: `0.756673`
- mean headline retention: `0.946477`
- mean middle retention: `0.820017`
- mean lower-support retention: `0.164207`
- 14/16 clean scenes contain OCR-visible copy in the masked zone;
- all 335 tokens in those occupied zones are removed;
- structural-gate scenes: `0/16`.

For critical held scenes 7, 9, 10, 11, and 16 under the 25% obstruction:

- mean full-text retention: `0.454035`
- mean headline retention: `0.856000`
- mean lower-support retention: `0.325462`
- mean bottom-quarter retention: `0.200000` because one critical scene has no clean bottom-quarter OCR copy; every occupied masked zone itself retains zero tokens;
- structural-gate scenes: `0/5`.

Fresh visual review agrees with the deterministic metric: the dominant scientific assertion layer remains visible while lower caveats, provenance, citations, axes, and conclusion copy are removed. Caption/player overlays therefore worsen the candidate's representation failure; they cannot repair it.

## Sealed-v8 obstruction finding

Twenty-one QA derivatives tested the seven sealed-v8 frames as clean, bottom-15%-masked, and bottom-25%-masked. Human full-sheet review found the high-contrast top-right `RESULT HELD` capsule visibly readable on 7/7 frames in all three variants. Auxiliary badge OCR is scale-invariant at 4/7 and is not treated as the visual gate.

The generic hold survives, but exact scene-specific boundaries do not all survive the bottom quarter:

- S2: the bottom `DO NOT SUM` scope note is obscured;
- S3: the label-frame physical-interpretation boundary is obscured;
- S4: the large `FRAME UNSTATED` explanation is partially obscured;
- S5: the column-check-only / storage-frame-unresolved boundary is obscured;
- S6: the paired-comparison / outcomes-withheld strip is obscured;
- S7: the separate-authorization next gate is obscured.

A generic `RESULT HELD` capsule is necessary but not an exact substitute for those scene-specific semantic boundaries.

## Evidence-backed correction

Pass 7 therefore proposes one bounded storyboard correction in `CAPTION_SAFE_STORYBOARD_CORRECTION_PASS7.json`: retain the persistent top-right `RESULT HELD` capsule and add one scene-specific gate line under the header, with its bottom at y=129/1080 (`0.119444`), fully above the bottom-quarter obstruction zone.

A QA-only proof under `qa/pass7_caption_safe_mockup/` applies the exact seven proposed lines without modifying v8. Clean and bottom-25%-masked contact sheets pass human review:

- 7/7 scene-specific gate lines remain readable;
- 7/7 `RESULT HELD` badges remain readable;
- 7/7 clean-to-masked top-75% regions are pixel-identical;
- the new line does not overlap the headline, subhead, badge, or dominant diagram;
- no result value, result plot, or scientific adjudication is added.

This proof is explicitly `NOT_V9_NOT_A_CANDIDATE`. Hwao/Fable may adopt, revise, or reject it from the sole integrator/writer seat; any adoption requires a new separately reviewed proposal iteration.

## Science blockers

Unchanged and binding:

1. no valid post-run independent A3.8 review for the frozen T4 artifact across the pass-5 all-209-file content proof;
2. `KUN_FRAME_REVIEW.md` remains `FRAME REVIEW: AGREES FRAME_UNSTATED`.

Therefore `video_reportable_now` remains `false`. Pass 7 performs no scientific adjudication and carries no T4 measured values.
