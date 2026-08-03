I have enough to deliver the review. All reads were read-only; I did not run shell/network tools or write files.

---

# External Read-Only Review — Lana Wave-2 Representativeness/Citation Patches (20260708T224851Z)

## 1. Overall verdict

**Conditional pass for lane-local integration; not ready for any public replacement or external submission.** These three patch drafts are a genuine improvement over the 212455Z Wave-2 revisions. The four resolvable blockers from the previous external tick are largely fixed: (a) headline fractions are now explicitly declared selection-convolved, (b) a cached-vs-public marginal representativeness table is present in all three, (c) the Hα proxy is defined with units and "binomial-only" uncertainty labeling, and (d) M3 P3 now prints Wilson intervals on its two small cells. Titles, abstracts, and "forbidden headline" boundaries are honestly demoted to optical denominators / target vectors.

**But three items are only papered over, not resolved, and two of those are correctness-grade:**

- **M2 P2's central result (the 0.138–0.152 density contrast) is still uncontrolled for the redshift/mass degeneracy that the internal nearest-neighbour proxy almost certainly carries.** A caveat sentence was added; the actual z–mass balance diagnostic the prior tick asked for was *not* run. The contrast may be largely a radial-selection artifact.
- **The BPT classification recipe — the definition of "optical AGN," the headline quantity in all three papers — is never stated in any draft.** M3 P3 additionally reports `f_BPT_AGN` and `f_high_exc` with **zero** BPT/high-excitation citations and no definition of the high-excitation threshold.
- **Figure-PDF-vs-caption verification (prior blocker #7) remains open.** Captions were rewritten to be safe; the preserved `figure1.pdf` bitmaps were not inspected against them. I did not inspect them either. Silent mismatch risk persists.

These are draft-quality artifacts (note the "Discussion outline" section headers) and are correctly scoped as such. My verdict is: fine to integrate locally after the fixes below; do **not** compile-and-mirror as public-linked PDFs yet.

---

## 2. Per-paper critique

### M2 P2 — Radio-jet environment → optical-AGN/density denominator

**Structure & guarding:** Good. Scope/citation-boundary section with explicit "forbidden headlines," honest "optical denominator, not jet coupling" framing, all 10 bibitems cited in-text. Arithmetic checks out (all three k-rows: low/high fractions and Δ reproduce exactly).

**The unresolved core problem — density proxy ≈ redshift.** The "density" is a nearest-neighbour distance in an (α,δ,z)→Cartesian embedding of a *flux-limited* sample. In such a sample NN distance is dominated by the radial selection: at higher z the sample is sparser → larger NN distance → labelled "low density"; low z → denser → "high density." So **"high-density quartile" ≈ "low-redshift subsample."** The draft's own numbers corroborate this: the high-density quartile has *fewer* massive hosts (1,980) than the low-density quartile (2,604) — the opposite of the real mass–environment relation, and exactly what you expect if "high density" is really "low-z small-volume." Lower-z galaxies also have better four-line S/N, which inflates BPT-classifiable AGN. **A large fraction — possibly all — of the 0.14 contrast could be a redshift/detectability artifact, not environment.** The draft flags "redshift-space distortions" and "z–mass balance" in the abstract but names neither this radial-selection degeneracy nor runs the balance check. This is the single biggest issue.

**Representativeness table is weakest here.** The marginal z/mass/sSFR check does nothing for a *density* paper, whose validity depends on **spatial/footprint completeness**. A SpecObjID cap plausibly biases the sky footprint and thus every edge-galaxy's neighbour count; the marginal table cannot detect that. The table should not be presented as if it addresses density representativeness.

**Reproducibility gaps:** the Δf interval method is unstated (Wilson? binomial? bootstrap? — contrast with M3 P3's explicit Wilson); the density code path is not cited in the reproducibility note (only `analysis_results.json`), unlike M3 P2 which cites `run_remaining_topic_pilots.py`.

### M3 P2 — Gas depletion/SFE → optical follow-up denominator

**Strongest of the three.** The selection-function handling is genuinely good: the sSFR-dependent retention warning (33.56% vs 94.85%) directly and correctly guts any temptation to read the 0.509–0.649 fractions as AGN prevalence among massive quiescents. The Hα proxy is now fully specified (observed `h_alpha_flux`, 10⁻¹⁷ cgs, ×4πD_L² with H₀=70, no extinction/aperture/Balmer/gas-mass correction), and uncertainties are labelled binomial-only. Cached/(S/N≥3) ratios reproduce (~25%). Gas-survey citations are correctly quarantined in the missing-observable paragraph.

**Gaps:** (1) **BPT demarcation undefined** — `f_BPT_AGN` is the whole table, yet which line (Kauffmann03 vs Kewley01 vs Kewley06 Seyfert/LINER split) separates "AGN," and whether composites/LINERs are included, is never stated. Baldwin/Kewley/Kauffmann sit in the bibliography **uncited in-text** (the diagnostic that produces the numbers has no in-text anchor). (2) Median `log L_Hα` values are reported to 0.01 dex with no dispersion/IQR — a single-number proxy with no scatter is under-labelled even for a proxy. Minor.

### M3 P3 — Simulation validation → observed SDSS target vector

**Structure & guarding:** Good framing (observed vector, no mock generated, no model validated/rejected). Wilson intervals added to the two N<500 cells; the 15-cell table sums to 60,000 (independently confirmed in the prior tick); small-cell values reconcile with the main vector (0.856/0.610/0.218). Simulation suites are correctly confined to the future-forward-modelling paragraph.

**Two real gaps:** (1) **`f_high_exc` is never defined anywhere in the manuscript** — the high-excitation threshold (the shared module uses `bpt_label==agn` ∧ `log_oiii_hb>0.25`) does not appear. A results-table column with no definition is a reproducibility hole. (2) **The bibliography contains no BPT or high-excitation reference at all** — two of the three reported quantities (`f_BPT_AGN`, `f_high_exc`) have zero method citation. This is worse than M3 P2's uncited-but-present situation. (3) Same undefined-BPT-demarcation issue as M3 P2.

---

## 3. Cross-paper ranked next steps (before any integration)

1. **Define the BPT "optical-AGN" recipe once, in the shared selection module, and cite it in-text in all three** — exact demarcation line(s), composite/LINER handling, and (for M3 P3) the high-excitation `log OIII/Hβ>0.25` definition. Add Baldwin/Kewley/Kauffmann to M3 P3's bibliography. This currently leaves the headline quantity of every paper unreproducible.
2. **M2 P2: actually run the z–mass(–detectability) balance diagnostic** across the low/high density quartiles, or explicitly demote the density contrast to "uncontrolled for the redshift–NN-distance degeneracy." Name the radial-selection confound, not just RSD/edge effects. Do not integrate the 0.14 contrast as a standalone finding without this.
3. **Verify each preserved `figure1.pdf` against its rewritten caption** (axis titles, panel labels, any embedded "jet coupling / gas depletion / simulation validation" text). This is the last open item from the previous tick and a silent-correctness risk; do it before any local compile-and-hash.
4. **Scope the representativeness table's reach honestly per paper** — add one sentence that the z/mass/sSFR marginal check does **not** address spatial/footprint or joint-distribution selection, and note that this makes it materially weaker evidence for M2 P2's density result than for the two denominator-only papers.
5. **Standardize uncertainty methodology labels** — M2 P2 should state its interval method (match M3 P3's explicit Wilson) and cite its density-estimator code path in the reproducibility note.

---

## 4. Sentences/claims to demote or guard

- **M2 P2, abstract:** *"the high-minus-low BPT optical-AGN fraction is 0.138–0.152 across k=5, 10, and 20"* — add inline: uncontrolled for the redshift/mass differences between density quartiles; the internal-density proxy is degenerate with radial selection.
- **M2 P2, abstract:** *"massive hosts in the high internal-density quartile have a higher BPT optical-AGN fraction than … the low-density quartile."* — guard: the contrast may be a redshift/line-detectability artifact of the flux-limited nearest-neighbour proxy, not an environmental effect.
- **M2 P2, Conclusion #2** — same guard; do not restate 0.138–0.152 without the confound caveat adjacent.
- **M2 P2, §Data:** the representativeness paragraph implies the marginal table bounds the sample's fitness for the density analysis — demote to "bounds broad z/mass/sSFR marginals only; does not test the spatial completeness the density estimate depends on."
- **M3 P3, Table `f_high_exc` column** — cannot stand until the high-excitation threshold is defined in-text; either define or remove the column.
- **All three, "f_BPT_AGN"** — every use inherits an undefined classification boundary; guard until the demarcation is stated and cited.

**Already adequately guarded (keep as-is):** M3 P2's "These high fractions are conditional on requiring all four optical lines; weak-line quiescent systems are excluded"; the shared SpecObjID "row-capped and non-random" caveat; all three "forbidden headline" boundary statements.

Net: fixes #1–#3 are prerequisites for local manuscript integration; none of the three should be compiled to a public-linked PDF or described as submission-ready until the BPT recipe is defined+cited, M2 P2's density confound is controlled or demoted, and the figures are verified against their captions.
