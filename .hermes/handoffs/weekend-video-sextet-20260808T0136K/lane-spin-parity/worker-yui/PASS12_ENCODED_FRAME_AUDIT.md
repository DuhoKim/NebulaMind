# Spin worker-Yui — isolated deepening pass 12 spatial-defocus audit

Extraction completed: 2026-08-08T07:52:04.626720+09:00
Audit completed: 2026-08-08T08:08:40+09:00
Status: QA static PNG derivatives and proposal-only storyboard correction; not a candidate or science verdict

## Custody

- Candidate: `/Users/duhokim/HermesOps/cockpit/videos/spin-parity-census-narrated-20260808T0149.mp4`
- Candidate SHA-256: `02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431`
- Candidate bytes were read only and remain equal to the official worker freeze.
- Sealed-v8 storyboard, renderer, seven frames, contact sheet, and receipt were not changed.
- The pass-7 caption-safe proof was read only; its bytes were not changed.
- No MP4, audio, TTS, shared/public asset, runtime, publication, browser, or Git operation occurred.

## Fresh encoded-frame method

Pass 12 independently reran the 30-fps, 160×90 grayscale frame-difference detector with a fixed 30-frame nonmaximum separation. It reproduced all 15 pass-11 cuts exactly. Sixteen fresh 1920×1080 RGB midpoints were decoded; all 16 are byte-identical to the pass-11 clean midpoints.

Each clean midpoint was deterministically filtered with Pillow `ImageFilter.GaussianBlur` at native 1920×1080. Four radii were tested:

1. 0.75 pixels;
2. 1.50 pixels;
3. 2.50 pixels;
4. 4.00 pixels.

Together with clean, the candidate census is 80 QA frames and five contact sheets. The canvas, mode, and frame boundaries do not change.

These are deterministic spatial-defocus presentation stresses. Radius values are packet parameters, not claims about a named lens, projector, display, viewer, platform, or service. Radius 1.50 is the operational floor in this packet; radius 2.50 and 4.00 are characterization only.

## Encoded candidate finding

Human contact-sheet review and deterministic metrics agree that spatial defocus does not demote the held candidate's dominant scientific-result hierarchy. Major headlines, large result numbers, plot and matrix silhouettes, and conclusion framing remain primary. Fine axes, legends, caveats, citations, provenance, and small qualifiers weaken first. No structural `RESULT HELD`, `FRAME UNSTATED`, `OUTCOMES WITHHELD`, `NO OUTCOME SHOWN`, or `RESULT LOCKED` gate appears in any variant.

Across all 16 scenes:

| Variant | Headline OCR recall | Full OCR recall | Lower-support recall | Numeric recall | RGB PSNR dB | Tolerant luma-edge recall | Gradient-energy ratio | Structural gate scenes |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| radius 0.75 | 1.000000 | 0.942890 | 0.768286 | 0.806990 | 34.445317 | 0.982094 | 0.444657 | 0 |
| radius 1.50 | 0.976652 | 0.790847 | 0.373819 | 0.572167 | 27.880050 | 0.786592 | 0.164739 | 0 |
| radius 2.50 | 0.943051 | 0.692690 | 0.275976 | 0.439394 | 24.854649 | 0.178779 | 0.063276 | 0 |
| radius 4.00 | 0.863677 | 0.343118 | 0.166687 | 0.411934 | 22.908392 | 0.000000 | 0.023008 | 0 |

For held-critical scenes 7, 9, 10, 11, and 16 at operational radius 1.50:

- headline recall: `0.966667`;
- full-text recall: `0.585729`;
- lower-support recall: `0.554870`;
- numeric recall: `0.590934`;
- structural held gates: `0/5`.

At severe radius 4.00, all-scene headline recall remains `0.863677` while lower-support recall falls to `0.166687`; structural gates remain `0/16`. Defocus therefore increases assertion-versus-support imbalance and cannot authorize or repair the candidate.

## Sealed-v8 defocus finding

Thirty-five QA derivatives tested seven sealed-v8 scenes in clean and four defocus variants.

At operational radius 1.50:

