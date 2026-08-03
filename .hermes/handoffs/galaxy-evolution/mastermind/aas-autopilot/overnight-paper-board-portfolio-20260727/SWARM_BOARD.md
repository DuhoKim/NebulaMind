# Overnight Paper Board Swarm Board

Window: 2026-07-27 21:58 KST to hard stop 2026-07-28 10:00 KST.

Execution marker: `OVERNIGHT_PAPER_BOARD_EXECUTION_ACCEPTED_20260727T215806KST`.

## Roles

| Packet | Primary lane | Task | Primary done marker |
|---|---|---|---|
| Coordination | Hwao / Fable | accept corrected board, inspect receipts, adjudicate, roll up | `HWAO_PB_COORDINATOR_ACCEPTED_20260727` |
| P0 | Lana / Fable | served TNG-validation representation and claim-consistency audit | `P0_LANA_PRIMARY_COMPLETE_20260727` |
| P1 | Kun / Codex | high-z cumulative-density/systematic-budget/source-role audit | `P1_KUN_PRIMARY_COMPLETE_20260727` |
| P2 | Goru / Antigravity | fesc lineage, bibliography identity, and citation-gap census | `P2_GORU_PRIMARY_COMPLETE_20260727` |
| Integration | Tori / Hermes | custody, cross-reviews, independent validation, report publication | final manifest + served receipt |

## Single-writer boundaries

Each primary lane writes only in its assigned `packets/<packet>/<lane>/` directory. Inputs in each lane's `input/` directory are immutable snapshots. Lanes must not write to project source, Lab records, public roots, the cockpit, DB/wiki state, services, or Git.

## Network and browser boundary

Public source reads, ADS/arXiv metadata, and browser research are approved. Stop on login, CAPTCHA, payment, account change, OAuth, token, secret, unusual traffic, or UI identity uncertainty. Do not use a source only because it is convenient; identity and source role must pass.

## Publication boundary

Only one new public Paper Board audit report may be published after integration preflight. No existing paper, PDF, card, Lab run, cockpit, or wiki content may be replaced.

## Stop files

- `GLOBAL_STOP_OVERNIGHT_PB_20260727.md`: stop all new/continuing substantive work.
- `CONTENT_FREEZE_OVERNIGHT_PB_20260727.md`: stop content changes; receipts and verification only.

All lanes check stop files at start, mid-run, and before final receipt.
