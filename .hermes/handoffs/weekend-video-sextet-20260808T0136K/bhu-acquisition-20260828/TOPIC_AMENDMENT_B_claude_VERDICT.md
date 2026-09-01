AMENDMENT_B_REFUTED

# Adversarial review — Amendment B (axis-substituted detection-class test)

Reviewer: claude seat (Opus). Date: 2026-09-01 KST. Review only; no file outside this one was
changed. Source read by targeted `grep -n` / `sed -n` extraction, never whole.

**Summary of the refutation in one paragraph.** Three of the four load-bearing claims fail on the
frozen text's own words, and each failure is independently sufficient. Claim 1 fails because this
text's *detection* criterion is itself evaluated at `a_LB` and because `β̂` sits four gates behind
`BS-8f`; there is no calibration-free path to a real-sky statistic here. Claim 4 fails because
`σ_β = 1/√N_eq` contradicts the frozen `Var(β̂) = Var_pop(s)/((N−1)·Var_pop(c))` by a factor of
√3, and the corrected arithmetic **inverts the proposal's own headline conclusion** — at the worst
axis the 3σ floor is 5.48%, above Longo's 4.08%. Claim 2 fails because §1 pre-refutes the
substitution in one sentence written and signed before this proposal existed. And the amendment
strips out the amplitude band, which was the only thing constraining the one systematic — BS-3g's
`a(c) = a₀ + γ(c − c̄)` — that the text says is still open, whose carrier it has already measured
at `corr(psfsize_r, cos θ) = +0.4188` in the analysed sample, and whose bound cannot be obtained
because the sweep "refuses until the run-time calibration artifacts exist." The amendment is not
"the surviving half"; it is the half that was protected by the half that died.

---

## Per-claim rulings

### Claim 1 — "CALIBRATION-FREE DETECTION" — **FAILS**

It fails twice, on quotation, and the second failure is structural.

**(a) This text's detection criterion is defined at `a_LB`.** §3, on the evaluation points, is
explicit and was written precisely so this could not be misread:

> "Decision bands evaluate at â / {â_b}; **the detection floor evaluates at a_LB / {a_LB_b}** —
> each evaluation point is named where it is used."

and §5 gives the floor itself:

> "**Detection floor (V3-pred F-7):** `3.09 · σ_ours(a_LB)`, printed in the results table. No Â_L
> below the evaluated floor is nameable REPRODUCED regardless of the band."

The proposal's whole thesis is that "detection" is the half that survives. In this document the
word *detection* is attached to a floor whose argument is `a_LB`, a BS-8f field. The one thing the
proposal names as calibration-free is the one thing the frozen text names as calibration-evaluated.

**(b) `β̂` on real sky is four gates behind BS-8f.** §3, the sentence immediately after the
estimand sentence the proposal quotes — same paragraph, and the proposal's quotation stops one
sentence short of it:

> "The branch predicate (after BS-8f, **before any real statistic**, explicitly tied to
> `adjudicate_path()`) first checks the calibration floor: any `a_LB_b < 0.85` emits an immediate
> pre-unblinding `INCONCLUSIVE-BY-CALIBRATION` and halts."

§4 restates it as a gate:

> "**Pre-Stage-C Calibration Gate:** Before running Stage C, the measured calibration bound must be
> checked. If any bin's `a_LB_b < 0.85`, it emits an immediate pre-unblinding
> `INCONCLUSIVE-BY-CALIBRATION` and the run halts. **Only if all bins satisfy `a_LB_b >= 0.85` may
> Stage C run.**"

and Stage C consumes the calibration directly:

> "Stage C (class E, BS-5f; after inference, before unblinding). The same frozen generator,
> addresses and pass rule, run on the sealed accepted-position mask … **with the measured a_LB
> (scalar) or {a_LB_b} (profile) from BS-8f.**"

> "FAIL → **INCONCLUSIVE-BY-POWER declared before unblinding; the run halts; no real-sky statistic
> is ever formed.**"

