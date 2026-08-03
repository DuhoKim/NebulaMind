# ADDENDUM — M2/SFA Omni voice-ref canary resume gate (after preflight local HOLD)

Issued by Hwao 2026-07-16. Amends brief `YUI_FLOW_M2_SFA_OMNI_VOICEREF_CANARY_BRIEF.md` (sha256 `315b3657…da5a2e`). Marker unchanged: `M2_SFA_OMNI_VOICEREF_CANARY_20260716`.
Preflight HOLD receipt acknowledged: `M2_SFA_VOICEREF_CANARY_PREFLIGHT_HOLD.json` (sha256 `72005dc3…86ad14`). Zero submits, zero credits, lease accounting clean.

## Decision: MANUAL PRECONFIG route. No new automated locator probing.

The no-hammer rule already fired after three bounded attempts, on a tab that also threw one client-side app error. A fresh locator would mean more live clicking on the account surface for uncertain gain. A human click-through is deterministic and cheap. `further_ui_attempts_forbidden_without_new_direction` stands — this addendum is NOT direction to retry the popup.

## Duho's manual step (in the exact target: window 1, tab 2 — the owned project)

1. Switch composer from Image (Nano Banana Pro) to **Video → Gemini Omni Flash**.
2. Attach/select the **Voice Reference**: `vo_test_01` (the named series-narrator asset).
3. If the same popup offers them: set **8s / 16:9 / 1x**.
4. Glance at the **displayed credits per submit** number (no need to write it down — Yui must read it programmatically anyway).
5. Leave the tab on the composer; tell Yui (or Hwao) "preconfig done".

## Yui's resume scope (READ-ONLY verification, then the one submit)

- Resume at **pre-submit verification only**. Verification basis: bounded READ-ONLY DOM/AX reads of the visible composer state — model name, voice-reference name, duration, aspect, output count, and the exact displayed credit number. Reading visible state is allowed; clicking through menus is not.
- Every gate item from the original brief still applies unchanged, including: exact-target verify, re-verify after paste, expected credit band 15–30 (READ AND RECORD exact; outside band → STOP), one submit, poll to terminal, post-download verbatim + voice-match checks, zero further submits either way.
- If bounded read-only verification cannot see the config: STOP again (second preflight hold receipt). Fallback is static evidence, not live probing — Duho copies a full-window screenshot into `/Users/duhokim/HermesOps/scripts/` (not Desktop/Downloads; TCC blocks those), and Hwao derives the next step offline.
- Manual preconfig does NOT waive verification. Never submit on the assumption that the human set it correctly.

## Security handling (hydration/session-state transcript exposure)

- Assessment: contained — local tool transcript only; receipt affirms no value retained/reused, no credential file touched, no account action.
- Standing rule (all agents): do NOT re-print, grep, quote, or copy that diagnostic output into any receipt, report, or file. Treat the affected transcript as sensitive. The diagnostic that returned it is retired from the toolkit for this lane.
- Optional hardening (Duho's call, not required): a Google session refresh would rotate the exposed state, but it disrupts live lanes (Goru's DR monitor lease L01021 is active). Defer unless desired; exposure is local-only.
