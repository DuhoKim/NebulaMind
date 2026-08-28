# Spin worker-Yui — isolated deepening pass 13 directional-smear audit

Extraction completed: 2026-08-08T08:28:29.947267+09:00
Audit completed: 2026-08-08T08:40:49+09:00
Status: QA static PNG derivatives and proposal-only integration guard; not a candidate or science verdict

## Custody

- Candidate: `/Users/duhokim/HermesOps/cockpit/videos/spin-parity-census-narrated-20260808T0149.mp4`
- Candidate SHA-256: `02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431`
- Candidate bytes were read only and remain equal to the official worker freeze.
- Sealed-v8 storyboard, renderer, seven frames, contact sheet, and receipt were not changed.
- Pass-7 and pass-12 proof bytes were not changed.
- No MP4, audio, TTS, shared/public asset, runtime, publication, browser, or Git operation occurred.

## Fresh encoded-frame method

Pass 13 independently reran the 30-fps, 160×90 grayscale frame-difference detector with fixed 30-frame nonmaximum separation. It reproduced all 15 pass-12 cuts exactly. Sixteen fresh 1920×1080 RGB midpoints were decoded; all 16 are byte-identical to the pass-12 clean midpoints.

Each clean midpoint was transformed by a centered horizontal box smear at native 1920×1080. The implementation edge-replicates the frame, uses unsigned 64-bit channel sums, and applies round-half-up integer division. Four odd kernel widths were tested:

1. 3 pixels;
2. 7 pixels;
3. 13 pixels;
4. 21 pixels.

Together with clean, the candidate census is 80 QA frames and five contact sheets. The canvas, RGB mode, vertical sampling, and frame boundaries do not change.

These are deterministic directional presentation stresses. Kernel widths are packet parameters, not claims about a named camera, lens, display, player, motion path, viewer, codec, platform, or service. Width 7 is the operational floor in this packet; widths 13 and 21 are characterization only.

## Encoded candidate finding

Human contact-sheet review and deterministic metrics show an anisotropic failure order. Horizontal smear suppresses x-gradient energy and thin vertical structure much more strongly than y-gradient energy. Fine axes, legends, caveats, citations, provenance, narrow labels, and vertical boundaries weaken before large headlines, numbers, cards, charts, matrices, and conclusion framing. No structural `RESULT HELD`, `FRAME UNSTATED`, `OUTCOMES WITHHELD`, `NO OUTCOME SHOWN`, or `RESULT LOCKED` gate appears in any candidate variant.

Across all 16 scenes:

| Variant | Headline OCR recall | Full OCR recall | Lower-support recall | Numeric recall | RGB PSNR dB | Tolerant edge recall | X-gradient ratio | Y-gradient ratio | Structural gates |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| width 3 | 0.991523 | 0.909783 | 0.890593 | 0.612607 | 33.961180 | 0.980659 | 0.877791 | 0.956255 | 0 |
| width 7 | 0.938201 | 0.669520 | 0.623122 | 0.467254 | 27.208633 | 0.914601 | 0.566164 | 0.878370 | 0 |
| width 13 | 0.639157 | 0.162190 | 0.080261 | 0.418403 | 23.925342 | 0.712934 | 0.339609 | 0.817141 | 0 |
| width 21 | 0.185270 | 0.046657 | 0.037348 | 0.370486 | 22.275823 | 0.622272 | 0.221454 | 0.778613 | 0 |

For held-critical scenes 7, 9, 10, 11, and 16 at operational width 7:

- headline recall: `0.871209`;
- full-text recall: `0.375481`;
- lower-support recall: `0.281031`;
- numeric recall: `0.397778`;
- x-gradient energy ratio: `0.489162`;
- y-gradient energy ratio: `0.856135`;
- structural held gates: `0/5`.

At severe width 21, the OCR aid collapses, but full-sheet visual review still finds major headlines, large numbers, chart and matrix silhouettes, and conclusion hierarchy primary. This is not evidence that exact words survive; it demonstrates that the visual assertion layer outlives fine support even after exact-text recognition becomes unreliable. Structural gates remain `0/16`. Directional smear therefore cannot authorize or repair the candidate.

