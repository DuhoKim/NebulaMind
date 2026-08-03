# H7 receipt — Adversarial audit of P2 source ledger + debate map

Brief executed: `briefs/H7_BRIEF.md` (burn `fable-weekly-hard-burn-20260711T035354Z`)
ACK: 2026-07-11T04:13:19Z · Finalized: 2026-07-11T04:34Z · Hard stop honored: absolute 04:45:00Z (earlier than ACK+35min = 04:48:19Z); finalization began 04:33:48Z, inside the reserved 5-minute window.

- **status: COMPLETE** — all six check families executed in full; headline audit verdict: **PASS-WITH-FIXES** (0 BLOCKER, 0 MAJOR, 2 MINOR, 2 NOTE; zero count mismatches).

## Input custody (pinned vs recomputed, before use)

All under `fable-weekly-burn-20260711T010503Z/p2-cycle7-source-ledger/`:

| Input | Pinned sha256 (brief) | Recomputed | Bytes | Verdict |
|---|---|---|---|---|
| `SOURCE_LEAD_LEDGER.json` | `faadcc22f20e0037771f55e84e624a782ed93257716a779205dd6f5563ab0d07` | identical | 48925 | MATCH — used |
| `AGN_SFR_STATUS_DEBATE_MAP.md` | `8f3d33429bd70b372887fca3115e813189395d1203eff3f410344da64d0aafee` | identical | 13706 | MATCH — used |
| `PRIOR_WORK_COMPARISON_CANDIDATE.md` | `2545c71295d1c51fd4593a1ce0000cf6b7450d7db03e2fa32f7c6a1061414035` | identical | 9570 | MATCH — used |
| `P2_RECEIPT.md` | `ddcb5eaa74abaf849953d3728d15b53f23dd9f3e07a73fe5a9001863934bd83a` | identical | 11008 | MATCH — used |

No mismatches; nothing treated as unusable. Additional read-only inputs consulted for the audit (all inside the prior burn packet or paths listed by `P2_RECEIPT.md` itself): the 13 `sources-snapshot/` files, `P2_ACK.md`, the P2 done marker, and the receipt's source-table live originals — every recomputed hash matched the packet's claims (details in the headline audit, Check 6).

## Produced files (this lane, `h7-p2-ledger-debate-audit/`)

| File | Bytes | sha256 |
|---|---|---|
| `H7_ACK.md` | 72 | `4321e98ce624e34c7b018bb1ffc66a5895a4c523a709eec4b259e299c4cbcdc4` |
| `audit_checks.py` (mechanical checks, read-only on inputs) | 6447 | `127b5bcc64ce4195f818e3245231f1dd583132bf7f261adf6467fe241cb13868` |
| `P2_LEDGER_DEBATE_ADVERSARIAL_AUDIT.md` (headline) | 13942 | `d7bb37d644570f6470e780010cc3e8ea379ed9b4d391ba26d1e73ceb0376d179` |
| `H7_RECEIPT.md` | (self) | (self — hash not applicable) |
| `FABLE_HARD_BURN_H7_DONE_20260711T035354Z` | 0 | (empty marker, written immediately after this receipt) |

## Poll log (GLOBAL_STOP / HOLD_5H, burn root)

| UTC | GLOBAL_STOP_20260711T035354Z.md | HOLD_5H_20260711T035354Z.md |
|---|---|---|
| 2026-07-11T04:13:19Z (ACK) | absent | absent |
| 2026-07-11T04:25:39Z | absent | absent |
| 2026-07-11T04:27:00Z (between custody + spot-check steps) | not re-listed (covered by adjacent polls) | not re-listed |
| 2026-07-11T04:29:44Z | absent | absent |
| 2026-07-11T04:33:48Z (final, before receipt) | absent | absent |

All explicit polls: both markers absent; interval between explicit polls never exceeded ~5 minutes across the working window.

## Safety attestation

- No writes outside `<root>/h7-p2-ledger-debate-audit/`; no STOP/HOLD files created; T0.md, `briefs/`, other `h*` subdirs untouched and (other `h*`) unread.
- Prior burn root touched **read-only** (hash recomputation, line reads); byte-identical before/after by construction — no write operation was issued against it.
- Zero network calls; no browser. No runner/candidate writes, no DB/API/wiki publication, no deploy/restart, no git commands, no cron/launchd/background jobs, no billing/account/credential access, no cloud/GCP.
- Lead content verification (external literature truth) was NOT attempted — internal-integrity audit only, per the brief's binding boundary.

FABLE_HARD_BURN_H7_DONE_20260711T035354Z
