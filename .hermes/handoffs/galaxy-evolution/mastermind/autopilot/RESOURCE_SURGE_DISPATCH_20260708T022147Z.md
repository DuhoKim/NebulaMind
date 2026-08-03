# Resource surge dispatch — evidence/trust verification

Marker: RESOURCE_SURGE_EVIDENCE_TRUST_20260708T022147Z

User direction: only 4 panels are running while 14 are idle; use all useful resources, especially models with large quota/usage headroom.

Scope: safe read-only/static verification and no-apply reporting for the Galaxy Evolution evidence/trust candidates. No live-root copy, no product DB/API/page_versions, no product-wiki publish, no deploy/restart, no git, no cloud/OAuth/secrets/browser/cron.

Priority resources:
- Goru/Gemini High lanes for mechanical audits.
- Kun/Codex lanes for independent scriptable checks.
- Lana/Hwao only for no-apply review/coordination where safe; do not press stale mirror-apply prompts.

Required outputs: each dispatched lane writes one report under `.hermes/handoffs/galaxy-evolution/...` with this marker, exact inspected paths, PASS/WARN/FAIL, and next action if any.

Do not approve or execute any mirror/live-root write. The final evidence/trust packet is already READY_FOR_USER_APPROVAL; this surge improves independent verification only.
