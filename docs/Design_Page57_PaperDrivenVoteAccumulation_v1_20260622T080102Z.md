# Design — Paper-Driven Vote-Accumulation Trust Model (galaxy-evolution)

- **Author:** Kun (analyst)
- **UTC:** 2026-06-22T08:01:02Z
- **Status:** DESIGN ONLY. Read-only. No DB writes, no `--apply`, no code/repo changes. All recon below was `SELECT`-only against the live DB; model list is from a live `ollama list`. Any production apply later needs Papa's explicit seed + the 2026-06-19 safety gate.
- **Dispatch:** HwaO (agent:main:main), Papa directive 2026-06-22.
- **⚠️ SUPERSEDED IN PART — see _Revision 1 — page-58-base reconciliation_ at end of doc (2026-06-22):** Papa chose **page 58 `galaxy-evolution-v2` as the base**, REVERSING the §4 Option-B recommendation. §4, §8-flag-#1, and §11-step-4 are superseded by Revision 1; §3.1's calibration line and tone-gate usage are corrected there. **§3 pipeline shape, §6, §9, §10 still stand.**
- **Papa's verbatim directive:** *"each introduction of a paper fall onto the provenance-tracked distillation so that each sentence can be staked as either adding pro/con vote count or editing the prose a little. Consequently, it doesn't need to find a evidence for each claim."*

---

## Implementation update — 2026-06-25

**Why this doc did not move during PR #20:** the first executed slice treated Page57 as design input and landed the backend foundation first. That was a sequencing miss for documentation visibility: Page57's prose/content still did not change, but the implementation status below now records what actually landed.

**Landed in PR #20 (`31a669a`, `feat: add sentence trust rollup scaffold`):**

- Added ORM coverage for the already-committed `sentence_votes` and `sentence_trust` schema.
- Added deterministic sentence-level rollup service: `sentence_votes` → `sentence_trust`.
- Added `TrustMutationService.recalculate_sentence_trust(...)` as the seam for the future dual-source trust adapter.
- Added regression coverage for one-paper-per-sentence uniqueness, migration/model type parity, zero-vote `unverified`/`mixed` behavior, single-source cap, consensus/debated/challenged branches, update-in-place, `tone_distribution`, and the service seam.

**Still unchanged / not authorized by PR #20:**

- No Page57 or Page58 public prose/content changed.
- No live DB writes, no production migrations run, no `--apply`, no staking-loop writer, no frontend badge re-key.
- The §3.2 relevance requirement for contested vetoes remains owned by the matcher/staking slice: dissent must bind to *this* sentence's proposition before it can affect trust.

**Build-order status after PR #20:** Revision 1's Step 2 is now partially complete as an app-code scaffold: the ledger/aggregate schema has ORM models and a deterministic rollup seam. The next non-destructive slice is still a `--no-apply` dry-run over page 58's 168 usable intros, after the calibration work in Revision 1 Point 2: τ_rel intro×base gold, new pairwise stance gold, and tone-tier intro-transfer gate.

**Follow-up dry-run parity slice (`feat/page57-dry-run-trust-parity`):** the Page58 `--no-apply` staking dry-run now calls the same production `project_sentence_trust(...)` projector used by `TrustMutationService.recalculate_sentence_trust(...)`. This removes the prior duplicate `trust_level(...)` logic in the dry-run script, so `would_be_sentence_trust.jsonl` will use the same zero-vote, single-source, contested-veto, tone-tier, settled-share, and trust-score semantics as the eventual persisted `sentence_trust` rows. The dry-run report also surfaces `would_be_tone_tier`, `single_source`, and `contested_veto` flags. This still performs no live DB writes and does not authorize `--apply`.

**Slice-2 calibrated dry-run parity follow-up (`feat/page58-slice2-projector-parity`):** the calibrated Page58 Slice-2 dry-run now reuses the same `project_sentence_trust(...)` projector for baseline-plus-new vote projections instead of its older local `production_sentence_trust(...)` helper. This keeps the calibrated `would_be_sentence_trust_slice2.jsonl` projection aligned with production contested-veto, single-source, tone-tier, settled-share, and trust-score semantics while remaining `--no-apply` only.

**Projector contract hardening follow-up (`harden/sentence-trust-projector-contract`):** `project_sentence_trust(...)` now exposes an explicit typed projection contract and rejects impossible source/vote count combinations at the shared projector boundary. This protects both persisted rollups and Page58 dry-run callers from silently emitting invalid `vote_count`, single-source, or contested-veto projections. The validation remains compatibility-safe for legacy carried-forward baselines where distinct source counts may be lower than historical vote totals, but it rejects votes without sources, sources without votes, negative counts, and distinct-source counts above total vote rows. This remains code/test/docs only: no live DB writes, no `--apply`, and no frontend behavior change.

---

## 0. The core inversion (and its honest tradeoff)

