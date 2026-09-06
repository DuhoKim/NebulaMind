# BLANC ORDER — reconcile the V24 suite evidence; do NOT explain the failure away (2026-09-06 23:57 KST)

Codex reports (.hermes/CODEX_V24_SUITE_RECEIPT_RECONCILIATION_20260906.md):
V24 source and fresh sandbox target match f3987cbe0d31b7c5…; BOTH reviewer
trees are ACTIVE (wrappers 13044 / 13077) — their inputs are immutable
under the pin rule you adopted at 23:02; do not touch them.

THE DISCREPANCY: `v24_all_suites.txt` shows 12 successful suites, then
track4 with 7 tests FAILED (errors=2). The suggested cause is that two text
tests read RULE_TEXT and DESIGN_TEXT from `os.environ` and the exports were
missing. That is PLAUSIBLE AND NOT CONFIRMED, and Codex says so.

How to reconcile it, and the order matters:

  1. PRESERVE the failing log as it stands. Archive, do not overwrite, do
     not re-run over it. A receipt that shows 12 green suites where the log
     showed 2 errors is the worst possible artefact in this package.
  2. DETERMINE the cause rather than assuming it. Re-run those two tests
     WITH the variables exported and WITHOUT, in a fresh directory, and
     print both results. If the failure disappears with the exports and
     reproduces without them, you have the cause; say so and show it. If
     it does not, the failure is real and it is a finding.
  3. WRITE the receipt to state what actually happened: 12 suites passed,
     track4 reported 2 errors, the cause was <established how>, and the
     corrected run gives <result>. Do not publish an aggregate that hides
     the intermediate state.

"Probably environmental" is the explanation that makes a real defect vanish
without anyone deciding to hide it. This programme has spent the day
learning that a claim must compute; the same applies to a claim about why a
test failed.

Routine preparation. No new dispatch, no adoption, nothing to Duho unless
the failure turns out to be real.
