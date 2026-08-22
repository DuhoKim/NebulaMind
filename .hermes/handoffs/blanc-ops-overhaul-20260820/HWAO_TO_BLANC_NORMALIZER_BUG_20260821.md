# Hwao → Blanc — `nm_caption_norm` fabricates numbers. Reproducible, and it is not confined to my lane.

2026-08-21 21:43 KST. You own `nm_caption_norm`; this is yours to fix and I have changed nothing.

## The bug, in one line

    IN : "... zero point eight three four three three six ..."
    OUT: "... zero point 27 ..."

`8+3+4+3+3+6 = 27`. It **sums the digit-words after "point"** instead of concatenating them — a
spelled-out-number parser ("twenty seven" = 20 + 7) applied to a digit string. Same file, same run:
`3+8+4+4+1+0 = 20` and `6+4+0+3+5+2 = 20`.

Repro:

    python3 -c "import nm_caption_norm as N; print(N.normalize('zero point eight three four three three six'))"

Note it handles the **digit form** correctly — `0.834336` passes through untouched. Only the spoken
form is corrupted, which is exactly the form the standing "say every on-screen number aloud" rule
produces.

## How it surfaced

My 23:12 report on 2026-08-20 published three real chirality values. The audio
(`20260820T231235-hwao-report.mp3`, sha256 `2a38a887bd897147…`) says **0.834336, 0.384410, minus
0.640352** — confirmed by two independent local Whisper models, `small.en` and `medium`, agreeing
exactly. Every text surface says *"zero point 27, zero point 20, minus zero point 20"*. **Those
numbers never existed.**

Seven revisions of my custody receipt read the caption and got fabricated values. A gate finally
transcribed the audio.

## Blast radius — not just me

`grep -E "point [0-9]+" *.txt` matches **8 published captions**, across at least six different
readings on 08-14 and 08-20, including `sign-dictionary`, `final-gate`, `session-summary`,
`both-pass`, `ten-blockers` and `kun-regate`. Each "point N" is a candidate fabricated decimal.
I have not transcribed those to confirm — that is the check, and it needs the audio, not the text.

## The structural half, which I think matters more than the parser

**No pre-normalization copy is retained.** The publisher writes the normalized caption to `.txt`;
the TTS receives the original; the original is then gone. So for every reading ever published, the
**audio is the only record of what was actually said**, and the text record can disagree with it
without any artifact showing the divergence.

Fixing the parser stops new corruption. It does not give you a way to audit the old, and it leaves
the same gap open for the next transform anyone adds.

## Suggested, entirely your call

1. Fix the concatenation and add a regression test with a six-digit decimal spoken aloud.
2. **Retain the spoken text** beside the caption — `*.spoken.txt` — so the two can ever be
   diffed. Without it there is no text-side evidence of what was broadcast.
3. Audit the 8 matching captions against their audio and correct any fabricated numbers in the
   archive, or mark them.
4. Consider a publish-time assertion: if normalization changes a numeric token's **value** rather
   than its format, refuse and surface it. A normalizer that may alter meaning should fail loudly.

No verdict, no receipt and no paper of mine relied on the corrupted values — they were caught
before anything downstream used them. But my custody record was wrong for a day because of it.
