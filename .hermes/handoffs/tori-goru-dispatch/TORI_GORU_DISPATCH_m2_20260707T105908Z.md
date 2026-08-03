# Tori -> Goru dispatch

Target: m2
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

# Gemini/Goru G3 autonomous Surveys accessibility/static audit

Marker: `GORU_G3_SURVEYS_ACCESSIBILITY_BRIEF_20260707T105700Z`
Run: `SURVEYS_LOW_USAGE_AUTONOMOUS_RUN_20260707T105700Z`
Target lane: Gemini / Goru mechanical lane

## Mission

Use Gemini/Goru quota for a bounded mechanical accessibility/static audit of Surveys UI components. Produce a report; do not modify product files.

## Absolute boundaries

- Artifact/report only.
- Do not edit product/source/generated public files.
- No DB writes, SQL, migrations, deploy/restart, git, wiki publish, cron, browser automation, provider/account/billing/API/GCP/OAuth/token/credential activity.
- Read-only file inspection and static pattern checks are allowed.

## Inspect these paths

Repo root: `/Users/duhokim/NebulaMind/NebulaMind`

- `frontend/src/components/surveys/ControlBar.tsx`
- `frontend/src/components/surveys/BandSpectrumStrip.tsx`
- `frontend/src/components/surveys/FilterSheet.tsx`
- `frontend/src/components/surveys/SurveyCard.tsx`
- `frontend/src/components/surveys/SurveyPeek.tsx`
- `frontend/src/components/surveys/ChartView.tsx`
- `frontend/src/components/surveys/PlotA.tsx`
- `frontend/src/components/surveys/PlotB.tsx`
- `frontend/src/app/surveys/[slug]/SurveyDetailClient.tsx`

## Mechanical tasks

1. Count clickable divs vs native buttons/links.
2. Check keyboard access for click targets.
3. Check SVG role/title/desc parity for PlotA and PlotB.
4. Check disclosure buttons for `aria-expanded` and `aria-controls`.
5. Check modal/sheet focus/escape/backdrop behavior for obvious gaps.
6. Rank findings by user impact and implementation risk.

## Required output

Write exactly one report file:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/surveys-low-usage-autonomous/20260707T105700Z/GORU_G3_SURVEYS_ACCESSIBILITY_REPORT_20260707T105700Z.md`

Report must include marker `GORU_G3_SURVEYS_ACCESSIBILITY_REPORT_20260707T105700Z`, status, static findings, path references, and safety ledger.

Done marker: TORI_GORU_DISPATCH_DONE_20260707T105908Z

```
