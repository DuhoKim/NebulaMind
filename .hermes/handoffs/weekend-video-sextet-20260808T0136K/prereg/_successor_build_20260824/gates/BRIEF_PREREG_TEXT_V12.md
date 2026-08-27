# REFEREE BRIEF — the preregistration TEXT, round 3 (V12)

You are refereeing a **preregistration**: a promise about what will be measured, how, and what
counts as an answer, written before anyone looks at the result. Its whole value is that it
cannot be adjusted afterwards. Judge the promise.

**You have now refereed this document twice and returned NOT CLEAR both times.** Round 1 found
six blockers in V10; V11 repaired them; round 2 found four blockers **and every one of them was
inside a V11 repair** — nothing V10 had already survived came back. Your reports are all on disk
and V10 and V11 are unmodified beside V12.

**Read V12 as a fresh subject.** The evidence for that instruction is now this lane's own record:
two of round 1's blockers were defects I introduced the day before while repairing something
else, and all four of round 2's were defects I introduced the same morning while repairing round
1. My repair rate and my defect-introduction rate are close to equal. Treat a fixed sentence as a
new sentence.

**One blocker is deliberately NOT repaired.** Stage P remains dual-valued. Three of you found
that V11's prose declaration cannot bind while §0 says the pinned code defines every mechanism
and the pinned code implements the shared-null route. I agree, and no wording closes it: it needs
either the exact per-trial test implemented in the code §0 pins, with fixtures and a gate, or an
amendment to §0's precedence rule. That is the principal's decision, not mine, and it is stated
as open in §4 rather than papered over. **Please rule on whether stating it openly is an
acceptable posture for a document that is not yet frozen — and say so if it is not.**

## What V12 claims to have repaired, so you can aim at the claims

- **§6.1(2), the event order (all three of you).** V11 wrote "the lock, unblinding and BS-5f, in
  that fixed order", which licensed an unblinding preceding the confirmatory power gate. It now
  reads **BS-5f → lock → unblinding**. **Check it against §4, §5, §6.1(1) and §7 — is it now
  consistent everywhere, and does any other clause still imply a different order?**
- **The header (all three of you).** It called the predecessor's 208,405 measurements "successor
  input" while §6.2 said they are not an input. Now: the brick sample is input, the measurements
  are not, §6.2 governs. **Is any third statement about them still standing anywhere?**
- **§2.7(4)(5)(6), the truth of a reason (CODEX 3 / GPT56 F3).** Every predicate is recomputed
  from evidence in the ledger and any disagreement between status, reason and evidence is
  refused; the confidence quantity must be defined rather than thresholded; acceptance design
  becomes a new DESIGN slot **BS-2a**, gated as text and code before any image byte, with BS-2f
  demoted to a value-only realised partition. **Can an operator still choose the answer through
  this as written? Is BS-2a's boundary drawn in the right place?**

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

Write `PREREG_TEXT_V12_<YOURSEAT>.md` in this directory. Numbered findings, each with severity, the
section or quoted sentence at issue, why it fails as a *promise* rather than as prose, and the
smallest sufficient repair. Final line exactly `**CLEAR**` (this text is sound enough to be
frozen as a preregistration once its slots are filled) or `**NOT CLEAR**` (with the blocking
findings named). Anything asserted but not verified goes under `Testimony`.

Judge it as a promise someone will be held to, by people who were not in the room.
