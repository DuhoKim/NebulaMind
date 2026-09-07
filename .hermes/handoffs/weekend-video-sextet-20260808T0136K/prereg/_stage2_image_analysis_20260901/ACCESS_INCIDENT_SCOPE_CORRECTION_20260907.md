# Scope correction to the access incident — the exposure is larger and it predates the run
2026-09-07 23:32 KST / 14:32Z, stamped from `date`. HWAO. Correction by addition:
`MEDIUM_WCS_ACCESS_INCIDENT_20260907.md` (`7b33e498…`, commit `d61ca76b1`) stands as pushed.
Found by me this tick while checking whether anything else in the lane could hold the same class of
data. Metadata only — directory listings, `os.stat` and the pinned drawn lists. **No FITS byte, pixel
array, label or outcome was opened**, and none was needed.

## What the incident record missed
It audited only `OUT_A1_REPAIRED/tuning.planes/` and so attributed the exposure to the tuning fetch.
The lane also contains **`validation_bricks/`** — the Tier-C study's validation corpus: **1,885 brick
directories, 7,581 files, 23.7 GB**, image-r/maskbits/nexp-r planes plus per-brick checksums, written
**2026-09-05 02:28:45Z–07:05:31Z**, owned by `duhokim`, mode **755**. That is **two days before** this
run's input anchor, designation and draw.

Intersected with this run's pinned drawn lists:

| set | drawn | via tuning fetch | via Tier-C cache | in both | **union with pixels on this account** |
|---|---|---|---|---|---|
| validation | 2,000 | 24 | 130 | 5 | **149 (7.5%)** |
| holdout | 200 | 2 | 12 | 0 | **14 (7.0%)** |

The 121 overlapping validation brick directories each hold real `image-r` planes — 125 files,
1,490 MB — written 05:52:00Z–07:05:07Z on 09-05.

## What this changes, and what it does not
**It does not change the closure.** Attempt 2 was already void and option (A) already closed under
V15 E5(d), with A1 line 94 invalidating independently. Nothing here reopens anything.

**It changes the finding's character.** The larger part of the exposure was not created by this run at
all. Those bricks were fetched on 09-05 as legitimate Tier-C work, against a published,
checksum-identified corpus, **before this run's seed round existed** — so nobody could have known which
objects would later be drawn, and I make no suggestion that anyone peeked. But E5(d) forbids a
participant to **possess or cache** a fresh-validation-set pixel before the freeze receipts, and
possession is a state, not only an act: the moment the 09-07 draw defined the validation set, the
developing account already held pixels for 130 of its objects, in a world-readable lane directory
rather than in `/Users/nmcustody/fresh_validation_bricks/` under `chmod 700`. E5(a) is equally plain —
fresh-validation pixels are fetched only after the freeze receipts, and the journal's first timestamp
must post-date them; here the fetch predates the run.

## The real design finding, corrected and enlarged
My earlier note said a successor must fetch per-object cutouts or partition the draw by brick. That is
necessary and not sufficient. The deeper fact: **an Option-A-style fresh-validation custody boundary
cannot be hosted in a lane that already caches survey bricks for another study.** Any draw over a
catalogue whose objects live in cached bricks is exposed at the moment of the draw, by files that were
put there earlier and innocently. A successor must either draw only from bricks proven absent from
every cache on the account, or hold the entire brick cache inside the custody account from the start,
and the check belongs **before the draw**, not before the fetch.

**Preserved:** nothing deleted or moved; `validation_bricks/` is Tier-C's corpus and is referenced by
signed V15 (`_bricks_without_r_coverage.txt`) and by the Tier-C mini-prereg, so it is not mine to
remove. This is a factual report, not a proposed remedy.