The stuck pipeline is a **pull** model: each wiki claim reaches OUT to arXiv for a strict per-claim support, gated by a >10% proposer≠judge batch-veto. It has sat at ~23% coverage for weeks because most claims never find a clean one-shot support, and disagreement is treated as **failure** (veto → shelve).

This design is a **push** model: papers arrive, and each stake-worthy intro sentence reaches IN to the provenance-tracked distillation and **stakes** a pro-vote, a con-vote, or a small prose edit on the wiki sentence it bears on. Trust is an **accumulation across many papers**, not a lookup. Disagreement is no longer a veto — it is **data** (a con-vote → `debated` trust). The per-claim evidence search leaves the critical path entirely (§6).

**Honest tradeoff, stated up front so no one is surprised:** this does not *instantly* beat 23%. It trades a **stuck ceiling** for a **growing floor**. On day one most sentences are single-source or unstaked, so the covered-ratio starts LOW and *rises* as the 166-and-growing intro corpus accumulates votes. The win is that coverage is no longer capped by a one-shot gate — it compounds with every ingested paper, and every number it reports is an honest tally of real paper stakes rather than a strained strict-match. If Papa expects a same-week coverage jump, that expectation should be reset now: the deliverable is an **unstuck, monotonically-growing, fully-provenanced** trust surface, not a one-shot fill.

---

## 1. Verified current state (live DB, 2026-06-22 — confirmed by me, not taken on trust)

| Fact | Page 57 `galaxy-evolution` (LIVE) | Page 58 `galaxy-evolution-v2` (FROZEN) |
|---|---|---|
| page id | 57 | 58 |
| live version | v1708 (`page_versions.id=6197`), 13,325 chars, 8 flat `##` sections, source_note *"Papa-authorized Page57 v3 max-papers apply"* (2026-06-21) | v3, 10,305 chars, 6 `##` + 21 `###` |
| claims | **721**, but max `created_at`=2026-06-20 03:15:43 = the v1706 era → **stale vs v1708** | 0 |
| covered (claims w/ ≥1 evidence) | 164/721 ≈ **22.7%** — but this ratio measures **OLD-prose claims**, not the live v1708 prose | 0 |
| `sentence_provenance` | **0 rows** | **167 rows** (61 distinct arxiv_id, 1 page_version), `tone_tier ∈ {settled,contested}`, `relationship=source_of`, `match_method=deterministic_keyword_cluster_v1`, all `tier=1`, `match_confidence=NULL` |
| `sentence_trust` | 0 | 10 rows (`trust_level ∈ {consensus,debated}`) |

**Version churn worth flagging (§4):** page 57 went v1705(53,899 chars) → v1706(55,275) → v1707(55,268) → **v1708(13,325)**. The live page **shrank ~75%** on 2026-06-21. This is load-bearing for the merge decision.

**Input stream:** `paper_intros` = 248 rows, **166 with real text** (`length(intro_text)>50`), full intros 14k–25k chars each, `source='ar5iv'`, actively fetched today. This is the push corpus.

**Vote ledgers that exist:** `votes` (6,834 rows, keyed `edit_id` — *edit* votes) and `evidence_votes` (3,159 rows, keyed `evidence_id`). **There is NO per-sentence vote ledger.** `sentence_trust` already has the *aggregate* shape (`vote_count, settled_votes, contested_votes, settled_share, trust_score, trust_level, single_source, contested_veto`) but nothing writes per-sentence votes into it yet.

---

## 2. Reuse map — what exists, what's missing (don't reinvent)

| Component | Where | Status | Role in this design |
|---|---|---|---|
| Intro ingestion (ar5iv → `paper_intros`) | `backend/app/services/intro_fetch.py` — `fetch_intro()` L82, `select_excerpt()` L121, `_strip_html()` L34 | **PROD** | Reuse as-is. The push-stream feeder. |
| Vote→trust rollup | `backend/app/services/trust_calculator.py` — `recalculate_trust()` L17 (`trust_score=0.45·E+0.35·V+0.10·T`; tiers consensus/accepted/debated/challenged/unverified) | **PROD** | Adapt to read `sentence_votes` instead of `evidence_votes`; same tiering. |
| Inline trust badges (no superscripts / no References) | `frontend/.../ClaimBlock.tsx` `TRUST_BADGE` L106 + badge span L172; `WikiPageClient.tsx` `renderWikiMarkers()` L114 (`<!--claim:IDs-->` markers); `ProvenanceChip.tsx` | **PROD** | Reuse the badge component; **re-key markers claim→sentence** (gap, §3/§7). |
| `deterministic_keyword_cluster_v1` matcher (sentence↔paper, tone_tier) | `…/parked_review_wt_20260622/backend/scripts/extraction_provenance_rebuild_phase1.py` — `classify_subject()` L168, `apply_a8_direct_term_gate()` L276, `trust_for_members()` L289 | **EXPERIMENTAL** | Productionize as the relevance-match + provenance writer. |
| Gold-locked 3-tier tone-gate (settled/accepted/contested, **macro-F1 ≥ 0.70**) | `…/galaxy_evolution_v2/tone_gold_locked_3tier…/complete_and_score.py` — `predict_mima()` L74 (runs Mima=`qwen3.6:35b-a3b` / Nutty=`gpt-oss:20b`) | **EXPERIMENTAL** | **This IS the stance classifier** for the staking decision (§3.1). Productionize. |
| Per-sentence vote ledger | — | **MISSING** | New table `sentence_votes` (§3.2, design-only). |
| Edit proposal + proposer≠judge voting | `claim_edit_proposals` (+ `claim_proposal_votes`, `votes.edit_id`) | **PROD** | Generalize target claim→sentence for the prose-edit path (§3.3). |

