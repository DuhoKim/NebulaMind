# CODEX — GZ SPIN RECONNAISSANCE (2026-09-02)

## BOTTOM LINE

**A blind-preserving comparison is feasible outside the frozen sample, but Tier C's threshold-free exact count is NOT VERIFIED.** GZ1 is the relevant release: its human-vote catalogue publishes clockwise and anticlockwise direction fractions. Later GZ2/GZ:Hubble/GZ DECaLS/GZ DESI question trees measure spiral-arm *tightness*, not direction; the 8.67M-row GZ DESI product is model-predicted vote fractions (with a separate 96k human-vote training release, also without a direction question).

At 1.0 arcsec, the disjoint object tiers are A = 16,600, B = 8,465, and Tier C **at least** 542,865 direct DR10 matches, including **at least 22,693** high-confidence GZ1 objects. The remaining Tier-C uncertainty is bounded: 13,725 GZ1 positions lie in populated DR10-south brick rectangles but were not resolved by the catalogue query accelerator; 561 are high-confidence. Covering the verified Tier-C high-confidence set needs about 17,577 additional primary bricks, about 207.97 GiB at the observed mean.

The matched mask is only slightly brighter, is not larger, and has nearly identical photo-z, but its sky selection is highly non-representative. Agreement therefore does not transfer to the full mask. Recommend **(i): measure only outside the frozen sample**, after a new preregistration.

## Scope and hard boundary

This was catalogue and literature reconnaissance only. I did **not** inspect any image or cutout, read any per-object handedness label, run the instrument, form χ, or measure a spin in any tier. `P_CW` and `P_ACW` were used only as catalogue vote-fraction fields to count catalogue subsets; no object's direction was selected or inspected. Frozen text and `ref/` were not modified.

## Established facts carried forward with provenance

The following are restated rather than re-derived. `CODEX_REOPEN_ANALYSIS_20260902.md` reported them and `AGY_REOPEN_VERIFY_20260902.md` independently reproduced all ten numerical quantities exactly:

- Official GZ1 Tables 2+3 contain 667,944 + 225,268 = **893,212** rows.
- Against `../_successor_build_20260824/acquire/positions_selected_cut.csv` (49,211 retained rows), nearest-neighbour spherical matching at `<=1.0 arcsec` gave **16,604 matched mask rows**, **16,600 unique GZ1 objects**, **13,347 rows with any CW/ACW vote**, **1,040 with `P_CW+P_ACW>0.5`**, and **363 with `P_CW>=0.8 or P_ACW>=0.8`**. Sensitivity was 16,488 / 16,637 / 16,658 rows at 0.5 / 1.5 / 2.0 arcsec.
- Frozen V134 lines 721–723 make the actor table exclusive, and lines 735–737 admit only the allocated hand-check committee/ingestion/calibration path. An external catalogue therefore cannot populate `â` in this run at any count.
- The earlier assertion that the sign needed a published anchor was wrong. V134 lines 124–129 already make empirical anchoring admissible in kind through mandatory synthetic anchor BS-4. That does not authorize a GZ actor inside the frozen run.

## Q1. Which Galaxy Zoo release carries chirality?

### GZ1: confirmed

