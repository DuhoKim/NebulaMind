# Goru — C2 V2 New-Run Mapping REPAIR Brief (READ-ONLY, legal id `c2v2e2e0726a`)

- Dispatch marker: `OVERNIGHT_PAPER_BOARD_PUBLICATION_GORU_C2_V2_NEW_RUN_MAP_V2_BRIEF_V1`
- **Completion marker (emit ONLY when fully done):** `OVERNIGHT_PAPER_BOARD_PUBLICATION_GORU_C2_V2_NEW_RUN_MAP_V2_COMPLETE_V1`
- Parent approval: `OVERNIGHT_PAPER_BOARD_EXECUTION_APPROVED_20260726T133216Z`
- Prepared by: Hwao/Fable at Deepening Gate 4. Dispatched by: Tori (do not self-start).
- Lane: **existing Antigravity / agy Gemini subscription only** — no API-key, no GCP, no PAYG, no third-party route.
- This brief is standalone. **READ-ONLY mapping. Public status stays `AWAITING_EXPLICIT_PUBLISH_APPROVAL`.**

## Why this repair
The first new-run mapping proposed id `gated-e2e-demo-c2-v2`, which is **not routable**: `backend/app/routers/lab_runner.py` rejects any request where `not rid.isalnum()` (`get_run` l.183; `get_artifact` l.196), and the hyphens make `rid.isalnum()` False → `/api/lab/runs/gated-e2e-demo-c2-v2/artifact/draft.pdf` returns `400`. Re-map against the corrected **legal id `c2v2e2e0726a`** (12 chars, alphanumeric, currently ABSENT).

## PRESERVE the failed first mapping (do NOT touch)
Leave `publication/goru-v2-new-run-map/NEW_RUN_TARGET_MAP.md` and `publication/GORU_C2_V2_NEW_RUN_MAPPING_RECEIPT.md` **unchanged** — they stand as the recorded failed first mapping. Do not edit, overwrite, or delete them. Your repair output is a separate **versioned** deliverable.

## HARD prohibitions (absolute — STOP and report rather than do any of these)
- Do NOT overwrite/edit the baseline `gated-e2e-demo` run or ANY `lab-runs/**` artifact; **create nothing** in `lab-runs`.
- No public/static-root write; **no candidate copy** into any public/repo/served/`lab-runs` location.
- No browser automation / no live-site browsing; **no live HTTP** (verification is a plan, not executed).
- No deploy/restart, no DB/SQL/API write, no git, no cron, no account/billing/cloud config, no PAYG/Nous.

## Allowed READ roots (read-only)
1. `backend/app/routers/lab_runner.py` — the route validators (`get_run` l.181–191, `get_artifact` l.194–201), `list_runs` visibility (l.148–178), and `create_run` id convention (l.132–145).
2. Approved output root: V2 candidate hashes (`packets/C-candidate-build/lana/c2-mzr-gated-e2e-candidate-v2/`), the preserved first map + receipt (for reference, not editing), `reviews/hwao/HWAO_C2_V2_FINAL_ACCEPTANCE.md`, `publication/TORI_C2_V2_ROUTE_VALIDATION.md`, baseline; this brief.

## Allowed WRITE root (exclusive to you — single writer; VERSIONED)
- Deliverable ONLY under `…/publication/goru-v2-new-run-map-v2/`
- Receipt ONLY at `…/publication/GORU_C2_V2_NEW_RUN_MAPPING_RECEIPT_V2.md`
- Temp ONLY as `…/publication/goru-v2-new-run-map-v2/_tmp_*` (never TMPDIR, /tmp, scratchpad).

