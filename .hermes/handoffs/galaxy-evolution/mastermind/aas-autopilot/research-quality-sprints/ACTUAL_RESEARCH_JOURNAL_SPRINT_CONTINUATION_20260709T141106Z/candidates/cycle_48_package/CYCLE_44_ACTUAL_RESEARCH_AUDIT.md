# Cycle 44 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_44`
Audit UTC: 2026-07-09T19:58:58Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=272088 sha256=5a800ed3f993f3b9c4e779e5de2454939a5e121e5356a7d351699f254c1a80fe bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=558728 sha256=4ff60dab37ee738ca712302442d79295a99b4beb50add71ad375b040c0869d2c bad_markers=[]

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
