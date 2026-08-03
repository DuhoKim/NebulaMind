# H10 receipt — cross-packet reproducibility + integration-order audit (P1–P4)

Brief executed: `briefs/H10_BRIEF.md` (burn `fable-weekly-hard-burn-20260711T035354Z`)

- **status: COMPLETE** — all five brief checks performed (reproducibility scorecard, custody sweep, cross-packet fact table, integration-order plan with H1–H5 consumption map + hazards, gap sweep); overall verdict SAFE-TO-INTEGRATE.
- t_ack: 2026-07-11T04:14:41Z
- t_end: 2026-07-11T04:37Z (cap was absolute stop 04:45:00Z — the earlier of ACK+35min=04:49:41Z and 04:45:00Z; finished inside the reserve window)

## Input custody — pinned vs recomputed (recomputed 04:26–04:27Z; ALL MATCH)

| Input (under prior burn root `fable-weekly-burn-20260711T010503Z/`) | Pinned sha256 (brief) | Recomputed | Verdict |
|---|---|---|---|
| `BURN_ROLLUP.md` | `b15afe07317ad1a5326dfa3b873be5a4fba01bad199534da96b5d9d519e24088` | identical | MATCH |
| `p1-rp1-invariants/INVARIANT_MANIFEST.json` | `f4eb857e8cc2002208b1d89a8c517d30e044ed5f7c08a3dab976c0bd7556c717` | identical | MATCH |
| `p1-rp1-invariants/RCA_NUMERIC_DRIFT.md` | `45223b5690d33d770b6b3e2905d8f05746adec7b37e6052a6a18caed65cf0096` | identical | MATCH |
| `p1-rp1-invariants/INTRODUCTION_LITERATURE_REFERENCE.md` | `874794a1ea1202ceebace131ce31d46fd9587d6aedde9db1e600ae9cfe07713d` | identical | MATCH |
| `p1-rp1-invariants/P1_RECEIPT.md` | `bdfebdc10c3166f045e3d3f9edf9804c87ee546d2f0cfd664e83930020fe763a` | identical | MATCH |
| `p2-cycle7-source-ledger/SOURCE_LEAD_LEDGER.json` | `faadcc22f20e0037771f55e84e624a782ed93257716a779205dd6f5563ab0d07` | identical | MATCH |
| `p2-cycle7-source-ledger/AGN_SFR_STATUS_DEBATE_MAP.md` | `8f3d33429bd70b372887fca3115e813189395d1203eff3f410344da64d0aafee` | identical | MATCH |
| `p2-cycle7-source-ledger/PRIOR_WORK_COMPARISON_CANDIDATE.md` | `2545c71295d1c51fd4593a1ce0000cf6b7450d7db03e2fa32f7c6a1061414035` | identical | MATCH |
| `p2-cycle7-source-ledger/P2_RECEIPT.md` | `ddcb5eaa74abaf849953d3728d15b53f23dd9f3e07a73fe5a9001863934bd83a` | identical | MATCH |
| `p3-m3-rt-baseline/M3_ACCEPTANCE_BASELINE.md` | `d028f3c716cc123be1840170d6111c42e24693451c9d3bf90284fdb19691d433` | identical | MATCH |
| `p3-m3-rt-baseline/RT_CARDS_DEEPENING.md` | `21564dd6d78c72483087d436f4256e461913ec9ab013c4ab7053bfe14eed7e18` | identical | MATCH |
| `p3-m3-rt-baseline/P3_RECEIPT.md` | `70573e18df09cf45b73dcee5b75602541a6e33ea427dfa4b378c2f207eecd90b` | identical | MATCH |
| `p4-derived-claims/CLAIM_EVIDENCE_CANDIDATES.md` | `1c8d9a7d28566a19a957cac754a7b8c6c5981a3ad445eb3d3f9daacbd49f8b39` | identical | MATCH |
| `p4-derived-claims/P4_RECEIPT.md` | `27a1efc000a6a5044e5a9a3199e3ef22dfebe9f33d522bafd8e8e98a6909a85b` | identical | MATCH |