## Tasks (mapping only, for legal id `c2v2e2e0726a`)
1. **Legal-id + ABSENT verification.** Confirm `c2v2e2e0726a` satisfies the validators: `isalnum()` True, `len ≤ 32`. Verify both target paths are currently ABSENT (create-only): `lab-runs/c2v2e2e0726a.json` and `lab-runs/c2v2e2e0726a/` (→ `draft.pdf`, `draft.tex`, `result.png`). Record each as `ABSENT — create`.
2. **Route source-code validity.** Confirm, citing `lab_runner.py`, that `/api/lab/runs/c2v2e2e0726a/artifact/draft.pdf` is valid under `get_artifact` (`rid.isalnum()` True; `name` has no `/` or `..`; served from `RUNS_DIR/rid/name`) and that `get_run` accepts the id. Contrast explicitly with why the hyphenated id failed.
3. **Manifest requirements (grounded in source).** Record that `list_runs` (l.157–161) requires top-level `status: "done"` AND non-empty `result.summary` for list visibility. The `c2v2e2e0726a.json` must carry:
   - top-level `id`, `status` (`"done"`), `created_utc`, `spec` (with `spec.method`, `spec.data_sources`);
   - non-empty `result.summary`;
   - `result.figure_url` = `/api/lab/runs/c2v2e2e0726a/artifact/result.png`;
   - `result.pdf_url` = `/api/lab/runs/c2v2e2e0726a/artifact/draft.pdf`;
   - **omit** optional `result.review_url` / `result.review_verdict` / `result.review_cycles` **unless backed by an actual review artifact** placed in the run dir (do not fabricate a review). Likewise do not fabricate `lit_grounded`/`lit_papers` — absent → the API honestly reports "not grounded".
4. **Visible labels.** The four labels — `AI-draft`, `forced-demo`, `TENSION`, `unresolved-calibration` — must be surfaced in `result.summary` text (that is the field `list_runs` returns and displays), so they survive into the served representation.
5. **V2 candidate hashes (source of promotion).** Record: `candidate.pdf ac59ac609bab9c1fdbd74bab27920bdf6de70eac9721a066bdc74dc71384d08d`, `candidate.tex bb77d38d294792f44b05a2011774c6bbb3dbcf0dfc24adf3cb0c5bd5d52e7ee6`, `result.png ed83a8250b4a7a2ba969751f3519253f7a2e386080de239bd06e66baa9f82639`.
6. **Create-only backup/rollback (plan; DO NOT EXECUTE).** Nothing to back up (create-only). Rollback = delete exactly `lab-runs/c2v2e2e0726a.json` and `lab-runs/c2v2e2e0726a/`. State that the baseline `gated-e2e-demo` run is never touched.
7. **HTTP / SHA / visible-label verification plan (DO NOT EXECUTE).** SHA: created `draft.pdf` == `ac59ac60…`. HTTP: `curl -I /api/lab/runs/c2v2e2e0726a/artifact/draft.pdf` == `200` + expected `Content-Length` (and that it does NOT `400`, unlike the hyphenated id). Labels: served `summary`/manifest + PDF text carry the four labels.
8. **Blockers.** Record anything not determinable read-only.

## Deliverable
`publication/goru-v2-new-run-map-v2/NEW_RUN_TARGET_MAP_V2.md` — legal-id + route validity (with `lab_runner.py` line citations), ABSENT/create paths, manifest requirements, visible labels, V2 candidate hashes, create-only backup/rollback plan, verification plan, blockers. Headed `AI_DRAFT_NOT_HUMAN_GOLD`; include a read-only attestation (no public byte touched, no browser/live-HTTP, no candidate copy, no `lab-runs` create/edit, first map preserved).

## Stop conditions
Any step that would create/overwrite a `lab-runs` artifact, edit the preserved first map, a public write, a candidate copy, browser/live-HTTP, deploy, DB, git, or credentials; source drift; a payment/overage/top-up/Nous/PAYG prompt; any need to write outside `publication/`.

## Completion contract
`publication/GORU_C2_V2_NEW_RUN_MAPPING_RECEIPT_V2.md` must list the deliverable's SHA-256, the legal-id/route-validity confirmation, the ABSENT/create paths, the manifest requirements, the visible-label requirement, the create-only backup/rollback + verification plans, any blockers, an explicit "first map preserved unchanged / no `lab-runs` create / no public write / no browser / no live-HTTP / no candidate copy" attestation, and a completion state of `DONE` / `PARTIAL` / `BLOCKED` (never relabel PARTIAL/BLOCKED as success). Public status remains `AWAITING_EXPLICIT_PUBLISH_APPROVAL`. End the receipt with the completion marker on its own line:

`OVERNIGHT_PAPER_BOARD_PUBLICATION_GORU_C2_V2_NEW_RUN_MAP_V2_COMPLETE_V1`
