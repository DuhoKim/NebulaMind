# AGN–sSFR association: research-status and debate map

Packet: `FABLE_BURN_P2_SOURCE_LEAD_LEDGER_20260711T010503Z` (companion to `SOURCE_LEAD_LEDGER.json`)
Written: 2026-07-11 (Fable lane B, burn `20260711T010503Z`)
Status of this document: reader-facing reference, built **only from on-disk materials**. Zero network fetches were performed. Every external-literature statement below is a *lead*, not verified evidence, and carries its ledger classification inline. Nothing here is manuscript-ready and nothing here may enter any `candidates/` tree without a separate integrator approval.

Wording note: this map follows the cycle-7 wording contract (`HWAO_GEMINI_WEB_VERDICT_20260711T000400Z.md`): causal/settled verbs are not used for what these statistics do, and absolute quantities that are not commensurable with RP-1's matched-control difference are labeled as such at every mention.

---

## 1. The anchor: what RP-1 itself measured

RP-1's cycle-5 flagship tex is the ground truth for the study's own numbers. Quoted character-for-character from `sources-snapshot/rp1_flagship_polished.tex` (sha256 `63b3920e158ba3be3a78ac0fcf771a979ccf43afe1a8759eda921e1f35ae9384`) — cycles 6 and 7 corrupted this confidence interval by regenerating it, so only this cycle-5 wording may be copied forward:

Line 13 (abstract):

```
the preferred custody-backed comparison yields 8,146 pairs and a median $\Delta\log {\rm sSFR}$ of -1.309 dex, with a bootstrap 95\% confidence interval of [-1.334,-1.283] dex. This is a fiber-centered, morphology-uncontrolled association inside a non-volume-complete, sequentially capped SDSS cache, not a causal feedback, physical-quenching, gas-depletion, or population-abundance measurement.
```

Line 50 (results; defines the estimand):

```
a median $\Delta\log {\rm sSFR}$ (target minus matched control) of -1.309 dex is observed within this fixed-size, morphology-uncontrolled optical denominator and fiber-centered matched comparison.
```

Line 74 (scope):

```
the reported fiber-centered -1.309 dex sSFR offset is an association-only measurement within this fixed-size, morphology-uncontrolled optical denominator and is currently indistinguishable from a morphology, bulge-fraction, or aperture-sampling association. Its provenance-retained result is the preferred 8,146-pair, -1.309 dex offset with bootstrap 95\% interval [-1.334,-1.283] dex.
```

Plain reading, staying inside the tex's own framing [VERIFIED_LOCAL — ledger V01]:

- **Quantity:** median Δlog sSFR, *target minus matched star-forming control* — a matched-pair **difference** in log space, not an absolute sSFR, not a surface density, not a population abundance.
- **Value:** `-1.309` dex; bootstrap 95% interval `[-1.334,-1.283]` dex; 8,146 pairs.
- **Character:** association-only, morphology-uncontrolled, fiber-centered (SDSS 3-arcsec fiber, `1.2--6.5 kpc` across the window per tex line 25), selection-limited (four-line S/N≥3 BPT cut [VERIFIED_LOCAL — V04]), denominator-bound (fixed 60,000-galaxy DR17 cache, `0.02<z<0.12` [VERIFIED_LOCAL — V02]), sSFR proxy = MPA-JHU-style `specsfr_tot_p50` [VERIFIED_LOCAL — V03].
- **What the tex itself rules out:** reading the offset as causal feedback, physical quenching, gas depletion, or a population-abundance statement (tex lines 13, 19, 70).

**Do not compare `-1.309 dex` numerically to any published absolute sSFR, SFR, surface density, or quenching threshold.** It is a matched-control difference inside a specific capped denominator. Cross-study raw-value comparisons of this number were retracted in the rejected cycle-7 sidecar report and are classified REJECTED in the ledger (R02, R03, R06).

## 2. Where the question stands

The question RP-1 addresses (tex line 19): do broad optical BPT-selected galaxies have lower catalog median sSFR proxy than mass–redshift matched star-forming controls, inside a fixed low-redshift SDSS denominator? RP-1 reports: yes, by the matched-pair median above, with the association-only caveats built into the wording.

Around that narrow question sits a wider, genuinely unsettled literature. The cycle-7 Gemini Web sidecar report surveying that literature was **rejected** (`REJECTED_RETAIN_VERIFIED_SOURCE_LEADS_ONLY`); what survives from it is a set of *source leads*, five of which were retained after supervised link/abstract checks, all still pending full verification. Their claims are mapped below with status labels. A claim's presence here means "the literature appears to say this, pending verification" — not that it is settled.

