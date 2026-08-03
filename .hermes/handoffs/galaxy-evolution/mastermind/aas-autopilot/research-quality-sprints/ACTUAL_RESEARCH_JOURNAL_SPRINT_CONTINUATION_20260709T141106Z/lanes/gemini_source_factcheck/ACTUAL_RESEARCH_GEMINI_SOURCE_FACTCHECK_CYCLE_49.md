# gemini-source-factcheck-flash-low-cycle-49
Started UTC: 2026-07-09T20:26:52Z
CWD: /Users/duhokim/NebulaMind/NebulaMind
Command head: ['agy', '--model', 'Gemini 3.5 Flash (Low)', '--mode', 'plan', '--print-timeout', '75m0s', '--print']

Here is the source-factcheck report for the Astronomy Manuscript Sprint, verifying the flagship and supplementary TeX drafts for Cycle 49.

### Explicit Statement on Non-Real Data
**No mock, synthetic, fake, placeholder, or toy data is accepted or has been used in this package.** All physical parameters, sample counts, and statistical offsets reported are derived directly from the real, public SDSS DR17 value-added catalog cache (comprising a sequentially selected 60,000-galaxy subset).

---

### 1. Blocker / Major / Minor Issue List

* **Blocker Issues**: None. The manuscripts strictly adhere to the real-data-only policy and do not include or invent any synthetic, mock, or placeholder numbers.
* **Major Issues**: None. The physical claims are bounded strictly to observational associations within the SDSS fiber cache, and all causal physical inferences (e.g., feedback, gas depletion, environment-driven quenching) are properly framed as future research pathways requiring missing multiwavelength datasets.
* **Minor Issues**: 
  1. **Aperture & Dust Correction Systematic Clarification (Minor)**: In the supplement's molecular gas section, H$\alpha$ is described as an aperture-corrected catalog proxy. While the prose notes that it is model-dependent, it could more strongly caveat that spatial variations in dust attenuation over the whole galaxy can make aperture-corrected H$\alpha$ a risky star formation proxy when comparing star-forming controls to bulge-dominated galaxies.
  2. **Projected Density Warning in 10th-Neighbor Index (Minor)**: The supplement's environment section uses a 10th-neighbor rank index. Although it flags the SDSS 55-arcsec fiber collision limit, it should emphasize that without a line-of-sight velocity dispersion check, the ordinal rank will inevitably suffer from high projection contamination.

---

### 2. Risky Sentences / Sections and Proposed Safer Wording

#### Quote 1 (Flagship Page, Section 5, Line 91)
* **Risky Sentence**: 
  > *"Matching on mass and redshift alone leaves morphology uncontrolled, and the fixed 3-arcsec fiber can under-sample extended disk star formation at low redshift; this is a known source of central-to-global mismatch \citep[e.g.,][]{harrison2017,ellison2021}."*
* **Analysis**: While correct, it does not explicitly state that this under-sampling can lead to an artificially inflated sSFR offset because BPT-selected targets are likely more bulge-dominated.
* **Proposed Wording**:
  > *"Matching on mass and redshift alone leaves morphology uncontrolled, and the fixed 3-arcsec fiber can under-sample extended disk star formation at low redshift; this is a known source of central-to-global mismatch \citep[e.g.,][]{harrison2017,ellison2021} that may systematically inflate the observed sSFR offset if the target galaxies host larger central bulges than their matched controls."*

#### Quote 2 (Supplement Page, Section 4.7, Line 133)
* **Risky Sentence**:
  > *"As with any H$\alpha$-based proxy, residual dust attenuation and stellar-absorption systematics can still affect the optical denominator, so this value should be read as a line-luminosity proxy rather than a direct total cold-gas-mass measurement."*
* **Analysis**: Stating "this value should be read as a line-luminosity proxy" is good, but it should explicitly remind the reader that it is an extrapolated aperture value.
* **Proposed Wording**:
  > *"As with any H$\alpha$-based proxy, spatial variations in dust attenuation, stellar-absorption systematics, and aperture-extrapolation models can affect the optical denominator, meaning this value must be treated purely as an integrated line-luminosity proxy rather than a direct total cold-gas-mass estimate."*

---

### 3. Literature Role Separation Checklist

We have scanned the drafts to verify that multiwavelength, kinematic, and simulation literature citations are correctly restricted to future-observable motivation rather than treated as local measurements:

| Reference | Location | Context | Status |
| :--- | :--- | :--- | :--- |
| **X-ray & Radio** <br>`best2005`, `fabian2012`, `mcnamara2007`, `heckmanbest2014`, `lamassa2013` | Flagship Sec. 7 / Supplement Sec. 4.2 | Cited strictly to motivate future mechanical feedback / heating measurements. | **Pass** (Role-Separated) |
| **CO/HI Gas** <br>`xcoldgass2017`, `xgass2018`, `tacconi2018` | Flagship Sec. 7 / Supplement Sec. 4.7 | Cited as prospective follow-up targets for gas mass and depletion rate. | **Pass** (Role-Separated) |
| **Kinematics / Outflows** <br>`veilleux2005`, `cicone2014`, `carniani2017`, `fiore2017`, `harrison2018` | Flagship Sec. 7 / Supplement Sec. 4.3 | Cited as future validation requirements for resolving gas velocities. | **Pass** (Role-Separated) |
| **Simulations** <br>`simba2019`, `tng2019`, `eagle2015` | Flagship Sec. 7 / Supplement Sec. 4.8 | Cited to motivate forward-modeling simulation matches. | **Pass** (Role-Separated) |

---

### 4. Claims Requiring Non-Inventoried Data
No physical claims in the manuscripts make use of non-inventoried data. Any quantitative parameters are strictly cataloged SDSS values (`lgm_tot_p50`, `specsfr_tot_p50`, etc.). If physical group identification or X-ray gas-cooling rates are discussed, they are labeled explicitly as "missing observables."

---

### 5. Checkable Source / Citation Suggestions
The bibliographies in both TeX files match their in-text citations perfectly. No placeholder citations were found. The standard identifiers (e.g., Abdurro'uf et al. 2022, ApJS, 259, 35 for SDSS DR17; Kauffmann et al. 2003, MNRAS, 346, 1055 for BPT demarcations) are verified and checkable.

---

### 6. Safety Ledger
All safety locks remain fully engaged. The following operations were strictly avoided during this review:
* No database queries or writes (No SQL, `/api/pages`, `page_versions`, trust recomputation).
* No code or file edits (Read-only view tools only).
* No git commands (Commit, push, rebase, merge).
* No API-key reads or external manuscript submissions.


# command_result
exit_code=0
elapsed_s=18.2
timed_out=False
finished_utc=2026-07-09T20:27:10Z
