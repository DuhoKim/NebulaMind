# Literature/source grounding tick — Wave-2 high-risk papers

Marker: `LITERATURE_SOURCE_WAVE2_20260708T164632Z`

UTC: 2026-07-08T16:46:32Z  
Local: 2026-07-09 01:46:32 KST

## Scope and inputs read

Lane role: public source grounding for the overnight 9-paper Galaxy Evolution AAS pilot swarm. This is a source packet only: no prose edit, no bibliography insertion, no manuscript overwrite, and no public mirroring.

Read before synthesis:
- `OVERNIGHT_BRIEF.md`, `SWARM_BOARD.md`, `OVERNIGHT_LEDGER.md`
- Current AASTeX sources for M2 P2, M3 P2, and M3 P3 under `runs/SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z/`
- Lana selection-disclosure revision report `lanes/lana/ticks/TICK_20260708T161724Z.md`
- Hwao director priority report `lanes/hwao/HWAO_DIRECTOR_TICK_20260708T160831Z.md`
- Current public research-topic page and pre-proposal backup page for active-vs-historical context

Priority followed from Hwao/Lana blockers: **M2 P2**, **M3 P2**, and **M3 P3**.

## Acquisition note

- No credentials were used.
- arXiv export API metadata was fetched and raw XML was preserved by paper under `raw_payloads/`.
- A public unauthenticated Semantic Scholar check was attempted once and returned HTTP 429, so no Semantic Scholar metadata was used.
- This packet classifies sources as actual-result support versus scoped interpretation/future-data motivation; it does not authorize citation insertion or public publishing.

## High-level verdict

The Wave-2 bibliography gap is now bounded by three safe integration rules:

1. **M2 P2** can cite radio-AGN/environment sources only as a bridge from the optical BPT massive-host denominator to the missing radio/X-ray/hot-gas follow-up. They do not turn the SDSS density association into a jet-coupling-efficiency measurement.
2. **M3 P2** should cite COLD GASS/xCOLD GASS/xGASS as the reason CO/HI gas data are required. These sources explicitly guard against treating H-alpha or four-line optical selection as molecular gas mass, gas fraction, depletion time, or SFE.
3. **M3 P3** should cite TNG/EAGLE/SIMBA/iMaNGA-style work as future model/mock infrastructure. They do not validate, reject, rank, or falsify any feedback model until a mock catalogue is forward-modelled through the pilot selection function.

## Paper-specific source packet

### M2 P2 — environment proxy for optical AGN in massive hosts

Current pilot boundary: Massive-host optical BPT AGN fraction is higher in the high-density quartile than the low-density quartile in the cached SDSS four-line sample; no radio jet power, cavity energetics, hot-gas density, or coupling efficiency is measured.

| Priority | Source | Exact URL read | Year / authors | Why relevant | Supports actual result, or only future data? |
|---:|---|---|---|---|---|
| 1 | AGN-driven outflows and the AGN feedback efficiency in young radio galaxies | https://arxiv.org/abs/2009.11175v1 | 2020 — F. Santoro, C. Tadhunter, D. Baron, R. Morganti, J. Holt | Direct topical anchor for young radio galaxies, observed AGN-driven outflows, and feedback-efficiency language; useful because the paper title itself ties radio-galaxy outflows to efficiency estimates. | Motivates future radio/kinematic coupling data only; it does not support interpreting the SDSS optical-density pilot as a jet-coupling measurement. |
| 2 | The host galaxies of radio-loud AGN: mass dependencies, gas cooling and AGN feedback | https://arxiv.org/abs/astro-ph/0506269v1 | 2005 — P. N. Best, G. Kauffmann, T. M. Heckman, J. Brinchmann, S. Charlot, Z. Ivezic, et al. (7 authors) | SDSS-era radio-loud AGN demographic bridge linking host mass, cooling, and AGN-feedback framing; relevant to why the M2 P2 pilot isolates massive hosts before radio follow-up. | Scoped interpretation/target-stratification support only. It supports the massive-host/radio-AGN follow-up rationale, not actual radio power in the current optical sample. |
| 3 | Galaxy groups as the ultimate probe of AGN feedback | https://arxiv.org/abs/2403.17145v1 | 2024 — Dominique Eckert, Fabio Gastaldello, Ewan O'Sullivan, Alexis Finoguenov, Marisa Brienza, the X-GAP collaboration | Recent group-scale AGN-feedback review/status source; matches the proposal need for environment, hot gas, and group-regime measurements. | Future-data/status motivation only; no group catalogue, X-ray gas, or radio jet coupling was measured in this pilot. |

