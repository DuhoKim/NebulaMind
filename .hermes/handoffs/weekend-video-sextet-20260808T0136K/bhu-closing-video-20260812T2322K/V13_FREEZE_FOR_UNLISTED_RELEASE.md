# BHU V13 — exact freeze for gated unlisted release

Status: `FROZEN_V13_READY_FOR_GATED_UNLISTED_RELEASE`

- Candidate: `/Users/duhokim/HermesOps/cockpit/videos/bhu-closing-record-v13-local-20260813T0932Z.mp4`
- SHA-256: `060764c04ba095637cb484237064d501e097b1c326d7bf8b389a22292f96d9c2`
- 14,795,951 bytes · 402.000 s · 12,060 frames · 1920×1080 at 30 fps
- Streams: H.264 video, AAC mono audio, one default English mov_text subtitle stream

## Gates

- Pre-render exact-current seats: Lana PASS · Goru PASS · Kun PASS
- Encoded QA: 45/45 PASS
- Real decoded-AAC per-card WPM: 142.037–142.408; all inside 135–150
- Embedded subtitle stream extracted; 64 cue payloads and timings match source SRT/VTT and delivery sidecars.
- Card 05 decoded-frame preflight: open fading 95.4% gradient; no forbidden endpoint or scaled terminus.
- Conditional ILLUSTRATION tag not triggered: generated regions are stylized, non-quantitative metaphors and not observations.

## Release boundary

Unlisted upload only. Public visibility remains unauthorized. The prior unlisted V11 must remain untouched until V13 is uploaded, its caption track is inserted, and serving is verified.

- Freeze JSON: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-closing-video-20260812T2322K/V13_FREEZE_FOR_UNLISTED_RELEASE.json`
- The JSON enumerates the exact source, gate, renderer, QA, caption, generated-asset, candidate, and predecessor hashes.
