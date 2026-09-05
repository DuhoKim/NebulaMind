# What the black-hole-universe programme now says — an argued position (Tori, 2026-09-06, overnight, at Blanc's 00:53 KST note)

**Read this first.** This is not a review of the corpus and not a summary of the audit. It is one lane owner's argued answer to
five questions, written so that Duho can decide from this page alone whether the BHU lane holds a research programme or a pile
of annotations. Every finding carries the entry number or file it rests on; where I judge rather than find, the sentence says
"my judgement". Anything I could not source is marked UNSOURCED. No tier, warrant, standing or stamp moves; nothing runs;
nothing outward; paper HOLD.

**The verdict, in one paragraph (my judgement).** The programme is real but small. After the full tiering of 51 published
entries (`WARRANT_TABLE_20260903.md`: 3 CALIBRATED/FIRED, 2 CALIBRATED/LIVE, 8 QUALITATIVE-DIRECTIONAL, 4 THEORETICAL-OBSTRUCTION,
4 PROSPECT, 30 CONSISTENCY-ONLY), exactly **one** claim in the literature is falsifiable as stated and still alive against a
measurement (entry 31's neutron-star bar), **one** sign is watched (entry 54's closed curvature), and everything else that
looks falsifiable fixes a shape and leaves the magnitude free — six recorded instances with a stated breaker
(`SHAPE_MAGNITUDE_PATTERN_RECORD_20260904.md` V2). R3D added a seventh shape-without-magnitude result on the one construction
that seemed to fix a number by geometry alone. The live frontier is therefore not "which BHU model is right" but "does any
construction in this family compute a magnitude from its own equations" — and the census R3C2 is the instrument built to
answer that across the whole corpus at once. If the census returns no such construction, the honest description of the
literature is a set of consistent geometries with one surviving falsifier that belongs to a selection argument, not to a
geometry. If it returns even one, the programme has a target.

---

## 1. Which claims are actually falsifiable as stated, and which only look it

**Falsifiable as stated, and already fired (three).** Entry 1, Pathria 1972: "K = +1 and Λ ≤ Λ_c" — a closed, decelerating
dust universe; Planck 2018's q₀ = −0.527 ± 0.011 sits inside the forbidden gap by 43σ; FIRED, Duho's stamp 2026-09-02
(`PATHRIA_STANDING_RECONCILIATION_20260902.md`). Entry 7, Brown–Lee–Rho 2008: the kaon-condensate cap near 1.5 M☉; PSR
J0740+6620 at 2.08 ± 0.07 fired the instrument chain, not cosmological natural selection itself (synthesis §3). Entry 44,
Pourhasan–Afshordi–Mann 2014 §4: exact scale invariance n_s = 1; Planck's 0.9649 ± 0.0042 is 8σ away; FIRED for that model,
not for the holographic framework (synthesis §3). These three are the proof that the tiering means something: falsifiable
claims in this family do die.

**Falsifiable as stated and alive (one, plus one conditional).** Entry 31, Smolin 2004: no securely measured neutron star
above 2.5 M☉. Best measurement PSR J0952−0607, 2.35 ± 0.11 (1.36σ short, posterior above the bar 8.6%), GW190814's secondary
excluded as unresolved (synthesis §4; `b68_entry31_massbar_tripwire.py`, positive-controlled 2026-09-06). Its warrant is
DISPUTED and pinned (Rothman & Ellis 1993; Harrison 1995). This is the only route by which an observation kills a BHU
cosmology outright, and it is drifting away from firing. Entry 51, Popławski 2010: the ECKS minimum black-hole mass ~10¹⁶ kg
is a falsifier only for models that inherit the ECKS premise, and its floor is UNREPRODUCED from the stated inputs
(`K6_RESULT_20260904.md`, `K6_FLOOR_UNDERDETERMINED`) — alive in form, not usable as a number.

