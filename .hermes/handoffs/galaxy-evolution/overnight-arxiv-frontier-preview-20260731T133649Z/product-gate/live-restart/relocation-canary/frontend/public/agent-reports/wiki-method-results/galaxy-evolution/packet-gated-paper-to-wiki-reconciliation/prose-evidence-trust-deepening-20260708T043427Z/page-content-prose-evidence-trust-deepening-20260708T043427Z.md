# Galaxy Evolution — Method1 deterministic deepening v2 candidate

Parent marker: `AUTOPILOT_PROSE_EVIDENCE_TRUST_DEEPENING_20260708T043427Z`
Seed marker: `DEEPENING_RESOURCE_SEED_20260708T043427Z`
Status: progress/candidate artifact; not a final no-apply packet before `2026-07-08T06:34:40Z`.

This candidate deepens the first-pass M1 prose/evidence/trust upgrade while preserving evidence IDs, trust levels, paper links, article claim IDs, and the 3/30 bound model. It adds a clearer caution for claim `2929`, distinguishes evidence rows from distinct papers, and keeps the 27 unbound-local chips labeled as local evidence gaps rather than high-trust claims.

Coverage: `30` claim chips; `3` locally bound claims (`2931`, `2929`, `2946`); `27` unbound-local chips; `43` evidence rows across `26` distinct normalized arXiv IDs.

## Trust vocabulary

- `debated`: local ledger trust for `2931`; mixed support/context rows.
- `unverified`: local ledger trust for `2929`; all local rows are non-committal in this binding and should be read as context/caution, not direct support.
- `reported`: local ledger trust for `2946`; support remains model-bounded/reported, not consensus.
- `no local evidence / unbound`: not a trust level; the static candidate does not have local evidence rows for those chips.

## Article body

# Galaxy Evolution — Method1 prose/evidence/trust upgrade candidate

Markers: `AUTOPILOT_PROSE_EVIDENCE_TRUST_WIKI_UPGRADE_20260708T041216Z` · `PROSE_UPGRADE_RESOURCE_SEED_20260708T041216Z`

This static Method1 candidate keeps the same Galaxy Evolution article shape, but makes the evidence/trust layer easier to read. Three claim chips are locally evidence-bound in the Method1 ledger: claim `2931` is debated with 20 rows, claim `2929` is unverified with 14 rows, and claim `2946` is reported with 9 rows. The remaining 27 chips are real provenance chips but are labeled `no local evidence / unbound` in this candidate because their per-claim trust is not available from the local Method1 evidence/trust binding files.

Trust vocabulary in this candidate is deliberately narrow: `debated`, `unverified`, and `reported` are copied from the local bindings for the three bound claims. `No local evidence / unbound` is not a trust score and must not be read as high trust; it means the static Method1 artifact did not bind local evidence rows for that chip.

Limitations: no product DB/API calls, no page-version record write, no live wiki publication, no invented evidence IDs, and no invented citations. External paper links are the stored arXiv URLs from the bindings JSON.

# Galaxy Evolution

> Highlighted claim chips mark statements with provenance in the underlying claim/evidence layer. They are used sparingly here: the page is a narrative synthesis first, with the fuller evidence graph available through the linked claim surfaces.

## Overview: Galaxy Evolution as a Regulated Baryon Cycle

Galaxy evolution is the study of how dark matter halos, gas accretion, star formation, feedback, environment, and cosmic time combine to build the observed galaxy population. The useful modern picture is not a single ladder from blue spirals to red ellipticals. It is a regulated baryon cycle: halos assemble and acquire gas, galaxies convert only part of that gas into stars, feedback returns energy and enriched material to the circumgalactic medium, and quenching processes eventually reduce or shut down star formation.

The red sequence, green valley, and blue cloud remain useful observational landmarks, but they are outcomes rather than mechanisms. A clear synthesis should therefore start with causal structure: what sets the baryon supply, what regulates star formation, what shuts galaxies down, and which observations separate internal feedback from external processing. Galaxy quenching is jointly regulated by internal mass-linked processes and environment-linked processes; the separability and relative priority of those channels depend on sample selection, redshift, and how quenching is measured. [2931 · debated · 20 evidence]

## Dark Matter Halos & Structure Formation

