# Provider gauges unified to percent-used convention

Marker: PROVIDER_GAUGES_UNIFIED_USED_RECEIPT_20260706T153655Z

User correction:
- Provider usage limits were hard to comprehend because some bars/text used "used" while others used "left" or "available".
- Unify the display.

Applied convention:
- Every provider/status bar now displays percent used.
- Observed remaining/available quota readings were converted before display.
- Source caveats are still present, but the displayed direction stays percent used.

Conversions now shown:
- Claude / Fable / Lana:
  - Fable model used: 22% used.
  - All Claude models used: 16% used.
- Codex / Kun:
  - gpt-5.5 5h used: 9% used.
  - gpt-5.5 weekly used: 47% used.
  - Codex Spark 5h used: 0% used.
  - Codex Spark weekly used: 0% used.
- Gemini / Goru:
  - Gemini weekly used: 3% used.
  - Gemini 5h used: 1% used.
  - Antigravity Claude/GPT weekly used: 0% used.
  - Antigravity Claude/GPT 5h used: 0% used.
- Tori / Hermes:
  - Context gauge: up to 70% context used.

Files updated:
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/stable-cockpit-canonical.json`
- Rendered both stable public roots through `tools/stable_cockpit_renderer.py render-all-public-roots`.

Current cockpit marker preserved:
- `ULTRA_USAGE_FORMAT_GATE_COCKPIT_20260706T153234Z`

Guard verification:
- `tools/stable_cockpit_guard.py check --marker ULTRA_USAGE_FORMAT_GATE_COCKPIT_20260706T153234Z` returned PASS.
- Public cockpit HTTP status: 200.
- Public marker present: yes.
- Rich stable cockpit contract present: yes.
- Stable roots relocked with `uchg`: yes.

Exact public/content verification:
- Provider card count: 4.
- Sub-gauge count: 10.
- Status JSON provider count: 4.
- Status JSON sub-gauge count: 10.
- Codex used label present: `gpt-5.5 9% 5h · 47% weekly used`.
- Gemini used label present: `Gemini 3% weekly · 1% 5h used`.
- Spark zero-used labels present.
- Provider data mixed-direction phrases absent: yes.
- Old provider phrases absent from HTML: yes (`91% 5h / 53% weekly left`, `97% weekly / 99% 5h left`, `100% available`, `raw remaining`).
- `APPROVE EXECUTE` absent: yes.
- `NO ACTIVE EXECUTION PHRASE` present: yes.

Safety boundary:
- No live wiki publish.
- No page_versions write.
- No DB/SQL/migration/trust recompute.
- No deploy/restart.
- No git commit/push/merge.
- No cloud/API/GCP/billing/account/payment/credits action.
- No browser automation.
- No Ultra/Gemini/Antigravity prompt execution.

Result:
- Provider usage gauges are now readable in one convention: percent used.
