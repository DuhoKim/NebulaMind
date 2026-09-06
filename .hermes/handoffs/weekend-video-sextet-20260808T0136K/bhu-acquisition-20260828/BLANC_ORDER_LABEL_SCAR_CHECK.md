# BLANC ORDER — finish the label rename; ten references still read as pending (2026-09-06 23:53 KST)

V27 carries the new label, and the interpretation protocol has it. But the
prereg still has 13 occurrences of `DERIVED_ONLY`, and my classifier says
only 3 are clearly historical. I looked at four of the rest:

  787   "`DERIVED_ONLY` is the clean pole of a graded order"      — reads LIVE
  952   "a label question, the principal's with the other"        — now FALSE
  1046  "authorized and therefore NOT done: the DERIVED_ONLY rename" — now FALSE
  1237  "**Not repaired, Duho's:** the name `DERIVED_ONLY`"       — now FALSE

Three of those four assert the rename is still pending and still Duho's.
As of my 23:45 order it is neither: both V26 reviewers confirmed it
label-only, and it is being implemented as routine.

Do the audit you did for REPRO_EXACT, and do it the same way:
  - classify EVERY surviving `DERIVED_ONLY` as LIVE (governs the run) or
    HISTORICAL (records what an earlier version said);
  - rename the live ones;
  - keep the historical ones and make sure each is unambiguously in a
    change-record context, not floating in operative prose;
  - for the three that assert it is pending or Duho's: those are not
    history, they are STALE STATEMENTS. Correct them to say the rename was
    implemented as routine on both reviewers' label-only finding, with the
    date;
  - report the counts, as you did last time.

This is the same defect family the rename audit was invented for. It cost
nothing last time because you caught it; it costs nothing this time either,
as long as it is finished rather than assumed.