Dark matter halos provide the gravitational scaffolding for galaxy formation, but halo mass alone does not determine how efficiently baryons become stars. At the low-mass end, shallow potential wells make galaxies sensitive to feedback: Stellar feedback suppresses star formation in lower mass halos. [2905 · no local evidence / unbound] In the same regime, feedback is not merely an after-the-fact correction, because in low-mass halos, stellar feedback processes regulate the baryon cycle. [2906 · no local evidence / unbound]

The connection between halo history and galaxy properties is less settled than a one-parameter halo-mass model would suggest. halo assembly history shapes galaxy properties. [2912 · no local evidence / unbound] Similarly, the properties of a galaxy are shaped by its host dark matter halo. [2918 · no local evidence / unbound] Those statements are best read conditionally: metallicity, large-scale environment, gas supply, feedback timing, and merger history can redirect similar halos into different visible outcomes.

At the massive end and at cosmic noon, quiescent systems probe how stellar shutdown couples to halo growth. Massive quiescent galaxies at $z\sim2-3$ are hosted by dark matter halos with masses of approximately $10^{12.5}$-$10^{13}\,M_\odot$. [2920 · no local evidence / unbound] High-redshift massive-galaxy claims should be written cautiously. JWST has sharpened tensions between inferred stellar masses and expected halo abundances, but stellar-population modeling, dust, emission-line contamination, AGN light, IMF assumptions, and spectroscopic completeness all affect the interpretation. The observations are powerful tests of galaxy-formation efficiency and modeling assumptions, not automatic falsifications of the cosmological frame.

## Gas Supply, Star Formation & Feedback

The gas cycle links accretion, the interstellar medium, the circumgalactic medium, and later recycling. Stellar feedback is the clearest bridge between local star formation and galaxy-scale regulation: stellar feedback drives galactic outflows. [2909 · no local evidence / unbound] Those outflows can remove low-entropy gas, stir the circumgalactic medium, regulate metal retention, and change the later supply available for star formation.

Star formation follows the usable cold-gas supply, the density and turbulence of that gas, and the timescale on which inflow replenishes it. Gas removal and depletion can suppress star formation by reducing the usable cold-gas reservoir, but the evidence should distinguish true reservoir loss from morphological quenching, turbulent regulation, and environment-specific stripping. [2930 · no local evidence / unbound] That distinction matters because reservoir removal, suppressed inflow, turbulent support, morphological stabilization, and cluster stripping leave different observational signatures.

Not every proposed feedback channel is equally settled. In dusty, optically thick star-forming environments, radiation pressure remains a live point of tension: radiation pressure is a significant feedback mechanism in environments with high optical depth to UV photons. [2916 · no local evidence / unbound] Gas depletion time is one way to connect star-formation rate to the available molecular reservoir, but the presence of gas is not the same as efficient star formation. early-type galaxies can exhibit molecular gas depletion timescales exceeding 10 Gyr. [2911 · no local evidence / unbound] At the opposite boundary, the molecular gas depletion timescale in starbursts and galaxy mergers can be as short as about 100 Myr. [2907 · no local evidence / unbound] These are boundary conditions, not universal recipes.

## AGN Feedback & Quenching

Quenching is not a single event. It can be rapid or slow, central or environmental, preventive or ejective, and it can leave different signatures in stellar populations, gas reservoirs, and morphology. At cosmic noon, AGN-linked shutdown is often discussed as a fast channel: the quenching of star formation in massive galaxies by AGN feedback at $z\sim2$ is a rapid process. [2913 · no local evidence / unbound]

The stronger AGN synthesis is conditional rather than absolutist. Internal AGN feedback can regulate or quench star formation through jets, outflows, turbulence, circumgalactic heating, and starvation, but the sign and strength of the effect depend on feedback mode and gas phase, and positive feedback can occur locally. [2929 · unverified · 14 evidence] Mechanistically, Active galactic nuclei can drive feedback through a kinetic mode, where powerful jets and outflows mechanically interact with the surrounding medium. [2915 · no local evidence / unbound] Over longer timescales, sustained AGN heating of hot gas reservoirs is reported as a maintenance mechanism in massive systems, though its support remains model-dependent or simulation-bounded rather than a measured prevalence. [2946 · reported · 9 evidence] Together, those claims support a picture in which jets, winds, and hot-halo heating can reduce the cooling flow that would otherwise refuel star formation without requiring every AGN episode to quench a galaxy.

