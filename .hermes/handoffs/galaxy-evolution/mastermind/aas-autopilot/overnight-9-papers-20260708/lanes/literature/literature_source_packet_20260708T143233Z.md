# Literature/source grounding tick — Wave-1 papers

Marker: `LITERATURE_SOURCE_TICK_20260708T143233Z`

UTC: 2026-07-08T14:32:33Z  
Local: 2026-07-08 23:32:33 KST

## Scope and inputs read

Lane role: public-source grounding for the overnight 9-paper Galaxy Evolution AAS pilot swarm. This is a source packet only: no prose edit, no bibliography insertion, no manuscript overwrite, no public mirroring.

Read before synthesis:
- `OVERNIGHT_BRIEF.md`, `SWARM_BOARD.md`, `OVERNIGHT_LEDGER.md`
- Hwao director tick `lanes/hwao/HWAO_DIRECTOR_TICK_20260708T140119Z.md`
- Goru data tick `lanes/goru/ticks/GORU_TICK_20260708T141459Z.md`
- Lana Wave-1 revision drafts for `m1_rp2_environment_quenching`, `m1_rp3_maintenance_heating`, and `m2_p1_outflow_escape_recycling`
- Current Wave-1 AASTeX sources under `runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/`
- Current public research-topic pages and active Galaxy Evolution page/backups for context

Priority followed from Hwao: **M1 RP-2**, **M1 RP-3**, **M2 P1**.

## Acquisition note

- No credentials were used.
- Primary usable metadata came from the public arXiv API and Crossref API.
- Semantic Scholar was attempted but returned HTTP 429 for unauthenticated searches during this tick, so I did not rely on it.
- Web extraction/search tooling was not configured; no billing/API-key setup was attempted.

## High-level verdict

The three Wave-1 manuscripts need two different kinds of citations:

1. **Method/provenance anchors** that support the actual SDSS optical-line pilot measurements: SDSS DR17, SDSS technical summary, BPT diagnostics, Kewley/Kauffmann demarcations, and SDSS star-formation/AGN host catalog context.
2. **Physical-context anchors** that motivate the full future programs while staying out of the actual-result claim: environment/central-satellite/halo follow-up for M1 RP-2; X-ray/radio cavity and cooling measurements for M1 RP-3; multiphase outflow/escape/recycling follow-up for M2 P1.

No source found in this tick turns the Wave-1 SDSS optical proxies into causal proof of environmental quenching, maintenance heating, or gas escape/recycling. The safest integration use is to cite physical-context papers as **motivation/follow-up requirements**, not as support for the pilot result itself.

## Shared method/provenance anchors for all three papers

| Source | Exact URL | Why relevant | Supports actual result, or only future data? |
|---|---|---|---|
| Abdurro'uf et al. 2021, **The Seventeenth Data Release of the Sloan Digital Sky Surveys: Complete Release of MaNGA, MaStar and APOGEE-2 Data** | https://arxiv.org/abs/2112.02026 | Direct DR17 release citation; stronger than only citing the original SDSS technical summary for a DR17 pilot. | **Supports actual data provenance/method.** |
| York et al. 2000, **The Sloan Digital Sky Survey: Technical Summary** | https://arxiv.org/abs/astro-ph/0006396 | Historical SDSS survey/instrument/data-system anchor already cited in the manuscripts. | **Supports actual survey provenance/method.** |
| Baldwin, Phillips & Terlevich 1981, **Classification parameters for the emission-line spectra of extragalactic objects** | https://doi.org/10.1086/130766 | Original BPT line-ratio diagnostic frame used by the optical classification workflow. | **Supports actual BPT method**, not physical feedback interpretation. |
| Kewley et al. 2001, **Theoretical Modeling of Starburst Galaxies** | https://arxiv.org/abs/astro-ph/0106324 | Theoretical maximum-starburst demarcation used in BPT separation. | **Supports actual BPT demarcation method.** |
| Kauffmann et al. 2003, **The Host Galaxies of AGN** | https://arxiv.org/abs/astro-ph/0304239 | SDSS narrow-line AGN host context and empirical optical AGN demarcation. | **Supports actual optical-AGN interpretation/method.** |
| Kewley et al. 2006, **The Host Galaxies and Classification of Active Galactic Nuclei** | https://arxiv.org/abs/astro-ph/0605681 | Useful classification caveat for Seyfert/LINER/composite branches; helps guard high-excitation wording. | **Supports actual classification guardrails.** |
| Brinchmann et al. 2003/2004, **The physical properties of star forming galaxies in the low redshift universe** | https://arxiv.org/abs/astro-ph/0311060 | MPA/JHU-style SDSS SFR/sSFR measurement context; useful for catalog sSFR caveats. | **Supports actual catalog-property methodology.** |

