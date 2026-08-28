# QA — spin-method-canary-20260808T0204

## Verdict: **PASS — as a method-only silent canary.**

This verdict authorizes nothing beyond itself: not narration, not publication, not a result cut.
`video_reportable_now` remains `false`; the freeze decision
`BLOCK_SUBSTANTIVE_RESULT_RENDER; ALLOW_METHOD_ONLY_CANARY` remains in force.

## Checks performed

**1. Numeric-source guard** — PASS (11/11 cards), run twice via the candidate-workspace renderer
copy (`--check`). Evidence audit read, not just the exit code: every matched number is a single
hit on the semantically correct line (`rows_parsed`, `N_tie`, `probed`). No `<-- CHECK` flags.

**2. Semantic scope audit (manual — the guard cannot do this).** Card → `allowed_scope` mapping:

| # | Card | Scope item |
|---|---|---|
| 1 | title | (no claim) |
| 2 | "result is not yet reportable" | unresolved-result boundary |
| 3 | rules frozen before fetch | frozen source/sample funnel |
| 4 | 667,944 rows parsed | frozen source/sample funnel |
| 5 | funnel figure | frozen source/sample funnel |
| 6 | A = (N_CW − N_ACW)/(N_CW + N_ACW), value withheld | predeclared asymmetry equation |
| 7 | mirroring schematic | handedness convention and alignment schematic |
| 8 | 36/36 column alignment | handedness convention and alignment schematic |
| 9 | controls designed in advance, outcomes withheld | predeclared bias-control design |
| 10 | why the verdict is absent (limit card, amber bar) | unresolved-result boundary |
| 11 | close: method first | unresolved-result boundary |

Forbidden-scope sweep: no T3/T4 numbers or outcomes, no MIXED, no significance, no
dipole/parity/cosmology, no GRB/SN Ia/dark-energy/quasar/H0, no black-hole-universe, no
DESI/Ganalyzer, nothing from the excluded user note. Two guard-invisible issues were found by this
audit and fixed **before** render (monochrome-control mention; blocker count) — recorded in
RECEIPT.md.

**3. Silence** — ffprobe shows exactly one stream: H.264 video, 1920×1080, 30 fps, yuv420p.
No audio stream exists, so nothing can be un-muted downstream. Mean volume: not applicable.

**4. Encoded-frame QA** — contact-sheet.jpg (11 frames, chronological) reviewed at render time:
no blank frames, no label collisions, figures legible, source footers present, limit card carries
the amber accent, boundary appears by card 2 (~16 s in) and again at the close.

**5. Figure QA** — both PNGs redrawn deterministically from the pinned `T1_FUNNEL.json`
(sha `ed97758a…`, byte-identical to the freeze). Funnel shows sample counts only, with an explicit
on-figure statement that A is not computed; per-rung CW/ACW accounting is text-only (no comparative
bars). Schematic spirals are exact mirror images by construction; the unresolved stored-direction
convention is stated on the figure itself. Quarantined figures untouched.

**6. Structure (Duho's bar)** — stakes and boundary up front (card 2 ends ~16 s), assertion
headings on every figure, no divider cards, ends on the boundary statement, not on caveats.

## Known limits

- Duration 114.0 s vs storyboard 108.0 s: the concat demuxer's repeated final entry holds the
  close card ~6 s. Cosmetic for a silent canary; flagged for any future narrated cut where card
  timing matters.
- Card `seconds` were chosen for silent reading pace. A narrated sibling (if ever authorized)
  re-times from audio and would need its own QA.
- The character overlay is the locked series reference (decoration only, faded, no information).
