# Hwao — Publish Preflight Receipt (packet NM-C2V2-20260727-A)

- Parent approval: `OVERNIGHT_PAPER_BOARD_EXECUTION_APPROVED_20260726T133216Z`
- Authored by Hwao/Fable at Publication Preflight Gate 5. Machine-authored; not human gold.
- **Status: `AWAITING_EXPLICIT_PUBLISH_APPROVAL`. Nothing was published.** No `lab-runs`, public/static-root, current-Lab, source, DB/wiki, git, cron, browser, deploy, account/billing, or PAYG byte was written this gate. No memory/config written. No live HTTP executed.

## Packet files (SHA-256; every file except this receipt)
| file | SHA-256 |
|---|---|
| `PREVIEW_MANIFEST.json` (2,566 B) | `fa4c815578aef3f01a7e18985f83725fefab052d4735987577f77f76f4d6b0ba` |
| `PUBLISH_PACKET.md` | `68e524972ed106a994528f9c90a3080bfe0436ba4db0fb649f6e9da5d1c60646` |
| `EXACT_DIFF.md` | `e5158b0691e0b6eef970a932882ff91b495cdd6ba77366fc5262f9303a795dee` |
| `BACKUP_ROLLBACK.md` | `315e1f2cd3bdc54a517302a5a041129b31959dfacb2d03287b9c0a9cccea243a` |
| `VERIFY_PLAN.md` | `e9025f345b51486f31f9eb7fe59682bdac2d5305a3eca1ddcd76f38cdf672c5e` |
| `PUBLISH_COMMANDS.md` | `8dbf1b5a655f3f37db585eeb942ccad36a55980abbdd7db0089d5c48fa009780` |
| `MANIFEST_VALIDATION.md` | `d4d46fc645ddf3ffd7a8b7f9072fe0e05ad70d5f93c740260f9bfd7d31d70604` |

## Scope
A **create-only** promotion of the frozen, final-accepted **C2 V2** candidate to a **new** route-valid run id `c2v2e2e0726a`: one new directory + four new files (`draft.pdf`, `draft.tex`, `result.png`, `<id>.json`). No baseline overwrite; `gated-e2e-demo` and every other run untouched; no deploy/restart (dynamic serving auto-discovers the new run).

## Risk
**HIGH-RISK** — a live/public/current-Lab mutation of the served `lab-runs` tree. The classification is HIGH-RISK even though bounded by create-only controls; the controls mitigate but do not downgrade it.

## Rollback
Ownership-gated, manifest-first: remove the manifest first (revokes discovery), then only the three exact files, then `rmdir` the exact dir. A pre-existing target aborts before any ownership is claimed, so a guard failure deletes nothing. Manifest is created via an `O_EXCL` helper that can only ever delete a file it itself created. The EXIT trap self-disables before rollback. No unguarded/broad deletion.

## Verification (planned; not executed here)
Pre-write: legal id, source/V1/V2 hashes, target absence, manifest schema/labels/routes. Post-write: local SHA/byte on all four creates; full baseline 38/38 SHA manifest + explicit `gated-e2e-demo` `draft.pdf`/`draft.tex`/`.json`. Served (active post-approval, JSON-parsed): local + public `get_run`/artifact 200s, list membership, all four `result.summary` labels, served-PDF bytes hash, and rendered disclosure / TENSION / unresolved-calibration text; public uses a bounded 12×5s settlement poll. Any failure → ownership-gated rollback → verify absence.

## Manifest validation (read-only, all PASS)
`PREVIEW_MANIFEST.json` is valid JSON; id alphanumeric + length 12 (≤ 32); `status:"done"` + non-empty `result.summary` (visibility gate); the four labels `AI-draft`/`forced-demo`/`TENSION`/`unresolved-calibration` present; `figure_url`/`pdf_url` match the id; review + `lit_*` fields omitted; all target paths ABSENT; candidate V2 hashes match; source baseline unchanged. Validators cited accurately (`get_run`: alphanumeric + max length 32; `get_artifact`: alphanumeric + safe artifact name, no length check).

## Preflight no-mutation confirmation (this gate)
- `lab-runs/c2v2e2e0726a.json` — ABSENT. `lab-runs/c2v2e2e0726a/` — ABSENT.
- baseline `gated-e2e-demo/draft.pdf` still `0d863bff…` (unchanged).
- All packet writes were confined to `publication/publish-packet-NM-C2V2-20260727-A/`.

## Approval
Execution requires the exact phrase: **`APPROVE PUBLISH NM-C2V2-20260727-A`**. The owner's earlier broad approval authorized preparing this packet, not executing its now-specified exact diff. Public status stays `AWAITING_EXPLICIT_PUBLISH_APPROVAL`.

`OVERNIGHT_PAPER_BOARD_HWAO_PUBLISH_PACKET_READY_V1`
