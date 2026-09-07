B5_REVIEW=ABSENCES_HOLD

Kimi adversarial referee pass on `B5_VALIDITY_20260907.md`, 2026-09-07. Brief: break four ABSENCE claims by finding the thing claimed missing. I attacked all four rows with fresh literature searches, attacked row (iii) hardest with a source B5 does not cite, and spot-re-verified B5's bound quotes in its own local publisher copies. None of the four NOT-ESTABLISHED verdicts broke. One wording slip found (header says "three assumptions"; the report assesses four rows). Several available reinforcements B5 did not use are recorded as understatements; they strengthen B5 and change no verdict. I repaired nothing.

=====================================================================
1. ROW-BY-ROW ATTACK RESULTS
=====================================================================

----- Row (i): macroscopic Weyssenhoff spin-fluid averaging at R_F >= 1 — HOLDS

Sources tried, beyond B5's set:

- Brechet, Hobson, Lasenby, CQG 24, 6329 (2007), "Weyssenhoff fluid dynamics in general relativity using a 1+3 covariant approach." READ: arXiv abstract only (arXiv:0706.2367v2; journal-ref CQG 24:6329). A dynamical/constraint analysis; no validity window in what I read.
- Brechet et al. 2008 (the paper B5 cites) — I re-read B5's own local publisher text (`b5_sources/brechet2008_publisher.txt`) beyond the quoted lines. Its abstract's "provided that the spin density exceeds the rate of shear" (lines 20-25) is a BOUNCE CONDITION, not a validity window for the averaging. Its §3.2 (lines 284-294) is exactly the conditional assumption B5 quotes ("assumed to be randomly oriented"); §4 (lines 316-321) confirms the perfect-fluid reduction happens only AFTER the averaging is imposed. No error estimate, no density window.
- Obukhov & Korotky, CQG 4, 1633 (1987), "The Weyssenhoff fluid in Einstein-Cartan theory." READ: ADS/Inspire abstracts + citation snippets only (IOP article page not fetched). Variational theory and effective-fluid reduction; no validity window in anything I read.
- Gasperini, PRL 56, 2873 (1986), "Spin-dominated inflation in the Einstein-Cartan theory." READ: APS publisher ABSTRACT page (journals.aps.org/prl/abstract/10.1103/PhysRevLett.56.2873). It USES the spin-dominated regime for inflation; the abstract supplies no validity condition.
- Ziaie, Ranjbar, Sepangi, EPJC 74, 3154 (2014), "Einstein-Cartan gravitational collapse of a homogeneous Weyssenhoff fluid." READ: Springer article page partial extract (open-access page, not the PDF). It assumes the averaged spin fluid (its Eqs. (14)-(17) averaging rules) in a collapse and computes bounces; no validity condition stated in what I read.
- PRD 107, 084004 (2023), "Relativistic cosmology and intrinsic spin of matter: Results and theorems in Einstein-Cartan theory." READ: search-result abstract snippet only. No validity window.
- Nomura, Shirafuji, Hayashi, PTP 86, 1239 (1991), "Spinning test particles in spacetime with torsion." READ: citation snippets only. Test-particle dynamics, not a fluid-validity derivation.
- A dedicated search for breakdown statements ("spin fluid" torsion cosmology "breaks down"/"ceases to be valid" high density) returned only GR->U4 transition statements and Popławski's own methodology critiques (already in B5).

Nothing found establishes the averaging at spin term >= whole ordinary density, and no sufficient validity window containing that regime surfaced. The necessary-condition situation is exactly as B5 states (Hehl 1974 quote re-verified locally, see §5). Row (i) NOT ESTABLISHED survives.

----- Row (ii): ideal ultrarelativistic thermal matter used with it — HOLDS

GRG §9's "kinetic equilibrium" stipulation was spot-verified in the saved publisher HTML. I searched standard-cosmology EoS/equilibrium literature for anything establishing the description in this regime or giving an equilibration-rate window. What exists assumes equilibrium FLRW without torsion or a production source; nothing I found computes equilibration against deformation at a sheared, spin-dominated bounce. READ: search-level only; no publisher full text read for this row; I therefore make no stronger claim than: I found no source that breaks it. Row (ii) NOT ESTABLISHED survives.

