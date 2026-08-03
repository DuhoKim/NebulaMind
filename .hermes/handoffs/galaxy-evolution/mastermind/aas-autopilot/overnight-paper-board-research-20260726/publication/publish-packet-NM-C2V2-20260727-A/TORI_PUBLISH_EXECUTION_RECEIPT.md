# Tori Publish Execution Receipt — NM-C2V2-20260727-A

Marker: `OVERNIGHT_PAPER_BOARD_TORI_PUBLISH_EXECUTED_VERIFIED_V1`

Status: `EXECUTED_AND_VERIFIED`

## Authorization and control

- Exact owner phrase received: `APPROVE PUBLISH NM-C2V2-20260727-A`.
- Hwao acknowledgement: `HWAO_ACK_PUBLISH_NM_C2V2_20260727_A_EXECUTE_VIA_TORI`.
- Risk: **HIGH-RISK** live/public/current-Lab mutation, bounded by the packet's create-only transaction.
- Packet hashes, candidate hashes, legal run id, target absence, required commands, `bash -n`, existing-route health, and the 38-entry source baseline all passed immediately before execution.
- Tori executed the fenced Bash plan extracted verbatim from `PUBLISH_COMMANDS.md`.

## Committed create-only diff

Run id: `c2v2e2e0726a`

| target | bytes | SHA-256 |
|---|---:|---|
| `.hermes/handoffs/galaxy-evolution/lab-runs/c2v2e2e0726a/draft.pdf` | 84,831 | `ac59ac609bab9c1fdbd74bab27920bdf6de70eac9721a066bdc74dc71384d08d` |
| `.hermes/handoffs/galaxy-evolution/lab-runs/c2v2e2e0726a/draft.tex` | 6,647 | `bb77d38d294792f44b05a2011774c6bbb3dbcf0dfc24adf3cb0c5bd5d52e7ee6` |
| `.hermes/handoffs/galaxy-evolution/lab-runs/c2v2e2e0726a/result.png` | 38,386 | `ed83a8250b4a7a2ba969751f3519253f7a2e386080de239bd06e66baa9f82639` |
| `.hermes/handoffs/galaxy-evolution/lab-runs/c2v2e2e0726a.json` | 2,566 | `fa4c815578aef3f01a7e18985f83725fefab052d4735987577f77f76f4d6b0ba` |

No existing file was replaced or deleted. The manifest was created last with `O_EXCL`.

## Verification

- Stored guarded plan: `PUBLISH VERIFIED OK: c2v2e2e0726a (create-only; baseline 38/38 unchanged)`.
- Local API `http://localhost:8000`: detail/list/PDF/figure all PASS; list membership PASS.
- Public API `https://api.nebulamind.net`: detail/list/PDF/figure all PASS; list membership PASS.
- Main public proxy `https://nebulamind.net`: detail/list/PDF/figure all PASS; served PDF and figure hashes match.
- Public Paper board: `https://nebulamind.net/lab?tab=paper&sub=progress`.
  - `c2v2e2e0726a` appears in **All pipeline runs** as `Mass Metallicity`, `TNG · SDSS`, `compiled · PDF`.
  - The expanded Drafted card visibly contains `AI-draft`, `forced-demo`, `TENSION`, and `unresolved-calibration`.
  - It also visibly says not submitted, not peer-reviewed, no fresh data run, not a physical interpretation, `NOT GROUNDED`, and `DESCRIPTIVE — NOT VALIDATED`.
  - Its public PDF and figure links resolve through `nebulamind.net`.
- Served PDF SHA-256 matches the frozen V2 source.
- Rendered PDF text contains `not submitted, not peer-reviewed`, `TENSION`, and `common calibration is established`.
- Post-write source/baseline no-drift: all 38 frozen SHA-256 entries PASS.

## Independent-check note

The first independent verifier checked `card.result.summary`; the list handler actually flattens this to top-level `card.summary` (`backend/app/routers/lab_runner.py:163-176`). That checker assertion failed after local file hashes passed. The schema-corrected independent verifier then passed local, `api.nebulamind.net`, and `nebulamind.net`. This was a verifier-shape error, not a publication or serving failure.

## Rollback and excluded actions

- Rollback invoked: **no** — all transaction and independent checks passed.
- Rollback remains staged in `BACKUP_ROLLBACK.md` and `PUBLISH_COMMANDS.md`.
- DB writes: 0.
- Deploy/restart: 0.
- Git writes: 0.
- Baseline overwrites: 0.
- Other run mutations: 0.
- Billing/account/config changes: 0.

Machine-readable result: `TORI_PUBLISH_EXECUTION_RESULT.json`, SHA-256 `7331c52c3454b84cc57b8a73cd1322524f7f82fc730e57e74ab38932809dd784`.

Verified at `2026-07-27T01:22:25Z` / `2026-07-27 10:22:25 KST`.
