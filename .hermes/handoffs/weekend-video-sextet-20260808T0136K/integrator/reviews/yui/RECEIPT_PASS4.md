# RECEIPT — integration pass 4 (integrator/)

Seat `yui-video-integration`, 2026-08-08 02:34–02:42 KST (stamps from `date`).
Authority byte-unchanged: order `ac5d3531…`, DELEGATION, COORDINATION_UPDATE.

## What changed and why

- **Fresh QA on canary v1 (0204)** at pass start: PASS, bit-stable third run in a row.
- **The one evidence-backed correction — canary v2
  (`canaries/spin-method-canary-20260808T0235/`)**: v1's funnel card claimed sequential
  narrowing that `T1_FUNNEL.json` does not state (readouts are parallel siblings). Card 5
  redrawn as parallel branches, adopting the spin worker's independently validated
  parallel-readouts structure with credit; all other cards text-identical. Guard 11/11 twice;
  full §5 receipts (RECEIPT.md, QA.md with PASS verdict, hashes.txt, ffprobe.txt,
  contact-sheet.jpg) inside the canary dir. **v1 preserved unchanged** as the failed-candidate
  record.
- **`reviews/yui/audit_canary.py`** (new): parameterized canary QA runner generalizing the
  pinned `audit_pass2.py`; ran on v2 (PASS) and appended v2 to `qa/ENCODED_AUDIT.json`.
- **Requests**: spin lane's method-only proposal reviewed in full — CONCUR, reply at
  `requests/REPLY_spin-parity_20260808T0240K.md`; c41-uvlf pass-3 discrepancy resolved by their
  v7 packet — ack at `requests/REPLY_c41-uvlf_ACK_20260808T0240K.md`. Hwao-only decisions
  (deck-of-record structure, shared-renderer primitives, v7 acceptance) escalated in
  STATUS/ledger, not acted on.
- **`INTEGRATION_LEDGER.md`** pass-4 entry appended; **`STATUS.json`** refreshed.

## Preserved, not touched

Canary v1 and all its receipts; every lane candidate incl. held/failed; failed proposal
iterations; pre-order `lanes/*`; repo `tools/`; public MP4s; all prior replies and receipts.

## Hashes

See `hashes_pass4.txt` beside this receipt.

## Gates

No publication, shared/public asset writes, TTS, Git writes, or browser automation. No halt
condition hit. Window end 2026-08-10 07:00 KST.
