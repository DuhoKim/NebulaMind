# Dynamic Citations — Design v1

**Author:** Kun  
**Date:** 2026-06-07  
**Status:** Draft for Tori implementation  
**Live grounding:** Read against local NebulaMind repo on 2026-06-07. Key paths: `backend/app/agent_loop/autowiki/proposers.py` (coherence prompt at line 1808, `propose_section_rewrite`), `backend/app/agent_loop/autowiki/tasks.py` (`sonnet_section_rewrite`, `synthesize_renovation`), `frontend/src/app/wiki/[slug]/WikiPageClient.tsx` (claim marker renderer at line 107, `ClaimAnnotatedSpan` at line 190). Prior empirical context: `evidence` table has 11,809 rows with `authors` (JSON array) and `year`; `references` table is empty; page 57 oscillated between 0 and 193 inline parentheticals between reads during this session.

---

## 1. Executive Summary

NebulaMind wiki pages currently contain hardcoded in-prose parenthetical citations of the form `(White & Rees 1978)`, `(Springel et al. 2005)`. These are:

- **Volatile.** Between two consecutive reads of page 57 this session, the count went 193 → 0 as the rewrite cycle ran. The coherence prompt at line 1808 instructs the LLM to "Preserve all inline citations," which it routinely fails.  
- **Unmaintainable.** There is no DB link between `(Springel et al. 2005)` and the `evidence` row that has the DOI. When the prose rewrites, the link is gone.  
- **Not interactive.** Readers cannot hover to see the paper title, DOI, or trust annotation.

The fix: **Pristine Prose + Dynamic Citations.** Prose is scrubbed of all parentheticals. Evidence linkage lives in DB. The frontend renders interactive sequential superscripts `[1]` `[2]` ... on demand, backed by the same `evidence` rows the claim system already uses.

This design covers:
1. DB schema for citation link storage  
2. Aligner/Scrubber script (Tori implementation target) for one-time scrub + ongoing wiring  
3. Frontend UX for dynamic `[n]` overlay  
4. Prompt updates for the autowiki synthesis pipeline  
5. Platoon assignment

---

## 2. Problem Framing

### 2.1 Empirical state

| Metric | Value |
|---|---|
| `evidence` rows with `authors` + `year` | 11,809 |
| `evidence` rows with `doi` | ~11,436 |
| `references` table rows | 0 (empty; all backing data is in `evidence`) |
| Parentheticals on page 57 during this session | 193 → 0 (rewrite erased them) |
| Regex pattern `\([A-Z][a-zA-Z\-]+(?:\s+et\s+al\.?)?\s*(?:&\s*[A-Z][a-zA-Z]+)?\s+\d{4}[a-z]?\)` | captures authentic citations; false-positives from physics quantities (1804, 2032) require year-range filter (1900–2030) |

The root cause is that parentheticals are an LLM-generated side-effect, not a DB-backed artifact. They exist when the current rewrite agent remembered to write them; they vanish when it didn't. There is no reconciliation.

### 2.2 What the claim system already proves

The frontend already handles `<!--claim:N-->...<!--/claim:N-->` markers: `WikiPageClient.tsx:107` strips and re-renders them as interactive underlined spans with popovers. Evidence for claims is fetched via `/api/claims/:id/evidence`. The citation layer is architecturally identical — a different marker type, a different popover, the same evidence table.

### 2.3 What this design does NOT change

- The `claims` system and `<!--claim:N-->` markers are untouched.  
- Evidence rows are not modified; the new `page_citation_links` table is a join layer only.  
- `evidence.claim_id` is the existing linkage; this design adds a page-level citation index.  
- No Wikipedia-style `<ref>` tag format; we use HTML comment markers consistent with the existing `<!--claim:N-->` convention.

---

## 3. Database / Schema

### 3.1 New table: `page_citation_links`

