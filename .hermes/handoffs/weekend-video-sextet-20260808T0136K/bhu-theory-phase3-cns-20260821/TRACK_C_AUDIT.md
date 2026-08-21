# Track C — does CNS entail a low neutron-star maximum mass?

**The question, from the brief:** the 2026-08-17 adjudication said CNS "can retreat from the
Brown–Bethe EOS route, at the price of no longer being tested by this channel." Nobody had checked
whether Smolin's argument *requires* a soft equation of state, or whether the mass prediction is a
detachable rider Brown–Bethe supplied.

**The answer is neither, and the framing was wrong** — established from a preprint, so this is
context-grade rather than a verdict on the published record (§5).** CNS does not predict M_max ≈ 1.5 M⊙. It makes
a **local-maximum** claim, and the neutron-star mass enters only as a *diagnostic* of which side of a
critical parameter we sit on.

## 1. Smolin's actual argument

From Smolin, *"Using neutron stars and primordial black holes to test theories of quantum gravity"*
(astro-ph/9712189), §2 — **source status flagged hard in §5 below**:

There is a critical strange-quark mass μ_c. Below it, kaon condensation gives a low upper mass limit
(~1.5 M⊙); above it, conventional equations of state give an upper limit "almost certainly above 2".
A sufficiently heavy pulsar therefore shows μ > μ_c. Then, verbatim:

> "Furthermore, this would refute 𝒮 because it would then be the case that a decrease of μ would
> lead to a world with a lower upper mass limit for neutron stars, and therefor more black holes."

**That is the whole logic, and it is not the logic anyone in our record has been using.** CNS claims
our universe's parameters sit at a *local maximum* of black-hole production. A heavy neutron star
refutes it not because CNS predicted a light one, but because it would show that a *small decrease in
μ* would produce **more** black holes — so we are demonstrably not at a local maximum. The mass limit is a probe of the parameter space's local gradient. *(Gate C note 1: calling it
"never a prediction" overshoots — a falsifiable upper bound is a one-sided prediction in the
Popperian sense, and Smolin does offer one, at 2.5 M⊙. The correct and surviving claim is that CNS
does not predict the specific number ≈1.5 M⊙; that is Brown–Bethe's.)*

Consequences that follow immediately:

- **"CNS predicts M_max ≈ 1.5" is false.** That is Brown–Bethe's prediction. Smolin borrows their
  calculation as an instrument for reading μ against μ_c.
- The refutation inherits every assumption in "decreasing μ increases black-hole count". Smolin
  states the escape route himself, in his own footnote: the argument holds only if μ is an
  independent parameter that can be varied without disturbing star formation.

## 2. Smolin's threshold is 2.5 M⊙, not 2.0

Abstract and §5, verbatim: **"the observation of a pulsar with mass greater than 2.5 M⊙ would cleanly
refute the theory."** §2 adds a weaker form — "if one is completely confident of Bethe and Brown's
upper limit of 1.5, any value higher than this would be troubling."

Brown–Lee–Rho use "∼> 2 M⊙ … to be safe"; our own pre-registered criterion used 2.00 M⊙. **All of our
limb-1 work has been run against a threshold 0.5 M⊙ below the one the theory's author states.**

Against Smolin's number (receipt R5):

| star | mass | vs 2.5 M⊙ | class |
|---|---|---|---|
| PSR J0740+6620 | 2.08 ± 0.07 | **−6.0σ** | timing (qualifying) |
| PSR J1614−2230 | 1.928 ± 0.017 | −33.6σ | timing (qualifying) |
| PSR J0952−0607 | 2.35 ± 0.17 | −0.9σ | light-curve (excluded class) |

**Nothing reaches it.** The heaviest qualifying star sits 6σ below Smolin's clean-refutation
threshold, and even the excluded-class object falls short.

## 3. The limb that actually fired is not Smolin's test at all

Searched the full text for the double-neutron-star asymmetry criterion: **"4%" — 0 hits.
"asymmetr" — 0 hits. "double neutron" — 0 hits.** The 4% limb is entirely Brown–Lee–Rho's, derived
in Phys. Rept. 462 §3.2 from helium-burning lifetimes (Track B). It tests the Brown–Bethe formation
scenario. It is not a CNS falsifier and Smolin never proposes it.

## 4. What this does to our own record — sharpening, not reversal

The 2026-08-17 adjudication was careful and its per-link verdict survives: it said the chain is
falsified **as the source states it**, and explicitly that "CNS as a hypothesis is not thereby
refuted." That holds. What Track C adds is *why*, and it is stronger than the reason given:

- CNS is not refuted **not merely because it can retreat** from the Brown–Bethe route, but because
  **it never made the prediction that failed.** The falsified prediction is Brown–Bethe's.
- On Smolin's own stated criterion — a pulsar above 2.5 M⊙ — **CNS has not been refuted, and is not
  close.** The strongest qualifying measurement is 6σ short.
- Our lane-2 cockpit page, checked verbatim after Gate C flagged this as unverified: it says the
  chain "fails by its author's own second test" — accurate, since Brown–Lee–Rho authored that test —
  and that "Smolin's hypothesis is not refuted either — it loses its flagship falsifiable
  prediction". **That second clause is the one Track C corrects.** Smolin's flagship falsifiable
  prediction is a pulsar above 2.5 M⊙, and it has not been lost: nothing observed comes within 6σ of
  it. What was lost is Brown–Bethe's 1.5 M⊙ ceiling, which Smolin used as an instrument. The page is
  right that CNS is not refuted and wrong about what it forfeited.

## 5. Source status — the limit on how far this can be pushed

**This finding rests on a preprint.** INSPIRE confirms astro-ph/9712189 has no publication record.
Under the standing rule (peer-reviewed articles are the base layer; preprints are context, never
audit targets), Track C's conclusion is **context-grade, not base-layer**, and must not be presented
as a verdict on the published record.

The two published sources remain unobtained:

- **Smolin 1992, CQG 9, 173** (bibliography entry 6) — not on arXiv; not obtained.
- **Smolin 2004, Physica A 340, 705** — existence and pagination verified via Crossref
  (DOI 10.1016/j.physa.2004.05.021, vol 340, pp. 705–713); Elsevier paywalled, and unlike the
  Phase 2 PLB case **the INSPIRE file store holds no document for it** (checked: 0 documents).

So the honest statement is: *the argument structure recovered here is Smolin's own, in his own words,
but from a source our rules classify as context.* Confirming it against either published paper is the
outstanding acquisition, and until then B-18 stays UNVERIFIED-AT-GATE rather than resolved.

## Receipts
- **R5** (`receipts/r5_smolin_threshold.py`): measured masses against the 2.5 M⊙ and 2.0 M⊙ thresholds.

## Constraints receipt
Literature hosts only (arXiv API, ar5iv, api.crossref.org, inspirehep.net). `portal.nersc.gov`
untouched. No new observations. Lane-only writes. Nothing published, committed or uploaded.
"BHU is falsified" would be false and is not said: this concerns CNS, one branch of 28 papers.

— Tori, 2026-08-21 KST. Ungated pending Gate C.
