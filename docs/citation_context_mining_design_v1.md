# Citation Context Mining (CCM) — Design v1

**Author:** Kun (analyst)
**Date:** 2026-06-07
**Status:** Draft for HwaO review → Tori implementation
**Live grounding:** Read against the local NebulaMind repo on Mac Studio (`Duhoui-MacStudio.local`) on 2026-06-07. Verified paths and facts are cited inline. Empirical DB snapshot at read time: `claims` = 1075 rows (unverified 333, debated 314, accepted 351, consensus 41, challenged 34, contested 2); `claim_type` established 733 / debate 342; `evidence` = 11,922 rows, of which 11,468 carry `ads_bibcode`. ADS token present in `settings.ADS_API_KEY` (len 40, prefix `dEtX…`).

---

## 0. Reading Guide & Relationship to Existing Designs

This document specifies a new ingestion pipeline. It deliberately reuses existing machinery and does **not** fork parallel structures. Before implementing, Tori must hold three sibling designs in view:

- `docs/dynamic_citations_design_v1.md` (2026-06-07, Kun) — owns the `<!--cite:N-->` prose marker and `page_citation_links` join table. **CCM does not touch prose or markers.** CCM operates one layer below: it manufactures `evidence` rows. If a CCM-linked paper later needs an inline marker, that is dynamic-citations' job, not CCM's.
- `docs/jury_system_upgrade_v1.md` (2026-06-06) and `docs/platoon_realignment_v2.md` (2026-06-07) — own the 3-juror stance jury and the Pico/Mima/Nutty-Heavy platoon. **CCM reuses the jury contract**, but introduces a cheaper Pico-only fast path for the high-volume introductory-citation case (justified in §6 and §9).
- `docs/trust_calibration_design_v1.md` and the live `app/services/trust_calculator.py` + `app/routers/claims.py:recalculate_trust_v2` — own the E/V/T/H trust score and the bucket thresholds. **CCM changes no trust code.** It only feeds `supports` evidence into the existing recalculation, and §7 proves why that is sufficient — and why it is in fact the *only* way to legitimately green these claims.

The single most important architectural claim of this document, stated up front so reviewers can attack it directly:

> **CCM does not invent a new trust pathway. It supplies the missing input — recent, peer-reviewed, jury-approved `supports` rows — that the existing v2 trust function already requires for Consensus but cannot currently obtain for baseline historical claims, because nobody writes new papers re-proving textbook facts. We harvest the *introductions* of papers that build on them instead.**

---

## 1. Problem Statement

### 1.1 The structural gap

NebulaMind grounds every wiki assertion in a `claims` row whose `trust_level` is recomputed by `recalculate_trust_v2` (`app/routers/claims.py:114`). The Consensus (green) bucket requires (verified against live source):

```python
elif (TS >= settings.TRUST_CONSENSUS_MIN          # 0.75
      and n_supports >= settings.TRUST_CONSENSUS_MIN_SUPPORTS   # 3
      and n_challenges == 0):
    new_level = "consensus"
```

For an empirically *settled* claim — e.g. *"White & Rees (1978) established that gas cools radiatively inside dark-matter halos"* or *"SDSS (Strateva et al. 2001 / Blanton et al. 2003) revealed galaxy color bimodality"* — this gate is currently unreachable, for two compounding reasons:

1. **Sparse evidence.** These claims sit at 1–2 `evidence` rows. `n_supports >= 3` never trips. They are stuck at `unverified` (gray) or, at best, `accepted`.
2. **The freshness floor actively demotes them.** Even if we manually attached three 1978–2003 papers, the v2 freshness floor (`app/routers/claims.py`, verified) fires:

```python
if (new_level == "consensus" and sup_years
        and (datetime.utcnow().year - max(sup_years)) > settings.FRESHNESS_FLOOR_YEARS):   # 10
    cutoff = datetime.utcnow() - timedelta(days=settings.FRESHNESS_FLOOR_NEW_EVIDENCE_DAYS)  # 90
    recent = any(e.created_at >= cutoff for e in evidence)
    if not recent:
        new_level = "accepted"   # demoted out of green
```

So old supporting papers alone are mathematically *insufficient*: the only supports are >10 years old and no evidence was added in the last 90 days. The claim is forced back to `accepted`. The temporal `T` component (`-0.05 * (years_since - DECAY_FREE_YEARS)/5`, capped at `-DECAY_MAX_PENALTY = 0.30`) compounds the drag on `TS`.

**The trust machine is behaving correctly.** A claim whose entire evidentiary support is decades old, with zero recent corroboration, *should* be flagged for re-confirmation. The defect is not in the trust math — it is that we are not feeding the machine the recent corroboration that demonstrably exists in the literature.

### 1.2 Where the recent corroboration actually lives

Nobody publishes *"We hereby re-confirm that gas cools in halos (White & Rees 1978)."* But thousands of 2020–2026 papers open their **introduction** with sentences such as:

> *"Following the standard radiative cooling framework established by White & Rees (1978), baryons condense at the centres of dark-matter halos…"*

That sentence is a recent (`year >= 2024`), peer-reviewed, on-topic act of scientific endorsement of the seminal claim. It is exactly an E-component `supports` signal, and — critically — its **recency defeats both the temporal decay and the freshness floor**. Three such 2024–2026 citing papers per claim produce `n_supports >= 3`, `n_challenges == 0`, recent `created_at`, recent `sup_years` → green, stably.

CCM is the pipeline that finds those introductory citation contexts, classifies them, and writes them as `supports` evidence.

### 1.3 Scope boundary (what CCM is NOT)

- CCM is **not** a general citation-graph importer. It runs only against a curated allow-list of **seminal claims** (§2). Indiscriminate citation import would flood `evidence` with low-relevance rows and corrupt trust scores.
- CCM does **not** classify a paper's *findings*. It classifies whether the *introductory citation context* is a standard supportive/background invocation of the seminal work. A modern paper that cites White & Rees (1978) in order to *challenge* it is routed to `challenges`/`ABSTAIN`, never silently to `supports` (§6.4). This guard is what keeps CCM from manufacturing false consensus.
- CCM writes **no prose** and edits **no wiki page content**. It only inserts `evidence` rows and lets the existing `recalculate_trust_v2` do its job.

---

## 2. Stage 1 — Seminal Claim Mapping

### 2.1 Goal

Produce a curated, auditable registry that maps each baseline historical/theoretical claim to its **canonical source paper(s)**, expressed as ADS bibcodes (primary key for citation querying). This registry is the *only* entry point to the pipeline; nothing runs without an explicit seminal mapping.

### 2.2 Why a new table rather than overloading `claims`