Central structure is another route into quenching. Central galaxy quenching is influenced by properties such as velocity dispersion, bulge mass, and central black hole mass. [2917 · no local evidence / unbound] In the same family of observables, the growth of central stellar mass density is linked to mass quenching. [2921 · no local evidence / unbound] These observables should be treated as coupled diagnostics rather than independent switches.

## Environment, Morphology & Structural Growth

Environment changes galaxies by stripping, starving, perturbing, and merging them. In clusters, environmental processing can transform star-forming disks into passive lenticular systems: the morphological transformation of quenched disks in clusters results in the formation of S0 galaxies. [2914 · no local evidence / unbound] That is a structural statement as much as a star-formation statement, because it links a galaxy's orbit and gas loss to its final morphology.

Satellite and cosmic-web claims sharpen the environmental picture. Satellite galaxies can experience environmental quenching after infall into groups or clusters, especially when simulations or observations identify quenched low-mass systems as satellite analogues rather than isolated centrals. [2934 · no local evidence / unbound] Galaxy environment correlates with morphology and colour, but alignment or morphology-only evidence should be treated as contextual unless it directly connects dense environments to quenched early-type populations. [2932 · no local evidence / unbound] At high redshift, Environmental quenching signatures at high redshift are plausible but should be presented as an active observational constraint, not as a settled universal pathway. [2933 · no local evidence / unbound]

Dense environments do not act through one channel. Dense groups and clusters can accelerate transformation through hydrodynamical interaction with the intracluster medium and gravitational processing, but the dominant channel is system-dependent. [2936 · no local evidence / unbound] Outside groups and clusters, Cosmic-web filaments, sheets, nodes, and voids can shape galaxy evolution through coherent tidal fields that torque protogalactic gas and influence later accretion geometry. [2935 · no local evidence / unbound] The role of environment also has a boundary case: Environmental effects are not a primary quenching mechanism in isolated massive galaxies. [2908 · no local evidence / unbound] That claim is useful because it separates isolated systems from clusters and groups, but it should remain caveated until reconciled with the broader environmental-quenching literature.

Mergers are a second structural channel, but different merger regimes should be separated. The minor-merger route remains contested: mass growth from minor mergers is consistent with the observed size evolution of massive elliptical galaxies. [2922 · no local evidence / unbound] Major mergers are more direct events in this section's narrative: major mergers can increase galaxy size by a factor of approximately two while doubling the stellar mass. [2923 · no local evidence / unbound]

## Chemical Enrichment & Cosmic Timing

Chemical enrichment records the integrated history of star formation, inflow, and outflow. Metallicity scaling relations act as clocks and regulators: they encode how much gas has been processed into stars, how much enriched material has been lost, and how much low-metallicity gas has diluted the interstellar medium. The fundamental metallicity relation is consistent to within approximately 0.1 dex in oxygen abundance from redshift $z=0$ to $z\sim2.3$. [2910 · no local evidence / unbound] That stability constrains baryon-cycle models across a large fraction of cosmic time.

This timing perspective explains why galaxy evolution is not simply a sequence from blue disks to red spheroids. Different galaxies can enter the same observed class by different routes: early gas exhaustion, central quenching, environmental processing, late structural assembly, or combinations of these mechanisms. Low-mass chemically active systems in sparse environments add a caution: environment is not a one-directional predictor of gas content or future quenching.

## High-Redshift & Reionization Frontier

At high redshift, galaxy evolution connects directly to reionization and to the first dense stellar systems. Environmental effects can appear early in the low-mass population: environmental quenching can suppress star formation in low-mass galaxies at high redshift. [2919 · no local evidence / unbound] The same era raises the question of which sources supplied enough ionizing photons to reionize the intergalactic medium.

Globular-cluster progenitors are one candidate source population. Globular clusters are sources of ionizing photons during the epoch of reionization ($z\gt 6$). [2925 · no local evidence / unbound] The relative contribution of those systems remains unsettled rather than a settled replacement for faint galaxies: the ionizing photon contribution from faint galaxies during the reionization epoch is secondary to that of proto-globular clusters. [2926 · no local evidence / unbound] Current evidence is mixed, so competing source populations should remain side by side until the source budget is better constrained.

