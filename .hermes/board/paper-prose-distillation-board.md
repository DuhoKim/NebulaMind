# NebulaMind Paper Prose Distillation Board — The Baseline mirror

Updated: 2026-07-21 22:43:53 KST / 2026-07-21T13:43:53Z
Status: ACTIVE — CLAIM LEDGER CONTRACT V1 COMPLETE; STATUS/DEBATE MAP NEXT
Marker: `BOARD_RECONCILIATION_G1_COMPLETE_20260721T134353Z`
Review marker: `THE_BASELINE_PREIMPLEMENTATION_REVIEW_PATCHED_20260703T0824Z`
Contract completion marker: `CLAIM_LEDGER_CONTRACT_V1_AGN_COMPLETE_20260703T0830Z`
Execution phrase: `NO ACTIVE EXECUTION PHRASE`

## Mission

Turn large volumes of published papers into clear, trustworthy prose without losing scope, uncertainty, contradiction, or provenance.

## Canonical primitive

```text
papers -> claim/status ledger -> research-status/debate map -> prose -> derived claims/evidence/trust
```

Rules:
- Sentences are renderings, not truth primitives.
- Every prose sentence must bind to one or more ledger entries.
- Prose modality may never exceed ledger certainty.
- When sentence and ledger disagree, sentence changes.
- Claim rescue / evidence hunting is forbidden.

Canonical plan: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/plans/2026-07-01_205807-paper-prose-distillation-roadmap.md`

## Pre-implementation review consensus

Fable, Lana, and Goru all returned `PASS_WITH_PATCHES`. The Baseline primitive and sequence are accepted; the schema/enum patches are now applied. Implementation remains held until the user approves the next docs-only gate.

Accepted before implementation:
- canonical enum registry
- canonical ledger schema names
- certainty derivation rule
- stance matrix schema
- wording-contract check schema
- prose sentence-binding schema
- countercase quota
- missing-critics test
- ledger-to-production stance mapping requirement

Review run: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/baseline-preimplementation-review-20260703T0810Z`

## Current Baseline progress

| Stage | State | Next |
|---|---|---|
| Corpus protocol | partial | formalize coverage cells and PRISMA flow in Claim Ledger Contract run |
| Source inventory | partial | reuse 26 AGN full-text checked papers |
| Span extraction | partial | normalize spans into ledger schema |
| Claim/status ledger | **complete** | validated and preserved as `CLAIM_LEDGER_CONTRACT_V1_AGN_COMPLETE_20260703T0830Z` |
| Status/debate map | **next** | design proposal pending; G6 remains held |
| Wording contract | specified | make machine-checkable |
| Prose preview | blocked | no prose until ledger passes |
| Exact-diff/product change | locked | separate approval only |

## Quartet lane state

- Hermes: integrated Baseline + cockpit, safety verifier.
- Fable: done — doctrine co-author, tripwires/rejections.
- Lana: done — pipeline/gates/method bindings.
- Goru: done — schema/mechanical gates/done checks.

## Lanes

### L1 — Corpus protocol and inventory

Owner: Goru mechanical lane, Hermes verifies.

Done when:
- corpus protocol exists
- flow counts found -> screened -> eligible -> included exist
- every coverage cell has a candidate or named blocker

### L2 — Claim/status ledger extraction

Owner: Lana semantic lane, Goru validates schema.

Done when:
- ledger JSONL parses
- every entry has assertion, modality, scope, evidence spans, stance, certainty dimensions, links, verification status
- every source ID maps to included paper inventory

### L3 — Status/debate computation

Owner: Lana + Fable review, Hermes integrates.

Done when:
- every status label traces to ledger entries
- debate axes have named positions
- counterevidence retained

### L4 — Wording contract and prose preview

Owner: Hermes drafts only after ledger/status pass; Lana reviews; Goru checks bindings.

Done when:
- every sentence has ledger binding
- zero orphan sentences
- zero modality overflow

### L5 — Evaluation and human adjudication

Owner: Hermes board, Goru metrics, human final judgment.

Done when:
- audit says what passed, failed, and what remains blocked before exact-diff/product mutation

### L6 — Product/UI only as support

Owner: Hermes gatekeeper.

Done when:
- any UI request names the exact Baseline bottleneck it removes
- no product/runtime change happens without separate approval

## Tripwires

`rescue search` · `orphan sentence` · `scope inflation` · `feed-dump corpus` · `false consensus` · `quote-mined zone` · `simulation-as-observation` · `topic-match evidence` · `score chasing` · `trust scalar laundering`

## Next gated step

The prior Contract v1 build request is retired because the validated packet is already complete. The board is a mirror, not the authority; the completion receipt wins when they disagree.

The status/debate-map design proposal is next, but G6 remains held. This reconciliation authorizes no prose, wiki publication, DB or SQL work, migrations, product or exact-diff changes, git actions, runtime changes, deploys, restarts, cockpit changes, or publication.

```text
NO ACTIVE EXECUTION PHRASE
```

## Safety ledger

- DB writes: 0
- SQL mutations: 0
- migrations: 0
- deploy/restart: 0
- product publish: 0
- git commit/push/merge: 0
- prose draft/publish: 0

BOARD_RECONCILIATION_G1_COMPLETE_20260721T134353Z