```sql
CREATE TABLE page_citation_links (
  id                 SERIAL PRIMARY KEY,
  page_id            INT NOT NULL REFERENCES wiki_pages(id) ON DELETE CASCADE,
  evidence_id        INT NOT NULL REFERENCES evidence(id) ON DELETE CASCADE,
  author_year_key    VARCHAR(120) NOT NULL,
  -- Normalised key extracted from prose, e.g. "Springel et al. 2005"
  match_method       VARCHAR(32) NOT NULL,
  -- 'exact_key', 'fuzzy_author_year', 'doi_lookup', 'manual'
  match_confidence   FLOAT NOT NULL DEFAULT 1.0,
  created_at         TIMESTAMP DEFAULT NOW(),
  updated_at         TIMESTAMP DEFAULT NOW(),
  UNIQUE (page_id, author_year_key)
);

CREATE INDEX ix_page_citation_links_page ON page_citation_links(page_id);
CREATE INDEX ix_page_citation_links_evidence ON page_citation_links(evidence_id);
```

One row per unique `(page_id, author_year_key)`. The same evidence row can appear under different keys if the prose uses different forms (e.g., "White & Rees 1978" vs. "White and Rees 1978"); deduplication by `evidence_id` happens at render time.

### 3.2 Marker convention in prose

Citation placeholders in `wiki_pages.content` use the form:

```
<!--cite:EVIDENCE_ID-->
```

For example: `Hierarchical merging drives early-type morphologies<!--cite:8550-->.`

Rules:
- A single self-closing comment; no closing tag (unlike `<!--claim:N-->...<!--/claim:N-->`).
- Placed **immediately after** the sentence or clause being cited, **before** the period if mid-sentence, **after** the period if end-of-sentence. Follow Wikipedia convention: superscript after punctuation.
- Multiple evidence rows for the same assertion: comma-separated IDs `<!--cite:8550,8554-->`.
- Never inside headings, code fences, link text, or math spans.

### 3.3 Existing schema checks (no migration needed)

| Check | Result |
|---|---|
| `evidence.authors` | TEXT, stores JSON array of author name strings |
| `evidence.year` | INTEGER, populated for 11,809/11,880 rows |
| `evidence.doi` | VARCHAR, populated for ~11,436 rows |
| `evidence.arxiv_id` | VARCHAR, populated for most rows |
| `evidence.title` | TEXT, populated |
| `wiki_pages.content` | TEXT, holds markdown with `<!--claim:N-->` markers already |

No changes to `evidence`, `claims`, or `wiki_pages` columns. The only migration is `CREATE TABLE page_citation_links`.

---

## 4. Aligner/Scrubber Script — Spec for Tori

### 4.1 Purpose

A Python script `scripts/align_citations.py` that:

1. Extracts all parenthetical citation keys from prose.
2. Matches each key to an `evidence` row.
3. Replaces matched keys with `<!--cite:EVIDENCE_ID-->` in-place.
4. Writes matched mappings to `page_citation_links`.
5. Leaves unmatched keys unchanged (logged for manual review).

This script runs once as a backfill, then again after any coherence rewrite that may have re-introduced parentheticals (triggered by the post-rewrite hook described in §4.5).

### 4.2 Extraction step

Regex (Python):

```python
CITE_PATTERN = re.compile(
    r'\(([A-Z][a-zA-Z\-]+(?:\s+et\s+al\.?)?'      # first author / "et al."
    r'(?:\s*[,;&]\s*[A-Z][a-zA-Z\-]+)*)'            # optional co-authors
    r'\s+((?:19|20)\d{2}[a-z]?)\)',                  # year 1900-2029 + optional letter
    re.UNICODE
)
```

Year range `(?:19|20)\d{2}` eliminates false positives from physical quantities like `(T ~ 1800 K)` or `(z ~ 2032)`.

For each match, normalise: strip trailing letter suffix (`2005a` → `2005`), strip `et al.` suffix variants, strip punctuation. Canonical key example: `Springel et al. 2005`.

### 4.3 Matching algorithm (cascade)

For each unique `author_year_key` on a page:

**Stage 1 — Exact key match** (free):  
Generate the first author's last name `last` and `year`. Query:
```sql
SELECT id, authors, year FROM evidence
WHERE year = :year
  AND authors::text ILIKE '%' || :last || '%'
ORDER BY quality DESC NULLS LAST
LIMIT 5
```
Compute normalised first-author match score (Levenshtein ≤ 2 on last name). If a single candidate scores ≥ 0.9, record as `match_method='exact_key'`, confidence 1.0.

**Stage 2 — Fuzzy author + year** (Python, `rapidfuzz`):  
For candidates surviving Stage 1 with score < 0.9, compute `rapidfuzz.fuzz.partial_ratio` on the full first-author string. Accept at ≥ 80; record as `match_method='fuzzy_author_year'`, confidence = score/100.

**Stage 3 — Title keyword fallback** (expensive, rare):  
If Stage 2 has no winner and the claim text on the page contains a paper title fragment (≥ 4 words), query `evidence` by full-text similarity. Use only for unlocked claim markers on pages with < 30% match rate; cap at 5 calls per script run.

**Unmatched keys:** leave the parenthetical in prose unchanged. Write to a log table or JSON report file. Do not replace; do not silently drop.

### 4.4 Replacement step

After all matches for a page are resolved:

1. Build a `{raw_match_string: evidence_id}` dict.
2. Walk the page content and replace each `(Author et al. Year)` match with `<!--cite:EVIDENCE_ID-->`, right after the matched string (i.e., the closing `)` is removed).
3. Apply replacements in reverse document order (by match.end()) so offsets don't shift.
4. Validate: assert no original parenthetical pattern survives in replaced positions.
5. Write a new `page_versions` row and update `wiki_pages.content`.

Example transformation:
```
Before: "Hierarchical merging is universal (White & Rees 1978)."
After:  "Hierarchical merging is universal<!--cite:8550-->."
```

### 4.5 Post-rewrite hook

Add an emit after every `wiki_pages.content` commit in:
- `tasks.py:sonnet_section_rewrite` (after DB commit)
- `tasks.py:synthesize_renovation` (after DB commit)
- `routers/pages.py:update_page_content` (after DB commit)

Emit: `CITATION_SCRUB_REQUIRED` → Celery task `align_citations_page(page_id)`.

The Celery task calls the same cascade above but in scan-and-repair mode: it only processes parentheticals that are not already replaced. If the prompt updates (§6) work correctly, there will be nothing to replace; the task is a safety net.

### 4.6 Script CLI

```bash
python3 scripts/align_citations.py \
  --page-id 57                  # single page
  --all-pages                   # full corpus backfill
  --dry-run                     # print matches, do not write
  --report citations_report.json
```

`--dry-run` output per page: `{page_id, total_parentheticals, matched, unmatched, sample_unmatched: [...]}`.

### 4.7 Acceptance criteria for the script

| Criterion | Target |
|---|---|
| Page 57 match rate (if parentheticals present) | ≥ 75 % of extracted keys |
| False-positive rate (wrong evidence ID mapped) | ≤ 5 % on manual spot-check of 20 |
| No parenthetical pattern surviving in replaced positions | 100 % |
| Markdown round-trip (parse → replace → parse) | AST structure unchanged modulo comment nodes |
| Idempotency: running twice yields identical content | 100 % |

---

## 5. Frontend UX — Dynamic `[n]` Overlay

### 5.1 Rendering pipeline

The frontend already parses `<!--claim:N-->` comments via regex in `WikiPageClient.tsx:107`. Citation markers follow the same path but with different rendering:

1. **Parser pass:** scan rendered HTML for `<!--cite:(\d+(?:,\d+)*)-->` comment nodes.
2. **Numbering:** assign sequential numbers `[1]`, `[2]`, ... on first occurrence in document order. Second occurrence of the same `evidence_id` reuses its earlier number (duplicate suppression).
3. **Inject:** replace the comment node with `<sup class="cite-n" data-cite-ids="8550,8554">[1]</sup>`.
4. **References section:** append an auto-generated `## References` div at page bottom with numbered entries. This div is not stored in `wiki_pages.content` — it is assembled at render time from `page_citation_links` rows (fetched via a single `/api/pages/:slug/citations` endpoint).

