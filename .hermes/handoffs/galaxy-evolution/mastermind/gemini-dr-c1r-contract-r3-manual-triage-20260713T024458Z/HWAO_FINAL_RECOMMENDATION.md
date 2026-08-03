# HWAO_FINAL_RECOMMENDATION — contract r3 + manual-queue triage (P4)

Packet: `gemini-dr-c1r-contract-r3-manual-triage-20260713T024458Z` · Hwao coordinator, per `HWAO_P4_BRIEF.md`. Recommendation only. The packet completion marker is deliberately NOT written here; Tori relays it after final packet hygiene.

## 1. Plain-English result

The approved offline step is done and independently verified. We now have a complete, standalone **proposed r3 contract** that fixes every contract-design defect the C1r investigation uncovered — with each change carrying its current rule, observed pressure, exact new wording, rationale, worked examples, and validator implications — plus a fully classified **73-entry manual-review ledger** in which every entry is routed to exactly one verification lane with custody receipts. Nothing was implemented, nothing was verified against real papers, and nothing live was touched: this packet produced reviewable paper, deliberately. The sealed C1r run remains FAIL_CLOSED and every cited source remains quarantined.

## 2. The r3 decisions (D1–D5) and D6 status

- **D1 — comparison scope, typed by cell role:** an agreement/tension *result claim* requires a comparability token wherever it appears (Section-1 emergent/notes cells, Section-3 bullets, GAP lines); calibration-target register is exempt only under the typed `CALIBRATION_TARGET_DESCRIPTION:` prefix, valid solely in the two calibration columns; a result claim can never borrow the prefix to escape.
- **D2 — four-qualifier rule, universal with typed fill:** every quoted numeric fraction/incidence is gated; tuned model parameters are labeled (`TRACER=MODEL_PARAMETER; SELECTION=NOT_APPLICABLE; DENOMINATOR=<coupled quantity>; REDSHIFT=NOT_APPLICABLE`), not exempted — SIMBA's ∼10% stays a genuine failure; fraction *words* without a numeric value are not gated.
- **D3 — Section-2 citation authority:** the dedicated Citation cell becomes the single authoritative citation for each atomic validation row; the Result cell is bound to it and not independently citation-gated; an empty Citation cell remains a hard FAIL. Sections 1 and 4 keep the same-cell rule unchanged. (Sole fail-closed relaxation — §3.)
- **D4 — ledger integrity:** index-based bidirectionality, normalized-key uniqueness, mandatory non-empty short names, `abs|html|pdf` + DOI/ADS normalization, and `NEAR_DUPLICATE` flagging (e.g. the 14↔29 `article`/`article-abstract` pair) for manual reconciliation — a strict tightening encoding every observed sealed failure mode.
- **D5 — GAP granularity:** exactly one `GAP:` item per rendered paragraph, each independently cited or token-carrying; multiple GAP lines in one paragraph is a structure failure — closes the merged-block loophole.
- **D6 — design-only status:** the validator/fixture consequences exist solely as a rule→check→fixture→expected-RED design matrix. **No validator code was written**; D6 is the test contract for a future, separately gated implementation phase.

## 3. Accepted D3 fail-closed impact (verbatim, per `HWAO_R3_REVIEW.md`)

> **FAIL_CLOSED_IMPACT: YES** — this removes the Result-cell same-cell citation requirement for Section 2. **Preserved guard:** every Section-2 row must still carry exactly one authoritative, non-empty, resolvable citation in its dedicated Citation cell, bound to the Result cell as one record; an empty or missing Citation cell is still a hard FAIL; the citation stays `QUARANTINED_PENDING_LOCAL_CHECK` and its actual support is a later manual `VERIFY_SOURCE_FIDELITY` decision. Net effect: no validation claim becomes uncited; the citation is relocated to one authoritative cell, not dropped.

This is the only gate relaxation in r3 (D1/D2/D4/D5 retain or tighten their gates), it was flagged by Lana, countersigned by Hwao with the preserved guard made binding, and it is surfaced here verbatim for Duho's visibility before any implementation gate is requested.

## 4. Triage result (73 entries, exactly once each)

| Lane | Count |
|---|---:|
| `VERIFY_SOURCE_FIDELITY` | 47 |
| `VERIFY_UNCERTAINTY_OR_SCOPE` | 18 |
| `VERIFY_SCIENTIFIC_COMPARABILITY` | 8 |
| `CONTRACT_R3_CHANGE` | 0 |
| `IGNORE_FOR_THIS_CONTRACT_TEST` | 0 |

Kun independently passed arithmetic/custody (composition 18/40/5/1/1/8 = 73, IDs M001–M073, source order preserved, deterministic FAIL codes absent from the ledger); Tori sampled all non-empty lanes and scanned all 73 assignments with zero disagreements; both zero-lane statements are countersigned.

## 5. Why zero `CONTRACT_R3_CHANGE` entries is correct

Every finding an r3 decision absorbs (D1's 6 unlabeled comparisons, D2's SIMBA missing-qualifier, D3's 8 Section-2 Result-cell citations, D4's C7 integrity finding, D5's GAP granularity) is a **deterministic FAIL in the 17-finding residue — outside the 73-entry manual queue** by construction (Plan Amendment A3). The manual queue contains only review-class findings, none of which exists solely because of a contract pressure r3 resolves; forcing any of them into the contract-change lane would have corrupted the classification. The D1–D5 crosswalk therefore lives in `design/CONTRACT_R3_DRAFT.md` §9, referenced by FAIL identity, and the ledger's zero is the arithmetically and definitionally correct outcome.

## 6. What this work did NOT do

No validator was implemented (D6 is design only). No source was retrieved and no scientific, source-fidelity, uncertainty, or comparability conclusion was reached — all 73 routed entries remain unverified and every citation remains `QUARANTINED_PENDING_LOCAL_CHECK`. No live run was armed and no retry/retro-acceptance occurred; C1r remains FAIL_CLOSED. No network, browser, git, DB, dashboard, deploy, cron, account, or secret action took place.

## 7. Recommended next sequence — each step behind its own fresh gate

1. **Gate A — offline validator-r3 implementation + tests:** implement the D6 design matrix as capture/validator changes in a new packet, strict RED→GREEN against the sealed fixtures (RED expectations per D6), then offline re-adjudication of the sealed C1r capture under r3 rules to confirm the predicted re-typing (e.g. the 8 D3 findings) with receipts. Offline only; requires a fresh Duho approval.
2. **Gate B — local source/science verification of the routed 73 entries:** the separately gated verification pass over the triage ledger (47 source-fidelity, 18 uncertainty/scope, 8 comparability), local-first with explicitly scoped retrieval rules, producing per-entry verdicts and a quarantine-release/reject list. Requires its own fresh Duho approval and its own network-scope decision.
3. **Gate C — live one-simulation canary under contract r3:** only after Gates A and B results are reviewed, a separate explicit Duho gate for a single supervised run with fail-closed adjudication under the r3 contract and repaired pipeline. Nothing before this point touches a live surface.

Recommended order is A → B → C; A and B are independent enough to run as separate approvals in either order, but C requires both reviewed.

## 8. Non-blocking future decision

The r3 header retains the title string "Joint C1R answer — `<REQ_ID>`" for continuity with existing adjudication tooling. When the future run packet assigns `<REQ_ID>` (Gate C), confirm whether keeping the "C1R" name is intentional or whether the title should become r3-native; either is acceptable, but the choice should be explicit in that packet's contract pin.

HWAO_R3_TRIAGE_FINAL_RECOMMENDATION_20260713T024458Z
