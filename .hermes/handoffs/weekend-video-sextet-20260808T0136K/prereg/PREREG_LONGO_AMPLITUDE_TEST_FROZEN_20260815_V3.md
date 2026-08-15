# PREREGISTRATION (v3 FREEZE CANDIDATE) — LONGO-AMPLITUDE TEST
## A preregistered test of Longo 2011's published dipole amplitude at Longo's published axis
## — amended to publish an aggregate-only output package with no derived catalogue
## — amended to the one-human hand-check protocol HC-1H
## — and amended to the single-band pixel input contract (128×128, r, float32)

**Lana (science / claim-boundary seat), 2026-08-15. Status: v3 FREEZE CANDIDATE — the 08-15
frozen text with the gated PC-1 input-contract amendment (§6) applied, and nothing else changed.
Supersession chain — the three predecessor hashes are embedded here; this candidate cannot carry
its own hash and is instead bound by the external Kun gate / freeze record, which pins this
file's SHA-256 at freeze:**
1. **08-12 draft** — superseded record, survives byte-for-byte:
   `PREREG_LONGO_AMPLITUDE_TEST_20260812.md`, SHA-256
   `ac43490054b159610385b8faac28dc4e3178161fadd97d66aa0418a1186b7590`.
2. **08-14 frozen** — superseded record, chmod 444, merged to a public repository, survives
   byte-for-byte: `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260814.md`, SHA-256
   `da2c6a21d994b9af7395347bf881075f855826ff859dd0415f15042f80ed3308`.
3. **08-15 frozen (v2)** — superseded record, chmod 444, merged to a public repository, survives
   byte-for-byte: `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815.md`, SHA-256
   `62dad44dd92acf2781d2c8cf25161f7f344e3fe6f7fec35b7e04308bd1539c12`.
