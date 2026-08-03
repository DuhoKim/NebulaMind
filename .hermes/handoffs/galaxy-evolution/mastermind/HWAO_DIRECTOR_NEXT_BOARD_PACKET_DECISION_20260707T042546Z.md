# Hwao-director decision — next Galaxy Evolution board packet

Decision marker: HWAO_DIRECTOR_NEXT_BOARD_PACKET_DECISION_20260707T042546Z
Brief followed: HWAO_DIRECTOR_NEXT_BOARD_PACKET_DECISION_BRIEF_20260707T042546Z
User direction: option 1 — "Hwao-director decides the next board packet."
Author: Hwao-director (pane %107)
Written: 2026-07-07T04:30Z (13:30 KST)
Mode: DECISION ARTIFACT ONLY. No panes dispatched, no method packet/draft written, no gate advanced.

---

## 0. Decision in one line

**Next board packet = Method2 corrected same-format conversion packet (Step B v2) that names a non-Lana draft-owner lane, then re-dispatches the existing verify lanes.** It is the single move that clears the board's only active blocker, stays entirely inside the docs/static safe zone, and puts all three methods back in a "done or moving" state. Dispatch waits for explicit user approval.

---

## 1. Recommended next board packet (one concrete choice)

Issue **`HWAO_M2_SAME_FORMAT_CONVERSION_ROLE_SPLIT_V2_<UTC>.md`** — a corrected Step B role-split for Method2 (Source-First Adjudication) that fixes the packet-design defect in `HWAO_M2_SAME_FORMAT_CONVERSION_ROLE_SPLIT_20260707T004129Z.md`.

The only substantive change vs the blocked packet: **add an explicit draft-owner (author) lane, and make it a different lane from the ones that review/rebuild that draft.** Everything else (the claim→evidence map for chips 2942–2947, the six carry-forward obligations F1–F6, the 28060 caution rule, the ≤30 chip bound, the renderer/contract rules, the hard rails) is carried forward unchanged from the 004129Z packet.

Concrete lane split for v2:
- **Draft-owner / author — Kun-m2.** Kun assembles the same-format Markdown draft at the packet's target path by realizing the RATIFIED S2 source-position ledger (`lana/LANA_SFA_SOURCE_ADJUDICATION_20260707.md`, RATIFIED WITH NOTES) through the packet's fixed claim→evidence map as cautious reader-facing prose over the v1709 9-H2 skeleton. Rationale: the conversion is tightly specified and deterministic (the map, chips, and exclusions are already fully pinned in the packet), and Kun's standing competency is exactly "can this be regenerated deterministically from the ledger + local artifacts alone?" — so Kun is the lane best suited to produce a reproducible draft, and having Kun author it removes no independent check as long as the rebuild-parity check is reassigned to a different lane (below). *(Acceptable alternative if Kun's pane is unavailable: Goru-m2 as author, with the rebuild check staying with Kun. Not Lana, not Hwao.)*
- **Overclaim review — Lana-m2** (unchanged role): independent overclaim/verb-discipline review of Kun's draft against F1–F6 and the 28060 caution rule. Lana never authors — this preserves the separation that the blocked packet was missing.
- **Conformance counts + rebuild-parity — Goru-m2:** mechanical field-by-field conformance (title, blockquote, 9-H2 order, claim-chip count+IDs = {2942–2947}, cite-marker count+numeric IDs, forbidden-content scan) **and** an independent re-derivation from the ledger+map to confirm the draft is reproducible by a lane other than its author.
- **Receipts-last — Tori-m2** (unchanged role): receipts ledger; Method2-workspace status only; stop-on-blocker.
- **Method verdict — Hwao-m2:** A5-equivalent verdict after the four lanes land, on the Method1 precedent (independent re-verification of the actual draft, not a re-trust of self-reports).

Binding design rule the v2 packet must encode (this is what was violated): **the draft-owner lane may not also be the lane that overclaim-reviews or rebuild-checks its own draft** (no solo author+review loop, per the quintet role table). One author + three independent verify lanes + Hwao verdict.

