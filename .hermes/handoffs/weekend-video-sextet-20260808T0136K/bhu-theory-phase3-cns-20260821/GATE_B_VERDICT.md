PASS_P3B_TRACKB

# Gate B verdict — Track B (strict in-house model / He-giant proviso)

**Reviewer:** fresh one-shot adversarial gate, no prior context. Read PHASE3_BRIEF.md,
TRACK_B_INTERIM_FINDING.md (original §1–6 AND the SETTLED reversal), the three receipts, and the
three primary sources in `sources/`. Consulted C08 but did not re-litigate it. All three receipts
rerun with `python3` and reproduce the printed tables. No network; portal.nersc.gov untouched.

**Bottom line:** the reversal is **sound, not over-corrected**. The author correctly (a) established
J1913+1102 shares the He-star channel the proviso is written for, then (b) showed the proviso's
*magnitude* (0.1–0.2 M⊙) is superseded by the modern DNS-formation budget, so the margin returns to
~21σ — and (c) *kept* the one genuinely valuable observation (the caveat is quantified in a companion
paper, contra the adjudication's "unquantified") rather than throwing it away to look decisive. The
single load-bearing move — mapping BLR's He-red-giant transfer onto Tauris's budgeted phases — is
justified by the sources. Three minor, non-blocking notes below; none moves the verdict.

---

## Check 1 — the 4% derivation. **CHECK (with one labelled auditor addition).**
`blr_physrept_clean.txt` 1119–1123, verbatim: *"Helium burning takes up 10% of the star lifetime …
To go from lifetimes to masses one must divide by about 2.5, so the two giant progenitors must be
within 4% of each other in mass."* The 10%, the "divide by about 2.5", and the 4% are **all the
source's own**, and 10%/2.5 = 4% is the source's own arithmetic — not a reconstruction. R2 reproduces
it (`derived threshold : 4.0% (paper: 4%) -> CHECK`).

The physical justification `τ ∝ M/L, L ∝ M³·⁵ ⇒ τ ∝ M⁻²·⁵` in the interim §1 is **auditor-supplied** —
Sec 3.2 states the factor 2.5 without deriving it. It is correct standard main-sequence physics
(d ln τ = −2.5 d ln M, so a 10% lifetime window ⇒ 10%/2.5 = 4% mass window) and the exponent equals
the source's own divisor, so it is internally consistent and faithful. The finding already flags it
as its own reasoning ("With τ ∝ M/L and L ∝ M³·⁵…"); adequately transparent.

## Check 2 — the proviso quote. **CHECK.**
`blr_physrept_clean.txt` 1139–1144, verbatim: *"During the helium burning red giant, ∼0.1 to 0.2 M⊙
can be deposited on the first born neutron star by the helium star companion, and the first born
neutron star should be that much more massive than the other, in addition to the possible ∼4%
difference in mass because they must burn helium at the same time."* The finding's quotation,
including *"in addition to"*, is accurate. The proviso is stated (1133–1134) for *"the lower mass
neutron stars in the double pulsars J0737−3039 and J1756−2251"* — exactly the two systems the finding
names. Direction: the source says the deposit lands on the **first-born** and makes it **heavier**.

## Check 3 — the channel match. **CHECK.**
`ferdman2020_clean.txt` 83, verbatim: J1913+1102 is *"part of a population of several very close DNS
binary systems … (e.g. PSRs J0737−3039A/B and J1756−2251). These imply an evolutionary path in which
the second-formed NS was born as a result of an envelope-stripped helium star progenitor…"* — BLR's
two systems, same mechanism. Line 74: *"With a spin period of 27 ms, PSR J1913+1102 was the
first-formed neutron star (NS) in this binary system; this was subsequently recycled by accretion of
matter from the [progenitor to the second NS]."* Masses (40, 80): pulsar **1.62 ± 0.03** (heavier,
first-formed), companion **1.27 ± 0.03** (second-formed). **Heavier = first-born → matches the
proviso's predicted direction.** Had the asymmetry run the other way the proviso would be
inapplicable; it does not. R3 reproduces both the channel note and the direction check.

## Check 4 — THE CRUX: is BLR's He-giant transfer one of Tauris's budgeted phases? **YES — mapping justified.**
BLR's mechanism (1140, 958) is mass transferred **onto the first-born NS by the helium-star companion
during that companion's helium-shell-burning / He-red-giant stage**. Tauris budgets exactly this
configuration: IV.2 common envelope, IV.3 *"wind accretion from the helium/Wolf-Rayet star"* in
*"NS–helium star binaries"* (1437–1448), IV.4 *"Case BB Roche-lobe overflow"* — RLO from the expanded
helium star onto the NS (1450–1463), IV.5 shell impact (≪10⁻³ M⊙, 1489). The mapping is not the
auditor's construction: Tauris states it directly at 1493–1494 — *"the HMXB donor star (the
progenitor of the second-born NS) provides the material for potential accretion onto the first-born
NS in all above-mentioned phases."* That is BLR's proviso configuration verbatim. There is **no
un-budgeted channel** by which the helium-star companion could deposit onto the first-born NS outside
Tauris's phases; IV.6 (accretion efficiency, 1491–1499) only *lowers* the accreted fraction further.
The 0.0134 M⊙ therefore does confront the proviso on its own terms. **The reversal's single
load-bearing step holds; no HOLD on this axis.**

