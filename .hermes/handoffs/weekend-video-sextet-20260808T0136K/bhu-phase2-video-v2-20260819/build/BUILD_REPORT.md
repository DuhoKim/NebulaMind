# Local Phase-2 explainer v2 build report

Status: `FROZEN_LOCAL_ONLY_READY_FOR_KIMI_P2V2_RENDER_GATE`
Candidate: `build/BHU_PHASE2_EXPLAINER_V2_LOCAL_REVIEW.mp4`
SHA-256: `db4fcd92f7730618e9f66f6f13303ecec3019ed5da5da9d22a75a6264c671b5f`
Duration: 475.200 seconds

## QA

- Full decoded-audio gateway ASR: `PASS_FULL_RENDERED_AUDIO_ASR_NO_CONTRACT_RESIDUALS`
- Contract-bearing residuals: 0
- Cosmetic residuals: 1
- Assertion heading on every decoded state: `PASS_ASSERTION_HEADING_EVERY_DECODED_STATE`
- Encoded captions: `PASS_EXACT_ENCODED_CAPTION_PAYLOADS`
- Equation projection: `PASS_EXACTLY_THREE_PERMITTED_EQUATIONS`
- Honest no-plots cards: `PASS_HONEST_NO_PLOTS_CARDS_EXACTLY_02_06_08`
- Four pinned figures, attributions, walkthroughs: `PASS_FOUR_PINNED_PAPER_FIGURES_LARGE_ATTRIBUTED_AND_ANIMATED`
- BAND ladders and Planck markers: `PASS_LABELED_BANDS_LADDERS_AND_PLANCK_MARKERS`
- Full decode: `PASS`
- Mean/max volume: -20.9 / -0.4 dB

## Safety

Local Pillow + ffmpeg pipeline only; Hermes gateway TTS/ASR only. No uploads, Flow, Veo, image-generation credits, or cockpit-root audio writes. portal.nersc.gov was not used.

Ready for the Kimi v2 render gate; not publication-authorized.
