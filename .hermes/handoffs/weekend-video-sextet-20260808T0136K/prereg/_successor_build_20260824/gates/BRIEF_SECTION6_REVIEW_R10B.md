# REFEREE BRIEF — §6 tenth pass. Four repairs. One reverses an instruction I gave.

Subject: **`SECTION6_DRAFT_AGY_R10B.md`**. Its sha256 is printed into `runner_s6rev10b_round.log`
at send time; verify the file you read matches.

## What changed

Your R9C reports gave four findings. **You split on severity** — GPT56 logged three BLOCKER, CODEX
logged the same ground as three MAJOR with zero blocking. They have been treated as blocking, on the
principle that a freeze cannot rest on whichever seat was more lenient. If you think that is
over-strict, say so.

1. **The four join-anomaly branches now terminate once.** `INCONCLUSIVE-BY-MISSING-RECORD`,
   `-DUPLICATE`, `-ORPHAN` and `-MALFORMED` are kept, and missing/duplicate/extra/malformed are
   **deleted from row P's void column**, which is reserved for prohibited execution outside the
   symbol, silent inner-join loss, and discretionary retry.
2. **An ordered adequacy decision tree is frozen.** Any attrition emits
   `INCONCLUSIVE-BY-CALIBRATION` and **no Stage-C rerun is performed**. Part 2 and residual risk R3
   are conformed; R3's "void" language is gone.
3. **Clause 8 terminates.** The retrospective-custody question must be resolved before freeze, and
   **if it is unresolved at freeze time the run is refused.** The principal keeps the whole pre-freeze
   window to decide the substance; the document no longer depends on a decision that might never come.
4. **The power-inapplicability branch was re-cut** — see below.

## The repair I most want checked, because I got it wrong first

CODEX's R9C finding 3 showed that an instruction I gave in R9 was wrong. I directed
`INCONCLUSIVE-BY-POWER` when the 962/1,000 criterion cannot be applied. CODEX read the pinned code:
`stage_power` returns a boolean when `n_trials == N_TRIALS` and `None` when it differs, so an
inapplicable criterion means the trial structure departed from the frozen protocol — which V15 lines
570–573 make **VOID**, not inconclusive. The branch either downgraded a void or was unreachable.

R10b was told to split the causes: **any deviation from the pinned 1,000-trial protocol or frozen
Stage-C implementation terminates `VOID`**; `INCONCLUSIVE-BY-POWER` survives only for a named lawful
inapplicability state produced by the *unchanged* protocol; and **if no such lawful state exists, the
branch is to be deleted** and the pinned `< 962` rule applied alone.

**Check which it chose, and check it against `../ref/successor_ref_v9.py` lines 1275–1277 yourself.**
If it kept a lawful-inapplicability state, does that state actually exist in the code, or has a
branch been preserved to be safe? An unreachable branch is what clause 10 forbids.

## Also judge

- **Apply clause 10 to the whole table again.** It found three defects last round including one in
  the clause list itself. Run it as a test, not a formality — including against clause 10.
- **Is "no Stage-C rerun is performed" consistent everywhere?** Row P, Part 2, R3 and any residual
  risk must say the same thing. A repair in the row that leaves Part 2 asserting the old behaviour is
  the failure this document keeps producing.
- **Sweep the numbers again.** Both of you have swept twice and found nothing after the one
  fabrication. Sweep again anyway.
- **Confine the diff.** R9c → R10 → R10b should show only the four repairs plus metadata.

## Not in scope

The attrition-intolerance design question — that one removal ends the study inconclusive by
calibration — is with the principal and is **not** a prose defect. Do not accept a draft that
weakens the fail-closed calibration rule to escape it; that would be renaming the finding.

Findings 1, 2, 2b and 3 remain **UNRESOLVED** pending the BS-2a artifact. BS-2a is REFUSED by all
three seats; rows C2 and E cannot run; BS-6 and the first image byte stay blocked.

Do not read `/Users/duhokim/NebulaMindData/`. Nothing is authorised to fetch. No deadline.

## Verdict

`SECTION6_REVIEW_R10B_<YOURSEAT>.md`. Numbered findings with severity, row/clause, why it fails,
smallest sufficient repair. Unverified assertions under `Testimony`. Final line exactly `**CLEAR**`
or `**NOT CLEAR**`.

**If §6 is now sound as prose and the remainder is genuinely the BS-2a mechanism, say so.** Ten
rounds have each been narrower than the last. I would rather have an eleventh finding than a
courtesy pass — but if there is nothing left, saying so is the useful answer.