---

## 2. Why this packet is next (from current verified state)

Verified state as of this decision:
- **Method1 — PASS**, draft static, not published (`HWAO_PGR_METHOD_VERDICT_20260707T040523Z`: A1–A5 unanimous, 14,221-byte 9-H2 draft, 30 chips, deterministic, contract-clean, `DRAFT_PREPARED_STATIC_NOT_PUBLISHED`). Method1 needs nothing more to be *complete*; its only remaining step is publication, which is a higher-risk, separately-gated action — not a docs/static packet the director should open autonomously.
- **Method2 — ROLE_TABLE_BLOCKER** (`TORI_M2_SAME_FORMAT_CONVERSION_RECEIPT_20260707T035927Z`): all three worker lanes plus Tori are blocked on the same root cause — the Step B packet listed the draft as a deliverable but assigned **only verification roles** (Lana overclaim, Goru conformance, Kun rebuild, Tori receipts) and **no author**. Lana correctly refused to both produce and review the draft (forbidden solo loop). Method2 cannot move at all until the director issues a corrected packet with a real draft-owner. It is the only *stuck* lane on the board.
- **Method3 — PASS_WITH_ISSUES for P1.5** (`HWAO_M3_P15_RE_VERDICT_20260707T041033Z`): no blocker; P2 (docs-only) may open via a separate Hwao P2 lane-split; P3 stays closed. Method3 is *available* for more work but is not blocked.

