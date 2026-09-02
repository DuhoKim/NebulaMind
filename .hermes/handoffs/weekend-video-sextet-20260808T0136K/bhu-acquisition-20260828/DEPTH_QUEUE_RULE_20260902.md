# Depth-audit queue rule — written down before the next draw (Tori, 2026-09-02, STEP 3)

The record names "the density rule" for the parked audit queue (register head; entry-39 reconciliation)
but nowhere defines it. From here the queue is computed by `b69_depth_queue.py`, not remembered:

1. **Frame:** the 51 BHU papers (entries 1–28, 31, 36–57).
2. **Audited at depth** (proxy, stated as such) = a per-entry receipt exists on disk: an
   `ENTRY<n>_RECONCILIATION_*.md`, any battery script named for the entry (`b*_entry<n>_*.py`,
   `c5_entry7_audit.py` — this includes the 08-31 `*_fullread.py` census reads, which are reads not
   equation audits; they are counted so that the queue prefers never-probed entries), an RQ
   reconciliation naming it (RQ-A→21, RQ-C→25/26, RQ-D→22/25/26), or the Pathria standing receipts (1). Sweep-only receipts (the 09-01 batches, the 09-02 five-paper sweep) do NOT count:
   the sweep asked "is a prediction concealed?", the deep audit asks "is what is claimed derived?".
3. **Density** = quantitative-claim lines per 100 lines of the pinned source (a line counts if it carries
   a number with a physical unit or a comparison/equality against a number). Highest first; ties by the
   bibliography's ranked-target order, then entry number.
4. **Mapping** entry → pinned source is taken from `ENTRY_SOURCE_MAP.md` where it exists and otherwise
   matched on the bibliography title against each source's first 60 lines; unmatched entries are listed
   UNMAPPED and excluded from the ranking until pinned by hand.
5. The rule is a preregistration: changing it is a dated edit here, never a silent re-sort.
