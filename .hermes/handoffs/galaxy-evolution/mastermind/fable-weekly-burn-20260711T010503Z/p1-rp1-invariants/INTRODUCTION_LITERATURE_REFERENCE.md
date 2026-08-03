# RP-1 invariant-safe introduction & literature reference block

Marker: `FABLE_BURN_P1_INTRO_LIT_REFERENCE_20260711T010503Z` (packet `HWAO_FABLE_BURN_P1_BRIEF_20260711T010503Z`)

> **REFERENCE MATERIAL ONLY — NOT A CANDIDATE.**
> This file must never be copied into, or written anywhere near, the sprint's `candidates/` tree. It exists so future prose lanes (introduction / literature phases) can check their candidate text against a numerically frozen reference. Base package: `candidates/cycle_05_package` (SHA-256 anchors in `INVARIANT_MANIFEST.json` → `snapshot_sha256`). Every numeral below is byte-identical to cycle 5 and to `INVARIANT_MANIFEST.json`. If any sentence here disagrees with the manifest, the manifest wins.

## 0. Rules of use (summary of the verbatim-carry rule, RCA §5)

1. Numerals in candidate prose are **copied from cycle 5 character-for-character** — never re-derived from artifacts, tables, or memory, never re-rounded. In particular: the CI is `[-1.334,-1.283]` (canon), **not** `[-1.334,-1.282]`, and the line-188 supplement cell is `2.830`, **not** `2.831`, even though the raw artifact nearest-rounds the other way. If that feels wrong, report it; do not fix it inline.
2. Any numeral not present in `INVARIANT_MANIFEST.json` **must not appear** in candidate prose. External literature values are not exempt: until they are verified (network access — GATED) and registered in the manifest, quantitative prior-work comparisons stay as named placeholders (§3).
3. Quantitative referents are frozen ("across mass bins", "target minus matched control", "fiber-centered"). Rewording around them is fine; changing what a number refers to is not.
4. Before audit, run the §4 checklist.

## 1. Canonical numeric sentences (verbatim from cycle 5)

These are the load-bearing quantitative sentences. A prose lane may reuse them whole, or embed the bolded strings unchanged in new sentences. File key: FLG = `flagship_rp1/aastex/rp1_flagship_polished.tex`, SUP = `supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex`; line numbers are cycle-5 anchors.

### 1.1 The result (FLG)

- FLG:13 (abstract): "Broad optical BPT-selected galaxies are matched to star-forming controls in stellar mass and redshift only; the preferred custody-backed comparison yields 8,146 pairs and a median $\Delta\log {\rm sSFR}$ of -1.309 dex, with a bootstrap 95\% confidence interval of [-1.334,-1.283] dex."
- FLG:57 (Table 1 row, carry as one string): `Broad optical BPT-selected targets, S/N$\geq3$, nearest SF control with replacement & 8,146 & -1.309 & [-1.334,-1.283] & Preferred association estimate \\`
- FLG:65 (Fig. 2 caption core): "($N=8{,}146$ pairs, variance-normalized Euclidean matching in standardized $(\log M_\star,z)$ space, with replacement and without a maximum mass--redshift caliper). The median offset is $-1.309$ dex with bootstrap 95\% interval $[-1.334,-1.283]$ dex."
- FLG:74 (conclusion): "Its provenance-retained result is the preferred 8,146-pair, -1.309 dex offset with bootstrap 95\% interval [-1.334,-1.283] dex."

### 1.2 Sample and selection (FLG)

- FLG:31: "The retained pilot analysis sample is a fixed 60,000-galaxy subset selected sequentially by \texttt{specObjID}." / "The strict public four-line S/N$\geq3$ eligible parent count of 249,917 galaxies, and the corresponding 24.0\% cache coverage, are selection-context diagnostics rather than custody-backed independent result rows;"
- FLG:22/32: "Because the sample is restricted to $0.02<z<0.12$, the standard local BPT demarcations are used here without any redshift-evolution correction." / "Over the redshift interval $0.02<z<0.12$, the SDSS 3-arcsec fiber subtends roughly 1.2--6.5 kpc, so the catalog median sSFR proxy comparison is fiber-centered rather than global."
- FLG:39 (denominator census): "The custody-backed analysis denominator contains 39,553 star-forming galaxies, 12,234 intermediate/composite galaxies, 8,146 broad optical BPT-selected targets, and 67 unclassified objects."
- FLG:39 (matching quality): "In the preferred estimate, this yields 100\% target coverage (8,146 of 8,146 targets matched), and the unrestricted Euclidean match has median absolute separations of 0.0045 dex in $\log M_\star$ and 0.00021 in redshift"
- FLG:39 (lines): "BPT classes are computed from H$\alpha$, H$\beta$, [O~III]$\lambda5007$, and [N~II]$\lambda6584$ using standard demarcations"

