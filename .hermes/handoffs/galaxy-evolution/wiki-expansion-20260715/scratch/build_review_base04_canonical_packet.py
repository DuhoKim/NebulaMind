import json
from pathlib import Path

AREA = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/wiki-expansion-20260715")
REGISTRY = AREA / "area_review_04_naab_ostriker_2017_CURATED_SOURCE_REGISTRY.json"
OUT = AREA / "area_review_04_naab_ostriker_2017_DR_PACKET.md"
registry = json.loads(REGISTRY.read_text())

body = """# Review Base 04 canonical advisory packet — Naab & Ostriker 2017

status: READY_FOR_HWAO_REVIEW
advisory_only: true
wiki_write_performed_by_tori: false
canonical_source_base_not_live_wiki_prose: true
raw_packet_sha256: 69860881137f7c919f2bc9be32f149eace280672df093870ff63abb8f54e9af0
source_registry_status: PASS
usable_sources: 44
primary_sources: 40
supporting_reviews_or_references: 4
quarantined_sources: 9

## 1. Review identity and scope map

[REV04] Naab, Thorsten & Ostriker, Jeremiah P. (2017, Annual Review of Astronomy and Astrophysics) | title=Theoretical Challenges in Galaxy Formation | DOI:10.1146/annurev-astro-081913-040019; arXiv:1612.06891; ADS:2017ARA&A..55...59N | role=review_synthesis | trust_score=0.98 | boundary=2017 synthesis centered on unresolved ISM, star formation, stellar feedback, outflows, and numerical galaxy-formation modeling.

- Shared problem: cosmological models must connect halo-scale inflow and CGM exchange to parsec/sub-parsec ISM processes they generally cannot resolve.
- ISM: supports a multiphase, turbulent, magnetized, cosmic-ray-bearing medium rather than a single effective fluid.
- Star formation: empirical density/SFR laws are useful subgrid anchors; calibration is not a first-principles derivation.
- Stellar feedback: photoheating, radiation, winds, supernovae, and nonthermal pressure act at different times and scales; no universal single-channel hierarchy was established.
- Outflows: supports mass, energy, momentum, and metal transport into fountains and the CGM; launch and recycling remain model dependent.
- Numerical methods: supports bounded comparison of thermal, kinetic, delayed-cooling, decoupled-wind, and more explicit approaches; numerical convergence is not automatically physical convergence.
- Black-hole feedback appears only as a bounded galaxy-scale ingredient. Accretion, jet, and AGN-demographic microphysics remain outside this packet.
- Post-2017/JWST/ML follow-up is outside the historical review boundary.

## 2. Established findings

[REV04-E01]
- role: established
- epistemic_type: review_synthesis
- atomic finding: Low galaxy baryon-conversion efficiencies and substantial circumgalactic gas make inflow, outflow, and recycling central to galaxy-formation models.
- scope/boundary: The accounting requirement is robust; individual phase fluxes and recycling times are not uniquely measured.
- review basis: Introduction and Section 1.
- confidence note: High for the baryon-cycle framing.
- source keys: [REV04], [REV04-P025], [REV04-P045], [REV04-P046]
- trust_score: 0.95

[REV04-E02]
- role: established
- epistemic_type: hydrodynamic_simulation
- atomic finding: Early cooling-only simulations formed excessive central stellar mass and lost too much baryonic angular momentum, motivating strong regulation and better numerical treatment.
- scope/boundary: Severity depends on resolution, UV background, star formation, feedback, and merger history.
- review basis: Sections 2.1-2.2.
- confidence note: High as a historical simulation failure mode.
- source keys: [REV04], [REV04-P001], [REV04-P002], [REV04-P004], [REV04-P009], [REV04-P022], [REV04-P023], [REV04-P032], [REV04-P033]
- trust_score: 0.95

[REV04-E03]
- role: established
- epistemic_type: review_synthesis
- atomic finding: The ISM is multiphase and supported by interacting thermal, turbulent, magnetic, cosmic-ray, and gravitational components.
- scope/boundary: Relative pressures and phase fractions vary with galactic environment, density, height, and star-formation activity.
- review basis: Sections 1 and 3.
- confidence note: High for multiple components, moderate for their local partition.
- source keys: [REV04], [REV04-P008], [REV04-P020], [REV04-P031], [REV04-S01]
- trust_score: 0.94

[REV04-E04]
- role: established
- epistemic_type: calibration
- atomic finding: Cosmological simulations commonly encode unresolved star formation using density and timescale criteria calibrated against resolved or global gas-SFR relations.
- scope/boundary: Thresholds, eligible phase, efficiency, pressure floor, and averaging scale differ among models.
- review basis: Section 2.1.
- confidence note: High for modeling practice, moderate for physical uniqueness.
- source keys: [REV04], [REV04-P010], [REV04-P021], [REV04-P023], [REV04-P024], [REV04-P028], [REV04-P039], [REV04-P041]
- trust_score: 0.95

[REV04-E05]
- role: established
- epistemic_type: analytic_theory
- atomic finding: A supernova remnant transfers energy and momentum through free-expansion, Sedov-Taylor, shell-formation/radiative, and later momentum-dominated stages.
- scope/boundary: Ambient density, metallicity, turbulence, pre-existing bubbles, and clustering alter shell-formation scales and final momentum.
- review basis: Section 3.1.
- confidence note: High for stage structure, moderate for one universal terminal value.
- source keys: [REV04], [REV04-P007], [REV04-P012], [REV04-P018], [REV04-P026], [REV04-P030], [REV04-P044], [REV04-S02]
- trust_score: 0.96

[REV04-E06]
- role: established
- epistemic_type: hydrodynamic_simulation
- atomic finding: Depositing supernova thermal energy at insufficient resolution can radiate it away before the remnant performs the resolved mechanical work, producing numerical overcooling.
- scope/boundary: Outcome depends on gas-element mass, ambient density, injection temperature, timestep, cooling, and whether terminal momentum is explicitly supplied.
- review basis: Sections 2.2 and 3.1.
- confidence note: High.
- source keys: [REV04], [REV04-P003], [REV04-P014], [REV04-P018], [REV04-P026], [REV04-P030], [REV04-P038]
- trust_score: 0.97

[REV04-E07]
- role: established
- epistemic_type: review_synthesis
- atomic finding: Pre-supernova photoheating, radiation, and winds can restructure stellar birth environments before supernova explosions, altering later energy and momentum coupling.
- scope/boundary: Relative channel importance depends on cloud surface density, metallicity, clustering, and resolution.
- review basis: Sections 3.2-3.3.
- confidence note: High for timing/coupling, lower for a universal hierarchy.
- source keys: [REV04], [REV04-P003], [REV04-P018], [REV04-P044], [REV04-S02]
- trust_score: 0.90

[REV04-E08]
- role: established
- epistemic_type: review_synthesis
- atomic finding: Stellar feedback must launch or maintain galactic outflows to regulate low-mass galaxies and transport metals beyond star-forming disks.
- scope/boundary: Required regulation is robust; mass loading, velocity, phase structure, and escape fraction are galaxy- and implementation-dependent.
- review basis: Sections 1.3 and 3.
- confidence note: High for importance, moderate for quantitative scalings.
- source keys: [REV04], [REV04-P014], [REV04-P015], [REV04-P027], [REV04-P035], [REV04-S04]
- trust_score: 0.93

[REV04-E09]
- role: established
- epistemic_type: hydrodynamic_simulation
- atomic finding: Ejected gas need not escape permanently; fountain interaction with halo gas can exchange angular momentum and return fuel to disks.
- scope/boundary: Recycling depends on halo mass, launch speed, drag/mixing, cooling, and corona rotation.
- review basis: Sections 1.3 and 3.5.
- confidence note: High for recycling as a pathway, moderate for its rate.
- source keys: [REV04], [REV04-P009], [REV04-P029], [REV04-P045]
- trust_score: 0.90

[REV04-E10]
- role: established
- epistemic_type: analytic_theory
- atomic finding: Magnetic fields and cosmic rays can provide dynamically important nonthermal pressure and can change disk support and wind acceleration.
- scope/boundary: Conclusions depend on magnetic topology and uncertain cosmic-ray diffusion, streaming, losses, and coupling.
- review basis: Sections 1.1 and 3.4.
- confidence note: High for relevance, moderate for quantitative transport.
- source keys: [REV04], [REV04-P008], [REV04-P049]
- trust_score: 0.90

[REV04-E11]
- role: established
- epistemic_type: review_synthesis
- atomic finding: Distinct subgrid feedback implementations can reproduce overlapping galaxy population statistics after calibration.
- scope/boundary: Agreement with calibrated observables is not evidence that launch physics, phase structure, or recycling are correct.
- review basis: Sections 2.2 and 3.5.
- confidence note: High.
- source keys: [REV04], [REV04-P003], [REV04-P014], [REV04-P038], [REV04-P041]
- trust_score: 0.97

[REV04-E12]
- role: established
- epistemic_type: observation
- atomic finding: Low-redshift absorption measurements reveal a substantial cool, enriched CGM around galaxies, providing a reservoir and transport benchmark for models.
- scope/boundary: Ionization corrections, metallicity, geometry, cloud sizes, and halo selection dominate mass estimates.
- review basis: Section 1.3.1.
- confidence note: High for detection and enrichment, moderate for total mass.
- source keys: [REV04], [REV04-P045]
- trust_score: 0.91

## 3. Open debates and tensions

[REV04-D01] | role=debate | topic=Control of star-formation efficiency | positions=Turbulence and gravity establish the efficiency versus early stellar feedback terminates collapse and sets the integrated value. | unresolved=Cosmological boxes did not resolve cloud formation and disruption together. | boundary=Cloud scale, density, metallicity, tracer, and averaging time. | source keys=[REV04], [REV04-P020], [REV04-P024], [REV04-P028], [REV04-P039], [REV04-S01] | trust_score=0.91
[REV04-D02] | role=debate | topic=Dominant stellar-feedback channel | positions=Supernovae provide the main long-lived mechanical budget versus radiation, photoionization, winds, and clustering conditioning the medium enough to control coupling. | unresolved=Timing and cross-channel nonlinearities were not resolved in large volumes. | boundary=Cloud surface density, metallicity, stellar population, and resolution. | source keys=[REV04], [REV04-P003], [REV04-P018], [REV04-P026], [REV04-P044], [REV04-S02] | trust_score=0.90
[REV04-D03] | role=debate | topic=Thermal versus kinetic feedback | positions=Stochastic high-temperature thermal deposition can avoid immediate losses versus kinetic/momentum injection better representing unresolved remnants and wind launch. | unresolved=Both could be calibrated, and both depend on resolution and numerical coupling. | boundary=Gas mass, temperature jump, kick prescription, hydrodynamic decoupling. | source keys=[REV04], [REV04-P014], [REV04-P026], [REV04-P030], [REV04-P038] | trust_score=0.94
[REV04-D04] | role=debate | topic=Explicit versus effective feedback | positions=Resolve individual channels and remnants versus encode their net effect through effective equations of state, delayed cooling, or calibrated winds. | unresolved=Required dynamic range remained impractical for cosmological populations. | boundary=Do not compare methods without matching resolved scale and calibration set. | source keys=[REV04], [REV04-P003], [REV04-P041], [REV04-P044] | trust_score=0.93
[REV04-D05] | role=debate | topic=Wind mass loading and recycling | positions=Strong ejective winds permanently lower efficiencies versus much outflowing material recycling through fountains and the CGM. | unresolved=Multiphase fluxes and return times were hard to observe and numerically sensitive. | boundary=Halo mass, redshift, radius, phase, velocity cut, and time window. | source keys=[REV04], [REV04-P009], [REV04-P014], [REV04-P029], [REV04-P045] | trust_score=0.91
[REV04-D06] | role=debate | topic=Cosmic-ray and magnetic support | positions=Nonthermal pressure may drive cool extended winds versus uncertain transport and losses limiting dynamical impact. | unresolved=Diffusion and streaming coefficients were poorly constrained. | boundary=Magnetic topology, ionization, losses, dimensionality, and resolution. | source keys=[REV04], [REV04-P008], [REV04-P049] | trust_score=0.88
[REV04-D07] | role=debate | topic=Physical versus numerical convergence | positions=Better resolution should converge feedback coupling versus new resolved phases changing the effective problem and requiring revised prescriptions. | unresolved=Few calculations spanned cloud-to-halo scales with fixed physics. | boundary=Convergence must specify observable, algorithm, subgrid model, and physical scale. | source keys=[REV04], [REV04-P018], [REV04-P026], [REV04-P030], [REV04-P038], [REV04-P044] | trust_score=0.96
[REV04-D08] | role=debate | topic=Calibration degeneracy | positions=Reproducing stellar masses and SFRs demonstrates effective regulation versus tuned agreement hiding incorrect mechanisms and secondary predictions. | unresolved=Multiple independent out-of-sample observables were not simultaneously matched uniquely. | boundary=Separate calibrated targets from predictions. | source keys=[REV04], [REV04-P003], [REV04-P014], [REV04-P038], [REV04-P041] | trust_score=0.97

## 4. Key measurements, model benchmarks, and calibrations

[REV04-N01] | role=calibration | metric=Core-collapse supernova energy scale | value=order 10^51 erg per event | sample/method=canonical explosion-energy budget | calibrated_or_predicted=assumed physical input | caveat=event diversity and coupling fraction | source keys=[REV04], [REV04-P012], [REV04-S02] | trust_score=0.94
[REV04-N02] | role=benchmark | metric=Terminal radial momentum per isolated supernova | value=order 2-3 x 10^5 Msun km s^-1 near n_H~1 cm^-3 | sample/method=high-resolution remnant calculations | calibrated_or_predicted=simulation/theory benchmark | caveat=density, metallicity, inhomogeneity, clustering, pre-processing | source keys=[REV04], [REV04-P018], [REV04-P026], [REV04-P030] | trust_score=0.91
[REV04-N03] | role=benchmark | metric=Shell-formation/cooling transition | value=order 10^4-10^5 yr and tens of parsecs for an isolated 10^51 erg event near n_H~1 cm^-3 | sample/method=analytic and resolved remnant models | calibrated_or_predicted=environment-dependent benchmark | caveat=not a universal injection radius/time | source keys=[REV04], [REV04-P007], [REV04-P012], [REV04-P026] | trust_score=0.88
[REV04-N04] | role=measurement | metric=Global Kennicutt-Schmidt slope | value=surface SFR approximately proportional to total-gas surface density^1.4 in the original global sample | sample/method=disk-averaged normal and starburst galaxies | calibrated_or_predicted=observational calibration | caveat=gas phase, conversion factors, scale, and regime | source keys=[REV04], [REV04-P024] | trust_score=0.93
[REV04-N05] | role=measurement | metric=Molecular-gas depletion time | value=order 2 Gyr across much of nearby normal-disk regime | sample/method=resolved nearby-galaxy gas and SFR maps | calibrated_or_predicted=observational benchmark | caveat=CO conversion, dense/starburst regimes, aperture | source keys=[REV04], [REV04-P028] | trust_score=0.90
[REV04-N06] | role=calibration | metric=Wind mass-loading factor | value=eta = mass outflow rate / SFR; no universal 2017 value | sample/method=subgrid wind models and simulations | calibrated_or_predicted=often assumed/calibrated or model-predicted | caveat=measurement radius, phase, time averaging, recycling | source keys=[REV04], [REV04-P014], [REV04-P038] | trust_score=0.94
[REV04-N07] | role=benchmark | metric=Nonthermal Galactic-disk support | value=magnetic and cosmic-ray energy densities are of comparable order to other major ISM components | sample/method=vertical hydrostatic-equilibrium accounting | calibrated_or_predicted=analytic/empirical benchmark | caveat=Milky Way locality and model assumptions | source keys=[REV04], [REV04-P008] | trust_score=0.86
[REV04-N08] | role=measurement | metric=Cool CGM baryonic reservoir | value=order 10^10-10^11 Msun for the cited low-redshift L* halo sample under adopted ionization models | sample/method=COS-Halos absorption and photoionization modeling | calibrated_or_predicted=observational inference | caveat=ionization, metallicity, geometry, cloud size, halo selection | source keys=[REV04], [REV04-P045] | trust_score=0.84

## 5. What remained unknown in 2017

[REV04-U01] | role=future | gap=First-principles emergence of galaxy-scale star-formation laws | importance=calibrated laws limit prediction in new regimes | needed=cloud-resolving radiation-MHD/chemistry linked to galaxy environments | source keys=[REV04], [REV04-P020], [REV04-P024], [REV04-P028], [REV04-P039]
[REV04-U02] | role=future | gap=Survival, mixing, and acceleration of cold gas in hot winds | importance=sets observable phase loading and recycling | needed=high-resolution multiphase MHD with conduction and tracer-forward observations | source keys=[REV04], [REV04-P029], [REV04-P045], [REV04-S04]
[REV04-U03] | role=future | gap=Hierarchy and coupling of pre-supernova feedback channels | importance=sets the density into which supernovae explode | needed=coupled radiation, winds, ionization, and resolved clustered supernovae | source keys=[REV04], [REV04-P003], [REV04-P018], [REV04-P044], [REV04-S02]
[REV04-U04] | role=future | gap=Physical mass loading and recycling scalings | importance=controls stellar masses, metallicities, and fueling | needed=phase-resolved fluxes over radius/time plus scale-bridging simulations | source keys=[REV04], [REV04-P014], [REV04-P029], [REV04-P045]
[REV04-U05] | role=future | gap=Cosmic-ray transport and magnetic coupling | importance=may change cool-wind acceleration and disk support | needed=constrained diffusion/streaming/loss models with gamma-ray and wind tests | source keys=[REV04], [REV04-P008], [REV04-P049]
[REV04-U06] | role=future | gap=Physical validation beyond tuned population statistics | importance=different implementations can match the same target | needed=same-initial-condition resolution ladders and independent gas/CGM/metal/structure predictions | source keys=[REV04], [REV04-P003], [REV04-P014], [REV04-P038], [REV04-P041]

## 6. Primary-citation harvest

The 40 rows below are primary observational, empirical, analytic, or simulation papers directly cited by Naab & Ostriker 2017. Four cited supporting reviews/references are retained separately and not counted toward the primary total. Nine raw candidates are quarantined because exact review membership or identity failed.
"""

