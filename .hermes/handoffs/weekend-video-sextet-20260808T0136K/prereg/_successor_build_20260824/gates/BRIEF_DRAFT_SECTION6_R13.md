# DRAFTING BRIEF — R13. A frozen threshold was carried without its phase. Two repairs.

Subject: `SECTION6_DRAFT_AGY_R12.md`, sha256
`6339d940842fecad772034eb942600444afbf495a6da392aff6dec5e21d79dd7`.
Read `SECTION6_REVIEW_R12_GPT56.md` and `SECTION6_REVIEW_R12_CODEX.md` first.

**GPT56 returned CLEAR — the first clear verdict on §6 in twelve rounds.** It confirms R12 seats the
protocol-deviation check in Row J before Stage-C execution and BS-5f issuance, binds the successful
verification into BS-5f, exhausts the lawful Stage-C PASS/FAIL partition, and leaves no Stage-C FAIL
branch in Row P. **All of that is credited and stays.**

**CODEX did not clear it, and CODEX is right.** The verdict is being taken as blocking. A freeze
cannot rest on whichever seat was more lenient.

## Defect 1 — the calibration halt happens after unblinding, and it must happen before

Row P places the `a_LB_b < 0.85` decision at **P8, after unblinding**. But
`../PREREG_SUCCESSOR_DRAFT_V15_20260827.md` lines 566–567 say any `a_LB_b < 0.85` yields
`INCONCLUSIVE-BY-CALIBRATION, **pre-unblinding halt**`. The aggregate needed to decide it **already
exists in BS-8f at P4**.

So as written, the draft permits **BS-5f, BS-L and unblinding itself** to occur after a frozen
calibration failure that the governing text says must halt the run before anyone looks. That is not a
placement preference. It weakens the fail-closed calibration rule the review brief expressly
protects, and it lets a run be unblinded that should already have stopped.

CODEX's diagnosis of the underlying error is worth writing into Part 3 in your own words: **the
number was carried from the frozen record, but its required phase and stopping effect were not.** A
threshold has three parts — the value, the phase it binds at, and what it does when it fails. R8
fabricated the value. R12 carried the value and dropped the other two.

**Repair:**
- **Evaluate `a_LB_b < 0.85` immediately after BS-8f and before BS-L** — in Row I, in Row J before
  Stage C, or in a separately named pre-lock gate. Pick one and say which.
- On failure, **emit `INCONCLUSIVE-BY-CALIBRATION` and halt**, pre-unblinding.
- **Require BS-L / `verify_lock()` to bind the complementary calibration PASS.**
- **Remove the Row P low-bound branch**, or state there only that Row P binds the already-verified
  pre-unblinding calibration PASS.
- **Keep Row P's distinct post-unblinding removal/applicability branch** — that one is separate and
  correct.

## Defect 2 — a citation that proves something else (MINOR)

Part 5 item 16 says "the frozen code at lines 1275–1276 admits no lawful state where the count differs
without a breach." Lines 1275–1276 only implement `if refuted or nonconservative: return succ, False,
audit`. **The count-dependent return is line 1277**, which returns `None` when `n_trials != N_TRIALS`.
The no-deviation legality rule comes from **Row J's new pre-run verification**, not from the code.

**Repair:** attribute the no-deviation rule to Row J, and cite lines 1275–1277 only for the
implementation's self-verification and count-return partition. Read those lines yourself.

## Before you finish

Run clause 10 in both directions again. Moving a decision to an earlier phase can orphan whatever
depended on it later — that is exactly what R11 did when it deleted a branch, and R12 has now been
caught in the mirror-image error of leaving a decision too late.

## Not in scope

The attrition-intolerance design question is with the principal. Findings 1, 2, 2b and 3 stay
UNRESOLVED pending BS-2a. Do not weaken the fail-closed calibration rule — this repair strengthens it.

## Deliverable

`SECTION6_DRAFT_AGY_R13.md` — complete, self-contained, five parts, in a single write.

Do not modify the preregistration. Do not read `/Users/duhokim/NebulaMindData/`. Nothing is
authorised to fetch. No deadline.