The official Galaxy Zoo release page says GZ1 volunteers chose among six categories including “clockwise spiral” and “anticlockwise spiral”; Table 2 gives the fraction of votes in each category for objects with DR7 spectra, and Table 3 gives the same category fractions for objects without DR7 spectra ([Galaxy Zoo data release](https://data.galaxyzoo.org/)). The release paper's schema note defines `CW` and `ACW` as the fractions of votes for “ClockWise spirals” and “AntiClockWise spirals”; Table 3 uses the same definitions ([Lintott et al. 2011, Tables 2–3](https://pure.port.ac.uk/ws/portalfiles/portal/1517011/166.full.pdf)). The local files expose the corresponding columns:

> `OBJID, RA, DEC, NVOTE, P_EL, P_CW, P_ACW, P_EDGE, P_DK, P_MG, P_CS, ...`

Thus claim (a) is **confirmed**: these are per-object direction vote fractions derived from human votes. `P_CW` and `P_ACW` are raw category fractions; the released debiasing fields combine spiral classes and do not separately debias the two directions.

GZ1 ancillary Tables 5–7 also retain human direction-category fractions: Table 5 is the mirrored-image bias study, Table 6 the monochrome study, and Table 7 combines main and bias-study votes. They are not an intermediate successor release; they are GZ1 bias products. This reconnaissance used Tables 2+3 only.

### GZ DESI: confirmed model predictions, no direction task

Walmsley et al.'s 8.67M catalogue consists of automated deep-learning measurements. Its release documentation says the catalogue values are “predicted vote fractions,” meaning the expected fraction of volunteers selecting each answer; the advanced file adds `proportion_asked` and credible intervals ([GZ DESI Zenodo release, current record](https://zenodo.org/records/8360385)). The paper describes automated measurements trained on volunteer votes ([Walmsley et al. 2023](https://arxiv.org/abs/2309.11425)). The principal's cited Zenodo 8331338 appears to be an earlier record/version; the current versioned record resolves to 8360385.

The spiral schema is appearance/tightness, not screen direction. The inherited task is “How tightly wound do the spiral arms appear?” with answers `Tight`, `Medium`, and `Loose`; the adjacent task counts arms ([GZ DECaLS decision tree and schema](https://academic.oup.com/mnras/article/509/3/3966/6378289)). Therefore claim (b) is **confirmed**. The Zenodo release separately provides volunteer votes for about 96k GZD-8 galaxies, but those votes follow this non-direction decision tree and do not supply CW/ACW chirality.

### Intermediate releases

I found **no post-GZ1 release with a human clockwise/anticlockwise direction task**. GZ2 replaced GZ1's one-step directionality categories with a branched tree whose spiral questions are presence, winding tightness, and arm count. GZ:Hubble adds a clump branch to the GZ2-style tree; GZ DECaLS iterates that tree. GZ DECaLS does publish human vote catalogues, but their spiral “winding” is tight/medium/loose, not handedness. This conclusion follows the published decision-tree descriptions, not merely absence of conveniently named columns.

## Q2. The three-tier overlap

### Catalogue identities and matching rule

- Tier A pin: `positions_selected_cut.csv`, 49,211 rows.
- Parent pin: `../_successor_build_20260824/acquire/positions_selected.csv`, **65,060 rows**. Its query and `quality_cut_receipt.json` identify it as the pre-quality-cut parent (`n_before=65060`, `n_after=49211`). The similarly named 208,408-row file elsewhere is not this pin.
- Match: nearest-neighbour spherical separation `<=1.0 arcsec`.
- To make tiers disjoint at the GZ1-object level, priority is A, then B, then C. Two GZ1 objects had both a retained and a quality-cut parent row; they are assigned to A. Row counts are retained below for continuity with the earlier receipt.
- “Any vote” means `P_CW+P_ACW>0`; “>0.5” is strict; “high-confidence” means `P_CW>=0.8 or P_ACW>=0.8`.

| Disjoint tier (unique GZ1 objects) | Total matched | Any CW/ACW vote | `P_CW+P_ACW>0.5` | High-confidence |
|---|---:|---:|---:|---:|
| **A — retained 49,211 mask; burns blind** | **16,600** | **13,343** | **1,039** | **363** |
| **B — parent but quality-cut; blind status ambiguous** | **8,465** | **6,770** | **845** | **346** |
| **C — DR10-south, outside parent; verified direct-match lower bound** | **>=542,865** | **>=401,214** | **>=48,098** | **>=22,693** |
| C footprint ceiling, not asserted as matched | 556,590 | 407,964 | 49,162 | 23,254 |
| C unresolved interval width | 13,725 | 6,750 | 1,064 | 561 |

For comparison with the prior row-based receipt, Tier A has 16,604 matched mask rows with the established 13,347 / 1,040 / 363 thresholds. The raw quality-cut-out subset has 8,468 matched rows (8,467 unique GZ1 objects) with 6,772 / 846 / 346; removing the two A/B object overlaps gives the disjoint B row above.

### Why Tier C is a bound, not an invented exact count

I first placed all GZ1 positions into the official populated `survey-bricks-dr10-south.fits.gz` rectangles, then queried actual `ls_dr10.tractor_s` rows in those bricks. To keep the query finite, the bulk retrieval used `dered_mag_r<20`, deliberately generous relative to the GZ1 Main Galaxy Sample's SDSS Petrosian `r<17.77` selection. Local nearest-neighbour reduction produced 542,865 outside-parent direct matches in the disjoint C tier. Because matches reach the query ceiling and 13,725 outside-parent footprint positions remain unresolved, the accelerator cannot certify completeness. The exact Tier-C values are therefore **NOT VERIFIED**; the table reports the directly demonstrated lower bound and the brick-footprint ceiling. This uncertainty does not threaten viability: the verified high-confidence lower bound alone is 22,693.

### Tier B blind-status argument

Argument for “not burned”: these 15,849 parent rows were excluded before the sealed 49,211-row mask, so their labels cannot reveal a retained-object sign or alter the frozen retained-mask statistic. Argument for “still protected”: they belong to the authenticated 65,060-object parent and the exclusion was part of the same blind construction, so inspecting their morphology could leak selection/instrument behaviour relevant to the retained population and could violate the spirit of P0 even if not its final mask. The principal must rule; I do not treat B as safe.

## Q3. What would Tier C cost in data?

The **verified lower-bound** Tier-C high-confidence set contains 22,693 objects in 19,204 distinct DR10 primary coadd bricks. Comparing their `brickname` values with the 12,117 locally held r-band brick filenames gives 1,627 already held and **17,577 additional primary bricks**.

Observed mean brick size:

`143.37 GiB / 12,117 = 0.01183296 GiB per brick`.

Estimated additional storage:

`17,577 × 0.01183296 = 207.97 GiB` (about **208 GiB**).

Method: count unique primary `brickname` values for the verified Tier-C high-confidence matches, subtract exact locally held brick names, and multiply by the observed mean. This is a primary-brick coverage estimate, not a byte manifest and not a cutout operation. It excludes up to 561 unresolved high-confidence footprint candidates and does not add any neighbour-brick padding a later cutout planner might require, so budget above 208 GiB.

## Q4. Are the overlap objects comparable to the mask?

All values below come from DR10 catalogue columns for a like-for-like comparison: `dered_mag_r`, fitted `shape_r` in arcsec, and `photo_z.z_phot_median`. The full mask has complete values for all three fields in the catalogue join. Quantiles are 5/25/50/75/95 percent.

| Population / field | N finite | Mean | q05 | q25 | median | q75 | q95 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Full mask: dereddened r | 49,211 | 16.921 | 15.931 | 16.565 | 17.006 | 17.361 | 17.633 |
| GZ1-matched mask: dereddened r | 16,604 | 16.900 | 16.051 | 16.589 | 16.962 | 17.276 | 17.543 |
| Full mask: `shape_r` (arcsec) | 49,211 | 3.135 | 1.621 | 2.075 | 2.671 | 3.582 | 6.198 |
| GZ1-matched mask: `shape_r` (arcsec) | 16,604 | 2.951 | 1.624 | 2.067 | 2.627 | 3.435 | 5.237 |
| Full mask: photo-z | 49,211 | 0.09642 | 0.03555 | 0.07447 | 0.09993 | 0.12285 | 0.14266 |
| GZ1-matched mask: photo-z | 16,604 | 0.09660 | 0.03729 | 0.07575 | 0.09933 | 0.12211 | 0.14232 |

The matched subset is only modestly brighter (median difference −0.043 mag), is slightly **smaller**, not larger (median −0.044 arcsec and a shorter upper tail), and has essentially the same photo-z distribution. This closeness is partly by construction: the parent itself requires `dered_mag_r<17.7`, `shape_r>1.5`, and `z_phot_median<0.15`, while GZ1 is dominated by the SDSS Main Galaxy Sample of extended objects with Petrosian `r<17.77` ([GZ1 sample selection](https://pure.port.ac.uk/ws/portalfiles/portal/1517011/166.full.pdf)).

Nevertheless, the GZ1-matched subset is sky-selected and requires historical SDSS targeting/imaging and a successful crossmatch. **Any agreement rate measured on it does NOT transfer to the sample as a whole.** The catalogue marginals show no catastrophic magnitude/size/redshift mismatch, but they cannot establish exchangeability in morphology, surface brightness, crowding, image quality, or sky position.

## Q5. Sky coverage

Yes. The actual matches demonstrate that GZ1 coverage reaches the catalogue called DR10-south, which extends well north of the celestial equator. The earlier attribution of the ~34% overlap chiefly to Stripe 82 is refuted.

For the 16,604 Tier-A matched rows:

- RA degrees, min/1/10/25/50/75/90/99/max percentiles: **0.790, 11.080, 175.878, 199.910, 217.535, 229.873, 240.561, 254.105, 358.714**.
- Dec degrees, same percentiles: **−10.866, −9.814, −0.024, 6.116, 17.138, 26.159, 29.204, 33.044, 34.603**.
- Defining the conventional Stripe 82 box explicitly as RA 300°–360° or 0°–60° and Dec −1.25° to +1.25°, only **473/16,604 = 2.849%** lie in it; **97.151%** lie elsewhere.

Thus the overlap is a broad northern/equatorial DR10-south overlap, concentrated around the SDSS northern footprint, not a Stripe-82-dominated band. The matched median Dec is +17.14°.

## Q6. What could the comparison actually claim?

### a. Meaning of an agreement rate

A measured agreement rate would establish reproducibility/compatibility between this instrument's signed classifications and GZ1 human vote labels on the selected, matched, measurable population under the declared thresholds and rendering. It could reject independence or chance-level concordance and reveal gross parity/sign failures.

It would **not** identify either system's accuracy against true handedness. If ours and GZ agree 90%, the disagreement budget cannot be apportioned between our errors, GZ human errors, correlated image ambiguities, selection effects, or convention mistakes without an independent truth source or a latent-class design with additional assumptions. It would not validate amplitude calibration `â`, population representativeness, or the frozen run, and it would not make GZ labels admissible under V134.

### b. Can the comparison determine sign mapping?

Yes, empirically, if the two labelers are positively associated with the same apparent-winding property. For binary labels, reversing one sign changes agreement `p` to `1−p` (apart from ties/exclusions). A precommitted convention producing agreement far above 0.5 while its complement is far below 0.5 identifies the relative sign mapping.

Confounders are important: both systems might share a parity error; correlated errors can create high agreement without truth; GZ1 has documented human/selection asymmetries; a sky-dependent or rendering-dependent parity transformation can defeat a single global mapping; close-to-50% agreement is uninformative; and choosing the mapping after examining the same agreement statistic inflates the reported fit. The synthetic BS-4 absolute anchor remains the cleaner absolute-frame anchor. A GZ comparison should be a preregistered relative-sign diagnostic, ideally with the mapping determined on a disjoint outside-mask subset and agreement estimated on another outside-mask subset.

### c. Honest deliverable

Recommend **an empirical sign determination plus a signed agreement rate**, with both stages precommitted and sample-split. Also report the complementary rate and a sign-invariant diagnostic such as `|2p−1|` as a robustness check, but do not substitute an unsigned number for the scientific deliverable: unsigned agreement conceals whether the implementation is globally inverted. Phrase the result as inter-method concordance, never standalone accuracy.

## Recommendation

Choose **(i), measure only outside the frozen sample**, under a new, signed preregistration that fixes: Tier-C catalogue identity; exact match and ambiguity rules; removal of the current `r<20` reconnaissance accelerator via a complete match; GZ vote threshold/tie handling; parity-preserving render convention; BS-4 absolute sign anchor; disjoint sign-mapping and agreement subsets; and the estimand/uncertainty calculation. Do not touch Tier A unless the principal explicitly chooses a disclosed supersession and accepts that P0's blind is spent. Hold Tier B pending an explicit blind-status ruling.

`COUNT` counts 78 newly measured catalogue quantities: 12 tier cells, 4 brick/storage cells, 42 Q4 distribution cells, and 20 Q5 sky-distribution cells. Provenance-restated values and diagnostic bounds are excluded from that accounting.

SEAT: CODEX
VERSION: GZ-SPIN-RECON-V1
VERDICT: FEASIBLE-WITH-LIMITS
RECOMMENDATION: i
COUNT: 78
