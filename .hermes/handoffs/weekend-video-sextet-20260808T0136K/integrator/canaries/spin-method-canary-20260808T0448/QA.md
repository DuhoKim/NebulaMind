# QA — spin-method-canary-20260808T0448 (v8)

## Verdict: **PASS — as a method-only silent canary.**

Authorizes nothing beyond itself. `video_reportable_now` remains `false`.

## Checks

1. **Numeric-source guard**: PASS 11/11, run twice; single-hit evidence unchanged.
2. **Structural hold** (sealed-v8 standard + pass-4 temporal guard): `RESULT HELD` badge
   present top-right on every one of the 11 encoded states — the hold no longer depends on
   individual boundary cards. Static cards mean the badge trivially persists frame-long; if
   this deck ever gains motion, the lane's temporal guard (no fade/entrance may drop the
   badge) applies.
3. **All prior standards carried forward**: parallel readouts, forbidden-term sweep,
   question-first opening, audience citations, equation bridges, dominance definition.
4. **Silence**: single H.264 video stream, 1920×1080 @ 30 fps; no audio stream exists.
5. **Machine QA**: 11 states / 11 cards, all 10 expected cuts, zero unexpected, sha matches
   `hashes.txt`, 118.0 s = 112.0 s + 6.0 s close hold.
6. **Encoded-frame QA**: contact sheet reviewed — badge collision-free everywhere (figure
   headings wrap narrower by design); all states otherwise match v7.
7. **Renderer-copy delta audit**: single bounded change (badge helper + figure-heading
   wrap); pre/post shas recorded; repo `tools/` untouched.

## Known limits

- Character overlay + URL close remain pending Hwao's deck-of-record ruling.
- Concat close-card hold unchanged; re-time if ever narrated.
- mzr-census's 4-second-max evidence-state pacing contract is noted but NOT adopted: it is
  pending that lane's own independent regate, and its clause-aligned reveal design is coupled
  to narration — inapplicable to a silent reading-pace deck without a ruling.
