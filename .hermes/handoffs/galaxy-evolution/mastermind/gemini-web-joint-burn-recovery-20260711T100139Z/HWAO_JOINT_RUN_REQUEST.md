# HWAO BRIEF — Gemini Web joint burn recovery

Task ID: `gemini-web-joint-burn-recovery-20260711T100139Z`
Requested by: Duho
Coordinator: Hwao
Operator/receipt verifier: Tori
Mechanical helper: Goru

## User direction

Duho wants Tori to help Goru run Gemini Web Deep Research burn work together.

## Current hard facts

1. The prior Tori extension packet closed on account-verification hard stop:
   - `.hermes/handoffs/galaxy-evolution/mastermind/gemini-web-rampage-extension-20260711T064115Z/RAMPAGE_EXT_HARD_STOP_VERIFICATION_20260711T093749Z`
   - evidence: `evidence/hard_stop_verification_20260711T093749Z.json`
2. Goru's independent `ruthless_weekend_burn.py` was terminated by explicit user approval.
3. That macro opened 94 prompt tabs and wrote 93 outputs; all 93 outputs had the same SHA-256 and are invalid/audit-only.
4. The macro did not explicitly select Pro + Deep Research, did not click Start research, did not target the newly created tab during capture, and lacked quota/marker/verification gates.
5. Google verification has not been manually cleared in this session. No browser launch may occur yet.

## Required fresh packet — prepare only, do not launch

Create a new Hwao-owned joint-run packet under this task directory or a clearly linked sibling directory. It must supersede—not resume—the closed extension packet.

### Roles

- Hwao: coordinator and packet author.
- Tori: sole Gemini Web browser writer/launcher, exact-tab custodian, capture/receipt verifier, hard-stop executor.
- Goru: local-only mechanical helper: topic dedupe, prompt schema validation, expected-marker map, local receipt/count/hash checks. Goru must not control Chrome, System Events, Playwright, cookies, profiles, login, CAPTCHA/verification, or Gemini Web.

### Mandatory gates

- Packet remains NOT_ARMED until Duho explicitly confirms the Google unusual-traffic verification is manually cleared.
- Fresh trusted DOM/account/model/mode/quota evidence after that confirmation.
- Exact Pro + Deep Research plan flow: prompt once, plan snapshot, Start research once, verify active/completed server state.
- Exact new conversation URL/tab identity per run; never scan/capture the first arbitrary Gemini tab.
- No global paste/Enter, no `Chrome activate`, no screen hijack.
- Conservative concurrency: sequential by default; at most two only if the packet explicitly proves safe slot behavior. Starts staggered at least 90 seconds.
- One launch per prompt, no retry of a VOID, no follow-up steering except one packet-authorized neutral truncation continuation.
- Marker exactly once and final nonblank line; otherwise VOID.
- Fresh quota evidence before and after every run or bounded pair. Stop at the packet threshold even if meter appears non-responsive.
- Immediate packet-wide hard stop on unusual traffic, verification/CAPTCHA, login/account wall, model/mode uncertainty, capture-target uncertainty, TCC denial, or quota-source uncertainty.
- No cookies, `__Secure-1PSID`, undocumented APIs, cloned profiles, headless/stealth browser, Playwright, billing/API enablement, DB/wiki/publish/deploy/restart/git writes.

### Topic and custody requirements

- Do not blindly reuse the 94 weekend topics. Dedupe them against the 15 valid reports already captured in the base/extension rampage packets.
- Treat all 93 Goru macro outputs as invalid/audit-only; never ingest or cite them.
- Select a small first canary (one prompt) with a unique completion marker and explicit scientific non-overlap.
- Require prompt hash, plan hash, conversation URL, body hash/bytes, marker count/final-line check, exclusive CAPTURED xor VOID marker, and append-only ledger.

## Deliverables

1. `DIRECTION.md`
2. `MANIFEST.json`
3. one canary prompt only
4. append-only `WAVE_LEDGER.md`
5. `HWAO_JOINT_RUN_PACKET_READY_20260711T100139Z`

Packet-generation only. Do not browse, launch, dispatch Gemini Web, alter accounts, or ask for secrets.

Done response must include the standalone marker:
`HWAO_JOINT_RUN_PACKET_READY_20260711T100139Z`
