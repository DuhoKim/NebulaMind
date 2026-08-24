PASS_TRACK_A

# Gate verdict — Phase 4 Track A adversarial gate (kimi seat, 2026-08-24)
Gate: KICKOFF_GATE_TRACKA.txt (mandate: REFUTE). Verdict written to KGATE_TRACKA_VERDICT.md
per coordinator override (codex gate owns GATE_TRACKA_VERDICT.md); all other kickoff
instructions applied. Method: independent re-derivation and re-computation of every claim from
the pinned source (../bhu-reading-20260823/sources/0210105_clean.txt) using different solvers
and formulations than the lane scripts (DOP853/RK45 vs lane LSODA; eta_e-formulated crossing
solver vs lane chi-formulation). Evidence: _tmp_kgate_verify.py, _tmp_kgate_verify2.py,
_tmp_kgate_verify_out.txt in this directory. No track file modified.

## Attack 1 — the analytic claims: ALL CONFIRMED (attack failed)

(a) z_c(center) = sqrtN(eta_e). Re-derived: center sight line crosses when eta_o - eta_e =
r_*(eta_e) = eta_e*sqrtN(eta_e), so 1+z = eta_o/eta_e = 1+sqrtN. Verified numerically against
my own root-solve: agreement 4.4e-16.

(b) x_max(z;t_obs) = eta_o[(1+sqrtN(eta_e))/(1+z) - 1], eta_e = eta_o/(1+z). Re-derived from
the mu=+1 grazing condition x + chi = r_*(eta_e). Additionally proved EXACTLY (grid-free,
pure algebra): the P3 cap edge mu_c = (rho_s^2 - x^2 - chi^2)/(2 x chi) equals 1 identically
at x = x_max, so "cap opens exactly at x_max" is an algebraic identity, not a numeric
coincidence. Lane CSVs reproduce: a3_window.csv x_max column to rel <= 1.1e-4 (worst row at
the t_1100 zero-crossing, abs 4e-7); a4_regime_map.csv x_max_at_t to abs 6.5e-8; prose samples
t=0.14 -> 0.20 (mine 0.1993), band-middle -> 5.7e-4 (mine 5.74e-4), t->t_vis -> 1.1e-3 (mine
1.1485e-3) all match. One prose-only exception: see nit N1.

(c) Seed u = 1/3 - (4/3)sqrt(S). Re-derived by my own perturbation analysis of (5.4) with
u = 1/3 - w, sigma = 1/3: prefactor -> 1/(3S), numerator -> -3w^2 + (8/3)S, denominator ->
w + (4/3)S, ansatz w = a*sqrt(S) closes with -a/2 = (8/3-3a^2)/(3a) -> a^2 = 16/9. The
receipt's algebra (A1_RECEIPT.md line 9-12) matches mine term for term. I extended one order:
the O(S) coefficient is +20/3 (not needed by the track; recorded for the next reviewer).
Numeric confirmation: (1/3-u)/sqrt(S) -> 1.3333 on my independent orbit; backward integration
from the regular S=1 endpoint lands on the seed to 8 digits without being told to (reproduced);
gpt1's checks.json independently reports radiation_asymptotic_ratio 1.33327.

(d) Time mapping d ln t/dsqrtN = 2/(s - sqrtN). Re-derived from H = 1/(2t) (sigma=1/3),
sqrtN = r_bar H, dr_bar/dt = H r_bar + s: d(sqrtN)/dt = (s - sqrtN)/(2t) exactly. My
independent integration (anchored t=1 at sqrtN=1) matches lane t(q) to max rel dev 5.4e-10
over t in [2.8e-11, 1]. FRW-side identity r_bar = 2 t sqrtN: CSV-internal spread 6.75e-7
(receipt claims 6.8e-7, consistent).

