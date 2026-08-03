# Cycle 2 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_02`
Audit UTC: 2026-07-09T14:26:20Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=262910 sha256=1cc4a1a51c8c142893d675fdcf630cc2c5d99453304ecf4484b62504fe887f1d bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=550989 sha256=a07086ab0460516dec42c8e68595f70b362fa0fd276e6db4d9e8cfab6b7336ef bad_markers=[]

## Guards
- flagship missing required phrases: []
- supplement missing required phrases: []
- flagship missing numeric invariants: []
- forbidden mock/synthetic data-use hits flagship: []
- forbidden mock/synthetic data-use hits supplement: []

Fatal failures: 0

## Real-data policy
- Never use mock, synthetic, fake, placeholder, or toy data.
- Do not invent numeric values, sample sizes, citations, URLs, DOIs, arXiv IDs, ADS bibcodes, or figure results.
- New quantitative claims must be traceable to the real local SDSS artifacts inventoried by this sprint or to a cited public source with URL/DOI/arXiv/ADS metadata.
- If a value is not present in the local real-data inventory or a cited public source, write 'not measured here' or 'needs real data'.
- Literature-only sources may motivate future work; they do not become measured NebulaMind results.
- The RP-1 flagship remains an optical SDSS/BPT association pilot unless real additional observables are supplied.