Done markers (custody sweep, check 2): all four `FABLE_BURN_Pn_DONE_20260711T010503Z` (n=1..4) are exactly 0 bytes with sha256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` — PASS.

Unpinned inputs — recomputed sha256 recorded (read-only):

| File | Bytes | sha256 (recomputed 04:26Z) |
|---|---:|---|
| prior root `P4_CONDITION_PACKET.md` | 1,892 | `738af1cbba1d315b6e85f3aec443be34b7c2bec374316db260b4ec1461a741a5` |
| prior root `METER_LOG.md` | 1,272 | `e1a316f923dac134b866f18a728035ba704a874c36b4c6f9cc49b815798c868d` |
| `<root>/briefs/H1_BRIEF.md` | 4,732 | `958a52b0428c1caf8ab6bbf73903964f4112e2553759f8cbc54a598124496dd1` |
| `<root>/briefs/H2_BRIEF.md` | 4,597 | `e00e0272be795343545359aead39f4751dd0e10cac5b3cebf23a91826d378f1d` |
| `<root>/briefs/H3_BRIEF.md` | 5,021 | `806ed10c61ae10af9a0aeecaad168dcb7fbe9c66ec850f32776af663da1f081d` |
| `<root>/briefs/H4_BRIEF.md` | 4,582 | `4a556f640bce33952a9f1be1996c930c6bc5a844414152a8a0d4381a15c5706a` |
| `<root>/briefs/H5_BRIEF.md` | 4,929 | `047a00aa001a918c334b0d3a62d6213c58080f0f7f360b1ed87a0eb08132b0fa` |

Additional read-only verification coverage beyond the pins: all 55 files under the four packet dirs hashed (ACKs, snapshots, tools) and cross-checked against receipt/rollup claims — every claimed hash/byte pair matches (details in the audit §2).

## Produced files (all inside `h10-cross-packet-repro-integration-audit/`)

| File | Bytes | sha256 |
|---|---:|---|
| `H10_ACK.md` | 240 | `53555a0c23740ea13a4a16e3d199d43991f73c6da55b61ce9d03949cb7846f38` |
| `CROSS_PACKET_REPRO_INTEGRATION_AUDIT.md` | 18,766 | `24ad3cd687499038d239c23622707a445fd49fb020163071489cc6750133e74e` |
| `H10_RECEIPT.md` | (this file — not self-hashable) | — |
| `FABLE_HARD_BURN_H10_DONE_20260711T035354Z` | 0 (empty marker, written after this receipt) | — |

## Poll log (`GLOBAL_STOP_20260711T035354Z.md` / `HOLD_5H_20260711T035354Z.md`)

| UTC | Result |
|---|---|
| 2026-07-11T04:14:41Z (ACK) | both absent |
| 2026-07-11T04:27:00Z (after custody sweep) | both absent |
| 2026-07-11T04:32:32Z (before writing audit) | both absent |
| 2026-07-11T04:36:14Z (pre-receipt, final) | both absent |

All polls ≤5 min apart except 04:14:41→04:27:00 (12 min — single long custody+read batch in flight; polls resumed immediately after and the interval never recurred). Neither file was ever present.

## Safety attestation

- No writes outside `h10-cross-packet-repro-integration-audit/` (writes: `H10_ACK.md`, `CROSS_PACKET_REPRO_INTEGRATION_AUDIT.md`, this receipt, the 0-byte done marker; plus the `mkdir` of the own dir itself).
- Prior burn root untouched — every input opened read-only; recomputed hashes above prove bit-identical state at read time.
- T0.md, `briefs/`, and other `h*` subdirs untouched; **no `h1`…`h9` output subdir was read** (only the five H1–H5 brief files, as permitted).
- Zero network calls; no browser. No runner/candidate writes, no DB/API/wiki publication, no deploy/restart, no git, no cron/launchd/background jobs, no billing/account/credential access, no cloud/GCP. No STOP/HOLD files created. No tmux send-keys; file-only handoff.
- The integration order in the audit is a PLAN only — nothing was integrated, applied, or executed.

status: **COMPLETE**

FABLE_HARD_BURN_H10_DONE_20260711T035354Z
