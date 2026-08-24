# Track B freeze — the observational bounds, verified and frozen (2026-08-24, Tori)

Frozen from the two platoon harvests after coordinator verification. The harvests carry the
full verbatim quotes, locations, citations, and source hashes; this freeze is the bounds table
plus the verification receipt. Nothing here combines, reweighs, or concludes — Track C does
that under gates.

## Verification receipt

Every quote in both harvests was verified against the locally fetched primary sources with
`b_verify_quotes.py` v4, rebuilt to the codex gate's specification after its HOLD
(GATE_TRACKB_VERDICT.md) proved v3's numeric filter could pass corrupted quotes: v4 extracts
ALL numbers boundary-aware (any length, decimals, ranges, σ/percent parts), binds each quote
to the source files its own harvest entry declares, emits a per-quote machine-readable ledger
(`b_verify_ledger.json`, 50 rows), and carries a SELF-TEST in which the gate's own corrupted
counterexample must fail (it does; the genuine quote passes). Result: **50/50 PASS, zero
manual acceptances** — 42 on the primary criterion (all tokens + ≥30% prose shingles), 7
PASS_NUMERIC (≥2 tokens all present in the bound source, prose degraded by table/math
rendering; source spans recorded in the ledger), 1 PASS_PHRASE (no numbers; exact 8-word span
recorded). Binding: 43/50 matched within the source files their harvest entries declare; 7
(agy entries that declare no `sources/` path inline) fell back to the harvest's whole source
directory — flagged `bound_to_declared: false` in the ledger, not hidden. Pins at freeze:
- HARVEST_CMB_BOUNDS.md (gpt2) sha256 beba95a7c8f5093e1a962ccffefa465038a58b6f3c83bfaff8ba6ddbe4662714
- HARVEST_H0_ANISOTROPY.md (agy) sha256 6d97c67900348e5569dd802478b6bb8628640cd45e58b5b6e21c243286883f5a
- b_verify_quotes.py (v4) sha256 f1664ce081392c21a2050249eeb16c6a813adcb0981f60a1518a19105732d81c
- b_verify_ledger.json sha256 8155de4a143266abdc856bc796c7ace3efc86605e50e973b6c96dcb1a4844adb

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
