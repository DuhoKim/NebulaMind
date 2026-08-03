# Kun — Baseline method comparison reproducibility review

Marker: `KUN_BASELINE_METHOD_BOARD_REVIEW_20260706T0825Z`

## Verdict

From a reproducibility and decision-protocol perspective, compare the current method against these two alternatives:

1. Current: `Packet-gated claim-layer reconciliation`
2. Alternative A: `Source-first claim adjudication`
3. Alternative B: `Debate-map-to-prose Baseline rebuild`

Do not elevate `display hygiene first` to a peer method. It is a tactical cleanup lane, not a Baseline-completion method, because it can improve visible confusion while leaving scientific state unresolved. Do not elevate `evaluation-first readiness gate` to a peer method either. It is a governance gate that every method should carry, not a competing production path.

## Method 1: Packet-gated claim-layer reconciliation

Permanent slug: `/methods/packet-gated-claim-layer-reconciliation`

Definition: starts from existing product claims, chips, source-position rows, trust artifacts, and page state; prepares bounded packets to recast, retire, re-parent, hide, relabel, or recompute derived artifacts without unsafe legacy-data loss.

Use when: production state already exists and must be corrected without breaking claim IDs, page history, claim chips, trust receipts, or public reader surfaces.

Inputs:
- Current claim rows, source-position rows, evidence attachments, page/chip display state, trust artifacts, and prior packet receipts.
- A stated target slice, such as a claim family, page section, or source-position queue segment.
- Pre-packet snapshot hashes or equivalent durable receipts.

Outputs:
- Read-only diagnosis report.
- Proposed packet manifest.
- Claim disposition table.
- Exact before/after artifact list.
- Verification checklist and rollback/postcondition requirements.
- No public state change unless a later separately gated execution path exists.

Stop gates:
- Any missing pre-snapshot, current-state ambiguity, orphaned claim disposition, unmatched claim count, stale public copy dependency, or inability to prove rollback/postconditions.
- Any packet that optimizes a trust/display score rather than reconciling claims to evidence and Baseline doctrine.

Allowed artifacts:
- Markdown reports, JSON/JSONL manifests, static HTML decision helpers, CSV/TSV audit tables, checksums, dry-run validation logs.

Safety boundaries:
- No DB/API/network execution inside the advisory method.
- No SQL, deploy, restart, git mutation, public cockpit mutation, page publish, trust recompute, or packet execution.
- No approval phrase embedded in the homepage or report.

Reproducibility strength: strongest for legacy production safety because it forces exact artifact identity, count reconciliation, rollback planning, and a separate apply boundary.

Reproducibility weakness: can feel backwards from the scientific story. It repairs product state, but it does not by itself guarantee the final Baseline has a coherent papers-to-ledger-to-prose argument.

## Method 2: Source-first claim adjudication

Permanent slug: `/methods/source-first-claim-adjudication`

Definition: starts from papers and source-position evidence, adjudicates what each source actually supports, qualifies, refutes, or does not inform, then permits claims or prose only after source-level stance and scope are recorded.

Use when: support status is uncertain, source links may be topical rather than evidential, claims have inflated scope, or the team needs a durable evidence foundation before deciding prose or product changes.

Inputs:
- Corpus protocol, paper list, full-text or abstract-only access labels, quoted spans with locations, rhetorical-zone tags, source metadata, and target questions/coverage cells.
- Existing claim IDs may be included as comparison targets, but they are not the authority.

Outputs:
- Source-position ledger with exact span locations, rhetorical zone, stance, scope, method/evidence type, and access level.
- Accept/limit/reject/no-info adjudication table for claims or candidate assertions.
- Coverage-gap list and countercase list.
- Reproducible source bundle manifest with hashes where available.

Stop gates:
- Any claim-source link lacks a findings-level rationale span.
- Any abstract-only source is treated as full support without being labeled.
- Any paper is used because it is merely topical.
- Any disagreement/countercase is filtered out instead of recorded.
- Any span location, source access label, or stance rationale is missing.

Allowed artifacts:
- Markdown adjudication report, JSONL source-position ledger, quote table, coverage matrix, exclusion table, source manifest, checksum file, static review HTML.

Safety boundaries:
- Read-only evidence work only.
- No claim/product mutation, DB write, trust recompute, page publish, SQL, API execution, deploy/restart, git mutation, or public cockpit mutation.
- The method may recommend a later packet, but must not contain an execution trigger.

Reproducibility strength: best at preventing topic-match evidence attachment, quote-mined introductions, and claim rescue. It makes the evidential authority auditable before any prose or production state depends on it.

Reproducibility weakness: can stall completion if every visible problem is pushed back to source work. The homepage must state proportionality rules: use it for disputed or high-impact claim families, not every cosmetic label.

## Method 3: Debate-map-to-prose Baseline rebuild

Permanent slug: `/methods/debate-map-to-prose-baseline-rebuild`

