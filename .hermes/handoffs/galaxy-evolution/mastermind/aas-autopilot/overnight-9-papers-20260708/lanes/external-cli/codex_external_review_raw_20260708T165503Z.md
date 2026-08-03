**M1 RP-2 — SDSS Density Proxy For Environmental Quenching**

Structure/readiness: This is a credible revision draft, but still reads like an integration scaffold rather than a finished AAS manuscript. The main weakness is that the Methods section leaves the quenched sSFR threshold unresolved, explicitly saying it must be inserted later. That blocks publication readiness because the central dependent variable is undefined.

Missing evidence/citations: The bibliography only covers SDSS/BPT basics. The literature packet says this paper needs DR17, Brinchmann-style sSFR provenance, and environment-quenching anchors such as Peng/Baldry for interpretation, with Wetzel/Goubert only as future-data context. Those are not yet integrated.

Overclaiming/scope leakage: The draft mostly guards claims well. The title and framing are appropriately “density proxy,” not halo environment. The remaining risk is the phrase “environmental quenching” in the title/topic: the text should keep saying this is a nearest-neighbour association, not causal quenching.

Reproducibility gaps: Missing exact quenched threshold; missing density formula details; no edge/mask/fiber-collision handling beyond caveat; no clear uncertainty convention for the quartile fractions; figure caption says future integration should define plotted bins, so the current figure is not portable.

Next steps: Insert exact sSFR threshold and density computation from code/artifacts; add parent-to-cached denominator selection disclosure; integrate DR17, sSFR, and environment literature; make figure/table captions self-contained; add a short robustness paragraph for S/N and mass-redshift adjustment limits.

**M1 RP-3 — Optical-AGN Denominator For Maintenance-Heating Follow-Up**

Structure/readiness: This is the cleanest of the three conceptually. It correctly reframes the paper as an optical denominator rather than a heating test. Still, the low-sSFR threshold is unresolved, so the massive low-sSFR row is not fully reproducible.

Missing evidence/citations: The bibliography lacks the maintenance-heating context called out in the source packet: Best 2005, McNamara & Nulsen 2007/2012, Heckman & Best 2014, and DR17/sSFR provenance. Without these, the follow-up motivation is under-anchored.

Overclaiming/scope leakage: The interpretation guard is strong. Main leakage risk is using “maintenance-heating” in the title without immediately qualifying that no heating/cooling observable is measured. The abstract does this, so keep that pattern everywhere.

Reproducibility gaps: Missing exact low-sSFR threshold; optical AGN definition is too compressed; no selection-function attrition for massive emission-line hosts; binomial intervals are described as approximate but not formula-specific enough; figure caption is not self-contained.

Next steps: Insert exact low-sSFR and BPT criteria; add massive-host parent/S/N/cached attrition counts from the selection packet; integrate radio/X-ray/cavity literature only as future measurement anchors; make nondetection accounting a required follow-up design element.

**M2 P1 — High-Excitation Optical-AGN Denominator For Outflow Escape/Recycling**

Structure/readiness: The draft is useful but not merge-ready. It openly says the exact high-excitation criterion is missing, although the Hwao context later recovers it as `bpt_label == agn` and `log_oiii_hb > 0.25`. That needs to be inserted before any further review.

Missing evidence/citations: The paper lacks Kewley 2006 classification caveats and all outflow/escape/recycling context sources from the literature packet. Those should be split cleanly: classification sources support the measured denominator; Cicone/Fiore/Carniani/Veilleux/Fabian motivate future multiphase follow-up only.

Overclaiming/scope leakage: The text is careful, but the median sSFR offset risks being read as feedback evidence. It should be explicitly labeled as descriptive target characterization, not suppression caused by outflows.

Reproducibility gaps: Missing exact high-excitation criterion in the draft; no denominator attrition statement; no uncertainty on median sSFR offset; no description of how medians were computed or whether bootstrap intervals exist; figure caption still requires fuller plotted-variable definitions.

Next steps: Insert the recovered high-excitation definition; add denominator selection/attrition disclosure; add uncertainty or clearly mark medians as descriptive; cite classification and outflow literature with strict claim boundaries; make table notes define all thresholds and units.

**Cross-Paper Priority List**

1. Resolve all unnamed thresholds: RP-2 quenched sSFR, RP-3 low-sSFR, M2 P1 high-excitation criterion.
2. Add selection-function disclosure for the shared 60,000-row capped SDSS emission-line denominator.
3. Integrate DR17, BPT, and sSFR provenance citations across all three.
4. Add topic-specific citations, but separate actual-method support from future-data motivation.
5. Make every table and figure portable: thresholds, denominators, plotted bins, uncertainty definitions, and source artifact paths should be explicit.
6. Remove or qualify any wording that turns optical SDSS proxy counts into causal quenching, maintenance heating, or escape/recycling evidence.
7. Add a short reproducibility appendix/table listing parent selection, cuts, denominators, thresholds, artifact names, and uncertainty conventions.
