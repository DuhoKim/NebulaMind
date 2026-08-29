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

**Counts: 58 verified-published entries — 51 BHU papers (1–28, 31, 36–57) and 7 support entries
(29–30, 32–35, 58); 8 appendix items plus 5 pending-verification / ruled-context items. Numbering note: additions
after 2026-08-22 take the next free number rather than renumbering, so cross-references to
entries 1–29 elsewhere in the record stay valid; tier is stated per entry, not implied by
number. Branches 9–10 added 2026-08-22 by the bibliography gate.**
Class tally over the 51 BHU papers, **recomputed by script 2026-08-29 and independently recounted
by two seats**: **4 CALIBRATED-FALSIFIER (2 FIRED — entries 7, 44; 2 LIVE — entries 31, 51),
7 QUALITATIVE-DIRECTIONAL**, 3 PROSPECT, 32 CONSISTENCY-ONLY, 1 THEORETICAL-OBSTRUCTION, 4 UNREAD
— sums to 51. *(The 7 remaining numbered entries — 29, 30, 32, 33, 34, 35, 58 — are support-role
and carry no Testability label, which is why there are 58 entries and 51 papers. Previously read
"3 CALIBRATED-FALSIFIER, 8 QUALITATIVE-DIRECTIONAL, 3 PROSPECT, 33 CONSISTENCY-ONLY, 4 UNREAD",
which predates entry 44's re-tier and omitted the obstruction class.)* (20 entries read and classed 2026-08-23, batches 1–6 and 8–9; A0 read in batch 7.
Batch-9 correction: entry 6 reclassed CALIBRATED-FALSIFIER → QUALITATIVE-DIRECTIONAL — the 1992
text contains no mass-threshold falsifier; that class had been inherited from the entry-7 chain
at triage. The branch's calibrated falsifiers are entries 7 and 31.

**BLIND-SWEEP FLAGS ARE NOT FINDINGS (entries 36, 37, 38, 40, 41).** Added 2026-08-28
(Tori), Duho ruling. A blind re-classification of the 19 entries with pinned full text proposed
six promotions. One (entry 51) was gated twice and applied. **The other five are recorded as
BLIND-FLAGGED, NOT ADJUDICATED, and their tiers are unchanged.**

They were not gated on purpose. The sweep **failed its own control**: of three entries seeded
with known gated answers, entry 54 came back CALIBRATED-FALSIFIER quoting the abstract bracket —
reproducing, independently, the exact error two seats had corrected that morning. A single-pass
blind read carries the same overclaim bias as the method that built this bibliography, so it
cannot audit it. All six proposals ran in that direction, and five came from the engine that
promoted 5 of 10 while the other promoted 1 of 5 and twice found numbers and declined.

Gating five candidates from an instrument demonstrated biased in exactly that direction would
cost five rounds to return noise. A better-designed sweep can revisit them cheaply now that
`../bhu-theory-phase6-curvature-20260827/ENTRY_SOURCE_MAP.md` exists. Working artefacts and both
gate verdicts for entry 51 are in that lane.

**TIER COUNT IS NOT LIVE-FALSIFIER COUNT. Read both lines before quoting either.** Added
2026-08-28 (Tori) because I have now mis-stated this tally twice in one day, in both directions.
The tier describes the CLAIM — *"testability classes per brief: CALIBRATED-FALSIFIER (number +
threshold)"*, i.e. its **shape**, not whether the reasoning behind it is sound. Separate axes
describe its **STANDING** (has it fired) and, added 2026-08-29, its **WARRANT — scoped to calibrated falsifiers only** (does the theory actually produce *this*
falsifier).

> **SCOPE, corrected 2026-08-29 after both gate seats refuted the first version.** I justified the
> column by saying "a warrant only exists where there is a calibrated claim". **That is false.** A
> directional claim can fail to follow in the asserted direction, a PROSPECT can fail to connect
> theory to instrument, a THEORETICAL-OBSTRUCTION can rest on a disputed no-go. **My original cost
> objection to Duho was right the first time and my reversal was wrong.** What is implemented here
> is four calibrated-falsifier warrant cells — **NOT a corpus-wide warrant audit, which has not
> been done.** If the axis is ever extended to the other classes the maintenance cost returns.

> **Why the warrant column exists.** Duho returned open question 4 to me with the instruction
> *"answer question 4"*. The two reviewers had split: one held that a theory cannot keep a
> falsifier its own logic does not generate, so the tier must fall; the other that the tier
> describes claim shape and doubts about reasoning belong in notes. **Both are right about
> different axes, and the record had only two.** Dropping the tier would mean redefining
> "testability class" retroactively across 51 papers on the strength of one dispute; leaving it
> alone would hide a real one. **A warrant column costs four rows, not fifty-eight** — a
> consistency-only paper has no falsifier whose reasoning could be disputed — which is the cost
> objection I put to Duho and got wrong. **No tier and no standing changed.**

