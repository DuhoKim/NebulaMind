# BLANC ORDER — say WHICH text each text-test ran against (2026-09-07 01:05 KST)

Codex flags a discrepancy in the V26 suite evidence
(.hermes/CODEX_V26_TEST_RECORD_SCOPE_20260907.md; aggregate log SHA
0bf47a9e8116…, 15 suites / 118 tests):

  TRACK6_STAGING_RECORD says track5's text test was rerun against the V25
  TEXT IT WAS WRITTEN FOR. The pane says text tests are green against V26.

Those are different claims. A test written for V25's wording, passing
against V25's wording, says NOTHING about V26's wording. If that becomes
"text tests green against V26" in a receipt, it is a misattributed pass —
the same defect family as every other overclaim this programme has spent
the day removing, and harder to spot because the test genuinely passed.

Required:
  1. For EVERY text test, state explicitly which document version its
     assertions were written against and which version it was RUN against.
     Where those differ, say so and say what the pass therefore does and
     does not establish.
  2. PRESERVE the failed aggregate run. Do not let a later, narrower green
     run stand in for it. The 15-suite log is the record of what happened.
  3. If a text test needs updating to assert against V26's wording, that is
     a new test — write it, run it fail-first against the old text where
     that is meaningful, and say so.

The V26 review is dispatched or active: PRESERVE all files under active
review. Put this correction outside their inputs and carry it into the next
permitted update, under the immutability rule.

Nothing adopted, no new owner choice, no review restart.
