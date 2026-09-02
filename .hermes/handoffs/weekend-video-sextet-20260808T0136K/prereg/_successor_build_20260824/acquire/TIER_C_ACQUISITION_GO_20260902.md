# TIER-C ACQUISITION — GO RECEIPT

**Started** 2026-09-02 ~14:40 KST. **Authorization chain:**

1. Duho's task (2026-09-02, via Blanc, direction #54): "measure galaxy spin for
   overlapped galaxies with Galaxy Zoo and compare with GZ label" — step-1
   recon delivered, `CODEX_GZ_SPIN_RECON_20260902.md`, recommendation (i).
2. Duho's ruling (2026-09-02 13:49 KST, via Blanc, direction #55, verbatim "as
   Hwao's rec"): choice 2 — verify, then go. agy confirmation ⇒ path (i)
   ADOPTED and the Tier-C brick acquisition AUTHORIZED to start without a
   further round-trip. Tier B held. Tier A untouched. Mini-prereg still returns
   to Duho for signature before any measurement.
3. agy verification landed 14:01 KST: `AGY_BC_VERIFY_20260902.md`,
   **VERDICT: CONFIRMED** — Tier B exact (8,465/6,770/845/346), Tier-C
   geometric ceiling independently rebuilt (23,257 high-conf vs codex 23,254),
   brick cost independently 210.06 GiB (+1.0% vs codex 207.97), Stripe-82 and
   median-Dec sky claims confirmed.

## What is being fetched

* Manifest: `tier_c_manifest_v1.json` — **17,947 bricks**, sha256
  `b4f189a8c260f74d8bf3da2bfc189bbdc3db232f83c9a57dbdf7cb001ba89bbe`.
  Derived from the recon's audited match table under the audited 1.0″ rule:
  Tier-C high-confidence objects (23,237) → 19,614 distinct primary bricks,
  minus 1,667 already held. **Deliberately superset-leaning** (~212 GiB est.
  vs codex's verified-set 207.97): the extra ~4 GiB buys coverage for the
  complete-match sample the mini-prereg requires when the r<20 accelerator is
  cured; extra bricks are inert bytes under an acquisition-only scope.
* Destination `bricks_tier_c/` + journal `tier_c_fetch_receipts.jsonl`, kept
  separate from the #52 closure so its zero-extra-files invariant stays
  checkable. Same downloader (`fetch_bricks.py`, now parameterized;
  the #52 defaults are untouched), same NERSC path, same per-brick published
  SHA-256 verification, same pacing: 4 workers, 0.5 s delay.

## Scope

**ACQUISITION ONLY**, same boundary as #52: no cutouts, no instrument, no χ,
no handedness label. The measurement itself waits for Duho's signature on the
mini-preregistration (`MINI_PREREG_GZ_TIERC_DRAFT_V1_20260902.md`, drafted,
not yet refereed).

## Disclosed operational defect (mine)

The two watchers armed to fire this go both polled
`pgrep -f "agy --dangerously"` — a pattern each watcher's own command line
contains. They matched each other, reported agy alive after it had exited
(~14:01), and would have waited forever. Caught at 14:2x by noticing the
"running" process's cwd never changed; both were killed and the fetch was
launched directly after re-reading the final verdict. Nothing was fetched
before the verdict was final. Lesson recorded: process-liveness patterns must
be self-excluding (`pgrep -x`, or a `[c]haracter-class` breaker).

First 31 bricks: all `OK`, checksums matching. ETA at the #52 measured rate
(~960 bricks/hr): **~18.7 h**.