The §7 dependency edges close it: `BS-8f` **blocks `Stage C`**; `BS-5f` (Stage C receipt)
**blocks `BS-L`**; `BS-L` **blocks `unblinding`**; and `BS-7f` — "production permutation record:
β̂_obs, canonical 800,000-byte payload digest, p, environment" — is *post-unblinding*. So the
observed slope and its permutation p-value, the exact two quantities claim 1 says are
calibration-free, are produced **four edges downstream of the slot that stage two closed**. Not
"in principle recoverable"; unreachable by construction in this text.

**(c) Even the choice of estimator needs â.** §3: "spread `<= 0.03` selects the scalar path, and
spread failure only (`> 0.03`) selects the profile path." The spread is over `{â_b}`. With no
BS-8f there is no scalar-vs-profile determination, so there is no determinate estimator to run —
before any question of what its output means.

### Claim 2 — "AXIS SUBSTITUTION IS MINIMAL" — **FAILS**

§1's claim boundary, frozen and signed, disposes of it in one sentence:

> "This tests that published amplitude at that published axis. **It does not test A ≈ 0.02, Shamir,
> BHU, or whether the sky is isotropic. Fixed-axis.** The machine axis is the `AXIS` constant; all
> coordinate pairs are display-only."

The proposal asks for all three of the excluded things at once: it changes the axis (against
*Fixed-axis* and against `AXIS` being a constant of the frozen reference); it motivates the new
axis by BHU ("A rotating parent black hole imprints *one* preferred axis" — proposal, line 51),
which §1 names as out of scope; and it reports "whether a modulation exists", which is a test of
"whether the sky is isotropic", also named as out of scope. A referee shown that sentence beside
this proposal will not need a second argument.

"Changes `c` and nothing else" is also simply false about this document. The substitution moves:
§1 (claim boundary + the `AXIS` constant), §2.7 (the +0.4188 systematics measurement is
axis-specific — "Measured on the frozen `AXIS`"), §3 (branch predicate, detection-floor evaluation
point), §4 (the `N_eq ≥ 100,000` floor, Stage C's inputs, BS-5p's geometry), §5 (both numeric
verdicts, the detection floor, `BATTERY-NEQ`), §6.1 (the normative lifecycle table, from which
BS-8f would be deleted), and §7 (the BS-8f → Stage C, BS-3g → BS-6, BS-5f → BS-L edges). Seven
sections and four dependency edges is not the smallest possible change.

And §0's precedence rule makes the prose route unavailable regardless: the pinned code defines
every mechanism and **code beats prose**. `successor_ref_v9.py` is frozen at `6a9abbbd`; §11
records that its "`SLOT_SCHEMA` does not contain `BS-3g`, and it **cannot gain one**". A frozen
reference whose schema cannot be extended cannot execute an amended design. What the proposal
describes is therefore necessarily a **new pinned reference with a new §0** — i.e. a new study, as
the proposal's own "How it should be built" section half-concedes. Calling it an amendment
understates it by exactly the amount that matters.

Finally, §5 closes the outcome registry: "The **canonical study-run lifecycle outcome registry**
emits exactly one outcome per **run**", and its numeric members are `REPRODUCED-LONGO`,
`REJECTED-AT-LONGO-AMPLITUDE`, `INCONCLUSIVE` — all three defined through `Â_L`. **There is no
detection-class outcome in this registry.** A detection result has no name the frozen machinery is
permitted to emit.

### Claim 3 — "IT REMOVES THE EXACT BLOCKER THAT CLOSED STAGE TWO" — **FAILS**

The 38-person panel is not the blocker; it was one costed *route* to the blocker's object. The
blocker is that `a` is unmeasured. Amendment B does not measure `a` and does not remove the text's
dependence on it (claim 1 above). It **hides** the dependence by choosing a report that does not
print `Â_L`, while every gate between the mask and `β̂` still demands `a_LB`.

Worse, it does not even remove the panel from its own critical path. The proposal's precondition 2
is "Bound γ, or stop. BS-3g must be filled." §11 states what filling BS-3g requires:

> "the sweep **refuses until the run-time calibration artifacts exist**, by design."

and §7 states the consequence of not filling it:

