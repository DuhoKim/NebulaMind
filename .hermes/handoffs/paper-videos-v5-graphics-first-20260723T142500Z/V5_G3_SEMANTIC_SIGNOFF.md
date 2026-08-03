# V5-G3 SEMANTIC SIGN-OFF — z9 motion-graphics canary spec (no faces)

Coordinator: Hwao · Lana semantic hat (honest record: ruling executed by Hwao in-lane, falsifiable via cited rows/anchors) · 2026-07-24 KST
Scope: `V5_G3_MOTION_GRAPHICS_SPEC.json` only. This turn writes spec + sign-off and nothing else — no audio/video build, no presenter/face/office asset, no YouTube, visibility, site, DB, git, runtime, or cockpit action.

## Release interpretation on record

Duho's "switch to Studio, office setting" clarification timed out; the selected safest interpretation (per relay) is: G3 runs on the Mac Studio host with **no faces and no office imagery**, and the warm research-office setting is **reserved for the presenter intro/outro at V5-G4 only**. This spec encodes that: office assets are hard-banned in G3, noted as a G4-only reservation.

## Contract compliance — PASS

| Requirement | Where satisfied |
|---|---|
| Bounded representative canary from the signed storyboard | 17 rows (12–22, 24–29) in storyboard cut order; exclusions justified row-by-row in `canary_selection.excluded_and_why` |
| Conceptual diagram with exact label | CG_D (rows 20–21) and CG_E (rows 24–27) both carry "CONCEPTUAL — illustration, not data"; label presence + ≥22 px height is a QA assertion |
| Figure 1 progression axes→curves→red points→−0.69 gap→anchor swap→blue stack | Rows 12–19 + 22 traverse VS1→VS6 — all six signed view states, none repeated identically |
| Uncertainty separation (bound design rule) | `cg_e_design_rule_binding`: split panel with divider — calibration systematic (0.1–0.2 dex band vs 0.69 dex deficit bar, rows 25–26) LEFT; five-galaxy sample markers (row 27) RIGHT; blending prohibited |
| Explicit non-detection boundary | Rows 28–29 verbatim, warning-styled, with a dedicated boundary QA |
| No presenter/face/office in G3 | Hard-banned; freeze-frame QA asserts zero such content; office deferred to G4 |
| Exact signed sentences | Sentences byte-locked to the amended `V5_G2_Z9_STORYBOARD.json`; row 22's "that stack" keeps its antecedent because rows 20–21 are retained — coherence preserved by selection, never by rewording |
| am_michael speed 1.0 + 1.0 s pauses | `audio_contract_when_built` mirrors the V5-G1 measured contract |
| One action/sentence, onset ±0.3 s | `action_rule` + `sync_qa`; rebased timeline gives every onset target |
| No invented geometry/numbers; overlays never cover points | `source_locks.hash_lock_rule` (crop sha `8d1575a7…` verified pre-render, abort on mismatch) + `coordinate_view_state_qa` (five red points always fully visible; overlay boxes may not intersect point regions or the blue square); no sigma/p-value/detection language allowed |
| ≤150 s and 105–125 delivered WPM | Planned 106.1 s and 113.7 WPM (201 words; arithmetic: 201/106.1×60 = 113.67) — comfortable margins |
| Studio absolute tool paths, no cv2 | `/opt/homebrew/bin/ffmpeg`, `/opt/homebrew/bin/ffprobe`, PIL+numpy+matplotlib pipeline; cv2 import prohibited |

## Accounting audit (word/duration convention as verified at G2)

Included-row words: 7+13+7+9+13+16+15+10+6+11+20+6+19+15+9+18+7 = **201**. Speech seconds (sum of signed row end−start): **90.1**. 16 pauses × 1.0 s ⇒ **106.1 s** total; delivered WPM **113.7**. All inside contract.

## Ruling

**SIGNED — the G3 spec is approved exactly as written.** Any change to included rows, sentences, timings, actions, or QA rules voids this sign-off. The G3 build is the next bounded Tori step on the Studio host per the spec's `after_sign`; faces remain prohibited through all of G3, and the office setting enters only with the G4 presenter bookends after Duho watches the G3 canary.

HWAO_V5_G3_MOTION_SPEC_SIGNED_COMPLETE
