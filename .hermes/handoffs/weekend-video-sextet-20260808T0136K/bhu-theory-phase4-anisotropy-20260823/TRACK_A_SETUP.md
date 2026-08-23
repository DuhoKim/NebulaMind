# Track A setup — the strict interior model (opened 2026-08-23 23:14 KST, Tori)

## Pinned sources (the ONLY equation sources for this track)

- S1: astro-ph/0210105 (= Smoller & Temple, PNAS 100, 11216 (2003)), held as
  `../bhu-reading-20260823/sources/0210105_clean.txt`, sha256 82fd8322…
- S2: Smoller & Temple 2000 (CMP 210, 275), `smoller_temple_2000_clean.txt` +
  PDF sha256 ef904904… — the outside-the-horizon precursor; general shock equations.
- S3: Smoller & Temple 1997 (ARMA 138, 239), sha256 6e709a9c… — ODE machinery,
  Lax admissibility, speed formulas.
- S4: Blau–Guendelman–Guth 1987 (PRD 35, 1747), sha256 1d195f5f… — junction/geometry
  anchor (context; not expected to contribute equations to Track A).

## The model as the pinned text states it (S1, cross-referenced by line in the clean text)

- Interior: critically expanding (k = 0) FRW metric. Exterior beyond the shock: a
  "TOV metric inside the Black Hole" (S1 §3) — the A < 0 continuation the standard TOV
  equations do not reach (S1 states the standard TOV metric "cannot be continued into a
  Black Hole", citing their [6]).
- The shock lies BEYOND ONE HUBBLE LENGTH from the FRW center (S1 §2) — this is forced:
  at fixed t there is a critical radius r̄_crit such that the mass inside a shock beyond it
  puts the universe inside a black hole (S1 §2).
- The matching system: ODEs (4.1)–(4.3) in S1, in shock-frame variables
  u = p̄/ρ, v = ρ̄/ρ, σ = p/ρ, with the constraint v = [−σ(1+u) + (σ−u)N] / [(1+u) + (σ−u)N].
- Distinguished equation of state: only for σ = 1/3 (pure radiation) does the shock emerge
  from the Big Bang at finite nonzero speed (= c) (S1 §2) — the text's own headline structure.
- Large-time asymptotics: the shock weakens to a zero-pressure Oppenheimer–Snyder interface;
  the whole configuration eventually emerges from a WHITE HOLE horizon of an ambient
  Schwarzschild spacetime (S1 abstract/§1) — bounded total mass, asymptotically flat outside.

## The derivation target

An observer at comoving offset x_off from the FRW center. The interior FRW region is exactly
homogeneous — so the honest starting statement, which shapes everything downstream, is:

**A0 (to prove or refute first): within the pure-FRW interior, an off-center observer sees NO
local anisotropy; every anisotropic observable must enter through the boundary — i.e., through
the direction-dependent comoving distance to the shock surface.**

If A0 holds (expected), the observables are boundary-mediated and the derivation plan is:

1. **A1 — shock trajectory.** Integrate the S1 ODE system from the σ = 1/3 exact starting point
   to obtain r_shock(t) and the TOV-side profile; receipts as scripts in this dir
   (`_tmp_*` intermediates, final scripts committed).
2. **A2 — past light cones.** For observer (x_off, t₀): the largest redshift z_c(n̂, x_off)
   at which the past light cone in direction n̂ crosses the shock. The anisotropy of z_c is
   the raw geometric signal: Δz_c/z_c ~ f(x_off / r_shock).
3. **A3 — observables.**
   (a) CMB: does the last-scattering sphere cross the shock for any allowed x_off? If yes —
   direction-dependent truncation/modification (low-ℓ prediction). If no — the CMB constrains
   nothing here, and the record says so (feeds K2).
   (b) Late-time expansion: direction dependence of the redshift–distance relation for sources
   whose light samples regions gravitationally influenced by the shock/TOV side; the H₀
   dipole amplitude as a function of x_off.
   (c) The non-kinematic dipole: the observer's motion relative to the FRW frame is a free
   parameter in ΛCDM but structured here; state carefully what is and is not predicted.
4. **A4 — the prediction functions.** D(x_off, R_shock) for each observable in A3, tabulated,
   with validity domains; these are what Track B's frozen bounds confront.

## Honesty rails specific to this track

- If A0 fails in an interesting way (TOV-side influence propagating into the interior — e.g.,
  through the pre-shock-formation epoch), that is a finding, not an error; document and re-plan.
- The k = 0 choice is S1's, not ours; no switching to k ≠ 0 mid-track (that is a different
  model and would need a brief addendum).
- Lookback through the shock touches the σ = 1/3 era where the shock moves at c — expect
  causal-contact subtleties; resolve them from the equations, not from intuition.
- Any equation not derivable from S1–S3 as pinned = STOP, record the gap, check the PNAS
  published version (per the freeze record), and only then proceed.

## State

- [x] Sources pinned, model transcribed from S1 with locations
- [ ] A1 shock trajectory (numerics) — next session's work
- [ ] A2, A3, A4 — sequenced after A1
