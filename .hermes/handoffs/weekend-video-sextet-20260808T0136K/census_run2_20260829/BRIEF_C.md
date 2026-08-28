# Classify these papers by what it would take to refute them

You have no other context and need none. Do not look outside the paper files listed for you and
this brief. **If you encounter any pre-existing classification of these papers anywhere, ignore
it and record that you saw it in the `saw_prior_labels` field.**

## Classes

- `CALIBRATED-FALSIFIER` — the authors state a quantity and a value such that a specified
  OBSERVATION would refute the model. The threshold must be on something observable, not on an
  internal model parameter. "If Omega_k > 0 is confirmed, this is dead" qualifies. An inequality
  a model parameter must satisfy for self-consistency does NOT.
- `QUALITATIVE-DIRECTIONAL` — a directional claim, no calibrated threshold.
- `CONSISTENCY-ONLY` — compatible with observation; states no prediction that could fail.
- `PROSPECT` — points at future instruments as the way it might be tested, without supplying the test.

## Protocol, in order, for each paper

1. Find the strongest falsifiability-flavoured claim in the abstract. Quote it.
2. Go into the BODY and hunt for text that WEAKENS, CONDITIONS or WITHDRAWS it — "assume",
   "if X has a different origin", "could be smaller", "we expect", "approximately", "conjecture",
   a factor constrained below one, an inequality making a stated value a bound. Quote what you
   find with its location, or record that you searched and found none.
3. Classify on 1 AND 2 together. If the body withdraws the magnitude, the class follows the body.
4. Decide whether a reader classifying on the ABSTRACT ALONE would have reached a different class.

Some texts are OCR'd: "sufficiently" may render "SuMciently", "2.5" as "2:5". Read through it.

## OUTPUT CONTRACT — read this twice

Write **only a JSON array**, nothing before or after it, to the file named below. No prose, no
markdown fences, no commentary. One object per paper, with exactly these keys:

    [
      {"entry": 1,
       "class": "CONSISTENCY-ONLY",
       "abstract_quote": "...",
       "body_qualification": "..." or "SEARCHED-NONE-FOUND",
       "abstract_alone_class": "CONSISTENCY-ONLY",
       "diverges": false,
       "threshold_is_observable": true/false/null,
       "confidence": "high",
       "saw_prior_labels": false}
    ]

`abstract_alone_class` is what step 4 would give on the abstract alone; `diverges` must equal
(`class` != `abstract_alone_class`). `threshold_is_observable` applies only when class is
CALIBRATED-FALSIFIER — say whether the threshold is on an OBSERVABLE or on a model parameter;
use null otherwise. A file too mangled to class gets `"class": "UNREADABLE"`.

## Your papers — batch C. Write to `census_C.json` in this directory.

    entry 38 -> /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-reading-20260823/sources/math-ph_0302036_clean.txt
    entry 39 -> /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-reading-20260823/sources/1105.6127_clean.txt
    entry 40 -> /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-reading-20260823/sources/2008.02136_clean.txt
    entry 41 -> /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-reading-20260823/sources/2007.11556_clean.txt
    entry 43 -> /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-reading-20260823/sources/2304.12018_clean.txt
