# QA — spin-method-canary-20260808T0256 (v3)

## Verdict: **PASS — as a method-only silent canary.**

Authorizes nothing beyond itself. `video_reportable_now` remains `false`.

## Checks

1. **Numeric-source guard**: PASS 11/11, run twice; single-hit evidence on `rows_parsed`,
   `N_tie`, `probed`.
2. **Forbidden-term sweep** (new in v3, standard upheld by the spin lane's completed
   independent audit): no visible parity/dipole/cosmological/GRB/SN Ia/dark-energy/quasar/H0/
   DESI/Ganalyzer terms in any heading, body, or figure text. The boundary is stated neutrally
   without naming excluded contexts.
3. **Semantic scope**: card→allowed_scope mapping unchanged from v2 (parallel-readouts card
   retained); title rename does not alter any claim.
4. **Silence**: single H.264 video stream, 1920×1080 @ 30 fps; no audio stream exists.
5. **Machine QA** (`audit_canary.py`): 11 states / 11 cards, all 10 expected cuts within
   0.35 s, zero unexpected, sha256 matches `hashes.txt`, 114.0 s = 108.0 s + 6.0 s close hold.
6. **Encoded-frame QA**: title and schematic frames verified at full resolution from the
   encoded MP4; contact sheet covers all 11 states.

## Known limits

- Character overlay and URL close remain (house canary style); the spin worker's PASS deck
  omits both — that structural choice is escalated to Hwao, not resolved here.
- Readouts figure's internal title still duplicates the card heading (cosmetic carry-over).
- Same concat close-card hold; re-time if ever narrated.
