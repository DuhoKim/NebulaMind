# Cycle 21 actual-research audit

Marker: `ACTUAL_RESEARCH_CYCLE_AUDIT_21`
Audit UTC: 2026-07-09T17:00:43Z

## Compile results
- `rp1_flagship_polished.tex` ok=True bytes=266082 sha256=a956075d6360f9cbc256588e24a1e033144bb65e919bd1fb1a8ab4a266f236ba bad_markers=[]
- `supplementary_denominator_atlas.tex` ok=True bytes=555571 sha256=82569447199af766eabe3b72464b4eb25ee92488a713ba09a9577324adce5a71 bad_markers=[]

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
