# galaxy-evolution Coherence Pass — Brief for Rakon

**Author:** Kun 🔬
**Date:** 2026-05-16 14:30 KST
**For:** Rakon (deepseek-r1:671b on Mac Pro) — immediately after current `rakon:lock` releases.
**Goal:** transform fragmented 87,152-char page assembled by 4+ agents over 5 days into a single coherent review article — single voice, no duplicates, clean section flow with transitions.
**Scope:** **`wiki_pages.id = 57`** (galaxy-evolution) ONLY. Don't touch other pages.

---

## 1. Section audit (live, 2026-05-16 14:25 KST)

Page is **87,152 chars across 12 top-level (`##`) sections**, not 13 as the prompt suggested — the H1 `# Galaxy Evolution` is the title, not a section. 41 claims (26 accepted · 9 challenged · 5 debated · 1 consensus). Hero tagline is currently NULL.

| § | Section header | Chars | H3s | Action | Reason |
|---:|---|---:|---:|---|---|
| 1 | Overview & Historical Foundations | 6053 | 0 | **KEEP** (trim ref-list dump from end) | First section, scene-setting. Has a reference dump at end that breaks flow — move references to bottom of page. |
| 2 | Physical Mechanisms | 7658 | 2 | **KEEP + absorb §11's H3** | Gas Accretion + Star Formation Regulation. Absorb the orphan §11 H3 "Star-Forming Regions: Molecular Clouds to Stellar Birth" which is wildly misplaced under "DM Halos" today. |
| 3 | Dark Matter & Structure Formation | 8240 | 2 | **MERGE with §11** → "Dark Matter, Halos & Structure Formation" | §11 is "Dark Matter Halos and Galaxy Assembly" — duplicate scope. Merge into one coherent treatment. |
| 4 | Star Formation & Quenching | 6294 | 2 | **MERGE with §9** → "Star Formation, Quenching & Color Bimodality" | Main Sequence + Quenching is inseparable from Color Bimodality (green valley = quenching in progress). §9 currently a separate section is artificial. |
| 5 | AGN Feedback | 6885 | 2 | **MERGE with §7's "Contested Claims: AGN Feedback" H3** → "AGN Feedback & Quenching Debates" | Papa-flagged duplicate. §7 has a sub-section that fully overlaps with §5. Pull it back into §5. |
| 6 | Environmental Effects | 7735 | 1 | **KEEP as-is** | Well-bounded. Morphology-density, ram-pressure stripping. Only one H3; could use a second on tidal/galaxy harassment. |
| 7 | Observational Evidence of Galaxy Evolution | 7469 | 3 | **REWRITE** — strip AGN H3 (→§5), absorb §12's "High-Redshift Galaxies" H3, rename to "Observational Evidence & Multi-Wavelength Surveys" | Currently a kitchen-sink section with overlapping content. Becomes the surveys/instruments section. |
| 8 | Galaxy Scaling Relations | 6836 | 2 | **MERGE with §10** → "Galaxy Scaling Relations & Size Evolution" | Tully-Fisher / Faber-Jackson / Fundamental Plane / size growth are all empirical morphological relations — same conceptual unit. |
| 9 | Color Bimodality & Green Valley | 7021 | 3 | **MERGE into §4** (Star Formation & Quenching) | See §4. |
| 10 | Galaxy Size Evolution | 7623 | 3 | **MERGE into §8** | See §8. |
| 11 | Dark Matter Halos and Galaxy Assembly | 6795 | 1 (misplaced) | **MERGE into §3** + reassign H3 to §2 | Duplicate scope of §3. The only H3 ("Star-Forming Regions: Molecular Clouds to Stellar Birth") doesn't belong under DM halos — move to §2 Physical Mechanisms. |
| 12 | Galaxy Evolution: Established Findings and Open Questions | 8119 | 5 | **DECOMPOSE** — meta-section, doesn't belong | Papa-flagged. Has 5 H3s: "High-Redshift Galaxies" → §7. "The Bimodal Color Distribution" → §4 (duplicate of §9 content!). "Quantitative Facts:" → distribute inline across the page. "Open Debates:" → new dedicated section §9 in target. "References:" → page-bottom References block. |