## Observational Evidence & Surveys

The evidence base is multi-wavelength and redshift-dependent. Rest-frame optical and near-infrared spectra constrain stellar populations, nebular lines, metallicities, and dust. Submillimetre and radio observations constrain hidden star formation and molecular or atomic gas. X-ray and radio signatures identify AGN power and hot atmospheres. Integral-field spectroscopy maps outflows, rotation, turbulence, and spatially resolved quenching. Large imaging and spectroscopic surveys connect individual mechanisms to population statistics.

Current and near-future facilities should be framed by the physical ambiguity they reduce. JWST constrains rest-frame optical diagnostics at high redshift and tests early mass budgets. ALMA and radio facilities trace molecular gas, dust-obscured star formation, and cold reservoirs. Euclid, Rubin, DESI, and related wide surveys connect galaxy populations to large-scale environment, weak lensing, clustering, and cosmic-web structure. The point is not to list missions; it is to connect each observing mode to a mechanism-level uncertainty.

## Synthesis & Open Tensions

Galaxy evolution is regulated by baryon supply, the conversion of gas into stars, the return of energy and metals through feedback, and the environments that reshape reservoirs after infall. The clearest picture is causal rather than linear: halo growth creates the gravitational setting, gas accretion and recycling provide fuel, stellar and AGN feedback regulate how efficiently that fuel forms stars, and groups, clusters, and cosmic-web geometry alter the boundary conditions.

The open frontier is not whether any one mechanism matters. It is when each dominates, how strongly it couples to observable gas phases, and how those answers change with mass, redshift, and environment. Remaining tensions include the abundance of massive galaxies in early JWST samples, survival of cold streams in hot halos, scaling of feedback efficiency with simulation resolution, the relative importance of direct stripping versus starvation, and the source budget for reionization. Those topics should become additional sourced claims only when their evidence is mapped cleanly into the claim/evidence layer.

## Method1 evidence/trust coverage

- Bound chips: `3/30` (`2931`, `2929`, `2946`).
- Unbound local chips: `27/30` (`2905, 2906, 2907, 2908, 2909, 2910, 2911, 2912, 2913, 2914, 2915, 2916, 2917, 2918, 2919, 2920, 2921, 2922, 2923, 2925, 2926, 2930, 2932, 2933, 2934, 2935, 2936`).
- Bound local evidence rows: `43` (`20 + 14 + 9`).
- Citation markers injected into article body: `0`.

### Claim 2931: quenching depends on sample, redshift, and environment

- Trust shown here: `debated`; score `+0.34`; local evidence rows `20`; stance mix `none: 16, supports: 4`.
- Scope: this is local Method1 evidence/trust binding only; no product DB/API trust recompute or invented citation IDs.

