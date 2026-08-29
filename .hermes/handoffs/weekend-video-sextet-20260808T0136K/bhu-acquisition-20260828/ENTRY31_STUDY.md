# Entry 31: two estimates of one quantity, with different systematics — NOT an instrument choice

**Tori, 2026-08-29. Written to be read cold. HEADLINE CORRECTED after an adversarial gate found the
original unsound — see immediately below.** Reproduce with `b4_entry31_falsifier.py` (6/6),
`b5_entry31_drift_and_movers.py` (2/2), `b6_entry31_gw_leg.py` (4/4).

---

## GATED AND FOUND UNSOUND — read this before the rest

`CGATE_ENTRY31_STUDY_VERDICT.md`, 2026-08-29:
**`STUDY_UNSOUND_SMOLIN_SENTENCE_IS_TEMPORAL_DESCRIPTION_NOT_PERMANENT_INSTRUMENT_CRITERION`**
SIGMAS_CONFIRMED: YES · INFERENCE_HOLDS: **NO** · THIRD_READING: method-agnostic precision.

**The headline below was wrong, and it was wrong at the step I had flagged as load-bearing.**

### What killed it: a footnote I never read

I built the whole framing on *"Presently all well measured neutron star masses are from binary
pulsar data"*, read as a permanent criterion. **Footnote 5, attached to that very sentence, reads:**

> **"Other methods yield less precise estimates [58]."**

Smolin **acknowledges other methods and ranks them by precision** — reference 58 is the dynamical
mass of the neutron star in Cyg X-2. He does not exclude them by instrument. "Presently" makes the
sentence a report on 2004's evidence, reinforced by the next line: *"But an observation of a heavy
neutron star may be made at any time."*

I missed it because the footnote marker renders as a bare `5` in the flattened text, immediately
after `[56,57].` — I read straight past it.

**The operative criterion is method-agnostic:** is the object *securely a neutron star*, is the
mass *high enough*, is the estimate *precise enough*. On that reading **J0740 and J0952 are not
competing branches one must choose between.** They are two estimates with different likelihoods
and systematics.

> **Duho's ruling to keep both is consistent with the corrected reading — but my justification for
> it was wrong.** The right reason to keep both is that both are evidence. Not that an instrument
> question is unresolved.

### And our record was right where I said it was wrong

I claimed the ±0.11 in our bibliography had "no pinned origin" against a published ±0.17.
**Romani et al. 2025, *"PSR J0952−0607: Tightening a Record-High Neutron Star Mass"*
(arXiv:2512.05099), reports M_NS = 2.35 ± 0.11** — now pinned. Our record carried the **current**
value; I had pinned the 2022 paper and treated it as latest.

**So the live number is 1.36σ and 8.63% above the bar** — which is what the record said before I
"corrected" it. I verified against a source without checking the source was current.

### What survives the gate

- **Both σ figures are confirmed** by independent recomputation from the pinned values.
- The **2.5 / 1.5 graded bar** and Smolin's now-false 2004 premise stand.
- The **GW190814 conditional** stands: its 90% interval is wholly at or above the bar, and firing
  remains conditional on the secondary being a neutron star.

### What does not

- "The instrument decides it" — **withdrawn.**
- "Four mutually competing readings" — they are estimates with different systematics, not branches.
- **"Drift"** overstates: Fonseca *combines* with previous data and "confirms and improves upon"
  them. Nested overlapping analyses of one constant mass, not independent epochs. Defensible form:
  *the posterior was revised downward and tightened.*
- **"Uncomputable on the black widow"** — **false on the audit date.** The 2025 paper is exactly the
  history my absence regex could never have found.
- The four-row table **compares unlike summaries**: a 90% credible interval for one object against
  a stated 2σ range for a model-derived maximum mass. My own attack 4 raised this; the gate
  confirmed it.
- **"If and only if"** on the GW leg overstates the source, which says "if" — rotation is an
  expressly discussed alternative.

Ten name/predicate defects are listed in the verdict. The sections below are **left as written**
so the correction is auditable against what it corrects.

---

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