Orbit itself: my DOP853/RK45 integrations (different seed point, tighter tolerances) match
lane a1_results.csv u(S) to max 2.0e-9 over all 40001 rows; (4.3),(4.5) re-algebraed on the
CSV to 2.7e-11 / 3.7e-7; entropy conditions (4.6) and (5.5) hold on every row; Thm 2 max s =
0.999959 < 1; Thm 3 s -> 1 at O(sqrt(S)) rate confirmed. The A1 receipt's "saddle connection,
forward shooting diverges" claim is REAL: I reproduced it — forward integration from S=1e-4
with seed perturbation +1e-8 veers to deviation 0.89 by S=0.9 (unperturbed seed: 4.4e-2 from
truncation error alone). Backward integration from the regular endpoint is the correct method.

## Attack 2 — A0 / null-H0: SOLID (attack failed)

The matched solution has the k=0 FRW metric exactly on the interior side (S1 section 4:
Lipschitz matching, "no delta function sources at the shock"). Null geodesics depend only on
the metric traversed; any photon path wholly inside the FRW region is a path in exact FRW, so
an off-center comoving observer sees the standard isotropic redshift-distance relation at any
offset. Loopholes probed and closed:
- Shock motion: subluminal everywhere (Thm 2 verified numerically); motion of the boundary
  does not alter the interior metric.
- Boundary conditions: no delta-function sheet at the shock, so no sheet-lensing of
  non-crossing paths either.
- Observer after shock exit (t > t_crit): out of scope — the regime map tops out at
  t_obs = 0.999 t_crit and every claim is made below it.
- Peculiar velocity: correctly flagged by the track (A2 receipt, A3(c)) as the one free
  kinematic dipole, same as in FRW.
Consequence: the track's "NO H0 dipole for interior sources — not small: zero" is correct, and
the refutation of the Phase-4 brief's motivating H0 claim by its own strict model stands.

## Attack 3 — dichotomy collapse / "strictly unobservable": survives on photons (attack failed
on the kickoff's stated trigger); one scope advisory

Kickoff trigger: "if a boundary-induced effect on non-crossing photons exists at any order,
the claim fails". NONE EXISTS — proof: the interior metric is exactly FRW; propagation effects
are path functionals of the metric; a path wholly inside traverses exact FRW; therefore the
effect on non-crossing photons is zero at every order, not merely small. ISW-type tails cannot
leak inward because there is no approximation to leak through — the FRW side is a given exact
metric in the matching construction.
- GW channel (failed attack): the exact solution is spherically symmetric about the FRW
  center; spherical symmetry admits no radiative tensor modes, so the model contains no GW
  background whose anisotropy could betray an offset observer.
- Neutrino channel (partial escape, non-binding): in principle the boundary intersects the
  neutrino last-scattering surface for a wedge of sub-P2-surface parameter space
  (x_max(z_ls) < x_off < x_max(z->infty) = RSTAR0 - eta_obs). But (i) the claim as used in
  every receipt is photon-scoped ("opacity + interior exactness"); (ii) the strict model is a
  single perfect fluid with sigma = 1/3 — no decoupled neutrino component exists in-model;
  (iii) CnuB anisotropy detection is beyond any forecast sensitivity, i.e. K2-flavored
  untestability, which is already the track's stated conclusion ("consistency bought at the
  price of untestability").
ADVISORY (wording, not physics): TRACK_A_VERDICT.md item 2's "STRICTLY UNOBSERVABLE" is exact
only scoped to photon observables; A3's own regime-1 wording ("untestable by this observable")
is the correctly scoped form. Track C should carry the scoped wording. This does not amend any
number and does not trigger the kickoff's amendment clause.

## Attack 4 — transcriptions vs pinned source: CLEAN (attack failed)

Checked against 0210105_clean.txt: (4.1) line 118 -> (5.4) line 189 change of variables
S = 1/N re-derived (du/dS = du/dN * (-1/S^2)); script dudS matches (5.4) exactly. (4.2) line
122, (4.3) line 130, (4.5) line 146, (5.6) line 203, (6.1) line 255, (6.2)/(6.3) lines
269-275, Theorem 1 + (5.7) lines 209-221, Theorem 2 lines 225-229, Theorem 3 lines 233-247:
all transcribed exactly; no OCR errors, no dropped factors, no sign errors. The §6 quotes in
A2_RECEIPT ("1.8 <= t_crit/t0 <= 4.5, 1 < sqrtN0 <= 4.5") match source line 286.

