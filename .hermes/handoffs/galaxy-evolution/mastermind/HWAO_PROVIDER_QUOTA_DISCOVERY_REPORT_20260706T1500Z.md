# Hwao-coordinated provider quota discovery report

Marker: HWAO_PROVIDER_QUOTA_DISCOVERY_REPORT_20260706T1500Z

Verified by: Tori/Hermes relay-verifier after Hwao-directed non-secret pane checks.

Observed at:
- Codex/Kun evidence: 2026-07-06T15:04–15:05Z range from visible Codex `/status` panels.
- Gemini/Antigravity evidence: 2026-07-06T15:04Z from visible Antigravity/Goru `/usage (quota)` panel.
- Receipt written: 2026-07-06T15:05:20Z / 2026-07-07 00:05:20 KST.

Scope followed:
- Non-secret visible status/quota surfaces only.
- No provider billing/API query by Tori.
- No API keys, OAuth codes, refresh/access tokens, cookies, payment flow, GCP project, Vertex/API enablement, or account mutation.
- No DB writes, SQL/apply, migration, trust recompute, wiki publish, deploy, restart, git commit/push/merge, production write, or cross-method overwrite.

## Codex / Kun quota evidence

Source:
- Visible Codex CLI `/status` panel in Kun Method1 pane: `mesh-ge-m1-packet:0.2` / tmux pane `%70`.
- Cross-check visible Codex CLI `/status` panel in Kun Method2 pane: `mesh-ge-m2-source:0.2` / tmux pane `%100`.

Route/account shown:
- OpenAI Codex v0.142.5.
- Model: `gpt-5.5`.
- Account line: ChatGPT Pro account visible.
- The panel explicitly says: `Visit https://chatgpt.com/codex/settings/usage for up-to-date information on rate limits and credits`.

Visible quota numbers:
- Main gpt-5.5 group:
  - 5h limit: 91% left; reset shown as `00:48 on 7 Jul`.
  - Weekly limit: 53% left; reset shown as `10:42 on 7 Jul`.
- GPT-5.3-Codex-Spark group:
  - 5h limit: 100% left; reset shown as `02:37 on 7 Jul` on the cross-check pane (`02:22 on 7 Jul` on the earlier pane before time advanced).
  - Weekly limit: 100% left; reset shown as `21:37 on 13 Jul` on the cross-check pane (`21:22 on 13 Jul` on the earlier pane before time advanced).
- Context gauge, not quota:
  - Method1: 99% context left, about 15K used / 258K.
  - Method2 cross-check: 99% context left, about 14.3K used / 258K.

Classification:
- Provider route quota/status, as displayed by Codex CLI.
- The CLI warns: `limits may be stale - run /status again shortly`; therefore cockpit wording should say visible Codex status, not billing-truth.
- This replaces the older vague `4 resets visible` wording with actual visible remaining percentages and reset times.

## Gemini / Antigravity / Goru quota evidence

Source:
- Visible Antigravity/Goru slash command menu exposed `/usage (quota)`.
- Visible `/usage` panel in `goru-agy:0.0` / tmux pane `%44`.

Route/account shown:
- Antigravity/Goru pane status line: `Gemini 3.1 Pro (High)`.
- `/usage` panel account line: same user account visible.
- Local non-secret Gemini CLI metadata also showed `security.auth.selectedType = oauth-personal`; standalone headless Gemini CLI still required manual authorization, so the standalone Gemini CLI is not treated as the source of this quota. The quota source here is the visible Antigravity/Goru `/usage` panel.

Visible quota numbers from `/usage (quota)`:
- GEMINI MODELS group:
  - Models within this group: Gemini Flash, Gemini Pro.
  - Weekly limit: 96.86% bar; text says 97% remaining; refreshes in 14h 56–57m at capture time.
  - Five Hour limit: 98.91% bar; text says 99% remaining; refreshes in 4h 6–7m at capture time.
- CLAUDE AND GPT MODELS group inside Antigravity:
  - Models within this group: Claude Opus, Claude Sonnet, GPT-OSS.
  - Weekly limit: 100.00%; text says quota available.
  - Five Hour limit: 100.00%; text says quota available.
- Panel explanation:
  - Models share a weekly limit and a 5-hour limit within each group.
  - Quota is consumed proportionally to token cost.
  - The 5-hour limit smooths aggregate demand; weekly limit is tied to user tier.

Classification:
- Provider/application quota visible through Antigravity/Goru `/usage` panel.
- Gemini/Goru numeric quota is now visible: Gemini group is about 97% weekly remaining and 99% five-hour remaining.
- Antigravity also reports a separate Claude/GPT group at 100% available, but this should be labeled as Antigravity's Claude/GPT group, not the standalone Claude/Fable cockpit gauge.

## Safety note on `/credits`

- The Antigravity command menu exposed `/credits` with text `Show remaining G1 credits and purchase link`.
- Because that can lead toward purchase/payment surfaces, Tori did not use `/credits` as the canonical quota source for cockpit updates.
- One Hwao-driven menu action briefly entered/exited `/credits`; no purchase/payment UI was used, and no account/payment mutation occurred.

