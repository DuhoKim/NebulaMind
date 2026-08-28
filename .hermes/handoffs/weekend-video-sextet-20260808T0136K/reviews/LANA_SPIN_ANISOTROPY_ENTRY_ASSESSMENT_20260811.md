# Lana — galaxy spin-anisotropy dispute: is there a tractable, non-circular entry?

**Lana (science / claim-boundary seat), 2026-08-11.** Duho's redirect: *"we cannot prove the BHU with the
spin parity anisotropy, but still, that is the only way to study the cosmology."* The BHU line is closed
(Kun's PASS_FINAL_CLOSING_RECORD_ON_REVISION_5) and stays closed: **nothing below is a BHU test and
nothing below may be dressed as one.** The target is the spin-anisotropy dispute in its own right — which,
unlike BHU, has real numbers on both sides and a live fight. **NOT_WORTH_DOING_YET remains an acceptable
outcome. Nothing is committed; Duho decides after reading me and Kun.**

**Method.** Load-bearing claims below were fetched today from the primary abstracts (arXiv), not recalled
— tonight's lesson was five engines characterising a paper from its abstract and being wrong, so
everything full-text-dependent is marked **[VERIFY]** and §6 makes the reads a precondition. One naming
correction at the outset: the rebuttal Hwao's brief calls "Iye and Hayashi" is, per the primary record,
**Iye, Yagi & Fukumoto** (ApJ 907, 123); I found no Hayashi on that paper — the name likely garbles Yagi
or Fukumoto **[VERIFY if a separate Hayashi rebuttal exists]**. Tori's open marker on "the exact Shamir
rebuttal set" is resolved at abstract level in §1.

> **Revision 2 (2026-08-11) — re-assessment on Tori's prior-art facts
> (`TORI_SPIN_PRIOR_ART_20260811.md`, full methods/results read, not abstracts). Her findings settle the
> open questions of Rev 1: Kun's Patel–Desmond blocker does NOT cover this design (label-level reanalysis
> only, no own classifier, no mirror run of their own, free-axis statistics); but most of Rev 1's Option B
> already exists in pieces — Shamir 2024 (own HSC Ganalyzer labels + a mirror rerun), Jia, Zhu & Pen 2023
> (CE-ResNet, the enforced reflection-equivariant architecture, trained on GZ1 labels, no anisotropy
> test), Tadaki 2020 (HSC CNN, flip-augmented, no axis test). The one thing nobody has done: preregistered
> fixed-axis tests at the published Longo/Shamir axes; and no paper combines raw-pixel orientation
> custody, enforced equivariance, and fixed-axis prereg. §7 below is the re-assessment Hwao ordered:
> (a) what remains genuinely ours, (b) the equivariance-vs-label-bias crux, (c) whether the fixed-axis
> test alone carries a study. Rev 1's §0 verdict and §3 kill-switch B are superseded by §7; Rev 1's
> naming flag is resolved — no Hayashi on ApJ 907, 123 (Iye, Yagi & Fukumoto); Masao Hayashi is on the
> Tadaki 2020 author list, which explains the conflation.**

---

## 0. Verdict up front

**Yes — conditionally. This is the clearest entry of the three triages I have run this campaign.** The
dispute's decisive question — *is the claimed asymmetry on the sky or in the sorter?* — is exactly the
question our GZ1 lane built an instrument for (the paired-flip test), and the lane's own post-mortem
names the two failure modes any credible entry must delete: **human labelling bias** and an **unstated
frame convention**. Both are deletable by construction: a **machine classifier with mirror-antisymmetry
enforced, run on raw FITS imaging whose orientation we control end-to-end, with pre-registered tests at
the claim papers' own published axes** (which are now fixed numbers — Longo's (l,b) = (52°, 68.5°),
Shamir's RA = 132°, Dec = 32° — so axis freedom is dead for a confirmatory test). Either outcome is a
real result. Three kill-switches in §6, the sharpest being novelty: a 2024 Hyper Suprime-Cam
symmetry paper may already be close to this design and must be read before anything is frozen.

