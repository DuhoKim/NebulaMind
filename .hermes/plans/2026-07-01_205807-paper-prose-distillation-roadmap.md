# The Baseline — NebulaMind paper-to-prose operating plan

> **For Hermes and every helper lane:** this is the canonical operating plan for NebulaMind paper distillation. Use board-divided execution: Hermes captains and verifies, Lana designs/reviews the semantic pipeline, Goru performs mechanical checks, and Fable performs outside doctrine/adversarial review.

Marker: `THE_BASELINE_PREIMPLEMENTATION_REVIEW_PATCHED_20260703T0824Z`
Updated: 2026-07-03 17:01:20 KST / 2026-07-03T08:01:20Z
Status: CANONICAL BASELINE UPDATED AFTER PRE-IMPLEMENTATION QUARTET REVIEW — docs/cockpit only; no prose publish; no DB writes.

## Goal

Turn large volumes of published papers into clear, trustworthy NebulaMind prose without losing source scope, uncertainty, contradiction, or provenance.

## The primitive

**The primitive is not a sentence. The primitive is a claim/status ledger entry.**

The canonical flow is:

```text
papers -> claim/status ledger -> research-status/debate map -> prose -> derived claims/evidence/trust
```

Three invariants govern all work:

1. **Ledger-primary.** The claim/status ledger is the single source of truth. Prose is a rendering of the ledger, never the other way around.
2. **Every prose sentence binds to the ledger.** A sentence with no ledger entry behind it is an orphan sentence and must not ship.
3. **Prose modality may never exceed evidence certainty.** If the ledger says “observed in one scoped sample,” the prose may say “can / in this sample”; it may not say “does / generally.”

When prose and ledger disagree, the prose changes. Searching for papers to rescue an overbroad sentence is forbidden by name.

## Quartet authorship for this Baseline update

This update integrates all four Quartet lanes:

- **Fable** — outside doctrine co-author. Report: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/baseline-quartet-20260703T0738Z/fable_baseline_coauthor_report.md`
- **Lana** — methods/pipeline co-author. Report: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/baseline-quartet-20260703T0738Z/lana_baseline_coauthor_report.md`
- **Goru** — mechanical schema/gate co-author. Report: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/baseline-quartet-20260703T0738Z/goru_baseline_coauthor_report.md`
- **Hermes** — integration, cockpit, verification, and safety ledger.

Source survey integrated:

- Integrated doctrine: `/Users/duhokim/NebulaMind/NebulaMind/docs/v1_paper_distillation_methods_survey_20260703T0716Z/reports/PAPER_DISTILLATION_METHODS_SURVEY_INTEGRATION.md`
- Decision JSON: `/Users/duhokim/NebulaMind/NebulaMind/docs/v1_paper_distillation_methods_survey_20260703T0716Z/artifacts/methods_survey_integration_decision.json`

## What existing fields teach us to borrow

| Existing field / method family | What to borrow | How NebulaMind uses it | Hard limitation |
|---|---|---|---|
| PRISMA / Cochrane / living systematic reviews | Corpus protocol, inclusion/exclusion flow, “as of” cadence | Every section corpus has a protocol and found -> screened -> eligible -> included counts | A pile of recent papers is not a corpus |
| GRADE | Certainty dimensions and wording discipline | Certainty caps the strongest allowed prose wording | Do not collapse certainty into a reader-facing scalar |
| TextRank / LexRank / MMR / submodular coverage | Candidate ranking, diversity, balanced shortlist selection | Build 20–40 paper shortlists across topic, stance, method, scope, and countercases | Salience is not truth |
| SciFact / MultiVers / Evidence Inference / FEVER | Claim decomposition, rationale spans, stance labels | Every claim-source link must have an exact findings-level rationale span | Topic match is not evidence |
| Rhetorical / argumentative zoning | Background/method/finding/interpretation tags | Prevent quote-mining introductions or related-work text as findings | Zone tags must be audited |
| S2ORC / GROBID / SciBERT / SPECTER / SciNCL | Full-text structure, section parsing, citation graph, embeddings | Retrieve and structure papers at scale | Retrieval finds nearby text, not validated evidence |
| STORM / OpenScholar / PaperQA-style systems | Perspective map, grounded generation, citation verification loops | Render prose after the status/debate map exists | Grounded writing is downstream of the ledger |
| Elicit / scite / Semantic Scholar TLDR / Consensus / Scholarcy | UX patterns: cards, stances, question tables, quick summaries | Inspire review surfaces and operator cockpit views | Closed/opaque outputs are not authority |

## The exact step-by-step workflow

Follow these steps in order for every section of every page. Do not start a later step until the previous gate passes.

### Pre-implementation review consensus

Fable, Lana, and Goru all returned `PASS_WITH_PATCHES` before implementation. The primitive and step order are accepted. The required patches are schema-canonicalization and cockpit clarity, not a redesign.

Accepted patches before Claim Ledger Contract v1 starts:
1. Use one canonical ledger schema; lane-report variant field names are superseded.
2. Define all enum values in one registry.
3. Distinguish `modality` (assertion wording strength) from `certainty_level` (support strength).
4. Make the wording contract a function of `(certainty_level, epistemic_type, source_access)`.
5. Derive `certainty_level` from dimensions with a deterministic rule; do not hand-pick it.
6. Put stance on claim-source/span links, not as an uncontrolled entry-level field.
7. Add exact schemas for the stance matrix, wording contract check, and sentence bindings.
8. Quantify countercase quota.
9. Include ledger-to-production stance mapping before any product mutation.
10. Keep the first ledger contract small: schema + 8 AGN seed entries + the claim-2299 trio, roughly 12 entries. Do not turn the Baseline into ritual.

### Proportionality rule

Steps 0–9 may run inside one approved docs-only packet. They do not require one approval per micro-step. Only Step 10, which can touch product data or runtime state, requires a separate exact execution phrase. For a single-section run, artifacts may be consolidated if every pass condition remains individually checkable.

### Canonical enum registry

All implementations and validators must use these spellings exactly.

```yaml
certainty_level:
  - established
  - widely_supported
  - emerging_sample_limited
  - actively_debated
  - contradicted_or_model_dependent
  - no_info

epistemic_type:
  - review
  - observational_sample
  - single_case
  - simulation
  - theory
  - method

source_access:
  - full_text
  - abstract_only
  - metadata_only

rhetorical_zone:
  - background
  - related_work
  - method
  - finding
  - interpretation
  - limitation

modality:
  - is_are_does
  - commonly_probably
  - may_or_can
  - shows_can_occur
  - mixed_debated
  - in_model_only
  - reported_only

stance:
  - supports
  - qualifies
  - contradicts
  - mixed
  - no_info

links.type:
  - specializes
  - generalizes
  - contradicts
  - qualifies
  - depends_on
  - same_axis

verification_status:
  - pending
  - validated
  - blocked
