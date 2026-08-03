# Cycle 49 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_49`
Audit UTC: 2026-07-09T20:38:32Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=273707 sha256=249569cb3e519e3f457630e6035264d8c77de3a609828b5c95b0861094253aad bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=559736 sha256=044733c863fc9724b9cfe9a998f66425511040a58ac5b025ffd4b228d6eb2980 bad_markers=[]

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