> "or non-conforming BS-3g receipt leaves the `blocks BS-6` edge undischarged, and **BS-6 does not
> open**. There is no partial or provisional BS-3g receipt."

BS-6 is "image transport approval … blocks **first image byte**." So: no calibration → no BS-3g →
no BS-6 → no image byte. The proposal's own hardest precondition is **circular against the exact
resource stage two ruled unobtainable**, and it also blocks the 148 GB already downloading from
having any analysed use. The ruled mapping is `a(c) = a₀ + γ·(c − c̄)`; there is no `a₀` to perturb
around without BS-8f, so the sweep is parameterised by the missing quantity.

### Claim 4 — "POWER" — **FAILS** (and the corrected arithmetic reverses its conclusion)

**(a) `σ_β = 1/√N_eq` contradicts the frozen variance by √3.** §3 pins it:

> "`perm_sigma_exact()` (the EXACT permutation sd, `Var(β̂) = Var_pop(s)/((N−1)·Var_pop(c))`,
> verified against exhaustive enumeration by fixture `PERM-SIGMA-EXACT`)."

With `s ∈ {−1,+1}` so `Var_pop(s) ≈ 1`, and `N = 49,211`, `Var_pop(c) = 0.7517`:
`σ_β = 1/√(49,210 × 0.7517) = 0.005199`. The proposal uses `1/√110,983 = 0.003002`. The ratio is
exactly `√3 = 1.732`, because `N_eq = 3·N·Var(cos θ)` is a **leverage-normalised equivalent count**
(full-sky isotropic `Var(cos θ) = 1/3` ⇒ `N_eq = N`) used by the frozen text **only as a gate
threshold** — §2.3 "`N_eq = 3·L_ret ≥ 100,000` floor"; §4 "The gate is N_eq and it passes". It is
never used as an inverse variance. Repurposing it as one overstates precision by 73%.
Correct `σ_A` at `a = 0.85` is **0.00743, not 0.00429**.

**(b) The "model validation" validates nothing, and cannot.** Under the frozen variance,
`Â_L = 0.04243` at `a = 0.85` is **5.71σ**, and even at the impossible ceiling `a = 1.0` it is only
**8.16σ** — no accuracy `a ≤ 1` reproduces 9.5σ. So the *correct* formula does not match the
receipt either. That means the agreement of the *incorrect* formula with 9.5σ is a coincidence
between an error and a receipt the proposal has not reconciled (different geometry, different
injected `a`, or a different scale for `β̂` — the proposal does not know which). "Which is why I
trust the table" is the reasoning error: a numerical coincidence was used to license a formula
that contradicts the frozen definition it is supposed to implement.

**(c) The corrected table inverts the proposal's headline.** Same leverage formula, frozen
variance, `a = 0.85`:

| ψ | Var(cos θ′) | N_eq | proposal 3σ floor | **frozen-variance 3σ floor** | Longo 4.08% detectable? |
|---|---|---|---|---|---|
| 0° | 0.7517 | 110,976 | 1.29% | **2.23%** | yes |
| 30° | 0.5948 | 87,814 | 1.45% | **2.50%** | yes |
| 45° | 0.4379 | 64,652 | 1.69% | **2.92%** | yes |
| 60° | 0.2810 | 41,490 | 2.10% | **3.64%** | marginal |
| 90° | 0.1241 | 18,329 | 3.17% | **5.48%** | **NO** |

The stated conclusion — "even at the worst axis, Longo-scale (4.08%) stays detectable" — is
**false** on the study's own variance. And Shamir-scale (1–2%) is not merely "lost off-axis"; it is
below the 3σ floor at **every** angle including ψ = 0.

**(d) The frozen power floor kills the amendment at every real CMB axis — from the proposal's own
table.** §4 fixes the gate: "post-exclusion N = 49,211 Var = 0.7517 **N_eq = 110,983 floor
100,000 — PASS**". Solving `3 × 49,211 × Var(cos θ′) ≥ 100,000` needs `Var(cos θ′) ≥ 0.6774`,
which under the proposal's own leverage formula requires **ψ ≤ 20.1°**. Longo's axis is
`(l, b) = (52°, 68.5°)` (§1). Computed angles to the candidate axes the proposal names
(axis-folded to [0°, 90°]):