```

Canonical naming rule: field names in this Baseline are authoritative. Variant names in lane reports are superseded. For example, use `assertion`, not `claim_statement`; use `evidence_spans[]`, not a bare `source_bibcodes[]` as the source of truth. `source_bibcodes` may exist only as a derived convenience index equal to the deduplicated list of `evidence_spans[].paper_id`.

### Step 0 — Pick the section and freeze the question

Owner: Hermes captain, with Fable if scope is contentious.

Do this:
1. Name the page, section, and exact reader question.
2. Name the current prose or claim rows that are in scope.
3. Name what is out of scope.
4. Record the artifact directory for this run.

Required artifact:
- `RUN_DIR/README.md`

Pass condition:
- A human can read the README and say exactly what the packet is and is not allowed to change.

Stop if:
- The task objective is “raise trust,” “find support,” “rescue wording,” or “improve score.” Those are not valid objectives.

### Step 1 — Write the corpus protocol before collecting papers

Owner: Lana for semantic coverage; Goru for mechanical quotas; Hermes integrates.

Do this:
1. Define coverage cells before search. Minimum cells:
   - mechanism
   - prevalence/frequency
   - dominance/causal attribution
   - alternatives/countercases
   - method limitations
   - reviews/status backbone
2. Write the search queries per cell.
3. Write inclusion rules.
4. Write exclusion rules.
5. Record flow counts as papers move through the protocol:
   - found
   - deduped
   - screened
   - eligible
   - included
   - excluded with reason

Required artifacts:
- `RUN_DIR/artifacts/corpus_protocol.md`
- `RUN_DIR/artifacts/corpus_flow.json`
- `RUN_DIR/artifacts/candidates_raw.jsonl`
- `RUN_DIR/artifacts/candidates_screened.jsonl`

Pass condition:
- Every required coverage cell has at least one candidate.
- Countercase/alternative cell contains **at least 2 independent sources per named debate axis**, or the packet records a signed attestation: `no countercases found after targeted search`, listing the exact queries used. Token compliance with one stale countercase fails this gate.
- Goru can reproduce the counts from the JSONL files.

Stop if:
- The corpus is only a recency feed.
- A shortlist is made by raw ranking before coverage cells exist.
- The operator cannot tell why a paper was included.

### Step 2 — Acquire full text and label source strength

Owner: Hermes for acquisition, Goru for file/count checks.

Do this for every included paper:
1. Store stable identifiers: bibcode, DOI, arXiv ID, title, year, URL.
2. Fetch full text when available.
3. If only abstract is available, label it permanently as `abstract_only: true`.
4. Parse or extract sections when possible.
5. Record whether the paper is a review, observational sample, single case, simulation, theory, or method paper.

Required artifacts:
- `RUN_DIR/artifacts/included_papers.jsonl`
- `RUN_DIR/artifacts/fulltext_inventory.json`
- `RUN_DIR/artifacts/source_strength_summary.md`

Pass condition:
- 100% of included rows have stable IDs and a source-strength label.
- Abstract-only rows are marked and cannot later masquerade as full-text findings.

Stop if:
- A paper has no stable identifier.
- Abstract-only evidence is being used for strong prevalence or mechanism claims.

### Step 3 — Extract candidate spans with location and rhetorical zone

Owner: Lana for semantic extraction; Goru samples location/format; Hermes verifies.

Do this for each paper:
1. Extract exact quotes, not paraphrases.
2. Record location: section, page, paragraph, table/figure if known.
3. Tag rhetorical zone:
   - `background`
   - `related_work`
   - `method`
   - `finding`
   - `interpretation`
   - `limitation`
4. Extract scope fields if present:
   - sample size
   - redshift
   - mass range
   - environment
   - fraction/percentage/ratio
   - simulation name/model assumptions
5. Keep background/related-work spans, but do not allow them to count as findings.

Required artifact:
- `RUN_DIR/artifacts/evidence_spans.jsonl`

Minimum JSONL row shape:

```json
{
  "paper_id": "bibcode_or_doi_or_arxiv",
  "title": "string",
  "span_id": "stable_span_id",
  "quote": "exact quoted text",
  "location": {"section": "Results", "page": 7, "paragraph": 3},
  "rhetorical_zone": "finding",
  "epistemic_type": "observational_sample",
  "scope": {"n": 123, "redshift": "z~2", "mass": "M*>10^10.5", "fraction": "46%"},
  "limits": ["sample-limited", "selection effects"]
}
```

Pass condition:
- 100% of candidate spans have paper ID, quote, location, zone, and epistemic type.
- Finding claims use `finding` or carefully justified `interpretation` zones, not background.

Stop if:
- A sentence from an introduction/review-of-others is being cited as the paper’s own finding.
- A quote has no location.

### Step 4 — Build the claim/status ledger

Owner: Lana creates semantic entries; Goru validates schema; Hermes integrates.

Each ledger entry must be atomic: one assertion, one scope, one certainty posture. Compound statements split.

Required artifact:
- `RUN_DIR/artifacts/claim_status_ledger.jsonl`

Required ledger schema:

```json
{
  "entry_id": "ledger_agn_0001",
  "assertion": "AGN-driven outflows can expel cold gas in selected massive galaxies.",
  "modality": "may_or_can",
  "scope": {
    "population": "massive galaxies",
    "sample": "specific observed samples",
    "redshift": "z~2 where applicable",
    "mass": "if reported",
    "environment": "if reported",
    "simulation_context": null
  },
  "epistemic_type": "observational_sample",
  "source_access": "full_text",
  "method_or_model": "survey/instrument/model if known",
  "source_bibcodes": ["derived_from_evidence_spans"],
  "evidence_spans": [{
    "paper_id": "bibcode",
    "span_id": "span_0001",
    "quote": "exact quote",
    "location": "section/page/paragraph",
    "rhetorical_zone": "finding",
    "stance": "supports",
    "rationale": "This findings sentence directly reports the scoped result."
  }],
  "certainty_dimensions": {
    "directness": "direct|indirect|model_only",
    "consistency": "consistent|mixed|single_source",
    "precision": "quantified|qualitative|unclear",
    "sample_size": "n/value/unknown",
    "model_dependence": "none|low|high"
  },
  "certainty_level": "emerging_sample_limited",
  "links": [{"type": "specializes", "entry_id": "ledger_agn_general_mechanism"}],
  "as_of": "2026-07-03",
  "verification_status": "pending",
  "verification_note": "why pending/validated/blocked"
}
```

`modality` vs `certainty_level`:
- `modality` is the strength of the assertion as written. Example: “can expel” = `may_or_can`; “expels” = `is_are_does`.
- `certainty_level` is the strength of the support behind the assertion.
- Prose is capped by both: the rendered sentence may not be more declarative than the assertion’s `modality`, and may not be stronger than `certainty_level` allows.

Deriving `certainty_level` from dimensions:
1. Start from evidence type: review or multi-sample direct observational evidence may reach `established`; single observational sample starts at `emerging_sample_limited`; simulation/theory starts with explicit model/theory bounds.
2. Downgrade one tier for each: `consistency = mixed|single_source`, `directness = indirect|model_only`, `precision = qualitative|unclear`, or `model_dependence = high`.
3. If credible sources disagree in stance, set `certainty_level = actively_debated` unless the disagreement is resolved in the rationale.
4. If the entry has no span-level support, set `certainty_level = no_info` and block rendering.
5. `certainty_level` is a deterministic result of dimensions, not a hand-picked confidence label.

Pass condition:
- Ledger JSONL parses.
- Every entry has at least one evidence span unless explicitly marked `no_info` or `open_question`.
- Every source ID maps to the included paper inventory.
- No compound entries remain.

Stop if:
- The ledger entry says “AGN feedback quenches galaxies” while spans only support “outflows occur in a subset.”
- A source is attached by topic rather than by rationale span.

### Step 5 — Verify claim-source stance

Owner: Lana for stance reasoning; Goru for exact linkage/counts; Hermes verifies samples.

For every ledger entry and paper link, assign one stance:
- `supports`
- `qualifies`
- `contradicts`
- `mixed`
- `no_info`

Do this:
1. Read the exact span.
2. Ask: does this span support the exact assertion, not merely the topic?
3. Record why in one short rationale sentence.
4. Preserve contradictions and mixed evidence.

Required artifact:
- `RUN_DIR/artifacts/claim_source_stance_matrix.jsonl`

Required JSONL row shape:

```json
{
  "entry_id": "ledger_agn_0001",
  "paper_id": "bibcode",
  "span_id": "span_0001",
  "stance": "supports",
  "rationale": "The quoted findings sentence reports the scoped assertion.",
  "rhetorical_zone": "finding",
  "source_access": "full_text",
  "reviewer": "lana|hermes|goru",
  "verification_status": "validated"
}
```

Authority rule: this stance matrix is the normalized claim-source link table. Ledger `evidence_spans[]` may embed the same values for readability, but validators treat `claim_source_stance_matrix.jsonl` as the authoritative link audit.

Pass condition:
- Every claim-source link has stance + rationale + span ID.
- No `supports` label exists without a finding-level rationale span.

Stop if:
- A paper is being attached because title/abstract keywords match.
- Counterevidence is being filtered out to make prose cleaner.

### Step 6 — Compute the research-status/debate map

Owner: Lana with Fable adversarial review; Goru checks coverage/counts; Hermes integrates.

Do this for each section axis:
1. Group ledger entries by mechanism, prevalence, dominance, alternatives, and limitations.
2. Assign status:
   - `established`
   - `widely_supported`
   - `emerging_sample_limited`
   - `actively_debated`
   - `contradicted_or_model_dependent`
   - `no_info`
3. Name the positions and the papers holding them.
4. Write what would change the status in future.
5. Stamp the map with “as of DATE.”

Required artifacts:
- `RUN_DIR/artifacts/status_debate_map.json`
- `RUN_DIR/reports/STATUS_DEBATE_MAP.md`

Pass condition:
- Every status label traces to ledger entries.
- Every debate axis has named positions.
- Countercase quota is met or the section is blocked. For each `established` or `widely_supported` status, the map must answer: “who would disagree, and are they in the corpus?” If unanswered, downgrade the status or fix the corpus.

Stop if:
- “Consensus” is computed from a biased retrieval denominator.
- “Actively debated” is treated as a failure rather than a valid reader-facing result.

### Step 7 — Apply the wording contract

Owner: Hermes applies; Lana reviews; Goru checks mechanically.

Allowed wording rule:

The wording contract is a function of three axes: `(certainty_level, epistemic_type, source_access)`.

1. `certainty_level` controls how confident the sentence may sound.
2. `epistemic_type` controls required qualifiers such as “in simulations” or “single case.”
3. `source_access` controls whether the source is full text, abstract-only, or metadata-only.

| Axis condition | Max prose language | Forbidden wording |
|---|---|---|
| `certainty_level = established` | “is / are / does” with normal scope | universal claims outside corpus scope |
| `certainty_level = widely_supported` | “commonly / probably / appears to” | “always / proves” |
| `certainty_level = emerging_sample_limited` | “can / may / in this sample / in a substantial subset” | “generally / is common” unless prevalence supports it |
| `certainty_level = actively_debated` | “evidence is mixed / actively debated; X argues..., Y finds...” | hiding the disagreement |
| `certainty_level = contradicted_or_model_dependent` | “not established,” “model-dependent,” or explicitly bounded | declarative field-level claims |
| `certainty_level = no_info` | not renderable except as open question | factual prose claim |
| `epistemic_type = single_case` | “shows this can occur” | “common / typical” |
| `epistemic_type = simulation` | “in simulations / in this model” | observed-frequency language |
| `source_access = abstract_only` | “reported / can (as reported)” only when the abstract itself states the finding | sole support for prevalence-general, dominance, or `established` wording |
| `source_access = metadata_only` | not renderable except as source-discovery metadata | any evidence claim |

Required artifact:
- `RUN_DIR/artifacts/wording_contract_check.json`

Required JSON shape:

```json
{
  "sentences": [
    {
      "sentence_id": "sent_0001",
      "text": "AGN feedback can expel gas in a substantial subset of massive galaxies.",
      "bound_entry_ids": ["ledger_agn_0001"],
      "max_allowed_tier": "may_or_can",
      "actual_tier": "may_or_can",
      "certainty_level": "emerging_sample_limited",
      "epistemic_type": "observational_sample",
      "source_access": "full_text",
      "passes": true,
      "failure_reason": null
    }
  ]
}
```

Pass condition:
- Every planned prose sentence has a max allowed wording tier.
- Every sentence maps to `sentence_id`, `bound_entry_ids`, `max_allowed_tier`, and `actual_tier`.
- Zero planned sentences exceed their ledger tier.

Stop if:
- A reviewer has to rely on “sounds careful” rather than a recorded tier.

### Step 8 — Render prose only after Steps 0–7 pass

Owner: Hermes drafts; Lana reviews; Fable may adversarially challenge; Goru checks sentence bindings.

Do this:
1. Draft paragraphs from the status/debate map, not from memory.
2. Bind every sentence to one or more ledger entry IDs.
3. Put debate inside topical paragraphs, not hidden in an isolated “uncertainty” ghetto.
4. Keep the reader-facing voice clear and compact.
5. Do not create or mutate DB rows. This is still an offline preview.

Required artifacts:
- `RUN_DIR/reports/PROSE_PREVIEW.md`
- `RUN_DIR/artifacts/prose_sentence_bindings.jsonl`

Required JSONL row shape:

```json
{
  "sentence_id": "sent_0001",
  "paragraph_id": "para_agn_001",
  "text": "AGN feedback can expel gas in a substantial subset of massive galaxies.",
  "bound_entry_ids": ["ledger_agn_0001", "ledger_agn_0002"],
  "citation_span_ids": ["span_0001", "span_0007"],
  "actual_tier": "may_or_can",
  "max_allowed_tier": "may_or_can",
  "passes_binding_check": true,
  "passes_modality_check": true
}
```

Pass condition:
- 100% of sentences have ledger bindings.
- 0 orphan sentences.
- 0 modality overflows.

Stop if:
- A sentence cannot be bound. Delete or rewrite it.

### Step 9 — Adversarial audit before any exact-diff packet

Owner: Fable/Lana for critique; Goru for mechanical validation; Hermes integrates.

Audit checklist:
- orphan sentence
- scope inflation
- missing countercase
- simulation-as-observation
- prevalence without sample/fraction
- quote-mined background zone
- false consensus
- claim rescue
- score chasing

Required artifacts:
- `RUN_DIR/reports/ADVERSARIAL_AUDIT.md`
- `RUN_DIR/artifacts/mechanical_validation.json`

Pass condition:
- All audit blockers are either resolved or explicitly accepted by the operator.

Stop if:
- Any tripwire below is pulled and unresolved.

### Step 10 — Complete the Galaxy Evolution wiki page through an approval-gated exact-diff/product gate

Owner: Hermes, with production-data mutation preflight if DB writes are proposed.

This is the final Baseline execution gate for the canonical Galaxy Evolution wiki page. It is separate from docs-only Baseline work and always needs explicit approval. Step 10 is not merely “prepare a packet”; it ends only when the approved exact diff has been applied, probed, and the wiki page is verified complete — or when the operator chooses to stop at a non-executed packet.

Required before any DB/product/wiki mutation:
1. Whole-page before/after diff.
2. Row-level backup.
3. Rollback script or rollback plan.
4. Goru validation JSON.
5. Lana/Fable review.
6. Exact user EXECUTE phrase.
7. Post-apply probes.
8. Ledger-to-production stance mapping table. Required mapping must be explicit before any derived evidence row is written: `supports -> supports`; `qualifies -> neutral` plus qualifier note unless stronger mapping is justified; `contradicts -> challenges|refutes` by strength; `mixed -> split links or neutral+mixed note`; `no_info -> none`. No production evidence stance may be improvised.

Pass condition:
- The approved exact diff has been applied, post-apply probes pass, rollback remains available, and the canonical Galaxy Evolution wiki page is verified complete.

Stop if:
- Anyone tries to bundle prose preview and production mutation into one informal step.

## Tripwires anyone may pull

Any Quartet member or the operator may halt work by naming one of these:

- `rescue search`
- `orphan sentence`
- `scope inflation`
- `feed-dump corpus`
- `false consensus`
- `quote-mined zone`
- `simulation-as-observation`
- `topic-match evidence`
- `score chasing`
- `trust scalar laundering`

A pulled tripwire is a finding to record, not an argument to win.

## Immediate AGN worked-example seeds

The next artifact should populate these as ledger entries from the 26 already full-text-checked AGN papers:

1. Ejective mechanism exists in selected AGN / massive galaxies.
2. Outflow prevalence is significant in some scoped samples, not universal.
3. D’Eugenio 2024 is a case/mechanism example, not prevalence.
4. AGN maintenance/heating is a distinct preventive channel.
5. Gas retention and low star-formation efficiency qualify simple gas-removal stories.
6. Strangulation/environment/stripping remain alternative quenching channels.
7. Central/BH predictors and halo/environment drivers are both real axes.
8. Simulation rows support mechanisms under model assumptions, not observed frequency.

Claim 2299 must split into linked ledger entries:

- mechanism: AGN feedback can expel/heat gas in scoped contexts.
- prevalence: outflow signatures appear in a substantial subset, not universally.
- dominance/debate: AGN vs stellar feedback/environment/recycling remains actively debated.

## Graphical progress model for cockpit

The cockpit must display this progress chain:

```text
[1 corpus protocol] -> [2 source inventory] -> [3 span extraction] -> [4 claim ledger] -> [5 status map] -> [6 wording contract] -> [7 prose preview] -> [8 adversarial audit] -> [9 exact-diff gate]
```

Current state as of this update:

| Stage | State | Evidence |
|---|---|---|
| 1 corpus protocol | partial / needs contract formalization | AGN corpus gate and source survey exist |
| 2 source inventory | partial | 26 AGN full-text scope checks exist |
| 3 span extraction | partial | scope checks have spans but not final ledger schema |
| 4 claim ledger | next required | Claim Ledger Contract v1 not yet built |
| 5 status map | blocked by ledger | status map must derive from ledger |
| 6 wording contract | specified here | needs machine-checkable artifact |
| 7 prose preview | blocked | no prose until ledger passes |
| 8 adversarial audit | future | after preview |
| 9 exact-diff gate | locked | requires separate approval phrase |


## Pre-implementation review discussion synthesis

Review run: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/baseline-preimplementation-review-20260703T0810Z`

