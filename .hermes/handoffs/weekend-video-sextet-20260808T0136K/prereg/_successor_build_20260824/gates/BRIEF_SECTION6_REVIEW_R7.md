# REFEREE BRIEF — §6 seventh pass. One finding was repaired. Judge that, and the honesty of the rest.

Subject: **`SECTION6_DRAFT_AGY_R7.md`**, sha256
`ecccedde495a88377497057a4334c676f651f559fc0a7b2635a78dca8a990f30`.
Author: the agy seat. You are not its author.

## What this pass was allowed to touch

Your R6b reports gave three blocking findings. I scoped this pass to **finding 2 only** — the
unbound downstream consequence of refusing reason (c) — because you both placed the repairs for
findings 1 and 3 in a replacement **BS-2a design artifact**: byte-exact schemas, canonical
serialization, a pinned independent verifier, an attestation chain, fixture oracles. The seat was
forbidden to attempt those here and told not to invent schemas.

**Part 5 now records findings 1, 2, 2b and 3 as UNRESOLVED**, which is the disposition CODEX asked
for: a future-work list is not a repair receipt. Confirm that is honest rather than evasive — and if
marking the reason-(c) *refusal* itself UNRESOLVED understates what you already credited (you both
passed the future-execution-status attack), say so.

Route (a) — rebuilding the sealed pre-lock execution supervisor — was ruled out of scope, because it
would reverse a refusal the principal authorised. The seat took **route (b)**.

## What to judge

**1. Does row P's new contract actually close the power-gate defect?** Row P now performs a pinned
post-unblinding exact-parent join against the independently fixed attempt set; forbids silent
inner-join loss, requiring any object in the mask and absent from the join to be a named
deterministic terminal state; gives absent and non-finite measurements explicit terminal states
**evaluated before the confidence exclusion**; forbids discretionary retry; and widens the mandatory
recomputation trigger from confidence removals to **any** removal, refusing the verdict if a locked
adequacy condition fails. Test whether that is now evaluable — whether a gate could decide it — or
whether it names states without defining them.

**2. Row I now fails the run before BS-8f** if any allocated object lacks a finite output. The draft
says this accepts a "leakage cost." Judge that cost. Does knowing the run halted at BS-8f disclose
anything about handedness, or only about data completeness? The seat chose to fail closed rather
than define calibration over a provably usable sealed subset. Say whether that was the right trade
and whether the alternative was actually available.

**3. Did anything you confirmed held get disturbed?** Mechanically diff R6b → R7. The clause bodies
should be untouched (I measured 9 clauses at identical average length), all twenty rows present, and
the three protected properties intact. §6.2 and §6.3 are now reconstituted as real text rather than
the parenthetical placeholders you were shown last round — check the reconstitution is faithful to
R5 and introduces nothing.

**4. Is BS-5f's rule now stated?** The draft claims BS-5f cannot certify a mask containing rows the
verdict cannot use without triggering refusal. Verify that against the actual text and against
current V15 §4.

## Standing state

BS-2a remains **REFUSED** by all three seats; rows C2 and E cannot run; BS-6 and the first image
byte stay blocked. The draft describes a pipeline it admits cannot presently execute.

Do not read `/Users/duhokim/NebulaMindData/`. Nothing is authorised to fetch. No deadline.

## Verdict

Write `SECTION6_REVIEW_R7_<YOURSEAT>.md` here. Numbered findings with severity, the row/clause at
issue, why it fails, smallest sufficient repair. Unverified assertions under `Testimony`. Final line
exactly `**CLEAR**` or `**NOT CLEAR**`.

If §6 is now sound **as prose** and the remaining work is genuinely the BS-2a mechanism rather than
this document, say that explicitly — it is a useful verdict and I will act on it.
