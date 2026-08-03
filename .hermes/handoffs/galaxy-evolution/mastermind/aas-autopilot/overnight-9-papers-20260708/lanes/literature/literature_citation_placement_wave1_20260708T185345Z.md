# Literature/source grounding — Wave-1 citation placement review

Marker: `LITERATURE_WAVE1_CITATION_PLACEMENT_20260708T185345Z`

UTC: 2026-07-08T18:53:45Z  
Local: 2026-07-09 03:53:45 KST

## Scope and inputs read

Focused on three Wave-1 papers after the Lana selection/definition cleanup: M1 RP-2, M1 RP-3, and M2 P1. Read the overnight brief, swarm board, ledger, current run-root manuscripts, current topic pages and backups, the Wave-1 literature packet, Hwao direction, and the Lana 20260708T182812Z revision drafts. This is a source-grounding/citation-placement packet only; no manuscript, PDF, public page, product DB/API, deploy, git, billing/OAuth, cron, or external submission change is authorized or performed.

## Acquisition and mechanical checks

- Public arXiv export API only for primary metadata; raw XML was preserved by paper under `raw_payloads/20260708T185345Z/`.
- Unauthenticated Semantic Scholar batch enrichment was attempted once; HTTP status: `200`. It is enrichment only and not required for the conclusions.
- Association records: **19** across **17** unique arXiv sources; duplicate record keys: **[]**.
- arXiv metadata found for **19/19** association records; Semantic Scholar enrichment found **19/19**; abstracts **19/19**; DOI in arXiv record **17/19**; author/year **19/19**.

## Paper-specific placement rules

### M1 RP-2 — SDSS density proxy for environmental quenching

Boundary: actual cached-SDSS nearest-neighbour density versus catalog-sSFR quenching association; not halo/central-satellite causal environmental quenching.

| Priority | Source | Exact URL | Year / authors | Placement / relevance | Supports actual result, or only future data? |
|---:|---|---|---|---|---|
| 1 | The Seventeenth Data Release of the Sloan Digital Sky Surveys: Complete Release of MaNGA, MaStar and APOGEE-2 Data | https://arxiv.org/abs/2112.02026v2 | 2021 — Abdurro'uf, Katherine Accetta, Conny Aerts, Victor Silva Aguirre, et al. (341 authors) | Data/Selection: public SDSS DR17 provenance; DR17 release paper anchors the public survey release used by the cached SDSS pilot. | supports actual method |
| 2 | The physical properties of star forming galaxies in the low redshift universe | https://arxiv.org/abs/astro-ph/0311060v2 | 2003 — J. Brinchmann, S. Charlot, S. D. M. White, C. Tremonti, et al. (7 authors) | Data/Selection: catalog SFR/sSFR and value-added-property caveat; SDSS low-redshift physical-property/SFR context for catalog sSFR-based quenching flags. | supports actual method |
| 3 | Mass and environment as drivers of galaxy evolution in SDSS and zCOSMOS and the origin of the Schechter function | https://arxiv.org/abs/1003.4747v2 | 2010 — Y. Peng, S. J. Lilly, K. Kovac, M. Bolzonella, et al. (64 authors) | Introduction/Discussion: mass and environment as separable population axes; Mass/environment quenching framework helps interpret why a mass-redshift adjusted density-proxy diagnostic is meaningful. | supports scoped result interpretation |
| 4 | Galaxy bimodality versus stellar mass and environment | https://arxiv.org/abs/astro-ph/0607648v2 | 2006 — I. K. Baldry, M. L. Balogh, R. G. Bower, K. Glazebrook, et al. (7 authors) | Introduction/Discussion: local density and bimodality context; SDSS-like colour bimodality versus stellar mass and environment context; close to the paper's density-proxy/quenching association. | supports scoped result interpretation |
| 5 | Galaxy evolution in groups and clusters: satellite star formation histories and quenching timescales in a hierarchical Universe | https://arxiv.org/abs/1206.3571v2 | 2012 — Andrew R. Wetzel, Jeremy L. Tinker, Charlie Conroy, Frank C. van den Bosch | Limitations/Future work: satellite histories, group catalogues, infall/preprocessing; Group/cluster satellite quenching-timescale work specifies missing central/satellite and infall information. | motivates future data only |
| 6 | The role of environment and AGN feedback in quenching local galaxies: Comparing cosmological hydrodynamical simulations to the SDSS | https://arxiv.org/abs/2401.12953v1 | 2024 — Paul H. Goubert, Asa F. L. Bluck, Joanna M. Piotrowska, Roberto Maiolino | Limitations/Future work: model comparison and intrinsic/environment predictor separation; Recent SDSS-plus-simulation comparison frames environment and AGN feedback jointly, guarding against causal overclaim from one density proxy. | motivates future data only |

