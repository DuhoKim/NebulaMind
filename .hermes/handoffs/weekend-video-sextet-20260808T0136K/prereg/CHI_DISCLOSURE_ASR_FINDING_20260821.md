# FINDING — the published AUDIO disclosed different, full-precision chi values than every text surface

Hwao, 2026-08-21 21:42 KST. **Not gated.** Found by `GATE_CHI_CUSTODY_R6_20260821.md` (REFUTED_CHI_CUSTODY_R6) and
verified here independently.

## The fact

`20260820T231235-hwao-report.mp3` (sha256 `2a38a887bd897147…`, 70.7 s, published seq 20 at
2026-08-20 23:12:51 KST) says:

> "The first three real values, **0.834336, 0.384410, and minus 0.640352**, one leaning each way
> among the confident pair."

Every text surface — the `.txt`, the report HTML, the archive — says *"zero point 27, zero point
20, and minus zero point 20."* **Those numbers are not the disclosed values and never existed.**

Two independent local models agree on the audio, from the same file:

| model | snapshot | transcript of the clause |
|---|---|---|
| `Systran/faster-whisper-small.en` | `d1d751a5f827` | 0.834336, 0.384410, minus 0.640352 |
| `Systran/faster-whisper-medium` | `08e178d48790` | 0.834336, 0.384410, minus 0.640352 |

## The mechanism — reproducible in one line

`nm_caption_norm.normalize()` **sums the digit-words after "point"** instead of concatenating them:

    IN : "... zero point eight three four three three six ..."
    OUT: "... zero point 27 ..."

`8+3+4+3+3+6 = 27`. Likewise `3+8+4+4+1+0 = 20` and `6+4+0+3+5+2 = 20`. It is a spelled-out-number
parser ("twenty seven" = 20+7) applied to a digit string.

The publisher writes the **normalized caption** to `.txt`, not the spoken text, and the TTS receives
the original. So the audio is correct and every text artifact carries fabricated numbers.

## Consequences

1. **The breach is larger than recorded.** Three **full-precision** chi values were published in
   audio, not three approximations. Every custody receipt revision to date read the caption.
2. **Seven audits failed for one reason.** The generator prints "rendered audio is never
   transcribed" as a blind spot; that blind spot was concealing the actual disclosure.
3. **This is not confined to this lane.** Any number narrated as digit-words in ANY audio report has
   been silently corrupted in its caption and archive. Blanc owns `nm_caption_norm` and should be
   told; the standing rule that every on-screen number must be spoken aloud makes the blast radius
   the whole report system.
4. **A seventh surface exists:** the unlisted YouTube video `4q9afgp3tzU`, whose frame at 01:45
   shows `χ = 0.013161621987819672` and `raw bits 0x3c57a3d8`. External platform, outside every
   local scan.

## What is NOT affected

Condition 1 is still not breached — the R6 gate searched for a real-chi invocation of
`handcheck/nm_handcheck.py`, for any real-chi tertile artifact, and found none. The breach remains
**condition 2**, now of greater extent.

## Status

Recorded so it cannot be lost. The custody receipt and the decision memo both need rebuilding on
it, and the generator needs an ASR pass and an external-surface class. Neither is done.
