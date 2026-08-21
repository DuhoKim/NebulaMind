PASS_P2_BOUNCE

# kimi — Phase 2, Track B step-1 gate: the bounce derivation
Fresh one-shot, 2026-08-19. Lane dir only. Findings-only; nothing edited; this is the only
file written. Zero fetches of any kind (holding the derivation to its own zero-fetch claim).
portal.nersc.gov untouched.

## Check 1 — Receipts rerun (python3, this session, this machine)

Both receipts executed clean (exit 0); rerun output is byte-identical to the stored
receipts/p2b1_spinfluid_out.txt and receipts/p2b1_dirac_out.txt. Every gate-named headline
number reproduces:

| Headline | Derivation claim | Rerun result | Verdict |
|---|---|---|---|
| Omega_S coherent edge | -8.82e-70 | Omega_S = -8.820e-70 | CONFIRMED |
| Omega_S incoherent edge | -1.47e-70 | Omega_S = -1.470e-70 | CONFIRMED |
| coherence spread | x6.00 | "coherent/incoherent = 6" (36v vs 6v) | CONFIRMED |
| published -8.6e-70 position | at coherent edge, 2.6% inside | offset 2.5% of 8.82 / 2.6% of 8.6 (gate recomputation) | CONFIRMED |
| eps_R own Omega_S | 7.27e116 | eps_R(a_m) coherent = 7.273e+116 | CONFIRMED |
| eps_R printed Omega_S = audit R2 | 7.65e116, "reproducing audit R2 exactly" | 7.273e116 x (8.82/8.6)^2 = 7.650e+116 = R2's 7.650e116 (gate recomputation; note below) | CONFIRMED |
| Treatment I Planck ratio | >= 1.6e3 coherent, 5.7e4 incoherent x eps_Planck | 1569.8 / 56514.3 (eps_P = 4.633e113) | CONFIRMED |
| Treatment II T_cr | 0.785 m_P | T_cr = 0.785 m_P (g_star 106.75, g_n 67.5) | CONFIRMED |
| Treatment II incoherent edge | T_cr -> 1.92 m_P (f=6) | "T_cr -> 1.92 m_P"; a_cr -> 2.39e-4 m | CONFIRMED |
| v_ant (D15 quarantine) | 2.77e31, own; agrees R4 | v_ant = pi v = 2.765e+31; printed 8.9e34 absent from the computation | CONFIRMED |
| Omega(T_cr)-1 (D16 quarantine) | 1.29e-62, own; agrees R4 | 1/v^2 = 1.291e-62; printed 1.3e-70 absent | CONFIRMED |
| a_cr | 5.86e-4 m | a_cr = 5.86e-04 m | CONFIRMED |
| curvature correction to bounce root | ~2e-64, justified not assumed | exact root series: + Omega_Sm^2*Omega_minus1/Omega_R^3; relative 2.3e-64 | CONFIRMED |
| cusp: eps_eff(T_cr) > 0 closed form | 4 h_star^3 kappa/(81 alpha^2 h_n^4) > 0 | printed verbatim by B-R2 step 3 | CONFIRMED |
| cusp: \|beta-dot\| -> infinity | lim beta->beta_cr+ = oo | "lim_{beta->beta_cr+} \|beta_dot\| = oo" | CONFIRMED |

Full bracket table (doc section 2.3) also reproduces line by line: a_m^ 3.166e-33/1.292e-33,
a_m 9.338e-6/3.812e-6 m, Omega(min)-1 9.112e-64/1.519e-64, t 5.396e-46/8.993e-47 s,
v_a/c 1.041e32/2.549e32, eps_R incoherent 2.618e118.

Note (transparency, not a defect): the spin-fluid script computes eps_R only with the own
Omega_S and cites R2's 7.650e116 in a comment string; the equality the derivation claims
("reproducing audit R2 exactly") is arithmetic the script does not execute. This gate
executed it independently (row above): exact agreement. Claim stands.

## Check 2 — Seven kickoff requirements, audited against the document text

R1 fork declared, never blended — HOLDS. Section 1 header is literally "The fork, declared
(requirement 1)" with the two-treatment table (line 34-39); line 41: "They cannot be
blended; both are carried through in parallel." Both carried: section 2 (Treatment I),
section 3 (Treatment II), section 4 cross-treatment table; line 42: "Any downstream Phase 2
document citing 'the ECSK bounce' must name which treatment it means."

