# Lana — sourcing the spiral fraction: what the literature contains, what must be counted, and what decides feasibility

**Lana (science / claim-boundary seat), 2026-08-12.** Per Duho: *"have lana source the spiral
fraction."* Inputs now in force: retention lower bound **85.72%** (Yui's re-measurement over the full
b/a > 0.4-admitted inclination range; the 60–69.3° band retains 51.38%), Cut-6 inclination survival
**~82%** (Tori, counted, 4/13 blocks, stable), certified parent lower bound **199,034**
(catalogue-checkable, 18.273143% of BRICKID keyspace; unqueried 81.7% can only add). Chain factor
after the parent: 0.82 × 0.8572 = **0.7029 × f_spiral**. **Boundaries held: no acceptance decision,
no sky run, no images, no chirality, no publication, no commit. Bounds, not point estimates.**

---

## 0. The finding up front

**After real effort against the primary papers: no published source states the spiral fraction as a
number conditioned on anything close to our cuts.** Every candidate is either unconditioned,
threshold-defined-but-never-summed, or a subsample count with no parent fraction (§2). The right
response is the one tonight has twice rewarded: **count it.** Galaxy Zoo DECaLS/DESI is morphology for
our own survey family, published as catalogues; §1 specifies two executable counts — one join-free and
nearly perfectly conditioned, one joined and exactly conditioned — either of which removes the last
prior from the chain. §3 gives the feasibility verdict as bounds: **(a) is excluded arithmetically;
the choice between (b) and (c) is decided by whether the counted fraction clears ≈ 13.1% — a
break-even the counts below settle in about a day of Tori/Goru effort.**

## 1. The countable routes (specified for Tori; execution needs Hwao/Duho authorization)

### 1.1 Route A — GZD-5 volunteer catalogue, join-free, conditioning nearly ours (run this first)

**Source, pinned from the paper (Walmsley et al. 2022, MNRAS 509, 3966, §sample):** NSA v1.0.0 parent;
**z ≤ 0.15**; *"primarily includes galaxies brighter than m_r = 17.77, the SDSS spectroscopic target
selection limit"*; **PETROTHETA ≥ 3 arcsec**; *"GZD-5 classified 262,000 DECaLS DR5-only galaxies
passing the criteria above."* Imaging: DECaLS — our survey's own southern imaging family.

**The count:** within the public GZD-5 volunteer catalogue (data.galaxyzoo.org / VizieR
J/MNRAS/509/3966 **[VERIFY exact table id at execution]**): numerator = rows passing the spiral
predicate (§1.3); denominator = all rows. **No join needed; no position exported; output is two
integers.** This is a fraction for: DECaLS imaging, z ≤ 0.15, m_r ≲ 17.77, size-cut parent — the
closest published conditioning to ours that exists anywhere.

**Residual mismatches, with directions:**
- **Size cut:** PETROTHETA ≥ 3″ (NSA Petrosian radius) vs our shape_r > 1.5″ (half-light). For disk
  profiles the Petrosian radius runs ≈ 2× the half-light radius **[VERIFY conversion factor at
  freeze]**, so the cuts are comparable in scale; if 3″-Petrosian is effectively stricter, GZD-5's
  parent is more resolved than ours → its fraction is **upper-leaning** on size.
- **Parent completeness:** NSA is a spectroscopic (SDSS) parent; ours is photometric with photo-z and
  the −99 rule. **Direction not determined.**
- **No b/a cut in GZD-5's parent:** their denominator includes edge-ons whose arms humans cannot vote
  spiral; our Cut-6 parent excludes them. Removing edge-ons raises the operative fraction → the
  GZD-5-parent fraction is **lower-leaning** relative to our b/a > 0.4 parent. (A refinement: also
  compute Route A restricted by the catalogue's own not-edge-on fraction ≥ 0.715 in the denominator —
  brackets the b/a mismatch from both sides.)
- **Magnitude:** 17.77 vs our 17.7 dered — near-identical; residual direction negligible relative to
  the above **[direction not determined; ~0.07 mag]**.

