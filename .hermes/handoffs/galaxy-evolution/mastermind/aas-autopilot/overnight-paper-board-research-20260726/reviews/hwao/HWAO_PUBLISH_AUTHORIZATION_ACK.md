# Hwao — Publish Authorization ACK (packet NM-C2V2-20260727-A)

- Marker: `OVERNIGHT_PAPER_BOARD_HWAO_PUBLISH_AUTHORIZATION_ACK_V1`
- Parent approval: `OVERNIGHT_PAPER_BOARD_EXECUTION_APPROVED_20260726T133216Z`
- Recorded by Hwao/Fable. Machine-authored coordination artifact; not human gold. This step wrote NO `lab-runs`, public, source, DB, deploy, git, memory, or config byte — only this ACK under the approved output root.

## Approval received
The owner supplied the exact required phrase: **`APPROVE PUBLISH NM-C2V2-20260727-A`** — a byte-exact match to the phrase specified in `PUBLISH_PACKET.md` / `HWAO_PUBLISH_PREFLIGHT_RECEIPT.md`. The Gate-5 packet is therefore **AUTHORIZED for bounded execution**.

## Authorization scope (bounded; Tori executes — Hwao does NOT)
Per the standing role split, **Tori performs the bounded execution**; Hwao coordinates/adjudicates and does not run the publish. Execution is authorized **only** as specified in the packet, with no deviation:
- **Exactly the four create-only operations** in `EXACT_DIFF.md`: `mkdir lab-runs/c2v2e2e0726a/` + create `draft.pdf` (`ac59ac60…`, 84,831 B), `draft.tex` (`bb77d38d…`, 6,647 B), `result.png` (`ed83a825…`, 38,386 B), and `c2v2e2e0726a.json` (from `PREVIEW_MANIFEST.json`, `fa4c8155…`, 2,566 B) created LAST.
- Run **`PUBLISH_COMMANDS.md`** verbatim (transaction-safe: `set -euo pipefail`; ownership-gated, self-disabling EXIT rollback; `O_EXCL` manifest helper; noclobber artifacts; manifest-last; full baseline 38/38 check; JSON-parsed label checks; served PDF-text checks; bounded 12×5s public settlement poll).
- **No baseline overwrite** (`gated-e2e-demo` immutable), **no deploy/restart**, no edit to any other run, no source/DB/wiki/git/cron/browser/account/PAYG action, no scope creep beyond the four exact creates.
- On **any** verification failure, Tori must trigger the ownership-gated manifest-first rollback and confirm all four targets + the run dir are ABSENT again.

## Preconditions reaffirmed at ACK time
- Targets ABSENT: `lab-runs/c2v2e2e0726a.json`, `lab-runs/c2v2e2e0726a/` (create-only).
- Candidate V2 frozen: `candidate.pdf ac59ac60…`, `candidate.tex bb77d38d…`, `result.png ed83a825…`.
- Baseline `gated-e2e-demo` unchanged: `draft.pdf 0d863bff…`, `draft.tex f1aeadd8…`, `.json 46ddd75d…`.
- Classification: **HIGH-RISK** live/public/current-Lab mutation, bounded by create-only controls.

## Handoff
Tori: execute the bounded packet, then produce an execution receipt (post-write hashes, local + public served/label/PDF-text verification results, baseline-unchanged confirmation, and rollback status if any) for Hwao's final audit. Until Tori's execution receipt lands, public status is **transitioning from `AWAITING_EXPLICIT_PUBLISH_APPROVAL` to executing under this authorization** — Hwao will set the final published/served status only after Tori's verified receipt.

`OVERNIGHT_PAPER_BOARD_HWAO_PUBLISH_AUTHORIZATION_ACK_V1`