- `RESULT HELD` remains visually recognizable on 7/7 scenes;
- large method/status boundaries remain readable on 7/7 scenes;
- no required meaning becomes ambiguous;
- full-text OCR recall is `0.805395`;
- headline OCR recall is `0.979692`;
- lower-support OCR recall is `0.836566`;
- numeric OCR recall is `0.741868`;
- tolerant luma-edge recall is `0.831907`.

At severe radius 4.00, large `RESULT LOCKED`, `FRAME UNSTATED`, and `RESULT STATUS · HELD` hierarchy remains visually recognizable, but small qualifiers, citations, provenance, and exact minor labels are not acceptance-reliable. Severe radius 4.00 is therefore characterization only.

## Pass-7 caption-safe proof compatibility

Thirty-five additional derivatives tested the existing pass-7 proof.

At radius 1.50:

- all seven scene-specific top gate lines remain visually readable;
- all seven `RESULT HELD` badges remain visually recognizable;
- full-text OCR recall is `0.816863`;
- headline OCR recall is `0.919421`;
- lower-support OCR recall is `0.862973`;
- numeric OCR recall is `0.751392`;
- a single global PSM-11 exact-pattern aid detects five of seven specific lines.

The OCR miss does not overrule readable pixels, but it exposes a reproducibility weakness in the thin 25-pixel gate line. The pass-7 line box also extends outside the later pass-9 inner-five-percent title-safe rectangle. A bounded future-integration correction is therefore supported.

## QA-only strengthened-gate proof

`qa/pass12_sharpness_safe_mockup/` supplies a separate 35-frame proof, not v9 and not a candidate. It keeps all seven exact pass-7 scene lines unchanged and uses:

- box `x=102..1540`, `y=78..121`;
- 28-pixel bold type at 1080p;
- one-pixel same-color text stroke;
- three-pixel border;
- complete placement inside `x=96..1824`, `y=54..1026`;
- complete placement above the bottom-quarter obstruction zone;
- separation from header, generic badge, and headline.

At operational radius 1.50:

- scene-specific lines remain visually exact 7/7;
- cropped multi-PSM character-similarity acceptance is 7/7 at threshold `0.85`;
- mean best-of-PSM character similarity is `0.990148`;
- headline OCR recall is `0.976327`;
- full-text OCR recall is `0.837002`;
- no overlap, clipping, or semantic ambiguity is visible.

At radius 2.50, the same cropped character acceptance remains 7/7 with mean similarity `0.989418`. At severe radius 4.00, exact acceptance falls to 0/7 and mean similarity `0.253959`; gate containers and boundary hierarchy remain recognizable, but exact wording is not reliable. This confirms radius 4.00 as characterization only.

## Evidence-backed action

`SHARPNESS_RESILIENCE_STORYBOARD_CORRECTION_PASS12.json` proposes the narrow future-integration correction:

1. retain every exact pass-7 scene-gate sentence;
2. place the full gate container inside the inner-five-percent title-safe rectangle;
3. keep it above the bottom-quarter obstruction zone and separated from badge/headline;
4. use bold high-contrast type with enough stroke to pass the exact radius-1.50 transform;
5. retain a complete separate `RESULT HELD` capsule and large scene status boundary;
6. never carry a scientific qualifier, unresolved boundary, unavailable rung, or interpretation limit only in small body copy, footer, citation, fine line, or low-sharpness detail;
7. rerun defocus, JPEG recompression, black lift, crop, color/monochrome, obstruction, and 360p review after any Hwao-authored layout change.

The correction changes no science copy. Worker Yui created only a QA proof. Sealed v8 and the pass-7 proof remain unchanged; no v9 was created. Hwao/Fable remains the sole integrator and proposal writer.

## Science blockers

Unchanged and binding:

1. no valid post-run independent A3.8 review for the frozen T4 artifact across the all-209-file content proof;
2. `KUN_FRAME_REVIEW.md` remains `FRAME REVIEW: AGREES FRAME_UNSTATED`.

Therefore `video_reportable_now` remains `false`. Pass 12 performs no scientific adjudication and carries no T4 measured values.
