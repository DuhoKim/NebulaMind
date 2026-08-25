# Phase 5 brief — TOV-side optics (scoping, 2026-08-25 17:26 KST, Tori; for Duho's go)

## 0. The gap this closes, stated as Phase 4's gates forced it

Phase 4 (gated PASS, both engines) established the geometry of the shock-wave interior model
and was stopped three times by the same missing physics: nobody has computed how light behaves
when it crosses the shock. Consequences carried in the gated record:

- the hiding surface x_off < x_max(t_obs) is **sufficient, not necessary** — staying inside
  hides the wall, but crossing it is not shown to reveal anything;
- the single-cap result is a **crossing geometry, not a signal** — no amplitude, spectrum,
  or polarization exists;
- the C2 morphology finding is a **shape argument only**, and the branch stays
  CONSISTENCY-ONLY because of it.

Phase 5 computes the missing transfer. Success converts sufficiency into necessity and the cap
into either a calibrated prediction or an exclusion. Failure — of a specific, named kind —
closes the photon channel honestly.

## 1. The verification regime CHANGES here (read before anything else)

Phases 3 and 4 audited every equation against pinned published text. **No publication computes
TOV-side optics** — that is the gap. So:

- every equation is labelled **DERIVED (no pinned source)** or **PINNED (source + line)**;
  the two never blur, and a DERIVED equation may not be cited as if audited;
- **blind double implementation is PRIMARY, not a supplement**: two independent
  implementations from the same stated physics, neither seeing the other, as in A1;
- **limiting-case tests are the substitute for source-audit** and are mandatory:
  (a) shock strength → 0 must reproduce unperturbed FRW; (b) the p̄ → 0 limit must reproduce
  Oppenheimer–Snyder; (c) the optically-thin limit must reduce to pure geometric projection
  (Phase 4's A2/A4 result, which we already hold);
- textbook machinery may be used but must be cited to a specific text and equation
  (relativistic transfer: Lindquist 1966; Mihalas & Mihalas; MTW for geodesics), and any
  textbook equation adapted to this geometry becomes DERIVED at the point of adaptation.

## 2. Stages, fail-fast first

**S0 — optical depth of the exterior (the kill-fast stage).**
Question: can a photon cross the TOV side at all? Inputs we already hold: the A1 solution
tabulates v = ρ̄/ρ and u = p̄/ρ at the shock over ten decades (a1_results.csv, gated,
blind-double-confirmed). Design decision, declared up front because it is the honest hinge:
the exterior's ionization state is NOT given by the matching equations, so τ cannot be a
single number — S0 computes **τ as a function of the model's one free anchor** (the shock's
Big-Bang position r_*, equivalently the physical scale of t_crit) and of a declared
ionization assumption, and reports the anchor range in which τ ≫ 1 versus τ ≪ 1.
No single order-of-magnitude estimate will be presented as the result.
Kill criterion K1: if τ ≫ 1 across the whole physically admissible anchor range, the photon
channel is closed, the branch is UNTESTABLE-BY-LIGHT, and Phase 5 stops there with that
recorded as its finding.

**S1 — the crossing itself.** Photon geodesics across the FRW/TOV junction. The metric matching
is Lipschitz (C^1,1 in suitable coordinates, per the pinned ARMA/CMP results), so there is no
delta-function in the connection; but the FLUID velocity is discontinuous across a true shock,
so a crossing photon suffers a frequency shift relative to matter on the far side. Deliverable:
that shift as a function of crossing angle and shock strength, with the S3-pinned shock-speed
formula as input.

**S2 — the transfer function.** Temperature/intensity perturbation ΔT/T as a function of
direction for an observer at offset x_off, combining S1's crossing shift with S0's absorption
along the exterior path. Deliverable: T(μ; x_off, t_obs) — the object Phase 4 could not produce.

**S3 — angular power and confrontation.** Project T(μ) onto multipoles; compare the ℓ ≲ 10
amplitudes to the ALREADY-GATED Track B freeze (B3 rows). No new harvesting: the freeze is
frozen and its verifier is v8-gated. If a new bound class is needed, it is a gated Track B
addendum or nothing.

**S4 — verdict**, in the Phase 4 classes: EXCLUDED (amplitude exceeds the frozen bounds at
allowed offsets), CALIBRATED-FALSIFIER (a bounded prediction the sky can test), or PROSPECT
with the required sensitivity computed.

## 3. Kill criteria

- **K1** — τ ≫ 1 everywhere admissible → photon channel closed; stop at S0 (above).
- **K2** — perturbation below cosmic variance at ℓ ≤ 10 → PROSPECT, with the sensitivity a
  future instrument would need, computed and stated.
- **K3** — no free parameters beyond (x_off, t_obs) and the declared ionization assumption.
  Any additional dial requires a gate before it is used. (The Phase 3 βH⁴ lesson.)
- **K4** — if the junction requires physics outside the pinned metric (a shock-heated layer
  with its own thermodynamics, non-equilibrium radiation, etc.), STOP and record: that is a
  modelling choice, not a derivation, and it needs its own brief and go.
- **K5** — if S1's frequency shift proves gauge-dependent (an artifact of coordinates rather
  than an observable), record and stop; that would mean the crossing is unobservable in
  principle, which is itself a publishable-grade finding.

## 4. Scope fences

No .tex drafting. No new literature harvesting (the gated freeze is the observational input).
The spin-parity study stays untouched. The strongest sayable outcome remains about the
observable-scale interior branch; "BHU is falsified" is not a sentence this phase can produce.
Pre-horizon epochs only, inheriting Track A's gated domain.

## 5. Platoon composition (per the standing directive)

- blind-double on S0 and S2: one gpt seat implements independently from this brief's stated
  physics, never seeing my code (the A1 protocol, which caught nothing because both were right
  — the point is that it could have);
- kimi: gates only;
- agy: idle for this phase unless a textbook-equation transcription check is wanted.

## 6. Sequence

Brief → Duho's go (freezes it, sha-pinned) → S0 → **Duho pinged at the S0 outcome, because K1
may end the phase there** → S1–S4 with cross-engine gates per stage → phase-close report in
plain language.

No wall-clock estimate. S0 is days of work, not hours; the full chain is longer than Phase 4's.
