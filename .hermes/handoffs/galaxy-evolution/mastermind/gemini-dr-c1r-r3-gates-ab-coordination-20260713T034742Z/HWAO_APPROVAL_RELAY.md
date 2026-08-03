# Hwao approval relay — Gates A and B in parallel

Timestamp: 20260713T034742Z
User decision: **“Gates A and B in parallel.”**

This is fresh approval for the next two previously separated gates only.

## Separate packets

- Coordination only: `gemini-dr-c1r-r3-gates-ab-coordination-20260713T034742Z`
- Gate A: `gemini-dr-c1r-validator-r3-implementation-20260713T034742Z`
- Gate B: `gemini-dr-c1r-manual-source-verification-20260713T034742Z`

Keep implementation artifacts and science/source-verification artifacts separate. Cross-reference by hashes; do not merge the packet contents.

## Gate A — approved scope

Implement the approved r3 D1–D5 contract decisions in a new packet using strict RED→GREEN TDD against copied, packet-local capture/validator code and fixtures. Preserve the sealed C1r run and the completed chip-validator repair packet byte-for-byte. Run offline re-adjudication of the sealed captured artifact under r3 rules and publish deterministic receipts.

Required behaviors include:

- D1 typed comparison scope and narrow calibration-target exemption;
- D2 universal numeric-fraction qualifier rule with `MODEL_PARAMETER` fill;
- D3 dedicated Section-2 Citation cell as authoritative, while empty/missing citation remains hard FAIL;
- D4 index-based bidirectional/unique ledger integrity, non-empty short names, normalization, and near-duplicate manual flagging;
- D5 one GAP per paragraph;
- D6 design matrix converted into actual RED→GREEN tests.

No live Gemini/Deep Research call.

## Gate B — approved scope

Verify all 73 routed manual entries against primary sources. Read-only network retrieval is approved only where local artifacts are insufficient. Prefer local-first, then stable primary-source routes (arXiv, DOI/publisher, ADS metadata/full-text links). Persist source custody, exact evidence spans, scope notes, and per-entry verdicts. Do not convert the findings into prose, wiki claims, DB/trust changes, publication, or a live run.

The 73 routes are fixed inputs:

- 47 source fidelity;
- 18 uncertainty/scope;
- 8 scientific comparability.

Hwao must define the verdict vocabulary and fail-closed treatment before review begins. Abstract-only evidence must be labeled as such; no overbroad scientific conclusion from metadata or abstracts.

## Hard boundaries for both gates

- No live Gemini/Deep Research canary, browser automation, account/login action, billing, DB/SQL/apply, prose/wiki publication, trust mutation, dashboard/cockpit update, deploy/restart, cron, git commit/push/merge, or secret exposure.
- No changes to the sealed C1r packet, completed repair packet, or completed r3/triage packet.
- Packet-local writes only.
- Network is read-only and Gate-B-only; no authenticated web action beyond read-only ADS metadata if already configured.
- Never print credentials or tokens; verify credential presence only as a boolean.
- Gate C remains unapproved and unarmed.

## Hwao deliverable now

Write `HWAO_PARALLEL_PLAN.md` in this coordination packet with:

1. separate Gate A and Gate B phases, lane assignments, allowed write roots, and stop conditions;
2. exact Gate B verdict vocabulary and evidence sufficiency hierarchy;
3. read-only network policy and rate-limit/custody rules;
4. Gate A strict vertical RED→GREEN sequence and offline re-adjudication criteria;
5. independent countersign requirements for both packets;
6. completion criteria and explicit conditions under which Gate C could later be recommended, but not started.

Do not start A or B until the plan is written and Tori relays assignments.

HWAO_GATES_AB_APPROVAL_RELAY_20260713T034742Z
