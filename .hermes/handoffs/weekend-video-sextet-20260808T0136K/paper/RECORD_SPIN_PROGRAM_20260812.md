# RECORD — the spin-parity / Longo-amplitude program, 2026-08-08 → 2026-08-12
## A completeness-first record so nothing here has to be rediscovered

**Lana, 2026-08-12.** Per Duho: *"yes, it's not publishable yet. so just document so that you don't
lose in the future."* This is a **record, not a submission draft** (the earlier referee-structured
draft is retained beside this file as raw material). Optimised for the reader six months from now —
most likely us — who needs to answer **"can I use this?"** and **"why did they stop?"** without opening
twenty receipts. Completeness beats polish; the dead ends are kept deliberately, because the dead ends
are the expensive knowledge. **No result is claimed anywhere in this record. Nothing about spin
anisotropy in the universe; no adjudication of Longo or Shamir; no BHU claim. Nothing published,
submitted, or uploaded; the video track is on hold; Kun gates this record.**

> **Revision 2 (2026-08-12) — three wording repairs per Kun's record gate
> (`paper/KUN_RECORD_GATE_20260812.md`, PASS AS A RECORD WITH THREE REQUIRED WORDING REPAIRS). All
> three are operational-status repairs, not scientific ones — his rule: "A future reader must not
> infer that the instrument or preregistration has been cleared for sky use." Carried openly per §6
> item 10; replaced wording quoted verbatim:**
> **(1) Fast answer, instrument row.** Was: *"Can I use the instrument? Yes, with its receipts (§2):
> frozen weights + seeds + τ + identity tests are all hash-pinned. Do not retrain or re-calibrate
> without re-running the receipt suite; do not touch τ after any sky data."* — too operationally
> permissive read alone. Replaced with Kun's exact wording, adding "as the frozen synthetic-trained
> candidate instrument for preregistration work" and "Do not run it on real galaxy images until the
> preregistration is frozen and separately authorized."
> **(2) §2 identity paragraph.** Was: *"training defects cost sensitivity, never validity"* — safe as
> bounded there, but over-extendable to all trained-model failures. Replaced with Kun's exact wording:
> *"constant chirality-calibration defects in the wrapped estimator cost sensitivity; validity still
> depends on the pixel-path, sample-selection, and monopole-gradient controls below."*
> **(3) §6 item 4.** Was: *"Human labels, or ML trained on human chirality labels, as the anisotropy
> instrument — use the identity wrapper; it holds for any w."* — readable as banning human labels
> from calibration and bias-transfer work, which the design itself uses. Replaced with Kun's exact
> wording scoping the ban to the **result-bearing** instrument and admitting human labels for blinded
> attenuation checks and explicit bias-transfer studies.
> **Also folded:** Kun's settled/open lists into §0.1, so the permission-seeking reader meets them
> beside the fast answers rather than only in his gate. What he cleared is unchanged: numbers match
> the source receipts (his spot-check list), §6 items 4-as-scoped and 9 stand, route unlock
> conditions are the real ones, attribution accurate.**

---

## 0. Fast answers

| Question | Answer |
|---|---|
| **Why did they stop?** | Not a failure — a boundary. The program advanced to a drafted preregistration for a **Longo-amplitude test** with a bound survey route. The empirical run is BLOCKED at the last honest step: the accepted-yield count (BS-1) is still an assumption chain, not a measured count, and touching real catalogue rows is exactly the step that requires separate authorization. Everything earlier closed for stated, receipted reasons (§1). |
| **Can I use the instrument?** | Yes as the frozen synthetic-trained candidate instrument for preregistration work, with its receipts (§2). Do not run it on real galaxy images until the preregistration is frozen and separately authorized; do not retrain or re-calibrate without re-running the receipt suite; do not touch τ after any sky data. |
| **Can I use the prereg?** | Yes as a draft: `prereg/PREREG_LONGO_AMPLITUDE_TEST_20260812.md`. Ten binding slots; the open ones are listed in §5. It is NOT frozen. |
| **Can I revive a closed route?** | Read that route's entry in §1 first. Each has an explicit unlock condition. Reviving one without meeting its unlock condition will reproduce a documented dead end. |
| **What is the single biggest unresolved risk?** | Sample yield. Every count in the DR10.1-South chain is `[UNKNOWN — requires catalog query]`; the "~175,000 accepted" figure is three literature priors multiplied together (§4.4). If real retention lands below ~35% acceptance or the parent below ~1.15M, the power gate kills the run (INCONCLUSIVE-BY-POWER). |

