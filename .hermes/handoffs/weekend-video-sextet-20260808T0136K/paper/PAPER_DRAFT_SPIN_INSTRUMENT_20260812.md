# An architecturally antisymmetric instrument for galaxy-handedness measurement:
# three silent failure modes, an orientation-custody protocol, and a preregistered design

**DRAFT 1 — 2026-08-12 — METHODS PAPER. No measurement has been performed on any real galaxy. Kun
gates this draft before anything derives from it, including any video. Nothing is published,
submitted, or uploaded; Duho decides.**

> **SUPERSEDED AS DELIVERABLE, 2026-08-12 (same day):** Duho re-scoped — *"it's not publishable yet.
> so just document so that you don't lose in the future."* The current deliverable is the
> completeness-first record at `paper/RECORD_SPIN_PROGRAM_20260812.md`, which keeps the dead ends and
> receipt-only facts this draft omits. This draft is retained unchanged below as raw material for a
> future submission, when there is a result to submit. Do not derive artifacts from this file.

*Target venue class: methods/instrumentation (RASTI, Astronomy & Computing, PASP class), not a results
venue.*

---

## Abstract

The galaxy spin-handedness literature contains claimed sky-scale asymmetries (Longo 2011; Shamir 2012)
and null re-analyses (Land et al. 2008; Iye, Yagi & Fukumoto 2021; Patel & Desmond 2024) that reach
opposite conclusions, sometimes from the same data. We present a measurement *instrument* — not a
measurement — designed so that the instrument itself cannot be the origin of a handedness signal: a
classifier whose signed output obeys χ(mirror(x)) = −χ(x) as an architectural identity, for any weights
and any training data, verified bit-exactly on 1000/1000 synthetic spirals, with production retention
96.44% (one-sided lower 95% bound 96.15%) and 100% sign accuracy of accepted objects in every
signal-to-noise bin. The paper's principal contribution is negative knowledge, demonstrated with
numbers rather than argued: three failure modes, each of which silently produces a clean-looking wrong
answer. (i) An interpolating mirror violates the antisymmetry identity by 0.058–0.944 — one to twenty
percent of the χ scale, comparable to or exceeding the disputed 0.04-amplitude signal. (ii) A single
undeclared raster row flip does not degrade a handedness measurement but *inverts* it — every galaxy
backwards, nothing visibly wrong. (iii) A decision threshold calibrated on 240 null images instead of
8,000 turned a 0.089%-retention estimator into an apparently 7.8% one, and the artifact's signature —
retention *inverted* in signal-to-noise — shows its acceptances were noise. We give an end-to-end
orientation-custody protocol (per-object WCS determinant parity, declared row order, fail-closed
distortion handling, injected chiral sources), which is precisely the step left undocumented in the
existing literature. A preregistered fixed-axis test of one published claim is specified as future
work and deliberately not performed. This paper makes no claim about spin anisotropy in the universe.

## 1. Introduction

**1.1 A literature that disagrees with itself.** Claims of a preferred handedness of spiral galaxies
on the sky have been made at amplitudes near a few percent: Longo (2011) reported a dipole asymmetry
of −0.0408 ± 0.011 (chance probability 7.9×10⁻⁴) toward (l, b) = (52°, 68.5°) from 15,158 SDSS
spirals; Shamir (2012) reported P < 5.8×10⁻⁶ for anisotropy with a dipole axis at (RA, Dec) =
(132°, 32°) from 126,501 SDSS spirals. Against these: Land et al. (2008) found Galaxy Zoo's raw
handedness counts biased by the human labelling step itself — established by a mirrored-image
experiment — and consistent with isotropy after correction; Iye, Yagi & Fukumoto (2021) showed a
claimed 4.00σ dipole collapse to 0.29σ after removal of duplicate catalogue entries; Patel & Desmond
(2024) reanalysed all public label catalogues and found consistency with isotropy. Conflicting
conclusions have been reported from the same underlying data (McAdam & Shamir 2023). This pathology —
signals and nulls that depend on the instrument, the labels, and the statistic — motivates an
instrument-level intervention rather than another reanalysis.

**1.2 What this paper is and is not.** This is a methods paper. It contributes: (1) an instrument
that provably cannot manufacture a handedness signal (§2); (2) three demonstrated, numbered failure
modes that silently produce wrong answers in this measurement class (§3) — the paper's centrepiece;
(3) an end-to-end orientation-custody protocol filling a documented gap in prior work (§4); (4) a
prior-art analysis showing no existing study combines the required controls (§5); and (5) a
preregistered design for a fixed-axis test of one published claim, specified but deliberately not
executed (§6). **No handedness has been measured on any real galaxy in this work. Every number in
this paper derives from synthetic images or from published literature.** The paper is structured so
that no sentence changes if and when a measurement is later performed under the preregistration: that
measurement would be a separate work.

