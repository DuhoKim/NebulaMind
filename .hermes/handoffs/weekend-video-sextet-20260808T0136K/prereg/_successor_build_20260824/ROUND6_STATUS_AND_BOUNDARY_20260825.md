# ROUND-6 STATUS — what six gate rounds settled, and the boundary drafting has reached

Hwao, 2026-08-25 14:40 KST. For Duho. Nothing here asks to run anything.

## The state, plainly

The successor preregistration is **drafted** (V7, sha `f15b0b4d…`) with a pinned reference
implementation (`ref/successor_ref_v3.py`). It has been through **six adversarial gate rounds
across two engines — twelve reports, every verdict line REFUSED.** No PASS is claimed.

That is not failure; each round killed real defects. But round 6 exposed a boundary worth your
decision rather than another silent iteration.

## What the gates killed today (V6 → V7)

- **The manifest-closure repair you directed did not work in V6.** Both gates defeated it:
  hand the checker a planner map that omits a parent object, or one returning only home
  bricks, and a short manifest passed with a clean receipt. It compared a manifest against *an
  answer the caller supplied.* Now the planner is implemented and `close_manifest()` derives
  the required set from the frozen parent itself. Both attacks are negative fixtures.
- **The same hole then reappeared one level up** (codex, round 6): the parent *digest*, the
  brick *universe*, and the cutout *half-size* are still caller-supplied, so a caller who
  regenerates all three from a shortened parent passes. This is the hash-chain lesson again —
  a digest supplied alongside its own data proves consistency, not custody.
- Calibration returned raw agreement instead of the inherited HC-1H estimator; the allocator
  ignored the 30-per-stratum floor; `decide()` had a test seam through which both gates
  extracted a verdict with every guard monkeypatched; the raw/retained boundary still flipped
  the algorithm at 17-raw/16-retained. All repaired and fixtured.
- **A plain error of mine:** `CUTOUT_HALFSIZE_DEG` was 0.0186 while its own comment implied
  0.004658 — a 3.99× discrepancy. Now derived from `CUTOUT_PIX` and the pixel scale, never
  typed. (It erred toward over-inclusion, so it would have wasted bytes rather than caused a
  shortfall — but it is exactly the class of constant that caused the 60,310 gap.)

## The finding I consider most important, and it is against my own work

To make the power gate executable I first used a normal-tail critical value. Written as a
*universal* contract rather than a sampled one, the fixture failed its author: on **polar
geometry with imbalanced signs — the geometry this design selects** — the normal threshold is
anti-conservative. I replaced it with a measured null rather than tune an inflation factor.

Round 6 says the measured null is *still* not conservative enough, and **my own fixture now
demonstrates it: 21 of 22 Stage-P successes were confirmed by an independent Monte-Carlo test.
One was not.** The current pinned fixture output records that failure
(`ref/FIXTURES_V3_20260825_ROUND6.out`, exit 1) rather than a green transcript.

## The boundary

The remaining blockers split cleanly:

**(a) Closable by writing** — Stage-C/production type enforcement (done this round), slot
schemas, the battery's floor-edge case, allocator feasibility, planner digest completeness, RA
wraparound. Ordinary work, a few hours.

**(b) NOT closable by writing.** Binding the parent digest to a real BS-2s artifact, binding
the brick universe to a real release manifest, an actual availability probe for the DR11/
DR10.1 resolver, and tightening the power contract against the *real* accepted geometry — all
require class-P receipts that do not exist yet. They need the release decision (your Sep-5
fork) and a first authorized data step (a paced, receipted catalog fetch — no images).

In other words: **the draft has been hardened to the point where further hardening needs
data.** Six rounds got it here; a seventh would circle category (b) without being able to
close it.

## What I am not doing

Not running anything. Not fetching. Not freezing. Not asking to. The drafting authorization is
"writing only, its own gates before any data," and that boundary holds exactly where you set
it. The methods-note and strata questions remain untouched and undecided.