### 0.1 What is settled, what is open (Kun's record-gate lists, folded in so they live here, not only in his gate)

**Safe to rely on now:**
- No result exists.
- The BHU route is closed for current sky-statistics work because no calibrated BHU-specific target
  exists in the cited literature.
- The V1 class-floor design died on power/yield.
- The V2 Longo-amplitude route is the live design path but is blocked at accepted-yield / freeze.
- Pixel-path parity, resampling mirrors, and thin-null calibration are real failure modes with
  receipt-backed numbers.
- The production synthetic-trained instrument has receipt-backed synthetic retention and identity
  tests, **but not authorization for real-image use.**

**Still carries [VERIFY] or open status:**
- exact receipt line for the raw-vs-dereddened flag (§4.3);
- GZ1 paired-flip object count before external use (§1-R1, register);
- Shamir 2012 implied amplitude class (prereg BS-10);
- trailing-arm universality citation in the filament assessment;
- real DR10.1 accepted-yield counts (§4.4 — the blocker);
- real-image retention/acceptance and WCS pass rate (measurable only during an authorized run).

## 1. Route ledger — what was tried, what happened, what it cost, what remains open

### R1 — Galaxy Zoo 1 spin-parity lane (the original route). STATUS: DEAD-BUT-INSTRUCTIVE.
**What it did:** built the paired-flip test — classify each GZ1 galaxy's label against its mirrored
counterpart. **What it found:** perfect label flipping under mirroring (0 concordant of ~6,908 paired
objects) but **unbalanced**: 3,290 CW→ACW vs 3,618 ACW→CW, **dA_paired ≈ 0.095, SE ≈ 0.024**,
repeating across all four scored cells. Because mirroring cancels any genuine sky signal by
construction, this is a **sorter (human-labeller) asymmetry, not a sky measurement** — a modern,
larger-magnitude confirmation of Land et al. 2008's bias finding. **Why it died:** ruled
FRAME_UNSTATED — Galaxy Zoo never documents whether served images were as-seen or de-mirrored, so the
sign of the bias cannot be anchored to the sky and the result is **alive but uncitable**.
**Unlock condition:** the GZ team states the frame convention (one letter; was proposed, not sent).
**Do not repeat:** any handedness work on a catalogue whose image-frame convention is undocumented;
any human-labelled or human-label-trained chirality source (see R5's instrument for why that
restriction became solvable).

