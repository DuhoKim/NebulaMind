# Synthesis brief — R1–R3 from the three-way scientific-presentation consult

Filed 2026-08-08 ~14:00 KST at Duho's instruction ("dispatch the synthesis brief with R1-R3 to
Lana"). Source consults, all independent, in
`.hermes/handoffs/video-scipres-consult-20260808T0108K/`:
`LANA_SCIPRES_REVIEW.md`, `GORU_SCIPRES_REVIEW.md`, `YUI_SCIPRES_REVIEW.md`.

**Owner of this brief: Lana (`lana-overhaul` seat).** R1–R3 are Lana's own numbering.

## Authority and boundaries — read first

1. `HWAO_OVERHAUL_ORDER.md` is FROZEN and supersedes this brief wherever they differ. This is
   advisory input to the overhaul spec, not a competing order.
2. **Single-writer rule stands.** `status.json` gives the `integrator` seat exclusive ownership of
   `tools/nm_paper_video.py`, `nm_paper_plot.py`, `nm_paper_narrate.py`, `nm_paper_tts.py`.
   **Lana must not edit those files.** Deliver R1–R3 as an implementable spec the integrator seat
   executes. This brief exists because Duho asked for the consult findings to reach Lana, not to
   re-open writer ownership.
3. Scientific boundary unchanged: `video_reportable_now: false`,
   `BLOCK_SUBSTANTIVE_RESULT_RENDER; ALLOW_METHOD_ONLY_CANARY`. Nothing below authorizes a result
   claim. Per Lana's own amendment: "handedness", never "parity", in audience-facing text.

## Why these three, and what is already covered

Three independent reviews converged on one diagnosis: **the prior Deep Research consult fixed the
narration; nobody fixed the screen.** All three explicitly disagree that narrative structure alone
produces a scientific look. The HWAO order already bans the rejected grammar (no character, no
giant standalone-number card, no paragraph/quote cards, no internal filenames as citations, no long
frozen holds). R1–R3 are the **positive implementation spec** the order does not yet fix in
renderer terms — what to draw instead, and how to fail the build when it is wrong.

## R1 — Split screen text from narration (cheap; highest impact)

The single biggest register error: the narration script *is* the card heading + body verbatim, so
every on-screen paragraph is exactly what the voice says. Conference slides are terse noun phrases,
numbers and marks; the sentences belong to the speaker. When screen == voiceover the viewer files
it as "explainer video", never "talk". This is why applying BLUF/stakes/roadmap to the script
changed nothing visible — and it is newly load-bearing now that narration is authorized for this
method-only cut, because voice + identical on-screen prose is the exact failure mode.

Spec: add an optional per-card `screen` field — 2–4 terse lines or a stat, roughly <= 18 words
total — rendered **instead of** `body`. Narration keeps reading `heading` + `body`, so the narrate
tool is unchanged. Fallback when `screen` is absent: heading + extracted numerals only. Reversible
per card.

## R2 — Slide furniture (cheap)

No slide numbers, no running footer, no section markers, no date/authors on the title card. Every
scientific deck carries this; its absence is why each card reads as a floating quote-card. Goru
reached the same conclusion independently and framed it as a LaTeX Beamer footer.

Spec: persistent footer — short title left, "NebulaMind Lab · 2026-08" centre, "n / N" right (the
renderer already knows `idx` and `len(cards)`); thin top progress bar (x proportional to idx/N);
small-caps section tag top-right driven by a per-card `section` field. Title card gains date and
data credit ("data: Galaxy Zoo 1 — Land et al. 2008") as structured lines, not a paragraph.

Note this **answers Kun's dead-air objection**: it delivers the roadmap the Deep Research consult
prescribed as a persistent cue, with zero divider cards. `render_section`'s journal-style progress
rail is currently dead code — no `section` cards survive in the shipped storyboards — so the
roadmap presently exists in narration only. Yui independently recommended against restoring
full-screen section cards for the same dead-air reason.

## R3 — Restyle the plots for video (moderate; mostly `nm_paper_plot.py`)

Figures are matplotlib defaults, not video-typeset. Evidence from the 1903 cut: tick/axis type ~20px
at 1080p (illegible on a phone); the "pre-registered REVERSES bar" annotation clipped at the right
frame edge with its value missing; a caption footnote truncated mid-token ("LANA_T3_REDERIV…");
card heading duplicated as the internal plot title; three-line orange disclaimer captions reading as
debug output; and `drawn from spin-parity-census-…/T3_READING.json` repo paths on screen. Goru and
Yui both flagged the on-screen repo paths as the strongest "internal artifact, not presentation"
tell.

Spec: one shared rcParams — 28–34pt ticks/labels; no internal `title` (the card heading is the
title, which also kills the duplication); annotation placement inside the axes with wrapping;
captions cut to <= 2 short lines in one neutral gray; multi-clause orange disclaimers reduced to one
clause ("classifier bias study — not a handedness result"); provenance shortened to
`data: T3_READING.json`, with the full lane path moved to the video description.

**Build gate:** `render_figure` must *fail* on caption overflow exactly as the numeric guard fails
on unverified numbers. Clipped text is a rendering bug promoted to a review gate — the f15 clip
shipped precisely because nothing failed.

## Deliverable

`reviews/LANA_R1R3_SPEC.md` — R1–R3 as an integrator-executable spec (field names, draw order,
failure conditions, and the acceptance check for each), cross-referenced to the HWAO order so the
integrator can see at a glance where this adds detail versus where the order already rules.

Explicitly out of scope for this brief: Lana's R4–R9 (equation/table/stats card kinds, funnel
schematic, character demotion, per-line builds, regenerating the sibling videos) and Yui's
hash-bound build receipt. They are recorded in the source reviews and several are already implied
by the HWAO order; do not expand scope without Hwao.
