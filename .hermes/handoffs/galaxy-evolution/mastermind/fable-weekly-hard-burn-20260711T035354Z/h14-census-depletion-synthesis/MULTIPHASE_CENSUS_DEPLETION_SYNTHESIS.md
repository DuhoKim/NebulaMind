FABLE_HARD_BURN_H14_SYNTHESIS_20260711T035354Z

# Deep synthesis: multiphase census (m3_p1) + gas depletion efficiency (m3_p2)

Burn `fable-weekly-hard-burn-20260711T035354Z` · lane H14 · written 2026-07-11T04:32Z (UTC) · fully offline.
Inputs: hash-pinned snapshots only (all 9 sha256 recomputed and matched before reading; custody table in `H14_RECEIPT.md`). H5 owns value-level verification; this document is the deep synthesis. All arithmetic below reproduced by `tools/joint_crosscheck.py` (offline, reads the two snapshot JSONs only).

Convention note (binding, from `RCA_NUMERIC_DRIFT.md`): canon numerals are carried **verbatim**; grade-B derivations below are shown as evidence the canon string equals the nearest-rounding of the raw artifact value — they are *not* license to re-derive in prose. Neither RCA anomaly (`FLG-CI95`, `SUP-ROW-188`) involves either of these topics.

---

## 1. Artifact anatomy

### 1A. `m3_p1_multiphase_census/analysis_results.json` (sha256 `e71156…0683`, 2,375 bytes)

**Design in plain language.** One fixed 60,000-galaxy SDSS DR17 optical-emission-line sample (the same cache as the flagship; `source_sample` = `SDSS_AGN_SFR_PILOT_20260708T122000Z/data/analysis_sample_bpt.csv`, run `SDSS_REMAINING_TOPIC_PILOTS_20260708T125828Z`). Five *simple optical tracer definitions* of "AGN/feedback candidate" are each applied to that **same common denominator**, and the pilot statistic is the per-definition prevalence k/n with binomial standard error. The point measured is methodological: how much the inferred candidate prevalence moves when only the tracer definition changes, before any molecular/neutral/X-ray/radio phase is added. It is a tracer-*threshold* census, not a multiphase census — the multiphase part is the proposal (`full_proposal_requires`: "ionized, molecular, neutral, and X-ray/radio tracers measured over the same parent denominator and aperture model").

**Every field.** `card_id` p1; `slug`; `short_title` "Common-denominator optical tracer census in SDSS"; `proposal_title` "A multiphase, common-denominator census of AGN-driven outflows"; `pilot_question` (verbatim in JSON); `method` "debate-map-to-wiki-rebuild"; `run_id`; `source_sample` (path into live runs tree — pointer only, **not** followed per snapshot-only directive); `figure_pdf` (pointer, not followed); `sample_rows` 60000; `interpretation_guard` (SDSS-only pilot); `full_proposal_requires`; `result_bullets` (3); `prevalence_ratio_widest_to_narrowest` 3.080775840903511; `tracer_prevalence` (5 entries, each {fraction, k, n, se}).

**Every numeric, with units and role** (all fractions dimensionless on the common n = 60,000 denominator; k = count, galaxies; se = binomial standard error of the fraction):

| tracer definition | k | fraction | se | role |
|---|---|---|---|---|
| BPT AGN | 8,146 | 0.135767 | 0.001398 | narrowest tracer; anchors "0.136" |
| high [NII]/Hα | 11,497 | 0.191617 | 0.001607 | intermediate |
| low-sSFR+emission | 12,410 | 0.206833 | 0.001654 | intermediate; nearest kin to p2's subset |
| high [OIII]/Hβ | 19,019 | 0.316983 | 0.001900 | intermediate |
| red+emission | 25,096 | 0.418267 | 0.002014 | widest tracer; anchors "0.418" |
| ratio widest/narrowest | — | 3.0807758… | — | anchors "3.1" |

