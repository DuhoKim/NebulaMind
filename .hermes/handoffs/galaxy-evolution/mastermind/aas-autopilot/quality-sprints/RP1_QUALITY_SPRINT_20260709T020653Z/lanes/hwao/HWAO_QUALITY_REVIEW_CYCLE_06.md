# hwao-agy-cycle-6
Started UTC: 2026-07-09T02:44:01Z
CWD: /Users/duhokim/NebulaMind/NebulaMind

HWAO_QUALITY_REVIEW_CYCLE_06

## Publication-Readiness Verdict

**Flagship (RP-1):** 
**Verdict: conditionally ready for preprint, but requires one more local polish pass.** 
The manuscript successfully maintains the strict association-only claim boundary and correctly identifies the limitations of the cached data and optical proxies. It is scientifically honest. However, minor wording improvements are needed to clarify the sign convention in the text and formalize the language around the data cache before it faces external readers.

**Supplement (Denominator Atlas):**
**Verdict: excellent conceptual framing, needs minor caption expansion.**
Consolidating the 8 fragile drafts into a single denominator/target atlas was the correct scientific decision. It honestly catalogs the missing observables required for physical feedback claims. The text is safe, but the figure captions currently read like internal pipeline logs rather than journal-ready descriptions.

---

## Top 10 Concrete Improvements (Prioritized)

### Must Fix Before Public (Safe for Integrator to Edit)

1. **Explicitly state the $\Delta$ sign convention in the flagship text.**
   *Issue:* Table 2 states "$\Delta\log {\rm sSFR}$ is target minus matched star-forming control," but the main text in Section 4 just says "a median $\Delta\log {\rm sSFR}$ of -1.309 dex gives a large negative catalog-sSFR offset."
   *Action:* Update Section 4 text to explicitly state "target minus control" so readers don't have to hunt for the table caption to understand the direction of the offset.

2. **Formalize the "cache" language in the flagship.**
   *Issue:* Phrases like "cached-versus-public marginal checks" (Section 2) sound like internal database engineering rather than scientific methodology.
   *Action:* Rephrase to "marginal distribution checks between the pilot sample and the full public parent." Replace "cached analysis table" with "pilot analysis sample."

3. **Expand the supplement figure captions.**
   *Issue:* Captions like "SDSS optical denominator/proxy diagnostic for m1_rp2_environment_quenching" are internal filenames, not scientific descriptions.
   *Action:* Rewrite captions to describe the axes and the data shown (e.g., "Fraction of low-sSFR emission-line galaxies as a function of local density proxy...").

4. **Quantify the Seyfert-like offset reduction in the flagship text.**
   *Issue:* Section 5 says the narrower proxy reduces the magnitude to "roughly half the preferred broad-BPT estimate."
   *Action:* Quote the actual numbers from Table 2 in the text of Section 5: "...reduces the magnitude from -1.309 dex to -0.763 dex, roughly half..."

### Nice Local Polish (Safe for Integrator to Edit)

5. **Clarify the arbitrary nature of the 60,000 cap in the abstract.**
   *Issue:* The abstract mentions a "non-random, capped 60,000-row emission-line cache," which could confuse readers.
   *Action:* Briefly clarify in the abstract or Section 2 that this is an "artificial computational pilot cap," as correctly noted in Table 1, rather than a physical flux or volume limit.

6. **Standardize US/UK spelling.**
   *Issue:* The supplement uses "nearest-neighbour" (Section 3.1) but AASTeX typically expects US English ("neighbor"). 
   *Action:* Standardize to "neighbor", "catalog", etc., across both documents.

7. **Harmonize hyphenation of "star formation".**
   *Issue:* The flagship uses "specific star-formation rate" and "star formation rate" inconsistently.
   *Action:* Use "star formation rate" (noun) and "star-forming" (adjective) consistently.

8. **Tighten the BPT line ratio description.**
   *Issue:* Section 3 lists the lines but doesn't explicitly state the ratio axes.
   *Action:* Briefly add that the classes are based on the standard [O III]/H$\beta$ vs [N II]/H$\alpha$ diagnostic diagram.

### Needs New Data (Do Not Edit - For Future Work Only)

9. **Morphological and Aperture Controls.**
   *Limitation:* The flagship correctly notes that matching is not performed in morphology or aperture fraction. Fiber-based sSFR is highly sensitive to bulge-to-disk ratios.
   *Future Action:* Cross-match with morphological catalogs (e.g., Galaxy Zoo or deep learning metrics) to add a bulge-fraction caliper to the matching algorithm.

10. **Multiphase Gas Masses.**
    *Limitation:* The optical offsets cannot distinguish between actual gas depletion (feedback removing fuel) and reduced star formation efficiency (stabilization/morphological quenching).
    *Future Action:* Obtain ALMA CO or HI 21cm follow-up for the matched pairs to measure the $M_{H2}/M_\star$ and $M_{HI}/M_\star$ fractions directly.

---

## Safe Wording/Section Changes for the Integrator

The integrator is authorized to make the following exact changes to the `.tex` files in the next cycle:

**In `rp1_flagship_polished.tex`:**
- Section 2: Replace "cached-versus-public marginal checks" with "marginal distribution checks between the pilot sample and the full public parent."
- Section 4: Add "(target minus matched control)" immediately after the first mention of $\Delta\log {\rm sSFR}$ in the text.
- Section 5: Update "reduces the magnitude to roughly half" to "reduces the magnitude from -1.309 dex to -0.763 dex (Table 2), roughly half".
- Globally: Standardize hyphenation for "star formation" and spelling (e.g., neighbor).

**In `supplementary_denominator_atlas.tex`:**
- Section 3 (all subsections): Replace the raw internal filename string in the figure captions (e.g., `m1_rp2_environment_quenching`) with a human-readable title describing the actual variables being plotted.
- Globally: Fix "nearest-neighbour" to "nearest-neighbor".

**Do NOT change:**
- The numeric results (8,146 pairs, -1.309 dex, bootstrap intervals, subset counts).
- The association-only claim boundary (do not introduce causal feedback language).
- The list of missing observables.

---

## Safety Ledger

- **Read-only evaluation:** Completed successfully.
- **File modifications:** None.
- **Commands executed:** None.
- **Public/Live impact:** None. No public pages, wikis, or databases were touched. No git commits or external submissions were made.
- **Scope:** Confined entirely to a local review of the provided text package.


# command_result
exit_code=0
elapsed_s=30.5
timed_out=False
finished_utc=2026-07-09T02:44:32Z
