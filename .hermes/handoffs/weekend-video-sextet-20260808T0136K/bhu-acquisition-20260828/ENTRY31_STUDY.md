# Entry 31: the corpus's one live falsifier turns on an instrument choice, not on data

**Tori, 2026-08-29. Written to be read cold.** Reproduce with `b4_entry31_falsifier.py` (7/7) and
`b5_entry31_drift_and_movers.py` (2/2). Every number below is parsed from a pinned source.

---

## The headline

**Entry 31's status is not yet a fact about the universe. It is a fact about which compact object
you accept as a well-measured neutron star.**

Smolin (2004) predicts that a sufficiently heavy neutron star refutes cosmological natural
selection, and states his own bar: **2.5 M☉**. Against that single bar, from pinned sources, the
corpus supports **four readings that disagree — including one on which the falsifier has already
fired.**

| # | measurement | instrument | vs the 2.5 M☉ bar |
|---|---|---|---|
| 1 | PSR J0740+6620, 2.08 ± 0.07 | relativistic Shapiro delay, radio timing | **6.0σ away — effectively dead** |
| 2 | M_TOV from GW170817, 2.210 +0.116 −0.123 (2σ) | gravitational waves, tidal deformability | **bar sits above the interval — excluded** |
| 3 | PSR J0952−0607, 2.35 ± 0.17 | Keck optical light curve + radial velocities | **0.88σ short — live, ~19% above** |
| 4 | GW190814 secondary, 2.50–2.67 (90%) — **if it is a neutron star** | gravitational waves | **entire interval at or above the bar — FIRES** |

**Read rows 2 and 4 together or you will misread this.** Both are gravitational-wave measurements
of the maximum neutron-star mass, they come from the *same* analysis paper, and **they point in
opposite directions.** GW190814 forces M_TOV ≳ 2.5 *if* its secondary was a neutron star; the same
paper's preferred value from GW170817 puts the bar *above* its 2σ interval. A reader who sees only
row 4 will conclude the falsifier has fired. A reader who sees only row 2 will conclude it cannot.

**Nobody had noticed any of this**, because our record carried a single number — *1.36σ* — that
belongs to none of the four rows. It rested on an uncertainty (±0.11) with no pinned origin
against a published ±0.17.

**Duho has ruled on rows 1 and 3: keep both, no winner picked.** Rows 2 and 4 were pinned after
that ruling and he has not ruled on them.

---

## 1. The bar, from Smolin's own words

> *"Sufficiently high is certainly 2.5 M☉, although if one is completely confident of Bethe and
> Brown's upper limit of 1.5 solar masses, any value higher than this would be troubling."*

Our record's 2.5 M☉ is correct. **What it omitted is that the bar is graded** — 2.5 for certain
refutation, 1.5 for "troubling", conditional on crediting Bethe–Brown.

And Smolin names his own standard of evidence:

> *"Presently all well measured neutron star masses are from **binary pulsar data** and are all
> below 1.5 M☉."*

**That factual premise is now false.** Both pinned measurements exceed 1.5 by a wide margin —
including 2.08 by the very instrument he named. *The lower bar was passed years ago, and our
record never noticed because it tracked only the higher one.*

---

## 2. Why the instrument decides it

- **Radio timing** (J0740+6620) measures mass through the **relativistic Shapiro delay** — a
  general-relativistic propagation effect in the pulse arrival times. Few modelling assumptions.
- **Black-widow optical** (J0952−0607) measures mass by fitting **light curves and radial
  velocities of a companion being irradiated by the pulsar.** The mass depends on the heating
  model, the inclination, and the companion's Roche-lobe filling factor. Romani et al. argue their
  modelling uncertainties are small because the heating is not extreme — but this is a different
  and more model-dependent instrument than timing.

**Which one counts is not a technical question with a technical answer.** Romani et al. call
theirs *"the largest well-measured mass found to date"*; Smolin's sentence names binary pulsar
data. Both are defensible readings of "well measured."

