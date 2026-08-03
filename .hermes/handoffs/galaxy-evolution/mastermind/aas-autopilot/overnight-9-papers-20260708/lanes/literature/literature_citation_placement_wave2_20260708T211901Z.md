# Literature/source grounding — Wave-2 citation placement review

Marker: `LITERATURE_WAVE2_CITATION_PLACEMENT_20260708T211901Z`

UTC: 2026-07-08T21:19:01Z  
Local: 2026-07-09 06:19:01 KST

## Scope and inputs read

Focused on three Wave-2 high-risk papers after Lana's selection-disclosure revisions: **M2 P2**, **M3 P2**, and **M3 P3**. Read the overnight brief, swarm board, ledger, current run-root manuscripts, Lana lane-local revised manuscripts, current topic pages and pre-proposal backups, the prior Wave-2 source packet, and Hwao's latest director priorities. This is a source-grounding/citation-placement packet only: no manuscript, PDF, public page, product DB/API, deploy, git, billing/OAuth, cron, or external submission change is authorized or performed.

## Acquisition and mechanical checks

- Public arXiv export API only for primary metadata; raw XML was preserved by paper under `raw_payloads/20260708T211901Z/`.
- Unauthenticated Semantic Scholar batch enrichment attempted once; HTTP status: `200`; matched records: 20/20. It is enrichment only and not needed for the placement verdict.
- Association records: **20** across **18** unique arXiv sources; duplicate record keys: `[]`; arXiv metadata missing: `[]`.
- Every row below is classified as actual-method/scoped-result support versus future-data/model motivation. No citation is treated as support for unmeasured radio power, gas masses, depletion times, coupling efficiency, or simulation validation.

## Paper-specific placement rules

### M2 P2 — environment proxy for optical AGN in massive hosts

Boundary: Actual cached-SDSS result: BPT optical-AGN fraction versus internal nearest-neighbour density proxy in massive hosts; no radio jet power, hot-gas, cavity, or coupling-efficiency measurement.

| Priority | Source | Exact URL | Year / authors | Placement / relevance | Supports actual result, or only future data? |
|---:|---|---|---|---|---|
| 1 | The Seventeenth Data Release of the Sloan Digital Sky Surveys: Complete Release of MaNGA, MaStar and APOGEE-2 Data | https://arxiv.org/abs/2112.02026v2 | 2021 — Abdurro'uf, Katherine Accetta, Conny Aerts, Victor Silva Aguirre, Romina Ahumada, Nikhil Ajgaonkar, et al. (341 authors) | Data/Selection: public SDSS DR17 provenance for the optical emission-line parent sample. Anchors the public survey release used by the cached SDSS denominator. | supports actual method |
| 2 | The Host Galaxies and Classification of Active Galactic Nuclei | https://arxiv.org/abs/astro-ph/0605681v3 | 2006 — Lisa J. Kewley, Brent Groves, Guinevere Kauffmann, Tim Heckman | Data/Definitions: optical AGN host/classification context and BPT-class caveats. Supports why the manuscript must describe BPT labels as optical classification proxies, not feedback measurements. | supports actual method |
| 3 | The host galaxies of radio-loud AGN: mass dependencies, gas cooling and AGN feedback | https://arxiv.org/abs/astro-ph/0506269v1 | 2005 — P. N. Best, G. Kauffmann, T. M. Heckman, J. Brinchmann, S. Charlot, Z. Ivezic, et al. (7 authors) | Introduction/Discussion: massive-host radio-loud AGN demographic bridge. Connects massive-host SDSS demographics to later radio-mode/maintenance follow-up while keeping the current sample optical-only. | supports scoped target stratification |
| 4 | AGN-driven outflows and the AGN feedback efficiency in young radio galaxies | https://arxiv.org/abs/2009.11175v1 | 2020 — F. Santoro, C. Tadhunter, D. Baron, R. Morganti, J. Holt | Discussion/Future observables: young radio-galaxy outflows and efficiency language. Shows what kind of radio/kinematic data would be needed before discussing coupling efficiency. | motivates future data only |
| 5 | Heating Hot Atmospheres with Active Galactic Nuclei | https://arxiv.org/abs/0709.2152v1 | 2007 — B. R. McNamara, P. E. J. Nulsen | Limitations/Future work: hot-atmosphere heating, cavities, shocks, and cooling balance. Defines missing X-ray/hot-gas energetics that SDSS optical line ratios do not measure. | motivates future data only |
| 6 | Galaxy groups as the ultimate probe of AGN feedback | https://arxiv.org/abs/2403.17145v1 | 2024 — Dominique Eckert, Fabio Gastaldello, Ewan O'Sullivan, Alexis Finoguenov, Marisa Brienza, the X-GAP collaboration | Limitations/Future work: group-scale gas and AGN-feedback testbed. Motivates environment/group observations needed after the internal-density proxy. | motivates future data only |

