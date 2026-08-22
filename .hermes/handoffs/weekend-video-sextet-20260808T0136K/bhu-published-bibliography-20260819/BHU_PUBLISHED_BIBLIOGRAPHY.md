# BHU published bibliography — the corrected base layer

**Lana-2 (verification seat), 2026-08-19 15:52 KST.** Built from Goru's sweep (`GORU_BIBLIO_SWEEP.md`,
26 candidates), the derivation packet `../reviews/LANA_BHU_PREDICTION_DERIVATION_20260811.md`
(sha256 prefix `b244ea0a` — re-hashed and matched this session), the BHU track baseline JSON, and
fresh Crossref/arXiv searches. Scope label per brief: **BHU is Duho's personal side-interest, not a
NebulaMind research programme.**

**Verification method, stated once and applying to every "VERIFIED" line below.** Every publication
claim was resolved **this session (2026-08-19)** against the **Crossref DOI registry record** (the
machine form of the DOI page: journal, volume, pages, issue date, publisher), via
`api.crossref.org/works/<doi>` or a bibliographic query returning the exact title/author match.
No entry rests on arXiv metadata alone; where arXiv pages were consulted (Easson 2026) they were
used only to tie authorship to an already-verified journal record, never as the publication
evidence itself. Anything that could not be verified published is in Appendix A, with the reason.
Testability classes per brief: **CALIBRATED-FALSIFIER** (number + threshold) /
**QUALITATIVE-DIRECTIONAL** / **CONSISTENCY-ONLY** / **PROSPECT** (points at other instruments).

