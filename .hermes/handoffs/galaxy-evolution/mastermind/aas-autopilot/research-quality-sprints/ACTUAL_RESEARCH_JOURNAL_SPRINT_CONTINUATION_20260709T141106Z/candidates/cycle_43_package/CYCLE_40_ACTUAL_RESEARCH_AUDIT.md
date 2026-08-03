# Cycle 40 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_40`
Audit UTC: 2026-07-09T19:27:05Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=270837 sha256=5b440cbd4e618db84b7bffed47d2e9f706820264e0dff857ac3a03c6efe20e47 bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=558452 sha256=d482c611ed5cbdaafe983de676b51c43e55d43a3c17579ee3dc2403780a93662 bad_markers=[]

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
