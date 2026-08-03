# H6 receipt — adversarial audit of P1 invariant manifest + RCA

- brief: `H6_BRIEF.md`, burn `fable-weekly-hard-burn-20260711T035354Z`
- status: **COMPLETE**
- t_ack: 2026-07-11T04:13:19Z; t_finalize: 2026-07-11T04:32:32Z (cap: ACK+35min / absolute 04:45:00Z — finished ~12 min early)
- headline deliverable: `P1_INVARIANT_RCA_ADVERSARIAL_AUDIT.md` — packet verdict **PASS-WITH-FIXES**; 8 findings (1 MAJOR: RCA carry counts 102/103 are wrong under the manifest's own rule → 92/105 c6, 102/105 c7; 3 MINOR: identifier-digit token contamination ×2, near-miss clause unenforceable; 4 NOTE). All 5 check families run; custody 100% clean; RCA evidence chain E1–E7 reproduced from raw hash-verified bytes.

## Input custody (pinned in brief vs recomputed before use)

| file (prior burn root, `p1-rp1-invariants/`) | pinned sha256 | recomputed | verdict |
|---|---|---|---|
| `INVARIANT_MANIFEST.json` | `f4eb857e8cc2002208b1d89a8c517d30e044ed5f7c08a3dab976c0bd7556c717` | same | MATCH |
| `RCA_NUMERIC_DRIFT.md` | `45223b5690d33d770b6b3e2905d8f05746adec7b37e6052a6a18caed65cf0096` | same | MATCH |
| `INTRODUCTION_LITERATURE_REFERENCE.md` | `874794a1ea1202ceebace131ce31d46fd9587d6aedde9db1e600ae9cfe07713d` | same | MATCH |
| `P1_RECEIPT.md` | `bdfebdc10c3166f045e3d3f9edf9804c87ee546d2f0cfd664e83930020fe763a` | same | MATCH |

All four usable; no fail-closed exclusions needed. Additional read-only inputs (required by check families 2/3/5): the packet's own `sources-snapshot/` copies (12/12 sha256 = receipt-claimed hashes), `tools/build_manifest.py`, `P1_ACK.md`, P1 done marker (all bytes+sha = receipt claims), and — observationally — the 13 live originals under the sprint/runs trees incl. `matched_agn_sf_pairs.csv` (13/13 still match the receipt/custody hashes; CSV parsed read-only to verify RCA §2.5).

## Produced files (all inside `<own>` = `h6-p1-invariant-rca-audit/`)

| file | bytes | sha256 |
|---|---:|---|
| `H6_ACK.md` | 72 | `c31c50d1b27c517605fdb7df2d9c93128239e2369db03c95149197e4a6f1fc70` |
| `P1_INVARIANT_RCA_ADVERSARIAL_AUDIT.md` | 18,444 | `6b4ec32f32fda49dde99fbf8e332fb54d1628d1f963dff7d1c823e092cd62208` |
| `tools/h6_audit.py` | 16,243 | `197ec5418e9e3ef1520041ea37d5d7f5e0f611c3041b549dc5e18ef568d95424` |
| `tools/h6_audit_output.txt` | 26,101 | `c4f957bc8f6d2444481a7163244177ee7785caec35477141ea0cd1705e76605c` |
| `H6_RECEIPT.md` | — | (this file; self-hash n/a) |
| `FABLE_HARD_BURN_H6_DONE_20260711T035354Z` | 0 | (empty marker, created after this receipt) |

## Poll log (`GLOBAL_STOP_20260711T035354Z.md` / `HOLD_5H_20260711T035354Z.md` at burn root)

| time (UTC) | result |
|---|---|
| 2026-07-11T04:13:19Z (ACK) | both absent |
| 2026-07-11T04:19:28Z | both absent |
| 2026-07-11T04:28:25Z | both absent |
| 2026-07-11T04:32:32Z (pre-receipt) | both absent |

## Safety attestation

- Writes confined to `<own>` (`h6-p1-invariant-rca-audit/`): ACK, audit doc, tools/ (script + saved output), this receipt, done marker. Nothing written anywhere else on the machine; no STOP/HOLD files created.
- Prior burn root and all originals untouched (read-only opens + sha256 only; live-original hashes still match their receipt values after the audit, confirming no mutation).
- Zero network calls; no browser. No runner/candidate writes, no DB/API/wiki publication, no deploy/restart, no git, no cron/launchd/background jobs, no billing/account/credential/cloud/GCP actions. No tmux send-keys; no other `h*` subdir read.
- Timestamps via `date -u`; audit script uses no clock/randomness.

FABLE_HARD_BURN_H6_DONE_20260711T035354Z
