# C41 Status/Debate Map — v1

**The Step-6 deliverable the Baseline board has awaited since 2026-07-03: the map that answers the
frozen question and picks the Track-B study.**

## Header — verification state first

- **Every status label below binds to stance-VERIFIED entries.** Kun's Step-5 adversarial pass
  (verifier ≠ extractor ≠ composer) adjudicated all 80 entries against re-extracted source
  fulltext: **76 `verified_consistent` + 4 `verified_no_claim`, zero failures** — no assertion
  overstates its span, all 19 Step-4 rebinds honored, every certainty label earned or conservative
  (`KUN_STEP5_REPORT.md`; `C41_STANCE_MATRIX.jsonl` sha `59b61d7c…`;
  `VERIFICATION_STATUS_PATCH.jsonl` sha `bcfbeb0b…`).
- **Ledger-on-disk defect, disclosed:** `step4_v8_applier.py` (2026-08-04 14:11 KST) overwrote
  every entry's `verification_status` with the off-enum value `"validated"`, discarding the
  patch's own per-row values. The 76+4 census above therefore binds to the two pinned Kun
  artifacts, not to the ledger field. Byte-diff vs the pre-v8 backup confirms all content fields
  used by this map (`assertion`, `links`, `tags`, `modality`, `certainty_level`,
  `epistemic_type`, `source_bibcodes`) are untouched. Ledger not edited by this lane; applier to
  re-land the patch per-row. Map compiled against `C41_LEDGER.jsonl` sha `e2938298…`.
- **4 no-claim placeholders** (honest zeros, bound spans carry no checkable proposition):
  c41_018, c41_021, c41_059, c41_062. They join no axis and appear in the coverage table only.
- **8 binding-note nits** (assertion content runs past the bound span's truncation; in every case
  Kun confirmed the content in source fulltext — entries right, bindings incomplete): c41_007,
  c41_016, c41_019, c41_024, c41_031, c41_042, c41_053, c41_079. Flagged for span re-cut before
  Step-7 prose.
- **c41_004 / c41_005:** evidence-span zone reconciled to `unknown` and span stance capped at
  `qualifies` by applier v8 (the stance matrix carries `supports`); this map uses the more
  conservative on-disk reading for both.
- **Certainty landscape, stated up front:** 75/76 claims are `emerging_sample_limited`; c41_004
  alone is `actively_debated`. Status labels below are correspondingly flat — the debate structure
  of this corpus lives in modality (`mixed_debated`), the marker tags, and **cross-paper
  conflicts between stance-verified entries**, which is precisely what the interpretation contract
  requires for "disputed."
- **Vocabulary:** status values only from contract-v1.1 `certainty_level` enums as carried by
  member entries; modality tiers only from `modality`. **Lane law:** no sentence below uses a
  modality tier above the bound entry's ledger modality. Externally sourced context (the v2
  dispersion engine) appears only in bracketed blocks labeled *[engine context …]* and is never a
  claim.
- **Boundary:** this is a status/debate MAP artifact, not reader-facing prose (Step-7/8 are
  separate gates; wiki is deprecated, Lab placement is a separate gated proposal). **Information
  firewall:** compiled from ledger + stance matrix + frozen question + dispersion context only;
  no study lane was read — the map picks the study, not the reverse.
- Ledger `as_of` 2026-08-04; compiled 2026-08-04 14:26 KST; author Lana (no-overclaim lane); Hwao
  synthesis-reviews, Kun red-teams, Tori receipts.

## The frozen question (sha `9ac5ca1f…`)

> What do we currently know, what is actively disputed, and what remains unknown about how the
> earliest galaxies (z ≳ 6) formed their stars, enriched their gas, and ionized their
> surroundings — and where do simulation/model predictions and JWST observations genuinely
> disagree?

**K = 7 axes** (derivation: `C41_CONDENSATION_REPORT.md`; the three frozen axes are
super-structure, not a limit on K).