| entry | tier | standing | warrant | what it fires |
|---|---|---|---|---|
| 7 | CALIBRATED-FALSIFIER | **FIRED** | **no pinned challenge in this corpus** — a statement about what is filed here, **not a finding that the derivation is sound**; neither seat could verify the literature. This record already scopes what it fired: an instrument chain, not CNS — scope adjudication, not validation. | the Brown–Bethe / VM-HLS / kaon-condensation instrument chain at M ≳ 2 M☉. NOT CNS — the source gives CNS only "serious doubt" / "a serious obstacle". |
| 31 | CALIBRATED-FALSIFIER | **LIVE**, 1.36σ short | **DISPUTED, and the challenge is pinned** — Rothman & Ellis 1993 argue the selection argument needs every parameter change to reduce black holes while α and M_LC plausibly do the opposite; Harrison 1995 argues a recollapsing closed universe yields at most one offspring, removing differential reproduction. Smolin answers neither on those parameters. Read and gated 2026-08-29 (`b20`, `b21`, `b23`). **Silk 1997 still unread (paywalled).** | CNS, at Smolin's own 2.5 M☉ bar. Heaviest well-measured neutron star 2.35 ± 0.11 M☉; 8.6% posterior mass above the bar, and *moving away* from firing as the error tightens. |
| 51 | CALIBRATED-FALSIFIER | **LIVE**, unfired | **UNREPRODUCED FROM THE STATED INPUTS** — none of *six tested* routes from its ρ_Ce reaches the printed 10¹⁶ kg floor, the paper omits the connecting step, and the enumeration is **non-exhaustive**. **The
text we hold is the PUBLISHED one** — *Phys. Lett. B* 690(1) 73–77, © Elsevier — not a preprint, and
it goes from "cannot exceed ρ_Ce" to "its minimum mass … is ∼10¹⁶ kg" in **86 characters**, the whole
derivation carried by the words "from which". **Duho closed open question 2 on 2026-08-29 by
returning it to me; the ruling is that this stays an unreproduced step and is NOT called an error** (`b13`, arithmetic confirmed by both seats; shortfall 3.1–4.1 decades, and refining the inputs widens it). *(Read "DOES NOT FOLLOW" until CGATE_Q4 pointed out that converts a failure to reproduce into a proof of non-entailment and prejudges **open question 2**, which is still Duho's.)* | the four-dimensional ECKS density/minimum-mass chain, via the LHC route. **Not a direct BHU falsifier.** |
| 44 | CALIBRATED-FALSIFIER | **FIRED** | **EXPLICIT AND UNDISPUTED for the claim in this row** — the Sec. 4 model derives n_s = 1 openly; observation then rejected it at 8σ, which is its *standing*, not a failure of its derivation. **What lacks warrant is the successor**: an uncomputed ~4% correction sized to the measurement it must reproduce, deferred by the authors. *(Read "the warrant is what died" until CGATE_Q4 showed that collapses warrant into standing and defeats the point of a separate axis.)* | the Sec. 4 thermal free 5D field theory's prediction of **exact scale invariance, n_s = 1**. Planck: n_s = 0.9649 ± 0.0042, **8σ** from 1 (9σ with BAO); the authors concede >5σ themselves. **NOT the holographic white-hole framework** — they propose an uncomputed ~4% correction whose size is read off the measurement. Added 2026-08-29. |

So: **4 calibrated — 2 live, 2 fired — and TWO bear directly on a black-hole-universe theory:
entry 31, live; and entry 44, ALREADY FIRED.** *(Corrected 2026-08-29 when entry 44 was filed here.
This previously read "3 calibrated, 2 live … only ONE (entry 31) bears directly on a
black-hole-universe theory".)* Entry 51 constrains BHU only where a model inherits its ECKS
premise, and entry 7 fired an instrument rather than a cosmology — **but entry 44 is a BHU
construction in this record's own branch 10, and observation killed its computable core.** That is
the family's first falsifier to fire against one of its own cosmologies rather than against an
instrument chain, and the record did not say so until now. What survives there is the authors'
uncomputed correction, not the model that was tested. Any sentence of the form "the family has N live
falsifiers" must say which N it means. The honest short answer to "can this family still be
killed by observation?" is: **one route, entry 31, and it is drifting away from firing.**
**2026-08-28 correction: entry 54 reclassed CALIBRATED-FALSIFIER → QUALITATIVE-DIRECTIONAL**,
by gate `bhu-theory-phase6-curvature-20260827/BRIEF_ENTRY54_RETIER_GATE.md`; both seats returned
DEMOTE independently (`GATE_ENTRY54_RETIER.md` GPT56, `KGATE_ENTRY54_RETIER.md` KIMI), each
reading the pinned source rather than this record. Same shape as the batch-9 correction, one step
worse: entry 6's numeric threshold was absent from the text, whereas entry 54's is present but
conditional AND its falsification condition was recorded pointing at the wrong side of zero — the
entry claimed a confirmed flat universe refutes the model, when flatness at any achievable
precision is exactly where the model is comfortable. The error entered by copying the abstract's
compact bracket without the qualification four sentences below Eq. 27. Tori filed the finding
against her own 2026-08-23 classification and declined to self-adjudicate. The seats split only on
whether *exactly* Ω_k = 0 refutes: GPT56 yes on the strict inequality, KIMI no because exact
flatness is not confirmable at finite precision — KIMI's reading governs the operational
annotation now carried on the entry. The tally line above is updated accordingly; the branch's
calibrated falsifiers remain entries 7 and 31. CORRECTION to
the earlier floor claim: "8 unread, unobtainable on every free route, 16% irreducible" was
overstated — a second sweep on 2026-08-23 evening found free copies of 31 (VU Amsterdam academic
mirror), 36 (arXiv astro-ph/9812063, missed under API throttling), and 57 (author's UC Davis
page). Further shrunk 2026-08-23 22:30: entry 49 obtained via APS's IP entitlement on the CNU
campus address (Duho's insight — the Studio is inside the licensed range). Elsevier tested the
same way and CNU does NOT subscribe to the pre-1995 backfile ("does not subscribe to this
content", sighted on entry 48's page). The true credential wall is the 4 Elsevier papers — 42,
47, 48, 50 — ≈8%, needing document delivery / interlibrary loan, not just campus IP. Notes per paper in
`bhu-reading-20260823/`. **SUPERSEDED 2026-08-29 — this read "TWO live calibrated falsifiers: entry 54 … and entry 31".
Entry 54 is no longer calibrated** (re-tiered 2026-08-28 to QUALITATIVE-DIRECTIONAL; its Eq. 27 is
not a predicted window). The live calibrated falsifiers are **entry 31** (no neutron star above
Smolin's stated 2.5 M☉ bar — live as stated, though C08 adjudicated its Brown–Bethe instrument limb
broken at ≥8σ) and **entry 51**. The fired ones are entries 7 and 44. See the standing table in §0. Reading
corrected three triage-derived record claims in batches 1–5 and this floor claim in batch 6).

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
Testability: **CONSISTENCY-ONLY**. READ 2026-08-23 (Tori). Two pages of Bohr-quantization dimensional analysis — 10¹²² bits, no dynamics, no falsifier. The gate's low-weight/high-fit triage note was exactly right.
Record: harvest #16; direct universe-as-BH claim — the gate notes scientific weight may be low while scope fit is high.

## 2. Cosmological natural selection — the calibrated falsifier

**6. L. Smolin (1992). "Did the universe evolve?" Class. Quantum Grav. 9, 173–191.**
DOI 10.1088/0264-9381/9/1/016 — VERIFIED (Crossref: CQG, v9, p173-191, 1992-01).
Claim: universes reproduce through black holes with mutated constants, so our constants should be
near-optimal for black-hole production. (*The Life of the Cosmos* is the book-length version —
Appendix A6.)
**Full text OBTAINED 2026-08-23 ~23:00 KST** via IOP's IP entitlement on the Studio's CNU campus
address (second publisher opened by the campus-IP route; no credentials). Pinned:
`bhu-reading-20260823/sources/smolin_1992_did_the_universe_evolve_cqg9_173.pdf` (sha256
951bba97…, 20 pp, IOP header verified).
Testability: **QUALITATIVE-DIRECTIONAL** — READ 2026-08-23 (Tori, batch 9), **reclassed from
CALIBRATED-FALSIFIER**, the fourth triage-inherited class overturned by reading. The 1992 text
contains no neutron-star maximum-mass falsifier — no kaon condensation, no mass threshold. Its
three examples (inflaton λ ≈ λ_critical with a δρ/ρ that "cannot yet be taken seriously"; the
Δm sign argument Rothman–Ellis attacked; cold big-bang effects) are all directional, and the
conclusions concede the gap verbatim: the proposal "cannot be taken very seriously unless a
detailed scenario … falsifiable by some combination of experiment and theory, can be developed."
The calibrated falsifiers of this branch live where they were written: entry 7 (2008) and entry
31 (2004). Notes: batch 9.
Record: characterized in packet §1.4; the packet's [VERIFY] on the CQG citation is fully
resolved — publication and content both.
Audit-worthiness: **high** — the founding formulation; hypothesis S in original form, with the
locality-of-test point (compute R(p) only near our parameters) the later dialogue relies on.

**7. G. E. Brown, C.-H. Lee, M. Rho (2008). "Kaon Condensation, Black Holes, and Cosmological Natural Selection." Phys. Rev. Lett. 101, 091101.**
DOI 10.1103/PhysRevLett.101.091101 — VERIFIED (Crossref: PRL, v101, 091101, 2008-08-28).
(Publisher's Note PRL 101, 119901 pins the threshold symbol ≳, per the Phase 1 custody audit.)
Claim: the Brown–Bethe kaon-condensate EoS gives M_max ≈ 1.5 M☉; a neutron star with M ≳ 2 M☉
"would put in serious doubt or simply falsify" the chain including CNS.
Testability: **CALIBRATED-FALSIFIER / FIRED** *(standing appended 2026-08-29 for consistency with entries 51 and 44; the FIRED/LIVE value is UNCHANGED and is taken from the standing table in §0, not newly decided here)* — the family's clean number + threshold.
Record: **FIRED as to the Brown–Bethe / VM-HLS / kaon-condensation instrument chain at M ≳ 2 M☉;
for CNS the source supports "serious doubt" / "serious obstacle" / "put in doubt", NOT simple
falsification.** *(Corrected 2026-08-28 by two-seat audit — `CGATE_ENTRY7_VERDICT.md` and
`AGATE_ENTRY7_VERDICT.md` in `bhu-theory-phase6-curvature-20260827`, both UPHOLD_WEAK, each reading
the pinned APS version of record. The prior wording — "already adjudicated in our record — falsified
via limb 2" — assigned the disjunction's strong limb to CNS. The authors distribute the two limbs
deliberately and do not: the body's falsifiable prediction attaches "falsifies" to VM of HLS and
kaon condensation only, and CNS is not the object of that verb; the conclusion, in the authors' own
voice, gives BB and CNS a "serious obstacle"; the CCS/gravitational-wave passage again says
"falsify the BB scenario" but only "put in doubt the CNS theory". Reproduced: `c5_entry7_audit.py`
5/5, exit 0. Consequence for the record's coherence: because entry 7 did NOT kill CNS at ≳2 M☉,
entry 31's `2.5 M☉` bar is not moot, and its LIVE_CALIBRATED ruling stands — both seats declined to
overturn it. Both seats also noted that this tier conflates the NATURE of a claim with its STATUS:
entry 7 is CALIBRATED-FALSIFIER / FIRED, entry 31 is CALIBRATED-FALSIFIER / LIVE.
**STALE AS OF 2026-08-29 — this sentence used to continue "and the record carries no status axis
to say so. That schema change is NOT made here." Both halves are now false:** the standing table
in §0 IS that axis and predates this note's staleness, entry 51 carries the combined form inline,
and the schema question was closed on Duho's instruction "answer question 3" — see entry 44.)* The packet Rev 4 carries
the measurement facts:
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
no document (both checked 2026-08-21). **Full text OBTAINED 2026-08-23**: the published Physica A
PDF is openly hosted on a VU Amsterdam academic collection
(few.vu.nl/~wimu/Varying-Constants-Papers/Smolin-Physica-2004.pdf); pinned as
`bhu-reading-20260823/sources/smolin_2004_cns_physica_a340.pdf`
(sha256 46e57c43…, header/pagination verified: Physica A 340 (2004) 705–713).
Testability: **CALIBRATED-FALSIFIER / LIVE** *(standing appended 2026-08-29 for consistency with entries 51 and 44; the FIRED/LIVE value is UNCHANGED and is taken from the standing table in §0, not newly decided here)* — READ 2026-08-23 (Tori). §4 states the falsifier in the
author's own words: if the strange-quark mass is below a critical value, kaon condensation caps
neutron stars at "approximately 1.5 M☉" (attributed to Bethe–Brown calculations [52–54], not to
CNS itself); a sufficiently heavy neutron star refutes S, and "sufficiently high is certainly
2.5 M☉, although if one is completely confident of Bethe and Brown's upper limit of 1.5 solar
masses, any value higher than this would be troubling." This **confirms Track C's central
findings from the primary text**: CNS does not predict M_max ≈ 1.5 (that number is Brown–Bethe's
instrument).

**STATUS REWRITTEN 2026-08-29 on Duho's ruling — TWO BRANCHES, no winner picked.** This row
previously read "LIVE, 1.36σ short". That single number belonged to neither branch and rested on
an uncertainty (±0.11) with no pinned origin; the published figure is ±0.17. Replaced by:

| estimate | measurement | method | vs the 2.5 M☉ bar |
|---|---|---|---|
| — | PSR J0740+6620, 2.08 ± 0.07 | radio timing, relativistic Shapiro delay (Fonseca 2021) | **6.00σ** |
| — | PSR J0952−0607, **2.35 ± 0.11** | optical light curve + radial velocities (Romani **2025**, arXiv:2512.05099) | **1.36σ — P(M>2.5) = 8.6%** |
| — | GW190814 secondary, 2.50–2.67 (90%) | gravitational waves (**Abbott 2020**, arXiv:2006.12611) | **conditional — identity unresolved** |

*Not branches to choose between: three estimates bearing on one quantity, with different
likelihoods and systematics.* The related M_TOV = 2.210 +0.116 −0.123 (2σ) is a **separate paper**
(**Nathanail 2021**, arXiv:2101.01735), not the source of the GW190814 mass — an attribution this
row previously got wrong. On a **matched 2σ footing** GW190814's interval is **[2.482, 2.688]**,
whose lower bound falls **below** the bar, so it does not lie wholly above it at comparable
credibility.

**CORRECTED 2026-08-29 16:0x after an adversarial gate.** The two rows above are **two estimates
of one quantity with different systematics**, NOT two branches between which one must choose.
My earlier framing — that Smolin's "binary pulsar data" sentence sets a permanent instrument
criterion — was **refuted from his own footnote 5: "Other methods yield less precise estimates
[58]."** He ranks other methods by precision; he does not exclude them. Duho's ruling to keep
both is right, and now rests on the right reason: both are evidence.

**Row B's uncertainty is ±0.11, not ±0.17, and our record was right.** Romani et al. 2025
(arXiv:2512.05099, *"Tightening a Record-High Neutron Star Mass"*, now pinned) supersedes the 2022
±0.17. **The live figure is 1.36σ short, 8.63% posterior above the bar** — exactly what this row
carried before I wrongly called it unsourced. I had pinned the 2022 paper and treated it as
current.

**What remains undecided is not the instrument but the OBJECT**: whether a given compact object is
securely a neutron star, and how precise its mass estimate is.

**THE BAR IS GRADED AND THIS ROW NOW TRACKS BOTH.** The quotation above always carried it; the
*tracking* collapsed to 2.5 alone. Smolin gives **2.5 M☉ for certain refutation** and **1.5 M☉ for
"troubling"**, conditional on crediting Bethe–Brown. **The 1.5 bar was passed years ago — by both
measurements above, including the radio-timed one, i.e. by exactly the instrument Smolin named.**
His own factual premise, that all well-measured masses "are all below 1.5 M☉", is now false. A
record tracking only the higher bar hides a fired condition.

**Gravitational-wave leg, pinned 2026-08-29 AFTER the ruling and not covered by it.** GW190814's
secondary is **2.50–2.67 M☉ (90%)** — the entire interval at or above the bar — and the discovery
paper declines to classify it: *"either the lightest black hole or the heaviest neutron star."*
The tension analysis (`2101.01735`) states the conditional and its own preferred
M_TOV = 2.210 +0.116 −0.123 (2σ) puts the bar **above** that interval. So a third and fourth
reading exist, pointing opposite ways. See `ENTRY31_STUDY.md` §6. **Not folded into Duho's
two-branch ruling; flagged for him.**
Footnote 6 concedes in print that S could be saved by ad-hoc parameter-coupling fixes and
disclaims them absent independent support. Footnote 1 cites Rothman & Ellis (1993) [13] as the
source of the open-universe correction — corroborating appendix A0's citation trail **(READ 2026-08-29 — this said "their paper itself remains unread")**. Acquired as a free ADS
scan, `rothman_ellis_1993_qjras34_201.pdf`, 179,670 b, sha256 `ad76b7ace95c…`, 12 pp. **Their
critique targets Smolin 1992 — entry 6 — not this 2004 paper**, a distinction the record had not
drawn. Its central objection is *unidirectionality* — the scenario needs every parameter change to
reduce black-hole counts, while raising α or M_LC does the opposite — which the authors call a
"basic flaw in Smolin's scenario". They twice conclude his result is "probably reversed", and for
Δm = 0 say our universe would have *more* black holes, "in contradiction to his hypothesis". **And
page 209 confronts him with data**: cold/tepid-Big-Bang models, "in the wake of the COBE
observations … can almost certainly be pronounced dead." They nonetheless close by calling the
programme "certainly worth pursuing" — so it is a constructive endorsement of the programme
alongside attempted refutations of its concrete arguments.
**GATED**: `AGATE_B20` TRANSCRIPTION_CONFIRMED, `CGATE_B20`
TRANSCRIPTION_NARROWED_MISSED_COBE_CONFRONTATION. Both seats rendered the scan and verified every
quotation word-by-word — necessary because the scan has no text layer, so nothing here is
grep-verifiable. *(An earlier draft of this note called it "not a confrontation with data";
**withdrawn** — I had read pages 1, 2 and 11 and skimmed the rest, and page 209 is in the part I
skimmed.)*
**Bearing on this entry's own falsifier**: the objection is *upstream* of the 2.5 M☉ bar — it asks
whether the selection argument yields a prediction at all, not whether that prediction holds. The
seats split on how hard to put that; **the weaker form is adopted**: the bar's selection-theoretic
warrant is weakened or made conditional, not severed, since Rothman & Ellis analyse Smolin 1992 and
never touch the 2004 mass argument. **No tier change.** Smolin's §3 groups this with three others
as arguing S is "contradicted by present observation" — [13] supplies that for *one limb only*.
**[30] Harrison 1995 READ 2026-08-29** (`b21_harrison_objection.py`, gated `HARRISON_REFUTED_TENSION`
/ `HARRISON_REFUTED_CROSS_ENTRY_TENSION`): it is a **rival cosmology** — universes built by
intelligent life in a parent universe — not an observational refutation, and neither seat found any
confrontation with data on pp. 194–201. Its objection to Smolin sits in reference-note (11) and is
**topological**: a spatially closed universe recollapsing to a single future singularity swallows
every black hole into the common crunch, so "the black hole population fails to affect the
reproductive rate of universes, and each closed universe in Smolin's theory produces at most one
offspring universe." That attacks the *selection mechanism*, upstream of the mass bar. **It is
bounded**: it needs a RECOLLAPSE, so it does not reach bounce cosmologies — including entry 54's,
whose Ω_k < 0 is closed geometry *with* a bounce. *(A proposed cross-entry tension between entries
31 and 54 was refuted by both seats on exactly that distinction and is withdrawn; the bound is what
survives, recorded so nobody rediscovers the "tension" and files it.)*
**[14] Ellis 1993 READ 2026-08-29** (`b22`, both seats read it in full): it is a review of five
cosmological paradigms, **not a critique** — its only substantive mention of Smolin, p. 328, is
*favourable*, and it delegates criticism in one clause to Rothman & Ellis. **[31] Silk 1997
paywalled and unread.** Three of four read, and none is primarily "contradicted by present observation" — but **no conclusion is drawn** about Smolin's
collective characterisation until all four are.. Reader's note (mine, not the text's): §3's Λ discussion ends in an explicit
conjecture ("one can conjecture that the present value of Λ maximizes the formation of black
holes"), not a result.
Record: the CNS audit chain's missing base entry, now read; Track C's published-record basis is
upgraded to primary-source-confirmed. **Stale line corrected 2026-08-29:** this previously read
"with entry 54, this gives the family a SECOND live calibrated falsifier". Entry 54 was
subsequently demoted to QUALITATIVE-DIRECTIONAL, so entry 31 is the family's **only** candidate —
and per the two-branch status above, whether it is live at all is undecided.
Audit-worthiness: **high** — now discharged for the falsifier statement itself; entry 6 (CQG 9,
173) remains the other primary text for the theory's original formulation.

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
Testability: **CONSISTENCY-ONLY**. READ 2026-08-23 (Tori). Refines the PLB 694 bounce with all SM degrees of freedom: ε_bounce = 15.4 ε_Pl — above Planck density, a validity limit the paper concedes itself — with preons or trans-Planckian classicality as undischarged escapes; averaging still cited, not derived. Strengthens, and does not contradict, the Phase 2 audit.
Record: recalled by the gate with its DOI remembered EXACTLY (verified digit-for-digit); fills the hole between the 2010 and 2012 mechanism papers of this branch.

**40. N. Popławski (2021). "Gravitational collapse of a fluid with torsion into a universe in a black hole." J. Exp. Theor. Phys. 132, 374 (Zh. Eksp. Teor. Fiz. 159, 448).**
DOI 10.31857/S0044451021030068 — VERIFIED (Crossref: ZhETF, v159, p448-456, 2021). Added 2026-08-22 from the bibliography gate
(`bhu-biblio-gate-20260822/BGATE_VERDICT.md`, HOLD_BIBLIO_DIRECT_OMISSIONS). Tier: **W1**.
Testability: **CONSISTENCY-ONLY** **[BLIND-FLAGGED 2026-08-28, NOT ADJUDICATED — tier UNCHANGED.** A blind re-classification proposed promoting this to QUALITATIVE-DIRECTIONAL. Deliberately not gated: that sweep failed its own control (see the standing note above the entry list). The flag is a candidate from a biased instrument, not a finding. Do not promote on it.]. READ 2026-08-23 (Tori). Tolman-metric homogeneous collapse; the no-singularity result holds for the SHEAR-FREE case by construction, with inhomogeneous/rotating collapse expressly open. The R₀→π cycle asymptotics is the uncompressed lineage of the audited 2025 paper's B-14 defect.
Record: harvest #10; the mechanism's direct collapse continuation, published in JETP.

**41. N. Popławski (2021). "A nonsingular, anisotropic universe in a black hole with torsion and particle production." Gen. Relativ. Gravit. 53, 18.**
DOI 10.1007/s10714-021-02790-7 — VERIFIED (Crossref: GRG, v53, 2021-02). Added 2026-08-22 from the bibliography gate
(`bhu-biblio-gate-20260822/BGATE_VERDICT.md`, HOLD_BIBLIO_DIRECT_OMISSIONS). Tier: **W1**.
Testability: **CONSISTENCY-ONLY** **[BLIND-FLAGGED 2026-08-28, NOT ADJUDICATED — tier UNCHANGED.** A blind re-classification proposed promoting this to QUALITATIVE-DIRECTIONAL. Deliberately not gated: that sweep failed its own control (see the standing note above the entry list). The flag is a candidate from a biased instrument, not a finding. Do not promote on it.]. READ 2026-08-23 (Tori). Proves torsion alone loses to shear (σ² grows faster than a⁻⁶) and patches it with phenomenological βH⁴ particle production — the explicit form of the step the A2 audit marked heuristic (B-13), conceded in the mathematics and repaired with a free parameter.
Record: harvest #11; parentage construction beyond isotropy.

**51. N. J. Popławski (2010). "Nonsingular Dirac particles in spacetime with torsion." Phys. Lett. B 690, 73–77.**
DOI 10.1016/j.physletb.2010.04.073 — VERIFIED (Crossref: PLB, v690, p73-77, 2010). Added 2026-08-23, hunt round 2
(`bhu-biblio-gate-20260822/K2GATE_VERDICT.md` + `MORNING_HUNT_REPORT.md`). Tier: **W1**.
Testability: **CALIBRATED-FALSIFIER / LIVE** — re-tiered 2026-08-28 from QUALITATIVE-DIRECTIONAL by a blind re-classification, upheld by two independent gates (`bhu-theory-phase6-curvature-20260827/`: CGATE_ENTRY51_VERDICT.md, codex gpt-5.5; AGATE2_ENTRY51_VERDICT.md, hermes gpt-5.6-sol). READ 2026-08-23 (Tori). Dirac fields in ECKS cannot be singular; Cartan-radius extent, max density ~10⁵¹ kg/m³, minimum black-hole mass ~10¹⁶ kg (~10⁴³ GeV).
**The author's stated test is the LHC route**, verbatim: "Therefore the Large Hadron Collider (LHC), which can operate at energies up to ~10⁴ GeV, cannot produce micro black holes … if the four-dimensional ECKS theory is a correct theory of gravity." One-sided and positive-detection only: a confirmed black hole far below the ~10¹⁶ kg floor fires it; a null LHC search fires nothing. LIVE/unfired. **MEASUREMENT SIDE PINNED 2026-08-29** — this previously read "CMS reports no
evidence for microscopic black holes as of 2025-12" with **no citation of any kind**. Now
receipted: `2604.10732_clean.txt` (CMS, 13 TeV, 138 fb⁻¹) excludes semiclassical black holes and
string balls **below 8.4–11.4 TeV at 95% CL** (string balls 9.0–10.7), a model-dependent range, and `2511.10662_clean.txt` is the ML-based search on the
same dataset. Both set limits; neither reports a discovery.
**And the null is a weak CONFIRMATION, not a non-event**: Popławski forbids black holes below
~10¹⁶ kg (≈5.6×10⁴² GeV by E=mc², reproducing the record's ~10⁴³), CMS searched a range lying
*entirely inside* that forbidden region, and found nothing — which is what the theory predicts.
"One-sided, a null fires nothing" is right about firing and understates what a null contributes.
**The LHC route is bounded, not merely unexhausted**: each exclusion pushes the possible-detection
window upward and the collider's energy caps where it can go. An astrophysical constraint on
primordial black holes below 10¹⁶ kg would probe the same forbidden region without a collider —
a route this record does not currently track. See `b11_entry51_measurement.py` (2/2).
**GATED 2026-08-29 — route CONFIRMED IN DIRECTION, NARROWED IN STRENGTH.**
`b12_entry51_pbh_route.py` (8/8), `CGATE_B12_VERDICT.md` (ROUTE_NARROWED_FLOOR_AND_DETECTION_NOT_PINNED,
codex) + `AGATE_B12_VERDICT.md` (ROUTE_NARROWED_MATH_ERROR, agy), brief `GATE_BRIEF_B12.md`.
**What holds:** Popławski's floor is a bound on *density* — "the mass density of a black hole also
cannot exceed ρ_Ce" — stated 236 characters *before* the LHC sentence, so the LHC is his corollary
and **this record has been carrying his illustration as his scope**. Primordial black holes are
therefore a route, and the record previously had none but the collider.
**What was cut:** (a) the derivation is about *fermionic* matter — "Dirac particles cannot be
compressed to densities higher than the densities of its components" — so it does **not** cover
every PBH formation channel Carr et al. list (radiation overdensities, scalar condensates,
false-vacuum bubbles, domain walls); (b) 10¹⁷–10²³ g is a **caveated** window, not an open one —
the review's limits mostly assume a quasi-monochromatic spectrum, and sub-10¹⁸ g PBHs are reported
at <1% of DM (Laha et al., SPI/INTEGRAL); (c) **no present detection protocol is pinned** — the
GRB femtolensing bound over 5×10¹⁶–10¹⁹ g is disputed and omitted from the review's master plot;
(d) the forbidden band is 2.00 decades on the printed floor but **0.43 decades** on the floor
inverted from the paper's own ρ_Ce, a factor >4 in log width.
**What got broader:** firing it does *not* require PBHs to be the dark matter — a securely
identified primordial black hole below the floor suffices, trace population included.
**A number here was wrong and is corrected above:** "8.7 TeV" was never in the CMS source; an
extraction truncated the digit and I supplied it. The collider comparison is in any case
illustrative rather than a shared axis — CMS bounds *production* in large extra dimensions,
Popławski bounds *density* in 4D ECKS. Popławski's own "39 orders of magnitude" needs no CMS
figure at all.
**Open for Duho:** the seats split on whether 10¹⁶ kg is an arithmetic error (agy) or a stacked
order-of-magnitude estimate that must not be called one (codex). Both compute 2.7×10¹⁴ kg. Filed
in `OPEN_QUESTIONS_FOR_DUHO.md`; it changes no action here. Entry 51's tier is UNCHANGED either way.
**Reachability, ruled on by both gates:** the ~10³⁹ gap between LHC reach and the floor does NOT empty the threshold, because the collider operates on the *forbidden* side already — a detection far below the floor is a counterexample and cannot be rescued by shrinking the effect. Unlike entry 54, whose magnitude could retreat toward zero. Calibration is coarse: the source says "expect", "approximately", "conjecture", and gives no uncertainty interval or cross-section.
**WHAT IT FALSIFIES — scope, and it is not BHU.** The target is the four-dimensional ECKS density/minimum-mass chain. Entry 51 constrains a black-hole-universe model only where that model inherits the same ECKS premise. Not a direct BHU falsifier from this source.
**CORRECTION 2026-08-28 (Tori, against my own 2026-08-23 entry):** the sub-10¹⁶-kg primordial-black-hole discriminator is **mine, not Popławski's** — the second gate grepped the full text and found no occurrence of "primordial", "PBH", or "black-hole universe". My further claim that standard physics permits such a PBH is also not established by this paper. It may be recorded as a reader-derived route; it must not be attributed to the author. My original entry also called this "a numbered falsifiable consequence" while filing it QUALITATIVE-DIRECTIONAL — the evidence was in hand and mis-tiered anyway.
Record: kimi recall R6; the singularity-avoidance mechanism paper under the torsion-bounce line.

**52. "Big Bounce and Closed Universe from Spin and Torsion." ApJ 870, 78 (2019).**
DOI 10.3847/1538-4357/aaf169 — VERIFIED (Crossref: ApJ, v870, 78, 2019). Added 2026-08-23, hunt round 2
(`bhu-biblio-gate-20260822/K2GATE_VERDICT.md` + `MORNING_HUNT_REPORT.md`). Tier: **W1**.
Testability: **CONSISTENCY-ONLY**. READ 2026-08-23 (Tori). The k=1 correction to the audited 2016 ApJ paper (whose bounce values 'de facto considered a flat universe', per this paper). Quantifies the production requirement: C ~ aT must grow ~48 orders of magnitude to reach dark-energy acceleration — the free dial now has a required range and still no mechanism.
Record: harvest+triage pick #2; authors omitted pending the record itself (entry-42 precedent).

**53. "Analysis of big bounce in Einstein–Cartan cosmology." Class. Quantum Grav. 37, 025011 (2019).**
DOI 10.1088/1361-6382/ab5cb9 — VERIFIED (Crossref: CQG, v37, 025011, 2019). Added 2026-08-23, hunt round 2
(`bhu-biblio-gate-20260822/K2GATE_VERDICT.md` + `MORNING_HUNT_REPORT.md`). Tier: **W1**.
Testability: **CONSISTENCY-ONLY**. READ 2026-08-23 (Tori). CORRECTION: this is Cubero & POPŁAWSKI — same UNH group, companion to entry 52, NOT an independent line as the triage-derived record here briefly claimed. New structural result: the scale-factor bounce is double, with a single temperature bounce and a little crunch between.
Record: triage pick #7; a same-group companion analysis (Cubero & Popławski) — the 'independent line' triage claim was wrong and is corrected above.

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

**42. P. F. González-Díaz (1991). "Baby universe metric equivalent to an interior black-hole metric." Phys. Lett. B 261, 357–362.**
DOI 10.1016/0370-2693(91)90440-2 — VERIFIED (Crossref: PLB, v261, p357-362, 1991-06). Added 2026-08-22 from the bibliography gate
(`bhu-biblio-gate-20260822/BGATE_VERDICT.md`, HOLD_BIBLIO_DIRECT_OMISSIONS). Tier: **W1**.
Testability: **UNREAD** — full text unexamined here; class not assigned second-hand.
Record: harvest #31; early interior-equivalence result. Author filled 2026-08-23 from INSPIRE metadata (the record, not recall), resolving the earlier deliberate omission. Full text: paywalled, needs-access queue.

**43. "Birth of baby universes from gravitational collapse in a modified-gravity scenario." JCAP 06 (2023) 028.**
DOI 10.1088/1475-7516/2023/06/028 — VERIFIED (Crossref: JCAP, v2023, 028, 2023-06). Added 2026-08-22 from the bibliography gate
(`bhu-biblio-gate-20260822/BGATE_VERDICT.md`, HOLD_BIBLIO_DIRECT_OMISSIONS). Tier: **W1**.
Testability: **CONSISTENCY-ONLY**. READ 2026-08-23 (Tori). The corpus's only numerical-relativity demonstration of baby-universe birth: perturbed boson stars in Palatini f(R), throat hidden inside a horizon at all times. Conditional on the modified gravity; no observable.
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
Testability: **THEORETICAL-OBSTRUCTION** — **refiled 2026-08-29 on Duho's ruling ("then add
another category").** Previously CONSISTENCY-ONLY, which is wrong in *both* halves of that
definition: this paper neither shows compatibility with observation nor merely fails to state a
prediction. It **proves that a class of constructions cannot work** (Proposition 1, Proposition 2,
Theorem 1). The new tier asserts: *no member of a specified class of models can satisfy a
specified conjunction of conditions; refuted by exhibiting a counterexample in that domain, not by
any measurement.* Membership criterion and its controls: `b1_theoretical_obstruction_tier.py`.
**DOMAIN STATED 2026-08-29** (`b24_entry22_warrant.py`, gated `SCOPE_REFUTED_INFLATED_COUNT_AND_HOSTILE_FRAMING`
/ `SCOPE_NARROWED_COUNT_AND_CELL`) — the tier definition above says "a *specified* class" and "a
*specified* conjunction" and the entry never said which. It is: **Proposition 1** excludes
identifying the natural trapped slicing with exact FRW; **Proposition 2** bounds nondegenerate
comoving no-shell closed-FRW daughters of static, asymptotically flat, finite-ADM parents; the
**flat/open limb** additionally assumes curvature regularity, regular affine ends and ANEC. Shells,
modified asymptotics, non-FRW or non-comoving evolution, and added bulk stress-energy are
**expressly outside** the result — the author names these escape routes himself. Proof skeleton
checked against the source; the external completeness theorem was not independently verified.
*(This is a DOMAIN note, not a warrant flag. I first proposed the cell "scope-limited by
construction — eleven stated conditions", and both seats refuted it: the eleven was a count of
**phrases**, not assumptions — the real figure is eight hypothesis groups, or four-to-five
independent physical assumptions — and treating a theorem's stated hypotheses as a defect damns
ordinary rigour with scope. The paper advertises "minimal" in its own title. Propositions 1 and 2
are in fact **broader** than Theorem 1's headline: Prop 1 needs no matching, asymptotics or shell
assumption at all, and Prop 2 is independent of the regular core.)*
*(A follow-up I flagged — that this record's interior-matching series might fall outside the no-go
by using Israel junction conditions — is **FALSE and withdrawn**. Easson cites Israel and calls his
own conditions "Darmois–Israel **no-shell** conditions", and `2505.23877` states "No additional
surface term or exotic matter layer is required." Verified against both sources directly.)*

**PUBLICATION CAVEAT DISCHARGED 2026-08-29.** The "flagged for Miru's spot-check" above never
happened — Miru is a retired seat. Resolved instead at the A7 gate: **Phys. Rev. D 114, 044077,
published 24 August 2026** (received 25 June, accepted 31 July), DOI `10.1103/qs86-npwk`, verified
from APS by the codex seat. Note the date correction: **2026-07-31 was the ACCEPTANCE date**, not
publication. Still testimony rather than a pinned receipt — a seat's lookup, not a document in
this corpus.

Record: baseline corpus entry, now the sole member of a new tier. Audit-worthiness: **high** —
see ranked target 5.

**55. "Asymptotically de Sitter universe inside a Schwarzschild black hole." Phys. Rev. D 102, 066010 (2020).**
DOI 10.1103/physrevd.102.066010 — VERIFIED (Crossref: PRD, v102, 066010, 2020). Added 2026-08-23, hunt round 2
(`bhu-biblio-gate-20260822/K2GATE_VERDICT.md` + `MORNING_HUNT_REPORT.md`). Tier: **W1**.
Testability: **CONSISTENCY-ONLY**. READ 2026-08-23 (Tori). LQG interior bounce beyond minisuperspace; γ ≈ 0.274 gives an asymptotically de Sitter interior, and that γ coincides exactly with LQG's independent black-hole-entropy value. Suggestive, no falsifier — the quantum partner to entry 39's Planck-validity concession.
Record: triage pick #41 — kimi's #1 base candidate; the most direct recent interior-universe construction.

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

**56. "The mass of our observable Universe." MNRAS Lett. 521, L59–L63 (2023).**
DOI 10.1093/mnrasl/slad015 — VERIFIED (Crossref: MNRAS Lett, v521, pL59-L63, 2023). Added 2026-08-23, hunt round 2
(`bhu-biblio-gate-20260822/K2GATE_VERDICT.md` + `MORNING_HUNT_REPORT.md`). Tier: **W1**.
Testability: **QUALITATIVE-DIRECTIONAL**. READ 2026-08-23 (Tori), from the published MNRAS PDF. Finite-mass universe inside its own r_S; Λ = 3/r_S² as a boundary effect; M_T ≈ 6×10²² M☉. States its smoking gun — a cut-off in the largest-scale perturbations — with cited CMB measurements.
Record: triage pick #1; completes the published Gaztañaga series in this branch.

**54. "Gravitational bounce from the quantum exclusion principle." Phys. Rev. D 111, 103537 (2025).**
DOI 10.1103/physrevd.111.103537 — VERIFIED (Crossref: PRD, v111, 103537, 2025). Added 2026-08-23, hunt round 2
(`bhu-biblio-gate-20260822/K2GATE_VERDICT.md` + `MORNING_HUNT_REPORT.md`). Tier: **W1**.
Testability: **QUALITATIVE-DIRECTIONAL** (re-tiered 2026-08-28; was CALIBRATED-FALSIFIER). READ 2026-08-23 (Tori), RE-READ 2026-08-27 (Tori, phase 6). The surviving hard prediction is a **direction**: closed curvature, Ω_k < 0 — source line 336, "Inflation preceded by a bounce requires Ω_k < 0." Eq. 27 (`Ω_k = −(0.07 ± 0.02)(χ_*/χ_k)²`) is not a predicted window: the paper requires χ_k > χ_* (line 306), so the factor is strictly below 1 and Ω_k may approach 0 from below without limit; line 336 further conditions the magnitude on attributing the homogeneity scale to χ_* alone. **Operational annotation — falsifiable only from the open side:** a confirmed Ω_k > 0 refutes; **flatness at any finite precision does not** — the paper itself concedes "the current uncertainties remain too large to decisively rule out a flat universe" (line 480); a confirmed Ω_k ≲ −0.09 refutes only under the authors' own conditional χ_* identification. Exactly Ω_k = 0 would contradict the model, but exact flatness is not confirmable by any finite-precision observation, so that reading is operationally empty. Cites Planck PR3's 3σ preference for Ω_k ≈ −0.04 and same-direction ACT/DESI trends. **MEASUREMENT SIDE PINNED 2026-08-29** (`b15_entry54_curvature.py`, 5/5,
`AGATE_B15_VERDICT.md`). That sentence relays the source paper accurately — the "3σ" is its own
wording (line 480) — and an earlier draft of this note wrongly charged it with overstating Planck;
**that charge is withdrawn**, since Planck's "only about 1/10000 samples at Ω_K ≥ 0" is ~3.7σ, so
its "well over 2σ" is a floor. What the record was missing is Planck's **own resolution**, now
pinned at `1807.06209_clean.txt`: the TT,TE,EE+lowE value is Ω_K = −0.044 (+0.018/−0.015), but
*"combining with the lensing reconstruction (which is consistent with a flat model) pulls
parameters back into consistency with a spatially flat universe to well within 2σ"* — **Ω_K =
−0.0106 ± 0.0065**. Planck also ties the pull to the same systematic as its A_L anomaly and calls
the polarization result not robust at ~0.5σ to likelihood modelling (CamSpec: −0.037 +0.019/−0.014).
**So this is a live dispute and the record carried one side of it**; the paper takes the closed
side and cites Di Valentino et al. 2020 for it (not pinned here). `CGATE_B14_VERDICT.md` adds, from
a phase-6 citation audit, that the ACT paper's own summary runs contrary to our "same-direction"
gloss and the cited DESI analysis *assumes* Ω_K = 0 — **that is a seat's testimony, not verified
here.** Tier UNCHANGED; the weekly Ω_k sign watcher is unaffected and was checked, not assumed. NOTE: mis-seated in branch 3 at integration — this is Gaztañaga-line GR + quantum exclusion, no torsion; moved to branch 6, number unchanged.
Record: triage pick #27; the newest published bounce mechanism in the family.

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
**Full text OBTAINED 2026-08-23** via its arXiv version (astro-ph/9812063 — the eprint my
campaign-time checks missed under arXiv throttling); pinned as
`bhu-reading-20260823/sources/smoller_temple_2000_shockwave_astroph9812063.pdf` (sha256
ef904904…, 66 pp, title verified).
Testability: **CONSISTENCY-ONLY** **[BLIND-FLAGGED 2026-08-28, NOT ADJUDICATED — tier UNCHANGED.** A blind re-classification proposed promoting this to QUALITATIVE-DIRECTIONAL. Deliberately not gated: that sweep failed its own control (see the standing note above the entry list). The flag is a candidate from a biased instrument, not a finding. Do not promote on it.] — READ 2026-08-23 (Tori). Constructs the simplest exact
Einstein solution with a true shock wave at the leading edge of a k=0 FRW expansion inside a
static TOV exterior, matched to the observed H₀ and CMB temperature; derives bounds putting the
shock position at present time comparable to the Hubble length. The paper is explicit that the
model violates the Copernican principle (Earth near the center of a localized explosion) and that
the shock makes the early explosion unreconstructable ("impossible to reconstruct the details of
the early explosion from present data"); it poses "could our expanding universe have evolved from
the center of a great explosion?" as a question and offers the solution as "a starting point",
deriving no observational discriminant beyond the length-scale consistency. Reader's note (mine,
not the text's): the anti-Copernican geometry implies in-principle radial anisotropies, but the
paper does not compute any.
Record: recalled by the gate's training-memory attack, missing from bibliography AND harvest; the
programme's founding cosmology paper.
Phase 4 (2026-08-25, gated PASS both engines): this branch's geometry now carries a
quantified SUFFICIENCY surface — an observer offset below x_max(t_obs) keeps every direct
post-recombination CMB ray inside the exact-FRW interior (pre-horizon epochs; other
messengers unanalyzed). Its only near-threshold signature is a single circular cap around
one axis, and the frozen large-angle anomalies are NOT morphology-compatible with it
(localization and patch-character fail on all seven frozen rows; scale evidence absent).
Class unchanged — CONSISTENCY-ONLY; the named path to a calibrated test is TOV-side optics,
uncomputed by anyone. Receipts: `../bhu-theory-phase4-anisotropy-20260823/`.
 The black-hole-interior version of this construction is
entry 37 (PNAS 2003); here the shock sits outside any horizon.

**37. J. Smoller & B. Temple (2003). "Shock-wave cosmology inside a black hole." PNAS 100, 11216–11218.**
DOI 10.1073/pnas.1833875100 — VERIFIED (Crossref: PNAS, v100, p11216-11218, 2003-09). Added 2026-08-22 from the bibliography gate
(`bhu-biblio-gate-20260822/BGATE_VERDICT.md`, HOLD_BIBLIO_DIRECT_OMISSIONS). Tier: **W1**.
Testability: **CONSISTENCY-ONLY** **[BLIND-FLAGGED 2026-08-28, NOT ADJUDICATED — tier UNCHANGED.** A blind re-classification proposed promoting this to QUALITATIVE-DIRECTIONAL. Deliberately not gated: that sweep failed its own control (see the standing note above the entry list). The flag is a candidate from a biased instrument, not a finding. Do not promote on it.]. READ 2026-08-23 (Tori). Theorem-grade exact GR: big bang as a localized explosion inside a Schwarzschild black hole, subluminous shock beyond the Hubble length, white-hole exit; σ=1/3 uniquely selected. The only paper read so far with no underived ingredient — and no stated falsifier.
Record: harvest #17; the branch-defining title. (Harvest metadata said 2002; Crossref says 2003 — the verified year is used.)

**38. J. Smoller & B. Temple (2004). "Cosmology, black holes and shock waves beyond the Hubble length." Methods Appl. Anal. 11, 77–132.**
DOI 10.4310/maa.2004.v11.n1.a7 — VERIFIED (Crossref: MAA, v11, p77-132, 2004). Added 2026-08-22 from the bibliography gate
(`bhu-biblio-gate-20260822/BGATE_VERDICT.md`, HOLD_BIBLIO_DIRECT_OMISSIONS). Tier: **W1**.
Testability: **CONSISTENCY-ONLY** **[BLIND-FLAGGED 2026-08-28, NOT ADJUDICATED — tier UNCHANGED.** A blind re-classification proposed promoting this to QUALITATIVE-DIRECTIONAL. Deliberately not gated: that sweep failed its own control (see the standing note above the entry list). The flag is a candidate from a biased instrument, not a finding. Do not promote on it.]. READ 2026-08-23 (Tori). The theorems behind entry 37. The authors' own caveat: 'only rough qualitative models' — the TOV-side equation of state cannot be imposed, only bounded. Rigor about the mathematics and equal rigor about its limits.
Record: recalled by the gate, missing from both documents; the programme's expanded interior construction.

**57. J. Smoller & B. Temple (1997). "General relativistic shock waves that extend the Oppenheimer–Snyder model." Arch. Rational Mech. Anal. 138, 239–277.**
DOI 10.1007/s002050050041 — VERIFIED (Crossref: ARMA, v138, p239-277, 1997). Added 2026-08-23, hunt round 2
(`bhu-biblio-gate-20260822/K2GATE_VERDICT.md` + `MORNING_HUNT_REPORT.md`). Tier: **W1**.
**Full text OBTAINED 2026-08-23**: the published version is self-archived on Blake Temple's UC
Davis page (math.ucdavis.edu/~temple/!!!PubsForWeb/cv47.pdf); pinned as
`bhu-reading-20260823/sources/smoller_temple_1997_oppenheimer_snyder_arma138_cv47.pdf` (sha256
6e709a9c…, 39 pp, Springer header verified: ARMA 138 (1997) 239–277).
Testability: **CONSISTENCY-ONLY** — READ 2026-08-23 (Tori). Pure mathematical infrastructure:
re-derives the FRW/Oppenheimer–Tolman shock-matching ODEs in simplified form, proves
Lax-admissibility conditions, and obtains formulas for shock/sound/fluid speeds for numerical
use. Explicitly restricted to shocks OUTSIDE the Schwarzschild radius (A > 0), and its §6 result
is that outside that radius the solutions model explosions, not collapse. No observational
content; the cosmological framing is one sentence (the FRW core may be "a star or the universe as
a whole", with the big bang beginning as a shock-wave explosion per their earlier PRD paper).
Record: kimi recall R5; the programme's method precursor, predating entry 36.
Phase 4 (2026-08-25, gated PASS both engines): this branch's geometry now carries a
quantified SUFFICIENCY surface — an observer offset below x_max(t_obs) keeps every direct
post-recombination CMB ray inside the exact-FRW interior (pre-horizon epochs; other
messengers unanalyzed). Its only near-threshold signature is a single circular cap around
one axis, and the frozen large-angle anomalies are NOT morphology-compatible with it
(localization and patch-character fail on all seven frozen rows; scale evidence absent).
Class unchanged — CONSISTENCY-ONLY; the named path to a calibrated test is TOV-side optics,
uncomputed by anyone. Receipts: `../bhu-theory-phase4-anisotropy-20260823/`.
 The
inside-the-horizon step the BHU reading cares about is entirely in later entries (36 stays
outside horizons too; entry 37 goes inside).

## 10. White-hole / holographic-origin big bang

Added 2026-08-22: distinct from branch 7's entangled-CFT interiors per the gate's branch-gap
finding; the big bang as the interior/exterior of a white-hole or 5D collapse.

**44. R. Pourhasan, N. Afshordi & R. B. Mann (2014). "Out of the white hole: a holographic origin for the Big Bang." JCAP 04 (2014) 005.**
DOI 10.1088/1475-7516/2014/04/005 — VERIFIED (Crossref: JCAP, v2014, 005, 2014-04). Added 2026-08-22 from the bibliography gate
(`bhu-biblio-gate-20260822/BGATE_VERDICT.md`, HOLD_BIBLIO_DIRECT_OMISSIONS). Tier: **W1**.
Testability: **CALIBRATED-FALSIFIER / FIRED** — re-tiered 2026-08-29 from QUALITATIVE-DIRECTIONAL on Duho's instruction *"answer question 3"*, which returned open question 3 to me to decide. **What fired is the Sec. 4 model, not the framework** — see the standing table in §0. Audit `b17_entry44_audit.py` (6/6), gates `CGATE_B17` / `AGATE_B17`, both of which called the previous label wrong and in this same direction. READ 2026-08-23 (Tori), AUDITED 2026-08-29 (Tori). 3-brane out of 5D BH formation; thermal atmosphere gives scale-invariance without inflation. Rare self-honesty: states its own base model is 'already ruled out at >5σ' (exact scale-invariance vs the observed red tilt) and names the fix as its immediate challenge.
**RECEIPTED 2026-08-29** (`b16_entry44_tilt.py`, 4/4): Planck 2018 VI eq. (19),
`1807.06209_clean.txt`, gives n_s = 0.9649 ± 0.0042 — *"which is 8σ away from scale-invariance
(n_s = 1), confirming the red tilt of the spectrum at high significance"* — and nearly 9σ adding
BAO (n_s = 0.9665 ± 0.0038). **So the paper's ">5σ" is true and conservative.** Found by
`CGATE_B14_VERDICT.md`: this is an experimental-status claim with a significance and *no
instrument named*, invisible to the sweep's original vocabulary.
Record: harvest #24; the 5D holographic/white-hole origin — the line the caption-era Afshordi identification traced back to.

**45. "White hole cosmology and Hawking radiation from quantum cosmological perturbations." Phys. Rev. D 106, 123505 (2022).**
DOI 10.1103/PhysRevD.106.123505 — VERIFIED (Crossref: PRD, v106, 2022-12). Added 2026-08-22 from the bibliography gate
(`bhu-biblio-gate-20260822/BGATE_VERDICT.md`, HOLD_BIBLIO_DIRECT_OMISSIONS). Tier: **W1**.
Testability: **CONSISTENCY-ONLY**. READ 2026-08-23 (Tori). QFT in the white-hole interior; Hawking radiation from cosmological-style perturbations. Reading revises the triage: not a universe-origin claim — family-adjacent; flagged for possible demotion to support, not unseated unilaterally.
Record: harvest #7; a second published white-hole cosmology route.

## 11. False-vacuum / laboratory child universes

Added 2026-08-23: the "can a universe be MADE inside a collapse" programme — sibling to branch 4,
recalled by the second-family gate and in neither the bibliography nor any harvest until tonight.

**47. K. Sato, H. Kodama, M. Sasaki & K. Maeda (1982). "Multi-production of universes by first-order phase transition of a vacuum." Phys. Lett. B 108, 103–107.**
DOI 10.1016/0370-2693(82)91152-2 — VERIFIED (Crossref: PLB, v108, p103-107, 1982). Added 2026-08-23, hunt round 2
(`bhu-biblio-gate-20260822/K2GATE_VERDICT.md` + `MORNING_HUNT_REPORT.md`). Tier: **W1**.
Testability: **UNREAD** — text unexamined here.
Record: kimi recall R4; the earliest multi-universe-production construction.

**48. E. Farhi & A. H. Guth (1987). "An obstacle to creating a universe in the laboratory." Phys. Lett. B 183, 149–155.**
DOI 10.1016/0370-2693(87)90429-1 — VERIFIED (Crossref: PLB, v183, p149-155, 1987). Added 2026-08-23, hunt round 2
(`bhu-biblio-gate-20260822/K2GATE_VERDICT.md` + `MORNING_HUNT_REPORT.md`). Tier: **W1**.
Testability: **UNREAD** — text unexamined here.
Record: kimi recall R1; the no-go analysis for manufacturing a child universe. (Kimi remembered p149-153; Crossref says 149-155 — verified pages used.)

**49. S. K. Blau, E. I. Guendelman & A. H. Guth (1987). "Dynamics of false-vacuum bubbles." Phys. Rev. D 35, 1747–1766.**
DOI 10.1103/physrevd.35.1747 — VERIFIED (Crossref: PRD, v35, p1747-1766, 1987). Added 2026-08-23, hunt round 2
(`bhu-biblio-gate-20260822/K2GATE_VERDICT.md` + `MORNING_HUNT_REPORT.md`). Tier: **W1**.
**Full text OBTAINED 2026-08-23 22:30 KST** via APS's IP-based institutional entitlement on the
Studio's CNU campus address ("Access Provided by Chungnam National University" — Duho's insight
that the Studio sits inside the licensed range; no credentials involved). Pinned:
`bhu-reading-20260823/sources/blau_guendelman_guth_1987_prd35_1747.pdf` (sha256 1d195f5f…, 20 pp,
PRD 35(6) 15 March 1987 header verified).
Testability: **CONSISTENCY-ONLY** — READ 2026-08-23 (Tori, batch 8). The family's strongest
peer-reviewed anchor for the exterior-black-hole / interior-closed-universe geometry: above a
critical mass the false-vacuum region inflates, the exterior observer sees a Schwarzschild black
hole, the interior a closed universe that causally disconnects (unequivocally so once black-hole
evaporation completes). Proves the initial-singularity obstacle (Penrose theorem + WEC) that
entry 48 sharpens; credits entry 47 for "child universes"; labels its Minkowski-instability idea
"a matter of speculation"; and candidly reports the exact solutions show no evidence for the
information-repository effect. No observational discriminant. Notes: batch 8.
Record: kimi recall R3; the junction-condition machinery child-universe constructions stand on.

**50. E. Farhi, A. H. Guth & J. Guven (1990). "Is it possible to create a universe in the laboratory by quantum tunneling?" Nucl. Phys. B 339, 417–490.**
DOI 10.1016/0550-3213(90)90357-j — VERIFIED (Crossref: NPB, v339, p417-490, 1990). Added 2026-08-23, hunt round 2
(`bhu-biblio-gate-20260822/K2GATE_VERDICT.md` + `MORNING_HUNT_REPORT.md`). Tier: **W1**.
Testability: **UNREAD** — text unexamined here.
Record: kimi recall R2 — remembered under the wrong title ("An obstacle to building…"); venue, volume and pages were exact, and the VERIFIED title is used here.

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

**58. The axis-prediction measurement** (added 2026-08-23): M. J. Longo, "Detection of a dipole in
the handedness of spiral galaxies with redshifts z ~ 0.04," Phys. Lett. B **699**, 224–229 (2011),
DOI 10.1016/j.physletb.2011.04.008 — VERIFIED (Crossref: PLB, v699, p224-229, 2011). kimi recall
R10. The original published spin-handedness dipole claim — the adjudication instrument for the
family's preferred-axis prediction, and the amplitude the DESI spin-parity campaign tests. Entry
29's role, for the axis observable. Not a BHU paper; support tier by the same rule.

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
One of the family's four calibrated number-plus-threshold entries, and the CNS branch's. *(Read "The family's one calibrated number-plus-threshold" until 2026-08-29; there are now four — 7, 31, 44, 51.)* A strict night would recompute the Brown–Bethe
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
uncalibrated? If a number exists, this becomes a **fifth** calibrated falsifier *(the ordinal read "second" until 2026-08-29; entries 7, 31, 44 and 51 are calibrated)*; if not,
it reclassifies to PROSPECT-without-a-number and says so in print.

**5. Easson 2026 — entry 22.**
The newest constraint result: obstructions to minimal regular-BH cosmologies. High leverage as a
cross-programme check — a strict night would verify the no-go theorems and map which of the other
published interiors (Dymnikova 18/19, Bronnikov 20, Roupas 21, Gaztañaga 25/26, Popławski 11) they
kill, restrict, or spare. One publication-metadata caveat stands (see entry 22) pending Miru's
spot-check.

---

## Appendix A — context, not base (excluded from the base layer, with reasons)

**A0 (VERIFIED 2026-08-23).** T. Rothman & G.F.R. Ellis, "Smolin's Natural Selection Hypothesis,"
Q. J. R. astr. Soc. (1993) 34, 201–212. Verified against the ADS-hosted journal scan
(bibcode 1993QJRAS..34..201R, free full text), title page sighted: authors, title, volume and
pages exact; received 1992 November 19. Pinned:
`bhu-reading-20260823/sources/rothman_ellis_1993_qjras34.pdf` (sha256 ad76b7ac…, 12 pp,
image-only scan — no text layer). The gate's 2026-08-22 recall was digit-exact after all;
Crossref/INSPIRE both genuinely lack the record (QJRAS predates DOI coverage), which is why
verification had to wait for the ADS route. Cross-check: entry 31's footnote 1 cites this paper
as ref [13], the source of the open-universe correction Smolin accepted. Status: context (Appendix
— a critique of CNS, not a BHU-family paper); summary states CNS "appear[s] to contain a number
of conceptual and technical flaws". READ 2026-08-23 (Tori), all 12 pages from the scan: the
critique's strongest point is the primordial-black-hole objection (Δ(p) should peak over ALL
holes, not stellar remnants; §6 names excluding PBHs "the primary requirement") — which entry
31's text does not answer (it answers the neutron-universe and Λ points and refers the rest to a
book appendix). The critics flag in print that the stars↔black-holes association is their own
reconstruction, concede their neutron-universe reversal is "tentative", grant the programme is
"certainly worth pursuing", and their 1993 "no more nor less amenable to experiment than the
anthropic principle" charge is precisely what entry 31's §4 falsifier was built to answer. Full
notes: `bhu-reading-20260823/READING_NOTES_01.md` batch 7.

**A0b (pending verification / ruled context, 2026-08-23, hunt round 2).** Kimi recalls not seated:
J. Silk, "Holistic cosmology" (Science 277, 1997) — published CNS critique, verify before seating
beside A0; L. Smolin, "The status of cosmological natural selection" (book chapter, Carr ed. 2007;
= hep-th/0612185) — book, context by standing rule; T. X. Zhang black-hole-universe series —
memory-uncertain, recalled venue is fringe (*Progress in Physics*); H. Culetu comment line —
memory-uncertain, no fixable venue. Also deliberately NOT seated from kimi's top-10: the EC
wormhole/inflaton/S-brane/MPLA rows (#22, #43, #44, #40, #21) — mechanism-family, not on-claim;
recorded here so their exclusion is a decision, not an oversight.


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
