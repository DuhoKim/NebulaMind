# YUI Flow Veo native voiceover test 01 — PASS WITH MIXED-AUDIO CAVEAT

Packet: `studio-simultaneous-web-viability-test-20260714T034720Z`
Actor: Yui, Flow operator on Mac Studio
Authorization: direct Duho approval in the active session
Completed UTC: `2026-07-14`

## Bounded scope

Exactly one Flow generation was authorized and submitted. No retry and no follow-on narration generation occurred.

Verbatim submitted prompt:

> Cinematic slow push through a glowing cyan-and-gold spiral galaxy in deep space. A warm, calm, professional female documentary narrator delivers a clean studio voiceover with no on-screen speaker: "NebulaMind. An astronomy encyclopedia written entirely by artificial intelligence." Subtle cosmic ambience kept low under the voice.

## Flow configuration and custody

- project: `a22b5b61-833d-4e62-857b-4a7030b93bfa`
- model: `Veo 3.1 - Quality`
- Lite used: no
- output count: `1x`
- duration: `8s`
- aspect ratio: `16:9`
- displayed cost: `100 credits`
- separate audio switch exposed by Flow: no; Veo native audio was prompt-driven
- final pre-submit media baseline: 16
- submit UTC: `2026-07-14T13:27:13Z`
- account-submission lease: `L00263`
- submit events: 1
- generation retries: 0
- immediate card state: provisional `Failed`
- account lease released: `2026-07-14T13:27:18Z`
- page-scoped challenges: 0
- target drift: 0

## Settled result and saved artifact

- media id: `c06e3a84-377a-44c6-b070-f26b8bc060bc`
- detail prompt match: exact
- final state: playable, readyState 4
- duration: 8.000 seconds
- resolution: 1280x720
- video: H.264, 24 fps
- audio: AAC, stereo, 48 kHz, approximately 140 kbps
- saved path: `/Users/duhokim/HermesOps/scripts/clips/narration/vo_test_01.mp4`
- overwrite used: false
- bytes: 7,028,410
- SHA-256: `135d485f99e1966fd6739efad20748fe0a01155972b372ae31a8a4ea535e9d23`

## Credits

- live pre-submit balance: 23,538
- live post-settlement balance: 23,438
- observed delta: 100 credits
- displayed cost: 100 credits
- unexplained delta: zero

## Audio evidence

OpenAI Whisper transcription of the full audio:

> Nebula Mind, an astronomy encyclopedia written entirely by artificial intelligence.

The same exact transcription was produced from the stereo mid/center extraction. Whisper returned one English segment spanning 0.0–7.0 seconds.

Side-channel extraction was 8.6 dB quieter than the center/mid channel and produced a degraded transcription, supporting that the intelligible narrator is center-dominant rather than buried in the stereo ambience.

Signal measurements:

- full mix mean/max: -18.3 / -0.9 dB
- center/mid mean/max: -21.3 / -3.9 dB
- side mean/max: -29.9 / -11.5 dB
- center-to-side difference: 8.6 dB
- center-to-side power ratio: approximately 7.24:1
- clipping observed: no; peak remained below full scale

Spectrogram and waveform review showed one continuous speech-like utterance, no visible overlapping second speech pattern, no clipping plateau, and a lower-level broadband/ambient bed rather than large competing music peaks. These visual/audio-signal checks cannot prove biological speaker identity or provide a perfect diarization guarantee.

## Requested judgments

### (a) Does the audio clearly speak the line?

**Yes, high confidence.** Full-mix and center-channel Whisper both recovered the complete intended sentence without omitted or substituted content words.

### (b) Is it a single clean narrator voice, cleanly extractable and not buried under music?

**Yes for practical use under infographic slides, with one caveat.** Evidence supports one center-dominant narrator and no second/overlapping voice; the voice is intelligible and not buried under music. The file is not a pristine dry voice stem: subtle cosmic ambience is baked into the same AAC mix, and some speech energy remains in the stereo side channel. Using the full audio track under slides should work cleanly. Producing a voice-only stem would require light source separation or denoising.

### (c) How close is the spoken wording to the script?

**Effectively exact.** Raw character similarity is 98.18%. After treating Whisper's `Nebula Mind` tokenization as the brand word `NebulaMind`, normalized script tokens match exactly. The only differences are transcription formatting: `NebulaMind` became `Nebula Mind`, and Whisper used a comma where the script has a period. No spoken content word was omitted, added, or substituted.

## Gate

This one-clip native voiceover test passes for narration-under-slides use. No additional narration clips were generated. Duho/Hwao must decide whether the baked-in low cosmic ambience is acceptable before authorizing the remaining narration set.

YUI_FLOW_VEO_NATIVE_VOICEOVER_TEST01_PASS_20260714
