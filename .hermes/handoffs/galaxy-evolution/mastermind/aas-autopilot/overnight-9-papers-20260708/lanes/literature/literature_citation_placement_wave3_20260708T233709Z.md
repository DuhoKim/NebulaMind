# Literature/source grounding Wave-3 citation placement — 20260708T233709Z

Marker: `LITERATURE_WAVE3_CITATION_PLACEMENT_20260708T233709Z`

Scope: lane-local source grounding for M1 RP-1, M2 P3, and M3 P1. No manuscript/public/page/API/database/git/deploy changes.

## Inputs checked
- `OVERNIGHT_BRIEF.md`
- `SWARM_BOARD.md`
- `runs/SDSS_AGN_SFR_PILOT_20260708T122000Z/aastex/sdss_agn_sfr_pilot_aas.tex`
- `runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_aas.tex`
- `runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_aas.tex`
- `lanes/lana/revision-drafts/m1_rp1_sdss_agn_sfr/aastex/sdss_agn_sfr_pilot_lana_control_baseline_20260708T204532Z.tex`
- `lanes/lana/revision-drafts/m2_p3_feedback_transition_mass/aastex/m2_p3_feedback_transition_mass_lana_claim_contract_20260708T204532Z.tex`
- `lanes/lana/revision-drafts/m3_p1_multiphase_census/aastex/m3_p1_multiphase_census_lana_threshold_contract_20260708T204532Z.tex`
- `topic pages/current+backup under frontend/public/agent-reports/wiki-method-results/galaxy-evolution/`

