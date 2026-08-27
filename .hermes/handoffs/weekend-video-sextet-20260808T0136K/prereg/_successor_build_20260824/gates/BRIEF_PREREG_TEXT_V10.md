# REFEREE BRIEF — the preregistration TEXT, not the machinery

You are refereeing a **preregistration**: a promise about what will be measured, how, and what
counts as an answer, written before anyone looks at the result. Its whole value is that it
cannot be adjusted afterwards. Judge the promise.

This is a different job from the five rounds that came before it. Those refereed one mechanism —
the code that computes which images the study needs — and it is now frozen and cleared. **Nobody
has ever refereed the text.** That asymmetry is why you are here: the machinery has been examined
five times and the document it serves has been examined zero.

## What the study claims to test

Spiral galaxies wind one way or the other. In 2011 Longo reported that the split is not even
across the sky: a roughly four percent excess of one handedness in one direction and the other
handedness in the opposite direction, along a specific axis. This study tests **that specific
claim** — that amplitude, that axis — and nothing wider.

The predecessor study was **declined** on 2026-08-25. Its sample could not deliver the
sensitivity it was designed around: 208,407 galaxies all bunched near one end of the tested axis,
scoring 0.058 on the spread measure against a required 0.15. The licence to proceed had been
recorded as passed using a number measured on a different, larger population. Neither document
was wrong; they were never compared. The successor selects 65,060 galaxies placed at both ends
of the axis instead.

## What to review

- **`../PREREG_SUCCESSOR_DRAFT_V10_20260825.md`** — the subject. 490 lines, §0 through §10.
- `../ref/successor_ref_v9.py` and `../ref/closure_worker_v9.py` — the code §0 says *defines*
  every mechanism. Frozen and read-only.
- `FREEZE_CLOSURE_V9_20260826.md` — what the frozen mechanism is and the nine items open against
  it.
- `CLOSURE_V9_KIMI.md` — the mechanism's referee verdict (CLEAR, one seat).
- `../real/REAL_GEOMETRY_RESULT_20260825.md` — the measured geometry and the power result,
  including a retraction you should read as an example of how this lane handles being wrong.
- `../real/STAGEP_EXACT_RECEIPT_20260826.json` — the restored power measurement.

Do not read `/Users/duhokim/NebulaMindData/`.

## What I am asking you to decide

**1. Can this promise fail?** Find the sentence that says what result would count as the claim
being reproduced, and the sentence that says what would count as it not being reproduced. Are
both unambiguous to someone who wants to wriggle? If the text can absorb any outcome, it is not
a preregistration.

**2. Where are the researcher degrees of freedom?** Name every place where a choice remains open
that could be made after seeing data — a threshold, a cut, a definition, an exclusion, a
tie-break, a "if X then we will instead". For each, say whether the text closes it or leaves it
open.

**3. Is anything circular?** Does any threshold, floor or decision boundary depend on the data it
will later judge? The power gate and the decision regions (§4, §5) are where I would look first.

**4. Do the text's numbers match the artifacts?** §0 pins code by digest; §2 and §5 quote
measured values. Check the quoted numbers against the files. Three stale figures were found and
fixed on 2026-08-26 — a code pin naming bytes that no longer existed, a power result that had
been retracted, and a download size that priced the selected bricks rather than the images
actually required. **Assume more remain and look for them.**

**5. Is the blinding real?** The predecessor's measurements are archived and sealed. The
redesign was driven by geometry — where galaxies sit — and not by any look at outcomes. Does
the text make that binding, and could someone comply with every word while still having seen
what they should not? What would show it if they had?

**6. Is the text honest about its own incompleteness?** It declares twelve prerequisite slots.
One is filled. Does the document read as more finished than it is? Does any section state a
result as established that its own later sections qualify?

**7. Does it overclaim what an answer would mean?** Specifically: what a null result would and
would not establish. A null here does not prove the universe is isotropic, does not exclude
smaller amplitudes, and does not settle other researchers' separate claims.

**8. What is missing entirely** that a preregistration of this kind should contain, and that
nobody has noticed because they were busy refereeing the machinery?

## What I already know is wrong, so you can spend your time elsewhere

Stated so you do not have to rediscover it — and if you find any of it understated, say so.

- Eleven of twelve prerequisite slots are unfilled. There is no receipt on disk for any of them
  except the manifest-closure slot filled on 2026-08-26.
- The exact power calculation lives in a measurement harness, not in the code §0 pins, so the
  slot that depends on it cannot be filled yet.
- The selection artifact has no producer receipt — nothing proves it is the output of the
  algorithm the text describes, only that its bytes have not changed since.
- The mechanism's referee panel returned one seat of the several intended; two were refused by
  their provider.
- §2.1 leaves the data-release choice open as a bound fork resolving by 2026-09-05.

## Verdict

Write `PREREG_TEXT_<YOURSEAT>.md` in this directory. Numbered findings, each with severity, the
section or quoted sentence at issue, why it fails as a *promise* rather than as prose, and the
smallest sufficient repair. Final line exactly `**CLEAR**` (this text is sound enough to be
frozen as a preregistration once its slots are filled) or `**NOT CLEAR**` (with the blocking
findings named). Anything asserted but not verified goes under `Testimony`.

Judge it as a promise someone will be held to, by people who were not in the room.