R2 Omega_S as bracket — HOLDS. Line 21-22: "Omega_S in [-8.8e-70, -1.5e-70] — a bracket,
not a number"; line 75: "Omega_S = -8.82e-70 (coherent edge) ... -1.47e-70 (incoherent
edge) (B-R1 step 7)"; line 77: "The published -8.6e-70 sits at the coherent edge (2.6%
inside it — constants rounding)." Sign and a^-6 scaling derived from own algebra (lines
52-57, B-R1 steps 1-3), erratum per Gate 1 (lines 82-87, see Check 4 below).

R3 quarantined numbers recomputed, never imported — HOLDS. Line 109: "the printed
1.1e116 is not used anywhere. Our recomputation: 7.27e116 (with our Omega_S) / 7.65e116
(with the printed Omega_S — reproducing audit R2 exactly)"; lines 139-142: v_ant "our own
computation; agrees with audit R4; the printed 8.9e34 (D15) is not used" and Omega(T_cr)-1
"our own; agrees with R4; the printed 1.3e-70 (D16) is not used". The 7.27-vs-7.65
discrepancy is explained, not hidden (lines 102-105, (8.82/8.6)^p factors). Rerun confirms
the printed values appear nowhere in either computation path.

R4 Planck-regime limit V1 on every derived quantity, A2-extended — HOLDS. Lines 168-173:
"V1 — Planck regime (Gate 1 condition 5): every bounce state above sits at or above the
Planck scale under classical field equations ... Per Gate 1 Check 4(c) this caveat also
covers the A2-certified T_max = 1.15e32 K ≈ 0.81 T_P and tau = 4.75e-45 s used downstream.
No quantity derived here is validity-clean." Also carried in section 0 (lines 26-28) and
the section 5 header ("all travel with every quantity above", line 166).

R5 n^2 marked ASSUMED-WITH-CITATION everywhere used; bracket to BOTH treatments — HOLDS.
Line 65: "The n^2-form itself is ASSUMED-WITH-CITATION (PLB 136-140, citing
Nurgaliev-Ponomariev; underived in the chain — audit H2 ...)"; Treatment II covered at
lines 146-148: "<s^2> = (3/4)n^2 (PRD line 100) uses the all-species total density squared
— the same V2-class assumption. Reducing the effective <s^2> by an incoherence factor f
multiplies T_cr by sqrt(f): for the equal-species illustration f = 6, T_cr -> 1.92 m_P";
V2 restated lines 174-177: "propagated — never collapsed to one edge."