## Paper-specific source packet

### M1 RP-2 — SDSS density proxy for environmental quenching

Current pilot result from Lana/Goru: high-density quartile quenched fraction 0.230 versus low-density quartile 0.181; bootstrap high-minus-low interval [0.041, 0.059]; mass-redshift adjusted LPM coefficient 0.032 ± 0.004. This is an SDSS nearest-neighbour proxy, not a halo/central-satellite result.

| Priority | Source | Exact URL | Why relevant | Supports actual result, or only future data? |
|---:|---|---|---|---|
| 1 | Peng et al. 2010, **Mass and environment as drivers of galaxy evolution in SDSS and zCOSMOS and the origin of the Schechter function** | https://arxiv.org/abs/1003.4747 | Frames mass-quenching and environment-quenching as separable population terms in SDSS/zCOSMOS; directly helps interpret why a mass-redshift adjusted density-proxy diagnostic is meaningful. | **Supports actual result interpretation**, with guard that this pilot is simpler and not a full separability analysis. |
| 2 | Baldry et al. 2006, **Galaxy bimodality versus stellar mass and environment** | https://arxiv.org/abs/astro-ph/0607648 | Shows color bimodality variation with stellar mass and projected neighbour density in SDSS-like local data; close conceptual match to a density-proxy/quenched-fraction diagnostic. | **Supports actual result interpretation**, especially density-proxy caveats. |
| 3 | Wetzel et al. 2012/2013, **Galaxy evolution in groups and clusters: satellite star formation histories and quenching timescales in a hierarchical Universe** | https://arxiv.org/abs/1206.3571 | Uses SDSS group/cluster catalogs and simulations to connect satellites, infall, preprocessing, and quenching timescales. | **Motivates future data**: group catalogues, central/satellite labels, infall/preprocessing; not measured in the pilot. |
| 4 | Goubert et al. 2024, **The role of environment and AGN feedback in quenching local galaxies: Comparing cosmological hydrodynamical simulations to the SDSS** | https://arxiv.org/abs/2401.12953 | Recent SDSS-plus-simulation framing that explicitly separates intrinsic and environmental predictors. | **Motivates future model/comparison layer**; does not validate the current nearest-neighbour proxy as causal. |

Integration guard for M1 RP-2: cite Peng/Baldry when saying the density-proxy association sits in a known mass/environment literature; cite Wetzel/Goubert only when saying the full test needs group/halo/central-satellite and model-comparison information.

### M1 RP-3 — optical-AGN denominator for maintenance-heating follow-up

Current pilot result from Lana/Goru: massive subset has 3,997/9,298 BPT AGN (0.430); massive low-sSFR subset has 3,459/5,695 BPT AGN (0.607). This is an optical denominator, not a heating/cooling or duty-cycle measurement.

| Priority | Source | Exact URL | Why relevant | Supports actual result, or only future data? |
|---:|---|---|---|---|
| 1 | Best et al. 2005, **The host galaxies of radio-loud AGN: mass dependencies, gas cooling and AGN feedback** | https://arxiv.org/abs/astro-ph/0506269 | SDSS-based radio-loud AGN host demographics; useful bridge from massive hosts to radio-mode follow-up. | **Mixed**: supports target-stratification logic, but not the optical BPT fraction as a radio/jet-power measurement. |
| 2 | McNamara & Nulsen 2007, **Heating Hot Atmospheres with Active Galactic Nuclei** | https://arxiv.org/abs/0709.2152 | Review anchor for X-ray cavities, shocks, and hot-atmosphere energy injection. | **Motivates future X-ray/cavity data only.** |
| 3 | McNamara & Nulsen 2012, **Mechanical Feedback from Active Galactic Nuclei in Galaxies, Groups, and Clusters** | https://arxiv.org/abs/1204.0006 | Mechanical feedback review; precise language for cavity power versus cooling-luminosity tests. | **Motivates future heating/cooling and duty-cycle data only.** |
| 4 | Heckman & Best 2014, **The Co-Evolution of Galaxies and Supermassive Black Holes: Insights from Surveys of the Contemporary Universe** | https://arxiv.org/abs/1403.4620 | Review/status anchor for radiative-mode versus radio-mode AGN populations and survey interpretation. | **Status/motivation**, not direct support for heating in this pilot. |
| 5 | Eckert et al. 2024, **Galaxy groups as the ultimate probe of AGN feedback** | https://arxiv.org/abs/2403.17145 | Group-scale hot-atmosphere feedback frame; aligns with the proposed X-ray/radio group follow-up. | **Motivates future group/hot-gas data only.** |

