# Codex/Kun K3 autonomous Surveys test-gap audit

Marker: `CODEX_KUN_K3_SURVEYS_TEST_GAP_BRIEF_20260707T105700Z`
Run: `SURVEYS_LOW_USAGE_AUTONOMOUS_RUN_20260707T105700Z`
Target lane: Codex / Kun, gpt-5.5 subscription lane

## Mission

Work on NebulaMind Surveys pages by auditing frontend/backend test coverage for the Surveys Atlas and detail pages. Produce a test-gap report and exact proposed test additions, but do not edit product files.

## Absolute boundaries

- Artifact/report only.
- Do not edit product/test/source files.
- No DB writes, SQL, migrations, deploy/restart, git, wiki publish, cron, browser automation, provider/account/billing/API/GCP/OAuth/token/credential activity.
- Safe inspections and tests are allowed; redirect caches/temp outside repo if needed.

## Repo and files to inspect

Repo root: `/Users/duhokim/NebulaMind/NebulaMind`

Primary files:
- `frontend/scripts/test-surveys-atlas-ia.mjs`
- `frontend/package.json`
- `frontend/src/app/surveys/page.tsx`
- `frontend/src/app/surveys/[slug]/SurveyDetailClient.tsx`
- `frontend/src/components/surveys/*.tsx`
- `frontend/src/components/surveys/plotting.ts`
- `backend/app/routers/surveys.py`
- `backend/app/services/survey_health.py`
- Any existing backend tests if present.

## Specific questions

1. What important Surveys behavior is currently tested?
2. What important behavior is untested but easy to cover with static/smoke scripts?
3. Which tests can be added without a browser/server/DB?
4. Which tests require fixture/API/server work and should wait?
5. Are there suspicious dead assertions or stale assumptions in the existing smoke script?

## Required verification

Run:
- `cd frontend && npm run test:surveys-atlas-ia`
If you inspect backend tests, list commands you did or did not run.

## Required output

Write exactly one report file:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/surveys-low-usage-autonomous/20260707T105700Z/CODEX_KUN_K3_SURVEYS_TEST_GAP_REPORT_20260707T105700Z.md`

Report must include:
- Marker: `CODEX_KUN_K3_SURVEYS_TEST_GAP_REPORT_20260707T105700Z`
- Status: PASS / PASS_WITH_FINDINGS / BLOCKED
- Commands run and results
- Current coverage map
- Proposed tests with exact filenames and assertion intent
- Optional exact patch proposals, but do not apply
- Safety ledger confirming no forbidden actions
