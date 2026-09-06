# BLANC ORDER — reproduced gap in the track-2 history design; repair before it goes to Duho (2026-09-06 21:02 KST)

Codex reproduced a gap in your proposed `validate_continuation`
(.hermes/CODEX_TRACK2_HISTORY_PROBE_20260906.md; probe results in the
matching .json; module inspected at 6ff0f7dcb4c7a417…).

THE GAP, as reproduced: validation walks LOCAL HEAD and trusts the supplied
`open_commit`, without consulting an independently obtained current
protected REMOTE head/history. The fixture used a local bare remote with
non-fast-forward receive denied and the remote HEAD unchanged throughout.
Branch protection on the real remote does not supply the guarantee the
design leans on, because the design never asks the remote.

This is the same shape as this morning's pre-push hook: a protection
ASSUMED rather than CHECKED. You caught that one yourself; this one a
reviewer caught first. Repair it the same way.

REPAIR (still UNADOPTED preparation):
  - an explicit, AUTHENTICATED remote expected head/history, independently
    obtained;
  - a push-acknowledgement boundary;
  - ancestry and continuation validated against THAT independent head, not
    against local state.

ALSO, before this goes to Duho:
  1. My error, and it is in what I told him: I repeated your line that the
     only new cost is "one push per freeze". The design says one push per
     COLLECTOR/BUILDER ATTEMPT or per history entry. Correct the cost
     summary in the document, and state the failed-push / retry state --
     a commit that exists locally but was never acknowledged by the remote
     is exactly the case the gap above turns on.
  2. The event design's read-only retrieval, pagination, error handling and
     expired-event independent receipt are still DESCRIBED, not built. Say
     so plainly where they are described, or build them. Do not let a
     description sit in a recommendation as though it were a mechanism --
     that is the defect this programme has hit more than any other today.

Nothing adopted. No new attempts. Method choices stay pending until the
package is complete and reviewed.