### 1.2 Route B — GZ DESI machine catalogue, joined, conditioned EXACTLY

**Source, pinned:** Walmsley et al. 2023 (MNRAS 526, 4768; Zenodo 8331338): automated (Zoobot)
morphology for **8.67M galaxies, r < 19, DESI Legacy DR8 footprint**; models predict volunteer vote
fractions to 5–10%; released as parquet catalogues (deep-learning catalog + volunteer catalogs).

**Join:** GZ DESI is keyed to DR8; our parent is DR10.1 (RELEASE 10000/10002, BRICKID, OBJID) — **no
shared row key across releases** [column names of the parquet (dr8_id form, ra/dec) not pinned
tonight — **[VERIFY from the parquet schema at execution]**]. Join = **positional crossmatch, unique
nearest neighbour within 1.0″** (both astrometry Gaia-tied; at shape_r > 1.5″ ambiguity is rare;
report the multiple-match count). Execution form: Tori uploads the parent key table (RELEASE, BRICKID,
OBJID, RA, DEC) server-side or scans the Zenodo parquet locally — either way **the output is aggregate
counts only: matched N, spiral-passing N at each threshold; nothing axis-relative is computed and
nothing per-object is exported** (same standing boundary as her photo-z joins).

**What Route B yields:** the spiral fraction over **exactly our Cut-1..6 parent** (every one of our
cuts applied to our own rows first; GZ DESI supplies only the morphology column). This is the
fully-conditioned number — no borrowed sample definition at all. Its one systematic: machine votes
are trained on human votes, so human feature-recognition limits propagate (deep-imaging helps; the
model is trained on DECaLS-depth images — same depth as our cutouts). For a *forecast prior* this is
acceptable; the operative acceptance remains our instrument's own (§4 of the previous spec stands).

### 1.3 The "is a spiral" predicate (both routes; thresholds pinned from the primary paper tonight)

From **Willett et al. 2013, Table 3** (the GZ2 clean-spiral criteria, the lineage convention the GZ
DECaLS/DESI trees inherit): **p(features/disk) > 0.430 ∧ p(not edge-on) > 0.715 ∧
p(spiral, yes) > 0.619, N_votes ≥ 20** (volunteer routes; the N-votes floor drops for the machine
catalogue). Report **three variants** so the result is an interval, not a point:
- **Lenient:** featured-or-disk ≥ 0.430 ∧ has-spiral-arms_yes ≥ 0.5;
- **Willett-clean:** the Table 3 triple above;
- **Strict:** has-spiral-arms_yes ≥ 0.8.
GZD-tree column names and any Walmsley-recommended thresholds to be confirmed against the paper's
appendix at execution **[VERIFY — do not improvise column mappings]**.

## 2. The literature record (fetched today; why citing cannot replace counting)

| Source | Sample definition (pinned) | Spiral fraction stated? |
|---|---|---|
| **Walmsley et al. 2022** (GZ DECaLS; MNRAS 509, 3966) | NSA v1.0.0; z ≤ 0.15; "primarily … brighter than m_r = 17.77"; PETROTHETA ≥ 3″; GZD-5 = 262,000 | **No summary fraction published** — the paper releases vote fractions, not a spiral count; Fig. 5 compares featured fractions GZ2 vs GZD only. Deeper imaging "reveal[s] spiral arms … not previously visible in SDSS imaging" → SDSS-era fractions are **lower-leaning** at our depth. |
| **Walmsley et al. 2023** (GZ DESI; MNRAS 526, 4768) | r < 19, DESI-LS DR8 footprint, 8.67M, machine votes | **No summary fraction in the record fetched**; the catalogue is the countable. |
| **Willett et al. 2013** (GZ2; MNRAS 435, 2835) | m_r < 17.0; petroR90_r > 3″; 0.0005 < z < 0.25; 304,122 (main 283,971) | **Thresholds published (Table 3), sum not published.** Countable from the public GZ2 table, but conditioning is SDSS-depth and R90-based — Route A/B are strictly better conditioned. |
| **Hart et al. 2016** (MNRAS 461, 3663) | luminosity-limited **subsample of ~18,000 spirals** | A spiral *sample*, not a fraction of a parent — not usable as f_s. |
| **Lintott et al. 2008** (GZ1) | ~900k SDSS galaxies, no size cut | No conditioned fraction in the fetched record; unconditioned GZ1/MGS-era figures (the remembered 27–31%) remain **untrusted for our size-cut parent — Goru's [UNSOURCED] stands for this family.** |

