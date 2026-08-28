# RECEIPT — spin-method-canary-20260808T0448 (v8)

Seat: `yui-video-integration`. Rendered 2026-08-08 04:48–04:52 KST (stamps from `date`).
Freeze in force: unchanged — `spin-method-canary-pass1-20260808T0153K`.

## What this is

Version 8 of the silent, method-only galaxy-spin visual canary. **v1–v7 preserved unchanged.**

## The one change, and its evidence

**Persistent `RESULT HELD` status badge on every frame.** Sealed-v8 standard under-extracted in
pass 8: the worker deck's final audit confirms "persistent `RESULT HELD`" on all frames, and
the lane's pass-2/pass-4 encoded audits fault the held 0149 candidate precisely because its
hold status is subordinate rather than structural ("no dominant held boundary"; "a small
caveat cannot carry the gate"). The pass-4 audit's temporal guard makes the same requirement
explicit for any motion integration. This canary's boundary previously lived on three cards
only; it is now structural on all 11.

Implementation:

- **Bounded renderer-copy edit #2** (allowed by DELEGATION): `paste_status_badge()` draws an
  amber pill top-right when a card carries `status_badge`; figure-card headings wrap narrower
  when a badge is present so text never collides. Pre-edit copy sha `68240834…` (pass-9 state)
  recorded in `hashes.txt`; repo `tools/` untouched, Git gate closed.
- Storyboard: `"status_badge": "RESULT HELD"` on all 11 cards. No other text changed from v7.

## Verification

- Numeric-source guard: PASS 11/11 twice.
- Machine QA (`audit_canary.py`): PASS — 11 states, all expected cuts, none unexpected, single
  silent H.264 stream, sha `7baaa40e…` matches `hashes.txt`, 118.0 s = 112.0 s + 6.0 s close
  hold.
- Encoded-frame QA: badge verified present and collision-free on all 11 states from the
  encoded contact sheet, including both figure cards and all character cards.

## Gates untouched

No TTS, no Git, no upload/publication, no shared-tool or public-asset writes.
