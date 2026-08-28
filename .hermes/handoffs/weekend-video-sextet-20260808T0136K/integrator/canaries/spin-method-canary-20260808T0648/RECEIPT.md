# RECEIPT — spin-method-canary-20260808T0648 (v9)

Seat: `yui-video-integration`. Rendered 2026-08-08 06:48–06:55 KST (stamps from `date`).
Freeze in force: unchanged — `spin-method-canary-pass1-20260808T0153K`.

## What this is

Version 9 of the silent, method-only galaxy-spin visual canary. **v1–v8 preserved unchanged.**

## The one change, and its evidence

**The `RESULT HELD` capsule moved fully inside the inner-5% safe rectangle** (x 96..1824,
y 54..1026 at 1920×1080). Spin's pass-9 safe-area audit established the guard quantitatively
and found even their sealed v8 deck violating it ("move the full header and complete RESULT
HELD capsule inward") — an upheld finding that applied identically here: the v8 canary's
capsule reached x=1860 and started at y=44, breaching the rectangle on two sides.

Implementation: **bounded renderer-copy edit #3** — badge coordinates only (right edge
W−100=1820 ≤ 1824; top y=58 ≥ 54). Card text, figures, and all other pixels unchanged from
v8. Pre-edit copy sha `ead4fd5c…` recorded in `hashes.txt`; repo `tools/` untouched.

## Verification (guard clause-8 re-run stack)

- Numeric-source guard: PASS 11/11 twice.
- Machine QA (`audit_canary.py`): PASS — 11 states, all cuts, silent single stream,
  sha `6d81e183…` matches `hashes.txt`, 118.0 s.
- **Safe-area**: 5% symmetric crop frame verified — complete capsule (border included)
  survives inside the crop.
- **360p acceptance**: re-run — capsule legible on 11/11 downscaled states at the new
  position.
- **Five-mode color-vision**: sheets regenerated (`color_vision/`); design unchanged in color
  terms from v8's PASS (text/border carry the gate).
- Left accent bar and character overlay remain in the outer band as decorative-only, which
  the guard explicitly permits.

## Gates untouched

No TTS, no Git, no upload/publication, no shared-tool or public-asset writes.
