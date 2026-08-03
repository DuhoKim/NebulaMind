# DUHO_RESET_RESUME_BATCH9 — clear epoch-collision freeze, resume

Authorized by Duho (2026-07-14), relayed by Hwao (captain).

## Finding
Broker fail-closed froze at e1572 on a ledger epoch collision (e1563) caused by a concurrent
Hwao-attributed journal append racing the live broker during paper_09 submit. NOT an account
challenge/CAPTCHA/throttle. The fork was already repaired (e1573). 8/9 reference packets are safe.

## Authorization (Tori, DR operator + Goru)
1. Execute the broker reset / clear the emergency freeze under this authorization; append the
   ledger resume entry (broker-only); verify VERIFY_OK.
2. Resume and finish paper_09 (last DR packet): submit -> POLL to terminal -> save the reference
   packet (advisory_only) to the packets dir -> delete only that run's own conversation -> log.
3. Write the batch summary receipt (9/9, sources per packet, any anomalies).
4. RELEASE the account-submission rail so Yui's narration batch AND the read-only Gemini usage
   check can proceed.

## Guardrail to prevent recurrence
During active submits, ONLY the broker writes the ledger — no concurrent DIRECT journal/ledger
appends from any side (the race was a direct Hwao-side append; Hwao stays off the live ledger).
Rails otherwise unchanged: real page challenge=STOP+freeze, serialized submit, no secrets, fail
closed on target drift.

DUHO_RESET_RESUME_BATCH9_20260714
