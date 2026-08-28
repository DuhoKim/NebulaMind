# QA — spin-method-canary-20260808T0235 (v2)

## Verdict: **PASS — as a method-only silent canary.**

Authorizes nothing beyond itself. `video_reportable_now` remains `false`.

## Checks

1. **Numeric-source guard**: PASS 11/11, run twice; evidence audit single-hit on the semantically
   correct lines. No flags.
2. **Semantic scope**: identical to v1's card→allowed_scope mapping except card 5, which now maps
   to "frozen source/sample funnel" **more faithfully** — it presents the three readouts exactly
   as `T1_FUNNEL.json` structures them (parallel siblings), where v1 added an unsupported
   sequential-nesting claim. Forbidden-scope sweep unchanged: no T3/T4 material, no result
   values, no dipole/parity/cosmology, no excluded pointers.
3. **Silence**: single H.264 video stream, 1920×1080 @ 30 fps; no audio stream exists.
4. **Machine QA** (`audit_canary.py`): 11 states / 11 cards, all 10 expected cuts within 0.35 s,
   zero unexpected cuts, sha256 matches `hashes.txt`, duration 114.0 s = 108.0 s + 6.0 s concat
   close hold.
5. **Encoded-frame QA**: corrected card 5 verified at full resolution from the encoded MP4 —
   parallel-branch geometry, amber `PARALLEL READOUTS — NOT A SEQUENTIAL FUNNEL` banner, per-readout
   accounting line, and "A NOT computed" statement all legible; remaining states match v1.

## Known limits

- The figure's internal title line duplicates the card heading (cosmetic; consider dropping the
  in-figure title in a future cut).
- Same concat close-card hold as v1; benign for a silent cut, re-time if ever narrated.
- Card durations remain silent-reading floors.
