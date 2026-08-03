I've reviewed all three drafts in full. Below is the critique. I verified every arithmetic value in the tables against the abstracts myself; findings noted where relevant. No files written, no commands run.

---

# External read-only critique — Tori Wave-2 result-table drafts (20260708T143512Z)

## A. Overall publish-quality triage

All three are **internally consistent, honestly-guarded denominator/target-vector pilots** — not publishable science papers, and correctly they never claim to be. Arithmetic checks out (see per-paper notes; Paper 3's 15 cells sum to exactly 60,000). The recurring, self-aware "interpretation guard" and reproducibility markers are a genuine strength: the drafts pre-empt the main overclaiming risk.

Triage verdict: **not submission-ready as standalone manuscripts** (expected — they're addenda to source `_aas.tex` files), but **structurally sound enough to integrate** once the shared gaps below are closed. There are **no blocker-level correctness errors** in the numbers I could check. The blockers are all about *missing method/definition disclosure* that would make the tables unusable to an outside reader or unreproducible.

Shared cross-cutting issues (detailed in C):
- **Selection-function attrition never quantified** — parent 60,000 requires S/N≥3 in all four lines; the fraction of the true underlying population dropped is never stated. This is the single most important missing number for every paper.
- **Statistical treatment inconsistent** — Paper 1 has CIs (method unstated); Papers 2 & 3 have none.
- **Literature is method-only** — the 4-item bibliography (BPT, Kauffmann, Kewley, York) is identical across all three and contains zero topical references.
- **Figures are undescribed boilerplate** — identical caption text; the reader cannot tell what `figure1.pdf` shows.
- **Column definitions/units missing** — `log L_Hα`, `f_Q`, `f_high exc.` are undefined.

---

## B. Per-paper

### 1. `m2_p2_radio_jet_environment`

**Arithmetic (verified):** k=5 Δ=0.506−0.368=0.138 ✓; k=10 Δ=0.142 ✓; k=20 Δ=0.152 ✓. Abstract range 0.138–0.152 matches the table.

- **[major] Unequal "quartile" counts unexplained.** Line 34–36: the low-density quartile has *more* massive hosts (2,604/2,746/2,906) than the high-density quartile (1,980/1,864/1,819). If these are density quartiles, why are the massive-host counts unequal — and why does the *low*-density bin hold more massive galaxies, which runs against the usual mass–density relation? This needs one sentence of explanation (quartiles defined on the full sample, then massive-host subset counted) or it reads as an error.
- **[major] The three rows are not independent confirmations.** Lines 34–36 re-bin the *same* massive hosts under k=5/10/20; the abstract's "scale-robust" (line 17) and "stable across the three internal density rankings" (line 28) imply independent corroboration. They are correlated re-measurements — legitimate as a robustness check, but the wording overstates it. Downgrade "robust" to "insensitive to neighbour-count choice."
- **[major] CI method unstated.** Line 34–36 give `[low, high]` intervals with no stated construction (Wilson / binomial / bootstrap) and no p-value or significance statement. An outside reader can't reproduce or weight them.
- **[minor] "Radio-jet" in title/abstract with zero radio data.** The scope paragraph (line 23) and interpretation guard (line 49) handle this well, but the title (line 12) plus keyword `galaxies: active` could still let a casual reader think jet coupling was measured. The guard language is adequate; flagging as residual risk only.
- **Next steps:** state CI method; explain the quartile-count asymmetry; add ≥1 topical citation (e.g. a radio-AGN/environment reference the integrator supplies — do not invent one); describe the figure.

### 2. `m3_p2_gas_depletion_efficiency`

**Arithmetic (verified):** 5,229/10,270=0.509 ✓; 4,822/8,400=0.574 ✓; 3,692/6,729=0.549 ✓; 3,459/5,695=0.607 ✓; 1,999/3,334=0.600 ✓; 1,909/2,941=0.649 ✓. Abstract denominator range 2,941–10,270 matches.

- **[blocker] Emission-line selection guts the "quenched" denominator, and this is not quantified.** The sample requires S/N≥3 in Hα, Hβ, [O III], [N II] (line 25), yet the rows select *low-sSFR / quenched* hosts. Quenched galaxies are precisely those most likely to *lack* detectable emission lines, so this "denominator for CO/dust follow-up" is a strongly biased sub-population (emission-line-retaining quenched galaxies), not the quenched population a gas-follow-up target list would want. The draft must state what fraction of massive low-sSFR galaxies were removed by the S/N cut, or explicitly redefine the denominator as "emission-line-detected massive low-sSFR galaxies."
- **[major] BPT AGN fractions of 0.51–0.65 are a selection artifact, presented without that caveat.** Lines 34–39: these very high AGN fractions follow directly from requiring 4-line S/N≥3 in low-sSFR hosts (LINER/AGN-like line ratios dominate). The `\tablecomments` (line 41) only caveats the Hα column, not the AGN-fraction column. Add a caveat that the AGN fraction is conditioned on emission-line detection.
- **[major] `Median log L_Hα proxy` has no units and no definition.** Line 32/34–39: "40.03" — presumably log(erg s⁻¹), but unstated; and "proxy" of what is not defined. Blocks reuse.
- **[minor] No CIs on any column**, unlike Paper 1 — inconsistent with sibling drafts.
- **Next steps:** report parent→denominator attrition; add the AGN-fraction selection caveat; give units; add xCOLD GASS / gas-depletion topical citation (integrator-supplied).

### 3. `m3_p3_simulation_validation`

**Arithmetic (verified):** 15 cells sum to exactly 60,000 ✓. f_Q min 0.001 / max 0.856 and f_BPT_AGN min 0.001 / max 0.610 match the abstract (lines 17 vs 35–49). This is the cleanest of the three.

- **[major] Core columns undefined.** `f_Q` (quenched — by what sSFR or color cut?), `f_high exc.` (high-excitation — undefined entirely), and `median u−r` (units/rest-frame? k-corrected?) have no definitions anywhere (lines 33, 51). For a "target vector simulations must reproduce," the definitions *are* the product; without them the table is not reusable.
- **[major] Smallest cells are statistically thin and uncaveated.** The 11.0–12.5 / 0.02–0.05 cell (line 47) has N=390 driving the headline f_Q=0.856, f_AGN=0.610 max values quoted in the abstract; the 8.0–9.5 / 0.08–0.12 cell (line 37) has N=300. No per-cell uncertainty is given, so a simulation "matching" these to 3 decimals would be over-fitting noise. Add per-cell N-based errors or a minimum-N flag.
- **[minor] Three-decimal precision oversells resolution** (e.g. 0.001, 0.007) for cells where N implies ~±0.005 or worse. Round to significance or attach errors.
- **[minor] Selection-function caveat is present (line 51) and good**, but the same "before mocks are passed through selection/aperture/noise" list should be tied to the missing definitions of f_Q/f_high exc. so a modeller knows exactly what to reproduce.
- **Next steps:** define every column; add per-cell uncertainties or an N-threshold flag; add a simulation-suite topical citation (integrator-supplied); describe the figure.

---

## C. Cross-paper recommendations for the integrator

1. **[blocker, shared] Report the selection-function attrition once, prominently.** All three inherit the same parent (60,000 at 4-line S/N≥3). State how many galaxies the S/N cut removed from the underlying SDSS DR17 population, so every "denominator" and "target vector" carries its representativeness caveat. Most acute for Paper 2 (quenched hosts).
2. **[major, shared] Harmonize statistical treatment.** Either add CIs to Papers 2 & 3 or state why they're omitted; and standardize the CI construction (name the method) so Paper 1's intervals are reproducible. Pick one convention across the wave.
3. **[major, shared] Provide a real column-definitions block.** A shared glossary defining `f_Q`, `f_BPT AGN`, `f_high exc.`, `log L_Hα proxy` (with units), density-quartile construction, and "massive host" cuts would fix multiple per-paper blockers at once, since the definitions are common.
4. **[major, shared] The 4-reference bibliography is identical and topical-literature-free.** Each paper needs a small topical reference set (radio-AGN/environment; molecular-gas depletion; feedback simulations). **Do not synthesize these — the integrator must supply real citations**; the drafts correctly avoid inventing them, so keep that discipline.
5. **[major, shared] Figures are undescribed.** Identical boilerplate captions (Paper1 line 44, Paper2 line 47, Paper3 line 57) plus absolute local `\graphicspath` (line 7 in each) means (a) a reader learns nothing about the figure and (b) the path won't resolve off this machine. Add per-figure descriptive captions and a relative/portable graphics path before any merge.
6. **[minor, shared] Cross-consistency check available for free.** Papers 1–3 share the 60,000-galaxy parent, so overlapping massive-host BPT AGN fractions (P1 high-density ~0.51; P2 logM≥10.8 ~0.55; P3 massive bins ~0.43–0.61) should be internally reconcilable. A short appendix or integrator note confirming they agree where selections overlap would strengthen the whole wave.
7. **[minor, shared] Provenance is named but not pinned.** All three cite source CSVs/JSON by filename (lines 52–55 / 54–58 / 64–68) but include no row counts or hashes in-file. The drafts themselves say a hash manifest "should accompany" a merge — good; make that a hard gate before integration.

---

## D. Severity summary

| Severity | Items |
|---|---|
| **Blocker** | P2: emission-line selection biases the quenched denominator, unquantified. Shared: selection-function attrition never reported. |
| **Major** | P1: unequal quartile counts unexplained; rows not independent ("scale-robust" overclaim); CI method unstated. P2: high AGN fractions uncaveated; `log L_Hα` units/definition missing. P3: f_Q/f_high exc./u−r undefined; thin small-N cells drive headline extremes. Shared: inconsistent statistics; missing column glossary; no topical literature; undescribed figures. |
| **Minor** | P1: residual "radio-jet" title risk. P2: no CIs. P3: over-precise decimals; caveat-to-definition linkage. Shared: cross-paper consistency check; provenance not hash-pinned. |

**Bottom line:** No fabricated data or arithmetic errors found; the honesty guards are the drafts' strongest feature and should be preserved verbatim. The gating work before integration is disclosure, not re-analysis — quantify the selection attrition, define the columns, standardize the statistics, and attach real topical citations and figure descriptions. None of these require changing a single reported value.
