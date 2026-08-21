# Track B, interim — the source quantifies the caveat the adjudication called unquantified

**Status: INTERIM, UNGATED.** Nothing here is load-bearing until it passes a gate. It touches a
gated artifact (`C08_MASS_ADJUDICATION_20260817.md`, `PASS_C08_ADJUDICATION`), so I am filing it as
a disclosure rather than a correction, and the verdict direction is **unchanged**.

**New source, obtained today:** Brown, Lee & Rho, *Phys. Rept.* **462** (2008) 1 — arXiv:0708.3137v2,
`sources/ar5iv_0708.3137.html` (sha256 `fc3ed8cd…`), cleaned to `sources/blr_physrept_clean.txt`.
This is `BLR-kaon07`, the paper the PRL falsifier imports links (2) and (3) from. It was never in the
lane before; the PRL audit established there was nothing in the PRL itself to re-derive.

## 1. The 4% is genuinely derived, and it is correct

§3.2: two progenitors must burn helium simultaneously to enter helium common-envelope evolution;
helium burning is ~10% of stellar lifetime; "to go from lifetimes to masses one must divide by about
2.5". With τ ∝ M/L and L ∝ M³·⁵, so τ ∝ M⁻²·⁵, a 10% lifetime window is a 10%/2.5 = **4% mass
window**. Receipt R2 reproduces it exactly. **CHECK** — and worth saying plainly, because the PRL
gave no derivation at all and this one is clean.

## 2. But the same section quantifies the "He red giant" caveat — and it is not small

The PRL's limb-2 prediction carries the parenthetical *"(modulo some small additional shift by He
red giant)"*. The 2026-08-17 adjudication treated that as an **unquantified** qualifier and argued
the verdict was invariant to it. §3.2 of the Phys. Rept. quantifies it:

> "During the helium burning red giant, ∼0.1 to 0.2 M⊙ can be deposited on the first born neutron
> star by the helium star companion, and the first born neutron star should be that much more
> massive than the other, **in addition to** the possible ∼4% difference in mass…"

0.1–0.2 M⊙ is not a small shift. Against PSR J1913+1102's Δm = 0.309 ± 0.011 M⊙, a 0.2 M⊙ deposit is
**65% of the entire observed asymmetry**.

## 3. What that does to the margin (receipt R2)

| source-predicted ceiling | value | observed Δm | exceedance |
|---|---|---|---|
| bare 4% only | 0.052 M⊙ | 0.309 ± 0.011 | **22.8σ** |
| 4% + 0.1 M⊙ deposit | 0.152 M⊙ | 0.309 ± 0.011 | **13.9σ** |
| 4% + 0.2 M⊙ deposit | 0.252 M⊙ | 0.309 ± 0.011 | **5.1σ** |

**The verdict direction survives every reading — J1913+1102 exceeds the source's own ceiling even at
maximum generosity.** What does not survive is the *margin*. The adjudication's "≈21σ on the
deciding limb" and its statement that J1913+1102's asymmetry "cannot be a 'small additional shift'
on any reading" are correct against a bare 4% and overstated against the source's own quantified
proviso: at 0.2 M⊙ the exceedance is 5.1σ, roughly a quarter of the reported figure.

## 4. The question that now decides the margin — and it is open

The proviso is not stated generically. §3.2 raises it specifically for the lower-mass neutron stars
in **J0737−3039 and J1756−2251**, where the companion passed through a helium-burning red giant and
deposited mass on the first-born. **Whether PSR J1913+1102 shares that channel is not resolved
here.** If it does, the ceiling is ~0.252 M⊙ and the exceedance is 5.1σ. If it does not, the bare 4%
applies and the adjudication's ~21σ stands. Ferdman et al. 2020 and the 2026 A&A update model that
system's formation; neither has been read for this purpose. This is the next acquisition.

## 5. Fairness to the adjudication

It reached the right verdict, on a criterion sealed before the evidence, and it **disclosed** this
caveat rather than hiding it — §4 of that document raises the He-giant qualifier unprompted and
argues around it. The gap is not diligence; it is that the qualifier's quantification lives in a
companion paper that was not in the lane. Nothing in the C08 verdict is reversed by this: limb 2
still fires. Only the confidence language needs a footnote.

## 6. Minor: which mass is the denominator

The adjudication reports 19.3% (Δm / m_heavier); Δm / m_lighter is 24.0%. "More than 4% different
from each other" does not fix the denominator. Immaterial to any verdict, noted for reproducibility.

## Receipts
- **R2** (`receipts/r2_four_percent.py`): the 10%/2.5 → 4% derivation, and the ceiling/exceedance
  table above at deposits of 0.0 / 0.1 / 0.2 M⊙.

— Tori, 2026-08-21 KST. Interim, ungated. Literature hosts only; portal.nersc.gov untouched.

---

# SETTLED (2026-08-21, same day) — and this largely REVERSES §3 above

Duho: *"read Ferdman 2020 and settle the channel question"*, then *"get Tauris 2017 and settle the
accreted mass"*. Both done. The two questions split, and the answers point opposite ways.

