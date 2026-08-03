# HWAO_PLAN — offline contract-r3 draft + 73-entry manual-queue triage

Packet: `gemini-dr-c1r-contract-r3-manual-triage-20260713T024458Z` · Approval: Duho, 2026-07-13T02:44:58Z, per `HWAO_APPROVAL_BRIEF.md`. Hwao coordinates only. All outputs in this packet; the repair packet and sealed C1r packet are immutable inputs. All hard boundaries of the brief apply verbatim (no live model run, browser, network/source retrieval, DB/wiki/product write, dashboard/cockpit write, deploy/restart, git, cron, account/quota/credential action). This step ends at a reviewed r3 draft + complete triage ledger + receipts + Hwao recommendation; validator implementation and any live canary each need a separate explicit user gate.

## 0. Pinned triage lanes (Hwao definitions — binding; refinements only via logged Hwao amendment)

- `VERIFY_SOURCE_FIDELITY` — disposition depends on whether a cited source actually exists/resolves/supports the claim. Routed to the **later, separately gated** local-verification pass; no retrieval in this packet.
- `VERIFY_SCIENTIFIC_COMPARABILITY` — semantic correctness of comparability labels (`MATCHED_SELECTIONS`/`NON_COMMENSURABLE_UNMATCHED_SELECTIONS`), overlap-column claims, and cross-estimand commensurability judgments.
- `VERIFY_UNCERTAINTY_OR_SCOPE` — faithfulness of `UNCERTAINTY_NOT_QUOTED_BY_SOURCE` usage, quoted values, redshift/selection scope, and four-qualifier semantic content.
- `CONTRACT_R3_CHANGE` — the entry exists only because of a contract-design pressure being resolved in r3 (e.g., cited-claim reviews that D3's channel decision re-types); must name the D-item that absorbs it.
- `IGNORE_FOR_THIS_CONTRACT_TEST` — no further action within this contract test (e.g., duplicate flags on the same defect, formatting-only reviews with no scientific content). **Never means scientifically accepted**; each entry states the residual risk in one clause.

Rules: exactly one lane per entry; ties break toward a `VERIFY_*` lane (fail-closed); every entry preserves clause, code, and `source_refs` verbatim from `validator_result_v2.json` plus a ≤1-line reason; arithmetic must reconcile to 73 both by lane and by clause:code.

## 1. Phases and exact deliverables

**P0 — ACK + custody pin (Kun, Tori; gate for everything).**
Lane ACKs per role table. Kun writes `receipts/KUN_INPUT_CUSTODY_RECEIPT.md`: sha256 of the inputs of record per the **patched** `HWAO_APPROVAL_BRIEF.md`, re-checked at packet close. Path correction (binding, per Duho 2026-07-13): the current contract of record is the sealed packet's `../gemini-dr-revised-canary-20260712T045317Z/prompt/C1r.md` (expected sha256 `fffac44fbf6e9abe3afb1f8f34f3a9e3e7688991f319c4927459fb29ac00e1ef`, byte-identical to the sealed `runs/c1r/prompt_submitted.md`) — NOT a repair-packet copy. All D1–D6 "current rule" quotations in `design/CONTRACT_R3_DRAFT.md` must cite that sealed file and its line numbers. Both source packets (sealed canary + repair) remain byte-immutable; any hash mismatch ⇒ stop condition 1.

**P1a — r3 decision drafts (Lana, high reasoning).**
`design/CONTRACT_R3_DRAFT.md`: full proposed r3 contract text plus one change-record per decision **D1–D6**, each with the seven mandatory fields (current rule → observed pressure → proposed r3 wording → rationale → positive example → negative example → validator implication):
- **D1** comparison definition + Section-1 scope (calibration-target register vs agreement/tension claims incl. emergent cells; typed `CALIBRATION_TARGET_DESCRIPTION` option on the table);
- **D2** four-qualifier numeric rule scope (every quoted fraction vs a precisely defined population/statistical class — the question T14 Rule B deferred here; SIMBA ∼10% is the canonical example pair);
- **D3** authoritative Section-2 citation channel (in-Result citation, dedicated Citation cell, or a defined relation — must end the schema-vs-C4 redundancy);
- **D4** ledger integrity (row uniqueness, non-empty short names, index↔source integrity, duplicate and near-duplicate handling incl. URL-variant normalization, the 14↔29 case);
- **D5** one GAP item per paragraph/logical unit;
- **D6** validator/fixture consequences as a **design matrix only** (rule → check → fixture need → RED expectation) — no code.
Constraint: no silent weakening of fail-closed behavior; any proposal that relaxes a gate must carry an explicit `FAIL_CLOSED_IMPACT` flag for Hwao (and, if accepted, Duho visibility in the final recommendation).

**P1b — mechanical queue extraction (Goru; parallel with P1a).**
`triage/GORU_MANUAL_QUEUE_TABLE.json` + `.md`: all 73 MANUAL entries extracted verbatim (index, clause, code, status, source_refs, evidence snippet) with a clause:code count table. No classification. Deterministic, packet-local tooling only; standing Antigravity cap ≤40% of the 5h window.

**P2 — classification (Lana, using P1b).**
`triage/TRIAGE_LEDGER.md` + `triage/TRIAGE_LEDGER.json`: one pinned lane per entry with reason and preserved refs; per-lane and per-clause:code arithmetic tables reconciling to 73; a `CONTRACT_R3_CHANGE` cross-map naming the absorbing D-item for each such entry.

**P3 — independent verification.**
- Kun: `receipts/KUN_TRIAGE_ARITHMETIC_RECEIPT.md` — 73 accounted exactly once (no dupes/omissions), lane sums correct, ledger JSON↔MD consistent, input hashes unchanged.
- Tori: `receipts/TORI_SPOT_VERIFICATION_RECEIPT.md` — independent re-check of ≥15 sampled entries (≥2 from every lane) against `validator_result_v2.json` and the sealed body refs; any disagreement is logged, not silently fixed.
- Hwao: `HWAO_R3_REVIEW.md` — countersign of the r3 draft (D1–D6), explicitly listing any `FAIL_CLOSED_IMPACT` items, plus adjudication of any Lana↔Tori classification disagreements (T14 pattern: rulings logged, no silent edits).

**P4 — close.**
Hwao writes `HWAO_FINAL_RECOMMENDATION.md` (what r3 changes, what the triage implies, exact next gates for Duho: validator-implementation gate and, separately, live-canary gate). Then, last, marker `markers/C1R_CONTRACT_R3_TRIAGE_DONE_20260713T024458Z`.

## 2. Lane assignments (quintet; no solo lanes; Tori relays after reading this plan)

| Lane | Work | Writes only under |
|---|---|---|
| Hwao | coordination, lane-definition pins (§0), r3 countersign, disagreement adjudication, final recommendation | packet root, `markers/` |
| Lana | D1–D6 change records + full r3 text (P1a); 73-entry classification (P2) | `design/`, `triage/TRIAGE_LEDGER.*` |
| Goru | mechanical 73-entry extraction + count tables (P1b) | `triage/GORU_*`, `_tmp_*` in-packet |
| Kun | custody + arithmetic receipts (P0, P3) | `receipts/KUN_*` |
| Tori | relay, spot verification (P3), packet hygiene | `receipts/TORI_*` |

## 3. Review / countersign requirements

1. r3 draft is not final until `HWAO_R3_REVIEW.md` countersigns all six D-items; any `FAIL_CLOSED_IMPACT` item is surfaced verbatim in the final recommendation for Duho.
2. Triage ledger is not final until Kun's arithmetic receipt AND Tori's spot-verification receipt both pass and Hwao has resolved any logged disagreement.
3. Lane-definition changes or new lanes: only by logged Hwao amendment to §0 — classification may not invent categories.
4. Completion marker is written only after every deliverable and receipt above exists.

## 4. Stop conditions (fail-closed; STOP = partial receipt + escalate to Hwao/Duho)

1. Any input-of-record hash mismatch vs the repair packet's published values, at P0 or close.
2. Extraction finds ≠73 MANUAL entries.
3. Any entry unclassifiable under §0 lanes (no silent new lane).
4. Any step would require network research, source retrieval, browser, or provider API — explicitly out of scope this packet.
5. An r3 proposal cannot avoid weakening fail-closed behavior and Lana/Hwao cannot agree on a flagged alternative.
6. Any write outside this packet; any git/dashboard/live action.
7. Goru exceeding the standing quota cap.
8. Unresolved Lana↔Tori classification disagreement after Hwao adjudication attempt.

HWAO_CONTRACT_R3_TRIAGE_PLAN_DONE_20260713T024458Z
