# hwao-agy-low-cycle-43
Started UTC: 2026-07-09T19:41:05Z
CWD: /Users/duhokim/NebulaMind/NebulaMind
Command head: ['agy', '--model', 'Gemini 3.1 Pro (Low)', '--mode', 'plan', '--print-timeout', '75m0s', '--print']

ACTUAL_RESEARCH_HWAO_DIRECTOR_CYCLE_43

### 1. Publication-Readiness Verdict

**RP-1 Flagship:** NOT READY for publication as a causal physical-mechanism paper, but ALMOST READY as an association-only pilot or research note. The manuscript strictly and repeatedly caveats the lack of morphological/structural controls (e.g., `fracDeV`, concentration index) and aperture effects. Because these structural proxies were not cached, the reported -1.309 dex sSFR offset cannot be disentangled from the known bulge-fraction/mass correlation. It must remain explicitly framed as a selection-limited, fixed-size optical baseline.

**Supplementary Denominator/Proxy Atlas:** ALMOST READY as a data-release/catalog note, provided it is marketed strictly as a follow-up checklist and observational baseline. The atlas is highly repetitive with its caveats (which is safe, but stylistically dense) and successfully avoids making unsupported physical claims about environment, maintenance heating, or outflows without the required multiwavelength data.

---

### 2. Top 12 Concrete Quality Improvements (Ranked by Scientific Value)

1. **Explicit Causal Disclaimer in Abstract (Flagship):** Add a single sentence to the abstract explicitly stating that the observed offset cannot be used to confirm or refute AGN feedback or quenching models due to the missing structural controls.
2. **Clarify the "Fixed-Size 60,000-Galaxy" Limitation (Flagship):** Specify exactly why the cache was capped at 60,000 (e.g., computational limit, database timeout, arbitrary pilot choice) to prevent readers from assuming it is a statistically rigorous sub-sampling.
3. **Consolidate Repetitive Caveats (Supplement):** The supplement repeats the exact same missing observables and selection-bias caveats (e.g., "55-arcsec fiber-collision limit", "strict four-line S/N>=3 parent") in almost every subsection. Consolidate these into the "Shared denominator limitations" section and reference them briefly in the subsections to improve readability.
4. **Quantify the Bias Direction (Flagship/Supplement):** State the expected direction of the fiber-aperture bias (e.g., central fiber misses extended star-forming disks, inflating the apparent quenching in bulge-dominated broad BPT targets).
5. **Address the 67 Unclassified Objects (Flagship):** The flagship mentions 67 unclassified objects are retained in the denominator but excluded from pairing. Add a brief note on whether they are expected to skew the baseline (likely negligible, but worth one sentence).
6. **Improve Table 1 Clarity (Flagship/Supplement):** Ensure the "Retention vs. spectro-z parent" column is explicitly defined as cumulative or stage-by-stage to avoid reader confusion.
7. **Define "High-Index" and "Low-Index" Quartiles Better (Supplement - Environment):** Clarify if "high-index" means numerically larger rank (further away, less dense) or a reversed scale. 
8. **Reframe "Transition Mass" Language (Supplement):** The term "mass transition" in the abstract of the 6th integrated draft hints at physical feedback. Soften this to "selection-sensitive mass bin" throughout.
9. **Clarify Linear Probability Model (Supplement - Environment):** The coefficient of "0.032 +/- 0.004" is provided without units or clear context on the baseline rate. Provide the baseline probability to contextualize the effect size.
10. **Acknowledge LINER Contamination Extent (Flagship):** While mentioned, explicitly state that in the mass bin of interest ($\log M_\star \geq 10.8$), LINERs and retired galaxies dominate the broad BPT class, meaning the primary signal is likely structural, not accretion-driven.
11. **Streamline the 8-Part Supplement Structure:** Ensure the transitions between the 8 notes clearly link back to the shared missing observables table (Table 3), rather than treating them as disconnected silos.
12. **Unify the Definition of "Low-sSFR" (Supplement):** The flagship notes a -1.309 dex offset, but the supplement refers to a "pilot threshold" for low-sSFR. Explicitly define this threshold (e.g., $-11$ dex) where used.