`claims` already carries `claim_type ∈ {established, debate}` (live values confirmed: 733 established, 342 debate). "Seminal" is **not** a third claim_type — a seminal claim is still `established`; seminality is an orthogonal annotation plus a bibcode binding. Overloading `claim_type` would (a) break the autowiki proposers that branch on `claim_type == "established"` (e.g. `proposers.py:1832`) and (b) lose the bibcode binding. So we add a dedicated mapping table.

### 2.3 New table: `seminal_claim_map`

```sql
CREATE TABLE seminal_claim_map (
    id                  SERIAL PRIMARY KEY,
    claim_id            INT NOT NULL REFERENCES claims(id) ON DELETE CASCADE,
    canonical_bibcode   VARCHAR(30) NOT NULL,      -- ADS bibcode, e.g. '1978MNRAS.183..341W'
    canonical_label     VARCHAR(120) NOT NULL,     -- human key, e.g. 'White & Rees 1978'
    canonical_doi       VARCHAR(100),              -- optional cross-ref
    canonical_arxiv_id  VARCHAR(30),               -- usually NULL for pre-2000 papers
    topic_keyphrases    TEXT,                      -- JSON array; on-topic gate terms (see §2.6)
    enabled             BOOLEAN NOT NULL DEFAULT TRUE,
    added_by            VARCHAR(40) NOT NULL DEFAULT 'manual',  -- 'manual' | 'kun_audit' | agent name
    notes               TEXT,
    created_at          TIMESTAMP DEFAULT NOW(),
    updated_at          TIMESTAMP DEFAULT NOW(),
    UNIQUE (claim_id, canonical_bibcode)
);

CREATE INDEX ix_seminal_claim_map_claim    ON seminal_claim_map(claim_id);
CREATE INDEX ix_seminal_claim_map_bibcode  ON seminal_claim_map(canonical_bibcode);
CREATE INDEX ix_seminal_claim_map_enabled  ON seminal_claim_map(enabled) WHERE enabled;
```

A claim may map to several seminal bibcodes (e.g. color bimodality → Strateva 2001 *and* Baldry 2004); one row per `(claim_id, bibcode)`. The `UNIQUE` constraint blocks duplicate mappings.

SQLAlchemy model — new file `app/models/seminal.py`, registered in `app/models/__init__.py`:

```python
# app/models/seminal.py
import datetime as dt
from sqlalchemy import ForeignKey, String, Text, Boolean, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class SeminalClaimMap(Base):
    __tablename__ = "seminal_claim_map"
    id: Mapped[int] = mapped_column(primary_key=True)
    claim_id: Mapped[int] = mapped_column(ForeignKey("claims.id", ondelete="CASCADE"), index=True)
    canonical_bibcode: Mapped[str] = mapped_column(String(30), index=True)
    canonical_label: Mapped[str] = mapped_column(String(120))
    canonical_doi: Mapped[str | None] = mapped_column(String(100), nullable=True)
    canonical_arxiv_id: Mapped[str | None] = mapped_column(String(30), nullable=True)
    topic_keyphrases: Mapped[str | None] = mapped_column(Text, nullable=True)   # JSON array
    enabled: Mapped[bool] = mapped_column(Boolean, default=True, server_default="true")
    added_by: Mapped[str] = mapped_column(String(40), default="manual", server_default="manual")
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[dt.datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
```

### 2.4 Seeding the registry

Two complementary seeding paths:

**(a) Curated YAML seed (authoritative, human-reviewed).** A checked-in file `backend/data/seminal_claims.yaml` is the source of truth for the initial batch. Kun authors it; Papa/HwaO review. Example:

```yaml
# backend/data/seminal_claims.yaml
- label: "White & Rees 1978"
  bibcode: "1978MNRAS.183..341W"
  doi: "10.1093/mnras/183.3.341"
  match_claims:
    - page_slug: "galaxy-formation"
      text_contains: "cool"           # disambiguator within page
  keyphrases: ["radiative cooling", "dark matter halo", "gas condensation", "hierarchical"]

- label: "Strateva et al. 2001"
  bibcode: "2001AJ....122.1861S"
  doi: "10.1086/323301"
  match_claims:
    - page_slug: "galaxy-formation"
      text_contains: "bimodal"
  keyphrases: ["color bimodality", "red sequence", "blue cloud", "SDSS"]

- label: "Springel et al. 2005"        # Millennium Simulation
  bibcode: "2005Natur.435..629S"
  doi: "10.1038/nature03597"
  match_claims:
    - page_slug: "galaxy-clusters"
      text_contains: "simulation"
  keyphrases: ["N-body simulation", "large-scale structure", "halo merger tree"]
```

A loader script `scripts/ccm_seed_seminal_map.py` resolves each `match_claims` entry to a concrete `claim_id` (join `claims` → `wiki_pages` on `page_slug`, filter `claims.text ILIKE '%text_contains%'`), validates the bibcode against ADS (one `ads_lookup` call each, reusing `app.services.paper_search`), and upserts `seminal_claim_map` rows. `--dry-run` prints the resolved `(claim_id, bibcode, label)` triples for Kun sign-off before any write.

**(b) Bibcode backfill from existing evidence (bootstrap accelerator).** 11,468 of 11,922 `evidence` rows already carry an `ads_bibcode`. For any `claims` row whose existing evidence includes a pre-2010, high-`citation_count` paper, that bibcode is a *candidate* seminal source. `scripts/ccm_seed_seminal_map.py --suggest` emits these candidates to a review JSON; they are **never** auto-enabled — Kun promotes them into the YAML. This keeps the registry human-authoritative while exploiting data we already hold.

### 2.5 Selection criteria for the initial batch

Target the claims that are both (a) genuinely seminal and (b) currently mis-bucketed. Concretely, seed from the intersection:

```sql
SELECT c.id, c.text, c.trust_level, c.page_id
FROM claims c
WHERE c.claim_type = 'established'
  AND c.trust_level IN ('unverified', 'accepted', 'debated')
  AND EXISTS (                       -- has at least one old, well-cited backing paper
      SELECT 1 FROM evidence e
      WHERE e.claim_id = c.id AND e.year IS NOT NULL AND e.year <= 2010
  );
```

This is a finite, reviewable set (low hundreds at most, given 733 established claims). CCM is intentionally *not* run corpus-wide.

### 2.6 On-topic keyphrase gate

`topic_keyphrases` is reused verbatim by Stage 4 (Pico) and Stage 3 (extractor) as an on-topic guard, mirroring the proven `term_overlap_count` pre-gate in `scripts/targeted_ads_miner.py:335`. A citing paper whose introduction mentions the seminal bibcode but shares **zero** keyphrases with the claim is discarded before any LLM call — this is the cheap defense against a paper that cites White & Rees (1978) for an unrelated cosmological-simulation reason.

---

## 3. Stage 2 — NASA ADS Citation Querying

### 3.1 Reuse the existing ADS client