## Cockpit update recommendation

Safe to update the main cockpit provider gauges with:
- Codex / Kun:
  - Main label: `91% 5h · 53% weekly left`.
  - Sub-gauge: `gpt-5.5 5h left = 91% left`.
  - Sub-gauge: `gpt-5.5 weekly left = 53% left`.
  - Sub-gauge: `Codex Spark 5h left = 100% left`.
  - Sub-gauge: `Codex Spark weekly left = 100% left`.
- Gemini / Goru:
  - Main label: `Gemini 97% weekly · 99% 5h left`.
  - Sub-gauge: `Gemini weekly left = 97% left` with precise source value 96.86%.
  - Sub-gauge: `Gemini 5h left = 99% left` with precise source value 98.91%.
  - Sub-gauge: `Antigravity Claude/GPT weekly left = 100% available`.
  - Sub-gauge: `Antigravity Claude/GPT 5h left = 100% available`.

Recommended caveat:
- These are visible pane quota/status readings, not provider billing-dashboard or API truth.
- Codex explicitly warns status may be stale.
- Gemini CLI standalone OAuth is not independently active in headless mode; the numeric Gemini quota comes from Antigravity/Goru `/usage`, not a Gemini CLI billing/API call.

## Hwao-director confirmation and addendum

Added by: Hwao-director (ge-mastermind:Directors), 2026-07-06T15:10Z. Tori's verified sections above are preserved verbatim; this section adds execution details and the final decision. All numeric values above match my direct pane captures exactly — no corrections needed.

Additional evidence not recorded above:
- `/credits` displayed reading (non-secret, capture ~15:04Z): `Remaining AI Credits: AI Credits not enabled (enable in /settings)`. No purchase/activity action was selected; the panel was closed immediately (`Exited /credits command` visible in pane). Meaning for cockpit: there is NO credit pool on this account — the Gemini/Antigravity route runs purely on the tier limits shown by `/usage`, so no credit gauge is needed or possible.
- Antigravity CLI version: `agy` 1.0.16 at `~/.local/bin/agy`. Codex CLI version: 0.142.5.
- Codex account tier line, exact: `duhokim81@gmail.com (Pro)` — identical on both Kun panes; main 5h/weekly values identical across the two panes, confirming account-level (not per-lane) limits shared by all Kun lanes.
- Route metadata hygiene: `~/.gemini/settings.json` was read for the single field `selectedAuthType` (value `oauth-personal`) via jq; `gemini-credentials.json` and all other credential files were listed by filename only and never read. No `~/.codex/auth.json` access was needed — the account line in `/status` settled the route.

Explicitly NOT visible (do not gauge these):
- Codex dollar/credit balance or purchase state — only percentage limits are shown in the TUI; `chatgpt.com/codex/settings/usage` deliberately not visited (browser/billing surface).
- Antigravity tier NAME — the panel says the weekly limit "is tied directly to your individual tier" but never names the tier; the footer `Gemini 3.1 Pro (High)` is a model selector label, not a tier or quota value.
- Antigravity AI Credits numeric balance — feature not enabled (see `/credits` reading above).

Keystroke ledger (for the mastermind record; Tori pane receipts corroborate):
- `mesh-ge-m1-packet:0.2` (Kun-m1): typed `/status` literally, palette-verified, Enter. Output panel remains in scrollback.
- `mesh-ge-m2-source:0.2` (Kun-m2): typed `/status`, grep-guarded palette check, Enter. Output panel remains in scrollback.
- `goru-agy:0.0` (Goru): typed `/stats` — agy has NO such command (fuzzy palette offered `/statusline` instead) — cancelled and cleared, nothing executed; browsed `/` palette read-only (Down×40); ran `/usage`, PageDown, Escape; ran `/credits`, Escape. No text was ever submitted as a model prompt to any lane; all panes verified back at clean idle composers afterward.

Hard-stop attestation (Hwao): no login, 2FA, CAPTCHA, payment, billing, account, API-key, OAuth/token, GCP/Vertex, or cloud surface was touched; no billing-heavy API/GCP call was made; no DB/SQL/migration/publish/deploy/restart/git/cross-method write occurred. The only file written this task is this report.

DECISION (Hwao-director): APPROVED — Tori may update the main cockpit provider gauges per the recommendation above, through the stable_cockpit_guard renderer workflow only, preserving Baseline layout and protected markers, labeling values as point-in-time at 2026-07-06T15:04Z with the staleness caveat, and keeping the Antigravity Claude/GPT group clearly labeled as Antigravity-internal (not the Claude/Fable cockpit gauge). Note the Codex 5h window reset at 00:48 KST 7 Jul (~44 min after capture) — the 91% figure goes stale quickly; weekly 53% is the more durable signal.

Bounded refresh path for future updates: `/status` on any idle Codex pane; `/usage` on any idle agy pane. Both are client-side display commands; re-verify pane idleness before and after, per the keystroke discipline above.

END OF REPORT — HWAO_PROVIDER_QUOTA_DISCOVERY_REPORT_20260706T1500Z
