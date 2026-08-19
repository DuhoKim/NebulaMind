TORI_P1V_BUILD_COMPLETE

# Tori — Phase 1 results video local build

- Packet gate: `PASS_EXPLAINER_PACKET` (first line verified before build).
- Candidate: `build/BHU_PHASE1_RESULTS_VIDEO_LOCAL_REVIEW.mp4`
- Candidate SHA-256: `e32cc6109c7b7a514b0b0336a6ac65783f25d0407e764f2504307cb49aa5e4fc`
- Duration: `355.433333` seconds (within 240–360 seconds).
- Panel 01 end: `34.0` seconds (within 35 seconds).
- Final QA: `PASS_LOCAL_RENDER_QA_READY_FOR_MIRU_REVIEW`.
- Decoded final-audio ASR: `PASS_EXACT_ASR_WORD_DIFF_WITH_TARGETED_CONTEXT_ADJUDICATION`.
- Heading pixel QA: `PASS_EXACT_HEADING_PROJECTION_AND_ENCODED_PIXELS`.
- Encoded caption QA: `PASS_EXACT_ENCODED_CAPTION_PAYLOADS`.
- Forbidden sweep (`is falsified`, `we proved`, `theory is dead`, `Smolin`): `PASS_FORBIDDEN_SWEEP`, 0 hits.
- Exact on-screen equations: `Λ = 3Ω²/c²` and `w = +1/3`, both projected.
- Font: `/System/Library/Fonts/Helvetica.ttc`; Helvetica index 0 contains every required `Ω/²/⁹/⁻` glyph, so fallback was not required. Choice and glyph audit are recorded in `build/qa/card-text-and-geometry-audit.json`.
- Freeze: `FROZEN_LOCAL_ONLY_READY_FOR_MIRU_REVIEW`; provenance verification `PASS_FROZEN_PROVENANCE_VERIFIED`.
- Safety: local deterministic Pillow + ffmpeg pipeline; managed gateway TTS/ASR only; no upload, no publication, no video-generation credits; `portal.nersc.gov` untouched.

Primary receipts:
- `build/FREEZE.json`
- `build/BUILD_REPORT.md`
- `build/qa/final-qa-report.json`
- `build/qa/card-text-and-geometry-audit.json`
- `build/audio/timeline.json`
