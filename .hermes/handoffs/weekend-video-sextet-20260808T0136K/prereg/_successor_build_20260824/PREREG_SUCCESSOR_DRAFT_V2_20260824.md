# PREREGISTRATION DRAFT V2 — LONGO-AMPLITUDE TEST ON A LEVERAGE-CHOSEN FOOTPRINT

> **THIS IS A DRAFT. NOTHING IN IT IS IN FORCE.** It becomes a preregistration only when its
> text passes adversarial gates, every binding slot holds a receipt, and Duho signs the freeze.

Hwao, 2026-08-24 23:14 KST. V2 repairs all eight findings of `agy/REVIEW_AGY_20260824.md`
(REPAIR-FIRST) against V1 (superseded, kept). Design authority: `SUCCESSOR_SCOPE_20260821.md`.
Predecessor carried by quotation from `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md`
(sha256 `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`), every quotation
below re-verified against that file this evening.

## §1 Claim boundary and target

This tests Longo 2011's published **|A_L| = 0.0408, σ_pub = 0.011** at Longo's published axis
**n̂_L : (l, b) = (52°, 68.5°) ≡ (α, δ) = (217°, 32°)** [V3 line 124, by quotation]. It does not
test A ≈ 0.02, Shamir, BHU, or whether the sky is isotropic. A null rejects only the published
amplitude at the published axis under the preregistered rule. **Fixed-axis.** A free-axis scan
is a different study and is not authorised by this document.

## §2 Population, selection, and the bounded catalog acquisition

