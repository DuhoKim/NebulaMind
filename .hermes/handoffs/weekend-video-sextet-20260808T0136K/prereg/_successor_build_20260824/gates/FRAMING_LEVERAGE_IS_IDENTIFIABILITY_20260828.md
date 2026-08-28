# The leverage choice is load-bearing. The document justifies it in the wrong currency.

**Duho, reviewing a conference abstract:** *"isn't it how you subsample it? and is the number of
sample our bottleneck? i don't think how to subsample it is that significantly meaningful
scientifically."*

**He is right that counting statistics are not the bottleneck, and right that the framing is off.
He is not right that the subsampling is scientifically insignificant — but the document gives him
every reason to think so.**

## 1. Counting statistics are not binding. Blanc's arithmetic holds.

Longo: `A = −0.0408 ± 0.011` from 15,158 spirals. Scaling `σ ∝ 1/√N_eff`:

    N_eq = 110,983        σ ≈ 0.0041   → a Longo-level signal is 10.0σ
    at 50% of N_eq        σ ≈ 0.0058   →  7.1σ
    at 25% of N_eq        σ ≈ 0.0081   →  5.0σ
    at 10% of N_eq        σ ≈ 0.0129   →  3.2σ

**A quarter of the sample would settle it.** Nothing about this study is limited by how many galaxies
it has.

## 2. But Var(cos θ) is not a sample-size quantity. It is an identifiability quantity.

For a linear fit `y = a + b·x`, `Var(b̂) = σ²/(N·Var(x))`. **`N·Var(x)` is the slope information.**

The estimator fits handedness sign against `cos θ`. Two things can produce an excess of one
handedness:

- a **true dipole** — the slope `b` — which **flips sign across the axis**;
- a **flat classification bias** — the intercept `a` — which does **not**.

**When `Var(cos θ)` is small, `a` and `b` are degenerate.** A sample bunched at one end cannot
distinguish "the universe has a handedness dipole" from "the classifier prefers S-shapes". That is
not an efficiency problem. It is the difference between a measurement and an artefact.

Blanc's instinct — that placing objects at both ends breaks the dipole/monopole degeneracy — is
**correct**, and it is **not a separate argument**. It is the physical meaning of `Var(cos θ)`, the
quantity already frozen in `N_eq = 3·N·Var(c)`. Nothing needs inventing; the document already
computes the right number and describes it as the wrong thing.

    predecessor  Var 0.058   →  slope information  1×
    successor    Var 0.7517  →                    13.0×
    isotropic    Var 1/3     →  successor is 2.26× an isotropic footprint

## 3. So the write-up is mis-framed, and Duho found it

§4 and BS-5f present `N_eq` as **effective sample size** — a counting-statistics currency, in which
the study is already rich, which is exactly why the design reads as an optimisation. Its actual role
is **separating a dipole from a constant bias**, a systematics currency, in which the study is not
rich at all.

**Recommended:** state `Var(cos θ)`'s role as identifiability where `N_eq` is introduced. This is an
interpretation of an existing frozen quantity, not a new claim, and needs no threshold change.

## 4. The predecessor's decline is weaker than stated — and should be restated, not reopened

    predecessor  N = 208,407  Var = 0.058  →  N_eq = 36,263   (floor 100,000)
    predecessor  σ ≈ 0.0071                →  a Longo-level signal is 5.7σ

**"It could not have detected the signal" is false.** At 36,263 it would have been a 5.7σ statistical
detection. What is true is that it carried **13× less slope information**, so it could far less
readily separate a real dipole from a flat classification bias — and a 5.7σ result that cannot be
distinguished from a classifier artefact is not worth having.

**That is a better ground for the decline than the one recorded, and it does not reopen it.** The
decline is signed and stands. But if the stated reason is repeated as "insufficient sample leverage",
someone will eventually check the arithmetic and find 5.7σ.

## 5. The awkward shape Blanc names, which is the real bottleneck

**The design selects ON position. The property the estimator needs is independence conditional ON
position.** V29 §2.7 line 378 records that as **not established**, and both seats verified that
wording.

Choosing the footprint for leverage does not address that and plausibly sharpens it: the more the
sample is structured by position, the more any position-correlated selection effect can imitate the
signal. `corr(psfsize_r, cos θ) = +0.3659` is not decoration — it is the same axis.

**The bottleneck is not how many galaxies, nor how they are spread. It is whether anything that
varies with position on the tested axis can imitate a dipole.** That is where the study's risk lives
and where its defence should be built.

## What this changes

Nothing frozen. No threshold, no receipt, no slot. It is a framing correction to §4/BS-5f's
description of `N_eq`, plus a more defensible statement of why the predecessor was declined.

**Not done here, and Duho's to decide:** whether to record the restated decline ground against the
signed decision, and whether the conditional-independence gap should now be attacked directly rather
than carried as a stated assumption.
