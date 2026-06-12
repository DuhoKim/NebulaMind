# Claim Marker Persistence - Design v1

**Author:** Kun
**Date:** 2026-06-02 14:43 KST
**Status:** Draft for Tori implementation
**Live grounding:** Read against local NebulaMind repo on 2026-06-02. Relevant code paths: `backend/app/agent_loop/autowiki/tasks.py` (`sonnet_section_rewrite`, `autowiki_tick` section rewrite), `backend/app/agent_loop/autowiki/proposers.py` (`propose_section_rewrite` prompt), `backend/app/agent_loop/tasks.py` (`synthesize_renovation`, `sync_verbatim_markers_nightly`), and `backend/app/agent_loop/marker_embed/*` (`claim_marker_embed_page`, `run_pipeline`, `inject_markers`). Prior empirical context from HwaO: page 57 has 85 engine-matched claims; targeted full-page rewrite reached 85/85 visible markers, then autonomous section rewrites degraded to 34 markers in about 90 minutes.

---

## 1. Executive Recommendation

The durable fix is **not** to keep giving every section rewriter all page claims and hope the LLM preserves global coverage. That is structurally unstable: a section rewrite can only honestly assert the claims that belong in that section, and replacement semantics destroy markers that were present in the old section.

Recommended architecture:

1. **Create a canonical claim-to-section ownership layer in the DB.**
   Each claim should have a persistent owner section, assignment confidence, assignment method, and lifecycle status. `claims.section` already exists, but it is a loose text field; for marker persistence it should become an auditable mapping, preferably in a new table.

2. **Make every section rewrite section-scoped.**
   A rewrite of section S receives only:
   - claims owned by S,
   - optional nearby/related claims for context,
   - the current markers and trust/consensus markers already present in S,
   - an explicit minimum retention contract for owned claims.

3. **Run a post-rewrite repair pass after commit, scoped to the rewritten section and version.**
   This pass should be lightweight in prose terms: it must not rewrite prose. It should either reinsert markers onto existing asserted text or report a missing-assertion deficit. It should preserve trust/consensus markers and all non-claim HTML comments.

4. **Add a coverage watchdog with rollback/escalation.**
   If page-level visible claim coverage drops below a target floor (recommended: 80 percent of active engine-matched claims) or a rewritten section loses too many owned markers, do not silently accept drift. Trigger repair; if repair cannot recover, queue a targeted section regeneration with missing owned claims as hard requirements.

The key design principle is: **the DB owns marker intent; page prose contains marker realization.** Prose can change autonomously, but each write is reconciled against the canonical ownership map before it becomes the stable visible page.

---

## 2. Current System Observations

### 2.1 Author-time marker prompting exists but is underpowered

Tori's Phase 2b changes are visible in the three requested rewrite surfaces:

- `sonnet_section_rewrite` loads up to 200 page claims and prompts Sonnet to weave markers inline.
- `propose_section_rewrite` in the AstroSage proposer path includes the same marker instructions.
- `synthesize_renovation` includes page claims in its synthesis prompt and asks the model to preserve/weave markers.

This is useful, but too global. The prompt says "key claims on this page", while the write target is one section. The model is incentivized to select a small natural subset, and the replacement deletes whatever markers existed in that section before.

### 2.2 The current repair pipeline re-derives markers from prose

`claim_marker_embed_page` calls `run_pipeline`, which:

- strips existing `<!--claim:*-->`, `<!--/claim:*-->`, and `<!--topic:*-->` markers;
- resolves claims by `claims.section`;
- aligns claim text to current sentences;
- injects marker pairs through `inject_markers`;
- writes a new `page_versions` row and logs `claim_marker_runs`.

This is conservative and good for avoiding stale anchors. But it has no persistent concept of "this claim belongs to this section and must remain covered unless explicitly retired." If a rewrite no longer asserts a claim, the repair task drops the marker rather than recovering the missing assertion.

### 2.3 There is a dispatch timing hazard

In both autowiki section-write paths, `emit_reembed(page_id)` is called before the surrounding DB transaction commits. If Celery starts quickly, the marker task can read pre-rewrite content. The manual router calls `emit_reembed` after commit, which is safer. The design should use after-commit dispatch or pass an expected page version/content hash to the repair task.

### 2.4 Existing marker syntax is mixed in practice

The prompt examples use single comments such as `<!--claim:123-->`, while the marker injector/frontend path expects paired spans: `<!--claim:123-->...<!--/claim:123-->`. The persistence design should normalize internally on paired marker spans for renderability, while tolerating single opening comments from LLM output by converting them in repair.