### R2 — Black-hole-universe cosmology (the original motivation). STATUS: CLOSED, WITH A CLOSING RECORD.
**Closing record:** `reviews/LANA_BHU_PREDICTION_DERIVATION_20260811.md`, Revision 5
(SHA-256 b244ea0a…), Kun PASS_FINAL_CLOSING_RECORD_ON_REVISION_5; Tori citation-custody PASS after a
fresh-session re-verification. **The finding:** "BHU" is not one model — at least five programmes that
disagree (Pathria's GR identification; Poplawski's torsion bounce, which *explains apparent isotropy*;
Poplawski's rotating-parent axis scenario; Smolin's CNS; the Frolov–Markov–Mukhanov/Easson–
Brandenberger/Dymnikova baby-universe branch, whose stated prospects are PBH populations and GW echoes,
not sky statistics). The axis source, arXiv:1910.10819**v2** (revised 29 May 2025 — v1 contains no
axis language at all), is physics.pop-ph with **no journal version located as of 2026-08-11**; its
full text has real mechanics (Kerr-radius FLRW correction, Λ = 3Ω²/c²) and explicitly states CW/ACW
counts "should be different" — an **explicit, source-backed qualitative claim, but not a calibrated or
pre-data forecast** (v2 postdates the handedness studies it cites). It supplies **no amplitude, scale,
redshift law, lower bound, independently predicted axis, or acceptance region.**
**Kun's boundary, verbatim, which any future mention must carry:** nothing currently published gives a
distinguishable BHU sky-statistics prediction — **which is NOT the same as BHU being untestable in
principle.** The one falsifiable number in the family is CNS's neutron-star branch (Brown–Lee–Rho:
Brown–Bethe maximum ~1.5 M☉; a mass ≳ 2 M☉ would "put in serious doubt or simply falsify" the chain;
PSR J1614−2230 at 1.97 ± 0.04 and PSR J0740+6620 at 2.08 ± 0.07 (68.3% credibility) **enter** that
regime; the disjunction is not adjudicated by us) — nuclear astrophysics, not sky statistics, fully
exploited by others. **What it cost:** four sky-statistics lanes (spin handedness, public-data
isotropy/parity, quasar dipole, 4PCF) ran before anyone read the primary BHU literature; when we did,
every lane's dead end was explained at once. **Do not repeat:** (a) hunting generic anisotropy data as
a "BHU test" — generic anisotropy is all the axis scenario offers, so you land in other people's
disputes; (b) characterising any paper from its abstract — **five engines did that to 1910.10819 and
all five were wrong**; v1-vs-v2 version history was load-bearing. Read full texts or mark [VERIFY].

### R3 — Quasar number-count dipole (Mittal–Singal). STATUS: CLOSED AS A STUDY; PRODUCED A METHODS NOTE.
**What happened:** the Mittal 2024 / Singal 2024 factor-of-3–4 amplitude disagreement on (strongly
supported) the same Quaia v0.1.0 release was found **non-attributable from the published record** —
choices coupled, an order-unity mask correction unstated, different estimands. Deliverables that
stand: the external methods note (`reviews/LANA_METHODS_NOTE_MITTAL_SINGAL_ATTRIBUTABILITY_20260811_
EXTERNAL.md`, Kun PASS, permitted claim frozen in its §5) and a passed video. **Why closed:** Duho —
*"quaia data is already has been used for anisotropy studies at least twice… don't spill sweat on
it."* **Unlock condition:** none sought; the note's own §4/§5 name what a reconstruction scope would
require (Tori-verified recoverable artifacts or recorded replacement conventions).
**Do not repeat:** re-running the same dipole question on new data and calling it new; freezing
seat-name provenance into external artifacts (the note needed four revisions to become external-clean
— the lesson list lives in its changelog).

### R4 — 4PCF parity (Philcox / Hou–Slepian–Cahn vs Krolewski et al.). STATUS: PARKED, ENTRY DEFINED.
**Assessment:** `reviews/LANA_4PCF_PARITY_ENTRY_ASSESSMENT_20260811.md`. One defensible narrow entry
exists: a covariance-robustness reanalysis on *published* 4PCF data products (no tetrahedra of our
own), because the live dispute sits in the covariance/significance construction, not the data vector.
**Four kill-switch preconditions were never executed** (primary reads confirming the dispute locus by
quotation; redundancy check that no published artifact already is that study; Tori custody on the
public products; DESI DR1 parity status). **Why parked:** Duho redirected to the spin dispute itself.
**Unlock condition:** run the four checks; any failure → NOT_WORTH_DOING_YET stands. **Do not
repeat:** independent full 4PCF measurement (compute-blocked, redundant), or any covariance study that
doesn't first check whether Krolewski/DESI already published the cross-covariance table.

### R5 — The spin-anisotropy dispute → the Longo-amplitude test. STATUS: LIVE, BLOCKED AT THE YIELD COUNT.
**Chain of artifacts, in order:** entry assessment (+Rev 2 on Tori's prior-art facts:
`reviews/LANA_SPIN_ANISOTROPY_ENTRY_ASSESSMENT_20260811.md`) → Tori prior-art custody
(`reviews/TORI_SPIN_PRIOR_ART_20260811.md`: five method families, each holding **at most one** of
{image-level labels, orientation custody, enforced antisymmetry, preregistered fixed axes}) → design
V1 (`reviews/LANA_SPIN_DESIGN_BRIEF_20260812.md`) → feasibility spike (`spike/`) → **the class-floor
abandonment** (below) → design V2, narrowed per Duho: *"narrow it to Longo's amplitude"*
(`reviews/LANA_SPIN_DESIGN_BRIEF_V2_20260812.md`) → prereg draft
(`prereg/PREREG_LONGO_AMPLITUDE_TEST_20260812.md`) → filament-alignment assessment
(`prereg/LANA_FILAMENT_ALIGNMENT_ASSESSMENT_20260812.md`) → production-instrument receipts (§2) →
survey-route binding (§4) → **STOP at the real-catalogue boundary.**