Integration guard for M1 RP-3: cite method anchors for the BPT optical fraction; cite maintenance-heating papers only in the Scope/Discussion as defining the **missing** measurements: jet power, cavity enthalpy, cooling luminosity, halo selection, nondetections, and duty-cycle time averaging.

### M2 P1 — high-excitation optical AGN denominator for outflow escape/recycling tests

Current pilot result from Lana/Goru: 4,440/60,000 high-excitation optical AGN candidates (0.074); median log sSFR -11.53 versus -10.14 for the full denominator. The exact high-excitation criterion still needs to be pulled from the analysis code before final methods text.

| Priority | Source | Exact URL | Why relevant | Supports actual result, or only future data? |
|---:|---|---|---|---|
| 1 | Kewley et al. 2006, **The Host Galaxies and Classification of Active Galactic Nuclei** | https://arxiv.org/abs/astro-ph/0605681 | Best immediate anchor for any high-excitation/Seyfert/LINER/composite classification caveat in the SDSS line-ratio context. | **Supports actual classification guardrails**, pending exact candidate criterion from code. |
| 2 | Cicone et al. 2013/2014, **Massive Molecular Outflows and Evidence for AGN Feedback from CO Observations** | https://arxiv.org/abs/1311.2595 | CO molecular-outflow sample; motivates why molecular velocities and outflow rates are needed beyond SDSS optical selection. | **Motivates future multiphase outflow data only.** |
| 3 | Fiore et al. 2017, **AGN wind scaling relations and the co-evolution of black holes and galaxies** | https://arxiv.org/abs/1702.04507 | Scaling relations and duty-cycle caveats for AGN winds; helps prevent overreading one optical denominator. | **Motivates future wind/energy-coupling data only.** |
| 4 | Carniani et al. 2017, **AGN feedback on molecular gas reservoirs in quasars at z~2.4** | https://arxiv.org/abs/1706.08987 | Shows disturbed molecular reservoirs in high-z quasars, while remaining a small targeted sample; good guard that detections do not define escape fractions. | **Motivates future reservoir/kinematic data only.** |
| 5 | Veilleux, Cecil & Bland-Hawthorn 2005, **Galactic Winds** | https://arxiv.org/abs/astro-ph/0504435 | Broad review of wind physics, recycling of energy/metals, and multiwavelength diagnostics. | **Status/motivation**, not actual SDSS result support. |
| 6 | Fabian 2012, **Observational Evidence of AGN Feedback** | https://arxiv.org/abs/1204.4114 | Review/status source for jets, winds, gas ejection/heating, and feedback claims. | **Status/motivation only**; cite as field frame, not proof of escape/recycling in this pilot. |

Integration guard for M2 P1: method citations can support the optical candidate denominator; outflow papers should be tied to the required follow-up observables: IFU outflow velocities, halo escape speeds, CO/neutral/ionized phase coverage, CGM tracers, and nondetections.

## Bibliography-gap actions for a later integration pass

1. Add a DR17 citation to all three Wave-1 papers: Abdurro'uf et al. 2021 (arXiv:2112.02026; DOI 10.3847/1538-4365/ac4414).
2. Add Brinchmann et al. for SDSS catalog SFR/sSFR context if the manuscripts keep using catalog sSFR as a central variable.
3. For M1 RP-2, add Peng 2010 and Baldry 2006 as actual interpretation anchors, then Wetzel 2012/2013 as a future-data caveat.
4. For M1 RP-3, add Best 2005 as the SDSS-to-radio demographic bridge, then McNamara & Nulsen 2007/2012 as future measurement anchors.
5. For M2 P1, do not insert Cicone/Fiore/Carniani/Fabian as if they support the measured SDSS result; insert them only in a discussion paragraph explaining why resolved multiphase data are necessary.
6. Before any final M2 P1 methods text, inspect the analysis code for the exact high-excitation criterion; the JSON summary is not enough.

## Safety ledger

- Files written: this packet, a JSONL source ledger, a summary JSON, and a lane-local tick note under `lanes/literature/`.
- Ledger append: one concise line to `OVERNIGHT_LEDGER.md`.
- No public pages, live roots, product DB, API/pages, page_versions, trust, deploy/restart, git, billing, OAuth, external submission, or new cron jobs touched.
- No active execution phrase.

Source JSONL: `literature_sources_20260708T143233Z.jsonl`  
Summary JSON: `literature_summary_20260708T143233Z.json`