----- Row (iii): persistence of the unpolarised isotropic average under strong sheared contraction — HOLDS (attacked hardest; see §2)

----- Row (iv): fixed-beta, beta*H^4 through an entire collapse — HOLDS, and reinforceable

- B5's §3 inventory quotes were spot-verified against the saved publisher HTML: "phenomenologically given by" (present), "contracting or expanding universe" (present), "too small"/"too big" (one occurrence each), "kinetic equilibrium" (present), Eq. (33) anchor (present), and the "only approximate" admission (6 raw hits = 3 distinct statements, each duplicated once in the markup — B5's "all three occurrences" is correct).
- GRG's own reference [14] for the production prescription is Popławski, ApJ 832, 96 (2016), "Universe in a black hole in Einstein-Cartan gravity" (I extracted GRG's reference list from the saved HTML myself). The IOP publisher page is Radware-bot-walled — B5's logged failed access is genuine; I confirmed the captcha artifact locally (`b5_sources/pop2016_publisher.html`). I instead read the arXiv copy, arXiv:1410.3881v2, whose header prints "The Astrophysical Journal 832 (2), 96 (2016)" and whose comment says "published version". CUSTODY FLAG: this v2 was revised 2026-05-26; my wording is bound to the arXiv copy, not to the 2016 version of record.
  In §6 of that copy, the production scalar is explicitly an ANSATZ: "At a bounce ... the rate of production of particles (and thus K) should vanish", "A scalar, vanishing for [effective density] = 0 ... is proportional to K = P^2 - 3 P_ik P^ik", "Ultimately, K should be derived from quantum field theory in the Riemann–Cartan spacetime of the ECSK theory of gravity", and "The simplest form of K that vanishes at a bounce and has the same dimension as P^2 is K = beta(kappa epsilon-tilde)^2". The source lineage itself records that the microscopic derivation does not exist and that the vanishing of production at the turning point is IMPOSED, not derived. This directly confirms B5's §3 observation ("that is a property of the ansatz") from GRG's own cited predecessor.
- Microscopic production literature, checked independently: Zel'dovich & Starobinsky, JETP Lett. 26, 373-377 (1977), "Rate of particle production in gravitational fields." READ: FULL TEXT from the journal's own site (jetpletters.ru PDF). It computes the local production rate of massless conformal particles: (1/960 pi) C_iklm C^iklm (scalar; 1/320 pi neutrinos; 1/80 pi photons; gravitons R^2/288 pi), under explicit conditions: weakly anisotropic Bianchi I to second order in anisotropy; massless (massive admissible if hbar^-4 m^4 << |Riem^2|); locality fails at higher orders. This is peer-reviewed, supplies explicit validity conditions — and has a DIFFERENT functional structure from beta H^4: in a sheared flat Bianchi I at H=0 the Weyl invariant built from shear need not vanish, so the published microscopic rate does not share the ansatz's imposed zero at the turning point. Its perturbative conditions also do not contain this route's strong-shear collapse. Beilin et al., Sov. Phys. JETP 51, 1045 (1980): seen only through ApJ 2016's Eq. (39) use and its reference entry (massive spin-1 rate (c/288 pi) P^2); same conclusion, same custody caveat.
- No source found establishes beta H^4 with fixed beta through an entire collapse. Row (iv) NOT ESTABLISHED survives, with published reinforcement available (§4).

=====================================================================
2. THE STRONGEST ATTACK: (iii), spin polarisation under shear
=====================================================================

NEW SOURCE B5 DOES NOT CITE: B. Fu, S. Y. F. Liu, L. Pang, H. Song, Y. Yin, "Shear-Induced Spin Polarization in Heavy-Ion Collisions", Phys. Rev. Lett. 127, 142301 (2021). Peer-reviewed (PRL). READ: arXiv:2103.10403v1 FULL HTML (theory, conditions, results, references); journal-ref confirmed on the arXiv page and via the APS listing in search results. I did not read the APS publisher page itself.

