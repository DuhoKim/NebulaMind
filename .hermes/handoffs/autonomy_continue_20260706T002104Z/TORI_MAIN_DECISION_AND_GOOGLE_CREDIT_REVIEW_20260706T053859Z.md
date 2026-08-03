# Tori main decision helper + Google credit investigation — 20260706T053859Z

Marker: `MAIN_DECISION_GATE_20260706T053859Z`

Status: `REPORT_COMPLETE_NO_EXECUTION`

## Main decision HTML

Local standalone files generated:

- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/main-decision-20260706T053859Z.html`
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/latest-main-decision.html`
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/main-decision-20260706T053859Z.json`
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/latest-main-decision.json`

Mirrored local-live files were also written under:

- `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/`

Public note: new report filenames currently return 404 from the live site without a static-server refresh, so the same decision summary was rendered into the stable served cockpit instead.

Public verified served pages:

- `https://nebulamind.net/agent-reports/live-steering-cockpit.html`
- `https://nebulamind.net/agent-reports/live-steering-status.json`
- `https://nebulamind.net/agent-reports/mobile.html`
- `https://nebulamind.net/agent-reports/copy-execution-phrase.html`
- `https://nebulamind.net/agent-reports/latest-execution-phrase.txt`

Verification: HTTP 200, `NO ACTIVE EXECUTION PHRASE` present, packet execution phrases absent. Stable cockpit/status/mobile include `MAIN_DECISION_GATE_20260706T053859Z`.

## Main decision stated

Recommended immediate decision: keep NebulaMind DB writes unarmed and contain the Google/Gemini credit burn first. After billing is quiet, choose exactly one next lane:

1. execute P2 later with its exact local packet phrase;
2. execute P5 later with its exact local packet phrase;
3. skip DB writes for now and decide P1/P3/P4 spec lanes first.

No packet-specific execution phrase is quoted in public or in this receipt.

## Google / Gemini credit investigation

### Strongest local suspects

1. `goru-agy` tmux pane
   - tmux pane: `goru-agy:0.0`
   - PID: `19248`
   - command: `/Users/duhokim/.local/bin/agy --model Gemini 3.1 Pro (High)`
   - cwd: `/Users/duhokim/.openclaw/workspace`
   - runtime: about 5 days 20 hours
   - CPU sample: about 4–8%
   - network: established remote 443 connections to `34.54.84.110` and `216.239.32/36.223`; local listeners on 127.0.0.1 ports 50404/50405
   - pane state: at prompt after the P5 repaired payload report; not currently writing files
   - interpretation: likely Antigravity/agy Google AI route; likely candidate for Google AI/Antigravity credit usage. Ultra quota source is not proven from local evidence because no non-secret tier/credit `/stats` readout was obtained.

2. Three standalone Gemini CLI node process pairs
   - parent/child pairs: `6320/6459`, `7316/8856`, `9792/9794`
   - command: `/opt/homebrew/bin/gemini --skip-trust`
   - cwd: `/Users/duhokim/NebulaMind/NebulaMind`
   - runtimes: about 23–24 hours
   - CPU sample: 0.0%
   - network: child nodes have established remote 443 connections to `104.16.8/9/10.34`
   - tmux listing: not associated with a visible current tmux pane in `tmux list-panes`
   - environment check: no `GOOGLE_API_KEY`, `GEMINI_API_KEY`, `GOOGLE_CLOUD_PROJECT`, Vertex, ADC, Anthropic, or OpenAI env vars found in those process environments
   - interpretation: likely stale/hidden Gemini CLI sessions. They may not be actively burning while idle, but they are unnecessary open candidates and should be stopped if the goal is to eliminate Google-credit leakage.

### Things not implicated

- Current Hermes model route: `openai-codex` / `gpt-5.5`, not Gemini.
- Hermes config has no `model.base_url` override.
- Hermes `.env` does not define `GOOGLE_API_KEY`, `GEMINI_API_KEY`, `GOOGLE_CLOUD_PROJECT`, `GOOGLE_GENAI_USE_VERTEXAI`, `GOOGLE_GENAI_USE_GCA`, `GOOGLE_APPLICATION_CREDENTIALS`, or Vertex project vars.
- Active process env for the suspect PIDs also did not contain those Google/GCP/API-key variables.
- Hermes cron jobs: one paused, one completed; none active.
- User crontab: no Google/Gemini match.
- Launchd Google match found only Google Updater, not model usage.
- `gcloud` is not installed in this shell, so no direct GCP billing/logging query was available locally.
- `ccusage` is not installed in this shell, so local token/cost accounting was unavailable.

### Gemini/Ultra route interpretation

- `~/.gemini/settings.json` has `security.auth.selectedType = oauth-personal`.
- `~/.gemini/google_accounts.json` exists, but `active_present = false`.
- `~/.gemini/gemini-credentials.json` exists but is not normal JSON; likely encrypted/opaque credential storage.
- Therefore standalone Gemini CLI Google-login / Ultra usage is not proven from config alone.
- The active `agy` process may be authenticated separately through Antigravity; model availability is proven by the running process, but Ultra quota source is not proven without a non-secret tier/credit stats readout.

## Actions not taken

- Did not kill or pause `goru-agy` because it is a visible named lane and stopping it would be a side effect.
- Did not kill the standalone `gemini --skip-trust` processes because stopping user processes should be explicitly approved.
- Did not install tools, query GCP billing APIs, or mutate cloud state.
- Did not execute any NebulaMind DB/SQL/prose/git/deploy action.

## Recommended next action

If the goal is to stop the leak immediately, approve stopping the Google/Gemini lanes. The least disruptive order is:

1. Stop the three stale standalone `gemini --skip-trust` process pairs.
2. Pause/stop `goru-agy` if you do not want Goru/Antigravity consuming more Google AI credit.
3. Keep NebulaMind packets at `NO ACTIVE EXECUTION PHRASE` until billing is quiet.

Safety state remains:

- Active execution phrase: `NO ACTIVE EXECUTION PHRASE`
- DB writes: 0
- SQL/apply/rollback execution: 0
- Trust recompute: 0
- Prose/wiki publish: 0
- Git/deploy/restart: 0