---

## 3. Canonical Claim-Section Ownership

### 3.1 Should each section own a pre-assigned set of claims?

**Yes.** This is the central fix.

A claim marker is not just typography; it is the join between prose and evidence/trust data. That join needs a stable owner. Section ownership gives every rewrite a local responsibility: "for this section, preserve or reassert these claims."

Without ownership, page-level coverage is an emergent property of independent rewrites. With ownership, page-level coverage becomes the sum of section-level contracts.

### 3.2 Recommended table

Add a table rather than overloading `claims.section`:

```sql
CREATE TABLE claim_section_assignments (
  id SERIAL PRIMARY KEY,
  claim_id INTEGER NOT NULL REFERENCES claims(id) ON DELETE CASCADE,
  page_id INTEGER NOT NULL REFERENCES wiki_pages(id) ON DELETE CASCADE,
  owner_section TEXT NOT NULL,
  owner_section_key TEXT NOT NULL,
  assignment_status TEXT NOT NULL DEFAULT 'active',
  assignment_method TEXT NOT NULL,
  confidence FLOAT NOT NULL DEFAULT 1.0,
  evidence JSONB,
  last_seen_marker_version INTEGER,
  last_seen_marker_section TEXT,
  last_seen_marker_span TEXT,
  missing_since TIMESTAMP,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  UNIQUE (claim_id)
);

CREATE INDEX ix_claim_section_assignments_page_section
  ON claim_section_assignments(page_id, owner_section_key);
```

`owner_section_key` should be a normalized stable key, for example lowercase heading text with punctuation collapsed. If NebulaMind later introduces section IDs, this key can migrate to that ID.

### 3.3 Assignment algorithm

Use a deterministic cascade:

1. **Existing exact section:** if `claims.section` matches a current H2, assign there with `method='claim_section_exact'`, confidence 1.0.
2. **Fuzzy section match:** if `claims.section` no longer matches but is close to a current H2, assign with `method='claim_section_fuzzy'`, confidence from the fuzzy score.
3. **Current marker location:** if the claim marker is visible in page content, assign to the section containing that marker with `method='marker_location'`.
4. **Semantic section classifier:** for unresolved claims, classify against H2 titles plus section summaries using Sonnet or Atom/AstroSage. Require JSON output and confidence.
5. **Orphan bucket:** if confidence remains low, mark `assignment_status='orphan_pending'`; do not force it into a section.

Page 57 likely starts with high confidence because `claims.section` is already used by the marker pipeline and prior audits found section-name matching to be clean after remap.

### 3.4 Ownership changes

Ownership should be stable but not immutable.

Allow reassignment when:

- a section is renamed or merged;
- a full-page coherence pass restructures the page;
- repair repeatedly finds the claim asserted in a different section with high confidence;
- a human/admin override moves it.

Every reassignment should be logged in a small history table or audit JSON. This matters because moving a claim changes where the trust marker is expected to appear.

---

## 4. Section Rewrite Contract

### 4.1 Prompt input

For a rewrite of section S, provide:

- `owned_claims`: all active claims assigned to S, ordered by `order_idx` or assignment confidence;
- `must_keep_claims`: accepted/consensus/high-trust claims owned by S;
- `optional_claims`: debated/unverified claims owned by S that can be omitted only if the section remains scientifically coherent;
- `existing_section_markers`: claim IDs and trust/consensus comments currently visible in S;
- `page_context_claims`: at most 5 to 10 related claims from adjacent sections, explicitly labeled "context only, do not force into this section."

Do **not** pass all 85 page claims as a flat list to every section rewrite. That is the failure mode.

### 4.2 Prompt output contract

Require a machine-readable footer after the markdown section:

```text
<!--marker-report
{
  "section": "Quenching Mechanisms",
  "asserted_claim_ids": [123, 124, 125],
  "omitted_owned_claim_ids": [{"id": 126, "reason": "not asserted in rewritten prose"}],
  "preserved_control_markers": ["accepted", "consensus"]
}
-->
```

The repair pass can strip this report before final publish or leave it in a non-rendered audit location. The point is not to trust the LLM blindly; the point is to make omissions explicit and testable.

### 4.3 Commit gate

Before accepting the section replacement:

- parse visible claim markers in the new section;
- compare against `owned_claims`;
- require all `must_keep_claims` to be either visibly marked or listed as omitted with a valid reason;
- require section owned coverage above a floor, recommended 80 percent for page 57 while the page has 85 engine-matched claims;
- preserve all non-claim control comments from the old section unless explicitly invalidated.