### 1.3 Supplement baselines (SUP)

- SUP:92 (environment): "The high-index quartile has a low-sSFR emission-line fraction of 0.230 (3,456/15,000), while the low-index quartile has 0.181 (2,710/15,000). The bootstrap high-minus-low interval is [0.041, 0.059], and a linear probability model adjusted for log stellar mass and redshift gives a high-index coefficient of 0.032 +/- 0.004, corresponding to an approximate 3.2 percentage-point increase in low-sSFR incidence at fixed mass and redshift."
- SUP:103 (maintenance heating): "The massive subset (\(\log M_\star \geq 10.8\)) contains 9,298 emission-line galaxies, of which 5,695 are low-sSFR by the pilot threshold. The broad optical BPT-selected fraction is 0.430 in the massive subset and 0.607 among massive low-sSFR objects."
- SUP:114 (outflow kinematics): "High-excitation broad optical BPT-selected candidates number 4,440 of 60,000 emission-line galaxies (0.074). Their median \(\log {\rm sSFR}\) is -11.53, compared with -10.14 for the full denominator."
- SUP:125 (radio-jet environment): "Among massive hosts, the high-index quartile has a broad optical BPT-selected fraction of 0.509, while the low-index quartile has 0.367. The bootstrap high-minus-low interval is [0.112, 0.170]."
- SUP:136 (mass-bin diagnostic): "The first stellar-mass bin with low-sSFR fraction above 0.5 is \(\log(M_\star/M_\odot) \in [11.0,12.5]\), and the broad optical BPT-selected incidence peaks in the 11.0--12.5 bin at 0.520 within this selection-limited, SpecObjID-capped pilot sample."
- SUP:147 (tracer census): "Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418. The widest-to-narrowest prevalence ratio is 3.1 before adding molecular, neutral, X-ray, or radio phases."
- SUP:158 (gas depletion): "the massive low-sSFR denominator contains 6,729 galaxies in the SDSS emission-line sample." / "Its broad optical BPT-selected fraction is 0.549, and the median H-alpha luminosity proxy is \(\log (L_{\mathrm{H}\alpha}/\mathrm{erg\,s^{-1}}) = 40.061\)." / "The median H-alpha luminosity proxy is 0.66 dex lower than in massive star-forming emission-line galaxies."
- SUP:169 (simulation vector — frozen referent): "The pilot writes 15 mass-redshift cells with \(n \geq 50\) as a compact comparison vector for low-sSFR fraction, broad optical BPT-selected incidence, and median \(u-r\) colour versus mass and redshift. Across mass bins, low-sSFR fractions span 0.005-0.729, and broad optical BPT-selected fractions span 0.003-0.520."
- SUP:176–190: the 15 target-vector table rows are invariants as whole rows (manifest `SUP-ROW-176 … SUP-ROW-190`); carry the table byte-identical, including `2.830` at line 188.

## 2. Invariant-safe INTRODUCTION delta (for a future "introduction" phase)

Drop-in expansion built strictly on cycle-5 wording; connective prose adds **no numerals**. Sentences in quotes are verbatim cycle-5 strings from §1 and may be reused as-is.

