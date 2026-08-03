# Five-paper explainer batch plan

Marker: `NEBULAMIND_FIVE_PAPER_VIDEO_PLAN_V1`

## Scope

Create one explainer for each durable Paper-stage manuscript ratified by Hwao:

1. z≈9–10 unlensed metallicity deficit
2. scaling relations from SDSS to JWST
3. massive-galaxy abundance versus IllustrisTNG
4. MZR aperture/calibration methods framework
5. calibration-is-not-validation TNG test

Transient `/api/lab/runs` records and demos are excluded.

## Media contract

- 1280×720, 30 fps, H.264 + AAC, faststart, 74 seconds each.
- Silent approved Flow-astronomer portrait during 2.5-second opening and 1.5-second outro only.
- No visible speaking presenter and therefore no false lip-sync.
- Six narrated evidence scenes totaling 70 seconds.
- Female `en-US-EmmaNeural` voice, scene-bounded and timing-checked.
- No music.
- Burned-in exact narration plus matching manual English SRT.
- Actual frozen PDF title page shown; all other graphics are deterministic text/value cards.
- No quantitative chart geometry unless directly encoded by a source value.

## Acceptance gates

Per video:

1. frozen source hashes still match before render and before final mux;
2. exact title/description/status wording from `paper_video_specs.json`;
3. source PDF and first page exist;
4. six narrated scenes, non-overlapping SRT, full caption text, no silent truncation;
5. voice metadata says female Emma;
6. duration 74.0 ± 0.08 seconds;
7. 1280×720, 30 fps, H.264 High, yuv420p, AAC stereo 48 kHz;
8. integrated loudness target approximately −16 LUFS and true peak ≤ −1.5 dBTP;
9. full decode succeeds; black/silence scans reviewed;
10. temporal frames visually pass; scene 1 and status scene checked at full resolution;
11. independent ASR recovers the scientific numbers/status, with proper-noun variants normalized only in QA notes;
12. SHA-256 and byte size recorded.

Batch:

- five exact-title duplicate inventories before upload;
- uploads occur once each as unlisted and are checkpointed immediately;
- manual captions must be serving before any public flip;
- public visibility remains a separate post-review gate;
- Nebula source integration occurs only after stable YouTube IDs exist;
- Git and runtime deployment remain separately gated.
