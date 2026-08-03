# Tori -> Goru dispatch

Target: m1
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

# Gemini/Goru G2 autonomous Surveys data-shape audit

Marker: `GORU_G2_SURVEYS_DATA_SHAPE_BRIEF_20260707T105700Z`
Run: `SURVEYS_LOW_USAGE_AUTONOMOUS_RUN_20260707T105700Z`
Target lane: Gemini / Goru mechanical lane

## Mission

Use Gemini/Goru quota for a bounded mechanical data-shape audit of Surveys API/model/frontend types. Produce a report; do not modify product files.

## Absolute boundaries

- Artifact/report only.
- Do not edit product/source/generated public files.
- No DB writes, SQL, migrations, deploy/restart, git, wiki publish, cron, browser automation, provider/account/billing/API/GCP/OAuth/token/credential activity.
- Read-only file inspection and JSON/static counts are allowed.

## Inspect these paths

Repo root: `/Users/duhokim/NebulaMind/NebulaMind`

- `backend/data/seed_surveys.json`
- `backend/app/routers/surveys.py`
- `backend/app/models/survey.py`
- `backend/app/services/survey_health.py`
- `frontend/src/components/surveys/constants.ts`
- `frontend/src/components/surveys/plotting.ts`
- `frontend/src/components/surveys/PlotA.tsx`
- `frontend/src/components/surveys/PlotB.tsx`

## Mechanical tasks

1. Count seed survey rows and band/status distributions.
2. Count null/filled values for plotting fields: `wavelength_center_um`, `z_max`, `dr_year`, `data_volume_tb`, `limiting_magnitude`, `num_sources_count`, `sky_coverage_deg2`.
3. Compare backend response fields to frontend `Survey` type fields.
4. Check whether PlotA/PlotB plottability logic handles nulls and log-scale non-positive values.
5. Identify any type/field mismatch or high-risk data assumption.

## Required output

Write exactly one report file:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/surveys-low-usage-autonomous/20260707T105700Z/GORU_G2_SURVEYS_DATA_SHAPE_REPORT_20260707T105700Z.md`

Report must include marker `GORU_G2_SURVEYS_DATA_SHAPE_REPORT_20260707T105700Z`, status, counts, path references, and safety ledger.

Done marker: TORI_GORU_DISPATCH_DONE_20260707T105908Z

```
