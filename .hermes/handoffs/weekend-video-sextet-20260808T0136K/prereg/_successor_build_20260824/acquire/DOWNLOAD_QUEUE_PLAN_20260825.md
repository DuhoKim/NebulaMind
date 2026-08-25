# IMAGE DOWNLOAD — QUEUED, GATED ON THE CLOSURE CHECK

Duho, 2026-08-25 ~18:30 KST: *"queue the download after the closure check clears."*

**Nothing downloads until the closure check clears an independent referee round.** This file
records the plan, the gate, and the order — so the gate is a state of the world, not a memory.

## The sequencing problem, stated first

The 6,445 selected bricks are the bricks whose GALAXIES we want. They are **not** the images we
need. Each galaxy's cutout may require neighbouring bricks that lie OUTSIDE the selection —
that is the whole content of the closure property, and the exact gap that ended the
predecessor (manifest 60,308, parent needed 60,310).

So the image manifest cannot be derived from the brick list. It has to be derived from the
GALAXIES, and that needs their sky positions.

## Order of operations

| # | step | authorization | status |
|---|---|---|---|
| 1 | Fetch catalogue positions (ra, dec, ls_id) for the ~65,060 galaxies in the 6,445 selected bricks | catalog-only step, authorized 2026-08-25 | to run |
| 2 | Run `close_manifest()` over those galaxies with the FROZEN planner → the image brick list, with counts in the receipt | none needed (local) | after 1 |
| 3 | **GATE:** independent referee round on the closure check and its output | — | **blocks step 5** |
| 4 | Build the transfer manifest + approval file (byte ceiling, digest-pinned) | prepared, not executed | after 2 |
| 5 | Launch the paced, receipted transfer | **queued — fires only on a clean step 3** | BLOCKED |

## Why step 3 is the gate and not a formality

The closure check has failed twice in one day: it returned only the home brick for both
historical objects (reproducing the predecessor's defect), and its first repair was wired into
a fixture while the production path still called the broken routine. Both are now fixed and
verified against the real sky, but neither fix has survived an independent review round.
Downloading against an unconfirmed closure is repeating the mistake that ended the last study.

## What the download is, when it fires

- Source: the release's coadd image tree, r-band, exactly the bricks the closure names.
- Scale: order 77 GB (≈6,445 bricks at the predecessor's measured 12.2 MB/brick, plus edge
  neighbours the closure adds).
- Transport: `_tori_transfer_20260819/nm_image_transfer.py`, which moved 60,308 files with a
  60,308/60,308 producer-checksum match and zero quarantines. Paced, receipted per file, under
  a pre-fixed byte ceiling, refusing any file not in the digest-pinned manifest.
- Blinding: images are bytes. Downloading them does not touch the blinding. Computing spins
  from them does, and that is not authorized and not queued.

## What is NOT authorized by this

No cutouts, no spin measurement, no statistic, no freeze. The rulebook remains a draft under
review.

---

## GATE RESULT 2026-08-25 ~19:30 KST: **NOT CLEAR — the download does not fire**

Both referee seats returned **NOT CLEAR** (`gates/CLOSURE_GPT56.md`, `gates/CLOSURE_CODEX.md`),
independently and with the same three blockers. **The queued transfer stays blocked.**

**What both confirmed works.** On the honest path, against the pinned real geometry, the two
historical objects require exactly five distinct bricks; the complete five-brick manifest
passes; and omitting either `3471m885` or `2857m870` is refused by name. The mechanism computes
the right answer.

**Why that is not sufficient to download against.** Every one of its supposed external
witnesses is still supplied by the caller:

1. **The parent is not held by a verified receipt.** `close_manifest()` takes
   `expected_parent_digest` and a `selection_receipt` dict from the caller and only checks that
   the dict says `slot == "BS-2s"` and carries a matching digest. A shortened parent with a
   regenerated digest and a hand-built dict passes. Worse, `SLOT_SCHEMA["BS-2s"]` does not even
   contain `parent_digest`, and `receipt()` returns metadata and hashes rather than the supplied
   fields — so the *canonical* receipt cannot be consumed by the routine that requires one,
   while a receipt-*shaped* dict can.
2. **The geometry is not bound to the pinned sidecar.** The object that actually determines the
   answer is whatever the caller passes.
3. **`frozen_planner_digest()` does not digest all the code that runs**, and no expected planner
   digest is enforced — so the reported digest can stay identical while different planner code
   or configuration executes.

**The pattern, stated plainly:** a witness is only a witness if the code *computes* it from the
artifact. Mine *accepts* it as an argument at every point. That is the same defect class as
rounds 6, 7 and 8, one level further out each time.

**Repair direction** (not yet implemented): recompute the sidecar digest from the file on disk
and compare to a pinned constant; load the parent from the selection artifact on disk and
recompute its digest there rather than accepting one; pin an expected planner digest and
enforce it; make `receipt()` carry the fields its consumers need so canonical receipts are
usable and ad-hoc dicts are not.

**Status: the image download remains queued and unfired.** Nothing has been downloaded.
