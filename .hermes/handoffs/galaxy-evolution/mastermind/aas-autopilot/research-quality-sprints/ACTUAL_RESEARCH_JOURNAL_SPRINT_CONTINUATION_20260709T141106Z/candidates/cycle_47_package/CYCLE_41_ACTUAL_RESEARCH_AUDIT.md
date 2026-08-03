# Cycle 41 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_41`
Audit UTC: 2026-07-09T19:33:47Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=271316 sha256=f49a806893cb365bbd6d78a24b4e830ca4888c9221f92f6c805c01b55e8123de bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=558459 sha256=4babbc869f9755d1810b90c98a8362d144947bdd2a43652f95fb3c662db11ea5 bad_markers=[]

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
