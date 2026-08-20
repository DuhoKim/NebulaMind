# Feature spec — slides as a DEFAULT part of every audio report

Requested by Duho, 2026-08-20, verbatim: **"can you add graphics or slides on below of the audio
play, like Tori added it on her podcasts?"** then, on seeing a one-off page proposed:
**"i mean let's make it as a default feature for audio report"**.

Owner: **Blanc (OPS)** — this is shared audio-report infrastructure (`nm_status_say.sh`,
`nm_fable_say.sh`, `nm_audio_index.py`, `listen.html`, `archive.html`), not one lane's surface.
Written by Hwao after doing the groundwork below so none of it needs re-deriving.

## What "default" means

Every spoken report — from any Fable, without the speaker doing anything extra — renders with a
slide deck beneath the player on `listen.html` and in `archive.html`. A speaker MAY supply a
richer deck explicitly; if they don't, one is derived automatically.

## Groundwork already done (reuse, don't rebuild)

1. **The house pattern exists** — Tori's `reports/podcasts/index.html` + `slides.js`. Deck format,
   proven and worth keeping verbatim:
   ```js
   window.DECKS = { "<episode-key>": [
     {t: 7.6, k:"kicker", h:"headline", b:["bullet (HTML ok)", "..."],
      g:"generatedGraphicName", img:"file.jpg", attr:"credit"}, ... ]};
   ```
   Renderer: a `timeupdate` listener picks the last slide whose `t` ≤ currentTime; clickable
   time-chips seek. Her CSS variables (`--cyan/--amber/--rose/--green`, `.slide/.kicker/.num`)
   are the established look — inherit them so reports and podcasts feel like one system.
2. **Forced alignment already exists and works on report audio**:
   `scripts/nm_audio_align.py FILE.mp3` writes `FILE.times.json`. **It must be run with
   `/Users/duhokim/.hermes/hermes-agent/venv/bin/python`** — the system python3 lacks
   `faster_whisper` (this cost me a failed run; noted so it costs you none).
   Output shape, verified today on a real report:
   `{"mode":"aligned","coverage":0.9766,"duration":58.464,"n":8,"ends":[3.98,7.62,25.58,...]}`
   → sentence *starts* are `[0] + ends[:-1]`. Coverage <~0.8 or `mode != "aligned"` ⇒ fall back
   to proportional-by-character timing, and say so in the page (never silently fake precision).
3. **Sentence text** is already archived beside the audio as `FILE.txt`.

## The derivation (the default path)

At build time, after alignment: one gateway LLM call (Nous-covered, same route as TTS) that
receives the report text **already split into aligned sentences with their start times** and
returns deck JSON. Binding rules for the prompt, because a slide is a claim:

- **Slides may only restate what the audio says.** No new facts, no numbers absent from the text,
  no interpretation. If a sentence has no number, its slide has no number.
- Group into 4–8 slides; each slide's `t` MUST equal one of the supplied sentence start times
  (never an invented time).
- `h` ≤ ~9 words; 1–3 bullets, each ≤ ~22 words; `k` is a 1–3 word kicker.
- Numbers wrapped in `<span class="num">`, failures in `.bad`, passes in `.ok`.
- Deterministic-ish: temperature low; cache the deck next to the audio as `FILE.deck.json` so a
  rebuild never re-bills or re-rolls a different deck.
- If the call fails: no deck file, and the page renders audio-only exactly as today. **Slides must
  never block archiving** — same rule the aligner already follows.

## The explicit path (optional, for set-piece reports)

`nm_fable_say.sh <fable> "text" --deck deck.json` copies the supplied deck to `FILE.deck.json`
and skips derivation. Same schema. This is how a milestone report gets hand-made graphics.

## Graphics

Start text-only (the deck's `g`/`img` fields optional and unused). Then, when it earns it, a small
shared `report_graphics.js` of inline-SVG generators callable by name — e.g. a progress bar, a
pipeline chain, a pass/fail badge. Keep them data-driven from values the speaker passes, never
decorative fictions.

## Acceptance

- A brand-new report, spoken with no extra flags, appears on `listen.html` with a working deck.
- Re-running the index does not change an existing deck (cache honored).
- A report whose alignment fails still archives, audio-only.
- One end-to-end check on a real past report (suggest today's DESI evening report,
  `20260820T165959-hwao-report.mp3`, whose `.times.json` is already built).
