# DUHO_GOLIVE_ARCHITECTURE_B — live concurrent Flow + DR authorization

Packet: studio-simultaneous-web-viability-test-20260714T034720Z (→ live operation phase)
Captain: Hwao/Fable. Decision by Duho: 2026-07-14, via Hwao's A/B verdict + account-plane gate.

## Decision (Duho, explicit)
Architecture B adopted and taken LIVE. Duho was shown the shared-account risk (account-wide
quota; a challenge freezes both sides; same-account concurrent submission UNKNOWN and is the
mechanism that shadow-throttled the earlier Veo runs) and chose **"same account, run now,"**
accepting that risk. **This lifts the account-plane gate ONLY.**

- **Yui = Flow operator, Mac Studio** (CUA-bound Flow driver; established Flow lane).
- **Tori = DR operator, Mac Pro** (pure DOM/CDP; cua-driver absent).
- **Hwao = captain**; broker on the Studio owns all leases.

## Greenlit now
- Live Flow job submission + quota spend on the Studio (Yui).
- Live Deep Research runs on the Pro (Tori).
- Both concurrently on the single Ultra Google account.

## Rails STILL IN FORCE — these protect the account; do NOT bypass
1. **Concurrent RUN, serialized SUBMIT** — the broker account-submission lease still serializes
   the actual submit moments across both hosts. Never submit on both sides in the same instant.
2. **Challenge = STOP, not solve.** Any Google challenge / CAPTCHA / sign-in / 2FA / permission
   prompt on EITHER host → immediate STOP + broker freeze BOTH sides. Do NOT click through or
   solve it. Surface Hwao→Duho; only Duho resumes. (This rail is what keeps "accept the risk"
   from becoming a ban.)
3. **No secrets** — never read/copy/expose credentials, cookies, tokens, or profile contents.
4. **Bounded first pass** — each side runs ONE small job first, capture receipt, verify clean,
   THEN continue. No large batch on the first live concurrent attempt.
5. **Ledger is source of truth** — append receipts; disagreement is STOP-class to Hwao.
6. **Emergency STOP** available to anyone; broker freezes both sides; Duho-only resume.

## First bounded tasks
- **Yui (Flow/Studio):** submit ONE Flow job live, capture result + receipt, report via ledger.
  Coordinate with the working Flow driver (`clips/flow_generator_batch.py` / Garu·WonE helpers).
- **Tori (DR/Pro):** start ONE Deep Research run live on the Pro, capture receipt, report.
- **Consult up** (Hwao / each other) when blocked — Duho's standing instruction.

Report first receipts to Hwao for relay to Duho before scaling up.

DUHO_GOLIVE_ARCHITECTURE_B_20260714

## Lane teams (added 2026-07-14, Duho) — operator + Gemini-savvy agy driver
- **Flow / Studio:** operator **Yui** + hands-on driver **WonE** (agy, ran the Flow generator).
- **DR / Pro:** operator **Tori** + hands-on driver **Goru** (agy).
- Division of labor: the **agy helper drives** the Gemini/Flow surface hands-on and writes
  receipts to the ledger; the **operator verifies** receipts and reports to Hwao. Coordination
  is **ledger-mediated** (no direct peer-to-peer control between hermes operator and agy).
- All rails above apply to the agy drivers equally: serialized submit via the broker
  account-submission lease; challenge/CAPTCHA/sign-in = STOP + surface to Hwao (never solve);
  no secrets; bounded first pass. agy drivers work only in their Hwao-scoped lane.

## Communication channel rule (Duho, 2026-07-14)
**Default: Duho routes directives through Hwao (captain).** Anything that changes scope,
priority, or a gate goes through Hwao, who issues consistent orders to BOTH lanes and keeps
the brief + ledger + memory in sync. This prevents cross-channel drift (e.g., one lane hearing
"routing only" while the live decision is already "run now").

**Direct escape hatches (no Hwao hop):**
1. **Emergency STOP** — anyone, always direct. Broker freezes both sides; only Duho resumes.
2. **Genuine urgency** — captain-relay latency waits for a busy pane to go idle; if Duho needs
   it now, direct into the operator's pane is faster.
3. **Duho's own hands-on Flow/Studio work with Yui** — Duho's lane; staying hands-on is fine.

**The reconciliation rule that makes the hybrid safe:** if Duho gives an operator a DIRECT
directive that changes scope/priority/gate, that operator must (a) log it to the run ledger and
(b) notify Hwao, so Hwao reconciles it across lanes. Operators never silently re-scope a lane on
a direct message. Hwao's orders remain authoritative for cross-lane consistency; a direct Duho
STOP always wins immediately.