Lane verdicts:
- Fable: `PASS_WITH_PATCHES` — doctrine sound; add proportionality, abstract-only tier, countercase quota, stance mapping, missing-critics test, cockpit next-gate visibility.
- Lana: `PASS_WITH_PATCHES` — sequence sound; canonicalize enums, field names, certainty derivation, stance location, and schema authority before implementation.
- Goru: `PASS_WITH_PATCHES` — cockpit parses; add machine-checkable schemas for stance matrix, wording-contract check, and sentence bindings.

Hermes integration decision: all requested patches above are accepted into this Baseline. Claim Ledger Contract v1 may start only from this patched Baseline, not from the earlier unpatched variant.

Review reports:
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/baseline-preimplementation-review-20260703T0810Z/fable_preimplementation_review.md`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/baseline-preimplementation-review-20260703T0810Z/lana_preimplementation_review.md`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/baseline-preimplementation-review-20260703T0810Z/goru_preimplementation_review.md`

Review marker: `THE_BASELINE_PREIMPLEMENTATION_REVIEW_PATCHED_20260703T0824Z`

## Approval phrases

### Recommended next approval: build the ledger contract

```text
claim ledger contract
```

Expanded version:

```text
APPROVE CLAIM LEDGER CONTRACT V1: Build a docs-only Claim Ledger Contract v1 and AGN worked example from the 26 already full-text-checked AGN papers. Produce schema Markdown, JSONL ledger entries, wording-contract checks, and Goru/Lana/Fable review reports. No Galaxy Evolution prose draft, no DB writes, no SQL mutations, no migrations, no deploy/restart, no product publish, no commit/push/merge, no secrets, and no exact-diff packet without separate approval.
```

## Safety ledger

This Baseline update changed documentation/cockpit artifacts only.

- DB writes: 0
- SQL mutations: 0
- migrations: 0
- product publish: 0
- exact-diff packet execution: 0
- deploy/restart: 0
- git commit/push/merge: 0
- secrets: 0
- Galaxy Evolution prose drafting: 0

THE_BASELINE_PREIMPLEMENTATION_REVIEW_PATCHED_20260703T0824Z
