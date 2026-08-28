# Spin worker-Yui — isolated deepening pass 6 multi-resolution encoded-frame audit

Extraction completed: 2026-08-07T20:15:44.050454+00:00 (2026-08-08T05:15:44.050454+09:00)
Audit completed: 2026-08-08T05:21:40+09:00
Scope: exact held Hwao candidate and sealed-v8 downscale derivatives, read-only; no candidate, audio, shared tool, public asset, or sealed-v8 pixel changed.
Verdict: `FAIL_SCIENTIFIC_PRESENTATION_AND_HELD_SOURCE_GATE`

## Fresh multi-resolution extraction

- Candidate: `/Users/duhokim/HermesOps/cockpit/videos/spin-parity-census-narrated-20260808T0149.mp4`
- SHA-256: `02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431`; exact official-freeze match.
- Fresh scene detection at threshold 0.04 again found 15 cuts and 16 scenes.
- Pass 6 independently decoded each scene midpoint at 1920×1080, 1280×720, 960×540, and 640×360 using deterministic Lanczos scaling: 64 RGB PNGs total.
- All 16 native 1080p hashes reproduce pass 4's midpoint hashes byte-for-byte.
- Exact receipt and per-frame hashes: `qa/pass6_resolution_audit/extraction_receipt.json`.
- Contact sheets: `contact_sheet_1080p.png`, `contact_sheet_720p.png`, `contact_sheet_540p.png`, and `contact_sheet_360p.png` under `qa/pass6_resolution_audit/`.

## Scientific-presentation finding

The held candidate's hierarchy degrades asymmetrically. Dominant headlines, large number cards, matrix cells, and plot silhouettes remain salient under downscale, while lower support, caveat, citation, provenance, and small axis text disappears much faster.

Deterministic Tesseract token-multiset retention relative to fresh native 1080p:

| Resolution | Full-frame mean | Headline-region mean | Lower-support mean | Structural-gate scenes |
|---|---:|---:|---:|---:|
| 1080p | 1.000000 | 1.000000 | 1.000000 | 0/16 |
| 720p | 0.942152 | 0.997500 | 0.897305 | 0/16 |
| 540p | 0.840371 | 0.977510 | 0.702634 | 0/16 |
| 360p | 0.728766 | 0.961206 | 0.230643 | 0/16 |

The critical held scenes 7, 9, 10, 11, and 16 degrade more sharply at 360p:

- full-frame retention: 0.380218;
- headline-region retention: 0.903130;
- lower-support retention: 0.416629;
- structural `RESULT HELD`, `FRAME UNSTATED`, or `OUTCOMES WITHHELD` phrase: 0/5 scenes at every resolution.

Mean OCR-recognized numeric-token count across all scenes falls from 5.4375 at 1080p to 1.1875 at 360p, but the visually dominant number cards, bars, matrix cells, and chart forms remain identifiable. This does not make the deck safer: the qualification layer is lost more aggressively than the assertion layer.

Scene-specific representation consequences:

- Scene 7 retains a dominant result plot and headline at 360p while fine plot labels, caveats, and internal provenance largely collapse.
- Scenes 9 and 11 retain their bar geometry and dominant claim headlines while small axes and explanatory provenance lose legibility.
- Scene 10 retains the large matrix counts and headline while fine labels and provenance recede.
- Scene 16 retains the URL and work-in-progress close without adding a structural held boundary.

A small disclaimer or citation therefore cannot carry semantic authorization. Low-resolution playback amplifies the exact representation defect rather than hiding it.

## Sealed-v8 low-resolution check

Pass 6 derived 28 QA-only v8 frames at the same four resolutions and inspected four contact sheets under `qa/pass6_v8_legibility/`. Sealed v8 source pixels and hashes remain unchanged.

Human full-sheet review reads the high-contrast top-right `RESULT HELD` capsule on 7/7 scenes at 1080p, 720p, 540p, and 360p. Large structural reinforcement remains present where needed: `RESULT LOCKED` on scene 1, `FRAME UNSTATED` on scene 4, `OUTCOMES WITHHELD` on scene 6, and the full-frame `RESULT STATUS · HELD` close on scene 7.

Badge-crop OCR detects 5/7 badges at every resolution and misses scenes 1 and 5 even at 1080p. Because the miss set is unchanged across all four scales and both badges remain visually readable, this is a stable OCR/layout limitation rather than downscale loss. Human visual review is the decisive badge test; OCR remains auxiliary.

No evidence-backed pixel defect warrants v9. V8 already preserves its structural hold through 360p while omitting result values and plots.

## Evidence-backed correction

`LOW_RESOLUTION_REPRESENTATION_GUARD_PASS6.json` adds a non-pixel integration contract for Hwao:

1. Treat a 360p downscale as a representation-boundary acceptance test.
2. Put every semantic hold in headline-scale copy or a persistent high-contrast `RESULT HELD` capsule.
3. Never rely on footer, citation, provenance, caveat, or small axis copy to carry the gate.
4. Keep the badge visually readable on 7/7 scenes after any authorized render, crop, or compression.
5. Retain pass 5's clean hard cuts and reject blank or badge-free transition frames.
6. Reject any integration where result-bearing headlines, numbers, or plot silhouettes survive downscale but their hold does not.

This correction changes no sealed pixel and grants no render, narration, candidate, or publication authorization.

## Exact blocker state

Pass 5 directly content-covered all 209 regular source files for exact T4/A3.8 identity markers and found no valid post-run independent A3.8 review record. Pass 6 does not reinterpret that absence or the quarantined result artifact. `KUN_FRAME_REVIEW.md` remains exactly `FRAME REVIEW: AGREES FRAME_UNSTATED`.

`video_reportable_now` remains `false`. Preserve 0149 as failed evidence. If Hwao later authorizes method-only integration, start from sealed v8 and enforce both the pass-5 hard-cut contract and pass-6 360p representation guard. Result integration, narration, encoding, publication, and public wiring remain separate explicit gates.
