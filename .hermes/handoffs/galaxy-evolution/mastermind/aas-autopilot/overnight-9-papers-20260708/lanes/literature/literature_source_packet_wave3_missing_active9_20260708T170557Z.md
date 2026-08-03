# Literature/source grounding tick — Wave-3 missing active-9 papers

Marker: `LITERATURE_SOURCE_WAVE3_MISSING_ACTIVE9_20260708T170557Z`

UTC: 2026-07-08T17:05:57Z  
Local: 2026-07-09 02:05:57 KST

## Scope and inputs read

This tick closes the largest remaining active-9 bibliography/source-grounding gap: **M1 RP-1**, **M2 P3**, and **M3 P1** had not been covered by the prior Wave-1/Wave-2 topic-specific source packets. It is a source packet only: no manuscript overwrite, no PDF change, no citation insertion, and no public mirroring.

Read before synthesis: `OVERNIGHT_BRIEF.md`, `OVERNIGHT_LEDGER.md`, the 8-paper manifest, the public-link verification packet, current AASTeX sources for RP-1/M2 P3/M3 P1, Hwao director guidance, Goru robustness results, Lana revision notes, and prior literature/source packets.

## Acquisition and corpus-gate discipline

- Started from an accepted coverage matrix with target roles per paper: actual data/method anchor, status/context anchor, and future-data/overclaim guard.
- Used ADS metadata acquisition because ADS credentials were available to the local Hermes tool environment. Raw ADS JSON payloads were preserved by paper.
- Also fetched raw arXiv export XML by paper for stable arXiv IDs/versions. arXiv availability counts below come from ADS `identifier` entries, not a top-level arXiv field.
- Attempted one unauthenticated Semantic Scholar enrichment/status probe; it returned HTTP 429 and was not used.
- Deduplicated by ADS bibcode first, then DOI/title fallback. No source is being treated as full-text evidence; this clears only local citation-integration review.

## Mechanical summary

- Deduplicated source records: **17**; duplicate keys: **0**.
- ADS bibcodes: 17/17; DOI: 17/17; ADS abstracts: 17/17; ADS identifier entries: 17/17.
- arXiv availability counted from ADS identifiers: 17/17.

## Paper-specific integration rules

### M1 RP-1 — SDSS AGN/sSFR matched-control pilot

Current pilot boundary: Actual SDSS DR17 emission-line matched-control association; not causal AGN-feedback proof and not a complete quiescent-galaxy census.

Coverage roles observed: actual_data_or_method, overclaim_guard, scoped_interpretation. Missing target roles: none.

| Priority | Source | ADS bibcode | Year / authors | Role | Why relevant | Safe integration guard |
|---:|---|---|---|---|---|---|
| 1 | The Seventeenth Data Release of the Sloan Digital Sky Surveys: Complete Release of MaNGA, MaStar, and APOGEE-2 Data | 2022ApJS..259...35A | 2022 — Abdurro'uf, Accetta, Katherine, Aerts, Conny, Silva Aguirre, Víctor, Ahumada, Romina, Ajgaonkar, Nikhil, et al. (341 authors) | actual_data_or_method | Public SDSS DR17 release paper; anchors the survey provenance for all three local SDSS pilots. | Use in Data/Sample sections to identify the public survey release and preserve the distinction between SDSS observables and missing follow-up data. |
| 2 | The physical properties of star-forming galaxies in the low-redshift Universe | 2004MNRAS.351.1151B | 2004 — Brinchmann, J., Charlot, S., White, S. D. M., Tremonti, C., Kauffmann, G., Heckman, T., et al. (7 authors) | actual_data_or_method | Low-redshift SDSS physical-property and star-formation reference; directly relevant to catalog SFR/sSFR context in the matched-control pilot. | Cite near catalog-property definitions and keep estimator assumptions/aperture caveats explicit. |
| 3 | The host galaxies and classification of active galactic nuclei | 2006MNRAS.372..961K | 2006 — Kewley, Lisa J., Groves, Brent, Kauffmann, Guinevere, Heckman, Tim | actual_data_or_method | AGN host/classification source tied to optical diagnostic diagrams; supports why BPT/line-ratio labels are classification proxies. | Use when defining optical-BPT classes and when warning that classification labels are not feedback measurements. |
| 4 | On the Star Formation-AGN Connection at z &lt;~ 0.3 | 2013ApJ...765L..33L | 2013 — LaMassa, Stephanie M., Heckman, T. M., Ptak, A., Urry, C. Megan | scoped_interpretation | Directly addresses star formation--AGN connection at low redshift, matching the pilot's association-only topic. | Use in Introduction/Discussion with wording such as 'context for the AGN--SFR connection', not as confirmation of a causal mechanism. |
| 5 | Retired galaxies: not to be forgotten in the quest of the star formation - AGN connection | 2015MNRAS.449..559S | 2015 — Stasińska, G., Costa-Duarte, M. V., Vale Asari, N., Cid Fernandes, R., Sodré, L. | overclaim_guard | Retired-galaxy/LINER caveat source for optical line classifications in AGN/SF studies. | Use in Limitations to demote broad AGN-feedback language and require stricter subclasses/follow-up. |

