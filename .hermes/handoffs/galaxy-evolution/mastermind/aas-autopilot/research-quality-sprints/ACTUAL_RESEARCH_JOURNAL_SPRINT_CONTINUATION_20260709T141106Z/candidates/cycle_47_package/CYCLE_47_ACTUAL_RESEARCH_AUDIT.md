# Cycle 47 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_47`
Audit UTC: 2026-07-09T20:19:30Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=273320 sha256=7a1bf35cb3d45b00778c9c122feb0dfed3d0ef424c648d830f47879271eb7870 bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=559502 sha256=3b0c304f1520fefbe751317248b163507709fb810093f85a0efd1ce02ee52350 bad_markers=[]

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
