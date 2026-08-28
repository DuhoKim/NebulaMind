# Build receipt — introduction rebuild v3

Timestamp: 2026-08-09T00:11:29+0900 KST
Status: `LOCAL_SELF_QA_PASS_PENDING_POST_ENCODED_REVIEW`

## Deliverable

- File: `spin-method-overhaul-canary-20260808T1959K.mp4`
- SHA-256: `c5e7deed0dc243ccff170fdb72b128f4816a85e1ed4dbc185543e53496baa240`
- Bytes: 16,065,978
- Duration: 187.695 seconds
- Video: H.264, 1920×1080, 30 fps, 5,630 decoded frames
- Audio: AAC, mono, 48 kHz
- Full decode: PASS

## Narration and timing

- Script: `narration_script_v3.json`
- Script SHA-256: `1865f96b334a44499c58b6fdf545e140110bde2680ed202593dda2bd3a121f8b`
- TTS receipt: `audio_v3/synthesis_receipt.json`
- TTS receipt SHA-256: `129b2e37f29d6e5b7a41678924adb897082b16574fd18b30518ed63c3a2153a3`
- Voice: Alloy via managed OpenAI audio gateway
- Speed: 1.18
- Music: none
- Narration master: `audio_v3/narration_master.wav`
- Narration-master SHA-256: `74f2860b59c7ebf71816694c652f9a7e316346094e16db0b6e35499b337c024d`
- Timeline: `audio_v3/timeline.json`
- Timeline SHA-256: `4e44a05eaf2e228b71c376e2c6f1ffdb7061856291aaaac5b1923f4df087f5f9`
- Subtitles: `spin-method-overhaul-canary-20260808T1959K-v3.srt`
- Subtitle SHA-256: `13dd85d937221dedadb4f31e1dbe30cfa81c4bc68bb8f055babf48e9e7fd7724`
- Sentence count: 27
- Word count: 354
- Delivered rate: 115.000 WPM
- PCM master duration: 187.695646 seconds
- Maximum A/V start quantization delta: 0.016584 seconds

## Renderer and QA lineage

- Renderer: `build.py`
- Renderer SHA-256: `8f90a4fc35f79311c923b67cb765415efaaeb2885d568de7188cabe7a61a020c`
- Build receipt JSON: `build_receipt.json`
- Build receipt SHA-256: `3dd4155681c10c90eef0e5b5d1f7a9262d47cb1b7e9f83c906e60f090a2f511f`
- Machine QA: `encoded_qa.json`
- Machine-QA SHA-256: `5fab3cc03dc5989a837d6ce6fe9164bf79468981c06b6ac5024f11a87ce6e7ab`
- Encoded contact sheet: `encoded-contact-sheet-v3.jpg`
- Contact-sheet SHA-256: `128af3494de7dc7820ccef78ca90149b42c1ab319306d8ca8b755eb49c032bcf`
- Encoded introduction transcription: `encoded_qa/encoded-introduction-transcription.json`
- Introduction-transcription SHA-256: `7c8aac440b5055d620b94286d77e3f8f4bfcd3924312a38becaa2ea9b1363aa2`
- Source manifest: `source_manifest_v3.json`
- Source-manifest SHA-256: `6b4331a39667df4f6e79bf1c07037ce3dbc599a74b019611ece34bdd05e62199`

## Verification outcome

- Encoded machine checks: 26/26 PASS.
- Encoded four-sentence introduction transcription: exact match.
- Encoded contact-sheet visual inspection: PASS.
- Full H.264/AAC decode: PASS.
- Loudness: −20.31 LUFS; true peak −2.30 dBTP.
- Longest near-unchanged run: 5.5 seconds; no freeze at or above eight seconds.
- Captions: maximum two lines.
- Forbidden claim/OCR/internal-filename hits: none.

## Predecessor preservation

- `spin-method-overhaul-canary-20260808T1312K.mp4`: `40804f86b221bc9af3d5107b923b954b379e0734e384c33c29fc0363712d65c9`
- `narration_script_v2.json`: `3f033dd02d00767c6bb4cc1baf8b7197a78847bad076411cbaed9aab732cd416`

Both match their frozen predecessor hashes.

## Closed-gate receipt

`video_reportable_now=false`. This candidate remains local and pending independent post-encoded review. It was not uploaded, copied into cockpit/videos, committed, deployed, or published.
