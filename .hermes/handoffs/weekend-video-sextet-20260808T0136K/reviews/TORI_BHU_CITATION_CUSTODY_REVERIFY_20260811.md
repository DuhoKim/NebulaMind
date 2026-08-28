# TORI — BHU CITATION-CUSTODY RE-VERIFICATION

**Seat:** Tori / custody and citation verification only  
**Date:** 2026-08-11  
**Scope:** source resolution, version custody, quotation accuracy, and claim-to-source fit. This is not a scientific-merit review, acceptance, publication, or Kun's separate re-gate.

## Plain verdict for Duho

**LOAD-BEARING CITATION CUSTODY: PASS.**

The current packet's actual closure premise is supported by the current full text of arXiv:1910.10819v2: the paper contains a real qualitative handedness assertion and substantial mechanics, equations, scales, functional forms, and retrospective observational numbers, but it contains no calibrated model prediction for the amplitude, scale dependence, or redshift dependence of the galaxy-handedness statistic; no independently predicted sky direction; no finite positive lower bound on the handedness effect; and no source-defined numerical acceptance region for a prospective finite-precision handedness test.[6]

**NARROW OPERATIONAL CLOSURE: SUPPORTED.** The four routes named by the packet—galaxy handedness, public-data isotropy/parity, quasar number-count dipole, and parity-odd 4PCF—do not have a calibrated BHU-specific target in this source.[6] This does not mean that the paper contains no qualitative claims, no equations, no numbers, or no proposition that observations could count against.[6]

**WHOLE-PACKET “CLEAN CUSTODY”: NOT QUITE YET AS WRITTEN.**[6]

Two small wording points should be repaired before calling every sentence clean: (i) `reviews/LANA_BHU_PREDICTION_DERIVATION_20260811.md:336` should say that no finite-precision test can be **numerically** scored against a **source-defined acceptance region**, because the same paragraph correctly acknowledges qualitative outcomes that could count against the prose claims; and (ii) lines 236 and 280 should use Brown–Lee–Rho's own approximately `1.5 M_sun` Brown–Bethe maximum, or add a separate primary citation for the packet's `1.5–1.6 M_sun` range.[6][9][12]

The phrase “real, but uncalibrated, prediction” at lines 128 and 363 is source-defensible only in the limited sense of an explicit qualitative model consequence; “explicit, source-backed qualitative claim, but not a calibrated or pre-data forecast” would be less flattering and more exact.[6]

Nothing is published or accepted. Duho decides; Kun re-gates separately.

## 0. Artifact and prescribed-order custody

The target read for this receipt is exactly:

- `reviews/LANA_BHU_PREDICTION_DERIVATION_20260811.md`
- 36,833 bytes
- SHA-256 `efa2d48dbbc52984d60f3228e068ad278614ad0682d14b79301c46539436a36b`
- self-identified as Revision 4

I completed the fresh primary-source check before opening the prior receipt. The pre-receipt findings were sealed at `reviews/_tori_bhu_reverify_sources_20260811/INDEPENDENT_FINDINGS_BEFORE_PRIOR_RECEIPT.md` at 2026-08-11T11:55:14Z. Only then did I open `reviews/TORI_BHU_CITATION_CUSTODY_VERDICT_20260811.md`.

The prior receipt is 27,501 bytes, SHA-256 `b3f0a41681d25debdd8f10d434aa7666dea9287679075da9afdefa7bb814fcf3`. It gated a 24,478-byte predecessor of the Lana packet, SHA-256 `209f9eff4abafac59a703f851be3a2c9b37b936a9fe0e8afad352288902622b6`, not the current 36,833-byte target. This receipt is the fresh custody check on the current bytes.

## 1. arXiv:1910.10819 — metadata, journal status, and version history

### 1.1 Primary category and identifiers

The current arXiv record is `arXiv:1910.10819v2`, *Universe in a rotating black hole and preferred axis*.[4][7]

Its primary category is **physics.pop-ph (Popular Physics)**; it is cross-listed in **astro-ph.CO** and **gr-qc**.[4][7]

The arXiv-issued DOI is **10.48550/arXiv.1910.10819**, resolving at https://doi.org/10.48550/arXiv.1910.10819.[19] DataCite identifies the current resource as version 2 and `resourceTypeGeneral: Preprint`.[19]

### 1.2 Journal-version result

