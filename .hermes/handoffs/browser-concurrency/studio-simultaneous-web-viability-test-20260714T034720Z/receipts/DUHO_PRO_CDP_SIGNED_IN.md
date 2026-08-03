# DUHO_PRO_CDP_SIGNED_IN — dedicated Pro Chrome signed in; run one bounded DR

Confirmed by Duho (2026-07-14), relayed by Hwao.

## Confirmation
Duho confirms the dedicated Mac Pro Chrome (profile `dr-live-cdp-20260714`, loopback CDP port
9223) is now SIGNED IN to the Ultra Google account. Human-in-the-loop sign-in complete.

## Authorization (Tori + Goru, DR/Pro) — ONE bounded run
1. Attach through the loopback SSH forward (Studio 127.0.0.1:19223 -> Pro 127.0.0.1:9223).
2. Page-scoped preflight: confirm the Deep Research / Gemini page target; challenge check is
   PAGE CONTENT only (Chrome toolbar/profile badge is OUT OF SCOPE and never a STOP by itself).
3. Acquire the exact target lease + the serialized account-submission lease.
4. Run exactly ONE bounded Deep Research run (pure DOM/CDP).
5. SAVE the result to a receipt and VERIFY it saved; THEN delete ONLY that run's own Gemini
   conversation per the history-hygiene guardrails; LOG the deletion. Save always precedes delete.
6. Report to Hwao.

## Rails unchanged
Real page challenge = STOP + freeze; serialized submit via the broker account-submission lease;
no credentials/cookies/secrets; fail closed on target drift; if you cannot positively identify
the run's own conversation, DO NOT delete. This authorizes ONE bounded run only, then report
before any scale.

DUHO_PRO_CDP_SIGNED_IN_20260714
