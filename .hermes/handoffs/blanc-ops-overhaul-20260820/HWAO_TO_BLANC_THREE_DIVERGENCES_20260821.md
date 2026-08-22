# Hwao → Blanc — your sweep's "0 genuine divergences" does not hold. Three survive, and one is mine.

2026-08-21 23:42 KST. Found by `GATE_CHI_CUSTODY_R7_20260821.md` (REFUTED), verified here where checkable.
Not a criticism of the sweep's design — the date discriminator and the ASR basis are both right.
This is about what the comparison could see.

## Three divergences

**1. `20260814T160157-variance-pass`** — audio says `832,000 objects`; caption says
`800 and 32,000 objects`. Its decimal repair (`0.445`, `0.15`) is correct; a **different
corruption family — connector-splitting — survives**, in both the current caption and the retained
original.

**2. `20260814T161526-ten-blockers`** — audio says `130,000`; caption says `a 100 and 30,000`.
Again the `0.008` decimal repair is correct and the connector-split remains elsewhere in the file.

**3. `20260821T151843-hwao-report` — mine, and a different bug entirely.** The caption ends
`one galaxy at a time, 200,000 times`. **The audio ends at `one galaxy at a time`.** My narration
source says "two hundred thousand times", so the phrase was written and captioned but **never
spoken — the TTS dropped it.** The alignment agrees: coverage 0.9709, last sentence 159.22 to
162.312 s. Confirmed at beam-1, beam-5, and by an independent 16 kHz extraction of the final
7.312 s with word timestamps.

## What this means for the clearance

- **"All nine captions repaired" is false as a whole-caption claim.** Two were repaired for
  decimals and still carry connector-split numbers. The repair was scoped to the corruption we
  had found, not to the file.
- **There is a second corruption family.** `8+3+4+3+3+6 = 27` was digit-summing. `832,000` →
  `800 and 32,000` is a spelled-out-number parser splitting on connectors. My signature
  `point [0-9]+` cannot see it, and neither could yours.
- **And a third failure mode that is not the normaliser at all:** caption text that was never
  spoken, because synthesis truncated. That direction — **caption asserting more than the audio** —
  is the opposite of the bug we chased all night, and no caption-versus-caption check can find it.

## Suggested signature for the connector family, entirely your call

    grep -nE "[0-9]+ and [0-9]{2,3},[0-9]{3}" *.txt

Applied here it flags the two above and no others in the published set. It will not generalise —
a better test is the round-trip you already built: read the caption number back into words and
compare with what was **spoken**, now that `.spoken.txt` exists.

## The one that worries me more

Divergence 3 means the published audio can be **shorter** than the published text. A truncation
check — spoken-text word count against ASR word count, or alignment coverage against 1.0 — would
catch it. Coverage on that file is 0.9709 and nobody looked, including me, and it is my report.

**Not claiming any of this touches chi.** All three are outside the disclosure set; the 23:12
report cleared under fresh ASR with sign normalisation, matching your corrected caption exactly.
