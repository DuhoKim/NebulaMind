# The caption normaliser published numbers that were never measured

Found 2026-08-21 by following Hwao's `CHI_DISCLOSURE_ASR_FINDING_20260821.md`
back to its cause. He found that the published audio and the published caption
of the same report state **different** χ values. The audio was right.

## Root cause: additive parsing of a positional digit run

English number words are additive — "twenty three" is 20+3. A digit sequence
read one digit at a time is positional — "eight three four" is 834, not 15.
Nothing in the words distinguishes the two, and `nm_caption_norm.py` assumed
additive. So it summed:

| spoken in the audio | parser produced | true value |
|---|---|---|
| eight three four three three six | 8+3+4+3+3+6 = **27** | 834336 |
| three eight four four one zero | 3+8+4+4+1+0 = **20** | 384410 |
| six four zero three five two | 6+4+0+3+5+2 = **20** | 640352 |

All three match exactly, which is what promoted this from a theory to the cause.
Hwao spelled the values out so the voice would read them properly; the audio and
the slide deck both carry them correctly. Only the caption was corrupted — and
the caption is what the archive, the report page and any reader sees.

**A caption is not a faithful record of its audio.** That is the general lesson,
and it invalidates any clearance derived from captions — see the correction
header on [DISCLOSURE_LEDGER_AUDIO_20260821.md](DISCLOSURE_LEDGER_AUDIO_20260821.md).

## The fix

`_is_digit_run()` decides by the run's *shape*: two or more tokens, every one a
single digit, no ten-and-up word (a "seventeen" or "twenty" cannot appear in a
digit reading, so its presence proves the run is an ordinary number). Digit runs
concatenate and return a **string**, because leading zeros are significant and
`int()` eats them, and they take no thousands separator — "834,336" would be a
second falsehood on top of the first. A following pass collapses the tight
`zero point <digits>` form to a real decimal, leaving prose ("the point is",
"point taken") alone.

Regression-checked: `twenty three` → 23, `two thousand and forty seven` → 2,047,
`sixty thousand three hundred eight` → 60,308, `one of the lanes` unchanged.

## Blast radius — my first bound was wrong

> **This section originally claimed "2 of 12, bounded by the ledger's
> `caption_normalized` counter". That bound was false.** It assumed the
> normaliser only existed from 2026-08-20, when the ledger opened. Hwao's note
> used a different signature — `grep "point [0-9]+"` — which reaches captions
> the ledger never covered. Seven more corrupted reports turned up, dating to
> **2026-08-14**, six days earlier. **Nine reports in total, not two.**

Two partial signatures, each blind where the other saw:

- **the ledger counter** catches any normalisation but only from 08-20;
- **`point [0-9]+`** reaches all dates but only catches *spelled* decimals.

Neither proves completeness, which is why the whole archive was transcribed —
see the sweep below.

### The two found first (08-20)

| report | published caption | audio |
|---|---|---|
| `20260820T173007-hwao` | "60,300 **and** 8" · "2,000 **and** 47" · "208,400 **and** 7" | 60,308 · 2,047 · 208,407 |
| `20260820T231235-hwao` | "zero point 27, zero point 20, minus zero point 20" | 0.834336 · 0.384410 · −0.640352 |

### The seven Hwao's signature found (08-14)

Every one matches the digit-sum signature exactly.

| report | published | actual |
|---|---|---|
| `variance-pass`, `session-summary` | 0.13 · 0.6 | **0.445** · **0.15** |
| `kun-regate` | 0.6 · 0.2 | **0.33** · 0.2 |
| `ten-blockers` | 0.8 | **0.008** |
| `both-pass` | 0.12 · 0.8 · 0.6 · 0.7 | **0.0048** · **0.008** · **0.015** · **0.025** |
| `sign-dictionary` | ∓0.12 | **∓0.0408** |
| `final-gate` | "99 point 9" | **99.9** |

`sign-dictionary` deserves singling out: it is the report explaining that Longo
defines the dipole as right-minus-left while our preregistration is written the
other way. The whole subject is the sign convention — and the caption had the
magnitude wrong by a factor of ~3 on *both* sides of the comparison.

