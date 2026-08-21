PASS_P2_STAGE1

# Miru — Phase 2, Gate 1 (stage 1): audits + ingredients verification
Fresh one-shot, 2026-08-19. Lane dir only. Findings-only; nothing edited; this is the
only file written. Fetches: api.crossref.org ONLY. portal.nersc.gov untouched.

## Check 1 — Receipts rerun (python3, this session, this machine)

All three receipts executed clean (exit 0). Every brief-named headline number reproduces:

| Headline | Audit claim | Rerun result | Verdict |
|---|---|---|---|
| A1 Omega_S coherent | recomputed -8.8e-70 vs published -8.6e-70 | Omega_S (n_total coherent) = -8.820e-70 | CONFIRMED |
| A1 cross-species coherence | worth x6.00 | incoherent -1.470e-70, printed "factor 6.00 smaller" | CONFIRMED |
| A1 PLB epsilon_R | off by x6.95 | eps_R = 7.650e+116 vs paper 1.1e116, "ratio 6.95" | CONFIRMED |
| A1 PLB bounce density | approx 1650x Planck | eps_R/eps_P = 1651.2 | CONFIRMED |
| A1 PRD T_cr | = 0.785 m_P | T_cr = 0.785 m_P (g_star=106.75, g_n=67.5) | CONFIRMED |
| A2 A-8 exponent misprint | (adot/c)^3 = (Omega-1)^(-3/2), paper prints -3 | R0: PASS identity, "paper prints (Omega-1)^(-3): ERROR" | CONFIRMED |
| A2 A-9 undeclared a_i = 1 m | printed block holds only at a_i=1 m, vs 1e4 m two lines later | R1: 4c*tau=5.7e-36 m; a_i=1m -> 5.7e-36 & N=7.35e52; a_i=1e4 -> 5.7e-40 & 7.35e58; "matches a_i = 1 m" | CONFIRMED |
| A2 B-14 closure contradiction | textual | source-pinned below (receipts carry no numeric for it) | CONFIRMED at source |
| A2 B-19 g_b = 29 vs 28 | typo-class, effect <0.5% on T_max | R6: g_b=28 -> T_max 1.152e32 K; g_b=29 -> 1.158e32 K; "< 0.5%"; source-pinned below | CONFIRMED |

Collateral confirmations in the same runs: PLB P9-P12 all reproduce (a_m^ 3.126e-33,
a_m 9.22e-6 m, Omega-1 8.884e-64, t 5.261e-46 s, v_a 1.054e32 c, N 1.17e96); PRD D15/D16
internal-inconsistency mechanics reproduce exactly (v_ant = 8.850e34 only with the a_r->a_0
slip; own-definition 2.765e31; Omega(T_cr)-1 = 1.291e-62 own-inputs vs printed 1.3e-70);
A2 R3 (Tolman Einstein tensor, five components), R4 (homogeneous reduction), R5
(turning-point threshold, symbolic difference 0), R7 (trace identity) all PASS.

### Spot-checks of my choice (grep/sed extraction from pinned sources/ only)

CHECK row — A1 P9 (PLB a_m^ and a_m). sources/1007.0587/main.tex:
  line 222: \hat{a}_m=\sqrt{-\frac{\Omega_S}{\Omega_R}}=3.1\times10^{-33},
  line 225: ...minimum but finite scale factor ... $a_m=9\times10^{-6}\,\mbox{m}$.
Matches the audit row and the R2 recomputation (3.126e-33; 9.22e-6 m). CHECK stands.

ERROR row — A1 D15 (PRD v_ant). sources/1111.4595/cosmology_torsion.tex:
  line 277: v_\textrm{ant}(T_\textrm{cr})\approx 8.9\times 10^{34}
Pinned print confirmed; R4 shows it reproduces ONLY under the a_r->a_0 substitution
(8.850e34 -> matches: True) while the paper's own a_eq definition gives 2.765e31. ERROR
stands, including the audit's exact-slip attribution.

