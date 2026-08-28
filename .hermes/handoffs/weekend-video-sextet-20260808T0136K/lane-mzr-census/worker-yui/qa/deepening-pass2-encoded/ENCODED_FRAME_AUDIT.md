# Deepening pass 2 — fresh encoded-frame scientific-presentation audit

Audit timestamp: 2026-08-08T02:27:59+09:00

Exact read-only candidate: `/Users/duhokim/HermesOps/cockpit/videos/mzr-archive-census-narrated-20260808T0155.mp4`

Candidate SHA-256: `0bdfd12dcc87098e1034196bc973df4ace79044cadc4261f3f827b65d7cd162d`

Fresh verification: 13,989,937 bytes; 128.4 s; H.264 1920×1080 at 30 fps plus AAC mono 24 kHz. The hash is unchanged from the prior audit. Twenty fresh encoded frames were extracted at labeled timestamps into this directory. Contact-sheet SHA-256: `5ac85b0f20ac582edb9ff9b52633170675a7f2b69ff9f0530e9fcadcc52ff563`.

All findings below are from encoded pixels, not renderer intent or audio inference.

## Pixel sequence and blocking evidence

- 000 s: section-only `Introduction` hold.
- 008 s: prose-first question card describes a pre-registered catalogue census.
- 016–024 s: full metallicity-versus-redshift scatter under `The spread this work is about`; body says the vertical spread is the problem `this census exists to measure`. This is a direct scientific-representation mismatch: T1 is metadata enumeration and makes no metallicity/MZR measurement.
- 032–040 s: `The method is the point` prose hold; retrieval rails and per-axis channel counts are not visualized.
- 045–048 s: giant `157`; 178 and 21 survive only in body text. The 19-redshift/2-abundance split and modifier examples are absent. Audience citation exposes `T1_FINDINGS.md`.
- 055–056 s: proportional bar compares 157 with 62 and labels 62 `explicit gas-phase evidence`. This overstates a frozen description-term regex and makes 62 look like a privileged subset, even though the heading says reach is not eligibility. The chart omits the 178→21→157 conservation path, all-157-to-T2 topology, and the exact `not an eligibility filter` boundary. An internal run/path is drawn across the chart.
- 064–065 s: giant `62` repeats `explicit gas-phase evidence`; no same-frame term-regex, non-eligibility, all-157-to-T2, or T2-status lock appears. Audience citation exposes `T1E_GASPHASE_COUNT.json`.
- 072–080 s: prose says seven recall members returned and three controls stayed out, but does not render `7/7` or `0/3` and does not warn that these controls missed the dominant precision-contamination mode.
- 088–096 s: prose says rules were frozen before any table was judged, but no qualified `contract frozen · 157-table application not completed · no eligible-table count` gate is shown. Audience citation exposes `FREEZE_RECORD_T2.md`.
- 104–112 s: the closing claim says `The redshift tag is applied to the symbol Z, not the concept — stellar coordinates, gravitational redshifts and model grids all enter candidacy.` This compresses two distinct precision failures into one slogan. Galactic height and model-grid metal fraction are symbol/meaning collisions. Stellar gravitational redshift and gravitational-redshift velocity are genuine gravitational-redshift quantities whose failure here is target-domain mismatch for a galaxy-MZR census. T1 records all four as semantically distinct examples and leaves actual rulings to T2. The frame should not imply that every example is `not the concept`.
- 120 s: section-only `Summary` hold.

The encoded sequence remains prose/section-hold dominant. It does not show the required evidence grammar as a persistent scientific presentation.

## Fresh verdict

`FAIL_FOR_SCIENTIFIC_REPRESENTATION_GRAPHICS_GRAMMAR_AND_CONTAMINATION_TAXONOMY`

The candidate remains preserved and read-only. This verdict does not authorize replacement, shared-tool edits, TTS, upload, or publication.

## Next evidence-backed correction

Create a preserved worker visual revision that keeps the corrected 178→−21→157→T2 topology and 62 side inset, but replaces the undifferentiated `symbol-Z contamination` example strip with two explicit evidence-bounded groups:

1. `SYMBOL / MEANING COLLISION`: Galactic Cartesian height; stellar-grid metal fraction (model Z).
2. `TARGET-DOMAIN MISMATCH`: stellar gravitational redshift; gravitational-redshift velocity.

Label both as recorded precision-failure examples, not T2 rulings. In narration, say the frozen controls did not cover the dominant precision-contamination mode; do not say every recorded contaminant is `not the concept`.