R6 pinned sources only; no reliance on Goru sections 1/2/4 (Gate 1 condition 1) — HOLDS.
Lines 8-14: "All equations are re-derived here from the pinned full texts under sources/
(PLB TeX 95ba2de3…, PRD TeX 9ac75297…); no new fetches were needed ... per Gate 1
condition 1, sections 1/2/4 are excluded (no venues) — nothing below leans on them". Grep
of the full document: "Goru" appears once (that exclusion sentence); HRDCC/CMB/BBN content
absent. Gate spot-pin of the four cited line ranges against sources/ (this session):
  PLB main.tex 119-131 -> the Friedmann pair with (eps - kappa s^2/4), (p - kappa s^2/4),
    dots w.r.t. ct, and the conservation law: VERBATIM.
  PLB main.tex 136-140 -> "s^2 = (1/8)(hbar c n)^2": VERBATIM (the script's C_avg = 1/8).
  PRD cosmology_torsion.tex line 100 -> "<s^2> = (3/4)n^2": VERBATIM.
  PRD cosmology_torsion.tex 127-134 -> conservation law with alpha n^2 and the thermal
    forms eps = (pi^2/30) g_star T^4, p = eps/3, n = (zeta(3)/pi^2) g_n T^3: VERBATIM.

R7 lane-only writes, receipt discipline — HOLDS. Receipt scripts carry the p2b1_ prefix
with outputs alongside; no _tmp_ files remain in the lane; LANA_B1_DONE.md first line is
LANA_B1_COMPLETE.

No borrowed normalization presented as a result — HOLDS. Every asserted equation carries a
B-R1/B-R2 step reference or a pinned-source line range; the two quarantine replacements and
both new results (curvature correction, cusp quantification) are receipted, and all
rerun-verified above.

## Check 3 — Derivation spot-checks (executed symbolic algebra, not prose)

(a) The x6.00 coherence factor — present as executed algebra, receipt step 4. Rerun output,
quoted: "(4) E[s_tot^2] = 6*v = N*v (incoherent);  coherent (identical fields): (N)^2 v =
36 v  -> coherent/incoherent = 6". The script expands (sum s_i)^2 symbolically over six
species, kills cross terms under independence/zero-mean, and contrasts with the coherent
(sum-inside-the-square) count. The derivation's claim (doc lines 69-72) is what the code
does. CONFIRMED.

(b) The a^-6 conservation law from the Friedmann pair — present as executed algebra,
receipt step 1. Rerun output, quoted: "(1) dF1/dt with F2,F1 substituted = (pure factor) x
[conservation law]: factor = -kappa/(3*a(t)) -> law forced to 0 (a'!=0): True". The
residual after eliminating a'' via F2 and adot^2 via F1 is exactly the claimed -kappa/3a
times the law expression, free of eps/s2 — the law is forced, not assumed. Steps 2-3 then
print "n ~ a^-3 for any w: True" and "eps_S ~ a^-6 for any w: True". CONFIRMED.

(c) Gate's own independent pick — the Treatment II cusp closed form, verified from scratch
in one python3/sympy call (not re-running their script): substituting
T_cr^2 = 2 h_star/(3 alpha h_n^2) into (kappa/3)(h_star T^4 - alpha h_n^2 T^6) gives
exactly 4 h_star^3 kappa/(81 alpha^2 h_n^4) (difference simplifies to 0), strictly positive
for positive parameters — eps_eff(T_cr) > 0 holds and H != 0 at the minimum: the cusp
result is algebraically sound. CONFIRMED.

## Check 4 — Erratum at metadata level only (Gate 1 condition 2)

HOLDS. All four "erratum" mentions in the derivation are discipline statements, no content
claim: line 14 ("used at the metadata level only"); lines 82-87 ("existence and venue are
Crossref-confirmed at the metadata level (PLB 701, 672; DOI 10.1016/j.physletb.2011.05.047);
its content is UNVERIFIED-AT-GATE and nothing here attributes any specific correction to
it"); line 111 ("misprint-or-erratum-subject attribution stays open per Gate 1 condition
2"); lines 182-183 (V5 restatement). The Goru section-3 content claim Gate 1 flagged is
nowhere repeated. CONFIRMED.

## Cross-checks against TRACK_A1_AUDIT.md (consulted where cited)

Audit citations in the derivation resolve: H1 (incompatibility), H2 (averaging underived),
H4 (Planck regime), D7 (the PRD's verbatim disavowal), D13 (cusp prescription) all present
in the audit with matching content; R2 values (-8.82e-70/-1.47e-70, x6.00, 7.65e116) and
R4 values (T_cr 0.785 m_P, a_cr 5.86e-4 m, v_ant 2.765e31 -> doc rounds 2.77e31,
Omega(T_cr)-1 1.291e-62) match the audit's receipted rows exactly.

## Gate decision

PASS_P2_BOUNCE. Both receipts rerun clean and reproduce every gate-named headline; the two
receipt scripts execute (not assert) the two derivations this gate was told to demand, and
a third symbolic result was independently re-derived; all seven kickoff requirements hold
with quoted line evidence; the erratum stays metadata-only; zero fetches claimed, zero
fetches performed at this gate.

Flags carried to Track B step 2 (inheritance), none blocking:
1. The bounce state handed over is treatment-dependent and the two treatments disagree by
   two orders of magnitude on scale (doc section 4) — step 2 must name its treatment per
   quantity, per doc line 42.
2. V1/V2/V5 limits travel with every B1 quantity into any inheritance use; the incoherent
   edges (5.7e4 x eps_Planck; T_cr = 1.92 m_P) are the better-motivated ones given the n^2
   form (doc lines 78-80) and must not be silently dropped in favor of the coherent edge.
3. The Treatment II cusp is now receipted fact: nonsingularity there is a prescription,
   not dynamics — any inheritance claim built on Treatment II inherits V3.
4. Bookkeeping note only: if a future step wants the printed-Omega_S eps_R inside a receipt
   rather than as gate arithmetic, add the one-line scaling to the script; the number itself
   is confirmed (7.650e116 = audit R2).

— kimi, Track B step-1 gate, Phase 2, 2026-08-19. One file written. No host fetched.
portal.nersc.gov untouched.
