# Tori -> Goru dispatch

Target: goru
Timestamp: 20260726T153742Z

## Payload

```text
GORU / ANTIGRAVITY BRIEF — Tori-dispatched — 20260726T153742Z

Use Gemini/Antigravity quota for this scoped Tori helper task.

Safety boundary:
- Stay inside the explicit scope in the brief below.
- Prefer read-only mechanical checks, counts, inventories, source maps, repro checks, and draft reviews.
- Do not do DB writes, deploy/restart, git commit/push/merge, cloud/GCP/Gemini API config changes, secrets inspection, or live publication unless the user gives a separate explicit gate.
- If command permission is needed, ask for the smallest exact command; Tori will approve only scope-matching safe commands.
- Write/report exact files, counts, commands, and blockers. Do not self-certify unverified external facts.

Assigned brief:

# Goru — Publication Target Mapping Brief (READ-ONLY discovery)

- Dispatch marker: `OVERNIGHT_PAPER_BOARD_PUBLICATION_GORU_TARGET_MAP_BRIEF_V1`
- **Completion marker (emit ONLY when fully done):** `OVERNIGHT_PAPER_BOARD_PUBLICATION_GORU_TARGET_MAP_COMPLETE_V1`
- Parent approval: `OVERNIGHT_PAPER_BOARD_EXECUTION_APPROVED_20260726T133216Z`
- Prepared by: Hwao/Fable at Deepening Gate 1. Dispatched by: Tori (do not self-start).
- Lane: **existing Antigravity / agy Gemini subscription only** — no API-key, no GCP, no PAYG, no third-party route.
- This brief is standalone. **READ-ONLY mapping. You WRITE nothing except your own deliverable + receipt under `publication/`. Public status stays `AWAITING_EXPLICIT_PUBLISH_APPROVAL`.**

## Your role
Identify, by static read-only inspection only, the **current SERVED public target** that a future promotion of the C2 candidate would touch, the **publication route / manifest / index coupling**, the **current bytes + hashes** of that target, and the exact **backup / rollback requirements** a future publish packet must satisfy. Produce a mapping document. Change nothing; promote nothing; browse nothing.

## HARD prohibitions (absolute — STOP and report rather than do any of these)
- **No public/static-root write** of any kind; **no candidate copy** into any public, repo, or served location.
- **No browser automation / no live-site browsing** (do not fetch `nebulamind.net`/`lab.nebulamind.net`).
- **No deploy/restart, no DB/SQL/API write, no git, no cron, no account/billing/cloud config, no PAYG/Nous.**
- No live HTTP execution — produce the HTTP-verification **plan** (commands to run later under the publish gate), do not run it now.
- If identifying the target would require any of the above, STOP and record what is blocked; do not work around it.

## Allowed READ roots (read-only)
1. The NebulaMind repo, read-only, to trace serving: the Next.js/front-end app and its routes, any `public/` or static-export root, the backend artifact-serving code (e.g. how `/api/lab/runs/<id>/artifact/...` resolves), and any papers/board index or manifest. (This is the one lane permitted to read outside `lab-runs` + the output root, strictly read-only, for public-mapping only.)
2. The approved output root: the C2 candidate (`packets/C-candidate-build/lana/c2-mzr-gated-e2e-candidate/`) for the immutable candidate hashes, `reviews/hwao/HWAO_ABCD_FIRSTPASS_ROLLUP.md`, `reviews/tori/TORI_CD_FIRSTPASS_VALIDATION.md`, baseline, this brief.

## Allowed WRITE root (exclusive to you — single writer; under approved output root only)
- Deliverable ONLY under `…/publication/goru-target-mapping/`
- Receipt ONLY at `…/publication/GORU_PUBLIC_TARGET_MAPPING_RECEIPT.md`
- Temp ONLY as `…/publication/goru-target-mapping/_tmp_*` (never TMPDIR, /tmp, scratchpad).

## Tasks (mapping only)
1. **Current served target.** Trace from the repo where reader-facing paper/candidate content is served. Distinguish (a) a static public file on disk (record its exact path) from (b) dynamic API serving from `lab-runs` (record the route + resolver). State precisely what a C2 promotion would create or replace, and whether that target path is currently **absent (create)** or **occupied (replace → needs backup)**.
2. **Route / manifest / index coupling.** Identify how a published item is referenced/discoverable — any index page, JSON manifest, board, or route table that couples the served bytes to a public URL. Record the exact file(s) and how an entry is added (append vs regenerate). Note the host/subdomain mapping if evident from config (do not test it live).
3. **Current bytes + hashes.** For each exact target/index file a promotion would touch, record current byte size + SHA-256 (from disk, read-only). If the target does not yet exist (create-path), record `ABSENT — create` explicitly. Record the immutable C2 candidate hashes (`candidate.pdf eed8992d…`, `candidate.tex c615b2f3…`) as the source-of-promotion.
4. **Backup / rollback requirements.** Specify exactly what a future publish packet must back up before writing (current served bytes if replace; the index/manifest before edit) and the exact **rollback command form** (written as a plan, NOT executed) to restore prior state. List the required visible labels (AI-draft / forced-demo / TENSION / unresolved-calibration) that must survive into any served form, plus the SHA + HTTP smoke-test **plan** a publish packet must run post-promotion.
5. **Gaps / blockers.** Record anything that cannot be resolved read-only (e.g. target only determinable by a live request) as an explicit blocker for the publish packet — do not resolve it by a forbidden action.

## Deliverable
`publication/goru-target-mapping/PUBLIC_TARGET_MAP.md` — served-target identification, route/manifest/index coupling, current-bytes+hashes table (or `ABSENT — create`), backup/rollback requirements + rollback command form, required visible labels, SHA/HTTP smoke-test plan, and blockers. Headed `AI_DRAFT_NOT_HUMAN_GOLD`; state clearly it is a read-only mapping and no public byte was touched.

## Stop conditions
Any step that would require a public write, a candidate copy, browser/live-HTTP, deploy, DB, git, or credentials; source drift; a payment/overage/top-up/Nous/PAYG prompt; any need to write outside `publication/`.

## Completion contract
`publication/GORU_PUBLIC_TARGET_MAPPING_RECEIPT.md` must list the deliverable's SHA-256, the identified served target + coupling, the current-bytes/hashes (or ABSENT-create), the backup/rollback requirements, any blockers, an explicit "no public write / no browser / no candidate copy" attestation, and a completion state of `DONE` / `PARTIAL` / `BLOCKED` (never relabel PARTIAL/BLOCKED as success). Public status remains `AWAITING_EXPLICIT_PUBLISH_APPROVAL`. End the receipt with the completion marker on its own line:

`OVERNIGHT_PAPER_BOARD_PUBLICATION_GORU_TARGET_MAP_COMPLETE_V1`

Done marker: TORI_GORU_DISPATCH_DONE_20260726T153742Z

```
