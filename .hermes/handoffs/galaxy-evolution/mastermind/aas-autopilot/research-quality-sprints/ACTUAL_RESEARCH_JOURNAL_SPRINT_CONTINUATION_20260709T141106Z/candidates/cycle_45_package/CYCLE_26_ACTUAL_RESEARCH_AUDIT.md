# Cycle 26 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_26`
Audit UTC: 2026-07-09T17:37:02Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=267961 sha256=07b8bc7255a8ae378718993c8454afd74389829d32b6582d1ed1c9793a809d90 bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=556096 sha256=911d24fd2e6f3221aefa76235d98495ef46ec948ce55ae874ed3beb026dcd166 bad_markers=[]

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