**Falsifiable-looking, but not as stated (the bulk of what sounds testable).**
- The 60° causal-horizon cutoff, entries 23–27 (Gaztañaga 2020–2022) and 56: the *scale* is the papers' own and
  non-circular (`PROGRAM_A_FREEDOM_MAP_20260902.md`); the *amplitude* is not — no perturbation prescription exists, the
  author says so (2003.11544 L466), two formalisations are provably incompatible, and the amplitude was proven irreducibly free
  by the lane's committee (memory of the 09-03 adjudication; receipts in the freedom-map gates). It cannot be scored.
- The de Sitter-core ringdown, entry 21 (Roupas 2022): frequencies derived and in LISA's band, amplitude free
  (`K5_RESULT_20260904.md`, `K5_AMPLITUDE_FREE`).
- The torsion bounce, entries 9–11 (Popławski 2010, 2012, 2014): the n² closure is a convention with two printed coefficients
  six times apart in one paper (`K3S1_RESULT_20260903.md`); the derivation that would fix it is uncontrolled where it matters
  (`K3S3_RESULT_20260904.md`); the inflationary numbers of entry 59 rest on a chosen β (`R3A_RESULT_20260904.md`, `BETA_FREE`).
- Λ from a boundary, entry 56: w = −1 follows only from an assumed constant mass; the paper's own text permits M(τ)
  (`R3B_RESULT_20260904.md`, `RIGIDITY_ABSENT`). Its "prediction" is shared with ΛCDM unless the mass is held fixed by fiat.
- The Dymnikova regular-core floor, entries 18–20, 55: see §2.

**Directional only (eight entries).** Entry 54's closed curvature is the one directional claim with a watched instrument
(`project_desi_curvature_watch`: a CONFIRMED Ω_k > 0 refutes; flatness does not); entries 6, 23–27 and 56 assert or derive a
direction without a magnitude (`WARRANT_TABLE_20260903.md` tokens `W_DIRECTION_*`). A direction is a sign test, and only 54's
sign has a survey pointed at it.

**Not falsifiable at all, as published, and honestly labelled so:** the 30 CONSISTENCY-ONLY entries. They are geometries and
matchings that show a universe *can* sit inside a black hole in some model; none states a number a measurement could miss.
That is not a criticism of the papers, which mostly do not claim more; it is a fact about what the programme has to work with.

## 2. What R3D retires, and what it leaves standing

**The finding** (`R3D_RUN_FILING_20260905.md`, class `DYM_POSITIVE_FLOOR_UNREPRODUCED`, V31 name; three routes agree to every
digit): the Dymnikova regular-core metrics, read exhaustively from the four pinned texts, give a double-horizon mass family
`M_crit(r0) = 0.878794537877033… c² r0 / G` over a **free core scale** r0 (ε0 via r0² = 3c⁴/8πGε0). The infimum over the free
scale is 0. No positive minimum black-hole mass follows from the construction as printed.

**What it retires.** The hope that the regular-core branch supplies, by geometry alone, the floor that ECKS (entry 51) could
not supply from density: `K6_RESULT` had found the ECKS floor underdetermined for want of a size–mass relation; R3D shows the
Dymnikova branch has no floor either, because the one scale that would set it is an input, not an output. Taken together,
**no minimum black-hole mass is derived anywhere in this corpus** (my judgement: this is the strongest single negative result
the lane holds, because both families that were supposed to give one were tested to their printed inputs). It also retires,
for this corpus, the "quantum-gravity core sets a mass scale" motif as a *derived* claim; it survives only as an assumption.

