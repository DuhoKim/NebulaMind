# gemini-agy-deep-cycle-7
Started UTC: 2026-07-09T03:41:45Z
CWD: /Users/duhokim/NebulaMind/NebulaMind

GEMINI_AGY_DEEP_REVIEW_CYCLE_07

## 1. Overview & Executive Summary

This deep-review report covers the Cycle 7 quality sprint candidates: the polished flagship paper (RP-1) and the supplementary denominator/proxy atlas. Both drafts have been reviewed from the perspective of a skeptical journal reviewer. While the authors have introduced several valuable guardrails (e.g., explicitly stating that these are optical associations rather than physical feedback measurements), several subtle risks, citation-role ambiguities, and potential denominator-to-physics misinterpretations remain.

---

## 2. Key Issues & Risk Log

### Issue 1: Over-reliance on "Seyfert-like" and "Broad BPT AGN" nomenclature without physical confirmation
* **Severity**: Major
* **Risky Sentence (Flagship, Sec 1)**: 
  > "For that reason the paper uses the phrase 'broad optical BPT AGN' and treats stronger Seyfert-like cuts as a sensitivity check rather than as an interchangeable label."
* **Paraphrase of Risk**: Defining a group as "broad optical BPT AGN" primarily via emission line ratio cuts (S/N or Kewley boundaries) risks leading the reader to assume these are confirmed accretion-powered objects, even when acknowledging LINER/retired galaxy contamination.
* **Safer Replacement Wording**: 
  > "For that reason, this paper designates the sample as 'optically selected BPT emission-line sources' and treats high-excitation/Seyfert-like cuts as sensitivity checks to examine the impact of non-accretion contamination (e.g., LINER-like emission from retired stars)."

---

### Issue 2: Environmental Ordinal Rank vs. Local Density Interpretation
* **Severity**: Major
* **Risky Sentence (Supplement, Sec 3.1)**:
  > "Within this selection-biased emission-line denominator, the relative 10th-neighbor index covaries with the catalog low-sSFR fraction; this index is only an internal ordinal rank..."
* **Paraphrase of Risk**: The correlation shown in Figure 1 and Section 3.1 between "low-sSFR fraction" and "10th-neighbor rank" can easily be misconstrued by readers as a physical environmental quenching effect, despite the caveat text. An ordinal rank in a highly incomplete (24%) and biased denominator does not map to any standard cosmic environment.
* **Safer Replacement Wording**:
  > "Within this capped, 24% complete emission-line subset, the internal ordinal rank of 10th-neighbor distances exhibits a statistical association with the low-sSFR catalog fraction. This ordinal rank is a relative sample metric and does not correspond to physical environmental volume densities or dark matter halo regimes."

---

### Issue 3: H-alpha Luminosity Proxy vs. Star-Formation Rate
* **Severity**: Major
* **Risky Sentence (Supplement, Sec 3.7)**:
  > "The median H-alpha luminosity proxy is 0.66 dex lower than in massive star-forming emission-line galaxies."
* **Paraphrase of Risk**: Describing $\rm H\alpha$ luminosity as a "proxy" for gas depletion without matching for morphology or aperture fraction is highly misleading. In bulge-dominated galaxies, central $\rm H\alpha$ can be dominated by retired stellar populations rather than active star formation or cold gas properties.
* **Safer Replacement Wording**:
  > "The median catalog-derived $\rm H\alpha$ luminosity parameter is 0.66 dex lower than in the massive star-forming comparison group. This difference reflects line emission within the central 3-arcsec fiber and must not be used to infer global star-formation rates or cold-gas depletion times."

---

### Issue 4: Massive Bins Selection-Function Artifact Warning
* **Severity**: Minor
* **Risky Sentence (Supplement, Sec 3.5)**:
  > "The first stellar-mass bin with low-sSFR fraction above 0.5 is $\log(M_\star/M_\odot) \in [11.0,12.5]$. The optical AGN fraction peaks in the 11.0-12.5 bin at 0.520."
* **Paraphrase of Risk**: A reader skimming Figure 5 might assume the 11.0–12.5 dex bin represents a physical transition mass for AGN feedback, when in reality, the emission line S/N requirement systematically eliminates passive galaxies in that mass range, creating a highly skewed survivor cohort.
* **Safer Replacement Wording**:
  > "Due to the S/N requirements of the emission-line denominator, massive passive galaxies are preferentially excluded. As a result, the surviving sample exhibits an artificial concentration of low-sSFR and BPT classifications in the $\log(M_\star/M_\odot) \in [11.0,12.5]$ bin, which must not be interpreted as a physical transition threshold or representative population abundance."

