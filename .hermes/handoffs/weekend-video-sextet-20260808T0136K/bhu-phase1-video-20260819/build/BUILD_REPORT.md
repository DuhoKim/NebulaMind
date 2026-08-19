# Local render build report

Status: `FROZEN_LOCAL_ONLY_READY_FOR_MIRU_REVIEW`
Candidate: `BHU_PHASE1_RESULTS_VIDEO_LOCAL_REVIEW.mp4`
SHA-256: `e32cc6109c7b7a514b0b0336a6ac65783f25d0407e764f2504307cb49aa5e4fc`
Duration: 355.433 seconds

## QA

- Final gate: `PASS_LOCAL_RENDER_QA_READY_FOR_MIRU_REVIEW`
- Decoded-audio ASR word diff: `PASS_EXACT_ASR_WORD_DIFF_WITH_TARGETED_CONTEXT_ADJUDICATION`
- Encoded card headings: `PASS_EXACT_HEADING_PROJECTION_AND_ENCODED_PIXELS`
- Encoded captions: `PASS_EXACT_ENCODED_CAPTION_PAYLOADS`
- Forbidden sweep: `PASS_FORBIDDEN_SWEEP`
- Full media decode: `PASS`
- Mean/max volume: -16.4 / -2.2 dB

## Safety and scope

Local Pillow + ffmpeg pipeline only. Gateway TTS and ASR only. No Veo, no Flow, no credits, no upload.

Panels 03, 04, 07, 08, and 09 use deterministic, explicitly labeled quantitative geometry; no unlabeled logarithmic compression is used.

## Deviations from the v1 approach

No approach deviations. The implementation changes are limited to this lane's 7 hash-pinned gated inputs, Phase 1 graphics, output names, and content-specific ASR normalization.
Gateway stages were invoked with the Hermes checkout virtual-environment Python because the host python3 cannot import the current managed gateway's PEP 604 type syntax; this did not change the v1 media or gateway approach.

This artifact is ready for Miru render review, not publication.
