# FREEZE — the manifest-closure mechanism, at v9

2026-08-26, Hwao. **This supersedes `FREEZE_CLOSURE_V8_20260826.md`; it does not rewrite it.**
The v8 record stands as written, including its account of why a claim known to be false was
frozen as written. v9 exists because Duho read that account and directed the claim be fixed
rather than carried. KIMI cleared v9 at 23:08 KST.

## What is frozen

| artifact | sha256 |
|---|---|
| `ref/successor_ref_v9.py` | `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148` |
| `ref/closure_worker_v9.py` | `28f8e1f9a8c7bd3d4cf1aabf71a7dfae5f9a1da6b92a6f09fd9c65bfc7ea5959` |
| `ref/FIXTURES_V9_20260826.out` | `fab32ba24cedcedf7fe601c3a8d9dbde13f57b1c9bf2e0b88963bcfebc33a8b5` |
| `gates/closure_probe_suite_v9.py` | `b218aa998ac8ef97a0c4c933d73068d18ff45ce3553cb7bc80f1fe59be8c91d7` (34 probes) |
| `gates/CLOSURE_PROBE_V9_RECEIPT_20260826.json` | `stable_sha256 687a4543d14b48120a84d6e4fbefb41826ec2f7a9a9cc9a34e0a63c6e29e9131` |
| `gates/CLOSURE_V9_KIMI.md` | `f2ee062bb7f1ced33e5530d6655765f32b5830342154274ecf885c73dc722f01` |

34/34 conforming, 13 verify hooks declared and 13 run. Closure: **65,060 objects → 6,445
selected → 12,117 required bricks**, `plan_digest aaeaa9f3…`.

## What changed from the v8 freeze

The false claim is gone. Two sentences said every receipt records the worker's `sys.path`;
after v8 none did. v9 captures interpreter state before the isolation gate and returns it beside
every result, so **W03 measures 4 entries with `isolated=True` on a closure and B04 measures 7
on a refusal**. The claim is now checked by probes rather than asserted by prose.

## The limitation, unchanged and still first-class

**One referee seat.** codex and gpt56 were refused by their provider's safety filter, twice
each, on material including their own prior reports. Duho ruled a single verdict may stand. **A
one-seat review is a narrower review, not a stronger one**, and anything citing this freeze
should carry that sentence with it. Five rounds of history remain legible: v4 (two seats, both
NOT CLEAR), v5 (NOT CLEAR), v6, v7, v8, v9 (CLEAR with conditions). v4–v8 are unmodified on disk.

## Known-open — carried, not closed

1. **KIMI-V9 F3, and it is this round's own shape.** "even a refusal carries it" holds for the
   isolation refusal and every closure refusal, but **five other early `fail()` sites carry no
   interpreter state**: subject missing, subject digest mismatch, stdin not JSON, stdin lacking
   `manifest`, non-list manifest. The repair is one argument each. A round whose purpose was
   making two sentences true left the same sentence shape half-true on the same file.
2. **The frozen planner's three files** are verified and consumed by distinct reads.
3. **Three fingerprint blind spots** — module-as-value, class-method-reachable helper, C callable.
4. **The site-packages residual**: numpy, astropy (the sidecar's parser), erfa, scipy, yaml all
   resolve from the unpinned user directory; CLT site-packages precedes the add-back.
5. **Six `varies` strings**, B06's vacuous hook, F05's basis — named four times, never fixed.
6. **No worker timeout**; extra stdin keys ignored; manifest-type refusal on the WORKER-ERROR
   channel.
7. **R06's thin payload**; no frozen phase-aware refusal schema; `require_environment()` unused.
8. **The selection has no producer receipt** (CODEX-V5 F6) — the one item here that gates
   acquisition rather than merely being recorded.
9. **Bookkeeping**: the brief's question block is v8's verbatim and cites a probe removed in v7;
   the suite's text names stale versions in places.

## What this freeze is not

- **Not authorization to fetch.** No image byte fetched. The ≈148 GB ceiling is a planning
  decision; BS-6 gates the first byte and item 8 is unresolved.
- **Not a frozen preregistration.** It fills **BS-2m** — one of twelve class-P slots.
- **Does not settle power.** Stage P is *measured* (995/1000, exact per-trial nulls) but lives in
  a harness, not the frozen code. **BS-5p remains unfillable.**

## Why it stops here

Five rounds. For the last four, the only defects in the artifacts were mine, introduced while
repairing. Mechanism findings have been minor-only for three. The defect rate I add now exceeds
the rate the repairs remove — which is an argument about my error rate, not about the mechanism
being finished, and it is the honest reason to stop.
