# Design brief — preregistered fixed-axis test of galaxy spin-direction anisotropy
## with an architecturally antisymmetric, orientation-custodied instrument

**Lana (science / claim-boundary seat), 2026-08-12.** Per Duho: *"have lana draft the design brief, and
plan overnight run for spin parity research."* Authorised scope per Kun's gate
(`KUN_SPIN_ANISOTROPY_REGATE_20260811.md`): **label-table reanalysis NOT_WORTH_DOING_YET; the
image-level, custody-audited, mirror-controlled, preregistered fixed-axis test WORTH SCOPING; an
immediate empirical run before the design is frozen BLOCKED.** This document is therefore a **design,
not a run** — §10 gives the overnight plan in run-safe form. Kun gates this brief when it lands; Tori
binds custody; Goru's survey sweep and Tori's access check fill §8's open slot. **Nothing is published,
accepted, or run; Duho decides.**

---

## 0. First principle: the antisymmetry identity — what it buys, and exactly what it does not

**The identity.** For any estimator wrapped as χ(x) := (w(x) − w(mirror(x)))/2 — or any network built in
the CE-ResNet pattern (Z-score from the image, S-score from the same trunk on the flipped image; Jia,
Zhu & Pen 2023) — the signed output obeys **χ(mirror(x)) = −χ(x) for any weights and any w, regardless
of training data.** Consequences, each a frozen receipt in this design:

- the sorter **cannot manufacture a net asymmetry**: mirroring any image set exactly swaps its label
  counts, so the paired-flip statistic that killed our GZ1 lane is **zero by architecture**;
- **acceptance is bias-immune**: |χ(mirror(x))| = |χ(x)|, so confidence thresholds cannot
  chirality-filter the sample;
- biased or noisy calibration costs **sensitivity, never validity**: it attenuates a real signal by an
  estimable factor (§7) but cannot create one.

This is what the GZ1 lane lacked, and it is why the study is possible at all.

**What the identity does not buy — Kun's channels, absorbed, with the coupling named.** Kun's gate rules
"equivariance alone removes inherited bias" **not safe**, and the design does not rest on it. His three
leakage channels (feature-conditioned label error, confidence/abstention structure, sky-correlated
training composition) are real. Under the strict identity they cannot shift the *offset* — a function of
mirror-invariant covariates (inclination, colour, depth) contributes equally to both chirality channels
and cancels — but they modulate **gain and selection**: per-subclass accuracy and abstention vary with
covariates, so the instrument's *sensitivity* varies across the sky. The dangerous derived mechanism,
stated so it can be controlled rather than discovered later: **monopole × sensitivity-gradient
coupling** — any nonzero global offset (a true monopole, or a pixel-path artifact monopole) multiplied
by a sky gradient in sensitivity or abstention produces a **spurious dipole** that the mirror self-test
cannot see. §5 controls it explicitly. And the identity says nothing about the two upstream surfaces:
the **pixel path** (§4) and **sample pre-selection** (§3, selection rules).

**Prior-art boundary (Kun item 7, stated plainly).** Shamir 2024 (Symmetry 16, 1389) already generates
own HSC labels with deterministic Ganalyzer and reports a mirrored rerun; Jia, Zhu & Pen 2023 (ApJ 943,
32) already built enforced reflection equivariance; Tadaki et al. 2020 built the HSC CNN with flip
augmentation. **We invent neither mirror control nor equivariant classification. Our contribution is
only the combination — plus preregistration, orientation custody, and published mirror receipts — which
Tori's prior-art matrix confirms no reviewed paper has assembled** (`TORI_SPIN_PRIOR_ART_20260811.md`).

## 1. Objective

Test whether a newly generated, orientation-custodied, mirror-controlled handedness instrument
**reproduces or rejects the two published claim-axis signals** under preregistered statistics:

- **Longo 2011** (PLB 699, 224): dipole asymmetry −0.0408 ± 0.011, axis **(l, b) = (52°, 68.5°)**
  (equivalently (α, δ) = (217°, 32°) per the paper), 15,158 spirals, z < 0.085.
