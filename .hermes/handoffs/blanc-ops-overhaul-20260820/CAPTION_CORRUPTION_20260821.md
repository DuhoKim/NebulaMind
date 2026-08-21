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

## Blast radius, and how it was bounded

The corruption can only exist where the normaliser ran, so the ledger's
`caption_normalized` counter bounds it: **12** publish events record a
normalised caption. Each was transcribed locally and its numbers compared
against its caption. **2 of 12** were corrupted; the other ten normalised
ordinary numbers and are correct.

| report | published caption | audio |
|---|---|---|
| `20260820T173007-hwao` | "60,300 **and** 8" · "2,000 **and** 47" · "208,400 **and** 7" | 60,308 · 2,047 · 208,407 |
| `20260820T231235-hwao` | "zero point 27, zero point 20, minus zero point 20" | 0.834336 · 0.384410 · −0.640352 |

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

## This correction does not reduce the disclosure

It increases it in text. The audio always spoke the full-precision values; now
the text surfaces say the same thing instead of three numbers that never
existed. Making the record accurate and making it less exposed are different
goals, and this file serves the first. Whether that report stays published is
Duho's call; the withdrawal mechanism in
[PUBLICATION_LEDGER.md](PUBLICATION_LEDGER.md) keeps it visible on the record if
he wants it used.
