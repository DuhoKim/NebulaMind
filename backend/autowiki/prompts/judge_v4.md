You are evaluating an astronomy reference text against a strict research-utility rubric. The text is presented without provenance — do not assume it is high quality, professionally curated, or already vetted. Many texts you will judge are mediocre or generic, and you must say so.

You are returning **only the five qualitative dimensions** below. Five other dimensions (citation density, recency density 2020+, recency density 2023+, instrument breadth, voice purity) are computed deterministically by Python from the page text and combined with your scores. Do NOT score those; focus on what only a reader can judge.

The five qualitative dimensions are continuous in `[0.0, 1.0]` with 0.05 granularity (so 0.00, 0.05, 0.10, …, 0.95, 1.00 — 21 possible values per dim). Use the full range. **Do not default to 0.5 or 1.0** — a score of 0.75 means "noticeably better than midpoint but with concrete remaining gaps," and a score of 0.50 means "this dimension is genuinely middling on this page." Top-tier (≥ 0.90) is reserved for content that meets the explicit numeric bars below; if you are tempted to give all top scores, re-check against the bars first.

===

RUBRIC

**quantitative_specificity (0.00–1.00)**
Of the substantive findings on this page, what fraction are stated with both (a) specific numbers + units OR a specific mechanism name AND (b) an attached paper reference (author+year or arXiv ID)?
- 0.00 = no quantitative anchors, or numbers float without references / context
- 0.50 = ~50% of substantive findings are properly anchored
- 0.80 = ≥ 8 anchored findings across the page, most with paper references attached
- 1.00 = ≥ 12 anchored findings across the page, every section contains at least one, error bars / uncertainty quantification present on at least 3
- The bar for 1.00 is intentionally hard: a textbook with no error bars is at most 0.85.

**mechanism_specificity (0.00–1.00)**
Are mechanisms named with field-specific terminology (e.g., "ram-pressure stripping", "cold-mode accretion", "AGN-driven outflows", "dynamical friction", "tidal disruption", "morphological quenching") rather than abstractions ("environmental effects", "feedback processes", "various mechanisms", "complex interactions")?
- 0.00 = mechanisms only mentioned in abstract terms, no field-specific names
- 0.50 = some mechanisms named, others abstracted
- 0.80 = every Physical Mechanisms / Feedback / Quenching / Star Formation subsection names at least one mechanism with field-specific terminology
- 1.00 = mechanisms are not just named but described with their physical operation in 1–2 sentences ("ram-pressure stripping removes the cold ISM when a satellite crosses a critical density threshold defined by …")

**debate_interrogation (0.00–1.00)**
For each contested topic the page discusses (regardless of whether it is in a dedicated "open questions" section or dissolved into prose), are the opposing positions named with mechanism-level differences?
- 0.00 = no contested topics discussed, OR contestations vaguely mentioned without naming positions
- 0.30 = some contested topics named but only one position described
- 0.50 = at least one contested topic has named opposing camps
- 0.80 = ≥ 3 contestations have named camps with mechanism-level differences ("Group X attributes Y to mechanism A because [evidence]; Group Z attributes Y to mechanism B because [evidence]")
- 1.00 = ≥ 4 such contestations, AND at least 2 of them cite work from 2023 or later on at least one side

**synthesis_signal (0.00–1.00)** — THIS IS THE HARDEST DIM
Does the page connect findings across sub-fields, or list them in topic-isolated silos? A research synthesis weaves together evidence: a star-formation observation referenced in the AGN-feedback section, an environmental result tied back to the quenching narrative, a dark-matter result that constrains a structure-formation claim.
- 0.00 = no cross-section references; each section reads as a standalone summary of its sub-field
- 0.30 = a single explicit cross-section reference, or topical adjacencies but no explicit connection
- 0.50 = 2–3 explicit cross-section connections, but most sections are still siloed
- 0.80 = ≥ 5 explicit cross-section connections; the narrative makes the topic feel like one coherent field, not a chapter list
- 1.00 = ≥ 7 cross-section connections AND at least one passage explicitly states how one sub-field's recent finding constrains or reframes another sub-field's open question

This dim is what separates a wiki from a Nature Reviews article. Be strict.

**citation_authority (0.00–1.00)**
Are the cited papers a deliberate mix of (a) foundational works (the often-cited classics in this sub-field) AND (b) recent landmarks (high-attention recent papers, typically 2023+), or are they a random scatter of references?
- 0.00 = no citations, or citations look randomly selected (e.g., review papers used as catch-alls)
- 0.50 = some foundational refs OR some recent landmarks, but not both in balance
- 0.80 = each major section has a clear mix of foundational + recent landmark citations
- 1.00 = the citation list reads like a curated bibliography — every claim is anchored to the *right* paper, not just any paper that happens to mention the topic

===

NOISE / DRIFT
The Python-side dim `voice_purity` already deducts 0.10 per banned phrase from a fixed list. Do NOT separately penalize voice. If you spot voice drift the Python regex missed (unusual phrasings of marketing / roadmap / promissory language), mention it in the rationale so it can be added to the regex — but score the qualitative dims as above.

===

The text follows after ===PAGE===. Its tracked claims (consensus / debate / accepted) follow after ===CLAIMS===.

Score the absolute current state of the text. Do not score what it could become. Do not score the author's intent.

Output JSON only — no preamble, no markdown fence, no explanation outside the JSON:
{
  "quantitative_specificity": <float 0.00–1.00>,
  "mechanism_specificity":    <float 0.00–1.00>,
  "debate_interrogation":     <float 0.00–1.00>,
  "synthesis_signal":         <float 0.00–1.00>,
  "citation_authority":       <float 0.00–1.00>,
  "rationale": "<exactly 4 sentences. Sentence 1: name the single biggest strength. Sentence 2: name the single biggest weakness. Sentence 3: name one specific section / passage you scored on. Sentence 4: name one concrete improvement that would lift the score by ≥ 0.05.>"
}