Integration guard for M2 P2: keep the measured result as an optical BPT AGN-versus-density association in massive hosts. Use these sources to motivate the missing radio jet power, hot-gas, group-environment, and coupling-efficiency measurements.

### M3 P2 — optical denominator for gas-fraction versus efficiency tests

Current pilot boundary: The pilot identifies an emission-line-detected massive low-sSFR optical denominator and H-alpha proxy baseline; it has no CO/dust gas masses, molecular gas fractions, depletion times, or star-formation efficiencies.

| Priority | Source | Exact URL read | Year / authors | Why relevant | Supports actual result, or only future data? |
|---:|---|---|---|---|---|
| 1 | COLD GASS, an IRAM legacy survey of molecular gas in massive galaxies: I. Relations between H2, HI, stellar content and structural properties | https://arxiv.org/abs/1103.1642v1 | 2011 — Amelie Saintonge, Guinevere Kauffmann, Carsten Kramer, Linda J. Tacconi, Christof Buchbender, Barbara Catinella, et al. (24 authors) | COLD GASS molecular-gas survey anchor for massive nearby galaxies; establishes that H2/HI/stellar structural measurements are the relevant data for gas-fraction tests. | Motivates future CO/H2 data and gas-fraction interpretation; it does not support treating SDSS H-alpha proxy as a molecular-gas measurement. |
| 2 | COLD GASS, an IRAM Legacy Survey of Molecular Gas in Massive Galaxies: II. The non-universality of the Molecular Gas Depletion Timescale | https://arxiv.org/abs/1104.0019v1 | 2011 — Amelie Saintonge, Guinevere Kauffmann, Jing Wang, Carsten Kramer, Linda J. Tacconi, Christof Buchbender, et al. (24 authors) | COLD GASS depletion-timescale paper; directly relevant to the depletion-time versus SFE distinction the proposal wants to test. | Future-data motivation and wording guard: depletion time is a molecular-gas/SFR quantity, not derivable from the current SDSS four-line denominator alone. |
| 3 | xCOLD GASS: the complete IRAM-30m legacy survey of molecular gas for galaxy evolution studies | https://arxiv.org/abs/1710.02157v1 | 2017 — Amélie Saintonge, Barbara Catinella, Linda J. Tacconi, Guinevere Kauffmann, Reinhard Genzel, Luca Cortese, et al. (21 authors) | xCOLD GASS complete IRAM-30m legacy-survey release; broad modern survey anchor for molecular gas in galaxy-evolution studies. | Motivates the needed CO follow-up denominator; not actual support for any gas-depletion result in the pilot. |
| 4 | xGASS: Total cold gas scaling relations and molecular-to-atomic gas ratios of galaxies in the local Universe | https://arxiv.org/abs/1802.02373v1 | 2018 — Barbara Catinella, Amélie Saintonge, Steven Janowiecki, Luca Cortese, Romeel Davé, Jenna J. Lemonias, et al. (13 authors) | xGASS cold-gas scaling-relation source linking atomic and molecular gas ratios in local galaxies; relevant to distinguishing gas availability from efficiency. | Future-data/status motivation for HI+H2 gas inventory; not actual SDSS result support. |

Integration guard for M3 P2: call the current object set an emission-line-detected optical follow-up denominator. Use gas-survey citations only when saying the full test requires CO/HI/dust gas masses and aperture-matched SFRs.

### M3 P3 — SDSS target vector for feedback-model validation

Current pilot boundary: The pilot writes an observed SDSS target vector across mass/redshift cells; no simulation catalogue has been forward-modelled through the SDSS/MaNGA/ALMA/X-ray/radio selection functions.

