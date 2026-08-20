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
| `{"kind":"skymap"}` | **DESI**: accepted bricks in RA/Dec over the 208,407 parent galaxies, with the RA-ordered transfer front labelled on the image (it is not a missing region) |
| `{"kind":"failstrip"}` | **DESI**: outcome counts from receipts.jsonl *including the zeros* — "no digest mismatch so far", never "verified perfect" |
| `{"kind":"throughput","hours":24}` | **DESI**: bricks/hour from receipt timestamps; flat hours are the frozen transfer window, and no ETA is printed |

The three DESI graphics read `receipts.jsonl` themselves, so their numbers come
from disk rather than your script — they are exempt from the spoken-number rule
and carry their own count and timestamp, so a screenshot cannot age silently.
Built to Hwao's spec in `DESI_GRAPHICS_ANSWER_20260820.md`; the mosaic stays
deterministically unsorted on purpose (sorting cutouts by χ or committee state
would make a picture of a blinded result).

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

## Speaking numbers

**Fixed 2026-08-20 (thanks Hwao):** "two thousand **and** forty seven" used to be
split into `2,000 and 47`, so the caption never contained 2,047 and a slide
claiming it was correctly refused — Hwao lost 4 of 6 slides to this. The
normalizer now absorbs `and` inside a number when a scale word precedes it, so
all of these are safe:

| you say | caption shows |
|---|---|
| two thousand and forty seven | `2,047` |
| two hundred and fifty | `250` |
| one hundred and twenty three thousand | `123,000` |
| three machines **and** two repairs | `3 machines and 2 repairs` (correctly kept apart) |

Captions written *before* this fix keep the split form, and I deliberately do
**not** auto-merge old ones: most `<number> and <number>` pairs in the archive
are genuinely two numbers ("17 and 30 minutes"), and merging them blind would
corrupt real captions. If an old reading's caption blocks a slide you need, ask
me and I will re-transcribe that one from its audio.

## Practical note

Write the numbers you want on screen **into the spoken text**. If you want the
brick total on a progress bar, say the total out loud. That constraint is the
feature: the slides can never tell Duho something the audio did not.

Files: `nm_deck_build.py` (authored path), `nm_deck_derive.py` (fallback),
`nm_report_graphics.py` (generators), `nm_report_postprocess.sh` (the chain).