Decision logic (per the brief's criterion "most coherent board progress while respecting gates"):
- A method sitting in ROLE_TABLE_BLOCKER is the least-coherent state on the board and is exactly the "low visible activity / stalled" symptom the user has been reacting to. **Clearing the only blocker restores all three methods to done-or-moving and is the highest-coherence single move.**
- The fix is low-risk: it is bounded, method-local, docs/static work of the same class already completed in Method1 — no gate escalation, unlike Method1 publication.
- It is squarely a director-level responsibility: the blocker is a packet-design defect only the director/Hwao can correct (workers cannot self-assign a draft-owner without breaking the role table).

Method3 P2 is a strong, even lower-risk candidate, but it is *additive* forward motion on an already-passing method; opening new work elsewhere while Method2 stays blocked is less coherent than clearing the blocker first. It is sequenced as the recommended follow-on in §7.

---

## 3. What this packet authorizes / does not authorize

**Authorizes (all method-local, docs/static, Method2 only):**
- Writing the corrected v2 role-split packet under the Method2 handoff root (`method2/hwao/`).
- Upon later user-approved dispatch: Kun authoring the same-format draft at `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/galaxy-evolution-same-format-draft.md`; Lana/Goru/Kun/Tori lane receipts; Hwao method verdict; Method2-workspace status set to `DRAFT_PREPARED_STATIC_NOT_PUBLISHED`.
- Chips 2942–2947 only, numeric-only cite markers, ≤30 chip bound, renderer/contract rules per `docs/wiki_content_contract_v1.md` + `frontend/CITATION_POLICY.md`.

**Does NOT authorize (unchanged hard rails):**
- No live wiki / `page_versions` publish; the draft stays static (publication is a separate future user gate).
- No cross-method reuse: Method2 must not import Method1's chips (2905–2936) or bind to Method3 artifacts.
- No DB/SQL/migration/trust recompute; no deploy/restart/service mutation; no git; no cloud/API/GCP/billing/account/payment/credits/OAuth/token; no browser automation; no cron; no route/config mutation; no cockpit/global/shared-parent write; no Ultra/Gemini/Antigravity. `ULTRA_NOT_NEEDED` stands.
- No rejected source rows (28070, 28076, 28080, 28082, 28083, 28084, 28110, 28114, 28118, 28127, 28139, 28143) cited; 28133 stays background-only; 28111 excluded; 28060 caution-only, never in a claim chip.

---

## 4. Exact panes / lanes to dispatch later (only if the user approves execution)

Dispatch order once approved (each pane gets one short pointer to the v2 packet naming its exact deliverable; helper panes are currently idle at empty composers, so no restart is needed):

1. **Hwao-m2 `%97`** — write the corrected v2 role-split packet (this is the packet itself; author lane fix).
2. **Kun-m2 `%100`** — draft-owner: author `galaxy-evolution-same-format-draft.md` from the RATIFIED S2 ledger via the packet map.
3. **Lana-m2 (SFA Lana pane, `lana-tori2-sfa %50` — confirm at dispatch)** — independent overclaim review of Kun's draft.
4. **Goru-m2 `%99`** — mechanical conformance counts + independent rebuild-parity re-derivation.
5. **Tori-m2 `%101`** — receipts-last; set Method2-workspace status `DRAFT_PREPARED_STATIC_NOT_PUBLISHED`.
6. **Hwao-m2 `%97`** — method verdict after lanes 2–5 land.

Notes: Kun (author) and Lana/Goru (reviewers) must be distinct panes — that separation is the whole point of the correction. Goru/Kun panes show idle model-placeholder composer text ("Write tests for…"), which is not active work; they are free to receive pointers. Confirm the exact Method2/SFA Lana pane id before dispatch (the SFA second-lane runs in `hwao-tori2-sfa %49` / `lana-tori2-sfa %50`).

---

## 5. Stop gates and safety rails

- **Stop-on-blocker:** any lane hitting a missing input or role conflict writes `ROLE_TABLE_BLOCKER` and stops — do not solo-resolve. (If v2 still somehow leaves an ambiguous author, that surfaces as a blocker rather than a silent solo draft.)
- **Publication gate stays shut** for all three methods: Method1's PASS draft, Method2's forthcoming draft, and any Method3 P2 draft are all static-only; live-wiki/`page_versions` publication is a separate, explicit future user gate.
- **P3 (Method3) stays CLOSED** behind a fresh authorized snapshot + Goru re-check + separate user gate; I2/I3 are binding prerequisites there.
- **Hard rails (all lanes, unchanged):** no live wiki/page_versions, DB/SQL/trust recompute, deploy/restart, git, cloud/API/GCP/billing/account/payment/credits/OAuth/token, browser, cron, route/config, cross-method/shared-parent, or Ultra/Gemini/Antigravity action.
- **This decision pass's own footprint:** read-only reads of the three verified verdict/receipt artifacts + the blocked packet + a read-only pane map; **one write only** — this decision artifact. No pane dispatched, no method packet/draft written, no approval pressed, no gate advanced.

---

## 6. Dispatch timing — WAIT for user approval

**Tori should WAIT. Do not dispatch on this artifact alone.** This is a director decision, not an execution order, and the user is the gate for putting lane work in motion (consistent with the brief's "if the user approves execution" framing and the standing role-table protocol). Recommended next step: Tori relays this recommendation to the user; on an explicit go, Tori dispatches the §4 sequence (starting with Hwao-m2 writing the v2 packet). Until then, all Method2 panes remain parked and the blocker stands as-is.

---

## 7. Recommended sequencing after this packet (director forward view, not authorized here)

1. **Now (this decision):** Method2 corrected conversion packet → on user go, dispatch §4. Clears the blocker.
2. **Next (or in parallel — methods are isolated, both docs/static):** **Method3 P2** — a separate Hwao-issued P2 lane-split for the docs-only same-format Markdown draft (title + blockquote + exactly 9 H2s, **no** claim/cite markers, no binding), honoring the §4 scope guards (GAP-A/B/C/D) and folding the trivial I1 Goru GO-marker addendum. Lowest-risk work on the board; can run alongside Method2 if the user wants maximum board activity. P3 stays closed.
3. **Deferred — separate explicit user gate, NOT a docs/static packet:** **Method1 publication** of the completed PASS draft to the live wiki/cockpit. Higher-risk (touches live wiki/`page_versions`, public surfaces, and likely trust/route recompute). Requires its own user authorization with a stated publish target and rollback plan; the director does not open this autonomously. Surface it to the user as "Method1 is done and ready to publish when you choose to open that gate."

Stopping after this decision artifact.