primary = [row["source"] for row in registry["rows"] if row["source"]["source_class"] == "primary"]
supporting = [row["source"] for row in registry["rows"] if row["source"]["source_class"] != "primary"]
for s in primary:
    body += f"\n[{s['key']}] {s['authors']} ({s['year']}, {s['journal']}) | title={s['title']} | DOI:{s['doi']}; arXiv:{s['arxiv']}; ADS:{s['ads_bibcode']} | role={s['role']} | review_locator={s['review_locator']} | {s['boundary']}"
body += "\n\n### Supporting cited reviews or references — not counted as primary\n"
for s in supporting:
    body += f"\n[{s['key']}] {s['authors']} ({s['year']}, {s['journal']}) | title={s['title']} | DOI:{s['doi']}; arXiv:{s['arxiv']}; ADS:{s['ads_bibcode']} | role={s['role']} | review_locator={s['review_locator']} | {s['boundary']}"

body += "\n\n## 7. DO_NOT_USE_UNVERIFIED\n\n"
for row in registry["rows"] + registry["quarantined_rows"]:
    raw = row.get("raw_identity")
    if raw and row.get("corrected_from_raw"):
        s = row["source"]
        body += f"UNCITED_NOT_USABLE | raw {s['key']} tuple title={raw['title']}; DOI:{raw['doi']}; arXiv:{raw['arxiv']}; ADS:{raw['ads_bibcode']} | cross-wired composite identity | authoritative tuple is title={s['title']}; DOI:{s['doi']}; arXiv:{s['arxiv']}; ADS:{s['ads_bibcode']}\n"
