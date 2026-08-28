# Hwao integration request — C41 MZR anchor-gap video

Request class: candidate integration only. No upload, publication, TTS, shared-tool, or public-artifact action is authorized by this paper lane.

## Recommended evidence package

- `EVIDENCE_FREEZE.json` — deterministic extraction of the frozen run, paper, public-paper hash match, and current-video probe.
- `STORYBOARD_PROPOSAL.json` — nine sentence/action beats, display citations separated from verification paths, 106 s of duration floors, 212 words, 120 WPM at those floors.
- `PROPOSAL_VALIDATION.json` — `PASS_PROPOSAL_ONLY`, no errors or warnings.
- `FRAME_DIAGNOSIS.md` and `qa/current/VERDICT.json` — exact current encoded-artifact failure.
- `proposals/stills-v2/` — corrected graphics-first proposal stills and QA. `stills-v1/` is retained as failed first-pass evidence.

## Requested integration actions

1. Treat the current public MP4 as stale-lineage QA input, not the candidate base. It is 81.0 s with nine observed scene states and no audio, while the current source storyboard has sixteen cards totaling 107.5 s.
2. Build the candidate around the explicit unit sequence:
   - 79 archive tables;
   - 23 candidate tables with redshift available in-table or by sibling join;
   - 11 tables fetched at run time across 8 catalogs, with 12 candidate tables unreachable;
   - 95 z > 3 rows with tabulated λ4363 flux;
   - 5 contract-grade anchors with direct-Te abundance and linked stellar mass.
3. Use equal-width non-proportional stage cards across table/row/anchor unit changes. Never let the geometry imply a single-unit funnel.
4. Use proportional geometry only for the 95-row accounting: 64 below S/N floor, 12 no Hβ, 6 missing required flux, 8 Te failures, and 5 survivors.
5. Show the mass-bin result against one common decision baseline:
   - actual bars 2, 1, 0;
   - shared dashed minimum `N = 3 anchors per bin`;
   - `+2` anchors below the frozen `log10(M*/M_sun) = 8` floor in a separate side pool, explicitly not a fourth bin.
6. Do not use `lit_metallicity.png` as evidence, the existing bins PNG as the final decision chart, or panel a of `ANCHOR_GAP_FIGURE.png` as a short-video relation result. The reasons are recorded in `STORYBOARD_PROPOSAL.json`.
7. Use author/year/journal or the public paper citation on screen. Keep internal filenames and absolute paths in QA manifests only.
8. Hold the final statement: `ARCHIVE CENSUS — NOT A GALAXY RELATION`, with explicit exclusions of a calibrated high-z relation, a deficit verdict, sky absence, and an FMR result.
9. If and only if Hwao authorizes narration, use the managed Nous route with `gpt-4o-mini-tts`, voice `alloy`, speed `1.18`. Measure each generated clip, then set each affected card to `max(duration_floor, audio_duration + pad)`. A heading or body edit requires a full affected-card narration recut.
10. After integration, inspect opening, 79/23/11/95/5 unit transitions, row-accounting frame, mass-bin threshold frame, and final boundary at full encoded resolution. Preserve failed candidates and contact sheets.

## Suggested implementation path

The v2 PNGs can be used directly as proposal figures, or Hwao can port their deterministic geometry into the shared renderer. The latter is a shared-tool decision and remains Hwao-only. The worker-Yui lane did not modify the shared renderer or storyboard of record.

## Closed gates

- No narration or TTS was invoked.
- No MP4 candidate bundle was written.
- No shared tool was modified.
- No current or public artifact was modified.
- No publication action is requested.

This request is stored in the mapped worker-Yui lane because the user’s coordination update restricted this worker to that directory. Hwao may consume or copy it into the integrator request queue.
