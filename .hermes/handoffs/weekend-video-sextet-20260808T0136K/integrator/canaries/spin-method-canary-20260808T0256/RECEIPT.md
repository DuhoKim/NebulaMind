# RECEIPT — spin-method-canary-20260808T0256 (v3)

Seat: `yui-video-integration`. Rendered 2026-08-08 02:56–03:00 KST (stamps from `date`).
Freeze in force: unchanged — `spin-method-canary-pass1-20260808T0153K`.

## What this is

Version 3 of the silent, method-only galaxy-spin visual canary. **v1 (0204) and v2 (0235) are
preserved unchanged.** v2 remains the parallel-readouts correction record; v3 supersedes it as
the current canary.

## The one change, and its evidence

The spin lane's independent audit chain completed (`INDEPENDENT_QA.md`): the v3-proposal
adversarial review's sole blocker was a persistent visible "parity" header, and the lane's v5
PASS required **zero visible forbidden audience terms** — upholding the negation-association
finding this seat had held as a watch-item since pass 5. Applied here:

- title heading → "Galaxy spin handedness — the method, before the verdict" (was
  "Galaxy spin parity — …");
- schematic boundary line → "Whether stored directions are as-seen or corrected-back is
  UNRESOLVED — until the convention is stated, the measurement's meaning is not recoverable"
  (was "… no sky, dipole, or parity meaning may be attached");
- automated sweep over all card text: zero occurrences of parity/dipole/cosmology/GRB/SN Ia/
  dark-energy/quasar/H0/DESI/Ganalyzer as visible audience terms (one case-insensitive hit on
  "designed" containing "desi" — false positive, recorded for honesty).

All counts, figures' geometry, card structure, and every other statement are unchanged from v2.
Sources re-pinned sha-identical to the freeze (`ed97758a…`, `fc73061f…`).

## Verification

- Numeric-source guard: PASS 11/11 twice; evidence single-hit on the correct lines.
- Machine QA (`audit_canary.py`): PASS — 11 states, all expected cuts, none unexpected, single
  silent H.264 stream, sha `2c803bba…` matches `hashes.txt`, +6.0 s concat close hold.
- Encoded-frame QA: both changed frames (title, schematic) verified at full resolution from the
  encoded MP4; remaining states match v2.

## Gates untouched

No TTS, no Git, no upload/publication, no shared-tool or public-asset writes.
