import json
from pathlib import Path

AREA = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715")
REGISTRY = AREA / "area_review_03_somerville_dave_2015_CURATED_SOURCE_REGISTRY.json"
OUT = AREA / "area_review_03_somerville_dave_2015_DR_PACKET.md"
registry = json.loads(REGISTRY.read_text())

body = """# Review Base 03 canonical advisory packet — Somerville & Davé 2015

status: READY_FOR_HWAO_REVIEW
advisory_only: true
wiki_write_performed_by_tori: false
canonical_source_base_not_live_wiki_prose: true
raw_packet_sha256: 508f5f53543c3d4e25430e04fd87088a6ffe81dfbba79517c02c49c625bc4661
source_registry_status: PASS
usable_sources: 50
primary_sources: 46
supporting_reviews: 4
scope_quarantined_sources: 8

## 1. Review identity and scope map

[REV03] Somerville, Rachel S. & Davé, Romeel (2015, Annual Review of Astronomy and Astrophysics) | title=Physical Models of Galaxy Formation in a Cosmological Framework | DOI:10.1146/annurev-astro-082812-140951; arXiv:1412.2712; ADS:2015ARA&A..53...51S | role=review_synthesis | trust_score=0.98 | boundary=2015 synthesis of semi-analytic and cosmological hydrodynamic galaxy-formation models; retain calibration, numerical, mass, redshift, resolution, cosmology, and subgrid boundaries.

- Cosmological backbone: supports hierarchical halo assembly and baryonic accretion as shared model structure; it does not make baryonic prescriptions first-principles.
- Semi-analytic models: support rapid controlled experiments on merger trees; their differential prescriptions and parameters remain phenomenological.
- Hydrodynamic simulations: directly evolve resolved gravity and gas dynamics; unresolved ISM, stellar feedback, and black-hole coupling remain subgrid.
- Model-observation comparison: supports benchmark and tension mapping; matching a tuned target does not identify the true physical mechanism.
- Baryon cycle: supports linked inflow, star formation, outflow, recycling, and enrichment; individual rates and pathways remained uncertain.
- Structure and morphology: supports bounded roles for angular momentum, mergers, instabilities, and environment; no single channel explains every galaxy.
- Black-hole feedback is retained only as a bounded galaxy-scale model ingredient. Accretion microphysics and AGN-centered sources are quarantined.
- Post-2015 simulations, JWST results, and machine-learning inference are outside this packet.

## 2. Established findings

[REV03-E01]
- role: established
- epistemic_type: review_synthesis
- atomic finding: Both semi-analytic models and cosmological hydrodynamic simulations begin from hierarchical dark-matter assembly and add baryonic cooling, star formation, feedback, enrichment, and structural evolution.
- scope/boundary: Shared architecture does not imply identical numerical solutions or uniquely determined baryonic physics.
- review basis: Sections 1.2-1.4 and 2.
- confidence note: High as a framework statement.
- source keys: [REV03], [REV03-P001], [REV03-P002], [REV03-P039]
- trust_score: 0.96

[REV03-E02]
- role: established
- epistemic_type: empirical_inference
- atomic finding: The shallow low-mass galaxy abundance relative to the halo mass function requires strongly mass-dependent suppression of baryon conversion in shallow potential wells.
- scope/boundary: Necessity is robust; the detailed mass loading, energy coupling, and recycling mechanism are not uniquely inferred.
- review basis: Section 4.1; stellar-mass-function comparisons.
- confidence note: High for suppression, moderate for mechanism.
- source keys: [REV03], [REV03-P004], [REV03-P009], [REV03-P010], [REV03-P042]
- trust_score: 0.94

[REV03-E03]
- role: established
- epistemic_type: review_synthesis
- atomic finding: Gas accretion separates usefully into rapidly cooling filamentary/cold pathways and shock-heated hot-halo pathways, with the balance depending on halo mass, redshift, metallicity, and environment.
- scope/boundary: The modes overlap; a fixed universal mass threshold is an approximation.
- review basis: Section 1.3; gas accretion and cooling.
- confidence note: High for the two limiting regimes, moderate for exact partition.
- source keys: [REV03], [REV03-P005], [REV03-P026]
- trust_score: 0.93

[REV03-E04]
- role: established
- epistemic_type: review_synthesis
- atomic finding: Cosmological volumes cannot resolve the full multiphase ISM and individual star-forming clouds, so both model families require subgrid star-formation and feedback prescriptions.
- scope/boundary: Numerical resolution and hydrodynamic method change what is unresolved and how subgrid energy couples.
- review basis: Sections 2.2, 3.1, and 3.3.
- confidence note: High.
- source keys: [REV03], [REV03-P019], [REV03-P020], [REV03-P024], [REV03-P049]
- trust_score: 0.97

[REV03-E05]
- role: established
- epistemic_type: observation
- atomic finding: Resolved and global gas-SFR relations provide the empirical foundation for star-formation recipes used in models.
- scope/boundary: Total-gas and molecular relations differ by regime and scale; calibration does not establish a universal cloud-scale efficiency.
- review basis: Section 3.1.
- confidence note: High for empirical correlation, moderate for causal interpretation.
- source keys: [REV03], [REV03-P006], [REV03-P008], [REV03-P038], [REV03-P045]
- trust_score: 0.94

[REV03-E06]
- role: established
- epistemic_type: review_synthesis
- atomic finding: Stellar-driven outflows are central to lowering low-mass galaxy efficiencies, transporting metals, and coupling the ISM to the CGM.
- scope/boundary: Required model effect is robust; launch mechanism, mass loading, hydrodynamic coupling, and recycling remain model-dependent.
- review basis: Section 3.3.2 and Section 4.1.
- confidence note: High for importance, moderate for implementation.
- source keys: [REV03], [REV03-P004], [REV03-P018], [REV03-P049], [REV03-P050]
- trust_score: 0.93

[REV03-E07]
- role: established
- epistemic_type: semi_analytic_model
- atomic finding: Successful galaxy population models require preventive suppression of cooling and star formation in massive halos in addition to low-mass stellar feedback.
- scope/boundary: Radio-mode black-hole feedback is a phenomenological galaxy-scale implementation, not proof of unique AGN microphysics; virial heating and environmental channels also matter.
- review basis: Sections 3.3 and 4.1.
- confidence note: High for a high-mass suppression channel, lower for unique cause.
- source keys: [REV03], [REV03-P015], [REV03-P046], [REV03-P051]
- trust_score: 0.89

[REV03-E08]
- role: established
- epistemic_type: observation
- atomic finding: Most star-forming galaxies occupy a relatively narrow SFR-stellar-mass sequence, making sustained gas supply and regulation a central model benchmark.
- scope/boundary: Selection, SFR indicator, stellar masses, redshift, and treatment of starbursts/quiescent systems affect slope and scatter.
- review basis: Section 1.1.2.
- confidence note: High for the sequence, moderate for a unique equilibrium interpretation.
- source keys: [REV03], [REV03-P047], [REV03-P053]
- trust_score: 0.94

[REV03-E09]
- role: established
- epistemic_type: empirical_inference
- atomic finding: Abundance matching places peak stellar conversion efficiency near Milky-Way-scale halos and much lower efficiencies toward both lower and higher halo masses.
- scope/boundary: Inference assumes halo catalogs, galaxy mass functions, scatter, satellite treatment, and stellar-mass systematics.
- review basis: Section 4.1.
- confidence note: High for non-monotonic efficiency, moderate for exact normalization.
- source keys: [REV03], [REV03-P009], [REV03-P010], [REV03-P011], [REV03-P032]
- trust_score: 0.93

[REV03-E10]
- role: established
- epistemic_type: review_synthesis
- atomic finding: Mergers, dissipative gas dynamics, and internal disk instabilities can all alter bulges, compactness, and morphology.
- scope/boundary: Relative importance varies with mass, gas fraction, redshift, orbit, and environment; morphology alone does not identify the channel.
- review basis: Section 4.2.
- confidence note: High for multiple channels, moderate for their population weights.
- source keys: [REV03], [REV03-P016], [REV03-P021], [REV03-P022], [REV03-P023], [REV03-P029], [REV03-P030]
- trust_score: 0.91

[REV03-E11]
- role: established
- epistemic_type: analytic_theory
- atomic finding: Halo angular momentum and baryonic retention/loss provide a baseline connection between halo properties and disk sizes.
- scope/boundary: Simple angular-momentum conservation is modified by feedback, torques, accretion geometry, mergers, and component exchange.
- review basis: Section 4.2.1.
- confidence note: High as a baseline, moderate as a quantitative prediction.
- source keys: [REV03], [REV03-P003], [REV03-P048], [REV03-P054]
- trust_score: 0.91

[REV03-E12]
- role: established
- epistemic_type: observation
- atomic finding: Stellar and gas-phase metallicity relations provide independent constraints on integrated star formation, enrichment, inflow, and metal loss.
- scope/boundary: Calibration scales, apertures, yields, dust, and abundance methods can shift normalizations.
- review basis: Sections 1.1.2 and 3.1.
- confidence note: High for mass trends, moderate for absolute metallicity and mechanism.
- source keys: [REV03], [REV03-P012], [REV03-P013], [REV03-P017], [REV03-P018]
- trust_score: 0.93

## 3. Open debates and tensions

[REV03-D01] | role=debate | topic=SAM versus hydrodynamic convergence | positions=Different techniques can converge on broad populations versus agreement being driven by shared calibrations and analogous subgrid assumptions. | unresolved=Controlled same-initial-condition and same-physics comparisons remained limited. | boundary=Numerical method, resolution, and calibration sets must be explicit. | source keys=[REV03], [REV03-P020], [REV03-P024], [REV03-P025], [REV03-P035] | trust_score=0.91
[REV03-D02] | role=debate | topic=Cold versus hot accretion | positions=Filamentary cold supply dominates much galaxy growth versus stable virial shocks and cooling atmospheres controlling massive systems. | unresolved=Mode definitions, mixing, feedback, resolution, and tracer observability alter classifications. | boundary=Halo mass, metallicity, redshift, and environment dependent. | source keys=[REV03], [REV03-P005], [REV03-P026] | trust_score=0.90
[REV03-D03] | role=debate | topic=Wind implementation and recycling | positions=Kinetic kicks, thermal deposition, or more explicit multiphase feedback produce the required regulation through different paths. | unresolved=Launch scales are unresolved in cosmological boxes and recycled gas is difficult to observe directly. | boundary=Mass loading and recycling are model outputs tied to subgrid choices. | source keys=[REV03], [REV03-P018], [REV03-P049], [REV03-P050] | trust_score=0.90
[REV03-D04] | role=debate | topic=Low- and high-mass quenching | positions=Stellar feedback dominates shallow halos while virial heating/black-hole feedback suppresses massive systems versus overlapping environmental and supply processes. | unresolved=Multiple implementations match some of the same tuned population statistics. | boundary=No claim that one channel explains every quenched galaxy. | source keys=[REV03], [REV03-P004], [REV03-P015], [REV03-P033], [REV03-P046], [REV03-P051] | trust_score=0.88
[REV03-D05] | role=debate | topic=Angular momentum and size evolution | positions=Sizes largely reflect halo spin with approximate angular-momentum retention versus feedback-selective loss, torques, and accretion history setting sizes. | unresolved=Direct baryon-angular-momentum accounting across phases was incomplete. | boundary=Disk/spheroid, mass, redshift, and selection dependent. | source keys=[REV03], [REV03-P003], [REV03-P048], [REV03-P054] | trust_score=0.89
[REV03-D06] | role=debate | topic=Mergers versus internal structural evolution | positions=Major/minor mergers dominate spheroid and compact-galaxy growth versus violent disk instability and secular evolution contributing substantially. | unresolved=Observed morphology and simulations did not uniquely reconstruct histories. | boundary=Gas fraction, orbit, mass ratio, redshift, and resolution. | source keys=[REV03], [REV03-P016], [REV03-P021], [REV03-P022], [REV03-P023], [REV03-P029], [REV03-P030] | trust_score=0.90
[REV03-D07] | role=debate | topic=Subgrid degeneracy | positions=Phenomenological recipes are adequate effective descriptions versus different recipes yielding similar calibrations but divergent mechanisms and secondary predictions. | unresolved=The physical launch and coupling scales were unresolved and systematic code comparisons were sparse. | boundary=Numerical convergence is not physical validation. | source keys=[REV03], [REV03-P019], [REV03-P020], [REV03-P024], [REV03-P049] | trust_score=0.95
[REV03-D08] | role=debate | topic=Reproducing stellar-mass functions without overcalibration | positions=Matching evolving mass functions demonstrates successful regulation versus extensive tuning hiding incorrect gas-cycle mechanisms. | unresolved=Mass-function, SFR, gas, metallicity, and structural constraints were not simultaneously matched uniquely. | boundary=Distinguish calibrated observables from predictions. | source keys=[REV03], [REV03-P009], [REV03-P010], [REV03-P015], [REV03-P032], [REV03-P051], [REV03-P055] | trust_score=0.94

## 4. Key measurements, model benchmarks, and calibrations

[REV03-N01] | role=benchmark | metric=Peak stellar-to-halo conversion scale | value=maximum near halo mass ~10^12 Msun, with lower efficiency on both sides | sample/method=multi-epoch abundance matching | calibrated_or_predicted=empirical inference used as model target | caveat=stellar masses, halo catalogs, scatter, satellites | source keys=[REV03], [REV03-P009], [REV03-P010], [REV03-P032] | trust_score=0.91
[REV03-N02] | role=benchmark | metric=Cold/hot transition scale | value=order 10^11.5-10^12 Msun halo mass in idealized/theory and cited simulations | sample/method=cooling-time versus compression and hydrodynamic accretion histories | calibrated_or_predicted=theory/simulation result | caveat=redshift, metallicity, geometry, feedback, definition | source keys=[REV03], [REV03-P005], [REV03-P026] | trust_score=0.88
[REV03-N03] | role=measurement | metric=Star-forming main-sequence scatter | value=order 0.3 dex for selected star-forming populations | sample/method=multiwavelength field surveys to z~2.5 | calibrated_or_predicted=observational benchmark | caveat=SFR and mass estimators, selection, redshift bins | source keys=[REV03], [REV03-P047], [REV03-P053] | trust_score=0.89
[REV03-N04] | role=calibration | metric=Global Kennicutt-Schmidt relation | value=surface SFR approximately proportional to gas surface density^1.4 in the original global sample | sample/method=disk-averaged normal and starburst galaxies | calibrated_or_predicted=empirical subgrid anchor | caveat=scale, gas phase, conversion factor, dynamical regime | source keys=[REV03], [REV03-P008] | trust_score=0.93
[REV03-N05] | role=measurement | metric=Molecular-gas star-formation relation | value=approximately linear over much of nearby disk regime with order-Gyr depletion times | sample/method=sub-kpc resolved nearby-galaxy maps | calibrated_or_predicted=observational benchmark | caveat=CO conversion, resolution, dense/starburst regimes | source keys=[REV03], [REV03-P006] | trust_score=0.91
[REV03-N06] | role=measurement | metric=Local gas-phase mass-metallicity relation | value=measured for roughly 53,000 SDSS star-forming galaxies | sample/method=fiber spectroscopy and strong-line calibration | calibrated_or_predicted=observational benchmark | caveat=aperture and abundance-calibration systematics | source keys=[REV03], [REV03-P013] | trust_score=0.94
[REV03-N07] | role=measurement | metric=Galaxy size-mass evolution to z~3 | value=star-forming and quiescent populations show different mass-normalized size evolution | sample/method=3D-HST+CANDELS structural fits | calibrated_or_predicted=observational benchmark | caveat=rest wavelength, Sérsic modeling, progenitor selection | source keys=[REV03], [REV03-P054] | trust_score=0.91
[REV03-N08] | role=benchmark | metric=Evolving star-forming/quiescent stellar-mass functions | value=population functions constrained to z~4 in the cited UltraVISTA analysis | sample/method=photometric redshifts and SED masses | calibrated_or_predicted=model target, not a model output | caveat=mass completeness, Eddington bias, IMF, photo-z | source keys=[REV03], [REV03-P055] | trust_score=0.90

## 5. What remained unknown in 2015

[REV03-U01] | role=future | gap=Physical launch and coupling of stellar feedback across unresolved scales | importance=sets mass loading, phase structure, and regulation | needed=multiscale simulations and resolved wind/ISM observations | source keys=[REV03], [REV03-P018], [REV03-P049], [REV03-P050]
[REV03-U02] | role=future | gap=Direct rates and geometry of cosmological inflow | importance=separates supply regulation from feedback regulation | needed=CGM kinematics/metallicity plus tracer-forward simulations | source keys=[REV03], [REV03-P005], [REV03-P026]
[REV03-U03] | role=future | gap=Wind recycling times and baryon pathways through the CGM | importance=recycled gas may dominate later fueling | needed=Lagrangian phase tracking and observational inflow/outflow discrimination | source keys=[REV03], [REV03-P018], [REV03-P049]
[REV03-U04] | role=future | gap=Unique cause of massive-galaxy quenching | importance=different mechanisms can match the bright-end cutoff | needed=gas-state, environment, halo, and time-resolved quenching tests | source keys=[REV03], [REV03-P015], [REV03-P033], [REV03-P046], [REV03-P051]
[REV03-U05] | role=future | gap=Relative roles of mergers and internal processes in structural evolution | importance=connects morphology to assembly history | needed=kinematics, stellar populations, pair histories, and controlled simulations | source keys=[REV03], [REV03-P016], [REV03-P021], [REV03-P022], [REV03-P023], [REV03-P054]
[REV03-U06] | role=future | gap=Physical convergence rather than calibration convergence | importance=similar observables can arise from different subgrid mechanisms | needed=same-initial-condition multi-code tests, resolution ladders, and out-of-sample observables | source keys=[REV03], [REV03-P019], [REV03-P020], [REV03-P024]

## 6. Primary-citation harvest

The 46 rows below are primary observational, empirical, analytic, semi-analytic, or simulation papers directly cited by Somerville & Davé 2015. Four cited reviews are retained separately for orientation and are not counted toward the primary total. Eight raw candidates are quarantined for absent review membership or AGN-microphysics scope.
"""

