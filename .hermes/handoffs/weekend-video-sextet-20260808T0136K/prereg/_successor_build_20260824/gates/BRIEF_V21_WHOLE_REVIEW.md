# REFEREE BRIEF — V21, whole document. Sixth assembled round.

Subject: **`../PREREG_SUCCESSOR_DRAFT_V21_20260827.md`**, sha256
`8386d5f0b3cdc8ed4161545dbcf2f8e4898c9c68942ddfc117b3103ef6ea10e5`. **Verify before opening; state
what you compared and what it returned.** 25 lines changed from V20.

## The evidence standard, continued

Both of you met it last round — AST parses against source sha `6a9abbbd…`, return sites at 1591–1625,
the decision helper at 1561–1588. **Keep doing that.** Any claim of mechanical verification states the
comparison and its result, or is filed as `Testimony`.

## What V21 changes

Your V20 finding was that line 473's inventory is **true** while the guard sentence three lines above
was still present-tense and false. Both repaired:

1. **Line ~461 is now explicitly required-but-unimplemented**: *"Required but unimplemented guards:
   the runner must require and verify the canonical BS-L artifact and the one-use unblinding receipt,
   verify the exact final-mask binding and post-unblinding ledger recomputation before forming any
   statistic…"*
2. **Line 473's return inventory is unchanged** — you both verified it true — and its unresolved list
   now includes **BS-L verification** and **authenticated one-use unblinding-receipt verification**,
   which CODEX found missing.
3. **`VOID`'s unresolved reverse reachability is stated**, clause 10 is declared **not yet
   executable**, and the `VOID` converter with branch-complete fixtures is added to §11 as a
   **pre-BS-6 dependency** in §7. **BS-6 is now blocked for a second, separately named reason.**
4. The V19→V20 aggregate-validation trace row corrected; V20→V21 entry added.

## What to judge

1. **Digest first**, with the comparison stated.
2. **Read the neighbours.** Three rounds running, a repair was correct and local while an identical
   defect sat in the adjacent sentence. **Check the sentences either side of every change**, and check
   §5 and §11 for any remaining present-tense claim of an unimplemented capability.
3. **Is the extended unresolved list now complete?** You found two missing items last round. Look for
   a third.
4. **Does the `VOID` construction hold?** It converts an unresolved clause-10 branch into a named
   prerequisite for the first image byte. Check the dependency is real in §7 — a prerequisite that
   nothing enforces is the same defect in a new place — and that "branch-complete fixtures" is
   specified tightly enough for a gate to fail an incomplete one.
5. **Clause 10 across §§0–11, both directions**, expecting it to be **explicitly unresolved at
   `VOID`**. That is the intended state. Confirm the document says so rather than implying closure.
6. **Every threshold: value, phase, failure effect.**
7. **All five §10 trace entries accurate?** State what you compared.

## Standing state

Findings 1, 2, 2b and 3 **UNRESOLVED**; **BS-2a REFUSED**; rows C2 and E cannot run; **BS-6 and the
first image byte blocked** — now for two separately named reasons. V15–V20 held at their reviewed
digests, verified immutable.

Do not read `/Users/duhokim/NebulaMindData/`. Nothing is authorised to fetch. No deadline.

## Verdict

`V21_WHOLE_REVIEW_<YOURSEAT>.md`. Numbered findings with severity, section and line, why it fails,
smallest sufficient repair. Unverified assertions under `Testimony`. Final line exactly `**CLEAR**`
or `**NOT CLEAR**`.

**Judge independently; do not converge.** If V21 is now a correct preregistration that is honest about
being an unfinished programme, that is a legitimate verdict and worth stating in those words. If
something is still wrong, a finding is worth more than a clear.
