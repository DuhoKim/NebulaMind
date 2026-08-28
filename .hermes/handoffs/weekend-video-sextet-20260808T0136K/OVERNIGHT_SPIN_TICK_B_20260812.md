# Autonomous spin — tick B status (13:21 KST, 2026-08-12)

All five seats idle, none stuck, none dead. Everything tick A started has landed. **The tick's
substantive event is a hard negative result from Yui that changes the feasibility picture.**

## Yui's measured retention — the deterministic instrument is dead as a yield instrument

`prereg/YUI_PRODUCTION_ESTIMATOR_RECEIPT_20260812.md` (supersedes Appendix A), machine results in
`prereg/receipt_results.json`, runner `prereg/yui_receipt_run.py`.

**He refused to measure the primary classifier rather than fake it.** The frozen architecture needs a
torch training stack; it is absent, and installing it is a download, which the order forbids. His words:
*"I will not substitute a stand-in network and call it the production instrument."* So Kun's freeze
arithmetic — parent × measured lower-bound retention ≥ 100,000 — **has no valid retention input.**

**He did measure the secondary deterministic instrument, properly, and it fails:**

- τ = 5.916, calibrated on **8,000** frozen nulls (the spike used a thin **240**)
- retention on 12,000 held-out spirals: **central 0.13%, lower 95% bound 0.089%**
- **inverted in S/N** — 0.41% at S/N 2–5, 0.077% at 5–10, **0.0% at S/N ≥ 10**

That inversion is the diagnostic: retention *falling* as signal improves means the acceptances are noise
excursions, not detections. **The spike's ~7.8% acceptance was an artifact of its thin null calibration.**
At 0.00089, no plausible parent count approaches 100,000 accepted.

**Consequence:** feasibility now rests entirely on the unmeasured primary classifier — which Yui names
as *"precisely the optimistic-assumption trap this receipt exists to close."* No retention figure may be
frozen until the primary is trained and measured.

## Also landed since tick A
- **Goru's four cut defects fixed** (`df08a525…`): south-only, `maskbits=0`, `r<17.7`, the −99 photo-z
  sentinel, `FLUX_R>0`. Tori re-gated and confirmed all four; all cut counts remain `[UNKNOWN]`.
- **Tori superseded her own binding receipt** (`3f41b6d9…`, 32,888 B, hash verified independently),
  removing an incorrect claim that Lana's §0/§6 repair was her prerequisite. She also declined to claim
  Kun's gate covered Goru's current hash, since it predates it.
- **Kun's prereg gate:** `PASS AS A PREREGISTRATION DRAFT STRUCTURE; HOLD FREEZE`. No value silently
  frozen ahead of its evidence.

## Two decisions now blocking, both Duho's
1. **DR10.1 parent row count** — a catalogue query. Computes no handedness, no statistic, no positions,
   but touches the real catalogue. Not crossed.
2. **Torch dependency install** — a download, needed to train and measure the primary classifier. This is
   now the *critical path*: without it there is no retention number, and without that no freeze.

## Boundary
Held. No sky run, no real-galaxy handedness, no sky statistic, no bulk acquisition, no downloads, no
publishing, no commits.
