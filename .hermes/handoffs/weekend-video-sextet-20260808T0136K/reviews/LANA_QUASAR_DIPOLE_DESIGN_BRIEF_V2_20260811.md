# DESIGN BRIEF v2 — Quaia-core number-count dipole vs the CMB-kinematic expectation

Per Duho's order *"redraft it quaia-centred with exact records pinned,"* and Kun's hold on v1
(`KUN_QUASAR_DIPOLE_DESIGN_BRIEF_GATE_20260811T0845K.md`, HOLD_DESIGN_BRIEF_FREEZE_NOT_GATEABLE).
Redrafted by Lana; I own the claim boundary. Filed **2026-08-11 10:16 KST**. **Brief only — no run, no
statistic computed, public data only, no new labelling.** Duho chose Kun's Quaia-core route; this supersedes
v1 (`…_20260811.md`, CatWISE-core), which is preserved but is **not** authority. Every item below is a
**value**, a **named Tori-custody artifact bound at freeze**, or an explicit **"cannot be frozen from hand"
finding** — never a promise to freeze later. **NOT_WORTH_DOING_YET is a successful outcome.**

---

## VERDICT UP FRONT — NOT_WORTH_DOING_YET, as drafted (a result, with a named flip condition)
On the Quaia-core route as constrained, the brief **cannot be frozen into values on its two pivotal items**,
and until it can it adds only one more contestable selection-treatment to a contested field — so the honest
outcome is **NOT_WORTH_DOING_YET**. This is not "the study is worthless"; it is Kun's gate applied honestly:
*if it cannot be frozen, it does not proceed.* The exact conditions that flip it to worth-doing are in §10 —
they are concrete and belong to Tori and Goru, not to my imagination.

---

## §0. Kun's standing question, answered head-on: what frozen control does this add beyond published work?
**The published record, verbatim.** The Quaia dipole is **already measured — twice, on the same catalogue,
with opposite conclusions:**
- **Mittal, Blanton et al. 2024** (MNRAS 527, 8497; arXiv:2311.14938), Bayesian: *"we find significant
  evidence that the Quaia quasar dipole is consistent with the CMB dipole, both in terms of the expected
  amplitude and direction,"* after excising galactic-plane selection-contaminated regions.
- **Singal 2024** (MNRAS 532, L1; arXiv:2403.16581), same Quaia 1.3M sample: *"We instead find a dipole 3–4
  times as large as the CMB dipole though in the same direction."*

**So the answer is sharp.** A bare re-measurement of the Quaia dipole adds **nothing** — it exists. What the
field does **not** have, and the reason Mittal and Singal disagree on the *same data*, is a **selection-
function treatment fixed as values before the amplitude is seen.** Mittal's consistency and Singal's 3–4×
excess are the *same catalogue* under *different selection treatments*; neither analysis pre-registered its
treatment, so each is open to the "you chose the treatment that gives your answer" objection — which is
exactly why the dispute is live. **The one genuinely new control a Quaia-core brief could add is a single,
pre-registered selection-function treatment that removes that freedom.** That is real, and it is specific.

**But it cannot be frozen as values now, for two independent reasons (each fatal on its own):**
1. **Tori's mandatory upstream artifact/quality-flag sensitivity gate cannot be met on Quaia.** Quaia carries
   **no row-level warning bits**, so the sensitivity of the dipole to upstream artifacts cannot be tested
   from the catalogue itself. This is a real limitation of the recommended catalogue; it must be *handled*
   (via an external artifact / scanning-law map bound as a value), **not skipped** — and I cannot bind such
   a map from hand.
2. **The selection-treatment cannot be pre-declared from hand, and it is the whole dispute.** Freezing it
   requires binding the exact Quaia selection-function + random package (§2) *and* pre-declaring every
   defect-(4) attribute — model family, link function, pixelization, smoothing scale, coefficient-freezing
   policy, train/test split, mask-interaction terms — as values, **before** any amplitude is seen. I do not
   hold these as values, and if any one is left selectable it is precisely the manufacture route Kun blocked.

**Therefore the honest answer to Kun is: the value-add is real and named (a pre-registered selection
treatment adjudicating the live Mittal-vs-Singal split), but it is not freezable into values at this
drafting — so NOT_WORTH_DOING_YET, with the §10 flip condition.** Answered in the brief, not in conversation.

---

