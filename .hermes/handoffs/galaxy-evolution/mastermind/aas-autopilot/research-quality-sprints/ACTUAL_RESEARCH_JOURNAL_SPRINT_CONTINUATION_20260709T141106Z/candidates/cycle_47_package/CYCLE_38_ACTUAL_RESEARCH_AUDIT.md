# Cycle 38 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_38`
Audit UTC: 2026-07-09T19:12:24Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=270517 sha256=0bdeb581c838837052120d95c4e50016f99e9cffa89b42df22a823786cc55f12 bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=558454 sha256=073507715944e22e2a64de5ea2de71114155381426d61a64ea03ea57e09c823d bad_markers=[]

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