ADS access already exists and is the **only** sanctioned ADS surface: `app/services/paper_search.py:ads_search()` (verified). It reads `settings.ADS_API_KEY`, sends `Authorization: Bearer <token>`, and returns `PaperRecord` objects. CCM **must not** open a second ADS client; it calls a thin new helper that wraps the same module so token handling, `User-Agent`, and error semantics stay centralized.

### 3.2 The citation query

ADS exposes the second-order operator `citations()`, which returns the papers that cite a given bibcode. The CCM query, for a seminal bibcode `B`:

```
q = citations(bibcode:"<B>")
fq = database:astronomy
fl = bibcode,title,abstract,author,year,doi,identifier,citation_count,pub
sort = date desc
rows = 200            # paginate via `start` for highly-cited works
```

New function in `app/services/paper_search.py` (extends, does not replace):

```python
def ads_citing_papers(bibcode: str, *, rows: int = 200, start: int = 0,
                      min_year: int | None = None) -> list[PaperRecord]:
    """Return modern papers that CITE the given seminal bibcode (ADS citations() op).

    Reuses the module's auth + _ads_to_record mapping. Caller paginates via `start`.
    """
    if not settings.ADS_API_KEY:
        raise PaperSearchError("ADS_API_KEY not configured")
    q = f'citations(bibcode:"{bibcode}")'
    if min_year:
        q = f'{q} year:{min_year}-'          # ADS open-ended range
    params = {
        "q": q,
        "fl": ADS_FIELDS,                      # already includes abstract,identifier
        "rows": rows,
        "start": start,
        "sort": "date desc",
        "fq": "database:astronomy",
    }
    url = f"{ADS_SEARCH_URL}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {settings.ADS_API_KEY}",
        "User-Agent": "NebulaMind/1.0 (citation-context-mining)",
    })
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read())
    except Exception as e:
        raise PaperSearchError(f"ADS citations request failed: {e}") from e
    docs = data.get("response", {}).get("docs", [])
    return [_ads_to_record(d) for d in docs]
```

Worked example payload (HTTP GET, token in header):

```
GET https://api.adsabs.harvard.edu/v1/search/query
    ?q=citations(bibcode%3A%221978MNRAS.183..341W%22)+year%3A2023-
    &fl=bibcode,title,abstract,author,year,doi,identifier,citation_count,pub
    &rows=200&start=0&sort=date+desc&fq=database%3Aastronomy
Authorization: Bearer dEtX…(40 chars)
User-Agent: NebulaMind/1.0 (citation-context-mining)
```

### 3.3 Recency window — the design lever that makes greening legitimate

`min_year` is the knob that targets the freshness floor. Default `min_year = current_year - 2` (i.e. 2024+ at time of writing). Rationale, tied directly to §1.1:

- The freshness floor demotes unless evidence with `created_at` in the last 90 days **and** a recent `sup_years` exists. CCM rows are inserted now (`created_at = now`), so the `created_at` half is automatically satisfied on every run.
- But `sup_years` reads `evidence.year` — the **publication** year of the citing paper, not the insert date. To also satisfy the recency intent of the floor, the citing papers themselves must be recent. `min_year = year - 2` guarantees `max(sup_years) >= year - 2`, comfortably inside `FRESHNESS_FLOOR_YEARS = 10`.

This is deliberate and defensible: we are asserting consensus **because the modern literature actively builds on the seminal result right now**, evidenced by 2024–2026 citing papers — not merely because an old paper exists. If a seminal claim has *no* recent citers, CCM produces nothing and the claim correctly stays out of green. That is a feature.

### 3.4 Rate-limit discipline

ADS enforces a daily quota (the `X-RateLimit-Remaining` / `X-RateLimit-Reset` headers). The existing code does not read them; CCM adds minimal handling in the wrapper's Celery caller (not the pure function):

- Read `X-RateLimit-Remaining` from each response; if `< 50`, stop the run early and persist a `ccm_run` checkpoint (§5.5) for resumption next beat.
- On HTTP 429, honor `Retry-After`; do not hammer. Back off and reschedule via the existing Celery retry mechanism.
- Batch: one `citations()` call per seminal bibcode per run returns up to 200 citers; a few hundred seminal bibcodes ⇒ a few hundred ADS calls/day, far under quota. Pagination (`start += rows`) only for works with >200 recent citers, which is rare in a 2-year window.

### 3.5 Output of Stage 2

For each enabled `seminal_claim_map` row, a deduplicated list of candidate `PaperRecord`s (the modern citers), each carrying `bibcode`, `title`, `abstract`, `authors`, `year`, `doi`, `arxiv_id`. These flow to Stage 3. Candidates already present as `evidence` for this `claim_id` are dropped immediately using the proven `already_attached` predicate (§5.2).

---

## 4. Stage 3 — Introduction / Citation-Context Extractor

### 4.1 The hard constraint: NebulaMind stores abstracts, not full text

Verified: `evidence.abstract` and `arxiv_fetch` capture **abstracts only**. There is no `full_text`, no `introduction`, no body-section column anywhere in `app/models/*` (grep confirmed). Therefore "parse the introduction section" cannot mean "read a stored intro" — there is none. CCM must *acquire* the citation context. Three tiers, cheapest first, stop at first success:

### 4.2 Tier A (primary) — Semantic Scholar citation contexts, no PDF parsing

Semantic Scholar's Graph API exposes, for a cited paper, the **`contexts`** (the verbatim sentence(s) surrounding each in-text citation) and **`intents`** (S2's own `background` / `methodology` / `result` classification) of every citing paper. This is purpose-built for exactly our problem and avoids PDF/LaTeX parsing entirely.

Endpoint (paginated):

```
GET https://api.semanticscholar.org/graph/v1/paper/<PAPER_ID>/citations
    ?fields=contexts,intents,isInfluential,citingPaper.externalIds,
            citingPaper.title,citingPaper.year,citingPaper.abstract
    &limit=1000&offset=0
```

`<PAPER_ID>` is resolved from the seminal bibcode's DOI/arXiv via `ADS:<bibcode>` or `DOI:<doi>` external-id lookup (S2 accepts `DOI:10.1093/...` and `arXiv:...` id forms). The response gives, per citer:

```json
{
  "contexts": [
    "Following the standard cooling framework of White & Rees (1978), we assume baryons condense at halo centres."
  ],
  "intents": ["background"],
  "isInfluential": false,
  "citingPaper": {
    "externalIds": {"ArXiv": "2503.01234", "DOI": "10.3847/..."},
    "title": "The cold gas content of z~3 halos",
    "year": 2025,
    "abstract": "..."
  }
}
```

The `contexts[*]` strings are precisely the introductory citation sentences Pico must classify. `intents == ["background"]` is a strong free prior that the citation is introductory/supportive (used as a feature, not a substitute for Pico — §6.4). New helper in `app/services/paper_search.py`:

```python
S2_CITATIONS_URL = "https://api.semanticscholar.org/graph/v1/paper/{id}/citations"

def s2_citation_contexts(s2_id_or_extid: str, *, limit: int = 1000, offset: int = 0) -> list[dict]:
    """Return citing-paper records WITH contexts+intents for a cited paper.
    `s2_id_or_extid` may be a raw S2 id, 'DOI:<doi>', or 'arXiv:<id>'."""
    fields = ("contexts,intents,isInfluential,"
              "citingPaper.externalIds,citingPaper.title,"
              "citingPaper.year,citingPaper.abstract")
    params = {"fields": fields, "limit": limit, "offset": offset}
    url = S2_CITATIONS_URL.format(id=urllib.parse.quote(s2_id_or_extid, safe=":")) \
          + "?" + urllib.parse.urlencode(params)
    try:
        with urllib.request.urlopen(url, timeout=20) as resp:
            data = json.loads(resp.read())
    except Exception as e:
        raise PaperSearchError(f"S2 citations request failed: {e}") from e
    return data.get("data", [])
```

Cross-walk: Stage 2 (ADS `citations()`) and Tier A (S2 `/citations`) are redundant discovery paths for the *same* relationship. We run **ADS as the authoritative citer set** (richer astronomy coverage, our paid token) and use **S2 purely to fetch the context sentence** for each ADS-confirmed citer, joined on DOI/arXiv id. This avoids trusting S2's citer completeness while still getting its context strings. If S2 has no context for an ADS citer, fall through to Tier B.

### 4.3 Tier B (fallback) — abstract as proxy context

If S2 yields no context sentence for a citer (common for very recent papers not yet indexed), fall back to the citer's **abstract** (already returned by the ADS `citations()` call, no extra fetch). Seminal works are frequently invoked in abstracts too (*"…building on the cooling model of White & Rees…"*). The abstract is passed to Pico with an explicit flag `context_source = "abstract"` so the classifier (and audit log) knows it judged an abstract, not a pinpoint intro sentence. Lower prior; Pico threshold unchanged.

### 4.4 Tier C (last resort, rate-capped) — arXiv intro extraction

Only for high-value seminal claims still short of `n_supports >= 3` after Tiers A+B, and only for citers with an `arxiv_id`. Fetch the arXiv source/HTML (`ar5iv` rendered HTML is the cleanest: `https://ar5iv.org/abs/<arxiv_id>`), isolate the first `<section>`/`Introduction` heading, and extract sentences containing the seminal author surname + year token. This is the only tier that touches full text; it is deterministic (regex on author-year), capped at **5 papers per CCM run** (mirrors the Stage-3 cap discipline in `dynamic_citations_design_v1.md §4.3`), and never blocks the pipeline. Extracted sentences then go to Pico exactly like Tier A contexts.

### 4.5 Context object handed to Stage 4

Each surviving candidate becomes a `CitationContext`:

```python
@dataclass(frozen=True)
class CitationContext:
    claim_id: int
    seminal_label: str            # "White & Rees 1978"
    seminal_bibcode: str
    citing_bibcode: str
    citing_arxiv_id: str | None
    citing_doi: str | None
    citing_title: str
    citing_year: int
    context_sentence: str         # the intro/abstract sentence to classify
    context_source: str           # 's2_context' | 'abstract' | 'arxiv_intro'
    s2_intent: str | None         # 'background' | 'methodology' | 'result' | None
    keyphrase_hits: int           # on-topic gate (§2.6); pre-filter < 1 => drop
    citing_record: PaperRecord    # full record for evidence insert
```

The on-topic gate (`keyphrase_hits < 1` ⇒ drop) runs **before** Pico, so no LLM tokens are spent on off-topic citers.

---

## 5. Stage 5 — Auto-Link Database Updates  *(ordering note: DB design precedes classifier prompts so §6 can reference these rows)*

### 5.1 What gets written, and to which existing table

CCM writes **`evidence`** rows — the same table `targeted_ads_miner.insert_evidence` writes (verified at `scripts/targeted_ads_miner.py:826`). No new evidence-like table. The mapping `PaperRecord → evidence` reuses `PaperRecord.to_evidence_dict()` (verified at `paper_search.py`). CCM-specific column values:

| `evidence` column | CCM value | Rationale |
|---|---|---|
| `claim_id` | the seminal claim's id | links to the baseline claim |
| `stance` | `"supports"` (only on Pico SUPPORTIVE) | feeds E-component positively |
| `source_channel` | `"citation_context_mining"` | **new channel tag**, distinct from `targeted_ads_miner` — enables audit, rollback, metrics |
| `arxiv_verified` | `bool(record.arxiv_id)` | matches existing gate semantics |
| `peer_reviewed` | `True` if ADS `pub` is refereed else `False` | ADS citers in `database:astronomy` are overwhelmingly refereed |
| `quality` | Pico confidence-scaled (§6.5), clamped `[0.50, 0.80]` | introductory citations are *good* but not primary-result evidence; capped below jury-verified primary evidence |
| `summary` | the verbatim `context_sentence` (≤500 chars) | the quotable proof, mirrors `targeted_ads_miner` summary semantics |
| `abstract` | citer abstract | standard |
| `ads_bibcode` / `doi` / `arxiv_id` / `year` / `title` / `authors` | from `to_evidence_dict()` | standard |
| `stance_jury_run_at` | `now()` | marks classifier pass |
| `verified_at` | `now()` | supportive context is a positive verification act |
| `consensus_vote` / `consensus_scorecard_id` | NULL | CCM uses the lightweight path, not the full scorecard jury (§6, §9) |

### 5.2 Duplicate avoidance (reuse the proven predicate)

CCM **must** reuse `already_attached(db, claim_id, record)` (verified at `targeted_ads_miner.py:320`), which checks `Evidence.claim_id` against `arxiv_id` / `doi` / `ads_bibcode`. This already prevents the same paper being attached twice to the same claim across *both* miners (it queries the whole `evidence` table for that claim, source-agnostic). CCM adds **one** extra guard for its own re-runs:

```python
def ccm_already_linked(db, claim_id: int, record: PaperRecord) -> bool:
    # primary: shared predicate covering arxiv/doi/bibcode
    if already_attached(db, claim_id, record):
        return True
    # belt-and-suspenders for context re-mining (same paper, new run)
    if record.bibcode:
        return bool(db.query(Evidence.id).filter(
            Evidence.claim_id == claim_id,
            Evidence.ads_bibcode == record.bibcode,
            Evidence.source_channel == "citation_context_mining",
        ).first())
    return False
```

A `UNIQUE` partial index hardens this at the DB layer against race conditions between concurrent Celery workers:

```sql
CREATE UNIQUE INDEX uq_ccm_evidence_claim_bibcode
    ON evidence (claim_id, ads_bibcode)
    WHERE source_channel = 'citation_context_mining' AND ads_bibcode IS NOT NULL;
```