## 1. The two sides, from the primary record (fetched today)

**Claim side.**
- **Longo 2011** (arXiv:1104.2815; Phys. Lett. B): 15,158 SDSS spirals, z < 0.085; dipole asymmetry
  **−0.0408 ± 0.011**, chance probability **7.9×10⁻⁴**; axis ≈ (l, b) = (52°, 68.5°); spin correlation
  claimed to ~210 Mpc/h. Handedness assignment: human/assisted scan of SDSS images **[VERIFY method in
  full text]**; no mirrored-image test mentioned in the abstract.
- **Shamir 2012** (arXiv:1207.5464; Phys. Lett. B): 126,501 SDSS spirals, z < 0.3; **P < 5.8×10⁻⁶**;
  dipole axis **RA = 132°, Dec = 32°** (RA 1σ: 107°–179°). Handedness by the **Ganalyzer** algorithm —
  machine-made **[VERIFY frame handling in full text]**.
- **McAdam & Shamir 2023** (arXiv:2302.06530; Adv. Astron.): GZ1 reanalysis; claims non-random spin
  distributions across all selection methods (volunteers, computer, unfiltered), parity-violation
  P < 0.01, dipole 2.33–3.97σ — i.e. the claim side holds that even the *rebuttal's own dataset* shows
  the signal.
- Plus a live comment war through 2024–25 (arXiv:2404.13864 contra Patel & Desmond; 2411.08723 contra
  the HSC symmetry paper; 2503.22839 "The Universe is Odd") **[VERIFY contents]**.

**Rebuttal side.**
- **Land et al. 2008** (arXiv:0803.3247; MNRAS — Galaxy Zoo): ~37,000 GZ1 spirals; found and corrected
  "a certain level of bias in our handedness results" via the **mirrored-image experiment** — the only
  direct instrument-level test in the literature — and concluded **consistent with isotropy, no
  significant dipole**, suggesting other claims "may also be affected and explained by a bias effect."
- **Iye, Yagi & Fukumoto 2021** (arXiv:2011.00662; ApJ 907, 123): dipole analysis with significance
  calibrated by 3D random-walk simulations; Shamir's catalogue gave **σ_D = 4.00**, but it contained
  **duplicate entries; after dedup the sample shrinks to 45% and σ_D collapses to 0.29**. Conclusion:
  SDSS data alone does not support large-scale symmetry breaking.
- **Patel & Desmond 2024** (arXiv:2404.06617; MNRAS 534, 1553): all public spin catalogues
  (binary Z/S-wise), Bayesian + frequentist dipole and hemisphere tests: **consistent with isotropy**;
  no evidence for anisotropy.
- **HSC symmetry paper 2024** (arXiv:2410.18884, "Symmetry in Hyper Suprime-Cam galaxy spin
  directions") — apparently a new-data null **[VERIFY authors, method, and whether the classifier and
  frame handling match our proposed design — this is the novelty kill-switch]**.

**Our own contribution to the record**, currently uncitable: the GZ1 paired-flip test found perfect label
flipping under mirroring (0 concordant) but **unbalanced** flips — 3,290 CW→ACW vs 3,618 ACW→CW,
dA_paired ≈ 0.095, SE ≈ 0.024, repeating across all four scored cells — a **sorter** asymmetry, since
mirroring cancels any sky signal by construction. It is a modern, larger-magnitude confirmation of
Land's bias finding, ruled FRAME_UNSTATED because Galaxy Zoo does not document whether served images are
as-seen or de-mirrored.

## 2. The five questions, answered

### Q1 — Where does the dispute actually live?
**Distributed across all three loci — which is itself the diagnosis — but the loci are separable:**
- **Measurement:** *not primarily disputed.* Raw count asymmetries in given catalogues largely reproduce
  — Land's raw GZ1 was asymmetric before bias correction; McAdam & Shamir reproduce GZ1 asymmetry across
  selections. Nobody claims the raw counts are miscounted.
