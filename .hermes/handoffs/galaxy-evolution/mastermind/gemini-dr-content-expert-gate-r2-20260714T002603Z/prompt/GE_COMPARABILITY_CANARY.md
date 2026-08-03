# Deep Research request — Selection commensurability of eight simulation-observation comparisons (Galaxy Evolution)

Request ID: REQ_GE_COMPARABILITY_20260713T160239Z

Role: You are a literature analyst for a galaxy-evolution research journal. Report only published work; you have no access to the journal's internal results.

Question: For each numbered comparison below, determine from the PRIMARY published literature: (a) the sample-selection function used on the simulation side of the claimed comparison; (b) the observational comparator actually used and its selection function; (c) whether the two selections are commensurable ("matched") as published; and (d) the correct PRIMARY peer-reviewed reference(s) for the comparison where the listed current source is an aggregator page, a project/blog page, or appears mis-attributed.

The eight comparisons (simulation | observable | claimed result | currently listed source):
1. IllustrisTNG | galaxy color bimodality distribution | agreement (sharp blue-to-red transition near M*≈10^10.5 M_sun) | https://oamonitor.ireland.openaire.eu/national/search/publication?pid=10.1093%2Fmnras%2Fstx3040 (aggregator — identify the primary paper)
2. EAGLE | specific star-formation rate vs stellar mass at intermediate redshift | tension (simulated relation steeper; observed normalisation higher at z≈1–2) | https://www.cambridge.org/core/journals/publications-of-the-astronomical-society-of-australia/article/relation-between-starformation-rate-and-stellar-mass-of-galaxies-at-z-14/2AAB84B2524F5870838E5BCC736A18DC
3. SIMBA | molecular gas mass distributions | tension (overproduces H2 mass fractions while matching the stellar mass function) | https://academic.oup.com/mnras/article/497/1/146/5866845
4. FIRE/FIRE-2 | visual morphologies and central mass concentrations in massive galaxies | agreement (convergence with resolution; central concentrations sensitive to wind recycling) | https://fire.northwestern.edu/2017/03/21/fire-2-simulations-physics-versus-numerics-in-galaxy-formation/ (project page — identify the primary paper)
5. ROMULUS | dual active-galactic-nucleus frequency | agreement (dual-AGN demographics vs larger contexts) | https://arxiv.org/abs/1607.02151
6. ASTRID | supermassive black hole mass and luminosity functions | agreement (broadly consistent constraints, notably before z=3) | https://arxiv.org/abs/2110.14154
7. FLAMINGO | kinetic Sunyaev-Zel'dovich effect of SDSS BOSS galaxies | tension (Planck/ACT stacking prefers stronger feedback than fiducial calibration) | https://arxiv.org/abs/2410.19905
8. BAHAMAS | cosmic shear and matter power spectrum clustering | tension (S8-resolving feedback strengths disagree with X-ray cluster gas fractions) | https://arxiv.org/abs/2410.19905 (same source as item 7 — verify whether this reference actually covers BAHAMAS, and if not identify the correct primary reference)

OUTPUT DISCIPLINE (binding): the report body is STRUCTURED ONLY, in this exact sequence: (a) the 4-line meta header; (b) Section 1 table; (c) Section 2 bullets; (d) the Links ledger; (e) the final completion-marker line, alone. Nothing else — no abstract, introduction, summary, or free narrative outside table cells, bullets, ledger lines, and the marker line.

Meta header (first 4 lines, exactly):
    # GE comparability canary — REQ_GE_COMPARABILITY_20260713T160239Z
    Run date (UTC): <YYYY-MM-DDTHH:MM:SSZ>
    Model: Gemini Pro (selected UI mode; backend version not exposed)
    Rows covered: <N> of 8
Emit the Model line verbatim; do not substitute a version number.

## 1. Selection commensurability ledger — Markdown table, one row per comparison, exactly these columns:
| Row | Simulation | Simulation-side selection (as stated, same-cell citation) | Observational comparator + selection (as stated, same-cell citation) | SELECTION_MATCH | Basis (≤2 sentences, same-cell citation) |
The SELECTION_MATCH cell contains exactly one token: MATCHED_SELECTIONS_CONFIRMED, PARTIALLY_MATCHED, UNMATCHED_SELECTIONS, or INDETERMINATE_FROM_PUBLISHED_SOURCES. Every claim-bearing cell carries its OWN checkable citation (arXiv ID, DOI, ADS bibcode, or URL) or UNCITED_NOT_USABLE; a citation in one cell does not cover another. An empty field is exactly NONE_FOUND.

## 2. Primary-source corrections — bullets only; one bullet per row whose listed current source is not the primary peer-reviewed source of the claimed comparison (at minimum evaluate rows 1, 4, 7, 8): "Row <N>: correct primary reference(s) = <citation(s)>; the listed source is <aggregator page | project page | mis-attributed — actually covers <what>>." Same-bullet citations mandatory.

## Links ledger — one line per unique cited source: <short name, non-empty> | <citation> | QUARANTINED_PENDING_LOCAL_CHECK. Bidirectional and unique: every inline citation appears exactly once here; every ledger row is cited inline at least once; no duplicates; no blank short names.

Wording contract: in your own voice the settled/causal register is BANNED (case-insensitive): establish/establishes/established/establishing, proves, proven, confirms that, settles, settled question, resolves the debate, definitively, conclusively, is now known, "demonstrates that … causes". A source's claim in that register appears only as an attributed quote with a checkable citation. Every quoted scientific number carries the source's uncertainty in the same cell OR the label UNCERTAINTY_NOT_QUOTED_BY_SOURCE (citation identifiers, section numbers, and the header row count are exempt). Any quoted numeric fraction or incidence carries, in the same cell: TRACER=<...>; SELECTION=<...>; DENOMINATOR=<...>; REDSHIFT=<...> (use NOT_APPLICABLE per qualifier as needed).

Safety locks: output is advisory only — not accepted evidence, not product-claim binding; do not present generated DOI/ADS/arXiv IDs as verified (all are quarantined pending local check); do not propose edits to any local artifact.

The last non-empty line of the report must be exactly the completion marker below, with nothing after it:
GEMINI_WEB_GE_COMPARABILITY_CANARY_DONE_20260713T160239Z