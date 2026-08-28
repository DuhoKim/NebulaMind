# Blind re-classification brief — read the paper, class it, do not look for our answer

You are classifying papers for a bibliography of black-hole-universe cosmology. **You are
deliberately NOT being told how we currently class them.** Do not go looking. If you find our
classification in any file, ignore it and say so in your output.

Why: three entries re-read this week were all misclassified in the same direction — our record
claimed more than the paper supported. A seat that knows the prior answer anchors on it, and an
anchored seat cannot find the opposite error. Your independence is the instrument.

## The four classes, verbatim from our scheme

- **CALIBRATED-FALSIFIER** — number + threshold. The authors state a quantity and a value such
  that a specified observation would refute the model. Not "this predicts curvature" but
  "if Ω_k > 0 is confirmed, this is dead".
- **QUALITATIVE-DIRECTIONAL** — a directional claim with no calibrated threshold. "Predicts
  closed curvature", "predicts a cutoff", with no number that could be exceeded.
- **CONSISTENCY-ONLY** — shows the model is compatible with observation; states no prediction
  that could fail.
- **PROSPECT** — points at other instruments or future surveys as the way it might one day be
  tested, without itself supplying the test.

## What to do, per paper in your batch

1. Read the pinned text. Paths are absolute; they are plain text extracted from the published
   paper. Some are OCR'd from scans and mangle ligatures and decimals — e.g. "suﬃciently"
   renders as "SuMciently" and "2.5" as "2:5". Read through that; do not let it hide a number.
2. Decide the class **on the paper's own content**.
3. **Quote the sentence that decides it.** If you class something CALIBRATED-FALSIFIER, quote
   the number and the threshold verbatim. If CONSISTENCY-ONLY, say what you looked for and did
   not find.
4. Note explicitly whether the paper contains **any author-stated number that a future
   observation could exceed**, even if you do not think it rises to a falsifier. This is the
   thing we are most likely to have missed.

## Output

Write ONE file, `BLIND_BATCH_<X>.md`, in the lane directory, containing for each entry:

    ## Entry <N>
    CLASS: <one of the four>
    DECIDING QUOTE: "<verbatim>"
    AUTHOR-STATED NUMBER A FUTURE OBSERVATION COULD EXCEED: yes/no — <what, verbatim, or "none found">
    CONFIDENCE: high/medium/low — <one line why>

No preamble, no summary. If a file is unreadable or too mangled to class, say
`CLASS: UNREADABLE` and why — that is a useful answer, not a failure.

## Batches

Lane: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/`
Sources live in `<lane>/bhu-reading-20260823/sources/`.

**BATCH A** — write `BLIND_BATCH_A.md`
    entry 1  -> 1111.1017_clean.txt
    entry 6  -> smolin_1992_clean.txt
    entry 31 -> smolin_2004_cns_clean.txt
    entry 36 -> smoller_temple_2000_clean.txt
    entry 37 -> 0210105_clean.txt

**BATCH B** — write `BLIND_BATCH_B.md`
    entry 38 -> math-ph_0302036_clean.txt
    entry 39 -> 1105.6127_clean.txt
    entry 40 -> 2008.02136_clean.txt
    entry 41 -> 2007.11556_clean.txt
    entry 43 -> 2304.12018_clean.txt

**BATCH C** — write `BLIND_BATCH_C.md`
    entry 44 -> 1309.1487_clean.txt
    entry 45 -> 2210.15186_clean.txt
    entry 49 -> blau_guendelman_guth_1987_clean.txt
    entry 51 -> 0910.1181_clean.txt
    entry 52 -> 1808.08327_clean.txt

**BATCH D** — write `BLIND_BATCH_D.md`
    entry 53 -> 1906.11824_clean.txt
    entry 54 -> 2505.23877_clean.txt
    entry 55 -> 2007.06664_clean.txt
    entry 57 -> smoller_temple_1997_clean.txt

Classify only your assigned batch.
