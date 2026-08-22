HOLD_K2_MEMORY_OMISSIONS

# K2 gate verdict — second-family recall-and-triage on the BHU bibliography

**Gate:** Moonshot Kimi second-family recall gate (K2), 2026-08-23 KST.
**Engine: Moonshot AI Kimi (kimi-k3).** No network. Training-memory recall only. This verdict does
not defer to the first (Codex-family) gate; all judgments below are made from this engine's own
memory sample against the two inputs.
**Inputs read in full:** `../bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md`
(46 verified-published entries + 6 support + appendix, branches 1–10) and `k2_candidates.json`
(70 rows). Nothing else was touched; no other file edited.
**Standing caveat for everything in §1:** this gate is no-network by brief, so every recall item
is **UNVERIFIED-AT-GATE** — memory-only, not checked against Crossref or any registry. MEMORY-
CONFIDENT means "this engine remembers it as a real published paper," not "verified." Each item
needs the same Crossref protocol BGATE used before it can touch the base layer.

---

## 1. RECALL ATTACK — published BHU-family papers in NEITHER document (the headline)

This engine's memory returned the following items, none of which appear in the bibliography's
46 entries / 6 support / appendix, and none of which appear among the 70 candidates.

**R1. E. Farhi & A. H. Guth, "An obstacle to creating a universe in the laboratory," Phys. Lett. B
183, 149–153 (1987).** MEMORY-CONFIDENT. The no-go analysis for manufacturing a child universe
from collapse — the published starting point of the whole "universe creation" question that
branch 4 (baby universes) answers. Best-remembered venue/year: PLB 183 (1987).

**R2. E. Farhi, A. H. Guth & J. Guven, "An obstacle to building a universe in the laboratory,"
Nucl. Phys. B 339, 417–490 (1990).** MEMORY-CONFIDENT (venue/year; page range approximate).
The full development of R1; the quantum-tunneling route around the classical obstacle.

**R3. S. K. Blau, E. I. Guendelman & A. H. Guth, "Dynamics of false-vacuum bubbles," Phys. Rev. D
35, 1747–1766 (1987).** MEMORY-CONFIDENT. The false-vacuum-bubble junction-condition machinery —
direct precursor physics of the Frolov–Markov–Mukhanov branch (entries 13–14), which the
bibliography holds without its foundations.

**R4. K. Sato, H. Kodama, M. Sasaki & K. Maeda, "Multi-production of universes by first-order
phase transition," Phys. Lett. B 108, 103–107 (1982).** MEMORY-CONFIDENT on title/venue/year;
pages approximate. Child-universe production from false vacuum. Scope is borderline (phase-
transition parentage, not black-hole parentage) — likely appendix/base-boundary call downstream,
but it is published physics the record lacks.

**R5. J. Smoller & B. Temple, "General relativistic shock waves that extend the Oppenheimer–Snyder
model," Arch. Rational Mech. Anal. 138, 239ff (1997).** MEMORY-CONFIDENT on authors/venue/year;
volume approximate. The OS-extension construction that branch 9 (entries 36–38) grows out of —
the bibliography added the branch 2026-08-22 without its precursor. A related monograph (Memoirs
AMS, ~2003–2004, locally-inertial Glimm scheme) is MEMORY-UNCERTAIN in its details.

**R6. N. J. Popławski, "Nonsingular Dirac particles in spacetime with torsion," Phys. Lett. B 690,
73–77 (2010).** MEMORY-CONFIDENT. The singularity-avoidance mechanism paper underpinning the
torsion-bounce chain (entries 8–12, 39–41). SUPPORT-class rather than base, but published in a
flagship venue and absent from both documents.

**R7. J. Silk, "Holistic cosmology," Science 277, 644 (1997).** MEMORY-CONFIDENT on venue/year;
page approximate. A published critique of Smolin's cosmological natural selection — the same
class as appendix A0 (Rothman & Ellis, still pending verification). Locating R7 would part-fill
the "no published CNS critique in the record" hole with a verifiable venue.

**R8. L. Smolin, "The status of cosmological natural selection," in *Universe or Multiverse?*
(B. Carr ed., Cambridge UP, 2007); arXiv hep-th/0612185.** MEMORY-CONFIDENT that it exists.
By this bibliography's own rule (A6: books are context, not base) it lands appendix-class at
best. Recorded so the recall is complete, not as a base candidate.

**R9. T. X. Zhang, "black hole universe" model series (~2009–2011).** MEMORY-UNCERTAIN on exact
titles/venues — recalled as appearing mostly in *Progress in Physics* (a fringe venue), with a
possible ApSS item. Even if located, FRINGE-class on venue. Listed for recall completeness; not
a base candidate.

