B1_REVIEW=CLASSES_WRONG

# KIMI B1 adversarial review — 2026-09-07

Referee: kimi (Moonshot), a seat that did not produce the algebra. Verdict: the no-production class
`B1_DEGENERATE_FINE_TUNED` STANDS — I re-derived it independently and it is corroborated by published
sources the lane did not lean on. But the fluid-row production class `B1_UNDERDETERMINED` is WRONG as
filed: the energy-transfer relation it declares absent ("the required one is named: J = 2Ψα_Fn. No
checked source prints it") IS printed in GRG 53, 18 — as Eq. (14), the first law for the effective
fluid, derived from the paper's own field equations, and restated as the entropy law Eq. (17).
Eq. (14) with Eq. (1) inserted is algebraically IDENTICAL to J = 2α_F n Ψ. The lane's own extraction
(SOURCES_20260907.md) skips Eqs. (12)–(14) and (17) — the same extraction-blindness failure mode the
lane documented in LANE_METHOD_NOTE_SHARED_INPUT_20260907.md hours earlier, repeated. One of the two
fluid-row classes fails, so the filed classes as a whole are wrong.

What I read for the physics: the arXiv HTML full text of 2007.11556v2 (the revised version that
identifies itself as the published GRG 53, 18), read by me today, in full. The Springer publisher page
remains behind the cookie handshake; I did not pass it. That split is stated, not blurred. PRD 85,
107502 and RMP 48, 393 equations below come from the lane's locally held APS publisher PDFs as
transcribed in PRD_PUBLISHER_VERIFY_20260907.md; I did not re-render those PDFs myself (disclosed in
the ledger).

## FINDING 1 (fatal, attack 3): J is printed in the paper. UNDERDETERMINED is refuted.

GRG 53, 18, §3, derives from its own field equations (10), via (12)–(13):

    (14):  d(ε̃ XY²)/dt + p̃ d(XY²)/dt = 0

and introduces it as "identical with the first law of thermodynamics" for a³ = XY². Expanding with
(1) (ε̃ = ε − αn², p̃ = p − αn²) and (16) (dV/dt = 3HV, V = XY²):

    (14)/V  =  ė − 2αnṅ + 3H(ε + p − 2αn²)  =  [ė + 4Hε] − 2αn[ṅ + 3Hn]  =  J − 2αnΨ

with p = ε/3, J := ė + 4Hε, Ψ := ṅ + 3Hn. That is EXACTLY B1's own energy-balance residual E_F, the
condition B1 says must be supplied. Machine check (`_tmp_kimi_j_check.py`, SymPy, exit 0):

    GRG(14)/V with p=eps/3  minus  B1 E_F = 0
    GRG(17) RHS/V  minus  2*a*n*Psi = 0

Eq. (17) is the same transfer written as the paper's entropy-production law: T d(sV)/dt = VJ =
2αnVΨ — i.e. the paper's own mechanism for the entropy increase its introduction says the scenario
needs. So the paper prints the required relation twice. The filed sentences — "unless an
energy-transfer term is supplied, and the required one is named: J = 2Ψα_Fn. No checked source prints
it" and "not because the answer is hard, but because an input is missing" — are false. The brief's
own test was explicit: if the paper supplies an equivalent energy-transfer/thermodynamic relation
elsewhere, the class UNDERDETERMINED is wrong. It supplies two.

What is actually true about the paper's production sector is the OPPOSITE of a missing input — it is
an internal contradiction. With the constant-coefficient thermal forms ε = h_*T⁴, p = ε/3,
n = h_nT³ (§9), the paper's own (14) reduces to

    (4h_*T³ − 6αh_n²T⁵)(Ṫ + HT) = 0,

so on any interval with production (Ṫ + HT = Ψ/(3h_nT²) ≠ 0 by the paper's own (37)), (14) forces
T² = 2h_*/(3αh_n²) — a single temperature, not an evolution. Machine check:

    Tdot required by (14)+thermal = -H*T
    Tdot printed as GRG (37)      = -H*T + Psi/(3*T**2*h_n)
    (14) residual when (37) holds = -2*Psi*T*(3*T**2*alpha*h_n**2 - 2*h_star)/(3*h_n)

GRG §9 solves {(36),(37),(11),(16)} ("Equations (36) and (37), with (11) and (16), determine the
time dependence of X, Y, and T") and never re-checks (14), which it had itself used for the
no-production case ("Without particle production, (1) and (14) give the constancy of XY²T³"). So the
correct diagnosis for the fluid row with production is one of:

  (a) the printed system {(9)–(11), (1), (34), (37), constant-coefficient thermal forms} is
      over-determined and inconsistent on any production interval — that is the prereg's own
      `B1_ILL_POSED`, not UNDERDETERMINED; or
  (b) if the constant-coefficient thermal specialization is relaxed, the general published system
      {(14), (34), field equations} is well-posed (B1's own C3 algebra shows the constraint then
      propagates), and whether production rescues the bounce is DECIDABLE from the published
      equations — merely uncomputed in this study. That would file as PRODUCTION_RESCUES or
      PRODUCTION_INSUFFICIENT after integration, not UNDERDETERMINED.

Either way the filed reason — "an input no source supplies" — cannot stand. Note also the result's
own framing "supply J and the system is well posed again" concedes the system is well-posed with J;
the paper already supplies J; the live defect is the conflict between the paper's (14) and its (37).

Consequence for the headline: "the Einstein–Cartan bounce is not generic" survives only in its
no-production half. "The mechanism that would rescue it is underdetermined as published" does not
survive: the mechanism is determined-as-published (via (14)) and inconsistent in its thermal
specialization, and the rescue question is computable and was not computed.

Root cause, for the record: SOURCES_20260907.md §B/S1 transcribes Eqs. (9),(10),(11) then jumps to
(15); Eqs. (12)–(14) and (17) were never extracted, so every seat that worked from the extraction
inherited the blind spot — the exact pattern of LANE_METHOD_NOTE_SHARED_INPUT_20260907.md.

## FINDING 2 (attack 1 failed): the central a⁻⁶ degeneracy survives, independently re-derived.

I derived the shear evolution myself. Bianchi I, ds² = −dt² + Σaᵢ²dxᵢ², Hᵢ = ȧᵢ/aᵢ, H = ΣHᵢ/3,
σ² = ½Σ(Hᵢ−H)². In Einstein–Cartan the connection equation is algebraic; after eliminating torsion
the field equation is the Levi-Civita Einstein equation sourced by the combined tensor (RMP (3.23)–
(3.24), quadratic in spin only — no metric derivatives, so no shear–torsion coupling can enter
geometrically). For the unpolarized Weyssenhoff fluid (RMP (5.18)), the derivative terms are linear
in spin and average to zero under the declared unpolarized average; the surviving source
(ρ+P−2κs²)uⁱuʲ + (P−κs²)gⁱʲ has ISOTROPIC spatial stress. The spatial Einstein equations then give,
for each direction, Ḣᵢ + 3HHᵢ = κ(ρ−P)/2 — the same right-hand side for all i — so subtracting any
two gives d(Hᵢ−Hⱼ)/dt + 3H(Hᵢ−Hⱼ) = 0, hence Hᵢ−Hⱼ ∝ a⁻³ and σ² = Σ²/a⁶ exactly. The only way
torsion could modify the shear law is an anisotropic stress or a spin–velocity-gradient correlation
(the τ·∇u term in (5.18)); both are excluded by the prereg's declared unpolarized, isotropic-stress
assumption (B1_CRITERION assumptions 2 and 4 declare this explicitly). Within the filed model the
shear law is unmodified. The torsion term αn² ∝ a⁻⁶ with conserved n; both coefficients are constant
(d(Sa⁶)/dt = 0, d(αn²a⁶)/dt = 2αna⁶Ψ = 0 without production — re-derived, and printed by the script).

Corroboration the lane did not cite: RMP's own printed Bianchi-I-type example (5.24) carries exactly
2σ₀²a₀⁶/a⁶ − k²s₀²a₀⁶/a⁶ — the same a⁻⁶ degeneracy, in the formalism anchor itself. And GRG's
introduction cites published peer-reviewed results — Kopczyński, Phys. Lett. A 43, 63 (1973);
Kuchowicz, J. Phys. A 8, L29 (1975); Tafel, Phys. Lett. A 45, 341 (1973) — that a Bianchi I universe
in EC "has no cosmological singularity if the effect of torsion is greater than that of shear": the
constant-comparison structure is the published result, not a new claim. (GRG's own §7 text "shear
grows faster than a⁻⁶" is its KS curvature-sourced law (30); Bianchi I is flat and lacks that source
— the lane's KS/Bianchi-I distinction here is correct.)

The criterion follows: 3H² = κε₀a⁻⁴ + (Σ² − κα_Fn₀²)a⁻⁶; H = 0 at finite a ⟺ κα_Fn₀² > Σ²,
a_min² = (κα_Fn₀² − Σ²)/(κε₀); equality or reverse inequality gives no finite positive root
(singular). At the root, Ḣ_b = κε₀/(3a_min⁴) > 0 — a smooth local minimum of the mean scale factor.
I verified every step by hand; b1_criterion.py (run by me, exit 0) asserts the same, including the
three-direction geometric component checks. `B1_DEGENERATE_FINE_TUNED` stands.

## FINDING 3 (attack 2 failed): alpha-independence holds on its domain.

The criterion is a comparison of κα_Fn₀² against Σ²; for every α_F > 0 the character is the same
constant inequality. The only boundary is α → 0⁺, where the allowed shear interval Σ² < κα_Fn₀²
collapses to the shear-free point — which makes the bounce MORE fine-tuned, not generic; the filed
class is unchanged. α < 0 would kill the bounce outright but is excluded by the model (α_F > 0
derived, ecsk_derive.py exit 0). Time-dependent α is outside the declared model (α carried as a
constant interval parameter, declared). No case found where α's value changes the character of the
answer within the stated domain.

## FINDING 4 (attack 4 verified): the ratio claim is correct, with one notation nit.

At the H = 0 root the constraint gives καn_b² = κε_b + S_b, hence
R = |δρ|/ε = αn_b²/ε_b = 1 + S_b/(κε_b) ≥ 1, equality iff S_b = 0, diverging as Σ² → καn₀².
The RESULT's formula καn₀²/(καn₀² − Σ²) matches (verified by hand and by the script). Nit:
RESULT §2 writes the symbol "|ε̃|/ε" using the K3/PRD tilde (correction) while the same document's
fluid row elsewhere uses GRG tildes (totals); B1_CRITERION discloses the distinction explicitly, the
RESULT does not re-disclose it at that sentence — but its words ("the ratio of the torsion
correction") are correct, so this is a disclosure nit, not an error. The GRG-literal ratio
|ε̃_GRG|/ε = Σ²/Δ is correctly handled in B1_CRITERION.

## FINDING 5 (scope policing): two sentences to quote; otherwise clean.

(a) RESULT §2: "So the bounce always sits where the spin correction is at least the whole ordinary
energy density — an order of magnitude past the 0.1 small-correction threshold K3 step 3 declared,
in both rows and across the entire α interval." — For the DIRAC row there is no dynamically attained
bounce at all (C3_DIRAC_NO_PRODUCTION=FAIL; the root is FORMAL_ONLY). This sentence lets a fluid-row
physical statement pass as a Dirac-row one without the FORMAL_ONLY qualifier that §1 correctly
attaches. The underlying conditional algebra is fine (B1_CRITERION states it conditionally); the
sentence as written over-extends it.

(b) RESULT §2: "Our own K3 result ... therefore applies a fortiori: the regime that produces the
bounce is the regime where the closure supplying its strength is not under control." — This is an
inference, not a computed result. K3's 2/3 and 0.32 T_cr are Dirac-row numbers; Amendment 1 itself
records that the fluid row's closure control at its own turning point "has not been computed by
anyone here". Partial support exists (C1_REEXAM computes R_F = 1 formally at the fluid turning
point, and K3S1 found the ℏ²/8 closure to be a convention, not a derivation), so the sentence is
defensible as an argument — but it transfers a Dirac-row computation across rows, the exact move
Amendment 1 flagged. Flagged, not counted as an error.

Clean elsewhere: RESULT §0 ("Nothing below is a statement about the literal KS system"), §3's
non-address list, prereg §7, and C1_REEXAM's literal-KS qualification (shear-free KS forces
−1/Y² = 0, impossible) are exactly the right scope controls. No Bianchi-I statement passed as KS;
no reduction result passed as a genericity answer beyond the flagged sentences.

## FINDING 6 (what the algebra shows that the result did not claim; other claims checked).

- The DIRAC row's UNDERDETERMINED label is questionable for the same reason as Finding 1, though the
  underlying FAIL is real and verified (residual −6Hα_Dκn², re-derived by hand and by the script).
  PRD's own first law for the total fluid exists (it is what yields PRD's Eq. (14)); the failure is
  that the prereg-IMPOSED simultaneous scalings ε ∝ a⁻⁴, n ∝ a⁻³ are incompatible with the Dirac
  w = −1 correction pair — an inconsistency of the imposed test system, not an input missing from a
  source. The result's own words ("with conserved particle number the ε̃ = −p̃ pair is not separately
  conserved") are the accurate statement; the class label sits loosely on it.
- The smooth-bounce conclusion (Ḣ_b > 0, a genuine local minimum of the mean scale factor — a real
  contrast with the Dirac cusp) is proved by the algebra and claimed in B1_CRITERION but not in the
  RESULT. Minor unclaimed support.
- The sharp trichotomy (equality Σ² = καn₀² is singular; reversed inequality singular) is in
  B1_CRITERION; RESULT could state it. Minor.
- All printed residuals in RESULT §1 match the script output and my hand derivations exactly:
  2Ψα_Fκn (number-only), 2Ψκ(3α_Fn² − 2ε)/(3n) (thermal), −6Hα_Dκn² (Dirac no-production),
  required J_F = 2α_FnΨ, J_D = 2α_DnΨ − 6Hα_Dn². C2 tensor residuals are zero matrices as claimed.
  c1_reexam.py (exit 0) and ecsk_derive.py (exit 0) reproduce every token they print, and the
  ecsk script's asserts (24/24 Hessian rank, Weyssenhoff ε_s = p_s = −κCn²/4, w = 1, continuity
  residual 0, opposite-pressure trial 3CHκn²/2) match my independent variation of the same action.

## Failed attacks (what I tried that held)

1. Shear-scaling refutation — failed: derived the shear law independently; torsion cannot enter it
   in the declared model (algebraic elimination, isotropic effective stress). Corroborated by RMP
   (5.24) and by the published Kopczyński/Kuchowicz/Tafel Bianchi results GRG cites.
2. Alpha-dependence — failed: no α > 0 case changes the character; α → 0⁺ only sharpens fine-tuning.
3. Ratio claim — failed: R ≥ 1 with equality iff Σ² = 0 is forced by the constraint balance itself.
4. Script-token distrust — failed: all three scripts run clean (exit 0) under /usr/bin/python3 and
   every token I spot-derived by hand (constraint residuals, required J, criterion, root, ratio,
   Ḣ_b, Dirac cusp algebra, ECSK fluid stress) matches. No hard-coded result literals found on
   reading the scripts.
5. DIRAC-row C3 failure — tried to find it spurious; it is real and correctly diagnosed as the
   w = −1 versus a⁻⁶ tension.

## Evidence ledger

- Read in full: B1_PREREG (incl. Amendment 1), B1_RESULT, b1_criterion.py, c1_reexam.py,
  ecsk_derive.py, B1_SIGN_RESOLUTION, SOURCES_20260907.md (all 795 lines), PRD_PUBLISHER_VERIFY,
  B1_CRITERION, B1_DERIVATION, C1_REEXAM, ECSK_DERIVATION, KIMI_SIGN_CHECK,
  LANE_METHOD_NOTE_SHARED_INPUT, K3S3_CHECK_SHEET_20260904.md (matches SOURCES §D quotes).
- Ran (all exit 0): /usr/bin/python3 ecsk_derive.py; b1_criterion.py; c1_reexam.py;
  _tmp_kimi_j_check.py (my own; printed identities above).
- Paper check for Finding 1: arXiv 2007.11556v2 HTML full text fetched and read by me in full
  (abstract through references); Eqs. (14), (17), (33)–(38), §9 line "Equations (36) and (37)...
  determine the time dependence", §11 approximation statements all read in place. This is the
  revised arXiv version identifying itself as the published GRG 53, 18 — an extraction of the
  publisher-corresponding text, read as a page, not the lane's extraction. Springer publisher page:
  not passed (cookie wall), same limitation the lane declared.
- PRD/RMP equations: relied on the lane's locally saved APS publisher PDFs as transcribed in
  PRD_PUBLISHER_VERIFY_20260907.md; I did not re-render the PDF pages myself. The C2 assertions in
  b1_criterion.py compare against those transcriptions and pass.

## Uncertainties and what I did not inspect

- I did not survey later literature for errata/corrections to GRG 53, 18; if an erratum withdraws or
  repairs (14)/(37), Finding 1's quotation base changes. No such erratum is recorded in the lane's
  checked records.
- My identification of (14) as holding under production rests on the paper printing no creation
  pressure or production-modified stress tensor (it prints none; §9 keeps (1) unchanged). If a
  reader repairs GRG with an external creation-pressure model, that repair — not the paper — could
  restore consistency; that would be a new input from outside the published text, which is what the
  prereg menu calls a next study, not this one.
- I did not recompute K3's 2/3 from the K3 scripts; I verified the check sheet matches the quotes
  the B1 documents carry.
- I did not verify the Springer page; the arXiv-vs-publisher equation identity for (14)/(17)
  specifically is covered only by the lane's claim that its publisher read matched the extraction —
  which did not include (14)/(17). That residual risk is stated plainly: my Finding 1 quotes are
  from the arXiv v2 full text.

## Bottom line for the coordinator

Filed classes should NOT stand as a set. `B1_DEGENERATE_FINE_TUNED` (fluid, no production) stands —
independently verified and published-corroborated. `B1_UNDERDETERMINED` (fluid, with production) is
refuted by the target paper's own Eq. (14)/(17): the named "missing" input J = 2Ψα_Fn is printed in
GRG 53, 18 as the effective first law and again as the entropy law. The honest re-filing is either
`B1_ILL_POSED` for the paper's printed thermal production system (its (14) and its (37) conflict on
any production interval with constant thermal coefficients), or a computed PRODUCTION_RESCUES /
PRODUCTION_INSUFFICIENT from the well-posed general system {(14), (34), field equations}. This
report repairs nothing; it reports.

B1_REVIEW=CLASSES_WRONG