**No journal version was located as of 2026-08-11.**[7][19][21]

That wording is intentionally dated and non-exhaustive.[7][19][21]

The arXiv API record has no `journal_ref` or publisher-DOI field; DataCite classifies the DOI object as a preprint; INSPIRE has the arXiv e-print but no `publication_info` or DOI for this record; and the exact-title/author Crossref query returned `total-results: 0`.[7][19][21]

This supports the packet's wording “no journal version located as of 2026-08-11.”[7][19][21]

It does **not** prove that no differently titled successor can exist anywhere.[7][19][21]

### 1.3 Version history is material, not cosmetic

**v1:** `arXiv:1910.10819v1`, submitted 23 October 2019 UTC, title *Black Hole Genesis and origin of inertia*, 2 pages.[1]

The complete v1 TeX source is 12,449 bytes / 123 lines.[3] A complete source scan found zero occurrences of `preferred axis`, `clockwise`, `counterclockwise`, `handedness`, or `Kerr radius`.[3]

Its central proposal is instead:

> “I propose that if the universe was born as a baby universe on the other side of the event horizon of a black hole existing in a parent universe, then the corresponding white hole provides the absolute inertial frame of reference in the universe.”[3]

**v2:** `arXiv:1910.10819v2`, revised 29 May 2025 UTC, retitled *Universe in a rotating black hole and preferred axis*, 5 pages.[4][7]

The complete v2 TeX source is 27,199 bytes / 255 lines and adds the inherited rotating axis, rotating-frame mechanics, galaxy-spin alignment and handedness, retrospective galaxy and bulk-flow summaries, and an evolving-dark-energy proposal.[6]

**Verdict on claim (1): SUPPORTED.**[1][4][6]

v1 and v2 are materially different.[1][4][6]

All preferred-axis and CW/CCW material belongs to v2, not v1.[3][6]

## 2. What the current v2 full text actually contains

### 2.1 Inherited axis and metric-scale proposal

The paper says:

> “A universe born from a rotating black hole should inherit its axis of rotation as a preferred axis.”[6]

It then says a complete description “should combine” the FLRW metric with the Gödel metric, and:[6]

> “The preferred direction should introduce small corrections to the FLRW metric, containing the Kerr radius `a=M/mc`, where `M` is the angular momentum of a rotating black hole and `m` is its mass.”[6]

This is a proposed scale entering as a correction, not a worked-out corrected cosmological metric and not a predicted numerical value of the parent spin.[6]

### 2.2 Equations and functional forms

The v2 body explicitly labels what follows as “Several qualitative consequences of the rotation of the universe” and derives standard non-relativistic rotating-frame relations.[6]

It gives the rotating-frame Lagrangian

`L = (1/2) m v^2 + m v·(Omega×r) + (1/2) m (Omega×r)^2 - U(r)`,

the force equation containing angular-acceleration, Coriolis, and centrifugal terms,

`m dv/dt = -dU/dr - m alpha×r - 2m Omega×v - m Omega×(Omega×r)`,

the centrifugal-force magnitude `m Omega^2 rho`, and the energy relation

`E = E0 - M·Omega`.[6]

For its dark-energy proposal the paper changes the centrifugal magnitude to `m Omega^2 r`, writes the acceleration as `Omega^2 r`, identifies `H=Omega` in the stated empty-universe comparison, and proposes:

> “The cosmological constant generated by the rotation of the universe would not be constant: `Lambda=3 Omega^2/c^2`.”[6]

It says angular velocity decreases as the universe expands, but provides no numerical `Omega`, parent-spin prior, or explicit `Omega(a)` law.[6]

Therefore any broad description of this preprint as having “no scales,” “no functional forms,” “no equations,” or “zero numbers” is false.[6] The current packet correctly records those older formulations as false and no longer uses them as its operative premise.[6]

### 2.3 Named observables and qualitative orientations

The v2 paper names the following observational consequences:

- CMB isotropy on the largest scales in the absolute frame;
- galaxy angular momenta tending to align parallel to the preferred axis;
- unequal clockwise and counterclockwise galaxy counts;
- galaxy-cluster bulk flow perpendicular to and away from the preferred axis; and
- a decreasing effective dark-energy term as the universe expands.[6]