## 3. The retained external leads (status inline)

1. **Ellison et al. (2016)** [NEEDS_NETWORK_VERIFICATION — N01] — lead: optically selected AGN hosts show a median global ΔSFR of `-0.06 dex` relative to matched controls. *Label: global-aperture matched-control SFR offset — different aperture and metric from RP-1's fiber-centered Δlog sSFR; not commensurable as raw values.* The raw sidecar report misquoted this as `-0.12 dex / 25 percent`; that figure is retracted [REJECTED — R01].
2. **Cid Fernandes et al. (2010/2011), arXiv:1012.4426** [NEEDS_NETWORK_VERIFICATION — N07] — lead: the WHAN diagram separates weakly accreting AGN from "retired galaxies" ionized by hot evolved low-mass stars, with a `W_Hα = 3 Å` boundary. Bears on how much of any broad optical AGN class is contaminated by non-accreting systems. RP-1's tex already cites this work for exactly that contamination risk (tex line 22).
3. **Gawade (2025), arXiv:2512.22268** [NEEDS_NETWORK_VERIFICATION — N05; 2025 preprint, unrefereed] — lead: green-valley median log10 sSFR of `-14.85 dex` in IllustrisTNG (pile-up at an imposed SFR floor) versus `-11.71 dex` in EAGLE (broad continuous distribution). *Label: absolute simulation medians — not commensurable with RP-1's matched-control difference as raw values.*
4. **Simard et al. (2011) / Mendel et al. (2014), VizieR `J/ApJS/196/11`** [NEEDS_NETWORK_VERIFICATION — N09] — lead: PSF-convolved bulge+disk decompositions for `1,123,718` SDSS DR7 galaxies (B/T, Sérsic indices). This is the concrete path to the morphology control RP-1 currently lacks.
5. **SDSS-V SPIDERS** [NEEDS_NETWORK_VERIFICATION — N11] — lead: optical spectroscopic follow-up of eROSITA X-ray sources. The program description held up in the supervised check; the claimed overlap with RP-1's exact `0.02<z<0.12` denominator did **not** and remains the specific thing a network pass must test.

Additional linked leads captured but not among the retained five: Gatto et al. (2025) nuclear values [N03/N04], Piotrowska et al. (2022) [N08], Tempel et al. (2014) [N10]. Unlinked leads (Schawinski 2014/2015, Brinchmann 2004, Salim 2007, Kewley 2005, Hickox 2014, Yang 2007, xCOLD GASS/Saintonge 2017, ALFALFA, MaNGA, TNG/EAGLE project claims) are `UNCITED_NOT_USABLE` in the corrected sidecar output and sit in the ledger as U01–U26, all [NEEDS_NETWORK_VERIFICATION].

## 4. Debate map

Each debate is stated as a genuinely open question, with the leads that bear on it. No side is settled by anything on local disk.

### D1 — Sign and size: is optical-AGN star formation suppressed, and by how much?

- Ellison et al. (2016) lead: global median ΔSFR `-0.06 dex` for optically selected AGN [N01] — a small global deficit. *Global matched-control SFR offset; not commensurable with RP-1's value as raw numbers.*
- Gatto et al. (2025) lead: nuclear (2.5-arcsec) stellar-population SFR measure of `-1.34 dex` (AGN) vs `-1.55 dex` (controls) — i.e. AGN *higher* by `+0.21 dex` in the nucleus [N03]. *Absolute nuclear values from an IFU sample — not commensurable with RP-1's matched-control difference.*
- The same Gatto lead (raw report only) has both AGN and controls sitting below the star-forming main sequence globally [N04].

