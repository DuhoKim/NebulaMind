# QA — spin-method-canary-20260808T0325 (v5)

## Verdict: **PASS — as a method-only silent canary.**

Authorizes nothing beyond itself. `video_reportable_now` remains `false`.

## Checks

1. **Numeric-source guard**: PASS 11/11, run twice; `display_citation` does not participate in
   verification — the retained `source` paths do, so the guard's coverage is unchanged.
2. **Audience-citation standard** (sealed v8 + three lane requests): no internal filenames,
   repository paths, or hashes visible in any audience frame; every sourced card carries a
   human-readable citation; verification identity lives in `hashes.txt`.
3. **Question-first opening, forbidden-term, and parallel-readouts standards**: carried
   forward from v4/v3/v2 unchanged.
4. **Silence**: single H.264 video stream, 1920×1080 @ 30 fps; no audio stream exists.
5. **Machine QA**: 11 states / 11 cards, all 10 expected cuts, zero unexpected, sha matches
   `hashes.txt`, 116.0 s = 110.0 s + 6.0 s close hold.
6. **Encoded-frame QA**: citation footers verified at full resolution from the encoded MP4;
   remaining states match v4.
7. **Renderer-copy delta audit**: single bounded change (footer citation logic); previous sha
   equalled the freeze-pinned repo renderer; delta recorded in RECEIPT + hashes.txt; repo
   `tools/` untouched.

## Known limits / queued corrections

- Equation card still lacks the one-A-per-readout bridge; "dominance" still undefined on
  screen — next in queue.
- Character overlay + URL close remain pending Hwao's deck-of-record ruling.
- Concat close-card hold unchanged; re-time if ever narrated.