The paper also imports observational numbers: galaxy samples of approximately `10^4`, `10^5`, `10^6`, and `10^2`; redshift ranges `z~0.04`, `z<0.3`, and `z<2`; cited fitted axes; an approximately 50% JADES count difference; a 630 km/s bulk flow; a mean fitted axis `alpha=197°±47°`, `delta=34°±3°`; and a computed 98.2° angle between the mean spin axis and cited flow axis.[6]

Those are retrospective data inputs and arithmetic summaries from cited observations. They are not independent values forecast by the BHU model before those observations.[6]

## 3. The galaxy-count sentence and whether “prediction” is fair

The current v2 text says, verbatim:

> “In the presence of the rotation of the universe, most galaxies should therefore tend to rotate in a preferred direction, coinciding with the direction of the angular velocity `Omega` of the universe. Consequently, the numbers of clockwise- and counterclockwise-spinning galaxies in a rotating universe should be different.”[6]

**Claim (2), literal citation verdict: SUPPORTED.**[6] The packet is accurate that v2 explicitly says the counts “should be different.”[6] The spin lane's count statistic was not invented without any source.[6]

**Claim (2), wording-strength verdict: QUALIFIED.**[4][6]

The source supports an explicit qualitative consequence/sign claim.[6]

It does not supply a calibrated numerical forecast, and it is not a pre-data prediction: v2 was revised in 2025 after the galaxy-handedness studies it cites and immediately uses those studies as seeming support.[4][6]

For maximum custody precision, “the lane was chasing an explicit, source-backed qualitative claim, but not a calibrated or pre-data forecast” is better than “a real prediction.”[4][6]

The packet's present phrase is not fabricated, because the source really says “should be different,” but it is generous unless its post-hoc and uncalibrated status remains visible.[4][6]

The current packet does make that status visible in section 1.3, so this is a wording recommendation rather than a failure of the load-bearing closure.[6]

## 4. The load-bearing negative formulation, element by element

The following verdicts apply specifically to the **galaxy-handedness statistic**, not to every equation or observable anywhere in the paper.[6]

| Element | Fresh full-text verdict | Exact boundary |
|---|---|---|
| No calibrated amplitude prediction | **SUPPORTED** | No predicted CW fraction, handedness-dipole amplitude, uncertainty, or transfer function from parent spin/`Omega` to the statistic appears.[6] |
| No calibrated scale dependence | **SUPPORTED WITH SCOPE** | The paper has physical scales (`a`, `rho`, `r`) and observational sample/redshift scales, but no angular, radial, or sample-scale law for the handedness statistic.[6] |
| No calibrated redshift dependence | **SUPPORTED** | It says `Omega` decreases with expansion, but never maps that statement to a handedness amplitude versus redshift.[6] |
| No independently predicted axis direction | **SUPPORTED** | All quoted sky coordinates come from cited fitted axes; `alpha=197°±47°`, `delta=34°±3°` is an arithmetic mean of those data-derived axes.[6] |
| No finite positive lower bound | **SUPPORTED** | “Most”/“should be different” supplies a sign/majority-style qualitative constraint, but no nonzero minimum asymmetry `epsilon`, detectability floor, or minimum parent spin.[6] |
| No numerical acceptance region | **SUPPORTED** | No source-defined estimator, tolerance, likelihood, amplitude threshold, or accept/reject interval is supplied for a prospective finite-precision handedness test.[6] |

The complete source also contains no `quasar`, `4PCF`, `four-point`, or `parity-odd` prediction and no occurrence of an acceptance, likelihood, tolerance, prior, clockwise-fraction, dipole-amplitude, or lower-bound contract.[6]

**Claim (3): SUPPORTED AS FORMULATED BY THE USER.**[6] This is the exact level at which the closure is safe: **no calibrated model prediction for handedness amplitude/scale/redshift dependence; no independently predicted axis; no finite lower bound; no numerical acceptance region for a finite-precision test.**[6]

It must not be strengthened into any of the following:

- “the preprint has no scales, forms, equations, or numbers”;
- “the preprint makes no qualitative falsifiable claim”;
- “no finite-precision observation could count against any prose claim”; or
- “the idea is untestable in principle.”

The current packet generally preserves that distinction.[6] Its one residual sentence at line 336 should insert “numerically” and “against a source-defined acceptance region” so it cannot be read as erasing the qualitative constraints acknowledged two sentences earlier.[6]

