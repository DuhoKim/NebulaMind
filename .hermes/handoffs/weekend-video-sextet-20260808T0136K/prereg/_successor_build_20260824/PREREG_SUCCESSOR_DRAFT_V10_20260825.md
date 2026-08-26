# PREREGISTRATION DRAFT V10 — LONGO-AMPLITUDE TEST ON A LEVERAGE-CHOSEN FOOTPRINT

> **THIS IS A DRAFT. NOTHING IN IT IS IN FORCE.** Drafting was authorized by Duho on
> 2026-08-25 (~12:2x KST, relayed by Blanc): *"Draft the prereg now."* That authorization
> covers **WRITING this frozen promise only** — selection rule, estimator binding, decision
> regions, power requirement, blinding clauses. It authorizes **no run, no fetch, no data
> touch**. This text goes through its own adversarial gates before any real datum is touched,
> exactly as its predecessor's discipline required. It becomes a preregistration only when
> every class-P slot holds a receipt, the gates pass, and Duho signs the freeze.

Hwao, 2026-08-25 18:00 KST. Supersedes V9 (sha `b97ba35c…`, REVISE from both seats; kept).
Predecessor status: **DECLINED BY SIGNATURE 2026-08-25**
(`DECISION_MEMO_DECLINE_TO_PROCEED_20260821.md`, EFFECTIVE, sha
`b4a1f1fcaa9acbaa6b9efd3ebbe9496be8c1d83c690a012dc7a4f8520840374f`); its verified
60,308-brick sample and 208,405 sealed χ measurements are archived as successor input.

## §0 Definition by reference implementation

Every operational mechanism of this preregistration — geometry, ledger, selection chain,
retention, manifest closure, mask typing, randomness addressing, injection, permutation
contract, estimators, sigmas, calibration, the decision function, the run guards, and all
digest serializations — is DEFINED by the code bytes of

- **`ref/successor_ref_v8.py`, sha256 `1bec5c2831464e023f2fee472a30480761b9a9f40cc034ba092cbfc28ad7758a`**
- the custody boundary it calls, **`ref/closure_worker_v8.py`, sha256
  `245057259830c60e65b179bc01053d531964a7005b560e264bdefa0745c0092d`**
- fixture output **`ref/FIXTURES_V8_20260826.out`, sha256
  `fab32ba24cedcedf7fe601c3a8d9dbde13f57b1c9bf2e0b88963bcfebc33a8b5`** (46 checks, ALL FIXTURES PASS)

> **THE PIN WAS STALE AND IS NOW PROVISIONAL (2026-08-26).** This section pinned
> `successor_ref_v4.py` at sha `0b312c96…` from 2026-08-25 17:47. That file was rewritten the
> same evening and four times since; the bytes named here defined nothing that existed. A
> document that defines every mechanism by code bytes fails completely when the pin drifts, and
> it drifted within hours of being written.
>
> The pin names v8, and **as of 2026-08-26 21:24 KST it is no longer provisional**: those exact
> bytes carry a completed referee verdict (`gates/CLOSURE_V8_KIMI.md`, **CLEAR**, sha
> `47d24f32…`) and are held read-only under `gates/FREEZE_CLOSURE_V8_20260826.md`. That verdict
> is **one seat**: the codex and gpt56 seats were refused by their provider's safety filter, so
> this is a narrower review than the panel intended, and the freeze record says so in its own
> text. v4 through v7 remain on disk unchanged so each round's referee reports stay legible
> against the digests they pin.

Prose states claims, thresholds, chronology, authority and conduct. **Where prose and code
could be read to disagree, the code is the definition and the prose is the defect.** The
frozen environment is asserted by `require_environment()` (python 3.9, numpy 1.26.4,
little-endian); receipts carry `environment_record()`; fixture digests are valid under that
environment. Supersedes V5–V9 and refs v1–v3, all retained for provenance.

Sources: `SUCCESSOR_SCOPE_20260821.md` incl. Amendment 1; predecessor
`PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md` (sha `b06901c8…`, "V3-pred"); its
selection receipt `LANA_BS6_PHOTOMETRIC_CUTS_20260814.md` (sha `5ff7f454…`, "BS6-pred").

## §1 Claim boundary, target, axis, and citation anchors

**Target, cited and verified from source 2026-08-25** (not from memory — the anchor-block
law): Michael J. Longo, *"Detection of a Dipole in the Handedness of Spiral Galaxies with
Redshifts z ~ 0.04"*, Physics Letters B (2011), **doi:10.1016/j.physletb.2011.04.008**,
bibcode **2011PhLB..699..224L**, arXiv:1104.2815. Its abstract states the dipole amplitude
as **"−0.0408 ± 0.011"** from **15,158** spirals, axis **"approximately (l, b) = (52°,
68.5°)"**.

