# PREREGISTRATION DRAFT V3 — LONGO-AMPLITUDE TEST ON A LEVERAGE-CHOSEN FOOTPRINT

> **THIS IS A DRAFT. NOTHING IN IT IS IN FORCE.** It becomes a preregistration only when every
> FREEZE-PREREQUISITE slot (§7 class P) holds a receipt, the text passes adversarial gates, and
> Duho signs the freeze. Class-E slots are execution gates governed by the frozen text and are
> filled during the run; each blocks the stage after it. (This two-class state machine repairs
> the V2 paradox where BS-6 was both required before freeze and forbidden until after it.)

Hwao, 2026-08-24 22:57 KST. V3 repairs the union of blocking findings from
`gates/GATE_GPT56_SUCCESSOR_V2.md` (findings 1–7) and `gates/GATE_CODEX_SUCCESSOR_V2.md`
(findings 1–6), both REFUSED verdicts on V2 (sha `8362166c…`, superseded, kept). Design
authority: `SUCCESSOR_SCOPE_20260821.md`. Predecessor: `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md`
(sha256 `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`, hereafter "V3-pred"),
and its hash-pinned selection receipt `LANA_BS6_PHOTOMETRIC_CUTS_20260814.md`
(sha256 `5ff7f45489b4b21066eeeaeaed10cd6087a0bfaa4c565f51bf934a02d9b6e361`, hereafter "BS6-pred").

## §1 Claim boundary, target, and the machine axis

This tests Longo 2011's published **|A_L| = 0.0408, σ_pub = 0.011** at Longo's published axis.
It does not test A ≈ 0.02, Shamir, BHU, or whether the sky is isotropic. **Fixed-axis.**

**The axis, machine-exact** [gpt56 F6 / codex F4]: the published rendering is galactic
**(l, b) = (52°, 68.5°)** [V3-pred line 124]. The frozen machine value is the ICRS unit vector
obtained from (l, b) = (52.000000°, 68.500000°) by the IAU rotation with NGP at ICRS
(192.85948°, 27.12825°) and l_NCP = 122.93192°:

**n̂_L = (−0.676971771271432, −0.509846551777774, +0.530816083537352)**

Every implementation consumes this vector verbatim; no runtime frame conversion is permitted.
The pairs (α, δ) ≈ (216.9844°, 32.0606°) and (217°, 32°) are display-only. For any sky position,
c = u · n̂_L with u the ICRS unit vector of (ra, dec).

## §2 Population, selection, and the bounded catalog acquisition

