# Local render build report

Status: `FROZEN_LOCAL_ONLY_READY_FOR_KUN_REVIEW`
Candidate: `BHU_EXPLAINER_V2_LOCAL_REVIEW.mp4`
SHA-256: `fba0964cce7c3734c48df070dfcd5f055aa5ce7b5ff9fc0ac15342a408359de5`
Duration: 341.300 seconds

## QA

- Final gate: `PASS_LOCAL_RENDER_QA_READY_FOR_KUN_REVIEW`
- Decoded-audio ASR word diff: `PASS_EXACT_ASR_WORD_DIFF_WITH_TARGETED_CONTEXT_ADJUDICATION`
- Encoded card headings: `PASS_EXACT_HEADING_PROJECTION_AND_ENCODED_PIXELS`
- Encoded captions: `PASS_EXACT_ENCODED_CAPTION_PAYLOADS`
- Full media decode: `PASS`
- Mean/max volume: -16.6 / -2.1 dB

## Safety and scope

Local Pillow + ffmpeg pipeline only. Gateway TTS and ASR only. No Veo, no Flow, no credits, no upload.

Panel 06 keeps the quoted 68.3% interval above the 2.00 line and uses a soft, endpoint-free 95.4% uncertainty halo crossing the line. It does not falsely draw 2.08 ± 0.07 itself below 2.00.

## Deviations from the v1 approach

No approach deviations. The implementation changes are limited to the v2 frozen inputs, 10-card visual plan, v2 output names, and v2 Brown–Bethe sentence IDs.
Gateway stages were invoked with the Hermes checkout virtual-environment Python because the host python3 cannot import the current managed gateway's PEP 604 type syntax; this did not change the v1 media or gateway approach.

This artifact is ready for Kun review, not publication.