**1.3 Provenance.** This work was carried out by an AI research crew (seat roles in §8) under the
direction of a human principal (D. Kim). Two of the three failure modes in §3 were found by
re-measuring our *own* earlier instrument and threshold — not by auditing others' work — and we
report them as such: an instrument report that includes its own failed first versions is evidence the
receipts are real (§8.2).

## 2. The instrument: antisymmetry as an architectural identity

**2.1 The identity.** Let mirror(·) be pure index reversal on the analysis raster (np.fliplr; no
resampling). For any scalar estimator w, define

  χ(x) = (w(x) − w(mirror(x))) / 2.

Then χ(mirror(x)) = −χ(x) holds *for any w*, because both sides reduce to the same two floating-point
evaluations with opposite sign, and IEEE-754 subtraction, negation and halving commute with sign
(receipt: bit-exact equality, 1000/1000 synthetic spirals; max |χ(mirror(x)) + χ(x)| = 0.0 exactly).
The same construction applies to a learned classifier by evaluating a shared trunk f on the image and
its index-reversed mirror: χ_net = (f(x) − f(mirror(x)))/2, equivariant *for any weights* (Jia, Zhu &
Pen 2023 introduced this pattern; we adopt it, we do not claim it).

**2.2 What the identity guarantees.** (i) The instrument cannot produce a net handedness on any image
ensemble: mirroring the ensemble exactly swaps the label counts. The paired-flip statistic that
exposed human labelling bias in Galaxy Zoo 1 (Land et al. 2008; our own measurement of the same
effect gave a flip-imbalance of ≈0.095 ± 0.024 on GZ1 labels **[VERIFY: internal receipt; frame
convention of GZ1 remains undocumented, so this number is quotable only as an instrument statistic]**)
is zero *by architecture* here. (ii) Acceptance is handedness-blind: |χ(mirror(x))| = |χ(x)|, so
confidence selection cannot chirality-filter a sample. (iii) Training-set defects cost sensitivity,
never validity: a biased or broken w attenuates a real signal but cannot create one. We demonstrated
(iii) concretely: our first deterministic tracer contained a genuine sign-handling bug (a circular
unwrap that inverted 100% of recovered winding signs) — and the identity still held bit-exactly,
1000/1000. The bug cost accuracy; it could not manufacture asymmetry.

**2.3 What the identity does not guarantee.** Three boundaries, stated as sharply as the guarantee.
(a) It says nothing about chirality introduced *upstream* of the analysis raster — the pixel path
(§3.1, §3.2, §4). (b) It does not equalize *sensitivity* across the sky: accuracy and abstention may
vary with observing conditions, modulating the gain of a real signal; a nonzero global offset from any
source, multiplied by a sky gradient in sensitivity, produces a spurious dipole
("monopole × sensitivity-gradient coupling"), which must be bounded by an explicit control, not
assumed away. (c) It does not launder the *sample*: selection performed by any non-equivariant
upstream process (e.g., human-selected morphology catalogues) can carry handedness structure into the
sample membership. The preregistered design (§6) therefore selects on survey photometry and a
mirror-invariant spirality score only.

**2.4 Production implementation and synthetic validation.** The production instrument is a
shared-trunk ResNet-18-class network in the χ_net construction, trained *exclusively on synthetic
spirals* (20,000 images; master seed and per-image seed manifests published; no human chirality label
anywhere in training). Acceptance threshold τ = 4.4006 was fixed as the 99.5th percentile of |χ_net|
on 8,000 frozen null (armless-disk) images, calibrated before any retention measurement. On 12,000
held-out synthetics: retention 96.44% (one-sided lower 95% bound 96.15%); sign accuracy of accepted
objects 100% in every S/N bin; retention rising with S/N (89.11% at S/N 2–5; 99.07% at 5–10; 99.69%
at 10–20; 99.43% at 20–50) — the signature of acceptances that are detections, not noise (contrast
§3.3). Weights are frozen and hash-pinned (canonical serialization SHA-256 1075a4d9…; file
83008c1c…). Receipts on the production 128×128 float32 raster: mirror∘mirror byte-exact 200/200;
antisymmetry bit-exact 200/200; signed-zero behaviour documented (§3.4-adjacent caveat: +0.0 and −0.0
are value-equal but bit-distinct; all acceptance logic uses ordered value comparisons, never sign-bit
semantics, enforced by a unit test that fails on signbit/copysign branching). Caveat carried from the
receipt: these are synthetic S/N bins; mapping to a real survey's S/N distribution is part of the
preregistration, and real-image characteristics (PSF, blends, artifacts) are not simulated here.

