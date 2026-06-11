# arXiv → Wiki Feed — Consolidated Design

**Owner:** Kun 🔬  ·  **Implementer:** Tori  ·  **Status:** v2.0 — 2026-06-11, consolidated authoritative design
**Supersedes:** v1.3 (2026-05-25), archived verbatim at `docs/arxiv_wiki_feed_design_v1.3_archive_20260611.md`
**Filename:** `docs/arxiv_wiki_feed_design_v1.md`

**Companion docs:**
- `docs/beat_schedule_v3.md` — Celery beat layout this pipeline plugs into.
- `docs/ollama_model_policy_v1.md` — platoon roster and capability matrix.
- `docs/platoon_overhaul_v2.md` — 2026-06 roster overhaul (Pico/Vera/Mima/Nutty/Rakon seats).
- `docs/research_ideas_design_v1.md` — forward-looking sibling (papers → hypotheses); this doc is backward-looking (papers → evidence).
- v2 design series in `~/.openclaw/workspace/Design_ArxivWikiFeed_v2_*.md` — stage-level design records synthesized here. This doc is authoritative where they disagree.

---

## 1. Goal

Route daily arXiv papers into wiki pages as **evidence**, not just newsletter items (Papa's directive, 2026-05-10: "arXiv updates should feed the wiki, not just the newsletter"). The end state is a claim on a wiki page carrying a live, audited set of supporting papers that updates as the literature moves — with precision high enough that a domain scientist reading the page never encounters a mis-attached citation.

The system is **two layers sharing one intake**:

- **Layer 1 — live classifier ingest (`arxiv_ingest`).** In production since May. Paper-level TF-IDF routing into four outcomes (`claim_evidence` / `page_extension` / `new_topic_candidate` / `unrelated`). Fast, cheap, no LLM in the classify step. Recall-oriented; precision is delegated downstream and currently leaks (§3.1).
- **Layer 2 — element-level validated feed (`arxiv_wiki_feed_v2`).** Built May–June as one-shot scripts; this doc specifies its promotion to a daily pipeline. Claim elements paired with candidate papers, filtered, coverage-materialized, validated per element, and promoted under strict gates. Precision-oriented; this is the lane that is allowed to write claim-level `Evidence` rows going forward.

Layer 1 keeps the wiki *growing* (page extensions, new-topic proposals). Layer 2 keeps the wiki *true* (claim evidence). The long-term contract: **Layer 2 becomes the only writer of claim-evidence rows**; Layer 1's `claim_evidence` handler is demoted to a candidate-feeder for Layer 2 (§7.4).

---

## 2. What Is Already Built

| Component | Status | Where |
|---|---|---|
| Daily arXiv fetch (4 cats: astro-ph.GA/CO/HE/SR, UTC 01:00) | **live** | `app/agent_loop/arxiv_fetch.py`, `tasks.py` |
| Layer 1 classifier (TF-IDF cosine; claim ≥0.45, page ≥0.50, topic ≥0.30) | **live** | `app/agent_loop/arxiv_classifier.py` |
| Layer 1 handlers (claim_evidence / page_extension / new_topic) | **live**, claim_evidence yield-collapsed | `app/services/arxiv_ingest.py` |
| Candidate build (claim element × paper pairs) | one-shot script | `scripts/arxiv_wiki_feed_build_candidates.py` |
| Retrieval filter v2 (taxonomy + per-page calibration, BRK routing) | shipped, replay-verified | `scripts/retrieval_filter_v2.py`, `config/arxiv_retrieval_taxonomy.v1.yaml`, `config/page_retrieval_calibration.galaxy-evolution.v2.yaml` |
| Claim atomization (claim → elements, 863 merged elements) | one-shot, claim-level only | `scripts/arxiv_wiki_feed_v2_atomize.py` |
| Candidate-grounded atom backfill | designed, partially run | Q2-reopen + synonym-band design (locked) |
| Element-level validator (AstroSage primary, targeted mode) | one-shot runs (db_run_id=6) | `scripts/arxiv_wiki_feed_v2_phase2_validate.py` |
| Promoter (element-aware, dedup, manifest, rollback) | designed + script | `scripts/arxiv_wiki_feed_v2_phase3_promote.py` |
| Daily periodic wiring of Layer 2 | **missing — this doc specifies it** | §7 |
| Coverage materialization as first-class stage | **missing — this doc specifies it** | §4 stage D |
| Page generalization beyond galaxy-evolution | config exists for 1 page | §6 |

Roughly 80% of Layer 2 exists as audited one-shot scripts. The missing 20% is: coverage materialization as an explicit gate, daily scheduling, and the second page config.

---

## 3. Lessons That Shaped the Architecture

These are binding constraints, each paid for with a failed or near-failed run.

1. **Claim-level paper pairing does not work.** v1 paired whole claims with papers: 1,403 pairs yielded 5–6 strict supported rows; the Tier B audit measured precision 0.20 and returned REJECT. Evidence must be judged per **claim element**, not per claim.
2. **Unfiltered retrieval leaks off-domain papers.** 53.3% of v1 candidates were wrong-subdomain. The taxonomy retrieval filter (subdomain priors + per-section profiles) fixed this: 0.0% off-domain among supported rows in db_run_id=6.
3. **`boundary_review_keep` is audit routing, never promotion authority.** BRK rows are retained as retrieval provenance; they do not enqueue to the validator by default and can never reach the promoter without independent validator approval.
4. **Missing coverage is not rejection.** db_run_id=6's dominant failure codes (`atom_missing`, `precheck_missing`, `astrosage_missing`) were pipeline backlog masquerading as validator "no" votes. The validator may only consume `coverage_ready` rows; everything else is reported as backlog, never as negative evidence.
5. **Atoms must be candidate-grounded.** Claim-only atoms attached to every retrieved paper produced 28.5% grounding (24.3% outright hallucinated anchors). Atoms are generated per `(claim, element, paper)` triple, keyed by input hashes + prompt/model versions.
6. **Lexical overlap is too permissive a gate.** Generic-token overlap (`mass`, `galaxies`) flooded Atom-7B with junk. The semantic band — nomic-embed-text:v1.5 cosine ≥ 0.50 between element text and abstract, fail-closed when embeddings are unavailable — replaced it (locked design).
7. **`validated_ready` is a deterministic aggregate, never a model label.** Models emit per-element labels (`supported`/`partial`/`missing`/`contradicted`/`needs_human`); claim-level readiness is computed by code from required-element coverage.
8. **Production runs are immutable.** db_run_id=3 (and every shipped run) is never mutated. New work creates new runs; artifact reuse is by key reference; rollback sets `evidence_status='rolled_back'`, never deletes.

Layer 1 contributed its own lessons (v1.3 §11, preserved): the ADS verify step is the leak that collapsed `claim_evidence` yield to 0/7d (recent papers aren't indexed in ADS yet — a lag problem, not a relevance problem); 90.7% `unrelated` is the honest answer for a 43-page wiki, i.e. a coverage gap, not a classifier failure; and 79 `NewPageProposal` rows sit pending because no moderation surface exists.

---

## 4. Authoritative Pipeline (Layer 2)

```
        arXiv fetch (shared with Layer 1, UTC 01:00)
                         │
   [A] Candidate build ──┤  claim elements × new papers → candidate pairs
                         │
   [B] Retrieval filter v2  keep | drop | downrank | boundary_review_keep
                         │  (taxonomy YAML + per-page calibration config)
                         │
   [C] Semantic band        nomic-embed cosine(element, abstract) ≥ 0.50
                         │  fail-closed; rejects → excluded_coverage_rows
                         │
   [D] Coverage materialization
                         │  per-(claim, element, paper):
                         │   deterministic precheck → candidate-grounded
                         │   atom backfill (Atom-7B) → AstroSage verdict
                         │  coverage_pending → coverage_ready
                         │                   | blocked_retryable | blocked_terminal
                         │
   [E] Validator            consumes ONLY coverage_ready rows;
                         │  per-element labels; deterministic claim aggregate
                         │
   [F] Promoter             dedup (claim_id, arxiv_id); batch gates (§8);
                         │  append-only Evidence rows + manifest; rollback flag
                         │
   [G] Wiki render          inline evidence badges on the claim (§5)
```

Stage contracts (binding):

- **[A] Candidate build** is deterministic and always writes its rows, even when model services are down. It never blocks on coverage.
- **[B] Retrieval filter** emits one decision per row with full provenance (`retrieval_filter_version`, decision, boundary features). Shared code contains zero page/section literals; policy lives in YAML.
- **[C] Semantic band** threshold is a per-page config knob (`min_semantic_similarity`, default 0.50). On embedding-service failure the row is excluded, not admitted.
- **[D] Coverage materialization** is the stage this doc adds as first-class. Cache keys: atoms by `(claim_id, element_id, element_text_hash, prompt_version, model_version)`; precheck and verdicts additionally by `(paper_id, paper_text_hash)`. Reuse on key match; recompute only on changed text/paper/prompt/model or explicit force. Retry policy: max 3 attempts on `model_timeout`/`transient_service_unavailable`; `malformed_input` is terminal. **Cache invalidation rule:** if the element_id set changes (e.g. merged_320 updated), clear the verdict cache first — a stale cache silently starves coverage (2026-05-31 incident: 580/3807 pairs).
- **[E] Validator** runs targeted mode only, consumes `coverage_ready`, reports `coverage_pending`/`blocked` rows as backlog counts. An `--allow-incomplete-coverage` flag exists for diagnostics and is banned from production promotion paths.
- **[F] Promoter** consumes validator-approved rows only. Coverage readiness is necessary but not sufficient. Every batch writes a manifest (inputs, gates evaluated, rows written) before any DB write.

---

## 5. Citation Display Contract

Evidence renders as **inline badges attached to the claim**, in the ClaimBlock metadata-chip row (alongside ✏️ edit and 💡 research-ideas chips):

- A 📄 evidence chip per claim, expanding to the supporting papers: first-author + year + arXiv id, each linking out, each carrying its validation label and run provenance on hover/expand.
- **No numbered superscripts** in prose. **No References section** at page bottom. The page reads as continuous review-article prose; evidence is per-claim metadata, not page chrome.
- Contradicting papers (element label `contradicted`) render in the same chip with a distinct marker — they are first-class evidence, not suppressed.
- This is per-claim inline metadata, which the WikiPageLayout §5 dissolution rule explicitly permits; page-level evidence banners or reference blocks are what that rule bans.

---

## 6. Page-Agnostic Contract

Galaxy-evolution is the **first consumer, not a special case**. Binding rules:

- Shared pipeline code (filter, band, coverage, validator, promoter) contains no page slugs, section names, or domain marker literals. All such values arrive via per-page YAML: `config/page_retrieval_calibration.<page>.v2.yaml`.
- Onboarding a second page = writing its calibration config + claim atomization run. No code changes. The second-page onboarding is itself the acceptance test for this contract (§10 step 6).
- Coverage requirements (`atom_decomposition`, `precheck`, `astrosage_verdict` required; retry/terminal policies) are page-config policy knobs over a shared mechanism.

---

## 7. From One-Shot to Daily

### 7.1 Daily task

New Celery task `arxiv_wiki_feed_daily`, chained after `fetch_arxiv_daily` completes (UTC 01:00 fetch → feed runs on its output; coexists with Layer 1's classify step, which runs inline in fetch). Steps per run: candidate build over papers ingested in the last 24 h × all onboarded pages' elements → filter → band → coverage backfill → validator → **stop before promoter** (Mode 1, §7.3). Each run gets a fresh `db_run_id`; all artifacts under a run-keyed directory.

Budget envelope per day (galaxy-evolution alone, ~50 papers/day intake): candidate pairs after filter+band historically ≲ 100/day; Atom-7B at ~1.5 s/row and AstroSage verdicts on the ready subset keep total model time well under 30 min on the Studio. The existing retry sweep slot (UTC 02:15) gains a Layer 2 sub-step: re-run `blocked_retryable` coverage rows.

### 7.2 Weekly report

Weekly digest (cron, Monday KST morning): per-page counts — attempted / coverage_ready / backlog / validator-supported / contradicted / promoted-eligible; off-domain-among-supported (must stay 0.0%); coverage backlog trend. Delivered to Papa via the normal report channel, not Discord spam.

### 7.3 Two promotion modes

- **Mode 1 (start here): auto-validate, manual-promote.** The daily task ends at a validator report. Papa (or Kun on review delegation) approves batches; promoter runs on explicit command. Stays in Mode 1 for ≥4 weeks.
- **Mode 2 (earned): budget-capped auto-promote.** Eligible only after ≥4 consecutive weekly audits at strict precision ≥0.95 on promoted rows. Caps: ≤10 evidence rows/day/page, audit sample of 10% routed to AstroSage adjudication, automatic halt + alert if any weekly audit drops below 0.95.

### 7.4 Layer 1 reconciliation

- Layer 1's `claim_evidence` handler stops inserting `Evidence` directly once Layer 2 daily is live; instead its hits are forwarded as candidate pairs into stage [A] (this also fixes the v1.3 P0 ADS-lag leak — Layer 2 does not gate on ADS indexing). Until then, the v1.3 §11.2 fix (delayed re-verify sweep for `verify_rejected` rows) remains the live mitigation.
- `page_extension` and `new_topic_candidate` lanes are untouched: they are growth lanes, out of Layer 2's scope.
- Backlog: validator runs 16–17 (the held-back rows from the BRK trim) are resolved as the first Mode 1 batches before daily wiring goes live.

---

## 8. Gates and Invariants

**Coverage gates (before any validator-rate interpretation):** 100% of validator-eligible rows attempted; ≥95% terminal-or-ready; ≤2% retryable residue; ≥80% ready among non-off-domain rows. Below the 80% bar, fix upstream — do not recalibrate the gate down.

**Promotion gates (first batch and every batch):** ≥30 deduped claim-paper rows and ≥15 distinct claims for a first page batch; audited strict precision ≥0.95; dedup on `(claim_id, arxiv_id)`; off-domain among promoted = 0 or batch halts.

**Invariants:** shipped runs immutable; append-only evidence with `evidence_status` lifecycle (`active` → `rolled_back`); manifest written before DB writes; validator never sees non-ready rows in production; BRK never promotes; `validated_ready` computed, never model-emitted.

---

## 9. Platoon Assignment

| Stage | Owner | Model/tool | Why |
|---|---|---|---|
| [A] Candidate build | deterministic Python | — | routing/provenance must be replayable and uptime-independent |
| [B] Retrieval filter v2 | deterministic Python + YAML | — | replay-equivalence tested; no model variance allowed in routing |
| [C] Semantic band | **nomic-embed-text:v1.5** (Ollama, local) | embeddings | cheap (~ms/row), local, fail-closed; no generative model needed |
| [D] precheck | deterministic Python | — | anchor/numeric overlap is string work |
| [D] atom backfill | **Pico** = `vanta-research/atom-astronomy-7b` | Atom-7B | ~1.5 s/row median; constrained JSON extraction with row-specific anchors; cheapest adequate tier |
| [D] verdict + [E] validator labels | **Vera** = AstroSage-70B | astrosage-70b | strongest local astronomy judgment; ~32 s/item, affordable at post-band volumes (≲100/day) |
| [E] adjudication audit (5–10% sample, `needs_human` triage) | **Vera** (AstroSage-70B) | audit-only | reserve the slow model for QC, not full-row work |
| Stance jury (Layer 1, downstream of evidence insert) | **Mima** = qwen3.6:35b-a3b | per platoon_overhaul_v2 | requires the API-level thinking switch: native `/api/chat` top-level `"think": false`, or compat `"reasoning_effort":"none"` — never the prompt-hack path |
| Structured-JSON fallback | **Nutty** = gpt-oss:20b | fallback | if Atom-7B degrades; verified non-thinking JSON emitter |
| [F] Promoter, aggregates, manifests | deterministic Python | — | gate evaluation must be exact and auditable |
| Banned from sync JSON paths | Rakon/Buddle (deepseek-r1 family) | — | reasoning lands in `<think>`, content arrives empty on synchronous structured calls |

All model stages run locally on the Studio (this host). No SSH wrapping — the kun agent host **is** the Mac Studio (verified 2026-06-04; TOOLS.md note).

---

## 10. Implementation Order for Tori

1. **Coverage materialization as a first-class stage** — status fields (`coverage_status`, `coverage_missing_stages`, `coverage_artifact_refs`), backfill command (input: retrieval run id; output: ready-manifest + blocked report; no promoter calls), validator entrypoint restricted to ready rows. Tests: missing-prereq row is `coverage_pending` not rejected; retryable failure doesn't mutate filter decisions; cache reuse on key match; run_id=3 fixture untouched.
2. **Resolve runs 16–17 backlog** through the new coverage stage; produce the first Mode 1 validator report for Papa.
3. **`arxiv_wiki_feed_daily` Celery task** chained after fetch; retry-sweep sub-step at 02:15; run-keyed artifacts; Mode 1 stop-point.
4. **Weekly report cron** (§7.2 counters).
5. **Layer 1 `claim_evidence` forwarding** into stage [A]; retire direct Evidence inserts from `arxiv_ingest` (keep the audit rows).
6. **Second page onboarding** (Papa picks the page) as the page-agnostic acceptance test — config + atomization only; any required code change is a contract violation to flag, not patch around.

Each step is artifact-only first, DB-wired only after Papa reviews the corresponding report (the run_id=6 pattern).

## 11. Out of Scope

Newsletter rendering; research-ideas (forward-looking) pipeline; survey-directory autowiki; NewPageProposal moderation UI (tracked as v1.3 §11.4, unchanged priority — the 79-row backlog persists); any change to council/Quality-Guard mechanics.

---

*v2.0 consolidates the v1.x live-pipeline doc (archived) with the thirteen `Design_ArxivWikiFeed_v2_*` / audit documents in the openclaw workspace. — Kun, 2026-06-11*
