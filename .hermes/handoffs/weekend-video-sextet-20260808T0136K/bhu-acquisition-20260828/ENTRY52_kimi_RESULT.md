AUDIT_HOLDS_CONSISTENCY_ONLY

# Entry 52 — Unger & Poplawski (2019), ApJ 870, 78 (arXiv 1808.08327) — deep audit, kimi seat
Pinned source: `../bhu-reading-20260823/sources/1808.08327_clean.txt` (716 lines). Nothing else read.
Arithmetic note: this session's compute tools (terminal python, execute_code) were approval-blocked in
single-query mode, so every recomputation below was done by hand with intermediate values shown. Constants
used: G = 6.674e-11, hbar = 1.0546e-34, c = 2.9979e8, k_B = 1.3807e-23, zeta(3) = 1.20206.

## 1. The threshold result — what is derived, what is borrowed, is "closed" ever derived?

Chain (all line receipts from the pinned text):

- Spin-fluid effective source, eq (1) lines 42-46: eps~ = eps - alpha n_f^2, p~ = p - alpha n_f^2,
  alpha = kappa(hbar c)^2/32. BORROWED closure: EC torsion integrated out + Papapetrou multipole spin
  fluid (lines 38-40, cites NSH, HHK, EC1-EC6). Not derived here.
- Kinetic-equilibrium ultrarelativistic closures, line 111: eps = h* T^4, p = eps/3, n_f = h_nf T^3,
  with h* and h_nf built from g_b, g_f. BORROWED (cites Ric). g_* FIXED: "g_b = 29 and g_f = 90"
  (line 113), standard-model counts stated without derivation and held fixed for the whole run.
- Friedmann with spin correction, eq (8) lines 116-118: derives from substituting the closures into the
  EC Friedmann eq (6). Paper-internal algebra.
- First law, eq (9) line 122: (adot/a + Tdot/T)(1 - 3 alpha h_nf^2 T^2/(2 h*)) = 0 -> eq (10)
  adot/a + Tdot/T = 0 -> integrated eq (17) line 172: x y = C. Paper-internal; C is a free integration
  constant (line 176).
- Turning points: eq (18) line 179, ydot = 0 condition (19) line 188, quadratic (20) line 195, roots
  (21) line 201, discriminant >= 0 -> C >= sqrt(8/9), eq (22) line 210, i.e. aT >= sqrt(8/9) a_cr T_cr,
  eq (23) line 216. Pure algebra from (18)+(19); no step is hidden. Verified by hand: discriminant of
  y^4 - 3C^4 y^2 + 2C^6 = 0 in z = y^2 is 9C^8 - 8C^6 >= 0 iff C^2 >= 8/9. Holds.
- Second threshold with Lambda: eq (40) line 402, late-time reduction (42)-(43), no-turning-point
  condition C > (12 lambda)^(-1/4) (44), then the matter-era cubic (49) and condition (50) ->
  C > (2/(9 sqrt(3 lambda)))^(1/3) / x_eq = 1.9e48, eq (51) lines 487-489. Paper-internal algebra.

Is "closed" DERIVED anywhere? No. Line 67: the paper "analyz[es] the expansion of the universe for all
three cases: k = 1, k = 0, k = -1" — k = +1 is an assumed branch, one of three. What is derived is an
EXISTENCE CONDITION INSIDE the k = 1 branch (a closed branch has turning points only if C >= sqrt(8/9)),
plus a local-formation claim: "a closed universe forms in a region of space within a trapped null surface
when this threshold is reached" (line 69, citing ApJ = Poplawski 2016, ref 1 line 506). The trapped-null-
surface premise is borrowed, not derived. There is no dynamical selection of k = +1 anywhere in the text;
flat and open branches are shown to be UNRESTRICTED (lines 370, 393), i.e. the dynamics does not prefer
any curvature sign. The 2026-09-01 ruling A(a) (assumed ansatz -> tier holds) is confirmed on re-derivation.

## 2. Numbers — extraction with inputs, recomputation

Printed numbers and their inputs:

- T_cr = (2 h*/(3 alpha h_nf^2))^{1/2} = 9.410e31 K, eq (14) line 153.
- a_cr = (9 hbar c/(8 sqrt2))(alpha h_nf^4/h*^3)^{1/2} = 3.701e-36 m, eq (15) line 159.
- C >= sqrt(8/9) = 0.94281, eq (22) line 210.
- Stationary point at C = sqrt(8/9): y = sqrt(32/27) = 1.08866, x = sqrt(3)/2 = 0.86603 (lines 222-224).
  Internal consistency check: x*y = 0.86603*1.08866 = 0.94281 = sqrt(8/9) = C, matches eq (17) xy = C.
- C = 1 gives x = 1, y_min = 1 (eqs 26-27, lines 244-250); greatest T in closed EC = sqrt(3/2) T_cr
  (line 258).
- Expansion factor "9 C^2 / 2" and equal temperature-decrease factor (line 259), C >> 1.
- lambda = Lambda a_cr^2/3 = 5.0e-124, eq (41) line 408, from Lambda = 1.1e-52 m^-2 (line 412).
- T_eq = 8.8e3 K (line 459); x_eq = T_eq/T_cr = 9.4e-29, eq (48) line 468.
- C > 1.9e48, eq (51) line 487.
- g_b = 29, g_f = 90 (line 113).

Recomputation by hand (constants above):
- h* = (pi^2/30)(29 + 7/8*90) k_B^4/(hbar c)^3 = 0.32899*107.75 * 1.1493e-15 = 4.073e-14.
  h_nf = (zeta(3)/pi^2)(3/4)(90) k_B^3/(hbar c)^3 = 0.121794*67.5 * 8.3245e7 = 6.844e8.
  alpha = kappa(hbar c)^2/32 = 2.0766e-43 * 9.9957e-52 / 32 = 6.487e-96.
- T_cr = sqrt(2*4.073e-14 / (3*6.487e-96*(6.844e8)^2)) = sqrt(8.146e-14 / 9.115e-78) = sqrt(8.937e63)
  = 9.45e31 K. Printed 9.410e31. Agreement to ~0.5% (constant rounding). REPRODUCES.
- a_cr = (9*3.1616e-26/11.3137) * sqrt(6.487e-96*(6.844e8)^4/(4.073e-14)^3)
  = 2.5151e-26 * sqrt(2.1064e-20) = 2.5151e-26 * 1.4513e-10 = 3.65e-36 m. Printed 3.701e-36.
  Agreement to ~1.4%. REPRODUCES.
- lambda = 1.1e-52 * (3.701e-36)^2 / 3 = 1.1e-52 * 1.3697e-71 / 3 = 5.02e-124. Printed 5.0e-124.
  REPRODUCES exactly.
- x_eq = 8.8e3 / 9.410e31 = 9.35e-29. Printed 9.4e-29. REPRODUCES.
- Threshold (51): (2/(9 sqrt(3*5.0e-124)))^{1/3} / 9.4e-29 = (2/3.4857e-61)^{1/3} / 9.4e-29
  = (5.7377e60)^{1/3} / 9.4e-29 = 1.7900e20 / 9.4e-29 = 1.904e48. Printed 1.9e48. REPRODUCES exactly
  from the paper's own printed inputs.

Unstated inputs (the entries-9/10/11 pattern repeats):
- Lambda = 1.1e-52 m^-2 (line 412) is stated with no citation and no fit here.
- T_eq = 8.8e3 K (line 459) is stated with no derivation and no citation.
- g_b = 29, g_f = 90 (line 113) stated as standard-model counts, not derived.
One phrasing slip worth noting: line 259 says the universe "can expand by a factor of 9 C^2/2 and its
temperature can decrease by the same factor." From eq (25)/Table 1, y+^2/y-^2 = 3C^4/((2/3)C^2) = 9C^2/2,
so the LINEAR expansion factor is (3/sqrt2) C ~ 2.12 C, and x_max/x_min = sqrt((3/2)/(1/(3C^2)))
= (3/sqrt2) C likewise. "9 C^2/2" is the ratio of the squared nondimensional scale factors; the linear
factor and the temperature factor agree with each other but not with the printed "same factor" sentence.
Internal only; does not change any threshold.