**The class-floor abandonment arithmetic (keep this; a submission would cut it):** V1's indicative
N ≥ 30,000 gate was wrong: Goru's exact simulation gives **8.0% power at A = 0.02, p < 0.001,
N = 30,000**. Reliable power at the class floor needs **N ≥ 200,000 accepted** — and no public survey
supplies it: DESI Legacy best-case **~175,000** (itself an assumption chain, §4.4), Pan-STARRS
**262,000 on paper but ~33,000 in Shamir's real run** (seeing/noise destroys arm gradients), HSC
~105,000, Euclid Q1 ~11,000. Duho resolved by narrowing to **Longo's A ≈ 0.0408**, where N = 100,000
gives 100% simulated power (76% at 30k). **Consequence, stated in every boundary since:** a null
tests *Longo's amplitude at Longo's axis* — canonical sentence, byte-identical wherever it appears:
> **"A null here does not establish that the sky is isotropic; it rejects only Longo's published amplitude at Longo's published axis if the preregistered rejection rule is met."**

## 2. The instrument as built — every number and hash in one place

**The identity (the design's first principle):** χ(x) = (w(x) − w(mirror(x)))/2 with mirror = pure
index reversal obeys χ(mirror(x)) = −χ(x) **for any w / any weights / any training** — bit-exact
1000/1000 on synthetic spirals, max |χ(m(x)) + χ(x)| = 0.0. It guarantees: no manufactured net
asymmetry (paired-flip ≡ 0 by architecture); mirror-invariant acceptance (|χ|); and constant
chirality-calibration defects in the wrapped estimator cost sensitivity; validity still depends on the
pixel-path, sample-selection, and monopole-gradient controls below — demonstrated by a real bug (naive
circular unwrap) that inverted 100% of
recovered signs while the identity held 1000/1000. It does NOT cover: upstream pixel-path chirality,
non-equivariant sample pre-selection, or monopole × sensitivity-gradient coupling (all handled by
design controls, not by the identity).

**Production classifier (primary instrument), all receipt values
(`prereg/YUI_PRODUCTION_ESTIMATOR_RECEIPT_20260812.md`, `train_results.json`,
`receipt_results.json`):**
- Shared-trunk ResNet-18-class, χ_net = (f(x) − f(mirror(x)))/2, index-reversal mirror only;
  trained on **synthetics only** — no human chirality label anywhere.
- Training set 20,000 images; master seed **LONGO-AMPLITUDE-FREEZE-M1**; per-image seeds
  SHA-256(M‖i); manifests: train-20000 sha 498a505c84bb6d70…, null-8000 sha 1963132f2f36e7aa…,
  heldout-12000 sha 9b8607b7eb3b863d….
- **Weights FROZEN:** file `prereg/weights_frozen.pt` sha256
  83008c1cbdae511af5d30020540e1e281c62c2bd95d3cb05527fc0687bf49e6d; canonical serialization sha256
  1075a4d91c295d7f3256128534a0b8c4d097fb9d162169df1ac698843637a589. Policy: never touched after sky
  data.
- **τ = 4.4006456017494235** — 99.5th percentile of |χ_net| on the 8,000 frozen nulls, calibrated
  *before* any retention measurement.
- **Retention on 12,000 held-out synthetics: 96.44% central, 96.15% one-sided lower 95%**; sign
  accuracy of accepted = **100% in every S/N bin**; retention **rises** with S/N: 89.11% (S/N 2–5,
  n=3452) → 99.07% (5–10) → 99.69% (10–20) → 99.43% (20–50). Kun's arithmetic uses the lower bound:
  at 0.9615, N ≥ 100,000 accepted needs a parent of ≈ 104,000 *classifiable* spirals.
- **Production-raster receipts (128×128 float32):** R1 mirror∘mirror byte-exact 200/200; R2
  antisymmetry bit-exact 200/200; R3 signed zero — χ_sym = 0.0, bits 0x0 vs 0x80000000, value-equal,
  ordered comparison in the acceptance path (never signbit/copysign).
- Stack: isolated venv `prereg/venv_torch` (torch 2.8.0, numpy 1.26.4, ~439 MB), MPS training
  (10.6 min), single-thread CPU eval. Caveat that must survive: synthetic S/N bins; real-image PSF,
  blends and artifacts are unsimulated; the DR10.1-South S/N distribution must be mapped before yield
  multiplication.

**Secondary (deterministic) tracer — disqualified as-is, and the disqualification is a §3 finding:**
spike version (argmax polar peak-tracing, `spike/yui_identity/w_chi.py`): τ = 4.198 from **240**
nulls → apparent ~7.8% retention; recalibrated on the 8,000-null set: **τ = 5.916, retention 0.13%
central / 0.089% lower-95, and inverted in S/N** (0.41% at S/N 2–5 → 0.077% → 0.0 → 0.0). A better
deterministic w (peak prominence, multi-arm consensus) is an open task; its identity wrapper is
already proven.

## 3. Three failure modes, each with a number — the transferable knowledge

1. **Resampling mirror:** an interpolating reflection (axis off-grid by 0.25 px, bilinear) violates
   the identity by **0.058–0.944** — 1–20% of χ scale, i.e., up to ~20× the disputed 0.04 signal.
   Control: index-reversal-only mirror; byte-exact mirror∘mirror test; a canary test that *proves* the
   suite detects a resampling mirror.
2. **Undeclared row flip:** honouring a flip's determinant recovers the true sky sign; silently
   ignoring the same flip **inverts every galaxy consistently and invisibly** — degradation zero,
   correctness inverted. In a literature where S/Z vs CW/ACW conventions already vary, a pipeline
   inversion is indistinguishable in a published table from a convention choice. Control: per-object
   WCS determinant parity + declared row order + injected known-chirality sources + a silent-flip
   control that the audit must *catch*.
3. **Thin null calibration:** 99.5th percentile from 240 nulls (≈1.2 expected tail events — the
   threshold was set by the 2–3 noisiest nulls) made a 0.089%-retention instrument look like a 7.8%
   one. Diagnostic signature: **retention inverted in S/N** = acceptances are noise. Control: ≥8,000
   nulls for a 99.5th percentile (≈40 tail events); τ frozen before any retention or sky measurement;
   retention-vs-S/N a mandatory receipt with inversion disqualifying.

**Provenance, kept on purpose:** modes 1 and 3 (and the §2 sign-inversion bug) were found by
re-measuring **our own earlier work** under our own receipt discipline — not by auditing others. That
is the discipline functioning, and any future write-up keeps the failed versions in the text.

## 4. Survey-route facts that today exist only in receipts (first things that would be lost)

Source: `prereg/TORI_SURVEY_ROUTE_BINDING_20260812.md` (+ its evidence dir) and
`prereg/GORU_ACCEPTED_YIELD_RECEIPT_20260812.md` (sha df08a525…, 12:57 KST revision).

**4.1 The bound route (frozen):** DESI Legacy **DR10.1 South (DECam)** only — never `ls-dr9-north`,
never the composite `ls-dr10` layer (north/south seam at Dec 32.375°). Measurement pixels: the
generated FITS cutout service `https://www.legacysurvey.org/viewer/fits-cutout` with frozen params
`layer=ls-dr10-south&pixscale=0.262&bands=grz&size=256`, FITS only, **no post-delivery transform of
any kind**; the delivered generated-TAN pixels + WCS *are* the measurement input (upstream Lanczos-3
resampling accepted on exactly those terms, never repeated downstream). Catalogue route: DR10.1
sweeps under `10.1/` (RELEASE 10000/10002), row-key join `(RELEASE, BRICKID, OBJID)` — coordinate-only
joins forbidden where a row key exists. Brick summary: **post-December-2023 replacement only** (the
original was replaced for inaccurate counts/columns). Longo's axis maps to
(RA, Dec) = (216.9844°, +32.0606°), antipode (36.9844°, −32.0606°) — both on the DR10-south side of
the seam; footprint var(cos θ) ≥ 0.15 remains an *empirical, uncomputed* gate.

**4.2 Distortion branch (frozen):** **fail-closed on distortion.** Any SIP/PV/CPDIS/DET2IM metadata →
halt before any object statistic; no local-Jacobian branch implemented; no silent linear-determinant
fallback; identical delivered WCS across g,r,z required or halt. The one permitted header check
(16×16 r-band, 5,760 bytes, sha ac212f9d…) returned clean TAN, no distortion keys, CD determinant
−5.2966e-09 → **linear WCS parity REVERSING**, FITS array-transform determinant +1, combined parity
REVERSING — a live demonstration that this route's parity must be carried per object, not assumed.

**4.3 The traps Tori's binding caught (each would have silently corrupted a later run):**
- **Photo-z −99 sentinel:** the row-matched `10.1-photo-z` product fills failures with −99; a naive
  `z < 0.15` cut passes them. Goru's Cut 3 is therefore frozen as `0 ≤ z_phot_median < 0.15`.
- **Raw-vs-dereddened ambiguity:** Goru's Cut 4 computes r from raw `FLUX_R`, while the covariate
  matrix defines r and g−r as extinction-corrected via `MW_TRANSMISSION_*`; the SDSS-analogue
  r < 17.7 limit's convention is thereby ambiguous as written. **Must be frozen (one convention,
  stated) before any counting** [attribution pointer: flagged in Tori's audit trail — **[VERIFY exact
  receipt line]**].