Integration guard: cite Peng/Baldry as scoped context for the density-proxy association; keep Wetzel/Goubert in the missing-data paragraph requiring group/halo/central-satellite/model-comparison information.

### M1 RP-3 — optical-AGN denominator for maintenance-heating follow-up

Boundary: actual optical BPT-AGN fractions in massive emission-line hosts; not jet power, cavity enthalpy, cooling balance, or duty cycle.

| Priority | Source | Exact URL | Year / authors | Placement / relevance | Supports actual result, or only future data? |
|---:|---|---|---|---|---|
| 1 | The Seventeenth Data Release of the Sloan Digital Sky Surveys: Complete Release of MaNGA, MaStar and APOGEE-2 Data | https://arxiv.org/abs/2112.02026v2 | 2021 — Abdurro'uf, Katherine Accetta, Conny Aerts, Victor Silva Aguirre, et al. (341 authors) | Data/Selection: public SDSS DR17 provenance; DR17 release paper anchors the public survey release for the optical denominator. | supports actual method |
| 2 | The host galaxies of radio-loud AGN: mass dependencies, gas cooling and AGN feedback | https://arxiv.org/abs/astro-ph/0506269v1 | 2005 — P. N. Best, G. Kauffmann, T. M. Heckman, J. Brinchmann, et al. (7 authors) | Introduction/Discussion: SDSS-to-radio demographic bridge for massive hosts; SDSS radio-loud AGN demographics connect massive-host target selection to later radio-mode follow-up without measuring jet power here. | supports scoped target stratification |
| 3 | Heating Hot Atmospheres with Active Galactic Nuclei | https://arxiv.org/abs/0709.2152v1 | 2007 — B. R. McNamara, P. E. J. Nulsen | Scope/Discussion: X-ray cavity, shock, hot-atmosphere heating observables missing from SDSS; Review anchor for hot-atmosphere heating tests; defines future calorimetric observables absent from the optical pilot. | motivates future data only |
| 4 | Mechanical Feedback from Active Galactic Nuclei in Galaxies, Groups, and Clusters | https://arxiv.org/abs/1204.0006v1 | 2012 — B. R. McNamara, P. E. J. Nulsen | Scope/Discussion: mechanical feedback and heating-to-cooling measurement requirements; Mechanical-feedback review supports requiring jet/cavity power and cooling luminosity before maintenance-heating claims. | motivates future data only |
| 5 | The Co-Evolution of Galaxies and Supermassive Black Holes: Insights from Surveys of the Contemporary Universe | https://arxiv.org/abs/1403.4620v1 | 2014 — Timothy Heckman, Philip Best | Introduction: radiative-mode versus radio-mode AGN population context; Survey review helps separate optical/radiative and radio/mechanical AGN modes; not a measurement in the SDSS pilot. | status motivation only |
| 6 | Galaxy groups as the ultimate probe of AGN feedback | https://arxiv.org/abs/2403.17145v1 | 2024 — Dominique Eckert, Fabio Gastaldello, Ewan O'Sullivan, Alexis Finoguenov, et al. (6 authors) | Future work: group/hot-gas regime for feedback energetics; Group-scale AGN-feedback status source identifying the hot-gas/group observations needed after the optical denominator. | motivates future data only |

Integration guard: use Best/Heckman-Best as target-stratification/status context, and McNamara/Nulsen/Eckert only to define the future X-ray/radio/hot-gas measurements; do not imply the optical BPT fraction measures heating balance.

### M2 P1 — high-excitation optical-AGN denominator for outflow escape/recycling tests

Boundary: actual high-excitation optical target denominator and sSFR contrast; not outflow velocity, escape speed, gas phase mass, or recycling fraction.

