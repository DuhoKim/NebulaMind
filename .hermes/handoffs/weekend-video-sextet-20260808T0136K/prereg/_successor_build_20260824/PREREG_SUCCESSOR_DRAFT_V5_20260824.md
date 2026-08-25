# PREREGISTRATION DRAFT V5 — LONGO-AMPLITUDE TEST ON A LEVERAGE-CHOSEN FOOTPRINT

> **THIS IS A DRAFT. NOTHING IN IT IS IN FORCE.** It becomes a preregistration only when every
> class-P slot holds a receipt, the text passes adversarial gates, and Duho signs the freeze.
> Class-E slots are execution gates governed by the frozen text, filled during the run by their
> named producers; each blocks the stage after it.

Hwao, 2026-08-24 23:41 KST. V5 repairs the union of `gates/GATE_GPT56_SUCCESSOR_V4.md` (F1–F8)
and `gates/GATE_CODEX_SUCCESSOR_V4.md` (F1–F10), both REFUSED on V4, by a structural change:

**§0 Definition by reference implementation.** Every operational mechanism of this
preregistration — geometry, the ledger and its traversal, the selection pass, retention, the
randomness addressing, injection, the permutation contract, all estimators and sigmas, and all
digest serializations — is DEFINED by the code bytes of
**`ref/successor_ref.py`, sha256 `67bc4876858c4cb4445ccf40f41a4d3977c1d43e0b88ec5890d9b6b0091a4449`**,
whose fixture battery output is frozen at
**`ref/FIXTURES_20260824.out`, sha256 `c82b2a253c4f55b9b4f28f697d496f8e8cbf5762771307c036ca77dd65950e25`**
(ALL FIXTURES PASS, environment recorded in the output: numpy 1.26.4, darwin). Prose below
states claims, thresholds, chronology, and conduct; where prose and code could be read to
disagree, THE CODE IS THE DEFINITION and the prose is the defect. Fixture digests are valid
under the recorded environment; every receipt produced by the code records its own
environment, and the blind double (§6) runs both implementations under one recorded
environment.

Sources: design authority `SUCCESSOR_SCOPE_20260821.md` incl. Amendment 1; predecessor
`PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md` (sha256
`b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`, "V3-pred"); its selection
receipt `LANA_BS6_PHOTOMETRIC_CUTS_20260814.md` (sha256
`5ff7f45489b4b21066eeeaeaed10cd6087a0bfaa4c565f51bf934a02d9b6e361`, "BS6-pred").

## §1 Claim boundary, target, axis