- **Gaia version trap:** Legacy's embedded Gaia columns are **EDR3**; the covariate battery requires
  **DR3** stellar density — must come from `gaiadr3.gaia_source` at the ESA TAP endpoint (CC BY-NC
  3.0 IGO; anonymous queries fine).
- **WCS-validity loss is uncountable in advance:** per-object cutout delivery and WCS pass/fail can
  only be counted with per-object image headers — i.e., only during an authorized run. Any yield
  forecast excludes it by necessity.
- **`FLUX_R > 0`** added to Cut 2 to reject zero-optical-flux DUP rows that survive `TYPE != 'PSF'`.
- Known product issues to handle at counting time: 52 SGA large galaxies missing from DR10
  processing; duplicate Gaia `ref_id` issue; ~2% of Tractor bricks may have header/catalogue
  disagreements (rsync-era); `maskbits==0` chosen over selective bit exclusion (Goru's stated
  rationale: no unmodeled artifact survives).
- **Licence state:** Viewer images CC BY 4.0 with exact visible credit "Legacy Surveys / D. Lang
  (Perimeter Institute)"; paper acknowledgment required; photo-z use requires citing Zhou et al.
  (2023) + extra acknowledgment; **no separate catalogue licence found — derived-catalogue
  publication permission is an open freeze item, not assumed.**

