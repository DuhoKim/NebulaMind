# gemini-agy-deep-cycle-1
Started UTC: 2026-07-09T02:11:24Z
CWD: /Users/duhokim/NebulaMind/NebulaMind

GEMINI_AGY_DEEP_REVIEW_CYCLE_01

# Deep Review Report: Galaxy Evolution Quality Sprint (Cycle 1)

This review evaluates the candidate flagship paper (RP-1) and the supplementary denominator/proxy atlas from a skeptical peer-review perspective, focusing on overclaims, selection biases, citation alignment, and physical interpretation risks.

---

## 1. Blocker & Major Issues: Denominator vs. Physical Reality

### Issue 1.1: The "Quenched" Terminology Contradiction inside an Emission-Line Denominator
* **Severity:** **Blocker**
* **Risky Phrasing:** 
  > "...high-density quartile has quenched fraction 0.230..." (Supplement, Section 3.1)
  > "...quenched fraction and optical AGN incidence rise..." (Supplement, Section 3.5)
* **Critique:** All analyzed galaxies are selected from a strict four-line BPT denominator requiring $\text{S/N} \geq 3$ in $\text{H}\alpha$, $\text{H}\beta$, $\text{[O III]}$, and $\text{[N II]}$. Truly quenched (passive/red-sequence) galaxies generally lack these emission lines entirely and are excluded from the sample. Defining a "quenched fraction" within a sample that *excludes* line-less quenched galaxies by construction is a severe denominator error. A reader will mistake this for the physical quenched fraction of the galaxy population.
* **Proposed Replacement:** 
  > "...high-density quartile has a low-sSFR emission-line fraction of 0.230..."
  > "...the fraction of low-sSFR targets and optical AGN incidence rise..."

### Issue 1.2: Capped Cache Selection Bias Untreated in Offsets
* **Severity:** **Major**
* **Risky Phrasing:** 
  > "The preferred matched comparison yields 8,146 pairs and a median $\Delta\log \text{sSFR}$ of -1.309 dex..." (Flagship, Abstract)
* **Critique:** The flagship notes that the cached table is a capped, non-random 60,000-row subset (24.0% of the strict parent). Since the BPT S/N constraints disproportionately retain high-sSFR galaxies (94.9% of the high-sSFR parent vs. 33.6% of the low-sSFR parent), any matching result is heavily conditioned on this selection function. The abstract and matched-control result section present the -1.309 dex offset as a clean physical measurement rather than a conditional, cache-dependent value.
* **Proposed Replacement:** 
  > "For the analyzed capped emission-line cache, the preferred matched comparison yields 8,146 pairs and a median sSFR offset of -1.309 dex..."

---

## 2. Citation-Role and Methodology Alignment

### Issue 2.1: Simulation and Multiphase Gas References Listed Without In-Text Context
* **Severity:** **Minor**
* **Risky Phrasing:** The bibliographies of both the Flagship and Supplement list references like `\bibitem[Dave et al.(2019)]{simba2019}`, `\bibitem[Saintonge et al.(2017)]{xcoldgass2017}`, `\bibitem[Cicone et al.(2014)]{cicone2014}`, and `\bibitem[Nelson et al.(2019)]{tng2019}`, but these are not cited in the text to contextualize the observations.
* **Critique:** Without clear in-text citations, these references risk looking like method support or comparison data when they must only serve as future-data motivation (since no actual CO/HI, simulation mock, or resolved kinematic data are analyzed here).
* **Proposed Replacement:** Add explicit motivation text in the Supplement or remove the unused bibliography entries. 
  * *Example for `xcoldgass2017`:* "These target lists are intended as denominators for future molecular gas surveys, such as those motivated by xCOLDGASS \citep{xcoldgass2017}."

---

## 3. Missing Observables & Caveats Ledger

The following sections in the supplement have gaps between the nominal science targets and the actual SDSS observables:

| Section / Note | Nominal Physical Target | Missing Observables (Required for Physical Claims) |
| :--- | :--- | :--- |
| **3.1 (Environment)** | Halo/Group Quenching | Group catalogs, satellite/central classification, halo mass estimates. |
| **3.2 (Maintenance)** | AGN Heating vs. Cooling | X-ray cavity/cooling-luminosity, radio jet power, non-detection modeling. |
| **3.3 (Outflow)** | Gas Escape & Recycling | Resolved gas kinematics (molecular/ionized/neutral), CGM tracers. |
| **3.4 (Radio Jets)** | Radio-Jet Environment Coupling | Radio jet morphology, shock energetics, calibrated jet power. |
| **3.5 (Transition)** | Mass Transition Feedback | Molecular gas fractions, baryon deficits, stellar feedback indicators. |
| **3.7 (Gas Fraction)**| Gas Depletion / Starvation | CO or dust-based molecular gas masses, aperture-matched SFR. |
| **3.8 (Simulation)** | Physical Model Validation | Mock catalogs processed through identical SDSS BPT selection/noise masks. |

---

## 4. Ranked Integrator Action Items

1. **[Priority 1] Rename "Quenched Fraction"**: Update all instances of "quenched fraction" and "quenched" in both drafts to "low-sSFR emission-line fraction" or "low-sSFR fraction within the emission-line denominator" to prevent physical misinterpretation.
2. **[Priority 2] Qualify the Abstract Offsets**: Modify the Flagship abstract to explicitly state that the $-1.309$ dex offset is conditional on the capped 60,000-row BPT selection.
3. **[Priority 3] Clean Up or Link Bibliography**: Either insert explicit motivational citations for `cicone2014`, `xcoldgass2017`, `simba2019`, and `tng2019` in the body text or prune them from the bibliography.

---

## 5. Safety Ledger

* **Live Writes/Modifications:** None.
* **Command Executions:** None.
* **Publishing/Deployments:** None.
* **External API/Network Requests:** None.
* **Git Operations:** None. All reviews performed strictly read-only on the provided local candidates.


# command_result
exit_code=0
elapsed_s=14.8
timed_out=False
finished_utc=2026-07-09T02:11:39Z
