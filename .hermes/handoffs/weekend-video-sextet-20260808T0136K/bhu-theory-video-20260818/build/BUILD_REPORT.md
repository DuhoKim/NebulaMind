# Local render build report

Status: `FROZEN_LOCAL_ONLY_READY_FOR_KUN_REVIEW`
Candidate: `BHU_THEORY_CLOSURE_VIDEO_LOCAL_REVIEW.mp4`
SHA-256: `26626fc26ee7cfc31f3ce0b8c720588ed4150b195e9454c743b4c91fd6a7988e`
Duration: 328.400 seconds

## QA

- Final gate: `PASS_LOCAL_RENDER_QA_READY_FOR_KUN_REVIEW`
- Decoded-audio ASR word diff: `PASS_EXACT_ASR_WORD_DIFF_WITH_TARGETED_CONTEXT_ADJUDICATION`
- Encoded card headings: `PASS_EXACT_HEADING_PROJECTION_AND_ENCODED_PIXELS`
- Encoded captions: `PASS_EXACT_ENCODED_CAPTION_PAYLOADS`
- Forbidden sweep: `PASS_FORBIDDEN_SWEEP`
- Full media decode: `PASS`
- Mean/max volume: -16.3 / -2.2 dB

## Safety and scope

Local Pillow + ffmpeg pipeline only. Gateway TTS and ASR only. No Veo, no Flow, no credits, no upload.

Panel 06 uses an explicitly stepped magnitude ladder, with 6 tenfold ticks, 4 complete ×10 step blocks, and closed-world NEEDED/ALLOWED endpoint labels.

## Deviations from the v1 approach

No approach deviations. The implementation changes are limited to this lane's 7 hash-pinned gated inputs, theory-closure graphics, output names, and a content-keyed Brown–Bethe retake policy if that name appears.
Gateway stages were invoked with the Hermes checkout virtual-environment Python because the host python3 cannot import the current managed gateway's PEP 604 type syntax; this did not change the v1 media or gateway approach.

This artifact is ready for Kun review, not publication.