4. **This candidate (v3)** — the working text; becomes the preregistration only when sha-pinned
   after Kun's freeze-gate PASS. The applied amendment is
   `LANA_PC1_INPUT_AMENDMENT_20260815.md` at Revision 3 (SHA-256
   `519ab5ba33c5e9d670b5654fb41f6941293c5d969c5515fb0284ebe8d52d70fb`; all [VERIFY] markers
   filled from primary sources or deleted per Kun's blocker; GZ DECaLS rationale repaired to
   Kun's exact wording per `KUN_V3_FREEZE_GATE_20260815.md`), direction approved by Duho, gated
   by Kun PASS_PC1_AMENDMENT_FOR_V3_DRAFTING / HOLD EXECUTION
   (`KUN_STRATEGY_GATE_20260815.md`).

**Nothing is frozen, published, accepted, committed, or pushed by writing this candidate; Kun
gates it; the freeze is a separate act; Duho owns acceptance.**

**Why this candidate exists.** Old BS-1 **FAILED**: its validity range required *"licence permits
derived-catalogue publication"*, and no primary source establishes that permission (Tori's BS-1
licence receipt; Kun's final gate). Duho decided to **redesign the output rather than seek
permission**. Kun's redesign re-gate: *"PASS AS A REDESIGN DIRECTION; HOLD FREEZE UNTIL THE
AMENDMENT IS REWRITTEN AND RE-GATED"* — this document is that amendment, assembled into the full
design.

**The statement this document must never be misread against (Kun's unsafe framing, quoted so it
cannot creep back): it is NOT the case that "BS-1 now passes unchanged." Old BS-1 remains FAILED
as written. The licence problem was not solved; the published output was redesigned so that the
permission is no longer required, and the slot is REWRITTEN accordingly (§B). Anything that reads
as a retrospective licence cure is wrong.**

**K-8 timing statement, explicit (re-affirmed for the HC-1H amendment and again for the PC-1
input-contract amendment, 2026-08-15):** no real-sky statistic has been computed anywhere in
this program — no chirality label, no sky estimand, no unblinding of any kind, and no science
cutout has been fetched. The output-package amendment, the HC-1H hand-check amendment, and the
PC-1 input-contract amendment are all therefore made at the only safe time, before the run.
None is, or must ever be described as, a post-hoc change. (Altering the §F-10 output boundary,
the §5 hand-check protocol, or the §6 input contract *after* any real-sky statistic falls under
K-8 and voids the run.)

**Changes in this v3 candidate relative to the 08-15 frozen (v2) text, complete list:** (1) the
PC-1 input-contract amendment applied to §6 — PC-1 amended, the route request superseded to
`bands=r` / `size=128`, and the input contract IC-1…IC-7 incorporated as frozen text; (2) four
binding prerequisites to sky access added to §6 (successor route binding; input-function receipt
+ R1–R5 rerun; conditional PC-3/PC-4 re-gate; `nm_acquire_cutouts.py` barred from execution);
(3) header/status, supersession chain, provenance chain, and this changelog updated accordingly;
(4) the v2 changelog below is carried as historical record, relabelled from "this candidate" to
"the v2 text". Nothing else differs; BS-1's licence limb remains FAILED as written; F-10, BS-11,
the cumulative-release policy, HC-1H and HC-7, the STOP rule, K-1…K-14, the canonical boundary
sentence, and every §B receipt reference and hash carry unchanged. **This candidate fixes the
input contract, not the delivery route** — the acquisition channel is still unresolved and
awaits Duho's operator-query decision; approval of this text is not approval of any delivery
mechanism.

**Changes in the v2 text relative to the 08-14 frozen text (carried record):** (1) amendment
A1–A5 applied to §5 (HC-1…HC-6 → HC-1H, HC-7 added including trigger (v)); (2) header/status,
supersession chain, provenance chain, and this changelog updated accordingly; (3) two conforming
row-count references updated to the amended protocol, prohibitions unchanged in force — F-10.d's
*"including 'small' tables like the 500 hand-check rows"* and P7's *"never the 500 rows"* now
name the 850-label HC-1H per-label table. Nothing else differs; BS-1's licence limb remains
FAILED as written, F-10/BS-11/cumulative-release policy, the STOP rule, K-1…K-14, the canonical
boundary sentence, and every §B receipt reference and hash carry unchanged.

**Title rule (Kun, binding):** every derived artifact of this study titles itself a
**"Longo-amplitude test"** — never a "spin anisotropy test."

**Canonical boundary sentence** (byte-identical wherever it appears):
> **"A null here does not establish that the sky is isotropic; it rejects only Longo's published amplitude at Longo's published axis if the preregistered rejection rule is met."**

**Headline boundary (carried with the title):**
> This tests Longo's published `A ≈ 0.0408` amplitude at Longo's published axis. It does not test
> `A ≈ 0.02`, Shamir, BHU, or whether the sky is isotropic.

**Provenance chain (extending the 08-12 note):** … 08-12 draft → Kun prereg-draft gate →
slot-filling receipts (§B) → Kun final gate (**BS-1 FAIL on licence; nine slots PASS or PASS WITH
REPAIR/NOTICE**) → Duho: redesign the output → Lana output redesign → Tori licence clearance
(CONDITIONALLY VIABLE, six corrections) → Kun redesign re-gate (PASS AS DIRECTION; HOLD FREEZE) →
assembled candidate (`70d68620…` — superseded by this revision) → linter built + gated
(`YUI_RELEASE_LINTER_20260814.md`) → Kun amendment gate (PASS DIRECTION AND LINTER; HOLD FOR THREE
TEXT REPAIRS; `KUN_AMENDMENT_GATE_20260814.md`) → repaired candidate (three repairs: BS-11
filled, cumulative-release policy bound at F-10.f, custody + ACCEPT semantics at F-10.f/i) → Kun
final exact-hash confirmation → Duho acceptance → **08-14 FREEZE** (`da2c6a21…`, merged) →
Duho's one-human constraint → HC-1H design (`LANA_ONE_HUMAN_ATTENUATION_20260814.md`) → Kun
HC-1H gate (PASS WITH FIVE REQUIRED REPAIRS) → repairs → Kun re-gate (HOLD FOR TWO STATISTICAL
REPAIRS: shared-ε̂ variance summed-then-squared; pilot carry-forward selection bias) → repairs →
Kun final gate (HOLD FOR HC-7 trigger (v), synthetic/repeat identity exposure) → repair →
Kun PASS_HC1H_CLOSE_ON_EXACT_HASH (`b2590e42…`) → Duho acceptance of HC-1H, 01:08 KST
2026-08-15 → v2 candidate (amendment A1–A5 applied to §5) → Kun metadata gate
(HOLD_FREEZE_FOR_METADATA_REPAIR; two repairs) → **08-15 FREEZE (v2)** (`62dad44d…`, merged) →
PC-1/estimator input mismatch found (route fetches 12× the consumed pixels) → Kun strategy gate
(PASS_WITH_REPAIRS_FOR_STRATEGY_ONLY; HOLD EXECUTION; `KUN_STRATEGY_GATE_20260815.md`) → Duho
approves the amendment direction (128×128, one band, float32) → Lana PC-1 input amendment (band
decision: r; parity argument) → Kun PASS_PC1_AMENDMENT_FOR_V3_DRAFTING (parity argument held;
[VERIFY] fills a blocker) → fills from primary sources / one claim corrected (amendment Rev 2,
`16a4a601…`) → Kun freeze gate HOLD_V3_FREEZE_FOR_GZ_DECALS_RATIONALE_REPAIR (the "Every
parent" sentence over-claimed the Walmsley source) → GZ DECaLS rationale repaired to Kun's
exact wording (amendment Rev 3, `519ab5ba…`) → **this v3 candidate (PC-1 amendment applied to
§6)** → Kun freeze re-gate → Duho.

**STOP rule (unchanged, absolute):** any sky run, result, publication, or accepted status remains
unauthorised; the moment the next step would touch real galaxies, this lane STOPS and reports that
as the successful outcome.

---

## 1. Claim under test (frozen — carried unchanged)

**Longo 2011**, *Phys. Lett. B* 699, 224–229 (DOI 10.1016/j.physletb.2011.04.008): dipole asymmetry
in spiral-galaxy handedness of **|A_L| = 0.0408, σ_pub = 0.011**, at the axis
**n̂_L : (l, b) = (52°, 68.5°)** (equivalently (α, δ) = (217°, 32°) as published), from 15,158 SDSS
spirals at z < 0.085. The test asks exactly one question: **does an instrument that cannot produce
the sign reproduce or reject this amplitude at this axis?**

## 2. Frozen statistical protocol (F-1…F-9 carried unchanged; F-10 added)

- **F-1 Estimand.** D̂(n̂_L) = (1/N)·Σᵢ sign(χᵢ)·cos θᵢ over accepted galaxies; Â = 3·D̂
  (unbiasedness receipt: spike, injected 0.0400 → recovered 0.0402); Â_c = Â/(2a−1), a from §5.
- **F-2 Order of reporting.** Monopole M̂ first, always; then D̂(n̂_L); then secondaries. No
  free-axis quantity is computed before the fixed-axis quantities are locked to disk.
- **F-3 Null.** Label-permutation: **N_perm = 100,000** over fixed positions and footprint.
  One-sided p at Longo's sign.
- **F-4 σ definitions.** σ_D ≡ √(1/(3·N_accepted)); σ_ours ≡ 3·σ_D/(2a−1);
  σ_comb ≡ √(σ_pub² + σ_ours²) with σ_pub = 0.011.
- **F-5 Sign.** REPRODUCED requires **Longo's sign at Longo's oriented axis** — convention filled
  at BS-5 by quotation; in our East-of-North winding convention the target is **Â(n̂_L) = +0.0408**,
  with the **mandatory synthetic absolute-sign anchor** run before any real image (BS-5 receipt).
- **F-6 Decision regions (exhaustive, mutually exclusive):**
  - **REPRODUCED-LONGO:** permutation p < **0.001** AND sign per F-5 AND |Â_c − 0.0408| ≤ 3·σ_comb.
  - **REJECTED-AT-LONGO-AMPLITUDE:** permutation p > **0.05** AND (|Â_c| + 3·σ_ours) < **0.0408**.
  - **INCONCLUSIVE:** any other numeric outcome, or any triggered INCONCLUSIVE rule in §4/§6.
  - **INCONCLUSIVE-BY-POWER:** declared before unblinding if the §5 power gate fails; no run.
- **F-7 Effective detection floor:** one-sided floor **3.09·σ_ours** on Â_c; at frozen minima
  (N = 100,000, a = 0.85) floor = **0.0242**; at a = 0.90: **0.0212**. No Â_c below the evaluated
  floor can be called REPRODUCED regardless of the band; the evaluated floor is printed in the
  results table. (Evaluated at the bound inputs in the BS-9 receipt: floor **0.0148**; at the
  a-floor: **0.0212** — see §B BS-9.)
- **F-8 Secondaries (non-decision, reported after primary lock):** (i) D̂ at Shamir's axis
  (RA = 132°, Dec = 32°), interval only — **no decision language about Shamir in any output**
  (K-14; BS-10 pins the amplitude class as informational); (ii) one free-axis scan on a HEALPix
  **Nside = 16** grid (3,072 directions), permutation-calibrated global-maximum statistic; cannot
  modify or rescue the primary outcome.
- **F-9 One run.** Any parameter change after any real-sky statistic voids the run (K-8);
  re-entry only via a new preregistration.

- **F-10 Output boundary (NEW — licence-scoped, frozen before any real-sky statistic).**
  - **(a) Published artifacts are exactly the frozen package** P1–P10 (paper) and S1–S5
    (supplement) of §8. Nothing outside the package is released; **any unlisted artifact is
    forbidden by default** (closed-world, as in the video lane's text contract).
  - **(b) Controlling release rule — Tori's six package-wide conditions
    (`TORI_OUTPUT_LICENCE_CLEARANCE_20260814.md` §3), mandatory and controlling, applied to the
    COMPLETE release cumulatively, not per file:**
    1. **Rowless:** no object key, row, coordinate, URL, source field, per-object derived
       quantity, or reversible row hash.
    2. **Fixed and finite:** schema and cells frozen before real-sky statistics; no post-result
       boundaries, dynamic query interface, or unlimited slicing.
    3. **Study-result only:** cells contain this study's estimands, instrument summaries,
       uncertainties, or controls — not re-tabulated survey attributes.
    4. **Non-reconstructable cumulatively:** no combination, overlap, differencing, version
       sequence, or auxiliary release can recover membership or object-level attributes.
    5. **Non-substitutive cumulatively:** the package cannot function as the source catalogue, a
       derived catalogue, or a catalogue-scale lookup/re-analysis product.
    6. **Separate image compliance:** any source image pixels follow their actual layer's licence
       and credit route; image compliance cannot cure a catalogue-like table.
  - **(c) Numeric guardrails — additional conservative engineering limits, applied AFTER (b), and
    explicitly NOT legal safe harbors or licence thresholds:** every ordinary aggregate cell
    k ≥ 50 (sub-threshold masked under the frozen rule); no ordinary table/map above 5,000
    released cells; cells frozen and object-independent; no per-object keys or coordinates; no
    aggregated re-tabulations of survey attributes. **If (b) and (c) ever conflict, (b) wins.**
  - **(d) Cumulative-release prohibitions (Tori correction 2):** no overlapping or differenced
    table families, no subsequent finer-binned versions, no public slice/query APIs, no
    brick-by-brick or fine-pixel exports, no per-object anything — including "small" tables like
    the per-label hand-check table (850 labels under HC-1H; the 08-14 text said "the 500
    hand-check rows" — conformed to the amended protocol, prohibition unchanged in force).
  - **(e) Commitments:** one SHA-256 for the canonical private per-object result file (fixed
    schema, sorted by the survey row key) and one per each of the **67** fixed partition slices,
    published. The private files are retained unpublished. **Claim wording is frozen (Kun):**
    *"Commitment hashes cryptographically bind the private result file and allow byte-equality
    checking after an independent rebuild."* **Banned wordings:** that hashes prove the hidden
    rows are scientifically correct, or are "strictly stronger than table inspection."
  - **(f) Release manifest + linter (machine-enforced; Binding Slot BS-11, filled):** every public
    release passes the pinned automated check over the **complete package** that rejects row-like
    schemas, identifiers, coordinates, URLs, per-object quantities, unapproved grids, cell counts
    above the guardrail, and cumulative overlap/differencing hazards. Hand judgment does not
    substitute. **Cumulative-release policy (Kun's required sentence, binding on all future
    behaviour):** *"Every future public release, correction, supplement, figure-data package, video
    data appendix, or replacement package must be linted against the cumulative release-history
    registry for this study, including all prior and concurrent public artifacts; an
    isolated-package ACCEPT is insufficient for publication."* The **cumulative release registry**
    lives at `prereg/release_linter/RELEASE_REGISTRY.json` in this study's custody archive and
    travels with the study record; every public artifact is entered with its hash at release time.
    **A missing, stale, or unconsulted registry is a release HOLD.**
    **ACCEPT semantics (a claim to readers, stated here so it cannot be overclaimed):** *"Linter
    ACCEPT means only that no implemented deterministic release rule fired on the exact hash-pinned
    cumulative package supplied to it; it is not a licence determination, a proof against every
    reconstruction attack, a freeze, publication approval, or Duho acceptance."*
  - **(i) Named human custody (the responsibilities the machine cannot discharge):**
    **Release steward — Tori (custody seat):** verifies manifest truth against the actual files and
    release intent before the linter runs — the linter pins declarations; it does not verify them.
    **Freeze steward — Tori (custody seat), independently confirmed by Kun at each release gate:**
    verifies and records that schema/cell freeze attestations were true before any real-sky
    statistic — the linter can hash-pin an attestation but cannot observe whether it was true when
    made. **Science/claim seat — Lana:** verifies that accepted files make no scientific or legal
    claim beyond the manifest and linter scope. Seat reassignments, if staffing changes, are
    recorded in the release registry. Duho owns acceptance above all of these.
  - **(g) Data-availability statement (frozen, verbatim in the paper):** *"No per-object
    NebulaMind derived catalogue is public or available on request. Reproducibility is by
    rebuilding from cited public products, frozen code, aggregate outputs, and commitment
    hashes."*
  - **(h)** No per-object quantity derived from survey pixels or rows is distributed in any
    artifact of this study. Survey acknowledgment and citation obligations (Legacy scientific
    acknowledgment; photo-z citation of Zhou et al. 2023; Gaia DR3 credit) are carried in full.

## 3. Instrument (frozen; slot receipts at §B)

- **I-1 Primary:** equivariant classifier, CE-ResNet pattern, **trained exclusively on synthetic
  spirals — no human chirality label anywhere in training.** Production spec = BS-3 (Appendix A,
  filled): frozen weights, τ = 4.4006456017494235, generator + seed schedule, receipts. **Zero-case
  clarity (Kun repair):** the R1/R2 identity witness is the **1,000-probe nonzero production
  grid** (bit-exact 1,000/1,000); the **R3 signed-zero probe is a separate edge-case receipt** —
  the two are distinct tests and must never be conflated in any receipt or paper text.
- **I-2 Secondary:** deterministic Ganalyzer-class geometric estimator, antisymmetrization-wrapped;
  spec = BS-4 (filled). Disagreement rates on jointly-accepted objects are published **as rates
  and per-partition aggregates under F-10; the per-object disagreement list is hash-committed,
  never distributed.** **Load-bearing warning (Kun, verbatim, required here and at the BS-4
  slot):** *"The secondary instrument is a sparse, training-free cross-check with near-total
  abstention; it is not a high-yield substitute for the primary and cannot rescue primary failure
  or supply an independent powered estimate."* (Measured: production held-out acceptance
  16/12,000 = 0.133% retention, 99.867% abstention; fresh 1,000-probe acceptance 1/1,000.)
- **I-3 Hard rules (carried verbatim):** the **no-resampling mirror** rule (pure pixel-index
  reversal; mirror(mirror(x)) byte-exact on the exact dtype; interpolating-mirror violation
  0.058–0.944 is the standing demonstration) and the **signed-zero rule** (value comparisons only;
  the unit test that fails on any sign-bit branch).
- **I-4 Identity receipts required before any real image:** 1,000/1,000 bit-exact
  χ(mirror(x)) = −χ(x) for BOTH instruments on the production rasters, plus paired original/mirror
  outputs, flip-balance, confidence/abstention deltas — **published in full for synthetic
  receipts; for real-sky objects, published as aggregate counts and deltas under F-10, with the
  per-object mirror file hash-committed (F-10.e), never distributed.**
- **I-5 Sample selection:** survey photometric cuts only (BS-6, filled); **b/a > 0.4** (frozen);
  spirality gate via the mirror-invariant score s(x); **no human morphology flags, no Galaxy Zoo
  membership, anywhere in the chain.** **BS-6 wording rule (Kun):** the `type <> 'PSF'` predicate
  is an **automated Tractor source-type / point-source exclusion** — it is never to be described
  as visual morphology, Galaxy Zoo membership, spiral selection, or a chirality label. No
  surface-brightness cut exists in the frozen design ("none" is the correct fill, not a late
  invention).

## 4. Covariate battery (carried unchanged; products = BS-2, filled)

CB-1…CB-8 carry verbatim from the 08-12 draft (10 covariates; Nside = 128 maps, pixel-lookup, no
interpolation; Nside = 32 sensitivity/abstention maps masked < 50; z-scoring and 5% missing-data
rule; Layer A stratified permutation with L_C thresholds 0.25/0.5·σ_D and deterministic
coarsening; Layer B logistic + GBT with AUC triggers 0.520/0.550 and frozen hyperparameters/seeds;
CB-6 order of operations; CB-7 coupling bound with |D̂| > 5·B trigger; CB-8 mirror-pair
accounting). **BS-2 outcome (filled): 9 of 10 core covariates survive by the absolute-count
lower-bound coverage rule; arm-contrast is dropped rather than invented — within the ≥ 8/10
validity range.**

## 5. Hand-check attenuation protocol HC-1H (amended 2026-08-15; one-human protocol; HC-6 wording per Kun's BS-8 ruling)

*(This section is the 08-14 frozen §5 with amendment A1–A5 of
`LANA_ONE_HUMAN_ATTENUATION_20260814.md` (`b2590e42…`) applied — accepted by Duho, closed by Kun
on exact hash. The 08-14 frozen wording it replaces survives byte-for-byte in
`PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260814.md` (`da2c6a21…`). K-8 is untripped: no real-sky
statistic exists, so this amendment is pre-run.)*

**[A1]** HC-1…HC-6 are replaced by the one-human protocol HC-1H
(`LANA_ONE_HUMAN_ATTENUATION_20260814.md` §2, incorporated as frozen text): one human checker
(Duho — the project's single permitted human), 850 blinded labels (500 real, 200 blind synthetic
ground-truth injections, 150 mirrored re-presentations), 9 strata = machine-committee state ×
|χ| tertile with Neyman allocation (floor 30 real/stratum), machine committee as
stratifier/allocator/diagnostic only and never inside `a`.
- **HC-3 (amended) [A2]:** Checker: one human (Duho). No second checker exists or is claimed.
  Individual random error is measured, not adjudicated: by the mirrored re-presentation non-flip
  rate (ε̂_rr) and by blind synthetic ground-truth injections (ε̂_syn), both under the sealed key.
  Instructions frozen with this document; sessions ≤ 50 images; instrument signs never visible to
  the checker.
- **HC-4 (amended) [A3]:** per-stratum raw agreement â_s is corrected for measured reference
  noise by the GLOBAL synthetic-injection error rate ε̂, a_s = (â_s − ε̂)/(1 − 2·ε̂)
  (per-stratum ε̂_syn,s are diagnostics only, never corrections; ε̂_rr is the consistency
  cross-check); a = Σ w_s·a_s with population weights. **a is the HC-1H one-human,
  synthetic-error-corrected attenuation estimate; it does not claim equivalence to a multi-human
  truth-reference measurement and carries the synthetic-realism caveat wherever printed.** σ_a is
  computed by the frozen formula
  σ_a² = Σ_s w_s²·Var(â_s)/(1−2ε̂)² + [Σ_s w_s·(2â_s−1)/(1−2ε̂)²]²·Var(ε̂) (+ covariance ≥ 0)
  — the shared ε̂'s derivative summed across strata before squaring, never squared per stratum —
  at realized counts with conservative binomial variances — no expected width is frozen;
  propagated as σ(2a−1) = 2σ_a into σ_ours and both F-6 decision regions (bands evaluated at the
  corrected a, printed with propagated widths). **Hand-check publications are per-stratum
  aggregates only (F-10); the per-object HC table, the sealed key, and the synthetic-injection
  manifest are retained unpublished and hash-committed.**
- **HC-5 (amended) [A4]:** Validity floors (frozen, matched to the one-human reference): (1a)
  a_LB = a − 1.645·σ_a ≥ a_gate(N), the power-gate break-even at the actual bound N by the
  corrected linear rule (2a−1)·0.0408/3 ≥ 4.9354·σ_D — a_gate = 0.7905 at N = 130,076, recomputed
  at freeze; (1b) the instrument-quality floor a_LB ≥ 0.85, retained on its own justification
  (correction-factor amplification ≤ 1.43; one-human correlated-error headroom) and explicitly
  not the HC-6 break-even — (1b) binds; (2) no stratum with a_s < 0.70; (3) global ε̂ ≤ 0.05;
  (4) ε̂_rr compatible with ε̂ within 2σ, and stratum diagnostics without unresolved > 2σ
  incompatibility. Any failure → INCONCLUSIVE-BY-POWER, run does not start. **HC-7 (hard
  protocol-integrity triggers):** missing stratum population counts, broken random-within-stratum
  sampling, an unsealed or compromised key, machine/instrument signs visible to the checker, or
  synthetic/repeat identity exposure — if the checker can identify which items are synthetic,
  repeated, or mirrored repeats before key opening, the affected batch is void unless the
  predeclared in-session flag-discard-replace rule applies
  (`LANA_ONE_HUMAN_ATTENUATION_20260814.md` §2, incorporated) — → hard INCONCLUSIVE; the affected
  measurement is void.
- **HC-6 Power gate (amended wording per Kun's BS-8 ruling; final sentence amended [A5]):** the
  pinned harness
  (`spike/sim_power.py`) has hardcoded inputs and accepts no parameters; **the frozen rule is
  therefore: the pinned harness is inspected and its analytical power logic (the
  normal-approximation p-value computation embodied in `compute_power_curve()`) is evaluated
  directly at A_eff = (2a−1)·0.0408 and the bound N — the freeze text must not say the harness was
  literally rerun at custom inputs.** Requirement: power ≥ 0.95 at p < 0.001. Freeze-time receipt
  (BS-8): power ≈ 1.0000 at N = 130,076, a = 0.999711, A_eff = 0.04077642. **This gate is
  re-evaluated by the same analytical method at the noise-corrected, one-sided-95% lower-bound
  hand-checked a (HC-4/HC-5.1) before unblinding**; failure →
  INCONCLUSIVE-BY-POWER, no run. Minimum accepted sample: **N_accepted ≥ 100,000**.

*(The optional 150-label pilot (§2b of the incorporated HC-1H text) is available at Duho's
choice; its only outcomes are PASS-TO-FULL-HC1H or INCONCLUSIVE; its 40 synthetics never enter
the final ε̂.)*

## 6. Pixel-path custody and negative controls (PC-1 amended 2026-08-15; the rest carried)

*(This section is the 08-15 frozen §6 with `LANA_PC1_INPUT_AMENDMENT_20260815.md` Rev 3
(`519ab5ba…`) applied — direction approved by Duho, gated by Kun for v3 drafting. The defect
repaired: the route binding froze `size=256`, `bands=grz` while the frozen estimator consumes a
single-channel 128×128 tensor — 12× more delivered pixels than consumed, with the reduction step
frozen nowhere. Kun ruled PC-1 the wrong document; the science determination (amendment §2,
incorporated) is that one band suffices — chirality is parity-odd, pixelwise color is
parity-even, so color carries no sign information and its only effect is sensitivity, which is
measured by HC-1H and gated by HC-5/HC-6 — and the band is r, on pinned extinction arithmetic
(A/E(B−V): g 3.214, r 2.165, z 1.211; Legacy Surveys DR10 documentation), sourced arm-contrast
ordering (Yu, Ho, Barth & Li 2018, DOI 10.3847/1538-4357/aacb25: arm strength "stronger in bluer
bands than redder bands"), and the study parent's r-band guarantee: for the study's selected
parent, r is directly constrained by the frozen `flux_r > 0` and `dered_mag_r < 17.7` cuts;
Walmsley et al. 2022 §2.2 separately supports that the GZ DECaLS NSA parent is primarily
r-limited (m_r = 17.77), while noting exceptions — the guarantee rests on our frozen study cuts,
not on a claim that every GZ DECaLS source is r-limited. Color-driven sky-correlated sensitivity
remains routed to the R1–R5 rerun, HC-1H
attenuation, the HC-5/HC-6 floors, and the covariate battery — parity alone is not claimed to
prove it safe. K-8 is untripped: no real-sky statistic exists; this amendment is pre-run.)*

**PC-1 (amended 2026-08-15):** Single survey, single cutout route, exact versions (BS-1);
checksums and query logs at the Mittal–Singal custody standard. The pixel input contract is
frozen by `LANA_PC1_INPUT_AMENDMENT_20260815.md` §3 A2–A3 (incorporated as frozen text): single
band r, 128×128, float32, with the delivered raster consumed whole — no reduction, resampling,
or plane selection step may exist between delivery and tensor. The route request supersession:
`bands=r` (exactly and only r; g, z, i and WISE are not measurement channels) and `size=128` (a
single square 128×128 analysis raster, matching the frozen estimator input exactly — delivered
pixels = consumed pixels). All other route-binding lines carry unchanged: `layer=ls-dr10-south`,
`pixscale=0.262`, FITS only, no post-delivery rotate/reproject/interpolate/resize/WCS transform,
delivered planes in FITS-native row order as the final analysis raster, mirror as byte-exact
pixel-index reversal on that raster only. The input contract IC-1…IC-7 (band/plane FAIL_CLOSED
rule; nanomaggy units; no added background handling; invalid-pixel rule with frozen cap;
fixed monotone scaling map with **no data-dependent normalization of any kind**; float32
little-endian C-order (1, 128, 128); mirror as exact even-size index permutation between columns
63 and 64, applied after conversion and nowhere else in the χ path) is incorporated as frozen
text; its two open constants (invalid-fraction cap, scaling-map constants) are BINDING SLOTS
filled on synthetics only.

**Binding prerequisites to sky access (not notes — sky access is barred until each holds):**
1. **Tori's successor route binding** for the exact single-band FITS schema, including HDU/plane
   identity (IC-1's slot), issued and gated before any science cutout is requested.
2. **Yui's hash-pinned input-function receipt** — invalid-pixel cap, monotone scaling map, code
   hash, tensor layout — **and the full R1–R5 identity / retention / calibration rerun through
   that exact input function** (byte-identical code path to production). The old R1–R5 receipts
   were produced on the superseded input path and are not evidence about the instrument as now
   consumed.
3. **PC-3 parity and PC-4 fail-closed re-gated on the local path** if cutting ever moves off the
   service — WCS custody would transfer onto our code and must be re-verified, not assumed.
4. **`nm_acquire_cutouts.py` must not execute.** It hardcodes `grz`, `256` and `[3, 256, 256]`:
   the gated acquisition pipeline is built to the superseded contract and requires a separately
   gated replacement before any fetch.

PC-2…PC-5 and NC-1…NC-6 otherwise carry verbatim from the 08-12 draft, including: delivered
pixels + WCS as measurement input; per-object parity logging; **distortion branch declared at
BS-7 (filled): FAIL_CLOSED on SIP/PV/CPDIS/DET2IM — the local-Jacobian branch is not selected**;
injection battery (≥ 1,000 sources, 100% signed recovery, silent-flip and scrambled-WCS controls
must be detected); C1 mirror-run count-swap and D̂-negation (aggregate by construction); C2–C6
as frozen. The secondary-instrument warning of §3 I-2 applies to any C-battery use of the
secondary.

## 7. Outcome handling (amended)

- All outcomes — REPRODUCED-LONGO, REJECTED-AT-LONGO-AMPLITUDE, INCONCLUSIVE,
  INCONCLUSIVE-BY-POWER — are published **with the full receipt set as bounded by F-10 (aggregate
  artifacts P1–P10 and S1–S5; per-object files hash-committed, never distributed).** INCONCLUSIVE
  triggers are exact; the word cannot be negotiated after the fact.
- A REPRODUCED-LONGO outcome triggers an adversarial systematics re-audit inside the lane before
  any claim, video, or upload exists. It would NOT identify BHU (Kun, verbatim: *"Any positive
  spin result … would be a spin-anisotropy/statistical-isotropy result only"*).
- Every derived artifact carries the title rule, the canonical boundary sentence (byte-identical),
  the headline boundary, and — where it reports data availability — the F-10.g statement verbatim.

## 8. The frozen public output package (NEW)

**Paper (P1–P10):** P1 M̂ with interval (first). P2 D̂(n̂_L), permutation p, Â, Â_c, a with
interval. P3 the F-6 decision verbatim with all thresholds; the 3σ UL if null-consistent. P4 the
evaluated-constants table (BS-9 form) at final N and hand-checked a. P5 secondaries per F-8
(Shamir interval only; scan global-maximum summary). P6 the selection funnel (aggregate counts per
cut, abstention, mirror-exclusions, final N). P7 per-stratum attenuation aggregates (9 strata,
Wilson intervals; never the per-label rows — 850 under HC-1H). P8 covariate battery outputs (L_C values, AUC, LR, Holm
flags; CB-7 bound B and components). P9 negative controls (C1 totals, C3 values, C6 splits with
χ², NC-7 shells, blocked-jackknife σ). P10 synthetic instrument receipts (identity, retention and
sign-accuracy tables, τ, weight hashes, injection audit, power).
**Supplement (S1–S5):** S1 masked Nside = 32 maps (accepted count, abstention fraction, mean sign,
sensitivity; k ≥ 50 mask). S2 the one fixed 67-row partition-aggregate table. S3 the frozen
pipeline (selection spec, code, weights, seeds, environment, query templates, consumed-product
hashes; no credentials, no cached source responses, no identifiers/coordinates/rows). S4 the
F-10.e commitments. S5 this preregistration, its amendments, and gate history.
**Retained privately, unpublished, hash-committed:** the per-object results table, per-object HC
labels and key, all fetched cutouts.

**What is lost — the corrected table (a claim to readers; must not overstate):**

| Check the catalogue enabled | Lost? | Substitute |
|---|---|---|
| Byte-level verification of our result | No | commitments + independent rebuild (byte equality after rebuild — F-10.e wording) |
| **Spot-checking NebulaMind's individual hidden labels against images** | **Yes, except through rebuild** | *"A reader may run the public classifier on arbitrary cutouts to test code behavior. Exact verification of NebulaMind's private label for a given object requires rebuilding the canonical slice or full file and matching the published commitment hash."* (Kun's corrected row, verbatim) |
| Auditing our selection (dedup, cut correctness) | No | selection is deterministic from public inputs + published predicates; rebuild reproduces it |
| Bulk re-analysis of our signs at ≳ 3° scales | Partially | S1 maps; sub-degree analyses do not survive |
| Object-level / sub-degree reuse of our labels (cross-matching, environmental studies, per-object ML) | **Yes — lost** | none without rebuild |
| Arbitrary re-cuts / re-weighting | Partially | S2 + covariate-decile aggregates support coarse re-weighting; arbitrary re-cuts require rebuild |
| Object-level audit of the hand-check | **Yes — lost** (also by F-10.b rule 1) | per-stratum aggregates + published protocol; sealed-key design is the integrity mechanism |
| Cheap inspection of our exact per-object output | **Yes — lost** | rebuild + commitment match |

**Reproducibility claims, frozen at Kun's safe strength:** the package proves *bindingness*
(F-10.e wording) and enables deterministic rebuild from public products; **correctness rests on
the preregistration, source products, code, tests, aggregate receipts, and independent rebuild —
not on the hashes.** Full reproduction costs the reader the public-source retrieval and compute
stated openly in the paper (order 10² GB of polite-rate fetching plus classification); this is
materially more expensive than downloading a catalogue, and the paper says so.

## B. BINDING SLOT REGISTER — updated, every receipt named and pinned

| ID | Status | Receipt(s) — filename · SHA-256 |
|---|---|---|
| **BS-1 (REWRITTEN)** | Old validity text *"licence permits derived-catalogue publication"* — **FAILED, stays failed as written** (`TORI_BS1_LICENCE_20260814.md` · `34aad1f1…d375d2684e`; `KUN_FINAL_GATE_20260814.md` · `0c4a5ce6…a40bf0d9a`). **Replacement validity text (Kun's, verbatim in substance):** *"licence/terms permit the frozen aggregate-only output package: no per-object derived catalogue, no object identifiers, no coordinates, no source rows, no per-object derived quantities, no request-only private catalogue, and no public artifact family that cumulatively reconstructs membership or functions as a catalogue substitute; Legacy acknowledgement/citation obligations are carried in full; any Legacy image pixels, if ever used, follow the separate image-credit route."* Supporting: route binding `TORI_SURVEY_ROUTE_BINDING_20260812.md` · `3f41b6d9…9163d3a87`; closure packet `TORI_BS1_CLOSURE_PACKET.md` · `50bf06b0…301b8f5` (N-bound 130,076); **footprint variance PASS** `TORI_FOOTPRINT_VARIANCE_RECEIPT.md` · `9f6955e3…082326c0` (count-weighted var(cos θ) = 0.445201 ≥ 0.15 with ≥ 2× the 0.0124 bracket); yield `GORU_ACCEPTED_YIELD_RECEIPT_20260812.md` · `bbe3bbaa…3ff3dac9172`; redesign `LANA_OUTPUT_REDESIGN_20260814.md` · `6ca36544…3eb0f6f16`; clearance `TORI_OUTPUT_LICENCE_CLEARANCE_20260814.md` · `47702d37…e911ae4c5c5`; direction pass `KUN_REDESIGN_REGATE_20260814.md` · `83315785…aa14d0a7`. **Effective only upon Kun's PASS of this candidate.** |
| BS-2 | PASS | `TORI_BS2_COVARIATES_20260814.md` · `9f869c5b…b7585a57` — 9/10 survive; arm-contrast dropped, not invented |
| BS-3 | PASS | `YUI_PRODUCTION_ESTIMATOR_APPENDIX_20260812.md` · `331a941a…334f9fc3`; **authoritative retention** `YUI_INCLINATION_RETENTION_REMEASURE_20260812.md` · `012cb5fd…59c48709e1073` (85.72% LB, full Cut-6 range); identity witness `YUI_BS3_IDENTITY_1000_20260814.md` · `df73396b…2932d87dae595`; R4/R5 `YUI_BS3_R4_R5_RECEIPTS.md` · `fd2fdc07…dbfbdebe9c20b44`; inventory `GORU_BS3_INVENTORY.md` · `20af48e0…375d87dd205`. Superseded (recorded, not used): `YUI_PRODUCTION_ESTIMATOR_RECEIPT_20260812.md` · `b4e2f5b5…3609e18a`. R1/R2 grid ≠ R3 zero-probe (frozen distinction, §3 I-1) |
| BS-4 | PASS WITH REQUIRED NOTICE | `YUI_BS4_SECONDARY_INSTRUMENT_20260814.md` · `cefbfb04…953d82720` — the §3 I-2 warning is part of the slot |
| BS-5 | PASS | `LANA_BS5_LONGO_SIGN_20260814.md` · `b7c32dcf…0abb0a72ca` — Longo quoted, mapped; target +0.0408 in our convention; **synthetic absolute-sign anchor mandatory before real images** |
| BS-6 | PASS | `LANA_BS6_PHOTOMETRIC_CUTS_20260814.md` · `5ff7f454…4c565f51bf934a02d9b6e361` — TYPE = automated source-type exclusion (frozen wording, §3 I-5); SB cut = none in the frozen design |
| BS-7 | PASS | `TORI_BS7_DISTORTION_20260814.md` · `cb6fa7b6…eb44d955e` — FAIL_CLOSED branch declared |
| BS-8 | PASS WITH DECLARED DEVIATION ACCEPTED | `GORU_BS8_POWER_RECEIPT_20260814.md` · `b6207c7f…6233f014a92` — analytical evaluation of the pinned harness logic (§5 HC-6 wording); power ≈ 1.0000, far from the 0.95 threshold, so the deviation rescues nothing |
| BS-9 | PASS | `LANA_BS9_CONSTANTS_TABLE_20260814.md` · `4459ed1f…e04ed226a` — σ_ours 0.004805 ≤ 0.008; floor 0.0148 ≤ 0.025; robust at a = 0.85 |
| BS-10 | PASS AS INFORMATIONAL | `LANA_BS10_SHAMIR_CLASS_20260814.md` · `2c16559a…5786c17` — amplitude class pinned; **K-14 stands regardless**; published-journal locator binding remains cleanup if publication-facing |
| **BS-11 (NEW)** | **FILLED** (Kun amendment gate §2) | **Fill rule (Kun's, substantially verbatim):** *"Before any public release, the complete proposed release package, plus every prior or concurrent public release in this study's cumulative release registry, must pass the pinned `nm_release_lint.py` at SHA-256 `7ff18bfc9272bcbb924b77cb81f2b37c45a130c2b1c5ba1fbc9b95baaab323ac`; the linter self-test must report `PASS_SYNTHETIC_SELFTEST fixtures=22/22`; the unit suite must pass 36/36; any linter REJECT, self-test mismatch, unlisted file, manifest mismatch, or missing cumulative-release registry is a release HOLD."* **Validity range (all four bind):** valid only for schema-version-1 packages described in `YUI_RELEASE_LINTER_20260814.md`; valid only for aggregate-only packages, not per-object releases; valid only as an engineering release gate — not legal advice, publication authority, freeze, or acceptance; **valid only when run on the complete cumulative package context, not an isolated directory.** Pinned artifacts: `release_linter/nm_release_lint.py` · `7ff18bfc9272bcbb924b77cb81f2b37c45a130c2b1c5ba1fbc9b95baaab323ac`; `release_linter/SELFTEST.md` · `c23bed0d42865961bba1240dbcb52fb496281d044afa766a64c6a07253f66706`; `release_linter/test_nm_release_lint.py` · `4316567c26b68296fcc870534dea66b56f34cf5167bc78e16b11576d8bf309cb`; `release_linter/YUI_RELEASE_LINTER_20260814.md` · `1c47e8d9c4b4c1ff1af0ebb29d97c2b39c8a22d8e45b2342df32ecd67e07b29b`. Owner Yui (implementation) / Tori (release custody, §F-10.i). |

Cross-cutting audit receipts: `FINAL_BS1247_CLOSURE_AUDIT.json` · `01bdb1a8…4401a5d54c12`;
`KUN_REGATE_BS1_BS3_20260814.md` · `e5bc40fc…602ba483a66`.

**Freeze condition:** all slots (now eleven) inside their validity ranges — with BS-1 judged
against its REWRITTEN text and BS-11 filled — then the assembled document is sha-pinned and
returns to Kun for the freeze gate. Any slot outside its range → INVALID, back to design.

## Kill switches

K-1…K-14 carry unchanged and bind this document (K-8 and the STOP rule restated in the preamble;
K-14 restated at F-8/BS-10). F-10 adds no new kill switch; its violation class is caught by BS-11
before release and by K-8 after any real-sky statistic.

---

## Open questions for Kun's freeze gate (stated, not silently resolved)

1. **BS-11 sequencing — RESOLVED by the fill:** the linter exists, is hash-pinned, passed
   `PASS_SYNTHETIC_SELFTEST fixtures=22/22` and 36/36 unit tests under Kun's own rerun, and BS-11
   is now FILLED with his fill rule and validity range. The question dissolves; recorded rather
   than deleted so the register's history stays legible.
2. **BS-1 wording precedence:** the replacement validity text is Kun's own from his §1; Tori's six
   conditions are incorporated at F-10.b as controlling. If Kun wants the six conditions repeated
   inside the BS-1 cell verbatim rather than by reference to F-10.b, that is an editorial change
   with no semantic content — flagged so it is not mistaken for one.

**Nothing in this candidate authorises a run. No real-sky statistic exists. Kun gates; Duho owns
acceptance.**

— Lana, 2026-08-15.