---

### 3. What Can Be Improved Now (Using Local Inventoried Data)

*   **Statistical Refinement of the Current Cache:** The standard errors on the median offset (e.g., the bootstrap interval [-1.334, -1.283]) can be further analyzed by breaking down the 8,146 pairs into narrower stellar-mass bins to see if the offset is purely driven by the highest-mass end.
*   **Marginal Distribution Checks:** The draft mentions marginal checks show differences < 5 percentage points from the parent. These distributions (mass, redshift, sSFR) of the 60,000 cached sample vs the 249,917 parent can be plotted or tabulated using the existing `csv_files` and `json_files`.
*   **S/N Ratio Sensitivity Drill-down:** The draft already contrasts S/N$\geq3$ with S/N$\geq10$. The existing data can be used to show the continuous trend of the offset as the S/N threshold increases, demonstrating the preferential loss of passive hosts.

---

### 4. What Requires New Real Data (MUST NOT BE WRITTEN AS A RESULT)

*   **Morphological/Structural Correlation:** Do not claim the offset is due to AGN feedback. This requires R_90/R_50, `fracDeV`, or central velocity dispersion metrics which were not cached.
*   **Global Quenching/sSFR:** Do not claim global galaxy quenching. This requires aperture-matched SFRs or IFU data to account for extended star-forming disks outside the 3-arcsec fiber.
*   **Halo Mass / Environmental Density:** Do not claim physical environmental density or halo quenching. This requires group catalogs, central/satellite labels, and fiber-collision corrections. The 10th-neighbor rank must remain a relative projected index.
*   **Jet Power / Maintenance Heating:** Do not claim mechanical feedback efficiencies. This requires X-ray cavity energetics and radio morphology/age.
*   **Outflow Escape/Recycling:** Do not claim gas is escaping the halo. This requires resolved IFU velocities, halo potentials, and multiphase (CO/HI) gas masses.

---

### 5. Exact Guidance for the Integrator (Safe Wording/Citation Changes)

*   **Flagship, Abstract:** Change "cannot be disentangled from morphology..." to "cannot be disentangled from morphology... and therefore must not be interpreted as evidence of active feedback or physical quenching."
*   **Flagship, Section 1:** Change "The result is not a causal claim or inference..." to "The result is strictly an observational association within this specific cached sample and cannot support causal claims regarding feedback..."
*   **Supplement, Abstract:** Change "The 55-arcsec SDSS fiber-collision limit also biases projected-neighbor statistics..." to "The 55-arcsec SDSS fiber-collision limit severely biases projected-neighbor statistics in dense regions, rendering physical density inferences impossible without forward modeling."
*   **Citations:** Ensure all references to multiwavelength datasets (radio, X-ray, CO/HI) in the supplement strictly use phrases like "To measure this physical parameter, future follow-up must incorporate data similar to [Citation]" rather than "As shown in [Citation], this parameter is...".

---

### 6. No-Mock-Data Receipt and Safety Ledger

*   **Mock Data Status:** ZERO mock, synthetic, fake, placeholder, or toy data proposed or generated.
*   **Metrics & Values:** All numbers, sample sizes, and offsets discussed (-1.309 dex, 8,146 pairs, 60,000 cache limit) are strictly quoted from the provided real-data TeX excerpts. No new numbers were invented.
*   **Citations:** No URLs, DOIs, arXiv IDs, or ADS bibcodes were generated or invented.
*   **Boundary Preservation:** The association-only boundary for RP-1 is strictly preserved and heavily reinforced in the recommendations.
*   **Write Operations:** ZERO. Read-only review mode strictly adhered to. No file edits, no DB writes, no API calls, no git commits, no cron jobs.


# command_result
exit_code=0
elapsed_s=28.5
timed_out=False
finished_utc=2026-07-09T19:41:33Z
