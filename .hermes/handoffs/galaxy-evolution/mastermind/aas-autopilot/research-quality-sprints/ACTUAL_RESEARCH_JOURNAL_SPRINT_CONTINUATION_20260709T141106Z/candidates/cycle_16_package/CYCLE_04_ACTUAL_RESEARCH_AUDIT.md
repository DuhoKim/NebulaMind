# Cycle 4 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_04`
Audit UTC: 2026-07-09T14:45:13Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=262871 sha256=710528b1236e0cabd85f17e01f7fca5f785d14d7bb52779570cd3d801d536535 bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=550921 sha256=0ea461e1d8a75c0d84a97e49a9adc52eb1a068907d838f84eaa72cceb75fdb26 bad_markers=[]

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
