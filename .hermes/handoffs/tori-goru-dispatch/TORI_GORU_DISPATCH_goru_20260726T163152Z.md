# Tori -> Goru dispatch

Target: goru
Timestamp: 20260726T163152Z

## Payload

```text
GORU / ANTIGRAVITY BRIEF — Tori-dispatched — 20260726T163152Z

Use Gemini/Antigravity quota for this scoped Tori helper task.

Safety boundary:
- Stay inside the explicit scope in the brief below.
- Prefer read-only mechanical checks, counts, inventories, source maps, repro checks, and draft reviews.
- Do not do DB writes, deploy/restart, git commit/push/merge, cloud/GCP/Gemini API config changes, secrets inspection, or live publication unless the user gives a separate explicit gate.
- If command permission is needed, ask for the smallest exact command; Tori will approve only scope-matching safe commands.
- Write/report exact files, counts, commands, and blockers. Do not self-certify unverified external facts.

Assigned brief:

# Goru — C2 V2 New-Run Target Mapping Brief (READ-ONLY, create-only path)

- Dispatch marker: `OVERNIGHT_PAPER_BOARD_PUBLICATION_GORU_C2_V2_NEW_RUN_MAP_BRIEF_V1`
- **Completion marker (emit ONLY when fully done):** `OVERNIGHT_PAPER_BOARD_PUBLICATION_GORU_C2_V2_NEW_RUN_MAP_COMPLETE_V1`
- Parent approval: `OVERNIGHT_PAPER_BOARD_EXECUTION_APPROVED_20260726T133216Z`
- Prepared by: Hwao/Fable at Deepening Gate 3. Dispatched by: Tori (do not self-start).
- Lane: **existing Antigravity / agy Gemini subscription only** — no API-key, no GCP, no PAYG, no third-party route.
- This brief is standalone. **READ-ONLY mapping. Public status stays `AWAITING_EXPLICIT_PUBLISH_APPROVAL`.**

## Why this brief
The Gate-1 mapping found serving is dynamic from `lab-runs/` and that overwriting `gated-e2e-demo` would mutate an immutable baseline INPUT run (rejected by Hwao). Map the **safer create-only path**: a NEW run id **`gated-e2e-demo-c2-v2`** whose files do not yet exist, so the baseline run is never touched. This is mapping only — create nothing, promote nothing.

## HARD prohibitions (absolute — STOP and report rather than do any of these)
- **Do NOT overwrite or edit the baseline `gated-e2e-demo` run or ANY `lab-runs/**` artifact.**
- No public/static-root write; **no candidate copy** into any public/repo/served/`lab-runs` location.
- No browser automation / no live-site browsing; **no live HTTP** (verification is a plan, not executed).
- No deploy/restart, no DB/SQL/API write, no git, no cron, no account/billing/cloud config, no PAYG/Nous.
- If mapping would require any of the above, STOP and record the blocker.

## Allowed READ roots (read-only)
1. The NebulaMind repo, read-only, for serving mechanics only: `backend/app/routers/lab_runner.py` (how `*.json` are globbed and how `/api/lab/runs/<id>/artifact/<name>` resolves), the run-JSON schema/fields, and how a NEW `<id>.json` + `lab-runs/<id>/` dir becomes discoverable + served.
2. Approved output root: V2 candidate (`packets/C-candidate-build/lana/c2-mzr-gated-e2e-candidate-v2/` for hashes), `publication/goru-target-mapping/PUBLIC_TARGET_MAP.md` (prior mapping), `reviews/hwao/HWAO_C2_REDTEAM_ADJUDICATION.md`, `HWAO_C2_V2_BUILD_ACCEPTANCE.md`, baseline; this brief.

## Allowed WRITE root (exclusive to you — single writer)
- Deliverable ONLY under `…/publication/goru-v2-new-run-map/`
- Receipt ONLY at `…/publication/GORU_C2_V2_NEW_RUN_MAPPING_RECEIPT.md`
- Temp ONLY as `…/publication/goru-v2-new-run-map/_tmp_*` (never TMPDIR, /tmp, scratchpad).

## Tasks (mapping only, for run id `gated-e2e-demo-c2-v2`)
1. **Exact ABSENT/create paths.** Map the exact target paths a create-only promotion would produce and confirm each is currently ABSENT (nothing to overwrite): `lab-runs/gated-e2e-demo-c2-v2.json` (top-level manifest), `lab-runs/gated-e2e-demo-c2-v2/draft.pdf`, `…/draft.tex`, `…/result.png`. Record each as `ABSENT — create`.
2. **Source-code route coupling.** From `lab_runner.py`, document how the new id is discovered and served purely by creating `<id>.json` (status `done`, populated `summary`) + the `lab-runs/<id>/` artifacts, mapping to `/api/lab/runs/gated-e2e-demo-c2-v2/artifact/<name>`. Confirm NO existing run/JSON needs editing (create-only, additive).
3. **Candidate V2 hashes (source of promotion).** Record the V2 bytes that would be copied into the new run dir: `candidate.pdf` `ac59ac609bab9c1fdbd74bab27920bdf6de70eac9721a066bdc74dc71384d08d`, `candidate.tex` `bb77d38d294792f44b05a2011774c6bbb3dbcf0dfc24adf3cb0c5bd5d52e7ee6`, `result.png` `ed83a8250b4a7a2ba969751f3519253f7a2e386080de239bd06e66baa9f82639`.
4. **Preview/manifest field requirements.** Enumerate the fields the new `<id>.json` must carry for the run to appear + serve the PDF, and specify that the visible labels — `AI-draft`, `forced-demo`, `TENSION`, `unresolved-calibration` — must be surfaced in the served `summary`/fields (and a preview/draft flag if the schema supports one) so they survive into the served form.
5. **Create-only backup/rollback plan.** Since create-only, there is **nothing to back up** (no existing bytes replaced); rollback = delete exactly the newly created `lab-runs/gated-e2e-demo-c2-v2.json` and `lab-runs/gated-e2e-demo-c2-v2/` directory. Write the exact create-only rollback command **form** (DO NOT EXECUTE), and state explicitly that the baseline `gated-e2e-demo` run is never touched.
6. **HTTP / SHA / visible-label verification plan (DO NOT EXECUTE).** SHA check that the created `draft.pdf` == `ac59ac60…`; HTTP check `curl -I /api/lab/runs/gated-e2e-demo-c2-v2/artifact/draft.pdf` == `200` + expected `Content-Length`; visible-label check that the served summary/manifest and the PDF text carry the four labels. All as a plan for the future publish packet.
7. **Blockers.** Record anything not determinable by static read-only inspection.

## Deliverable
`publication/goru-v2-new-run-map/NEW_RUN_TARGET_MAP.md` — ABSENT/create paths, route coupling, V2 candidate hashes, preview/manifest field requirements, create-only backup/rollback plan + rollback command form, HTTP/SHA/visible-label verification plan, and blockers. Headed `AI_DRAFT_NOT_HUMAN_GOLD`; include a read-only attestation (no public byte touched, no browser/live-HTTP, no candidate copy, no baseline-run edit).

## Stop conditions
Any step that would require overwriting `gated-e2e-demo` or any `lab-runs` artifact, a public write, a candidate copy, browser/live-HTTP, deploy, DB, git, or credentials; source drift; a payment/overage/top-up/Nous/PAYG prompt; any need to write outside `publication/`.

## Completion contract
`publication/GORU_C2_V2_NEW_RUN_MAPPING_RECEIPT.md` must list the deliverable's SHA-256, the ABSENT/create target paths, the route coupling, the V2 candidate hashes, the preview/manifest field requirements, the create-only backup/rollback plan, the verification plan, any blockers, an explicit "no public write / no browser / no live-HTTP / no candidate copy / no baseline-run edit" attestation, and a completion state of `DONE` / `PARTIAL` / `BLOCKED` (never relabel PARTIAL/BLOCKED as success). Public status remains `AWAITING_EXPLICIT_PUBLISH_APPROVAL`. End the receipt with the completion marker on its own line:

`OVERNIGHT_PAPER_BOARD_PUBLICATION_GORU_C2_V2_NEW_RUN_MAP_COMPLETE_V1`

Done marker: TORI_GORU_DISPATCH_DONE_20260726T163152Z

```
