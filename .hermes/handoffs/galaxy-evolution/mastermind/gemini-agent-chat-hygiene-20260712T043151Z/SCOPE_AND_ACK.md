# ACK & SCOPE — agent-owned Gemini chat hygiene (RECORD-ONLY; no browser action)
Handoff: `gemini-agent-chat-hygiene-20260712T043151Z` · Author: Hwao · 2026-07-12
Direction (Duho): workflow-created Gemini chats dominate Duho's recent history; Tori to identify
**only agent-owned** conversation IDs and inspect for a **non-destructive Archive/Hide** action.

## ACK
Hwao acknowledges — **record-only, no browser action taken.** This file records the bounded scope
and the provenance-backed agent-owned ID allowlist for Tori. Nothing here authorizes a live action.

## Bounded scope (binding)
- **Action class: non-destructive Archive/Hide ONLY.** No delete, no rename, no content edit, no
  bulk irreversible action.
- **Targets: agent-owned conversations ONLY.** A conversation is agent-owned only if it is
  provenance-confirmed in our own ledgers/macro logs (allowlist below). Anything not
  provenance-confirmed = treat as **Duho-owned = do not touch**.
- **No archive capability ⇒ permanent delete (SUPERSEDED by the standing rule).** The standing Duho
  rule 2026-07-12 (`POST_CAPTURE_CLEANUP_STANDING_RULE.md`) is the separate explicit choice: if
  Gemini offers no non-destructive archive/hide, **permanently delete the exact agent-owned
  conversation ID and verify absence** — but ONLY after result-saved + custody/hashes-verified +
  exact-ID provenance (never title-only, never Duho-owned). See that file for the mandatory gate order.
- **Duho-owned chats are never archived/hidden/deleted/changed** under any circumstance without a
  separate explicit Duho choice.
- **Identification is local-first** (from our records), not by trawling Duho's history. Any *live*
  inspection or archive execution is a **future gated step** under the standing regime (verification
  hard stop, Duho-only verification clear, no bypass, exact-target custody, one action at a time, all
  hard stops) — **not authorized now**.

## Agent-owned ID allowlist
- **Set 1 — provenance-backed (20 IDs), `AGENT_OWNED_IDS.txt`:** each traceable to a specific run row
  in the rampage base + extension ledgers. These are safe-to-consider agent-owned.
- **Set 2 — weekend-macro chats (~94 tabs / 93 outputs; likely the bulk of the domination):** their
  IDs are **NOT** in `/app/<16hex>` form in `gemini-web-deep-research/weekend_burn.log` (plain grep =
  0 matches), so they must be derived from the macro's own logs/outputs in their stored form and
  **each confirmed agent-owned** (its prompt matches our sidecar prompt) before any action. Macro
  content stays quarantined/audit-only; identification-for-archive is allowed but must be
  provenance-confirmed **per chat** — no guessing, no pattern-archiving of unconfirmed chats.
- **Joint C1 + current canary: no conversations created** (never launched) — nothing to archive there.

## Not authorized here
No browser action, no archive/hide execution, no deletion, no Duho-owned changes, no
DB/product/git/deploy/cron. ACK + record only. Tori proceeds with identification (local-first) and,
for any live inspection or action, returns for the gated step / separate explicit choice.