## 3. Three silent failure modes — the centrepiece

Each failure mode below (i) produces a wrong answer with no visible symptom in ordinary quality
checks, (ii) is demonstrated with a number on synthetic data, and (iii) has a named, receipt-level
control. We suggest referees treat this section as the paper's transferable content: the modes apply
to any projected-chirality measurement, not only ours.

### 3.1 The resampling mirror: approximate antisymmetry manufactures signal

Replacing index reversal with an interpolating reflection (affine transform, reflection axis displaced
0.25 px from the grid centreline, bilinear interpolation) breaks the identity by
**|χ(mirror(x)) + χ(x)| = 0.058–0.944** across test spirals — one to twenty percent of the χ scale.
Against a disputed sky signal of amplitude ~0.04, an "almost antisymmetric" sorter can inject an
artifact the size of the entire effect. The cause is structural: under resampling,
mirror(mirror(x)) ≠ x, so the two sides of the identity no longer share their evaluations.
**Control:** the mirror inside χ must be pure pixel-index reversal on the final analysis raster —
never affine, WCS-based, interpolating, rotating, reprojecting, or subpixel — with
mirror(mirror(x)) == x verified *byte-exactly* on the exact dtype passed to w; plus a canary test that
deliberately substitutes a resampling mirror and asserts the identity *fails* (proving the test suite
can see the fault). Never construct mirrored inputs in sky coordinates by interpolation; mirror by
index reversal and account for sky parity separately.

### 3.2 The undeclared row flip: inversion, not degradation

A single silent row-order flip anywhere in the pixel path (FITS row order versus display convention;
a cutout service's internal transpose; a converter's default) does not blur or weaken a handedness
measurement — it **inverts** it: 100% of recovered winding signs flip, consistently, on otherwise
perfect data. Every downstream statistic remains internally coherent; magnitudes, significances and
correlations are untouched; only the *sign* of every conclusion is wrong. Demonstrated in our
pixel-path audit: with a known-chirality synthetic source injected under retained survey WCS cards,
honouring a row flip's determinant recovers the true sky sign; silently ignoring the same flip
recovers the inverted sign, with nothing else visibly wrong. This mode is especially dangerous in
this literature because sign conventions (S/Z versus CW/ACW) already vary across catalogues — a
pipeline inversion is indistinguishable, in a published table, from a convention choice.
**Control:** §4's custody protocol — the parity of every coordinate transformation is computed and
logged, never assumed; end-to-end injected chiral sources are required to recover known signs through
the delivered pixel path; and a deliberate silent-flip control must be *detected* by the audit before
any real data is touched.

### 3.3 The thin null calibration: a threshold that manufactures an instrument

Our first deterministic tracer's acceptance threshold was calibrated as the 99.5th percentile of |χ|
over **240** null images (τ = 4.198). Under that threshold the tracer appeared to be a
~7.8%-retention instrument. Recalibrating the *same* tracer's threshold on **8,000** frozen nulls
(τ = 5.916) revealed the truth: retention 0.13% central, **0.089% one-sided lower 95% bound** — the
apparent instrument was mostly accepting noise excursions above an underestimated threshold. The
diagnostic signature is the S/N profile of retention: the properly-calibrated tracer's acceptances
concentrate at *low* S/N (0.41% at S/N 2–5, falling to exactly 0 above S/N 10) — **retention inverted
in signal-to-noise**, the fingerprint of acceptances that are noise, not detections. Contrast the
production instrument (§2.4), whose retention *rises* with S/N under a threshold calibrated on the
full 8,000-null set. A 99.5th percentile estimated from 240 draws has an expected count of 1.2 tail
events — the threshold was set by the two or three noisiest nulls in a small sample.
**Controls:** null calibrations sized so the target percentile is estimated from ≳40 tail events
(≥8,000 nulls for the 99.5th percentile); threshold frozen *before* any retention or sky measurement;
and retention-versus-S/N published as a mandatory receipt, with inversion treated as disqualifying.
**Provenance, stated deliberately:** this failure and §2.2's sign-inversion bug were found by
re-measuring our own earlier work under our own receipt discipline. We regard that as the discipline
functioning, and we report the failed versions rather than omitting them.

