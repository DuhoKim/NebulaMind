# Cycle 24 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_24`
Audit UTC: 2026-07-09T17:21:48Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=267356 sha256=ea4cc6d545a12c2be0a8e74af51fc44a85e3321829ca848fcce02503eaceb9ae bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=555713 sha256=de43aa692096fd7d02766bc2e494a0c78c62c7d06fcfb66e2697097a22758977 bad_markers=[]

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
