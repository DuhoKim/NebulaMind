# BHU corpus synthesis memo — the durable deliverable

**Tori, 2026-08-31 10:32 KST.** Converts the completed sweep of the black-hole-universe published
bibliography into one durable memo, per Duho's "new target." **Base layer = peer-reviewed journal
articles only** (standing rule). Every claim here is a receipt: it quotes the primary text with a
page/equation/section reference, or names the pinned source + the gate that adjudicated it. No
memory-written claims. Authoritative source of every figure: `BHU_PUBLISHED_BIBLIOGRAPHY.md` (the
58-entry record, itself receipted to primaries) and its §0 standing table; battery `check.py` = 77
green. **No wiki placement — the Lab is the surface, and surfacing is a separate flagged step.**

Sweep state: **58 entries = 51 BHU papers + 7 support instruments.** 55 read in full; entries 1
(Pathria) and 3 (Stuckey) abstract-confirmed (paywalled bodies); entries 2, 42, 47 gated holdouts
(Duho: leave gated). Every readable entry double-gated by two adversarial seats.

---

## 1 · The verdict structure — what the base layer actually contains

### 1a. Tier map (parsed from the record, not recited)

| tier | count | what it means |
|---|---:|---|
| CONSISTENCY-ONLY | 31 | a construction shown compatible with observation; **predicts nothing measurable** |
| QUALITATIVE-DIRECTIONAL | 7 | a *direction* (sign, inequality) but no calibrated window |
| CALIBRATED-FALSIFIER | 4 | a number **and** a threshold that a measurement can cross — **entries 7, 31, 44, 51** |
| THEORETICAL-OBSTRUCTION | 3 | a no-go: proves a class cannot satisfy a conjunction — **entries 5, 22, 48** |
| PROSPECT | 3 | a "detectable" claim whose amplitude/rate is not yet computed |
| support (no tier) | 7 | imported measurement instruments (29, 30, 32–35, 58), not BHU-claim papers |
| UNREAD (gated) | 2 | **42, 47** — paywalled, left gated |

**58 total.** The field is dominated by consistency-only prose: **32 of 58 predict nothing
measurable** — they show the idea is *not ruled out*, which is not the same as support for it.

### 1b. Which entries carry a real number + threshold, vs. prose

Only **four** entries put a number against a threshold a measurement can cross — the
CALIBRATED-FALSIFIER tier (7, 31, 44, 51; §2 below). One more, **Gaztañaga (25)**, *displays* a
number but it is not predictive:

> Entry 25: "the Λ–r_S identification is a number, but it is fixed **from** the measured Λ rather
> than predicting it" (Λ = 3/r_S²; Symmetry 14, 1849).

Everything else in the "directional" and "consistency" tiers is prose: a matching construction, a
sign, or an existence demonstration. **The base layer's testable surface is essentially the four
calibrated falsifiers plus the obstruction theorems — the other 51 entries are context.**

### 1c. Overclaim taxonomy — the five ways a "prediction" dissolved under audit

The census survived five rounds of two-seat refutation. The recurring overclaim patterns, each with
its exemplar and primary receipt:

1. **Fitted-not-predicted** (entry 25). A number that looks predictive is fixed *from* the datum it
   "explains." Λ = 3/r_S² is read off the measured Λ; the "prediction" is the coincidence between
   the dark-energy scale and entry 23's causal-horizon cutoff — *"the scale is fitted from the
   anomalies it explains"* (Ranked §3). This is entry 25's falsifier-and-escape-clause in one
   sentence: the number and the reason it cannot fail are the same clause.
2. **Instrument-fired, not the claim** (entry 7). The falsifier crosses the *instrument's* threshold
   (Brown–Bethe M_max ≈ 1.5 M☉), but the source only says a heavy neutron star *"would put in
   serious doubt or simply falsify"* CNS (PRL 101, 091101; ≳ symbol pinned by Publisher's Note PRL
   101, 119901). Firing the instrument chain is a scope adjudication, **not** a refutation of the
   cosmology.
3. **Correction sized to the measurement** (entry 44). When the base model died at 8σ, the fix
   offered is *"an uncomputed ~4% correction whose size is read off the measurement it must
   reproduce"* (§0 table) — curve-fitting deferred as future work.
