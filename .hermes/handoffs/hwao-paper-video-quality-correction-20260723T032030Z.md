# Hwao relay — five paper-video quality correction

Marker: `USER_REJECTED_FIVE_PAPER_VIDEO_QUALITY_20260723T032030Z`
Recorded: `2026-07-23T03:20:30Z`
Authority: direct user correction — “the quality of the paper videos are too low”

Clarification marker: `USER_CLARIFIED_AUDIO_AND_COMPREHENSION_ARE_PRIMARY_20260723`
User correction: “no their audio quality is low and paper explanation is not easy to understand”

## Required coordinator interpretation

Treat the existing five public paper videos as quality-rejected V1 artifacts. Preserve them and the current website embeds until replacement V2 review masters pass and the user separately approves upload/publication/swap/site integration.

## Verified current state

- Five V1 videos are public, processed, embeddable, and manually captioned.
- All are 74.0 seconds, 1280×720, 30 fps.
- Local video-stream bitrates are only 318–338 kb/s; total bitrates are 497–516 kb/s.
- Live YouTube playback tops out at 720p for the flagship V1.
- The live flagship page embeds `hHxmycvPalE`; the live frontier page embeds `QjdJ1WZpiJY`, `XiB4dpn2o3g`, `jVyK-y_KQ14`, and `gDIVbF8ZUFg`.
- No current ID, privacy state, or embed was changed during this audit.

## Corrected root-cause audit

The user's primary rejection is audio quality and explanation clarity. Visual/template quality is secondary.

1. The source voice is Edge TTS MP3 at 24 kHz, mono, 48 kb/s. It is then upsampled to 48 kHz PCM and encoded as AAC; that changes the container specification but cannot restore missing source detail.
2. The renderer begins at `+20%` synthesis speed and raises individual scenes as high as `+33%` to `+60%` to force the text into fixed slots. The final `atempo` guard therefore missed a major perceptual failure already baked into synthesis.
3. Each paper carries 192–196 technical words in 70 narrated seconds: about 165–168 words per minute before allowing for pauses. The technical-explainer comprehension target is approximately 105–130 words per minute.
4. Each 10–13 second scene contains roughly 28–37 words plus three numeric cards and a conclusion. Viewers must decode unfamiliar terms while new evidence continues arriving.
5. The scripts assume prior knowledge of terms such as redshift, dex, direct-Te, mass–metallicity relation, star-forming main sequence, calibration anchor, abundance scale, and IllustrisTNG. Definitions and intuitive stakes are mostly absent.
6. The narrative jumps from question to sample to result to caveat without a worked example, causal explanation, or recap. It reports paper contents but does not teach the paper.
7. Short hard scene boundaries and near-one-second silence gaps make the narration feel assembled rather than conversational.
8. Loudness and final AAC bitrate passed, but those checks cannot certify voice naturalness, pronunciation, cadence, intelligibility, or pedagogical quality.
9. The outputs passed deterministic correctness QA, but the release process lacked an actual user-reviewed voice canary and a comprehension gate.

## Recommended bounded next move

Hwao should scope an audio-and-comprehension canary before any full V2 render:

- target: z≈9–10 unlensed metallicity-deficit paper;
- first deliverable: two or three high-fidelity female-voice samples reading the same representative 30–45 second plain-English passage;
- user must review the actual voice for naturalness, clarity, pronunciation, pace, and authority before batch narration;
- do not use the rejected Edge TTS 24 kHz / 48 kb/s source chain;
- use a natural synthesis rate and prohibit synthesis speed above `+10%` or final timing correction above `1.10×`; extend runtime instead;
- rewrite for a curious non-specialist: define metallicity, redshift, and dex before using them; explain the question, why the comparison is hard, one concrete result, and what it does not prove;
- explain the sample structure explicitly: five Pollock galaxies define the core redshift 9.3–9.9 result, while GN-z11 extends the direct-temperature sample to six and checks the sign at redshift 10.6; do not flatten these into one unexplained count;
- target 105–125 spoken words per minute, one new technical term or one key number at a time, with explicit recap sentences;
- estimate comprehension with a cold-reader review that must accurately answer: What was measured? Why was lensing avoided? What does a 0.7-dex deficit mean? What is still uncertain?;
- only after voice and script approval, build a 120–180 second local V2 canary with manual captions and audio-first QA;
- visual upgrades and higher resolution remain useful but are not substitutes for intelligible narration.

After user review of the canary, Hwao may coordinate the remaining four V2 builds. Upload, public replacement, unlisting V1, website embed changes, Git landing, build/restart/deploy, and deletion remain separate explicit gates.

## User approval and bounded execution — 2026-07-23T03:40:35Z

The user said “okay go ahead” after the audio-first canary workflow was proposed. This authorized the local review canary, not publication or replacement.

Completed local artifacts:
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/paper-video-v2-audio-canary-20260723T032030Z/Z9_AUDIO_CANARY_NOVA_V2_REVIEW.wav`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/paper-video-v2-audio-canary-20260723T032030Z/Z9_AUDIO_CANARY_SHIMMER_V2_REVIEW.wav`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/paper-video-v2-audio-canary-20260723T032030Z/QA_REPORT.json`

Both candidates pass technical QA at 105–125 WPM using lossless PCM review masters. The full five-video V2 build remains gated on the user's listening selection. No YouTube, website, embed, deployment, or Git mutation occurred.

## Full-batch and YouTube publication authority — 2026-07-23

The user then instructed: “now apply all to the videos and publish on Youtube”. Tori is executing the bounded five-video V2 build using the technically preferred Shimmer canary and publishing five new public YouTube IDs with manual captions.

Scope boundary remains explicit: old V1 videos stay public; website embeds/source, Git, and runtime deployment remain unchanged because those were not included in the instruction.