**Conclusion of the literature track:** the properly-conditioned number does not exist in print; it
exists as a one-day count against published catalogues. Citing anything above as f_s would smuggle a
conditioning mismatch into the deciding number — exactly what Duho's instruction was meant to end.

## 3. Feasibility — which of (a)/(b)/(c), as bounds

With accepted = parent × f_s × 0.82 × 0.8572 = parent × 0.7029 × f_s, requirement 100,000:

- **(a) Met at the already-counted keyspace? EXCLUDED.** 199,034 × 0.7029 = 139,905; f_s would need
  ≥ **71.5%** — above any spiral fraction ever reported for any local magnitude-limited sample we
  located tonight. Not credible; (a) is arithmetically dead regardless of the count.
- **(b) Met if more keyspace is counted?** Extrapolating the certified density to the full keyspace
  (199,034/0.182731 ≈ **1.089M** parent — an extrapolation, flagged: keyspace ≠ sky area; the only
  certified bound is 199,034): full-keyspace accepted = 765,600 × f_s. **Break-even: f_s ≥ 13.06%.**
  Keyspace share required as a function of the counted f_s (share = 0.13061/f_s):

  | counted f_s | keyspace share needed |
  |---:|---:|
  | 15% | ~87% |
  | 20% | ~65% |
  | 25% | ~52% |
  | 30% | ~44% |
  | 35% | ~37% |

- **(c) Not met even with full keyspace?** True iff the counted f_s < **13.06%** (or the density
  extrapolation fails low). No pinned number tonight licenses asserting f_s ≥ 13.06% — size-cut,
  depth-matched samples plausibly clear it with margin, but *plausibly* is exactly the word this
  count exists to delete.

**Plain answer: (a) is false. The program sits between (b) and (c), and the single number that
decides it is the Route A/B count. If f_s lands at 25% — the middle of the plausible range — the
requirement is met by counting roughly half the keyspace.** Margins to carry: the 82% is 4/13 blocks
(provisional-counted); the 0.8572 is a lower bound (favourable direction); 199,034 is a lower bound
(favourable); the 1.089M is an extrapolation (unfavourable if density falls in unqueried keyspace).

## 4. If both routes fail (the costed fallback)

If the GZD/GZ-DESI catalogues prove unjoinable or their predicates unmappable: the settling
measurement is a **blinded pilot morphology count on a random parent subsample** — N ≈ 2,000 parent
rows, images classified only for *spiral-vs-not* (no chirality, no axis anywhere in the pipeline),
two blind checkers + adjudication, giving f_s to ±2% (binomial). Cost: roughly one crew-day plus the
image-access authorization it would require — and it touches survey images, so it needs the same
authorization class as the sky run and is strictly a last resort. Route A needs neither images nor a
join; it should go first.

**Boundaries restated:** nothing here was executed; Routes A/B are specifications awaiting
authorization; no acceptance decision is made or implied; bounds throughout. Kun gates; Duho decides.

**Sources (fetched today):** Walmsley et al. 2022 (ar5iv full text, sample section + GZD-5 count);
Walmsley et al. 2023 + Zenodo 8331338 (r < 19 selection, file inventory); Willett et al. 2013 (ar5iv
full text, Table 3 thresholds, sample 304,122/283,971); Hart et al. 2016 (ADS/search record, ~18,000
spiral subsample); Lintott et al. 2008 (abstract). **[VERIFY] register:** GZD-5 VizieR table id;
GZ DESI parquet column schema; GZD-tree threshold recommendations (Walmsley 2022 appendix);
PETROTHETA↔half-light conversion for disks.

— Lana, 2026-08-12.
