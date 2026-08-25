# PREREGISTRATION DRAFT V1 — LONGO-AMPLITUDE TEST ON A LEVERAGE-CHOSEN FOOTPRINT

> **THIS IS A DRAFT. NOTHING IN IT IS IN FORCE.** It becomes a preregistration only when its
> text passes adversarial gates, every binding slot holds a receipt, and Duho signs the freeze.

Hwao, 2026-08-24 22:47 KST. Supersedes the same-day skeleton (kept). Design authority:
`SUCCESSOR_SCOPE_20260821.md`. Predecessor carried by quotation from
`PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md`
(sha256 `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`).

## §1 Claim boundary and target

This tests Longo 2011's published **|A_L| = 0.0408, σ_pub = 0.011** at Longo's published axis
**n̂_L : (l, b) = (52°, 68.5°) ≡ (α, δ) = (217°, 32°)** [V3 line 124, by quotation]. It does not
test A ≈ 0.02, Shamir, BHU, or whether the sky is isotropic. A null rejects only the published
amplitude at the published axis under the preregistered rule. **Fixed-axis.** A free-axis scan
is a different study and is not authorised by this document.

## §2 Population, selection, and the bounded catalog acquisition

**Release.** DR11 if its photo-z catalog exists at freeze; else DR10.1. Decision date
2026-09-05 (Duho's call either way). The design below is release-agnostic; only input paths
change.

**Galaxy cuts.** Cut-6 exactly as frozen in V3, carried by quotation at freeze (incl.
`flux_r > 0`, `dered_mag_r < 17.7`, and the frozen z cut on `z_phot_median`).

**Selection rule (geometry first, counts second).** Per-brick |cosθ| about n̂_L is pure
geometry, computable today for every brick. Bricks are ranked by |cosθ| DESCENDING and accepted
in that order. **Contiguous-BRICKID selection is banned.** The stopping rule is written on
leverage, not count: stop when accepted-sample `L = N·Var(cosθ) ≥ L_min` (BS-5 sets L_min from
the power gate with margin; floor: N_eq = 3L ≥ 100,000). L is computable from positions alone —
no χ, no image byte, is involved in selection at any point.

**Bounded acquisition (the 1.8 TB trap, named).** The full DR10.1 sweep set is 1,436 files
averaging ~1.24 GB (measured 2026-08-24, gpt1 inventory sha
`2df3a22065344a3378e069b022d316f39164ddc908f73d0fb4cfcf40323e0550`) ≈ 1.8 TB. The full set is
therefore NEVER fetched. Sweep tiles are fetched in descending order of their maximum |cosθ|
overlap, each tile's Cut-6 galaxies are counted per brick as it arrives, accumulated leverage is
recomputed, and fetching HALTS at L_min with margin. Expected footprint: the polar tiles only.
Every fetch is paced and receipted (URL, sha256, bytes) under an approval ceiling fixed before
the first byte.

**Open item (BS-1b).** The photo-z product does NOT live in the sweep directories (0 of 2,872
inventoried files match). Its DR10.1 path must be located and receipted before the acquisition
plan is frozen; if per-object photo-z requires a separate paced fetch, it falls under the same
ceiling discipline.

## §3 Primary statistic

On the accepted sample, with s_i ∈ {+1, −1} the spin sign and c_i = cosθ_i:

- **Estimator (monopole projected out by construction):**
  `Â_c = Σ(s_i − s̄)(c_i − c̄) / Σ(c_i − c̄)²`
- **Normalisation is a procedure, never a constant:** the amplitude comparison to A_L uses
  `E[cos²θ]` evaluated on the accepted sample. The constant `3·D̂` (full-sky special case;
  +42.76% silent inflation on the predecessor's footprint) is banned from every formula and
  every receipt.
- **Null and variance:** exact permutation of s over fixed positions; analytic check
  `Var(Â_c) = Var(s)·Var(c)/(N−1)`; the permutation is authoritative.
- **Sidedness, declared once, here: one-sided at Longo's oriented sign** (East-of-North
  winding, F-5). The harness must implement exactly this sentence; BS-7 is the identity receipt
  between this line and the harness's self-reported test. The predecessor's two-sided
  `sim_power.py` is not carried.

## §4 Power gate (the repair that would have caught the predecessor)

Named inputs, all receipted at BS-5: `N_accept`; **accepted-sample `Var(cosθ)` measured on
actual accepted positions** (a uniform-sphere value is not an admissible input); labelling
floor a = 0.85 (F-7, carried); sidedness per §3. Procedure: simulated injection of A = 0.0408
at n̂_L into permutation nulls on the REAL accepted positions, diluted by the floor; requirement
**power ≥ 0.95**. Fails → **INCONCLUSIVE-BY-POWER declared before unblinding** and no real-sky
statistic is ever formed — the predecessor proved this off-ramp functions.

## §5 Decision regions (exhaustive, mutually exclusive; carried in form from V3 F-6)

- **REPRODUCED-LONGO:** permutation p < 0.001 AND Longo's sign per §3 AND
  |Â_c − 0.0408| ≤ 3·σ_comb.
- **EXCLUDED-AT-AMPLITUDE:** p ≥ 0.001 region per V3's exclusion arithmetic, evaluated at the
  §4 power (only reachable if the gate passed).
- **INCONCLUSIVE-BY-POWER:** declared pre-unblinding per §4.
No third real-sky path exists.

## §6 Conduct rules

- **Disclosure.** Nothing derived from any real χ value — no value, no sign, no summary, no
  count of signs — is published, spoken, or written outside the sealed results store before the
  primary lock. (The predecessor's §4/condition-2 breach is the reason this sentence exists.)
- **No strata.** The centred estimator needs no tertiles; the predecessor's one-shot strata
  hazard is retired by design, not by discipline.
- **Void rule (F-9 carried).** Any change to a §2–§5 parameter after the first real-sky χ read
  voids the run. Amendments before that point require a gated amendment record.
- **Custody.** Every acquisition receipted with digests; deliverables sha-pinned at gate
  dispatch by the gate's own report (external witness) and committed to git; self-referential
  hash chains are not custody. Records follow the describe-vs-compute law: claims are
  print-and-eval commands; author statements sit under a Testimony heading; no universal
  quantifiers.
- **Blind double.** Selection numbers (accepted N, Var(cosθ), L) are produced by two
  implementations built from spec in isolation (Hwao's `_successor_instrument_20260823/`;
  gpt2's `gpt2/calc_leverage.py`, fixtures passed 2026-08-24). Freeze requires their agreement
  on the real catalog input; disagreement is a stop, not a reconciliation exercise.

## §7 Binding slots

| slot | content | status 2026-08-24 |
|---|---|---|
| BS-1 | release choice + catalog provenance (paths, versions) | open — Duho + Sep 5 rule |
| BS-1b | photo-z product location + fetch plan under ceiling | open — located next session |
| BS-2 | selection receipt: brick list, per-brick cosθ, accepted N, Var(cosθ), L — blind-doubled | pipeline built; awaits catalogs |
| BS-3 | instrument carried: weights `83008c1c…`, τ = 4.4006456017494235, antisymmetry identity | receipts exist in predecessor tree |
| BS-4 | synthetic absolute-sign anchor rerun under this prereg | open |
| BS-5 | power-gate receipt (four named inputs) + L_min derivation | open — after BS-2 |
| BS-6 | transport approval: manifest sha, byte ceiling, producer checksum list per release | open — AFTER freeze only |
| BS-7 | sidedness identity: harness self-report == §3 sentence | open |

## §8 Carried untouched / rebuilt

**Carried:** instrument weights + τ, antisymmetry identity + receipts, HC-1H committee and
sealed-key protocol, transport with per-brick digest custody, cutout/inference runners with
authorisation gating, receipts discipline. **Rebuilt:** parent selection, footprint receipt,
F-1..F-7 as above, power gate, this preregistration.

## §9 Gate plan

1. agy (independent family) reviews this draft against the scope note's seven requirements.
2. Repair; then formal adversarial gates: gpt-5.6-sol (config default) + codex (cross-family).
   kimi wallet in reserve for a third family if a gate splits.
3. Freeze candidate → sha pin by the gate's own report → **Duho's sign-off** → 444 + git.
4. Only then: BS-6 and the polar image campaign (3 streams from day one).