## §1. Catalogue identity — [FROZEN to a single record type; hash Tori-bound — NO "OR"]
**Quaia (the Gaia–unWISE quasar catalogue; Storey-Fisher, Hogg et al. 2024, ApJ 964, 69; arXiv:2306.17749)
is the sole primary catalogue** (Tori's correction v2: Quaia is the provenance-side single recommendation).
- **ONE record, not a disjunction.** The catalogue is the **Quaia data release deposited on Zenodo**, a
  **single deposited record**, taken as distributed. **No "DOI *or* repository," no alternative mirror, no
  reconstruction** — the v1 defect. The specific version string, the record's **sha256 and byte-count**, and
  the exact file list are **bound by Tori's custody receipt at freeze**; I name the record type here and mark
  the hash **Tori-bound, not guessed**. ⚠️ [FINDING] I do not hold the checksum/byte-count from hand; a
  record that cannot be bound to a single versioned checksum is a §10 not-worth-doing trigger.
- **Which Quaia cut is a §4 decision**, not a catalogue choice — see §4.
- **CatWISE is NOT core.** Per Tori it is at most **DOCUMENTED_CONDITIONAL_RECONSTRUCTION**; it may appear, if
  at all, only as a clearly-labelled conditional cross-reference, never as a primary or co-equal catalogue.
  v1's silent promotion of CatWISE to core is retracted.

## §2. Selection-function + random package — [THE PIVOT — cannot be frozen from hand → FINDING]
The Quaia selection function and its associated random/expected-density product are the object the entire
Mittal-vs-Singal dispute turns on. To freeze, **all** of the following must be pinned as values, none
selectable:
- the **exact selection-function map file(s) + randoms**, path + sha256 + byte-count (Tori custody, single
  record, no "or");
- **HEALPix `NSIDE` and ordering** (RING/NESTED), **coordinate frame** (Galactic/Equatorial/Ecliptic), and
  **map-value convention** (completeness vs expected-count; normalisation), all stated as values;
- the **correction model**: family, **link function**, pixelization, **smoothing scale**, **coefficient-
  freezing policy** (coefficients fixed by the published method or frozen before the dipole is computed —
  never fit to reduce the dipole), **train/test split**, and **mask-interaction terms**.
- ⚠️ **[FINDING — pivotal]** I hold **none** of these as values, and they cannot be reconstructed from hand
  without seeing the Quaia selection product. Per defect (4) and Kun's gate, **if any attribute is chosen
  after seeing data, or cannot be pinned to the published Quaia method, the freeze fails and the outcome is
  NOT_WORTH_DOING_YET.** This is the item that most directly forces the verdict.

## §3. Upstream artifact / quality-flag sensitivity gate — [TORI-MANDATORY; currently UNMET → FINDING]
Tori requires a sensitivity test to upstream artifact/quality flags. **Quaia has no row-level warning bits**,
so this **cannot be satisfied from the catalogue** and must not be skipped. The only admissible route is an
**external artifact / scanning-law map** — e.g. a Gaia-scanning-law or unWISE depth/coverage product — bound
as a single custody value (path + sha256), against which the dipole's stability is a **pre-declared** check.
- ⚠️ **[FINDING]** No such external map is bound from hand, and whether one exists at adequate resolution to
  stand in for row-level flags is unverified. Until an external artifact map is bound as a value **and** the
  dipole shown pre-registered-stable against it, **Tori's gate is unmet and the brief cannot proceed.**

## §4. Primary sample cut — [ONE primary value; NO ladder; global test pre-declared if multi-threshold]
- **[FROZEN PROTOCOL VALUE]** Exactly **one primary magnitude / redshift / sample cut**, fixed before any
  amplitude is seen — the published Quaia clean-sample definition (e.g. the `G`-magnitude / redshift
  selection of the release), **quoted verbatim from Storey-Fisher et al. 2024 at freeze**, not chosen by us.
  v1's un-ranked `16.5 / 16.0 / 15.5` trio — three chances at an amplitude with no primary and a substituted
  value — is **withdrawn**; that was the manufacture route.
- **[FROZEN PROTOCOL VALUE]** If more than one threshold is examined at all, it is **only** as a **single
  pre-declared multiplicity-corrected global test** across a **fixed** threshold set named before any
  amplitude is seen — **not a ladder**, and the correction (e.g. the family-wise / global test statistic) is
  itself pinned as a value. No threshold is added, dropped, or shifted after a statistic is seen.
- ⚠️ [FINDING] I do not hold the exact primary cut string verbatim; it must be quoted from the Quaia paper
  before freeze, not reconstructed.

## §5. Sky mask — [TORI-CUSTODY VALUE; full identity pinned]
One mask, adopted (the Quaia-recommended Galactic-plane + selection mask), never reconstructed or varied
after an amplitude is seen. Pinned as values at freeze: **path + sha256 + byte-count; HEALPix `NSIDE` and
ordering; coordinate frame; mask-value convention (which value = masked); and composition order** if built
from more than one cut. ⚠️ [FINDING] I do not hold these from hand; Tori binds the file and its attributes.

## §6. Kinematic-dipole convention — [FROZEN CONVENTION + frozen parameters]
- **[FROZEN VALUE]** Ellis & Baldwin (1984): `D_kin = [2 + x(1+α)]·β`, with `β = v/c` from the CMB dipole
  velocity **v = 369.82 km s⁻¹** (Planck 2018; `β ≈ 1.2336×10⁻³`).
- **[FROZEN PROTOCOL VALUE]** `x` (source-count slope) and `α` (spectral/SED index) are taken **verbatim from
  the published Quaia sample values at the frozen §4 cut** — measured by the catalogue authors, **not fit by
  us to the dipole**. ⚠️ [FINDING] I do not hold the sample `x, α` from hand; carry verbatim before freeze.

## §7. Decision rule — [FROZEN VALUES, pre-registered]
Computed once, on the frozen inputs, **only if §§1–6 fully freeze and §3's gate is met**:
- **DETECTION** (kinematic null rejected): the corrected amplitude exceeds `D_kin`, significant at **≥ 3σ**
  under a **pre-declared** null, **and** stable across the §4 global test, **and** stable against the §3
  external-artifact map within its pre-declared tolerance.
- **NULL**: the corrected amplitude is consistent with `D_kin` within the pre-declared null.
- **INCONCLUSIVE** (exact conditions, pre-registered as values): the result **changes across the §3
  artifact-sensitivity check beyond the pre-declared tolerance**; **or** the §4 global test is internally
  inconsistent; **or** the §2 selection treatment carries any parameter that could not be frozen before the
  amplitude. Any of these ⇒ INCONCLUSIVE, reported plainly.
(The 3σ and all tolerances are pre-registered here as values; none is revised after any statistic.)

## §8. Execution — [FROZEN VALUE, computed once]
Computed **once**, fresh, fully receipted; **no parameter revision after any statistic is seen — any
post-hoc change voids the run** (the A2 discipline Kun enforces). Receipt pins: catalogue record + sha256;
selection package + randoms + sha256 + every §2 attribute; external artifact map + sha256 + §3 result; mask +
sha256 + attributes; §4 cut (+ global-test set if any); `x, α, β` + formula ref; computed `D`, `D_kin`, `σ`,
artifact-sensitivity delta; and the §7 decision.

## §9. Claim boundary — [BINDING, verbatim, unchanged]
- **A DETECTION may say:** *"the number-count dipole amplitude exceeds the CMB-kinematic prediction at
  [significance], and an exclusively-kinematic interpretation is rejected."* It **may not** say "the universe
  is anisotropic," "the cosmological principle is refuted," or attribute the excess to any cause (intrinsic
  anisotropy, local structure, BHU, or any model). **The test is sharp; the origin is degenerate — that
  asymmetry is the whole discipline.**