### 1.1 Confirmed pathologies (Papa's list, verified)

- ✓ **Duplicate AGN treatment**: §5 (`## AGN Feedback`, 6885 chars) AND §7's `### Contested Claims: AGN Feedback and Quenching Mechanisms` — yes, full overlap.
- ✓ **§12 is a meta-section**: 8119 chars of redux content (5 H3s, 3 of which duplicate other sections; 2 of which — "Quantitative Facts:" and "Open Debates:" — should be distributed inline).
- ✓ **No transitions**: every section opens cold (e.g., §3 opens "The ΛCDM paradigm posits…" with zero connective tissue from §2's star-formation regulation discussion).
- ✓ **Mixed voice**: §4 opens with `### The Star-Forming Main Sequence ⏎ ⏎ The star-forming main sequence (SFMS) encodes a tight, near-linear correlation…` (AstroSage-formal). §1 ends with a bare reference list dump (Nutty/copy-paste). §12 has `### Quantitative Facts:` colon-prefixed list-headers (Sonnet's idiom). Inconsistent.
- ✓ **Reference handling is chaotic**: ref-list dumps at end of §1, §5, §12. Inline `[Author Year]` citations are inconsistent — some `(Author et al. 2018)`, some `Author et al. (2018)`, some `[Author 2018]`.

---

## 2. Merge map

```
CURRENT (12 sections, 87,152 chars)            →  TARGET (9 sections + References footer)
─────────────────────────────────────────────────────────────────────────────────────────
§1  Overview & Historical Foundations          →  §1  Overview & Historical Foundations
                                                    (ref-list dump moved to References)

§2  Physical Mechanisms                        →  §2  Physical Mechanisms
   + §11's H3 "Star-Forming Regions"               (gas accretion, SF regulation, +
                                                    molecular-cloud → stellar birth H3)

§3  Dark Matter & Structure Formation          →  §3  Dark Matter, Halos & Structure Formation
+ §11 Dark Matter Halos and Galaxy Assembly        (merged; redundancy eliminated)

§4  Star Formation & Quenching                 →  §4  Star Formation, Quenching & Color Bimodality
+ §9  Color Bimodality & Green Valley              (merged; SFMS → quenching pathways →
+ §12's "Bimodal Color Distribution" H3             color bimodality → green valley)

§5  AGN Feedback                               →  §5  AGN Feedback & Quenching Debates
+ §7's "Contested Claims: AGN Feedback" H3         (merged; one canonical AGN section)

§6  Environmental Effects                      →  §6  Environmental Effects
                                                    (kept as-is; minor expansion encouraged)

§8  Galaxy Scaling Relations                   →  §7  Galaxy Scaling Relations & Size Evolution
+ §10 Galaxy Size Evolution                        (merged; TFR/FJ/FP/size growth as one
                                                    empirical-relations section)

§7  Observational Evidence of Galaxy Evolution →  §8  Observational Evidence & Multi-Wavelength Surveys
   minus AGN H3 (→ §5 target)                       (rewritten; surveys, multi-λ instruments,
   + §12's "High-Redshift Galaxies" H3               high-z observational frontier)

§12 Established Findings and Open Questions    →  §9  Open Questions & Frontier Debates
   decomposed:                                      (decomposed §12 + Contested Claims pulled
   - "High-Redshift" H3 → §8                         from §7; ONLY content that isn't already
   - "Bimodal Color" H3 → §4                         on the page elsewhere)
   - "Quantitative Facts:" → distributed
   - "Open Debates:" → §9 target
   - "References:" → References footer
                                               →  References (page-bottom footer, consolidated
                                                    from §1/§5/§12 ref-list dumps + inline cites)
```

---

## 3. Target structure — 9 sections + References footer

```
# Galaxy Evolution

[hero paragraph: 2-3 sentences, currently missing — Rakon writes one]

## 1. Overview & Historical Foundations
   - The questions galaxy evolution asks (when, how, why galaxies change)
   - Historical milestones (Hubble morphology, deep surveys, lambda-CDM, JWST era)
   - Active subfields and their interfaces
   - [transition into §2]

## 2. Physical Mechanisms
   ### Gas Accretion and the Cold-Flow Paradigm
   ### Star Formation Regulation and the Main Sequence
   ### Molecular Clouds to Stellar Birth     (NEW — from §11's misplaced H3)
   - [transition into §3]

## 3. Dark Matter, Halos & Structure Formation
   ### The Stellar-to-Halo Mass Relation
   ### Galaxy Bias and Large-Scale Structure
   ### Hierarchical Halo Assembly             (merged from §11 content)
   - [transition into §4]

## 4. Star Formation, Quenching & Color Bimodality
   ### Star-Forming Main Sequence
   ### Quenching Pathways and Timescales
   ### Red Sequence, Blue Cloud, Green Valley  (merged from §9)
   - [transition into §5]

## 5. AGN Feedback & Quenching Debates
   ### The M–σ Relation and Co-evolution
   ### Radiative vs Kinetic Mode Feedback
   ### Contested Claims: causal vs correlative role of AGN  (merged from §7's H3)
   - [transition into §6]

## 6. Environmental Effects
   ### The Morphology-Density Relation
   ### Ram-Pressure Stripping
   ### Tidal Interactions and Harassment
   - [transition into §7]

## 7. Galaxy Scaling Relations & Size Evolution
   ### The Tully-Fisher Relation
   ### Faber-Jackson and the Fundamental Plane
   ### Size Growth and the Two-Phase Assembly Picture  (merged from §10)
   ### Major vs Minor Mergers: a Contested Partition
   - [transition into §8]

## 8. Observational Evidence & Multi-Wavelength Surveys
   ### Optical/NIR Surveys: SDSS, COSMOS, 3D-HST, CANDELS
   ### High-z Frontier: JWST and ALMA   (merged from §12's H3)
   ### Spatially-Resolved Spectroscopy: IFU and MaNGA
   - [transition into §9]

## 9. Open Questions & Frontier Debates
   ### Tension over JWST high-z stellar mass budgets
   ### Dust-obscured fraction of cosmic SFR density at z=4–7
   ### Compact "red nugget" → present-day elliptical pathway
   ### Bulge-growth: secular vs merger-driven
   ### Drivers of cosmic reionization
   (one short paragraph per open question — distill the page's 5 debated + 9 challenged claims into a clean enumerable list)

## References
   (alphabetized, consolidated from all section ref-dumps + inline citations.
    Format: standard author-year list. Drop duplicate refs.)
```

**Why 9 + References (not 8, not 10):**
- 8 would force §6 Environmental Effects into §3 or §7 — neither fits cleanly.
- 10 would re-split Color Bimodality from Quenching, undoing the §4 merge.
- 9 is the floor for a comprehensive astronomy review.

---

## 4. Constraints Rakon must preserve

These are HARD constraints. Violation = rollback.

1. **All 41 claims must remain attributable** — every claim currently on the page traces to a `claims` table row with `trust_level`. Rakon must not drop any claim's substantive content; it can rephrase but not delete. List of claim IDs (for Tori to validate post-write):
   ```
   SELECT id, trust_level, LEFT(text, 80) FROM claims WHERE page_id=57 ORDER BY id;
   ```
   Post-rewrite content must contain semantic equivalents of all 41 claims. Spot-check the 15 contested (debated + challenged) ones especially carefully.

2. **All inline citations preserved** — every `(Author Year)`, `Author et al. (Year)`, `Madau & Dickinson 2014`, etc., that currently appears must survive in the rewrite, in normalized form `(Author et al. Year)`. Do not invent new citations. Do not delete existing ones.

3. **All quantitative facts preserved** — every number (z, M_⊙, SFR, mass, scaling-relation slope, etc.) currently on the page must survive. Rakon may move a fact between sections during merge, but not delete or modify the value.

4. **Single unified voice** — "authoritative review article" style. Concrete prose, no rhetorical questions, no "we" first person, no "interestingly" or "remarkably" hedging. Past or present tense as appropriate. Match the §3 Physical Mechanisms tone (the most consistent section currently).

5. **Transitions between every section** — last sentence of each section connects forward to the next section's topic. Not a meta-transition ("In the next section we will…"). A *substantive* one: e.g., end of §4 mentions AGN-driven quenching → opens §5 with "AGN feedback operates in two primary modes…".

6. **No new claims invented** — Rakon must not add scientific claims not already on the page. The coherence pass is restructuring + rewriting prose, NOT adding new research.

7. **Markdown structure** — H1 stays `# Galaxy Evolution`, then H2 for each of §1–§9, H3 for sub-sections as listed in §3 above. Single newline between paragraphs, double newline before headings. References as `## References` footer.

---

## 5. Rakon prompt (drop-in, paste directly into `_call_rakon`)

```
SYSTEM PROMPT
=============

You are Rakon, a senior astronomy reviewer with deep expertise in galaxy
evolution. You are restructuring a Wikipedia-style review article that was
assembled by four different agents over five days. The result is fragmented,
duplicative, and inconsistent in voice. Your job: produce a single coherent
rewrite with a unified review-article voice, no duplicate content, and clean
transitions between sections.

You are NOT adding new scientific claims. You are NOT inventing new citations.
You are restructuring existing content with better organization and prose.

USER PROMPT
===========

Below is the current state of the "Galaxy Evolution" wiki page (87,152 chars,
12 fragmented sections). Rewrite it as a coherent review article using the
EXACT target structure provided.

TARGET STRUCTURE (use these 9 H2 sections + References footer, in this order):

1. ## Overview & Historical Foundations
2. ## Physical Mechanisms
   ### Gas Accretion and the Cold-Flow Paradigm
   ### Star Formation Regulation and the Main Sequence
   ### Molecular Clouds to Stellar Birth
3. ## Dark Matter, Halos & Structure Formation
   ### The Stellar-to-Halo Mass Relation
   ### Galaxy Bias and Large-Scale Structure
   ### Hierarchical Halo Assembly
4. ## Star Formation, Quenching & Color Bimodality
   ### Star-Forming Main Sequence
   ### Quenching Pathways and Timescales
   ### Red Sequence, Blue Cloud, Green Valley
5. ## AGN Feedback & Quenching Debates
   ### The M–σ Relation and Co-evolution
   ### Radiative vs Kinetic Mode Feedback
   ### Contested Claims: Causal vs Correlative Role of AGN
6. ## Environmental Effects
   ### The Morphology-Density Relation
   ### Ram-Pressure Stripping
   ### Tidal Interactions and Harassment
7. ## Galaxy Scaling Relations & Size Evolution
   ### The Tully-Fisher Relation
   ### Faber-Jackson and the Fundamental Plane
   ### Size Growth and the Two-Phase Assembly Picture
   ### Major vs Minor Mergers: A Contested Partition
8. ## Observational Evidence & Multi-Wavelength Surveys
   ### Optical/NIR Surveys: SDSS, COSMOS, 3D-HST, CANDELS
   ### High-z Frontier: JWST and ALMA
   ### Spatially-Resolved Spectroscopy: IFU and MaNGA
9. ## Open Questions & Frontier Debates
   (one short paragraph per debate, drawn from the page's contested claims)
## References
   (consolidated, alphabetized author-year list)

HARD CONSTRAINTS:
- Preserve all 41 substantive claims on the page (rephrase OK, delete NOT OK).
- Preserve all inline citations in form (Author et al. Year). Do not invent.
- Preserve all quantitative facts (z, M_⊙, slopes, fractions, dates). Do not modify.
- Single unified voice: authoritative astronomy review article. Concrete prose.
  Past or present tense as appropriate. No first-person "we". No rhetorical
  flourishes like "interestingly" or "remarkably". Match Physical Mechanisms tone.
- Transitions: last sentence of each section connects substantively forward.
- DO NOT invent new claims, datasets, instruments, or citations.
- DO NOT add a hero tagline (that is a separate task).

OUTPUT FORMAT:
- Markdown.
- H1 line: `# Galaxy Evolution` (already in source — keep verbatim).
- Then H2 sections in the order above.
- H3 sub-sections within each H2 as listed above.
- All references consolidated into a single `## References` footer.
- Single newline between paragraphs; double newline before headings.
- Total length target: 65,000–80,000 chars (current page is 87,152 — coherence
  pass typically tightens by 10–20%).

CURRENT PAGE CONTENT (87,152 chars):
=====================================

{full_page_content}

Now produce the rewritten page.
```

---

## 6. Pre-run checklist for Tori (before dispatching Rakon)

1. **Snapshot current page state** — write the current `wiki_pages.content` to a new `PageVersion` row so we can roll back:
   ```sql
   INSERT INTO page_versions (page_id, version_num, content, created_at)
   SELECT 57,
          COALESCE((SELECT MAX(version_num) FROM page_versions WHERE page_id=57), 0) + 1,
          content,
          NOW()
   FROM wiki_pages WHERE id = 57;
   ```

2. **Verify `rakon:lock` is released** before dispatching (current run holds it until ~15:25 KST per Papa). Wait until `redis-cli get rakon:lock` returns nil, then proceed.

3. **Use a long timeout** — `_ollama_chat(...,model=MODEL_RAKON, timeout=28800)` (8 h, per §7.2 B3 in `job_schedule_v1.md`). This single Rakon call may take 4–6 h given the 87k-char input.

4. **Dispatch:**
   ```python
   from app.agent_loop.research_ideas.auto_improvement import _ollama_chat, MODEL_RAKON, OLLAMA_MACPRO
   prompt = COHERENCE_PROMPT.format(full_page_content=current_content)
   result = _ollama_chat(OLLAMA_MACPRO, MODEL_RAKON, prompt, temperature=0.3, timeout=28800)
   ```

5. **Post-run validation gate** — before writing the result to `wiki_pages.content`, validate:
   - Length ≥ 50,000 chars (catches truncated output)
   - Contains all 9 expected `## ` H2 headings in correct order
   - Contains ≥ 35 of the 41 claim semantic equivalents (Atom-7b cosine ≥ 0.7 per claim against rewrite — fail if < 35)
   - Contains a `## References` footer
   - No banned phrases: "interestingly", "remarkably", "in this section we", "as we discussed"

   If any check fails → log to `autowiki_runs` with `decision='gate_reject'` + reason, do **not** overwrite the page.

6. **Atomic write** — wrap the page update + new PageVersion + autowiki_runs log in a single transaction.

7. **Post-write smoke test** — `sonnet-judge-tick` at the next 20-min slot should produce a higher q1 than today's 0.66 baseline (target ≥ 0.78). If q1 drops below 0.60, **rollback automatically** to the snapshot.

---

## 7. Platoon Assignment

| Step | Model | Why |
|---|---|---|
| §1 Audit (this doc) | (Kun, no LLM) | Static analysis of headings + Atom-7b cosine for duplicate detection |
| §5 Coherence rewrite | **Rakon (deepseek-r1:671b)** | The hardest step — needs to hold 87k chars of context and produce a coherent review-article rewrite. Only Rakon has the structural-reasoning depth + context capacity (after Tera ingestion fails because gemma3:27b's 128k context still chokes on the prompt+output combined). |
| §6.5 post-write validation | Atom-7b for cosine, Python for structural checks | Fast, free, local — same Atom that already gates research_ideas |
| §6.7 post-write q1 audit | sonnet-judge-tick (existing 20-min cadence) | Authoritative quality gate, cloud API. If sonnet rates < 0.60, rollback. |

— 🔬 Kun, 2026-05-16 14:30 KST