## Sealed-v8 directional-smear finding

Thirty-five QA derivatives test the seven sealed-v8 scenes.

At operational width 7:

- `RESULT HELD` remains visually readable on 7/7 scenes;
- large method/status boundaries remain readable on 7/7 scenes;
- direct labels, arrows, borders, connectors, rails, and status columns remain distinguishable;
- no required meaning becomes ambiguous;
- full-text OCR recall is `0.550579`;
- headline OCR recall is `0.728767`;
- lower-support OCR recall is `0.471187`;
- tolerant luma-edge recall is `0.950304`;
- x-gradient energy ratio is `0.514001` while y-gradient energy ratio is `0.941538`.

OCR under directional smear is a conservative aid, not the verdict: the full-resolution and contact-sheet pixels remain legible well beyond the exact-token score. At severe width 21, badges and large status hierarchy remain visually recognizable, but fine direct labels, citations, provenance, and exact minor copy are no longer acceptance-reliable. Width 21 is characterization only.

## Pass-7 caption-safe proof compatibility

Thirty-five derivatives test the existing pass-7 proof.

At width 7:

- all seven scene-specific top gates remain visually exact;
- all seven `RESULT HELD` badges remain visually readable;
- full-text OCR recall is `0.583573`;
- headline OCR recall is `0.767133`;
- lower-support OCR recall is `0.476388`;
- a single global PSM-11 exact-pattern aid detects six of seven gate lines.

The OCR miss does not overrule readable pixels. It confirms that global OCR order and narrow horizontal glyph structure are fragile under an anisotropic transform.

## Pass-12 strengthened title-safe proof compatibility

Thirty-five derivatives test the pass-12 strengthened proof without changing it.

At operational width 7:

- all seven exact scene-specific gate lines remain visually readable;
- all seven complete `RESULT HELD` badges remain visually readable;
- cropped multi-PSM character-similarity acceptance remains 7/7 at threshold `0.85`;
- mean best-of-PSM gate similarity is `0.987813`;
- full-text OCR recall is `0.517288`;
- headline OCR recall is `0.672214`;
- x-gradient energy ratio is `0.518562` while y-gradient energy ratio is `0.949846`;
- no overlap, clipping, or semantic ambiguity appears.

At width 13, all seven strengthened gate lines remain visually exact, but the recorded OCR character aid is no longer monotonic or dependable. At width 21, seven gate containers, badges, and large status boundaries remain recognizable, but exact gate wording, small direct labels, citations, provenance, and thin vertical separators are not acceptance-reliable. Widths 13 and 21 remain characterization only.

## Evidence-backed action

`DIRECTIONAL_SMEAR_GUARD_PASS13.json` adds a non-pixel future-integration guard:

1. use the exact centered width-7 transform as a packet-specific operational review floor;
2. require 7/7 exact strengthened scene-gate lines visually and at the recorded `0.85` cropped character threshold;
3. require 7/7 complete `RESULT HELD` capsules and large scene-status boundaries;
4. preserve header/gate/badge/headline separation without clipping or overlap;
5. retain direct labels plus arrows, borders, connectors, rails, and stable positions;
6. carry no required distinction only through a thin vertical edge, one-pixel separator, narrow glyph spacing, small copy, citation, provenance footer, or fine axis;
7. keep human full-sheet and full-resolution review decisive;
8. treat widths 13 and 21 as characterization only;
9. rerun directional smear cumulatively with spatial defocus, JPEG recompression, black lift, title-safe crop, color/monochrome, obstruction, and 360p review.

No further pixel or copy correction is justified. The pass-12 strengthened proof already passes the operational width-7 floor. Sealed v8 and both proofs remain unchanged; no v9 was created. Hwao/Fable remains the sole integrator and proposal writer.

## Science blockers

Unchanged and binding:

1. no valid post-run independent A3.8 review for the frozen T4 artifact across the all-209-file content proof;
2. `KUN_FRAME_REVIEW.md` remains `FRAME REVIEW: AGREES FRAME_UNSTATED`.

Therefore `video_reportable_now` remains `false`. Pass 13 performs no scientific adjudication and carries no T4 measured values.