For autonomous rewrites, omission should not be fatal for every debated claim. It should be fatal for accepted/consensus claims and for page-level coverage below the watchdog threshold.

---

## 5. Post-Rewrite Marker Repair

### 5.1 Is lightweight repair viable?

**Yes, but only as marker repair, not silent claim resurrection.**

A viable repair pass can:

- convert single `<!--claim:N-->` comments into paired spans when the nearby sentence asserts the claim;
- reinsert missing paired markers around existing sentences that already assert owned claims;
- restore trust/consensus/control comments that were accidentally dropped;
- update `last_seen_marker_*` fields;
- record missing assertions for later regeneration.

It should not:

- invent new prose;
- attach a claim to merely topical text;
- use old marker positions if the old sentence is gone;
- preserve a marker just because the old section had it.

### 5.2 Repair algorithm

After a committed section rewrite:

1. Load the committed page version and the rewritten section text.
2. Load active assignments for that section.
3. Strip only claim markers from the new section for alignment; preserve other HTML comments.
4. For each owned claim:
   - if a valid paired marker already exists, validate it and keep it;
   - if a single opening marker exists, validate the containing sentence and convert to a paired span;
   - otherwise run semantic alignment against sentences in the rewritten section;
   - inject a paired marker only if the sentence asserts the claim with high confidence.
5. Merge the repaired section back into the same committed page version or create a new marker-repair version linked to `source_version`.
6. Log claimed, repaired, missing, and unsafe counts.

The existing `marker_embed` pipeline already has many of these pieces. The main change is that repair should be **section-scoped and assignment-aware**, rather than page-wide and stateless.

### 5.3 Risks

Main risks and mitigations:

- **False positive anchoring:** a marker on a related but non-equivalent sentence misleads trust rendering. Mitigation: strict predicate-equivalence prompt, Atom/Sonnet veto, no topical anchors counted as trust markers.
- **Coverage gaming:** adding markers to weakly related sentences just to hit 80 percent. Mitigation: separate `asserted_marker_count` from `topic_anchor_count`; coverage floor only counts asserted markers.
- **Race conditions:** repair reads stale page content. Mitigation: dispatch after commit and pass `expected_source_version`; abort if version changed.
- **Marker syntax corruption:** LLM emits unmatched comments. Mitigation: repair normalizes paired markers and validator rejects unmatched/duplicate IDs.
- **Control marker loss:** generic claim stripper removes unrelated comments. Mitigation: strip only `<!--claim:N-->`, `<!--/claim:N-->`, and optionally `<!--topic:N-->`; preserve `<!--accepted-->`, `<!--consensus-->`, and unknown comments by default.

---

## 6. Trust and Consensus Marker Preservation

Trust/consensus markers such as `<!--accepted-->`, `<!--consensus-->`, or related control comments should be treated as **control markers**, not claim markers.

Rules:

1. The claim-marker stripper must never remove unknown HTML comments.
2. The repair pass should inventory control markers in the old section and new section.
3. If a control marker is attached to a claim marker, preserve it with that claim where possible.
4. If a control marker cannot be confidently reattached, keep it in an audit log and do not blindly place it elsewhere.
5. Frontend rendering should ultimately prefer live `claims.trust_level` for color/state, with control comments used only for legacy compatibility or special consensus annotations.

This avoids the common failure where a "repair" script successfully restores `<!--claim:N-->` while deleting the trust annotation that made the marker meaningful.

---

## 7. Coverage Watchdog

Add a watchdog task that runs after every repair and periodically across active pages.

Recommended metrics:

- `active_claims`: claims with active assignment status.
- `visible_asserted_markers`: valid paired claim markers in current page content.
- `owned_section_coverage`: visible asserted markers for section S divided by active assigned claims for S.
- `page_coverage`: visible asserted markers divided by active claims.
- `must_keep_missing`: accepted/consensus assigned claims with no valid marker.
- `marker_churn`: markers lost and regained across the last N versions.

Recommended gates for page 57:

- warning below 80 percent page coverage;
- repair retry below 80 percent;
- targeted regeneration below 70 percent or if any accepted/consensus claim is missing after repair;
- emergency alert below 50 percent.

The current nightly verbatim sync alarm checks marker count `<30` for page 57. Replace that with assignment-aware coverage. A fixed marker count is brittle once pages have different claim counts.

---

## 8. How This Answers the Four Questions

### Q1. Should each section have a pre-assigned set of claims it owns?

Yes. Assign every active claim to one canonical owner section. Start from `claims.section`, then repair via marker location, fuzzy heading match, and semantic classification. Store this outside raw prose so autonomous rewrites inherit stable responsibilities.

