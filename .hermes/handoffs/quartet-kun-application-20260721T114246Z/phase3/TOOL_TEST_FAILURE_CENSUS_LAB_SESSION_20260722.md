# Tool-test failure census — Kun recommendation #6

By: Claude Code (Lab session), 2026-07-22. Read-only/tests, no gate. Pins the exact failing node IDs +
cause + fix-vs-quarantine recommendation per each (Kun: "no broad skip, no quarantine claim before a decision").
Suite run: `pytest tools/tests/ tests/test_render_ge_autopilot_dashboard_v2.py tests/test_galaxy_evolution_autopilot.py`
Result: **4 failed, 132 passed** (Kun's July-21 count was 5; the set shifted as autopilot markers advanced — this is the current, exact list).

## The 4 failures (exact node IDs)

### Cause A — stale hardcoded overnight-report markers (3) · time-dependent, brittle
The tests assert a specific date-stamped marker string that the live renderer advances over time
(current marker: `GE_AUTOPILOT_OVERNIGHT_20260719_CORPUS_GATES_DONE`; tests pin `..._20260712` / `_C1R_REPAIR_20260713...`).
Not a product bug — brittle test assertions ("staleness-window").
1. `tests/test_render_ge_autopilot_dashboard_v2.py::test_overnight_report_uses_live_usage_snapshot`
   — asserts `report["marker"] == "GE_AUTOPILOT_OVERNIGHT_REPORT_20260712"` (line 47).
2. `tools/tests/test_ge_autopilot_dr_overnight_report.py::test_deep_research_overnight_report_shows_completed_offline_repair`
   — EXPECTED_MARKER hardcoded `GE_AUTOPILOT_C1R_REPAIR_20260713T010203Z_DONE` (line 14).
3. `tools/tests/test_ge_autopilot_dr_overnight_report.py::test_private_html_keeps_usage_first_and_deep_research_panel_is_read_only`
   — asserts the same stale marker present in rendered HTML.
   → RECOMMEND FIX: assert marker *shape/prefix* (`GE_AUTOPILOT_OVERNIGHT_*` / structural invariants) instead of a
     frozen date string; or feed a fixed marker via fixture. Low-risk, test-only.

### Cause B — stale renderer API reference (1) · code drift
4. `tools/tests/test_nous_credits_usage.py::test_stable_cockpit_renders_amount_first_without_a_main_percentage`
   — calls a `stable_cockpit_renderer.render_*` attribute that no longer exists (the renderer was refactored;
     current render_* funcs: render_provider_usage_gauges, render_pills, render_stable_cockpit_html, ...).
   Not a product bug — the renderer works; the test references an old API name.
   → RECOMMEND FIX: point the test at the current renderer function / update the expected shape. Low-risk, test-only.

## Verdict
All 4 are pre-existing **test-maintenance staleness**, disjoint from the product/backend suite (which is green).
None are product regressions. Recommendation: **FIX** (all four are trivial, test-only) rather than quarantine —
a quarantine would just hide brittle tests that are cheap to make robust. Awaiting decision per Kun's #6.

---

## RESOLVED — 2026-07-22 (all 4 fixed, suite green: 136 passed, 0 failed)

Fix command: `pytest tools/tests/ tests/test_render_ge_autopilot_dashboard_v2.py tests/test_galaxy_evolution_autopilot.py` → **136 passed**.

Root causes were deeper than "stale markers": three tests pinned an *entire hand-updated report snapshot*, one was a `sys.modules` pollution flake.

1. **tests/test_render_ge_autopilot_dashboard_v2.py** — marker + card-title + `next_action` text were frozen to the 20260712 snapshot. Fixed: derive marker from `RENDERER.OVERNIGHT_REPORT_MARKER`; keep the input-derived `Usage quota` card checks; replace the frozen `Goru custody incident` card assertion and the `trusted extractor` next_action text with structural checks (≥2 cards, each has title/status; next_action non-empty).

2. **tools/tests/test_ge_autopilot_dr_overnight_report.py** — `test_deep_research...` pinned the whole 20260713 C1R-repair report (headline, 7 exact card titles, a *fixed* `reported_at_utc` that is now dynamic/current-time). Fixed: `EXPECTED_MARKER = renderer.OVERNIGHT_REPORT_MARKER`; rewrote the test to the stable read-only contract — marker matches the renderer constant, `approval_phrase == "NO ACTIVE EXECUTION PHRASE"`, usage-first card, structural card shape, and the old stale-marker negative regression checks. `test_private_html` needed only the derived marker (panel ordering / h2 / no-buttons/forms already held).

3. **tools/tests/test_nous_credits_usage.py** — NOT a stale API. `test_monitor_pane_selection.py` and `test_provider_usage_quota_parsing.py` inject a *stub* `stable_cockpit_renderer` (only `DEFAULT_PUBLIC_ROOTS`/`write_outputs`) into `sys.modules`; running alphabetically before the nous test, the stub shadowed the bare `import stable_cockpit_renderer` → missing `render_provider_usage_gauges`. Fixed: load the real module by path via `importlib.util.spec_from_file_location`. Now order-independent (verified: passes with the stub-polluters forced first).

All four files are untracked local dev/ops tooling (not product, not on `main`) — edited in place, no PR.