Insert path uses `INSERT … ON CONFLICT DO NOTHING` semantics (catch `IntegrityError`, rollback the single row, continue) so a duplicate never aborts the batch.

### 5.3 Audit trail — `trust_audit_log` (correct schema, verified)

The schema (verified `app/models/claim.py:TrustAuditLog`) is **claim-level**, recording trust-level transitions with E/V/T/H components and a `trigger` string. CCM does **not** write `evidence`-level rows into it (wrong grain). Instead, CCM follows the existing contract exactly: after inserting its `supports` rows for a claim, it calls the canonical recalculation, which itself appends the `trust_audit_log` row when the level changes. CCM's contribution is a distinct `trigger` value so the green transition is attributable to CCM:

```python
from app.routers.claims import recalculate_trust_v2
new_level, ts = recalculate_trust_v2(
    claim_id, db,
    trigger="ccm_citation_context",      # NEW trigger string, audit-greppable
    actor_agent_id=ccm_agent_id,         # the CCM service agent (see §5.4)
)
```

`recalculate_trust_v2` already writes the `TrustAuditLog` row with `old_level`, `new_level`, `e_component`, etc. (verified it persists + audits at the tail of the function). The only change is recognizing `"ccm_citation_context"` in the trigger allow-lists used by `get_trust_history` (`app/routers/claims.py:614`) so the history endpoint surfaces CCM transitions. This is a one-line addition to that `trigger IN (...)` set; no schema change to `trust_audit_log`.

Per-evidence provenance (which context sentence, which source tier, Pico raw output) is **not** forced into `trust_audit_log`. It lives in:
- `evidence.summary` = the verbatim context sentence (queryable),
- `evidence.source_channel = 'citation_context_mining'` (filterable),
- a dedicated `EvidenceVote` row recording Pico's verdict (next).

### 5.4 Pico's verdict recorded as an `EvidenceVote` (reuse, not reinvent)

To keep CCM inside the existing evidence-provenance model, each inserted evidence row gets **one** `EvidenceVote` (verified model at `claim.py:EvidenceVote`) capturing Pico's decision — exactly as `targeted_ads_miner.insert_evidence` records juror votes (`targeted_ads_miner.py:855`):

```python
db.add(EvidenceVote(
    evidence_id=ev.id,
    value=1,                                  # SUPPORTIVE
    agent_id=agent_id_for_label(db, "Pico-CCM", settings.ASTRO_SCORER_MODEL),
    reason=context_sentence[:500],
    weight=1.0,
    voter_type="agent",
    scheduled_via="ccm",                      # existing nullable column, verified
    latency_ms=pico_latency_ms,               # existing nullable column, verified
))
```

A dedicated agent row `CCM-Pico` (role `jury`, model `vanta-research/atom-astronomy-7b`) is created once via the existing `agent_id_for_label` helper pattern (`targeted_ads_miner.py:816`). This means CCM evidence is **vote-backed**, so it also contributes to the V-component of trust through the existing `EvidenceVote` aggregation in `recalculate_trust_v2` — a second, independent reason the claim moves toward green.

### 5.5 Run bookkeeping — `ccm_runs`

For idempotency, resumption, and metrics, a lightweight run table (parallels `autowiki_runs`, referenced in `debated_claim_seeder_v1.md`):

```sql
CREATE TABLE ccm_runs (
    id                 SERIAL PRIMARY KEY,
    seminal_map_id     INT REFERENCES seminal_claim_map(id) ON DELETE CASCADE,
    claim_id           INT NOT NULL,
    started_at         TIMESTAMP DEFAULT NOW(),
    finished_at        TIMESTAMP,
    ads_citers_seen    INT DEFAULT 0,
    contexts_fetched   INT DEFAULT 0,
    pico_supportive    INT DEFAULT 0,
    pico_rejected      INT DEFAULT 0,
    evidence_inserted  INT DEFAULT 0,
    new_trust_level    VARCHAR(20),
    ads_rl_remaining   INT,             -- checkpoint for quota-aware resume
    status             VARCHAR(20) DEFAULT 'running',  -- running|done|partial|error
    error              TEXT
);
CREATE INDEX ix_ccm_runs_claim ON ccm_runs(claim_id);
```

`status='partial'` + `ads_rl_remaining` lets the next beat resume seminal bibcodes not yet processed when the daily ADS quota is hit mid-run (§3.4).

### 5.6 Transaction discipline

Per claim: open a transaction, insert all qualifying evidence + votes with `flush()` (matching `targeted_ads_miner` which `flush()`es per row), then **one** `recalculate_trust_v2` call, then `commit()`. On any `IntegrityError` for a single evidence row, savepoint-rollback that row only (the partial unique index makes this a no-op dedupe), never the whole claim. This mirrors the existing miner's per-row `flush` + batch `commit` rhythm and guarantees the audit-log transition reflects the full evidence set committed in that pass.

---

## 6. Stage 4 — Pico (Atom-7B) Classifier Prompts

### 6.1 Why Pico, and which exact model

Verified platoon facts:
- `settings.ASTRO_SCORER_MODEL = "vanta-research/atom-astronomy-7b"`, served at the Studio Ollama OpenAI-compatible endpoint (`OLLAMA_STUDIO_BASE_URL = http://localhost:11434/v1`).
- Pico is the astronomy-domain juror in the live 3-model stance jury (`targeted_ads_miner.jury_models()`, label `Atom-7B`) and `platoon_realignment_v2.md` explicitly keeps Pico as the fast 7B / ~5 GB / sub-second domain scorer — and rejects swapping it out for heavy models precisely because *"Pico handles batch volume."*

CCM is a **batch-volume** problem (potentially thousands of citation contexts). It is the textbook Pico workload: short input (one sentence + one claim), binary-ish output, astronomy priors helpful, latency-critical, cost = $0 (local). Routing CCM's first-pass classification to a cloud model would be both slower per-call under our rate discipline and needlessly paid. So Pico owns the high-volume first pass; the full 3-juror cloud-augmented path is reserved for the *escalation* case (§6.6, §9).

### 6.2 The classification task — sharply scoped

Pico answers exactly one question per `CitationContext`:

> Does this citation-context sentence invoke the seminal work **as accepted background / standard framework that the citing paper builds upon or assumes** (SUPPORTIVE), or does it invoke it **to dispute, revise, or contrast against** (NON-SUPPORTIVE), or is it **not actually about the seminal claim's substance** (OFF-TOPIC)?

Only SUPPORTIVE yields a `supports` evidence row. NON-SUPPORTIVE and OFF-TOPIC are logged and dropped (NON-SUPPORTIVE optionally routed to the challenge pipeline — §6.4). This three-way scoping is what prevents CCM from manufacturing false consensus from papers that cite the seminal work in order to *challenge* it.

### 6.3 System prompt (Pico)

