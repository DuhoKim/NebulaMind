PASS_P2_INHERIT

# kimi — Phase 2, Track B step-2 gate: the inheritance derivation (second reviewer, fresh one-shot)
2026-08-19. Lane dir only. Findings-only; nothing edited; this is the only file written.
Zero fetches of any kind (holding the step to its own zero-fetch claim). portal.nersc.gov
untouched. Reviewed adversarially: this gate guards the phase's ORIGINAL claims.

## Check 1 — Receipts rerun (python3, this session, this machine)

All three receipts executed clean (exit 0); each rerun is BYTE-IDENTICAL to the stored
receipts/p2b2_{mass,spin,shear}_out.txt. Every gate-named headline number reproduces:

| Headline | Doc claim | Rerun result | Verdict |
|---|---|---|---|
| M->(a0,sinR0,T0) map re-derived symbolically | a0=(r0^3/r_g)^1/2, sinR0=(r_g/r0)^1/2, T0 closed form | "True / True" + printed closed form for T0 from the two defining relations | CONFIRMED |
| bounce state M-independent, both treatments | T_max=1.152e32 K (I), T_cr=0.785 m_P (II) | same values carried; neither depends on M (functions of g*,g_n,kappa only) | CONFIRMED |
| cross-treatment bounce-density disagreement | ~x730 | eps_b(I)=7.112e114 / eps_b(II)=9.781e111 J/m^3 -> x727 | CONFIRMED |
| a0*T0 scaling | prop. chi^(3/4) M^(1/2) | "-> proportional to chi^(3/4) M^(1/2): True" (symbolic) | CONFIRMED |
| spin ceiling 10 M_sun a*=0.7 | 1.5e-27 (I) / 1.4e-26 (II) | 1.51e-27 / 1.36e-26 | CONFIRMED |
| ceiling scaling | prop. M^(-2/3) | ratio 4.642e-06 = (1e8)^(-2/3) exactly | CONFIRMED |
| causality excess, conserved J | 6.6e26 | Omega_cons=5.06e57 vs c/R_b=7.66e30 -> 6.6e26 (= 1/eps_max, internally consistent) | CONFIRMED |
| polarization sliver | <= 5e-13 (I) / 3e-12 (II) | 5.1e-13 (I) / 2.6e-12 (II) | CONFIRMED with nit N1 |
| frozen-ratio theorem | both terms a^-6, ratio constant | ratio = -12 Sigma2/(C kappa^2 n0^2), "a-independent: True"; bounce root a_m^2 = (C kappa^2 n0^2 - 12 Sigma2)/(4 epsR0 kappa), positive iff Sigma2 < kappa^2 C n0^2/12: True | CONFIRMED (sympy-executed) |
| bracket-independence of theorem | both edges a^-6; eps_max moves only 6^(1/3)~1.8 | coherence bracket changes C's value, not the exponent; 6^(1/3)=1.817 arithmetic checks | CONFIRMED |

Planck-convention consistency checked: p2b2_spin_channel.py uses reduced m_P
(sqrt(hbar c^5/8 pi G)) for T_II = 0.785 m_P; p2b1_dirac_derivation.py line 38 uses the
identical definition (prints "reduced m_P"). eps_b(II) is calibrated to the same B1 bounce
state — no hidden factor-sqrt(8pi) between steps. The x730 fork is internally consistent.

## Check 2 — Adversarial pass on the two original claims

(a) The ceiling (doc section 2.2). Chain inspected link by link:
- xi is the rigid-rotation inertia prefactor (I = xi M R^2), xi=2/5 uniform sphere, bracket
  0.2-0.5 — NAMED in the doc (line 75) and in the receipt docstring. v_rot = J_b/(xi M R_b)
  is just Omega R for rigid rotation.
- R_b = (3M/4 pi rho_b)^(1/3): the full parent mass as a uniform ball at the treatment's
  bounce density — a modeling choice, NAMED as such (line 74-75), and the whole result is
  flagged order-of-magnitude ("derived, order-of-magnitude, assumptions named", line 71).
