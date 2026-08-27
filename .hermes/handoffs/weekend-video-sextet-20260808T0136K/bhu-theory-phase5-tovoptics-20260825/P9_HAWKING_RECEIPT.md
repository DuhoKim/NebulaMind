# P9 — can Hawking radiation test the black-hole-universe model?

Question posed by Duho, 2026-08-27 17:0x KST: *"what about Hawking radiation? any literature
mention about it? and use it to prove BHU cosmology?"*

**Verdict: NO — not with what these papers supply.** The route fails on the source itself
(reason 1 in the bottom line: the audited artifacts never define a Hawking observable), and the
naive Schwarzschild calculation is independently unusable on structural and amplitude grounds
(reasons 2 and 3).

> **Header corrected 2026-08-27 at REGATE5.** This originally read *"it fails four independent
> ways, each fatal on its own"*. Two changes: reason 4 (the factor-of-two comparison) is
> **supporting only** and is not fatal on its own; and the verdict is **source-pinned** — it
> closes the route *as these papers supply it*, not for any conceivable added
> horizon-thermodynamics model. See the scope box in the Bottom line and the correction
> appended at the end.

Computation: `p9_hawking.py`, Python 3.9.6, `python3 p9_hawking.py` → exit 0, **16/16 checks**.
Every number below is printed by that file. Literature claims below are quoted from primary
sources pinned in this repo or fetched this session; nothing here is asserted from memory.

---

## Part 1 — the literature (what is actually there)

### 1a. Smoller & Temple themselves say nothing about it

Grep over the pinned clean text of the audited source
(`bhu-reading-20260823/sources/math-ph_0302036_clean.txt`):

- `grep -i hawking` → **2 hits, both in the reference list** (Hawking & Israel, *Einstein
  Centenary Survey*; Hawking & Ellis, *Large Scale Structure of Spacetime*). Neither is cited
  for radiation.
- `smoller_temple_1997_clean.txt`: `grep -c -i hawking` → **0**.

There is no Hawking radiation content in the model this lane has been auditing.

### 1b. The horizon in the model is a WHITE hole horizon — verbatim

> "the shock wave can be approximated by a zero pressure, k = 0 Oppenheimer-Snyder (OS)
> interface that emerges from the **White Hole event horizon** of an ambient Schwarzschild
> metric of finite mass."

and the time orientation is *fixed* by the entropy condition, in the direction that excludes
Hawking's setup:

> "the FRW metric expanding outward behind a shock wave emanating from a White Hole is entropy
> satisfying, while its time reversal, the FRW metric contracting into a Black hole, is entropy
> violating."

Hawking's derivation is for a **black** hole formed by collapse, with the outgoing flux read at
future null infinity. A white hole is its time reverse. The model does not merely fail to
discuss Hawking radiation — it fixes the arrow of time to the case where the standard
derivation does not apply.

### 1c. Smoller & Temple take the CMB temperature as an INPUT

> "H₀ and the background radiation temperature T₀ ... the freedom to assign T₀ is represented by
> the freedom [to ...]"

T₀ is an *assignable constant* of the solution. A model that inputs the CMB temperature cannot
also derive it. Any "the CMB is the model's own radiation" claim built on this solution is
circular by construction.

### 1d. The one published white-hole + Hawking paper is already in our bibliography

Entry **45**, `BHU_PUBLISHED_BIBLIOGRAPHY.md`: *"White hole cosmology and Hawking radiation from
quantum cosmological perturbations."* **Phys. Rev. D 106, 123505 (2022)**, DOI verified.
Read 2026-08-23. Rated **CONSISTENCY-ONLY** — QFT in the white-hole interior, Hawking radiation
from cosmological-style perturbations, **no falsifier**, and my read note demoted it to
family-adjacent rather than a universe-origin claim. It does not supply a test.

### 1e. The nearest thing to a "CMB from the black hole universe" claim is NOT Hawking radiation