- **A NULL may say:** *"the dipole is consistent with the CMB-kinematic expectation within [sensitivity]."*
  It may not say "the universe is isotropic" or "the dispute is settled."
- **INCONCLUSIVE** is reported plainly and is a successful outcome. Separate study from spin/BHU; BHU is a
  labelled personal-interest footnote or absent.

## §10. Disposition + the exact conditions that flip NOT_WORTH_DOING_YET → worth-doing
Brief only; no run, no data acquisition, no statistic; nothing unblocks any lane; nothing accepted without
Duho. **Current verdict: NOT_WORTH_DOING_YET**, because the two pivotal items (§2 selection treatment, §3
artifact-sensitivity gate) cannot be reduced to values now, and without them a Quaia measurement only adds
one more contestable treatment to the Mittal-vs-Singal split.

**It flips to worth-doing — and becomes a genuinely new, pre-registered contribution — if and only if ALL
of these freeze as values, in this order:**
1. **§1** the exact Quaia release bound to a single record + sha256 + byte-count (Tori);
2. **§2** the exact selection-function + randoms package bound as a single record, and **every** defect-(4)
   attribute pinned to the published method / pre-declared before any amplitude (Tori + Goru);
3. **§3** an external artifact / scanning-law map bound as a value, standing in for Quaia's absent row-level
   flags, with a pre-declared sensitivity tolerance (Tori) — Tori's mandatory gate met, not skipped;
4. **§4** the one primary cut quoted verbatim, and any multi-threshold examination reduced to a single
   pre-declared multiplicity-corrected global test — no ladder;
5. **§6** the sample `x, α` carried verbatim.
If any of 1–5 cannot be reduced to a value, **the honest outcome stays NOT_WORTH_DOING_YET** — and that,
per the order, is itself the finding. Kun gates the freeze; Tori binds custody and owns the §3 limitation;
Goru builds the data side; my claim boundary (§9) governs any output. Relay submitted.