What it establishes (bound to the arXiv copy I read):
- At first order in hydrodynamic gradients, a thermal relativistic fluid develops an explicit shear-induced polarization (SIP): their Eq. (4), A^mu_SIP = -beta n0(1-n0) (p_perp^2/epsilon0) epsilon^{mu nu alpha rho} u_nu Q_alpha^lambda sigma_{rho lambda} — quadrupolar in momentum space via the tensor Q, arising from the magnetic-current term. Derived two ways: chiral kinetic theory (massless) and one-loop linear response (arbitrary mass), the latter matching the gradient expansion to the small-frequency behaviour of a retarded axial-Wigner/stress correlator.
- In a data-calibrated QGP hydrodynamic model (MUSIC, AMPT initial conditions, sqrt(s_NN)=200 GeV), SIP competes with thermal-vorticity effects in the DIFFERENTIAL (azimuthal) polarization; in the "strange memory" scenario SIP dominates and matches the data's qualitative angle dependence; they varied EoS/viscosity/freezeout and found the sign pattern generic.
- Critical nuance in B5's favour: "the contribution from SIP and TIP to GLOBAL polarization is insignificant" — a published, quantitative instance of B5's own argument that "a momentum-dependent quadrupole can cancel in an integrated mean."

Regime conditions (as printed): local-equilibrium distribution; slow gradient expansion ("slow varying flow velocity and temperature"); free/weakly-coupled quasiparticle content; QGP at ~150-200 MeV; freezeout hypersurface prescription; no gravity, no torsion, no spin-curvature feedback.

Transfer to the R_F >= 1 Bianchi I contraction: NONE published that I could find, and the gap is not cosmetic — the EC bounce regime lacks a local-equilibrium small-gradient expansion at the turning point and adds spin-torsion coupling the hydrodynamic calculation never includes. Fu et al. therefore establishes neither persistence nor failure of the isotropic average HERE. It makes the worry concrete (shear DOES induce calculable spin structure in a relativistic fluid at first order) while its global-insignificance result cuts the other way for the net first moment. Both directions remain regime-bound. B5's symmetric sentence — "Both a negligible response and a dynamically important response in this particular regime are NOT ESTABLISHED" — is exactly the right calibration, and survives this source.