- Bounce state: BOTH treatments used, results bracketed (1.5e-27 / 1.4e-26); Gate-flag-1
  treatment-naming honored.
- Inequality direction: FORCED, not chosen — given the named premise (the published bounce
  is homogeneous and non-rotating, so rotation at the patch must be sub-relativistic,
  v_rot < c), J_b < xi M R_b c follows and eps_max = xi c^2 R_b/(a* G M) is algebra. The
  premise itself is a consistency demand, and its failure mode is stated as Reading 2.
- Structural premise "torsion couples to intrinsic spin only; orbital J has no torsion
  channel" — PINNED, verified at source: sources/1007.0587/main.tex line 88 "Since Dirac
  fields couple minimally to the torsion tensor, the torsion of spacetime ... does not
  vanish in the presence of fermions"; lines 100-103 define the spin tensor s_ij^k = s_ij u^k
  as the fluid's spin density; the Cartan-source structure (eq. com, lines 105-108) carries
  only s^2 and spin-gradient terms. The pin supports the positive claim (source = intrinsic
  spin tensor); the negative claim (no orbital-J channel) is the exhaustive-reading
  consequence of that source list. Adequately pinned, not bare assertion.
- Both readings stated (lines 89-96): bounded inheritance vs the homogeneous bounce never
  happens for rotating parents. Neither silently chosen.

(b) The frozen-ratio theorem (doc section 3). Symbolic step rerun (above). Premise attack:
- w-dependence: NONE. The a^-6 torsion scaling rests on n prop. a^-3, which B1 derived for
  any w (spin-fluid w=+1 and Dirac w=-1 alike) — the theorem is treatment-independent.
- V2 (n^2 averaging): enters only the torsion term's normalization (C); the theorem is an
  exponent statement, so the x6 coherence bracket cannot touch it — the doc's
  bracket-independence claim (lines 125-127) is correct, and the 6^(1/3)~1.8 eps_max shift
  is arithmetic that checks.
- Isotropy: NOT assumed — the setup is precisely the minimal anisotropic extension (shear
  term added to the Friedmann equation), so it does not beg the isotropization question.
- Shear-side premise (+Sigma^2 a^-6) is standard Bianchi-I-type GR bookkeeping; it is named
  in the receipt docstring but not pinned to a pinned-source line — recorded as nit N3
  (zero-fetch constraint; standard result, and the theorem's direction makes it conservative
  for the conclusion drawn).