primary = [row["source"] for row in registry["rows"] if row["source"]["source_class"] == "primary"]
supporting = [row["source"] for row in registry["rows"] if row["source"]["source_class"] != "primary"]
for s in primary:
    body += f"\n[{s['key']}] {s['authors']} ({s['year']}, {s['journal']}) | title={s['title']} | DOI:{s['doi']}; arXiv:{s['arxiv']}; ADS:{s['ads_bibcode']} | role={s['role']} | review_locator={s['review_locator']} | {s['boundary']}"
body += "\n\n### Supporting cited reviews — not counted as primary\n"
for s in supporting:
    body += f"\n[{s['key']}] {s['authors']} ({s['year']}, {s['journal']}) | title={s['title']} | DOI:{s['doi']}; arXiv:{s['arxiv']}; ADS:{s['ads_bibcode']} | role={s['role']} | review_locator={s['review_locator']} | {s['boundary']}"

body += "\n\n## 7. DO_NOT_USE_UNVERIFIED\n\n"
for row in registry["rows"] + registry["quarantined_rows"]:
    raw = row.get("raw_identity")
    if raw and row.get("corrected_from_raw"):
        s = row["source"]
        body += f"UNCITED_NOT_USABLE | raw {s['key']} tuple title={raw['title']}; DOI:{raw['doi']}; arXiv:{raw['arxiv']}; ADS:{raw['ads_bibcode']} | cross-wired composite identity | ADS-correct physical tuple is title={s['title']}; DOI:{s['doi']}; arXiv:{s['arxiv']}; ADS:{s['ads_bibcode']}\n"
