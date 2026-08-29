# Entry 31: the corpus's one live falsifier turns on an instrument choice, not on data

**Tori, 2026-08-29. Written to be read cold.** Reproduce with `b4_entry31_falsifier.py` (7/7) and
`b5_entry31_drift_and_movers.py` (2/2). Every number below is parsed from a pinned source.

---

## The headline

**Entry 31's status is not yet a fact about the universe. It is a fact about which neutron star
you accept as "well measured."**

Smolin (2004) predicts that a sufficiently heavy neutron star refutes cosmological natural
selection. Against the same bar, from the same corpus:

| accepted measurement | mass | instrument | distance from bar | P(above bar) |
|---|---|---|---|---|
| **PSR J0740+6620** | 2.08 ± 0.07 | relativistic Shapiro delay, radio timing | **6.0σ** | ~1 × 10⁻⁹ |
| **PSR J0952−0607** | 2.35 ± 0.17 | Keck optical light curve + radial velocities | **0.88σ** | **19%** |

**Effectively dead, or live at one in five.** Nobody had noticed, because our record carried a
single number — *1.36σ* — that sits between the two answers and belongs to neither. It came from
an uncertainty (±0.11) with no pinned origin; the published value is ±0.17.

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

## 5. What this is for Duho to decide

**Which instrument counts** — and it decides whether the corpus has **one live falsifier or zero.**

- Accept **radio timing only**: entry 31 is 6σ from firing and the BHU corpus has **no live
  calibrated falsifier at all**.
- Accept **the black widow**: entry 31 is 0.88σ short with **19% posterior mass above the bar** —
  a real test, currently undecided, and the only one the programme has.

I have not resolved it, and should not: it turns on which measurement Smolin would have accepted,
and he is not available to ask.