Tests Longo 2011's published **|A_L| = 0.0408, σ_pub = 0.011** at Longo's published axis
(galactic (52°, 68.5°)); not A ≈ 0.02, not Shamir, not BHU, not isotropy. **Fixed-axis.** The
machine axis is the `AXIS` constant in the reference code (the ICRS unit vector derived as the
code's docstring states); every coordinate pair is display-only; `cos θ` is `cos_theta()`.

## §2 Population, selection chain, acquisition

**Release.** DR11 if its photo-z product exists at freeze; else DR10.1. Decision date
2026-09-05 (Duho). Only input paths change.

**Cuts.** The eight BS6-pred predicates, restated with predicate 6 as its executable form:
`brick_primary = 1`; `maskbits = 0`; `type <> 'PSF'` (BS6-pred §3(b) disclosure carried);
`flux_r > 0`; photo-z join with `0 ≤ z_phot_median < 0.15` (predecessor product
`ls_dr10.photo_z`; successor product receipted at BS-1b);
`POWER(shape_e1,2)+POWER(shape_e2,2) < 0.1836734693877551`; `dered_mag_r < 17.7`;
`shape_r > 1.5`. No surface-brightness cut exists (BS6-pred §3(a)).

**BS-2c count oracle (class P).** An independently enumerated **release brick-universe
manifest** (the release's survey-bricks product for the hemisphere) is hash-pinned with its
cardinality. Grouped per-brick counts under the eight predicates are **left-joined onto that
manifest**; absent groups materialize as explicit `n_eligible = 0` rows; the receipt proves
(i) the anti-join in both directions is empty, (ii) manifest cardinality equals table row
count, (iii) the grouped sum equals the ungrouped total from the same service. Counting is
server-side; row payloads are not fetched. The receipt pins the query texts, endpoint, a
request/byte ceiling fixed before the first query, and the canonical `'<f8'` bytes of every
brick's `c_j` (computed once by `cos_theta()`; downstream consumes these bytes and never
recomputes from ra/dec). Zero-count bricks stay in the receipt and are excluded from
traversal by the code's frozen rule.

**BS-2o order ledger (class P).** `greedy_ledger()` over the BS-2c table: full deterministic
traversal, per-prefix `(k, brickid, N, Var, L_raw)`; no threshold input. Ledger digest =
`ledger_digest()`.

**BS-5p planning power (class P).** For ascending ledger prefixes k, `stage_power()` at
`(STAGE_P, prefix=k)` on the prefix's **retained** planning objects: counts
`retained_counts()` (per-brick integer floor at 0.8572), objects at brick centres, floor
a = 0.85. **L_ret(k)** = `sse(retained_counts, c)` of the prefix. Success = one-sided
p < 0.001; PASS = **x ≥ 962 of 1,000** (the code's frozen integer; derivation in code
comment). **L_min_plan = L_ret of the smallest passing prefix; L_plan = 1.2 × L_min_plan.
The N_eq floor binds RETAINED leverage: 3·L_ret ≥ 100,000.** L_raw is reported alongside,
never thresholded.

**BS-2s cut + reduction (class P).** `local_pass()` on the BS-2o order at L_plan (evaluated
on retained counts, matching BS-5p's L_ret semantics). For candidate universes of ≤ 16
positive-count bricks the code's exact enumeration IS the algorithm (minimum cardinality by
construction — this covers every fixture); for production scale the result is exactly what the
frozen procedure returns and **no minimality claim attaches to it** (Scope Amendment 1
discipline; the word "minimizes" is retired). Reaching the move cap is FAIL. The receipt
reports S_final, L_ret(S_final), L_raw(S_final), brick count, the pre-reduction baseline, and
the fixture battery (the five gate counterexamples are IN the frozen fixture output).
Stage P is re-run once on S_final at `(STAGE_P, prefix=0)` and must pass (L_plan already
fixed — acyclic).

**Acquisition.** Catalog row payloads (positions, ids) are fetched only for S_final bricks,
paced, under the BS-2c-stated ceiling. Image bytes: only after freeze, only S_final, under
BS-6. Contiguous-BRICKID selection remains banned. (Sweep-bulk context: the gpt1 inventory,
sha `2df3a220…`, holds two 1,436-file version groups; the selected release would be ~1,436
files extrapolating to ~1.776 TB from its five measured sizes — an estimate, and the reason
bulk fetch was rejected.)

## §3 Statistics

Defined by the code: `beta_slope()` (raw centred slope β̂; the banned constant `3·D̂` appears
nowhere); `perm_record()` (Monte Carlo permutation, n_perm = 100,000, plus-one one-sided p at
Longo's oriented East-of-North sign, ties by exact float ≥, non-finite fails closed);
σ_β = `np.std(beta_perm, ddof=1)`. **Estimand:** scalar path `Â_L = β̂/(2â−1)`; fallback path
`Â_L = β̂/ŵ` with `w_profile()` (unit weight per accepted object — the same empirical measure
as β̂). **Sigmas:** `sigma_ours_scalar(σ_β, β̂, a*, σ_a)` and
`sigma_ours_profile(σ_β, β̂, ŵ, w_gradient(), Cov_a)` where **Cov_a is the FULL covariance
matrix of {â_b} including the shared synthetic-error contribution, a mandatory BS-8f field.**
Decision bands use a* = â (scalar) or {â_b} (fallback); the detection floor uses a* = a_LB
(scalar) or {a_LB_b} with the same profile formula (fallback), where
`a_LB(_b) = â(_b) − 1.645·σ_a(_b)` one-sided. `σ_comb = sqrt(σ_pub² + σ_ours(â)²)`.
**Declared assumption (Testimony at freeze): Cov(β̂, â) = 0 and Cov(β̂, {â_b}) = 0** — the
audit's agreement indicators vs permutation-null variability conditional on the mask; declared,
not proven.

## §4 Power gate, two stages

**Stage P** — §2 BS-5p above (planning bound; brick-centre retained objects; floor a = 0.85).
**Stage C (class E, BS-5f; after inference, before unblinding).** `stage_power()` at
`(STAGE_C, prefix=0)` on the **sealed accepted-position mask** (BS-2f: per-object brickid,
objid, position, acceptance flag, calibration-bin label — never a χ sign), rows in the code's
canonical order (ascending brickid, then objid), with the measured a_LB (scalar) or {a_LB_b}
(fallback) from BS-8f. Uniform-sphere, parent-position, or any non-mask input is inadmissible.
FAIL → **INCONCLUSIVE-BY-POWER before unblinding; the run halts; no real-sky statistic is
formed.**

## §5 Decision regions (V3-pred F-6 thresholds, applied to Â_L)

- **REPRODUCED-LONGO:** p < **0.001** AND Longo's sign AND |Â_L − 0.0408| ≤ 3·σ_comb.
- **REJECTED-AT-LONGO-AMPLITUDE:** p > **0.05** AND (|Â_L| + 3·σ_ours(â)) < **0.0408**.
- **INCONCLUSIVE:** any other numeric outcome (0.001 ≤ p ≤ 0.05 included) or any triggered
  INCONCLUSIVE rule in this document.
- **INCONCLUSIVE-BY-POWER / INCONCLUSIVE-BY-CALIBRATION:** per §4 / §6; no run.
**Floor (V3-pred F-7):** one-sided **3.09·σ_ours(a_LB)** on Â_L (fallback: profile formula at
{a_LB_b}), printed in the results table; no Â_L below it is nameable REPRODUCED.

## §6 Conduct

- **Disclosure.** Nothing derived from any real χ value — value, sign, summary, or count —
  leaves the sealed results store before primary lock.
- **No strata in the estimator.** (The labelling audit's bins are audit design, not sky
  statistics.)
- **Calibration.** The bin-construction ALGORITHM (three count-weighted c-tertile boundaries
  over accepted objects, unit weight per object) and the joint allocation rule with V3-pred's
  nine HC strata (hand-check quotas allocated over the 3 × 9 product cells proportionally to
  cell counts, minimum 10 per non-empty cell) are frozen in **BS-8p**. The numeric boundaries
  are instantiated and sealed at **BS-2f** (positions + flags only, before any χ sign is
  opened); **BS-8f** consumes them and reports â, σ_a, per-bin â_b, σ_ab, a_LB(_b), and the
  full Cov_a matrix. **Admissibility:** `max_b |â_b − â| ≤ 0.03` AND every `a_LB_b ≥ 0.85` →
  scalar path; spread failure only → fallback path; any `a_LB_b < 0.85` →
  **INCONCLUSIVE-BY-CALIBRATION, pre-unblinding halt.** V3-pred's HC-1H measurement and
  validity rules (committee, sealed keys, HC-5, HC-6) are carried by quotation at freeze.
- **Void rule.** Any post-first-real-χ change to ANY binding rule, parameter, algorithm, slot
  schema, randomness/serialization contract, or decision threshold in this preregistration —
  §§1–6, the reference code, and the slot register alike — **voids the run**; only the
  mechanical filling of predeclared class-E values by their frozen producers is exempt.
  Post-read amendments cannot cure a void.
- **Custody.** Receipts with digests; deliverables sha-pinned at gate dispatch by the gate's
  own report and committed to git; self-referential hash chains are not custody;
  describe-vs-compute law throughout.
- **Blind double.** A second implementation is built from this constitution + the reference
  code's INTERFACE (function signatures, address scheme, serialization schema) without reading
  the reference code's bodies; both run under one recorded environment on identical inputs
  (including BS-2c's pinned `c_j` bytes). Agreement: integer/sequence outputs exact; digest
  payloads byte-equal; float scalars ≤ 1e-9 relative. Divergence is a STOP recorded as a
  finding, never reconciled by editing either side toward the other.

## §7 Binding slots

**Class P (before freeze):** BS-1 release choice + provenance (Duho, Sep 5 rule) · BS-1b
photo-z product paths/columns/join keys · BS-2c count oracle (universe manifest + closure
proofs + c_j bytes + ceilings) · BS-2o order ledger (blind-doubled) · BS-5p planning power
(L_min_plan, L_plan, L_ret basis) · BS-2s reduction + fixtures + Stage-P re-pass
(blind-doubled) · BS-3 instrument identity: weights `83008c1c…`, τ = 4.4006456017494235,
antisymmetry identity · **BS-9 input-path rebinding [gpt56-V4 F7]: the release-specific
single-band HDU/plane schema, the production input function (code + hash + tensor layout), a
full R1–R5 rerun through that production path, and the gated replacement runner —
`nm_acquire_cutouts.py` remains PROHIBITED per V3-pred lines 374–386; predecessor R1–R5
receipts are historical context, never evidence for this run's path** · **BS-7p** randomness/
serialization declaration + the frozen fixture battery output (both pins in §0) + boundary
p-value and injection digests · BS-8p calibration + HC plan (above).

**Class E (during the run; each blocks the next stage):** BS-6 image transport approval
(manifest sha, byte ceiling, producer checksum list) → first image byte · BS-2f sealed
accepted-position mask + sealed calibration boundaries → Stage C · BS-8f accuracy receipt
(fields per §6) → Stage C · BS-5f Stage-C power receipt → unblinding · **BS-7f** production
permutation record (β̂_obs, the canonical 800,000-byte payload digest, p, environment,
recomputation from raw indices AND labels) → decision release.

**Testimony obligations at freeze:** the zero-covariance assumptions (§3); the ~1.776 TB
estimate's basis; Amendment 1's operationalization statement.

## §8 Carried / rebuilt / retired

**Carried:** instrument weights + τ + antisymmetry identity (as identity, subject to BS-9
rebinding); HC-1H committee + sealed keys + HC-5/HC-6; transport custody discipline.
**Rebuilt:** selection chain, statistics, power gate, input-path binding, this text.
**Retired:** descending-|c| ranking; the V2 symbol Â_c; "maximizes"/"minimizes" as claims;
both pre-V4 leverage implementations; `nm_acquire_cutouts.py` (prohibited, not retired-silent).

## §9 Repair trace (V4 → V5)

gpt56 F1 & codex F2 → BS-7p/BS-7f split (§7). gpt56 F2 & codex F1 → §0 code-as-definition:
exact mode ≤ 16 bricks IS the algorithm (all five counterexamples in the frozen fixture
output); "minimizes" retired; move semantics, scan orders, cap-FAIL in code. gpt56 F3 &
codex F3/F4 → §6: algorithm in BS-8p, boundaries sealed at BS-2f, unit-weight measure,
`w_gradient()` + full Cov_a + fixture in code. gpt56 F4 & codex F5 → address-based
`rng_at()`, spawn banned, APIs frozen in code, prefix/stage in the address, canonical row
order, injection digests in the fixture output. gpt56 F5 & codex F8 → BS-2c universe
manifest + left-join + zero rows + dual anti-join + zero-exclusion rule (code). codex F6 →
L_ret defined; thresholds bind L_ret; L_raw reported. gpt56 F6 & codex F7 → c_j pinned as
bytes at BS-2c; frozen op order in code; binary digest schema; JSON retired from digest duty.
gpt56 F7 → BS-9. gpt56 F8 & codex F9 → §6 void rule over everything binding. codex F10 →
per-version inventory numbers (§2).

Next: re-gate THIS text + the pinned code (gpt-5.6-sol + codex). Then freeze candidate →
Duho's sign-off → 444 + git → class E.
