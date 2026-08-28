# Candidate — spin-parity-census, alloy recut (canary #1)

Built 2026-08-08 01:49 KST by Hwao acting as integrator. **Local candidate only. Not uploaded, not
published, not wired anywhere.**

## What changed vs the published cut

The published video (`uch2gFhtd3g`) is narrated by **edge-tts Andrew**, cut while the Nous account
was at $0.00. Duho then ruled: *"go back to alloy for consistency"* — the channel's other five
videos use alloy. Nous credits landed ($99.99, gateway HTTP 200 verified), so this recuts all 16
cards to **alloy via the managed gateway**.

Storyboard is UNCHANGED — same 16 cards, same wording, same figures. Narration only.

## Route + the calibration

`gpt-4o-mini-tts` · voice `alloy` · **speed 1.18** · mono MP3 24 kHz.

Speed is calibrated, not chosen: at speed 1.0 this model reads ~18.5 s where the channel's shipped
alloy track for the identical script is 15.59 s. Measured on that script — `1.0→18.46s`,
`1.15→15.10s`, `1.19→16.03s`, `1.25→14.66s` — with ~±0.5 s run-to-run variance. Left at 1.0 the
video would grow ~19% and stop matching the channel.

## Facts

- MP4: `spin-parity-census-narrated-20260808T0149.mp4`, 28,637,729 bytes
- **243.30 s (4 m 03 s)**, 1920×1080, h264 + aac mono 24 kHz, mean volume −20.4 dB
- 16/16 cards passed the numeric-source guard at mux time
- Narration total 223.4 s across 16 tracks
- Previous alloy set backed up to `_audio_spin-parity-census/_backup_20260808T0147/`

## Comparison

| Cut | Voice | Duration |
|---|---|---|
| `…20260807T1903` (published as `uch2gFhtd3g`) | edge Andrew +25% | 237.3 s |
| **`…20260808T0149` (this candidate)** | **alloy 1.18** | **243.3 s** |

+6 s: alloy at 1.18 sits slightly slower than Andrew at +25%. Within the ±0.5 s/card TTS variance
band, not a pacing regression.

## Not done, deliberately

No upload. No replacement of the published cut. No `paperVideos.ts`, no cockpit, no Git. Those are
closed gates under `HWAO_WEEKEND_ORDER.md` §7 and need Duho's fresh approval.