Integration guard: keep the measured result as a matched-control optical-AGN/sSFR association in the capped SDSS four-line denominator. The packet strengthens method provenance and retired/LINER caveats; it does not turn the offset into causal AGN-feedback evidence.

### M2 P3 — mass transition in quenching and optical AGN incidence

Current pilot boundary: Actual SDSS mass-bin quenched-fraction / optical-BPT-AGN incidence diagnostic; no gas fractions, halo masses, baryon deficits, or causal stellar-vs-AGN feedback separation.

Coverage roles observed: actual_data_or_method, future_data_guard, status_or_debate_context. Missing target roles: none.

| Priority | Source | ADS bibcode | Year / authors | Role | Why relevant | Safe integration guard |
|---:|---|---|---|---|---|---|
| 1 | The Seventeenth Data Release of the Sloan Digital Sky Surveys: Complete Release of MaNGA, MaStar, and APOGEE-2 Data | 2022ApJS..259...35A | 2022 — Abdurro'uf, Accetta, Katherine, Aerts, Conny, Silva Aguirre, Víctor, Ahumada, Romina, Ajgaonkar, Nikhil, et al. (341 authors) | actual_data_or_method | Public SDSS DR17 release paper; anchors the survey provenance for all three local SDSS pilots. | Use in Data/Sample sections to identify the public survey release and preserve the distinction between SDSS observables and missing follow-up data. |
| 2 | Stellar masses and star formation histories for 10<SUP>5</SUP> galaxies from the Sloan Digital Sky Survey | 2003MNRAS.341...33K | 2003 — Kauffmann, Guinevere, Heckman, Timothy M., White, Simon D. M., Charlot, Stéphane, Tremonti, Christy, Brinchmann, Jarle, et al. (22 authors) | actual_data_or_method | SDSS stellar-mass and star-formation-history methodology source; anchors why stellar mass is a central axis in the transition-mass pilot. | Use when describing stellar-mass binning and catalog mass dependence. |
| 3 | The dependence of star formation history and internal structure on stellar mass for 10<SUP>5</SUP> low-redshift galaxies | 2003MNRAS.341...54K | 2003 — Kauffmann, Guinevere, Heckman, Timothy M., White, Simon D. M., Charlot, Stéphane, Tremonti, Christy, Peng, Eric W., et al. (11 authors) | status_or_debate_context | Classic SDSS mass-dependence paper tying star-formation history/internal structure to stellar mass. | Use to motivate mass-bin diagnostics while explicitly requiring gas/halo/morphology controls before causal labels. |
| 4 | Quantifying the Bimodal Color-Magnitude Distribution of Galaxies | 2004ApJ...600..681B | 2004 — Baldry, Ivan K., Glazebrook, Karl, Brinkmann, Jon, Ivezić, Željko, Lupton, Robert H., Nichol, Robert C., et al. (7 authors) | status_or_debate_context | Observed color-magnitude bimodality source; relevant to quenching/transition framing around the stellar-mass scale. | Use in background, not as evidence that the pilot has measured the physical origin of bimodality. |
| 5 | Galaxy bimodality due to cold flows and shock heating | 2006MNRAS.368....2D | 2006 — Dekel, Avishai, Birnboim, Yuval | future_data_guard | Cold-flow/shock-heating model source for mass-scale quenching discussions. | Use only as motivation for missing halo/gas follow-up, not as support that the pilot identifies shock heating. |
| 6 | Mass and Environment as Drivers of Galaxy Evolution. II. The Quenching of Satellite Galaxies as the Origin of Environmental Effects | 2012ApJ...757....4P | 2012 — Peng, Ying-jie, Lilly, Simon J., Renzini, Alvio, Carollo, Marcella | status_or_debate_context | Mass/environment quenching framework; useful for separating mass transition from environmental satellite effects. | Use to motivate future environment/central-satellite controls and to avoid conflating mass with halo environment. |
| 7 | The Fundamental Signature of Star Formation Quenching from AGN Feedback: A Critical Dependence of Quiescence on Supermassive Black Hole Mass, Not Accretion Rate | 2023ApJ...944..108B | 2023 — Bluck, Asa F. L., Piotrowska, Joanna M., Maiolino, Roberto | future_data_guard | Recent debate/status source emphasizing quenching dependence on black-hole mass rather than accretion rate. | Use only to state which missing variables are needed before assigning the mass transition to AGN feedback. |

