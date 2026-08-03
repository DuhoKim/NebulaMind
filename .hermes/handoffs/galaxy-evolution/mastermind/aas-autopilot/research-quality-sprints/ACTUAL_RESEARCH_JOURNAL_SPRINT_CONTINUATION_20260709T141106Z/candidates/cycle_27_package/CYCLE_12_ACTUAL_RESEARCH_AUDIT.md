# Cycle 12 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_12`
Audit UTC: 2026-07-09T15:49:18Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=265290 sha256=bb6f6c1f5a4f6682809a10246009bf6cadd1dd0884e4ee9ffea7bebcb6f85397 bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=552697 sha256=eb5d7187908058f4a2679b67d0f793d5da2e739e3a326f1d63bcd9e1cf8ba6d9 bad_markers=[]

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