**Release.** DR11 if its photo-z product exists at freeze; else DR10.1. Decision date
2026-09-05 (Duho's call either way). Only input paths change with the release.

**Galaxy cuts — the full predecessor Cut-6 predicate set, restated from BS6-pred**
[codex F1; nothing is described as absent this time]:
1. `brick_primary = 1`
2. `maskbits = 0`
3. `type <> 'PSF'` (Tractor source-model classification; BS6-pred's §3(b) disclosure carried)
4. `flux_r > 0`
5. photo-z join with `0 ≤ z_phot_median < 0.15` — **the predecessor's photo-z predicate, carried**;
   the product was `ls_dr10.photo_z`; the successor release's equivalent product, its file paths,
   and join keys are receipted at BS-1b
6. inclination `shape_e1² + shape_e2² < 0.1836734693877551` (⟺ b/a > 0.4; V3-pred I-5)
7. `dered_mag_r < 17.7`
8. `shape_r > 1.5`
No surface-brightness cut exists (documented absence, BS6-pred §3(a)).

**Selection rule** [gpt56 F4 / codex F4 — descending-|c| is retired as non-optimal; the
counterexample (c = 0.99, 0.98, −0.50 → L ratio 22,201×) becomes a mandatory fixture]:
a **deterministic greedy marginal-gain optimizer** over per-brick eligible counts. State:
accepted set S. Step: accept the brick j maximizing L(S ∪ {j}) = N·Var_w(c) (count-weighted,
population divisor N). Ties: larger |c_j| first, then smaller BRICKID. Stop when
L(S) ≥ **L_plan** (§4). Determinism: given identical inputs the accepted sequence is unique.
Mandatory test battery (BS-2p): the counterexample fixture; asymmetric one-sided footprints;
unequal counts; a crossing-boundary fixture where the last accepted brick changes L by < 1e-6.
**Planning approximation, disclosed:** planning uses brick-centre c and eligible-parent counts
(post-photo-z Cut-6). Decision-grade power never uses these (§4 Stage C).
**Contiguous-BRICKID selection remains banned.**

**Bounded acquisition.** The full DR10.1 sweep set is 1,436 files ≈ 1.8 TB (gpt1 inventory sha
`2df3a220…`) and is NEVER fetched whole. Sweep + photo-z tiles are fetched in the optimizer's
acceptance order, counted on arrival, and fetching HALTS at L_plan. Every fetch paced and
receipted under an approval ceiling fixed before the first byte.

## §3 Statistics: raw slope, corrected estimand, frozen permutation contract

With s_i ∈ {+1, −1} the OBSERVED spin sign and c_i as in §1:

- **Raw centred slope:** `β̂ = Σ(s_i − s̄)(c_i − c̄) / Σ(c_i − c̄)²`. Monopole projected out by
  construction. Under `E[s|c] = A_obs·c`, β̂ estimates A_obs on any footprint; analytic check
  `Var(β̂) = Var(s)/((N−1)·Var(c))`. The full-sky constant `3·D̂` is banned everywhere.
- **Attenuation and the decision estimand** [gpt56 F1 / codex F2]: a symmetric classifier with
  accuracy a gives `E[s_obs|c] = (2a−1)·A_L·c`. The decision estimand is
  **`Â_L = β̂ / (2â − 1)`** with â the receipted point estimate (BS-8f). β̂ is never compared
  to 0.0408; Â_L always is. (V2 reused the symbol Â_c for an uncorrected quantity; that symbol
  is retired.)
- **Uncertainties, defined here** [gpt56 F2 / codex F2]: σ_β = permutation SE of β̂;
  **`σ_ours² = σ_β²/(2â−1)² + ( 2·σ_a·β̂/(2â−1)² )²`** (delta method for uncertainty in â);
  **`σ_comb = sqrt(σ_pub² + σ_ours²)`** with σ_pub = 0.011.
- **Permutation contract, frozen** [codex F5]: Monte Carlo permutation test (not exhaustive),
  **n_perm = 100,000** (the predecessor's value). p is plus-one corrected, one-sided at Longo's
  oriented sign (East-of-North winding, V3-pred F-5):
  `p = (1 + #{β̂_perm ≥ β̂_obs}) / (1 + n_perm)`, ties counted by exact float ≥.
  RNG: numpy `default_rng(20260824)`; permutation k uses the generator's k-th draw; batching
  must not change the stream (BS-7 verifies by digest). Resolution: attainable p ranges from
  9.9999e-6 to 1; the p < 0.001 threshold is reachable with margin (BS-7 must demonstrate
  fixtures on BOTH sides of 0.001 — a vacuous-resolution harness cannot pass).

## §4 Power gate, two stages [gpt56 F3 / codex F3 — the L_min cycle is dissolved]

**Stage P — planning bound (class P, BS-5p, before freeze).** Deterministic and independently
rederivable. Inputs: eligible-parent per-brick counts and centres (§2), conservative retention
lower bound **0.8572** (predecessor BS-3 receipt, carried), floor **a = 0.85** (V3-pred F-7
minima). Injection generator, frozen: latent `s ~ Bernoulli((1 + A_L·c)/2)` with A_L = 0.0408
at n̂_L, then symmetric flip with probability (1 − a). **n_trials = 1,000** injected skies;
success = one-sided p < 0.001 under the §3 contract. **PASS rule: Clopper–Pearson 95% lower
confidence bound on the success fraction ≥ 0.95** (point estimates do not pass; one lucky sky
cannot claim power 1.0). Output: **L_min_plan** = the smallest optimizer prefix passing this
rule; **L_plan = 1.2 × L_min_plan** (margin frozen at 1.2). Floor: N_eq = 3·L ≥ 100,000 must
also hold.

**Stage C — confirmatory gate (class E, BS-5f, after inference, before unblinding).** The SAME
frozen algorithm, generator, seeds, and PASS rule, run on the **sealed actual accepted-position
mask** (positions of objects the instrument accepted — the mask uses acceptance flags and
positions only, never a χ sign) with the **measured a_LB** from BS-8f in place of the floor.
A uniform-sphere input, a parent-position input, or any non-mask input is inadmissible. FAIL →
**INCONCLUSIVE-BY-POWER declared before unblinding; the run halts; no real-sky statistic is
ever formed.**

## §5 Decision regions — V3-pred F-6 restated, applied to Â_L

- **REPRODUCED-LONGO:** permutation p < **0.001** AND sign per §3 AND |Â_L − 0.0408| ≤ 3·σ_comb.
- **REJECTED-AT-LONGO-AMPLITUDE:** permutation p > **0.05** AND (|Â_L| + 3·σ_ours) < **0.0408**.
- **INCONCLUSIVE:** any other numeric outcome — explicitly including 0.001 ≤ p ≤ 0.05 — or any
  triggered INCONCLUSIVE rule elsewhere in this document.
- **INCONCLUSIVE-BY-POWER:** per §4 Stage C; no run.

**Detection floor (V3-pred F-7, carried):** one-sided floor **3.09·σ_ours** on Â_L, evaluated
at the receipted a_LB and accepted N, printed in the results table; no Â_L below the evaluated
floor can be called REPRODUCED regardless of the band.

## §6 Conduct rules

- **Disclosure.** Nothing derived from any real χ value — no value, no sign, no summary, no
  count of signs — is published, spoken, or written outside the sealed results store before the
  primary lock.
- **No strata in the estimator.** The centred slope needs no tertiles; the one-shot strata
  hazard is retired by design. (The labelling audit's internal strata in BS-8 belong to the
  hand-check protocol, not to any sky statistic.)
- **Labelling-accuracy apparatus** [gpt56 F5]: V3-pred's HC-1H measurement and validity rules
  are carried by quotation at freeze — machine committee + sealed-key hand-check; **HC-5:
  a_LB = â − 1.645·σ_a ≥ 0.85 one-sided, with the per-stratum and synthetic-error gates; HC-6:
  power re-evaluated at the measured a_LB** (= §4 Stage C). BS-8p freezes the rules and the
  measurement plan; BS-8f holds â, σ_a, a_LB and all integrity triggers. §3's correction and
  §4 Stage C consume BS-8f, and the §5 floor is evaluated at a_LB.
- **Void rule.** Any change to a §1–§5 parameter after the first real-sky χ read voids the run.
  Amendments before that point require a gated amendment record.
- **Custody.** Every acquisition receipted with digests; deliverables sha-pinned at gate
  dispatch by the gate's own report and committed to git; self-referential hash chains are not
  custody; describe-vs-compute law throughout.
- **Blind double, common interface** [gpt56 F6 / codex F4]: BOTH prior implementations
  (`_successor_instrument_20260823/selection_leverage.py`; `gpt2/calc_leverage.py`) are
  **retired as interface-non-conforming** (kept for provenance; codex measured their live
  disagreement: 78-brick symmetric difference, Var relative diff 4.1e-4). Two NEW
  implementations are built from the amended spec in isolation, to one contract —
  input: brick table `{brickid, ra, dec, n_eligible}` + the §1 vector verbatim;
  output: ordered accepted brickid sequence, N, Var(c), L at halt, emitted as JSON.
  Agreement: brick sequence and every integer **exact**; Var(c), L, N_eq **relative diff
  ≤ 1e-9**. A third print-and-eval comparator reads both outputs; any excess divergence is a
  STOP recorded as a finding — neither implementation is ever edited toward the other.

## §7 Binding slots — two classes

**Class P (freeze-prerequisite: every one holds a receipt before the text can be frozen):**

| slot | content | status 2026-08-24 |
|---|---|---|
| BS-1 | release choice + catalog provenance | open — Duho + Sep 5 rule |
| BS-1b | photo-z product for the release: file paths, columns, join keys, cut predicate №5 provenance | open (product absent from sweep dirs, 0/2,872) |
| BS-2p | planning selection receipt: optimizer implementation pair per §6, test battery incl. the counterexample + crossing fixtures, accepted sequence, N, Var, L — blind-doubled | open — implementations to be rebuilt |
| BS-3 | instrument carried: weights `83008c1c…`, τ = 4.4006456017494235, antisymmetry identity | receipts exist in predecessor tree |
| BS-4 | synthetic absolute-sign anchor rerun under this prereg | open |
| BS-5p | Stage-P power receipt: generator, seeds, n_trials, CP bound, L_min_plan, L_plan | open — after BS-2p |
| BS-7 | permutation/behavioural identity [gpt56 F7]: on fixed-seed fixtures (incl. nonzero-monopole asymmetric footprint), the harness emits (a) the declaration `{statistic: centred_slope, null: permutation, sidedness: one_sided_greater_at_longo_sign, n_perm: 100000}`, (b) β̂_obs and the sha256 of the canonical float64 serialization of the FULL β̂_perm vector; the receipt script recomputes both from raw arrays with the frozen formula and compares value, digest, and p; plus the two-sided-of-0.001 resolution demonstration | open |
| BS-8p | HC-1H rules carried by quotation + measurement plan (committee, sealed keys, HC-5/HC-6 text) | open |

**Class E (post-freeze execution gates; each blocks the stage after it):**

| slot | content | blocks |
|---|---|---|
| BS-6 | transport approval: manifest sha, byte ceiling, producer checksum list | first image byte |
| BS-2f | final accepted-position mask receipt (sealed; positions + acceptance flags only) | Stage C |
| BS-8f | measured â, σ_a, a_LB + HC integrity triggers | Stage C |
| BS-5f | Stage-C confirmatory power receipt | unblinding |

## §8 Carried untouched / rebuilt / retired

**Carried:** instrument weights + τ, antisymmetry identity + receipts, HC-1H committee and
sealed-key protocol with HC-5/HC-6, transport with per-brick digest custody, cutout/inference
runners with authorisation gating, receipts discipline. **Rebuilt:** parent selection (greedy
optimizer), footprint receipt, statistics §3, power gate §4, this preregistration. **Retired:**
descending-|c| ranking; both prior leverage implementations (interface-non-conforming); the V2
symbol Â_c.

## §9 Gate plan and repair trace

V2 → V3 trace: gpt56 F1 & codex F2 → §3 (β̂/Â_L split, σ definitions); gpt56 F2 & codex F5 →
§3 permutation contract (n_perm=100,000, seeds, plus-one, resolution) + §4 CP pass rule;
gpt56 F3 & codex F3 & codex F6 → §4 two stages + §7 two classes; gpt56 F4 & codex F4 →
§2 optimizer + §6 interface rebuild; gpt56 F5 → §6 HC carry + BS-8p/f; gpt56 F6 → §1 machine
vector; gpt56 F7 → BS-7 digest comparison; codex F1 → §2 full Cut-6 restatement with photo-z
predicate carried.

Next: re-gate THIS text (gpt-5.6-sol + codex, fresh dispatch, sha-pinned). Then freeze
candidate → Duho's sign-off → 444 + git. Class-E execution begins only after that.