**Q1 — does J1913+1102 share the He-star channel the proviso is written for? YES.**
Ferdman et al. 2020 (Nature 583, 211; arXiv:2007.04175, `sources/ar5iv_2007.04175.html`,
sha256 `20278257…`) places it in a population it names as "e.g. PSRs J0737−3039A/B and
J1756−2251" — exactly BLR's two systems — with "the second-formed NS … born as a result of an
envelope-stripped helium star progenitor", and the pulsar as "the first-formed neutron star …
subsequently recycled by accretion of matter from the progenitor to the second NS". The mass
ordering matches the proviso's direction too: first-born 1.62 ± 0.03, second-formed 1.27 ± 0.03.

**Q2 — was 0.1–0.2 M⊙ actually deposited? NO. The proviso's magnitude does not survive.**
Tauris et al. 2017 (ApJ 846, 170; arXiv:1706.09438, sha256 `09c86153…`) — the DNS-formation
authority Ferdman cites — budgets it phase by phase (receipt R4):

| phase | ΔM_NS |
|---|---|
| common envelope (their adopted upper limit) | 0.01 M⊙ |
| wind accretion, NS–helium-star binaries | < 4×10⁻⁴ M⊙ |
| Case BB RLO, DNS-forming binaries | 5×10⁻⁵ – 3×10⁻³ M⊙ |
| **total, every phase at maximum** | **0.0134 M⊙** |
| generous ceiling adopted after Gate B note (a): enhanced Case BB | **~0.02 M⊙** |

They explicitly reject the higher figure: MacLeod & Ramirez-Ruiz's CE limit of < 0.1 M⊙ is "an
overestimate", and the observational argument is direct — four DNS systems have a recycled
component below 1.38 M⊙, and "if all these NSs had accreted of the order 0.1 M⊙ they would need to
have been born with a mass of M_NS < 1.28 M⊙ … unexpected for the mass of the first-born NS in so
many systems." **BLR's proviso is overstated by 7× to 15×.**

That also sources what I had flagged as my own unsupported reasoning: the pulsar's 27 ms spin marks
mild recycling, and mild recycling means little accreted mass. Tauris makes it quantitative.

**Consequence — the margin comes back, and §3 of this document is superseded:**

| ceiling | value | exceedance |
|---|---|---|
| BLR proviso at 0.2 M⊙ *(my §3 reading)* | 0.252 M⊙ | 5.1σ |
| **Tauris budget, 0.0134 M⊙** | **0.065 M⊙** | **21.6σ** |
| bare 4% | 0.052 M⊙ | 22.8σ |

**The 2026-08-17 adjudication's "≈21σ on the deciding limb" is correct** — 21.6σ on the defensible
ceiling. Its confidence language needs no correction after all.

**But its *reasoning* is still worth upgrading, and that is what this track adds.** It argued the
He-giant caveat was unquantified and the verdict invariant to it. In fact the caveat *is* quantified
— in a companion paper that was not in the lane — at a value large enough to cut the margin to 5σ
had it stood. The verdict survives not because the caveat is unquantifiable, but because the
quantification is contradicted by the modern DNS-formation literature by an order of magnitude.
That is a stronger footing, and it is checkable.

**Correcting myself plainly:** §3 above proposed 5.1σ as the honest figure. It is not. It was
conditional on BLR's 0.1–0.2 M⊙, which one paper deeper turns out to be superseded. 21.6σ stands.

## Receipts
- **R3** (`receipts/r3_channel_settled.py`): channel and mass-ordering match, both mass measurements.
- **R4** (`receipts/r4_accreted_mass.py`): the phase-by-phase accretion budget and the ceiling table.


## Gate B — PASS_P3B_TRACKB, and the three notes applied

Gate B passed the track and, on the crux, confirmed the mapping the whole reversal rests on. BLR's
proviso is mass transferred onto the first-born NS by the helium-star companion; Tauris states
directly that "the HMXB donor star (the progenitor of the second-born NS) provides the material for
potential accretion onto the first-born NS **in all above-mentioned phases**." So there is no
un-budgeted channel, and the 0.0134 M⊙ confronts the proviso on its own terms. It also confirmed I
did not over-retract: the observation that the caveat *is* quantified in a companion paper, contrary
to the adjudication's "unquantified", survives the reversal and is kept.

Three notes, all applied:

- **(a) "every phase at maximum" overstated the ceiling.** A more generous figure is ~0.02 M⊙
  (enhanced Case BB). Adopted above. It changes nothing: 21.0σ instead of 21.6σ.
- **(b) The τ ∝ M⁻²·⁵ justification for BLR's "divide by about 2.5" is mine, not theirs.** The source
  gives the divisor without the scaling. It stays labelled as reconstruction.
- **(c) The headline σ depends on which masses are used, and the tighter set is not in the lane.**
  21.6σ / 21.0σ come from the 2026 A&A update (1.599/1.290 ± 0.008), cited as arXiv:2606.19276 but
  never pinned here — **UNVERIFIED-AT-GATE**. On Ferdman 2020's own in-lane masses (1.62/1.27 ± 0.03)
  the same ceilings give **6.7σ (Tauris sum)** and **6.5σ (enhanced Case BB)**. The verdict direction
  is robust to the choice; the specific margin is not, and must be attributed rather than presented
  as measurement-independent. Pinning the A&A update is the outstanding acquisition.
