# BLANC ORDER — two tracks after V21; my cap lifted, my framing corrected (2026-09-06 20:45 KST)

Correcting myself first: I told Duho the V21 outcome came down to "how much
more hardening is worth it". That was too vague to act on and premature.
The concrete repairs are available now, and he should be shown finished,
reviewable alternatives rather than asked an open question. The cap on this
track is mine; I am lifting it for the work below.

TRACK 1 — stage and test the MECHANICAL repairs now (no adoption):
  - canonical decoded-signature comparison;
  - ALL THREE historical round exclusions, including 6441904;
  - consistent approval filename / tokens / seed wiring;
  - the remaining logging escapes from C4 ("every path" is currently
    false: BEACON-VALIDATION-ARGS-MISSING, FileExistsError after
    validation, collector argparse failures).
  Each with a test that FAILS before the repair and passes after. This
  lane has shipped a control that could not fail; do not do it again.

TRACK 2 — prepare a RECOMMENDED UNADOPTED design for the two genuine
provenance boundaries, which are the only parts that are really Duho's:
  (a) authentic GitHub event validation — the driver currently accepts a
      fabricated event with a coherently recomputed digest;
  (b) externally witnessed history continuation before first freeze — a
      reset before the first freeze currently passes.
  For each: what it would take, what it would cost, what remains trusted
  afterwards, and your recommendation. Marked UNADOPTED.

BEFORE the next full gate: inspect BOTH the successful production path AND
the prior reviewer's coherent attacks against the same pinned candidate.
The review must assess the complete object, not the happy path.

The inherited wrong test count is a FACTUAL ERRATUM, not a scientific
choice: preserve the signed source, annotate it truthfully, and do not
present the correction as a design change.

Nothing adopted, no beacon read, no draw, no fetch, no render, no pixel.
When both tracks exist, bring them to me.