Stored in the prompt registry (`PromptRegistry`, verified in use at `targeted_ads_miner.py:130`) under id `ccm_intro_classifier`, policy `ccm_v1`, so it is versioned and hashed like the stance prompt. Literal text:

```
You are a precise astronomy citation-context classifier for a knowledge base.

You are given:
  CLAIM: a settled, foundational astronomy statement.
  SEMINAL WORK: the historical paper that the claim attributes the result to.
  CITATION CONTEXT: one sentence (from a MODERN paper) that cites the SEMINAL WORK.

Decide how the modern sentence uses the seminal work, with respect to the CLAIM:

  SUPPORTIVE  — The sentence treats the seminal result as accepted background,
                standard framework, established method, or a premise the modern
                paper builds on or assumes. Typical signals: "following",
                "based on", "as established by", "the standard ... of",
                "building on", "in the framework of", "as shown by".

  NONSUPPORTIVE — The sentence cites the seminal work to dispute, revise,
                challenge, correct, or contrast against it. Signals: "contrary
                to", "unlike", "revises", "in tension with", "challenges",
                "fails to", "we revisit".

  OFFTOPIC    — The sentence cites the seminal work for a reason unrelated to
                the substance of the CLAIM, or is only a passing list citation
                with no assertion about the claim's content.

Hard rules:
1. Judge ONLY the provided sentence. Do not use outside knowledge about the paper.
2. SUPPORTIVE requires that the sentence actually concerns the CLAIM's subject.
   A supportive tone about an unrelated point is OFFTOPIC, not SUPPORTIVE.
3. If the sentence both builds on AND partially disputes, choose NONSUPPORTIVE.
4. Do not be generous. A vague mention with no clear stance is OFFTOPIC.
5. Output ONLY the final block, nothing after it.

Output EXACTLY:
###LABEL: <SUPPORTIVE|NONSUPPORTIVE|OFFTOPIC>
###CONFIDENCE: <LOW|MEDIUM|HIGH>
```

### 6.4 User template

```
CLAIM:
{claim_text}

SEMINAL WORK: {seminal_label}   (bibcode {seminal_bibcode})

CITATION CONTEXT (from {citing_year} paper "{citing_title_short}"):
"{context_sentence}"

CONTEXT SOURCE: {context_source}        # s2_context | abstract | arxiv_intro
S2 INTENT HINT: {s2_intent_or_none}     # advisory only; do not defer to it
```

`{claim_text}` is normalized through the existing `normalize_claim_text` (`targeted_ads_miner.py`, strips claim/trust markers, LaTeX, numerics) so Pico never sees `<!--claim:N-->` noise. `{context_sentence}` is the verbatim mined sentence. The `S2 INTENT HINT` is passed as a *feature* but the prompt explicitly forbids deferring to it (rule-free advisory), so we keep Pico as the decider while still benefiting from S2's `background` signal.

### 6.5 Parsing, thresholds, and quality mapping

Parsing mirrors the proven `parse_juror` regex discipline (`targeted_ads_miner.py:696`), with a `_last_match` strategy so any stray reasoning (Atom-7B is not a `<think>` model, but defense-in-depth is cheap) does not poison the verdict:

```python
LABEL_RE = re.compile(r"###LABEL:\s*(SUPPORTIVE|NONSUPPORTIVE|OFFTOPIC)", re.I)
CONF_RE  = re.compile(r"###CONFIDENCE:\s*(LOW|MEDIUM|HIGH)", re.I)
```

Acceptance and quality:

| Pico LABEL | CONFIDENCE | Action | `evidence.quality` |
|---|---|---|---|
| SUPPORTIVE | HIGH | insert `supports` | 0.80 |
| SUPPORTIVE | MEDIUM | insert `supports` | 0.68 |
| SUPPORTIVE | LOW | **hold** → escalate (§6.6) | — |
| NONSUPPORTIVE | any | drop; emit `ccm_challenge_candidate` event for the separate challenge pipeline | — |
| OFFTOPIC | any | drop, log to `ccm_runs.pico_rejected` | — |

Quality is clamped to `[0.50, 0.80]` (§5.1): introductory endorsements are solid but must never outrank a jury-verified primary-result paper (which `targeted_ads_miner` can score up to its own ceiling). This keeps the E-component honest — three SUPPORTIVE intro citations at 0.68–0.80 sum to ≈2.0–2.4, which through `E = tanh((E_sup − E_chal)/1.5)` yields `E ≈ 0.79–0.85`; with `TRUST_W_EVIDENCE = 0.45` that alone contributes ≈0.36 to `TS`, and the Pico `EvidenceVote`s add positive V (§5.4). Combined with a non-negative T (recent years, no decay) this clears `TRUST_CONSENSUS_MIN = 0.75` once `n_supports ≥ 3` and `n_challenges == 0`. The arithmetic is shown explicitly in §7.

### 6.6 LOW-confidence escalation — bounded reuse of the full jury

A SUPPORTIVE/LOW result is *not* discarded and *not* trusted. It is escalated to the existing 3-model stance jury (`run_jury_async`, Mima + Nutty-Heavy + Pico) using the **claim vs. citing-paper abstract** as the standard jury input. This:
- caps cloud/heavy spend to the genuinely ambiguous minority,
- reuses verified code (no new juror logic),
- means CCM's cheap path handles the bulk while quality is preserved on the margin.

Escalation volume is capped per run (default 20) to bound latency/cost; overflow is deferred to the next beat via `ccm_runs.status='partial'`.

### 6.7 Saturation guardrail (verified hazard)

