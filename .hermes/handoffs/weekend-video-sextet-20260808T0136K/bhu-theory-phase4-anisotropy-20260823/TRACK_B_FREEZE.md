# Track B freeze — the observational bounds, verified and frozen (2026-08-24, Tori)

Frozen from the two platoon harvests after coordinator verification. The harvests carry the
full verbatim quotes, locations, citations, and source hashes; this freeze is the bounds table
plus the verification receipt. Nothing here combines, reweighs, or concludes — Track C does
that under gates.

## Verification receipt

Verifier `b_verify_quotes.py` **v5**, rebuilt twice under codex gate pressure (HOLD →
HOLD-residue → this version). What v5 proves for every quote:

- **Ordered numeric relations**, not token sets: each quote's numbers (with signs and
  range/exponent hyphens preserved as tokens) must appear IN ORDER within a bounded window of
  one bound source. The gate's three corruption classes — absent fragments, range order swaps
  ("5–10"→"10–5"), exponent sign flips (10⁻⁵→10⁺⁵) — are embedded as mandatory self-tests and
  all FAIL.
- **Per-entry source binding, zero fallbacks**: entries that declare `sources/` paths bind to
  them; agy's entries (which declare none — its tarballs unpacked to one root) bind through
  `b_binding_map.json`, an explicit per-entry map with the identification evidence recorded
  (title or distinctive-content grep per file). A quote with no resolvable binding FAILS.
- **Reproducible span ledger** (`b_verify_ledger.json`, 50 rows): full quote text + sha256,
  bound source path + sha256, the ordered expression sequence, and the matched span (offsets +
  excerpt). Composite table-cell quotes verify per segment (each segment ordered-matched in the
  same file); attribution tails embedded in the harvest's quote lines ("— Abstract, PDF
  p. 1.[2]") are stripped before extraction, since their digits are locations, not values.

**Result: 50/50 PASS, zero manual acceptances, zero directory fallbacks.**

Pins at freeze (v5):
- HARVEST_CMB_BOUNDS.md (gpt2) sha256 beba95a7c8f5093e1a962ccffefa465038a58b6f3c83bfaff8ba6ddbe4662714
- HARVEST_H0_ANISOTROPY.md (agy) sha256 6d97c67900348e5569dd802478b6bb8628640cd45e58b5b6e21c243286883f5a
- b_verify_quotes.py (v5) sha256 2d8b1eca007d69b4724614fdecdd6b77a167151f5c6e8b30f12dad9babfb68cc
- b_verify_ledger.json sha256 c049a98a69db800a583724778e59c40008eeb6e64f45a579fa3285931bcedb85
- b_binding_map.json sha256 74e53f0c706ddf2c23856d17ffc090ea67d57ed7127cd0174374ef01550687ae

## B2 — CMB dipole (the discriminant-adjacent set)

| # | bound / claim (paper's own framing) | value | source |
|---|---|---|---|
| B2.1 | Planck solar dipole amplitude | 3362.08 ± 0.99 µK; v = 369.82 ± 0.11 km/s | Planck 2018 I (A&A 641, A1) |
| B2.2 | First direct intrinsic-dipole bound | \|Δ1,int\| < 3.6–3.7 mK (95% CI) | Ferreira & Quartin, PRL 127, 101301 |
| B2.3 | Velocity from aberration/modulation | 384 ± 78 (stat) ± 115 (syst) km/s | Planck 2013 XXVII |
| B2.4 | Non-kinematic contribution allowance | up to ~40% without contradicting Planck | Schwarz+ 2016 (CQG 33, 184001) |
| B2.5 | CatWISE quasar dipole excess | 2× expected; 4.9σ | Secrest+ 2021 (ApJL 908, L51) |
| B2.6 | Joint radio+quasar excess | 5.1σ joint (2.6σ + 4.4σ) | Secrest+ 2022 (ApJL 937, L31) |
| B2.7 | Bayesian CatWISE reanalysis | 2.46 ± 0.18 × kinematic; 5.7σ | Dam+ 2023 (MNRAS 525, 231) |
| B2.8 | Radio counts overdispersion excess | 3.67 ± 0.49 ×; 5.4σ | Böhme+ 2025 (PRL 135, 201001) |
| B2.9 | COUNTER: VLASS+RACS consistent | 331/399 km/s ≈ CMB velocity | Darling 2022 (ApJL 931, L14) |
| B2.10 | COUNTER: mask/multipole reassessment | ~2σ; consistency not ruled out | Abghari+ 2024 (JCAP 11, 067) |
| B2.11 | COUNTER: clustering/mask reassessment | 3.27–3.63σ revised | Bashir+ 2026 (ApJ 1003, 162) |

Both sides frozen; the dipole-excess dispute is unresolved in the literature and stays that way
in this record.

## B3 — large-angle anomalies (what a near-threshold cap would have to hide in)

| # | bound / claim | value | source |
|---|---|---|---|
| B3.1 | Low-ℓ power deficit | 5–10% at ℓ ≲ 40; 2.5–3σ | Planck 2013 XV |
| B3.2 | Low large-angle variance LTP | ~1% (0.5–0.8% with 2016 mask) | Planck 2018 VII |
| B3.3 | Optimized variance estimator LTP | ≤0.33% (PR3), ≤1.76% (PR4); T+P: no sim as low as data; finite-ensemble floor stated | Billi+ 2024 (JCAP 07, 080) |
| B3.4 | Cut-sky S½ missing correlations | p < 0.24% robust; HFI-100: 0.03% | Copi+ 2015 (MNRAS 451, 2978) |
| B3.5 | COUNTER: quadrupole not anomalous | ΛCDM at cumulative 0.824; full-sky C(θ) within 95% | Bennett+ 2011 (WMAP7) |
| B3.6 | COUNTER: Bayesian odds | "1 in 10 or 1 in 20"; "no convincing evidence" | Efstathiou 2003 |
| B3.7 | COUNTER: estimator dependence | full-sky p = 8% vs masked 0.065%; "unconvincing evidence" | Efstathiou, Ma & Hanson 2010 |

The significance of the large-angle anomalies is CONTESTED in print; the freeze carries both
positions with equal custody, per the brief's B3 instruction.

## B1 — expansion-rate anisotropy (REFERENCE TIER ONLY, per gated Track A)

Track A (gated PASS) establishes the exact null for wholly-interior light paths, so these
bounds cannot discriminate the σ=1/3 interior model; frozen as reference context. Entries per
agy's harvest: Migkas+ 2020 (13±4%, 3.59σ), Migkas+ 2021 (13±3%, 4.3σ), Dam+ 2023 (cross-ref
B2.7), Hu+ 2024 Pantheon+ region fits (4.48σ; H0,max 74.26±0.39), and the remaining harvest
entries as listed in HARVEST_H0_ANISOTROPY.md. If a future track models boundary-crossing or
boundary-influenced expansion probes (uncalibrated today), this tier re-opens.

## What Track C may and may not do with this table

- MAY: confront P2/P3 (sufficient hiding condition; cap geometry) with B3's contested
  anomalies; judge whether a single-cap morphology is consistent with either side of B3.
- MAY: use B2.2's intrinsic-dipole bound where the model makes a photon-channel statement.
- MAY NOT: resolve the B2 dipole-excess dispute or the B3 significance dispute — those are
  literature disputes, not ours to adjudicate.
- MAY NOT: use B1 as a discriminant (gated Track A scope).
