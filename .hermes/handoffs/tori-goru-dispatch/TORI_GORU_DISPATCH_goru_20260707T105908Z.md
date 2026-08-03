# Tori -> Goru dispatch

Target: goru
Timestamp: 20260707T105908Z

## Payload

```text
GORU / ANTIGRAVITY BRIEF — Tori-dispatched — 20260707T105908Z

Use Gemini/Antigravity quota for this scoped Tori helper task.

Safety boundary:
- Stay inside the explicit scope in the brief below.
- Prefer read-only mechanical checks, counts, inventories, source maps, repro checks, and draft reviews.
- Do not do DB writes, deploy/restart, git commit/push/merge, cloud/GCP/Gemini API config changes, secrets inspection, or live publication unless the user gives a separate explicit gate.
- If command permission is needed, ask for the smallest exact command; Tori will approve only scope-matching safe commands.
- Write/report exact files, counts, commands, and blockers. Do not self-certify unverified external facts.

Assigned brief:

# Gemini/Goru G1 autonomous Surveys file-map and surface audit

Marker: `GORU_G1_SURVEYS_FILEMAP_BRIEF_20260707T105700Z`
Run: `SURVEYS_LOW_USAGE_AUTONOMOUS_RUN_20260707T105700Z`
Target lane: Gemini / Goru mechanical lane

## Mission

Use Gemini/Goru quota for a bounded mechanical audit of the NebulaMind Surveys page surface. Produce a report; do not modify product files.

## Absolute boundaries

- Artifact/report only.
- Do not edit product/source/generated public files.
- No DB writes, SQL, migrations, deploy/restart, git, wiki publish, cron, browser automation, provider/account/billing/API/GCP/OAuth/token/credential activity.
- Read-only file inspection and simple counts are allowed.

## Inspect these paths

Repo root: `/Users/duhokim/NebulaMind/NebulaMind`

- `frontend/src/app/surveys/`
- `frontend/src/components/surveys/`
- `frontend/scripts/test-surveys-atlas-ia.mjs`
- `backend/app/routers/surveys.py`
- `backend/app/models/survey.py`
- `docs/survey_explorer_design_v1.md`
- `docs/survey_detail_page_v1.md`

## Mechanical tasks

1. Build a file map of Surveys page and component files.
2. Count which components include interactive controls (`button`, `a`, `select`, `input`, `role="button"`).
3. List route/API endpoints involved in Surveys pages.
4. Note any product files that appear unused/dead by imports.
5. Identify the top 5 places a Tori implementation pass should inspect next.

## Required output

Write exactly one report file:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/surveys-low-usage-autonomous/20260707T105700Z/GORU_G1_SURVEYS_FILEMAP_REPORT_20260707T105700Z.md`

Report must include marker `GORU_G1_SURVEYS_FILEMAP_REPORT_20260707T105700Z`, status, counts, path references, and safety ledger.

Done marker: TORI_GORU_DISPATCH_DONE_20260707T105908Z

```