| # | Axis (question) | Entries | Super-axes | Status (enum) |
|---|---|---|---|---|
| A1 | Bright-end pace: how fast does the UV-bright census decline beyond z ≈ 8? | 11 | FE (+IO via 065) | `actively_debated` (carried by c41_004; all other members `emerging_sample_limited`) |
| A2 | Efficiency physics: does constant star-formation efficiency suffice, and to what z? | 7 | FE (+IO via 031) | `emerging_sample_limited` (two-sided via c41_011 `mixed_debated`) |
| A3 | Calibration validity: do locally calibrated metallicity diagnostics survive at high z? | 22 | CE (+FE) | `emerging_sample_limited` (two-sided via c41_037 `mixed_debated`) |
| A4 | FMR/MZR survival: do the scaling relations survive at z > 3? | 14 | CE (+FE, IO) | `emerging_sample_limited` (two-sided via c41_042 `mixed_debated`) |
| A5 | Early enrichment: how early, and through what channels? | 10 | CE (+FE) | `emerging_sample_limited` (one-sided-plus-open, declared) |
| A6 | Reionization budget: can the observed population supply it? | 10 | IO (+FE) | `emerging_sample_limited` (two-sided at assumption level) |
| A7 | Budget attribution: is the ionizing/excitation power in the tested objects stellar? | 3 | IO+CE+FE | `emerging_sample_limited` (one-sided, boundary-ruled) |

FE = formation_efficiency, CE = chemical_enrichment, IO = ionizing_output. c41_065 is the map's
only dual membership (A1+A6, declared under rule R4).

---

## A1 — Bright-end pace: how fast does the UV-bright census decline beyond z ≈ 8?

**The corpus's flagship dispute — its only `actively_debated` entry lives here.**

**Sides**

- **Slow evolution / bright-galaxy over-abundance (JWST era):** c41_074 (`is_are_does`):
  spectroscopic confirmation of JADES-GS-z14-0/-1 confirms the UV luminosity function evolves
  slowly at high redshift, with more luminous galaxies than predicted by a variety of pre-JWST
  models. c41_004 (**holder**, `mixed_debated`, `actively_debated`): spectroscopic constraints
  indicate mild UVLF evolution towards z~12, creating tension with theoretical models of rapid
  evolution — the one entry whose single source carries both sides of the tension. c41_076
  (`mixed_debated`): the measured z~16 **candidate** number density is in clear tension with
  pre-JWST predictions, extending the over-abundance to z~17 — candidates, not confirmations.
  c41_078 (`reported_only`): the JWST abundance of UV-bright z>10 galaxies is reported to have
  challenged traditional models, prompting refined star-formation prescriptions.
- **Rapid decline (earlier censuses):** c41_047 (`reported_only`): pre-JWST HST searches reported
  tentative evidence for a z~10 deficit implying rapid UVLF/SFRD evolution at z>8. c41_063
  (`is_are_does`): the SFRD decreases significantly from z~9 to z~12 — while any further decline
  to z~16 is not larger than the measurement errors; this entry carries a decline AND a
  flattening, one per redshift range.
- **Common ground:** c41_056 (`is_are_does`): a non-evolving UVLF between z~10 and lower
  redshifts is ruled out at 4–5σ — evolution exists; the dispute is its pace.
- **Census qualifiers (bind both sides):** c41_046 (`may_or_can`): the rapid apparent SFRD
  decline at z>8 may reflect the fixed luminosity detection limit. c41_067 (`may_or_can`):
  the contamination-rate estimate may be overestimated. c41_071 (`is_are_does`): the z~7–8 LF
  keeps a Schechter shape. c41_065 (`is_are_does`, dual with A6): steep faint end (α ~ −2) and a
  non-accelerated decline of UV luminosity density beyond z~8 when integrated to M_trunc = −15.

**Best evidence with source-strength:** slow side — 2024Natur.633..318C (c41_074,
observational_sample, full_text: spectroscopic z~14 confirmations); 2024ApJ...960...56H (c41_004,
full_text; span stance `qualifies` after v8). Rapid side — 2011Natur.469..504B (c41_056:
contamination-corrected ~0.8 z~10 galaxies, 4–5σ); 2023ApJS..265....5H (c41_063). All
observational_sample, all full_text, all single-source per entry.