4. **Unreproduced from the stated inputs** (entry 51). A printed threshold that no route from the
   paper's own inputs reaches: *"none of six tested routes from its ρ_Ce reaches the printed 10¹⁶ kg
   floor, the paper omits the connecting step, and the enumeration is non-exhaustive"* (§0 table).
5. **Attributed threshold** (entry 31). The falsifying number is credited to *others*, not derived
   by the claimant: the 1.5 M☉ cap is *"attributed to Bethe–Brown calculations [52–54], not to CNS
   itself"* (Smolin §4, Physica A 340).

A sixth, structural, pattern sits above these: **tier-count ≠ live-falsifier-count.** The record
warns it in bold (§0): four calibrated falsifiers, but only two are LIVE-and-unfired, and one of
those is drifting *away* from firing (§2).

---

## 2 · The live-falsifier ledger

The §0 standing table, restated with each threshold and its receipt. **Two FIRED, two LIVE**, plus
the directional curvature watch.

| entry | status | threshold (primary ref) | current data |
|---|---|---|---|
| **7** Brown–Lee–Rho CNS | **FIRED** (scope: the *instrument*, not CNS) | neutron star M ≳ 2 M☉ "would … falsify" the Brown–Bethe/kaon-condensation chain (PRL 101, 091101; ≳ pinned by Note 119901) | heavy pulsars ≳ 2 M☉ observed; **fires the M_max≈1.5 instrument chain, not CNS** — the source gives CNS only "serious doubt." No pinned challenge in this corpus. |
| **44** Pourhasan et al. white-hole | **FIRED** (the Sec. 4 model, not the framework) | the 5D thermal field theory predicts exact scale invariance, **n_s = 1** (JCAP 04(2014)005 §4) | Planck 2018 VI eq (19): **n_s = 0.9649 ± 0.0042, 8σ from 1** (9σ with BAO); authors concede >5σ. Successor is an uncomputed ~4% correction (pattern 3). |
| **31** Smolin CNS | **LIVE, 1.36σ short** | a neutron star above **2.5 M☉** refutes CNS (Smolin §4, Physica A 340) | heaviest well-measured NS **2.35 ± 0.11 M☉**; 8.6% posterior mass above the bar and **moving away from firing as the error tightens.** Disputed (Rothman–Ellis 1993, Harrison 1995, Silk 1997 -- all three now read + pinned; every published critic attacks the reasoning, none the 2.5 Msun number. |
| **51** Popławski torsion | **LIVE, unfired** | a minimum black-hole mass floor **~10¹⁶ kg** (PLB 690, 73; VoR pinned, word-for-word identical to preprint on the floor) | **unreproduced from the stated inputs** — six routes from ρ_Ce tested, none reaches 10¹⁶ kg; connecting step omitted; enumeration non-exhaustive. The number stands in print but is not derivable from what the paper gives. |
| **54** Gaztañaga bounce (curvature) | directional, **LIVE but NOT FIRED** | predicts **closed** curvature, Ω_k < 0; refutes on a *confirmed* Ω_k > 0 (open); PRD 111, 103537 §VI, Eq. 27 | DESI DR2+CMB **Ω_k = +0.0023 ± 0.0011 (~2.1σ open)** — adverse (opposite sign) but not a detection; ACT "no departure from flatness"; Planck combined ~1.6σ closed. Guarded by the **b63 battery tripwire** (re-fires at ≥3σ open). Both seats: B61. |

**Reading the ledger honestly:** of the family's whole published output, exactly two calibrated
falsifiers remain LIVE (31, 51), and neither is close — 31 is drifting away from its bar, 51's
number cannot be reproduced from its own inputs. The two FIRED ones (7, 44) each fired a *sub-model*
(an instrument chain; a Sec. 4 field theory), not the cosmological framework. **Nothing in the base
layer is currently refuted at the framework level, and nothing is currently on the edge of firing.**

---

## 3 · What the three gated papers would unlock — ranked, with a price tag

All three are pre-2010/pre-web paywalled, ~a few thousand won each by interlibrary copy (never a
price in the record; ILL is the lawful route). Ranked by what a read would actually add:

1. **Entry 47 — Sato, Kodama, Sasaki & Maeda (1982), PLB 108, 103.** *Highest value.* The earliest
   false-vacuum multi-universe-production mechanism, and the missing member of the false-vacuum
   branch that the Farhi–Guth **obstruction (entry 48)** is *about*. Reading it closes the one open
   question in that branch: does the 1982 mechanism fall inside Farhi–Guth's no-go, or predate and
   sidestep it? That is a genuine obstruction cross-check, not completeness for its own sake.
   **Unlock: does entry 48's no-go bind the branch's founding paper.**
2. **Entry 42 — González-Díaz (1991), PLB 261, 357.** *Medium.* Baby-universe branch (with 13/14/15
   /17/43); "baby universe metric equivalent to an interior black-hole metric." A read tests whether
   it adds a metric-equivalence result the branch does not already have, or is another consistency
   construction. **Unlock: one row's tier — likely consistency-only, possibly a directional edge.**
3. **Entry 2 — Good (1972), Physics Today 25(7), 15.** *Lowest.* A one-page note on nested
   ("Chinese-box") universes. Historical completeness only; no mechanism, no observable.
   **Unlock: nothing testable — provenance only.**

**Recommendation for the access decision:** if any single paper is worth an ILL, it is **47** — it
converts an *assumed* obstruction-branch relationship into a checked one. 42 and 2 are completeness.

---

## 4 · Candidate next falsifiers the family's own texts imply but never state

These are testable edges the primary papers gesture at without committing to a number. Each is a
*candidate* — the memo's honesty is that none is yet a stated falsifier.

1. **The Popławski interior transfer function (entries 8–12).** The only published multi-paper
   mechanism with explicit field equations, yet *"the transfer function the literature never wrote —
   from parent-hole parameters through the bounce to any interior observable"* is absent (Ranked
   §1). Deriving it in-house would state whether **any finite-amplitude interior signature survives**
   the Einstein–Cartan bounce (spin-density parameter Ω_S = −8.6×10⁻⁷⁰, erratum included). If a
   finite amplitude survives, that is a new calibrated falsifier; if not, the branch is
   consistency-only *by derivation*, not by omission.
