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
