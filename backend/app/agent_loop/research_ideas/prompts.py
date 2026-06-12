"""LLM prompts for the Research Ideas pipeline (§3.3 of design doc)."""

RAKON_SKELETON_PROMPT = """You are a senior astronomy research strategist. Given a wiki
page's claims, debates, and recent literature, generate 12 candidate research
questions, each anchored to a SPECIFIC combination of observational surveys.

WIKI PAGE
---------
Title: {title}
Slug: {slug}
Tagline: {hero_tagline}

ESTABLISHED CLAIMS (top 20 by trust):
{claims_block}

ACTIVE DEBATES (claim_type='debate'):
{debates_block}

RECENT LITERATURE (last 365 days, page-tagged):
{arxiv_block}

SURVEY COVERAGE — claims with explicit survey mention:
{survey_coverage_block}
  e.g.  JWST: 14 claims, 3 debates ;  DESI: 9 claims, 2 debates ; ...

EXISTING IDEAS ON THIS PAGE (do NOT duplicate):
{existing_ideas_block}

ALLOWED SURVEY COMBOS (use exactly two):
JWST+DESI, JWST+Euclid, JWST+ALMA, JWST+HSC, JWST+LSST, JWST+VLA,
DESI+Euclid, DESI+HSC, DESI+ALMA, DESI+LSST,
ALMA+Euclid, ALMA+HSC, ALMA+LSST, ALMA+VLA,
Euclid+HSC, Euclid+LSST,
HSC+LSST, LSST+VLA

OUTPUT FORMAT — strict JSON, no prose:
{{
  "skeletons": [
    {{
      "combo": "JWST+DESI",
      "question": "<1-sentence research question, falsifiable>",
      "why_now_skeleton": "<2-3 sentences: which debate or recent papers create the gap>",
      "approach_skeleton": "<3-5 sentences: what data, what cuts, what measurement, expected N>",
      "anchors": {{
        "claim_ids": [<ids from claims_block>],
        "debate_ids": [<ids from debates_block>],
        "arxiv_ids": ["<arxiv ids from arxiv_block>"]
      }}
    }},
    ...12 total...
  ]
}}

CONSTRAINTS:
- Each question MUST be answerable by combining the two named surveys; do not
  propose questions either survey can answer alone.
- Each question MUST reference at least 1 claim_id OR 1 debate_id from this page.
- Each question SHOULD reference at least 1 arxiv_id when one is relevant.
- Spread combos: at most 3 ideas per single combo.
- No vague verbs ("understand", "explore"). Use measurable verbs ("measure",
  "constrain", "test whether", "rule out").
- No ideas requiring data that does not yet exist (e.g. "LSST DR2" if LSST
  hasn't released DR1).
- If you cannot generate 12 high-quality ideas, generate fewer — quality over quota.
"""

ASTROSAGE_POLISH_PROMPT = """You are an astronomy domain expert reviewing a draft
research idea. Rewrite for domain precision. Reject if implausible.

DRAFT
-----
Survey combo: {combo}
Question: {question}
Why now (skeleton): {why_now_skeleton}
Approach (skeleton): {approach_skeleton}

WIKI PAGE CONTEXT
-----------------
{title} — {hero_tagline}

Top 5 page claims:
{claims_block_5}

TASK:
1. Rewrite "why_now" in 2-3 sentences using domain-precise framing:
   reference quantitative findings (z range, mass bin, sample size) where
   possible. Cite paper titles from the anchors where applicable.
2. Rewrite "approach" in 3-5 sentences with concrete observational specifics:
   instrument mode (e.g. JWST/NIRSpec MOS, DESI BGS-Bright), wavelength /
   band, expected sample size, the actual measurement (e.g. "sSFR-clumpiness
   correlation in 4 mass bins"), and dominant systematic.
3. Domain plausibility check — answer "plausible: yes/no". Reject if:
   - Sample sizes inconsistent with survey footprint / depth
   - Redshift or mass range outside what the surveys actually cover
   - Measurement assumes spectral feature outside instrument bandpass
   - Question already definitively answered (cite the paper if so)
4. Suggest 1-3 dominant systematics for the approach.

OUTPUT JSON:
{{
  "plausible": "yes" | "no",
  "rejection_reason": "<empty if yes>",
  "question": "<may slightly edit for precision, keep falsifiable>",
  "why_now": "<polished prose>",
  "approach": "<polished prose>",
  "systematics": ["<systematic 1>", "<systematic 2>", ...]
}}
"""

ATOM_SCORING_PROMPT = """Score this astronomy research idea on two axes.
Return JSON only.

IDEA
----
Survey combo: {combo}
Question: {question}
Why now: {why_now}
Approach: {approach}

ANCHORS
-------
Anchored to {n_claims} page claims, {n_debates} debates, {n_papers}
recent papers.

EXISTING ACTIVE IDEAS ON THIS PAGE
----------------------------------
{existing_ideas_short}

SCORING

novelty (0-1):
  1.0 — no existing paper on this exact combination; opens new axis
  0.7 — one or two related papers; idea pushes a clear extension
  0.4 — replication / refinement of recent published work
  0.1 — directly answered in last 24 months

feasibility (0-1):
  1.0 — both surveys have public DR covering this; tractable in <6 months
  0.7 — one DR public, other archival or proposed
  0.4 — requires new proposal cycle; multi-year horizon
  0.1 — needs surveys not yet operational, or 10-100x current sample

OUTPUT:
{{
  "novelty": <float 0-1>,
  "feasibility": <float 0-1>,
  "duplicates_existing_idea_id": <int or null>,
  "one_line_rationale": "<plain text>"
}}
"""