- Scope honesty: the doc states the theorem derives no bound on production ("derives no
  bound on what production does", lines 122-123), verdict UNDETERMINED, and names that it
  cuts against the chain's isotropization language. Honest.

## Check 3 — Honest-parameterization audit

- No transfer function manufactured: HOLDS. Section 0 line 28 "No transfer function is
  manufactured"; section 2 opens with the published-absence finding and derives only bounds.
- Everything undetermined marked STILL-PARAMETERIZED with MODEL_SPEC rows cited: A4 named at
  line 96 ("remains STILL-PARAMETERIZED (MODEL_SPEC row A4)"); A3/A5/A7 rows in the table
  carry their spec content.
- A4 upgraded, none eliminated: table row A4 "STILL-PARAMETERIZED, NOW BOUNDED: eps in
  [0, eps_max] ... derived (B2-R2), conditional on Reading 1"; net line 144: "one Phase 1
  parameter gained a derived ceiling (A4); none was eliminated."
- A0-A9 cross-reference table complete: 10 rows, A0 through A9, each with a status
  (NOT-APPLICABLE / STILL-ASSERTED / STILL-PARAMETERIZED / PARTIALLY-DERIVED-ELSEWHERE /
  UNCHANGED / SUPPORTED-consistency-only). Complete.
- Both ceiling readings stated, not silently chosen (lines 89-96).
- Conceptual-mapping note (recorded, not a defect): the ceiling bounds J_b/J_parent while
  spec A4's eps multiplies omega_ref; the doc's A5 row states the roof applies to the
  f_b*eps product. The mapping is acknowledged, not hidden.

## Check 4 — Requirements sweep (seven binding requirements, quote-line evidence)

R1 M channel through both treatments: doc lines 32-53; B2-R1 prints True/True + closed
form; line 43 "The bounce state is M-independent in both treatments"; lines 45-47 the x730
fork with treatment named per quantity; line 48 a0 T0 prop. chi^(3/4) M^(1/2); A-18 washout
noted lines 51-53. HOLDS.
R2 a* channel, first principles, no manufactured transfer: lines 57-96; three results (no
torsion channel / ceiling / sliver) each receipted (B2-R2); line 96 the parameterization
statement with A4 cited. HOLDS.
R3 shear UNDETERMINED + bound attempt: lines 109-127; B2-R3 sympy receipt; axis-memory
consequence stated (lines 121-124). HOLDS.
R4 V1/V2 markers travel: section 5 lines 148-162 — V1 on every bounce-state quantity and on
eps_max through R_b; V2 accounted including the negative finding (line 154: "V2 enters eps_b
via h*-normalization? No — eps_b is thermal"); V3 on Treatment II uses; V5 unchanged. HOLDS.
R5 cross-reference table: section 4, A0-A9 complete, A4 upgraded-bounded, none eliminated.
HOLDS.
R6 sources discipline: lines 7-8 "pinned copies under sources/ and this lane's gated
documents only; Goru sections 1/2/4 remain excluded"; grep of the full doc: "Goru" appears
only in that exclusion sentence; HRDCC appears only as the excluded claim (line 59); no
CMB/BBN content. HOLDS.
R7 lane-only writes, no residue: no _tmp_ files in the lane dir; receipts carry p2b2_ prefix
with outputs alongside; B2_DONE.md first line B2_COMPLETE. HOLDS.
Zero-fetches claim held: grep of P2_DERIVATION_INHERITANCE.md and B2_DONE.md for
http/www/.com/.org/.gov/crossref/arxiv./fetch returns only the discipline sentences
themselves ("zero new fetches"; "portal.nersc.gov untouched"). No URL or host appears
anywhere in the deliverable. CONFIRMED.

## Nits recorded (non-blocking; none touches a conclusion)

N1: doc line 101 says the polarization sliver is "<= 5x10^-13 (I)"; the receipt computes
5.1e-13 — a 2% rounding overstatement of the "<=" (correct phrasing: ~5e-13). The (II)
bound 3e-12 holds (2.6e-12). Dismissal conclusion unaffected by ~50 orders of margin.
N2: p2b2_spin_channel.py part (B) computes Omega_max once, outside the treatment loop, from
Treatment I's R_b; the printed Treatment-II sliver (2.6e-12) therefore uses a mismatched
(too large) Omega. The matched-input value would be ~3e-13 — i.e. the bug is CONSERVATIVE
(overstates the sliver). Conclusion (torsion sector unpolarized) stands with more margin.
N3: the shear-side premise +Sigma^2 a^-6 in B2-R3 is standard GR bookkeeping, named in the
receipt docstring but not pinned to a pinned-source line (zero-fetch step). The torsion side
is B1-derived. The theorem's application direction is safe under it.

## UNVERIFIED-AT-GATE

None. Every gate-named check completed within the time box.

## Gate decision

PASS_P2_INHERIT. All three receipts rerun byte-identical and reproduce every headline
number; both original claims survive an adversarial read (premises named, inequality
direction forced, structural premise pinned at source, theorem bracket- and w-independent,
scope stated honestly); the parameterization audit shows no manufactured transfer function,
a complete A0-A9 table with A4 bounded and none eliminated, and both ceiling readings
stated; all seven kickoff requirements hold with quoted line evidence; zero fetches claimed
and zero performed. Three conservative-direction nits recorded for the wrap-up ledger.

— kimi, second reviewer, Track B step-2 gate, Phase 2, 2026-08-19. One file written.
No host fetched. portal.nersc.gov untouched.
