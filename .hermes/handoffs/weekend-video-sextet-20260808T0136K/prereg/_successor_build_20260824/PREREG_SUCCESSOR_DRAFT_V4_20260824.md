# PREREGISTRATION DRAFT V4 — LONGO-AMPLITUDE TEST ON A LEVERAGE-CHOSEN FOOTPRINT

> **THIS IS A DRAFT. NOTHING IN IT IS IN FORCE.** It becomes a preregistration only when every
> class-P slot (§7) holds a receipt, the text passes adversarial gates, and Duho signs the
> freeze. Class-E slots are execution gates governed by the frozen text, filled during the run;
> each blocks the stage after it.

Hwao, 2026-08-24 23:19 KST. V4 repairs the union of blocking findings from
`gates/GATE_GPT56_SUCCESSOR_V3.md` (F1–F6) and `gates/GATE_CODEX_SUCCESSOR_V3.md` (F1–F8),
both REFUSED on V3 (sha `1c4788c5…`, superseded, kept). Sources: design authority
`SUCCESSOR_SCOPE_20260821.md` **as amended 2026-08-24 by its Amendment 1** (the "maximise"
requirement is operationalized, not claimed as global optimality — see §2); predecessor
`PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md` (sha256
`b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`, "V3-pred"); its selection
receipt `LANA_BS6_PHOTOMETRIC_CUTS_20260814.md` (sha256
`5ff7f45489b4b21066eeeaeaed10cd6087a0bfaa4c565f51bf934a02d9b6e361`, "BS6-pred").

## §1 Claim boundary, target, and the machine axis

This tests Longo 2011's published **|A_L| = 0.0408, σ_pub = 0.011** at Longo's published axis.
It does not test A ≈ 0.02, Shamir, BHU, or whether the sky is isotropic. **Fixed-axis.**

Published rendering: galactic **(l, b) = (52°, 68.5°)** [V3-pred line 124]. Frozen machine
value — the ICRS unit vector from (l, b) = (52.000000°, 68.500000°) under the IAU rotation with
NGP (192.85948°, 27.12825°), l_NCP = 122.93192°:

**n̂_L = (−0.676971771271432, −0.509846551777774, +0.530816083537352)**

Every implementation consumes this vector verbatim; no runtime frame conversion. The pairs
(α, δ) ≈ (216.9844°, 32.0606°) and (217°, 32°) are display-only. c = u · n̂_L.

## §2 Population, selection, and the acyclic planning chain