for row in registry["quarantined_rows"]:
    s = row["source"]
    body += f"UNCITED_NOT_USABLE | {s['key']} {s['authors']} ({s['year']}) title={s['title']} | ADS:{s['ads_bibcode']} | {row['quarantine_reason']}\n"
concepts = [
    "UNCITED_NOT_USABLE | one model technique is inherently correct | overbroad claim | SAMs and hydro have different strengths and shared unresolved physics",
    "UNCITED_NOT_USABLE | matching a tuned stellar-mass function proves the feedback mechanism | calibration circularity | distinct prescriptions can fit the same target",
    "UNCITED_NOT_USABLE | subgrid prescriptions are first-principles predictions | category error | they approximate unresolved processes",
    "UNCITED_NOT_USABLE | convergence at one resolution proves physical convergence | unsupported inference | numerical and physical convergence are distinct",
    "UNCITED_NOT_USABLE | all quenching has one cause | overbroad claim | halo, stellar, black-hole, environmental, and supply channels overlap",
    "UNCITED_NOT_USABLE | all high-redshift star formation is merger driven | overbroad claim | main-sequence and instability channels remain",
    "UNCITED_NOT_USABLE | post-2015/JWST/ML source anchors captured by web search | outside date and not review-cited | excluded from usable rows",
    "UNCITED_NOT_USABLE | AGN demographics, accretion-disk, jet, or black-hole-spin claim | outside non-AGN core scope | only bounded galaxy-scale feedback phenomenology is retained",
]
body += "\n".join(concepts) + "\n"

body += "\n## 8. Review and source identity ledger\n\n"
body += "[REV03] | Somerville & Davé (2015, Annual Review of Astronomy and Astrophysics) | DOI:10.1146/annurev-astro-082812-140951; arXiv:1412.2712; ADS:2015ARA&A..53...51S | role=review | bounded 2015 galaxy-formation model synthesis\n"
for row in registry["rows"]:
    s = row["source"]
    body += f"[{s['key']}] | {s['authors']} ({s['year']}, {s['journal']}) | DOI:{s['doi']}; arXiv:{s['arxiv']}; ADS:{s['ads_bibcode']} | role={s['role']} | {s['boundary']}\n"
body += "\nREVIEW_BASE_03_DR_COMPLETE_REFERENCE_ONLY\n"
OUT.write_text(body)
print(json.dumps({"canonical_packet": str(OUT), "chars": len(body), "lines": len(body.splitlines()), "primary": len(primary), "supporting": len(supporting), "quarantined": len(registry['quarantined_rows'])}, sort_keys=True))
