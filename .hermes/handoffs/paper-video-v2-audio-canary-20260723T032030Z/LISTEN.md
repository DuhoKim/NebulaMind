# Listen to the flagship V2 audio canaries

Marker: `NEBULAMIND_Z9_AUDIO_CANARY_LISTENING_GATE_V2`

These are local, lossless, loudness-normalized review files. They use the same 101-word plain-English script, OpenAI `gpt-4o-mini-tts`, and 0.80× provider speed. No post-synthesis time compression was used.

## Candidate A — Nova

```sh
afplay /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/paper-video-v2-audio-canary-20260723T032030Z/Z9_AUDIO_CANARY_NOVA_V2_REVIEW.wav
```

- Duration: 52.30 seconds
- Pace: 115.9 WPM
- Loudness: -16.17 LUFS
- True peak: -1.90 dBTP

## Candidate B — Shimmer

```sh
afplay /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/paper-video-v2-audio-canary-20260723T032030Z/Z9_AUDIO_CANARY_SHIMMER_V2_REVIEW.wav
```

- Duration: 54.18 seconds
- Pace: 111.9 WPM
- Loudness: -16.11 LUFS
- True peak: -1.96 dBTP

## What to judge

1. Does the voice sound clearly female, natural, and pleasant enough for all five papers?
2. Can you understand the explanation without reading the paper?
3. Is the pace calm enough, or still rushed?
4. Are “metallicity,” “gravitational lensing,” and “zero point seven dex” pronounced acceptably?
5. Would you prefer Nova, Shimmer, or neither?

Technical QA slightly favors Shimmer because it is slower and produced a lower raw independent-ASR error rate. That is not a substitute for your listening decision.

## Boundary

The full V2 video build remains paused at this listening gate. The five current YouTube videos and website embeds were not changed.