**Sign, stated so it cannot be inverted by a later reader.** Longo's published amplitude
carries a MINUS sign in his convention. Our East-of-North winding convention maps it to
**+0.0408** (V3-pred F-5), and the code constant `A_LONGO = +0.0408` is our-convention while
`A_LONGO_PUBLISHED_SIGNED = −0.0408` records his. The mandatory synthetic absolute-sign
anchor (BS-4) re-establishes the mapping empirically before any real image; the fixture
`BATTERY-SIGN` demonstrates that an injected **−0.0408** sky is never called REPRODUCED.

This tests that published amplitude at that published axis. It does not test A ≈ 0.02,
Shamir, BHU, or whether the sky is isotropic. **Fixed-axis.** The machine axis is the `AXIS`
constant; all coordinate pairs are display-only; frames are ICRS wherever coordinates appear.

## §2 Population, release choice-point, selection chain, manifest closure

### §2.1 The release choice-point — BOUND, both branches specified, resolved on its date

The DR11-vs-DR10.1 fork stays **open inside this frozen text as a bound choice-point**, so
the data decision slots in on its date without reopening frozen wording. Exactly one branch
is selected at BS-1 and recorded there; nothing else in this document changes with the
branch.

- **Branch A — DR11.** Selected iff the DR11 photo-z product exists and is publicly
  retrievable at the resolution moment. Inputs: DR11 south sweep catalogs, DR11 photo-z
  product, DR11 survey-bricks manifest, DR11 coadd image tree.
- **Branch B — DR10.1.** Selected otherwise. Inputs: the corresponding DR10.1 products.
- **Resolution rule.** BS-1 is filled on the earlier of (i) the day DR11 photo-z is confirmed
  available, or (ii) **2026-09-05**. On (ii) with photo-z still absent, Branch B is selected
  and the choice-point closes; waiting further requires a gated amendment.
- **Branch-invariance requirement.** BS-1's receipt must show that every downstream artifact
  named in §7 is produced by the same code path under either branch, differing only in the
  recorded input paths/versions. Any branch-specific logic is a defect, not a configuration.
- Status at drafting (MEASURED 2026-08-24): DR11 pages exist; no photo-z product is present.

### §2.2 Galaxy cuts — the eight predecessor Cut-6 predicates, restated from BS6-pred

