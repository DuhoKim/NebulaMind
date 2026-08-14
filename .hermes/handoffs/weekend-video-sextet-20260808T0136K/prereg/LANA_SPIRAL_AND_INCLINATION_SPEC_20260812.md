# Lana — spiral fraction (properly conditioned) and the inclination cut as a countable

**Lana (science / claim-boundary seat), 2026-08-12.** Inputs: Tori's certified parent lower bound
(208,407 dered Cut-5; **199,034 meeting every catalogue-checkable requirement**; BRICKID keyspace
1..121,000 of 662,174 = 18.273143% — keyspace, not sky area; the unqueried 81.7% can only add) and
Goru's correct CANNOT_BE_DETERMINED. **Boundaries held: no acceptance decision (Duho owns it), no sky
run, no images, no chirality, no publication, no commit. Bounds, not point estimates.**

---

## 0. The three answers in one paragraph

**Task 1:** the properly conditioned spiral fraction is **[UNSOURCED as a number tonight — by design,
not failure]**: no primary source publishes a fraction conditioned on exactly our cuts, but **GZ2's
sample definition is pinned and is the closest published conditioning** (m_r < 17.0, petroR90_r > 3″,
0.0005 < z < 0.25 — a *size-conditioned* sample, unlike the bare MGS fractions Goru rightly refused to
trust), and the fraction for OUR cuts is **computable as a count from GZ2's public table** rather than
recalled — the same prior-to-countable conversion as Task 2. I specify that count verbatim below.
**Task 2:** the inclination cut is fully countable from `SHAPE_E1/E2`: survive iff
**shape_e1² + shape_e2² < 9/49** (exactly b/a > 0.4), executable in Tori's aggregate form as written in
§2. **The check:** Hwao's suspicion is confirmed — **Yui's retention was measured on synthetics with
inclination 0–60° only** (appendix, generator spec line: "inclination 0–60°"), while b/a > 0.4 admits
discs to **69.3°** (q₀ = 0.2). The 96.15% does **not** yet cover **22.7%** of the population the cut
will select; the conservative floor if that band retained zero is **74.4%**. Two closure options with
numbers in §3; the cheap one needs no sky data.

## 1. Task 1 — the spiral fraction, conditioned on our cuts

**Our parent's conditioning (Tori/Goru chain, catalogue-checkable):** DR10.1-South, brick_primary,
maskbits==0, TYPE≠'PSF', FLUX_R>0, 0 ≤ z_phot_median < 0.15, **dered r < 17.7**, **shape_r > 1.5″
(half-light)**.

**Why the usual numbers don't transfer (Goru was right to refuse them):** the remembered
Lintott 2008 / Bamford 2009 ~27–31% class figures describe the SDSS Main Galaxy Sample —
magnitude-limited, **no size cut**. Our parent is size-cut at shape_r > 1.5″, which preferentially
removes exactly the small, distant, feature-hidden galaxies whose presence *lowers* an unconditioned
spiral fraction. Applying an unconditioned fraction to a size-cut parent double-counts resolvability
and **understates** yield — the direction of the error is known even though its size is not.

**The pinned conditioning match (primary-source, fetched today):** Galaxy Zoo 2 (Willett et al. 2013)
selected **m_r < 17.0, petroR90_r > 3″, 0.0005 < z < 0.25** — magnitude within 0.7 mag of ours,
redshift range containing ours, and critically **a size cut**. Correspondence of the size cuts: for
disk-dominated profiles R90/R50 ≈ 2 (concentration ~2.0–2.3 for exponential disks **[VERIFY exact
figure at freeze; assumption flagged]**), so petroR90 > 3″ ≈ half-light > ~1.5″ — closely comparable
to our shape_r cut. GZ DECaLS (Walmsley et al. 2022) covers our *footprint and depth* and is the
second source; its abstract does not state the selection, and I will not quote its cuts from memory
**[VERIFY: pin the GZ DECaLS selection (NSA-based, size and magnitude limits) from the paper's §2
before any use]**.

**The number itself — specified as a count, not recalled:** the conditioned fraction is computable
from the **public GZ2 morphology table** (data.galaxyzoo.org / VizieR, Willett et al. 2013) with our
cuts applied to *their* columns — no survey images, no chirality, no DR10.1 rows:

> **GZ2-COUNT (for Tori/Goru, needs Hwao/Duho authorization to execute):** over the GZ2 main-sample
> table restricted to **0.0005 < z < 0.15** and **m_r < 17.0**: numerator = rows with debiased
> p_features × p_spiral ≥ T and N_class ≥ 20; denominator = all rows in the restriction. Report at
> **T = 0.5 (lenient) and T = 0.8 (strict)** as an interval, with raw row counts, catalogue version,
> and query text in the receipt. The strict/lenient pair brackets the threshold convention; both are
> counts from a published table, not priors.

