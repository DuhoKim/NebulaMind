# CANDIDATE (reference block only): Quantitative comparison to prior work

> **GATE — READ FIRST.** This is a *candidate/reference* section drafted to address the recurring cycle-audit blocker `missing explicit quantitative comparison to prior work`. It is **not approved for any manuscript, candidate package, or `candidates/` tree**. Placing it anywhere downstream requires (1) the separately approved network verification pass over the `NEEDS_NETWORK_VERIFICATION` leads it cites, and (2) a separate integrator approval. Produced by Fable lane B, burn `20260711T010503Z`, from on-disk materials only; zero network fetches.

Ledger: `SOURCE_LEAD_LEDGER.json` (`FABLE_BURN_P2_SOURCE_LEAD_LEDGER_20260711T010503Z`). RP-1 numerals below are verbatim from `sources-snapshot/rp1_flagship_polished.tex` (sha256 `63b3920e158ba3be3a78ac0fcf771a979ccf43afe1a8759eda921e1f35ae9384`), the cycle-5 ground truth; cycles 6/7 corrupted the confidence interval by regenerating it, so the interval must be copied character-for-character from cycle 5: `[-1.334,-1.283]`.

Inclusion rule (fail-closed): a prior-work number appears below **only if an on-disk record beyond the rejected sidecar report itself supports it** — i.e. the five retained leads, whose values carry supervised abstract/page-level attestations in `JOURNAL_CYCLE7_GEMINI_WEB_20260710T232711Z_TORI_PRELIMINARY.md` and the integration verdict. Linked leads without any such attestation of their *values* (Gatto et al. 2025 nuclear values, Piotrowska et al. 2022 threshold, Tempel et al. 2014 details) are **excluded** from the comparison rows and listed in §4. Every row carries its ledger status; nothing in this section is verified evidence yet.

---

## 1. Candidate section text

*(Draft prose for a future "Comparison to prior work" subsection. Bracketed status tags travel with the text and must not be stripped until the network pass upgrades the corresponding ledger entries.)*

The result of this pilot is a median $\Delta\log {\rm sSFR}$ (target minus matched control) of -1.309 dex, with a bootstrap 95\% confidence interval of [-1.334,-1.283] dex, over 8,146 matched pairs — an association-only, morphology-uncontrolled, fiber-centered offset inside a fixed, selection-limited SDSS DR17 denominator. Because this is a matched-pair difference of a fiber-based catalog proxy, it is not numerically interchangeable with global offsets, absolute sSFR values, or quenching thresholds reported elsewhere; the comparisons below are therefore framed per estimand, and absolute quantities are labeled as non-commensurable with our statistic.

The nearest methodological relative in the retained literature leads is the matched-control comparison of Ellison et al. (2016) [NEEDS_NETWORK_VERIFICATION — ledger N01], for which the indexed abstract reports a median global $\Delta$SFR of -0.06 dex for optically selected AGN relative to matched controls. Both that measurement and ours are matched-control differences, and both find the AGN-classified population offset downward; the two numbers are nonetheless not commensurable as raw values, differing in aperture (global versus 3-arcsec fiber), in metric (SFR versus catalog sSFR proxy), and in control variables (Ellison et al. additionally match local density, which our pilot does not). We therefore read the Ellison et al. lead as a directional cousin under a different estimand, not as a scale reference for our offset. An earlier sidecar figure of -0.12 dex / 25 percent attributed to this work was a misquote and is retracted [REJECTED — ledger R01]; it must not be cited.

At the opposite end of the estimand space, simulation green-valley medians quoted by Gawade (2025) [NEEDS_NETWORK_VERIFICATION — ledger N05; 2025 preprint, unrefereed] — median $\log_{10}$ sSFR of -14.85 dex for IllustrisTNG centrals piling up at an imposed SFR floor, versus -11.71 dex for EAGLE's continuous distribution — are absolute simulation quantities [non-commensurable with our matched-control difference as raw values]. Their relevance to this pilot is not numeric but structural: the multi-dex disagreement between major simulations for the same transitioning population indicates that no single simulated sSFR scale currently anchors an observed association of our type, and that a selection-matched mock comparison (listed among this paper's missing observables) is required before any simulation-based reading of our offset.

