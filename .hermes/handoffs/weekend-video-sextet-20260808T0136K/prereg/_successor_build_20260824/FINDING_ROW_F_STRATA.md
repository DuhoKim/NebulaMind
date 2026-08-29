**STATUS: ANSWER — for the principal, via Blanc. Asked 22:46 KST: do §6.3's "V3-pred's nine HC strata"
mean HC-1H's machine-committee state × |χ| tertile IN THIS DRAFT?**
**THE ANSWER IS THE THIRD ONE: THE DRAFT IS SILENT, and it cannot be determined from the text.** It
neither redefines the strata nor restates them. **Three things I could establish are below, and one of
them is a defect that does not depend on the strata question at all.**

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

## What I am not doing

**No repair is applied.** Repairing item 3 means changing Row F's stated read surface or its emission,
and repairing item 4 means either redefining the strata or scoping the quotation — **both change what
the study permits, so neither is mine.** **Nothing here is evidence about the sky.** BS-6 and the first
image byte remain blocked.
