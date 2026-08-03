# DIRECTION — Deep Research next phase: read-only DOM validation (A) + conditional single C1 canary (B)
Handoff ID: `gemini-dr-next-phase-canary-20260712T033422Z` · Author: Hwao (coordinator only)
Commissioned: fresh Duho direction 2026-07-12 ("proceed to the next Deep Research phase; supervision minimal")

## 0. State & standing locks (binding)
- Supersedes the hold on `../gemini-web-joint-burn-recovery-20260711T100139Z` for **C1 only**; that
  packet's C1 prompt, marker, and C1-only discipline are reused verbatim (custody in §5).
- **Goru remains LOCAL-ONLY** — no browser/System Events/AppleScript/Chrome/cookies/profiles/login/
  CAPTCHA/Gemini Web/network-to-Google. Goru does nothing live in this packet.
- **Incident quarantine stands:** `tools/gemini_deep_research_driver.py`, `tools/R15_prompt.txt`
  (untracked) — never imported, executed, or used as a base.
- Local capture core is validated (`../goru-deep-research-capture-dev-20260712T030531Z`,
  `LOCAL_CORE_PASS`, review `cc8b2a4b…`). Its live DOM adapter was a **separate gate** — that gate
  is Phase A here.

## 1. Authority & supervisory budget (Duho minimal)
- **Duho acts ONLY for, and nothing else:** (i) login / verification / CAPTCHA **if the surface
  demands it** (human-only — no agent ever touches a verification surface, and clearing is never a
  bypass); (ii) **the single Start-research click** (this packet sets policy: the one "go" is a human
  click). Duho does not compose, quota-check, adjudicate, or capture.
- **Tori handles everything else:** exact-target custody, fresh consumer quota-burn preflight,
  compose/select/submit up to the plan, read-only monitor + capture, immutable receipt, finally-style
  post-run quota refresh, and all hard stops.
- **No verification bypass. No extra Start-research (exactly one, ever). No DB/product/git/deploy/
  cron writes.**

## 2. Roles (quintet; ACK before Phase A)
| Agent | Allowed | Banned |
|---|---|---|
| Hwao | coordinator/packet author; records gate outcomes | execution, browsing, dispatch |
| Tori | sole browser operator: Phase-A read-only DOM validation; Phase-B compose/select/submit-to-plan, read-only monitor/capture, quota preflight+refresh, receipts; hard-stop executor | issuing any Start-research; solving verification/CAPTCHA; second actions; anything in §7 |
| Duho | human: verification/CAPTCHA clear (if demanded) + the one Start-research click | (delegates all else to Tori) |
| Goru | LOCAL-ONLY: may author adapter/selector code under the dev lane behind an un-invoked boundary for Tori to run read-only; assists analysis | any browser/live/System Events/network action |
`TORI_ACK` + `GORU_ACK` (quoting role locks) required in `WAVE_LEDGER.md` before Phase A.

