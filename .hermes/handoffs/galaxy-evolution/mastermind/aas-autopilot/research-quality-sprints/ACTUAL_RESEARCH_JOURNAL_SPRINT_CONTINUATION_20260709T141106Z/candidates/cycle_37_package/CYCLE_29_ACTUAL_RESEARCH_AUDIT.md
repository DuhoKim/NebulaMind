# Cycle 29 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_29`
Audit UTC: 2026-07-09T17:57:25Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=269124 sha256=b25573cb3c0ed90480e138b30fe9384ea77c3393754869866e80384afcb44ded bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=557358 sha256=9525f1f20a453a303f9f4300cee10f780b36ebab47b70a7a89576de9f73278d5 bad_markers=[]

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