| CMB axis | ψ from Longo | Var(cos θ′) | N_eq | vs. floor 100,000 |
|---|---|---|---|---|
| hemispherical power asymmetry / dipole modulation (227°, −15°) | 53.6° | 0.345 | 50,960 | **FAIL (0.51×)** |
| low-ℓ quadrupole–octopole alignment (260°, 60°) | 49.9° | 0.384 | 56,748 | **FAIL (0.57×)** |
| "axis of evil" variant (240°, 63°) | 48.4° | 0.401 | 59,206 | **FAIL (0.59×)** |
| CMB kinematic dipole (264°, 48°) | 61.1° | 0.271 | 39,984 | **FAIL (0.40×)** |

Every candidate lands at ψ ≈ 48–61° and misses the frozen floor by a factor of 1.7–2.5. On the
frozen §4 gate the amendment's outcome is **`INCONCLUSIVE-BY-POWER`, declared before unblinding**,
with no statistic ever formed. The proposal's precondition 4 ("Re-derive the power gate at the new
axis; the frozen `N_eq ≥ 100,000` floor was axis-specific and does not transfer") is therefore not
a formality — it is a request to **lower a threshold after learning the existing one fails on the
new axis**. That is a post-hoc threshold change, and it is the second-worst thing a preregistration
amendment can contain after a post-hoc axis. §5's own validation battery was built to stop exactly
this run: "an under-powered geometry must yield INCONCLUSIVE-BY-POWER **derived from N_eq**, never
from a caller-supplied boolean (`BATTERY-NEQ`)."

**(e) The leverage formula's assumptions are false for this sample, in the optimistic direction.**
The algebra is right *given* its premises: writing `m̂ = cos ψ n̂ + sin ψ ê`, `cos θ′ = cos ψ·c +
sin ψ·u`, so `Var(cos θ′) = cos²ψ Var(c) + sin²ψ Var(u) + 2 cos ψ sin ψ Cov(c, u)`, and the stated
form follows only if `Cov(c,u) = 0`, `E[u]=0`, `E[u²] = (1 − E[c²])/2`, and `E[c²] = Var(c)`.
Both premises are contradicted by the frozen text:
- **`E[c] ≠ 0`.** §4: "The two-ended split moves as a fact about the sample and not a threshold
  failure: 48.0/52.0 → **40.8/59.2** because `psfsize_r` correlates with cos θ at +0.37." With
  `E[c] ≠ 0`, `E[c²] = Var(c) + E[c]² > Var(c)`, so the true transverse variance
  `(1 − E[c²])/2` is **smaller** than the formula's `(1 − Var(c))/2`. Off-axis leverage is
  overstated.
- **`Cov(c,u) ≠ 0`.** The footprint is DR10-**south**; Longo's pole is northern; the sample was
  built by a polar `|cos θ|` selection about that axis. The retained objects occupy a bounded,
  one-sided sky region — azimuthal symmetry about Longo's axis is false by construction, so the
  omitted cross-term is nonzero, is not sign-constrained, and can dominate at intermediate ψ.
  The table is therefore not a bound in either direction, only a guess.
- For a genuinely polar-selected sample the residual transverse spread is exactly the quantity the
  formula redistributes isotropically. Assigning all of it evenly to the two transverse directions
  is the most favourable assumption available, not a neutral one.

The proposal flags (e) itself as risk 3 — and then draws its conclusion from the table anyway. A
caveat that does not propagate into the conclusion is not a caveat.

**(f) The power gate is an open blocker even at ψ = 0.** §4: "**BS-5p cannot be filled until Stage
P is rerun on the actual post-exclusion mask.**" §2.6: "**STAGE P REMAINS DUAL-VALUED, AND THIS
TEXT CANNOT FIX IT** … the document still has two operative definitions and a later operator could
point at either. **No wording change closes this** … **BS-5p cannot be filled either way.**" A new
axis is a new geometry, requiring a third Stage-P rerun, on top of a blocker the frozen text
declares unclosable by text.

---