## 4. Orientation custody: the undocumented step

Projected chirality is the only common galaxy observable whose *sign* depends on the parity of every
transformation between detector and analysis raster. Yet the existing literature does not document
this chain: the most widely used deterministic classifier (Ganalyzer; Shamir 2011) states in its own
method paper that it ingests TIFF/JPG/PPM/BMP — not FITS — and the conversion actually used in
subsequent survey-scale analyses (e.g., the HSC application, Shamir 2024) is not published; no format,
row-order, or parity declaration accompanies the label catalogues **[pinned by an independent
full-text custody audit; receipts internal]**. Our protocol makes the chain explicit and auditable:

1. **One survey, one cutout route, exact versions**, with checksums and query logs retained.
2. **Delivered pixels + WCS are the measurement input.** If a cutout service has already resampled
   (e.g., services delivering generated TAN cutouts), that is not automatically disqualifying — but
   the injection battery (below) must run through the same service path, and no further resampling of
   any kind may follow.
3. **Per-object parity accounting:** the sign of the determinant of the WCS CD (or PC·CDELT) matrix
   is computed and logged per cutout; every raster transformation carries a declared row-order and
   determinant receipt; handedness is defined in sky coordinates (winding East-of-North) with
   pixel→sky parity applied per object, never assumed constant.
4. **Fail-closed distortion policy:** in the presence of distortion keywords (SIP/PV/CPDIS/DET2IM),
   either the product is rejected, or a locally-evaluated Jacobian sign replaces the linear
   determinant, with injected-source receipts — never a silent linear fallback.
5. **Injected chiral sources:** ≥1,000 synthetic spirals of known handedness, both parities, injected
   across the footprint and pushed through the entire delivered-pixel path; required outcome is 100%
   correct signed recovery and exact count swap under mirroring; deliberate silent-flip and
   scrambled-WCS controls must be *detected*.

## 5. Prior art and the gap

The components of a trustworthy handedness measurement exist separately in the literature; no work
combines them. An independent full-methods audit of the five relevant method families found: Shamir
(2024) generates its own HSC labels with a deterministic algorithm and reports a mirrored rerun — but
publishes no paired original/mirror outputs, no mismatch rate, no enforced antisymmetry identity, no
image-format or orientation declaration, and scans axes freely without preregistration. Jia, Zhu &
Pen (2023) built the enforced reflection-equivariant architecture — on survey JPEGs, trained on Galaxy
Zoo 1 human labels, with no anisotropy test of any kind. Tadaki et al. (2020) built an HSC CNN with
flip-augmentation — not an enforced identity — and no axis test. Patel & Desmond (2024) and Stiskalek
& Desmond (2024) are label-level statistical reanalyses that accept the disputed labels at face value.
**No reviewed work combines image-level label generation, end-to-end orientation custody, enforced
mirror-antisymmetry, and preregistered fixed-axis tests. Each family has at most one of the four.**
We claim the combination and the receipts — not the invention of any component.

## 6. The preregistered test — future work, deliberately not performed

A complete preregistration exists for a **Longo-amplitude test**: a confirmatory measurement of
Longo's published amplitude (0.0408 ± 0.011) at Longo's published axis (l, b) = (52°, 68.5°), with a
frozen decision procedure (detection at permutation p < 0.001 with matched sign and
attenuation-corrected amplitude within a pre-committed band; rejection requiring null-consistency
*and* a 3σ upper limit below 0.0408; exact INCONCLUSIVE triggers, including a declared-before-
unblinding power gate at N ≥ 100,000 accepted spirals, supported by simulation showing 100% power at
A = 0.04, p < 0.001). The preregistration names its alternative explanations in advance — including
intrinsic spin–large-scale-structure alignment, which is dismissed at this amplitude by a symmetry
argument (axis alignment is even under L → −L and projects to exactly zero net chirality; the
parity-odd channels — filament vorticity, filament rotation, signed spin–initial-condition
correlations — bound the contamination at ≲4×10⁻³ under generous assumptions) but is pre-committed as
a named alternative with shell-coherence and blocked-null controls regardless. **The measurement has
not been performed. No real galaxy has been classified. Execution requires the preregistration's
binding slots to be filled, an adversarial gate to pass, and separate explicit authorization.** The
boundary that governs any future execution is fixed now, verbatim:

> **"A null here does not establish that the sky is isotropic; it rejects only Longo's published amplitude at Longo's published axis if the preregistered rejection rule is met."**

> This tests Longo's published `A ≈ 0.0408` amplitude at Longo's published axis. It does not test
> `A ≈ 0.02`, Shamir, BHU, or whether the sky is isotropic.

## 7. What this paper does not claim

This paper makes **no statement about spin anisotropy in the universe**; it does **not adjudicate**
Longo's or Shamir's claims; it does **not** assert that the sky is or is not isotropic. On black-hole-
universe cosmology: that motivation was examined and set aside in a separate closing record before
this instrument was designed; the boundary of that record is: **nothing currently published supplies a
distinguishable BHU-specific sky-statistics prediction — which is not the same as BHU being untestable
in principle.** No result of the future preregistered test, in either direction, would support,
refute, or test BHU, and no artifact of this program may claim otherwise.

## 8. Authorship, provenance, and receipts

**8.1 Who did what.** This work was performed by an AI research crew operating under the direction and
final authority of the human principal (Duho Kim), who set the research question, all publication
boundaries, and the narrowing decision that defines §6. Seat contributions: **Lana** — design briefs,
antisymmetry analysis and its limits, decision regions, filament-alignment assessment, this draft;
**Yui** — instrument implementation, identity unit tests, production training/calibration and their
receipts (including both failure demonstrations in §3.1 and §3.3); **Tori** — pixel-path audit (§3.2
demonstration), source custody, full-text prior-art verification behind §5; **Goru** — statistics
recovery test, power curves, survey-yield feasibility; **Kun** — adversarial gates at every stage,
including the freeze conditions that §3–§4 encode; **Hwao** — coordination and dispatch. Findings in
this paper attributed to "we" were produced under this division; a machine-readable receipt trail
(sha-pinned artifacts for every number quoted) is retained and available **[repository/DOI to be
established at submission; VERIFY]**.

**8.2 Self-correction record, kept in the text on purpose.** The §3.3 thin-null artifact and the
§2.2 sign-inversion bug were failures of *our own* first instrument, found by our own re-measurement
under receipt discipline, and are reported with their numbers rather than replaced by the corrected
versions alone. We consider this the paper's strongest evidence that its receipts mean something.

**8.3 Reproducibility.** All numbers in §2–§3 regenerate from seeded synthetic manifests (master seed
and per-image SHA-256 seed schedule published; training set, null set and held-out set manifests
hash-pinned), frozen weights (hashes in §2.4), and runner scripts retained under the project archive.
No astronomical data were downloaded or read for any result in this paper, with one exception: a
single 5,760-byte public calibration cutout used (pixels replaced by synthetics) to validate WCS-card
handling in the §3.2 audit.

---

## [VERIFY] register (must be resolved before submission)

1. GZ1 flip-imbalance number (§2.2): internal receipt; quotable only as an instrument statistic given
   GZ1's undocumented frame convention — wording must keep that qualifier.
2. Prior-art §5 characterisations: pinned by internal full-text custody audit; convert internal
   receipts to citable statements (page/section references per paper) at submission.
3. Trailing-arm universality (implicit in "projected chirality ↔ sign(L·n̂)"): canonical citation
   needed (§6's alternative-explanation summary).
4. Repository/DOI for the receipt trail (§8.1).
5. Exact author list / crew-disclosure format per target journal's AI-authorship policy — the paper
   must not misrepresent who did what regardless of venue convention; if a venue forbids AI
   co-authorship, contributions move to an explicit, named contributions statement under the human
   author. **[Duho decides.]**
6. Journal-format references (Longo 2011 PLB 699, 224; Shamir 2012 PLB 715, 25; Land+ 2008 MNRAS 388,
   1686; Iye+ 2021 ApJ 907, 123; Patel & Desmond 2024 MNRAS 534, 1553; Jia+ 2023 ApJ 943, 32;
   Tadaki+ 2020 MNRAS 496, 4276; Shamir 2011 ApJ 736, 141; Shamir 2024 Symmetry 16, 1389; McAdam &
   Shamir 2023 Adv. Astron.; Stiskalek & Desmond 2024 RNAAS 8, 281) — all previously custody-pinned
   internally; format at submission.

**Status: DRAFT. Kun gates. Nothing published, submitted, or uploaded; Duho decides.**

— drafted by Lana, 2026-08-12, from sha-pinned receipts in `spike/` and `prereg/`.