**Release.** DR11 if its photo-z catalog exists at freeze; else DR10.1. Decision date
2026-09-05 (Duho's call either way). The design is release-agnostic; only input paths change.

**Galaxy cuts, two provenances kept distinct** [agy F4]:
- **Carried from V3 by quotation:** Cut-6 as frozen there, incl. `flux_r > 0` and
  `dered_mag_r < 17.7`. V3 contains no photo-z cut; none is attributed to it.
- **Successor-defined:** a photo-z selection cut on the release's photo-z product. Its column,
  value, and product provenance are fixed at freeze in BS-1b, quoted from the predecessor
  harvest's own frozen selection document (not from V3), or redefined with justification if the
  release's photo-z schema differs.

**Selection rule (geometry first, counts second).** Per-brick |cosθ| about n̂_L is pure
geometry, computable today for every brick. Bricks are ranked by |cosθ| DESCENDING and accepted
in that order. **Contiguous-BRICKID selection is banned.** The stopping rule is written on
leverage, not count: stop when accepted-sample `L = N·Var(cosθ) ≥ L_min` (BS-5 sets L_min from
the power gate with margin; floor: N_eq = 3L ≥ 100,000). L is computable from positions alone —
no χ, no image byte, is involved in selection at any point.

**Bounded acquisition (the 1.8 TB trap, named).** The full DR10.1 sweep set is 1,436 files
averaging ~1.24 GB (measured 2026-08-24; gpt1 inventory sha
`2df3a22065344a3378e069b022d316f39164ddc908f73d0fb4cfcf40323e0550`) ≈ 1.8 TB and is NEVER
fetched whole. Sweep tiles are fetched in descending order of their maximum |cosθ| overlap;
each tile's Cut-6 galaxies are counted per brick on arrival; accumulated leverage is
recomputed; fetching HALTS at L_min with margin. Every fetch is paced and receipted (URL,
sha256, bytes) under an approval ceiling fixed before the first byte.

## §3 Primary statistic

On the accepted sample, with s_i ∈ {+1, −1} the spin sign and c_i = cosθ_i:

- **Estimator:** `Â_c = Σ(s_i − s̄)(c_i − c̄) / Σ(c_i − c̄)²` — the monopole is projected out
  by construction.
- **Normalisation is internal to the estimator** [agy F3]: under the preregistered sign model
  `E[s_i | c_i] = A·c_i`, `Cov(s,c) = A·Var(c)`, so the centred slope estimates **A directly on
  any footprint**; no footprint constant appears anywhere. `E[cos²θ]` appears nowhere in this
  document. The full-sky constant `3·D̂` (+42.76% silent inflation on the predecessor's
  footprint) is banned from every formula and every receipt, including any covariance-form
  secondary.
- **Null and variance** [agy F1]: exact permutation of s over fixed positions is authoritative.
  Analytic check: **`Var(Â_c) = Var(s) / ((N−1)·Var(c))`**. (V1's `Var(s)·Var(c)/(N−1)` was the
  covariance-form D̂ variance, wrong for the slope by a factor Var(c)² — the error would have
  understated σ and faked power. Repaired per review.)
- **Sidedness, declared once, here: one-sided at Longo's oriented sign** under East-of-North
  winding (V3 F-5 convention), with the mandatory synthetic absolute-sign anchor run before any
  real image (**BS-4 receipt** [agy F8]). The harness must pass BS-7's behavioural identity
  (below), not merely restate this sentence.

## §4 Power gate (the repair that would have caught the predecessor)

Named inputs, all receipted at BS-5: `N_accept`; **accepted-sample `Var(cosθ)` measured on
actual accepted positions** (a uniform-sphere value is not an admissible input); labelling
floor a = 0.85 (V3 F-7 minima, carried); sidedness per §3. Procedure: inject A = 0.0408 at n̂_L
into permutation nulls on the REAL accepted positions, diluted by the floor. Requirement
[agy F5]: **probability ≥ 0.95 that the one-sided permutation p falls below 0.001** (the §5
REPRODUCED threshold — power is evaluated at the decision threshold, at no other α). Fails →
**INCONCLUSIVE-BY-POWER declared before unblinding** and no real-sky statistic is ever formed.

## §5 Decision regions — V3 F-6 restated in full, verbatim thresholds [agy F2]

- **REPRODUCED-LONGO:** permutation p < **0.001** AND sign per §3 AND |Â_c − 0.0408| ≤ 3·σ_comb.
- **REJECTED-AT-LONGO-AMPLITUDE:** permutation p > **0.05** AND (|Â_c| + 3·σ_ours) < **0.0408**.
- **INCONCLUSIVE:** any other numeric outcome — explicitly including the 0.001 ≤ p ≤ 0.05 gap
  — or any triggered INCONCLUSIVE rule elsewhere in this document.
- **INCONCLUSIVE-BY-POWER:** declared before unblinding per §4; no run.

**Detection floor (V3 F-7, carried):** one-sided floor **3.09·σ_ours** on Â_c, evaluated at
this run's accepted N and floor a, printed in the results table; no Â_c below the evaluated
floor can be called REPRODUCED regardless of the band.

## §6 Conduct rules

- **Disclosure.** Nothing derived from any real χ value — no value, no sign, no summary, no
  count of signs — is published, spoken, or written outside the sealed results store before the
  primary lock. (The predecessor's breach is why this sentence exists.)
- **No strata.** The centred estimator needs no tertiles; the one-shot strata hazard is retired
  by design.
- **Void rule (V3 F-9 principle, carried).** Any change to a §2–§5 parameter after the first
  real-sky χ read voids the run. Amendments before that point require a gated amendment record.
- **Custody.** Every acquisition receipted with digests; deliverables sha-pinned at gate
  dispatch by the gate's own report (external witness) and committed to git; self-referential
  hash chains are not custody. Records follow the describe-vs-compute law.
- **Blind double, with a numeric agreement criterion** [agy F6]: the two implementations
  (Hwao's `_successor_instrument_20260823/`; gpt2's `gpt2/calc_leverage.py`, spec-only,
  fixtures passed 2026-08-24) must agree on the real catalog input: accepted brick SET and
  every integer count **exactly**; `Var(cosθ)`, `L`, `N_eq` to **relative difference ≤ 1e-9**.
  A third print-and-eval comparator script reads both outputs and prints the differences; any
  excess divergence is a STOP recorded as a finding, never reconciled by editing either
  implementation to match the other.

## §7 Binding slots

| slot | content | status 2026-08-24 |
|---|---|---|
| BS-1 | release choice + catalog provenance (paths, versions) | open — Duho + Sep 5 rule |
| BS-1b | photo-z product location, column, cut value + provenance quotation + fetch plan under ceiling | open (product absent from sweep dirs — 0/2,872) |
| BS-2 | selection receipt: brick list, per-brick cosθ, accepted N, Var(cosθ), L — blind-doubled per §6 | pipeline built; awaits catalogs |
| BS-3 | instrument carried: weights `83008c1c…`, τ = 4.4006456017494235, antisymmetry identity | receipts exist in predecessor tree |
| BS-4 | synthetic absolute-sign anchor rerun under this prereg (referenced by §3) | open |
| BS-5 | power-gate receipt (four named inputs, §4) + L_min derivation | open — after BS-2 |
| BS-6 | transport approval: manifest sha, byte ceiling, producer checksum list per release | open — AFTER freeze only |
| BS-7 | sidedness behavioural identity [agy F7]: on a fixed-seed fixture with injected A > 0, the harness (a) emits the machine-readable declaration `{statistic: centred_slope, null: permutation, sidedness: one_sided_greater_at_longo_sign}` and (b) reports p equal to `(1 + #{Â_perm ≥ Â_obs}) / (1 + n_perm)`, recomputed independently by the receipt script on the same fixture | open |

## §8 Carried untouched / rebuilt

**Carried:** instrument weights + τ, antisymmetry identity + receipts, HC-1H committee and
sealed-key protocol, transport with per-brick digest custody, cutout/inference runners with
authorisation gating, receipts discipline. **Rebuilt:** parent selection, footprint receipt,
F-slots as above, power gate, this preregistration.

## §9 Gate plan

1. ~~agy independent-family review~~ — done, REPAIR-FIRST, all eight findings repaired in this
   V2 (traceability: F1→§3 variance; F2→§5 restated; F3→§3 normalisation; F4→§2 cut
   provenances; F5→§4 α named; F6→§6 tolerance; F7→BS-7 behavioural; F8→§3 slot ref).
2. Formal adversarial gates on THIS text: gpt-5.6-sol (config default) + codex (cross-family);
   kimi wallet in reserve for a third family if the two split.
3. Freeze candidate → sha pin by the gate's own report → **Duho's sign-off** → 444 + git.
4. Only then: BS-6 and the polar image campaign (3 streams from day one).