T.X. Zhang, *"Cosmic microwave background radiation of black hole universe"*, **Ap&SS 330,
157–165 (2010)** — peer-reviewed, so it clears the published-only bar. Its mechanism is
explicitly **ordinary blackbody radiation of the contents**: the universe "can be considered as
an ideal black body", cooling as it accretes and merges, with the thermal history "derived from
the Planck law of black body radiation and radiation energy conservation." That is the
radiation of the *matter*, not of the *horizon*.

**Scope limit, stated honestly:** the Springer page is paywalled and the INSPIRE record did not
render; the above is from search-result summaries of the abstract, not the article text. I am
**not** certifying Zhang's internal argument — only that the mechanism named in its abstract is
blackbody, not Hawking. Part 2E shows why no author could have chosen Hawking here.

### 1f. Precedent: the only serious attempt to see Hawking radiation on the sky did not survive

Not BHU (it is Penrose's conformal cyclic cosmology), but it is the live cautionary case for
"use Hawking radiation as a cosmological observable":

- An, Meissner, Nurowski & Penrose, **MNRAS 495, 3403 (2020)** — "Hawking points" claimed at
  99.98% confidence.
- Jow & Scott, **JCAP 03 (2020) 021** — after marginalising over ring size the excess is 87%,
  *little more than 1σ*. No statistically significant evidence.

---

## Part 2 — the calculation (16/16, `p9_hawking.py`)

Constants CODATA 2018. Run at both H₀ = 67.36 (Planck 2018) and 73.04 (SH0ES) km/s/Mpc; every
conclusion below holds at both, and the two ratios that matter are **exactly H₀-independent**.

### A. The famous "the universe satisfies the black hole condition" is an identity, not evidence

Mass inside the Hubble radius at critical density: `M_H = 9.246446e+52 kg` (Planck), and the
closed form is `M = c³/(2GH₀)` — reproduced to relative difference **0.000e+00**. Its
Schwarzschild radius is `r_s = 1.373312e+26 m`, and

    r_s / R_H = 1.000000000000        (check A2, |ratio−1| = 2.220e-16)

**This is Ω = 1 rewritten.** It is a consequence of assuming critical density, so it carries
exactly zero evidential weight for BHU. It should never be quoted as a coincidence.

### B. Scale, not degeneracy — SUPPORTING ONLY

> **CORRECTED 2026-08-27 by REGATE5.** This section was originally headed "THE DEGENERACY —
> this is the important one" and was made load-bearing. That was an overclaim; see the
> correction appended at the end of this receipt. The arithmetic below is unchanged and
> correct. The weight placed on it is not.

    T_Hawking(M_H)          = 1.326889e-30 K
    T_deSitter(H₀) = ħH₀/2πk = 2.653778e-30 K
    ratio                   = 2.000000000000        (check B1)

**The BHU Hawking temperature is exactly half the Gibbons–Hawking temperature that ordinary
ΛCDM already predicts for its own de Sitter horizon.** Using the asymptotic de Sitter rate
`H_Λ = H₀√Ω_Λ` instead, the ratio is 1.654932 (check B2).

~~So even granting a perfect thermometer of unlimited sensitivity, a horizon-temperature
measurement cannot distinguish BHU from standard cosmology — the two predictions are degenerate
at order unity.~~ **WITHDRAWN at REGATE5.** A factor of two is not a degeneracy: an ideal
thermometer *could* tell 1.3269e-30 K from 2.6538e-30 K.

The supportable statement is narrower. Both figures sit at the same `ħH/k_B` scale, so a
horizon temperature "of order `ħH/k_B`" is **not by itself evidence for BHU** — it is not a
*distinctive* prediction. That is a distinctiveness argument, and it supports the closure
without carrying it.

### C. STRUCTURAL — the quantum is bigger than the box

    Wien peak wavelength    = 2.183884e+27 m
    observable radius R_H   = 1.373312e+26 m
    λ_peak / R_H            = 15.9023               (check C1)

**The typical Hawking wavelength is ~16 times the radius of the observable universe.** Not one
mode fits inside the region we can see. This is not a sensitivity problem — there is no
apparatus, in principle, inside our horizon that can resolve a wavelength larger than our
horizon.

Note the ratio **15.9023 is identical at both H₀ values** — λ_peak and R_H both scale as 1/H₀,
so this number is immune to the Hubble tension and to any revision of the distance scale.

### D. Amplitude and timescale (the easy failures)

    u_Hawking / u_CMB       = 5.617799e-122         (check D1)
    t_evap                  = 2.107138e+135 yr = 1.451605e+125 Hubble times   (check D2)
    horizon entropy S/k_B   = 2.268133e+122

### E. What the "CMB is Hawking radiation" claim would actually require

Solving `T_H(M) = 2.72548 K` for M:

    required mass           = 4.501595e+22 kg = 0.6131 lunar masses = 0.0075 Earth masses
    required r_s            = 6.685913e-05 m = 66.86 micrometres     (check E1)
    M_H / M_required        = 2.054e+30                              (check E2)

**A 2.725 K Hawking source is a sub-lunar mass with a 67-micron horizon.** Thirty orders of
magnitude below the observable universe. This is why no author in the peer-reviewed BHU
literature identifies the CMB with Hawking radiation, and why Zhang (1e) reaches for blackbody
radiation of the contents instead.

---

## Part 3 — the trap this question walks into, and why I nearly fell in it

Writing `T_H = ħc³/8πGMk_B` for this model **assumes a Schwarzschild Killing horizon in
vacuum with a well-defined asymptotic region**. The version of Smoller–Temple this phase
audited has a **TOV fluid exterior** with `p = σρ`, and (1b) a **white** hole horizon whose time
orientation is fixed against Hawking's construction. The papers supply neither the vacuum
region nor the thermodynamics.

So quoting a Hawking temperature for this cosmology means **adding physics the source does not
contain, and then reporting a property of what was added.**

That is structurally the identical error REGATE4 failed me for four hours ago: the null I
claimed was a property of the two source closures I invented, not of the pinned model. The same
gap in the same papers — no thermodynamics for the exterior — defeats the optical test and the
Hawking test, by the same mechanism. That is a coherent finding, not a coincidence: **it is the
missing physics, not the difficulty of the measurement, that keeps closing these routes.**

---

## Part 4 — the one residue worth naming (NOT computed here)

The shock is **not** a horizon. Particle creation by a moving boundary is the dynamical
Casimir / moving-mirror effect, which is genuinely different physics from Hawking radiation,
and nobody appears to have computed it for the Smoller–Temple shock.

**Labelled scoping only, not a result of this receipt:** the shock's characteristic rate is
cosmological (~H), so the emission scale would land at the same ~10⁻³⁰ K as everything else in
Part 2, and would die at C and D for the same reasons. I have **not** computed this and do not
claim it. If it is ever worth doing, it needs its own brief and its own gate — and it would
need the same exterior thermodynamics the papers do not supply.

---

## Bottom line

**Hawking radiation, as these papers supply it, cannot prove — or test — BHU cosmology.**

> **Scope, tightened 2026-08-27 by `CGATE_REGATE5_CONFIRM_VERDICT.md`.** The sentence above
> originally read "Hawking radiation cannot prove — or test — BHU cosmology," full stop. That
> is broader than the evidence. What is established is that **the Smoller–Temple artifacts
> audited here do not themselves define a Hawking observable**, so importing the Schwarzschild
> formula reports a property of an added model. It is **not** established that no conceivable
> added horizon-thermodynamics model could ever produce an observable. Anyone who supplies the
> missing exterior thermodynamics as a defended physical model is outside this receipt's scope,
> not refuted by it.

1. **Not defined for this model:** white-hole horizon, non-vacuum exterior, no thermodynamics in
   the source; and T₀ is an input to the solution, not an output (1b, 1c, Part 3).
2. **Not resolvable, in principle:** peak wavelength ~16× the observable universe (C).
3. **Not detectable:** 10⁻¹²² of the CMB energy density; evaporation 10¹²⁵ Hubble times (D).
4. **Not distinctive** (supporting only, demoted at REGATE5): the same `ħH/k_B` scale ΛCDM
   already produces for its own horizon (B).

**Ordering corrected at REGATE5.** I originally made (4) the strongest and said it generalised
to any black-hole cosmology at the Hubble scale. It does not carry that weight. The strongest
is now **(1)**, and it is the only one of the four that is genuinely about the *source*.
**(2)** is the strongest self-contained argument: structural, in-principle, untouched by the
gate — but note that (2) and (3) bound what the **naive Schwarzschild calculation** could
deliver, not what any added thermodynamic model could deliver.

(1) is also what ties this route to the optical route, since both close on the same missing
physics — **as a diagnosis of these papers, not as a theorem.** The confirm seat set that limit
explicitly and I am keeping it: a neat unifying story is the same shape as the overclaim that
produced the hold.

*Files: `p9_hawking.py` (16/16), this receipt.*

*Status trail: written 2026-08-27 while Phase 5b was under HOLD per `REGATE4_DISPOSITION.md`.
Gated at REGATE5 — held by `CGATE_REGATE5_PHASE5B_VERDICT.md`
(HOLD_HAWKING_DEGENERACY_OVERCLAIM), passed by `AGATE_REGATE5_VERDICT.md` (PASS_PHASE5B), hold
discharged by `CGATE_REGATE5_CONFIRM_VERDICT.md` (CLEARED_HAWKING_DEMOTION) after the demotion
and this scope tightening. The two seats SPLIT on this point: agy called the closure solid and
raised no degeneracy objection; codex held on it. I acted on the hold because I judged it right
on the merits, and a third fresh seat agreed.*

---

# CORRECTION, 2026-08-27 — REGATE5 required repair

Gate: `CGATE_REGATE5_PHASE5B_VERDICT.md`, **HOLD_HAWKING_DEGENERACY_OVERCLAIM** (codex seat,
gpt-5.5, fresh context). Accepted in full.

## What the gate said

> "A factor of two is not a degeneracy in the discriminating-measurement sense. If both
> quantities were well-defined observables and were measurable with unlimited precision, they
> would be distinguishable."

## Accepted, and it is plainly right

I wrote that a perfect thermometer of unlimited sensitivity could not tell the two pictures
apart. But **1.326889e-30 K and 2.653778e-30 K are two different numbers.** An ideal instrument
distinguishes them. Calling an exact factor of two a "degeneracy" was wrong, and I made it the
load-bearing argument of the whole closure.

## What replaces it

Both figures sit at the same `ħH/k_B` scale, so a horizon temperature of that order is not by
itself evidence for BHU — it is not a **distinctive** prediction. Supporting, not load-bearing.

And the deeper point I had buried in Part 3 should have been the headline all along: **the BHU
value is not even well-defined.** `T_H = ħc³/8πGMk_B` presumes a vacuum Killing horizon with an
asymptotic region; the audited exterior is a TOV fluid and the horizon is white-hole oriented.
There is no sharp BHU number to compare against — the "prediction" is a property of the formula
imported, not of the solution being tested.

## What is untouched

The gate explicitly affirms the rest: *"the stronger objections in p9 still stand — the audited
Smoller-Temple model does not supply the horizon thermodynamics being computed, its horizon is
white-hole oriented in the cited construction, T0 is an assigned input rather than an output,
the naive thermal scale is about 1e-30 K, and the Wien wavelength is larger than the observable
region."* **The route stays closed.** No arithmetic in this receipt changed; `p9_hawking.py`
still runs 16/16, exit 0.

## The lesson, which is the same one as this morning

I picked the argument that sounded most striking — an *exact* factor of two — and made it carry
the conclusion, when the argument that actually carries it is duller and stronger: the papers do
not contain the physics. Twice in one day I have promoted the elegant claim over the robust one.
The structural argument (`λ_peak / R_H = 15.9023`, no mode fits inside the observable universe)
was always the best self-contained point and I ranked it second.

## Outstanding, and not repaired by this correction

**The overclaimed version was read aloud and published** — `20260827T171012-tori-report.mp3`
(queue seq 82, 17:10:12 KST), which states: *"the ratio between them is a factor of exactly 2 …
so even a perfect thermometer, of unlimited sensitivity, could not tell the two pictures
apart."* That recording now carries a withdrawn claim. Correcting the audio record is a separate
action and is **not** done by this file.
