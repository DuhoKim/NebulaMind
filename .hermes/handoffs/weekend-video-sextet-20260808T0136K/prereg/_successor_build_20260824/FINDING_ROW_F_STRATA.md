**STATUS: RULED — strata option (A), 2026-08-30 10:46. χ-derived strata ACCEPTED. Row D2 (stratum-
index producer, MAY READ χ) builds the index as a sealed, pinned, independently verified artifact —
slot BS-SI, CLASS E (the V85 class-P label violated §0 and was corrected at V87; generated move "class-P rows 17 → 16; class-E rows 8 → 9" — this header carried the erroneous intermediate for six revisions, GPT56-V91 F9), UNFILLED — Row F's widened surface consumes it and Row F's void clause is amended to its real inputs. Nine strata stay; no v9 unfreeze. The typed/capability barrier applies: the artifact reaches the allocation constructor only, and the positions-only boundary recomputation refuses stratum contamination. Applied in V85.**
# Row F, the nine HC strata, and what the text actually says

## 1. Bin construction is provably χ-free — Row F is NOT contradictory on the part its void clause names

**Established from the frozen reference** (`ref/successor_ref_v9.py`, sha256 `6a9abbbd…`), by reading
the functions §6.3 names:

- **`calibration_bins(c)`** takes **one argument, `c`** — the cos θ values — and returns the two
  interior boundaries at the **count-weighted c-tertiles**. It reads nothing else.
- **`assign_bins(c, boundaries)`** is `np.searchsorted` over those boundaries. Nothing else.

**Row F's void condition is "any χ-bearing input to bin construction", and for bin construction that
condition is satisfied by the code.** The `c`-tertiles are position tertiles, not |χ| tertiles. **On
this point Row F's `(χ-free)` annotation is true.**

## 2. The strata are undefined in this document — this is the silence, and it is deliberate silence

**Established by enumerating every occurrence** of *stratum*, *strata* and *tertile* in the draft.
**There are four**, and none defines the strata:

- §6.3, *"the 3 × 9 joint allocation with **V3-pred's nine HC strata**"* — a reference, not a definition.
- §6.3, the floor *"≥ 30 real labels per **live inherited HC stratum**"* — "inherited" again.
- §6.3's first bullet, *"No strata in the estimator"* — about the estimator, not the allocation.
- §10's closing note: ***"Undecided and untouched: the methods-note question and the strata
  question."*** **The document records that there is a strata question and that it is untouched.**

**In the frozen code**, `N_HC_STRATA = 9` is a bare constant and **no function assigns an object to a
stratum.** `cell_counts` appears only as a *parameter* of `allocate_handcheck`, and **the only value
ever constructed for it inside v9 is a synthetic constant in the fixture harness** (L1988,
`np.zeros((N_CAL_BINS, N_HC_STRATA)) + 200`). **The producer of the stratum assignment does not exist.**

**So I am not resolving the silence by inference, as instructed.** What HC-1H says — that the nine
strata are **machine-committee state (3) × |χ| tertile (3)** — is established from its accepted
artifact, but **HC-1H's rules enter this preregistration "by quotation at freeze" (§6.3) and have not
been quoted.** The draft does not adopt that definition and does not replace it. It defers.

## 3. A defect that does NOT depend on the strata question, and this one IS established

**Row F is stated to read *"the accepted partition's positions and acceptance flags only"* and to write
*"sealed boundaries, bin labels, **and the hand-check allocation**"*.**

**Positions and acceptance flags cannot produce a 3 × 9 stratum-indexed cell-count matrix.** A 9-way
stratum index requires an input Row F is not stated to read — **whatever the strata turn out to mean.**
`allocate_handcheck` consumes `cell_counts` shaped `(N_CAL_BINS, N_HC_STRATA)`; two of those axes' worth
of information is simply not in Row F's stated surface.

**So Row F's emit exceeds its stated read surface, independently of χ.** That is a defect in the row as
written, it is checkable today, and it needs a repair whichever way the strata question goes.

## 4. Why the silence is not stable, and when it stops being silence

**The event that ends the silence is identifiable: the quotation at freeze.** §6.3 says V3-pred's HC-1H
measurement and validity rules *"are carried by quotation at freeze."* If the definition quoted is
HC-1H's own, then on that day Row F is stated to construct, from χ-free inputs, an allocation over
strata defined by **|χ| tertile** — and **its own void clause fires on its own emission.**

**That is the same shape as Row L signing what its own void condition forbade**, and it would arrive
**at the worst possible moment**, because the freeze signature covers the text that contains it.
**Latent now; actual at freeze, unless the strata are redefined or Row F's surface is.**

## How this was established, separated as before

- **From the frozen code:** the signatures and bodies of `calibration_bins`, `assign_bins` and
  `allocate_handcheck`; the absence of any stratum-assignment function; the only in-module
  `cell_counts` value being a fixture constant. **v9 was read, never written — still `6a9abbbd`.**
- **From this draft:** all four stratum/strata/tertile occurrences, Row F's cell, BS-8p's row, and
  §10's "Undecided and untouched" note.
- **From HC-1H's accepted artifact** (`LANA_ONE_HUMAN_ATTENUATION_20260814.md`, via
  `HC1H_ACCEPTANCE_20260815.md`): that the inherited strata are machine-committee state × |χ| tertile.
- **NOT established, and not inferred:** whether this study's strata are χ-derived. **The text does not
  say, and I am not deciding it by reading the inheritance as if it had been quoted.**

## 5. THE INPUT ROW F'S EMISSION REQUIRES — named, as ruled at 23:02, and it is χ-bearing on BOTH axes