---

## 3. Citation Role Audit

Several citations in both drafts are used in a dense bundle that risks conflating method support (i.e., how the data was analyzed) with future-data motivation (i.e., what data is missing).

* **Citation Bundle**: `\citep{best2005,dekel2006,fabian2012,heckmanbest2014,lamassa2013,mcnamara2007,veilleux2005,xcoldgass2017,xgass2018,cicone2014,carniani2017,fiore2017,simba2019,tng2019,eagle2015,peng2010,piotrowska2022,wetzel2013}`
* **Flagged Behavior**: In **Section 6** of the flagship draft, this mega-bundle is cited to motivate missing observables. However, this conflates very different physical regimes (e.g., radio-jet coupling, molecular gas fractions, cosmological hydro-simulations, and environmental satellite quenching).
* **Correction**: Split the citations to explicitly target each missing observable category. Do not group them into a single parenthetical block. For example:
  * *Radio/X-ray Mode*: `\citep{best2005, fabian2012, mcnamara2007}`
  * *Molecular/Neutral Gas*: `\citep{xcoldgass2017, xgass2018}`
  * *Outflow/Kinematics*: `\citep{cicone2014, veilleux2005}`
  * *Simulations*: `\citep{simba2019, tng2019, eagle2015}`

---

## 4. Missing Observables Checklist

For any follow-up papers or revisions seeking to transform these baseline denominators into physical results, the following datasets are strictly required:

| Section / Topic | Missing Observables Required | Status in Candidate |
| :--- | :--- | :--- |
| **3.1 Environment** | Group/cluster catalogs, spectroscopic fiber-collision corrections, central/satellite labels. | **Missing** (SDSS 10th-neighbor proxy only) |
| **3.2 Maintenance Heating** | X-ray cavity/cooling luminosities, radio jet powers, halo-selected catalogs. | **Missing** (SDSS optical BPT only) |
| **3.3 Outflows** | Spatially resolved kinematics (IFU), multiphase (neutral/molecular) outflow tracer lines. | **Missing** (Single fiber catalog sSFR only) |
| **3.5 Transition Mass** | Complete volume-limited sample (not capped at 60k), morphology, and aperture corrections. | **Missing** (Arbitrary pilot cap + fiber bias) |
| **3.7 Gas Depletion** | $\rm CO(1-0)$ or dust-based molecular gas masses ($M_{\rm H2}$), matching global SFRs. | **Missing** (Central catalog sSFR and $\rm H\alpha$ proxy only) |
| **3.8 Simulations** | Synthetic observations generated via matching 3-arcsec fiber apertures and BPT S/N selection. | **Missing** (Direct parameter comparison only) |

---

## 5. Concrete Integrator Actions

Below is the prioritized list of text modifications and metadata tasks:

1. **[Priority 1 - Flagship & Supplement] Split the Mega-Citation Bundle**: Separate the references in Section 6 (Flagship) and Section 3 (Supplement) into specific subsections mapping directly to the missing observables (e.g., group catalogs, radio jets, cold gas, and cosmological simulations).
2. **[Priority 2 - Flagship Abstract & Sec 4] Amplify Aperture/Bulge Bias Caveats**: Explicitly mention that because the control sample is not matched in morphology, the $\Delta\log\text{sSFR}$ offset is likely inflated by the bulge-to-total ($B/T$) ratio differences.
3. **[Priority 3 - Supplement Sec 3.5] Add Warning on Selection Cut Artifacts**: Revise the text to emphasize that the high-mass BPT fraction peak is a direct consequence of the S/N selection cut excluding passive galaxies, rather than a physical transition.

---

## 6. Safety Ledger

* **Read-only execution**: Checked. No local files were edited, and no code execution was requested.
* **No public footprint**: Checked. No public sites, live APIs, git branches, or wikis were modified or accessed.
* **No billing/credentials**: Checked. No database or cloud infrastructure tools were run.


# command_result
exit_code=0
elapsed_s=16.1
timed_out=False
finished_utc=2026-07-09T03:42:01Z
