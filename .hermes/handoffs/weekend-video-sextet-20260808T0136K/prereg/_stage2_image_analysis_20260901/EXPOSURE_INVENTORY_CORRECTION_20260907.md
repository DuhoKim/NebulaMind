# Correction to BEGUN_RUN_EXPOSURE_INVENTORY_20260907.md — the exposure is pixels, not identities
2026-09-07 22:52 KST. The inventory (commit `2ea0bb719`) is preserved as written; this correction
attaches to it. A record is corrected by addition, never rewritten.

**What the inventory got wrong.** It listed holdout (200) and validation (2,000) as "catalogue IDs only
— A1 line 92: not opening". That conclusion was inferred from the **absence of label and outcome
files**. Absence of labels is not evidence about pixels, and the fetch is whole-brick: the tuning fetch
put the **pixels of 2 holdout objects and 24 validation objects** on this account's disk, in 25 shared
bricks, 75 plane files, 307.8 MB, written 12:32:32Z–12:45:58Z, owner uid 501.

**Corrected exposure table**

| exposure | count | kind |
|---|---|---|
| tuning identities with labels | 400 | labels read (values ∈ {−1, +1}) |
| holdout objects with **pixels on disk** | 2 | whole-brick fetch, no W, no opening record |
| validation objects with **pixels on disk** | 24 | whole-brick fetch, before any freeze receipt |
| remaining holdout identities | 198 | catalogue IDs only |
| remaining validation identities | 1,976 | catalogue IDs only |
| bricks fetched | 398 | 25 of them shared with holdout/validation |

**What the inventory's arithmetic was for, and why it no longer applies.** It computed the cost of
excluding the 400 label-exposed tuning identities from a future draw (effective pool 7,283 → 6,883).
That exclusion addresses label exposure only. It does not address this event, and no exclusion list can:
under V15 E5(d) the pixel access **voids attempt 2 and closes option (A)** for the begun run, and A1
line 125 forbids an amendment from curing prior exposure or restoring an expended attempt. The
exclusion arithmetic is retained as a fact about the pool, not as a proposed remedy.

Full finding, quoted clause and consequence: `MEDIUM_WCS_ACCESS_INCIDENT_20260907.md`.