Headline source-pins completed (textual A2 rows):
  B-14: sources/2509.11468/Collapse.tex line 230 "The value of $R_0$ does not change."
        vs line 281 "$\sin R_0$ decreases and $R_0\to\pi$ (completely closed universe)";
        with line 206 sinR_0=(r_g/r_0)^{1/2} fixing the R_0<pi/2 branch. Contradiction
        verbatim at source. ERROR stands.
  B-19: Collapse.tex line 152 "For standard-model particles, $g_b=29$ and $g_f=90$."
        vs sources/1410.3881/Universe.tex line 293 "$g_\textrm{b}=28$ and
        $g_\textrm{f}=90$". Both prints pinned. ERROR (typo-class) stands.

## Check 2 — Erratum record (api.crossref.org only)

GET https://api.crossref.org/works/10.1016/j.physletb.2011.05.047 — status ok. Metadata
returned, quoted:
  title:    Erratum to "Cosmology with torsion: An alternative to cosmic inflation"
            [Phys. Lett. B 694 (2010) 181]
  author:   Nikodem J. Poplawski
  container-title: Physics Letters B; volume 701; issue 5; page 672
  published-print: 2011-07; created 2011-05-27; publisher Elsevier BV
  type: journal-article; ISSN 0370-2693; DOI 10.1016/j.physletb.2011.05.047
  relation: {} ; abstract: none ; reference-count: 0

RESOLVED at the metadata level: the record exists and self-identifies in its title as the
erratum to Phys. Lett. B 694 (2010) 181. A1 H5's existence question closes.

UNVERIFIED-AT-GATE: the erratum's CONTENT. Crossref returns no abstract, no references,
no relation entry, and no full text; the sole permitted host cannot say what it corrects.
Consequences: (i) Goru ingredients section 3's sentence that the erratum "addresses
corrections to the magnitude and sign of the derived torsion density parameter Omega_S" is
an unattributed content claim — NOT supported by anything verifiable at this gate and
flagged accordingly; (ii) A1 P13 (epsilon_R x6.95) attribution stays open exactly as A1
left it: error vs erratum-subject unresolved, number quarantined either way.

## Check 3 — Ingredients discipline (GORU_P2_INGREDIENTS vs the brief's quotes+venues bar)

Item-by-item venue check:

- Section 1 (three spin-fluid critique quotes): NO named venue, author, journal, or DOI for
  any of the three. Ruling: NOT-USABLE-AS-PUBLISHED-INGREDIENTS. Note for the record:
  quotes 1-2 closely paraphrase the PRD paper's own self-critique ("not self-consistent",
  "violates the cosmological principle"), which A1 pinned verbatim to D112-115 — the
  CONTENT survives via A1's primary-source pin, but as ingredients these quotes fail the
  venue bar. Quote 3 (CMB/BBN ruling out a^-6 scaling) is unattributed and otherwise
  unsupported in this lane.
- Section 2 (HRDCC parent-inheritance, two quotes): NO named venue. Ruling:
  NOT-USABLE-AS-PUBLISHED-INGREDIENTS. Conflict adjudication below.
- Section 3 (erratum trail): venues named and specific (PLB 694, 4-5, 181-185, 2010; PLB
  701, 5, 672, 2011) — traceable, and the erratum half is now Crossref-confirmed (Check 2).
  Ruling: venue part USABLE; the appended content claim (Omega_S magnitude/sign) is
  UNVERIFIED-AT-GATE and must not be quoted as established.
- Section 4 (interior-vorticity/torsion bounds quote): NO named venue. Ruling:
  NOT-USABLE-AS-PUBLISHED-INGREDIENT. The CMB/BBN bound on a^-6 scaling needs a named,
  pinned source before P2_CONFRONTATION may lean on it.

