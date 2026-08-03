# Publish Packet — NM-C2V2-20260727-A

- Marker: `OVERNIGHT_PAPER_BOARD_PUBLISH_PACKET_NM_C2V2_20260727_A_V1`
- Parent approval: `OVERNIGHT_PAPER_BOARD_EXECUTION_APPROVED_20260726T133216Z`
- **Status: `AWAITING_EXPLICIT_PUBLISH_APPROVAL`.** This packet PREPARES a create-only promotion; it does NOT execute it. No file here writes to `lab-runs`, any public/static root, or any current-Lab byte.
- Candidate: C2 **V2** (final-accepted mechanics; Kun nine-item PASS). New run id: **`c2v2e2e0726a`** (route-valid, ABSENT).

## Candidate V2 hashes (immutable source of promotion)
| file | bytes | SHA-256 |
|---|---:|---|
| `candidate.pdf` | 84,831 | `ac59ac609bab9c1fdbd74bab27920bdf6de70eac9721a066bdc74dc71384d08d` |
| `candidate.tex` | 6,647 | `bb77d38d294792f44b05a2011774c6bbb3dbcf0dfc24adf3cb0c5bd5d52e7ee6` |
| `result.png` | 38,386 | `ed83a8250b4a7a2ba969751f3519253f7a2e386080de239bd06e66baa9f82639` |

## Exact four ABSENT → create paths (verified ABSENT this gate)
- `lab-runs/c2v2e2e0726a.json`
- `lab-runs/c2v2e2e0726a/draft.pdf`
- `lab-runs/c2v2e2e0726a/draft.tex`
- `lab-runs/c2v2e2e0726a/result.png`

## Nature of the mutation
A **create-only, additive** mutation of the public/current-Lab/source tree: four new files under one new run directory. **No baseline overwrite** — `gated-e2e-demo` (and every other run) is untouched. **No deploy/restart required**: the current dynamic serving code discovers a run purely by the presence of `<id>.json` (`status:"done"` + non-empty `result.summary`) and serves artifacts from `lab-runs/<id>/`, so the new run appears automatically once the files exist.

## Risk posture
**HIGH-RISK.** Executing this packet writes into the live, public-facing served `lab-runs` tree — a live / public / current-Lab mutation. It is classified **HIGH-RISK even though it is bounded by create-only controls** (a route-valid new id, manifest-last ordering, and a manifest-first guarded rollback; see `BACKUP_ROLLBACK.md` and `VERIFY_PLAN.md`). Those controls mitigate the blast radius but do **not** downgrade the risk classification. It must not proceed without the exact approval phrase. The served candidate visibly carries the AI-draft / forced-demo / TENSION / unresolved-calibration labels and is not represented as a validated or peer-reviewed result.

## Approval
The exact approval phrase required before ANY of the four creates is executed:

`APPROVE PUBLISH NM-C2V2-20260727-A`

The owner's earlier broad approval authorized **preparing** this packet, **not executing** its (previously unseen) exact diff. The exact diff is specified in `EXACT_DIFF.md` and must be reviewed before that phrase is given.

## Packet contents
`PREVIEW_MANIFEST.json` · `EXACT_DIFF.md` · `BACKUP_ROLLBACK.md` · `VERIFY_PLAN.md` · `PUBLISH_COMMANDS.md` · `MANIFEST_VALIDATION.md` · `HWAO_PUBLISH_PREFLIGHT_RECEIPT.md`.

Public status: `AWAITING_EXPLICIT_PUBLISH_APPROVAL`.
