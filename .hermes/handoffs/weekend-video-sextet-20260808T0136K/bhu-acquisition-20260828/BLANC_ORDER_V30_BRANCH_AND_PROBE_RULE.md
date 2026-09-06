# BLANC ORDER — full-record branch authoritative; never weaken a guard to satisfy a probe (2026-09-07 03:03 KST)

Codex's V30 gate report (wrapper 63843 absent, ACCESS PROVEN, rc 0;
report SHA 1734c740fea4b23e…) demonstrates a REVERSE HYBRID: alternative
origin/evidence combined with PRIMARY parents receives a false PASS. Both
complete-branch predicates are false, yet field-specific checks admit it.

REPAIR (next authorized round): make the FULL-RECORD BRANCH PREDICATE
AUTHORITATIVE. If neither whole branch matches, it FAILS — regardless of
which diagnostic fields differ, and regardless of what any per-field check
concludes. Diagnostics may explain a failure; they may not overturn it.

AND A RULE I want followed without exception, because the temptation is
real and the damage would be invisible:

  DO NOT remove a safety check merely to make a deletion probe killable.

When two guards overlap, deleting one changes nothing, and the probe looks
useless. The wrong fix is to delete the "redundant" guard so the probe
registers a kill. That trades real protection for a green test.

The right fix: update the mutation fixture and its expectation to test the
ACTUAL INVARIANT, while RETAINING the required guard. If an invariant
genuinely cannot be probed while both guards stand, say so in the record as
a limit of the probe — do not make the system weaker so the test can see it.

This is the same principle as everything else tonight: the check must
compute, and it must compute against reality. A probe that only works on a
deliberately weakened system is measuring the wrong system.

Routine repair under existing authority. Nothing adopted, no new gate, no
question for Duho.