**R10. M. J. Longo, "Detection of a dipole in the handedness of spiral galaxies with redshifts
z ~ 0.04," Phys. Lett. B 699, 224–229 (2011).** MEMORY-CONFIDENT. The original published
spin-handedness dipole claim — the root of the empirical line appendix A7 already rules out of
the base layer. Recall hit, appendix-class only.

**R11. H. Culetu, universe-as-a-black-hole comment line (~2008–2014).** MEMORY-UNCERTAIN —
remembered as arXiv-heavy with possible IJMPD/IJTP journal items. Recall-quality only; cannot
fix a venue from memory.

**R12 (boundary item).** N. J. Popławski, "Matter-antimatter asymmetry and dark matter from
torsion," Phys. Rev. D 83, 084033 (2011). MEMORY-CONFIDENT — but torsion phenomenology, not
interior cosmology; most likely out of BHU scope. Mentioned so the next gate doesn't spend a
cycle rediscovering it.

**Attribution catch on an existing base entry (second-family value, not a new item):**
bibliography **entry 20** lists "K. A. Bronnikov, J. C. Fabris (2007-class): *Regular black holes
and black universes*, GRG 39, 973–987." This engine remembers that paper's authors as
**K. A. Bronnikov, V. N. Melnikov & H. Dehnen** (arXiv gr-qc/0611022) — MEMORY-CONFIDENT.
Bronnikov & Fabris is a *different* real paper ("Regular phantom black holes," PRL 96, 251101
(2006)). Recommend the next gate re-check entry 20's author line against its preserved Crossref
JSON; if my memory is right, the base layer currently carries a wrong author attribution.

**Could NOT recall (stated for honesty):** the author line of base entry 42 (PLB 261, 357, 1991)
— no memory of it; the three branch-9 Smoller–Temple titles were not spontaneous recalls of this
engine (the programme is known to me, the specific 2000/2003/2004 titles were not) — consistent
with a genuinely different memory sample from the first gate.

---

## 2. TRIAGE of the 70 candidates

Harsh rules applied: seed-link count is not merit; venue quality gates everything; the A7-ruled
empirical spin line stays appendix regardless of how many seeds it cites; preprint servers
(Preprints.org, Research Square, Qeios, SSRN, arXiv) are no-review venues. Title+venue level
only — no abstracts or full texts at this gate (see §5).

**BASE (4):**
1. #1 "The mass of our observable Universe" (MNRAS Lett 2023) — BASE. Recalled as Gaztañaga;
direct BHU mass claim extending entries 23–27; flagship venue.
2. #2 "Big Bounce and Closed Universe from Spin and Torsion" (ApJ 2019) — BASE. Recalled as
Popławski; the missing mechanism-chain link between entries 11 (ApJ 2016) and 41 (GRG 2021).
3. #7 "Analysis of big bounce in Einstein–Cartan cosmology" (CQG 2019) — BASE. The exact bounce
mechanism of ranked target 1; IOP venue; author MEMORY-UNCERTAIN.
4. #41 "Asymptotically de Sitter universe inside a Schwarzschild black hole" (PRD 102, 066010,
2020) — BASE. Direct on-claim interior construction; flagship venue; author MEMORY-UNCERTAIN.

**SUPPORT (10):** #20 (Found. Phys. 2020, torsion/noncommutative-momentum formalism,
Popławski-line), #21 (MPLA 2018, EC closed-universe primordial fluctuations), #22 (PRD 96,
124017, EC dynamic wormholes — ER-bridge parentage class of entry 8), #27 (PRD 111, 103537,
2025 exclusion-principle bounce), #31 (IJTP 2023, regular-BH review — branch-5 context), #36
(PLB 2022 "What moves the heavens above?" — venue solid; recalled UNCERTAINLY as the
torsion/cosmic-rotation line feeding the axis question; if the recall is wrong this reclassifies
NOT-BHU), #40 (JHEP 2021, zero-shear S-brane non-singular BH — regular-interior family), #43
(PRD 95, 064049, EC wormholes), #44 (PLB 2016, ECSK inflaton reconstruction with particle
production — mechanism family of entry 41), #57 (Phys. Dark Universe 2023, GWs in EC theory —
EC phenomenology).

