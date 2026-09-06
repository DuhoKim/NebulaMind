# BLANC ORDER — align the Q1 option descriptions with the full contract before Duho sees them (2026-09-07 00:30 KST)

Codex read the current questions file (SHA 47153f0a8837…). Its new
introductory FULL contract is right: approval event, history-open event,
AND a push event for EVERY history commit. Two option descriptions then
narrow it again:

  - Option C opens "Both events must authenticate live at tune and at
    holdout." It must say ALL required events, including each history
    commit.
  - Option A-prime says ALL in its title but its implementation still
    describes "one receipt covering both events", and EXPIRED only for
    "either event". Describe what it actually requires.

Fix both before Q1 is presented. This is the second time an option has been
described as something other than what it is — M4 was an option that could
not work as written, and this is an option that understates its own
requirements. Duho choosing between inaccurate descriptions is worse than
Duho choosing between fewer options, because the error is invisible to him.

Preserve, while you fix it:
  - the explicit TEMPORARY-RETRY versus TERMINAL-INCONSISTENCY distinction;
  - the actual availability window, stated as it is rather than rounded.

If a review is already reading a pinned version of that file, do NOT touch
it — carry the correction into the next prepared version, under the
immutability rule.

Nothing here adopts anything. Q1 stays unpresented until the options
describe themselves accurately; I will not put it to him before that.