Definition: starts from a reviewed claim/status ledger and research-status debate map, then writes reader-facing Galaxy Evolution prose as a bounded rendering; derived product claims, evidence rows, and trust artifacts are emitted only after prose reconciles back to the ledger.

Use when: the primary goal is final Baseline completion rather than local cleanup, especially where the reader needs a coherent scientific story with uncertainty, countercases, and dated status.

Inputs:
- Reviewed corpus protocol.
- Claim/status ledger.
- Debate map with positions, counterpositions, certainty levels, and missing-critic checks.
- Wording contract mapping certainty, epistemic type, and source access to maximum prose modality.
- Sentence-binding schema.

Outputs:
- Reader-facing prose draft with every sentence bound to ledger entries.
- Prose sentence binding table.
- Wording-contract check.
- Debate/status summary.
- Derived-claim proposal and reconciliation plan for later packetization.

Stop gates:
- Any prose sentence lacks a ledger binding.
- Any sentence exceeds its certainty ceiling.
- Any debate axis lacks named positions or a recorded no-info/unknown state.
- Any derived claim/trust artifact cannot reconcile back to ledger entries.
- Any prose draft tries to rescue a legacy claim instead of rendering the ledger.

Allowed artifacts:
- Markdown prose draft, sentence-binding JSONL, wording-contract JSON, debate-map Markdown/JSON, static preview HTML, reconciliation tables, review report.

Safety boundaries:
- Docs/static preview only.
- No page publish, DB write, SQL, claim mutation, trust recompute, API/network call, deploy/restart, git mutation, or public cockpit mutation.
- No homepage wording that implies the prose draft is live product truth before packeted reconciliation.

Reproducibility strength: best match to the Baseline doctrine: papers to ledger to debate map to prose to derived product artifacts. It makes reader-facing completion auditable by sentence-level bindings.

Reproducibility weakness: unsafe if named `prose-first`, because that suggests prose can lead evidence. The permanent name should say `Debate-map-to-prose` or `Ledger-to-prose`, never simply `prose-first`.

## Recommended comparison protocol

Compare the three methods on the same decision dimensions:

- Starting authority: production claims, source spans, or reviewed ledger/debate map.
- Primary failure caught: legacy product drift, evidential misattachment, or overconfident/incoherent prose.
- Reproducible receipt: packet manifest, source-position ledger, or sentence-binding/wording-contract bundle.
- Stop condition: count/hash mismatch, missing source rationale, or orphan/over-modal prose sentence.
- Best next use: legacy cleanup, support adjudication, or final Baseline prose completion.

My default framing recommendation is `Debate-map-to-prose Baseline rebuild` for the next phase if the goal is final Galaxy Evolution Baseline completion. Keep `Packet-gated claim-layer reconciliation` as the production-safety method for carrying approved content into product state. Use `Source-first claim adjudication` when the ledger/debate map has disputed, missing, or topic-matched evidence.

## Permanent homepage requirements

Each method homepage should be static, durable, and non-executing. Required sections:

- Method name and stable slug.
- One-sentence definition.
- When to use / when not to use.
- Inputs.
- Outputs.
- Stop gates.
- Allowed artifacts.
- Safety boundaries.
- Reproducibility receipts.
- Relationship to Baseline steps.
- Common naming traps.
- Example decision question.
- Non-execution notice: the page describes a method and does not authorize mutation.

Recommended verification strings:

- `METHOD_HOME_PACKET_GATED_CLAIM_LAYER_RECONCILIATION`
- `METHOD_HOME_SOURCE_FIRST_CLAIM_ADJUDICATION`
- `METHOD_HOME_DEBATE_MAP_TO_PROSE_BASELINE_REBUILD`

## Ambiguities to remove before publication

- `Prose-first` is misleading. It sounds like prose leads evidence. Use `Debate-map-to-prose Baseline rebuild` or `Ledger-to-prose Baseline rebuild`.
- `Claim-layer reconciliation` could be mistaken for a science method. The page must say it is production-state reconciliation for existing claim artifacts, not the whole Baseline doctrine.
- `Source-first adjudication` must distinguish source stance from source existence. A paper being about a topic is not evidential support.
- `Evaluation-first readiness gate` should be named as a gate/checklist shared by all methods, not a comparable method homepage unless the product wants a fourth governance page.
- `Display hygiene first` should be named as `Display hygiene cleanup lane` if documented at all. Otherwise users may mistake visible label cleanup for scientific completion.
- All pages must avoid phrases that look like operational authorization. They should describe method boundaries, not provide mutation instructions.
- Slugs should not include dates, versions, or temporary board names. These are permanent method identities; dates belong in receipts, not URLs.

## Safety ledger

DB writes: 0. API/network calls: 0. SQL: 0. Packet execution: 0. Source/product code changes: 0. Git/deploy/restart: 0. Public cockpit mutation: 0. Approval phrases minted or quoted: 0.

KUN_BASELINE_METHOD_BOARD_REVIEW_20260706T0825Z
