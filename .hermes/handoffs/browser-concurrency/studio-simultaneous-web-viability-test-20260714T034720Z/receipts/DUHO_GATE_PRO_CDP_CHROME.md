# DUHO_GATE_PRO_CDP_CHROME — authenticated CDP Chrome on the Mac Pro for DR

Authorized by Duho (2026-07-14), relayed by Hwao (captain).

## Purpose
Unblock DR-on-Pro: the Pro's Chrome has no CDP endpoint (remote-debugging=false, 0 listeners),
so Goru/Tori cannot drive Deep Research. This gate authorizes ONE dedicated authenticated Chrome
on the Pro with a CDP endpoint.

## Authorized (DR lane: Tori + Goru)
1. Launch ONE dedicated Chrome ON THE MAC PRO with:
   - a NON-DEFAULT `--user-data-dir` (fresh sandbox profile dir inside the packet on the Pro; do
     NOT copy or reuse the default profile, cookies, or credentials);
   - `--remote-debugging-port=<port>` bound to LOCALHOST (127.0.0.1) on the Pro, reached from the
     Studio ONLY over the existing ssh -L authenticated forward (no 0.0.0.0, no open listener);
   - do NOT touch the Pro's default Chrome profile or any existing window.
2. Bring that Chrome up VISIBLE on the Pro (so Duho can sign in) and navigate to Google sign-in,
   then PAUSE and signal Hwao that it is ready for Duho. If you cannot surface a visible Chrome on
   the Pro's GUI from the controller, STOP and report that — Duho will launch it manually.
3. HUMAN SIGN-IN (Duho only): Duho signs the dedicated Chrome into the Ultra account. Agents never
   type credentials, handle 2FA, or solve any challenge. Any challenge during sign-in is Duho's.
4. After Duho confirms signed-in, Goru/Tori attach to the CDP endpoint (over the ssh -L forward)
   and run the ONE bounded live Deep Research run — pure DOM/CDP, serialized submit via the broker
   account-submission lease, capture receipt, report to Hwao before scaling.

## Rails unchanged
No credential/cookie/secret copying; a REAL page challenge = STOP+freeze; serialized submit; one
bounded run first. This gate covers ONLY the dedicated CDP Chrome + its sign-in + one bounded DR run.

DUHO_GATE_PRO_CDP_CHROME_20260714

## DR history hygiene (Duho, 2026-07-14) — save result, THEN delete own conversation
After each Deep Research run, keep the Gemini history uncluttered:
1. SAVE the DR result to a receipt and VERIFY it is saved (result text/artifact captured, receipt
   sha recorded, ledger entry). Result-save ALWAYS precedes any deletion.
2. Then delete ONLY the Deep Research conversation(s) THIS run created — identified by the exact
   conversation id / title / submit-timestamp captured during the run.
3. LOG the deletion (conversation id/title) to the ledger/receipt.

GUARDRAILS (binding):
- NEVER clear all history; NEVER delete any pre-existing or unrelated conversation.
- NEVER touch account settings, passwords, saved data, or anything outside the run's own chat.
- If you cannot POSITIVELY identify the run's own conversation, DO NOT delete — leave it and
  report to Hwao (fail safe).
- If the result-save is not verified, DO NOT delete.