**Instruction: name the input the emission actually needs, do not pick one that keeps the row looking
clean, and if it is χ-bearing say so plainly. It is χ-bearing, and worse than expected.**

A 3 × 9 stratum-indexed allocation needs, per object, **a calibration-bin index and a stratum index**.
The bin index is `assign_bins(c, boundaries)` — positions, **χ-free**. The stratum index is HC-1H's
**machine-committee state (3) × |χ| tertile (3)**, and **both of its axes are χ-derived**:

- **|χ| tertile** is the magnitude of the primary instrument's own per-object output. §6.1's scope
  makes *"any per-object instrument output — a χ value, sign, amplitude, confidence value"* χ-bearing.
  **This one is χ-bearing by definition.**
- **Machine-committee state** — HC-1H: *"agree-confident / disagree / low-confidence"* over *"two
  additional architectures"* — **is the agreement state of two classifiers about handedness.** It is a
  per-object machine handedness judgement. Under this document's own rule, **"Doubt resolves toward
  χ-bearing"**, and there is no doubt: **it is χ-bearing too.**

**So the expected finding — "drop the |χ| axis and the stratification becomes χ-free" — is false.**
Both axes are χ-derived, and **there is no χ-free version of HC-1H's stratification that keeps its
structure.** A χ-free stratification would be a **different design**, not a redefinition.

## 6. WHAT REDEFINING THE STRATA WOULD COST — established, and smaller in one way than feared

**The validity cost is NOT what I expected, and the source says so directly.**

`a = Σ w_s·a_s` with **population weights** `w_s`, and the noise correction `ε̂` is **global**, not
per-stratum — HC-1H is explicit that per-stratum error rates are *"published as diagnostics only, never
as per-stratum corrections."* A population-weighted mean of within-stratum attenuations **estimates the
same population quantity under any partition**. HC-1H states the consequence itself, about the
allocation: ***"a bad allocation costs efficiency, never validity."***

**So redefining the strata does not invalidate the inherited attenuation result. It degrades its
precision.** That is the honest form of the cost, and it is worth having before the decision rather
than after.

**Three real costs remain, and the first is a hard constraint rather than a trade-off.**

1. **`N_HC_STRATA = 9` and `HC_MIN_PER_STRATUM = 30` are FROZEN CONSTANTS in `successor_ref_v9.py`**
   (L89, L91). **A redefinition with a different number of strata cannot be expressed without
   unfreezing v9.** A redefinition that keeps **exactly nine** strata is expressible; anything else is
   not, and I am not proposing an unfreeze.
2. **σ_a would rise, and σ_a is what the gate tests.** Neyman allocation `n_s ∝ N_s·√(a_s(1−a_s))`
   concentrates labels where accuracy is uncertain; the |χ| axis is there because accuracy varies with
   signal strength. Remove it and the same 500 labels buy less precision. **Efficiency is exactly what
   the power floor `a_LB ≥ a_gate(N)` measures, so a cost HC-1H calls "never validity" can still turn
   a passing gate into `INCONCLUSIVE-BY-POWER`.** How much is not establishable without the numbers.
3. **The obvious χ-free substitute axis is correlated with the tested axis.** Image quality is the
   natural candidate, and §2.7 measures `corr(psfsize_r, cos θ) = +0.4188` in the retained sample.
   **Stratifying the calibration on a quantity that tracks the axis under test couples the calibration
   to the signal geometry** — the hazard §2.7 documents at length, arriving through the back door.

## 7. THE OPTIONS, with what each costs

- **(A) The strata are χ-derived; Row F is restructured to permit it.** *Cost:* the hand-check sample
  is selected using the quantity being measured, and **the allocated universe Row G sees is
  χ-conditioned** — the premise the access-schedule question rested on. *Mitigating, and it should be
  weighed:* the allocation is **sealed**, and V65's precommitted traversal now forbids the adaptive
  requests that turned χ-conditioning into a log channel. **The χ-conditioning would stay inside the
  sealed boundary.**
- **(B) Redefine the strata χ-free for this study.** *Cost:* it is a **new design, not a
  redefinition**, because both inherited axes are χ-derived; it must keep **exactly nine** strata or
  unfreeze v9; σ_a rises and the power floor may stop passing; and the natural substitute axis is
  correlated with the tested axis. *Not a cost:* validity — the estimand is partition-invariant.
- **(C) Keep HC-1H's strata and move the construction out of Row F**, so the allocation arrives as a
  pinned artefact from a producer permitted to read χ. *Cost:* it **relocates the χ-conditioning
  rather than resolving it**, and adds a producer and a verifier.

**I am not choosing.** (A) and (C) both accept a χ-conditioned allocation and differ in who builds it;
(B) rejects it and pays in precision and design work. **The one thing I would not do is decide it by
quoting HC-1H**, which settles it by import rather than by decision — and produces the contradiction
sooner rather than never.

## 8. THE SHAPE, said out loud because it is the third instance today

**Row F's obligations and its prohibitions were written by different hands at different times.** Its
`emits` cell inherits a 3 × 9 allocation from the predecessor design; its `may touch` and `what voids`
cells were written to keep bin construction χ-free. **Each is defensible alone and they contradict
together.** That is the same shape as Row L, whose void condition forbade the signatures the row itself
mandates, and as the class rule and the VOID clause claiming the same events. **A row assembled from
independently correct parts is where this keeps coming from, and the repair is to read each row against
its own other cells before trusting any of them.**

## What I am not doing

**No repair is applied.** Repairing item 3 means changing Row F's stated read surface or its emission,
and repairing item 4 means either redefining the strata or scoping the quotation — **both change what
the study permits, so neither is mine.** **Nothing here is evidence about the sky.** BS-6 and the first
image byte remain blocked.
