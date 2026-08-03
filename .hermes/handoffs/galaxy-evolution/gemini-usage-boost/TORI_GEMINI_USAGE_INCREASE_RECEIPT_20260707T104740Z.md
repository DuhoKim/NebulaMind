# Tori Gemini/Goru usage increase receipt

Marker: `TORI_GEMINI_USAGE_INCREASE_RECEIPT_20260707T104740Z`
Status: PASS

## User request

User asked to increase the Gemini line usage because the dashboard usage was low.

## Action taken

Dispatched four safe, read-only Antigravity/Goru audit packets to existing Goru panes using `tori-goru-dispatch`.

No new Gemini/GCP/API/billing/account surfaces were opened. No browser automation. No DB/wiki/deploy/git/cron action.

## Goru jobs dispatched

Dispatch logs:

- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/tori-goru-dispatch/TORI_GORU_DISPATCH_goru_20260707T104213Z.md`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/tori-goru-dispatch/TORI_GORU_DISPATCH_m1_20260707T104213Z.md`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/tori-goru-dispatch/TORI_GORU_DISPATCH_m2_20260707T104213Z.md`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/tori-goru-dispatch/TORI_GORU_DISPATCH_m3_20260707T104213Z.md`

Completed Goru reports and verified markers:

- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/gemini-usage-boost/GORU_STANDALONE_USAGE_TELEMETRY_AUDIT_20260707T104025Z.md`
  - marker verified: `GORU_STANDALONE_USAGE_TELEMETRY_AUDIT_DONE_20260707T104025Z`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/gemini-usage-boost/GORU_M1_STATIC_DEEP_AUDIT_20260707T104025Z.md`
  - marker verified: `GORU_M1_STATIC_DEEP_AUDIT_DONE_20260707T104025Z`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/gemini-usage-boost/GORU_M2_SOURCE_STATIC_AUDIT_20260707T104025Z.md`
  - marker verified: `GORU_M2_SOURCE_STATIC_AUDIT_DONE_20260707T104025Z`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/gemini-usage-boost/GORU_M3_DEBATE_STATIC_AUDIT_20260707T104025Z.md`
  - marker verified: `GORU_M3_DEBATE_STATIC_AUDIT_DONE_20260707T104025Z`

## Usage monitor result

Before the boost, dashboard Gemini/Goru line showed:

- `Gemini 0% used weekly · 1% used 5h`

After the four Goru jobs completed, I ran the existing safe monitor refresh through an idle visible Antigravity `/usage` pane.

Public and private dashboards now show:

- `Gemini 1.2% used weekly · 3.8% used 5h`

Observed source:

- `Idle Antigravity pane %44 /usage observed 2026-07-07T10:47:04Z; active Goru/Gemini panes: 4.`

Sub-gauges:

- Gemini weekly used: `1.2% used · 99% remaining · refresh 163h 13m`
- Gemini 5h used: `3.8% used · 96% remaining · refresh 3h 5m`
- Antigravity Claude/GPT weekly used: `0% used · Quota available`
- Antigravity Claude/GPT 5h used: `0% used · Quota available`

## URL verification

Public cockpit status:

- URL: `https://nebulamind.net/agent-reports/live-steering-status.json`
- HTTP: 200
- marker: `PROVIDER_USAGE_REALTIME_MONITOR_V1`
- observed: `2026-07-07T10:47:04Z`
- Gemini value: `Gemini 1.2% used weekly · 3.8% used 5h`

Private autopilot status:

- URL: `https://duho-macstudio.taila27502.ts.net/cockpit/ge-autopilot-status.json`
- HTTP: 200
- marker: `GE_AUTOPILOT_PROVIDER_USAGE_REALTIME_FEED_V1`
- observed: `2026-07-07T10:47:04Z`
- Gemini value: `Gemini 1.2% used weekly · 3.8% used 5h`

## Safety boundaries observed

- No DB/SQL writes.
- No `/api/pages`, page_versions, or live wiki publish.
- No deploy/restart/service mutation.
- No git commit/push/merge/rebase/reset.
- No cloud/GCP/Gemini API/billing/account/payment/credits/OAuth/token/secrets action.
- No credential/token/cookie files read.
- No browser automation.
- No cron.
- Public/private usage gauges refreshed only via visible Antigravity `/usage` and existing static dashboard monitor.