Integration guard: Use radio/X-ray/group sources to define the required follow-up observables; the result sentence must remain an optical-AGN/environment denominator statement.

### M3 P2 — optical denominator for gas-fraction versus efficiency tests

Boundary: Actual cached-SDSS result: massive low-sSFR four-line optical denominator and H-alpha proxy baseline; no CO/HI/dust gas masses, gas fractions, depletion times, or SFE measurement.

| Priority | Source | Exact URL | Year / authors | Placement / relevance | Supports actual result, or only future data? |
|---:|---|---|---|---|---|
| 1 | The Seventeenth Data Release of the Sloan Digital Sky Surveys: Complete Release of MaNGA, MaStar and APOGEE-2 Data | https://arxiv.org/abs/2112.02026v2 | 2021 — Abdurro'uf, Katherine Accetta, Conny Aerts, Victor Silva Aguirre, Romina Ahumada, Nikhil Ajgaonkar, et al. (341 authors) | Data/Selection: public SDSS DR17 provenance for the optical denominator. Anchors the survey release for the four-line emission sample and cached follow-up denominator. | supports actual method |
| 2 | The physical properties of star forming galaxies in the low redshift universe | https://arxiv.org/abs/astro-ph/0311060v2 | 2003 — J. Brinchmann, S. Charlot, S. D. M. White, C. Tremonti, G. Kauffmann, T. Heckman, et al. (7 authors) | Data/Definitions: SDSS physical-property, SFR, and catalog-sSFR context. Supports the catalog sSFR/H-alpha-property caveats in the optical-only manuscript. | supports actual method |
| 3 | COLD GASS, an IRAM legacy survey of molecular gas in massive galaxies: I. Relations between H2, HI, stellar content and structural properties | https://arxiv.org/abs/1103.1642v1 | 2011 — Amelie Saintonge, Guinevere Kauffmann, Carsten Kramer, Linda J. Tacconi, Christof Buchbender, Barbara Catinella, et al. (24 authors) | Discussion/Future data: COLD GASS molecular-gas survey anchor for massive nearby galaxies. Specifies the H2/HI/stellar measurements needed before gas-fraction statements. | motivates future data only |
| 4 | COLD GASS, an IRAM Legacy Survey of Molecular Gas in Massive Galaxies: II. The non-universality of the Molecular Gas Depletion Timescale | https://arxiv.org/abs/1104.0019v1 | 2011 — Amelie Saintonge, Guinevere Kauffmann, Jing Wang, Carsten Kramer, Linda J. Tacconi, Christof Buchbender, et al. (24 authors) | Discussion/Future data: depletion-timescale and non-universality guard. Directly supports the warning that depletion time is a molecular-gas-plus-SFR quantity, not an SDSS four-line quantity. | motivates future data only |
| 5 | xCOLD GASS: the complete IRAM-30m legacy survey of molecular gas for galaxy evolution studies | https://arxiv.org/abs/1710.02157v1 | 2017 — Amélie Saintonge, Barbara Catinella, Linda J. Tacconi, Guinevere Kauffmann, Reinhard Genzel, Luca Cortese, et al. (21 authors) | Discussion/Future data: xCOLD GASS complete CO legacy-survey anchor. Motivates the required CO follow-up denominator for molecular gas and depletion-time work. | motivates future data only |
| 6 | xGASS: Total cold gas scaling relations and molecular-to-atomic gas ratios of galaxies in the local Universe | https://arxiv.org/abs/1802.02373v1 | 2018 — Barbara Catinella, Amélie Saintonge, Steven Janowiecki, Luca Cortese, Romeel Davé, Jenna J. Lemonias, et al. (13 authors) | Discussion/Future data: xGASS HI+H2 scaling and molecular-to-atomic gas ratio context. Motivates separating gas availability from SFE with cold-gas data rather than optical H-alpha alone. | motivates future data only |