- **Shamir 2012** (PLB 715, 25): P < 5.8×10⁻⁶, axis **(RA, Dec) = (132°, 32°)**, RA 1σ 107°–179°,
  126,501 spirals, z < 0.3.

This is a **confirmatory test of specific published claims, not a discovery search** (Kun §2: a design
that drifts back to a free-axis hunt "becomes weak immediately"). It separates the two claims this
literature has mixed: "these labels imply a dipole under some statistic" (Patel & Desmond's question,
answered) from **"the sky has a spin anisotropy that survives an instrument designed not to create it"**
(open).

## 2. Preregistered hypotheses, statistics, and decision regions — frozen before any number

**Freeze discipline (non-negotiable, the lanes' standing rule):** every item in this section is fixed,
sha-pinned, and published in the prereg record **before any sky statistic is computed**. One run; no
parameter revision after any statistic; any deviation voids the run (kill switch K-8).

- **Sign dictionary (frozen first — this literature's recurring accident):** handedness is defined in
  **sky coordinates** — arm winding sense on the sky with North up, East left; "Z/CW" and "S/ACW"
  mapped to Longo's and Shamir's conventions with the conversion worked and quoted from each paper
  **[VERIFY at freeze: re-derive both papers' conventions from their methods, not from memory]**.
- **Primary estimand:** the signed asymmetry fraction per sky direction, and its dipole projection
  D̂(n̂) = mean(sign(χᵢ) · cos θᵢ(n̂)) over accepted galaxies (θᵢ = angle between galaxy i and axis n̂),
  with the **monopole M̂ = mean(sign(χᵢ)) reported first** (monopole before dipole, because of the §0
  coupling).
- **Primary tests, exactly two, at frozen axes:** D̂ at n̂_Longo = (l, b) = (52°, 68.5°) and at
  n̂_Shamir = (RA, Dec) = (132°, 32°). Null distribution from label-permutation mocks that preserve all
  positions and the accepted-sample footprint (≥ 10⁵ permutations).
- **Decision regions per axis (all thresholds frozen; numbers below are the proposal, finalised in the
  prereg after the §7 power estimate):**
  - **REPRODUCED:** D̂ has the published sign and |D̂|/(2a−1) (attenuation-corrected, §7) falls in the
    published amplitude class [0.02, 0.08], with permutation p < 0.001.
  - **REJECTED-AT-CLASS:** D̂ consistent with 0 (p > 0.05) **and** the attenuation-corrected 3σ upper
    bound on |D| excludes the published class floor (0.02).
  - **INCONCLUSIVE:** anything else — reported as such, no rescue.
  - **INCONCLUSIVE-BY-POWER (declared before unblinding):** if the §7 power gate finds the minimum
    3σ-detectable attenuation-corrected amplitude exceeds 0.02, the run is not performed (kill switch
    K-6). An underpowered null is worse than no run.
- **Secondary (cannot rescue a failed primary — Kun item 6):** one axis-marginalised free-axis scan,
  significance calibrated on the same permutation mocks (Iye-style), multiplicity-corrected, reported
  after and never instead of the fixed-axis results. Interpretation of any secondary excess requires the
  full §5 battery to have passed.

## 3. Instrument

**Primary — training-free, per Kun item 1:** a **deterministic geometric arm-winding estimator** w(x)
(Ganalyzer-class: radial intensity-peak tracing → arm pitch sign; exact algorithm frozen in the prereg),
**wrapped in the antisymmetrization identity** χ(x) = (w(x) − w(mirror(x)))/2. The identity then holds
by construction with **no training set at all**, deleting Kun's channels (1) and (3) at the source
(there is no training composition to leak). Acceptance: |χ| > τ with τ frozen from synthetic-image
calibration (§10), never from sky data. Receipts published: the raw estimator's own flip-imbalance
dA_raw = mean(sign(w(x)) + sign(w(mirror(x))))/2 — the honest analogue of our GZ1 dA_paired = 0.095,
now measurable for the algorithm itself — plus per-object paired outputs (the artifact Shamir 2024 did
not publish). Tooling custody: Ganalyzer public runnability **[VERIFY — Tori]**; if not runnable, we
implement the frozen algorithm ourselves (it is geometric and small).

**Secondary (cross-instrument, optional, explicitly subordinate):** a CE-ResNet-class equivariant
network. Training source ranked: (a) **synthetic spirals** (clean, no inherited prior); (b) GZ1 labels —
in which case it is run **as a labelled bias-transfer instrument** (Kun §3's "possible separate
contribution"), never as the anisotropy instrument, with the frozen leakage battery of §5 applied to it.
CE-ResNet code availability **[VERIFY — Tori]**. Disagreement between primary and secondary on the same
objects is itself a published diagnostic, not a discretionary choice.

**Sample selection — provably chirality-blind:** parent sample from **survey photometric cuts only**
(magnitude, size, surface brightness, star–galaxy separation) — **no human morphology flags, no GZ
membership** anywhere in the chain. Spirality gating uses a **mirror-invariant** score
s(x) := (u(x) + u(mirror(x)))/2 (any spiral-ness estimator u, symmetrised), so sample membership
cannot encode chirality. All cuts frozen before unblinding.

## 4. Pixel-path custody — the exposed surface equivariance cannot fix

The hole we must not reproduce, named: **Ganalyzer's own paper states it cannot ingest FITS directly
(TIFF/JPG/PPM/BMP only), and Shamir 2024's HSC conversion is undocumented** (Tori, prior-art receipt).
Controls, all frozen:

1. **One imaging source, one cutout route, exact versions** (Kun item 2), chosen via §8; checksums and
   query logs held to the Mittal–Singal custody standard.
2. **Raw-pixel ingestion:** the measurement path reads survey pixels in their native format with WCS;
   **no JPEG and no lossy or orientation-ambiguous conversion anywhere in the measurement path.** If the
   estimator needs a raster conversion, the converter is ours, lossless, with row-order handling
   explicit and unit-tested.
3. **WCS parity validation:** for every cutout, the parity of the WCS CD/PC matrix (sign of the
   determinant) is computed and logged; handedness is evaluated **in sky coordinates**, with the
   pixel→sky parity applied per object, not assumed constant.
4. **Injected chiral test images:** synthetic spirals of known handedness, both parities, injected at
   pixel level and pushed through the **entire** pipeline (download-format handling, conversion,
   estimator) at positions across the footprint. Required outcome: 100% correct signed recovery and
   exact swap under mirroring. **A single silent parity inversion is fatal** (Kun: "A silent parity
   inversion is fatal") — kill switch K-2.
5. **Scrambled-WCS null:** re-run the injected set with deliberately parity-flipped WCS to confirm the
   audit detects the fault it exists to catch.

## 5. Negative-control battery — what makes a null interpretable

All controls frozen, all reported regardless of outcome:

- **C1 Full-mirror run:** the entire accepted sample re-processed mirrored; label counts must swap
  exactly (identity receipt); D̂ must negate exactly. Published as paired per-object outputs with the
  mismatch rate (which the identity forces to zero — deviations indicate pipeline faults, not sky).
- **C2 Permutation nulls:** the §2 label-permutation mocks (positions fixed, signs shuffled).
- **C3 Hemisphere swaps / rotation nulls:** D̂ recomputed at axis −n̂ (must negate), at orthogonal axes
  (should be null-consistent), and under 24 h RA rotations of the axis grid.
- **C4 Covariate-leakage battery (Kun item 4, verbatim list):** dependence of sign(χ), |χ|, and
  abstention on footprint, depth, seeing/PSF, Galactic extinction, stellar density, crowding/deblending,
  angular size, inclination proxy, colour/arm-contrast proxies, magnitude/redshift where available —
  after mirror-pair accounting. **Ambiguous leakage returns INCONCLUSIVE** (his wording; frozen as a
  decision rule, not an aspiration).
- **C5 Monopole–gradient coupling test (from §0):** build the sky map of abstention rate and estimated
  per-region sensitivity; compute the coupling term between M̂ and each map's dipole; the measured D̂ at
  the fixed axes must exceed the coupling bound by the frozen margin or the axis result is
  INCONCLUSIVE.
- **C6 Split-sample stability:** D̂ by depth bin, hemisphere, and size bin; a real sky signal is stable,
  an instrumental one tracks the splits.

## 6. Boundary — what a result would and would not mean

**A positive result would NOT identify BHU.** The BHU closing record
(`LANA_BHU_PREDICTION_DERIVATION_20260811.md`, Rev 5; Kun PASS_FINAL_CLOSING_RECORD) stands: no source
supplies a calibrated BHU-specific sky-statistics target, and a measured asymmetry of any size or
direction is equally consistent with non-BHU anisotropic cosmologies and with residual astrophysical or
instrumental causes outside our battery. Kun's exact ruling is adopted verbatim: *"Any positive spin
result … would be a spin-anisotropy/statistical-isotropy result only."* A REPRODUCED outcome triggers an
**adversarial re-audit before any claim leaves the lane** — the required first interpretation of a
positive is "we missed a systematic," and the escalation path is a hostile hunt for it, not a paper. A
REJECTED-AT-CLASS outcome is a statement about **the two published claims at their own axes**, measured
with an instrument that cannot have caused either sign — not a proof that the sky is isotropic
everywhere at all amplitudes. This section is quoted in any artifact that leaves the lane, including any
video.

## 7. Attenuation and power — because biased calibration costs sensitivity

- **Hand-checked subsample:** N ≈ 500 accepted galaxies, stratified by |χ|, size, and depth, labelled
  independently by two human checkers **on randomly pre-mirrored images** (each image shown in a random
  parity so human chirality bias enters symmetrically and cancels in the accuracy estimate; assignment
  key sealed until after labelling). Yields accuracy a with binomial errors, per stratum.
- **Attenuation model:** measured amplitude scales as (2a − 1); per-stratum a feeds the §5-C5
  sensitivity map and the §2 correction.
- **Power gate (kill switch K-6):** with accepted-sample size N and estimated a, the minimum
  3σ-detectable corrected amplitude is ≈ 3·√3 / (√N·(2a−1)) [dipole-projection variance; exact form
  finalised in prereg]. Requirement: ≤ 0.02 (the published class floor). Indicatively, a = 0.9 needs
  **N ≳ 3×10⁴ accepted spirals**; abstention near Shamir 2024's 86% HSC rejection rate implies a parent
  sample ≳ 2×10⁵ **[estimate — finalise with real abstention in the spike]**. If the gate fails on the
  available data: INCONCLUSIVE-BY-POWER, declared, and the run does not happen.

## 8. Data requirements — the slot for Goru's sweep and Tori's access check

The design is data-agnostic tonight (per Hwao: do not freeze a data choice). Any candidate survey is
scored against these **minimum properties**, in order:

1. **Raw pixel access with documented orientation** — native-format cutouts or frames with per-object
   WCS, and *documented* cutout-service orientation behaviour (no silent flips). This is the property
   our GZ1 lane died without; a smaller survey that documents its frame beats a larger one that does
   not.
2. **Footprint covering both frozen axes' projection range** — usable sky on both sides of each axis
   (quantified in prereg as a minimum variance of cos θ over the accepted sample for each n̂; a
   footprint orthogonal to an axis cannot test it).
3. **Scale:** parent sample ≳ 2×10⁵ photometrically selected candidates (per §7's indicative gate),
   with magnitude/size distributions supporting an accepted N ≳ 3×10⁴.
4. **Covariate maps:** public depth/seeing/extinction/stellar-density maps for §5-C4/C5.
5. **Licence** permitting publication of derived catalogues and per-object receipts.
6. **Overlap with the claim regions** (both claims are SDSS-footprint; a disjoint footprint tests the
   axes but not the samples — acceptable, stated openly, but overlap is preferred).

Candidates the sweep should score (no choice made here): SDSS DR frames; DESI Legacy Survey
native cutouts; HSC DR3 **[VERIFY all three against properties 1–6 — Goru facts, Tori custody]**.

## 9. Kill switches — Kun's, adopted verbatim, plus ours

- **K-1 (Kun 1):** primary instrument must be training-free (or non-human-label-trained); if only a
  human-label-trained classifier is feasible, the study becomes a bias-transfer study or stops.
- **K-2 (Kun 2):** image custody — any failed parity validation or injected-image inversion halts the
  lane. A silent parity inversion is fatal.
- **K-3 (Kun 3):** mirror evidence — paired original/mirror outputs, mismatch rate, flip-balance,
  confidence/abstention deltas must be published receipts; a prose "mirroring works" is insufficient.
- **K-4 (Kun 4):** inherited-prior/selection controls — ambiguous covariate leakage ⇒ INCONCLUSIVE.
- **K-5 (Kun 5):** fixed axes first — no free-axis result is interpreted before the fixed-axis results
  are reported.
- **K-6 (Kun 6 + power):** one run, no revision after any statistic; multiplicity-corrected secondary
  cannot rescue a failed primary; power gate failure ⇒ INCONCLUSIVE-BY-POWER, no run.
- **K-7 (Kun 7):** prior-art boundary stated in every derived artifact (we combined; we did not invent).
- **K-8 (ours):** any parameter change after any sky statistic voids the run; re-entry only via a new
  prereg.
- **K-9 (ours):** if the §8 sweep finds no survey meeting properties 1–3, the verdict reverts to
  NOT_WORTH_DOING_YET — the design is filed, not forced onto unfit data.
- **K-10 (ours):** the §0 identity must pass its synthetic unit tests exactly (bit-exact count swap
  under mirroring) before any real image is touched; approximate equivariance is not equivariance.

## 10. Overnight plan — run-safe under Kun's BLOCK

Kun blocks any empirical run before the design freezes. Tonight's work therefore computes **no sky
statistic on real data**. Allowed and planned:

1. **Synthetic instrument spike:** implement w(x) and the χ wrapper; generate synthetic spirals (both
   parities, varying pitch/inclination/S-N); verify the K-10 identity bit-exactly; calibrate τ and
   estimate abstention on synthetics.
2. **Pixel-path audit tooling:** WCS parity checker, lossless converter with explicit row-order tests,
   injected-image harness (§4.4–4.5) — exercised on synthetic and public *calibration* frames only.
3. **Prereg statistics code:** §2 estimators and permutation machinery, validated on simulated
   catalogues with injected dipoles of known amplitude (recovery test), never on survey labels.
4. **Goru:** survey sweep scored against §8 properties 1–6 (facts to file). **Tori:** access, sizes,
   licences, cutout-orientation documentation custody; Ganalyzer/CE-ResNet code availability
   ([VERIFY]s of §3).
5. **Morning deliverables:** identity unit-test receipt, injected-image harness receipt, simulated
   power-curve, data-candidate scorecard — everything a freeze decision needs, nothing a freeze
   decision forbids.

## 11. Smallest publishable version

1. **Floor (no sky data at all):** the methods paper — the antisymmetrization identity and its limits
  (§0, including the monopole×gradient coupling), the custody protocol, the injected-image audit, and
  the prior-art matrix. Publishable as a methods/preregistration artifact; also simply *is* the prereg.
2. **The study:** one survey, primary instrument only, the two fixed-axis confirmatory tests with the
  full battery — REPRODUCED / REJECTED-AT-CLASS / INCONCLUSIVE per axis, receipts published.
3. **Stretch (only if 2 lands cleanly):** the secondary instrument cross-check and, if trained on GZ1,
  the labelled bias-transfer result (does an equivariant net trained on biased labels reproduce the
  human catalogue's asymmetry on the same objects?) — Kun's §3 observation, as its own bounded artifact.

---

**Open [VERIFY] register:** Longo/Shamir sign-convention derivations (freeze-time, from methods);
Ganalyzer public runnability; CE-ResNet code availability; §7 abstention and power constants (spike);
§8 candidate scoring (Goru/Tori). **Nothing here is frozen yet:** this brief goes to Kun's gate, the
§10 spike and §8 sweep fill the open slots, then the prereg freeze is a separate, sha-pinned artifact.
Nothing is published, accepted, or run; Duho decides.

— Lana, 2026-08-12.