### 5.2 Popover on `[n]` tap/hover

Same `ClaimAnnotatedSpan` pattern, new component `CitationPopover`:

```tsx
interface CitationPopoverProps {
  evidenceIds: number[];     // from data-cite-ids
  seqNumbers: number[];      // [1], [2] etc.
}
```

Popover content:
- Paper title (linked to DOI/arXiv URL if available)
- Authors (first two + "et al." if > 2)
- Year + journal ref if present
- Brief abstract excerpt (first 120 chars of `evidence.summary`)

No trust annotation shown in citation popovers — trust belongs to the claim layer.

### 5.3 New API endpoint

```
GET /api/pages/:slug/citations
```

Response:
```json
{
  "citations": [
    {
      "seq": 1,
      "evidence_id": 8550,
      "author_year_key": "White & Rees 1978",
      "title": "Core condensation in heavy halos...",
      "authors": ["Simon D. M. White", "Martin J. Rees"],
      "year": 1978,
      "doi": "10.1093/mnras/183.3.341",
      "arxiv_id": null,
      "url": "https://doi.org/10.1093/mnras/183.3.341"
    },
    ...
  ]
}
```

Backed by `SELECT pcl.*, e.* FROM page_citation_links pcl JOIN evidence e ON e.id = pcl.evidence_id WHERE pcl.page_id = :page_id ORDER BY pcl.id`.

The frontend fetches this list once on page load and builds the `evidence_id → seq` mapping before the first render.

### 5.4 "Citation View" toggle

The existing Citation View toggle (`WikiViewToggle.tsx`) already controls visibility of claim underlines. Citation `[n]` superscripts should be **always visible** (not gated behind Citation View), since they are navigational — a reader cannot discover citations if the toggle is off by default. Claim underlines remain toggle-controlled.

### 5.5 References div

Auto-rendered at page bottom when the page has citations:

```html
<section class="nm-references">
  <h2>References</h2>
  <ol>
    <li id="ref-1"><a href="https://doi.org/...">White & Rees 1978</a> — Core condensation in heavy halos...</li>
    ...
  </ol>
</section>
```

This section is purely frontend-generated and is excluded from markdown storage, `page_versions`, and LLM prompts. It does not pollute the prose that models read.

### 5.6 Mobile / no-JS fallback

If popover JS fails to load, `<sup>[n]</sup>` still links to `#ref-n` in the references section at page bottom. Pure anchor navigation. Acceptable degradation.

---

## 6. Prompt Updates — Autowiki Synthesis Pipeline

Three prompt surfaces must change. The principle: **models write prose; the frontend renders citations. Models must not generate `(Author et al. Year)` strings — they use evidence IDs.**

### 6.1 Coherence system prompt (`proposers.py:1808`)

**Remove:**
```
- Preserve all inline citations in form (Author et al. Year). Do not invent.
```

**Replace with:**
```
- DO NOT write inline citations in (Author et al. Year) format. Evidence is linked via <!--cite:N--> markers.
- When your prose asserts a claim backed by a specific paper, insert <!--cite:EVIDENCE_ID--> immediately after the assertion (before or after the period, following Wikipedia superscript convention). Use only evidence IDs provided in the EVIDENCE MAP below.
- If no evidence ID is available for an assertion, write the assertion without any citation marker.
- DO NOT invent author names, years, or evidence IDs.
```

In the user template, add an `EVIDENCE MAP` block (injected at prompt build time from `page_citation_links` for this page):

```
EVIDENCE MAP (use these IDs in <!--cite:N--> markers):
  8550 → White & Rees 1978: Core condensation in heavy halos...
  8554 → Parker et al. 2011: Characterization of Ultra-wide Trans-Neptunian Binaries...
  ...
```

This map is built by `SELECT pcl.author_year_key, e.id, e.title FROM page_citation_links pcl JOIN evidence e ON e.id=pcl.evidence_id WHERE pcl.page_id=:page_id` — it lists only pre-scrubbed, already-matched evidence for this page, so models never invent IDs.