Integration guard: use transition/bimodality/quenching sources to motivate mass-bin diagnostics, while saying the pilot lacks gas, halo, black-hole-mass, and central/satellite data needed to separate stellar-feedback from AGN-feedback regulation.

### M3 P1 — common-denominator optical tracer census

Current pilot boundary: Actual SDSS optical tracer denominator only; no molecular/neutral/X-ray/radio common-denominator outflow rates or kinetic powers measured.

Coverage roles observed: actual_data_or_method, future_data_guard, multiphase_status_context. Missing target roles: none.

| Priority | Source | ADS bibcode | Year / authors | Role | Why relevant | Safe integration guard |
|---:|---|---|---|---|---|---|
| 1 | The Seventeenth Data Release of the Sloan Digital Sky Surveys: Complete Release of MaNGA, MaStar, and APOGEE-2 Data | 2022ApJS..259...35A | 2022 — Abdurro'uf, Accetta, Katherine, Aerts, Conny, Silva Aguirre, Víctor, Ahumada, Romina, Ajgaonkar, Nikhil, et al. (341 authors) | actual_data_or_method | Public SDSS DR17 release paper; anchors the survey provenance for all three local SDSS pilots. | Use in Data/Sample sections to identify the public survey release and preserve the distinction between SDSS observables and missing follow-up data. |
| 2 | The host galaxies and classification of active galactic nuclei | 2006MNRAS.372..961K | 2006 — Kewley, Lisa J., Groves, Brent, Kauffmann, Guinevere, Heckman, Tim | actual_data_or_method | AGN host/classification source tied to optical diagnostic diagrams; supports why BPT/line-ratio labels are classification proxies. | Use when defining optical-BPT classes and when warning that classification labels are not feedback measurements. |
| 3 | Galactic Winds | 2005ARA&A..43..769V | 2005 — Veilleux, Sylvain, Cecil, Gerald, Bland-Hawthorn, Joss | multiphase_status_context | Broad galactic-winds review; establishes that a true census is multiphase and multiwavelength. | Use in background/limitations to frame the need for phase-complete follow-up. |
| 4 | Massive molecular outflows and evidence for AGN feedback from CO observations | 2014A&A...562A..21C | 2014 — Cicone, C., Maiolino, R., Sturm, E., Graciá-Carpio, J., Feruglio, C., Neri, R., et al. (15 authors) | future_data_guard | CO molecular-outflow source; gives a concrete missing phase for the common-denominator census proposal. | Cite only when specifying the future CO/molecular phase needed beyond the optical denominator. |
| 5 | AGN wind scaling relations and the co-evolution of black holes and galaxies | 2017A&A...601A.143F | 2017 — Fiore, F., Feruglio, C., Shankar, F., Bischetti, M., Bongiorno, A., Brusa, M., et al. (17 authors) | future_data_guard | AGN wind scaling-relations source; motivates kinetic-power/outflow-rate measurements absent from the optical tracer table. | Use in the future-work paragraph requiring velocities, radii, phase masses, and selection-matched denominators. |
| 6 | The multi-phase winds of Markarian 231: from the hot, nuclear, ultra-fast wind to the galaxy-scale, molecular outflow | 2015A&A...583A..99F | 2015 — Feruglio, C., Fiore, F., Carniani, S., Piconcelli, E., Zappacosta, L., Bongiorno, A., et al. (12 authors) | future_data_guard | Multi-phase Markarian 231 wind case; illustrates how hot/ultra-fast and galaxy-scale molecular components differ. | Use as an example of phase complexity, not as a denominator-wide incidence result. |
| 7 | The Independence of Neutral and Ionized Gas Outflows in Low-z Galaxies | 2018ApJ...853..185B | 2018 — Bae, Hyun-Jin, Woo, Jong-Hak | future_data_guard | Neutral-vs-ionized outflow relation source; directly supports the guard that one phase cannot stand in for all phases. | Use to warn that optical tracer prevalence cannot be extrapolated to neutral or molecular outflow prevalence without matched data. |
| 8 | A Review of Recent Observations of Galactic Winds Driven by Star Formation | 2018Galax...6..138R | 2018 — Rupke, David S. N. | multiphase_status_context | Recent galactic-winds observational review, useful as a non-AGN/stellar-feedback counterweight when discussing outflow drivers. | Use in background/limitations to separate AGN-driven, star-formation-driven, and mixed wind populations. |

