# HWAO Cockpit Direction — Decision Gate

Marker: HWAO_COCKPIT_DECISION_GATE_DIRECTION_20260706T0628Z
Issued by: Hwao (Fable), hwao-visible-20260706
Apply scope: Tori/Hermes — static cockpit update only

## 1) Status headline

**COCKPIT: DECISION GATE — ALL EXECUTION FROZEN.** Most lanes idle or offline; lana-fable quarantined for a stale unsent approval phrase. Duho picks the next move; nothing runs until a new explicit phrase is issued.

## 2) Lane board

| Lane | State | Usable now? | Note |
|---|---|---|---|
| hwao-visible-20260706 | ACTIVE | Yes — direction/chat only | Hwao decision seat |
| hermes-main | ACTIVE | Yes — relay/verify only | Tori; may apply this cockpit update only |
| lana-exec-2929 | IDLE | Standby | Clean prompt; usable only after user choice + new phrase |
| kun-codex | IDLE | Standby | Generic prompt; usable only after user choice |
| lana-claude | IDLE-STALE | No — needs hygiene | Old text in input; clear before any use |
| lana-fable | STALE-UNSAFE | **No — QUARANTINED** | Unsent old trust-recompute approval phrase in input. Never press Enter; clear-only; never reuse or display the phrase |
| hwao-exec-2929 | OFFLINE | No | Missing; relaunch only as part of a chosen move |
| goru-agy | OFFLINE BY DESIGN | No | Stays down — Google/Gemini credit-burn containment |

## 3) Next-move cards (user choice)

- **Card 1 — LANE HYGIENE SWEEP.** Clear stale input buffers: discard (never send) the old trust-recompute phrase in lana-fable; clear old text in lana-claude; optionally relaunch hwao-exec-2929 to a clean prompt. tmux-hygiene only, zero execution.
- **Card 2 — P1/P3/P4 DOCS REVIEW.** Walk the canonical docs-only specs at `docs/hwao_morning_blocker_specs_20260706T0308Z/` (manifest verified) and pick which blocker to promote. Promotion requires a future, separate explicit phrase — not part of this card.
- **Card 3 — P2/P5 PACKET STATUS (docs-only).** Inspect prepared local P2/P5 packets read-only. Packet approval phrases stay local-only and unpublished; nothing armed.
- **Card 4 — HOLD / STAND DOWN.** Keep the freeze; cockpit remains at this decision gate; no lane action.

## 4) Hwao recommendation

**Card 1 first.** The unsent trust-recompute phrase parked in lana-fable's input is the one live hazard on the board — a stray Enter would fire an approval. Clear it without sending, then Card 2 is the natural second move. Cards 2–4 are safe in any order after that.

## 5) Exclusions and hard safety ledger

- Standing public phrase: **NO ACTIVE EXECUTION PHRASE.**
- Ledger, all zero and staying zero under this direction: DB writes 0; SQL/apply/rollback 0; trust recompute 0; prose/wiki/page_versions publish 0; product code patch 0; git/deploy/restart 0; cloud/GCP/API mutation 0.
- Explicitly NOT authorized: DB writes, SQL apply/rollback, trust recompute, prose/wiki publish, product code patches, git/deploy/restart, and any GCP/Gemini/Antigravity usage. goru-agy remains offline.
- OpenClaw LaunchAgents: disabled/booted-out only; plist files intact, not deleted. Final process scan clean (no OpenClaw/Gemini/Google-credit suspect processes).
- Phrase hygiene: the cockpit must never render any approval-phrase text — not the stale lana-fable phrase, not the local P2/P5 packet phrases. Refer to them only by description.

## 6) Authorization to Tori

Tori/Hermes is authorized to apply **exactly one action**: render this direction as the static cockpit update via the canonical renderer, then run the standard public verification pass and report the verified result back. No lane input, no buffer clearing, no relaunches, no file changes beyond the cockpit artifact itself, and none of the excluded actions in §5. Card execution — including recommended Card 1 — waits for Duho's explicit choice.

## 7) Marker

HWAO_COCKPIT_DECISION_GATE_DIRECTION_20260706T0628Z
