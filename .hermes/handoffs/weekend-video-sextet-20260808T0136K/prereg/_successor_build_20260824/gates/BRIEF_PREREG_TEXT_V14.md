# REFEREE BRIEF — the preregistration TEXT, round 4 (V14)

You are refereeing a **preregistration**: a promise about what will be measured, how, and what
counts as an answer, written before anyone looks at the result. Its whole value is that it
cannot be adjusted afterwards. Judge the promise.

**Three rounds, three unanimous NOT CLEARs.** Round 1 found six blockers in V10. V11 repaired
them and round 2 found four, **all inside the V11 repairs**. V12 and V13 repaired those and
round 3 found three more, again in the repairs. V14 is the fourth attempt. Every earlier draft
and report is on disk, unmodified.

**Read V14 as a fresh subject.** The reason is this lane's record and not a courtesy: across
three rounds, nearly every blocker you have found was a defect I introduced while repairing the
previous one. The most recent was the sharpest — my V12 blockquote *claimed* the unanimous
round-1 blinding finding was repaired, and half of it was not. **Treat any sentence that claims
a repair as the least trustworthy sentence in the document**, including the ones added in V14.

**One blocker is still open, and it is not a text defect.** Stage P remains dual-valued because
§0 makes the pinned code definitive and the pinned code implements the shared-null route. Two of
you ruled that declaring this openly is honest draft status and not a freezeable promise; I
accept that ruling. Closing it requires implementing the exact per-trial test in the pinned code,
which changes that file's digest, breaks the frozen closure mechanism and voids the referee
verdict attached to it. That cost belongs to the principal to accept, and it has been put to him.
**Do not treat its openness as repaired; do tell me if leaving it open invalidates anything else
you would otherwise pass.**

## What V14 claims to have repaired, so you can aim at the claims

- **§6.1(2), the key-holder loophole (KIMI-V12 F3).** The ban was scoped to four powerful roles
  while read access was granted to named key holders, so a holder outside those roles could read
  a measurement pre-lock, authorised and merely logged. **The ban is now universal — no person
  and no process — and an authorised pre-lock read voids the run exactly as an unauthorised one
  does.** Is it universal in fact, or does some other clause still carve someone out?
- **§6.1(3), the exceptions (KIMI-V11 F4(ii)/(iii), carried unrepaired for two rounds).** "Blind
  automation permitted only where named here" named none; four processes are now named by pinned
  code symbol. The hand-check committee — the one group that must view χ-bearing cutouts before
  unblinding — was named nowhere and is now declared in BS-8p, barred from any other role. **Are
  those four processes the complete set? Is the committee's isolation real?**
- **§6.1(1) and §7, the lock/verdict cycle (GPT56-V12 F2 / CODEX-V12 1 / KIMI-V12 F1).** The lock
  is now **BS-L**, the verdict remains **BS-V**, and BS-5f blocks BS-L which blocks unblinding.
  **Can that sequence now be executed and receipted end to end?**
- **§7, BS-2a's class (CODEX-V12 2 / GPT56-V12 F3 / KIMI-V12 F2).** It was called a class-P
  prerequisite and placed in Class E, which would have let the text freeze before its acceptance
  rule existed. Moved to Class P with the threshold's naming authority added. Fifteen class-P
  slots, one filled.
- **Housekeeping surfaced while repairing:** a stale "BS-V's schema" left by the BS-L split, a
  sentence orphaned inside a blockquote, and §2.7's list running 1,2,3,4,6,7,5.

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

Write `PREREG_TEXT_V14_<YOURSEAT>.md` in this directory. Numbered findings, each with severity, the
section or quoted sentence at issue, why it fails as a *promise* rather than as prose, and the
smallest sufficient repair. Final line exactly `**CLEAR**` (this text is sound enough to be
frozen as a preregistration once its slots are filled) or `**NOT CLEAR**` (with the blocking
findings named). Anything asserted but not verified goes under `Testimony`.

Judge it as a promise someone will be held to, by people who were not in the room.