| # | evidence_id | paper | year | stance | votes |
|---:|---:|---|---:|---|---|
| 1 | 28063 | The role of environment and AGN feedback in quenching local galaxies: Comparing cosmological hydrodynamical simulations to the SDSS | 2024 | none | 0/0 |
| 2 | 28068 | Surveying the Whirlpool at Arcseconds with NOEMA (SWAN). IV. Extent of active galactic nucleus feedback on the interstellar medium | 2026 | none | 0/0 |
| 3 | 28096 | arXiv:arXiv:1712.04452 |  | none | 0/0 |
| 4 | 28099 | arXiv:1308.5224 |  | none | 0/0 |
| 5 | 28100 | Environmental Quenching of High-Redshift Galaxies: Interpreting JWST Observations with Simulations | 2026 | none | 0/0 |
| 6 | 28106 | Environmental Quenching of High-Redshift Galaxies: Interpreting JWST Observations with Simulations | 2026 | none | 0/0 |
| 7 | 28113 | Small and Complex II: Characterizing the Disk and Stellar Envelope of Edge-on $z \sim 0$ Massive Compact Galaxies | 2026 | none | 0/0 |
| 8 | 28116 | arXiv:arXiv:1712.04452 |  | none | 0/0 |
| 9 | 28128 | Environmental Quenching of High-Redshift Galaxies: Interpreting JWST Observations with Simulations | 2026 | none | 0/0 |
| 10 | 28130 | arXiv:arXiv:0901.1880 |  | none | 0/0 |
| 11 | 28132 | arXiv:2605.31052 |  | none | 0/0 |
| 12 | 28137 | The role of environment and AGN feedback in quenching local galaxies: Comparing cosmological hydrodynamical simulations to the SDSS | 2024 | none | 0/0 |
| 13 | 28147 | The role of environment and AGN feedback in quenching local galaxies: Comparing cosmological hydrodynamical simulations to the SDSS | 2024 | none | 0/0 |
| 14 | 28154 | arXiv:1308.5224 |  | none | 0/0 |
| 15 | 28159 | arXiv:2501.00986 |  | none | 0/0 |
| 16 | 28161 | arXiv:1308.5224 |  | none | 0/0 |
| 17 | 29784 | Euclid Quick Data Release (Q1). Quenching precedes bulge formation in dense environments but follows it in the field | 2025 | supports | 0/0 |
| 18 | 29767 | A Statistical Study of HI Gas in AGN-Hosting and Satellite Galaxies from ALFALFA and FASHI | 2026 | supports | 0/0 |
| 19 | 29787 | Systematically Measuring Ultra-Diffuse Galaxies. IX. A Gyr in the Life of Nearby Low Surface Brightness Galaxies | 2026 | supports | 0/0 |
| 20 | 29790 | Contrasting evolutionary pathways of fast- and slow-rotating galaxies in the green valley | 2026 | supports | 0/0 |

### Claim 2929: AGN feedback has context-dependent sign and strength

- Trust shown here: `unverified`; score `-0.14`; local evidence rows `14`; stance mix `none: 14`.
- Scope: this is local Method1 evidence/trust binding only; no product DB/API trust recompute or invented citation IDs.

| # | evidence_id | paper | year | stance | votes |
|---:|---:|---|---:|---|---|
| 1 | 28060 | Surveying the Whirlpool at Arcseconds with NOEMA (SWAN). IV. Extent of active galactic nucleus feedback on the interstellar medium | 2026 | none | 0/1 |
| 2 | 28070 | arXiv:2512.05584 |  | none | 0/0 |
| 3 | 28076 | A large, long-lived, slowly-expanding superbubble across the Perseus Arm | 2025 | none | 0/0 |
| 4 | 28080 | A large, long-lived, slowly-expanding superbubble across the Perseus Arm | 2025 | none | 0/0 |
| 5 | 28082 | arXiv:1507.06366 |  | none | 0/0 |
| 6 | 28083 | A large, long-lived, slowly-expanding superbubble across the Perseus Arm | 2025 | none | 0/0 |
| 7 | 28084 | A large, long-lived, slowly-expanding superbubble across the Perseus Arm | 2025 | none | 0/0 |
| 8 | 28110 | arXiv:arXiv:0901.1880 |  | none | 0/0 |
| 9 | 28114 | arXiv:1203.2926 |  | none | 0/0 |
| 10 | 28118 | arXiv:1203.2926 |  | none | 0/0 |
| 11 | 28127 | arXiv:2403.17145 |  | none | 0/0 |
| 12 | 28133 | arXiv:2009.11175 |  | none | 0/0 |
| 13 | 28139 | arXiv:2403.17145 |  | none | 0/0 |
| 14 | 28143 | arXiv:2403.17145 |  | none | 0/0 |

### Claim 2946: maintenance heating remains model-bounded/reported

- Trust shown here: `reported`; score `+0.45`; local evidence rows `9`; stance mix `supports: 9`.
- Scope: this is local Method1 evidence/trust binding only; no product DB/API trust recompute or invented citation IDs.

