# hwao-agy-cycle-9
Started UTC: 2026-07-09T03:54:16Z
CWD: /Users/duhokim/NebulaMind/NebulaMind

`HWAO_QUALITY_REVIEW_CYCLE_09`

## Publication-Readiness Verdict

**RP-1 Flagship:** **Conditionally Ready for Public Release (Pending Must-Fixes).** 
The manuscript is scientifically sound under the strict constraints of an association-only claim. It rigorously defends the boundary against causal AGN feedback and heavily caveats the 3-arcsec fiber and morphological mismatch. However, a few phrasing choices (e.g., the "20-fold" number) risk being quoted out of context by readers ignoring the caveats. Minor defensive tightening is required.

**Supplement (Denominator Atlas):** **Ready for Public Release (Pending Must-Fixes).**
The supplement excellently reframes the 8 abandoned papers as denominator/proxy baselines. By explicitly listing the "missing observables" required for physical inference, it effectively neutralizes over-claiming while preserving the hard work done on target vectors. 

---

## Top 10 Concrete Improvements (Ranked by Scientific Quality Effect)

### MUST FIX BEFORE PUBLIC (Safe Local Wording Changes)
These changes enforce the association-only boundary and prevent out-of-context citation of artifactual numbers.

**1. Contextualize the "20-fold" sSFR drop (RP-1 Sec 4):** 
The phrase *"roughly a 20-fold lower catalog sSFR"* is highly quotable and dangerous if isolated. The integrator must safely modify this sentence to ensure the aperture caveat is structurally bound to the number. (e.g., *"corresponds to roughly a 20-fold lower catalog sSFR within this fiber-centered comparison, which is heavily modulated by the central aperture..."*)

**2. Front-load the mass-bin artifact warning (Supplement Sec 3.5):** 
The text correctly identifies the optical AGN peak at $\log(M_\star/M_\odot) \in [11.0,12.5]$ as a selection-function artifact (S/N$\geq3$ dropping passive galaxies). However, this crucial disclaimer is at the *end* of the paragraph. Move it to the very beginning of the section so readers do not temporarily assume a physical feedback transition mass.

**3. Strengthen Table 1 selection warnings (RP-1 Sec 2):** 
Table 1 shows the drop from 373,445 to 60,000 rows. The caption notes it is an artificial cap, but must explicitly forbid volume density calculations right in the caption: *"This artificial cap means the sample cannot be used to derive volume-complete luminosity functions."*

**4. Clarify the physical mechanism boundary (RP-1 Sec 5):** 
Change *"rather than identifying a different physical mechanism"* to *"rather than identifying an active feedback mechanism."* This sharpens the distinction between passive contamination (LINER/retired) and active AGN feedback, reinforcing that no feedback is being claimed.

### NICE LOCAL POLISH (Safe Local Wording Changes)
These improve clarity and readability without altering the scientific claims or numerical results.

**5. Abstract numerical completeness (RP-1 Abstract):** 
Where the abstract states *"narrower Seyfert-like definitions reduce the offset magnitude"*, explicitly insert the number: *"...reduce the offset magnitude to -0.763 dex"*. This gives readers the full sensitivity range upfront.

**6. Unclassified objects disposition (RP-1 Sec 3):** 
Explicitly state that the 67 unclassified objects are retained in the overall denominator counts for completeness but are strictly excluded from the matched control pairing. 

**7. Explicitly define the H-alpha proxy limits (Supplement Sec 3.7):** 
Clarify whether the *median H-alpha luminosity proxy* used as a baseline for gas depletion is dust-corrected (e.g., via Balmer decrement) or raw. Adding a half-sentence clarifies the exact baseline being offered to CO/HI observers.

**8. Reinforce environmental limitations (Supplement Sec 3.1):** 
In the text describing the 10th-neighbor index, explicitly add that fiber collisions in SDSS systematically suppress dense-environment counts, heavily biasing this proxy before any physics is considered.

### NEEDS NEW DATA (Do Not Fix Locally - Acknowledge Only)
These require entirely new external data and cannot be addressed in the current manuscript, validating the need for the missing observables lists.

**9. Morphological Matching:** 
The -1.309 dex offset is contaminated by comparing broad-BPT (bulge-dominated) to star-forming (disk-dominated) galaxies. Determining if the offset survives at a fixed bulge-to-total ratio requires crossing the denominator with morphological catalogs (e.g., Galaxy Zoo or deep learning morphological measurements).

**10. Global / Resolved sSFR and Kinematics:** 
To escape the 3-arcsec fiber bias, the sample must be cross-matched with IFU surveys (like MaNGA or SAMI) to measure true global sSFR, resolved molecular/ionized outflows, and spatially resolved BPT maps. 

---

## Instructions for the Integrator

You are authorized to make the following safe wording/section changes to the local `.tex` files:
- **RP-1 `rp1_flagship_polished.tex`:**
  - Update the abstract to include "-0.763 dex".
  - Update Table 1 caption to explicitly mention volume-complete luminosity functions cannot be derived.
  - In Section 4, bind the "20-fold" text tightly to the fiber-aperture caveat in the same clause.
  - In Section 5, change "physical mechanism" to "active feedback mechanism".
- **Supplement `supplementary_denominator_atlas.tex`:**
  - In Section 3.5, move the sentences *"In this optical-emission-line denominator, the 11.0--12.5 dex peak is a selection-function artifact... It must not be interpreted as a universal feedback threshold."* to the very beginning of the subsection.
  - In Section 3.1, add a brief mention of fiber collisions to the text body alongside the 10th-neighbor index description.
- **Constraints:** Do not recalculate any statistics. Do not alter the 8,146 matched pairs, the -1.309 dex offset, or the -0.763 Seyfert proxy offset. Do not change the core claim. 

---

## Safety Ledger

- **Data Safety:** Read-only review completed. No internal databases, APIs, or public pages were queried or touched.
- **File Safety:** No files were edited, committed, or pushed.
- **Execution Safety:** No code was executed. No commands were run.
- **Claim Safety:** The association-only boundary is maintained and aggressively defended. No causal feedback claims are permitted or requested. All numerical results from the provided snapshot are strictly preserved. 
- **State:** Local manuscript review only. Awaiting integrator action on the recommended safe wording changes.


# command_result
exit_code=0
elapsed_s=37.3
timed_out=False
finished_utc=2026-07-09T03:54:54Z
