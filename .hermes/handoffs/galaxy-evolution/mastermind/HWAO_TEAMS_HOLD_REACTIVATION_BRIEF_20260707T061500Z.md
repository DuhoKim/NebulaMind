# Hwao director brief — teams appear on hold; issue safe reactivation packet

User signal: “i think all teams are on hold.”

Tori live scan result:
- Most Method1/2/3 mesh panes are parked at prompts after completed work or stale composer text, not actively working.
- No background Hermes process is currently running.
- No real provider quota/auth blocker was found for the mesh work. Generic old banners exist, but the current state is mostly idle/completed.
- Current completed static docs-only page artifacts exist:
  - Method1 wiki page: `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/wiki-page.html`
  - Method2 wiki page: `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/wiki-page.html`
  - Method3 wiki page: `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/wiki-page.html`
- User explicitly approved Tori sessions to use Goru/Antigravity/Gemini subscription lanes more heavily for scoped mechanical/read-only helper work.
- This is NOT approval for Gemini/GCP API fallback/config changes, crons, billing/account changes, DB writes, deploy/restart, git writes, live wiki/page_versions publication, route/config mutation, or cockpit/global mutation.

Task for Hwao-director:
Write one concise reactivation packet at:
`.hermes/handoffs/galaxy-evolution/mastermind/HWAO_TEAMS_HOLD_REACTIVATION_PACKET_20260707T061500Z.md`

Packet requirements:
1. State whether the board is actually blocked or merely parked/completed.
2. Name the next safe useful work that can run now without new risky gate. Prefer: read-only comparative evaluation of the three independent method wiki pages for user evaluation.
3. Provide exact lane assignments and prompts for:
   - Goru/Antigravity: mechanical comparison and counts across the three pages, method leakage check, source/chip/citation marker inventory, safety marker/published-state check.
   - Kun/Codex: reproducibility/static artifact consistency check across the three pages and their known receipt/verdict files.
   - Lana/Fable if useful: qualitative evaluation of page clarity/differentiation/readability, read-only only.
   - Tori: receipt integration and independent file verification.
4. Keep the work docs/static/read-only unless a lane writes its assigned local Markdown report under `.hermes/handoffs/galaxy-evolution/mastermind/`.
5. Explicit locks: no live wiki/page_versions publish, DB/SQL/trust recompute, deploy/restart, git commit/push/merge, Gemini/GCP API/config/billing changes, cloud account actions, browser automation, cron, route/config mutation, cockpit/global/shared-parent changes, or P3 claim/citation binding.
6. Include exact expected report filenames for each lane.
7. End with marker: `HWAO_TEAMS_HOLD_REACTIVATION_PACKET_20260707T061500Z`.

Do not dispatch other panes yourself. Do not open browser. Do not publish. Stop after writing the packet.
