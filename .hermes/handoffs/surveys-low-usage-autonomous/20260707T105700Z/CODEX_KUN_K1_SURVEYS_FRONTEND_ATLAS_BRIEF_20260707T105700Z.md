# Codex/Kun K1 autonomous Surveys frontend Atlas audit

Marker: `CODEX_KUN_K1_SURVEYS_FRONTEND_ATLAS_BRIEF_20260707T105700Z`
Run: `SURVEYS_LOW_USAGE_AUTONOMOUS_RUN_20260707T105700Z`
Target lane: Codex / Kun, gpt-5.5 subscription lane

## Mission

Work on the NebulaMind Surveys pages by doing a grounded implementation audit of the `/surveys` Atlas/List/Explorer frontend surface. Produce a report with concrete, low-risk findings and exact patch proposals if useful.

## Absolute boundaries

- Artifact/report only.
- Do not edit product files.
- Do not commit, push, open PRs, deploy, restart services, publish wiki/pages, run DB writes, run migrations, or touch credentials/secrets/account/billing/API/GCP/OAuth/token surfaces.
- Do not modify generated public cockpit/dashboard files.
- You may run read-only inspections and safe tests. If a command would write caches, redirect caches/temp output outside the repo or skip and report.
- If you discover a safe patch, include it as an exact diff/proposal in your report; do not apply it.

## Repo and files to inspect

Repo root: `/Users/duhokim/NebulaMind/NebulaMind`

Primary files:
- `frontend/src/app/surveys/page.tsx`
- `frontend/src/components/surveys/SurveysView.tsx`
- `frontend/src/components/surveys/ControlBar.tsx`
- `frontend/src/components/surveys/BandSpectrumStrip.tsx`
- `frontend/src/components/surveys/ChartView.tsx`
- `frontend/src/components/surveys/PlotA.tsx`
- `frontend/src/components/surveys/PlotB.tsx`
- `frontend/src/components/surveys/plotting.ts`
- `frontend/src/components/surveys/constants.ts`
- `frontend/scripts/test-surveys-atlas-ia.mjs`
- `docs/survey_explorer_design_v1.md`

## Specific questions

1. Does current `/surveys` behavior match the Atlas IA smoke expectations and design intent?
2. Are there obvious accessibility gaps in PlotA/PlotB/List controls?
3. Are URL params, filters, and axis choices robust against malformed input?
4. Does current implementation accidentally leave planned design pieces dead/unused (for example PlotB, plotType, depth-vs-breadth)?
5. What are the top 3 low-risk next changes for Tori to apply later?

## Required verification

Run or inspect:
- `cd frontend && npm run test:surveys-atlas-ia`
- If you run other commands, list exact commands and whether they wrote outside repo.

## Required output

Write exactly one report file:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/surveys-low-usage-autonomous/20260707T105700Z/CODEX_KUN_K1_SURVEYS_FRONTEND_ATLAS_REPORT_20260707T105700Z.md`

Report must include:
- Marker: `CODEX_KUN_K1_SURVEYS_FRONTEND_ATLAS_REPORT_20260707T105700Z`
- Status: PASS / PASS_WITH_FINDINGS / BLOCKED
- Files inspected with path references
- Commands run and results
- Findings ranked High/Medium/Low
- Exact proposed patches, if any, but do not apply
- Safety ledger confirming no forbidden actions
