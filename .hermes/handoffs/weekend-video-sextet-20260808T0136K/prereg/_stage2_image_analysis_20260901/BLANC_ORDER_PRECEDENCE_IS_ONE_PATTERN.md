# BLANC ORDER — stop repairing precedence instance by instance; it is ONE pattern (2026-09-07 03:20 KST)

Count the findings:

  V27-1  approval precheck overrides the repaired precedence
  V27-2  the history-open wrapper reproduces it
  V28-1/2 the same, after the V27-2 repair introduced a regression
  V29-1  seed re-derivation returns a RETRY before approval precedence runs
  V29-2  remote availability and approval retrieval bypass local
         open-event mismatches

Five findings, one shape: A CHECK RETURNS BEFORE THE RULE THAT SHOULD
GOVERN IT. Each has been repaired where it was found, and the next round
finds it somewhere else — including once in the repair itself.

So do not write a sixth point fix. Do this instead:

1. STATE THE PRECEDENCE ORDER ONCE, explicitly, as an ordered list of
   verdict classes: which outcome wins when two or more are simultaneously
   derivable, top to bottom, with no exceptions.
2. MAKE ONE PLACE ENFORCE IT. Every path that can produce a verdict returns
   its finding to that single resolver rather than returning a verdict
   itself. A precheck may CONTRIBUTE a finding; it may not DECIDE.
3. EXHIBIT the property: for each pair of classes that can co-occur,
   construct both and show the resolver picking the same winner regardless
   of which was derived first, and regardless of retrieval order.
4. Keep every existing precedence test; add the resolver's own.

If this cannot be done without touching something Duho has approved, STOP
and tell me which part and why — do not widen scope on your own.

The reason for the whole-pattern fix is not tidiness. Four of these five
were found by a reviewer constructing an attack, and one was introduced by
our own repair. That is the signature of a defect the current structure
regenerates. Point fixes will keep passing individually while the class
survives.

Routine repair under existing authority. Nothing adopted.
