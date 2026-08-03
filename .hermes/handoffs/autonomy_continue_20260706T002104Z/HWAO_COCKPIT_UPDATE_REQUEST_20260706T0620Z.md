# Hwao cockpit update request — 20260706T0620Z

Marker: `HWAO_COCKPIT_UPDATE_REQUEST_20260706T0620Z`

## User request

"Many tmux lanes are either offline or not active. Let Hwao update the cockpit so that I can choose next move."

## Current lane state from Tori's read-only tmux inspection

Present sessions/panes:

- `lana-fable` — present, Claude/Fable lane, but stale/idle with old trust-recompute approval phrase sitting in input; must be cleared before any new prompt.
- `lana-claude` — present, but stale/idle with old text in input.
- `lana-exec-2929` — present, idle.
- `kun-codex` — present, but idle at generic "Explain this codebase" prompt.
- `hermes-main` — current Tori lane.

Missing/offline:

- `hwao-exec-2929` — missing.
- `goru-agy` — missing/offline by design after Google/Gemini credit-burn containment.

## Safety state

- Public/standing phrase: `NO ACTIVE EXECUTION PHRASE`.
- DB writes: 0.
- SQL/apply/rollback: 0.
- trust recompute: 0.
- prose/wiki/page_versions publish: 0.
- product code patch: 0.
- git/deploy/restart: 0.
- cloud/GCP/API mutation: 0.
- Old OpenClaw LaunchAgents were disabled/booted out only; plist files were not deleted.
- Final process scan found no OpenClaw/Gemini/Google-credit suspect process after filtering normal Chrome/macOS services.

## Current artifacts / already prepared state

Prepared docs-only specs are present at:

`docs/hwao_morning_blocker_specs_20260706T0308Z/`

- `P1_LEGACY_OVERCLAIMS_2298_2299_2924_SPEC.md`
- `P3_2572_PRIMACY_RECAST_SPEC.md`
- `P4_LEVEL_SCORE_GUARD_RECOMPUTE_SPEC.md`
- `BLOCKER_SPECS_RESULT.md`
- `READONLY_API_SNAPSHOT_20260706T0308Z.json`

Tori verified these remain docs-only, no active phrase, no public execute phrase, and manifest 5/5 passes.

Prepared P2/P5 packets exist locally from the morning cycle but are not active and their packet-specific approval phrases must stay local-only, not public.

## What Hwao should decide for the cockpit

Please write a short coordinator direction for a public cockpit decision gate. The cockpit should help the user choose the next move and plainly show that many lanes are idle/offline.

Please include:

1. Current status headline.
2. Plain lane board: active/idle/offline and whether each lane may be used now.
3. Recommended next move options with labels the user can choose.
4. Which option Hwao recommends first, if any.
5. Explicit exclusions and hard safety ledger.
6. Whether Tori is authorized to apply the static cockpit update via the canonical renderer and public verification.
7. Marker to include in the cockpit.

Do not authorize DB writes, SQL/apply/rollback, trust recompute, prose/wiki publish, product code patch, git/deploy/restart, or GCP/Gemini/Antigravity usage.

Please write your answer to:

`.hermes/handoffs/autonomy_continue_20260706T002104Z/HWAO_COCKPIT_DECISION_GATE_DIRECTION_20260706T0620Z.md`

Required marker: `HWAO_COCKPIT_DECISION_GATE_DIRECTION_20260706T0620Z`