**Live local models confirmed installed today (Mac Studio `ollama list`):** `astrosage-70b` (AstroSage), `vanta-research/atom-astronomy-7b` (Atom-7B, 4.5 GB), `llama3.3:70b` (Blanc), `gpt-oss:120b`, `gpt-oss:20b`, `qwen3:30b-a3b-instruct`, `qwen3.6:27b/35b-a3b`, `llama3.1:8b`, and **embeddings** `qwen3-embedding:4b`, `qwen3-embedding:0.6b`, `nomic-embed-text:v1.5`. **NOT installed here:** any `deepseek-r1` (Rakon/Buddle/Nutty), `phi4` (Takji), `gemma3` (Tera) — the roster (2026-05-11) is stale on these. *(The roster also lists Kun/Rakon on Mac Pro, but my `hostname` check says this host is the Mac Studio.)*

---

## 3. The pipeline

```
paper_intros (push)                       provenance-tracked distillation (the page)
   │  intro_text                                  │  sentence_i, sentence_hash, embedding
   ▼                                              ▼
[A] split + claim-worthiness filter  ───►  [B] relevance match (embed cosine)
        (Atom-7B + embed)                         τ_rel? ── no ──► [E] emergent-structure pool (§5)
   │ yes                                          │ yes (matched sentence_i)
   ▼                                              ▼
[C] stance/tone classifier (gold-locked tone-gate, Atom-7B)
        agree ─► (a) PRO-vote     disagree ─► (b) CON-vote
        refine ─► (c) PROSE-EDIT proposal (§3.3)     low-conf ─► (d) NO-OP (abstain)
   │
   ▼
[D] sentence_votes ledger  ──► recalculate_trust() ──► sentence_trust ──► inline badge render
```

### 3.1 Staking decision — per stake-worthy intro sentence → (a)/(b)/(c)/(d)

For each arriving paper intro:

1. **Split + claim-worthiness filter (refines the directive).** Intros are 14–25k chars; most sentences are background/method, not stake-worthy. A paragraph/sentence splitter feeds **Atom-7B** a binary "is this a *finding/claim* (vs background/method)?" filter. Only finding-class sentences proceed. *This is a necessary refinement, not a contradiction, of "each sentence" — see §8 flag #2.*
2. **Embed + relevance match.** Embed each surviving intro sentence (`qwen3-embedding:4b`) and the distillation sentences; cosine-match to the nearest distillation sentence(s). If `max_cosine < τ_rel` (≈0.55) → **(d) no-op for the page**, route to the emergent pool (§5). Else carry the matched `sentence_index`.
3. **Stance classify (the gold-locked tone-gate).** Run the F1≥0.70 tone-gate on the `(intro_sentence, distillation_sentence)` pair → `{agree | disagree | refine | neutral}` + confidence:
   - `agree`, conf ≥ τ_vote (≈0.70) → **(a) PRO-vote** (+1) on that sentence.
   - `disagree`, conf ≥ τ_vote → **(b) CON-vote** (−1).
   - `refine` (relevant, adds a qualifier/number/nuance the sentence lacks; neither clean agree nor disagree) → **(c) PROSE-EDIT** proposal (§3.3).
   - conf < τ_vote OR `neutral` → **(d) NO-OP** (abstain; recorded `resolved=false`, never pollutes trust).
4. **One stake per (paper, sentence).** Dedup is mandatory (prior multi-vote-inflation incident): the ledger is `UNIQUE(page_version_id, sentence_index, sentence_hash, arxiv_id)`. Re-processing a paper **updates**, never duplicates. A single paper casts **at most one** pro OR con per sentence.

**Thresholds are calibrated, not guessed:** page 58's 167 provenance rows + its tone gold labels are the **calibration set**. Tune τ_rel and τ_vote so the gate reproduces the gold settled/contested split at F1≥0.70 before any live run.

### 3.2 Vote→trust mapping (→ `sentence_trust` → render)

