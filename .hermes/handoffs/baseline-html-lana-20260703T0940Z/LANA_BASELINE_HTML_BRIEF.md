# LANA BRIEF — baseline-html-distinct-20260703T0940Z — Build the public Baseline HTML page

Context:
- The operator asked: "the quartet build a HTML page that is publicly available and shows our Baseline distinctly" and then specifically asked Lana/Anthropic to do the HTML build.
- Hermes previously over-patched a cluttered cockpit. Your job is to replace that clutter with a clean, distinct, Baseline-first public HTML page.
- Canonical source of truth: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/plans/2026-07-01_205807-paper-prose-distillation-roadmap.md`
- Current status JSON: `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/live-steering-status.json`

Scope you may edit:
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/live-steering-cockpit.html`
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/baseline-roadmap.html`
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/mobile.html` only if needed for a small pointer/update
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/baseline-html-lana-20260703T0940Z/LANA_REPORT.md`

Out of scope / hard stop:
- No DB writes, no SQL, no migrations.
- No service restart, no deploy command.
- No product/wiki mutation.
- No git commit/push/merge.
- No secrets or credential reads.
- Do not edit unrelated report pages.

Design objective:
Build a clean, standalone-feeling public page at the stable URL `/agent-reports/live-steering-cockpit.html` that distinctly shows "The Baseline". It should not feel like a messy operational cockpit.

Required page semantics:
1. Title/hero must say plainly: "The Baseline" and "NebulaMind paper-to-prose operating plan".
2. Show the primitive prominently:
   `papers -> claim/status ledger -> research-status/debate map -> prose -> derived claims/evidence/trust`
3. Show the core invariants:
   - Ledger-primary.
   - Every prose sentence binds to the ledger.
   - Prose modality may never exceed evidence certainty.
4. Show exactly one canonical Step 0–10 list, with clear step names and gate/pass-condition summaries.
5. Step 10 must sound like completion of the wiki page, not just packet preparation:
   "Complete Galaxy Evolution wiki page through approval-gated exact-diff/product gate"
   Pass condition must mention approved exact diff applied, post-apply probes pass, rollback available, and canonical Galaxy Evolution wiki page verified complete.
6. Show current state distinctly but secondarily:
   - Claim Ledger Contract subpacket PASS.
   - Overall Galaxy Evolution wiki page NOT COMPLETE.
   - Next safe step is Step 6 full research-status/debate map, docs-only.
7. Show Quartet roles distinctly: Hermes captain/verifies, Lana methods/design, Goru mechanical validation, Fable outside/adversarial review.
8. Include a concise safety ledger: DB writes 0, SQL mutations 0, deploy/restart 0, product publish 0, git push/merge 0.
9. Include public verification marker exactly:
   `LANA_BASELINE_DISTINCT_HTML_BUILT_20260703T0940Z`

Visual objective:
- High-quality static HTML/CSS, no external dependencies.
- Distinct sections, strong hierarchy, readable on desktop and mobile.
- Avoid repeated step lists. Avoid left-nav duplicating all steps. Avoid old cluttered cockpit language.
- It is okay to use a tasteful dark theme, cards, timeline, and small badges.

Implementation hints:
- You may generate the HTML directly with a small Python script or edit the file manually.
- Prefer robust static HTML over framework code.
- Keep `/agent-reports/live-steering-cockpit.html` as the stable public page. Also write the same or closely related page to `/agent-reports/baseline-roadmap.html` for a canonical filename.
- Hermes will mirror/verify the public served root after your source edit; you do not need to deploy/restart.

Verification you should run:
- Confirm both HTML files contain `LANA_BASELINE_DISTINCT_HTML_BUILT_20260703T0940Z`.
- Confirm `live-steering-cockpit.html` contains exactly one detailed Step 0–10 list (no duplicate nav step list and no duplicate graphical chain).
- Confirm Step 10 text includes "verified complete".
- Confirm no DB/deploy/git commands were run.

Report:
Write `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/baseline-html-lana-20260703T0940Z/LANA_REPORT.md` with:
- PASS or BLOCKED.
- Files edited.
- Design summary.
- Verification commands/results.
- Safety ledger.
- Any caveats.
- End with standalone marker line:
  `LANA_BASELINE_DISTINCT_HTML_BUILT_20260703T0940Z`

Done condition:
- HTML files written, report written, verification commands run, no out-of-scope actions.
