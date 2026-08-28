# Local Phase-2 render build report

Status: `FROZEN_LOCAL_ONLY_READY_FOR_KIMI_RENDER_GATE`
Candidate: `build/BHU_PHASE2_RESULTS_VIDEO_LOCAL_REVIEW.mp4`
SHA-256: `f251d43cda0e7383d56864830cc3d0f68023b065205917edc2e2adb37964ffcb`
Duration: 330.467 seconds

## QA

- Full decoded-audio gateway ASR: `PASS_FULL_RENDERED_AUDIO_ASR_NO_CONTRACT_RESIDUALS`
- Contract-bearing residuals: 0
- Cosmetic residuals: 1
- Assertion headings and decoded pixels: `PASS_EXACT_ASSERTION_HEADINGS_AND_DECODED_PIXELS`
- Encoded captions: `PASS_EXACT_ENCODED_CAPTION_PAYLOADS`
- Equation projection: `PASS_EXACTLY_THREE_PERMITTED_EQUATIONS`
- Magnitude ladders and Planck markers: `PASS_LABELED_MAGNITUDE_GEOMETRY_AND_PLANCK_MARKERS`
- Full decode: `PASS`
- Mean/max volume: -20.2 / -1.1 dB

## Safety

Local Pillow + ffmpeg pipeline only; Hermes gateway TTS/ASR only. No uploads, Flow, Veo, image-generation credits, or cockpit-root audio writes. portal.nersc.gov was not used.

Ready for the Kimi render gate; not publication-authorized.