## Check 5 — the Tauris numbers. **CHECK, with note (a).**
- CE: 1434 verbatim — *"we take ΔM_NS = 0.01 M⊙ as a reasonable estimate for the upper limit of the
  amount of mass accreted by a NS during a CE phase."* **ADOPTED**, not merely mentioned. And they do
  argue the higher figure down: 1421–1422, MacLeod & Ramirez-Ruiz's *"upper limit of ΔM_NS < 0.1 M⊙"*
  is *"an overestimate"*, with the observational argument (1426–1431) — four DNS systems whose recycled
  component is <1.38 M⊙ would need birth masses <1.28 M⊙ if they had accreted ~0.1 M⊙, *"unexpected …
  in so many systems."* All quoted accurately in the finding.
- Wind: 1447–1448 verbatim — *"ΔM_NS < 4×10⁻⁴ M⊙ when integrating throughout the wind-accretion phase
  of the NS–helium star binaries."* CHECK.
- Case BB: 1463 verbatim — *"ΔM_NS = 5×10⁻⁵ − 3×10⁻³ M⊙."* CHECK. R4 reproduces total 0.0134 M⊙ and
  the ceiling table; the σ values (21.6 / 22.8 / 5.1 / 13.9) all reproduce.

**Note (a) — "every phase at maximum / generous-to-the-source ceiling" is slightly imprecise.**
Tauris also states, 1476, that *"Case BB RLO may, in a few cases, result in accretion of up to
(6−9)×10⁻³ M⊙"* — an enhanced max above the 3×10⁻³ the receipt used — and IV.5 shell impact
(≪10⁻³) is omitted. A strictly maximal Tauris ceiling is therefore ~0.019–0.020 M⊙, not 0.0134.
Recomputing: ceiling = 0.04·1.290 + 0.020 ≈ 0.072 M⊙, excess 0.237/0.0113 ≈ **21.0σ**; overstatement
of the BLR proviso becomes ~5×–10× rather than 7×–15×. The verdict direction and the "~21σ" headline
are **unchanged**; the write-up should either cite ~0.02 M⊙ as the ceiling or note the enhanced Case
BB figure, so the "each at maximum" wording is defensible. Non-blocking.

## Check 6 — over-correction. **No over-retraction.**
The valuable observation survives intact and remains true: the He-giant caveat *is* quantified — in
BLR Phys. Rept. 462 Sec 3.2 (0.1–0.2 M⊙), a companion paper not in the lane at C08 time — contrary to
the adjudication's treatment of it as an unquantified qualifier. The SETTLED section explicitly
preserves this ("the caveat *is* quantified … at a value large enough to cut the margin to 5σ had it
stood") and reverses only the *conditional margin claim* (5.1σ), which rested entirely on BLR's
magnitude being current. Since Tauris directly rejects that magnitude with both simulation and
observation, retracting the 5.1σ is correct, not decisiveness-theatre. The author gave away nothing
valid.

## Check 7 — overclaim sweep. **Clean.**
The finding confines itself to the mass-asymmetry limb ("limb 2 still fires", "the margin", "verdict
direction"). It never states or implies CNS is falsified, and never touches black-hole-universe
cosmology. "BHU is falsified" does not appear. Consistent with the brief's standing rule.

---

## Minor notes carried to the write-up (none blocking)
- **(a)** As above: cite ~0.02 M⊙ (enhanced Case BB) as the generous ceiling, or the "each at maximum"
  phrasing overstates; conclusion (~21σ, order-of-magnitude below the proviso) is unaffected.
- **(b)** The τ∝M⁻²·⁵ justification for the divisor 2.5 is auditor-supplied, correct, and already
  labelled as reconstruction — keep it labelled.
- **(c)** The headline σ values (22.8 / 21.6 / 5.1) are driven by the **2026 A&A-update** masses
  1.599/1.290 (±0.008), a source cited as arXiv:2606.19276 but **not in the lane** →
  UNVERIFIED-AT-GATE against a primary (reason: not provided; time-boxed). It is consistent with C08's
  19.3% and with Ferdman's own 1.62/1.27. Robustness check from R3/R4: on Ferdman's own wider errors
  (±0.042) the Tauris-budget ceiling still gives ~6.7σ and bare-4% ~7.1σ — the **verdict direction is
  robust to which mass measurement is adopted**; only the numeric margin depends on it. The write-up
  should attribute the specific "21.6σ" to the A&A update rather than presenting it as
  measurement-independent.

## Verdict
The reversal correctly maps BLR's proviso onto Tauris's budgeted phases, reproduces every quoted
figure, keeps the one durable finding (the caveat is quantified in a companion paper), and neither
over-claims nor over-retracts. Receipts run clean. **PASS_P3B_TRACKB.**

— Gate B reviewer (fresh one-shot), 2026-08-21 KST. Literature hosts only; no network;
portal.nersc.gov untouched. One file written: this one.
