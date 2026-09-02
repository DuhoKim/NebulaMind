AUDIT_HOLDS_CONSISTENCY_ONLY

Entry 53 — Cubero & Popławski (2019/2020), "Analysis of big bounce in Einstein–Cartan cosmology," CQG 37, 025011 (arXiv 1906.11824).
Blind-double audit, kimi seat, 2026-09-02. Sole source read: `../bhu-reading-20260823/sources/1906.11824_clean.txt` (551 lines). No other ENTRY53_* or result file opened.

1. DELTA VS ENTRY 52 (Unger & Popławski 2019)
   Same construction, same threshold structure, different scope. What 53 does that 52 does not:
   a) Turning-point analysis for ALL THREE curvatures, not only closed. The paper's own statement of purpose
      (lines 54–58): the earlier calculation "neglected the factor k = 1 in the Friedmann equations... de facto
      considering a flat universe" and "appeared to have a cusp-like behavior at the bounce"; "we refine those
      calculations by taking k into account and analyzing the turning points of the universe for all three cases:
      k = 1 (closed), k = 0 (flat), and k = −1 (open)." Conclusion repeats: "We eliminated the problem of a cusp"
      (line 432).
   b) Tables 1–3: explicit x_min, x_max, y(x_min), y(x_max), y_min for closed (lines 246–281), flat (305–325),
      open (351–381), plus all asymptotic C→∞ limits (lines 237–244, 243, 345–349).
   c) New time-dynamics result: the DOUBLE BOUNCE of the scale factor. From Eq. (27)–(30) and the scenario at
      lines 417–425: "at a bounce, the universe has a single bounce of the temperature and a double bounce of the
      scale factor with a little crunch between the two bounces"; vertical inflection of x(τ) at x = 1 (line 405,
      Eq. 29 line 401); symmetric iff C constant (lines 426–427). This dynamical detail is absent from 52.
   d) The trapped-null-surface formation statement (line 59): "a closed universe forms in a region of space within
      a trapped null surface when this threshold is reached. Such a region could be the interior of a black hole"
      (lines 59–60), repeated in conclusions (line 442). Qualitative scenario language, no derivation of the
      trapped surface itself — "could be," cited to ref BH (line 60).
   e) Different torsion coupling normalization. 53 switches from the spin-fluid α = κ(ℏc)²/32 (quoted in the
      intro, line 31) to the Dirac-form α = (9/16)κ(ℏc)² (Eq. 5, line 92) — a factor of 18 larger — because "the
      particle approximation for Dirac fields... is not self-consistent" and "violates the cosmological principle"
      (lines 42–43). Consequently the threshold constants differ from 52's aT ≥ √(8/9)·a_cr·T_cr: here the
      condition is C > e^(−1/2) (Eq. 24, line 224), equivalently a_min > a_cr at T = T_cr (Eq. 22, line 199, with
      C > e^(−1/2) ⇒ a_min = C e^(1/2) a_cr > a_cr). Same structural existence condition (a function of a and T
      above a threshold), different numerical constants from the different α. The physics content — torsion
      regularizes the singularity, closed branch exists only above threshold — is the same as 52; 53 is a
      refinement and generalization, not an independent line.

2. CLOSURE
   k = +1 is assumed, not derived: "Let us consider a closed relativistic universe, for which k = 1" (line 211),
   parallel to "for which k = 0" (line 285) and "for which k = −1" (line 330). The existence restriction applies
   only inside the assumed closed branch: two turning points exist iff C > e^(−1/2) (Eq. 24, lines 222–226);
   C = e^(−1/2) gives a stationary universe (lines 230–231); C < e^(−1/2) "the universe would not exist"
   (line 232). Flat and open are explicitly unrestricted, as in 52: "a flat universe and an open universe can
   exist for all positive values of the integration constant C" (line 440); Table 2/3 captions give domain
   (0, ∞) (lines 327, 382). The final threshold form is Eq. (31), lines 434–438: xy e^(−x²/2) > e^(−1/2).
   Q7-style ruling stands: existence exclusion inside the assumed construction.