Integration guard: Cite gas-survey papers only around the missing CO/HI/dust data requirement and the depletion-time/SFE wording guard.

### M3 P3 — SDSS target vector for feedback-model validation

Boundary: Actual cached-SDSS result: observed 15-cell mass-redshift target vector from the four-line optical sample; no simulation mock was generated or compared.

| Priority | Source | Exact URL | Year / authors | Placement / relevance | Supports actual result, or only future data? |
|---:|---|---|---|---|---|
| 1 | The Seventeenth Data Release of the Sloan Digital Sky Surveys: Complete Release of MaNGA, MaStar and APOGEE-2 Data | https://arxiv.org/abs/2112.02026v2 | 2021 — Abdurro'uf, Katherine Accetta, Conny Aerts, Victor Silva Aguirre, Romina Ahumada, Nikhil Ajgaonkar, et al. (341 authors) | Data/Selection: public SDSS DR17 provenance for the observed target vector. Anchors the observed SDSS release before any future mock comparison. | supports actual method |
| 2 | The IllustrisTNG Simulations: Public Data Release | https://arxiv.org/abs/1812.05609v3 | 2018 — Dylan Nelson, Volker Springel, Annalisa Pillepich, Vicente Rodriguez-Gomez, Paul Torrey, Shy Genel, et al. (14 authors) | Discussion/Future mock infrastructure: IllustrisTNG public data release. Identifies a public simulation suite that could be forward-modelled through matching selection. | motivates future model comparison only |
| 3 | The EAGLE project: Simulating the evolution and assembly of galaxies and their environments | https://arxiv.org/abs/1407.7040v2 | 2014 — Joop Schaye, Robert A. Crain, Richard G. Bower, Michelle Furlong, Matthieu Schaller, Tom Theuns, et al. (22 authors) | Discussion/Future mock infrastructure: EAGLE galaxy-formation/feedback suite. Provides a second feedback-model family for future survey-matched comparisons. | motivates future model comparison only |
| 4 | Simba: Cosmological Simulations with Black Hole Growth and Feedback | https://arxiv.org/abs/1901.10203v2 | 2019 — Romeel Davé, Daniel Anglés-Alcázar, Desika Narayanan, Qi Li, Mika H. Rafieferantsoa, Sarah Appleby | Discussion/Future mock infrastructure: SIMBA black-hole growth and feedback prescriptions. Defines another model family whose outputs would require forward modelling before comparison. | motivates future model comparison only |
| 5 | iMaNGA: mock MaNGA galaxies based on IllustrisTNG and MaStar SSPs. I. Construction and analysis of the mock data cubes | https://arxiv.org/abs/2203.11575v3 | 2022 — Lorenza Nanni, Daniel Thomas, James Trayford, Claudia Maraston, Justus Neumann, David R. Law, et al. (11 authors) | Methods/Future work: iMaNGA-style mock IFU construction and survey realism. Closest source for the required synthetic-observation step before using observed target vectors to test models. | motivates future model comparison only |
| 6 | Quenched fractions in the IllustrisTNG simulations: comparison with observations and other theoretical models | https://arxiv.org/abs/2008.00004v2 | 2020 — Martina Donnari, Annalisa Pillepich, Dylan Nelson, Federico Marinacci, Mark Vogelsberger, Lars Hernquist | Discussion/Future comparison: quenched-fraction comparisons with observations. Shows the kind of quenching comparison a real model-validation paper would need, after applying matching selections. | status/method motivation only |
| 7 | The Horizon-AGN simulation: morphological diversity of galaxies promoted by AGN feedback | https://arxiv.org/abs/1606.03086v2 | 2016 — Yohan Dubois, Sebastien Peirani, Christophe Pichon, Julien Devriendt, Raphael Gavazzi, Charlotte Welker, et al. (7 authors) | Discussion/Future observables: morphology as a model output, not a current SDSS-vector result. Motivates adding morphology to future validation; it is not measured in the current target vector. | motivates future model comparison only |
| 8 | AGN-driven quenching of star formation: morphological and dynamical implications for early-type galaxies | https://arxiv.org/abs/1301.3092v2 | 2013 — Yohan Dubois, Raphaël Gavazzi, Sébastien Peirani, Joseph Silk | Discussion/Future observables: AGN-driven quenching simulation implications. Useful background for simulation-predicted signatures, with the guard that the current pilot has not tested them. | motivates future model comparison only |

