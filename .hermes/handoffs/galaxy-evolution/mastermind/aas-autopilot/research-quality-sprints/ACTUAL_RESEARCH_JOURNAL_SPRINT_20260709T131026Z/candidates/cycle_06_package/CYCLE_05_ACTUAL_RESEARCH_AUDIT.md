# Cycle 5 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_05`
Audit UTC: 2026-07-09T13:52:47Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=261807 sha256=11325d6afb9fb9db211d56ff49e2e88f9aec448d4551aba611cc5d0511a4f7df bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=550500 sha256=38dda287f4e77efc127b2c3b59b297263c6526d0abccd1b133d35fe49af91c53 bad_markers=[]

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