| Priority | Source | Exact URL | Year / authors | Placement / relevance | Supports actual result, or only future data? |
|---:|---|---|---|---|---|
| 1 | The Seventeenth Data Release of the Sloan Digital Sky Surveys: Complete Release of MaNGA, MaStar and APOGEE-2 Data | https://arxiv.org/abs/2112.02026v2 | 2021 — Abdurro'uf, Katherine Accetta, Conny Aerts, Victor Silva Aguirre, et al. (341 authors) | Data/Selection: public SDSS DR17 provenance; DR17 release paper anchors the public survey release for the high-excitation optical target denominator. | supports actual method |
| 2 | The Host Galaxies and Classification of Active Galactic Nuclei | https://arxiv.org/abs/astro-ph/0605681v3 | 2006 — Lisa J. Kewley, Brent Groves, Guinevere Kauffmann, Tim Heckman | Data/Candidate definition: Seyfert/LINER/composite optical-classification caveats; Classification paper supports line-ratio guardrails for high-excitation optical AGN selection. | supports actual method |
| 3 | Galactic Winds | https://arxiv.org/abs/astro-ph/0504435v3 | 2005 — S. Veilleux, G. Cecil, J. Bland-Hawthorn | Scope/Discussion: multiphase wind physics and diagnostic requirements; Galactic-winds review motivates why velocity, geometry, phase mass, and multiwavelength data are needed beyond SDSS line ratios. | status motivation only |
| 4 | Massive Molecular Outflows and Evidence for AGN Feedback from CO Observations | https://arxiv.org/abs/1311.2595v1 | 2013 — C. Cicone, R. Maiolino, E. Sturm, J. Graciá-Carpio, et al. (15 authors) | Future work: molecular outflow mass/rate follow-up; CO molecular-outflow work specifies a missing cold-gas phase and outflow-rate observable; not support for an SDSS escape fraction. | motivates future data only |
| 5 | AGN wind scaling relations and the co-evolution of black holes and galaxies | https://arxiv.org/abs/1702.04507v1 | 2017 — F. Fiore, C. Feruglio, F. Shankar, M. Bischetti, et al. (17 authors) | Future work: wind scaling relations and kinetic-power measurements; Wind scaling-relations source motivates velocities/radii/phase masses and duty-cycle caution for future resolved follow-up. | motivates future data only |
| 6 | AGN feedback on molecular gas reservoirs in quasars at $z\sim$2.4 | https://arxiv.org/abs/1706.08987v2 | 2017 — S. Carniani, A. Marconi, R. Maiolino, C. Feruglio, et al. (21 authors) | Future work: high-z molecular-reservoir disturbance as targeted-case motivation; Quasar molecular-gas reservoir paper motivates resolved gas follow-up but must not be used as denominator-wide escape/recycling evidence. | motivates future data only |
| 7 | Observational Evidence of AGN Feedback | https://arxiv.org/abs/1204.4114v1 | 2012 — A. C. Fabian | Discussion: broad AGN-feedback review with explicit overclaim guard; Review source frames AGN feedback evidence while the pilot remains an optical target baseline. | status motivation only |

Integration guard: Kewley 2006 can support optical-classification caveats; wind/outflow papers belong in the required-follow-up paragraph and cannot support escape/recycling fractions from SDSS line ratios.

## Later manuscript-integration checklist

1. Current run-root Wave-1 manuscripts still have only the minimal York/BPT bibliography; the Lana drafts already contain the safer expanded citations. A later integration pass should migrate the citations with the same method/status/future-data separation, not just paste bibliography entries.
2. Preserve exact operational definitions before citations: RP-2 `specsfr_tot_p50 < -11.0` and 10th-neighbour density proxy; RP-3 `lgm_tot_p50 >= 10.8` and `specsfr_tot_p50 < -11.0`; M2 P1 BPT AGN plus `log([OIII]/Hb) > 0.25`.
3. Keep selection-function disclosure adjacent to all incidence language: 249,917 strict four-line S/N>=3 public rows, 60,000 cached rows, 24.0% coverage, `TOP 60000 ... ORDER BY specObjID`, and sSFR-dependent retention.
4. Treat this as local citation-integration readiness only. It does not authorize public prose/wiki changes, public-linked PDF replacement, DB/API writes, deploy, git, or external submission.

## Artifact manifest

- Markdown packet: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/literature/literature_citation_placement_wave1_20260708T185345Z.md`
- JSONL source/placement ledger: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/literature/literature_sources_wave1_citation_placement_20260708T185345Z.jsonl`
- Summary JSON: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/literature/literature_summary_wave1_citation_placement_20260708T185345Z.json`
- Raw arXiv XML for m1_rp2_environment_quenching: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/literature/raw_payloads/20260708T185345Z/m1_rp2_environment_quenching_arxiv_id_list.xml`
- Raw arXiv XML for m1_rp3_maintenance_heating: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/literature/raw_payloads/20260708T185345Z/m1_rp3_maintenance_heating_arxiv_id_list.xml`
- Raw arXiv XML for m2_p1_outflow_escape_recycling: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/literature/raw_payloads/20260708T185345Z/m2_p1_outflow_escape_recycling_arxiv_id_list.xml`
- Semantic Scholar batch status: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/literature/raw_payloads/20260708T185345Z/semantic_scholar_batch_status.json`

## Safety ledger

- No credentials used; no ADS token/API-key access attempted.
- No manuscript/PDF/public page/live root/product DB/API/page_versions/trust/deploy/restart/git/billing/OAuth/cron/external-submission changes.
- This packet supports later local citation-integration review only; it does not authorize prose publication or public-linked PDF replacement.
- No active execution phrase.