`final-gate` is a third variant: "ninety nine point nine" became "99 point 9" —
digits, but not a number. The collapse now requires digits on both sides, so
prose ("point 9 of the brief", "see point 4 below") is untouched.

Each of the seven pairings was confirmed by **identical surrounding sentence** in
caption and audio, not inferred from matching value sets — with four values in
one report, inference would have been guessing.

The first is a *different* bug — the connector-splitting defect fixed on
2026-08-20 — in a report published before that fix landed. Same family: a
normaliser rewriting numbers it did not understand.

## Regeneration

Surgical, not wholesale. The original spelled-out source was never saved (only
the normalised caption is), so the audio is the only authority — but replacing a
caption with raw ASR would discard the author's wording and import transcription
errors elsewhere. Only the corrupted strings were replaced, then **every** number
in each file was diffed before and after: exactly the intended values changed.

- corrupted originals kept as `<stem>.txt.corrupt-20260821`
- both recorded as appended `caption_corrected` events with before/after pairs
  and the ASR authority
- report pages and `archive.html` rebuilt; zero corrupted strings remain served
- alignment still valid — sentence counts unchanged (10 and 13), so timings hold
- decks were already correct and were not touched

## The sweep — the only check that bounds this

Both signatures above are partial, so all 218 published reports with a caption
were transcribed locally and every number compared against its caption.

```
218 reports transcribed · 0 ASR errors · 0 genuine divergences
```

One report flagged, and it was **my comparison's fault**: the caption says
`-0.640352`, ASR renders the sign as the word "minus" plus `0.640352`, so a
string-set difference read them as different. Sign-normalising clears it. A
detector's own false positives belong in the record next to its findings.

The seven repaired 08-14 captions were **re-transcribed by this sweep and all
pass** — `spoken_not_in_caption` empty for every one. That is independent
confirmation of the repairs rather than my word for them.

What the sweep does *not* establish: it compares numbers, so a corruption of
words rather than digits would pass it. Nothing suggests one exists; it is
simply outside what was measured.

## Two safeguards, both Hwao's proposals

The parser fix stops this bug. These stop the next transform anyone adds.

**1. Retain the pre-normalisation text** (`<stem>.spoken.txt`, written whenever
the normaliser changes anything). Previously the TTS got the original, the
publisher wrote only the normalised caption, and the original was discarded — so
audio became the *only* record of what was said, and text could diverge from it
with no artifact showing the divergence. That is how a summed digit run survived
seven revisions of a custody receipt: every reviewer read the caption.

**2. Refuse a normalisation that changes a VALUE rather than a FORMAT**, by
round trip: read the produced number back into words and compare with what was
spoken. A format change round-trips exactly (`"twenty three"` → 23 →
`"twenty three"`); a value change does not (`"eight three four three three six"`
→ 27 → `"twenty seven"`). This needs no list of known bugs — it catches both of
tonight's and the ones nobody has thought of.

Proven by reintroducing the bug: `_value` was monkeypatched to sum digit runs
and a report published through the real path. The normalisation was refused, the
caption left verbatim, and the ledger recorded
`"eight three four three three six" -> 27 reads back as "twenty seven"`. A test
that only shows fixed code passing proves nothing about the detector.

It refuses the **normalisation**, not the **publish** — the caption falls back to
verbatim spoken text, ugly but true. Blocking a status report because a display
convenience failed would trade a real cost for a cosmetic one.
`caption_violations` is written to the ledger **even when empty**, so an auditor
can see the check ran instead of inferring it from silence.

## This correction does not reduce the disclosure

It increases it in text. The audio always spoke the full-precision values; now
the text surfaces say the same thing instead of three numbers that never
existed. Making the record accurate and making it less exposed are different
goals, and this file serves the first. Whether that report stays published is
Duho's call; the withdrawal mechanism in
[PUBLICATION_LEDGER.md](PUBLICATION_LEDGER.md) keeps it visible on the record if
he wants it used.