**Counts: 46 verified-published entries — 40 BHU papers (1–28, 31, 36–46) and 6 support entries
(29–30, 32–35); 8 appendix items plus 1 pending-verification item. Numbering note: additions
after 2026-08-22 take the next free number rather than renumbering, so cross-references to
entries 1–29 elsewhere in the record stay valid; tier is stated per entry, not implied by
number. Branches 9–10 added 2026-08-22 by the bibliography gate.**
Class tally over the 40 BHU papers: 2 CALIBRATED-FALSIFIER, 4 QUALITATIVE-DIRECTIONAL, 3 PROSPECT,
19 CONSISTENCY-ONLY, 12 UNREAD (entries 31 and 36–46 — texts unexamined here; class deliberately
not assigned second-hand. The unread fraction is now 30% of the base layer and is the
bibliography's honest debt: reading them is the outstanding work, not finding more).

---

## 1. Founding and classic identifications

**1. R. K. Pathria (1972). "The Universe as a Black Hole." Nature 240, 298–299.**
DOI 10.1038/240298a0 — VERIFIED (Crossref: Nature, v240, p298-299, 1972-12).
Claim: a closed uniform-density universe sits inside a black hole and may oscillate within it,
provided its radius exceeds the Schwarzschild radius; it cannot expand without limit.
Testability: **CONSISTENCY-ONLY** — radius condition and bounded expansion, no distinguishing
observational statistic in the accessible abstract; the paywalled body remains [VERIFY].
Record: characterized in the Phase 1 packet §1.1. Audit-worthiness: **low-medium** — historically
foundational, but a strict night needs the full text first (still unobtained).

**2. I. J. Good (1972). "Chinese universes." Physics Today 25(7), 15.**
DOI 10.1063/1.3070923 — VERIFIED (Crossref: Physics Today, v25, p15, 1972-07).
Claim: nested ("Chinese-box") universes, each inside a black hole of the next.
Testability: **CONSISTENCY-ONLY** (a short note; content not read this session).
Record: was an open [VERIFY] in the packet ("not located online") — **the publication itself is
resolved here**; content remains unread. Audit-worthiness: **low** — a page-long note; historical
context only.

**3. W. M. Stuckey (1994). "The observable universe inside a black hole." Am. J. Phys. 62, 788–795.**
DOI 10.1119/1.17460 — VERIFIED (Crossref: AJP, v62, p788-795, 1994-09).
Claim: pedagogical demonstration that a closed FLRW dust universe can be embedded as the interior
of a Schwarzschild black hole.
Testability: **CONSISTENCY-ONLY**. Record: named in the brief as "Stuckey-class pedagogy if
published" — it is published; new to our record as a verified item. Audit-worthiness: **low** as a
target, **useful** as the cleanest pedagogical baseline for any strict interior-matching rebuild.

**4. H. Knutsen (2009). "The idea of the universe as a black hole revisited." Grav. Cosmol. 15, 273–277.**
DOI 10.1134/S0202289309030128 — VERIFIED (Crossref: Gravitation and Cosmology, v15, p273-277, 2009-07).
Claim: critical re-examination of the Pathria-style identification.
Testability: **CONSISTENCY-ONLY**. Record: **new to us** (surfaced by this session's Crossref
search, absent from packet and sweep). Audit-worthiness: **low-medium** — a published critique of
target #1; cheap due-diligence read before any Pathria-line audit.

**5. S. Khakshournia (2010). "A note on Pathria's model of the universe as a black hole." Grav. Cosmol. 16, 178–180.**
DOI 10.1134/S0202289310020131 — VERIFIED (Crossref: Gravitation and Cosmology, v16, p178-180, 2010-04).
(arXiv:1412.0105 is the posting of this published note.)
Claim: the Pathria identification holds only for certain Λ values and the horizon/maximal-expansion
matching is not smooth (null shell with surface pressure).
Testability: **CONSISTENCY-ONLY**. Record: characterized in packet §1.1 (used as the Pathria
commentary). Audit-worthiness: **medium** — the matching defect it identifies is exactly what a
strict junction-condition audit would re-derive.

**46. "Quantization of the universe as a black hole." Astrophys. Space Sci. 337, 19–20 (2012).**
DOI 10.1007/s10509-011-0909-1 — VERIFIED (Crossref: ApSS, v337, p19-20, 2011-11). Added 2026-08-22 from the bibliography gate
(`bhu-biblio-gate-20260822/BGATE_VERDICT.md`, HOLD_BIBLIO_DIRECT_OMISSIONS). Tier: **W1**.
Testability: **UNREAD** — full text unexamined here; class not assigned second-hand.
Record: harvest #16; direct universe-as-BH claim — the gate notes scientific weight may be low while scope fit is high.

## 2. Cosmological natural selection — the calibrated falsifier

**6. L. Smolin (1992). "Did the universe evolve?" Class. Quantum Grav. 9, 173–191.**
DOI 10.1088/0264-9381/9/1/016 — VERIFIED (Crossref: CQG, v9, p173-191, 1992-01).
Claim: universes reproduce through black holes with mutated constants, so our constants should be
near-optimal for black-hole production. (*The Life of the Cosmos* is the book-length version —
Appendix A6.)
Testability: **CALIBRATED-FALSIFIER** — via the neutron-star maximum-mass chain made explicit in
entry 7. Record: characterized in packet §1.4; the packet's [VERIFY] on the CQG citation details
is resolved at the publication level here (in-paper details still unread).
Audit-worthiness: **high** — one of the two published BHU-family papers whose falsifier is a
number.

**7. G. E. Brown, C.-H. Lee, M. Rho (2008). "Kaon Condensation, Black Holes, and Cosmological Natural Selection." Phys. Rev. Lett. 101, 091101.**
DOI 10.1103/PhysRevLett.101.091101 — VERIFIED (Crossref: PRL, v101, 091101, 2008-08-28).
(Publisher's Note PRL 101, 119901 pins the threshold symbol ≳, per the Phase 1 custody audit.)
Claim: the Brown–Bethe kaon-condensate EoS gives M_max ≈ 1.5 M☉; a neutron star with M ≳ 2 M☉
"would put in serious doubt or simply falsify" the chain including CNS.
Testability: **CALIBRATED-FALSIFIER** — the family's clean number + threshold.
Record: **already adjudicated in our record — falsified via limb 2** (the "simply falsify" limb of
the source's own disjunction), per the brief; the packet Rev 4 carries the measurement facts:
PSR J1614−2230 at 1.97 ± 0.04 M☉ (Demorest et al. 2010, Nature 467, 1081–1083,
DOI 10.1038/nature09466 — VERIFIED) and PSR J0740+6620 at 2.08 ± 0.07 M☉ (Fonseca et al. 2021,
ApJL 915, L12, DOI 10.3847/2041-8213/ac03b8 — VERIFIED); PSR J0952−0607 (~2.35 M☉) remains
[VERIFY]. Audit-worthiness: **high** — a strict night can recompute the EoS chain and put the
adjudication on a quantitative credibility footing rather than a disjunction reading.

**31. L. Smolin (2004). "Cosmological natural selection as the explanation for the complexity of the universe." Physica A 340, 705–713.**
DOI 10.1016/j.physa.2004.05.021 — VERIFIED (Crossref: Physica A, v340, p705-713, 2004-09). Added
2026-08-22 (Duho's instruction) after the Phase 3 audits found the falsifying paper's CNS
*requirement* (B-17, "the upper mass limit of neutron stars be as low as possible") cites this and
only this — the peer-reviewed half of link (4). No arXiv eprint; Elsevier paywalled; INSPIRE holds
no document (both checked 2026-08-21) — **full text unobtained, content unread**.
Testability: **UNREAD** — deliberately unclassified rather than classed from second-hand citations.
Record: the missing base entry the CNS audit chain leaned on throughout; obtaining it is the same
outstanding institutional-access acquisition as entry 6's full text.
Audit-worthiness: **high** — it is the published source of the requirement the whole falsifier
tests, and Track C stays context-grade until it or entry 6 is read.

## 3. Popławski torsion-bounce parentage — the published mechanism chain

**8. N. J. Popławski (2010). "Radial motion into an Einstein–Rosen bridge." Phys. Lett. B 687, 110–113.**
DOI 10.1016/j.physletb.2010.03.029 — VERIFIED (Crossref: PLB, v687, p110-113, 2010-04).
Claim: our universe may be the Einstein–Rosen-bridge interior of a black hole; radial geodesics
pass through. Testability: **CONSISTENCY-ONLY**. Record: new as a distinct verified entry (the
packet cites his series generically). Audit-worthiness: **medium** — the kinematic seed of the
parentage chain.

**9. N. J. Popławski (2010). "Cosmology with torsion: an alternative to cosmic inflation." Phys. Lett. B 694, 181–185.**
DOI 10.1016/j.physletb.2010.09.056 — VERIFIED (Crossref: PLB, v694, p181-185, 2010-11).
(Erratum: PLB 701, 672 — pinned at the Phase 1 custody audit.)
Claim: Einstein–Cartan torsion generates a nonsingular bounce that explains apparent flatness,
homogeneity and isotropy; derives present-day torsion density Ω_S = −8.6×10⁻⁷⁰; the pre-bounce
contraction "may correspond" to collapse inside a black hole in another universe.
Testability: **PROSPECT** — it names a verification route (inherited corrections coupling to other
fields) but defines no sensitivity floor or forecast amplitude.
Record: characterized in packet §1.2 (full-text audited by Tori). Audit-worthiness: **highest in
the family** — see ranked target 1.

**10. N. J. Popławski (2012). "Nonsingular, big-bounce cosmology from spinor-torsion coupling." Phys. Rev. D 85, 107502.**
DOI 10.1103/PhysRevD.85.107502 — VERIFIED (Crossref: PRD, v85, 107502, 2012-05-29).
Claim: the Dirac-spinor–torsion coupling generates the nonsingular big bounce.
Testability: **CONSISTENCY-ONLY**. Record: **new to us**. Audit-worthiness: **medium-high** — the
mechanism paper a strict re-derivation of entry 9's bounce would actually work through.
(Related published review, verified but not counted as a base entry: "Cosmological consequences of
gravity with spin and torsion," Astronomical Review 8, 108–115 (2013),
DOI 10.1080/21672857.2013.11519725.)

**11. N. J. Popławski (2016). "Universe in a black hole in Einstein–Cartan gravity." ApJ 832, 96.**
DOI 10.3847/0004-637X/832/2/96 — VERIFIED (Crossref: ApJ, v832, 96, 2016-12-01).
(arXiv:1410.3881; the v1 title differs — version-bound at the Phase 1 custody audit.)
Claim: spin-fluid bounce inside the horizon yields a nonsingular closed universe with a finite
inflation-like expansion phase without a scalar field.
Testability: **CONSISTENCY-ONLY** — per the Phase 1 full-body check: no preferred-axis, handedness,
spectral-index, or tensor forecast. Record: characterized in packet §1.2.
Audit-worthiness: **high** — pairs with entry 9 as the published core of the parentage mechanism.

**12. N. Popławski (2025). "Gravitational collapse with torsion and universe in a black hole." Int. J. Mod. Phys. A 40, 2544007.**
DOI 10.1142/S0217751X25440075 — VERIFIED (Crossref: IJMPA, v40, 2025-09-17).
Claim: continues the torsion-collapse/bounce line (per Kun's abstract check: not the axis line).
Testability: **CONSISTENCY-ONLY**. Record: pinned at Kun's Phase 1 gate. Audit-worthiness:
**medium** — the current state of the mechanism, to be read alongside entries 9–11.

**39. N. J. Popławski (2012). "Big bounce from spin and torsion." Gen. Relativ. Gravit. 44, 1007–1014.**
DOI 10.1007/s10714-011-1323-2 — VERIFIED (Crossref: GRG, v44, p1007-1014, 2012-01). Added 2026-08-22 from the bibliography gate
(`bhu-biblio-gate-20260822/BGATE_VERDICT.md`, HOLD_BIBLIO_DIRECT_OMISSIONS). Tier: **W1**.
Testability: **UNREAD** — full text unexamined here; class not assigned second-hand.
Record: recalled by the gate with its DOI remembered EXACTLY (verified digit-for-digit); fills the hole between the 2010 and 2012 mechanism papers of this branch.

**40. N. Popławski (2021). "Gravitational collapse of a fluid with torsion into a universe in a black hole." J. Exp. Theor. Phys. 132, 374 (Zh. Eksp. Teor. Fiz. 159, 448).**
DOI 10.31857/S0044451021030068 — VERIFIED (Crossref: ZhETF, v159, p448-456, 2021). Added 2026-08-22 from the bibliography gate
(`bhu-biblio-gate-20260822/BGATE_VERDICT.md`, HOLD_BIBLIO_DIRECT_OMISSIONS). Tier: **W1**.
Testability: **UNREAD** — full text unexamined here; class not assigned second-hand.
Record: harvest #10; the mechanism's direct collapse continuation, published in JETP.

**41. N. Popławski (2021). "A nonsingular, anisotropic universe in a black hole with torsion and particle production." Gen. Relativ. Gravit. 53, 18.**
DOI 10.1007/s10714-021-02790-7 — VERIFIED (Crossref: GRG, v53, 2021-02). Added 2026-08-22 from the bibliography gate
(`bhu-biblio-gate-20260822/BGATE_VERDICT.md`, HOLD_BIBLIO_DIRECT_OMISSIONS). Tier: **W1**.
Testability: **UNREAD** — full text unexamined here; class not assigned second-hand.
Record: harvest #11; parentage construction beyond isotropy.

## 4. The baby-universe branch

**13. V. P. Frolov, M. A. Markov, V. F. Mukhanov (1989). "Through a black hole into a new universe?" Phys. Lett. B 216, 272–276.**
DOI 10.1016/0370-2693(89)91114-3 — VERIFIED (Crossref: PLB, v216, p272-276, 1989-01).
Claim: black-hole interior evolves into a new universe under a limiting-curvature hypothesis.
Testability: **CONSISTENCY-ONLY**. Record: packet §1.6 (abstract level). Audit-worthiness:
**medium** — the branch's founding calculation.

**14. V. P. Frolov, M. A. Markov, V. F. Mukhanov (1990). "Black holes as possible sources of closed and semiclosed worlds." Phys. Rev. D 41, 383–394.**
DOI 10.1103/PhysRevD.41.383 — VERIFIED (Crossref: PRD, v41, p383-394, 1990-01-15).
Claim: the full development of entry 13. Testability: **CONSISTENCY-ONLY**. Record: packet §1.6.
Audit-worthiness: **medium**.

**15. D. A. Easson, R. H. Brandenberger (2001). "Universe generation from black hole interiors." JHEP 06 (2001) 024.**
DOI 10.1088/1126-6708/2001/06/024 — VERIFIED (Crossref: JHEP, v2001, 024, 2001-06-11).
Claim: universe generation from black-hole interiors with limiting curvature.
Testability: **CONSISTENCY-ONLY**. Record: packet §1.6. Audit-worthiness: **medium**.

**16. B. Pourhassan et al. (2025). "Multiversal entropy and information conservation in black hole nucleated baby universes." Nucl. Phys. B 1020, 117160.**
DOI 10.1016/j.nuclphysb.2025.117160 — VERIFIED (Crossref: NPB, v1020, 117160, 2025-11).
Claim: entropy/information accounting for black-hole-nucleated baby universes, with stated
observational prospects in primordial-black-hole populations and gravitational-wave echoes.
Testability: **PROSPECT** — prospects for other instruments, no sky-statistics target.
Record: packet §1.6 (the "2025 Nucl. Phys. B baby-universe paper"). Audit-worthiness:
**medium-high** — the branch's only recent entry with named observables; see ranked target list.

**17. H. Chakrabarty et al. (2020). "A toy model for a baby universe inside a black hole." Eur. Phys. J. C 80 (2020).**
DOI 10.1140/epjc/s10052-020-7964-0 — VERIFIED (Crossref: EPJC, v80, 2020-05).
Claim: explicit toy interior in which a baby universe replaces the singularity.
Testability: **CONSISTENCY-ONLY**. Record: baseline corpus entry, publication newly verified here.
Audit-worthiness: **low-medium**.

**42. "Baby universe metric equivalent to an interior black-hole metric." Phys. Lett. B 261, 357–362 (1991).**
DOI 10.1016/0370-2693(91)90440-2 — VERIFIED (Crossref: PLB, v261, p357-362, 1991-06). Added 2026-08-22 from the bibliography gate
(`bhu-biblio-gate-20260822/BGATE_VERDICT.md`, HOLD_BIBLIO_DIRECT_OMISSIONS). Tier: **W1**.
Testability: **UNREAD** — full text unexamined here; class not assigned second-hand.
Record: harvest #31; early interior-equivalence result. Authors deliberately omitted — the harvest did not return them and Crossref title/venue is what was verified; add the author line only from the record itself.

**43. "Birth of baby universes from gravitational collapse in a modified-gravity scenario." JCAP 06 (2023) 028.**
DOI 10.1088/1475-7516/2023/06/028 — VERIFIED (Crossref: JCAP, v2023, 028, 2023-06). Added 2026-08-22 from the bibliography gate
(`bhu-biblio-gate-20260822/BGATE_VERDICT.md`, HOLD_BIBLIO_DIRECT_OMISSIONS). Tier: **W1**.
Testability: **UNREAD** — full text unexamined here; class not assigned second-hand.
Record: harvest #6; direct collapse-to-baby-universe construction in modified gravity.

## 5. Regular-black-hole interiors (Dymnikova line)

**18. I. Dymnikova (1992). "Vacuum nonsingular black hole." Gen. Rel. Grav. 24, 235–242.**
DOI 10.1007/BF00760226 — VERIFIED (Crossref: GRG, v24, p235-242, 1992-03).
Claim: regular black hole with a de Sitter core — the vacuum-bubble interior mechanism.
Testability: **CONSISTENCY-ONLY**. Record: packet §1.6 names the class. Audit-worthiness:
**medium** — the interior every later "universe inside a regular BH" paper builds on.

**19. I. Dymnikova (2019). "Universes Inside a Black Hole with the de Sitter Interior." Universe 5, 111.**
DOI 10.3390/universe5050111 — VERIFIED (Crossref: Universe, v5, 111, 2019-05-10).
Claim: explicit universes-inside-a-regular-BH construction. Testability: **CONSISTENCY-ONLY**.
Record: **new to us**. Audit-worthiness: **medium**.

**20. K. A. Bronnikov, J. C. Fabris (2007)-class: "Regular black holes and black universes." Gen. Rel. Grav. 39, 973–987.**
DOI 10.1007/s10714-007-0430-6 — VERIFIED (Crossref: GRG, v39, p973-987, 2007-05).
Claim: "black universes" — regular BH solutions whose interior is an expanding universe.
Testability: **CONSISTENCY-ONLY**. Record: **new to us**. Audit-worthiness: **low-medium**.

**21. Z. Roupas (2022). "Detectable universes inside regular black holes." Eur. Phys. J. C 82, 255.**
DOI 10.1140/epjc/s10052-022-10202-6 — VERIFIED (Crossref: EPJC, v82, 2022-03).
Claim: regular black holes can contain dark-energy universes with matched mass-energy and entropy,
claimed detectable by gravitational-wave experiments in the μHz–Hz band (LISA-class).
Testability: **PROSPECT** — a named instrument band, but (per the abstract read this session) no
amplitude or threshold; whether the body derives one is exactly the strict-night question.
Record: baseline corpus entry (2203.13295), publication newly verified here.
Audit-worthiness: **high** — see ranked target 4.

**22. D. A. Easson (2026). "Obstructions to Minimal Regular Black Hole Cosmologies." Phys. Rev. D, published online 2026-07-31.**
DOI 10.1103/qs86-npwk — VERIFIED with a stated caveat: the Crossref record confirms an APS
Physical Review D journal-article of this exact title published online 2026-07-31, but the deposit
is still anonymized and carries no volume/article number yet; the arXiv v3 of 2606.25023 (author
D. A. Easson, sole) is marked "Version to appear in PRD." Publication fact rests on the DOI
registry record; authorship tie rests on the unique title match. **Flagged for Miru's spot-check.**
Claim: no-go obstructions for minimal regular-black-hole cosmologies.
Testability: **CONSISTENCY-ONLY** (a constraint result). Record: baseline corpus entry (preprint),
journal status newly established here. Audit-worthiness: **high** — see ranked target 5.

## 6. Gaztañaga interior-matching series

**23. E. Gaztañaga (2020). "The size of our causal Universe." MNRAS 494, 2766–2772.**
DOI 10.1093/mnras/staa1000 — VERIFIED (Crossref: MNRAS, v494, p2766-2772, 2020-04-15).
Claim: the causal horizon acts as a boundary producing a cutoff at the largest observable scales,
fitted against CMB anomalies. Testability: **QUALITATIVE-DIRECTIONAL** — claims a directional
signature (large-scale power cutoff / low quadrupole) whose scale is fitted from the data it
explains, not forecast ahead of it. Record: Phase 0 sweep territory; newly verified.
Audit-worthiness: **high** — see ranked target 3.

**24. E. Gaztañaga (2022). "A peek outside our Universe." Symmetry 14, 285.**
DOI 10.3390/sym14020285 — VERIFIED (Crossref: Symmetry, v14, 285, 2022-01-31).
Claim: the observable universe as the interior of a BHU with observational traces at the boundary.
Testability: **QUALITATIVE-DIRECTIONAL** (same cutoff-class claims). Record: baseline corpus entry
(2104.00521), publication newly verified. Audit-worthiness: **medium** — subsumed by 23/25/26.

**25. E. Gaztañaga (2022). "The Black Hole Universe, Part I." Symmetry 14, 1849.**
DOI 10.3390/sym14091849 — VERIFIED (Crossref: Symmetry, v14, 1849, 2022-09-05).
Claim: the bounded Friedmann–Lemaître sphere inside empty space reproduces FLRW observations for
interior observers and explains cosmic acceleration without dark energy via Λ = 3/r_S² (the
Schwarzschild radius acting as a cosmological constant).
Testability: **QUALITATIVE-DIRECTIONAL** — the Λ–r_S identification is a number, but it is fixed
*from* the measured Λ rather than predicting it; the falsifiable edge is the implied coincidence
between the dark-energy scale and the causal-horizon cutoff of entry 23.
Record: **new to us as a verified item** (Phase 0 named the series). Audit-worthiness: **high**.

**26. E. Gaztañaga (2022). "The Black Hole Universe, Part II." Symmetry 14, 1984.**
DOI 10.3390/sym14101984 — VERIFIED (Crossref: Symmetry, v14, 1984, 2022-09-22).
Claim: Part II of the same construction (formation from an FLRW cloud).
Testability: **QUALITATIVE-DIRECTIONAL** (with Part I). Record: new to us. Audit-worthiness:
**high**, jointly with 25.

**27. E. Gaztañaga (2022). "How the Big Bang Ends Up Inside a Black Hole." Universe 8, 257.**
DOI 10.3390/universe8050257 — VERIFIED (Crossref: Universe, v8, 257, 2022-04-21).
Claim: the collapse-to-bounce route into the BHU picture. Testability: **CONSISTENCY-ONLY**.
Record: new to us. Audit-worthiness: **medium**.

## 7. Holographic interior cosmology

**28. A. Sahu et al. (2025). "Holographic black hole cosmologies." JHEP 05 (2025) 233.**
DOI 10.1007/JHEP05(2025)233 — VERIFIED (Crossref: JHEP, v2025, 2025-05-28). Note: the arXiv page
(2411.14673) carries no journal-ref field — the Crossref journal record is the evidence, and this
is exactly why arXiv metadata alone is not trusted in either direction.
Claim: big-bang/big-crunch cosmologies behind black-hole horizons as entangled states of multiple
CFTs, with dominance conditions in 3D gravity.
Testability: **CONSISTENCY-ONLY**. Record: baseline corpus entry, newly verified.
Audit-worthiness: **low-medium** — far from any observable, but the only active holographic line.

## 9. Smoller–Temple shock-wave interior cosmology

Added 2026-08-22: a whole programme the original taxonomy lacked — FRW/TOV shock-matching
cosmologies constructed inside a black hole, found by the bibliography gate (one harvest hit,
two training-memory recalls).

**36. J. Smoller & B. Temple (2000). "Cosmology with a shock-wave." Commun. Math. Phys. 210, 275–308.**
DOI 10.1007/s002200050780 — VERIFIED (Crossref: CMP, v210, p275-308, 2000-03). Added 2026-08-22 from the bibliography gate
(`bhu-biblio-gate-20260822/BGATE_VERDICT.md`, HOLD_BIBLIO_DIRECT_OMISSIONS). Tier: **W1**.
Testability: **UNREAD** — full text unexamined here; class not assigned second-hand.
Record: recalled by the gate's training-memory attack, missing from bibliography AND harvest; the programme's founding cosmology paper.

**37. J. Smoller & B. Temple (2003). "Shock-wave cosmology inside a black hole." PNAS 100, 11216–11218.**
DOI 10.1073/pnas.1833875100 — VERIFIED (Crossref: PNAS, v100, p11216-11218, 2003-09). Added 2026-08-22 from the bibliography gate
(`bhu-biblio-gate-20260822/BGATE_VERDICT.md`, HOLD_BIBLIO_DIRECT_OMISSIONS). Tier: **W1**.
Testability: **UNREAD** — full text unexamined here; class not assigned second-hand.
Record: harvest #17; the branch-defining title. (Harvest metadata said 2002; Crossref says 2003 — the verified year is used.)

**38. J. Smoller & B. Temple (2004). "Cosmology, black holes and shock waves beyond the Hubble length." Methods Appl. Anal. 11, 77–132.**
DOI 10.4310/maa.2004.v11.n1.a7 — VERIFIED (Crossref: MAA, v11, p77-132, 2004). Added 2026-08-22 from the bibliography gate
(`bhu-biblio-gate-20260822/BGATE_VERDICT.md`, HOLD_BIBLIO_DIRECT_OMISSIONS). Tier: **W1**.
Testability: **UNREAD** — full text unexamined here; class not assigned second-hand.
Record: recalled by the gate, missing from both documents; the programme's expanded interior construction.

## 10. White-hole / holographic-origin big bang

Added 2026-08-22: distinct from branch 7's entangled-CFT interiors per the gate's branch-gap
finding; the big bang as the interior/exterior of a white-hole or 5D collapse.

**44. R. Pourhasan, N. Afshordi & R. B. Mann (2014). "Out of the white hole: a holographic origin for the Big Bang." JCAP 04 (2014) 005.**
DOI 10.1088/1475-7516/2014/04/005 — VERIFIED (Crossref: JCAP, v2014, 005, 2014-04). Added 2026-08-22 from the bibliography gate
(`bhu-biblio-gate-20260822/BGATE_VERDICT.md`, HOLD_BIBLIO_DIRECT_OMISSIONS). Tier: **W1**.
Testability: **UNREAD** — full text unexamined here; class not assigned second-hand.
Record: harvest #24; the 5D holographic/white-hole origin — the line the caption-era Afshordi identification traced back to.

**45. "White hole cosmology and Hawking radiation from quantum cosmological perturbations." Phys. Rev. D 106, 123505 (2022).**
DOI 10.1103/PhysRevD.106.123505 — VERIFIED (Crossref: PRD, v106, 2022-12). Added 2026-08-22 from the bibliography gate
(`bhu-biblio-gate-20260822/BGATE_VERDICT.md`, HOLD_BIBLIO_DIRECT_OMISSIONS). Tier: **W1**.
Testability: **UNREAD** — full text unexamined here; class not assigned second-hand.
Record: harvest #7; a second published white-hole cosmology route.

## 8. Measurement papers ridden by the family (verified, support-role only)

**29. The CNS test pair** (already cited under entry 7, counted once here as a bibliography entry
pair): Demorest et al. (2010), Nature 467, 1081–1083, DOI 10.1038/nature09466 — VERIFIED; Fonseca
et al. (2021), ApJL 915, L12, DOI 10.3847/2041-8213/ac03b8 — VERIFIED. These are the published
measurements that operate entry 7's falsifier; they are not BHU papers and are listed only so the
base layer contains its own adjudication instruments.

**30. The mechanism review the falsifier imports** (added 2026-08-22, Duho's instruction): Brown,
Lee & Rho, "Recent developments on kaon condensation and its astrophysical implications," Phys.
Rept. **462**, 1–20 (2008), DOI 10.1016/j.physrep.2008.03.002 — VERIFIED (Crossref: Physics
Reports, v462, p1-20, 2008-06); arXiv:0708.3137v2, pinned at
`../bhu-theory-phase3-cns-20260821/sources/ar5iv_0708.3137.html`
(sha256 `fc3ed8cd…`). This is `BLR-kaon07`, the companion the PRL falsifier (entry 7's chain)
imports links (2) and (3) from: it derives the 4% double-NS asymmetry limb (§3.2, the 10%
helium-burning window over 2.5) and quantifies the He-red-giant proviso at 0.1–0.2 M⊙ — the figure
Tauris et al. 2017 later supersede at 0.0134 M⊙ (Phase 3 Track B, gated `PASS_P3B_TRACKB`). Not a
BHU paper: it contains no universe-in-a-black-hole claim itself. Listed because the chain's
quantitative core lives here rather than in the papers that cite it, so the base layer names the
document its own audits actually re-derive from.

**32. The Brown–Bethe maximum-mass paper** (added 2026-08-22): G.E. Brown & H.A. Bethe, "A scenario
for a large number of low-mass black holes in the galaxy," ApJ **423**, 659 (1994), DOI
10.1086/173844 — VERIFIED (Crossref: ApJ, v423, p659, 1994-03). The actual home of M_max ≈ 1.5 M⊙ —
the number every limb-1 test is aimed at; the Phase 3 Track A audit found the falsifier paper
imports it from here without derivation (B-5, NOT-DERIVED-HERE). **Full text not held** — cited and
Crossref-verified only.

**33. The vector-manifestation pair** (added 2026-08-22): M. Harada & K. Yamawaki, PRL **86**, 757
(2001), DOI 10.1103/PhysRevLett.86.757 — VERIFIED; and Phys. Rept. **381**, 1–233 (2003), DOI
10.1016/S0370-1573(03)00139-X — VERIFIED. Link (1) of the falsifier chain (B-2,
ASSUMED-FROM-CITATION) lives here: the hidden-local-symmetry prediction that the gauge coupling
vanishes near chiral restoration. **Full text not held** — cited and Crossref-verified only.

**34. The limb-2 measurement** (added 2026-08-22): R.D. Ferdman et al., "Asymmetric mass ratios for
bright double neutron-star mergers," Nature **583**, 211–214 (2020), DOI 10.1038/s41586-020-2439-x —
VERIFIED. The published masses (1.62/1.27 ± 0.03) behind the deciding-limb margin of 6.7σ, and the
paper establishing PSR J1913+1102's He-star formation channel (Track B, `PASS_P3B_TRACKB`). Pinned:
`../bhu-theory-phase3-cns-20260821/sources/ar5iv_2007.04175.html` (sha256 `20278257…`). Entry 29's
role, for the other limb.

**35. The accretion budget** (added 2026-08-22): T.M. Tauris et al., "Formation of double neutron
star systems," ApJ **846**, 170 (2017), DOI 10.3847/1538-4357/aa7e89 — VERIFIED. The DNS-formation
authority whose per-phase budget (ΔM_NS ≈ 0.0134 M⊙ total) supersedes the He-giant proviso by 7–15×
and restores the ~21σ margin (Track B). Pinned:
`../bhu-theory-phase3-cns-20260821/sources/ar5iv_1706.09438.html` (sha256 `09c86153…`).

---

## Ranked: the strongest published targets to start from

Ranked by (published mechanism a strict model can re-derive) × (distance to a stated observable),
per the standing bar that "do the theory" means an adversarial equation-by-equation audit plus an
in-house strict model with derived transfer functions.

**1. The Popławski torsion-bounce chain — entries 9 + 11 (with 8, 10, 12 as the spine).**
The only published, multi-paper BHU mechanism with explicit field equations. A strict night would:
re-derive the Einstein–Cartan bounce and the Ω_S = −8.6×10⁻⁷⁰ number (erratum included); then
derive, in-house, the transfer function the literature never wrote — from parent-hole parameters
through the bounce to any interior observable — and state honestly whether *any* finite-amplitude
signature survives. This is also the only published route that touches the axis question
(Appendix A1) without using the unpublished preprint as a base.

**2. The CNS falsifier — entries 6 + 7 (+ the entry-29 measurements).**
The family's one calibrated number-plus-threshold. A strict night would recompute the Brown–Bethe
kaon-condensate M_max chain against modern EoS constraints and convert our record's "falsified via
limb 2" adjudication into a quantitative credibility statement (including whether J0952−0607
survives its [VERIFY]). Highest rigor-per-hour in the whole bibliography; the caveat is that it
tests CNS specifically, not interior-cosmology parentage.

**3. The Gaztañaga BHU series — entries 25 + 26 + 23 (24, 27 supporting).**
Published, recent, and unusual in the family for claiming observational consequences (Λ = 3/r_S²,
causal-horizon power cutoff, low quadrupole). A strict night would audit the junction conditions
equation-by-equation (the exact defect class Khakshournia found in Pathria, entry 5) and test the
cutoff claim against Planck likelihoods — with the post-hoc-fitting risk stated up front: the
scale is fitted from the anomalies it explains.

**4. Roupas 2022 — entry 21.**
A published "detectable" claim with a named instrument band (μHz–Hz, LISA-class). The strict
question is sharp and cheap: does the body derive an amplitude and rate, or is "detectable"
uncalibrated? If a number exists, this becomes the family's second calibrated falsifier; if not,
it reclassifies to PROSPECT-without-a-number and says so in print.

**5. Easson 2026 — entry 22.**
The newest constraint result: obstructions to minimal regular-BH cosmologies. High leverage as a
cross-programme check — a strict night would verify the no-go theorems and map which of the other
published interiors (Dymnikova 18/19, Bronnikov 20, Roupas 21, Gaztañaga 25/26, Popławski 11) they
kill, restrict, or spare. One publication-metadata caveat stands (see entry 22) pending Miru's
spot-check.

---

## Appendix A — context, not base (excluded from the base layer, with reasons)

**A0 (pending verification, 2026-08-22).** T. Rothman & G.F.R. Ellis, "Smolin's natural selection
hypothesis" — recalled by the bibliography gate as the published critique of CNS (QJRAS ~34, 1993).
NOT verifiable via Crossref (QJRAS predates DOI coverage) or INSPIRE (no record); enters nowhere
until a publication record is confirmed. The gate's recall of other identities in the same pass was
verified digit-exact, so this is likely real — likely is not the bar.

**A1. arXiv:1910.10819 — N. Popławski, "Universe in a rotating black hole and preferred axis."**
**Preprint-only; quarantined per the standing published-papers-only rule.** Primary category
physics.pop-ph; arXiv DataCite DOI only. Re-checked this session: Crossref bibliographic search
returns **no journal version** (consistent with the Phase 1 finding "no journal version located as
of 2026-08-11"). Cross-reference: the Phase 1 audit
`../reviews/LANA_BHU_PREDICTION_DERIVATION_20260811.md` §1.3 and Revisions 4–5 — v2 (2025) states
the CW/CCW count claim with mechanics but **no calibrated amplitude, scale, or redshift law, no
independently predicted axis direction, and no acceptance region**; v2 postdates the handedness
studies it cites. It remains the *motivating context* for the axis question; it is not a base
paper, and per this bibliography the published route to that question is ranked target 1.

**A2. arXiv:1110.5019 — Popławski, "Mass of the universe in a black hole."** No journal version
located this session (Crossref author+title search). Preprint-only → context.

**A3. arXiv:1108.0211 — Popławski, "Conformal time in a black-hole universe with torsion."** No
journal version located this session. Preprint-only → context.

**A4. arXiv:1610.03767 — Firouzjahi, "Primordial Universe Inside the Black Hole and Inflation."**
Topically in scope, but no journal version located this session. Preprint-only → context.

**A5. Popławski, "Universe in a black hole with spin and torsion," MG16 proceedings (2023),**
DOI 10.1142/9789811269776_0106 — conference proceedings, not a peer-reviewed journal article →
context alongside entries 9–12.

**A6. L. Smolin, *The Life of the Cosmos* (1997)** — a book, not a journal publication → context
for entry 6.

**A7. The Shamir spin-asymmetry line** — e.g. "New evidence and analysis of cosmological-scale
asymmetry in galaxy spin directions," J. Astrophys. Astron. 43 (2022),
DOI 10.1007/s12036-022-09809-8 (this one VERIFIED published), and the JADES paper
arXiv:2502.18781. **Excluded on scope, not on status:** per the Phase 1 packet §1.5 these papers
do not claim to test BHU (the JADES abstract never mentions it; the association is media framing).
They are contested observational context for ranked target 1's transfer-function question, not
BHU base papers. Journal status of 2502.18781 not adjudicated here since scope excludes it either
way.

**A8. The "black-hole lattice universe" programme — Goru candidates 18–24** (Yoo 1204.2411,
1306.1389, 1404.1435; Durk 1610.05635, 1707.08056; Schlue 1610.04172). **Excluded on scope:**
despite the name, these study universes *containing lattices of black holes* (inhomogeneous
cosmology / mathematical GR), not a universe *inside* a black hole. Publication status therefore
not adjudicated here.

---

**Session verification ledger:** every DOI above marked VERIFIED was resolved against its Crossref
registry record on 2026-08-19 (KST); raw JSON for the eight direct-DOI lookups is preserved in the
session scratchpad (`crossref_*.json`). Literature hosts only (api.crossref.org, arxiv.org,
doi.org/link.aps.org redirect, mdpi.com attempt, web search); portal.nersc.gov untouched.

— Lana-2, 2026-08-19 15:52 KST. Verification and classification only; no lane proposed, nothing
committed. Miru gates next (`MIRU_BIB_GATE.md`).