> **My inference, flagged as mine:** reading Smolin's sentence as a *permanent criterion* rather
> than a *description of the state of measurement in 2004* is a judgement I am supplying and he
> did not. The entire finding rests on it. **This is the one step where I am not reading the
> source but interpreting it**, and it should not be adopted without someone else checking it.

---

## 3. The drift claim is true only where it does not matter

Our record says entry 31 is *"drifting away from firing."* Computed per instrument:

| | epoch 1 | epoch 2 | verdict |
|---|---|---|---|
| **radio timing** | Cromartie 2020: 2.14 ± 0.095 → 3.79σ | Fonseca 2021: 2.08 ± 0.07 → **6.00σ** | **drift is REAL** — posterior above the bar fell by a factor of **76,510** |
| **black widow** | — | — | **UNCOMPUTABLE**: one measurement, no history |

**The reassuring half of our record's summary was carried entirely by the instrument on which
there is nothing left to reassure about.** On the branch where the falsifier is actually live, we
have a single measurement and no trend at all.

---

## 4. What would move it

**(A) Settle which branch we are on — highest value.** An independent mass for a black widow by a
method not dependent on modelling an irradiated companion. Shapiro delay needs a near-edge-on
orbit, which most black widows do not offer — so the realistic version is *population
consistency* across many systems, where a systematic bias would show as an offset. **Years, and
ongoing.**

**(B) Fire it on the conservative branch.** A radio-timed neutron star above 2.5 M☉. The heaviest
we hold is 2.08 ± 0.07 — firing needs ~0.4 M☉ more than any pulsar ever timed. **Not a near-miss.**
MeerKAT/TRAPUM, FAST, CHIME now; SKA in the 2030s.

**(C) Kill it outright.** Continued tightening on J0740+6620. Already happening, already at 6σ.
It cannot touch the black-widow branch — which is why (A) matters.

**(D) A third instrument, named but not pinned.** Gravitational-wave masses of compact objects in
the 2.5–3 M☉ range bear directly on the bar, since Smolin's argument concerns the maximum
neutron-star mass, not pulsars specifically. **No value is quoted here and no GW paper is pinned**;
the known difficulty is that an object in that range may be a light black hole, which is exactly
the ambiguity the bar cannot tolerate. Cheap to acquire and the obvious next pin.

---

## 6. The gravitational-wave leg — an object sitting on the bar whose nature is contested

Pinned today: the GW190814 discovery paper (`2006.12611`) and two analyses of what it implies for
the maximum neutron-star mass (`2007.10999`, `2101.01735`).

Smolin's argument concerns the **maximum neutron-star mass**, not pulsars specifically — so any
instrument measuring that maximum is on-bar. Gravitational waves supply two, and **they disagree
with each other.**

**GW190814's secondary is 2.50–2.67 M☉ at 90% credibility — the entire interval at or above the
bar.** And the discovery paper explicitly declines to say what it is:

> *"its secondary component is **either the lightest black hole or the heaviest neutron star**
> ever discovered in a double compact-object system."*

The tension paper states the conditional outright: GW170817 suggests **M_TOV ≲ 2.3 M☉**, while
GW190814 requires **M_TOV ≳ 2.5 M☉** *"if the secondary was a (non- or slowly rotating) neutron
star at merger."* Its own preferred value from GW170817 is **M_TOV = 2.210 +0.116 −0.123 M☉ (2σ)**
— which puts Smolin's bar **above** the interval, pointing the same way as radio timing and the
opposite way from the event the paper is named after.

**So whether the corpus's only live falsifier has already fired turns on whether one object
241 Mpc away was a neutron star or a black hole — a question its discoverers refused to answer.**
That refusal is the finding. It is not resolved here, and it should not be.

## 5. What this is for Duho to decide

**Which instrument counts** — and it decides whether the corpus has **one live falsifier or zero.**

- Accept **radio timing only**: entry 31 is 6σ from firing and the BHU corpus has **no live
  calibrated falsifier at all**.
- Accept **the black widow**: entry 31 is 0.88σ short with **19% posterior mass above the bar** —
  a real test, currently undecided, and the only one the programme has.

I have not resolved it, and should not: it turns on which measurement Smolin would have accepted,
and he is not available to ask.
