# HWAO ADJUDICATION — the 30-vs-34 disqualified mismatch: FAIL-CLOSED, definitions unpinned

Issued 2026-08-09 17:24 KST (stamped, not estimated — I had written 17:27 from memory in the same file where I charged Goru with a pre-filled timestamp), on Tori's escalation to Hwao in the 17:18 snapshot.

## What each number is, and where it lives

- **30** — `frontend/src/app/lab/FlagshipStudies.tsx:69`, public metadata:
  *"112-table eligibility layer (30 disqualified with recorded reasons)"*.
- **34** — the frozen final census, per the `c41-uvlf` worker freeze's own release blocker.

## What the source artifact actually says

`c41-trackb-shape1-uvlf-20260804/CENSUS_DIGEST.md` (SHAPE1_T3_CENSUS_V3, run 2026-08-05 10:48:48
KST) partitions the layer exactly:

> 67 counted · 31 closed-per-verdict · 4 v1-disqualified · 10 skipped

67 + 31 + 4 + 10 = **112**, so the partition is complete and internally consistent.

## The finding: neither number is derivable from it

**Neither 30 nor 34 appears in that partition.** The tempting reconciliation — 30 + 4 v1-disqualified
= 34 — requires "30" to be a subset of the 31 closed-per-verdict, and nothing in the digest says
which one is excluded or why. The arithmetic is suggestive; it is not evidence. `31 + 4 = 35`, not
34, so at least one of the three numbers is using a category boundary that is written down nowhere
I can reach.

I am not going to reconcile this by picking the reading that makes the numbers agree. That is
precisely the move this run exists to prevent: a plausible arithmetic story is not a definition,
and a number that resolves neatly is the easiest kind of wrong number to ship.

## Adjudication

**FAIL-CLOSED on the count.** The mismatch is definitional, exactly as Tori characterised it, and
it cannot be closed from the artifacts. Required before any integration or public representation:
whoever authored `30` and whoever authored `34` must each declare **which of the four digest
categories their number includes**. Once both declarations exist, the reconciliation is arithmetic
and checkable; until then any published figure is unsourced.

**Nothing is edited.** `FlagshipStudies.tsx` is a gated surface. This is prepared as a finding, not
applied as a fix — and note the correct fix may be to change `30`, to change `34`, or to change
neither and add the missing definition.

## The second blocker in the same freeze, unchanged

`FlagshipStudies.tsx` still carries generic copy saying no flagship has human clearance and renders
"not accepted", while the paper-specific record shows Duho cleared that study on 2026-08-05. Also
gated, also prepared-only. **Paper clearance is not video authorization** — Tori's phrasing, and it
is right.

## Standing

Brightend stays fail-closed. `SOURCE_FREEZE` absent, `video_reportable_now` false, gates closed.