**Unit audit (recomputed, all OK).** Every stored fraction equals k/n to ≤1e−12; every stored se equals √(p(1−p)/n) to ≤1e−9; stored ratio equals 0.418267/0.135767 to ≤1e−9. The five fractions are **not a partition**: Σ fractions = 1.2695 (Σk = 76,168 > 60,000). That is dimensionally sensible — the five definitions are overlapping selections on one denominator, so the sum has no unit meaning beyond mean labels/galaxy; it *does* imply a guaranteed overlap of ≥ Σk − 60,000 = 16,168 label assignments even if every galaxy carried at least one label. No timescales or luminosities appear in this artifact; nothing to check dimensionally beyond fractions ∈ [0,1] (all are).

### 1B. `m3_p2_gas_depletion_efficiency/analysis_results.json` (sha256 `429656…c9d9` per brief pin `42965b…c9d9`, 2,101 bytes)

**Design in plain language.** Same 60,000-galaxy parent (`sample_rows` 60000, same `run_id`, same `source_sample`). The pilot carves the **massive transition/quenched** subset with valid emission-line measurements — 6,729 galaxies — as the *denominator for future CO gas-fraction / depletion-time follow-up*, and characterizes it optically three ways: its broad optical BPT AGN fraction (3,692/6,729 = 0.5487 ± 0.0061), its median aperture-corrected Hα-luminosity proxy (median log₁₀(L_Hα/erg s⁻¹) = 40.0612), and that median's offset from massive star-forming emission-line galaxies (−0.6586 dex). The statistic is deliberately *not* a depletion time — SDSS optics cannot separate gas depletion from suppressed star-formation efficiency (`result_bullets[3]`, `interpretation_guard`); the artifact's product is the denominator plus an optical baseline.

**Every field.** `card_id` p2; `slug`; `short_title` "Optical denominator for gas-fraction versus efficiency tests"; `proposal_title` "Distinguishing molecular-gas depletion from suppressed star-formation efficiency in quenched galaxies"; `pilot_question`; `method`; `run_id`; `source_sample` (pointer, not followed); `figure_pdf` (pointer, not followed); `sample_rows` 60000; `massive_transition_quenched_rows` 6729; `agn_fraction_in_denominator` {fraction 0.5486699…, k 3692, n 6729, se 0.0060663…}; `median_log_lha_denominator` 40.06117405071403; `median_log_lha_offset_vs_massive_sf` −0.6585859816891073; `interpretation_guard`; `full_proposal_requires` ("CO or dust-based molecular gas masses, aperture-matched SFRs, morphology, and environment labels"); `result_bullets` (4).

**Every numeric, with units and role:**

| quantity | value | unit | role |
|---|---|---|---|
| massive_transition_quenched_rows | 6,729 | galaxies | CO follow-up denominator; anchors "6,729" |
| parent sample_rows | 60,000 | galaxies | common parent shared with p1 |
| AGN k, n | 3,692 / 6,729 | galaxies | BPT AGN inside subset |
| AGN fraction | 0.5486699… | dimensionless | anchors "0.549" |
| AGN se | 0.0060663… | dimensionless | binomial error |
| median log L_Hα | 40.06117… | log₁₀(erg s⁻¹) | optical SFR-proxy baseline; anchors "40.061"/"40.06" |
| offset vs massive SF | −0.65858… | dex | anchors "0.66 dex lower"; sign stored negative, prose says "lower" — consistent |

**Unit audit (recomputed, all OK).** 3692/6729 = 0.5486699… matches stored to ≤1e−12; se matches √(p(1−p)/n) to ≤1e−9; 6,729 ≤ 60,000 (0.1121 of parent); log L_Hα ≈ 40.06 → L_Hα ≈ 1.15×10⁴⁰ erg s⁻¹, a physically plausible aperture-corrected value for massive low-excitation galaxies; the offset is a difference of log₁₀ medians (dex, dimensionless) — coherent. **No efficiency or timescale is stored anywhere in the artifact** — dimensional coherence of "depletion efficiency" is vacuously satisfied and any timescale appearing in prose would be unbacked (none does; §3).

---

## 2. Claim inventory (cycle-5 supplement + flagship)

Grades: **A** = numeric/text string stated verbatim in the artifact (usually `result_bullets`); **B** = canon string is the nearest-rounding of a raw artifact field (derivation shown; RCA convention); **C** = consistent with artifacts but not independently checkable from the pinned inputs; **X** = unbacked. Manifest IDs from `INVARIANT_MANIFEST.json` (105 entries; 12 touch these topics).