`TOOLS.md` (Kun's own notes) and `platoon_realignment_v2.md` both warn that the Studio Ollama queue saturates when Celery jurors run, returning empty content. CCM must therefore:
- run its Pico batch **off-peak** relative to the stance-jury beats (jury fast-drain is every 30 min at `:00/:30`; CCM beat is placed at `:20` — §8),
- treat empty Pico content as `OFFTOPIC`-equivalent *hold* (re-queue, do not insert), never as a default verdict,
- add a 0.3 s inter-call sleep (the documented mitigation in `TOOLS.md`) and respect the `InferenceScheduler` advisory lock that `targeted_ads_miner` already uses, rather than hitting Ollama raw.

---

## 7. Trust-Math Walkthrough (the proof CCM works)

A fully worked example for *"White & Rees 1978 established gas cooling in DM halos"*, currently `unverified`, 1 old evidence row.

**Before CCM:** evidence = [White&Rees 1978, quality 0.55, supports]. `n_supports = 1`. `E = tanh(0.55/1.5) = 0.35`. No votes ⇒ `V = 0`. `T`: `years_since = 2026−1978 = 48`, `T = max(−0.05·(48−5)/5, −0.30) = −0.30`. `H = 0`. `TS = 0.45·0.35 + 0.35·0 + 0.10·(−0.30) + 0.80·0 = 0.158 − 0.030 = 0.128` → bucket `unverified` (and even if nudged, `n_supports < 3`). Gray. ✔ matches observed state.

**CCM run:** ADS `citations(bibcode:"1978MNRAS.183..341W") year:2024-` → ~40 modern citers; S2 contexts fetched; on-topic gate keeps ~25; Pico labels 12 SUPPORTIVE (8 HIGH, 4 MEDIUM), 9 OFFTOPIC, 3 NONSUPPORTIVE (logged as challenge candidates), 1 LOW→escalated→jury SUPPORTS. Insert the top, say, 6 SUPPORTIVE rows (a sensible per-run cap, §9) with quality {0.80×4, 0.68×2} and 6 positive Pico votes; `created_at = now`, years 2024–2026.

**After CCM:** supports = old(0.55) + 6 new ⇒ `E_sup = 0.55 + 4·0.80 + 2·0.68 = 0.55 + 3.20 + 1.36 = 5.11`; `E_chal = 0`. `E = tanh(5.11/1.5) = tanh(3.41) ≈ 0.998`. Votes: 6 positive Pico votes, `n_total = 6`, `confidence = 1 − e^(−6/2) = 1 − 0.0498 = 0.950`, `raw = 1.0` ⇒ `V = 0.950`. Temporal: `sup_years` now includes 2026 ⇒ `years_since = 0`, `T = 0`. `H = 0`. 

`TS = 0.45·0.998 + 0.35·0.950 + 0.10·0 + 0.80·0 = 0.449 + 0.333 = 0.782`.

Bucket test: `TS (0.782) ≥ 0.75` ✔ `and n_supports (7) ≥ 3` ✔ `and n_challenges == 0` ✔ ⇒ **consensus**. Freshness floor: `max(sup_years) = 2026`, `2026 − 2026 = 0 ≤ 10` ✔ — floor does not fire. **Green, stably.** ∎

This is the entire thesis, demonstrated against the live thresholds (`TRUST_CONSENSUS_MIN=0.75`, `TRUST_CONSENSUS_MIN_SUPPORTS=3`, `FRESHNESS_FLOOR_YEARS=10`, weights 0.45/0.35/0.10/0.80, `VOTE_CONFIDENCE_HALF_LIFE=2`, `DECAY_FREE_YEARS=5`). CCM changes no constant and no code in the trust path; it only supplies the recent supportive evidence the function already demands.

> **Sensitivity note for reviewers:** the result is robust but not infinite-margin. If only 3 SUPPORTIVE/MEDIUM rows (0.68) are found, `E_sup = 0.55 + 3·0.68 = 2.59`, `E = tanh(1.73) = 0.939`, votes `n_total=3` ⇒ `confidence = 1−e^{-1.5}=0.777`, `V=0.777`; `TS = 0.45·0.939 + 0.35·0.777 = 0.422 + 0.272 = 0.694` < 0.75 ⇒ **accepted, not consensus**. So the *de-facto* requirement for green is ~4+ supportive intro citations (or a mix including HIGH-confidence 0.80 rows). This is healthy: green should require a real cluster of modern endorsement, not the bare minimum. The per-run insert cap (§9) should therefore target ≥4–6 SUPPORTIVE rows where available.

---

## 8. Platoon Assignment & Scheduling

| Stage | Owner | Host / Endpoint | Cost | Justification |
|---|---|---|---|---|
| Seminal map seeding (YAML → DB) | Kun (authoring) + deterministic loader | Mac Studio (local DB) | $0 | Human-authoritative registry; Kun owns curation/analysis per SOUL role |
| ADS `citations()` querying | Deterministic Python (`ads_citing_papers`) | Mac Studio → ADS API (token) | $0 (quota) | No model needed; reuses paid ADS token via existing client |
| S2 context fetch (Tier A) | Deterministic Python (`s2_citation_contexts`) | Mac Studio → S2 API (free tier) | $0 | No key required at our rate; no LLM |
| Abstract proxy (Tier B) | Deterministic | Mac Studio | $0 | Uses already-fetched ADS abstract |
| arXiv intro extract (Tier C, capped 5/run) | Deterministic regex on ar5iv HTML | Mac Studio → ar5iv | $0 | Rare; author-year regex, no model |
| On-topic keyphrase gate | Deterministic (`term_overlap_count`) | Mac Studio | $0 | Reuses proven pre-gate |
| **Intro-context classification (bulk)** | **Pico = `vanta-research/atom-astronomy-7b`** | **Mac Studio Ollama `localhost:11434/v1`** | **$0** | **Batch-volume, short-input, astronomy-domain — Pico's designated workload per `platoon_realignment_v2.md`** |
| LOW-confidence escalation (bounded ≤20/run) | Full stance jury: Mima `qwen3:30b` + Nutty-Heavy `deepseek-r1:70b` + Pico | Mac Studio (Mima/Pico) + Nutty-Heavy local | $0 local | Reuses `run_jury_async`; only the ambiguous margin pays the heavy cost |
| Evidence + vote insert, dedup, audit recalculation | Deterministic Python + `recalculate_trust_v2` | Mac Studio (local Postgres `nebulamind-postgres-1`) | $0 | Reuses verified insert/dedup/trust code |
| Dry-run audit + threshold review | Kun | Mac Studio session | cloud-paid (Kun's own turns) | Analyst sign-off before enabling writes |

**No cloud LLM is on CCM's hot path.** This is a deliberate cost contrast with `targeted_ads_miner`, whose `SCREEN_MODEL = gemini-2.5-flash` pays per screen. CCM's input (one sentence) is small enough that Pico's astronomy priors are sufficient, so the bulk path is fully local/$0; cloud-equivalent spend appears only if a future operator opts the LOW-escalation jury onto a cloud juror.

### 8.1 Celery beat entry

Add to `app/agent_loop/worker.py` `beat_schedule` (verified structure). New task `app.agent_loop.ccm.run_ccm_cycle`, placed at `:20` to dodge stance-jury saturation windows (`:00`/`:30`/`:45`) per §6.7:

```python
"ccm-cycle-hourly": {
    "task": "app.agent_loop.ccm.run_ccm_cycle",
    "schedule": crontab(minute=20),          # hourly at :20, off-peak vs jury drains
    "options": {"queue": "ccm"},             # isolate from autowiki/jury queues
},
```

The task pulls the next batch of enabled `seminal_claim_map` rows not processed in the last `CCM_RECHECK_DAYS` (config, default 7), respects the ADS quota checkpoint, and self-limits via `CCM_MAX_CLAIMS_PER_RUN` (config, default 15) so one beat never floods. Because seminal facts change slowly, a weekly full sweep is ample; hourly cadence simply spreads the sweep thinly to stay under quota and off-peak.

### 8.2 New config knobs (`app/config.py`)

```python
CCM_ENABLED: bool = True
CCM_MIN_CITER_YEAR_OFFSET: int = 2          # min_year = current_year - this
CCM_MAX_CLAIMS_PER_RUN: int = 15
CCM_MAX_EVIDENCE_PER_CLAIM_PER_RUN: int = 6 # the insert cap referenced in §7
CCM_RECHECK_DAYS: int = 7
CCM_LOW_ESCALATION_CAP: int = 20
CCM_ARXIV_INTRO_CAP: int = 5
CCM_PICO_MODEL: str = "vanta-research/atom-astronomy-7b"
CCM_ADS_RL_FLOOR: int = 50                   # stop run when X-RateLimit-Remaining < this
```

---

## 9. Risks, Anti-Patterns, Quality Gates

1. **Manufacturing false consensus (top risk).** Mitigated by: (a) three-way Pico labeling that routes disputing citations to NONSUPPORTIVE, never `supports`; (b) `n_challenges == 0` is still required by the trust gate, so if CCM (or any pipeline) finds even one challenge the claim cannot be green — CCM cannot bulldoze a genuinely contested claim into green; (c) quality clamp `≤0.80` keeps intro citations below primary evidence; (d) the on-topic keyphrase gate; (e) seminal allow-list scoping (no corpus-wide citation import).
2. **Citation-context misattribution.** S2 contexts occasionally attach the wrong sentence to a citation. Mitigated by Pico's OFFTOPIC route + the requirement that the sentence concern the claim's subject (system-prompt rule 2) + verbatim storage in `evidence.summary` for human spot-audit.
3. **Ollama saturation false-negatives** (verified hazard): empty Pico content treated as *hold/re-queue*, never as a verdict; off-peak `:20` scheduling; 0.3 s inter-call sleep; advisory-lock respect (§6.7).
4. **ADS quota exhaustion:** `X-RateLimit-Remaining` checkpointing + `status='partial'` resume + hourly thin sweep (§3.4, §8.1).
5. **Duplicate evidence across miners:** source-agnostic `already_attached` + partial unique index + `ON CONFLICT DO NOTHING` (§5.2).
6. **Audit-grain error:** CCM never writes evidence-grain rows into the claim-grain `trust_audit_log`; provenance lives in `evidence.summary` / `source_channel` / `EvidenceVote` (§5.3–5.4).
7. **Over-greening drift:** a `ccm_runs` metrics review (Kun, weekly heartbeat) tracks how many claims CCM moved to consensus; a hard cap `CCM_MAX_CLAIMS_PER_RUN` plus the seminal allow-list bound blast radius. Rollback is a single `DELETE FROM evidence WHERE source_channel='citation_context_mining' AND claim_id=…` followed by `recalculate_trust_v2`, fully reversible.

**Pre-enable gate (blocking):** Tori runs the full pipeline in `--dry-run` over the seed batch; Kun reviews the `ccm_runs`-shaped report (per-claim: citers seen, Pico label histogram, projected `TS`, projected bucket) and signs off thresholds **before** `CCM_ENABLED` writes are turned on. No silent first write.

---

## 10. Proposed File Manifest (for Tori)

In dependency order:

1. `backend/migrations_runs/NNNN_ccm.sql` — `CREATE TABLE seminal_claim_map`, `ccm_runs`; partial unique index on `evidence`; (no change to `evidence`/`claims`/`trust_audit_log` columns).
2. `backend/app/models/seminal.py` + register in `app/models/__init__.py` — `SeminalClaimMap`, `CcmRun` models.
3. `backend/app/services/paper_search.py` — **extend** with `ads_citing_papers()` and `s2_citation_contexts()` (no edits to existing functions).
4. `backend/data/seminal_claims.yaml` — Kun-authored seed (reviewed by HwaO/Papa).
5. `backend/scripts/ccm_seed_seminal_map.py` — YAML loader, `--suggest`, `--dry-run`.
6. `backend/app/agent_loop/ccm.py` — `run_ccm_cycle` Celery task + `CitationContext` dataclass + tier A/B/C extractor + Pico classifier call (via `InferenceScheduler`) + insert/dedup/recalc orchestration.
7. `backend/app/services/prompt_registry` seed — register `ccm_intro_classifier` / `ccm_v1` system+user templates (§6.3–6.4).
8. `backend/app/agent_loop/worker.py` — add `ccm-cycle-hourly` beat entry (§8.1).
9. `backend/app/config.py` — add §8.2 knobs.
10. `backend/app/routers/claims.py` — add `"ccm_citation_context"` to the `get_trust_history` trigger allow-list (one-line; §5.3).
11. Tests:
    - `tests/ccm/test_ads_citations.py` — `ads_citing_papers` query shape + `_ads_to_record` mapping (mock ADS).
    - `tests/ccm/test_context_extractor.py` — S2 context join on DOI/arXiv; abstract fallback; arXiv-intro regex.
    - `tests/ccm/test_pico_classifier.py` — parse `###LABEL`/`###CONFIDENCE`; quality mapping; OFFTOPIC/NONSUPPORTIVE drop.
    - `tests/ccm/test_dedup_and_trust.py` — `ccm_already_linked`; partial-unique-index conflict; end-to-end fixture that drives a seeded claim from `unverified` → `consensus` through `recalculate_trust_v2` (the §7 walkthrough as an assertion).

Estimated effort: ~4 h schema+models+migration, ~5 h `ccm.py` orchestration + extractor tiers, ~2 h prompt registry + Pico parse, ~2 h dedup/trust wiring, ~3 h tests, ~1 h beat/config. Kun owns seed YAML authoring + dry-run sign-off out-of-band.

---

## 11. Final Position

CCM is not a new trust mechanism and must not become one. The live `recalculate_trust_v2` already encodes the correct epistemics: a claim is Consensus when it has ≥3 non-stale supporting papers, zero challenges, and recent corroboration. Baseline historical claims fail this today only because their corroboration is *implicit* — buried in the introductions of the modern papers that build on them — rather than written as standalone re-proofs. CCM's sole job is to surface that implicit corroboration: query ADS for who cites the seminal work *now*, fetch the citing sentence, let Pico confirm it is a standard supportive invocation, and write it as ordinary `supports` evidence through the existing insert/dedup/audit path. The trust function then greens the claim on its own, legitimately, and the freshness floor keeps it green only as long as the modern literature keeps citing it — which, for genuine textbook facts, it perpetually will.

The implementation is low-risk and reversible: no trust code changes, no existing-table column changes, source-channel-tagged rows for clean rollback, and a blocking dry-run gate before the first write. The single largest correctness dependency is Pico's three-way discipline (SUPPORTIVE vs NONSUPPORTIVE vs OFFTOPIC); §6 and §9 harden it, and the `n_challenges == 0` gate means even a Pico miss cannot green a truly contested claim.

— Kun 🔬