Integration guard: Simulation papers can motivate future forward modelling only; do not cite them as if the SDSS vector validates, rejects, ranks, or falsifies any model.

## Later manuscript-integration checklist

1. **M2 P2:** Add DR17/Kewley as method anchors; Best et al. can support massive-host/radio-mode target stratification; Santoro, McNamara--Nulsen, and Eckert belong only in the missing radio/X-ray/group-observable paragraph.
2. **M3 P2:** Add DR17/Brinchmann around the optical denominator and catalog-property caveat; place COLD GASS/xCOLD GASS/xGASS only where the manuscript says CO/HI/dust gas data are required before gas-fraction/depletion-time/SFE claims.
3. **M3 P3:** Add SDSS DR17 for the observed vector; simulation-suite citations belong in the future forward-modelling paragraph and must be paired with the statement that no mock catalogue has been run.
4. Preserve the shared selection-function disclosure before citation expansion: 249,917 strict four-line S/N>=3 public rows, 60,000 cached rows, 24.0% coverage, SpecObjID row-cap caveat, and sSFR-dependent retention.

## Artifact manifest

- Markdown packet: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/literature/literature_citation_placement_wave2_20260708T211901Z.md`
- JSONL source/placement ledger: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/literature/literature_sources_wave2_citation_placement_20260708T211901Z.jsonl`
- Summary JSON: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/literature/literature_summary_wave2_citation_placement_20260708T211901Z.json`
- Raw arXiv XML for m2_p2_radio_jet_environment: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/literature/raw_payloads/20260708T211901Z/m2_p2_radio_jet_environment_arxiv_id_list.xml`
- Raw arXiv XML for m3_p2_gas_depletion_efficiency: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/literature/raw_payloads/20260708T211901Z/m3_p2_gas_depletion_efficiency_arxiv_id_list.xml`
- Raw arXiv XML for m3_p3_simulation_validation: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/literature/raw_payloads/20260708T211901Z/m3_p3_simulation_validation_arxiv_id_list.xml`
- Semantic Scholar batch status/raw response: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/literature/raw_payloads/20260708T211901Z/semantic_scholar_batch_status.json` and `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/literature/raw_payloads/20260708T211901Z/semantic_scholar_batch_raw.json`

## Safety ledger

- No credentials used; no ADS token/API-key access attempted.
- No manuscript/PDF/public page/live root/product DB/API/page_versions/trust/deploy/restart/git/billing/OAuth/cron/external-submission changes.
- This packet supports later local citation-integration review only; it does not authorize prose publication or public-linked PDF replacement.
- No active execution phrase.
