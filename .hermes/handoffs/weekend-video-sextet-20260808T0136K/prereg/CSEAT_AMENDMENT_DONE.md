CSEAT_AMENDMENT_COMPLETE

# ACQ science seat (claude-seat) — pre-K-8 amendment draft delivered

**2026-08-20 18:57 KST.** Deliverable: `AMENDMENT_PREK8_20260820.md` · SHA-256
`e832a341f4c9c3937b8fcafc42d6dd7c15ca1e6ea32e5c9ae21856ab50e1380c` (562 lines).

**Status: DRAFT FOR KUN'S GATE, then Duho's freeze. Nothing frozen, accepted, published,
committed, or pushed by this lane.**

## The three items, decided

- **AM-A SIGN CONVENTION — frozen direct.** `χ > 0` ⟺ BS-3 generator `truth_sign = +1` ⟺
  counter-clockwise (↺) apparent winding East-of-North ⟺ Longo-"Left"; Longo's published
  `A ≡ (R−L)/(R+L) = −0.0408` reproduces in our (L−R) polarity as `Â(n̂_L) = +0.0408`, so
  REPRODUCED-LONGO requires `Â_c` **positive**. The rehearsal (1,896/2,000 = 94.800% direct,
  104 inverted, 0 exact zeros) **confirmed** the polarity BS-5 §3 already froze — it did not choose
  it. **No post-crossing sign flip, ever:** the convention is a property of the frozen weights and
  input contract, not of the sky, so no real-data observation can license a flip. An apparent
  inversion is a bug in one of three enumerated defect classes (raster parity / input contract /
  estimator plumbing), all detectable on synthetics; it triggers a **HOLD**, and if confirmed after
  any real χ, F-9 voids the run.

- **AM-B NEYMAN PRIORS — Jeffreys, frozen exactly.** `a_s^prior = (c_s + ½)/(m_s + 1)` over the
  entire frozen synthetic pool binned by the harness's own cutpoint binning; Decimal at prec 28 as
  `Decimal(2c_s+1)/Decimal(2(m_s+1))`. Chosen over fixed-0.5 and ∝N_s because both of those reduce
  to anti-informative proportional allocation, and ∝N_s-when-degenerate adds a branch triggered by
  realized data. **Jeffreys is provably never degenerate**, so `nm_handcheck.py:3187`'s
  zero-information refusal becomes unreachable by construction. Verified: the formula reproduces
  every prior in the rehearsal's `hc1h_neyman_priors.json` byte-for-byte as a string.
  **Firewall (the load-bearing part): allocation priors never enter the estimate.** `a` is computed
  per HC-4 from human labels; `a_s^prior` touches only the integer `n_s`. A bad prior costs σ_a
  width — the safe direction — and cannot bias `a` at all.

- **AM-C SPARSE CELL — merge recommended, hold as the frozen fallback.** Deterministic merge ladder
  within a committee state only, never across states, evaluated once on the complete population
  before any preparation call. Rejected: proceeding with a deficient cell (not executable without
  modifying a gated safety check; a `n_s<30` cell would likely trip HC-5.2 spuriously; collides with
  F-10.c's k≥50). **AM-C.3 precedence, decided before the crossing:** if a gated, hash-pinned merge
  implementation exists at the crossing, merge governs; if not, HOLD → INCONCLUSIVE-BY-POWER
  governs. Both branches are frozen now, so no discretion survives the crossing.

## What Kun must rule on

1. P7's "9 strata" (V3 line 414) becoming "`|S|` strata + merge record" — required by AM-C.1. If
   declined, AM-C.2 governs unconditionally.
2. Whether the merge implementation can be gated before the crossing (`HC1H_STRATA` is a hardcoded
   nine-tuple at `nm_handcheck.py:45–46`).
3. Whether AM-A.4's FAIL_CLOSED consequence for a non-anchored delivered raster parity is *entailed*
   by PC-1/PC-4 (my reading) or is an **addition** that must be frozen tonight.
4. Whether AM-A.5's `sign(0) = 0` is a reading of F-1 (my position) or a parameter needing freeze.
5. **One-way door, flagged deliberately:** a weight-bounding treatment for a whole committee state
   with N<30 is statistically better than AM-C.2 but would modify HC-4, which this amendment may not
   touch. It can only ever be added **before** the crossing. I do not recommend adding it; nobody
   should discover the option after it expires.

## Engineering observation (not a preregistration parameter)

Pilot mode bypasses `allocate_neyman` (`nm_handcheck.py:691–693`) and has **no explicit floor
guard**: a stratum with fewer than 10 members silently under-fills and surfaces only as a
total-count mismatch at line 839. If a pilot runs, it needs the same pre-flight check.

## Boundary

Real chirality labels computed: 0 · real χ read: 0 · real cutouts/tensors/positions/rows read: 0 ·
sky statistics: 0 · frozen files modified: 0 (V3 re-verified at `b06901c8…`, mode 444, unmodified
after the work) · network calls: 0 · publication/acceptance/freeze/commit/push: 0.
Files written: `AMENDMENT_PREK8_20260820.md`, this receipt.

Back to Kun to gate; Duho owns acceptance and the freeze.

— ACQ science seat (claude-seat), 2026-08-20.