3. NUMBERS (all extracted; every printed number with inputs)
   Constants: g_b = 29, g_f = 90 (line 111); α = (9/16)κ(ℏc)² (line 92); T_cr = √(2h*/3αh_nf²) = 2.218×10³¹ K
   (Eq. 11, line 132); a_cr = (27/8)ℏc√(αh_nf⁴/h*³) = 6.661×10⁻³⁵ m (Eq. 16, line 162); y_min = C e^(1/2)
   (Eq. 21, line 193); a_min = C e^(1/2) a_cr > 0 (Eq. 22, line 199); threshold C > e^(−1/2) = 0.60653 (line 224).
   Recomputed with bisection on f(x) = (3x²−2x⁴)e^(x²) = ±1/C² and y(x) = (C/x)e^(x²/2):
   - Table 1 row C=1: I get x_min = 0.555209, y(x_min) = 2.10126, x_max = 1.18912, y(x_max) = 1.70539
     (paper: 0.555209 / 2.10126 / 1.18912 / 1.70538 — agree to last digit, 1e-5 rounding on the last).
   - Table 1 row C=10: 0.057703 / 173.590 / 1.22444 / 17.2831 — exact match.
   - Table 1 row C=100: 0.005773 / 17320.9 / 1.22474 / 172.852 — exact match.
   - Asymptotics (lines 237–244): x_min → 1/(√3 C) → 0.0057735 at C=100 ✓; x_max → √(3/2) = 1.22474 ✓;
     y(x_min) → √3 C² = 17320.5 at C=100 ✓; y(x_max) → √(2/3)e^(3/4)C = 172.852 ✓;
     y(x_min)/y(x_max) → (3/√2)e^(−3/4)C, y(x_min)/y_min → √(3/e)C, y(x_max)/y_min → √(2/3)e^(1/4) = 1.04840
     — all algebraically consistent (cross-checked by dividing the asymptotic forms).
   - Table 2 (flat): x_max = √(3/2), y(x_max) = √(2/3)e^(3/4)C = 1.72852 C (line 326) ✓ — matches closed-branch
     C→∞ limit as stated (line 298).
   - Table 3 (open), recomputed: C=0.01 → x_max 2.33420, y 0.06531; C=0.1 → 1.64821 / 0.23599;
     C=1 → 1.25165 / 1.74866; C=10 → 1.22505 / 17.2874; C=100 → 1.22475 / 172.853 — all exact matches.
   - T_cr and a_cr from the stated inputs (g_b=29, g_f=90, Dirac α): I get T_cr = 2.23×10³¹ K (paper 2.218×10³¹)
     and a_cr = 6.57×10⁻³⁵ m (paper 6.661×10⁻³⁵) — within 0.5%/1.4%, consistent with the paper's rounded
     constants; no contradiction.
   Unstated inputs: ζ(3) enters h_nf (line 109) and is standard; no hidden numerical inputs found. Every printed
   number in the tables reproduces from the stated equations.

4. OBSERVATION-FACING CONTENT
   Line 39 repeats 52's delegated CMB sentence verbatim in substance: "This expansion also predicts the cosmic
   microwave background radiation parameters that are consistent with the Planck 2015 observations, as was shown
   in SD" — "as was shown in SD" delegates the derivation to Desai & Popławski 2016 (ref 12, lines 495–496);
   nothing about the CMB is derived here. The inflation/exponential-expansion and bounce-count claims are likewise
   delegated: "explaining inflation ApJ" (line 37, ref 10 = Popławski 2016 + Unger & Popławski 2019, line 490),
   "Inflation must increase the value of C... ApJ" (line 454), "several temperature bounces... SD" (line 455).
   There is no present-day Ω_k, no relic abundance, no data-tied bounce count, no derived observable anywhere in
   the paper. The black-hole/trapped-surface remark (lines 59–60, 442) is scenario language ("could be the
   interior of a black hole"), cited outward, not a prediction. A(a): every cited prediction belongs to the cited
   paper.

5. TIER CONSEQUENCE
   AUDIT_HOLDS_CONSISTENCY_ONLY. The paper is an internal-consistency refinement of the EC bounce: it corrects
   the k-neglect and cusp of the earlier calculation, extends the turning-point analysis to all three curvatures,
   and adds the double-bounce time dynamics. Its only restriction result is an existence condition inside an
   assumed k = +1 branch (closure assumed, not derived; flat/open unrestricted). All printed numbers reproduce
   from the stated equations with no unstated inputs. Nothing observation-facing is derived — CMB, inflation, and
   bounce-count claims are all delegated to SD/ApJ, matching the record that the "independent line" triage claim
   was wrong. No QUALITATIVE-DIRECTIONAL handle (no derived direction tied to an observable), no PROSPECT handle
   (no derived falsifiable statement with unstated-but-fixable inputs), no CALIBRATED-FALSIFIER content.

PLAIN-LANGUAGE PARAGRAPH
This paper is the companion fix-it paper to entry 52: it redoes the same Einstein–Cartan bounce calculation
correctly, keeping the curvature term the earlier work dropped, and checks all three universe types (closed,
flat, open). Its real new results are mathematical: the closed universe still only exists above a threshold (now
C > e^(−1/2), an existence condition inside an assumed closed universe, not something derived from data), the
flat and open cases are unrestricted, and the scale factor actually bounces twice with a small crunch in between.
Every number in its three tables recomputes exactly. But nothing in it touches observation: the CMB sentence is a
pointer to another paper, the black-hole remark is a "could be," and there is no derived prediction of any kind.
It is a consistency analysis of the same construction as entry 52, and the CONSISTENCY-ONLY tier holds.