Two further retained leads bound the *interpretation* rather than the magnitude of our offset. The WHAN diagnostic of Cid Fernandes et al. (2010/2011) [NEEDS_NETWORK_VERIFICATION — ledger N07], with its $W_{H\alpha} = 3$ Å boundary attested at abstract level, marks the contamination channel — retired galaxies ionized by evolved stars masquerading as weak AGN — that our broad optical BPT selection cannot exclude; any quantitative re-filtering of our denominator by WHAN class is future work gated on full verification of that boundary. The Simard et al. (2011) / Mendel et al. (2014) VizieR catalog `J/ApJS/196/11` [NEEDS_NETWORK_VERIFICATION — ledger N09], attested at page level to cover 1,123,718 SDSS DR7 galaxies with PSF-convolved bulge+disk decompositions, defines the concrete route to the morphology-controlled rerun that our own scope section identifies as the decisive next test of the offset's origin. SDSS-V SPIDERS [NEEDS_NETWORK_VERIFICATION — ledger N11] is retained only as a program-level lead toward an X-ray-selected cross-check of our optical denominator; its overlap with our exact $0.02<z<0.12$ window is specifically unverified and is quoted here as a question, not a capability.

## 2. Comparison table (candidate)

| Prior-work lead | Quantity (as attested on disk) | Estimand / aperture | Commensurability with RP-1's -1.309 dex matched-control difference | Ledger status |
|---|---|---|---|---|
| **RP-1 (this work, cycle-5 tex)** | median Δlog sSFR = `-1.309` dex; bootstrap 95\% interval `[-1.334,-1.283]` dex; `8,146` pairs | matched-pair difference; catalog sSFR proxy (`specsfr_tot_p50`); 3-arcsec fiber; `0.02<z<0.12` | anchor row | VERIFIED_LOCAL (V01–V04) |
| Ellison et al. (2016) | median global ΔSFR = `-0.06` dex (optically selected AGN vs matched controls) | matched-control difference; global SFR; SDSS optical selection | same *family* (matched-control difference); **not commensurable as raw values** (aperture and metric differ) | NEEDS_NETWORK_VERIFICATION (N01); misquoted `-0.12 dex` variant REJECTED (R01) |
| Gawade (2025), arXiv:2512.22268 | green-valley median log10 sSFR: TNG `-14.85` dex; EAGLE `-11.71` dex | **absolute** simulation medians; global | **non-commensurable absolute quantities** — context only | NEEDS_NETWORK_VERIFICATION (N05); preprint, unrefereed |
| Cid Fernandes et al. (2010/2011), arXiv:1012.4426 | WHAN boundary `W_Hα = 3 Å` (weak AGN vs retired galaxies) | classification boundary, not an sSFR offset | not a comparison quantity; bounds denominator contamination | NEEDS_NETWORK_VERIFICATION (N07) |
| Simard et al. (2011) / Mendel et al. (2014), VizieR `J/ApJS/196/11` | `1,123,718` SDSS DR7 galaxies with bulge+disk decompositions | catalog scale, not an sSFR offset | not a comparison quantity; enables the morphology-controlled rerun | NEEDS_NETWORK_VERIFICATION (N09) |
| SDSS-V SPIDERS | (no number retained; program description only) | X-ray-selected AGN follow-up program | qualitative selection cross-check; denominator overlap unverified | NEEDS_NETWORK_VERIFICATION (N11) |

## 3. Wording constraints carried by this section

- No causal or settled-verb framing anywhere ("establishes", "confirms", "demonstrates", "proves", "settles" and equivalents are prohibited for what these statistics do) — per the cycle-7 wording contract.
- Every absolute quantity above is labeled non-commensurable with RP-1's matched-control difference; the labels are part of the text and may not be edited out.
- RP-1 numerals must be copied from the cycle-5 tex character-for-character: `-1.309`, `[-1.334,-1.283]`, `8,146`.
- Status tags `[NEEDS_NETWORK_VERIFICATION — ledger …]` remain in the prose until the corresponding ledger entry is upgraded by the approved network pass; only then may an integrator convert them to normal citations.

## 4. Explicitly excluded from the comparison (fail-closed)

- **Gatto et al. (2025)** nuclear values (`-1.34`/`-1.55` dex, `+0.21` dex): linked in the rejected report but with **no on-disk attestation of the values** (ledger N03/N04); additionally, the raw report's claim that they are "highly commensurable" with our statistic is retracted (R02). Eligible for a future revision of this section only after network verification, and then only with non-commensurability labels.
- **Piotrowska et al. (2022)** threshold (`-11.0` dex) and predictor result: link resolves, values unattested on disk (N08); raw-value comparison retracted (R03).
- **Tempel et al. (2014)** filament-catalog details (N10): value-level support absent on disk; feasibility material, not comparison material.
- **All 26 `UNCITED_NOT_USABLE` leads** (U01–U26): no usable citation exists yet.
- **Every retracted claim** (R01–R07), including the `-0.12 dex` Ellison figure, all raw-value commensurability claims, causal wording, and the raw report's `6.7 kpc` fiber-scale figure (RP-1's tex states `1.2--6.5 kpc`).

> **Repeat gate:** candidate/reference block only. Not for `candidates/`, not for the manuscript, not for the wiki, until the gated network pass and a separate integrator approval both occur.