## 3. Phase A — read-only real-DOM adapter evidence / selector validation (NO actions)
**Purpose:** prove, against the REAL Gemini DOM, that the adapter's selectors correctly identify
every state and control the canary depends on — **read-only, zero actions** (no click, submit,
toggle, or start).
1. **Read-channel gate (first):** an authorized, trusted, tab-scoped **read-only DOM-text** mechanism
   must exist (the adapter's read path). If none exists / desktop capture is denied (0x0) / only
   screenshot-TCC or cookie/undocumented-API paths are available ⇒ write
   `DR_PHASEA_BLOCKED_NO_READ_CHANNEL_<UTC>` + reason and **STOP** (no bypass; this is the same wall
   that held C1 before — fail closed, don't work around it).
2. Tori opens `gemini.google.com/app` in the authenticated consumer profile. If a verification/login
   wall blocks load: Duho may clear it (human-only, logged); if unclearable ⇒ hard stop.
3. Read-only, capture DOM-scoped evidence (URL + UTC + scoped text + extractor id, hashed) proving
   each **critical selector** resolves, with a stability note: composer input; Deep-Research toggle +
   its active state; plan container; Start-research control; running/stop indicator; complete state;
   answer-body container; completion-marker/links-ledger region. **Plus wall-state selectors:**
   verification/CAPTCHA, billing/upsell, login. Evidence → `phaseA/`.
4. Produce `phaseA/SELECTOR_VALIDATION.md`: each selector → FOUND/NOT_FOUND + note; explicit
   attestation that **no action was taken**.
5. **Phase-A verdict:** all critical + all wall selectors FOUND and no action taken ⇒
   `DR_PHASEA_SELECTORS_VALIDATED_<UTC>`. Any critical/wall selector missing, any action taken, or
   any read-channel doubt ⇒ `DR_PHASEA_SELECTORS_FAILED_<UTC>` + reason and **STOP (no Phase B).**

## 4. Phase B — conditional single C1 canary (only after Phase A validated)
**Arming gate (ALL must hold; else `DR_C1_NOT_ARMED_<REASON>_<UTC>` and stop):**
- `DR_PHASEA_SELECTORS_VALIDATED_*` present.
- Verification confirmed clear (Duho confirmation OR Phase-A clean load with no wall in evidence).
- **Fresh consumer quota-burn preflight** captured to `evidence/quota_preflight_<UTC>` (URL+UTC+
  scoped text+extractor, hashed); PROCEED only if a real reading is < 80% used; if the meter is
  non-responsive, log it and proceed under that standing clause, but every §6 stop still applies.
- C1 prompt sha256 == `adeaa369…` (pinned §5); local tool sha == pinned; `TORI_ACK`+`GORU_ACK` present.
- ≥ 60 min to nominal weekly reset. No §6 trigger present.
- Then write `DR_C1_ARMED_<UTC>` (+ ledger row citing each evidence sha256). Exactly one of
  ARMED / NOT_ARMED exists before any launch.

**Run flow (single supervised conversation; exactly one Start):**
1. Tori: NEW conversation; record its **exact URL/tab identity immediately**; every read/write targets
   that exact conversation (never the first/focused tab). Copy prompt → `runs/c1/prompt_submitted.md`,
   sha must equal pinned C1.
2. Tori: positively select **Pro + Deep Research** (Phase-A-validated selector); capture
   `runs/c1/model_mode.json`. Uncertain ⇒ hard stop.
3. Tori: submit C1 **once** → plan appears; capture `runs/c1/plan_snapshot.md`.
4. **The one Start-research click — Duho (human).** Tori never issues a start. No second start ever.
5. Tori: positively verify active-research server state from that conversation's DOM
   (running/stop indicator). "Acknowledged, no stable control" (the R14 signature) ⇒ **do NOT
   re-click**; hard stop.
6. Tori: read-only monitor the exact conversation to completion; then capture the answer body
   exactly as produced → `runs/c1/body.md` (answer only). A non-steering reload of the SAME
   conversation URL is allowed solely to resolve stale DOM before capture (logged). At most ONE
   packet-authorized neutral "continue" **only** on visible mid-generation truncation (this is not a
   Start; logged); otherwise no follow-ups.
7. Marker check: `grep -c '<C1 marker>' body.md` == 1 **AND** `awk 'NF{last=$0} END{print last}'` ==
   the marker ⇒ `runs/c1/RUN_CAPTURED_C1`; else `runs/c1/RUN_VOID_C1` + `VOID_REASON.md`. **No retry.**
8. Tori: `runs/c1/meta.md` (model label, conversation URL, UTC start/end, operator=Tori, who clicked
   Start, arming marker, quota lines, anomalies, reload/continue log) + `runs/c1/CAPTURE_RECEIPT.md`
   (`wc -c` + sha256 for every run file; immutable afterward). No receipt on un-hashed text.
9. **Finally-style quota refresh:** regardless of CAPTURED / VOID / hard-stop, Tori captures
   `evidence/quota_postrun_<UTC>` (hashed). Then `DR_C1_DONE_<UTC>` (or the §6 hard-stop marker).

**Run acceptance (for CAPTURED):** exact-target custody held; Pro+Deep-Research positively confirmed;
C1 submitted once; exactly one human Start; active state verified; marker exactly once + final
non-blank line; immutable receipt written; pre- and post-run quota evidence hashed.

## 5. Custody pins
- C1 prompt: `../gemini-web-joint-burn-recovery-20260711T100139Z/prompts/C1.md` sha256
  `adeaa369f9eb82b2090e8c9232f3752ef45ce997fef858f0873c230c1626d265`; marker
  `GEMINI_WEB_JOINT_C1_OUTPUT_DONE_20260711T100139Z`.
- Validated local capture tool: `../goru-deep-research-capture-dev-20260712T030531Z/dev/wait_and_extract.py`
  sha256 `c42df80e39228f32c48d97efdc78df09ad1db98a8fa8bc13fec64cf1a196c49b`; review `cc8b2a4b…`
  (`LOCAL_CORE_PASS`). Any live DOM-adapter glue is authored behind the tool's un-invoked boundary and
  exercised **read-only** in Phase A; Tori code-reviews it before use.

## 6. Hard stops (any ⇒ immediate stop, `DR_HARD_STOP_<REASON>_<UTC>` + reason; no bypass, no retry)
Unusual-traffic / verification / CAPTCHA reappears · login/account wall · billing/upsell · model/mode
uncertainty (can't confirm Pro+Deep Research) · capture-target uncertainty (can't confirm the run's
own conversation) · quota-source uncertainty or real reading ≥ 80% · read-channel loss · TCC denial
(never bypass) · any second-Start pressure · operator doubt · weekly reset. Verification is cleared
ONLY by Duho, manually, never by any agent and never via cookie/profile/undocumented-API/stealth.

## 7. Quarantine & no-write locks
Outputs raw/advisory under this root; every external ID/link `QUARANTINED_PENDING_LOCAL_CHECK`; no
adjudication/integration during the run. **No writes to** DB, product/frontend, wiki, candidates,
SPRINT_STATUS, runner/runtime, **git, deploy, cron**, cloud, billing, account, credentials,
extensions. No cookies/`__Secure-1PSID`/undocumented APIs/cloned profiles/headless-stealth/Playwright.
All writes under this lane (temp `_tmp_*`). No secrets anywhere.

## 8. Exact markers (zero-byte unless noted, this lane root unless noted)
| Marker | Written by | Meaning |
|---|---|---|
| `HWAO_DR_NEXT_PHASE_PACKET_READY_20260712T033422Z` | Hwao | packet authored, ready (written now) |
| `DR_NEXT_PHASE_NOT_ARMED_20260712T033422Z` | Hwao | initial state: nothing armed; Phase A not run (written now) |
| `TORI_ACK` / `GORU_ACK` (ledger rows) | Tori / Goru | role-lock ACKs before Phase A |
| `DR_PHASEA_BLOCKED_NO_READ_CHANNEL_<UTC>` (+reason) | Tori | no trusted read channel ⇒ stop |
| `DR_PHASEA_SELECTORS_VALIDATED_<UTC>` / `DR_PHASEA_SELECTORS_FAILED_<UTC>` (+reason) | Tori | Phase A verdict |
| `DR_C1_ARMED_<UTC>` xor `DR_C1_NOT_ARMED_<REASON>_<UTC>` | Tori | Phase B arming decision |
| `runs/c1/RUN_CAPTURED_C1` xor `runs/c1/RUN_VOID_C1` (+`VOID_REASON.md`) | Tori | run outcome |
| `DR_C1_DONE_<UTC>` | Tori | normal terminal (after finally quota refresh) |
| `DR_HARD_STOP_<REASON>_<UTC>` (+`HARD_STOP_REASON.md`) | Tori | fail-closed terminal |

## 9. Acceptance gates (consolidated)
- **G-A1 read channel:** trusted tab-scoped read-only DOM mechanism exists (else BLOCKED/stop).
- **G-A2 selectors:** all critical + all wall selectors FOUND with stability notes.
- **G-A3 read-only:** zero actions in Phase A (attested).
- **G-B1:** Phase A validated + verification clear + quota preflight PASS (<80% or non-responsive-logged)
  + C1/tool sha match + ACKs + time-to-reset ⇒ ARMED.
- **G-B2 run:** exact-target custody · Pro+Deep-Research confirmed · one submit · **one human Start** ·
  active state verified · marker once + final line · immutable receipt · pre+post quota hashed.
- Any gate miss ⇒ the matching NOT_ARMED / VOID / HARD_STOP marker; no retry, no bypass, no C2/C3.

## 10. What Hwao did / did not do
Did: authored this packet (DIRECTION + MANIFEST + ledger seed + READY & NOT_ARMED markers +
`phaseA/`,`evidence/`,`runs/c1/`,`tori/` scaffolding), pinned C1/tool by sha256. Did NOT: browse,
open Gemini, read DOM/quota, dispatch, run any phase, touch a verification surface, or write outside
this lane. Phase A begins when Tori+Goru ACK and the read-channel gate passes.
