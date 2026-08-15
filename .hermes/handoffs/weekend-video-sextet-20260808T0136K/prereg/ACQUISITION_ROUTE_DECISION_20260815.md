# Acquisition route decision — Globus bulk transfer, local cutting

**Decided:** 2026-08-15 KST by Duho, verbatim: *"skip the post and follow the documented route"*.

## Why no query was sent

The drafted forum post was **not sent**. Reading the group first found
`decam-legacy-survey` thread "NERSC cutout service?" (May 2025), in which Andrew Engel solves
almost exactly our problem for ~16 million galaxies and writes it up *"for anybody who might find
it useful in the future"*. Asking would have required the community to re-explain its own archive.

## The documented route, from that thread

- **Transfer the image files from NERSC via Globus**, then generate cutouts locally.
  Dustin Lang: *"your Globus transfer is going to be by far the most time-consuming part."*
- Generate with `many-cutouts.py` — *"a very simple script … just looping over entries in a table"* —
  parallelised by splitting the input table. John Moustakas offers an MPI version at
  `desihub/fastspecfit/bin/get-cutouts`.
- **Sort the input table by brick-id** so each process works its own bricks and hits the cache.
  Andrew Engel reported **throughputs of thousands of images/sec** this way.
- **Only the image files are required**, not the full product set.
- **Brick-boundary margin (Dustin Lang):** objects near a brick edge pull data from a neighbouring
  brick, so a working set must include margin bricks — we would have hit this blind.

A separate thread records why the naive route is wrong: NERSC network operations blocks traffic
*"when they see what looks like DOS"*, and slow cutout-service downloads are attributed to
*"a lot of people trying to do bulk"*.

## Volumes and capacity

| item | figure |
|---|---|
| Globus transfer, `image-r` only | **~2.93 TB** across 270,577 files, plus margin bricks |
| local disk available | 14 TB — sufficient |
| cutting output, 128x128 one-band float32 | 54.6 GB |

## What this decision requires before any transfer

1. **Route amendment.** PC-1's delivery route changes from the cutout service to Globus bulk transfer
   plus local cutting. The v3 freeze fixed the *input contract*; this changes the *route*.
2. **PC-3 / PC-4 re-gate on the local path.** This is the substantive cost. When the survey serves a
   cutout, their service handles WCS. Cutting locally moves parity handling and fail-closed
   distortion policy **onto our code**, where it must be re-verified rather than assumed. Kun named
   this in `KUN_STRATEGY_GATE_20260815.md`.
3. **Tori's successor route binding** for the exact single-band FITS schema and brick-margin rule.
4. **Acquisition pipeline rebuild.** `nm_acquire_cutouts.py` targets the cutout service and hardcodes
   `grz`, `256`, `[3, 256, 256]`. Its custody, resume and fail-closed machinery carry over; its
   request construction does not.
5. **Globus endpoint access** — Duho's action, tied to his identity.

## Boundary

Nothing transferred. No Globus endpoint activated. `BUILD_ONLY_STOP` intact, `HOLD EXECUTION` stands,
K-8 untripped. No real-sky statistic exists.