**What it leaves standing.** Everything Dymnikova actually proves: the metric is an exact regular solution with Schwarzschild
and de Sitter limits, finite curvature invariants, and an anisotropic vacuum source (entry 18, `W_CONSTRUCTION_ASSERTED` on the
profile, which is an ansatz by the paper's own words). The R3E kit's unplanted run (disclosed in `R3E_…_DRAFT`, §0) indicates
the printed components are internally exact — so the branch is *consistent*, just not *predictive* of a mass. Entries that
lean on the same construction and are therefore touched: 19 and 20 (Dymnikova's later restatements; `W_MIXED`), 55 (the
asymptotically de Sitter interior inside Schwarzschild, PRD 2020; the R3D prereg §1 names it as sharing the de Sitter-core
premise), and, at one remove, entry 21 (Roupas's fluid-shell spectrum, which matches a de Sitter core to Schwarzschild: its
ringdown frequencies do not depend on a floor, so K5's result is untouched, but any "minimum object" reading of entry 21 is
UNSOURCED in the paper and should not be assumed). Entry 22 (Easson's obstructions) is not touched: R3D is a local mass
statement, not a junction theorem, and the obstruction's domain stays as adjudicated 2026-08-31.

**A boundary I keep:** R3D says "unreproduced from the stated inputs", not "false". A later paper that fixes r0 from a
quantum argument would reopen the floor; none in this corpus does (R3D §1, four texts read exhaustively).

## 3. Where the live frontier is now — ranked by contested × tractable

Duho's criterion is contested × tractable, not interest. Five questions; I judge each's scores from the record.

| rank | question | contested | tractable | why it moves the programme | instrument |
|---|---|---|---|---|---|
| 1 | **Does ANY construction in the corpus compute an observable magnitude from its own equations?** | 5 — the six-instance pattern says no; the pattern's own breaker says how to prove otherwise | 4 — the census is designed, V23 SIGNABLE | A single `CENSUS_COMPLETE` with one derived-only, within-precision claim on a magnitude breaks the pattern; none confirms it corpus-wide | R3C2 (`R3C2_REPRODUCTION_CENSUS_PREREG_20260904.md` V23) |
| 2 | **Will a secure neutron star cross 2.5 M☉?** | 4 — the bar is the author's own "certain refutation"; the warrant is disputed | 5 — it is a watch, tested and armed | The only outright observational kill in the family | b68 + Tuesday watch (`WATCH_POSITIVE_CONTROLS_20260906.md`) |
| 3 | **Does the entropy chain of entry 21 derive its temperature, or import it?** | 4 — "this object is really a black hole" rests on it | 4 — eight printed equations, kit executed | If T0 is derived, the corpus has its first construction-fixed thermodynamic magnitude; if imported, instance seven of the pattern | R3F (DRAFT 3) |
| 4 | **Is Smoller–Temple's present shock position bounded once the start epoch's printed floor is used?** | 3 | 5 — the PDF settled the formula tonight; C2 reproduces 0.019 | A bounded magnitude on the exact-GR branch would be the pattern's first partial breaker (condition 1 met; 2–5 to test) | R3G (DRAFT 3a) |
| 5 | **Does DESI's curvature confirm Ω_k > 0?** | 3 — entry 54 predicts closed; flatness does not refute | 3 — external cadence | Refutes the only watched directional claim | curvature watch (Hwao's cron, BHU's tripwire b63) |

Below the line (my judgement): R3E (entry 18's internal consistency — likely `PROFILE_CONSISTENT`, an annotation), R3H (which
downstream numbers are six-fold soft — a record, not a frontier), R3I (what "black hole" names — a referent map, useful for the
paper, not a falsifier), clusters #9 and #11 of the ranked packet (transfer function across the bounce; K2's shelled complement).

**The single sentence for Duho:** the frontier is question 1; everything else either feeds it (3, 4) or is a watch (2, 5).

## 4. The five drafted studies — what each settles and does not

- **R3E** (entry 18 source components vs its own metric): settles whether Dymnikova's printed tensor is the one its metric
  demands; does NOT settle whether the profile is physical — it is an ansatz either way. Honest verdict: the lane's own kit
  already shows zero residual (disclosed); this is an annotation-grade study unless a seat finds an OCR-dependent reading.
- **R3F** (entry 21 entropy): settles whether the Bekenstein–Hawking recovery is derived or conditional on an imported
  temperature; does NOT settle whether the object exists or is stable. Likely `ENTROPY_ASSUMED` by the paper's own "if"; still
  worth a seat-day because eq. 24's identity is the corpus's cleanest α-independent relation and nobody has checked it.
- **R3G** (Smoller–Temple shock position): settles whether the present shock distance is bounded by the printed floor on the
  start epoch (tonight's PDF reading says the logarithm is unsquared and a floor exists, so bounded is now the live option);
  does NOT settle whether the shock exists or is observable — the paper names no signature beyond "comparable to the Hubble
  length". If `INVARIANT_FIXED` files, it is the first construction-fixed magnitude in the family; my expectation is
  `MAGNITUDE_BOUNDED`, an order-of-magnitude claim that restates its inputs.
- **R3H** (entry 10's ⅛ vs ¾ propagation): settles which downstream printed numbers move under the other coefficient and by how
  much (linear quantities six-fold, square-root quantities 2.45-fold, under the declared threshold); does NOT settle the physics,
  which K3 already did. Honest verdict: a record for the paper's table, not a frontier; provenance limb blocked at source.
- **R3I** (referent census): settles which of three objects each entry's "black hole" denotes and where cross-referent citations
  are used as support; does NOT settle any physical claim. It would settle little on its own; its value is that the paper cannot
  be written without it. It should wait for R3C2's class ruling machinery to be reused.

## 5. What would make the programme unfalsifiable in practice — and whether the corpus shows it

Each claim can be falsifiable in principle and the programme still unfalsifiable in practice if **the number a measurement
would test is always the one left free**. That failure mode has a name in this lane now: the shape/magnitude pattern, six
instances, one stated breaker (`SHAPE_MAGNITUDE_PATTERN_RECORD_20260904.md` V2). R3D is the seventh case in kind (a scale left
free where a floor was expected), though it is filed under its own class rather than added to the record, which is Duho's to
amend. **I see the failure mode in the corpus, and I name it plainly: it is present.** Its mechanism is specific and
repeatable: the construction is exact where it is geometry (junctions, metrics, horizons — the 30 CONSISTENCY-ONLY entries,
the four obstructions, K2's theorem) and becomes a choice exactly where it must meet data (a normalisation, a coefficient, a
core scale, a fixity, a start epoch). A programme built this way can absorb any observation by moving the free number, and
the only claims that have died (1, 7, 44) are the ones whose authors, unusually, fixed the number.

Two further practical failure modes the corpus shows, with sources:
- **Borrowed falsifiers.** Entries 7 and 31 are CALIBRATED because they borrow a bar from nuclear physics (`W_BORROWED`); when the
  bar moves (kaon condensation fired), the cosmology re-parameterises to the next bar. The family's own geometries supply no bar.
- **Warrant by assertion.** Six of eight directional claims are `W_DIRECTION_ASSUMED` (entries 6, 23, 25, 27, 56 and, before
  reconciliation, 24 and 26), and the founding identification's successors (entries 23–27) rest on a scale that is
  non-circular but an amplitude that is not the papers' — the sharpest observational claim in the family cannot be scored at all.

**What would rescue the programme from this mode:** one construction that passes all five breaker conditions — a magnitude,
every constant traced, no surviving normalisation, no assumed fixity, a number ΛCDM does not share. R3C2 is the search for it,
corpus-wide, blind, receipted. My judgement: if the census files `CENSUS_COMPLETE` with zero derived-only within-precision
magnitudes, the record should say the family is a class of consistent geometries whose one live falsifier belongs to a
selection argument (entry 31) rather than to any black-hole interior, and the paper should be written that way. That is a
publishable, defensible conclusion; it is not the one the field would like, and it is the one the audit currently supports.

## What this document does not do
It moves no tier, warrant, standing or stamp; it runs nothing; it is not outward. Sources: the warrant table, the corpus synthesis
(`BHU_CORPUS_SYNTHESIS_20260902.md`, §§3–8, 12–14, K4), the pattern record V2, the K and R3 result files named inline, and
tonight's drafts. UNSOURCED items are marked as such above (one: any "minimum object" reading of entry 21).

BHU_PROGRAMME_SYNTHESIS_COMPLETE