**Residual conditioning mismatches, stated with their bound directions (never silently absorbed):**
1. **Magnitude 17.0 vs 17.7 (dered):** GZ2 does not cover our faintest 0.7 mag. Featured/spiral
   fractions generically fall toward the faint limit at fixed size cut, so the GZ2-count is
   **upper-leaning** for the faint extension. Treat the GZ2 interval as the bright-sample value; the
   faint-band value is unmeasured **[UNSOURCED — only a GZ DECaLS-based count or our own instrument
   can supply it]**.
2. **Spec-z vs photo-z:** GZ2 conditions on spectroscopic z; ours is photo-z with the −99 sentinel
   rule. Scatter across the z = 0.15 edge moves both ways; direction not determined; flag, don't
   guess.
3. **Human "has spiral arms" vs our instrument's acceptance:** the *forecast-relevant* fraction is
   ultimately "fraction of parent whose arm winding OUR instrument recovers at DECaLS depth," which
   only the instrument measures. Every catalogue fraction — GZ2 or GZ DECaLS — is a forecasting
   bound, not the operative quantity. (Walmsley's abstract itself notes deeper DECaLS imaging reveals
   spiral arms "not previously visible in SDSS imaging" — so SDSS-era human fractions are
   **lower-leaning** for arm *existence* at our depth, opposing the direction of mismatch 1;
   the honest statement is an interval, which is what GZ2-COUNT produces.)

**If no comparable size-conditioned source is accepted:** then the answer stays [UNSOURCED] and the
measurable replacement is a **pilot classification of a random parent subsample under the frozen
instrument on synthetic-validated thresholds** — which is a sky-adjacent act requiring the prereg
freeze and authorization; it cannot be done tonight and is not proposed as a shortcut.

## 2. Task 2 — the inclination cut, as a countable Tori can execute verbatim