## 5. Brown–Lee–Rho and the neutron-star measurements

### 5.1 Exact Brown–Lee–Rho threshold and consequence

The source is G. E. Brown, Chang-Hwan Lee, and Mannque Rho, *Kaon Condensation, Black Holes, and Cosmological Natural Selection*, **Physical Review Letters 101, 091101 (2008)**, DOI **10.1103/PhysRevLett.101.091101**.[9]

The corrected abstract says:

> “It is argued that a well measured double neutron star binary in which the two neutron stars are more than 4% different from each other in mass or a massive neutron star with mass `M ≳ 2 M_sun` would put in serious doubt or simply falsify the following chain of predictions: (1) nearly vanishing vector meson mass at chiral restoration, (2) kaon condensation at a density `n~3n_0`, (3) the Brown-Bethe maximum neutron star mass `M_max~1.5 M_sun` and (4) Smolin's ‘Cosmological Natural Selection’ hypothesis.”[9][12][22]

The exact relation is **`≳`**, not strict `>`, `>=`, or `≥`.[10][12][23]

The versioned arXiv source defines `\gsim` as “greater than or approx. symbol.”[12]

APS's Publisher's Note, **PRL 101, 119901 (2008)**, DOI **10.1103/PhysRevLett.101.119901**, states that a tagging error caused a relation-sign misprint in the online abstract; the rendered correction visibly reads `M ≳ 2 M_sun`.[10][23]

The body separately says:

> “A firm observation of any type of a neutron star whose mass is greater than `M_max^BB` or to be safe `≳ 2 M_sun` would present a serious obstacle to the BB and CNS scenarios.”[12][22]

Brown–Lee–Rho therefore do **not** say that a central estimate at or above strict 2.00 automatically and unambiguously falsifies all of CNS.[9][12][22]

Their own consequence is disjunctive—“put in serious doubt or simply falsify” the chain—and elsewhere “present a serious obstacle.”[9][12][22]

The same source repeatedly gives the Brown–Bethe maximum as approximately **1.5 M_sun**.[9][12][22]

The packet's `1.5–1.6 M_sun` range is not the exact number this source states; it should be narrowed to `~1.5 M_sun` unless a separate primary citation is supplied.[9][12][22]

### 5.2 PSR J1614−2230 — Demorest et al. 2010

P. B. Demorest et al., *A two-solar-mass neutron star measured using Shapiro delay*, **Nature 467, 1081–1083 (2010)**, DOI **10.1038/nature09466**; versioned author manuscript `arXiv:1010.5788v1`.[13][14][15]

The manuscript says:

> “The implied pulsar mass of `1.97±0.04 M_sun` is by far the highest yet measured with such certainty.”[15]

The paper uses MCMC to derive posterior distributions, says the pulsar-mass posterior is very well described by a normal distribution, and identifies the quoted table uncertainties as 1-sigma.[15]

The center is **1.97**, below strict 2.00.[15] Its 1-sigma interval is **1.93–2.01**, so it crosses 2.00 rather than clearing it.[15]

### 5.3 PSR J0740+6620 — Fonseca et al. 2021

E. Fonseca et al., *Refined Mass and Geometric Measurements of the High-mass PSR J0740+6620*, **The Astrophysical Journal Letters 915, L12 (2021)**, DOI **10.3847/2041-8213/ac03b8**; versioned author manuscript `arXiv:2104.00880v2`.[16][17][24]

The abstract says:

> “the pulsar mass `m_p = 2.08^{+0.07}_{-0.07} M_sun` (68.3% credibility) [was] determined by the relativistic Shapiro time delay.”[16][18][24]

The result is a model-averaged Bayesian posterior.[18][24]

The 68.3% interval is **2.01–2.15**, entirely above 2.00.[18][24]

The paper separately gives a **95.4% lower bound of 1.95 M_sun**, so the mass does not clear strict 2.00 at 95.4% credibility.[18][24]

### 5.4 Threshold-to-measurement verdict

| Source/result | Center versus strict 2.00 | Quoted interval versus strict 2.00 | Relation to Brown et al.'s `≳ 2` wording |
|---|---:|---:|---|
| Demorest: `1.97±0.04` | below | 1-sigma 1.93–2.01 crosses | approximately 2; does not strictly clear by center or full 1-sigma interval.[15] |
| Fonseca: `2.08+0.07/-0.07` | above | 68.3% 2.01–2.15 clears; 95.4% lower bound 1.95 does not | clearly enters the approximate-2 regime; clears strict 2 only at the quoted 68.3% level.[18][24] |