**Measurement dispersion (ledger-carried):** φ(z≈16, M_UV=−17) = 10^−3.47 (+0.13/−0.10)
Mpc⁻³ mag⁻¹ (c41_076, candidates); ~0.8 galaxies vs no-evolution expectation at z~10, 4–5σ
(c41_056); SFRD: significant decline z9→12 vs within-errors decline z12→16 (c41_063). *[engine
context: dispersion_v2 SFRD N=46 measurements, value spread −3.5..−1.0 log M⊙ yr⁻¹ Mpc⁻³,
overall scale factor S_all=3.78 — among the engine's promoted contested quantities.]*

**Status:** `actively_debated` (carried by c41_004); all other members `emerging_sample_limited`.

**Countercase check:** two-sided in-corpus — each side's entries are stance-verified against
their own sources; the qualifiers (046/067) are the in-corpus answer to "who would doubt the
census either side rests on."

**What would settle it:** spectroscopic confirmation of the z ≳ 15 photometric candidates — the
settling method exists in-corpus (c41_074's z~14 confirmations) and the specific missing
measurement is the confirmation (or refutation) of the c41_076 candidate population, under the
completeness/contamination controls that c41_046/c41_067 name. The settling measurement exists
and is in active use; it has not yet reached the contested redshift.

---

## A2 — Efficiency physics: does constant star-formation efficiency suffice, and to what redshift?

**Sides** (asymmetric — the dispute is where sufficiency ends and what closes the gap beyond, not
a flat contradiction)

- **Sufficiency to a horizon:** c41_064 (`may_or_can`): halo-mass-function growth plus a constant
  SFE model can readily explain UVLF evolution from z~10 to z~2.5. c41_011 (**holder**,
  `mixed_debated`, tag `tension_reported`): the observed SFRD is consistent with a constant-SFE
  prediction up to z=12, with tension arising only when z~15–16 samples are included. c41_022
  (`may_or_can`): THESAN's predicted SFRD seems consistent with observations at 10<z<13, though
  with faster evolution and significant reionization-history dependence. c41_068 (`is_are_does`):
  the earlier z>4 theory-observation tension has been largely resolved, though robust comparison
  still requires improved constraints.
- **Modification invoked:** c41_073 (`reported_only`): bursty star formation has been shown to
  significantly alleviate model-observation tension. c41_031 (`may_or_can`, binding-note nit):
  a top-heavy IMF or different SN yields could remove the reported O/Fe tension. c41_080
  (`in_model_only` — the ledger's only simulation-typed entry): within a semi-analytic framework,
  models matching the UVLF fail the observed clustering-bias evolution and vice versa, resolvable
  by a redshift- and mass-dependent star-formation duty cycle.

**Best evidence with source-strength:** all observational_sample full_text except c41_080
(simulation, model_dependence high) and c41_022 (simulation-confrontation content at
`may_or_can`). Single-source per entry throughout.

**Measurement dispersion:** none ledger-carried at axis level (assertions qualitative). *[engine
context: dispersion_v2 imf_slope has N=5, S=1.1 — the IMF lever is thinly measured across the
wider corpus.]*

**Status:** `emerging_sample_limited` (all members); two-sidedness carried by c41_011's
`mixed_debated` modality.

**Countercase check:** in-corpus — the sufficiency side's own holder (011) names the redshift
where its side's account breaks; 080 opposes sufficiency from inside model space
(`in_model_only` cap: never observed-frequency language).

**What would settle it:** the in-corpus discriminants are named — clustering-bias evolution
measured jointly with the UVLF (c41_080, currently in-model only), burst diagnostics
SFR10/SFR100 at z≈10 (c41_007, A5), O/Fe abundance patterns (c41_031). A dataset confronting one
SFE prescription with census + clustering + burst indicators simultaneously does not appear in
this corpus; the components each exist separately.

---

## A3 — Calibration validity: do locally calibrated metallicity diagnostics survive at high redshift?

**The corpus's largest axis (22 entries) and its clearest cross-paper contradiction cluster.**
Holder: c41_037 (`mixed_debated`): whether locally calibrated strong-line metallicity relations
remain valid at high redshift is under recent debate — the axis's existence is itself
ledger-carried.

**Sides**

- **Diagnostics shift or fail:** c41_033 (`is_are_does`): local N2/O3N2 calibrations
  underestimate high-z metallicity by 0.05–0.1 dex — while analog-built calibrations yield
  consistent values (this entry carries both sides' material). c41_035: N2S2- and N2O2-based N/O
  become inconsistent off the z~0 BPT locus. c41_044: different indicators yield different
  low-mass MZR slopes at high z. c41_045: strong-line calibrations are often mutually
  inconsistent, not fully explained by calibration samples. c41_049: methods disagree
  systematically with metallicity; the direct-vs-theoretical offset cause remains unknown.
  c41_032: the Jones et al. R23 calibration is inconsistent with the strong-line-emitter sample.
  c41_015: O32/Ne3O2/O3N2/O3S2 individually scatter-limited. c41_006: [Si III] 1893 metallicities
  scatter and do not reliably correlate with optical ones. c41_002 (local): direct t2 measurements
  are inconsistent with the values required to explain the ADF — a foundational tension inside
  the direct method itself.
- **Diagnostics workable:** c41_043 (`is_are_does`): O/Ne/H strong-line calibrations do not
  strongly evolve with redshift and can reliably estimate abundances to z~3 — the direct in-corpus
  counterparty to 033/035/044/045. c41_023: the direct method remains an important and successful
  tool locally. c41_024 (binding-note nit): Te + ICF machinery yields accurate ionic abundances
  ("all elements" is the source's own phrase).
- **Why they might fail (physical drivers):** c41_029: z>1 galaxies match high-z analogs and sit
  ≥2σ off the z~0 reference in O3/O2/R23/O32. c41_038: electron-density evolution alone cannot
  explain the z~2 BPT offset under non-evolving hardness — N/O and ionization parameter remain
  the candidate drivers. c41_058 (`may_or_can`): high log U ~ −2.5 in representative z~2 galaxies
  may arise from compact massive low-metallicity clusters. c41_034: the local anchor —
  composite SDSS spectra disentangle H II-region conditions from mass and sSFR. c41_009
  (`may_or_can`): the Nakajima-calibration disagreement may be parameterization, not physics.
- **Capability anchors:** c41_012 (`is_are_does`): auroral-line detections at z>3 remain limited
  to ~25 galaxies — **the axis's binding statistic**. c41_026: first EoR rest-optical spectra
  including auroral [O III] 4363. c41_061: first direct-method metallicity at z>1
  (7.5 +0.1/−0.2). c41_060: faint-line measurability at z~2 demonstrated.

**Best evidence with source-strength:** both sides observational_sample, full_text, single-source
per entry; the conflict 043-vs-{033, 035, 044, 045, 049} is between stance-verified entries and
is the map's cleanest "disputed" verdict under the interpretation contract.

**Measurement dispersion (ledger-carried):** 0.05–0.1 dex local-calibration underestimate
(c41_033); [Si III]-vs-optical scatter 0.35±0.28 dex (c41_006); ≥2σ line-ratio offsets from the
z~0 sample (c41_029); ~25 auroral anchor galaxies at z>3 (c41_012). *[engine context:
dispersion_v2's most overdispersed quantity is exactly this one — metallicity N=304, S_all=9.5,
split axis "calibration", values 7.0–9.1.]*

**Status:** `emerging_sample_limited` (all 22); debate carried by c41_037's `mixed_debated`
modality and the cross-paper cluster above.

**Countercase check:** two-sided in-corpus (043 vs the shift/fail cluster; 009 offers the
deflationary reading of one disagreement).

**What would settle it:** grow the z>3 auroral/Te anchor set beyond ~25 galaxies (c41_012 defines
the deficiency; c41_026/c41_013/c41_061 demonstrate feasibility), then re-test c41_043 against
c41_033/035/044/045 on matched samples with Te anchors. Concrete, falsifiable, and the
measurement exists — statistics are the gap.

---

## A4 — FMR/MZR survival: do the scaling relations survive at z > 3?

**Sides**

- **Framework holds (to intermediate z):** c41_036 (`is_are_does`): the FMR — higher SFR ↔ lower
  metallicity at fixed mass (definitional, correctly attributed). c41_057: the anticorrelation is
  present at low mass and absent above log M* > 10.9. c41_053 (binding-note nit: "preference…"
  slightly stronger than the source's "suggestive of"): the low-mass high-z MZR agrees with
  extrapolations, suggesting downsizing with energy-driven winds. c41_055: z~2–3 emitters are
  consistent with the z≤2.2 MZR. c41_027: CLASSY is consistent with the Local Volume MZR while
  bursting at high-z-like SFRs. c41_042-inside (`mixed_debated`, the stance matrix's only `mixed`
  row): metallicities agree with the Andrews & Martini MZR within −9.00 < sSFR < −8.25.
- **Deviations at high z / equilibrium broken:** c41_020 (`reported_only`): JWST observations are
  reported to challenge the FMR at z>3. c41_077 (`is_are_does`): low-mass, high-sSFR galaxies
  common at high z are inconsistent with the equilibrium conditions underlying the local FMR,
  indicating rapid early enrichment. c41_042-outside: broadly inconsistent with the MZR outside
  its sSFR window (binding-note nit: span omits the paper's own selection caveat).
- **Measurement base and open frame:** c41_008: 146 JWST galaxies across 3 dex in M* constrain
  the M–O/H–SFR relations to early assembly. c41_040: KMOS3D, 419 galaxies, z=0.6–2.7, single
  selection/tracer/methodology. c41_054: MASSIV annular abundances (50 galaxies, z~1.2). c41_048:
  z~2 sample, SFR ~5–100 M⊙/yr, median O/H 8.34. c41_039 (`reported_only`): MS slope ~1, ~0.3 dex
  scatter to z~5. c41_052 (`is_are_does`): MZR shape/normalization at z≳3 remain poorly
  constrained, especially at low mass — the axis's own open-frame entry.

**Best evidence with source-strength:** all observational_sample, full_text, single-source per
entry; the holds-vs-deviates conflict (036/053/055/027 vs 020/077, with 042 split across its own
window) is stance-verified on both sides.

**Measurement dispersion (ledger-carried):** the 042 agreement window −9.00 < sSFR < −8.25; MS
scatter ~0.3 dex (c41_039); sample scales 146 / 419 / 50 galaxies (008/040/054); median O/H 8.34
at z~2 (c41_048).

**Status:** `emerging_sample_limited`; two-sided via c41_042's `mixed_debated` modality plus the
020/077-vs-036/053/055 cross-paper conflict.

**Countercase check:** two-sided in-corpus, with 052 marking how much of the z≳3 regime is
unconstrained rather than contested.

**What would settle it:** an FMR test at z>3 holding selection, tracer, and calibration fixed —
the c41_040 single-methodology design extended past z=3 and anchored by A3's Te set. The design
exists in-corpus at z<3; its z>3 execution does not.

---

## A5 — Early enrichment: how early, and through what channels, did enrichment proceed?

**One-sided-plus-open, declared.** Frame-holder: c41_075 (`is_are_does`): the drivers of high-z
metallicity trends — inflow, outflow, AGN/stellar feedback — remain a "Grand Challenge."

**What the corpus establishes (at `emerging_sample_limited`, case-grade):**

- Enrichment is already substantial very early: c41_013 (`shows_can_occur`): O/H ~ 7.5–8.0 and
  log ξ_ion = 25.2±0.2 in a galaxy 460 Myr after the Big Bang — the in-corpus frontier epoch.
  c41_030 (`may_or_can`): ≥0.1-solar lower bounds at z~8 suggest prior star formation lasting
  tens of Myr or more. c41_025 (`shows_can_occur`): a low-mass galaxy at O/H = 7.16 +0.10/−0.12.
  c41_017 (`shows_can_occur`): GN-z9p4 at 7.37±0.15 with highly super-solar N/O and normal
  C/O, Ne/O. c41_001 (`may_or_can`): rapid formation may produce widespread sub-solar S/O and
  Ar/O.
- Star-formation mode context: c41_007 (`shows_can_occur`, binding-note nit): z≈10 sample with
  median sSFR 58 Gyr⁻¹ and bursty SF on 10-vs-100 Myr timescales (log SFR10/SFR100 = 0.4).
  c41_019 (`shows_can_occur`, binding-note nit): an interaction-driven gas-supply case (gas
  bridge in COSMOS24108) — the map's weakest placement, held here as a gas-supply case anchor and
  flagged as peripheral. c41_028 (`is_are_does`): the local-analog baseline — 1969 EELGs spanning
  7.7 < O/H < 8.6, −1.8 < log N/O < −0.8.
- **The axis's only debate edge — channel exclusion:** c41_016 (`is_are_does`, binding-note nit):
  massive-star wind yields with super-solar C and O cannot, without a conveyor-belt episode,
  explain the globular-cluster anomalies or the N/O and C/O of CEERS-1019 and GN-z11.

**Countercase honesty:** no in-corpus entry defends the excluded wind-only channel, and no entry
opposes the rapid-early-enrichment reading. The one-sidedness is a property of this working
corpus, not evidence of consensus — every member is single-source, and the axis status stays
`emerging_sample_limited`.

**Measurement dispersion (ledger-carried):** direct-method O/H across individual early objects
spans 7.16 – 8.0 (c41_025 / c41_017 / c41_013; c41_061 in A3) — **different objects at different
epochs: a definitional spread, not a measurement scatter on one quantity** (the AGN pilot's
do-not-average lesson, applied).

**Status:** `emerging_sample_limited` (all members); one-sided-plus-open, declared.

**What would settle it:** larger N-emitter samples with full abundance patterns (N/O, C/O, Ne/O —
c41_017's pattern set) to test c41_016's conveyor-belt requirement against alternatives; and
metallicity determinations at epochs earlier than 460 Myr. Both are direct extensions of
measurements this corpus already contains.

---

## A6 — Reionization budget: can the observed galaxy population supply it?

**Sides** (two-sided at the assumption level)

- **Sufficient under stated assumptions:** c41_066 (`is_are_does`): the steep UVLF extends to
  M_UV = −13 at z>6, consistent with the number of faint galaxies required to reionize the
  Universe **under standard assumptions**. c41_065 (`is_are_does`, dual with A1): faint-end slope
  α ~ −2 and non-accelerated UV-density decline integrated to M_trunc = −15. c41_079
  (`commonly_probably`, binding-note nit): stacked high-EW [O III] galaxies show ξ_ion
  **sufficient given high escape fractions**, and independent indicators suggest their escape
  fractions are probably high — sufficiency stays conditional at the source's own hedge. c41_070
  first half (`may_or_can`): observed populations can complete reionization by z~6.
- **Residual tension:** c41_070 second half: matching the large measured Thomson optical depth
  remains a challenge. c41_069 (`reported_only`): the CMB-polarization anchor, z_reion ≈
  10.6 ± 1.2.
- **Escape/production evidence — case-level and indirect only:** c41_003 (`shows_can_occur`):
  non-zero f_esc is necessary to reproduce one case's UV spectrum. c41_041 (`shows_can_occur`):
  β = −2.95±0.20, ≲20 Myr, O/H < 7.8 — conditions that **might** favor leakage. c41_014
  (`is_are_does`): 482-galaxy average spectra, β = −2.3..−2.7, dust-poor and young, bluer with z.
  c41_072 (`may_or_can`): median β ≲ −2.5 at z~8, possibly extremely metal-poor. c41_051
  (`may_or_can`): population link to luminous compacts. Cross-ref: log ξ_ion = 25.2±0.2 at
  460 Myr (c41_013, A5).

**Few-vs-many honesty (frozen question, sub-question 3):** in-corpus support exists only for the
faint-many framing (065/066) plus EW-selected stacks (079). **No entry argues the "bright few
dominate" side — that counterparty is absent from this working corpus** and is named as a gap,
not adjudicated.

**Best evidence with source-strength:** all observational_sample, full_text, single-source per
entry; the escape-fraction rows are the corpus's least direct — one SED-inferred case, one
conditions-based case, one indicator-based stack.

**Measurement dispersion (ledger-carried):** β = −2.3..−2.7 (c41_014) / −2.95±0.20 (c41_041) /
median ≲ −2.5 (c41_072); log ξ_ion = 25.2±0.2 (c41_013); z_reion = 10.6±1.2 (c41_069). *[engine
context: dispersion_v2 f_esc N=64, values 0.02–0.92, S_all=3.9 — the v2 machinery already
promotes f_esc as contested; this corpus's escape evidence is thinner than the engine-wide
spread.]*

**Status:** `emerging_sample_limited`.

**Countercase check:** the τ challenge (070) is the in-corpus counterweight to
sufficiency-under-assumptions; the absent "few" side is declared above.

**What would settle it — honesty required here:** **no entry in this corpus carries a direct
escape-fraction measurement at z ≳ 6; every in-corpus escape statement is inferred or
conditional** (003 SED-inferred; 041 conditions-based; 079 indicator-based). Settlement therefore
requires population-level escape indicators calibrated against direct measurements at accessible
redshifts, applied to EoR samples, plus a re-anchored optical depth. The direct settling
measurement at the epoch itself does not exist in this corpus — and the map does not assert that
it exists elsewhere.

---

## A7 — Budget attribution: is the ionizing/excitation power in the tested high-z objects stellar?

**Boundary axis.** The frozen question rules that Little Red Dots / high-z AGN are IN only
insofar as they bear on the three axes; their intrinsic nature is NOT a fourth axis. These three
entries enter exactly that way: as attribution checks on the budgets the other axes rest on.
This attribution-vs-budget seam is exactly the A7↔A6 boundary that the condensation report's ±1
judgment band (folding A7 into A6) refers to — an attribution check on A6's budgets, not the
forbidden AGN-nature axis.

**Single in-corpus side — AGN disfavored in the tested cases (all `shows_can_occur`, case-grade):**

- c41_050: spatially extended emission and absent N V / [Ne V] rule out an AGN as the dominant
  ionizing source in SGAS J105039.6+001730.
- c41_010: direct Te metallicities (7.91–7.93) are clearly inconsistent with AGN-model
  metallicities in this source, arguing against an AGN.
- c41_005 (tag `debate_countercase`; span stance `qualifies` after v8): diagnostic-diagram
  positions of specific high-z objects are inconsistent with AGN-NLR model tracks.

**Countercase honesty:** no in-corpus entry asserts AGN dominance in any object; the axis is
one-sided by corpus construction (the Step-1 boundary rule filtered LRD-nature papers). Absence
of the pro-AGN side here is a scope fact, not a finding.

**Status:** `emerging_sample_limited`. **Dispersion:** none ledger-carried.

**What would settle it:** the c41_050 method — high-ionization AGN line searches plus spatial
extent — applied systematically to the contested bright/LRD population feeding A1 and A6. The
method exists; the systematic application to the contested population is the missing piece.

---

## Where simulations/models and JWST observations genuinely disagree (frozen question, final clause)

Ledger-grounded disagreement points, each bound to stance-verified entries:

1. **Bright-end over-abundance vs pre-JWST model predictions** — the clearest: c41_074 (`is`),
   c41_076 (candidates, clear tension), c41_004 (holder), c41_078 (reported). Axis A1.
2. **Constant-SFE sufficiency horizon** — consistent to z~12 (c41_011, c41_022, c41_064), tension
   entering at z~15–16 (c41_011) and in clustering space (c41_080, in-model only). Axis A2.
3. **O/Fe vs yield/IMF assumptions** — a reported tension removable by assumption changes
   (c41_031, `may_or_can`). Axis A2.
4. **N/O–C/O anomalies vs massive-star wind yields** — wind-only enrichment excluded without a
   conveyor-belt episode for the named objects (c41_016). Axis A5.
5. **Observed objects vs AGN model tracks** — case-level exclusions (c41_005, c41_010, c41_050).
   Axis A7.

Modality note: items 3–5 are `may_or_can` / case-grade; only items 1–2 rest on `is_are_does` or
`mixed_debated` entries. No disagreement above is stated beyond its carrier's modality.

## Coverage table (every entry, its axis, its ledger enums — byte-copied from the ledger)

| entry | axis(es) | certainty_level | modality | flags |
|---|---|---|---|---|
| c41_001 | A5 | emerging_sample_limited | may_or_can | — |
| c41_002 | A3 | emerging_sample_limited | is_are_does | — |
| c41_003 | A6 | emerging_sample_limited | shows_can_occur | — |
| c41_004 | A1 | actively_debated | mixed_debated | v8 zone/stance reconciliation; debate_countercase |
| c41_005 | A7 | emerging_sample_limited | shows_can_occur | v8 zone/stance reconciliation; debate_countercase |
| c41_006 | A3 | emerging_sample_limited | is_are_does | — |
| c41_007 | A5 | emerging_sample_limited | shows_can_occur | binding-note nit |
| c41_008 | A4 | emerging_sample_limited | is_are_does | — |
| c41_009 | A3 | emerging_sample_limited | may_or_can | — |
| c41_010 | A7 | emerging_sample_limited | shows_can_occur | — |
| c41_011 | A2 | emerging_sample_limited | mixed_debated | tension_reported |
| c41_012 | A3 | emerging_sample_limited | is_are_does | — |
| c41_013 | A5 | emerging_sample_limited | shows_can_occur | — |
| c41_014 | A6 | emerging_sample_limited | is_are_does | — |
| c41_015 | A3 | emerging_sample_limited | is_are_does | — |
| c41_016 | A5 | emerging_sample_limited | is_are_does | binding-note nit |
| c41_017 | A5 | emerging_sample_limited | shows_can_occur | — |
| c41_018 | placeholder (R0) | no_info | is_are_does | — |
| c41_019 | A5 | emerging_sample_limited | shows_can_occur | binding-note nit |
| c41_020 | A4 | emerging_sample_limited | reported_only | — |
| c41_021 | placeholder (R0) | no_info | is_are_does | — |
| c41_022 | A2 | emerging_sample_limited | may_or_can | — |
| c41_023 | A3 | emerging_sample_limited | is_are_does | — |
| c41_024 | A3 | emerging_sample_limited | may_or_can | binding-note nit |
| c41_025 | A5 | emerging_sample_limited | shows_can_occur | — |
| c41_026 | A3 | emerging_sample_limited | shows_can_occur | — |
| c41_027 | A4 | emerging_sample_limited | is_are_does | — |
| c41_028 | A5 | emerging_sample_limited | is_are_does | — |
| c41_029 | A3 | emerging_sample_limited | is_are_does | — |
| c41_030 | A5 | emerging_sample_limited | may_or_can | — |
| c41_031 | A2 | emerging_sample_limited | may_or_can | binding-note nit |
| c41_032 | A3 | emerging_sample_limited | is_are_does | — |
| c41_033 | A3 | emerging_sample_limited | is_are_does | — |
| c41_034 | A3 | emerging_sample_limited | is_are_does | — |
| c41_035 | A3 | emerging_sample_limited | is_are_does | — |
| c41_036 | A4 | emerging_sample_limited | is_are_does | — |
| c41_037 | A3 | emerging_sample_limited | mixed_debated | — |
| c41_038 | A3 | emerging_sample_limited | is_are_does | — |
| c41_039 | A4 | emerging_sample_limited | reported_only | — |
| c41_040 | A4 | emerging_sample_limited | is_are_does | — |
| c41_041 | A6 | emerging_sample_limited | shows_can_occur | — |
| c41_042 | A4 | emerging_sample_limited | mixed_debated | binding-note nit |
| c41_043 | A3 | emerging_sample_limited | is_are_does | — |
| c41_044 | A3 | emerging_sample_limited | is_are_does | — |
| c41_045 | A3 | emerging_sample_limited | is_are_does | — |
| c41_046 | A1 | emerging_sample_limited | may_or_can | — |
| c41_047 | A1 | emerging_sample_limited | reported_only | — |
| c41_048 | A4 | emerging_sample_limited | is_are_does | — |
| c41_049 | A3 | emerging_sample_limited | is_are_does | — |
| c41_050 | A7 | emerging_sample_limited | shows_can_occur | — |
| c41_051 | A6 | emerging_sample_limited | may_or_can | — |
| c41_052 | A4 | emerging_sample_limited | is_are_does | — |
| c41_053 | A4 | emerging_sample_limited | is_are_does | binding-note nit |
| c41_054 | A4 | emerging_sample_limited | is_are_does | — |
| c41_055 | A4 | emerging_sample_limited | is_are_does | — |
| c41_056 | A1 | emerging_sample_limited | is_are_does | — |
| c41_057 | A4 | emerging_sample_limited | is_are_does | — |
| c41_058 | A3 | emerging_sample_limited | may_or_can | — |
| c41_059 | placeholder (R0) | no_info | is_are_does | — |
| c41_060 | A3 | emerging_sample_limited | shows_can_occur | — |
| c41_061 | A3 | emerging_sample_limited | shows_can_occur | — |
| c41_062 | placeholder (R0) | no_info | is_are_does | — |
| c41_063 | A1 | emerging_sample_limited | is_are_does | — |
| c41_064 | A2 | emerging_sample_limited | may_or_can | — |
| c41_065 | A1+A6 | emerging_sample_limited | is_are_does | — |
| c41_066 | A6 | emerging_sample_limited | is_are_does | — |
| c41_067 | A1 | emerging_sample_limited | may_or_can | — |
| c41_068 | A2 | emerging_sample_limited | is_are_does | — |
| c41_069 | A6 | emerging_sample_limited | reported_only | — |
| c41_070 | A6 | emerging_sample_limited | may_or_can | — |
| c41_071 | A1 | emerging_sample_limited | is_are_does | — |
| c41_072 | A6 | emerging_sample_limited | may_or_can | — |
| c41_073 | A2 | emerging_sample_limited | reported_only | — |
| c41_074 | A1 | emerging_sample_limited | is_are_does | — |
| c41_075 | A5 | emerging_sample_limited | is_are_does | — |
| c41_076 | A1 | emerging_sample_limited | mixed_debated | — |
| c41_077 | A4 | emerging_sample_limited | is_are_does | — |
| c41_078 | A1 | emerging_sample_limited | reported_only | — |
| c41_079 | A6 | emerging_sample_limited | commonly_probably | binding-note nit |
| c41_080 | A2 | emerging_sample_limited | in_model_only | — |

80/80 entries accounted: 76 claims mapped (75 `emerging_sample_limited` + 1 `actively_debated`),
4 placeholders excluded by rule R0; 1 declared dual membership (c41_065).

---
Map bound to ledger `as_of` 2026-08-04, sha `e2938298…`; compiled 2026-08-04 14:26 KST. Status labels
bind to the stance-verified census carried by `C41_STANCE_MATRIX.jsonl` +
`VERIFICATION_STATUS_PATCH.jsonl` (76 `verified_consistent` + 4 `verified_no_claim`, zero
failures); the on-disk `verification_status` field is defective per the header disclosure.