- **Significance:** genuinely disputed — duplicates inflating effective N (Iye's 4.00σ → 0.29σ is the
  single most decisive number in the literature), axis freedom (fitting the dipole axis, then quoting a
  p-value at the fitted axis), and estimator conventions (Patel & Desmond's Bayesian/frequentist
  reconstruction disagreeing with the claim side's cosine fits).
- **Systematics:** genuinely disputed and *instrument-level* — human labelling bias (Land's mirror
  experiment; our paired-flip), frame conventions, selection coupling.
Unlike Mittal–Singal (custody gap) and unlike 4PCF (covariance construction), **the decisive locus here
is the instrument, and instrument questions are answerable by building a better instrument** — which is
in reach.

### Q2 — Is this another methods note?
**No.** The papers publish their catalogues, their numbers, and (on the rebuttal side) their code
conventions; the disagreement is not about what the record withholds. The gap in the literature is a
*measurement* gap: every human catalogue carries the Land bias class; the principal machine catalogues
are the claim side's own instrument; and the rebuttals mostly *reanalyse existing catalogues* rather
than re-measuring with a bias-immune instrument. What is missing is a measurement, not a note — so for
once the deliverable is a study. (Subject to the §6-B novelty check against the HSC paper.)

### Q3 — The data question Duho actually asked
Scored against the two failure modes that killed our GZ1 lane — human sorter, unstated frame:

| Catalogue | Handedness by | Frame documented? | Verdict for us |
|---|---|---|---|
| Galaxy Zoo 1 | humans | **No — FRAME_UNSTATED (our terminal finding)** | dead as a sky instrument; alive only as a bias measurement |
| Galaxy Zoo 2 | humans (whether the tree even has a CW/ACW question: **[VERIFY]**) | **[VERIFY]** | inherits the human-bias class regardless; frame likely undocumented |
| GZ DECaLS / GZ DESI (Walmsley) | ML **trained on human labels** (direction question likely absent: **[VERIFY]**) | **[VERIFY]** | inherits human priors by training; not bias-immune |
| Shamir Ganalyzer catalogues (SDSS/Pan-STARRS/HSC; public at his site / VizieR) | machine, deterministic | partially — papers describe FITS handling **[VERIFY per catalogue]**; duplicates documented by Iye | machine ✓, but adjudicating Shamir's claim with Shamir's instrument has an independence problem; dedup mandatory |
| HSC spin catalogue (2410.18884) | **[VERIFY]** | **[VERIFY]** | possibly the closest existing thing to what we need — read first |
| **Raw imaging: SDSS DR17 frames / DESI Legacy Survey cutouts** | **our own machine classifier** | **by construction** — FITS WCS defines orientation; handedness defined in sky coordinates (winding East-of-North), never pixel space | **the only route that deletes both failure modes**; cutout-service orientation must still be audited (FITS bottom-left vs JPEG top-left row order is a real parity trap) **[VERIFY per service]** |

The direct answer: **no existing catalogue cleanly documents its frame while also avoiding human
labels.** The catalogue that satisfies Duho's criterion is the one we derive ourselves from raw FITS —
which is smaller work than it sounds, because the classifier need only answer one binary, mirror-covariant
question, not full morphology.

### Q4 — The circularity traps, named in advance
1. **Frame convention encoding the answer** (the GZ1 killer): any mirroring anywhere in the pipeline —
   cutout service, JPEG rendering, FITS row-order convention — flips or manufactures the signal. Cure:
   define handedness in **sky coordinates**, audit orientation end-to-end from WCS on a labelled test set
   of galaxies with known winding, and state the convention in the artifact.
2. **Human bias, including laundered through ML**: any classifier trained on Galaxy Zoo labels inherits
   the Land bias class. Cure: a **geometric, training-free** classifier (Ganalyzer-style arm-winding
   estimation, or equivalent we write), never a CNN trained on human votes.
3. **Classifier chirality**: a machine can itself be chiral (asymmetric kernels, raster order). Cure —
   and this is our lane's instrument reused: **run every image and its mirror; require anti-concordant
   output; symmetrise scores; report the paired-flip imbalance as the instrument's own bias statistic.**
   A sorter that fails its own mirror test disqualifies itself before touching the sky.
4. **Axis freedom / look-elsewhere**: fitting an axis, then quoting p at the fitted axis, is not a test —
   it is the central significance criticism of the claim side. Cure: **pre-registered fixed-axis tests at
   Longo's and Shamir's published axes** (fixed numbers now — no freedom left), plus one global
   axis-marginalised statistic with significance calibrated by simulation (Iye's random-walk method),
   all frozen before unblinding, under the lane's existing contract discipline.
5. **Duplicates**: Iye's finding; coordinate-match dedup before any statistic, with the dedup rule in
   the freeze.
6. **Selection/footprint coupling**: a dipole fit couples to the survey footprint crossed with any
   position-dependent classification efficiency. First-order cure: the statistic is an internal fraction
   (CW vs ACW along the same lines of sight); residual cure: mirror runs and hemisphere-swap nulls.
7. **Sign-convention babel**: S/Z vs CW/ACW conventions have flipped signs across this literature (we
   have had one Land-direction correction of our own already). Cure: a pre-committed sign dictionary in
   the contract, quoted per source paper.

### Q5 — Smallest version that still says something real
**The study (Option B):** *A frame-audited, mirror-antisymmetrised, machine re-measurement of the galaxy
spin-direction dipole on one dataset, with pre-registered confirmatory tests at the published claimed
axes.* One imaging source (SDSS DR17 or DESI Legacy), N ~ 10⁴–10⁵ spirals after quality cuts;
deterministic classifier + mirror enforcement; dedup; frozen statistics: global fraction, marginalised
dipole with simulation-calibrated significance, fixed-axis tests at (l,b) = (52°, 68.5°) and
(RA, Dec) = (132°, 32°). **Either outcome is real:** a null from a bias-immune instrument at the claimed
axes confronts the claims directly (and, unlike Patel & Desmond, does not inherit the disputed
catalogues); a surviving signal from an instrument that passes its own mirror test would be a major
result demanding escalation. Workstation-scale compute; the classifier is the only real build risk.
**The cheap parallel thread (Option A):** attempt to resolve GZ1's FRAME_UNSTATED by documentation
archaeology or a direct query to the Galaxy Zoo team — if the frame is ever stated, our existing
dA_paired = 0.095 ± 0.024 sorter-bias result becomes citable at zero additional compute, as a modern
confirmation and sharpening of Land 2008. Low cost, externally blocked, worth one letter.

## 3. Preconditions — kill-switches before any design brief

- **A. Primary reads (Lana):** full texts of Longo 2011, Shamir 2012, Iye+ 2021, Land 2008, Patel &
  Desmond 2024, McAdam & Shamir 2023, the HSC pair (2410.18884 + 2411.08723), and the 2024–25 comments —
  confirming §2-Q1's locus triage by quotation and resolving every [VERIFY] above. This also closes
  Tori's outstanding rebuttal-set marker properly.
- **B. Novelty check (the sharp one):** if the HSC symmetry paper (or anything in the comment chain)
  already implements a frame-audited, antisymmetry-enforced, pre-registered re-measurement, Option B
  collapses to a replication on a different footprint — say so honestly and let Duho decide if a
  replication is still wanted. If someone has already done exactly this, **NOT_WORTH_DOING_YET.**
- **C. Data/tooling custody (Tori):** cutout-service orientation documentation for the chosen imaging
  source (the FITS/JPEG row-order question, per service); availability and licence of a deterministic
  classifier (is Ganalyzer public and runnable? is SpArcFiRe **[VERIFY]** an option?); else scope the
  in-house classifier.
- **D. Feasibility spike:** classifier throughput and agreement testing on ~10³ cutouts against a
  hand-checked winding sample, before any full run.

## 4. Fit to the campaign, stated plainly

This entry reuses what the campaign already built — the paired-flip instrument, the freeze/pre-registration
discipline, the funnel accounting — and aims it at the dispute those tools were incidentally built inside.
It is not BHU: the BHU closing record stands, and a measured asymmetry of any size would not identify any
cosmological model (that finding survives). What this study adjudicates is narrower and honest: **whether
the contested spin-direction dipole survives an instrument that cannot have caused it.** That is a real
question in a real literature, it is contested×tractable in exactly the sense our frontier rule demands,
and it is the specific question our GZ1 post-mortem earned the right to ask.

## 7. Re-assessment on Tori's prior-art facts (Revision 2 — this supersedes §0 and §6-B)

### (a) What is genuinely ours, precisely

Tori's coverage matrix is the answer, and it is stark: **five method families, and none combines more
than one of the three controls the dispute actually turns on.** Shamir 2024 has own-label generation and
a mirror rerun — but no enforced antisymmetry identity (the paper says only that mirroring "does not
change the annotation", publishes no paired outputs and no mismatch rate), no documented image format or
orientation custody (Ganalyzer's own paper says it cannot ingest FITS directly; the conversion used is
undocumented), free-axis integer scans, no preregistration — and it is one party to the dispute. Jia,
Zhu & Pen 2023 have the enforced identity — and ran **no anisotropy analysis at all**, on Sky Viewer
JPEGs, on a GZ1-selected sample. Patel & Desmond and Stiskalek & Desmond have the statistics — and
inherit every disputed label at face value, by their own explicit statement.

So what is ours is not "a combination" as decoration — it is the closure property: **a measurement in
which every element either side has ever attacked is controlled simultaneously** — labels by an
architecturally antisymmetric sorter; orientation by raw-pixel/WCS custody with the audit published;
sample selection by provably mirror-invariant criteria; significance by preregistered fixed-axis tests
plus one free-axis check with published prereg. Each existing paper leaves at least one of those open,
and the comment war (2404.13864, 2411.08723) consists precisely of each side attacking the other's open
element. A result with no open element is the thing the literature cannot currently produce from either
camp — *that* is the contribution, and it answers a question none of the pieces answers alone: **do the
published axes survive when nothing about the instrument, the frame, the sample, or the statistics is
left for either side to dispute?**

### (b) The crux: does equivariance delete label bias, or inherit it?

Answerable analytically, and the answer restructures the design. With CE-ResNet's construction — Z-score
from the image, S-score from the same estimator on the flipped image — the identity
p_Z(mirror(x)) = p_S(x) holds **for any weights, regardless of training data**. Three consequences, each
checkable:

1. **The sorter cannot manufacture a net asymmetry.** On any image set, mirroring the set exactly swaps
   the label counts; our paired-flip statistic is identically zero *by architecture*, not by training.
   A GZ1-trained equivariant sorter does **not** carry the 0.095 bias forward as a false signal. The
   label bias steers *which* chirality-sensitive feature the network measures, but it cannot install a
   preference: over any mirror-symmetric image ensemble, the expected asymmetry of an antisymmetric
   sorter is exactly zero.
2. **Even confidence selection is bias-immune:** |score| is mirror-invariant under the same identity, so
   selecting confident classifications cannot chirality-filter the sample.
3. **What biased training *does* cost is sensitivity, and what equivariance does *not* fix is upstream.**
   Bad labels degrade the sorter's correlation with true chirality — attenuating a real signal (validity
   preserved, power lost, and the attenuation is estimable from a hand-checked subsample). And the
   identity says nothing about (i) **pixel-path chirality upstream of the network** — JPEG rendering,
   resampling, any mirroring in a cutout service — which an equivariant sorter would faithfully measure
   as if it were sky; or (ii) **chirality-biased pre-selection** — Jia's sample *is* GZ1's human-selected
   galaxy list, so human bias can still enter through who is in the sample, upstream of the perfect
   sorter.

So, to Hwao's fork: **equivariance genuinely deletes the sorter-borne component of label bias — by
construction, not empirically — which means "establish that it doesn't" dissolves as a study.** But this
is my derivation, not a literature citation: it goes in the design as a stated theorem with an empirical
demonstration (run the trained sorter on N images and their mirrors; counts must swap exactly; publish
the check), and the two leak paths it does *not* cover — pixel path and pre-selection — are exactly the
two controls the design must add. Both are closable: orientation custody from raw pixels with WCS, and a
parent sample defined by photometric cuts plus a *mirror-invariant* spirality score (invariance
enforceable by the same architectural trick, s(mirror(x)) = s(x)) — no human morphology flags anywhere.

### (c) Is the preregistered fixed-axis test enough on its own?

**No — and honestly so.** Run on existing labels, a fixed-axis re-test would add one cleaner p-value to a
literature drowning in p-values, still inheriting the label dispute; Patel & Desmond's free-axis nulls
(with look-elsewhere handled by their priors and mocks) already bound what a fixed-axis test on those
same catalogues could show. The fixed-axis element is necessary — it is the one thing Tori confirms
nobody has done, and it kills the claim side's axis-freedom problem at zero cost because Longo's
(l,b) = (52°, 68.5°) and Shamir's (RA, Dec) = (132°, 32°) are now frozen numbers — but it earns a study
only mounted on independent, bias-immune labels. Conversely, new labels without fixed-axis prereg would
repeat the field's original sin. Neither piece alone; together they are the study.

### The re-assessed verdict for Duho

**A defensible study remains, narrower and sharper than Rev 1's version:**

> **Preregistered fixed-axis re-measurement of the galaxy spin-direction dipole, using an architecturally
> reflection-equivariant sorter (CE-ResNet class, cited to Jia, Zhu & Pen) under end-to-end raw-pixel
> orientation custody, on a sample selected by provably mirror-invariant criteria — with confirmatory
> tests frozen at Longo's and Shamir's published axes and one free-axis check, prereg published before
> unblinding.**

Design deltas from Rev 1: adopt/retrain the CE-ResNet architecture rather than writing a deterministic
classifier from scratch (a deterministic second instrument, symmetrization-wrapped, stays as an optional
cross-check — it would also publish the original/mirror mismatch rate Shamir 2024 did not); selection
moves from "quality cuts" to *provably* mirror-invariant scores; the paired-flip demonstration and the
frame audit are published artifacts, not internal checks. Remaining kill-switches, updated: **(i)** Tori
custody on CE-ResNet code availability and on FITS-cutout orientation documentation for the chosen
survey (SDSS / DESI Legacy / HSC); **(ii)** the equivariance theorem's empirical demonstration in the
feasibility spike (if the identity fails numerically — augmentation leaks, preprocessing asymmetries —
the design falls back to symmetrization-wrapping, which is weaker but sufficient); **(iii)** a training
plan that either reuses GZ1 labels (valid per (b), stated openly, attenuation estimated) or uses
simulation-rendered spirals (cleaner, costlier). If (i) fails — no runnable equivariant implementation
and no documented cutout orientation — the honest verdict reverts to NOT_WORTH_DOING_YET.

**And a zero-compute deliverable now exists regardless:** Tori's matrix itself, plus (b)'s theorem, is a
publishable-grade methods observation — *every published machine catalogue in this dispute either lacks
enforced antisymmetry, lacks orientation custody, or lacks an anisotropy test; and enforced equivariance
provably confines any remaining instrument bias to sample selection and the pixel path*. If Duho wants
the smallest possible first step, that observation, written up with Tori's citations, is it — and it is
the natural preregistration preamble for the study proper.

— Lana, 2026-08-11, Revision 2 (Rev 1 assessed from primary abstracts; Rev 2 folds Tori's full-text
prior-art custody). Nothing designed, nothing frozen, no data touched. Next honest steps: Tori's §7
kill-switch (i) custody checks; my full reads of Jia 2023 + Shamir 2024 methods sections; then, if both
survive, a design brief for the study as re-scoped — with Kun attacking the equivariance theorem and the
mirror-invariant-selection claim hardest, since the whole design now stands on them.
