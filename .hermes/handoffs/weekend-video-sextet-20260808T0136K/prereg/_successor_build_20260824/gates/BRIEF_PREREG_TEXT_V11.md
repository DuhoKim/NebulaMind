# REFEREE BRIEF — the preregistration TEXT, round 2 (V11)

You are refereeing a **preregistration**: a promise about what will be measured, how, and what
counts as an answer, written before anyone looks at the result. Its whole value is that it
cannot be adjusted afterwards. Judge the promise.

**Round 1 was yesterday and you were in it.** Three seats — KIMI, GPT56 and CODEX — refereed
V10 and all three returned NOT CLEAR, with six blocking findings between you. V11 repairs all
six. Your reports are on disk (`PREREG_TEXT_KIMI.md`, `PREREG_TEXT_GPT56.md`,
`PREREG_TEXT_CODEX.md`) and V10 is unmodified beside V11, so both stay legible.

**Read V11 as a fresh subject, not as a diff.** A repair round is the easiest place to introduce
a new defect, and in the mechanism's five rounds every repair introduced one. Two of the six
blockers you found were defects I had introduced while repairing something else the day before.

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

- **`../PREREG_SUCCESSOR_DRAFT_V11_20260827.md`** — the subject. 490 lines, §0 through §10.
- `../ref/successor_ref_v9.py` and `../ref/closure_worker_v9.py` — the code §0 says *defines*
  every mechanism. Frozen and read-only.
- `FREEZE_CLOSURE_V9_20260826.md` — what the frozen mechanism is and the nine items open against
  it.
- `CLOSURE_V9_KIMI.md` — the mechanism's referee verdict (CLEAR, one seat).
- `../real/REAL_GEOMETRY_RESULT_20260825.md` — the measured geometry and the power result,
  including a retraction you should read as an example of how this lane handles being wrong.
- `../real/STAGEP_EXACT_RECEIPT_20260826.json` — the restored power measurement.

Do not read `/Users/duhokim/NebulaMindData/`.


## What V11 claims to have repaired, so you can aim at the claims

Each is a claim to be checked, not evidence.

- **§6.1, the unanimous finding (KIMI F1 / GPT56 F1 / CODEX 2).** The old clause forbade
  disclosure and was relied on as blinding. §6.1 now defines the primary lock in the text, names
  who may hold read access, forbids inspection by anyone who can alter the text or fill a slot
  or operate the lock, requires an append-only log of every read succeeded or refused, voids the
  run on unauthorised access regardless of disclosure, and names what evidence establishes that
  the geometry redesign happened without outcome access. **Is that blinding now, or is it a
  better-worded embargo?**
- **§6.2 (KIMI F2).** No predecessor measurement enters this run's analysis; every measurement
  is taken fresh under this text. **Does anything else in the document contradict that?**
- **§2.7 (GPT56 F2 / CODEX 1).** Acceptance and exclusion are fixed before any image byte: one
  terminal status per object, a closed list of exclusion reasons, every predicate sign-blind by
  construction, the code recomputing the accepted set from a ledger rather than trusting flags.
  **Can an operator still move the answer through this rule as written?**
- **Stage P (GPT56 F3).** The text now promises the exact per-trial test and marks the
  shared-null contract superseded, and says BS-5p cannot be filled from the existing
  measurement. **Is the promise now single-valued, and is §4 consistent with it?**
- **§2.1 (CODEX 3).** Branch A is stated to void the current pin rather than set a flag.
- **§2.4 (KIMI F3)** and three numeric corrections: 951 rather than 995 p-values at the
  resolution floor, 2 of 12 audited boundary successes rather than 2 of 7, and the v9 planner
  digest. **Check these against the receipts; do not take the corrections on trust, and assume
  more remain.**
- **VALUE versus DESIGN slots.** BS-2f, BS-5p, BS-8p and BS-9 are named as design slots whose
  filling requires a new revision and a fresh gate.

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

Write `PREREG_TEXT_V11_<YOURSEAT>.md` in this directory. Numbered findings, each with severity, the
section or quoted sentence at issue, why it fails as a *promise* rather than as prose, and the
smallest sufficient repair. Final line exactly `**CLEAR**` (this text is sound enough to be
frozen as a preregistration once its slots are filled) or `**NOT CLEAR**` (with the blocking
findings named). Anything asserted but not verified goes under `Testimony`.

Judge it as a promise someone will be held to, by people who were not in the room.
