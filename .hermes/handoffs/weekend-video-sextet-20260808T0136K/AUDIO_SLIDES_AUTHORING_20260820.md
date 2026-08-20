# Authoring slides for your own audio reports (Hwao, Tori — from Blanc)

Duho, 2026-08-20, verbatim: **"i think each Fable, now Opus should make it not
you, since they know better than you."** He is right — I do not know which
graphic matters in your report. So: **you author the deck, I render it.**

He also said, on seeing my first text-only slides: *"i expected more like
graphics, such as real images when it mentions image data."* Bullets that
restate the caption are not the point. When your report talks about galaxy
cutouts, the slide should show **the actual cutouts**.

## How to attach a deck

```
nm_fable_say.sh <hwao|tori> --deck /path/to/deck.json "your report text"
```

That is all. Alignment, rendering, archiving, and the listen page happen
automatically. Without `--deck` you still get an auto-derived text deck (the
fallback), but yours will always be better.

## Deck format (Tori's podcast DECK schema, unchanged)

```json
{"slides": [
  {"t": 7.62, "k": "kicker", "h": "headline max ~9 words",
   "b": ["bullet, HTML allowed, max ~22 words"],
   "g": {"kind": "cutgrid", "n": 12, "cols": 6}}
]}
```

- `t` = seconds into the audio. **Approximate is fine** — I snap each slide to
  the nearest real sentence start from forced alignment (and note the snap).
- `k` kicker (1-3 words), `h` headline, `b` 1-3 bullets.
- Inline spans: `<span class="num">` for numbers, `.ok` for passes, `.bad` for
  failures. They inherit the podcast palette (amber / green / rose).
- 4-8 slides reads best.

## Graphics available now (`g` directive — real data only)

| directive | what it draws |
|---|---|
| `{"kind":"cutgrid","n":12,"cols":6}` | grid of **real galaxy cutouts** from this run's verified tensors (DECaLS DR10 south, asinh stretch, deterministic pick) |
| `{"kind":"cutout"}` | one real cutout, enlarged |
| `{"kind":"progress","done":5300,"total":60308,"label":"bricks"}` | SVG progress bar |
| `{"kind":"badges","items":[["receipts pass",true],["manifest bug",false]]}` | pass/fail chips |

You can also supply your own art directly: `"img": "graphics/yourfile.png",
"attr": "credit line"` (drop the file in `reports/status-audio/graphics/`).

**Ask me for more generators.** A sky-coverage map, a gate-chain diagram, an
MZR scatter, a torsion schematic — if it can be drawn from data that exists on
disk, I will add it to `nm_report_graphics.py` and you call it by name.

## The two rules I enforce mechanically (not by trust)

1. **A slide may only restate what the audio says.** Every number in a slide —
   including numbers inside a `progress` or `badges` graphic — must already
   appear in your spoken text. Anything else is dropped with a note. I tripped
   this myself within ten minutes: I set a progress bar total of 60,308 when the
   audio only said 5,300, and the graphic was correctly discarded.
2. **Nothing is faked.** If a graphic's source data is missing, the slide keeps
   its text — you never get a placeholder that looks like data. If deck building
   fails entirely, the reading still archives, audio-only. Slides never block
   archiving.

## Practical note

Write the numbers you want on screen **into the spoken text**. If you want the
brick total on a progress bar, say the total out loud. That constraint is the
feature: the slides can never tell Duho something the audio did not.

Files: `nm_deck_build.py` (authored path), `nm_deck_derive.py` (fallback),
`nm_report_graphics.py` (generators), `nm_report_postprocess.sh` (the chain).
