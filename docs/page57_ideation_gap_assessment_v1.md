# Page 57 (Galaxy Evolution) — Research Ideation Gap Assessment v1

**Author:** Kun (analyst) · **Date:** 2026-06-12 · **Basis:** live DB reads on Mac Studio (`nebulamind` Postgres), full rendered-content read of `wiki_pages.id=57` (55,152 chars, updated 2026-06-11), frontend/backend source inspection. No sampling shortcuts — every number below is from a direct query.

**The bar (Papa's two tiers):**
- **Tier 1:** prose trustworthy enough to read without cross-checking; surfaces papers/topics he wasn't already aware of.
- **Tier 2:** page surfaces genuine research gaps Papa can convert into a pursuable research topic.

---

## 0. Verdict

| Tier | Status | One-line reason |
|---|---|---|
| Tier 1 | **NEAR-PASS, blocked by 3 mechanical defects + trust opacity** | Prose is genuinely graduate-textbook grade, but the page ships a mid-sentence truncation, and 63% of the claims a reader actually sees carry `unverified` trust. |
| Tier 2 | **FAIL — but it is a surfacing failure, not a generation failure** | The system already *generates* Tier-2 raw material (140 debated claims, 121 scored research ideas). 96% of contested claims and ~100% of research ideas never reach the rendered page. The gap machine works; the display pipe is disconnected. |

This distinction matters for what to build next: the marginal dollar goes to **wiring existing artifacts to the surface**, not to more generation loops.

---

## 1. Prose quality (Tier 1)

### 1.1 What is genuinely good
The body prose is compact, quantitative, and current — it reads like a review article, not AI filler. Specific strengths verified against the live text:

- Quantitative density is high and mostly correct-by-construction (SHMR peak ε≈20% at 10¹²M☉, KS index ~1.4, BTFR M∝V⁴ with <0.1 dex scatter, MZR offset ~0.5 dex at z=4–9).
- Contested areas are flagged *inline* in several sections (cold-stream resolution caveat "should be treated as upper limits", SFMS-scatter three-mechanism discussion, ejective-vs-preventive AGN feedback with the DESI inflow result on the preventive side). This is exactly the Tier-1→Tier-2 bridge style.
- Section-to-section segues exist and are non-formulaic. The JWST mass-tension section is an honest, multi-hypothesis treatment, not a hype paragraph.

### 1.2 Defects found (each verified in the live content)

| # | Defect | Location | Severity |
|---|---|---|---|
| D1 | **Mid-sentence truncation.** The JWST section ends `"Nitrogen-enhanced abundance"` — sentence cut dead, then the Open Questions header follows. A reader hits this and stops trusting the page. | end of "Early Massive Galaxies and JWST Discoveries" | HIGH |
| D2 | Stray `---` horizontal rule inside the High-Redshift section (between CSFRD and JWST subsections) — layout debris from a past edit. | before "Early Massive Galaxies" | LOW |
| D3 | **Duplicated content:** the MZR z=4–9 "~0.5 dex below local, O/H≈7.2–7.5" result appears verbatim-equivalent in both "Chemical Enrichment" and the JWST section. Same claim-marker triple `1758,1965,1967` is wrapped around *different text* in two different sections (SFMS scatter ¶ and Stellar Feedback ¶) — marker integrity violation. | two sections | MED |
| D4 | "Overview" cites SDSS ">700,000 galaxies… green valley <15%" with no evidence badge on the quantitative second half; a handful of similar uncited quantitative sentences exist. Minor relative to overall badge density. | Overview | LOW |

### 1.3 Trust opacity — the real Tier-1 blocker
Of the **75 claims actually surfaced** in the rendered page (claim markers), the trust mix is:

| trust_level | surfaced claims |
|---|---|
| unverified | 47 (63%) |
| consensus | 8 |
| accepted | 8 |
| debated | 6 |
| contested | 1 |
| challenged | 0 |

"Read without cross-checking" requires the *reader-visible* claims to be predominantly verified. Today the badge a reader most often encounters is `unverified` — even where the underlying statement is textbook-solid (e.g., hierarchical assembly). That is a **verification-throughput problem, not a correctness problem**: 221 of 421 live claims are unverified, and the jury/trust loop hasn't caught up to the renovated text.

**Tier 1 call:** content quality passes; the page as shipped does not, because of D1 plus the unverified-majority badge experience. Both are fixable without any new architecture.

---

## 2. Evidence coverage

Live numbers (claims excluding `parent_replaced`; evidence = `production_active`):

| trust_level | claims | with ≥1 evidence | with ≥1 evidence from ≥2024 | evidence rows |
|---|---|---|---|---|
| unverified | 221 | 114 (52%) | 15 (7%) | 310 |
| **debated** | **140** | **40 (29%)** | **27 (19%)** | 94 |
| accepted | 35 | 35 (100%) | 21 | 121 |
| consensus | 16 | 16 (100%) | 14 | 95 |
| challenged | 8 | 8 (100%) | 8 | 19 |

- Total: 775 active evidence rows; **198 (26%) from 2025–2026** — recency is real, driven by `targeted_ads_miner` (227 rows, all refereed, last added 2026-06-11) and `citation_context_mining` (75 rows, 2025–2026).
- **The inversion that hurts Tier 2:** the claims most valuable for ideation — debated ones — have the *worst* evidence coverage (29%). The literature linkage effort has flowed to consensus/accepted claims (100%) where it adds least ideation value.
- Papa-domain check: only **15 of 775** evidence rows mention DESI in title/abstract. The page cites the DESI cold-inflow result well, but DESI **BGS environmental quenching / cluster-vs-field sSFR** — Papa's own bench — is essentially unanchored. If the page should surface papers *he* doesn't know, his home survey's literature stream is the first place it must be dense.
- arXiv feed v2 state: last completed run promoted 2026-06-01; runs 16–17 (06-02) stopped at `candidates_built`. The Mode-1 daily cadence (first run tonight UTC 01:10) had not yet left a run row at assessment time — worth confirming tomorrow.

---

## 3. Gap surfacing — does Papa have to hunt manually? **Yes. Almost everything is buried.**

This is the section that decides Tier 2. Four independent disconnects, each verified:

### 3.1 Claim surfacing rate is 18%
421 live claims in the DB; **75 distinct claim IDs appear as markers** in the rendered content. The hidden 346 include:
- **134 of 140 debated claims (96%)**
- **all 8 challenged claims**

The DB section `Open Questions & Frontier Debates` alone holds 139 claims (126 contested) — research-grade statements like *"jellyfish SF suppression is driven by RPS of molecular gas, not starvation"* (8 evidence rows, latest 2026) or *"dominant ISM turbulence source at z>3 is gravitational instability, not stellar feedback"*. None of them render. The DB's claim sections and the page's headings don't even share names (9 vs 9, ~zero overlap) — the known section-drift problem means claim→prose anchoring has no stable target.

### 3.2 The Debates UI is dead — one NULL column
The frontend (`WikiPageClient.tsx`) has a full pro/con debates panel. The API (`/api/pages/galaxy-evolution/claims`) returns **`debates: 0`** because pairing requires `debate_stance`, and **all 187 claims with a `debate_topic` have `debate_stance = NULL`**. A complete product feature is dark because one column was never backfilled.

### 3.3 The research-ideas layer exists, is scored, and is invisible
- `research_ideas`: **121 ideas for page 57** (112 draft / 2 review-queue / 7 covered), avg novelty 0.82, avg feasibility 0.84, with survey combos, why-now, approach, systematics fields — this is exactly the Tier-2 artifact.
- **No frontend route exists for them** (no `research*` page in `frontend/src/app`). The only surface is the inline "⚡ open research questions" chip on ClaimBlocks…
- …and chips can only attach to *surfaced* claims: of 92 claims carrying idea anchors, **only 11 are surfaced** in the page. So ≈90% of ideas have no possible render path.
- **Quality gate needed before exposure:** the top-scored idea (novelty 0.95) refers to the *"DESI Legacy Survey of Space and Time (LSST)"* — a confabulated merge of two different surveys. Scores alone can't be trusted; ideas need a factual screen before Papa sees them.

### 3.4 The rendered "Open Questions & Future Directions" section is good but frozen
It lists 9 genuine frontier debates with citations — at coarse grain it *does* surface contested areas. But it contains **zero claim markers**, is disconnected from the live contested-claim pool and the ideas table, isn't ranked by activity/recency, and won't change when tomorrow's arXiv feed lands. It's a snapshot essay, not a living gap index.

Also noted: the contested pool itself needs dedup — claims 1949/1990/2086 are three near-identical phrasings of kinetic-vs-radiative AGN feedback at cosmic noon. Multiplicity inflates apparent debate breadth.

---

## 4. Delta to Tier 2 — what concretely is missing

**Classification: ~70% wiring/product, ~30% pipeline.** The generation side (claims, ideas, recent refereed evidence) already produces Tier-2 raw material. Ranked by leverage:

| # | Action | Type | Effort | What it unlocks |
|---|---|---|---|---|
| G1 | **Backfill `debate_stance`** for the 187 debate-topic claims (one LLM pass — Blanc or Buddle, classify pro/con per topic), then dedupe near-identical debate claims by embedding similarity. | pipeline (one-shot) | S | Turns on the already-built pro/con Debates panel. Single highest leverage-per-line in the system. |
| G2 | **Build the Open Questions section from the DB, not as static prose.** Render top-N debated claims ranked by (evidence recency × evidence count × jury activity), each with its evidence badges and any anchored ideas. Section regenerates when feed lands. | product | M | The "living gap index" — Tier 2's core surface. Eliminates manual hunting. |
| G3 | **Research-ideas review surface** (route or panel): list page-57 ideas with novelty/feasibility, anchored claims, survey combo; add a factual screen (survey-name/instrument validation against a controlled vocabulary) before display; statuses so Papa can promote/dismiss (`saved_by_papa` column already exists). | product | M | Converts 112 invisible drafts into Papa's ideation queue. |
| G4 | **Point evidence mining at debated claims.** Re-weight `targeted_ads_miner` so debated/challenged claims get priority; target ≥80% of debated claims with ≥1 post-2024 refereed row (today: 19%). Add a DESI BGS / environmental-quenching query band for Papa-domain density. | pipeline (re-aim) | S | Makes each surfaced debate decision-ready and surfaces papers in Papa's own field. |
| G5 | **Raise claim surfacing above ~60%** (today 18%): requires the section-name reconciliation between claim records and rendered headings, then a verbatim-sync/marker-embed pass. Without G5, G2 partially substitutes (it surfaces claims outside prose), so G5 can trail. | pipeline | M | Inline trust visibility for the majority of the corpus. |
| G6 | **Tier-1 mechanical fixes:** repair the truncated JWST sentence (D1), remove stray `---` (D2), dedupe the MZR paragraph and fix the reused `1758,1965,1967` marker (D3); push jury throughput on the 221 unverified claims, prioritizing the 47 *surfaced* ones (a reader-visible trust win for only 47 verifications). | pipeline | S | Closes Tier 1. |

**Sequencing recommendation:** G1+G6 first (days, mostly one-shot), G2+G3 as the next product sprint, G4 re-aim alongside, G5 last. After G1–G4, Tier 2 is testable with a concrete metric: *"Papa opens the page weekly and at least once a month exports one idea/debate into a real research note."* That behavioral metric — not a quality score — is the Tier-2 acceptance test.

---

## 5. Method appendix (for reproduction)

All queries run 2026-06-12 against local Docker Postgres (`nebulamind-postgres-1`, db `nebulamind`). Live-claim filter: `page_id=57 AND rewrite_status IS DISTINCT FROM 'parent_replaced'`; evidence filter: `evidence_status='production_active'`. Surfaced-claim set extracted from `<!--claim:...-->` markers in `wiki_pages.content` (75 distinct IDs). Frontend inspection: `frontend/src/app/wiki/[slug]/WikiPageClient.tsx` (debates panel, idea chips); API probe: `GET /api/pages/galaxy-evolution/claims` → `debates: []`. Idea anchors: `research_idea_anchors.kind='claim'` → 92 distinct claims, 11 surfaced.
