# Hwao — Publish Final Audit (packet NM-C2V2-20260727-A)

- Marker: `OVERNIGHT_PAPER_BOARD_HWAO_PUBLISH_FINAL_AUDIT_V1`
- Parent approval: `OVERNIGHT_PAPER_BOARD_EXECUTION_APPROVED_20260726T133216Z`
- Hwao/Fable final **read-only** adjudication of Tori's executed publish (`OVERNIGHT_PAPER_BOARD_TORI_PUBLISH_EXECUTED_VERIFIED_V1`, executed `2026-07-27T01:22:25Z`). Machine-authored; not human gold. This audit mutated nothing: no public cockpit update, no `lab-runs`/source/DB/deploy/git/memory/config write — only this audit file under the approved root.

## Verdict: EXECUTED & VERIFIED
The create-only promotion of the frozen, final-accepted **C2 V2** candidate to new run id **`c2v2e2e0726a`** is confirmed. Independent Hwao read-only checks concur with Tori's receipt. No discrepancy that affects publication or serving was found.

## Independent Hwao checks (read-only)
### 1. Exact targets / hashes — PASS (direct on-disk read)
| target | bytes | SHA-256 | result |
|---|---:|---|---|
| `lab-runs/c2v2e2e0726a/draft.pdf` | 84,831 | `ac59ac60…` | ✓ matches frozen V2 |
| `lab-runs/c2v2e2e0726a/draft.tex` | 6,647 | `bb77d38d…` | ✓ |
| `lab-runs/c2v2e2e0726a/result.png` | 38,386 | `ed83a825…` | ✓ (byte-identical to source figure) |
| `lab-runs/c2v2e2e0726a.json` | 2,566 | `fa4c8155…` | ✓ **byte-identical to the reviewed `PREVIEW_MANIFEST.json`** |
The run directory contains **only** these three artifacts — no scope creep.

### 2. 38/38 baseline — PASS
`shasum -a 256 -c INPUT_SHA256.txt` → **OK=38, FAILED=0**. The new id `c2v2e2e0726a` does **not** appear in the baseline manifest (0 occurrences) — the promotion is genuinely additive. Baseline `gated-e2e-demo` pins unchanged (`draft.pdf 0d863bff…`, `draft.tex f1aeadd8…`, `.json 46ddd75d…`). No existing run mutated.

### 3. Paper-board representation — PASS (data layer verified read-only)
The served manifest and PDF that back the board carry every required disclosure:
- `result.summary` contains **`AI-draft`, `forced-demo`, `TENSION`, `unresolved-calibration`**, plus "not submitted, not peer-reviewed", "no fresh data run", and "NOT a physical interpretation".
- Optional `review_*` fields **absent**; `lit_grounded`/`lit_papers` **absent** → the board honestly renders **NOT GROUNDED** (and DESCRIPTIVE — NOT VALIDATED per the summary).
- `status:"done"`, `method:"mass-metallicity"`, id-matched `figure_url`/`pdf_url` → satisfies the `list_runs` visibility gate; the list handler flattens `result.summary` → top-level `card.summary` (`lab_runner.py:163-176`), so the board card surfaces the labels.
- Rendered PDF text contains "not submitted, not peer-reviewed", "TENSION", and "common calibration is established".

### 4. Local / public served state — VERIFIED BY TORI; byte-corroborated by Hwao
**Scope note (honest):** Hwao's audit environment is network-sandboxed — live HTTP GETs to `localhost:8000`, `api.nebulamind.net`, and `nebulamind.net` were **UNREACHABLE from this audit context**, so Hwao did not independently re-run the live served checks. Hwao corroborates the served state indirectly and fully: the on-disk bytes the serving layer returns are exactly correct and byte-identical to the reviewed preview; the id is source-code-route-valid (`get_run`/`get_artifact` accept `c2v2e2e0726a`); the manifest satisfies `list_runs` visibility with honest fields. Tori, from a capable context, verified live: local + `api.nebulamind.net` + main `nebulamind.net` proxy — detail/list/PDF/figure all `200`, list membership true, served PDF & figure SHA-256 match the frozen source, and the public Paper board card visibly shows the four labels + not-submitted/not-peer-reviewed/no-fresh-data-run/not-physical + NOT GROUNDED + DESCRIPTIVE—NOT VALIDATED. Hwao concurs.

## Note on Tori's self-reported verifier-shape error
Tori recorded that a first independent checker looked for `card.result.summary` in the list response, while the list handler flattens it to top-level `card.summary` (`lab_runner.py:163-176`); the schema-corrected checker then passed on all three hosts. Independently confirmed here: this was a **checker-shape bug, not a publication or serving failure** — the label text is present in the served summary/PDF, and the served bytes match.

## Safety / transaction
- Rollback: **not invoked** (all checks passed); remains staged in `BACKUP_ROLLBACK.md` / `PUBLISH_COMMANDS.md`.
- Excluded actions (per Tori result + Hwao audit): DB writes 0, deploy/restart 0, git 0, baseline overwrites 0, other-run mutations 0, billing/account/config 0.
- This audit performed no mutation and did not touch the public cockpit.

## Final status
**PUBLISHED / SERVED** as a clearly-labelled autonomous **AI-draft research note** at run id `c2v2e2e0726a` (HIGH-RISK live/public mutation, executed create-only and verified; baseline immutable). This supersedes the prior `AWAITING_EXPLICIT_PUBLISH_APPROVAL` state for this candidate. The baseline `gated-e2e-demo` input was never overwritten.

`OVERNIGHT_PAPER_BOARD_HWAO_PUBLISH_FINAL_AUDIT_V1`
