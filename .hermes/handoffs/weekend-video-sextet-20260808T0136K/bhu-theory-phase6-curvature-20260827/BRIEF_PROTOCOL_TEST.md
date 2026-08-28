# Protocol test — four papers, and the point is to test the PROTOCOL, not the papers

You are classifying four papers by how falsifiable their claims are. **You are not told how we
class them.** Do not search for our classification; if you encounter it, ignore it and say so.

## Why this exists

An earlier blind pass over this corpus **failed its own control**. Seeded with three papers whose
correct classification had been settled by independent adjudication, it got two right and one
badly wrong — and the wrong one failed in a specific, diagnosable way: **it read the abstract's
headline claim and missed a qualification buried in the body that withdraws it.**

This brief adds one step designed to catch exactly that. Whether the step works is what is being
measured. Your four papers include the ones that were seeded before.

## The classes

- **CALIBRATED-FALSIFIER** — number + threshold. The authors state a quantity and a value such
  that a specified observation would refute the model.
- **QUALITATIVE-DIRECTIONAL** — a directional claim with no calibrated threshold. "Predicts closed
  curvature" with no number that could be exceeded.
- **CONSISTENCY-ONLY** — shows compatibility with observation; states no prediction that could fail.
- **PROSPECT** — points at future instruments as the way it might be tested, without supplying the test.

## THE PROTOCOL — do these in order, and show your work for each

For each paper:

**Step 1 — the headline.** Find the strongest falsifiability-flavoured claim in the abstract or
introduction. Quote it verbatim. This is what a fast reader would classify on.

**Step 2 — hunt the qualification. This is the step that matters.** Go into the body and search
specifically for text that WEAKENS, CONDITIONS or WITHDRAWS the step-1 claim. Look for: "assume",
"if ... has a different origin", "could be smaller", "we expect", "approximately", "conjecture",
"provided that", a factor constrained to be less than one, or an inequality that makes a stated
value a bound rather than a prediction. **Quote what you find, with its location. If you find
nothing after actually looking, say "searched, none found" — that is a real answer and is
different from not having looked.**

**Step 3 — classify on steps 1 AND 2 together**, not on step 1 alone. If the body withdraws the
magnitude the abstract states, the class follows the body.

**Step 4 — state whether steps 1 and 2 disagree.** If a fast reader classifying on the abstract
alone would have got a different answer from yours, say so explicitly and name both answers.

Note: some texts are OCR'd from scans and mangle ligatures and decimals — "sufficiently" may
render "SuMciently" and "2.5" as "2:5". Read through it; do not let it hide a number.

## Your four papers

Lane: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/`
Sources in `<lane>/bhu-reading-20260823/sources/`.

    entry 6  -> smolin_1992_clean.txt
    entry 31 -> smolin_2004_cns_clean.txt
    entry 51 -> 0910.1181_clean.txt
    entry 54 -> 2505.23877_clean.txt

## Output

Write `PROTOCOL_TEST_RESULT.md` in `<lane>/bhu-theory-phase6-curvature-20260827/`, per entry:

    ## Entry <N>
    STEP 1 HEADLINE: "<verbatim>"
    STEP 2 QUALIFICATION: "<verbatim + location>"  OR  searched, none found
    CLASS: <one of the four>
    ABSTRACT-ALONE WOULD GIVE: <same | different: NAME IT>
    CONFIDENCE: high/medium/low — one line

No preamble. If a file is too mangled to class, say `CLASS: UNREADABLE` and why.