## A1 — Does the calibration floor kill a calibration-free path? Is any verdict reachable without â?

**Yes, it kills it; and no verdict is reachable without â — with one exception that is fatal
rather than helpful.**

The gate order is unambiguous: BS-8f → calibration floor check → Stage C → BS-5f → BS-L →
unblinding receipt → BS-7f (`β̂_obs`, permutation record) → BS-V (verdict). The calibration check
runs "**before any real statistic**" (§3) and its failure is a **pre-unblinding halt**. §4 states
the consequence of the power branch in the same terms: "no real-sky statistic is ever formed."

On the brief's specific sub-question — **`INCONCLUSIVE-BY-CALIBRATION` *is* reachable without â**,
and that is precisely the problem. §5 lists its producers: "Row J pre-unblinding, pre-verdict
validator post-unblinding removal, or **aggregate non-finite/degenerate failures** … validated by
`validate_calibration_aggregates` **before** the < 0.85 comparison, emitting the authenticated
aggregate outcome". A missing or non-finite calibration aggregate fires the aggregate branch before
the numeric comparison is ever attempted. Earlier still, §5 names
`INCONCLUSIVE-BY-MISSING-ALLOCATED-OUTPUT` "(produced by Row I **pre-BS-8f abort**)". So the frozen
machinery, run with no BS-8f, has exactly two reachable outcomes and both are pre-statistic halts.
**The set of verdicts reachable without â is {INCONCLUSIVE-BY-MISSING-ALLOCATED-OUTPUT,
INCONCLUSIVE-BY-CALIBRATION}, and it contains no result.** The design anticipated a missing
calibration and specified that the run stops. Amendment B's proposal is, operationally, to walk
past a halt the frozen text emits by name.

Note also §5's record of an `assert` at `v9:1622`, "the verdict path's calibration-path consistency
guard" — the frozen production verdict path carries an assertion about the calibration path. And
`run_production_verdict()` "is the **only** production path to a verdict"; the seam-free fixtures
`PROD-NO-SEAMS` / `PROD-CALLS-GUARDS` / `PROD-REFUSES` exist because two earlier gates *did*
extract a verdict by monkeypatching guards. Extracting `β̂` around the calibration gate is the same
act those fixtures were written to make impossible.

## A2 — Machine-only committee, unknown and possibly position-dependent `a`, and γ̂ unmeasured

**This is the kill shot, and it is worse than the proposal's own risk 1 admits: the amendment
deletes the one constraint that was holding this systematic down.**

**(i) The premise is not "sign-symmetric"; it is "sign-symmetric *of accuracy a*", with `a`
constant.** §3: "A sign-symmetric classifier of accuracy a gives `E[s_obs|c] = (2a−1)·A_L·c`."
Removing the humans does not remove `a` from the estimand — it removes the only measurement of it,
and it removes the only measurement of whether it is constant (the `{â_b}` spread test). The
profile path exists in this text *because the text does not assume `a` is constant*.

**(ii) Under `a(c) = a₀ + γ(c − c̄)` with any nonzero parity-odd global offset `o`, the fake slope
is exactly the statistic Amendment B proposes to report.** The centred slope acquires
`β_fake ≈ o·γ`, which is algebraically indistinguishable from a real `(2a−1)·A_L`. Under a null sky
(`A_L = 0`) the permutation reference — which reshuffles against position — calls `β_fake`
significant. §1 says this in the frozen text's own words:

> "A classifier responding to parity-odd raster artefacts, to upstream non-equivariant processing,
> or to **sensitivity that varies with position can produce a dipole-like slope under a null sky**
> … a nonzero global offset multiplied by a sky gradient in sensitivity — *'which must be bounded
> by an explicit control, not assumed away.'* **That explicit control is DESIGN, UNFILLED.**"

**(iii) The proposal's stated mitigation is pre-refuted by the same section.** Proposal risk 2
offers "mirror-involution controls on real images are already byte-exact". §1:

> "**BS-3's `antisymmetry_receipt` verifies that identity. It does not measure sky-position
> dependence and this preregistration does not claim it does** — stratifying a quantity that is
> identically zero returns zero in every bin."

