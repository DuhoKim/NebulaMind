PASS_P2V2_RENDER

# kimi — Phase 2 explainer v2 render gate (second reviewer, fresh one-shot, attempt 2, bounded)

2026-08-19. Lane dir only. Findings-only; nothing edited; this is the only file written
in the lane dir (frame extractions went to /tmp/kimi_p2v2_frames/, outside the lane).
Zero fetches; portal.nersc.gov untouched. Hard-bounded pass: every check below completed
in a few tool calls; nothing was crawled.

Candidate: `build/BHU_PHASE2_EXPLAINER_V2_LOCAL_REVIEW.mp4`

## (1) Custody — PASS

- `shasum -a 256` of the candidate: `db4fcd92f7730618e9f66f6f13303ecec3019ed5da5da9d22a75a6264c671b5f`
  — byte-identical to GPT3_DONE.md's frozen receipt (line 6 / line 19).
- `ffprobe` duration: `475.200000` s — inside the 390–480 s window (matches GPT3_DONE.md).

## (2) ASR audit from stored records only — PASS

No live re-transcription performed; all findings read from ASR_QA.md as stored.

- Coverage: 12 panels (01–12), each headed "transcribed from audio decoded from the exact
  final MP4"; ASR_QA.md line 4 binds the transcripts to the custody SHA
  (`db4fcd92…1b5f`) verified in (1). Stored record belongs to this artifact.
- Cosmetic residual (count 1, quoted): panel 10, `replace` expected `['scherrer']` → ASR
  `['scherer']` — "cosmetic: phonetic ASR rendering of a cited proper name outside
  protected claims" (ASR_QA.md:166, :206).
  Judgment: CONCUR. The Dutta–Scherrer surname is a cited proper name; whisper's one-r
  spelling is an ASR representation variance, not a narration/render fault — the sentence's
  numbers and claim content are intact, and the on-screen attribution spelling lives in the
  visual layer (panel-10 attribution chip, verified legible in check 3). Accepted.
  Contract-bearing residuals: 0.
- Panel 08 repaired two-clause spin sentence, verbatim: present in Expected (ASR_QA.md:128)
  and protected-phrase PASS (:138): "Across all 4 papers, no equation carries the parent's
  spin through the bounce; the collapse papers mention it in exactly 1 sentence: 'It would
  still be valid for a more realistic gravitational collapse of an inhomogeneous and
  rotating fluid.'" ASR (:130) matches after declared numeric normalization.
- Panel 11 caveat sentence, verbatim: present in Expected (:176), ASR (:178), and
  protected-phrase PASS (:186): "One honest caveat: both bounces sit in the Planck regime
  treated classically, and the strict chain awaits external theorist review."
- The 10,000-times heading (R-1): on-screen heading, not narration, so correctly absent
  from ASR transcripts; grep-verified present at VISUALS.md:157 — Heading: "Even the most
  generous signal is 10,000 times below the floor" — exactly the packet-gate R-1 repair.

## (3) Frame audit — PASS (4/4 extractions, legibility judged from these 4 only)

Timestamps derived from STORYBOARD.json planned_seconds (cumulative starts: P01@0, P04@112,
P10@350, P12@433; sum 473 planned vs 475.2 actual — mid-panel picks stay in-panel).
One `ffmpeg -ss <t> -frames:v 1` per frame, four total:

1. P01 @ 17 s — verdict heading large and legible: "The inheritance route now has a
   ceiling, and it stays closed"; verdict chips present ("NO OBSERVABLE SIGNATURE
   SURVIVES", "10,000-100,000 x BELOW THE ALL-GALAXY FLOOR", "THE ROUTE STAYS CLOSED").
   No disclaimer/scope wording anywhere. PASS.
2. P04 @ 132 s (PRD-plot panel) — paper figure large and legible (a/acr vs t/t0 cusp
   curve, axes/ticks readable), attribution chip "Figure 1, arXiv:1111.4595 (author
   version)" present, assertion heading present. PASS.
3. P10 @ 372 s (reality check) — Dutta–Scherrer plot legible with attribution chip
   "Figure 2, arXiv:1006.4166 (author version)"; heading "Ancient helium allows the
   torsion whisper because it cannot hear it"; bound chips ("UP TO 30 × RADIATION AT
   10 MeV") legible. PASS for legibility/attribution.
   UNVERIFIED-AT-GATE: panel 10 is a 44 s animated sequence; this single mid-panel frame
   shows the Figure-2 bound curve only — the He/D/Li comparison figure and any band-ladder
   beat earlier/later in the panel were not sampled (4-extraction cap reached). No
   contradicting evidence; recorded, not chased.
4. P12 @ 455 s (final panel) — verdict heading large and legible: "The strongest
   inheritance route ends at a closed ceiling"; recap rows and both closing verdict boxes
   ("THE STRONGEST ROUTE NOW EXISTS AS A CEILING" / "THE CEILING SAYS THE ROUTE STAYS
   CLOSED") crisp; no placeholder, black frame, or error text. PASS.

Everything else visual (all other panels, animations, transitions) is UNVERIFIED-AT-GATE
by design of the 4-frame cap.

## (4) Disclaimer sweep — PASS

One grep over ASR_QA.md transcripts for `side[- ]interest|programme|personal interest|
scope_label|my[- ]interest`: zero hits. Disclaimer phrasings absent.

## Inherited / skipped

- Cockpit-root check: skipped per instruction; inherited from the v1 gate.

## Tooling note (for future gates)

`search_files` (ripgrep) returned 0 hits for strings present in these files because the
lane lives under a hidden `.hermes/` path, which ripgrep skips by default. All greps above
were run via terminal `grep` on absolute paths. One-line fix for any future gate in this
tree: use terminal grep, not search_files.

## Verdict

Custody byte-matches the builder's frozen receipt; duration in window; stored ASR records
cover all 12 panels of this exact artifact with 0 contract-bearing residuals and 1
accepted cosmetic residual; the repaired P08 two-clause sentence, P11 caveat sentence, and
the R-1 10,000-times heading all verify; the 4 sampled frames are legible, attributed,
verdict-true, and disclaimer-free. One bounded UNVERIFIED-AT-GATE item (panel-10 animated
sequence beyond the sampled frame) is recorded above and is the only unverified surface.
The v2 render passes this gate. This gate authorizes no upload, publication, credit spend,
or public status change by itself.

— kimi, 2026-08-19.
