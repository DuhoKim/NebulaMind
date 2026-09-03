# RESUMPTION NOTE — pre-compaction, written 2026-09-03 19:32 KST (Hwao, DESI lane; Blanc's ask 19:32 KST)
Everything below is on feat/paper-workflow-v2 unless marked _tmp (gitignored, on disk in this lane dir).
Standing rules unchanged: rulings only via Blanc's RELAY FROM DUHO; referees ONLY through
/Users/duhokim/HermesOps/scripts/nm_referee_dispatch.sh (ACCESS_SHA proof or no verdict); seat dispatches
with stdin closed; no kimi via --provider nous; audio: NM_SAY_NO_PLAY=1, digits, g graphic per slide (hold
lifted 10:56); git from the repo root; commit+push every draft/report as it lands; NO real pixel until every
pre-pixel gate passes; validation only (ruling "a"), nothing feeds the flagship.

## Frozen / signed state
* Mini-prereg **V11 SIGNED** 15:57:27 KST (MINI_PREREG_V11_FREEZE_RECORD_20260903.md; V10 superseded):
  coverage plane = exposure count (nexp-r); manifest v3 = image-r + maskbits + nexp-r; §7.11 three planes;
  invvar partial disclosed as known extras.
* Successor prereg: V134 P0-signed; **V135, V136 chat-signed** (BS-2v, BS-2a filled); **V137 drafted +
  SIGNABLE (AGY_V137_REFEREE_20260903.md, digest 9f2b4893…) but HELD** — Duho has BS3G_HEADROOM_MEMO_20260903.md
  (options i/ii/iii; recommended ii = fixture a₀ 0.95, Γ 0.10 → re-draft V137-H) and has NOT yet chosen.
  Pinned tooling: seal_gate V4 (SEAL_GATE_PIN_20260903.md is V3; V4 refereed via V11 rounds), renderer +
  anchor gate (RENDERER_ANCHOR_PIN_20260903.md), completeness gate 2-worker (COMPLETENESS_GATE_PIN_2W_20260903.md),
  local-sweep fallback (COMPLETENESS_FALLBACK_PIN_20260903.md), BS-3g tooling (BS3G_TOOLING_PIN_20260903.md).

## Mid-flight (live numbers at 2026-09-03 19:32 KST)
1. **Definitive TAP crossmatch (2 workers, Duho override #68):** chunks admitted 8933/8933; run_full.py pid 50535
   is in FINALISATION (stitch + §5 receipt); receipt expected at
   completeness_gate/artifacts_full/completeness_receipt_<UTC>.json (currently: none yet); wrapper
   completeness_gate/run_full_resume.sh --workers 2, pid file _tmp_run_full.pid; log completeness_gate/run_full_resume.log
   (its 'EPOCHSECONDS' line is the OLD first-launch error, not current). On receipt: verify funnel + 13,725
   dispositions terminal → commit receipt + pair list + checkpoint (force-add jsonl) → report to Blanc.
2. **Companion planes (post-V11 chain, _tmp_post_v11_chain.sh pid _tmp_post_v11_chain.pid; log
   ../_successor_build_20260824/acquire/tier_c_post_v11_chain.log):** nexp-r receipts 17947/17947 (complete), maskbits receipts 4209/17947 (running,
   4 workers); journals ../_successor_build_20260824/acquire/tier_c_fetch_receipts_nexp-r.jsonl / _maskbits.jsonl; DONE file ../_successor_build_20260824/acquire/tier_c_planes_DONE.txt.
   Then the chain runs **seal gate V4** automatically: seal_gate/seal_gate.py --manifest tier_c_manifest_v3.json
   --journal tier_c_fetch_receipts.jsonl --maskbits-journal … --nexp-journal … --known-extras-journal
   tier_c_fetch_receipts_invvar-r.jsonl --fetch --append → receipt seal_gate_receipt_v4_<ts>.json, log
   seal_gate_v4_run.log, appends to seal_journal_tierc.jsonl (6 records now). Invvar partial (2,693 files)
   ARCHIVED at ../_successor_build_20260824/acquire/bricks_tier_c_invvar_partial_ARCHIVE/ (never delete).
3. **GZ1 sweep fetch (Duho #65, 8 adaptive workers):** sweeps/fetch_sweeps.py --footprint a, pid _tmp_sweep_fetch.pid,
   data sweeps/data ( 44G), journal sweeps/sweep_fetch_receipts.jsonl (OK 28/352), log sweeps/sweep_fetch.log;
   ~12.5 GiB/h → ETA ~01:06 KST 09-05 for 405 GiB. Fallback route PINNABLE (not used tonight).
4. **BS-2c count run** (_finish_bs2c.py, since 09-01, ~2 days): still running; leave it.

## Monitors (this session) and wakes
* Monitor bdyk9z2yr — crossmatch progress/exit (follows _tmp_run_full.pid).
* Monitor bxeyxny3s — post-V11 chain progress/exit + seal V4 receipt summary.
* Monitor bksb5h718 — sweep fetch progress/worker events/exit.
* Shell waiter bkpql96nx — run_full.py exit → receipt summary.
* One-shot wakes: 19:47 (receipt), 21:07 (seal gate V4), 22:07 and 23:47 (receipt fallbacks).
All are session-only; after compaction re-arm what is missing (CronCreate) and re-read the pid files.

## Waiting on Duho (via Blanc)
* BS-3g headroom choice (i/ii/iii) → then V137 hand-off (digest 9f2b4893…) or V137-H re-draft + referee.
Recorders staged: _tmp_record_v136_signature.py pattern (copy for V137); _tmp_record_v11_signature.py (used).