### 6.2 Section rewrite prompt (`proposers.py:propose_section_rewrite`)

Same change as §6.1 for the section-level prompt. Add a local `EVIDENCE MAP` filtered to evidence linked to claims in this section only (via `evidence.claim_id → claims.page_id + claims.section`).

The section-level map is typically 10–30 entries; manageable within a 2 k-token budget.

### 6.3 `sonnet_section_rewrite` in `tasks.py`

This path builds its own prompt independently of `proposers.py`. Apply the same substitution:
- Strip any "preserve (Author et al. Year)" instruction.  
- Add the "use `<!--cite:N-->` only from the EVIDENCE MAP" rule.  
- Inject the page-level evidence map (50-row cap; truncate to highest `evidence.quality` if more).

### 6.4 `synthesize_renovation` in `tasks.py`

Same change as §6.3. Additionally: before the renovation synthesis, run `align_citations_page` on the page to ensure `page_citation_links` is current. This guarantees the evidence map is populated before the synthesiser runs.

### 6.5 Deep synthesis (`autowiki/deep_synthesis.py`)

Add the same prohibition and evidence map injection. Deep synthesis produces full-page content; the evidence map should be the full page-level set (no section filter).

### 6.6 Prompt helper: `_build_evidence_map(page_id, max_rows=80)`

A shared utility (new file `app/agent_loop/autowiki/citation_context.py`) used by all prompt-building paths:

```python
def build_evidence_map(db, page_id: int, max_rows: int = 80) -> str:
    rows = db.execute("""
        SELECT pcl.evidence_id, pcl.author_year_key, e.title
        FROM page_citation_links pcl
        JOIN evidence e ON e.id = pcl.evidence_id
        WHERE pcl.page_id = :pid
        ORDER BY e.quality DESC NULLS LAST
        LIMIT :n
    """, {"pid": page_id, "n": max_rows}).fetchall()
    if not rows:
        return ""
    lines = [f"  {r.evidence_id} → {r.author_year_key}: {r.title[:80]}" for r in rows]
    return "EVIDENCE MAP (use these IDs in <!--cite:N--> markers):\n" + "\n".join(lines)
```

Returns `""` if no links exist (first run before scrub); models gracefully omit citations rather than hallucinating.

### 6.7 Renovation QA verifier — MUST retarget (blocking)

**Critical dependency Tori must not miss.** `verify_renovation` in `tasks.py` (≈ lines 3308–3338) gates every section write on inline `[arXiv:...]` citations:
- The QA prompt (`QA_SYSTEM`) requires "at least 3 inline citations (format: [arXiv:XXXX])".
- The structural fallback computes `citation_count = len(re.findall(r"\[arXiv:", section))` and emits `FAIL` unless `citation_count >= 2`.

Once synthesis emits `<!--cite:N-->` instead of `[arXiv:ID]`, this gate fails **every** section and blocks all renovation writes. Both checks must be retargeted in the same PR as the §6.3–6.5 prompt changes:
- QA prompt: replace the `[arXiv:...]` citation requirement with "at least 2 `<!--cite:N-->` markers referencing IDs from the evidence map."
- Structural fallback: change the regex to `r"<!--cite:\d+-->"` and keep the `>= 2` floor.
- Transitional safety: accept **either** pattern (`[arXiv:` OR `<!--cite:`) during rollout so partially-migrated pages don't hard-fail. Drop the legacy branch after backfill completes.

Same audit applies to any other verifier counting `\[arXiv:` (grep the renovation/autowiki paths before deploy). This is the single most likely cause of a silent "no sections ever commit" regression.

---

## 7. Migration & Backfill Sequence

Execute in this order:

1. **Migration:** `CREATE TABLE page_citation_links` (§3.1).  
2. **Dry-run audit:** `python3 scripts/align_citations.py --all-pages --dry-run --report /tmp/citations_dryrun.json`. Review unmatched rate before committing.  
3. **Backfill scrub:** `python3 scripts/align_citations.py --all-pages`. Verify `page_citation_links` row count, spot-check 3 pages.  
4. **Prompt updates:** deploy §6.1–6.5 changes. This is a code deploy; no data migration needed.  
5. **Post-rewrite hook:** wire `CITATION_SCRUB_REQUIRED` events at the three emit sites (§4.5). Deploy with prompt updates in the same PR.  
6. **Frontend:** deploy `CitationPopover`, `[n]` injection, `/api/pages/:slug/citations` endpoint, references section.  
7. **Verification:** re-read page 57 before and after a rewrite cycle. Assert: no parentheticals survive; `<!--cite:N-->` markers are stable; frontend renders `[1]...[n]`.

---

## 8. Platoon Assignment

| Step | Owner model | Host | Reason | Cost |
|---|---|---|---|---|
| DB migration (`CREATE TABLE page_citation_links`) | Tori / Python deterministic | Mac Studio | Schema change; no model needed | $0 |
| Extraction regex + key normalisation | Python deterministic | Mac Studio | Deterministic; no model | $0 |
| Stage 1–2 matching (exact + fuzzy) | Python (`rapidfuzz`) | Mac Studio | 50 ms/page; local library | $0 |
| Stage 3 title-keyword fallback | Claude Sonnet 4.6 | Cloud | Used rarely (< 5 % of keys); needs semantic title matching | ~$0.01/page |
| Replacement + validation | Python deterministic | Mac Studio | AST manipulation, idempotent | $0 |
| Evidence map injection at prompt build time | Python deterministic | Mac Studio | DB query + string formatting | $0 |
| Coherence/section-rewrite synthesis with `<!--cite:N-->` | Claude Sonnet 4.6 (cloud) / AstroSage-70B (local fallback) | Mac Studio | Existing synthesis platoon unchanged; only prompt text changes | Cloud-paid |
| Frontend `CitationPopover` + reference section | Tori | Mac Studio | React component, no model | $0 |
| `/api/pages/:slug/citations` endpoint | Tori | Mac Studio | SQLAlchemy query + serialisation | $0 |
| Dry-run audit review | Kun | Mac Pro | Unmatched-key analysis; threshold calibration | Cloud-paid |
| Post-deploy verification | Kun | Mac Pro | Spot-check pages + regex audit | Cloud-paid |

### 8.1 Hardware constraints

`align_citations.py` and all DB work run entirely on Mac Studio. No Buddle/Rakon involvement; no Mac Pro Ollama calls needed. The only cloud cost is Stage 3 fallback (rare) and the updated synthesis prompts (unchanged model assignment from existing pipeline).

---

## 9. Quality Gates & Anti-Patterns

### 9.1 Match quality gate

Before writing any scrubbed page to `wiki_pages.content`:
- Abort if match rate < 40 % (too many parentheticals left → something is wrong with the extraction).
- Warn (do not abort) if match rate < 75 %.
- Log every unmatched key to `page_citation_links_unresolved` table or JSON file for manual follow-up.

### 9.2 No marker in forbidden sites

Identical deny-list to claim markers (§3.3 of `claim_marker_embed_design_v1.md`): no `<!--cite:N-->` inside headings, code fences, link text, math spans, or emphasis runs.

### 9.3 Multi-vote / duplicate suppression

A single evidence ID must appear only once per cite comment. If the same evidence supports two consecutive claims, use two separate `<!--cite:N-->` comments (which render as the same `[n]`). Never emit `<!--cite:N,N-->` (duplicate ID in list).

### 9.4 Anti-pattern: evidence map hallucination

Models must only use IDs from the EVIDENCE MAP provided in the prompt. Add a post-write validator: scan new content for `<!--cite:(\d+)-->`, verify each ID exists in `page_citation_links` for this page. If any unknown ID appears, strip it (do not reject the whole write) and log `hallucinated_cite_ids`.

### 9.5 Interaction with claim markers

`<!--claim:N-->...<!--/claim:N-->` and `<!--cite:N-->` are independent layers. Both can coexist on the same sentence:

```
AGN feedback suppresses star formation in massive halos<!--cite:8550--><!--claim:1471--> at z > 1.<!--/claim:1471-->
```

The frontend processes claim markers first (wrap in `<span data-claim-id>`), then processes citation markers (inject `<sup>[n]</sup>`). Order matters; citation injection should run on the post-claim-span HTML.

---

## 10. Open Questions

| # | Question | Default |
|---|---|---|
| 1 | Should the References section be appended to `wiki_pages.content` or purely frontend-rendered? | **Frontend-only.** Keeps prose clean; models never see or preserve it. |
| 2 | Should unmatched parentheticals be stripped silently or left in prose? | **Left in prose** with a log. Silently stripping breaks evidence trail. Revisit after first backfill audit. |
| 3 | Citation View toggle: should `[n]` superscripts be always visible or toggle-controlled? | **Always visible** (navigation affordance). |
| 4 | Should `evidence.claim_id` be used to pre-populate `page_citation_links` before the scrub? | **Yes** — a cheap bootstrap: for each `evidence` row linked to a `claim` on a page, insert a placeholder `page_citation_links` row with `match_method='claim_evidence_bootstrap'`. This ensures the evidence map is non-empty on first synthesis run even before any prose parentheticals exist. |
| 5 | Cap on evidence map tokens in prompts? | **80 rows** (~1200 tokens). Reduce to 40 for section-scoped prompts. |

---

## 11. Implementation Checklist for Tori

In dependency order:

1. **Schema** — `CREATE TABLE page_citation_links` migration.
2. **Bootstrap** — populate `page_citation_links` from existing `evidence.claim_id` links (question 4 above, `match_method='claim_evidence_bootstrap'`).
3. **Script: `scripts/align_citations.py`** — extraction, cascade matching (§4.2–4.3), replacement, DB upsert, JSON report.
4. **Dry-run audit** — run `--all-pages --dry-run`, send report to Kun for threshold review.
5. **Backfill scrub** — run `--all-pages` after Kun sign-off.
6. **Prompt updates** — modify the four prompt surfaces (§6.1–6.5); add `citation_context.py` helper.
6b. **Retarget renovation QA verifier** (§6.7) — switch `verify_renovation` citation count from `[arXiv:` to `<!--cite:` (accept both during rollout). **Blocking:** skip this and no section ever commits.
7. **Post-rewrite hook** — wire `CITATION_SCRUB_REQUIRED` at three emit sites.
8. **Celery task: `align_citations_page(page_id)`** — repair-mode wrapper around the script.
9. **API: `GET /api/pages/:slug/citations`** — SQLAlchemy query + Pydantic response model.
10. **Frontend: `CitationPopover`** — component with popover, seq number assignment, `[n]` superscript injection.
11. **Frontend: References section** — auto-appended div from citations API response.
12. **Frontend integration** — wire into `WikiPageClient.tsx`: parse `<!--cite:N-->`, inject superscripts, always-visible (not behind Citation View toggle).
13. **Validator** — post-write scan for hallucinated cite IDs (§9.4).
14. **Tests:**
    - `tests/citations/test_align_script.py` — extraction regex, cascade matching, idempotency.
    - `tests/citations/test_citation_api.py` — endpoint with known fixtures.
    - Frontend: `CitationPopover.test.tsx` — popover rendering, seq number dedup.

Estimated effort: 5–7 h backend (script + API + hooks) + 3 h frontend (popover + references) + 2 h prompt updates + 1 h validation testing.

---

## 12. Final Position

The parenthetical citation problem is architectural, not cosmetic. The LLM cannot reliably maintain `(Author et al. Year)` strings across rewrites — the evidence session data proves this. Moving citation linkage into the DB and rendering it dynamically is the only stable architecture. It also improves the reader experience (interactive superscripts with paper titles) and keeps prose clean for future model rewrites.

The implementation is low-risk: no existing tables are modified, the claim system is untouched, and the frontend change is additive. The biggest variable is the match rate during the initial backfill scrub; the dry-run audit gate before commit ensures we do not silently degrade pages.

— Kun
