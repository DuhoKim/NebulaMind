# Future result-figure/axes specification — HELD

Status: design request only. Do not render a result figure while `video_reportable_now` is false. No T3/T4 values are reproduced here.
Integrator: Hwao/Fable.

## Why this exists

The official narration-only canary proves the deck can carry plots, but its result plots visually outrank their caveats. If the science/status gate is ever cleared, result figures need a representation contract before values are inserted.

## Figure A — asymmetry by condition and rung

Required grammar:

- y-axis: `A = (N_CW − N_ACW) / (N_CW + N_ACW)`, unitless;
- explicitly define `ACW = anticlockwise` in the adjacent sentence or on-figure key;
- symmetric y-limits around zero, pinned before measured values are inserted;
- high-contrast zero line, visually quieter than markers;
- x-axis grouped first by condition, then by rung; never imply a time series;
- condition labels printed in full: normal, monochrome control, mirrored 1, mirrored 2;
- rung labels printed in full: dominance ≥0.80 and ≥0.60;
- direct marker labels or a complete legend; colour must not carry condition meaning alone;
- uncertainty convention in an audience-readable note, including whether bars are 1σ and how they were computed;
- classified N printed beneath each condition/rung marker;
- no significance adjective in the headline;
- no result value in a hero-number card detached from its axis, sample, and uncertainty.

Mandatory status layer:

- `RESULT CLEARED` only after an authoritative gate receipt exists;
- otherwise replace the entire figure with the method/status boundary—do not place a small `RESULT HELD` disclaimer beneath measured markers.

## Figure B — paired-flip matrix

Only after the required post-run independent T4 verdict record exists:

- 2×2 matrix axes name reference label and mirrored-condition label;
- cells are `CW→CW`, `CW→ACW`, `ACW→CW`, `ACW→ACW`;
- print `n_pair`, objects classified in only one condition, and objects in neither;
- identify the pair: mirrored N × normal or mirrored N × monochrome;
- identify whether the pair is a primary read or reported-only control;
- keep frame interpretation separate: paired flipping does not resolve `FRAME UNSTATED`;
- no Land-comparative language while the standing prohibition remains.

## Provenance boundary

Audience layer:

- human paper/catalogue citation;
- source role, e.g. `ARCHIVE CENSUS`, `BIAS CONTROL`, or `INDEPENDENT REVIEW`;
- retrieval/freeze date where relevant.

Receipt layer only:

- absolute local paths;
- SHA-256 hashes;
- exact JSON fields or document anchors;
- renderer/tool hashes.

Internal filenames such as `T3_READING.json`, `LANA_T3_REDERIVATION.md`, and `KUN_FRAME_REVIEW.md` must never substitute for audience citations on the figure.

## Presentation acceptance checks

At full 1920×1080 frame and at contact-sheet scale:

1. axis title, zero, conditions, rung, N, and uncertainty convention remain legible;
2. marker/error-bar geometry carries the claim, not a paragraph below it;
3. status text is at least as prominent as the result headline;
4. no caveat is smaller than the provenance footer;
5. the closing frame restates finding, boundary, and next gate without a URL-only close.

## Gate

`HELD_RESULT_FIGURE_SPEC_ONLY`

This file requests no value insertion, candidate render, TTS, upload, publication, shared-tool edit, or release action.