CONFLICT ADJUDICATION — ingredients item 2 vs both audits:
Item 2 asserts published parent-inheritance prior art (HRDCC: "rotational degrees of
freedom are preserved through the transition... the new universe inherits [the twist]").
A1 section 3 item 3: "The inheritance step (M, a* -> interior) has no published seed in
these two papers (P19: narrative only)." A2 focus finding 2.3: "There is no parent-spin
variable, no Kerr collapse, no angular-momentum transport, and no interior vorticity/axis
quantity anywhere in the audited chain... must therefore be built, not audited."
RULING: the audits prevail for this chain. They examined the four spine papers
equation-by-equation with receipts; item 2 offers no venue, no author, no quote source,
and — even if an HRDCC publication exists — it is not an ECSK parent->interior inheritance
calculation in the Poplawski chain the brief scoped. Item 2 is excluded from the Track B
base. The transfer function remains a Track B construction task; Phase 1's epsilon/f_b
parameterization stays live for spin inheritance and must be named as such (both audits
concur on this consequence).

## Check 4 — Cross-seat adjudication (A1 vs A2)

(a) Spin-fluid averaging step underived — AGREEMENT. A1: P5 and D5 both
"UNSUPPORTED-BY-DERIVATION" ("never derived"; both insert the all-species total inside the
square). A2: A-2 "ASSUMED-FROM-CITATION... it lives in A1's papers"; B-1 "drops the
spin-divergence term from G^ij without displaying the averaging step (cited)". No
disagreement to quote.

(b) Absence of any published spin-inheritance transfer function — AGREEMENT, explicit on
both sides. A1 section 3(3): "no published seed in these two papers (P19: narrative
only)". A2 focus 2(3): "Spin a* — absent... Any parent-spin->interior-axis transfer
function must therefore be built, not audited, and the published chain provides no
equation to start from." No disagreement to quote.

(c) Planck-regime classical-validity caveat — ASYMMETRY, not contradiction. A1 carries it
as named verdicts: H4 ("Both bounces sit at or above the Planck scale... Every downstream
claim inherits this"), P15 and D18 "UNSUPPORTED (regime)". A2 issues NO regime verdict:
its recomputed T_max = 1.152e32 K (A-4, ~0.81 T_P) and tau = 4.751e-45 s (A-5, ~88 t_P)
sit in the same near-Planck regime but are verdicted CHECK (arithmetic) with the validity
question unaddressed. The audits do not disagree on any number; A2 is simply silent where
A1 flags. Gate note for Track B: A1's H4 caveat applies to A2-derived quantities too —
T_max is within a factor ~1.2 of the Planck temperature, and the strict model must carry
the named validity limit across the whole chain, not just the A1 half.

## Gate decision and conditions carried into Track B

PASS. Both audits' receipted claims reproduce under independent rerun; their textual ERROR
rows pin to source verbatim; they agree on every cross-seat question put to this gate.

Conditions/flags that travel forward:
1. Goru ingredient sections 1, 2, 4 are excluded as published ingredients (no venues);
   section 3 usable for the erratum venue only. If Track B needs the spin-fluid-averaging
   critique or CMB/BBN a^-6 bounds, those must be re-acquired as named, pinned
   publications first.
2. Erratum CONTENT stays UNVERIFIED: epsilon_R(a_m^) remains quarantined (use R2's
   7.65e116, never the printed 1.1e116); likewise v_ant and Omega(T_cr)-1 per R4.
3. The A1 fork ruling stands untouched: spin-fluid (w=+1) vs Dirac (w=-1, cusp
   prescription) must be declared, not blended.
4. A2's usable exact results for Track B: the M->(a_0,T_0,R_0) map, T_max, tau,
   beta-window — all confirmed at this gate. B-13/B-14/B-17 mean closure, shear survival,
   and rotation come from the published chain as nothing more than assertions.
5. Planck-regime validity caveat extends over A2 quantities per Check 4(c).

— Miru, Gate 1 (stage 1), Phase 2, 2026-08-19. One file written. api.crossref.org the
only host fetched. portal.nersc.gov untouched.