Integration guard: call the current table an optical common-denominator tracer census. Use multiphase outflow sources only to justify why CO/HI/Na I/X-ray/radio/kinematic follow-up is required.

## Bibliography-gap actions for a later manuscript integration pass

1. RP-1: add DR17 and sSFR/catalog-method provenance, then add a retired/LINER caveat paragraph before any causal language.
2. M2 P3: add mass-transition/bimodality/quenching context, but label halo-shock and black-hole-mass papers as future-data/debate guards, not measured results.
3. M3 P1: add multiphase wind/outflow citations only in the background/future-work sections; the result table remains optical-only.
4. Preserve the selection-function disclosure from the attrition packet before merging any citation-enhanced draft into a primary manuscript.

## Artifact manifest

- Deduplicated JSONL candidate ledger: `lanes/literature/literature_sources_wave3_missing_active9_20260708T170557Z.jsonl`
- Summary JSON: `lanes/literature/literature_summary_wave3_missing_active9_20260708T170557Z.json`
- Raw ADS payloads for m1_rp1_sdss_agn_sfr: `lanes/literature/raw_payloads/20260708T170557Z/m1_rp1_sdss_agn_sfr_ads_identifier_payloads.json`
- Raw ADS payloads for m2_p3_feedback_transition_mass: `lanes/literature/raw_payloads/20260708T170557Z/m2_p3_feedback_transition_mass_ads_identifier_payloads.json`
- Raw ADS payloads for m3_p1_multiphase_census: `lanes/literature/raw_payloads/20260708T170557Z/m3_p1_multiphase_census_ads_identifier_payloads.json`
- Raw arXiv XML for m1_rp1_sdss_agn_sfr: `lanes/literature/raw_payloads/20260708T170557Z/m1_rp1_sdss_agn_sfr_arxiv_id_list.xml`
- Raw arXiv XML for m2_p3_feedback_transition_mass: `lanes/literature/raw_payloads/20260708T170557Z/m2_p3_feedback_transition_mass_arxiv_id_list.xml`
- Raw arXiv XML for m3_p1_multiphase_census: `lanes/literature/raw_payloads/20260708T170557Z/m3_p1_multiphase_census_arxiv_id_list.xml`
- Semantic Scholar status probe: `lanes/literature/raw_payloads/20260708T170557Z/semantic_scholar_status_check.json`
- Goru-style mechanical validation: `lanes/goru/ticks/GORU_LITERATURE_WAVE3_VALIDATE_20260708T170557Z.md` and `lanes/goru/artifacts/goru_literature_wave3_validation_20260708T170557Z.json`

## Safety ledger

No public pages, live roots, product DB, SQL, `/api/pages`, page_versions, trust recompute, deploy/restart, git write, billing/OAuth changes, new cron jobs, or external submissions. No active execution phrase.
