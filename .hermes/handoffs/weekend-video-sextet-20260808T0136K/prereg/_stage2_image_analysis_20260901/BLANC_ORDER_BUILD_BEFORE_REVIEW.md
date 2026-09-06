# BLANC ORDER — correction: BUILD the event paths; disclosure is not completion (2026-09-06 21:04 KST)

I gave you a choice I should not have given. My 21:02 order said of the
event design's retrieval, pagination, error handling and expired-event
receipt: "say so plainly where they are described, or build them."

That "or" was wrong. Disclosure is not completion. A design Duho is asked
to rule on must not rest on mechanisms that exist only as prose, however
honestly the prose is labelled — he would be approving an intention.

CORRECTED: BUILD them, before the design goes to review.

  - the read-only retrieval path, actually executing;
  - pagination, actually exercised;
  - error handling on the real failure modes, each shown taking its path;
  - the expired-event independent receipt path, built and demonstrated,
    including the case where the window has passed.

Fail-first where a test can express it, the way you did on track 1: show
the check failing before the mechanism exists, passing after. That receipt
is the strongest thing you produced today and it should be the pattern
here too.

Read .hermes/CODEX_TRACK2_HISTORY_PROBE_20260906.md IN FULL rather than
relying on my condensation of it — I have now twice compressed a note and
lost something that mattered (the cost line, and this).

Unchanged: the history-validator repair against an authenticated
independent remote head still stands; nothing is adopted; no new attempts;
method choices stay pending until a complete reviewed package exists.