### 2A. m3_p1 — supplement `supplementary_denominator_atlas.tex`

| # | claim (verbatim) | line | artifact field(s) | manifest | grade |
|---|---|---|---|---|---|
| P1-1 | "Tracer census & tracer prevalence in 60k sample (0.136 to 0.418)" | 64 | tracer_prevalence min/max fractions | SUP-ROW-064, SUP-TRACER-LO, SUP-TRACER-HI | **A** (strings in bullets[0]) + B: 0.1357666→3dp→0.136; 0.4182666→3dp→0.418 |
| P1-2 | "Within the same 60,000-galaxy denominator, simple optical tracer definitions produce prevalence from 0.136 to 0.418." | 147 | result_bullets[0] (verbatim), n=60000 | SUP-TRACER-LO/HI (lines [64,147]) | **A** |
| P1-3 | "The widest-to-narrowest prevalence ratio is 3.1 before adding molecular, neutral, X-ray, or radio phases." | 147 | prevalence_ratio… 3.0807758; result_bullets[1] | SUP-TRACER-RATIO (numeric_token, line 147) | **A** via bullet + B: 3.0807758→1dp→3.1. Wording drift vs bullet ("molecular, neutral, or X-ray/radio") — cosmetic, non-numeric |
| P1-4 | "This demonstrates why a common-denominator multiphase census is required; it does not measure molecular or neutral outflow rates." | 147 | result_bullets[2] | — (non-numeric) | **A** |
| P1-5 | "The follow-up ingredients are ionized, molecular, and neutral tracers, X-ray or radio tracers, a shared parent denominator, and a consistent aperture model." | 147 | full_proposal_requires | — | **A** (restatement) |
| P1-6 | provenance row: `m3_p1…/analysis_results.json` + SHA `e711…0683` | 44 | file itself | SUP-ROW-044 | **A** (SHA recomputed = pinned = printed) |
| P1-7 | "Tracer census & multiphase tracers; shared denominator; aperture model" (follow-up table) | 81 | full_proposal_requires | — | **A** |

### 2B. m3_p2 — supplement

| # | claim (verbatim) | line | artifact field(s) | manifest | grade |
|---|---|---|---|---|---|
| P2-1 | "Gas depletion & gas-depletion low-sSFR baseline; H$\alpha$ proxy (6,729 galaxies)" | 65 | massive_transition_quenched_rows | SUP-ROW-065, SUP-GAS-N | count **A**; label "low-sSFR baseline" **C** — see tension T1 |
| P2-2 | "the massive low-sSFR denominator contains 6,729 galaxies in the SDSS emission-line sample" | 158 | rows=6729; bullets[0] says "massive transition/quenched denominator" | SUP-GAS-N (lines [65,158]) | count **A**; renaming **C** (T1) |
| P2-3 | "Its broad optical BPT-selected fraction is 0.549" | 158 | agn_fraction… 0.5486699; bullets[1] "0.549" | SUP-GAS-BPT | **A** + B: 0.5486699→3dp→0.549 |
| P2-4 | "the median H-alpha luminosity proxy is log(L_Hα/erg s⁻¹) = 40.061" | 158 | median_log_lha 40.0611740 | SUP-GAS-LHA | **B**: 40.0611740→3dp→40.061 (bullet carries 2dp "40.06"; prose 3dp comes from the raw field, clean nearest-rounding) |
| P2-5 | "The median H-alpha luminosity proxy is 0.66 dex lower than in massive star-forming emission-line galaxies." | 158 | offset −0.6585860; bullets[2] "-0.66 dex offset" | SUP-GAS-DEX (numeric_token) | **A** via bullet + B: |−0.6585860|→2dp→0.66; sign/direction consistent ("lower" = negative offset) |
| P2-6 | "This denominator is note-specific and should not be conflated with the log M⋆≥10.8 maintenance-heating subset" | 158 | (cross-note guard; m1_rp3 has 9,298/5,695) | — | **A** (definitional guard; numerically supported: 6,729 ≠ 5,695 ≠ 9,298) |
| P2-7 | "SDSS optical data alone cannot distinguish bulk molecular-gas depletion from localized reductions in star-formation efficiency or measure total cold-gas mass" | 158 | result_bullets[3], interpretation_guard | — | **A** |
| P2-8 | aperture-corrected galSpecExtra proxy / no IMF conversion / no α_CO conversion performed / Balmer-decrement dust model | 158 | consistent with artifact's optical-only content (no gas mass, no conversion fields present) | — | **A/C** (accurate description of what the artifact does *not* contain; the catalog-provenance details themselves are not in the JSON — C, but risk-free guards) |
| P2-9 | provenance row: `m3_p2…/analysis_results.json` + SHA `4296…c9d9` | 45 | file itself | SUP-ROW-045 | **A** (SHA recomputed = pinned = printed) |