**Column basis (pinned in Tori's route binding §5):** DR10.1 sweep `SHAPE_E1`, `SHAPE_E2`; Tractor
ellipticity |e| = (1−q)/(1+q), q = b/a; hence **b/a = (1 − |e|)/(1 + |e|)** with
|e| = √(SHAPE_E1² + SHAPE_E2²).

**Threshold and exact algebra:** survive iff **b/a > 0.4**. Since (1−e)/(1+e) > 0.4 ⟺ e < 3/7,
the cut in catalogue columns is exactly:

> **Cut 6 (inclination; append to the existing chain in the same aggregate-count form):**
> `POWER(shape_e1,2) + POWER(shape_e2,2) < 0.1836734693877551`  — i.e., e² < 9/49 ⟺ b/a > 0.4 —
> with the validity predicate: `shape_e1` and `shape_e2` finite; rows with non-finite values FAIL
> (consistent with Tori's shape-validity rule; e ≥ 1 is excluded by the threshold itself).
> Count survivors after Cut 5, aggregate count only, no per-object retention.
> Note: TYPE='REX' rows carry e ≡ 0 and pass trivially — correct behaviour (roundness is not
> inclination), recorded so nobody "fixes" it later.

**Justification of 0.4 — how face-on arms must be:** for an inclined thin disc with intrinsic
axial thickness q₀, cos²i = (q² − q₀²)/(1 − q₀²). At q = b/a = 0.4: **i = 69.3°** for q₀ = 0.20,
**i = 67.6°** for q₀ = 0.13 — i.e., the cut keeps discs within ~67–69° of face-on. Physically, arm
winding direction requires the projected spiral geometry to remain single-valued along the arm; past
~70° the near and far arm segments overlap in projection and the winding sense degenerates —
this is the standard exclusion in the handedness literature (edge-on systems have no defined
chirality; b/a-type cuts near 0.4 are conventional **[VERIFY: pin one primary usage — e.g., the exact
inclination/axis-ratio cut in Longo 2011's §2 — at freeze; not from memory]**). The threshold was
frozen in design V2 §3/I-5 before tonight's counting question, which is the right order.

**Expected survival for orientation-random discs (forecast context only, not a count):** uniform
cos i ⇒ P(b/a > 0.4) = 1 − cos(69.3°) → **64.6%** of pure discs (q₀ = 0.2). The real parent contains
non-disc types whose survival differs; that is exactly why Cut 6 is now a **count**, not this number.

## 3. The check Hwao ordered — does 96.15% cover the population Cut 6 selects? **No.**

**Receipt facts:** Yui's production appendix (generator spec) states the synthetic population was
drawn with **"inclination 0–60°"** (both the 20,000-image training set and the 12,000 held-out set;
armless nulls "over the same inclination/S-N ranges"). The 96.44/96.15% retention and 100%
accepted-sign accuracy were measured on that population.

**The mismatch, quantified:** Cut 6 admits discs to i = 69.3° (q₀ = 0.2). For orientation-random
discs passing the cut, the band **i ∈ (60°, 69.3°]** is (0.5 − 0.354)/(1 − 0.354) = **22.7% of the
selected population** — and the instrument's retention and sign accuracy there are **unmeasured**.
Two further unknowns sharpen it: (a) the synthetic inclination *density* on [0°, 60°] is not stated —
uniform-in-i overweights face-on relative to the real uniform-in-cos-i population even inside the
measured range **[VERIFY from the generator code / manifests]**; (b) the generator's "analytic
squeeze" may not reproduce high-inclination arm blending realism. **Conservative floor:** if the
unmeasured band retained zero, effective retention over Cut-6 survivors is
0.9615 × 0.7735 = **74.4%** — the yield chain is broken at a second point exactly as suspected.

**Two closure options (Duho decides; no measurement is authorized by this spec):**
- **Option A (recommended; cheap; no sky data):** extend the held-out synthetic measurement to
  **i ∈ [0°, 70°]**, drawn uniform in cos i, re-report retention and sign accuracy per inclination
  bin at the SAME frozen τ and weights (no retraining — τ and weights untouched; this is
  measurement, not calibration). Yield forecast then uses the cos-i-weighted retention over Cut-6
  survivors. If high-inclination sign accuracy degrades below 100%, that is a finding, not a
  failure — it feeds the attenuation model.
- **Option B (no new measurement; costs yield):** tighten Cut 6 to match the measured range:
  i ≤ 60° ⟺ b/a > 0.529 (q₀ = 0.2) ⟺ **e² < 0.0948** (e < 0.3079). Survival among random discs
  drops 64.6% → 50.0% (−22.6% relative) — directly against the already-tight yield margin.

## 4. What tonight's numbers do to the yield question (bounds only)

- **Certified-only infeasibility, stated plainly:** even at f_spiral = 100%, the certified parent
  alone gives 199,034 × 0.646 × 0.9615 ≈ **123,700** ceiling — so reaching 100,000 from the queried
  18.27% keyspace alone would require f_spiral ≥ **81%**, which no population supplies. **More
  keyspace must be counted regardless of what the spiral fraction turns out to be.**
- **Keyspace-required table** (extrapolating the certified density 199,034/0.182731 ≈ 1.089M to full
  keyspace — an extrapolation, flagged: keyspace ≠ sky area and density need not be uniform; the only
  *bound* is the certified 199,034): required parent P = 100,000/(f_s × 0.646 × 0.9615), as keyspace
  share of the extrapolated density —

  | if f_spiral (GZ2-COUNT lands at) | required parent | keyspace share needed |
  |---:|---:|---:|
  | 15% | ~1.073M | ~98% |
  | 25% | ~0.644M | ~59% |
  | 35% | ~0.460M | ~42% |

  (All using the **unrepaired** 0.9615; under §3's conservative 74.4% floor, multiply required
  parents by 1.293 — at f_s = 25% that is ~0.833M, ~76% of keyspace. The §3 repair is therefore
  yield-critical, not cosmetic.)
- Design V2's old boundary line — "any parent below 1,142,858 cannot produce 100k at the optimistic
  chain" — now has a measured companion: the extrapolated full-keyspace parent is **~1.09–1.14M**,
  i.e., the program sits *at* that line, which is why the spiral fraction and the §3 gap are the two
  numbers that decide feasibility.

## 5. Actions this spec defines (all need authorization; none executed here)

1. **GZ2-COUNT** (§1): public-table count at T = 0.5/0.8 — Tori custody + Goru query.
2. **Cut 6 count** (§2): `e² < 9/49` aggregate count appended to Tori's chain.
3. **Option A synthetic extension** (§3): 0–70°, uniform cos i, frozen τ/weights.
4. **[VERIFY] register:** GZ DECaLS selection cuts (pin from paper §2); R90/R50 ≈ 2 disk-concentration
   figure; one primary-source inclination-cut precedent (e.g., Longo 2011 §2); synthetic inclination
   density on [0°, 60°] (from generator manifests).

**No acceptance decision is made or implied. Bounds, not point estimates, throughout. Nothing runs on
sky, nothing is published, nothing is committed. Kun gates; Duho decides.**

— Lana, 2026-08-12.
