# NebulaMind V3 — subscription-backed Gemini Omni gesture-edit canary

Marker: `NEBULAMIND_V3_GEMINI_OMNI_GESTURE_EDIT_PACKET_V1`

## Route

- Consumer subscription surface: signed-in Gemini Apps `Create video` / Gemini Omni, or the equivalent built-in Flow Agent/Tool.
- This is not Gemini CLI, Developer API, Vertex, GCP, or API-key billing.
- Generate exactly one output for the canary.

## Inputs

1. Six-second video input (identity, static starting gesture, facial timing, exact approved Michael audio):
   `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/paper-videos-v3-male-lipsync-20260723T050645Z/lipsync/NEBULAMIND_V3_PRESENTER_C_MICHAEL_GESTURE_SCENE_CANARY.mp4`
2. Presenter C identity reference:
   `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/paper-videos-v3-male-lipsync-20260723T050645Z/identity/candidate_c_young_black_male.png`
3. Presenter C open-palm body/gesture reference:
   `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/paper-videos-v3-male-lipsync-20260723T050645Z/identity/presenter_c_gesture_open_palm.png`

## Exact prompt

Edit the uploaded video rather than creating a new presenter. Preserve the same fictional young male astronomer, face, hairstyle, age, navy shirt with cyan seams, observatory background, camera position, duration, speaking timing, and science-explainer tone. Add restrained continuous upper-body teaching gestures throughout: small natural forearm movements and gentle open-palm hand motions at mid-torso, with occasional subtle emphasis toward the science content on the viewer's left. Keep both hands below the face and never cover the presenter or science cards. Gestures must be calm, purposeful, anatomically correct, and continuous rather than frozen; no waving, no dramatic pointing, no fast arms, and no extra or fused fingers. Preserve the existing speech audio exactly; do not generate, replace, remix, pitch-shift, slow, or accelerate the voice. Preserve the existing lip timing. Stable camera, stable identity, no text changes, no new captions, no logos, no cuts.

## Fail-closed review gates

Reject the output if any gate fails:

- The Michael voice differs audibly from the input.
- Audio duration, waveform lineage, or word timing changes.
- Lip timing no longer matches the approved Michael track.
- Presenter C identity, age, clothing, or background drifts.
- Hands have extra/fused/missing fingers or visible morphing.
- Gestures cover the face or science cards.
- Motion is shaking, theatrical, too fast, or discontinuous.
- Camera, text, science cards, duration, or aspect ratio changes.

## Custody

- Download is a separate action after generation.
- Final custody requires local MP4 bytes, probe, SHA-256, audio comparison, temporal hand sheet, and human review.
- No YouTube, website, Git, deployment, DB, or public visibility mutation.