**APPENDIX-CONTEXT (17):** the A7-ruled empirical spin/magnitude line — #3, #6, #8, #11, #12,
#17, #19, #34, #61, #64, #66, #68 (12 rows; #8 is the JADES paper A7 names explicitly); #46
(Synthese 2025 — philosophy-of-biology take on CNS); #49 (Elsevier eBooks — a book chapter, not
a journal article); #37, #38 (Preprints.org v1/v2 — preprint duplicates of **base entry 27**,
already in the layer as Universe 8, 257); #69 (SSRN — preprint twin of **base entry 26**,
Symmetry Part II "out of an FLRW cloud").

**FRINGE (20) — venue named as the reason:**
- #4 (Physical Science International Journal, 2014) — ScienceDomain pay-to-publish; a "First
  Critical Scientific Review" in a venue without meaningful review. Rank 4 of 70 by seed-links —
  the cleanest proof that citation-graph centrality is not merit.
- #9, #24, #25, #26, #48, #52 (J. Applied Mathematics and Physics, SCIRP) and #47 (J. Modern
  Physics, SCIRP) — predatory publisher; Hubble-tension/CMB-temperature numerology content.
- #14, #15, #16, #23 (Int. J. Advanced Astronomy) — predatory-grade venue; on-claim titles
  ("decelerating black hole universe" etc.) die at the venue; possible Howusu-line, MEMORY-
  UNCERTAIN.
- #45 (J. Astrobiology & Outreach, OMICS, 2014) — predatory publisher.
- #70 (Physics Essays, 2021) — notoriously weak review; content also NOT-BHU.
- #18/#39 (Preprints.org, Apollonian Universe v2/v1), #30 (Preprints.org, "eggshell" BHU —
  on-claim title, no review), #35 (Research Square fluid spheres), #63 (Research Square CMB
  preprint of #9's line), #58 (Qeios redshift bias — no traditional peer review).

**NOT-BHU (19):** #5/#55 (tired-light redshift bias, Particles — venue reviewed, claim off-
scope), #10 (shell cosmology), #13 (cosmological-horizon philosophy; MEMORY-UNCERTAIN, cheap
recheck), #28/#59/#65 (systematic-redshift-bias cluster), #29 (CMB–Hawking–Planck scale-relation
numerology), #32 (AJP pedagogy, no BHU claim inferable; MEMORY-UNCERTAIN), #33 (torsion dark
energy — not interior cosmology), #42 (Born reciprocity), #50 (f(T,𝒯) gravitational decoupling),
#51 (torsion wave–particle duality formalism), #53 (micro-BH battery engineering), #54 (Planck-
computer speculation — MDPI venue reviewed, claim off-scope), #56 (f(R,T) bounce without a BH),
#60 (cosmological-principle tests, CQG — solid venue, not interior cosmology), #62 (fluid-sphere
stability), #67 (composite-G numerology).