## API/artifact summary
- Public arXiv records requested: 20; arXiv status: `200`.
- Public Semantic Scholar batch status: `200` (raw/status saved even if rate-limited).
- JSONL records: 21; duplicate record keys: none.
- Raw payloads: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/literature/raw_payloads/20260708T233709Z`
- JSONL: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/literature/literature_sources_wave3_citation_placement_20260708T233709Z.jsonl`
- Summary JSON: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/overnight-9-papers-20260708/lanes/literature/literature_summary_wave3_citation_placement_20260708T233709Z.json`

## m1_rp1_sdss_agn_sfr
- **The Seventeenth Data Release of the Sloan Digital Sky Surveys: Complete Release of MaNGA, MaStar and APOGEE-2 Data** (2021;  Abdurro'uf, Katherine Accetta, Conny Aerts, Victor Silva Aguirre, Romina Ahumada, Nikhil Ajgaonkar, et al.).
  - URLs: arXiv: https://arxiv.org/abs/2112.02026v2; Semantic Scholar: https://www.semanticscholar.org/paper/6216b758b107999a9298fb76e6c3b7c439a8f9d8; DOI: https://doi.org/10.3847/1538-4365/ac4414
  - Placement: Data/sample provenance for SDSS DR17; cite wherever the public SDSS release is named.
  - Relevance: Grounds the survey release used by the cached DR17 optical-denominator analysis.
  - Use class: supports the actual SDSS method/data provenance or method guardrail; it still does not make the pilot causal.
- **The physical properties of star forming galaxies in the low redshift universe** (2003; J. Brinchmann, S. Charlot, S. D. M. White, C. Tremonti, G. Kauffmann, T. Heckman, et al.).
  - URLs: arXiv: https://arxiv.org/abs/astro-ph/0311060v2; Semantic Scholar: https://www.semanticscholar.org/paper/ad6e9e16252b74aa4c65def5ef98d41ed2b5e82e; DOI: https://doi.org/10.1111/j.1365-2966.2004.07881.x
  - Placement: Data/sample and Discussion paragraphs on catalog stellar mass and SFR/sSFR estimator assumptions.
  - Relevance: Documents SDSS low-redshift physical-property/SFR context; helps keep the RP-1 offset framed as a catalog-sSFR association.
  - Use class: supports the actual SDSS method/data provenance or method guardrail; it still does not make the pilot causal.
- **The Host Galaxies and Classification of Active Galactic Nuclei** (2006; Lisa J. Kewley, Brent Groves, Guinevere Kauffmann, Tim Heckman).
  - URLs: arXiv: https://arxiv.org/abs/astro-ph/0605681v3; Semantic Scholar: https://www.semanticscholar.org/paper/87929df561524051f18e252cc8112c6c3db8ddb9; DOI: https://doi.org/10.1111/j.1365-2966.2006.10859.x
  - Placement: Classification and Discussion guardrail after broad BPT-AGN definition.
  - Relevance: Explains AGN host classification and Seyfert/LINER branches; supports subclass/retired-ionization caveats, not the feedback conclusion.
  - Use class: supports the actual SDSS method/data provenance or method guardrail; it still does not make the pilot causal.
- **Retired galaxies: not to be forgotten in the quest of the star formation -- AGN connection** (2015; G. Stasińska, M. V. Costa Duarte, N. Vale Asari, R. Cid Fernandes, L. Sodré).
  - URLs: arXiv: https://arxiv.org/abs/1501.03812v1; Semantic Scholar: https://www.semanticscholar.org/paper/961870207f3f897d9281f5a9b723c55c244ab60f; DOI: https://doi.org/10.1093/mnras/stv078
  - Placement: Discussion caveat on LINER-like or retired-galaxy ionization contaminating broad BPT-AGN labels.
  - Relevance: Direct guardrail for interpreting optical line-ratio AGN in low-sSFR systems; it weakens causal language rather than supporting it.
  - Use class: motivates context/future data or guards interpretation only; do **not** cite as support for the pilot's measured result.
- **Can retired galaxies mimic active galaxies? Clues from the Sloan Digital Sky Survey** (2008; G. Stasinska, N. V. Asari, R. Cid Fernandes, J. M. Gomes, M. Schlickmann, A. Mateus, et al.).
  - URLs: arXiv: https://arxiv.org/abs/0809.1341v1; Semantic Scholar: https://www.semanticscholar.org/paper/5c269422552d3b8156b3e4d07021aad4abec7a4f; DOI: https://doi.org/10.1111/j.1745-3933.2008.00550.x
  - Placement: Optional added citation beside the retired/LINER caution if the manuscript needs a more explicit retired-galaxy anchor.
  - Relevance: Motivates not treating all AGN-looking line ratios as accreting AGN feedback signatures.
  - Use class: motivates context/future data or guards interpretation only; do **not** cite as support for the pilot's measured result.
- **On the Star Formation-AGN Connection at $z \lesssim 0.3$** (2013; Stephanie M. LaMassa, Timothy M. Heckman, Andrew Ptak, C. Megan Urry).
  - URLs: arXiv: https://arxiv.org/abs/1302.2631v1; Semantic Scholar: https://www.semanticscholar.org/paper/4013b1fc07a9f1d6454d2a2d27e4c5fad2283d70; DOI: https://doi.org/10.1088/2041-8205/765/2/L33
  - Placement: Introduction as motivation for a low-redshift AGN--star-formation association test.
  - Relevance: Useful context for RP-1, but does not validate the cached SDSS result or causal feedback.
  - Use class: motivates context/future data or guards interpretation only; do **not** cite as support for the pilot's measured result.

## m2_p3_feedback_transition_mass
- **The Seventeenth Data Release of the Sloan Digital Sky Surveys: Complete Release of MaNGA, MaStar and APOGEE-2 Data** (2021;  Abdurro'uf, Katherine Accetta, Conny Aerts, Victor Silva Aguirre, Romina Ahumada, Nikhil Ajgaonkar, et al.).
  - URLs: arXiv: https://arxiv.org/abs/2112.02026v2; Semantic Scholar: https://www.semanticscholar.org/paper/6216b758b107999a9298fb76e6c3b7c439a8f9d8; DOI: https://doi.org/10.3847/1538-4365/ac4414
  - Placement: Data/sample provenance for SDSS DR17; cite wherever the public SDSS release is named.
  - Relevance: Grounds the survey release used by the cached DR17 optical-denominator analysis.
  - Use class: supports the actual SDSS method/data provenance or method guardrail; it still does not make the pilot causal.
- **Stellar Masses and Star Formation Histories for 10^5 Galaxies from the Sloan Digital Sky Survey** (2002; Guinevere Kauffmann, Timothy M. Heckman, Simon D. M. White, Stephane Charlot, Christy Tremonti, Jarle Brinchmann, et al.).
  - URLs: arXiv: https://arxiv.org/abs/astro-ph/0204055v2; Semantic Scholar: https://www.semanticscholar.org/paper/56357df21e86010d20f3fd7e44b96905847a3a32; DOI: https://doi.org/10.1046/j.1365-8711.2003.06291.x
  - Placement: Scope/source grounding for the SDSS stellar-mass axis and catalog physical-property context.
  - Relevance: Supports use of stellar mass as an empirical axis in the SDSS denominator; not a feedback-regime proof.
  - Use class: supports the actual SDSS method/data provenance or method guardrail; it still does not make the pilot causal.
- **The Dependence of Star Formation History and Internal Structure on Stellar Mass for 10^5 Low-Redshift Galaxies** (2002; Guinevere Kauffmann, Timothy M. Heckman, Simon D. M. White, Stephane Charlot, Christy Tremonti, Eric W. Peng, et al.).
  - URLs: arXiv: https://arxiv.org/abs/astro-ph/0205070v2; Semantic Scholar: https://www.semanticscholar.org/paper/31f0d6aa72e2288be650f4e9e1114cb29377b549; DOI: https://doi.org/10.1046/j.1365-8711.2003.06292.x
  - Placement: Scope/source grounding where the manuscript motivates stellar mass and structure as transition variables.
  - Relevance: Anchors the mass/structure dependence of low-redshift galaxy star-formation histories; motivates but does not prove the physical transition.
  - Use class: motivates context/future data or guards interpretation only; do **not** cite as support for the pilot's measured result.
- **Quantifying the bimodal color-magnitude distribution of galaxies** (2003; I. K. Baldry, K. Glazebrook, J. Brinkmann, Z. Ivezic, R. H. Lupton, R. C. Nichol, et al.).
  - URLs: arXiv: https://arxiv.org/abs/astro-ph/0309710v1; Semantic Scholar: https://www.semanticscholar.org/paper/af4df63a72fdbd417f16c0011249b3c4f4259c25; DOI: https://doi.org/10.1086/380092
  - Placement: Introduction/source grounding for bimodality/transition framing.
  - Relevance: Motivates mass-binned low-sSFR/colour-transition diagnostics; not evidence for AGN causality.
  - Use class: motivates context/future data or guards interpretation only; do **not** cite as support for the pilot's measured result.
- **Mass and environment as drivers of galaxy evolution in SDSS and zCOSMOS and the origin of the Schechter function** (2010; Y. Peng, S. J. Lilly, K. Kovac, M. Bolzonella, L. Pozzetti, A. Renzini, et al.).
  - URLs: arXiv: https://arxiv.org/abs/1003.4747v2; Semantic Scholar: https://www.semanticscholar.org/paper/459b293a867451edd4dc9ed3284842f5bef368c4; DOI: https://doi.org/10.1088/0004-637X/721/1/193
  - Placement: Interpretation guard separating mass and environment quenching channels.
  - Relevance: Supports caution that mass-linked and environmental effects must be decomposed before attributing the SDSS mass vector to AGN feedback.
  - Use class: motivates context/future data or guards interpretation only; do **not** cite as support for the pilot's measured result.
- **Mass and Environment as Drivers of Galaxy Evolution II: The quenching of satellite galaxies as the origin of environmental effects** (2011; Yingjie Peng, Simon J. Lilly, Alvio Renzini, Marcella Carollo).
  - URLs: arXiv: https://arxiv.org/abs/1106.2546v2; Semantic Scholar: https://www.semanticscholar.org/paper/d49f5ce693d0b21192fb35eb160c22f497eaab26; DOI: https://doi.org/10.1088/0004-637X/757/1/4
  - Placement: Future-data/interpretation guard for central-satellite and environment separation.
  - Relevance: Shows why a transition-mass claim needs central/satellite/environment labels; motivates future data only for this pilot.
  - Use class: motivates context/future data or guards interpretation only; do **not** cite as support for the pilot's measured result.
- **Galaxy Bimodality due to Cold Flows and Shock Heating** (2004; Avishai Dekel, Yuval Birnboim).
  - URLs: arXiv: https://arxiv.org/abs/astro-ph/0412300v3; Semantic Scholar: https://www.semanticscholar.org/paper/06cf7e096ed3fd4239f7e90e3a5a98e0ec7cfa55; DOI: https://doi.org/10.1111/j.1365-2966.2006.10145.x
  - Placement: Interpretation guard where halo shock/hot-mode language appears.
  - Relevance: Motivates a halo-scale physical mechanism that the current SDSS optical table cannot test directly.
  - Use class: motivates context/future data or guards interpretation only; do **not** cite as support for the pilot's measured result.
- **The fundamental signature of star formation quenching from AGN feedback: A critical dependence of quiescence on supermassive black hole mass not accretion rate** (2023; Asa F. L. Bluck, Joanna M. Piotrowska, Roberto Maiolino).
  - URLs: arXiv: https://arxiv.org/abs/2301.03677v1; Semantic Scholar: https://www.semanticscholar.org/paper/94c087b431f0f866a5bb807224bf64554375c647; DOI: https://doi.org/10.3847/1538-4357/acac7c
  - Placement: Future-data paragraph requiring black-hole mass or velocity-dispersion information.
  - Relevance: Supports the manuscript guard that optical AGN incidence is not a substitute for black-hole-mass or accretion-history information.
  - Use class: motivates context/future data or guards interpretation only; do **not** cite as support for the pilot's measured result.
- **On the quenching of star formation in observed and simulated central galaxies: Evidence for the role of integrated AGN feedback** (2021; Joanna M. Piotrowska, Asa F. L. Bluck, Roberto Maiolino, Yingjie Peng).
  - URLs: arXiv: https://arxiv.org/abs/2112.07672v1; Semantic Scholar: https://www.semanticscholar.org/paper/6878e61a69bdf1f81114fff1aa27f1743011023a; DOI: https://doi.org/10.1093/mnras/stab3673
  - Placement: Optional future-data/interpretation citation for integrated AGN-feedback tests in central galaxies.
  - Relevance: Useful as a comparator for a later physical-transition analysis; does not support the current optical-denominator result by itself.
  - Use class: motivates context/future data or guards interpretation only; do **not** cite as support for the pilot's measured result.

## m3_p1_multiphase_census
- **The Seventeenth Data Release of the Sloan Digital Sky Surveys: Complete Release of MaNGA, MaStar and APOGEE-2 Data** (2021;  Abdurro'uf, Katherine Accetta, Conny Aerts, Victor Silva Aguirre, Romina Ahumada, Nikhil Ajgaonkar, et al.).
  - URLs: arXiv: https://arxiv.org/abs/2112.02026v2; Semantic Scholar: https://www.semanticscholar.org/paper/6216b758b107999a9298fb76e6c3b7c439a8f9d8; DOI: https://doi.org/10.3847/1538-4365/ac4414
  - Placement: Data/sample provenance for SDSS DR17; cite wherever the public SDSS release is named.
  - Relevance: Grounds the survey release used by the cached DR17 optical-denominator analysis.
  - Use class: supports the actual SDSS method/data provenance or method guardrail; it still does not make the pilot causal.
- **Galactic Winds** (2005; S. Veilleux, G. Cecil, J. Bland-Hawthorn).
  - URLs: Semantic Scholar: https://www.semanticscholar.org/paper/bcadc33db4acd4f7b77060cc606a00e8a51661db; DOI: https://doi.org/10.1146/annurev.astro.43.072103.150610
  - Placement: Scope/source grounding for why real outflow census work is multiphase/kinematic.
  - Relevance: Review-level anchor for physical wind observables; motivates future data rather than validating SDSS optical thresholds.
  - Use class: motivates context/future data or guards interpretation only; do **not** cite as support for the pilot's measured result.
- **A Review of Recent Observations of Galactic Winds Driven by Star Formation** (2018; David S. N. Rupke).
  - URLs: arXiv: https://arxiv.org/abs/1812.05184v1; Semantic Scholar: https://www.semanticscholar.org/paper/0564e19c53f748a79a10d9ed95d64d703ede583b; DOI: https://doi.org/10.3390/galaxies6040138
  - Placement: Scope/source grounding beside Veilleux review; clarifies that tracer prevalence needs phase/kinematic definitions.
  - Relevance: Review anchor for wind observations; supports interpretation guard, not the current SDSS prevalence as outflows.
  - Use class: motivates context/future data or guards interpretation only; do **not** cite as support for the pilot's measured result.
- **Massive Molecular Outflows and Evidence for AGN Feedback from CO Observations** (2013; C. Cicone, R. Maiolino, E. Sturm, J. Graciá-Carpio, C. Feruglio, R. Neri, et al.).
  - URLs: arXiv: https://arxiv.org/abs/1311.2595v1; Semantic Scholar: https://www.semanticscholar.org/paper/e49b1ac6be152076515288d513e53546d8f11e05; DOI: https://doi.org/10.1051/0004-6361/201322464
  - Placement: Future-data paragraph requiring molecular gas measurements.
  - Relevance: Concrete molecular-outflow anchor showing what the current SDSS optical table lacks.
  - Use class: motivates context/future data or guards interpretation only; do **not** cite as support for the pilot's measured result.
- **AGN wind scaling relations and the co-evolution of black holes and galaxies** (2017; F. Fiore, C. Feruglio, F. Shankar, M. Bischetti, A. Bongiorno, M. Brusa, et al.).
  - URLs: arXiv: https://arxiv.org/abs/1702.04507v1; Semantic Scholar: https://www.semanticscholar.org/paper/6c038b9c2c452bda6f67f5f6419c29a31455f25e; DOI: https://doi.org/10.1051/0004-6361/201629478
  - Placement: Future-data paragraph on wind scalings, velocities, and energetics.
  - Relevance: Motivates comparing wind quantities across phases; not evidence that SDSS line-ratio flags are outflows.
  - Use class: motivates context/future data or guards interpretation only; do **not** cite as support for the pilot's measured result.
- **The multi-phase winds of Markarian 231: from the hot, nuclear, ultra-fast wind to the galaxy-scale, molecular outflow** (2015; C. Feruglio, F. Fiore, S. Carniani, E. Piconcelli, L. Zappacosta, A. Bongiorno, et al.).
  - URLs: arXiv: https://arxiv.org/abs/1503.01481v2; Semantic Scholar: https://www.semanticscholar.org/paper/fab7b91c2700b38e05d70a08ad1846f53986e917; DOI: https://doi.org/10.1051/0004-6361/201526020
  - Placement: Future-data paragraph or caveat that single-object multiphase detections are physics anchors, not denominator prevalence.
  - Relevance: Illustrates multiphase measurements beyond SDSS optical ratios; should not be used as a population prevalence anchor.
  - Use class: motivates context/future data or guards interpretation only; do **not** cite as support for the pilot's measured result.
- **The Prevalence of Gas Outflows in Type 2 AGNs** (2015; Jong-Hak Woo, Hyun-Jin Bae, Donghoon Son, Marios Karouzos).
  - URLs: arXiv: https://arxiv.org/abs/1511.05142v3; Semantic Scholar: https://www.semanticscholar.org/paper/753842e2631cc6f1ed9b2613e0be118758ed9b83; DOI: https://doi.org/10.3847/0004-637X/828/2/97
  - Placement: Cautionary prevalence/context citation for ionized-gas outflows in Type 2 AGN.
  - Relevance: Relevant to future denominator design; its sample/selection should not be merged with the cached SDSS optical threshold fractions.
  - Use class: motivates context/future data or guards interpretation only; do **not** cite as support for the pilot's measured result.
- **The independence of neutral and ionized gas outflows in low-z galaxies** (2017; Hyun-Jin Bae, Jong-Hak Woo).
  - URLs: arXiv: https://arxiv.org/abs/1712.08944v2; Semantic Scholar: https://www.semanticscholar.org/paper/4d53bf786894d21b4beba1e9bd23c271bf0aae15; DOI: https://doi.org/10.3847/1538-4357/aaa42d
  - Placement: Future-data paragraph requiring separate neutral and ionized outflow measurements.
  - Relevance: Directly supports the guardrail that one phase/tracer cannot stand in for a multiphase census.
  - Use class: motivates context/future data or guards interpretation only; do **not** cite as support for the pilot's measured result.

## Integration guidance
- M1 RP-1 is strengthened by keeping SDSS DR17/MPA-JHU/BPT method citations adjacent to the method and retired/LINER citations adjacent to the caveat; LaMassa is only motivation.
- M2 P3 should keep the mass-vector result separate from physical transition claims: Kauffmann/Baldry support the empirical axes, while Peng/Dekel/Bluck/Piotrowska motivate variables missing from this pilot.
- M3 P1 should use the wind/outflow sources to say what a real multiphase census needs; none converts SDSS optical threshold fractions into outflow incidence.

## Safety
No credentials used. No DB/API/page_versions/wiki publish/live mirror/deploy/restart/git/cron/billing/OAuth/external submission changes. Writes were limited to this literature lane plus the separately authorized ledger append.
