# POST-CAPTURE CLEANUP — STANDING RULE (default gate)
Handoff: `gemini-agent-chat-hygiene-20260712T043151Z` · Author: Hwao (record only) · 2026-07-12
Authority: standing Duho rule 2026-07-12. Records/ACKs the rule and encodes its safety preconditions.
**No browser action, no archive, no deletion performed by Hwao.**

## Rule (verbatim)
> after each agent-created Gemini chat result is saved and artifact custody/hashes are verified,
> remove that exact chat from Recent. Prefer Archive/Hide if Gemini adds it; otherwise permanently
> delete the exact conversation ID immediately and verify absence. Never act on title-only matches or
> Duho-owned chats. This is now the default post-capture cleanup gate.

## Gate sequence (MANDATORY order — the preconditions exist to prevent irreversible loss)
Per agent-created conversation, cleanup runs ONLY after, in order:
1. **Result saved** — `body.md` (or equivalent) captured.
2. **Custody verified (HARD precondition)** — `CAPTURE_RECEIPT` written AND its `wc -c` + sha256
   independently re-verified (Tori) AND the marker/outcome recorded (CAPTURED or VOID). **Never
   remove a chat whose result is not saved and hash-verified.** (A VOID/aborted run qualifies only
   after its partial capture is hashed — nothing more is salvageable — never before.)
3. **Exact-ID provenance** — the conversation's EXACT ID/URL, recorded at launch as *that run's own*
   conversation, is confirmed agent-owned against the provenance allowlist. **Title-only / substring
   / "looks like ours" matches are forbidden. Duho-owned chats are never touched.**

Only then:
4. **Prefer Archive/Hide** (non-destructive) if Gemini offers it → archive that exact conversation.
5. **Else permanently delete** that exact conversation ID immediately (Duho's durable authorization).
6. **Verify absence** — confirm the exact ID no longer appears in Recent/history; capture the
   verification (scoped, hashed) into the run's meta/receipt so removal is auditable.

## Safety locks (binding)
- **Exact conversation ID/URL only** — never a title, substring, pattern, or bulk sweep of
  unconfirmed chats.
- **Never a Duho-owned chat.** Provenance uncertain for any chat ⇒ do NOT remove; treat as
  Duho-owned; escalate.
- **Deletion is irreversible** and permitted ONLY after step-2 custody verification. Custody not
  verified ⇒ STOP; never delete unsaved/unverified content.
- **Live browser action ⇒ gated regime:** executed by Tori with exact-target custody and all standing
  hard stops. If verification/CAPTCHA/unusual-traffic/login/billing/target-uncertainty appears,
  **hard stop before acting** — never bypass, verification cleared by Duho only. The cleanup is a
  targeted archive/delete on a known ID; it is not a Start and creates no new run.
- Goru stays LOCAL-ONLY (never performs this browser action); incident artifacts stay quarantined.

## Scope of application
- **Going forward:** the terminal step of every agent capture flow, including the canary **C1** run
  (immediately after its `CAPTURE_RECEIPT` is verified) and all future runs.
- **Backlog:** existing agent-owned chats — **Set 1** (20 provenance IDs, `AGENT_OWNED_IDS.txt`,
  results already saved+hashed) and **Set 2** (~94 weekend-macro chats; IDs derived from macro logs
  and confirmed **per chat**; outputs saved+hashed audit-only) — are eligible for the same
  archive-or-delete cleanup, exact-ID only, same preconditions.

## Not done by Hwao
Record + ACK only. No chat archived, hidden, deleted, or removed; no browser/DB/product/git/deploy/
cron action. Tori executes under the gated regime; provenance-uncertain or wall conditions ⇒ stop.
