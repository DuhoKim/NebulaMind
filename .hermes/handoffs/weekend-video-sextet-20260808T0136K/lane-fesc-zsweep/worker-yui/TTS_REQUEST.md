# Conditional TTS request — not ready to execute

Owner: Hwao.

Worker action: no TTS invocation, no audio creation, and no narration manifest.

## Current state

`NOT_READY` — the shared storyboard/plot still need the two semantic corrections, and no integrated silent canary has passed encoded-frame review.

## Unblock conditions

1. Hwao accepts and integrates the closure-envelope and no-SFRD-tail corrections.
2. Hwao renders an official silent canary.
3. Full-resolution encoded QA passes for the crossing, keyed percentages, scenario, limitation, and closing states.
4. Any narration edit after the current proposal receives fresh scientific review.

## Requested route after unblock

- provider: Nous managed TTS
- voice: Alloy
- speed: 1.18
- proposed copy source: `STORYBOARD_PROPOSAL.json:/scenes/*/narration_proposal`
- proposed storyboard container SHA-256: `49db67e9c565eef6c8ec0f53bf348e8ecf1f581168507ce6eb2fa24c4a44c182`
- narration-only SHA-256: `5bd6350f80160b12aa5202383bf90dbff6771440615e8263aa4870f5d0953a55` over UTF-8 scene narration values in order, each terminated by `\n`
- proposed timeline: 98 seconds
- proposed word count: 200
- arithmetic delivered pace: approximately 122 WPM

## Required post-TTS verification

- audio stream exists and uses the intended narration;
- no clipped waveform or audible truncation;
- peak and integrated loudness recorded;
- audio duration fits every scene without rushed tails or premature transitions;
- final A/V duration mismatch is within the integrator's accepted bound;
- full-resolution frames are re-extracted from the encoded narrated MP4;
- no upload or public replacement occurs without a separate gate.