### 2C. Both topics — flagship `rp1_flagship_polished.tex`

The flagship **never uses either topic's numbers**. It references the topics only as negative scope, and those claims are consistent with both artifacts:

| # | claim (verbatim excerpt) | line | grade |
|---|---|---|---|
| F-1 | "…not a causal feedback, physical-quenching, gas-depletion, or population-abundance measurement." | 13 | **A** (scope; matches p2 guard) |
| F-2 | "does not test feedback-related quenching scenarios, molecular gas depletion, radio-mode maintenance heating, or outflow escape/recycling in this dataset" | 19 | **A** (scope) |
| F-3 | "It is not a volume-complete census" | 25 | **A** (scope; matches p1 guard) |
| F-4 | "the preferred custody-backed comparison yields 8,146 pairs" | 13 | **A**, and jointly load-bearing: 8,146 = p1's BPT AGN k exactly (§3, C3) |

**No X-grade claims found** for either topic: every numeric string in the supplement's two subsections is either verbatim from `result_bullets` or a clean nearest-rounding of a raw field, and each carries the required guard.

---

## 3. Joint synthesis — are census and depletion mutually consistent?

**Verdict: mutually consistent; zero numeric tension; one naming tension.** The two artifacts share one parent denominator by construction, their only overlapping statistic (BPT AGN) nests correctly, and the prose never combines them numerically — so there is no combined claim to break. All joint numbers below are **new** (computed here, offline) and are *not* canon; promoting any of them into prose is a canon change (GATED).

### Consistency table