**Release.** DR11 if its photo-z product exists at freeze; else DR10.1. Decision date
2026-09-05 (Duho's call). Only input paths change with the release.

**Galaxy cuts — the full predecessor Cut-6 predicate set, restated from BS6-pred; predicate 6
quoted as its executable SQL form** [codex-V3 F7]:
1. `brick_primary = 1`
2. `maskbits = 0`
3. `type <> 'PSF'` (BS6-pred §3(b) disclosure carried)
4. `flux_r > 0`
5. photo-z join with `0 ≤ z_phot_median < 0.15` — the predecessor's photo-z predicate, carried;
   product was `ls_dr10.photo_z`; successor release's product receipted at BS-1b
6. `POWER(shape_e1,2)+POWER(shape_e2,2) < 0.1836734693877551` (executable form, byte-identical
   to BS6-pred; display equivalence: shape_e1² + shape_e2² < 0.1836…, ⟺ b/a > 0.4; V3-pred I-5)
7. `dered_mag_r < 17.7`
8. `shape_r > 1.5`
No surface-brightness cut exists (documented absence, BS6-pred §3(a)).

**The count oracle (BS-2c, class P)** [gpt56-V3 F2 / codex-V3 F4]: before any selection step, a
complete per-brick table `{brickid, ra, dec, n_eligible}` covering EVERY candidate brick of the
footprint is produced by **server-side count queries** (per-brick `COUNT(*)` under the eight
predicates, grouped by brick) through the same catalog query service whose full-keyspace census
certified the predecessor's 832,393 dered Cut-6 count — row payloads are never fetched for
counting. The table is hash-pinned. Its query text, service endpoint, and a completeness proof
(sum over bricks equals the ungrouped total count from the same service, shown side by side)
are part of the receipt. A byte/request ceiling for the query route is fixed in the receipt
before the first query. If the release's service cannot produce such counts, that fact is
receipted and an alternative bounded route is gated BEFORE any selection — the all-candidate
argmax is never run on partial counts. (The gpt1 sweep inventory at
`_successor_build_20260824/gpt1/sweep_inventory.jsonl`, sha `2df3a220…`, documents why bulk
sweep fetch was rejected: 2,872 files, 10 measured sizes averaging 1.24 GB — an ESTIMATED ~1.8
TB; estimate, not a byte inventory.)

**Selection: the acyclic planning chain** [gpt56-V3 F1/F3, codex-V3 F1/F2; Scope Amendment 1]:

- **BS-2o (order ledger).** A deterministic greedy pass over the complete count-oracle table:
  start with S = ∅; at each step accept the brick maximizing L(S ∪ {j}), where
  **L(S) = Σ_j n_j·(c_j − c̄_S)²** (count-weighted SSE about the count-weighted mean; the
  singleton value is defined ≡ 0 exactly). Marginal gains are evaluated by the frozen update
  identity `ΔL(j|S) = (N_S·n_j/(N_S+n_j))·(c_j − c̄_S)²` in IEEE-754 float64, in ascending-
  BRICKID candidate order; ties on ΔL (exact float equality) break by larger |c_j|, then
  smaller BRICKID. BS-2o emits the FULL traversal order and the per-prefix ledger
  `(k, brickid_k, N_k, Var_k, L_k)` for every prefix — **no halt, no threshold input.**
- **BS-5p (planning power → threshold).** Consumes the BS-2o ledger; finds **L_min_plan** = the
  L of the smallest prefix passing the §4 Stage-P rule; **L_plan = 1.2 × L_min_plan** (margin
  frozen). Also requires N_eq = 3·L ≥ 100,000.
- **BS-2s (cut + certified local improvement).** Cuts the BS-2o ledger at the smallest prefix
  with L ≥ L_plan → candidate set S₀. Then a frozen local-improvement pass minimizes brick
  count subject to L ≥ L_plan: repeat until no move applies — (i) remove any brick whose
  removal keeps L ≥ L_plan (candidates scanned in ascending ΔL-at-current-S, ties as above);
  (ii) swap any accepted brick for any unaccepted brick when the swap keeps L ≥ L_plan and
  reduces… (bricks have unit cost, so only removals reduce cost; swaps that keep count equal
  but raise L are applied only if they then enable a removal, evaluated in the frozen scan
  order). Maximum 10,000 moves; the pass is deterministic given the ledger. The receipt reports
  S_final, its L, its brick count, the S₀ baseline, and **verification against a brute-force
  subset oracle on every fixture with ≤ 12 bricks** — including BOTH published gate
  counterexamples (`c=[0.99,0.98,−0.50]` equal counts; `c=[0.04,−0.99,−0.91,0.43,−0.94],
  n=[8,14,33,25,25]`; `c=[−0.12,0.15,−0.67,0.43,−0.78], n=[8,8,18,7,3]`) and randomized
  unequal-count adversarial searches. Stage-P is then RE-RUN once on S_final and must pass
  (acyclic: L_plan is already fixed).
- **Claim discipline (Scope Amendment 1):** this chain is a frozen deterministic procedure with
  certified small-case optimality and receipted achieved-vs-baseline leverage. It is NOT
  claimed to be a global maximizer; the word "optimizer" is retired.
- **Contiguous-BRICKID selection remains banned.**

**Bounded acquisition.** Catalog row payloads (positions) are fetched ONLY for S_final's
bricks, through the receipted route, paced, under the BS-6-style ceiling for catalogs stated in
BS-2c. Image bytes: only after freeze, only S_final, under BS-6.

## §3 Statistics: raw slope, corrected estimand, frozen randomness

With s_i ∈ {+1, −1} the OBSERVED spin sign and c_i as in §1:

- **Raw centred slope:** `β̂ = Σ(s_i − s̄)(c_i − c̄) / Σ(c_i − c̄)²`; analytic check
  `Var(β̂) = Var(s)/((N−1)·Var(c))`. Monopole projected out by construction. The full-sky
  constant `3·D̂` is banned everywhere.
- **Permutation contract:** Monte Carlo, **n_perm = 100,000**, one-sided at Longo's oriented
  sign (East-of-North, V3-pred F-5): `p = (1 + #{β̂_perm ≥ β̂_obs}) / (1 + n_perm)`, ties by
  exact float ≥. **σ_β = np.std(beta_perm, ddof=1)** [gpt56-V3 F6].
- **Randomness, one master contract** [codex-V3 F3/F6]: `root = np.random.SeedSequence(20260824)`;
  `children = root.spawn(1 + n_trials)`. `children[0]` seeds `np.random.default_rng` for the
  real-data permutation stream; permutation k (k = 1…100,000) is the k-th successive
  `rng.permutation(s)` call on that generator — batching or reordering that changes the stream
  is non-compliant and detectable by the BS-7 digest. `children[t]` (t = 1…1,000) seeds
  injection trial t (§4). NumPy version and platform are recorded in every receipt using this
  contract; fixtures pin expected digests.
- **Serialization, canonical** [both V3 F6]: the digest payload is the 100,000 β̂_perm values
  in permutation-index order 0…99,999, as contiguous little-endian IEEE-754 binary64 (`'<f8'`,
  C-order) raw bytes, no header — exactly 800,000 bytes — hashed with SHA-256. Any non-finite
  value fails closed.
- **Attenuation and the decision estimand.** A sign-symmetric classifier with accuracy a gives
  `E[s_obs|c] = (2a−1)·A_L·c` when a is constant; §6's calibration gate decides whether the
  scalar model is admissible. Scalar path: **`Â_L = β̂/(2â−1)`**. Calibrated-profile path
  (fallback, frozen now): with per-bin accuracies â_b on the §6 calibration bins,
  `ŵ = Cov_w(c, (2â_{b(i)}−1)·c) / Var_w(c)` computed on the accepted mask (positions and bin
  labels only, no χ), and **`Â_L = β̂/ŵ`**.
- **Uncertainties, explicit functions** [codex-V3 F5]:
  `σ_ours(a*) = sqrt( σ_β²/(2a*−1)² + ( 2·σ_a·β̂/(2a*−1)² )² )` on the scalar path (the
  fallback path replaces the two derivatives by the frozen per-bin delta-method gradient over
  {â_b}). **Decision bands (§5) use σ_ours(â); the detection floor uses σ_ours(a_LB).** Both
  uses are named where they occur; no other evaluation point is admissible.
  `σ_comb = sqrt(σ_pub² + σ_ours(â)²)`. **Declared assumption:** Cov(β̂, â) is set to zero —
  â comes from the hand-check audit's agreement indicators, β̂'s null variability from
  permutations conditional on the mask; the assumption is declared, not proven, and is listed
  in §7's Testimony obligations for the freeze record.

## §4 Power gate, two stages

**Stage P — planning bound (class P, BS-5p).** Deterministic given the BS-2o ledger and this
text. For a prefix with per-brick eligible counts n_j and centres c_j:
- **Retention transform, integer and per-brick** [gpt56-V3 F4 / codex-V3 F3]:
  `n_ret_j = floor(0.8572 × n_j)` (predecessor BS-3 lower bound 0.8572).
- **Injection trial t:** for each retained object (brick centre c), latent
  `P(s_lat = +1 | c) = (1 + A_L·c)/2` with A_L = 0.0408: draw `B ~ Bernoulli`, map
  `s_lat = 2B − 1`; then flip: draw `U ~ Uniform[0,1)`, and `s_obs = −s_lat` iff `U < (1 − a)`,
  with **a = 0.85** (floor). All draws from `children[t]` in object order (ascending BRICKID,
  then object index within brick).
- **Success:** one-sided p < 0.001 under the §3 contract (its permutation stream seeded from
  `children[t]`'s first spawn, `children[t].spawn(1)[0]`, so trials are independent).
- **PASS rule, exact** [both V3]: n_trials = 1,000; one-sided 95% Clopper–Pearson lower bound
  `Beta⁻¹(0.05; x, 1001−x) ≥ 0.95`, equivalently **x ≥ 962 successes**. The two-sided
  convention is NOT used.
**Output:** L_min_plan (smallest passing prefix's L), L_plan = 1.2 × L_min_plan.

**Stage C — confirmatory gate (class E, BS-5f; after inference, before unblinding).** The same
frozen generator, seeds contract, and x ≥ 962 rule, run on the **sealed actual accepted-
position mask** (acceptance flags + positions only; never a χ sign), with the measured
**a_LB** (scalar path) or **{a_LB_b}** (fallback path) from BS-8f in place of the floor. A
uniform-sphere input, a parent-position input, or any non-mask input is inadmissible. FAIL →
**INCONCLUSIVE-BY-POWER before unblinding; the run halts; no real-sky statistic is formed.**

## §5 Decision regions — V3-pred F-6 restated, applied to Â_L

- **REPRODUCED-LONGO:** permutation p < **0.001** AND sign per §3 AND |Â_L − 0.0408| ≤ 3·σ_comb.
- **REJECTED-AT-LONGO-AMPLITUDE:** permutation p > **0.05** AND (|Â_L| + 3·σ_ours(â)) < **0.0408**.
- **INCONCLUSIVE:** any other numeric outcome — explicitly including 0.001 ≤ p ≤ 0.05 — or any
  triggered INCONCLUSIVE rule elsewhere in this document.
- **INCONCLUSIVE-BY-POWER / INCONCLUSIVE-BY-CALIBRATION:** per §4 Stage C / §6; no run.

**Detection floor (V3-pred F-7, carried):** one-sided floor **3.09·σ_ours(a_LB)** on Â_L,
evaluated at the receipted a_LB (fallback: the frozen per-bin conservative gradient at
{a_LB_b}) and accepted N, printed in the results table; no Â_L below the evaluated floor can be
called REPRODUCED regardless of the band.

## §6 Conduct rules

- **Disclosure.** Nothing derived from any real χ value — no value, no sign, no summary, no
  count of signs — is published, spoken, or written outside the sealed results store before the
  primary lock.
- **No strata in the estimator.** The centred slope needs no tertiles. (The labelling audit's
  internal design bins in **BS-8p** belong to the hand-check protocol, not to any sky
  statistic [codex-V3 F8].)
- **Labelling-accuracy apparatus + the calibration gate** [gpt56-V3 F5]: V3-pred's HC-1H
  measurement and validity rules are carried by quotation at freeze (machine committee +
  sealed-key hand-check; HC-5 `a_LB = â − 1.645·σ_a ≥ 0.85` one-sided with its per-stratum and
  synthetic-error gates; HC-6 power re-evaluation = §4 Stage C). **Additionally, binding:**
  the hand-check sample is stratified over **three calibration bins** in c, fixed at BS-2s as
  the accepted mask's count-weighted c-tertile boundaries (positions only). BS-8f reports per-
  bin â_b, σ_ab, a_LB_b. **Admissibility test for the scalar model, frozen:**
  `max_b |â_b − â| ≤ 0.03` AND every `a_LB_b ≥ 0.85`. Pass → scalar path. Fail the spread test
  only → the frozen calibrated-profile path (§3) with per-bin values. Any `a_LB_b < 0.85` →
  **INCONCLUSIVE-BY-CALIBRATION declared before unblinding; the run halts.**
- **Void rule.** Any change to a §1–§5 parameter after the first real-sky χ read voids the run.
  Amendments before that point require a gated amendment record.
- **Custody.** Receipts with digests; deliverables sha-pinned at gate dispatch by the gate's
  own report and committed to git; self-referential hash chains are not custody;
  describe-vs-compute law throughout.
- **Blind double, common interface.** Both prior implementations retired (codex-V2 measured
  their live disagreement). Two NEW implementations from the amended spec in isolation:
  input = the BS-2c table + the §1 vector + (for BS-2s only) the explicit L_plan value;
  output = JSON: full BS-2o order + ledger, and at BS-2s the final set, L, count. Agreement:
  sequences and integers exact; Var, L, N_eq relative diff ≤ 1e-9; digests of the canonical
  serializations equal. A third print-and-eval comparator; divergence is a STOP, never
  reconciled by editing either implementation toward the other.

## §7 Binding slots

**Class P (freeze-prerequisite):**

| slot | content | status 2026-08-24 |
|---|---|---|
| BS-1 | release choice + catalog provenance | open — Duho + Sep 5 rule |
| BS-1b | photo-z product: paths, columns, join keys, predicate-5 provenance | open |
| BS-2c | count oracle: complete per-brick eligible-count table via server-side counts; query text + completeness proof + ceiling; hash-pinned | open |
| BS-2o | order ledger: full deterministic traversal + per-prefix (N, Var, L); blind-doubled | open — after BS-2c |
| BS-5p | Stage-P receipt: frozen generator + x ≥ 962 rule; L_min_plan; L_plan | open — after BS-2o |
| BS-2s | cut at L_plan + certified local improvement + oracle verification on ≤12-brick fixtures (incl. all three gate counterexamples) + Stage-P re-pass on S_final; blind-doubled | open — after BS-5p |
| BS-3 | instrument carried: weights `83008c1c…`, τ = 4.4006456017494235, antisymmetry identity | receipts in predecessor tree |
| BS-4 | synthetic absolute-sign anchor rerun under this prereg | open |
| BS-7 | randomness/serialization identity: declaration record; β̂_obs; sha256 of the canonical 800,000-byte β̂_perm payload; receipt recomputes from raw indices AND labels; nonzero-monopole asymmetric fixture; p-resolution demonstration on both sides of 0.001; environment record (numpy version, platform) with pinned fixture digests | open |
| BS-8p | HC-1H rules carried by quotation + measurement plan incl. the three calibration bins | open |

**Class E (post-freeze execution gates):**

| slot | content | blocks |
|---|---|---|
| BS-6 | image transport approval: manifest sha, byte ceiling, producer checksum list | first image byte |
| BS-2f | sealed accepted-position mask receipt (positions + acceptance flags + calibration-bin labels only) | Stage C |
| BS-8f | measured â, σ_a, a_LB and per-bin â_b, σ_ab, a_LB_b + HC integrity triggers | Stage C |
| BS-5f | Stage-C confirmatory power receipt | unblinding |

**Testimony obligations at freeze:** the declared zero-covariance assumption (§3); the 1.8 TB
figure's status as an estimate; the Scope Amendment 1 operationalization statement.

## §8 Carried / rebuilt / retired

**Carried:** instrument weights + τ, antisymmetry identity, HC-1H committee + sealed keys +
HC-5/HC-6, transport custody discipline, cutout/inference runners with authorisation gating.
**Rebuilt:** selection (BS-2c/2o/5p/2s chain), statistics §3, power gate §4, this text.
**Retired:** descending-|c| ranking; the V2 symbol Â_c; the word "optimizer" as a claim; both
pre-V4 leverage implementations (provenance only).

## §9 Repair trace and gate plan

gpt56-V3 F1 & codex-V3 F2 → §2 acyclic chain (BS-2o ledger → BS-5p → BS-2s cut).
gpt56-V3 F2 & codex-V3 F4 → BS-2c count oracle (server-side counts; no payload fetch).
gpt56-V3 F3 & codex-V3 F1 → BS-2s certified local improvement + oracle fixtures + Scope
Amendment 1 (no global-max claim).
gpt56-V3 F4 & codex-V3 F3 → §4 integer retention floor, explicit ±1 mapping and flip law,
seed-spawn contract, one-sided CP with x ≥ 962 stated.
gpt56-V3 F5 → §6 calibration bins + admissibility test + frozen fallback estimator +
INCONCLUSIVE-BY-CALIBRATION.
codex-V3 F5 → §3 σ_ours(a*) explicit; bands at â, floor at a_LB; declared covariance
assumption.
gpt56-V3 F6 & codex-V3 F6 → §3 ddof=1, canonical '<f8' 800,000-byte digest, environment
records, fail-closed.
codex-V3 F7 → §2 predicate 6 as executable POWER(...) byte-form.
codex-V3 F8 → §6 BS-8p reference.

Next: re-gate THIS text (gpt-5.6-sol + codex, fresh dispatch, sha-pinned). Then freeze
candidate → Duho's sign-off → 444 + git → class E.