| Priority | Source | Exact URL read | Year / authors | Why relevant | Supports actual result, or only future data? |
|---:|---|---|---|---|---|
| 1 | The IllustrisTNG Simulations: Public Data Release | https://arxiv.org/abs/1812.05609v3 | 2018 — Dylan Nelson, Volker Springel, Annalisa Pillepich, Vicente Rodriguez-Gomez, Paul Torrey, Shy Genel, et al. (14 authors) | Public-data-release anchor for IllustrisTNG, one plausible simulation suite for future target-vector comparison. | Future model-comparison infrastructure only; the current pilot has not queried TNG or built SDSS-like mocks. |
| 2 | The EAGLE project: Simulating the evolution and assembly of galaxies and their environments | https://arxiv.org/abs/1407.7040v2 | 2014 — Joop Schaye, Robert A. Crain, Richard G. Bower, Michelle Furlong, Matthieu Schaller, Tom Theuns, et al. (22 authors) | EAGLE simulation-suite source with galaxy-formation/feedback model context; broad model family for comparison. | Future-data/status motivation only; no EAGLE mock was passed through the pilot selection function. |
| 3 | Simba: Cosmological Simulations with Black Hole Growth and Feedback | https://arxiv.org/abs/1901.10203v2 | 2019 — Romeel Davé, Daniel Anglés-Alcázar, Desika Narayanan, Qi Li, Mika H. Rafieferantsoa, Sarah Appleby | SIMBA simulation source with black-hole growth and feedback prescriptions; relevant because M3 P3 targets feedback-model validation. | Future model-comparison motivation only; not evidence that the SDSS vector validates or falsifies SIMBA. |
| 4 | iMaNGA: mock MaNGA galaxies based on IllustrisTNG and MaStar SSPs. I. Construction and analysis of the mock data cubes | https://arxiv.org/abs/2203.11575v3 | 2022 — Lorenza Nanni, Daniel Thomas, James Trayford, Claudia Maraston, Justus Neumann, David R. Law, et al. (11 authors) | Mock MaNGA galaxies based on IllustrisTNG and MaStar SSPs; directly illustrates the kind of survey-forward mock needed before comparing an observed SDSS/MaNGA-like vector to simulations. | Strong future-method support for forward-modelling/selection-function language; not actual result support. |
| 5 | Quenched fractions in the IllustrisTNG simulations: comparison with observations and other theoretical models | https://arxiv.org/abs/2008.00004v2 | 2020 — Martina Donnari, Annalisa Pillepich, Dylan Nelson, Federico Marinacci, Mark Vogelsberger, Lars Hernquist | IllustrisTNG quenched-fraction comparison with observations; close topical match to an observed quenched-fraction target vector. | Scoped interpretation/status source for what a real comparison would look like; the current pilot is not itself such a comparison. |

Integration guard for M3 P3: call the table an observed target vector. Use simulation citations only for future mock construction/comparison; do not say the pilot validates or falsifies any model.

## Bibliography-gap actions for a later integration pass

1. For M2 P2, add Santoro et al. 2020, Best et al. 2005, and Eckert et al. 2024 only in the discussion/future-observables context; if Best et al. is used near the result, say it supports target stratification rather than an actual radio measurement.
2. For M3 P2, add COLD GASS/xCOLD GASS/xGASS citations around the explicit statement that the SDSS pilot lacks molecular/atomic gas masses and cannot distinguish depletion from SFE.
3. For M3 P3, add TNG/EAGLE/SIMBA/iMaNGA citations around the future mock-selection paragraph; do not cite them as if a simulation comparison has been run.
4. Preserve the DR17/BPT method backbone from the prior packet for actual data provenance; the Wave-2 sources here are mostly topic/future-data anchors.

## Artifact manifest

- JSONL source ledger: `literature_sources_wave2_20260708T164632Z.jsonl`
- Summary JSON: `literature_summary_wave2_20260708T164632Z.json`
- Raw arXiv XML for m2_p2_radio_jet_environment: `raw_payloads/20260708T164632Z/m2_p2_radio_jet_environment_arxiv_id_list.xml`
- Raw arXiv XML for m3_p2_gas_depletion_efficiency: `raw_payloads/20260708T164632Z/m3_p2_gas_depletion_efficiency_arxiv_id_list.xml`
- Raw arXiv XML for m3_p3_simulation_validation: `raw_payloads/20260708T164632Z/m3_p3_simulation_validation_arxiv_id_list.xml`
- Semantic Scholar status check: `raw_payloads/20260708T164632Z/semantic_scholar_status_check.json`

## Safety ledger

- Files written under literature lane only: packet Markdown, JSONL source ledger, summary JSON, raw arXiv/Semantic-Scholar-status payloads, helper script, and lane-local tick note.
- Required shared ledger append: one concise line to `OVERNIGHT_LEDGER.md`.
- No public pages, live roots, product DB, API/pages, page_versions, trust, deploy/restart, git, billing, OAuth, external submission, or new cron jobs touched.
- No active execution phrase.