Open question: the sign of the association flips between apertures and methodologies in these leads (small global deficit; nuclear excess; RP-1's large fiber-centered matched-pair deficit on a catalog proxy). Whether these describe one population seen through different apertures/estimators, or different selection effects, is unresolved — and unresolvable from local disk.

### D2 — Physics or aperture: what does a fiber-centered deficit mean?

- RP-1's tex states the offset is "currently indistinguishable from a morphology, bulge-fraction, or aperture-sampling association" (tex line 74) [VERIFIED_LOCAL].
- Kewley et al. (2005) lead: a ~20 percent minimum fiber covering fraction is needed for fiber metrics to approximate global values, placing low-redshift fiber measurements on bulge-dominated scales [U04/U11/U20 — uncited in the sidecar report].
- MPA-JHU pipeline lead: for AGN hosts the pipeline substitutes Dn(4000)-based fits for emission-line SFRs, which the raw report argues biases bulge-dominated AGN hosts low [U19 — uncited; the highest-value verification target in the U-set, since RP-1's proxy is `specsfr_tot_p50` (V03)].
- Simard/Mendel decompositions [N09] are the retained path to testing this: rerun the match with structural controls and see whether the offset persists, shrinks, or disappears.

Open question: how much of `-1.309` dex survives morphology/aperture control. RP-1's wording already treats this as undetermined; the sidecar report's attempt to answer it causally was retracted [R04].

### D3 — Instantaneous accretion vs integrated history

- Piotrowska et al. (2022) lead: central-galaxy quenching is predicted far better by integrated supermassive black hole mass than by instantaneous accretion output; uses a global quenching threshold of `sSFR < -11.0 dex` [N08]. *Absolute global threshold — not commensurable with RP-1's matched-control difference.*
- Duty-cycle leads: accretion varies on `0.1–10 Myr` timescales while optical SFR tracers integrate over `100 Myr–1 Gyr` [U12/U21 — uncited], making single-epoch BPT state a temporally narrow flag.

Open question: whether any single-epoch optical AGN flag can carry information about quenching at all, versus merely marking where gas currently reaches the nucleus. RP-1's association-only framing is compatible with either answer.

### D4 — Who is in the denominator: selection and contamination

- RP-1's four-line S/N≥3 cut biases its denominator against emission-weak passive systems — RP-1's own tex says so (tex line 19) [VERIFIED_LOCAL — V04].
- Cid Fernandes WHAN lead [N07]: retired galaxies masquerade as weak AGN in BPT space; unfiltered, they would drag an "AGN" sample's median sSFR downward.
- SPIDERS lead [N11]: X-ray selection could provide an AGN sample less tied to optical line detectability — but its overlap with RP-1's exact denominator is precisely the unverified part.

Open question: how much of the measured association is created or inflated by who gets excluded (emission-weak systems) and who gets misclassified (retired galaxies). The sidecar's "What remains unknown" section framed this as the denominator-bias question; the ledger keeps it a question, not a finding.

### D5 — Simulations do not agree with each other

- Gawade (2025) lead [N05, preprint]: green-valley medians of `-14.85 dex` (TNG, floor pile-up) vs `-11.71 dex` (EAGLE, continuous). *Absolute simulation medians — not commensurable with RP-1's matched-control difference.*

Open question: with subgrid feedback implementations producing multi-dex disagreements between major simulations for the same population, simulation anchoring of any observed association is itself unsettled. Selection-matched mock comparisons (RP-1 tex line 75 lists them among missing observables) remain future work.

## 5. Common misreadings this map is designed to prevent

1. **Comparing `-1.309 dex` to `-0.06 dex` and concluding RP-1's effect is ~20× stronger.** Different estimands (fiber-centered catalog-proxy matched difference vs global SFR offset), different apertures, different metrics. The numbers are not commensurable as raw values [contract rule 2; R03].
2. **Comparing `-1.309 dex` to `-1.34/-1.55 dex` (Gatto) and calling them "close".** Coincidence of magnitude between a matched-pair difference and absolute nuclear values; the sidecar report made this comparison and it is retracted [R02].
3. **Reading the association causally** ("AGN quenches its host", "feedback clears gas", or any statement that the statistic settles aperture dependence, bulge dominance, or fueling). Retracted wording family [R04]; RP-1's tex forbids this reading in its own text.
4. **Treating the sidecar report's prose as citable literature.** The report is rejected; only ledger-tracked leads survive, and every one of them still requires the later, separately approved verification pass.

## 6. Verification queue implied by this map (all GATED — not runnable in this packet)

In priority order for a later, Duho-approved network pass:

1. N01 Ellison `-0.06 dex` (headline external anchor; also documents the R01 misquote).
2. U19 MPA-JHU AGN-host Dn(4000) substitution (bears directly on RP-1's own proxy).
3. N09 Simard/Mendel catalog fields and row count (unlocks the D2 morphology-control test).
4. N07 Cid Fernandes WHAN boundary wording (`= 3 Å` vs `> 3 Å`).
5. N05 Gawade preprint values and status (pin version; unrefereed).
6. N11 SPIDERS–denominator overlap (the specifically unsupported feasibility claim).
7. N08 Piotrowska predictor result and threshold usage.
8. Remaining N- and U-entries per `SOURCE_LEAD_LEDGER.json`.

---

*Companion files: `SOURCE_LEAD_LEDGER.json` (full lead-by-lead ledger with hashes), `PRIOR_WORK_COMPARISON_CANDIDATE.md` (candidate comparison section, integrator-gated). Source snapshots and hashes: `sources-snapshot/`.*