## Attack 5 — overclaims in TRACK_A_VERDICT.md: none found (attack failed), two nits below

All four numbered verdict claims are supported by the receipts and CSVs. The honesty ledger is
accurate: two self-corrections are real and documented (A1 anchor label; A3 trichotomy ->
dichotomy, forced by A4's failed check); the forward-shooting failure is real (reproduced, see
Attack 1). K3 respected: the paper's r* "free parameter" (S1 §7) is pure units once
t_crit = 1 and R(t_crit) = 1 are chosen — the k=0 system d(sqrtN)/dt = (s-sqrtN)/(2t) is
scale-invariant, so all family members coincide in t_crit units; t_obs scans the one genuine
remaining degree of freedom, and the track says exactly this.
Quantitative validations the receipts did NOT do, done here: (6.1) holds EXACTLY on the lane
solution (1/H0 = 0.552872 vs ((1+3 sigma)/2) r*_paper = 0.552872, rel dev 0 at print
precision); t_crit/t_vis = 3.6175 inside the sharp (6.3) bounds [e^{sqrt6/4}, e^{3/2}] =
[1.8448, 4.4817]; sqrtN0 = 1.5794 inside (1, 4.5].
Custody: all four sha pins verified (_tmp_a2_shas.txt: a2 script+CSV MATCH; A1_CROSSCHECK
prefix pins: a1 script 2ee881ea, a1 CSV 3264de39 MATCH). Blind double-implementation
independently re-confirmed by me from the raw CSVs: u median rel dev 4.6e-11, t 3.7e-8,
first-row identity t(sqrtN=1e5) = 2.7644109e-11 on both sides; r_shock(gpt1) = 2*r_bar(lane)
to 3.4e-7.

## Nits (recorded; none gate-binding)

N1. A4_RECEIPT.md P2 prose sample "t = 0.274 (~t_vis): 4.3e-3" is unsupported by
a4_regime_map.csv — the script's own t >= T_VIS guard leaves x_max_at_t EMPTY at those rows —
and is ~9% off my independent value 3.94e-3. All CSV-backed x_max numbers reproduce exactly;
this is a hand-computed prose sample only.
N2. A2_RECEIPT.md table row for x_off/r_* = 0.50 ("shock already crossed in 1 of 41 directions
(partial-sky)") is garbled: a2_zcross.csv shows 40 of 41 directions with finite z_c and
exactly ONE (mu = -1, anti-offset) staying inside the shock to the Big Bang. The CSV is
correct (reproduced to 5e-6); the parenthetical misleads.
N3. (5.6) admissibility fails on exactly 1 of 40001 CSV rows — the last row (S = 1 - 1e-8
endpoint, S - bound = 0 at machine precision). The lane's own check excluded this endpoint
(adm[:-1]). Benign seed-point artifact, transparently handled in-lane.

## Failed attacks (positive evidence of soundness)

Seed derivation; time mapping; center law; x_max formula; cap geometry (all re-derived and
numerically confirmed). A0/null-H0 (proof-level). GW and neutrino in-principle channels
against "strictly unobservable" (GW: excluded by spherical symmetry; neutrino: out-of-model,
out-of-sensitivity). Equation transcriptions (clean). Overclaims (none). Blind cross-check
(re-confirmed independently, tighter than claimed). The forward-integration instability claim
(confirmed real). One gate-side error worth recording: my first eta_e-formulated crossing
solver had inverted bracket logic (599 spurious mismatches); after correction, finite-z
agreement is 5.0e-6 max and the lane's chi-formulation was found to fail-safe (toward
"no crossing", the conservative direction) at the exact-grazing t_vis edge where my grid
clamping flipped the sign. Lane formulation validated at the edge.

Verdict: PASS_TRACK_A. This gate passes the Track A record as sound within its stated scope
(sigma = 1/3 strict interior model, photon observables, t_obs < t_crit); launching Track B/C
confrontation on these prediction functions is a separate act not authorized by this verdict.