> **Paragraph I-1 (context, no numerals).** Feedback from accreting nuclei is a standard ingredient of galaxy-evolution models, yet whether optically selected nuclear activity traces suppressed star formation at fixed stellar mass remains an association-level question in survey data. Optical emission-line classification and catalog star-formation proxies make that question testable at scale, but only inside the selection function of the parent spectroscopic survey \citep{brinchmann2004,kauffmann2003bpt,heckmanbest2014}.
>
> **Paragraph I-2 (this paper's question, verbatim numerals).** "This paper addresses a narrow association-only question within a low-redshift SDSS DR17 optical emission-line denominator: do broad optical BPT-selected galaxies have lower catalog median sSFR proxy than mass--redshift matched star-forming controls?" The analysis is deliberately bounded: "The retained pilot analysis sample is a fixed 60,000-galaxy subset selected sequentially by \texttt{specObjID}." Matching is in stellar mass and redshift only, and "the preferred custody-backed comparison yields 8,146 pairs and a median $\Delta\log {\rm sSFR}$ of -1.309 dex, with a bootstrap 95\% confidence interval of [-1.334,-1.283] dex."
>
> **Paragraph I-3 (claim boundary, verbatim skeleton).** "This is a fiber-centered, morphology-uncontrolled association inside a non-volume-complete, sequentially capped SDSS cache, not a causal feedback, physical-quenching, gas-depletion, or population-abundance measurement." Because the sample is restricted to "$0.02<z<0.12$" and the "3-arcsec" fiber subtends "1.2--6.5" kpc over that interval, all star-formation quantities are central-fiber proxies. The interpretation constraints of the Scope and limitations subsection govern everything that follows.
>
> **Paragraph I-4 (roadmap, no numerals).** Section 2 states the missing observables for causal inference; Sections 3 and 4 define the shared selection and the matched-control construction; Section 5 presents the retained result; the companion supplement organizes the denominator and proxy baselines for follow-up.

Rules applied: every numeral above appears in `INVARIANT_MANIFEST.json` with identical formatting; cite keys are restricted to the existing cycle-5 bibliography.

## 3. Invariant-safe LITERATURE-COMPARISON delta (for a future "literature" phase)

The audits repeatedly flag `missing explicit quantitative comparison to prior work`. A prose lane **cannot** close that blocker by typing literature numbers from memory — that is the same regeneration failure mode as the CI drift, aimed at external values. This scaffold separates what may be written now (structure, qualitative positioning, existing cite keys) from the slots that require verified values (GATED: needs network/ADS lookup plus manifest registration).

> **Paragraph L-1 (qualitative positioning — safe now).** Matched-control comparisons of optically selected active galaxies against inactive controls at fixed stellar mass are well established in SDSS studies \citep{ellison2011,schawinski2010}, and central/structural quantities are known to track quenching at least as strongly as optical nuclear classification \citep{bluck2014,piotrowska2022}. The fiber-aperture systematics of SDSS star-formation proxies \citep{kewley2005,brinchmann2004} and the contamination of low-ionization classes by retired stellar populations \citep{cidfernandes2011,stasinska2008,belfiore2016} bound what any optical-only offset can mean. Within those bounds, the present measurement — "the preferred 8,146-pair, -1.309 dex offset with bootstrap 95\% interval [-1.334,-1.283] dex" — is an association statement inside a fixed 60,000-galaxy denominator.
>
> **Paragraph L-2 (quantitative comparison — GATED slots).** A compliant quantitative comparison sentence has the form: "This offset is [larger/smaller/consistent with] the ⟨QTY-1⟩ dex offset reported by ⟨AUTHOR/YEAR, sample, matching variables⟩ [EXT-1]." Each ⟨QTY-n⟩/[EXT-n] slot must be filled only after (a) the value is verified against the cited paper (network access — **GATED, needs separate Duho approval**), and (b) the value is registered in `INVARIANT_MANIFEST.json` as a new `external_reference` entry in the same change. Until both happen, candidates must not contain any external quantitative value. Suggested slots, chosen because the works are already in the cycle-5 bibliography (no new bibitems needed): [EXT-1] Ellison et al. (2011) — SDSS pair/control sSFR offsets \citep{ellison2011}; [EXT-2] Schawinski et al. (2010) — early/late-type AGN host star-formation comparison \citep{schawinski2010}; [EXT-3] Bluck et al. (2014) — central-structure quenched-fraction dependence \citep{bluck2014}; [EXT-4] Piotrowska et al. (2022) — velocity-dispersion vs BPT-class quenching predictors \citep{piotrowska2022}.
>
> **Paragraph L-3 (why the comparison is bounded — safe now).** Any such comparison is conditional: the denominator here is "a fixed 60,000-galaxy subset selected sequentially by \texttt{specObjID}" with "the strict public four-line S/N$\geq3$" selection, so quantitative agreement or disagreement with volume-corrected or differently selected samples tests the selection function as much as the physics. The comparison paragraph must say so explicitly.

**Bibliography rule.** Prose phases may cite only keys already present in the cycle-5 bibliographies. Adding or removing a `\bibitem` is a declared change (RCA §5.5) — cycle 6 silently deleted four uncited flagship bibitems and cycle 7 re-added them, churn a carry rule would have flagged.

## 4. Pre-audit checklist for any candidate built from this block

From the candidate package root (`grep -F -c` = fixed-string count; `-c` counts matching lines — entries with multiple same-line occurrences use the manifest's `occurrences_expected` with `grep -o | wc -l`):

1. `grep -F -- '[-1.334,-1.283]' flagship_rp1/aastex/rp1_flagship_polished.tex | wc -l` → 4; `grep -F -- '[-1.334,-1.282]' …` → 0.
2. `grep -F -- '2.830 \\' supplementary_denominator_atlas/aastex/supplementary_denominator_atlas.tex | wc -l` → 1; `grep -F -- '2.831' …` → 0.
3. `grep -F -- '0.005-0.729' … | wc -l` → 1 and `grep -F -- '0.003-0.520' … | wc -l` → 1; `grep -F -- '0.001-0.856' …` → 0.
4. Full sweep: every entry in `INVARIANT_MANIFEST.json` for the candidate's file meets `occurrences_expected` under its `match_mode`, and no `table_row` entry differs by even one character.
5. No numeral appears in the candidate that is absent from the manifest (new numerals ⇒ stop; register per RCA §5.3 first).
6. Referent phrases intact: "Across mass bins", "target minus matched control", "fiber-centered".

`FABLE_BURN_P1_INTRO_LIT_REFERENCE_20260711T010503Z`