Supporting checks:
- B5's Becattini and Liu-Yin bound quotes re-verified in B5's own local publisher texts: "also the shear tensor contributes" (becattini2021_publisher.txt line 24) and the free/quasi-free field restriction (line 236); the relaxation-time small-gradient condition (liu_yin2021_publisher.txt lines 182, 291).
- Spin-relaxation timescale literature exists (e.g., PR C 101, 024907 (2020), "Relaxation Time for Strange Quark Spin in Rotating Quark-Gluon Plasma") — READ: search-result description/snippet only; QGP-specific; no transfer to this regime claimed or found.
- Barnett/Einstein-de Haas analogues: those channels are rotation-driven (vorticity-coupled); the Bianchi I congruence in this route is irrotational (Brechet's model is "homogeneous and irrotational"), so the equilibrium, Barnett-type polarisation channel vanishes and the first-order SHEAR channel (SIP above) is the relevant one. INFERENCE from the sources read, labelled as such.
- EC-side: Brechet's unaveraged source carries the explicit shear-spin term (B5 quotes it; I re-read the surrounding local text). Published EC models with ALIGNED (polarised) spin in anisotropic cosmologies exist — Kopczyński, PLA 39, 219 (1972) and PLA 43, 63 (1973), per GRG's own reference list, which I extracted from the saved HTML — but they ASSUME alignment; they do not compute polarisation growth under shear. CONTENT NOT READ (ADS blocked by human-verification); existence only.

Consequence for B1: if a polarisation response with anisotropic stress existed at this bounce, B1's isotropic-stress shear law would indeed be exposed — but no published calculation delivers that response in this regime, and the one new quantitative result found (global SIP insignificance) leans, weakly and non-transferably, the other way. B5's row (iii) verdict stands.

=====================================================================
3. OVERSTATEMENT SCAN ("NOT ESTABLISHED" sliding into "established to FAIL")
=====================================================================

No slide found. B5's modality guard is explicit and repeated ("NOT ESTABLISHED means not demonstrated by the inspected evidence, not a claim that no paper could exist"; "an effective description can include an interaction nonperturbatively"; "R_F >= 1 alone is not a theorem of fluid breakdown").

Closest approach, quoted verbatim: "Polarisation or surviving spin–shear correlations can leave anisotropic source terms, so the source-free shear evolution cannot simply be retained." Ruled acceptable: "simply" plus the immediately following "The relevant stress must be checked" keep this a due-diligence statement (the evolution cannot be ASSUMED), not a claim that the shear evolution IS wrong. Watch-listed only.

One wording slip (accuracy, not modality): the header says "Physical validity at the target bounce is NOT ESTABLISHED for all three assumptions" while the report assesses FOUR rows (averaging; thermal matter; isotropic average; production) and its own table has four NOT-ESTABLISHED rows. Recommend the lane correct "three" to "four" or name the intended grouping. I did not edit B5.

=====================================================================
4. UNDERSTATEMENTS (things the sources DO establish, available to B5)
=====================================================================

- Row (iv) reinforcement: GRG's own cited [14] (ApJ 832, 96 (2016)) explicitly frames the production scalar as an ansatz and defers its QFT derivation ("Ultimately, K should be derived..."), and the Zel'dovich-Starobinsky 1977 microscopic rate is a curvature-invariant law (Weyl^2 / R^2) with explicit weak-anisotropy and masslessness conditions — published evidence that the fixed-beta H^4 form is phenomenological AND that the known microscopic structure differs from it, including at H=0. B5 currently rests row (iv) on absence-within-GRG plus search scope; citing [14] and ZS 1977 would bind it affirmatively. Custody labels: [14] read via arXiv:1410.3881v2 (revised 2026-05-26, marked "published version"; IOP version of record bot-walled); ZS 1977 read in full from the journal site.
- Row (iii) reinforcement: Fu et al. PRL 127, 142301 (2021) is an uncited published instance of BOTH directions B5 argues abstractly — shear induces spin structure in a relativistic fluid, and the integrated/global response is insignificant. Citing it would make "a momentum-dependent quadrupole can cancel in an integrated mean" a published result rather than an argument.
- Neither understatement changes any row's verdict.

=====================================================================
5. FAILED ATTACKS (what I tried that held)
=====================================================================

1. Hunted a sufficient validity window for Weyssenhoff averaging at spin-dominated density across: Hehl 1974, RMP 1976, Gasperini 1986, Obukhov-Korotky 1987, Brechet 2007 and 2008, Ziaie 2014, PRD 107:084004 (2023), Nomura-Shirafuji-Hayashi 1991, plus a dedicated breakdown-wording search. Found necessary conditions, conditional assumptions, uses, and challenges — no sufficient window. Row (i) held.
2. Hunted an establishment of the ideal ultrarelativistic thermal description at the bounce (equilibrium/EoS literature). Only assumption-level statements. Row (ii) held. (Search-level evidence; disclosed.)
3. Attacked (iii) from both directions: sought a persistence proof or relaxation-timescale window for this regime (none found — the timescale literature is QGP-specific); sought a failure proof (SIP literature) — found Fu et al. 2021, which sharpens the concern but is regime-locked to small-gradient LTE quasiparticle media and reports an insignificant GLOBAL response. Both directions remain unestablished HERE. Row (iii) held.
4. Attacked (iv) via the microscopic production literature (ZS 1977 full text; Beilin 1980 via ApJ 2016) and via GRG's own [14]/[15] lineage. The microscopic law has a different invariant structure with its own explicit perturbative conditions; [14] admits ansatz status. Row (iv) held.
5. Circumvented B5's Radware-blocked [14] via the arXiv "published version" — the blockade is real but not evidence-critical; the arXiv copy corroborates, not contradicts, B5.
6. Quote-audited B5: Hehl 1974 "large number" (line 76) and "shorter char- acteristic length than the local fluid vorticity" (lines 133-135, hyphenation split as B5 disclosed); Becattini "shear tensor contributes" (line 24); Liu-Yin tau_R condition (lines 182, 291); GRG §8-10 inventory phrases in the saved HTML (all present; "only approximate" 3 distinct x2 markup duplicates). All verified accurate.

=====================================================================
6. EVIDENCE LEDGER
=====================================================================

Local (read in full unless noted): B5_VALIDITY_20260907.md; B4_RECONCILIATION_20260907.md; B3_CLASS_FILED_20260907.md; B1_RESULT_V2_20260907.md (incl. Amendments A and B); b5_sources/access.json; b5_sources/pop2016_publisher.html (head; captcha confirmed); GRG reference list extracted from b4_springer_access.html with my own script ([14]=ApJ 832:96, [15]=IJMPD 27:1847020, [50]=PRD 10:1066, [52]=ApJ 870:78); targeted re-reads of b5_sources/brechet2008_publisher.txt (lines 10-54, 280-329, grep hits), hehl1974_publisher.txt (67, 76, 133-135), liu_yin2021_publisher.txt (182, 291), becattini2021_publisher.txt (24, 236).

Web, with read-level per source:
- Zel'dovich & Starobinsky 1977, JETP Lett. 26, 373 — PUBLISHER-SITE FULL TEXT (jetpletters.ru PDF).
- Popławski ApJ 832, 96 (2016) — ARXIV COPY (arXiv:1410.3881v2 full HTML, marked "published version", revised 2026-05-26); IOP publisher page blocked (Radware), confirmed locally.
- Fu et al. PRL 127, 142301 (2021) — ARXIV COPY full text (arXiv:2103.10403v1 HTML); APS page not read.
- Gasperini PRL 56, 2873 (1986) — APS publisher ABSTRACT page only.
- Brechet et al. CQG 24, 6329 (2007) — arXiv abstract only.
- Popławski IJMPD 27, 1847020 (2018) — arXiv abstract only (essay; no physics claim taken from it).
- Ziaie et al. EPJC 74, 3154 (2014) — Springer page partial extract only.
- Obukhov & Korotky CQG 4, 1633 (1987) — abstract/snippets only.
- PRD 107, 084004 (2023); PR C 101, 024907 (2020); Nomura et al. PTP 86, 1239 (1991) — snippets only.
- Kopczyński PLA 39, 219 (1972) / PLA 43, 63 (1973) — existence only via GRG's reference list; content not read (ADS human-verification block).
- Preprints: none used for any physics claim; every load-bearing item above is published peer-reviewed, with arXiv copies labelled as arXiv copies.

Custody limitations declared: [14]'s quoted wording binds to arXiv:1410.3881v2 (2026 revision), not the 2016 version of record; Ziaie/OK87/Gasperini claims are bounded to abstract/partial reads as labelled; row (ii)'s negative is search-level. Constraints held: no writes outside bounce/ (this report plus _tmp_kimi_refs.py, a read-only extraction helper); no git operations; no secrets touched; B5 and all sibling filings left byte-unchanged.

=====================================================================
VERDICT: B5_REVIEW=ABSENCES_HOLD
All four NOT-ESTABLISHED rows survived targeted attempts to find the
thing claimed missing. No overstatement of the absence modality found
(one "three"/four-row wording slip, flagged, non-modal). Understatements
found are reinforcements available to B5 (ApJ 2016 ansatz admission and
ZS 1977 for row (iv); Fu et al. PRL 2021 for row (iii)); they change no
verdict. Report only; nothing repaired.
=====================================================================