**Claim (4): SUPPORTED.** The current packet accurately says the measurements **enter Brown–Lee–Rho's approximate-2-solar-mass regime**.[9][12]

It accurately distinguishes Demorest's central value from Fonseca's 68.3% versus 95.4% result.[15][18][24]

It correctly refuses to adjudicate whether Brown et al.'s “serious doubt or simply falsify” disjunction lands on one side or the other.[9][12][22]

The packet would overstate only if it said “CNS is definitively falsified,” “both measurements strictly exceed 2,” or “the entire quoted uncertainty range clears 2.”[9][15][18]

It no longer says those things.[9][15][18]

## 6. Comparison with the prior Tori receipt

The fresh check **reproduced the prior receipt independently** on every load-bearing point:

1. v1/v2 version history is material;[1][3][6]
2. v2 contains axis mechanics, equations, scales, functions, post-hoc numbers, and qualitative orientation claims;[6]
3. the defensible absence is the narrow lack of a calibrated handedness target, independent axis, lower bound, and numerical acceptance region;[6]
4. the exact Brown relation is `≳`, and Brown et al.'s consequence is disjunctive;[10][12][23]
5. Demorest does not clear strict 2 by center, while Fonseca clears it at 68.3% but not 95.4%; and[15][18][24]
6. a dated “no journal version located” is supportable, while an unbounded all-successors claim is not.[7][19][21]

I do **not** disagree with my earlier receipt on those findings.[3][6][12]

The earlier receipt was right to fail the predecessor packet's broad “no numbers/forms” and overstrong falsification wording.[6][9][12]

The current packet has incorporated those substantive repairs.[6][15][18]

The fresh check adds three precision notes not needed to preserve the closure: replace the remaining broad line-336 scoring sentence with explicitly numerical wording; source or narrow `1.5–1.6` to Brown et al.'s `~1.5`; and prefer “source-backed qualitative claim” over the potentially over-flattering “real prediction.”[6][9][12]

## 7. What resolved and what did not

### Resolved directly

- Both immutable arXiv versions, PDFs, and source archives resolved.[1][4][6]
- The arXiv API, DataCite DOI record, INSPIRE record, and exact Crossref query resolved.[7][20][21]
- Brown–Lee–Rho's APS version of record and Publisher's Note resolved through the official APS harvest full-text endpoint.[22][23]
- Demorest's Nature DOI landing page and versioned author manuscript resolved.[13][14][15]
- Fonseca's IOP version of record, DOI, and versioned author manuscript resolved.[16][17][24]

### Did not resolve cleanly; not used as authority

- `https://api.semanticscholar.org/graph/v1/paper/ARXIV:1910.10819?...` returned HTTP 429.
- The local ADS API request for `identifier:1910.10819` returned HTTP 401; no ADS conclusion was drawn.
- `https://www.nikodempoplawski.com/publications.html` currently resolves only to an “Under Construction” page.
- OpenAlex's lookup for DOI `10.48550/arXiv.1910.10819` returned a contaminated/mismatched title for another 2026 preprint; it was rejected as unreliable for this audit.
- The ordinary APS abstract extraction dropped the corrected math glyph. The glyph was recovered from the versioned TeX macro and visually checked in the one-page Publisher's Note PDF.[10][12][23]

## 8. Exact DOI and version bindings

