# Local render build report

Status: `FROZEN_LOCAL_ONLY_READY_FOR_KUN_REVIEW`
Candidate: `BHU_NEUTRON_STAR_EXPLAINER_LOCAL_REVIEW.mp4`
SHA-256: `e5d6fae9436e6f66ac5825802236f4f6cba095c1e9b6676b46bc55d1bc160e18`
Duration: 334.100 seconds

## QA

- Final gate: `PASS_LOCAL_RENDER_QA_READY_FOR_KUN_REVIEW`
- Decoded-audio ASR word diff: `PASS_EXACT_ASR_WORD_DIFF`
- Encoded card headings: `PASS_EXACT_HEADING_PROJECTION_AND_ENCODED_PIXELS`
- Encoded captions: `PASS_EXACT_ENCODED_CAPTION_PAYLOADS`
- Full media decode: `PASS`
- Mean/max volume: -16.7 / -2.2 dB

## Safety and scope

Local Pillow + ffmpeg pipeline only. Gateway TTS and ASR only. No Veo, no Flow, no credits, no upload.

Panel 03 keeps the quoted 68.3% interval above the 2.00 line and uses a soft, endpoint-free 95.4% uncertainty halo crossing the line. It does not falsely draw 2.08 ± 0.07 itself below 2.00.

This artifact is ready for Kun review, not publication.