The antisymmetry receipt is 1000/1000 on *synthetic* spirals and is, by the frozen text's own
statement, silent on the threat in question. It cannot substitute for γ̂.

**(iv) The carrier of the systematic has already been measured, is strong, and was made stronger by
the frozen cut.** §2.7:

> "Measured on the frozen `AXIS` with `successor_ref_v9.py`'s own `cos_theta()`:
> `corr(psfsize_r, cos θ)` is **+0.3659** in the 65,060-object parent, **+0.4188** in the 49,211
> retained … **The cut raised the seeing–position coupling in the sample that will actually be
> analysed**, by +0.0529; hemisphere contrast of the tested axis in the retained sample is
> **0.8104σ** of `psfsize_r` … **This is why the sensitivity-gradient control is a prerequisite and
> not a refinement.**"

That gradient is a *physical property of the retained sample*. Rotating the reporting axis does not
remove it; it re-projects it. And the re-projection is not benign: survey sensitivity structure
(seeing, depth, `nobs`, airmass, dust) has its **own** sky geometry — declination bands, ecliptic
and galactic structure — which has no reason to be aligned with Longo's axis. So while the *signal*
leverage falls by up to 6× off-axis, there is no argument at all that the *systematic* projection
falls with it, and it may rise. **The signal-to-systematic ratio at a CMB axis is unmeasured and
could be worse than at ψ = 0.** The proposal's power table quantifies only the numerator.

**(v) The decisive asymmetry the proposal inverts.** In the frozen design a fake `β̂` had to clear a
*two-sided amplitude band* to do damage: `REPRODUCED-LONGO` requires `p < 0.001` **AND** Longo's
sign **AND** `|Â_L − 0.0408| ≤ 3σ_comb` **AND** `Â_L ≥ the evaluated floor` (§5). A sensitivity
gradient must not merely produce a slope; it must produce a slope that lands within a few percent
of a *pre-specified published amplitude*, in a *pre-specified sign*. That is a demanding coincidence
and it is most of why the frozen design was defensible with BS-3g still open. **A detection-class
claim removes every one of those constraints.** Any nonzero `β̂` of either sign at any magnitude
becomes the reported result. Amendment B therefore does not "keep the robust half and drop the
fragile half" — it **drops the constraint that was making the design robust to its one
acknowledged open systematic and keeps the quantity that systematic directly manufactures.**

**(vi) γ̂ cannot be bounded, so the precondition cannot be met.** §11: "the sweep refuses until the
run-time calibration artifacts exist, by design." The ruled mapping is `a(c) = a₀ + γ·(c − c̄)` —
parameterised by `a₀`, a BS-8f product. The 5,049 evaluations with zero verdict flips are the
machinery's *robustness fixture with its honest fixture-scope caveat*, not a measurement of γ on
this sky; and those flips were counted against **verdicts defined by the amplitude band**, so they
carry no information at all about a detection-class decision that has no band.

**Answer to the brief's question, unqualified: no detection claim can be made while γ̂ is
unmeasured, and in this design γ̂ cannot be measured without the calibration that closed stage two.**

## A3 — Is the power arithmetic right?