1. Nikodem Popławski, *Black Hole Genesis and origin of inertia*, **arXiv:1910.10819v1**: https://arxiv.org/abs/1910.10819v1; PDF https://arxiv.org/pdf/1910.10819v1; source https://export.arxiv.org/e-print/1910.10819v1.[1][2][3]
2. Nikodem Popławski, *Universe in a rotating black hole and preferred axis*, **arXiv:1910.10819v2**: https://arxiv.org/abs/1910.10819v2; PDF https://arxiv.org/pdf/1910.10819v2; source https://export.arxiv.org/e-print/1910.10819v2; arXiv/DataCite DOI https://doi.org/10.48550/arXiv.1910.10819.[5][6][8]
3. G. E. Brown, Chang-Hwan Lee, and Mannque Rho, *Kaon Condensation, Black Holes, and Cosmological Natural Selection*, **PRL 101, 091101 (2008)**, DOI https://doi.org/10.1103/PhysRevLett.101.091101; APS full text https://harvest.aps.org/v2/journals/articles/10.1103/PhysRevLett.101.091101/fulltext; author source `arXiv:0802.2997v2` https://export.arxiv.org/e-print/0802.2997v2.[9][11][22]
4. G. E. Brown, Chang-Hwan Lee, and Mannque Rho, *Publisher's Note...*, **PRL 101, 119901 (2008)**, DOI https://doi.org/10.1103/PhysRevLett.101.119901; APS full text https://harvest.aps.org/v2/journals/articles/10.1103/PhysRevLett.101.119901/fulltext.[10][23]
5. P. B. Demorest et al., *A two-solar-mass neutron star measured using Shapiro delay*, **Nature 467, 1081–1083 (2010)**, DOI https://doi.org/10.1038/nature09466; `arXiv:1010.5788v1` https://arxiv.org/abs/1010.5788v1; source https://export.arxiv.org/e-print/1010.5788v1.[13][14][15]
6. E. Fonseca et al., *Refined Mass and Geometric Measurements of the High-mass PSR J0740+6620*, **ApJL 915, L12 (2021)**, DOI https://doi.org/10.3847/2041-8213/ac03b8; IOP PDF https://iopscience.iop.org/article/10.3847/2041-8213/ac03b8/pdf; `arXiv:2104.00880v2` https://arxiv.org/abs/2104.00880v2; source https://export.arxiv.org/e-print/2104.00880v2.[16][17][24]

## Final custody statement

The campaign's narrow closing claim is now citation-safe: **the v2 axis paper contains a qualitative unequal-count claim but no calibrated BHU-specific handedness target or finite-precision numerical acceptance region.**[6]

The neutron-star chain is accurately described as entering Brown–Lee–Rho's approximate-2-solar-mass “serious doubt or simply falsify” regime without adjudicating that disjunction.[9][15][18]

The whole Lana packet should remain **HOLD_FOR_TWO_MICRO_REPAIRS** rather than “fully clean” until line 336 is narrowed to numerical scoring and the two `1.5–1.6 M_sun` instances are either sourced or changed to Brown et al.'s `~1.5 M_sun`.[6][9][12]

The “real prediction” wording is defensible only with its existing post-hoc/qualitative qualification and is better rewritten less generously.[4][6]

Nothing is published or accepted. Duho decides; Kun re-gates separately.

## Sources

[1] https://arxiv.org/abs/1910.10819v1
[2] https://arxiv.org/pdf/1910.10819v1
[3] https://export.arxiv.org/e-print/1910.10819v1
[4] https://arxiv.org/abs/1910.10819v2
[5] https://arxiv.org/pdf/1910.10819v2
[6] https://export.arxiv.org/e-print/1910.10819v2
[7] https://export.arxiv.org/api/query?id_list=1910.10819
[8] https://doi.org/10.48550/arXiv.1910.10819
[9] https://doi.org/10.1103/PhysRevLett.101.091101
[10] https://doi.org/10.1103/PhysRevLett.101.119901
[11] https://arxiv.org/abs/0802.2997v2
[12] https://export.arxiv.org/e-print/0802.2997v2
[13] https://doi.org/10.1038/nature09466
[14] https://arxiv.org/abs/1010.5788v1
[15] https://export.arxiv.org/e-print/1010.5788v1
[16] https://doi.org/10.3847/2041-8213/ac03b8
[17] https://arxiv.org/abs/2104.00880v2
[18] https://export.arxiv.org/e-print/2104.00880v2
[19] https://api.datacite.org/dois/10.48550/arXiv.1910.10819
[20] https://inspirehep.net/api/arxiv/1910.10819
[21] https://api.crossref.org/works?query.title=Universe%20in%20a%20rotating%20black%20hole%20and%20preferred%20axis&query.author=Poplawski&filter=from-pub-date:2019-01-01&rows=20
[22] https://harvest.aps.org/v2/journals/articles/10.1103/PhysRevLett.101.091101/fulltext
[23] https://harvest.aps.org/v2/journals/articles/10.1103/PhysRevLett.101.119901/fulltext
[24] https://iopscience.iop.org/article/10.3847/2041-8213/ac03b8/pdf