- **New ledger `sentence_votes`** (mirrors `evidence_votes`; design-only): `id, page_version_id, sentence_index, sentence_hash, arxiv_id, value (+1/−1), stance_confidence, tone_tier, voter_type (model name), created_at`, `UNIQUE(page_version_id, sentence_index, sentence_hash, arxiv_id)`. Keyed on the **sentence**, not on an `evidence` row — that decoupling is precisely what removes the evidence mine (§6).
- **Rollup** = adapt `trust_calculator.recalculate_trust()` to aggregate `sentence_votes` per sentence into the **existing** `sentence_trust` columns:
  - `vote_count` = distinct-paper stakes; `settled_votes` = pro; `contested_votes` = con; `settled_share = settled/(settled+contested)`.
  - `trust_score` via the existing `E` term (pro−con, normalized); `V,T` stay 0 (Phase-1 parity).
  - `trust_level` via the existing tiers, sentence-driven: **consensus** (settled_share high, ≥3 distinct papers, 0 con) · **accepted** (net-pro, modest volume) · **debated** (both pro and con present, mid-band share) · **challenged** (net-con) · **unverified** (too few stakes).
  - `single_source=true` when 1 paper → **caps trust_level at a floor** (reuse the page-57 "single-support ≤ reported" rule). Trust *earns up* as more papers stake.
  - `contested_veto` fires only when ≥2 **independent** papers con a sentence the prose states as settled **AND** the dissent contests *this* sentence's proposition — apply the **relevance gate** from the prior §14 attribution-leak finding (keyword-adjacent dissent must not veto). Veto caps the level at `debated`, never silently flips to a fabricated debate.
- **Render:** reuse the production `TRUST_BADGE` inline component — color-coded badge after each sentence, click → `DebateEvidencePanel` listing the pro/con papers. **NO numbered superscripts, NO bottom References section** (Papa 2026-05-21). The only change is the marker key: sentence-level spans instead of `<!--claim:IDs-->` (§7 gap).

### 3.3 Prose-edit path (small edit, proposer≠judge, re-anchors provenance)

1. **Propose.** On a `refine` stake, **AstroSage-70B** drafts a **minimal** diff to the one sentence (bounded: single-sentence scope, ≤~25% token change; add a qualifier / sharpen a number / fold in a contested nuance), grounded in the intro sentence. Recorded via the existing proposal machinery (`claim_edit_proposals` shape generalized to a sentence target: `original_text, new_text, arxiv_evidence, evidence_summary, status, votes_approve/reject`). Rate-limited: **≤1 edit per sentence per cycle**; large rewrites are out of scope (those are a separate re-synthesis).
2. **Judge (proposer ≠ judge).** A **different** panel votes approve/reject via `claim_proposal_votes`/`votes`: **Blanc (`llama3.3:70b`) + `gpt-oss:120b` + Atom-7B** (astronomy-accuracy check) — none of which drafted it. Commit only on majority-approve with no higher-confidence credible reject. **`claude -p` is the tie-breaker ONLY** (capped, no metered key). This is the *only* place proposer≠judge tension survives, and it is bounded to small edits — it is no longer the whole-coverage gate.
3. **Re-anchor on commit.** A committed edit → new `page_version` (version bump) + new sentence text → **new `sentence_hash`**. Provenance is carried, not lost, using the **existing** `parent_sentence_provenance_id` column: the post-edit sentence row points to its pre-edit parent. `sentence_trust` re-keys to the new hash and **carries accumulated votes forward** when the edit is a refinement; only a proposition-changing edit re-opens votes for re-evaluation. The schema already has exactly the columns (`sentence_hash`, `parent_sentence_provenance_id`) this needs.

---

## 4. Merge plan — page 57 (live prose, no provenance) vs page 58 (provenance, frozen)

**Recommendation: Option B — re-provenance page 57's live prose; keep page 58 as the calibration/gold reference. NOT a promotion of 58 onto 57.**

| | **Option A — promote 58 onto 57** | **Option B — re-provenance 57 (recommended)** |
|---|---|---|
| Substrate | page 58's synthesis (has 167 provenance rows) becomes live | page 57's live v1708 prose stays; build its `sentence_provenance` from zero via the matcher |
| Pro | provenance already exists | no user-facing regression; provenance is built for the prose people actually see; substrate-agnostic model just needs *a* distillation + provenance |
| Con | page 58 is the cut Papa **rejected 2026-06-17 as "not a wiki" (too thin)**; promoting it live regresses breadth | matcher must run on un-provenanced prose → some **orphan sentences** (no paper match → `unverified`), which is honest, not a bug |

**Why B:** the provenance/vote model is a **trust layer**, not a content model — it should attach to whatever prose is canonical, and the canonical, featured page is 57. Page 58's value is its **emergent sections + tone gold labels** (the calibration set, §3.1/§5), which B *keeps and uses* rather than discarding. Building provenance for 57's prose is cheap (the deterministic matcher is reused) and low-regret.