**Tally: BASE 4 / SUPPORT 10 / APPENDIX-CONTEXT 17 / FRINGE 20 / NOT-BHU 19 = 70.**
Harvest-quality findings: ≥11 rows are duplicate journal/preprint/version rows of other rows
(#55→#5; #64→#6; #39→#18; #38→#37; #58,#59,#65→#28; #63→#9; #62→#35), leaving ≈59 unique works;
two rows (#37, #69) are preprint twins of base entries 27 and 26 the layer already holds. Roughly
one-sixth of the harvest (12 rows) is the already-ruled A7 empirical line. The "W1" tier label in
the JSON was applied to IJAA, SCIRP, OMICS, ScienceDomain, Preprints.org, Research Square, Qeios,
SSRN and Physics Essays rows alike — the tier is a citation-graph label, not a venue-quality
label; downstream lanes must not read it as one.

---

## 3. Top-10 BASE candidates (ranked, one-line reasons)

1. **#41 — PRD 102, 066010 (2020), dS universe inside a Schwarzschild BH** — the most direct
   on-claim published construction in the harvest; flagship venue; branch-5/Roupas-adjacent.
2. **#1 — MNRAS Lett 2023, "The mass of our observable Universe"** — completes the published
   Gaztañaga series (entries 23–27) with its newest member; flagship venue.
3. **#2 — ApJ 2019, Big Bounce and Closed Universe from Spin and Torsion** — the missing
   Popławski-chain link between the 2016 ApJ entry 11 and the 2021 GRG entry 41.
4. **#7 — CQG 2019, Analysis of big bounce in Einstein–Cartan cosmology** — an independent
   analysis of the exact mechanism ranked target 1 audits; a strict night gets two derivations
   to cross-check instead of one.
5. **#22 — PRD 96, 124017 (2017), EC dynamic wormholes** — parentage kinematics of entry 8's
   class; SUPPORT-tier unless the body constructs an interior universe.
6. **#43 — PRD 95, 064049 (2017), Einstein-Cartan wormhole solutions** — same mechanism family,
   flagship venue.
7. **#44 — PLB 2016, ECSK inflaton reconstruction with particle production** — the mechanism
   family of entry 41 (particle production in EC cosmology).
8. **#27 — PRD 111, 103537 (2025), bounce from quantum exclusion** — the newest published bounce
   route; candidate second mechanism; content unread.
9. **#40 — JHEP 2021, zero-shear S-brane non-singular BH** — regular-interior family feeding
   branch 5 and the Easson-2026 obstruction map.
10. **#21 — MPLA 2018, EC closed-universe primordial fluctuations** — the perturbation-level
    extension of the bounce line; closest in the harvest to an observable transfer function.

**Venue-itself-is-the-concern flags (candidate rows where venue, not content, is disqualifying):**
#4 (Physical Science International Journal), #45 (OMICS J. Astrobiology & Outreach), the SCIRP
cluster #9/#24/#25/#26/#47/#48/#52, the IJAA cluster #14/#15/#16/#23, #70 (Physics Essays), and
the no-review preprint rows #18/#30/#35/#37/#38/#39/#58/#59/#63. MDPI rows (Symmetry, Universe,
Particles, Astronomy, Quantum Reports) are reviewed venues — their exclusions above are on
scope/content (A7 line, tired light, numerology), not on venue.

---

## 4. Coverage boundary — what this memory does and does not cover

- **Cutoff honesty:** this engine's literature memory is strongest through ~2024 and thins fast
  after early 2025. 2025–2026 publications (Easson 2026, Pourhassan 2025, Popławski 2025 IJMPA,
  Sahu 2025, the JADES 2025 MNRAS paper, the Synthese 2025 CNS paper) are effectively invisible
  to spontaneous recall — I know them from these documents, not from training. **No completeness
  claim is made, for any year, and emphatically not for 2025+.**
- **Families this engine could not recall:** Russian-venue BHU items beyond what the documents
  show (entry 40's JETP publication was new to me); conference-proceedings items; regional-journal
  BHU lines (Indian/Chinese/Nigerian venues) beyond the Zhang/Howusu/Culetu-class recalled above;
  the specific branch-9 Smoller–Temple titles as spontaneous recall; the author line of entry 42.
- **What a memory sample proves:** §1's MEMORY-CONFIDENT items are claims about *my training
  sample of the literature*, which differs from the first gate's sample — that difference is the
  entire value of this gate. A recall that verifies (R1–R3, R5–R7 class) is a genuine omission in
  the record; a recall that fails verification is a false positive of this engine and should be
  recorded as such, not silently dropped.
- **Adjacent lines knowingly NOT raised as recalls** (remembered but judged out of scope, to save
  the next gate a cycle): loop-quantum-cosmology bounces (no BH parentage), Planck-star /
  black-to-white-hole transition (Rovelli–Vidotto line — BH bounce, not a universe inside),
  gravastars, mass-inflation interior physics (Poisson–Israel), Coleman/Giddings–Strominger
  baby-universe quantum cosmology, R_h=ct (Melia) cosmology, Dvali–Gomez quantum N-portrait.

## 5. UNVERIFIED-AT-GATE register (time-box statement)

- **All of §1:** memory-only recalls; gate is no-network by brief; nothing was checked against
  Crossref/arXiv. Every item requires the BGATE Crossref protocol before entering any layer.
  Reason unfinished: *no network permitted at this gate.*
- **All of §2–§3:** triage is title+venue+journal-reference level. No abstracts or full texts
  were read; author inferences on #1, #2, #7, #20, #36, #41 are recall-based, not read.
  Reason unfinished: *time-boxed triage brief; 70 rows, no full-text budget.*
- **Entry-20 attribution catch:** memory-only; verify against the session's preserved
  `crossref_*.json` for GRG 39, 973 before correcting the base layer.

**Verdict: HOLD_K2_MEMORY_OMISSIONS** — §1 carries at least six MEMORY-CONFIDENT published items
absent from both documents (R1–R3, R5–R7 scope-relevant; R4 scope-borderline; R8/R10
appendix-class), plus one MEMORY-CONFIDENT attribution catch on existing base entry 20. The base
layer must not be treated as recall-complete until R1–R7 clear (or fail) Crossref verification.

— **Kimi (Moonshot AI, engine: kimi-k3), second-family recall-and-triage gate, 2026-08-23 KST.**
Findings only. No files edited except this one. No network used. No prior verdict deferred to.