### Q2. Is a post-rewrite marker repair pass viable?

Yes. It is viable if it only touches markers and only anchors claims to sentences that already assert them. It is not viable as a way to maintain high coverage when the new prose no longer contains the claim. In that case, repair should report a missing assertion and trigger a targeted rewrite/regeneration.

### Q3. Should the DB store canonical claim-to-section mapping separately?

Yes. `claims.section` can seed the mapping, but a separate assignment table is better because it can track confidence, method, status, last-seen marker version, missing-since state, and reassignment history without overloading the claim itself.

### Q4. Any better architecture?

The best architecture is a **two-layer marker system**:

- DB assignment layer: durable claim ownership and coverage intent.
- Prose realization layer: paired inline markers in `wiki_pages.content`, regenerated after each write.

Author-time marker emission remains useful, but it becomes a first pass. The post-commit repair/watchdog is the source of stability.

---

## 9. Implementation Plan

### Phase 1 - DB ownership and audit

- Add `claim_section_assignments`.
- Backfill assignments for page 57 from `claims.section`.
- Add a script: `scripts/backfill_claim_section_assignments.py --page-id 57`.
- Add assignment-aware audit: count active claims, visible markers, missing by section, must-keep missing.

### Phase 2 - Section-scoped rewrite context

- Replace flat page-claim prompt blocks with `owned_claims` for the target section.
- Keep a small related-claims context bucket labeled context-only.
- Add marker-report footer parsing.
- Add commit gate for must-keep claims.

### Phase 3 - After-commit repair

- Change `emit_reembed` call sites so repair dispatch happens after commit.
- Pass `page_id`, `section_key`, and `expected_source_version`.
- Make repair section-scoped and assignment-aware.
- Normalize single comment markers to paired marker spans.
- Preserve control comments.

### Phase 4 - Watchdog and recovery

- Add `claim_marker_coverage_watchdog(page_id)`.
- Replace fixed count alarm with coverage ratio.
- If repair cannot recover section coverage, queue targeted section rewrite with missing owned claims as explicit requirements.
- Add dashboard columns to marker audit: owner section, assignment method, missing since, last seen version.

---

## 10. Platoon Assignment

| Job | Owner model | Reason | Fallback |
|---|---|---|---|
| DB migration and deterministic assignment backfill | Tori / Python deterministic | Schema and scripts should be exact, testable, and non-LLM | Kun review |
| Section ownership semantic classifier for unresolved claims | Claude Sonnet 4.6 | Reliable JSON and strict instruction following | AstroSage-70B for astronomy edge cases |
| Section rewrite authoring | Claude Sonnet 4.6 primary | Best structural compliance for section-specific contracts | AstroSage-70B when cloud unavailable |
| Local astronomy prose proposer | AstroSage-70B | Domain-calibrated draft prose | Gemma3 fallback already used in renovation |
| Marker repair alignment | Claude Sonnet 4.6 with strict predicate prompt | Current aligner already uses Sonnet due local Ollama saturation; reliable JSON | Atom-7B veto plus AstroSage edge review |
| Marker validation and injection | Python deterministic | Must be reproducible and auditable | None |
| Trust/control marker preservation audit | Python deterministic | Regex/AST inventory, no model needed | None |
| Coverage watchdog and alerting | Python deterministic | Ratios and thresholds are deterministic | None |
| Design/implementation review | Kun | Cross-path reasoning and failure-mode audit | HwaO coordination |

---

## 11. Acceptance Criteria

For page 57:

1. Backfilled assignments cover all 85 engine-matched claims or explicitly mark unresolved/orphan claims.
2. After 24 hours of autonomous section rewrites, visible asserted marker coverage remains at or above 80 percent of active assigned claims.
3. No accepted/consensus assigned claim is missing after repair unless marked orphan or retired with audit reason.
4. All visible claim markers are paired and frontend-parseable.
5. Unknown/control HTML comments, including trust/consensus markers, survive repair.
6. Repair jobs are version-scoped and do not read stale pre-commit content.
7. `claim_marker_runs` or a successor audit table records section-level owned, visible, repaired, missing, and rejected counts.

---

## 12. Final Position

Claim markers should be treated as a persistent data contract, not an optional stylistic output of a rewriter. The LLM can help create markers, but it should not be the only keeper of marker coverage. Store ownership in the DB, make each section rewrite responsible for its owned claims, repair markers after commit without changing prose, and let the watchdog trigger regeneration when prose no longer contains required claims.

This keeps autonomous rewriting alive while making marker coverage stable at page scale.

-- Kun