for row in registry["quarantined_rows"]:
    s = row["source"]
    body += f"UNCITED_NOT_USABLE | {s['key']} {s['authors']} ({s['year']}) title={s['title']} | ADS:{s['ads_bibcode']} | {row['quarantine_reason']}\n"
concepts = [
    "UNCITED_NOT_USABLE | numerical convergence proves physical correctness | overbroad claim | resolved scales and subgrid problem change with resolution",
    "UNCITED_NOT_USABLE | matching one tuned galaxy statistic validates a feedback mechanism | calibration circularity | multiple implementations can match overlapping targets",
    "UNCITED_NOT_USABLE | one feedback channel dominates universally | overbroad claim | hierarchy varies with environment, time, metallicity, and scale",
    "UNCITED_NOT_USABLE | subgrid prescriptions are first-principles predictions | category error | they approximate unresolved processes",
    "UNCITED_NOT_USABLE | one terminal supernova momentum applies to every event | overbroad claim | ambient medium, clustering, and pre-processing alter it",
    "UNCITED_NOT_USABLE | all outflowing gas permanently escapes | unsupported claim | fountains and recycling are central alternatives",
    "UNCITED_NOT_USABLE | post-2017/JWST/ML source anchors captured during browsing | outside date and not review-cited | excluded",
    "UNCITED_NOT_USABLE | accretion-disk, jet, black-hole demographic, or AGN-only claim | outside non-AGN scope | only bounded galaxy-scale regulation context is allowed",
]
body += "\n".join(concepts) + "\n"

body += "\n## 8. Review and source identity ledger\n\n"
body += "[REV04] | Naab & Ostriker (2017, Annual Review of Astronomy and Astrophysics) | DOI:10.1146/annurev-astro-081913-040019; arXiv:1612.06891; ADS:2017ARA&A..55...59N | role=review | bounded 2017 theoretical-challenges synthesis\n"
for row in registry["rows"]:
    s = row["source"]
    body += f"[{s['key']}] | {s['authors']} ({s['year']}, {s['journal']}) | DOI:{s['doi']}; arXiv:{s['arxiv']}; ADS:{s['ads_bibcode']} | role={s['role']} | {s['boundary']}\n"
body += "\nREVIEW_BASE_04_DR_COMPLETE_REFERENCE_ONLY\n"
OUT.write_text(body)
print(json.dumps({"canonical_packet": str(OUT), "chars": len(body), "lines": len(body.splitlines()), "primary": len(primary), "supporting": len(supporting), "quarantined": len(registry['quarantined_rows'])}, sort_keys=True))