2. **The Roupas amplitude (entry 21).** A published *"detectable"* claim with a named instrument
   band (μHz–Hz, LISA-class) but no computed amplitude/rate. *"If a number exists, this becomes a
   fifth calibrated falsifier; if not, it reclassifies to PROSPECT-without-a-number"* (Ranked §4).
   The cheapest high-leverage next audit in the corpus.
3. **The Gaztañaga causal-horizon cutoff (entries 23/25/26).** The series implies a power-spectrum
   cutoff at the causal horizon and ties the CMB low quadrupole to it. It is testable against Planck
   likelihoods — **but only becomes a falsifier if the cutoff scale is fixed independently** of the
   anomalies it explains (pattern 1). A prediction that fixes the scale from first principles, not
   from the low-ℓ deficit, would be the family's first genuine CMB falsifier.
4. **The preferred-axis / spin-parity edge (entry 58 → DESI).** Longo's handedness dipole
   (−0.0408 ± 0.011, PLB 699; entry 58, content-verified in b54) is the observational instrument for
   the rotating-parent family's preferred-axis prediction — *the amplitude the DESI spin-parity
   campaign tests.* A confirmed statistical-isotropy null on DESI Legacy (the Land 2008 direction)
   would be an implied refutation of the preferred-axis subfamily. **This is the live cross-lane
   edge — Hwao's prereg V124 is exactly this test.**
5. **Easson's cross-programme obstruction map (entry 22).** The 2026 no-go on minimal regular-BH
   cosmologies implies a *meta*-falsifier: mapping which published interiors (Dymnikova 18/19,
   Bronnikov 20, Roupas 21, Gaztañaga 25/26, Popławski 11) it **kills, restricts, or spares**
   (Ranked §5). Not a data-falsifier but a theory-internal one — a single theorem that could retire
   several rows at once.

---

## Provenance

Every figure above traces to a pinned primary or a two-seat gate verdict in the lane; the index is
`BHU_PUBLISHED_BIBLIOGRAPHY.md` §0 + entries, and the receipts are the `b*` battery checks and the
`AGATE_/CGATE_*` verdict files. All sources are now read: Silk 1997 (entry 31 third critic) was the sole unread dependency at memo time; read + pinned 2026-08-31, tier-neutral -- it attacks the black-hole-abundance reasoning, not the 2.5 Msun falsifier. This memo is a note on the corpus, **not** a study of
the cosmology; it belongs as the closing synthesis of the BHU line.