| # | evidence_id | paper | year | stance | votes |
|---:|---:|---|---:|---|---|
| 1 | 30780 | On the quenching of star formation in observed and simulated central galaxies: evidence for the role of integrated AGN f | 2022 | supports | 0/0 |
| 2 | 30781 | Quenched fractions in the IllustrisTNG simulations: the roles of AGN feedback, environment, and pre-processing | 2021 | supports | 0/0 |
| 3 | 30782 | AGN-driven quenching of star formation: morphological and dynamical implications for early-type galaxies | 2013 | supports | 0/0 |
| 4 | 30783 | The HORIZON-AGN simulation: morphological diversity of galaxies promoted by AGN feedback | 2016 | supports | 0/0 |
| 5 | 30784 | Self-regulated growth of supermassive black holes by a dual jet-heating active galactic nucleus feedback mechanism: meth | 2012 | supports | 0/0 |
| 6 | 30785 | Chaotic cold accretion on to black holes | 2013 | supports | 0/0 |
| 7 | 28089 | arXiv:2508.06707 |  | supports | 0/0 |
| 8 | 28123 | arXiv:2403.17145 |  | supports | 0/0 |
| 9 | 28158 | arXiv:2403.17145 |  | supports | 0/0 |
## Coverage limitations

The unbound-local chips are preserved as article provenance chips, but this static Method1 candidate does not display trust for them. Binding those rows would require the product claim/evidence layer or a later local evidence export. This candidate therefore favors explicit absence over false precision.

## Deepened local evidence boxes

### Claim 2931: joint internal/environment quenching depends on sample, redshift, and measurement

- Local trust: `debated`; score `+0.34`; rows `20`; distinct normalized arXiv IDs `13`; stance mix `none: 16, supports: 4`.
- Caution: Caution: this is debated rather than settled. Four rows are supporting, but the majority are none-stance/context rows, so the prose should keep sample selection, redshift, and measurement dependence visible.
- Row count is not distinct-paper count; repeated papers remain repeated rows because the local ledger contains separate evidence rows.

| # | evidence_id | paper | year | stance | votes |
|---:|---:|---|---:|---|---|
| 1 | 28063 | The role of environment and AGN feedback in quenching local galaxies: Comparing cosmological hydrodynamical simulations to the SDSS | 2024 | none | 0/0 |
| 2 | 28068 | Surveying the Whirlpool at Arcseconds with NOEMA (SWAN). IV. Extent of active galactic nucleus feedback on the interstellar medium | 2026 | none | 0/0 |
| 3 | 28096 | arXiv:arXiv:1712.04452 |  | none | 0/0 |
| 4 | 28099 | arXiv:1308.5224 |  | none | 0/0 |
| 5 | 28100 | Environmental Quenching of High-Redshift Galaxies: Interpreting JWST Observations with Simulations | 2026 | none | 0/0 |
| 6 | 28106 | Environmental Quenching of High-Redshift Galaxies: Interpreting JWST Observations with Simulations | 2026 | none | 0/0 |
| 7 | 28113 | Small and Complex II: Characterizing the Disk and Stellar Envelope of Edge-on $z \sim 0$ Massive Compact Galaxies | 2026 | none | 0/0 |
| 8 | 28116 | arXiv:arXiv:1712.04452 |  | none | 0/0 |
| 9 | 28128 | Environmental Quenching of High-Redshift Galaxies: Interpreting JWST Observations with Simulations | 2026 | none | 0/0 |
| 10 | 28130 | arXiv:arXiv:0901.1880 |  | none | 0/0 |
| 11 | 28132 | arXiv:2605.31052 |  | none | 0/0 |
| 12 | 28137 | The role of environment and AGN feedback in quenching local galaxies: Comparing cosmological hydrodynamical simulations to the SDSS | 2024 | none | 0/0 |
| 13 | 28147 | The role of environment and AGN feedback in quenching local galaxies: Comparing cosmological hydrodynamical simulations to the SDSS | 2024 | none | 0/0 |
| 14 | 28154 | arXiv:1308.5224 |  | none | 0/0 |
| 15 | 28159 | arXiv:2501.00986 |  | none | 0/0 |
| 16 | 28161 | arXiv:1308.5224 |  | none | 0/0 |
| 17 | 29784 | Euclid Quick Data Release (Q1). Quenching precedes bulge formation in dense environments but follows it in the field | 2025 | supports | 0/0 |
| 18 | 29767 | A Statistical Study of HI Gas in AGN-Hosting and Satellite Galaxies from ALFALFA and FASHI | 2026 | supports | 0/0 |
| 19 | 29787 | Systematically Measuring Ultra-Diffuse Galaxies. IX. A Gyr in the Life of Nearby Low Surface Brightness Galaxies | 2026 | supports | 0/0 |
| 20 | 29790 | Contrasting evolutionary pathways of fast- and slow-rotating galaxies in the green valley | 2026 | supports | 0/0 |

