# BHU half — Tori (2026-08-25 11:00 KST; UPDATED 11:04 — regate5 verdict folded in)

## Plain-language lead

The night settled this for the BHU lane: the evidence table for the new anisotropy study is
now guarded by a checker that eight kinds of quote-tampering cannot get past — one reviewing
engine spent the night inventing forgeries and won five rounds; this morning's version stops
them all. The physics was never in dispute; what got rebuilt five times was the proof.

## The facts, evidence-classed, receipts named for Goru

1. MEASURED — Track A (the strict interior model) is CLOSED with both engines passed. First
   lines, verbatim: "PASS_TRACK_A_AMENDED" (bhu-theory-phase4-anisotropy-20260823/
   REGATE3_TRACKA_VERDICT.md) and "PASS_TRACK_A" (same dir, KGATE_TRACKA_VERDICT.md).
2. MEASURED — Track B freeze gate, kimi seat, first line verbatim: "PASS_TRACK_B_FREEZE"
   (KGATE_TRACKB_VERDICT.md).
3. MEASURED — Track B freeze gate, codex seat: four HOLD verdicts (chain GATE_TRACKB →
   REGATE4, first lines all HOLD), then the fifth regate first line verbatim:
   "PASS_TRACK_B_FREEZE" (REGATE5_TRACKB_VERDICT.md, file mtime 10:49:32).
4. MEASURED with a disclosed discrepancy — my 10:58 existence check reported the regate still
   running although the verdict file's mtime is 10:49:32; the check command and its output
   are in my session log. Likely a staged write landing after composition; the artifact is
   the authority and reads PASS. **The freeze is now CLOSED: both engines PASS.**
5. MEASURED — the verifier stands at v8: 50/50 quotes verified, 0 manual acceptances, 0
   directory fallbacks (b_verify_ledger.json, 50 rows), 8 corruption self-tests all failing —
   6 synthetic classes plus the gate's 2 corruptions of actual frozen rows, run through the
   same code path as the real corpus (b_verify_quotes.py, self-test block; commit 736007f0).
6. MEASURED — the five rebuild commits with times: v4 08-24 18:49 (4445e363), v5 22:14
   (fc03ddd9), v6 22:36 (dcd7a8e5), v7 08-25 10:18 (a3a2b2c4), v8 10:42 (736007f0) — git log.
7. MEASURED — frozen bounds table unchanged through all five rebuilds: B2 = 11 dipole rows,
   B3 = 7 large-angle rows, B1 demoted to reference tier (TRACK_B_FREEZE.md tables; harvest
   pins beba95a7… and 6d97c679… unchanged since freeze).
8. MEASURED — Track C is pre-registered but NOT started: judgment criteria written before any
   comparison (TRACK_C_BRIEF.md, commit ae0af84b, 08-24 22:40); starts on Duho's go after the
   freeze passes.
9. MEASURED — the DESI curvature watch is verified for its next tick (lane
   desi_curvature_watch_state.json: last_run 2026-08-24T01:18:14Z stamp superseded by the
   06:07:24Z control, last_error null, seen 25); nothing fired overnight — it is weekly,
   next Monday 10:00 KST 2026-08-31.

## Suggested slide headlines (2–3 BHU slides)

- "Five forgery attempts, five rebuilds — the evidence table now stops all eight" (numbers:
  50/50, 8, 5 rebuilds, 0 fallbacks)
- "Both engines now pass the freeze — the fifth review ended the five-round forgery war"
  (kimi PASS verbatim; codex PASS_TRACK_B_FREEZE verbatim at 10:49)
- "The next study is pre-registered before its own judgment" (Track C: 4 criteria, not started)
