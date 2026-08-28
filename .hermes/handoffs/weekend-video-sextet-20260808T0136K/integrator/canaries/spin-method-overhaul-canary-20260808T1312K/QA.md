# QA — encoded spin method overhaul canary

Timestamp: 2026-08-08T14:03:11+0900 KST
Candidate state: `PENDING_SEXTET_POST_ENCODED_REVIEW`
Self-QA disposition: **PASS (19/19 machine checks)**
Overall Sextet PASS: **not issued**; Tori and Kun amendments are still required.

## Frozen encoded artifact

- MP4: `spin-method-overhaul-canary-20260808T1312K.mp4`
- SHA-256: `40804f86b221bc9af3d5107b923b954b379e0734e384c33c29fc0363712d65c9`
- Size: 13,697,038 bytes
- Duration: 159.000 s
- Video: H.264, 1920×1080, 30 fps, 4,770 frames
- Audio: AAC, 48 kHz, mono, one stream
- Full audio/video decode through EOF: PASS

The MP4 and its build inputs are frozen for the independent post-encoded review. They will not be rewritten unless a reviewer issues HOLD; any replacement must use a new version.

## Audio-first contract

- Fresh corrected lineage: `narration_script_v2.json` → 24 sentence-aligned Alloy calls → decoded PCM → solved pauses → `audio_v2/narration_master.wav`
- Voice: Alloy
- Synthesis speed: 1.18
- Music: none
- Words: 299
- Delivered pace: 115.0 wpm
- Master duration: 159.000 s
- Maximum audio-start to frame-quantized visual-action-start delta: 0.0166 s (limit ±0.3 s)
- Encoded integrated loudness: −20.31 LUFS
- Encoded true peak: −2.31 dBTP; no clipping
- Captions: 17 one-line and 7 two-line subtitles; zero over two lines

## Encoded media and motion QA

All 19 checks in `encoded_qa.json` pass:

- exactly one H.264 video stream and one AAC narration stream;
- 1920×1080 at 30 fps;
- encoded duration matches the PCM-derived duration within one frame;
- all 24 sentence-midpoint frames are nonblack;
- five independently decoded mirror positions are unique;
- no `freezedetect` event of 8 seconds or longer;
- at 2 fps, the longest near-unchanged run is 6.5 s under the recorded 0.08 luma-difference threshold;
- integrated loudness is in the intelligible QA range and true peak is below the no-clipping limit;
- OCR finds no forbidden topic term or internal filename on encoded pixels;
- narration contains no forbidden claim term;
- encoded MP4 hash matches `build_receipt.json`;
- rejected v1 narration master remains byte-preserved.

Encoded frame audit sheet: `encoded-contact-sheet-v2.jpg` (24 state midpoints plus five mirror-transform positions).

## Scientific presentation QA

Encoded visual self-QA: **PASS**.

- `s01–s05`: title/question, then two unresolved explanations; no opening disclaimer.
- `s06–s10`: the longest conceptual sequence and visual peak; one spiral collapses through a horizontal mirror plane, re-expands inverted, changes CW→ACW label, and separates MUST INVERT from NEED NOT INVERT predictions.
- `s11`: mirror logic, cuts, thresholds, and pairs are fixed before calculation.
- `s12–s13`: one Galaxy Zoo 1 source feeds three explicitly parallel readouts with counts attached to stages; the audience citation is `Galaxy Zoo 1 data release · Table 2`, not an internal filename.
- `s14–s16`: N_CW/N_ACW definitions, numerator, denominator, symmetric sign rail, and `VALUE WITHHELD`; sign convention and withholding share state 16.
- `s17–s18`: three-row bias-control matrix, failure modes, and `DESIGN ONLY · NO OUTCOMES`.
- `s19–s20`: self-imposed discipline first; specific open gates are consequences of a standard fixed before calculation.
- `s21`: known / not reportable / next scientific gate boundary.
- `s22–s24`: the opening images-versus-labeling question returns and closes on the mirror discriminant, not on workflow status.

All 24 states are graphics/diagram-led; captions remain a bounded subtitle strip. The rejected 11-card/presenter/paragraph-number-card base is not reused.

## Claim-boundary QA

PASS:

- symbolic equation only, no measured asymmetry value;
- no result direction or interpretation;
- no T3/T4 result figure or number;
- no forbidden topic language in narration or decoded-frame OCR;
- sample-funnel counts only, with sample size carrying the visual scale;
- no internal source filenames rendered to the audience.

## Remaining external gate

Tori has independently decoded this exact hash into `reviews/tori-overhaul-evidence/40804f86/`, including 2 fps OCR with zero forbidden hits, but has not yet appended the formal post-build verdict to `reviews/TORI_OVERHAUL.md`. Kun has not yet appended the new-candidate acceptance amendment to `reviews/KUN_OVERHAUL.md`.

Therefore this file records self-QA PASS only. Candidate status remains `PENDING_SEXTET_POST_ENCODED_REVIEW`; it must not be described as overall PASS yet.