## 3. The CMB-parameter claim (line 54)

Line 54: "This expansion also predicts the cosmic microwave background radiation parameters that are
consistent with the Planck 2015 observations Planck2015 ; Planck2016 , as was shown in SD ." SD = Desai &
Poplawski, Phys. Lett. B 755, 183 (2016), ref 30 line 593; Planck refs are 28-29, lines 587-590.

(a) Does THIS paper derive any CMB parameter (n_s, r, amplitude)? No. No spectral index, tensor-to-scalar
ratio, or amplitude is computed anywhere in the text; the only CMB sentence is line 54, and it explicitly
attributes the showing to SD ("as was shown in SD").
(b) Which quantities does it say SD predicted, and with what free inputs? The pinned text says NOTHING
beyond "the cosmic microwave background radiation parameters that are consistent with the Planck 2015
observations." No parameter names, no beta, no bounce count, no free inputs are stated. (SD not fetched,
per brief.)
(c) Does this paper use Planck consistency to constrain its own parameters? No. Nowhere in the text is
Planck consistency used to fix C, lambda, g_*, the number of bounces, or anything else. The only
observational input used quantitatively is Lambda = 1.1e-52 m^-2 (line 412), unattributed. Per the brief's
rule, the CMB prediction belongs to SD's entry, not to this one.

## 4. Observation-facing content of THIS paper

- Curvature sign: NOT derived (see 1). k = +1 is an assumed branch; flat and open are shown unrestricted.
- Any number + threshold an observation could hit: NO. Both thresholds (C >= sqrt(8/9), eq 22/33;
  C > 1.9e48, eq 51) are conditions on the nondimensional combination C = aT/(a_cr T_cr), a free
  integration constant of the model (line 176), not a predicted observable. There is no present-day
  Omega_k window, no predicted aT value, and no data constraint on the number of bounces — the bounce
  count appears only as an unconstrained possibility ("may undergo several bounces", line 53;
  cycles until the threshold is reached, lines 497-499).
- Net: no observation-facing content of its own; the only observational pointer (line 54) is delegated
  to SD.

## 5. Tier consequence, argued

CONSISTENCY-ONLY. Reasoning: (i) the headline aT threshold is an existence/exclusion condition inside an
assumed k = +1 branch — it says when the closed branch has turning points at all, not that the universe
is closed or what aT is; (ii) every printed number reproduces from the stated closures (fixed g_*,
kinetic equilibrium, spin fluid), and the one externally-sourced input (Lambda) is unattributed but
standard; (iii) the paper owns no DERIVED signed direction and no observation-hittable number of its own;
(iv) its single observation-facing sentence delegates the CMB parameters to SD, and per the brief a cited
prediction in another paper belongs to that paper, not to this entry. Nothing here reaches
QUALITATIVE-DIRECTIONAL (no derived curvature sign), PROSPECT (no number an observation could hit), or
CALIBRATED-FALSIFIER. The 2026-08-30 Q7 ruling (existence exclusion inside the construction) and the
2026-09-01 A(a) ruling (closed = assumed ansatz) both survive re-derivation.

## Plain-language paragraph

This paper takes a closed universe as one of three assumed possibilities and asks a housekeeping question:
given the spin-torsion bounce model with standard radiation thermodynamics, when does the closed branch
even have turning points? The answer is a clean piece of algebra — the product of scale factor and
temperature must exceed sqrt(8/9) times two model constants — and a second, huge threshold (C > 1.9e48)
for the universe to escape re-collapse once a cosmological constant is added. Every printed number I could
rebuild by hand checks out (T_cr, a_cr, lambda, x_eq, and the 1.9e48 threshold all reproduce), though the
equality temperature and the cosmological constant are plugged in without citation. What the paper never
does is derive that the universe IS closed, predict any value an observation could measure, or compute any
CMB parameter itself — the Planck agreement is explicitly borrowed from the earlier Desai-Poplawski paper
and belongs to that paper's ledger entry. The CONSISTENCY-ONLY tier holds.