| # | cross-check | arithmetic | verdict |
|---|---|---|---|
| C1 | shared parent | p1.sample_rows = p2.sample_rows = 60,000; same run_id; same source_sample path | **agrees** |
| C2 | BPT AGN nesting | subset AGN 3,692 ≤ census AGN 8,146 (necessary condition for p2-subset ⊂ 60k parent with same BPT rule); implied joint share: 3,692/8,146 = **45.3%** of all census BPT AGN sit inside the 6,729 CO-target denominator | **agrees** (share is new, not prose-backed) |
| C3 | flagship linkage | census BPT AGN k = 8,146 = flagship matched-pair count 8,146 (flagship line 13; manifest FLG-family + SUP-SHA-RESULTS ties both to `668ad7…d659df`) — three artifacts agree the BPT AGN class has exactly 8,146 members | **agrees** |
| C4 | census total vs depletion denominator (brief's "census totals vs depletion denominators") | 6,729 ≤ 12,410 (low-sSFR+emission tracer) and ≤ 25,096 (red+emission): necessary nesting conditions hold; if the transition/quenched cut implies the low-sSFR tracer cut, the subset is 54.2% of that tracer class. Row-level nesting is **not decidable** from summary JSONs | **agrees** as necessary condition; row-level check GATED |
| C5 | AGN enhancement vs mass trend | subset AGN fraction / census AGN prevalence = 0.5487/0.1358 = **4.04×**; sanity vs m3_p3 mass–z vector (supplement Table 4, massive bins 10.5–12.5 span BPT fractions 0.209–0.610): 0.549 falls inside the massive-bin bracket | **agrees** |
| C6 | implied depletion-timescale factor (brief's "implied depletion timescales from combining the two") | Hα-proxy offset −0.6586 dex → suppression factor 10^0.6586 = **4.556×** (canon-2dp form 10^0.66 = 4.571×). t_dep ≡ M_gas/SFR ⇒ Δlog t_dep = Δlog M_gas − Δlog SFR. With Δlog SFR-proxy = −0.6586: **pure-efficiency limit** (Δlog M_gas = 0): t_dep is 4.56× longer in the quenched subset; **pure-depletion limit** (Δlog t_dep = 0): M_gas is 4.56× lower. Every mixed case sits on Δlog M_gas = Δlog t_dep − 0.6586. Neither artifact stores a timescale, so 4.56× is a **degeneracy budget**, not a measurement — exactly the degeneracy p2's proposal is designed to split with CO | **independent** (no counterpart in p1 to contradict; arithmetic internally coherent) |
| C7 | tracer-choice propagation into CO targeting | p1's 3.08× prevalence spread means the *candidate* population feeding any outflow-driven-depletion interpretation changes by up to 3.08× with tracer definition; within the 6,729 subset the one measured tracer (BPT) already labels 54.9% — the census warns that another defensible tracer could label a very different subset share | **independent** (census bounds the ambiguity; no contradiction) |
| C8 | does prose combine them anywhere? | Searched supplement + flagship: the two subsections cross-reference only via the shared-limitations section and the m1_rp3 conflation guard (line 158). **No sentence combines a p1 number with a p2 number.** The only cross-topic numeric identity in canon is the implicit 8,146 (C3) | **independent by design** — and safe: every combined number is confined to this lane |

### Tension list

- **T1 (naming, C-grade).** The artifact names the 6,729 subset "massive **transition/quenched**" (field name, `pilot_question`, `result_bullets[0]`); the supplement calls it "gas-depletion **low-sSFR** baseline" (line 65) / "massive **low-sSFR** denominator" (line 158). No number conflicts, and line 158 already guards against conflation with the m1_rp3 log M⋆≥10.8 low-sSFR subset (5,695) — but the label collision is real: three distinct "massive low-sSFR-ish" counts now circulate (5,695; 6,729; 9,298). If "transition/quenched" is not literally the low-sSFR tracer cut restricted to massive hosts, the supplement's label is loose. Fix is a one-line vocabulary note; that is a **canon change — GATED** (verbatim-carry rule forbids inline fixing).
- **T2 (precision mixing, informational).** Bullet carries 40.06 (2dp); prose canon carries 40.061 (3dp). Both are clean nearest-roundings of 40.0611740; the manifest pins 40.061. No action — verbatim-carry protects it.
- **T3 (overlap not stated, informational).** The five p1 tracer sets overlap (Σk = 76,168 > 60,000; guaranteed ≥16,168 multi-labeled assignments), but the prose never says the definitions are non-exclusive. A hurried reader could misread the census as a partition. Optional clarifying clause — canon change, GATED.
- **No numeric tension.** All six topic canon strings (0.136, 0.418, 3.1, 6,729 with 0.549, 40.061, 0.66) are exact nearest-roundings of the pinned artifacts — these two topics contribute nothing to the RCA drift class.

---

## 4. Confounders

### m3_p1 (census)

| confounder | status |
|---|---|
| Tracer completeness (each optical cut has different EW/S-N sensitivity; four-line S/N≥3 parent already biased against passive systems) | **Partially addressable now**: per-tracer k,n,se quantify the statistical piece; the 3.08× spread *is* the completeness-sensitivity demonstration. Selection-function decomposition per tracer → **requires new run (GATED)** |
| Aperture | **Addressable now (argument)**: all five tracers are computed on the same 3-arcsec-fiber quantities over the same denominator, so the *ratio* 3.08 is internally aperture-consistent. Any global (non-fiber) prevalence → IFU/aperture model → **GATED** (artifact `full_proposal_requires`) |
| Conversion factors (α_CO-like) | **Addressable now (vacuous)**: no conversion is used anywhere in the optical pilot; molecular/neutral phases are explicitly deferred. Carry the guard verbatim |
| Sample overlap between tracer sets | **Not in artifact** (marginals only). Lower bound derivable offline: ≥16,168 overlapping label assignments (Σk − n). Full 5×5 overlap matrix → row-level re-run on the retained CSV → **GATED (runner)** |

### m3_p2 (depletion/efficiency)

| confounder | status |
|---|---|
| Phase tracer completeness (Hα proxy only; no CO/HI/dust) | **GATED by design**: `full_proposal_requires` CO/dust masses; the artifact's whole point is that the optical pilot cannot close this |
| Aperture (catalog aperture-corrected L_Hα extrapolates the fiber model-dependently; SFR aperture-matching absent) | **Addressable now (guard)**: supplement line 158 states the proxy provenance; aperture-matched SFRs → **GATED** |
| α_CO-like conversion assumptions | **Addressable now (vacuous + stated)**: no CO→H₂ conversion performed (line 158, with bolatto2013 as future requirement); Kroupa-IMF catalog scale noted for future M_gas/M⋆ — any actual conversion → **GATED** |
| Sample overlap (with p1 tracer classes; with m1_rp3 subset) | BPT overlap quantified in-artifact (3,692). Overlap with the other four tracers and with the 5,695/9,298 m1_rp3 subsets → row-level → **GATED (runner)** |
| Dust/Balmer-decrement model dependence of the Hα proxy | **Addressable now (guard)**: stated in canon (Charlot & Fall prescription); residual systematics flagged. Quantifying → new data → **GATED** |

---

## 5. Falsifiable predictions and next analyses (dependency-ordered)

**P0 — row-level cross-tab (first; unlocks everything; GATED: runner re-run on retained 60k CSV — the `source_sample` path points into the live runs tree, which this lane did not touch).**
Cross-tabulate the 6,729 subset against the five tracer sets. Falsifiable predictions: (a) |subset ∩ BPT AGN| = 3,692 exactly — failure would falsify artifact-internal consistency; (b) if the supplement's "low-sSFR baseline" label is right, subset ⊆ low-sSFR+emission (12,410) — a single counterexample row falsifies the label and forces the T1 vocabulary fix; (c) prevalence-enhancement ordering: subset-conditional enhancement should fall monotonically with base prevalence, from 4.04× (BPT) down to ≤2.39× (red+emission ceiling, since 1/0.4183 = 2.39).

**P1 — split the 4.56× budget (needs CO, xCOLD-GASS-depth; GATED: external data/network).**
Mass-matched CO of the AGN half (0.549) vs non-AGN half of the 6,729. If AGN-driven **depletion** dominates: gas fractions in the subset ≥ ~4.6× below massive-SF controls with t_dep roughly preserved, and the AGN half shows the larger gas deficit. If **efficiency suppression** dominates: gas fractions comparable to controls, t_dep longer by ~4.6×, AGN/non-AGN halves indistinguishable in gas fraction. The C6 budget line Δlog M_gas = Δlog t_dep − 0.6586 makes any CO measurement immediately placeable.

**P2 — widen the census to real multiphase (GATED: external survey data per `full_proposal_requires`).**
Measure molecular/neutral/X-ray/radio candidate prevalence over the *same* 60k denominator with one aperture model. Falsifiable: the widest-to-narrowest ratio must be ≥ 3.08 (adding definitions can only widen the envelope); if all added phases land inside [0.136, 0.418], the optical spread was already the full story — informative either way.

**P3 — forward-model consumption (GATED: simulation pipeline).**
Simulations passed through the exact selection (m3_p3 vector as target) must reproduce jointly: BPT-AGN prevalence 0.1358 ± 0.0014 on the full denominator **and** 0.549 ± 0.006 inside the massive transition/quenched cell **and** the −0.66 dex Hα-proxy offset. Reproducing the marginals but not the joint AGN-share (45.3%, C2) would falsify the sim's AGN–quenching coupling.

Ordering rationale: P0 is pure bookkeeping on retained data and validates the denominators; P1 consumes P0's target list and splits the physical degeneracy; P2 fixes the tracer ambiguity that otherwise propagates a 3.08× uncertainty into P1's target selection; P3 needs P0–P2 outputs as its joint target vector.

---

## 6. Stretch item

Not attempted — clock reserved for receipt at 04:40Z. Cycle-6/7 supplement diffs for these two topics remain open (P1 receipt pins the snapshot hashes; RCA §E-items already establish that neither cycle's drift touched the m3 strings).

*End of synthesis. Helper: `tools/joint_crosscheck.py`. Receipt: `H14_RECEIPT.md`.*
