# Cycle 13 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_13`
Audit UTC: 2026-07-09T15:56:42Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=265374 sha256=e771ccf2efa0a775b6a37196baee1f10cbd4c5c1bd101aa07adc217dec819ab8 bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=552697 sha256=ff9574ce0bde41adcb7a561d6ce4aee94a4a40869f0789556c6c0d9f056ddc3d bad_markers=[]

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