**4.4 The yield chain — what is a count and what is a prior (keep; this is the honest core):**
Frozen cut pipeline (Goru, revised): brick_primary ∧ maskbits==0 → TYPE≠PSF ∧ FLUX_R>0 →
0 ≤ z_phot_median < 0.15 → r < 17.7 → SHAPE_R > 1.5″. **Every surviving count is
`[UNKNOWN — requires catalog query]`.** The multiplied priors: spiral fraction ~25% (GZ DECaLS),
inclination survival ~70% (b/a > 0.4), classifier acceptance ~40–50% (literature CE-ResNet; our
production classifier's *synthetic* retention is 96.4%, but its real-image acceptance is **strictly
unknown**). Optimistic conversion ≈ 8.7% of parent → 100,000 accepted needs a parent ≈ **1.15M**
(at 35% acceptance: ≈ **1.6M**, which DR10.1-South likely cannot supply). Boundary arithmetic worth
keeping: at 25%×70%, the production estimator must retain ≥ **28.57%** of surviving face-on spirals
for a 2M parent to reach 100k; any parent below **1,142,858** cannot reach 100k at the optimistic
chain. **Tori's contradiction audit stands: "~175,000 accepted" is an assumption-chain output, not a
DR10.1 product count; BS-1 is OPEN and freeze condition 2 is PARTLY CLOSED.**

