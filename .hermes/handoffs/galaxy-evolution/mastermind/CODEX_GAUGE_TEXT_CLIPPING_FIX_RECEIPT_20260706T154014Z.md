# Codex provider gauge text clipping fix

Marker: CODEX_GAUGE_TEXT_CLIPPING_FIX_20260706T154014Z

User correction:
- The Codex usage-limit gauge was broken; text was not shown fully.

Cause found:
- Provider gauge cards were laid out four-across with `.provider-gauge-card { grid-column: span 3 }`.
- Gauge value text was centered inside a fixed-height pill with `overflow:hidden`.
- Codex has the longest reset labels, so the label text could be clipped/truncated visually.

Change made:
- Patched `tools/templates/stable-cockpit-template.html` only.
- Provider gauge cards now use two-column layout: `.provider-gauge-card { grid-column: span 6; min-width: 0 }`.
- Gauge tracks now use `min-height` + `height:auto` and `overflow:visible`.
- Gauge value text now uses `white-space: normal` and `overflow-wrap: anywhere`.
- Sub-gauge label rows now wrap instead of forcing long value text into one narrow row.

Rendered paths:
- Re-rendered both public roots via `python3 tools/stable_cockpit_renderer.py render-all-public-roots`.
- Preserved current cockpit marker: `ULTRA_USAGE_FORMAT_GATE_COCKPIT_20260706T153234Z`.

Guard verification:
- `python3 tools/stable_cockpit_guard.py check --marker ULTRA_USAGE_FORMAT_GATE_COCKPIT_20260706T153234Z` returned PASS.
- Public cockpit HTTP status: 200.
- Rich stable cockpit contract present: yes.
- Stable roots relocked with `uchg`: yes.

Public DOM/CSS verification:
- Codex card present: yes.
- Provider card count: 4.
- Sub-gauge count: 10.
- Codex labels present:
  - `gpt-5.5 9% 5h · 47% weekly used`
  - `9% used · resets 00:48 Jul 7`
  - `47% used · resets 10:42 Jul 7`
  - `0% used · resets 02:37 Jul 7`
  - `0% used · resets 21:37 Jul 13`
- New CSS present:
  - provider cards two columns: yes.
  - gauge track `overflow: visible`: yes.
  - gauge value `white-space: normal` + `overflow-wrap: anywhere`: yes.
  - sub-gauge labels wrap: yes.
- `APPROVE EXECUTE` absent: yes.
- `NO ACTIVE EXECUTION PHRASE` present: yes.

Headless Chrome layout verification:
- Browser: `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`, headless via Playwright.
- Public URL rendered: `https://nebulamind.net/agent-reports/live-steering-cockpit.html`.
- Codex card width: 562px.
- Codex card CSS grid column: `span 6`.
- Codex gauge track overflow: `visible`.
- Every Codex `.gauge-value` and `.sub-gauge-label b` text box checked `scrollWidth <= clientWidth` and `scrollHeight <= clientHeight`.
- Result: no Codex gauge value was clipped by its box.
- Debug screenshot saved locally: `/tmp/codex-provider-gauge-after-fix.png`.

Safety boundary:
- No live wiki publish.
- No page_versions write.
- No DB/SQL/migration/trust recompute.
- No deploy/restart.
- No git commit/push/merge.
- No cloud/API/GCP/billing/account/payment/credits action.
- No browser automation beyond headless read-only public layout verification.
- No Ultra/Gemini/Antigravity prompt execution.

Result:
- Codex provider usage gauge text is now wrap-safe and publicly verified as not clipped.
