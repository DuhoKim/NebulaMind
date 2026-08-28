# Self-QA — introduction rebuild v3

Timestamp: 2026-08-09T00:11:29+0900 KST
Candidate: `spin-method-overhaul-canary-20260808T1959K.mp4`
SHA-256: `c5e7deed0dc243ccff170fdb72b128f4816a85e1ed4dbc185543e53496baa240`
Disposition: **LOCAL SELF-QA PASS — 26/26 encoded checks; pending independent post-encoded review**

## Media integrity

- Full H.264 and AAC decode: PASS.
- Streams: exactly one H.264 video stream and one mono AAC audio stream.
- Raster and cadence: 1920×1080, 30 fps, 5,630 decoded frames.
- Encoded duration: 187.695 seconds; within one frame of the 187.695646-second PCM master.
- File size: 16,065,978 bytes.
- Audio: 48 kHz mono AAC.
- Encoded integrated loudness: −20.31 LUFS.
- Encoded true peak: −2.30 dBTP; no clipping.

## Audio lineage and timing

- Every one of the 27 sentences was freshly synthesized through the managed OpenAI audio gateway.
- Model: `gpt-4o-mini-tts`; voice: `alloy`; speed: `1.18`; music: none.
- One exact script sentence per TTS call; no predecessor audio reused.
- Narration: 354 words at 115.000 WPM.
- All visual action starts were rebuilt from decoded 48 kHz PCM sample positions.
- Maximum action-start/frame quantization delta: 0.016584 seconds.
- Build receipt, v3 timeline, v3 script, renderer, and narration-master hashes replay exactly.

## Introduction — spoken and visual

- i01: two balanced handednesses, CW and ACW; no counts or selected direction.
- i02: `IF GENUINE` sky/universe motivation; spoken clause uses `If one were` and `would be`.
- i03: human sorting alternative; spoken clause uses `apparent excess` and `could instead`.
- i04: both balanced explanations visibly point into `HOW DO WE TELL THEM APART?`.
- The existing technical disambiguation question follows at s02.
- No spoken disclaimer precedes the motivation.
- Encoded introduction transcription: exact 1.0 normalized match to all four script sentences.
- Conditional-universe clause: PASS, not clipped.
- Conditional-sorters clause: PASS, not clipped.
- Closing opening question: PASS, complete.
- No introduction frame contains a sample count or implies an observed excess.

## Required inherited structure

- Mirror remains the spoken and visual peak: 28.440-second section versus 17.370 seconds for motivation and 16.836 seconds for the next-longest section.
- Five encoded mirror-collapse/expansion samples have five unique frame hashes.
- Frozen-method discipline survives.
- Parallel funnel with source-attached counts survives.
- Full symbolic estimator survives.
- Symmetric sign rail and `VALUE WITHHELD` remain visibly paired.
- Bias-control matrix remains explicitly `DESIGN ONLY · NO OUTCOMES`.
- Gates remain framed as self-imposed discipline under `WE TIED OUR OWN HANDS`.
- Scientific boundary survives.
- Closing re-poses `IMAGES OR LABELING PROCESS?` and lands on the mirror discriminant.
- Persistent `METHOD DESIGN · NO MEASURED VALUE` banner survives from the first introduction frame.

## Encoded-frame, motion, caption, and OCR QA

- All 27 sentence-midpoint encoded frames are nonblack.
- Encoded contact sheet inspected: no clipping, broken state, blank frame, internal filename, or claim-boundary regression.
- Captions: all 27 at no more than two lines.
- Freeze detector: no event at or above eight seconds.
- Longest near-unchanged run at 2 fps: 5.5 seconds.
- OCR forbidden/internal-filename hits: none.
- Narration forbidden-term hits: none.
- Forbidden scope includes significance, dipole, parity, cosmology, GRB, SN Ia, dark energy, quasar, H0, black-hole language, DESI, and Ganalyzer.

## Preservation and gates

- Accepted-with-incident predecessor MP4 remains unchanged at SHA-256 `40804f86b221bc9af3d5107b923b954b379e0734e384c33c29fc0363712d65c9`.
- Predecessor `narration_script_v2.json` remains unchanged at SHA-256 `3f033dd02d00767c6bb4cc1baf8b7197a78847bad076411cbaed9aab732cd416`.
- `video_reportable_now` remains false.
- No upload, cockpit/video-root copy, Git action, deployment, deletion, or public operation occurred.

Machine report: `encoded_qa.json`.
Encoded visual receipt: `encoded-contact-sheet-v3.jpg`.
Encoded introduction transcript: `encoded_qa/encoded-introduction-transcription.json`.