## 5. Preregistration state (draft, not frozen)

`prereg/PREREG_LONGO_AMPLITUDE_TEST_20260812.md` (sha at write: ac43490054b159610385b8faac28dc4e…).
Frozen in the draft: decision regions (REPRODUCED-LONGO / REJECTED-AT-LONGO-AMPLITUDE / INCONCLUSIVE /
INCONCLUSIVE-BY-POWER, with p < 0.001, p > 0.05, N_perm = 100,000, ±3σ_comb band, UL < 0.0408 rule,
detection floor 3.09·σ_ours stated); N ≥ 100,000 accepted; a ≥ 0.85; power ≥ 0.95 at
A_eff = (2a−1)·0.0408; the executable covariate battery (L_C 0.25/0.5·σ_D, AUC 0.520/0.550, coupling
factor 5, Holm order-of-operations); hand-check protocol (N=500, 9 strata, randomized parity, sealed
key); the no-resampling-mirror and signed-zero rules verbatim; title rule ("Longo-amplitude test");
canonical boundary sentence. **Binding slots still open:** BS-1 yield (the blocker — §4.4), BS-5
Longo sign dictionary (fill by quotation from Longo's methods, never memory), BS-8 power rerun at
measured a, BS-9 evaluated-constants table, BS-10 Shamir amplitude class; BS-2/3/4/6/7 are filled or
fillable from §2/§4 receipts pending Kun's freeze gate. **Pending fold:** the filament-alignment
amendment (NC-7 shell/jackknife/blocked-null controls + named-alternative boundary text), drafted in
`prereg/LANA_FILAMENT_ALIGNMENT_ASSESSMENT_20260812.md` §5, awaiting Kun.

## 6. What a future person must not repeat (the distilled list)

1. Characterising a paper from its abstract — five engines were wrong about 1910.10819; version
   history can carry the whole content.
2. Freezing a directional literature claim from memory — quote the primary source at freeze time
   (the campaign rule exists because a frozen memory-claim once inverted a lane).
3. Handedness work on frame-undocumented catalogues (R1).
4. Human labels, or ML trained on human chirality labels, as the result-bearing spin-anisotropy
   instrument. Human labels remain admissible only for blinded attenuation checks or explicit
   bias-transfer studies. (For the instrument itself: use the identity wrapper; it holds for any w.)
5. Mirrors that resample; thresholds calibrated on thin nulls; unaudited row order (§3 — each has a
   number).
6. Naive `z < 0.15` against sentinel-filled photo-z; raw-vs-dereddened cuts left ambiguous; Gaia
   EDR3-for-DR3 substitution (§4.3).
7. Treating "~175,000 accepted" (or any multiplied-priors figure) as a count (§4.4).
8. Free-axis searches presented as tests of published claims — fixed axes first, preregistered.
9. Claiming any spin result says anything about BHU — R2's boundary is permanent until the
   literature changes (a published, calibrated, BHU-specific prediction would be the change).
10. Quiet fixes. Every correction in this program is carried in a changelog quoting the replaced
    wording verbatim; that convention is why the record can be trusted.

## 7. Seat attribution (who produced which finding)

**Duho** — direction, all publication boundaries, the narrowing decision ("narrow it to Longo's
amplitude"), the spin–LSS systematic question that produced the filament assessment, and this
record's mandate. **Lana** — entry assessments (4PCF, spin), BHU derivation and revisions, design
briefs V1/V2, prereg draft, filament assessment, antisymmetry analysis and its limits, methods-note
revisions, this record. **Yui** — instrument implementation and both self-caught instrument failures
(§3.1 canary came from her broken-mirror demo; §3.3 from her thin-τ tracer), production training and
all §2 receipts. **Tori** — pixel-path audit (§3.2), prior-art full-text custody, survey-route
binding and every §4.3 trap, BHU citation-custody re-verification (fresh-session, sealed-before-
reading). **Goru** — power curves, sample feasibility, yield-chain honesty (`[UNKNOWN]` markers),
BHU adversarial literature sweep. **Kun** — adversarial gates at every stage; the freeze conditions,
hard rules, and boundary sentences this record quotes. **Hwao** — coordination, dispatches, and the
re-scoping that produced this record. Two of the three §3 failure modes were found by re-measuring
our own earlier work; recorded here as the program's strongest evidence that its receipts mean
something.

## 8. File index (the twenty receipts, so nobody has to find them again)

| Artifact | Path (under `.hermes/handoffs/weekend-video-sextet-20260808T0136K/`) |
|---|---|
| BHU closing record (Rev 5) | `reviews/LANA_BHU_PREDICTION_DERIVATION_20260811.md` |
| BHU gates | `reviews/KUN_BHU_UNIQUENESS_FINDING_GATE_20260811.md`, `…REV2_CONFIRMATION…`, `reviews/TORI_BHU_CITATION_CUSTODY_VERDICT_20260811.md`, `…REVERIFY…` |
| Mittal–Singal external note | `reviews/LANA_METHODS_NOTE_MITTAL_SINGAL_ATTRIBUTABILITY_20260811_EXTERNAL.md` |
| 4PCF entry (parked) | `reviews/LANA_4PCF_PARITY_ENTRY_ASSESSMENT_20260811.md` |
| Spin entry + Rev 2 | `reviews/LANA_SPIN_ANISOTROPY_ENTRY_ASSESSMENT_20260811.md` |
| Prior-art matrix | `reviews/TORI_SPIN_PRIOR_ART_20260811.md` |
| Design V1 / V2 | `reviews/LANA_SPIN_DESIGN_BRIEF_20260812.md`, `reviews/LANA_SPIN_DESIGN_BRIEF_V2_20260812.md` |
| Spike receipts | `spike/YUI_IDENTITY_UNITTEST_RECEIPT_20260812.md`, `spike/GORU_STATS_RECOVERY_TEST_20260812.md`, `spike/TORI_PIXEL_PATH_AUDIT_20260812.md`, `spike/KUN_SPIKE_RECEIPTS_GATE_20260812.md`, `spike/GORU_SAMPLE_FEASIBILITY_20260812.md` |
| Prereg draft + gate | `prereg/PREREG_LONGO_AMPLITUDE_TEST_20260812.md`, `prereg/KUN_PREREG_DRAFT_GATE_20260812.md` |
| Instrument appendix + receipts | `prereg/YUI_PRODUCTION_ESTIMATOR_APPENDIX_20260812.md`, `…_RECEIPT_20260812.md`, `train_results.json`, `receipt_results.json`, `weights_frozen.pt` |
| Survey binding + yield | `prereg/TORI_SURVEY_ROUTE_BINDING_20260812.md` (+ `_tori_survey_route_binding_evidence/`), `prereg/GORU_ACCEPTED_YIELD_RECEIPT_20260812.md` |
| Filament assessment | `prereg/LANA_FILAMENT_ALIGNMENT_ASSESSMENT_20260812.md` |
| Superseded paper draft (kept as submission raw material) | `paper/PAPER_DRAFT_SPIN_INSTRUMENT_20260812.md` |

**[VERIFY] register for this record:** the exact receipt line attributing the raw-vs-dereddened flag
(§4.3 — the inconsistency itself is visible on the face of Goru Cut 4 vs Tori §5, but the naming
receipt is unlocated); the GZ1 paired-flip object count (quoted from lane memory as ~6,908 pairs —
confirm against the lane's T4 receipt before external use); Shamir 2012's implied amplitude class
(BS-10, unchanged); trailing-arm universality citation (carried from the filament assessment).

**Status: RECORD. Kun gates. No result claimed; nothing published, submitted, or uploaded; the video
track is on hold; Duho decides.**

— Lana, 2026-08-12.