`brick_primary = 1`; `maskbits = 0`; `type <> 'PSF'` (BS6-pred §3(b) disclosure carried);
`flux_r > 0`; photo-z join with `0 ≤ z_phot_median < 0.15` (predecessor product
`ls_dr10.photo_z`; the branch's product is receipted at BS-1b);
`POWER(shape_e1,2)+POWER(shape_e2,2) < 0.1836734693877551` (executable form, byte-identical
to BS6-pred; ⟺ b/a > 0.4, V3-pred I-5); `dered_mag_r < 17.7`; `shape_r > 1.5`. No
surface-brightness cut exists (documented absence, BS6-pred §3(a)).

### §2.3 Count oracle → order ledger → threshold → selection (acyclic, code-defined)

`build_plan()` performs the whole chain in one frozen call: **BS-2c** count oracle (complete
per-brick eligible counts left-joined onto an independently enumerated release brick-universe
manifest, zero rows materialized, validated by `validate_count_oracle()` which refuses on a
single missing or extra brick and on any grouped/ungrouped disagreement; counting is
server-side, row payloads are never fetched for counting; the query texts, endpoint and a
request/byte ceiling are pinned before the first query, and the `c_j` values are computed once
by `cos_theta()` and pinned as `'<f8'` bytes) → **BS-2o** threshold-free order ledger
(`greedy_ledger()`, positive-raw-count bricks only) → **BS-5p** planning power sets
`L_min_plan` and `L_plan = 1.2 × L_min_plan` → **BS-2s** selection (`local_pass()`).

**Raw versus retained, stated once and enforced in code:** raw counts drive the ledger and
the exact-mode boundary; **retained counts drive every threshold** — `L_ret`, the
`N_eq = 3·L_ret ≥ 100,000` floor, `L_plan`, and the reduction. Retention is the frozen
per-brick integer `floor(0.8572 × n)`.

**Selection claim discipline (Scope Amendment 1):** for candidate universes of ≤ 16
positive-count bricks the code's exact enumeration IS the algorithm, so minimum cardinality
holds by construction (all five adversarial gate counterexamples are fixtures and pass); at
production scale the result is exactly what the frozen procedure returns and **no minimality
or global-optimality claim attaches to it**. Contiguous-BRICKID selection remains banned.

### §2.4 Manifest closure — a frozen property, carried from the predecessor's own defect

**The property.** The selection defines the parent; **the parent's cutout geometry defines
the required brick set, INCLUDING neighbour bricks at the footprint edge**; the image
manifest may be frozen **only after that closure is computed**, and its count is recorded in
the receipt. A brick enumeration that closes over "bricks my objects sit in" is not closure.

**The check (BS-2m, class P, pre-freeze).** The planner is IMPLEMENTED in the reference code
(`plan_object_bricks`, footprint-edge neighbour rule included), and `close_manifest()` is the
single production entry point: it takes the frozen parent table plus its digest and **derives
every object's required bricks itself**. There is no argument through which a caller can hand
it an answer. It refuses on a parent-digest mismatch (an omitted or altered object changes the
digest), on any object planning zero bricks, and on a difference of even one brick in either
direction; it emits `parent_digest`, `planner_digest`, `plan_digest`, `required_count`,
`manifest_count` and the missing/extra bricknames into the receipt, so a future gate reads
numbers rather than an assurance.

**Round 6 then showed the seam had moved, not closed** — a caller could supply a shortened
parent *with a matching regenerated digest*, a shortened brick universe, or a zero cutout
half-size, and pass. That is the hash-chain lesson: a digest supplied alongside its own data
proves consistency, never custody. `close_manifest()` now binds to **external witnesses it
cannot regenerate**: the release brick universe must match the pinned digest `863e5ded…` and
the pinned cardinality 366,912; the parent digest must equal the one carried by the **BS-2s
selection receipt**; and the cutout half-size is a frozen constant derived from
`CUTOUT_PIX × CUTOUT_PIXSCALE_ARCSEC`, with no override parameter.

**Round 7 then found the planner itself was wrong, and this is the most important correction
in this document.** V8 shipped a *reimplemented* cutout planner. Run against the real
survey-bricks table it returned only the home brick for both historical objects —
reproducing the exact 60,308-vs-60,310 enumeration failure it existed to prevent — and its
fixtures passed only because they ran on a synthetic grid whose neighbour relationships this
author had constructed. Round 6's instruction to "pin and implement the cutout planner" was
read as *write a new one*; the frozen planner was already in the lane and correct.

**The reimplementation is RETIRED (it raises if called).** BS-2m binds to
`_objmanifest_20260820/build_object_manifest.py::plan_candidate_bricks` with its pinned
adapter, digest `36bbbf250215…`. Verified against the real sidecar: object 10997315463551936
→ `['3385m885', '3471m885']`, object 10995116744378804 → `['2857m870', '2894m872',
'2902m870']`. The closure fixtures now run on the **real** brick table and the **real**
historical objects, and a manifest omitting those neighbours is refused **by name**:
`CLOSURE-FROZEN-PLANNER`, `CLOSURE-RETIRED-REFUSES`, `CLOSURE-CATCHES-HISTORICAL`,
`CLOSURE-CALLER-TRUST` (3/3 — self-consistent shortened parent, shortened universe, unpinned
universe digest).

### §2.5 Acquisition

Catalog row payloads are fetched only for the selected bricks, paced and receipted, under the
ceiling fixed at BS-2c. **Image bytes only after freeze**, only for the closed manifest, under
BS-6, three streams from the start, with the producer checksum list cross-checked as the
predecessor's transport proved (60,308/60,308, zero problems).

### §2.6 The real geometry, measured (Branch B, DR10)

Run 2026-08-25 under Duho's catalog-only authorization; in the event **no fetch was needed**,
both inputs being already-acquired authorized artifacts. Receipt:
`real/REAL_GEOMETRY_RESULT_20260825.md`.

- Count oracle: universe **366,912** bricks, **270,577** with objects, **96,335** zero rows
  materialized, **832,393 / 832,393** objects placed, none outside the universe;
  count-weighted **Var(cosθ) = 0.445201**, independently reproducing the scope note's frozen
  0.4452.
- Selection **through the complete frozen reduction — removals AND the swap-then-removal
  phase** (round 8 found the swap phase missing; adding it leaves this result unchanged):
  **6,445 bricks**, **65,060 raw objects**,
  53,005 retained, **Var(cosθ) = 0.754664**, **N_eq = 120,002.9**. The
  declined run used 60,308 bricks / 208,407 objects / Var 0.0580 / N_eq 36,253 / 735.9 GB.
- **The images required are NOT the selected bricks: 12,117 bricks, ≈148 GB.** This line
  previously read "~76.8 GB of images", which was the selected 6,445 bricks priced as if they
  were the download. They are not. Each galaxy's cutout can require neighbouring bricks outside
  the selection, and the measured closure over the 65,060-object parent is **12,117 distinct
  bricks — 1.880× the selection** (`plan_digest aaeaa9f3…`, reproduced independently three
  times: by the closure itself, and twice by direct enumeration that never called it). At the
  predecessor's measured 12.2 MB/brick that is ≈147.8 GB, and Duho raised the planning ceiling
  to match on 2026-08-26.
- Stating it plainly because the draft got it wrong: **assuming the manifest equals the
  selection is the exact defect BS-2m exists to catch**, and it was sitting in this section's
  own summary line. The predecessor died of the same confusion at a smaller scale — a manifest
  of 60,308 against an analysis needing 60,310.
- **Stage P on the reduced set: 995/1000 against the x ≥ 962 rule, PASS** — measured
  2026-08-26 with **every trial judged against its own 20,000-permutation null**, so no shared
  reference null appears in the counting path
  (`real/stagep_exact.py`, receipt `real/STAGEP_EXACT_RECEIPT_20260826.json`, 431 s on 20
  workers). Geometry: the 6,445-brick reduced set, n = 53,005, Var(cosθ) = 0.754664,
  N_eq = 120,003.
  - **The earlier 997/1000 PASS is retracted**, not restated. It was measured on the
    PRE-reduction geometry and, decisively, before the conservatism check existed. That check,
    added in round 8, found the shared reference null was **not** conservative on this geometry:
    2 of 8 sampled trials had their own critical value above it (3.1672 and 3.1957 against
    3.1220) with a residual margin of only 1%.
  - What the exact re-run adds beyond the number: **zero trials disagree**. No trial was granted
    by the shared null and refused by its own, or the reverse. The round-8 finding stands as a
    finding and changed no verdict on this geometry, which means the earlier FAIL was a failure
    of the justification rather than of the result — a distinction that could only be settled by
    running it.
  - **Not yet in the definitional code.** `stagep_exact.py` is a measurement harness; the
    exact-null Stage P is not implemented in the file §0 pins. BS-5p is not fillable until it
    is, with its own fixtures and its own gate. 995 of the 1,000 own p-values also sit at
    `5.00e-05`, the resolution floor of a 20,000-permutation estimate — lower bounds, 20× below
    the 1e-3 test, so the verdict is unaffected but they are not measured values.
- Disclosed: the pinned `greedy_ledger()` and `local_pass()` are O(n²) in Python and will not
  run at 270,577 bricks. The vectorized equivalents used at scale are proven identical to them
  on 40 (order) and 30 (reduction) random cases; making the frozen implementations scale is
  open work, not a claim.

These fill the class-P inputs that six gate rounds said could not be closed by writing alone.


## §3 Statistics

Code-defined: `beta_slope()` (raw centred slope β̂; the full-sky constant `3·D̂` appears
nowhere); `perm_record()` (production Monte-Carlo permutation, **n_perm = 100,000**,
plus-one one-sided p at Longo's oriented sign, ties by exact float ≥, non-finite fails
closed, σ_β = `np.std(ddof=1)`); `perm_sigma_exact()` (the EXACT permutation sd,
`Var(β̂) = Var_pop(s)/((N−1)·Var_pop(c))`, verified against exhaustive enumeration by fixture
`PERM-SIGMA-EXACT`).

**Estimand.** A sign-symmetric classifier of accuracy a gives `E[s_obs|c] = (2a−1)·A_L·c`.
Scalar path: `Â_L = β̂/(2â−1)`. Profile path (frozen fallback, §6): `Â_L = β̂/ŵ` with
`w_profile()` under **unit weight per accepted object** — the same empirical measure as β̂.

**Uncertainties.** `sigma_ours_scalar(σ_β, β̂, a*, σ_a)` and
`sigma_ours_profile(σ_β, β̂, ŵ, w_gradient(), Cov_a)`, both fail-closed on non-finite or
degenerate input. **Cov_a is the FULL covariance matrix of {â_b} including the shared
synthetic-error term**, produced by `accuracy_from_handcheck()` — a mandatory BS-8f field,
not a supplied assumption. Decision bands evaluate at â / {â_b}; **the detection floor
evaluates at a_LB / {a_LB_b}** — each evaluation point is named where it is used.
`σ_comb = sqrt(σ_pub² + σ_ours(â)²)`, σ_pub = 0.011.

**Declared assumption (Testimony at freeze):** `Cov(β̂, â) = 0` and `Cov(β̂, {â_b}) = 0` —
the audit's agreement indicators versus permutation-null variability conditional on the mask.
Declared, not proven.

**Admissible input.** `SealedMask` and `FixtureMask` are **distinct, non-interchangeable
types**; production entry points call `require_sealed()` and refuse a fixture by type
regardless of its contents. A `SealedMask` requires the sealed calibration boundaries and
**recomputes bin labels from them** — a caller's disagreeing labels are refused, not trusted —
validates sign-vector length exactly, refuses any non-accepted row, sorts canonically by
(brickid, objid), and binds kind, schema, boundaries and acceptance flags into its digest, so
identical arrays under different provenance do not collide. Fixtures: `MASK-REFUSALS` (5/5:
fixture-to-production, bare vector, wrong sign length, disagreeing bins, non-accepted row) and
`MASK-KIND-IN-DIGEST`.

## §4 Power gate, two stages, with an equality contract

**Stage P (class P, BS-5p).** Injection is `inject_signs()` (two `rng.random()` calls per
object in canonical order; `Generator.binomial` is banned; accepts a scalar accuracy or a
per-bin vector). Planning objects are retained counts at brick centres. Floor a = 0.85.
Success = one-sided p < 0.001. **PASS rule: 1,000 trials, one-sided 95% Clopper–Pearson lower
bound ≥ 0.95, i.e. `x ≥ 962` successes** (the frozen integer; 961 fails).

**The power null, measured rather than assumed.** Running 1,000 × 100,000 full permutations
per prefix is not executable at production scale (a gate measured the nested kernel at ≈ 9
hours per prefix). Stage P therefore measures the **standardized permutation null once per
prefix** (`reference_null_z()`, 20,000 permutations) and judges all 1,000 trials against that
full empirical tail, with each trial's statistic **deflated by PWR_CONSERVATISM** so the
decision demands more evidence than the raw statistic provides.

A normal-tail approximation was tried first and **rejected on measurement**: across four
geometries the measured z\* ranged 3.0376–3.1355, bracketing the normal 3.0902, and on the
**polar geometry this design actually selects** the normal threshold came out
anti-conservative. A fixture-tuned inflation factor would have been fitting, not a contract.

Round 6 found that a measured null plus a fixed deflation is still **not conservative by
construction** — the same 1,000 skies could turn a FAIL into a PASS. The repair is not a
larger fudge factor. **Stage P now verifies itself**: every calibrated success landing within
10× of the decision threshold is re-tested against an independent full permutation run, and a
single unconfirmed success **fails the stage closed**. Far-from-boundary successes need no
confirmation, which is what keeps it affordable.

This is checked, and it bites: on a fixture sized to sit near 50% power the mechanism
**refuted 2 of 7 boundary successes and failed the stage closed** (`PWR-SELF-VERIFYING`),
while `PWR-CALIBRATED-ALONE-INSUFFICIENT` reproduces the round-6 finding directly (calibrated
decisions alone confirmed in only 21 of 22 cases). **Measured on the real REDUCED geometry (§2.6): 995/1000, PASS, with every
trial judged against its own null rather than a shared reference (2026-08-26). The earlier
997/1000 on the pre-reduction geometry is retracted.** **Production decisions
never use this path**: the production runner always executes the full 100,000-permutation
record on the sealed mask.

**Stage C (class E, BS-5f; after inference, before unblinding).** The same frozen generator,
addresses and pass rule, run on the **sealed accepted-position mask** (BS-2f: brickid, objid,
position, acceptance flag, calibration-bin label — never a χ sign), with the measured a_LB
(scalar) or {a_LB_b} (profile) from BS-8f. FAIL → **INCONCLUSIVE-BY-POWER declared before
unblinding; the run halts; no real-sky statistic is ever formed.**

## §5 Decision regions — computed, never read off a table

`run_production_verdict()` is the **only** production path to a verdict. It exposes **no
permutation injection, no permutation-count override, and no stage/trial/mask-kind override**;
it calls `require_environment()`, `require_authorization()`, `require_complete_sample()` and
`require_sealed()`, requires a BS-5f Stage-C receipt bound to that exact mask digest, derives
the N_eq floor from the mask's own geometry, and only then runs the full 100,000-permutation
record before the pure decision helper. Synthetic exploration lives in the separately named
`explore_verdict()`. (Both V6 gates monkeypatched every guard and still extracted a verdict
from the V6 code through a test seam; fixtures `PROD-NO-SEAMS`, `PROD-CALLS-GUARDS` and
`PROD-REFUSES` close that.) It emits exactly one of four outcomes (V3-pred F-6 thresholds,
applied to Â_L):

- **REPRODUCED-LONGO:** p < **0.001** AND Longo's sign AND |Â_L − 0.0408| ≤ 3·σ_comb AND
  Â_L ≥ the evaluated floor.
- **REJECTED-AT-LONGO-AMPLITUDE:** p > **0.05** AND (|Â_L| + 3·σ_ours(â)) < **0.0408**.
- **INCONCLUSIVE:** any other numeric outcome, explicitly including 0.001 ≤ p ≤ 0.05.
- **INCONCLUSIVE-BY-POWER / INCONCLUSIVE-BY-CALIBRATION:** §4 / §6; no run.

**Detection floor (V3-pred F-7):** `3.09 · σ_ours(a_LB)`, printed in the results table. No
Â_L below the evaluated floor is nameable REPRODUCED regardless of the band.

**Validation battery, carried from the lapsed build spec at its named boundaries** (V6's
version was weakened and both gates said so): A = 0 must never return REPRODUCED
(`BATTERY-A0`); A = −0.0408 must not return REPRODUCED (`BATTERY-SIGN`); **A = +0.0408 at a
powered N must return REPRODUCED-LONGO** (`BATTERY-POS`, measured Â_L = 0.04243, p = 2.2e-21);
and an under-powered geometry must yield INCONCLUSIVE-BY-POWER **derived from N_eq**, never
from a caller-supplied boolean (`BATTERY-NEQ`).

**Run guards, also carried from the lapsed spec:** `require_authorization()` refuses real
data without an authorization file pinned to a SHA-256 (that authorization does not exist and
must not be written yet); `require_complete_sample()` refuses unless every parent object has
a measurement receipt — a partial run is not a smaller run, it is a different experiment.

## §6 Conduct

- **Disclosure/blinding.** Nothing derived from any real χ value — value, sign, summary, or
  count of signs — is published, spoken, or written outside the sealed results store before
  the primary lock. The predecessor's §4/condition-2 breach is why this clause exists.
- **No strata in the estimator.** The centred slope needs no tertiles; the one-shot strata
  hazard is retired by design.
- **Calibration.** Bin-construction algorithm and the 3 × 9 joint allocation with V3-pred's
  nine HC strata are frozen in code (`calibration_bins()`, `assign_bins()`,
  `allocate_handcheck()` — proportional, largest remainder, explicit tie rule, and BOTH
  inherited floors enforced: ≥ 10 per non-empty joint cell **and ≥ 30 real labels per live
  inherited HC stratum** (V6 enforced only the first; a gate produced a formally-filled but
  invalid sample). Infeasible floors FAIL rather than shrink. `calibration_bins()` states and
  IMPLEMENTS one tie rule and refuses degenerate bins. Numeric boundaries are instantiated and
  sealed at **BS-2f** from positions and flags only. **BS-8f** reports â, σ_a, a_LB, per-bin
  â_b, σ_ab, a_LB_b, ε̂ and the full Cov_a via `accuracy_from_handcheck()`, which implements
  **the inherited HC-1H estimator** `a = (raw − ε)/(1 − 2ε)` with the shared-ε derivative
  propagated — so Cov_a's off-diagonal is a real shared-error term, not an additive constant.
  (V6 returned the raw agreement rate and both gates caught it.) **Admissibility (`adjudicate_path()`):**
  `max_b |â_b − â| ≤ 0.03` AND every `a_LB_b ≥ 0.85` → scalar path; spread failure only →
  profile path; any `a_LB_b < 0.85` → **INCONCLUSIVE-BY-CALIBRATION, pre-unblinding halt.**
  V3-pred's HC-1H measurement and validity rules (committee, sealed keys, HC-5, HC-6) are
  carried by quotation at freeze.
- **Void rule.** Any post-first-real-χ change to ANY binding rule, parameter, algorithm, slot
  schema, randomness/serialization contract, reference-code byte, or decision threshold in
  this preregistration voids the run; only the mechanical filling of predeclared class-E
  values by their frozen producers is exempt. Post-read amendments cannot cure a void.
- **One change per iteration** (external-practice adoption, 2026-08-25): every gated revision
  of this text changes one thing per finding, and the §10 trace maps finding → change; any
  change not traceable to a finding is listed separately with its hypothesis stated.
- **No claim stronger than its check.** Gate-state sentences never exceed the cited
  artifact's first line.
- **Custody.** Receipts with digests; deliverables sha-pinned at gate dispatch by the gate's
  own report (an external witness) and committed to git; self-referential hash chains are not
  custody; describe-vs-compute discipline throughout.
- **Blind double, honestly scoped** (gpt56-V5 F6 / codex-V5 F3): because §0 makes the code
  bodies normative, a second implementation cannot be required to reproduce body-defined bytes
  without reading them. Therefore: the second product is a **clean-room reimplementation from
  this constitution plus a published per-function normative specification** (op order stated),
  and it is gated against the reference on the fixture battery. Where the spec is insufficient
  to reproduce a digest, that is a **spec defect to be repaired**, not an agreement failure.
  Divergence in any integer, sequence, or verdict is a STOP recorded as a finding — never
  reconciled by editing either implementation toward the other.

## §7 Binding slots (producer · inputs available at that time · schema · code symbol · blocks)

**Class P — freeze prerequisites**

| slot | producer | content | code symbol | blocks |
|---|---|---|---|---|
| BS-1 | Duho | release branch A/B + provenance; branch-invariance evidence | — | everything |
| BS-1b | Hwao | photo-z product paths, columns, join keys, predicate-5 provenance | — | BS-2c |
| BS-2c | Hwao + blind double | universe manifest, per-brick counts, zero rows, closure proofs, ceilings, pinned `c_j` bytes | `validate_count_oracle` | BS-2o |
| BS-2o | Hwao + blind double | full traversal order + per-prefix ledger | `greedy_ledger`, `ledger_digest` | BS-5p |
| BS-5p | Hwao | L_min_plan, L_plan, retained basis, x ≥ 962 rule, addresses | `stage_power`, `build_plan` | BS-2s |
| BS-2s | Hwao + blind double | selected set, L_ret, L_raw, N_eq, fixtures, Stage-P re-pass | `local_pass`, `build_plan` | BS-2m |
| BS-2m ✅ **FILLED 2026-08-26** | Hwao | **manifest closure**: required set from the frozen cutout planner, counts, refusal on any difference. Receipt: `gates/FREEZE_CLOSURE_V8_20260826.md` — mechanism frozen at v8 (`successor_ref_v8.py` `1bec5c28…`, `closure_worker_v8.py` `245057259…`), 33/33 probes, referee `gates/CLOSURE_V8_KIMI.md` **CLEAR** (one seat; two seats refused by their provider). Derived closure: 65,060 objects → 6,445 selected → **12,117 required bricks**, `plan_digest aaeaa9f3…`, reproduced independently three times. Eight items carried open in the freeze record. | `close_manifest`, `closure_receipt` | manifest freeze |
| BS-3 | Hwao | instrument identity: weights `83008c1c…`, τ = 4.4006456017494235, antisymmetry identity | — | BS-9 |
| BS-9 | Hwao + gpt seat | **input-path rebinding**: branch-specific single-band HDU/plane schema, production input function (code + hash + tensor layout), full R1–R5 rerun through it, gated replacement runner. `nm_acquire_cutouts.py` remains PROHIBITED (V3-pred lines 374–386); predecessor R1–R5 receipts are historical context, never evidence for this run's path | — | BS-6 |
| BS-4 | Hwao | synthetic absolute-sign anchor rerun under this text | `inject_signs`, `decide` | unblinding |
| BS-7p | Hwao | randomness/serialization declaration + frozen fixture battery + boundary p-values + environment | `receipt`, `run_fixtures` | BS-6 |
| BS-8p | Hwao | HC-1H rules by quotation + measurement plan + 3 × 9 allocation | `allocate_handcheck` | BS-8f |

**Class E — execution gates**

| slot | producer | content | blocks |
|---|---|---|---|
| BS-6 | Hwao | image transport approval: closed manifest sha, byte ceiling, producer checksum list | first image byte |
| BS-2f | Hwao | sealed accepted-position mask + sealed calibration boundaries | Stage C |
| BS-8f | Hwao + hand-check committee | â, σ_a, a_LB, per-bin values, full Cov_a, integrity triggers | Stage C |
| BS-5f | Hwao | Stage-C confirmatory power receipt | unblinding |
| BS-7f | Hwao | production permutation record: β̂_obs, canonical 800,000-byte payload digest, p, environment | verdict |
| BS-V | Hwao | **verdict + primary lock**: `decide()` output, evaluated floor, path taken, mask digest | disclosure |

## §8 Inherited defects this text is built to prevent (named, so its gate can confirm each fix)

1. **Manifest-versus-parent gap (found 2026-08-25).** The predecessor's 60,308-brick manifest
   was frozen from an enumeration that did not close over the parent's neighbour
   requirements. **ls_id 10997315463551936** (dec −88.59) requires brick **3471m885**; **ls_id
   10995116744378804** (dec −87.13) requires brick **2857m870**. Both bricks exist in the
   release and appear in the producer's r-band checksum list; neither was in the manifest; the
   parent needed **60,310**. The cutter held both objects WAITING — fail-closed, the system
   working — but nothing detected the shortfall until the chain stalled two objects short at
   the end. **Fixed by §2.4 + BS-2m**, whose fixtures replay this exact shape and report the
   two bricknames.
2. **Footprint-blind power.** A uniform-sphere power calculation certified a footprint it
   never inspected. **Fixed by §4**: accepted-sample geometry is a named input; Stage C
   accepts only the sealed mask.
3. **Full-sky normalisation constant.** `3·D̂` inflated by 42.76% on the real footprint.
   **Fixed by §3**: the centred slope needs no footprint constant, and `3·D̂` is banned.
4. **Attenuation-versus-target mismatch.** Comparing a raw, attenuated slope to the undiluted
   published amplitude could formally REJECT a true signal. **Fixed by §3** (β̂ / Â_L split).
5. **Unreachable significance threshold.** Plus-one Monte-Carlo p at 999 permutations can
   never fall below 0.001; the predecessor's validator passed on that impossibility.
   **Fixed by §3/§4** (n_perm = 100,000; resolution demonstrated on both sides).
6. **Silent axis divergence.** Two "blind-double" implementations used axes 3.72 arcmin apart.
   **Fixed by §1/§0** (one pinned unit vector, display-only coordinates).
7. **Count-based stopping rule on ordered brick IDs.** Guaranteed a geometric cap.
   **Fixed by §2.3** (leverage stopping rule; contiguous selection banned).
8. **Verdict by human reading.** No implementation of the decision regions existed.
   **Fixed by §5** (`decide()` is the only verdict producer).

## §9 Academic-gates fields (external-practice adoption, 2026-08-25)

Citations carry bibcode/DOI (§1) and are verified from source at freeze, not from memory.
Coordinate frame (ICRS) and the axis representation are named wherever coordinates appear.
Data releases are named with version and branch (§2.1). Every catalog query is archived
VERBATIM as a runnable script in its receipt — no natural-language or MCP output enters a
receipt unreconstructed. Seeds, permutation counts, and environment are pinned (§0, §3–§4).
Checksums: producer-supplied digests are cross-checked against our bytes (§2.5).

## §10 Gate plan and repair trace

**V9 → V10.** Round 8 was the first round with both referee seats reporting (the earlier
seat-loss was a provider content classifier reading an offensive-security brief, not a
science objection; the brief is now written as a methods-referee request). Both returned
REVISE with **four findings each, down from nine and thirteen** in earlier rounds, and their
findings were the same four. All four are repaired:

| finding (both seats) | change |
|---|---|
| `close_manifest()` still called the RETIRED planner, so the round-7 closure repair was never wired to the production entry point | `close_manifest()` takes the release geometry sidecar and calls `frozen_plan_object()`; `planner_digest` is the frozen planner's; verified end-to-end on real data — a complete manifest passes and the historical short manifest is refused naming `['2857m870', '3471m885']`; new fixture `CLOSURE-PRODUCTION-USES-FROZEN` asserts the wiring by source inspection |
| the fast reduction omitted `local_pass()`'s **swap-then-removal** phase, so the 6,445 figure was not the frozen chain's output (counterexample: 6 bricks frozen vs 7 removal-only) | `_swap_then_remove` implemented; reproduces the referee's counterexample exactly; matches `local_pass` on **400 cases in the referee's own seed and regime, zero mismatches**; the real selection is **unchanged at 6,445** — the swap scan finds no improving swap on this geometry |
| Stage P confirmed only the boundary band, and one reference null was never shown conservative for 1,000 trials | a deterministic sample of NON-boundary successes is now confirmed too, and the shared reference null is measured against individual trials' own nulls; a non-conservative reference **fails the stage closed** |
| the count-oracle completeness proof compared a caller-supplied total with itself and its inputs were optional | the ungrouped total must equal the **pinned release total 832,393**; an omitted proof input is refused; the real oracle still validates under the stricter rule (`ORACLE-INDEPENDENT-WITNESS`) |

**Referee-confirmed positives this round:** all dispatch digests matched, the fixture
transcript reproduced byte-for-byte, the frozen planner returns both historical neighbour
bricks, and the 6,445-brick artifact reproduced exactly from the recorded inputs.

**Stage P HAS been re-measured on the reduced set (2026-08-26): 995/1000, PASS**, by the exact
route — one null per trial, no shared reference — which removes the assumption the widened audit
falsified rather than arguing it back. The retracted 997/1000 is described in §2.6. Two things
remain open and are not claimed closed: the exact Stage P lives in a measurement harness and not
in the code §0 pins, so **BS-5p cannot be filled yet**; and nobody has refereed the measurement,
so it is measured, not accepted.

**Disclosed rather than claimed closed** (unchanged): the clean-room specification for the
blind double, BS-9's input-function schema, the BS-V primary lock, and that the frozen
`greedy_ledger()`/`local_pass()` do not scale to the production universe — the fast
equivalents are evidenced by the batteries above, not proven in general.

Next: both referee seats on this text, the corrected code, and the real-geometry receipt.
**Undecided and untouched:** the methods-note question and the strata question.