### Claim 2929: AGN feedback can regulate or quench, but row evidence is non-committal in this local ledger

- Local trust: `unverified`; score `-0.14`; rows `14`; distinct normalized arXiv IDs `8`; stance mix `none: 14`.
- Caution: Caution: all 14 local rows are stance `none` (0 supporting and 0 refuting rows in this binding), with one displayed vote-disagree row and several archive/context rows. Read this box as provenance context for why the claim remains unverified, not as direct support for the prose sentence.
- Row count is not distinct-paper count; repeated papers remain repeated rows because the local ledger contains separate evidence rows.

| # | evidence_id | paper | year | stance | votes |
|---:|---:|---|---:|---|---|
| 1 | 28060 | Surveying the Whirlpool at Arcseconds with NOEMA (SWAN). IV. Extent of active galactic nucleus feedback on the interstellar medium | 2026 | none | 0/1 |
| 2 | 28070 | arXiv:2512.05584 |  | none | 0/0 |
| 3 | 28076 | A large, long-lived, slowly-expanding superbubble across the Perseus Arm | 2025 | none | 0/0 |
| 4 | 28080 | A large, long-lived, slowly-expanding superbubble across the Perseus Arm | 2025 | none | 0/0 |
| 5 | 28082 | arXiv:1507.06366 |  | none | 0/0 |
| 6 | 28083 | A large, long-lived, slowly-expanding superbubble across the Perseus Arm | 2025 | none | 0/0 |
| 7 | 28084 | A large, long-lived, slowly-expanding superbubble across the Perseus Arm | 2025 | none | 0/0 |
| 8 | 28110 | arXiv:arXiv:0901.1880 |  | none | 0/0 |
| 9 | 28114 | arXiv:1203.2926 |  | none | 0/0 |
| 10 | 28118 | arXiv:1203.2926 |  | none | 0/0 |
| 11 | 28127 | arXiv:2403.17145 |  | none | 0/0 |
| 12 | 28133 | arXiv:2009.11175 |  | none | 0/0 |
| 13 | 28139 | arXiv:2403.17145 |  | none | 0/0 |
| 14 | 28143 | arXiv:2403.17145 |  | none | 0/0 |

### Claim 2946: maintenance heating is reported/model-bounded rather than a measured-prevalence result

- Local trust: `reported`; score `+0.45`; rows `9`; distinct normalized arXiv IDs `8`; stance mix `supports: 9`.
- Caution: Caution: this is reported/model-bounded support. The nine local rows support a maintenance-heating framing, but the claim should not be upgraded to consensus or broad measured prevalence.
- Row count is not distinct-paper count; repeated papers remain repeated rows because the local ledger contains separate evidence rows.

| # | evidence_id | paper | year | stance | votes |
|---:|---:|---|---:|---|---|
| 1 | 30780 | On the quenching of star formation in observed and simulated central galaxies: evidence for the role of integrated AGN f | 2022 | supports | 0/0 |
| 2 | 30781 | Quenched fractions in the IllustrisTNG simulations: the roles of AGN feedback, environment, and pre-processing | 2021 | supports | 0/0 |
| 3 | 30782 | AGN-driven quenching of star formation: morphological and dynamical implications for early-type galaxies | 2013 | supports | 0/0 |
| 4 | 30783 | The HORIZON-AGN simulation: morphological diversity of galaxies promoted by AGN feedback | 2016 | supports | 0/0 |
| 5 | 30784 | Self-regulated growth of supermassive black holes by a dual jet-heating active galactic nucleus feedback mechanism: meth | 2012 | supports | 0/0 |
| 6 | 30785 | Chaotic cold accretion on to black holes | 2013 | supports | 0/0 |
| 7 | 28089 | arXiv:2508.06707 |  | supports | 0/0 |
| 8 | 28123 | arXiv:2403.17145 |  | supports | 0/0 |
| 9 | 28158 | arXiv:2403.17145 |  | supports | 0/0 |

## Non-final limitations

This is a deterministic progress candidate, not a final no-apply packet. No live wiki, product API, DB, SQL, page_versions, deploy, restart, git, browser, cloud/OAuth/secrets, or cron action is authorized or performed.