**The one hard dependency (flag #1, §8):** page 57's v1708 **shrank from 55k→13k chars on 2026-06-21**, and its 721 claims predate it (stale). Before we spend a matcher pass provenancing v1708, **Papa must confirm v1708 is the intended canonical prose** and not a candidate to revert to the richer v1705/v1706. *Re-provenancing prose that then gets reverted wastes the pass.* If Papa intends the richer prose, re-provenance that version instead — the design is identical, only the substrate version differs.

---

## 5. Emergent structure (sections = OUTPUT of clustering, per Papa 2026-06-18)

The distillation **grows from the push stream**, it is not a fixed taxonomy:

- The **no-op / no-match** intro sentences from §3.1-step-2 (high-quality findings that fit *no* existing distillation sentence) accumulate in an **emergent pool** with their embeddings.
- Periodically, **cluster the pool** (`qwen3-embedding:4b` vectors + deterministic agglomerative/HDBSCAN — no LLM). A cluster that crosses a density+size threshold = a topic the corpus is converging on that the page does not yet cover.
- A mature cluster → **AstroSage-70B** drafts a new distillation sentence (or a new `###` subsection) for it; it enters the page **born with provenance**: its founding cluster papers are its initial stakes (`single_source=false` if ≥2; trust earns up from there).
- **Section taxonomy is therefore discovered**, never mirrored from 57's 8 fixed `##` sections — exactly Papa's 06-18 reshape call. Page 58's existing emergent 6+21 layout is the **reference** for what clustered structure looks like, not a template to copy.

This is the growth engine that replaces per-claim evidence search: the page expands where *papers actually concentrate*, not where a claim-list told it to look.

---

## 6. Why this removes the evidence mine (per-claim strict-support search off the critical path)

| | OLD (pull, stuck) | NEW (push, this design) |
|---|---|---|
| Unit of work | a wiki **claim** | an arriving **paper-intro sentence** |
| Direction | claim → SEARCH arXiv for strict per-claim support | paper → STAKE onto the sentence it bears on |
| Disagreement | **veto** (>10% proposer≠judge → batch reject → shelve) | **data** (a con-vote → `debated` trust) |
| Coverage driver | strict one-shot match per claim (hard ceiling ~23%) | accumulation across 166-and-growing intros (growing floor) |
| `arxiv_wiki_evidence_candidates/validations` + gpt-oss strict-support validator | **on the critical path** | **off it** — optional deep-verify lane for high-stakes sentences only |

The per-claim search is gone because **trust no longer originates from a lookup**. It originates from the tally of papers whose intros staked the sentence. The batch-veto that froze coverage is structurally absent: there is no batch and no veto — only per-sentence pro/con accumulation, with disagreement rendered as `debated` rather than rejected. The old mine can persist as an *opt-in* audit for a handful of flagship sentences, but **coverage and trust are computed without it**.

---

## 7. Coverage / trust as a RATIO (Papa standing directive)

Report three ratios, never absolute row counts:
- **Provenance coverage** = `distillation sentences with ≥1 resolved stake / total distillation sentences`. Starts LOW after the first re-provenance pass (orphan sentences = honestly `unverified`) and **rises monotonically** as intros accumulate.
- **Settled share** = `Σ settled_votes / Σ (settled+contested) votes` across staked sentences — the page's overall agreement temperature.
- **Trust-level distribution** = fraction of staked sentences at consensus / accepted / debated / challenged. This is the headline health signal, reported as percentages.

Every report states the page_version it was computed against (the ratio is meaningless without it, given the v1708 churn).

---

## 8. Flagged ambiguities / infeasibilities (per dispatch — not papered over)

1. **Substrate version (BLOCKING, §4):** v1708 shrank 55k→13k on 06-21 and its claims are stale. Confirm with Papa that v1708 is canonical before provenancing it, else point the matcher at the intended richer version. *Cheapest possible question; highest-leverage answer.*
2. **"Each sentence" granularity:** not every intro sentence should vote — intros are mostly background/method. The design adds an Atom-7B claim-worthiness pre-filter so only findings stake. This **refines** the directive (prevents noise votes); confirm Papa accepts that only finding-class sentences cast stakes.
3. **Cold-start = honest-but-low trust:** brand-new and orphan sentences are `single_source`/`unverified` until papers accumulate. Coverage% starts low and grows — this is the model working, not failing. If a fast headline number is needed, this model will disappoint at first; set expectations (§0).
4. **Sentence-keyed rendering gap (frontend work):** the production badge renderer is claim-keyed (`<!--claim:IDs-->`); per-sentence trust needs a sentence-keyed marker + render path. Reusable badge component, new keying. Tori-scoped.
5. **New `sentence_votes` ledger required:** no per-sentence vote table exists today; the design proposes one (no DB write here).
6. **Vote-inflation guard is mandatory:** enforce `UNIQUE(page_version, sentence, arxiv_id)` so one paper = one stake per sentence (prior inflation incident).
7. **`contested_veto` relevance-gate:** reuse the existing column but bind the dissent to *this* sentence's proposition (prior §14 attribution-leak), so keyword-adjacent papers can't manufacture a debate.

---

## 9. Platoon Assignment (every periodic/real-time job → owner model + why)

| Job (cadence) | Owner model (host) | Why — capability · cost · speed |
|---|---|---|
| Intro ingestion ar5iv → `paper_intros` (periodic) | **No model** — `intro_fetch.py` HTTP (Tori) | Deterministic fetch+cache; free. Already production. |
| Sentence split + **claim-worthiness filter** (real-time per paper) | **Atom-Astronomy-7B** (Studio, 4.5 GB) | Fast astronomy triage is its exact role; ~166 papers × ~100 sentences = high volume → needs the cheap always-on scorer. |
| Embed intro + distillation sentences (real-time) | **`qwen3-embedding:4b`** (Studio, 2.5 GB); `nomic-embed-text` fallback | Embedding-only, no generation; tiny, fast, local. |
| Relevance match (cosine) | **No model** — vector search | Deterministic; free. |
| **Stance/tone classifier** = staking a/b/c/d (real-time, the gold-locked tone-gate) | **Atom-Astronomy-7B** primary; **Mima (`qwen3:30b`) / `gpt-oss:20b`** as the gold-locked escalation per the F1≥0.70 tone-gate | Per-pair astronomy classification at volume (~thousands of pairs) → Atom-7B default; the V2 tone-gate is gold-locked on Mima/gpt-oss:20b for borderline escalation. |
| Prose-edit **drafter** (refine class only, bursty) | **AstroSage-70B** (Studio, 42 GB) | Astronomy prose default; low volume (only refine sentences). |
| Prose-edit **judge panel** (proposer≠judge) | **Blanc (`llama3.3:70b`) + `gpt-oss:120b` + Atom-7B**; **`claude -p` tie-break ONLY (capped)** | Judges must differ from the AstroSage drafter; multi-family avoids correlated blind spot. claude -p is the bounded tie-break, no metered key. |
| Emergent-structure clustering (periodic) | **`qwen3-embedding:4b`** + deterministic clustering; **AstroSage-70B** drafts new sentence for a mature cluster | Vectors+clustering need no LLM; only the final draft needs astronomy prose. |
| Vote→trust rollup `sentence_votes`→`sentence_trust` (periodic) | **No model** — adapted `recalculate_trust()` (Tori) | Deterministic SQL; free; reuse production rollup. |
| Pre-apply safety / exit-gate (before ANY live write) | **Kun** (Claude Opus, analysis) | Per 06-19 incident: provenance/trust correctness + Papa seed required; no model self-certifies a live apply. |

**RAM/co-residency (from roster, validated against today's install):** Atom-7B (5 GB, pin always-on) + `qwen3-embedding` (2.5 GB) + **one** 70B fits the Studio comfortably; **never co-run AstroSage-70B + Blanc** (two 70Bs thrash) — serialize the draft (AstroSage) and judge (Blanc) phases of the edit lane. The high-volume staking loop (Atom-7B + embeddings) is light and runs continuously; the 70B edit lane is bursty and serialized. **Rakon (`deepseek-r1:671b`, Mac Pro) is intentionally unused** — it is cross-machine, exclusive (404 GB), and returns empty `content` on structured JSON; the bounded tie-break is `claude -p`, not Rakon.

---

## 10. No-paid-API / containment

- Ingestion, split, claim-filter, embedding, relevance match, stance classify, edit drafting, edit judging, clustering, and trust rollup all run on **local models or no model**. The single non-local touch is the **`claude -p` edit-tie-break**, capped and **subscription-only** — **no `NM_ANTHROPIC_API_KEY`, no metered Anthropic** anywhere in the loop.
- This design authorizes **no DB write and no apply.** Building `sentence_provenance`/`sentence_votes`/`sentence_trust` for real, and any live render swap, require Papa's explicit seed + the 2026-06-19 safety gate, with Kun as the pre-apply exit-gate.
- Every future artifact stamps `paid_lane_touched=false` / `local_only=true`; the exit-gate asserts them.

---

## 11. Build order for Tori (one concrete path; each step shippable)

1. **Confirm substrate** (Papa: v1708 vs richer revert — §8 #1). *Blocks step 4 only.*
2. `sentence_votes` table + generalize the proposal target to sentences (migration; no backfill).
3. Productionize the **matcher** (`extraction_provenance_rebuild_phase1.py`) and the **tone-gate** (`complete_and_score.py`) as services; calibrate τ_rel/τ_vote on page 58 gold to F1≥0.70.
4. Re-provenance the confirmed page-57 substrate (matcher pass) → populate `sentence_provenance` (dry-run artifact first; Kun gate; Papa seed).
5. Wire the staking loop (Atom-7B classify → `sentence_votes` → adapted `recalculate_trust()` → `sentence_trust`) over the 166 intros (dry-run ratios first).
6. Frontend: re-key the badge renderer claim→sentence (§7 gap).
7. Emergent pool + clustering (§5) as the growth engine.
8. Each live write is a separate Papa-seeded, Kun-gated apply — never a blind batch.

— Kun

---

## Revision 1 — page-58-base reconciliation (2026-06-22)

- **Author:** Kun (analyst) · **Dispatch:** HwaO, Papa decision FINAL.
- **Scope:** bounded reconciliation, **NOT a redesign**. **§3 pipeline shape, §6 (evidence-mine removal), §9 Platoon, §10 containment STAND unchanged.** Read-only; no DB writes, no `--apply`; local-only; `claude -p` tie-break-only, no `NM_ANTHROPIC_API_KEY`; coverage as RATIO.

**Decision reconciled:** base = **page 58 `galaxy-evolution-v2`** (id 58), NOT page 57 — **this reverses §4's Option-B recommendation.** Papa weighed my "page 58 was rejected 06-17 as not-a-wiki" con and overrode it: page 58's *native* provenance + emergent structure outweigh the thinness, because re-provenancing page 57 (Option B) RECONSTRUCTS provenance via a guessing matcher (orphans + misattribution), whereas page 58 already HAS it, built and internally consistent. **On the merits I concur with the override**: it removes the single largest risk I had *accepted* in v1 (the matcher's guesswork; v1 §4 con-column + §8 flag #1). The cost is breadth, which the push model is built to grow (§5). Recording the reversal honestly, not defending v1.

### Verified live state grounding this revision (SELECT-only, 2026-06-22)

| Fact | Measured |
|---|---|
| page 58 | id 58, slug `galaxy-evolution-v2`, 10,305 chars, updated 2026-06-18 |
| `sentence_provenance` (page 58) | **167 edges over 10 DISTINCT sentences**, 61 distinct arXiv, 1 page_version ⇒ provenance is **deep (~16.7 papers/sentence) but narrow (10 sentences)** |
| `sentence_trust` (page 58) | **10 rows = those 10 sentences**; trust_level **5 consensus / 5 debated**; keyed `(page_version_id, sentence_index)` |
| push-model columns present | `parent_sentence_provenance_id`, `sentence_hash` (re-anchor on edit); full vote rollup on `sentence_trust` |
| `paper_intros` | 250 rows, **168 with usable `intro_text`** (HwaO's "166 intros" ≈ this set, ±2 from the len>50 threshold) |
| tone gold (calibration) | 94 Papa-adjudicated rows; labels **accepted 60 / debated 23 / consensus 9 / challenged 2**; each is a **single `assertion_text` + `tone_label`** drawn from a **paper** (arxiv_id), not wiki prose, not a pair |

### Point 1 — §4 + build order → page-58-base

- **§4 is superseded.** Base = page 58. Its existing **167 `sentence_provenance` + 10 `sentence_trust` rows ARE the seed state** the staking loop accumulates onto. The 168 usable `paper_intros` stake **new** pro/con/edit votes onto those already-provenanced sentences (+ spawn emergent new sentences for no-match intros — §5 unchanged).
- **§11 step 4 (re-provenance page 57 via matcher) is DROPPED — moot.** Page 58 already has provenance; nothing to reconstruct. **This deletes the deterministic-keyword matcher from the dev path entirely**, and with it the orphan/misattribution risk. §11 step 3 reduces to productionizing the **tone-gate only** (the matcher resurfaces, if ever, only at deferred go-live for page 57 — Point 3).
- **§8 flag #1 (v1708 substrate) is CLOSED** — substrate is resolved; the v1708-vs-revert question no longer blocks the dev path.
- **Honest seed framing (ratio, not raw):** breadth today = **10 provenance-bearing sentences**; the 28 headings are markdown chrome around them. Sentence-level split = **5/10 consensus, 5/10 debated**. The push model's job is to **grow the denominator** (emergent pool → new sentences) and **deepen per-sentence vote counts**; coverage is the moving ratio (§7), never a raw count, and it starts narrow-but-honest by design (§0 tradeoff stands).

### Point 2 — calibration methodology (the real question the flip creates)

I measured the overlap the flip worries about, **at the paper level**:

- **tone-gold ∩ page-58-base papers = 56 / 64 (88%)** — calibration corpus and operating **base** are nearly the *same papers*.
- **tone-gold ∩ `paper_intros` papers = 4 / 64 (6%)** — calibration corpus is **essentially disjoint from the 168 incoming intros that actually cast votes.**

So the circularity is **partial, and it sits on the calibration↔base axis, not the calibration↔operate axis.** The cure follows from *which side varies at operate time*. The staking decision is really **three** classifiers, and the 94-row gold only covers one of them — so I split the methodology three ways (this **corrects v1 §3.1 step 3**, which leaned on the "tone-gate" for the pro/con *sign* the gold does not calibrate):

1. **Relevance — "does the intro bear on this base sentence?" (τ_rel, intro×base pair).** The genuinely *shifted* threshold. Do **NOT** set τ_rel from page-58's internal sentence↔own-source-paper pairs (the 56-paper in-sample corpus — wrong distribution). The base is only **10 sentences**, so the operating pair space is **fully enumerable** (168 × 10 = 1,680). Build the gold on that real distribution: sample a balanced **~80–120 (intro × base) pairs**, panel-label *bears-on / not*, **split BY INTRO PAPER** (no paper in both halves), tune τ_rel on the tune split, **ship the threshold clearing F1 ≥ 0.70 on the held-out validate split.** The 10 base sentences appear in both halves as fixed targets — correct, they *are* the fixed target set; the side that varies in production (intros) is held out.
2. **Stance direction — "does it support or contradict?" (the pro/con SIGN). ⚠️ NO existing gold.** This is the **highest-stakes** output (it sets the vote sign → `debated`/`challenged`) and the **94-row tone gold does NOT calibrate it** — that gold labels *single-assertion certainty*, not pairwise agree/disagree. Build a **small pairwise stance gold**: ~60–100 (intro-assertion vs base-sentence → supports / contradicts / neither) pairs from the operating intro×base space, panel-labeled, `claude -p` tie-break (capped), **F1 ≥ 0.70 held-out, split by intro paper.** *Flagging this as a real gap rather than papering over it — it is exactly the part not to let Tori improvise.*
3. **Tone tier — certainty of the intro assertion (single-assertion).** The existing **94-row gold calibrates THIS** task; it operates on intro assertions that are **94%+ paper-disjoint** from the gold → **not circular.** Keep it — but **GATE SHIP on an intro-domain transfer sample** (the gold is environmental-quenching-weighted and class-imbalanced, `challenged` n=2): draw **40–60 finding-class assertions from the actual incoming intros** (operating distribution, NOT the gold), panel-label locally, require **macro-F1 ≥ 0.70 on that held-out sample**; if a rare class underperforms, expand the gold *for that class only*. **Do not tune on the transfer sample — only gate.**

**Principle I'd defend to Tori:** *calibrate and report on the side that varies at operate time, and never ship on calibration-set F1.* This **supersedes the §3.1 line** ("page 58's provenance rows + tone gold are the calibration set… reproduce the gold split at F1≥0.70"), which under the flip would have tuned on the operating base. The recommendation is grounded in the measured **88% / 6%** overlaps, not a generic "hold out 20%."

### Point 3 — go-live path (DEFERRED — registered, not designed)

Page 58 is the **development base**; the public swap onto the live `galaxy-evolution` (page 57) slug is a **separate, later, Papa-seeded, Kun-gated apply** — not designed here. Two known downstream snags registered so they are not a surprise: **(a) the page-57 PUT canonicalizer block** — `math_dollar` / `bare_tex` / `math_html_unsafe` rejections mean the API PUT path fails on that slug and only raw-SQL writes land (corroborated by the live `wiki_pages.content_canonicalize_failed_at` / `…_failure_reason` columns); the eventual swap must pre-canonicalize the v2 content or seed via raw SQL under the Kun gate. **(b) the slug question** — does v2 content *move onto* the `galaxy-evolution` slug, or does the frontend *route `galaxy-evolution-v2` as primary*? Both viable; the choice is deferred to the go-live change. No swap design now.

### Point 4 — flag #2 default confirmed

**Only finding-class intro sentences vote** (the Atom-7B claim-worthiness pre-filter, §3.1 step 1) — confirmed consistent with the rest of the pipeline; HwaO's default stands unless Papa overrides. Effect: of the 168 usable intros, each is split and claim-worthiness-filtered first; only finding-class sentences proceed to relevance + stance. This is the necessary refinement of Papa's "each sentence" (§8 flag #2), not a contradiction of it.

### Net effect on build order (§11)

1 (substrate) → **resolved** (page 58). 2 (`sentence_votes` table) → stands. 3 → **tone-gate only**, plus the **three-target calibration above** (τ_rel intro×base held-out gold; a **new** pairwise stance gold for the pro/con sign; tone-tier gated on an intro-transfer sample). 4 (page-57 matcher) → **dropped** (moot; resurfaces only at deferred go-live). 5 (staking loop over the 168 intros onto **page 58**) → stands = the first `--no-apply` dry-run slice. 6 (sentence-keyed render), 7 (emergent pool), 8 (each write Papa-seeded + Kun-gated) → stand.

**Next:** Tori's first `--no-apply` dry-run = `sentence_votes` table + staking loop over the 168 intros onto page 58 → trust ratios; **Kun exit-gates that output** (no write, no seed authorized here).

— Kun (Revision 1)