No. See claim 4 above. In order of severity: `σ_β = 1/√N_eq` contradicts frozen §3 by √3 and
inflates precision 73% (a); the "model validation" is a coincidence and the corrected formula does
not reproduce the receipt at any admissible `a` (b); the corrected table reverses the proposal's
conclusion, with a 5.48% floor at ψ = 90° against Longo's 4.08% (c); every candidate CMB axis lands
at ψ ≈ 48–61°, giving `N_eq` 40,000–57,000 against the frozen floor of 100,000, so the amendment
fails §4's gate as written and the only outcome is `INCONCLUSIVE-BY-POWER` (d); and the azimuthal
and ±cos symmetry premises are both contradicted by the frozen text for this footprint, in the
optimistic direction (e). The one thing that survives is the `N_eq = 3·N·Var(cos θ)` convention
itself — correctly reproduced (`3 × 49,211 × 0.7517 = 110,976` vs. the text's 110,983) and
correctly identified as pure axis-dependent leverage. Everything built on top of it is wrong.

On azimuthal symmetry specifically: it is not "possibly unsafe", it is false by construction for
this sample — a *southern* footprint under a polar `|cos θ|` selection about a *northern* axis is
about as far from azimuthally symmetric as a survey mask gets. The proposal's own precondition 1
("measure `Var(cos θ′)` on the real mask") is the right instinct, and it is an admission that the
table it draws its conclusion from is not yet evidence.

## A4 — The integrity question

**REFUTED, and this would stand even if the arithmetic were flawless.**

A preregistration binds two distinct things: the *test* (protected against data-dependent choice)
and the *claim* (protected against outcome-dependent respecification). CMB-independence and
"before any handedness byte is read" address only the first. The second is untouched, and the
second is what happened here: **the trigger for the change was not new information about the sky;
it was the discovery that the signed claim is unobtainable.** The proposal states this itself and
does not evade it — the honesty is genuine and is why this review can be short — but honesty about
a defect is not a repair of it.

Three specific aggravations beyond the general shape:

1. **The proposal asks to relax a frozen threshold in the same breath.** Precondition 4 requests
   re-derivation of the `N_eq ≥ 100,000` floor *because the frozen floor fails at the new axis*
   (A3(d)). Choosing a new axis after the old claim died, and then lowering the power floor after
   discovering the new axis misses it, is two post-hoc moves compounding.
2. **"≤3 axes" is an uncorrected multiple comparison, and the axis set is itself a free choice.**
   The proposal's stated virtue over Longo and Shamir is that their axes "were fitted after the fact
   and the look-elsewhere effect ate the evidence". But the hemispherical power-asymmetry axis and
   the low-ℓ alignment axis are ~30–40° apart and are *different* axes; picking among the published
   CMB anomaly directions is a real degree of freedom, and no correction is specified. A capped-at-3
   family with no stated penalty is a weaker guarantee than the proposal claims for it.
3. **The surviving claim would not be publishable against the record §1 already cites.** §1 records
   the counter-anchor: Land et al. 2008, ~37,000 SDSS spirals, "consistent with statistical
   isotropy", "no significant dipole signal, and thus no evidence for overall preferred handedness",
   and that earlier studies "may also be affected and explained by a bias effect." A detection-class
   result at `N_eq` ≈ 40,000–57,000, from a machine committee of unmeasured accuracy, with an
   unbounded sensitivity gradient known to be `+0.42`-correlated with position, is exactly the
   object Land's paper says the field should stop producing.

A referee would see a post-hoc pivot. The mitigations the proposal offers are real but partial, and
they cure the smaller of the two problems.

**What the proposal gets right, and it should be said:** its own recommended construction —
"**Do not edit the signed text** … This should be a **successor preregistration that inherits**
stage one's frozen sample, instrument, and null" — is the correct shape, and the only shape in
which any version of this idea could ever be legitimate. That path is not closed by this review.
But it is a *new study* that must clear its own bar, and on the merits it fails A2 and A3
independently of any integrity concern. Fixing the integrity framing does not make it a study worth
running.

## A5 — Additional independently sufficient objections

1. **`AXIS` is a code constant of a frozen reference, and §0 makes code beat prose.** No prose
   amendment can change it; `successor_ref_v9.py` is frozen at `6a9abbbd` and §11 records that its
   `SLOT_SCHEMA` "**cannot gain**" entries. The amendment is unexecutable by the pinned reference.
2. **There is no detection-class outcome name.** §5's registry is closed and its three numeric
   members are all defined through `Â_L`. Emitting a result the registry does not contain is a
   protocol deviation, and §5's ordering rule makes a protocol deviation `VOID`, not an outcome.
3. **BS-8f is a node in a normative lifecycle table, not just a number.** §6.1 is "one lifecycle
   table, and **the table is normative**", and the one-use unblinding receipt sits downstream of
   BS-L which sits downstream of BS-5f which consumes BS-8f. Deleting BS-8f rewrites §6.1, which
   the proposal does not acknowledge.
4. **Sunk cost is doing argumentative work and should be named.** The proposal prices option (b) as
   "*Cost:* the 148 GB now downloading has no near-term scientific consumer." Giving a completed
   download a consumer is not a reason to change a signed claim. It is the reason to be most
   suspicious of the change. (And per claim 3, the amendment does not even unblock the images:
   BS-3g gates BS-6 gates the first image byte.)
5. **The instrument itself has an unclosed input path.** BS-9 ("input-path rebinding … full R1–R5
   rerun through it") blocks BS-6, and `nm_acquire_cutouts.py` "remains PROHIBITED". The amendment
   inherits this unfilled slot along with BS-3g, BS-5p, BS-2a, BS-2k, BS-2v and BS-L.
6. **The proposal's provenance section is itself a warning.** "Both failed twice … **treat claims
   1–4 as my reasoning, not as verified findings** — particularly the claim that detection is
   calibration-free, which is the one everything else rests on." That claim is the one this review
   finds false on direct quotation from the section the proposal cites. The author's own hedge was
   correctly aimed.

---

## Disposition

**AMENDMENT_B_REFUTED.** Any one of the following would be sufficient; there are five.

- Claim 1 is contradicted by §3's stated evaluation points and by §5's detection floor
  `3.09 · σ_ours(a_LB)`; `β̂` sits four dependency edges behind BS-8f, and the only outcomes
  reachable without â are two named pre-statistic halts.
- Claim 2 is contradicted by §1's frozen sentence, which names all three of the things the
  amendment proposes (a different axis, BHU, sky isotropy) as out of scope, and by §0's code-beats-
  prose rule over a frozen `AXIS` constant.
- Claim 3 is circular: its own precondition 2 requires the calibration artifacts stage two ruled
  unobtainable, and without them BS-3g blocks BS-6 blocks the first image byte.
- Claim 4's `σ_β` is wrong by √3 against frozen §3; corrected, the amendment's headline conclusion
  reverses, and every real CMB axis fails §4's `N_eq ≥ 100,000` floor by a factor of 1.7–2.5,
  yielding `INCONCLUSIVE-BY-POWER` by the frozen gate.
- The amendment removes the amplitude band, which was the only constraint restraining the one
  systematic (`a(c) = a₀ + γ(c − c̄)`) the text says is open, whose carrier it has measured at
  `+0.4188` in the analysed sample, and whose bound cannot be obtained.

**No minimum-repair set is offered, because "not refuted" was not reached.** The four claims do not
fail on presentation or on missing evidence that could be supplied; three of them fail against
quotations from the text they cite, and the fourth fails on arithmetic that reverses its own
conclusion when corrected. Repairing them would not produce a modified Amendment B — it would
produce a different proposal, on a different axis set, with a different power floor, a different
outcome registry, a different pinned reference, and a measured γ̂ that this lane has no route to.
That is a new study, and it should be argued for as one, from a blank page, with the parent's
unobtainable calibration recorded as its motivating history rather than as its inheritance.

The correct disposition of the parent remains the one already ruled on 2026-09-01: **stage one is
the deliverable.** Option (c) in the proposal's own list — "judge the axis substitution too close
to a post-hoc pivot to be worth the reputational risk, whatever its arithmetic says" — is the
answer, and this review adds that the arithmetic does not say what the proposal thinks it says
either.

---

*Verification basis. Frozen text read by targeted extraction at lines 109–136 (§1), 264–300 (§2.6),
405 (§2.7 systematics), 407–441 (§3), 441–494 (§4), 493–596 (§5), 805–812, 922, 934–956 (§7 slot
rows), 937 (BS-3g), 1558–1560, 1585 (§11). Angles computed by axis-folded dot product from §1's
`(l, b) = (52°, 68.5°)` against published CMB directions; `σ_β`, `σ_A` and the corrected floors
computed from §3's `Var(β̂) = Var_pop(s)/((N−1)·Var_pop(c))` with `N = 49,211`,
`Var_pop(c) = 0.7517`, `Var_pop(s) = 1`, `a = 0.85`. This reviewer reached the `σ_A = 0.00743`
result independently before observing that the codex seat's verdict file records the same value;
the agreement is noted as corroboration, not as its source.*
