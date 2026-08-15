# LANA — the attenuation measurement redesigned for one human (gated amendment)

**Lana (science / claim-boundary seat), 2026-08-14.** Per Duho's standing constraint: *"only 1 human
can participate in this project… run autonomously but leveraging as many resources you can use make
it accurate as possible, and I can oversee your run."* The one human is therefore **Duho himself**
— the overseer and the checker are necessarily the same person, and the design below is built for
that fact rather than around it. **K-8 statement, explicit: no sky statistic exists anywhere in
this program, so this amendment — and this repair of it — is made at the only safe time, before the
run, and is not a post-hoc change.** Documentation only; nothing frozen, published, accepted,
committed, or pushed; Kun gates; Duho owns acceptance.

> **Revision 2 (2026-08-14) — five repairs per Kun's gate (`KUN_HC1H_GATE_20260814.md`,
> PASS WITH REQUIRED REPAIRS: "scientifically usable after repair… not INCONCLUSIVE-BY-DESIGN").
> Carried openly:** **(1)** my power break-even *"a ≥ 0.873"* was wrong — I paired the
> observed-frame A_eff with the corrected-frame σ_ours, double-counting (2a−1); the condition is
> **linear** and the break-even is **a_gate ≈ 0.7905** (Kun's number, independently confirmed by
> Hwao; adopted). The stricter 0.85 is **retained but relabelled** as what it always was — the
> original instrument-quality floor, justified on its own terms, never the HC-6 break-even.
> **(2)** the frozen *"σ_a ≈ 0.012"* promise is replaced by a **formula-only rule** (Kun's
> realistic range 0.017–0.023 cited as the worked example). **(3)** 200 synthetics support **one
> global error correction plus stratum diagnostics**, not nine independent per-stratum corrections;
> the estimator is amended accordingly. **(4)** `a` is named honestly: the **HC-1H one-human,
> synthetic-error-corrected attenuation estimate**, not equivalent to a multi-human truth
> reference. **(5)** four protocol-integrity failures become **hard INCONCLUSIVE triggers**
> (HC-7). Also added at Kun's suggestion: an optional labelled **pilot** (§2b) that can only
> return PASS-TO-FULL-HC1H or INCONCLUSIVE. No disagreement is registered on Repair 1 — the
> arithmetic was mine and it was wrong.**

> **Revision 3 (2026-08-15) — two statistical repairs per Kun's re-gate
> (`KUN_HC1H_RECONFIRM_20260814.md`, HOLD FOR TWO STATISTICAL REPAIRS; all five prior repairs
> confirmed landed; a_gate = 0.79046 independently re-derived). Both corrections verified by my own
> recomputation before applying; no disagreement registered on either.**
> **(A)** My σ_a formula kept the diagonal form after the move to a single global ε̂ — squaring
> per-stratum derivatives before summing, which treats one shared error as nine independent ones.
> With one global ε̂ the derivative must be **summed first, then squared**; for nine balanced
> strata the diagonal form understates the ε̂ contribution by exactly 9× in variance, 3× in σ —
> precision the design does not have, propagating into σ(2a−1) and both F-6 bands. Formula
> replaced in §2 and in amendment A3.
> **(B)** The pilot carry-forward as written was selection-then-reuse: the pilot passes partly on
> ε̂ < 0.10, so reusing the pilot's synthetics in the final ε̂ biases it downward — inflating `a`,
> the dangerous direction. **Fix 1 adopted:** pilot synthetics are excluded from the final ε̂
> (they remain protocol-integrity validation); pilot real and retest labels may still carry
> forward because no pilot pass criterion references their values. Principle stated in §2b: no
> datum selected on may be reused in estimating the quantity it was selected on.

> **Revision 4 (2026-08-15) — one protocol-integrity trigger added per Kun's final gate (PASS THE
> TWO STATISTICAL REPAIRS; HOLD FOR ONE REMAINING PROTOCOL-INTEGRITY REPAIR). Kun had required
> this in his earlier re-gate; it was not relayed to me then — added now, at the only safe time
> (K-8 untripped; no sky statistic exists).** HC-7 gains trigger **(v) synthetic/repeat identity
> exposure**, in Kun's wording: the blinding assumption that the checker cannot distinguish
> synthetic from real or first-showing from repeat was load-bearing but unenforced — HC-7 covered
> only key compromise and visible machine signs, and identity can leak with the key intact. The
> escape hatch is now specified rather than implied: an in-session **flag → discard → replace**
> rule, valid only before key opening and only for specific flagged items; post-key or systematic
> exposure is hard INCONCLUSIVE. Also stated in §2b per Kun: the pilot carry-forward is clean
> only under the pass rule exactly as written — a criterion referencing real-label agreement or
> retest non-flip values would exclude those labels too.

---

## 0. Verdict up front

**One human can support a valid attenuation measurement — at a defined budget, with two additions
that replace what the second and third checkers were doing, and with machine effort placed where it
is provably harmless (stratification and allocation) rather than where it is quietly poisonous
(inside the reference).** The design below ("HC-1H") measures the human reference's own error rate
without a second human — by mirrored re-presentation (our paired-flip instrument, applied to the
human) and by blind synthetic ground-truth injection — then corrects `a` for it. The brief's
central fear is upheld with a sharper argument (§1): a machine reference doesn't just inflate `a`,
it inflates it *selectively on exactly the objects where the instrument is wrong*, which is the one
failure mode that switches off HC-5's safety while looking rigorous. Machines get three bounded
roles, none inside `a`. The honest limit that remains: a single human's *stable, confident*
misreadings on real images are detectable only insofar as synthetic realism reaches them — stated
in §5, not papered over.

## 1. The reasoning tested, as instructed — and where it bends

**Upheld, with the mechanism made precise.** `a` corrects the measured amplitude via
Â_c = Â/(2a−1). An error in the reference matters differently by its correlation with instrument
error: (i) reference errors **uncorrelated** with the instrument *deflate* measured agreement —
the safe direction (power gate gets harder, HC-5 trips sooner); (ii) reference errors **correlated**
with instrument errors *inflate* `a` — the dangerous direction. Two CNNs reading arms off pixels
share failure objects (faint, blended, tight-armed, low-S/N) almost by construction, so a machine
reference concentrates its agreement precisely where the instrument is most likely wrong. That is
why "genuinely different architecture with the correlation estimated and subtracted" fails in
practice: **estimating the machine–machine error correlation itself requires truth labels**, and
obtaining them from synthetics assumes synthetic realism transfers exactly where it is least tested
— the hard real objects. Circular at the load-bearing point.

**Where it bends — three bounded machine roles that are provably harmless:**
1. **Stratifier.** A stratified estimator is unbiased for ANY stratification variable — even one
   correlated with error — provided sampling within each stratum is random and the stratum weights
   are population counts. Machine committee state (agree-confident / disagree / low-confidence) is
   therefore a *legitimate* stratification axis: it concentrates human attention where the
   information is (the brief's direction 3) **without** the selection bias, because the human also
   labels random samples of the easy strata and the estimate reweights by known counts.
2. **Allocator.** Neyman allocation (n_s ∝ N_s·√(a_s(1−a_s))) minimizes σ_a per human label —
   machines estimate the allocation from synthetics; a bad allocation costs efficiency, never
   validity.
3. **Diagnostic.** Committee disagreement rates per stratum are published beside `a` (direction 4)
   and never enter it.

## 2. The design: HC-1H (one human + unlimited machine effort)

**Human budget: 850 labeled images total** (one person, chunked ≤ 50/session, ~possible in a
weekend of sessions; instructions frozen; no instrument signs visible at any point):
- **500 real accepted-sample images** — primary reference set;
- **200 blind synthetic injections** — generator spirals rendered survey-realistic, interleaved
  unmarked; the human's absolute error rate ε̂_syn against known truth, per difficulty stratum;
- **150 blinded re-presentations** — a random 30% of the real set shown again, **mirrored**, in
  randomized later positions: a consistent labeler must flip; the non-flip rate measures
  self-inconsistency ε̂_rr (the paired-flip instrument applied to the human — this replaces the
  second checker's function of catching random individual error).

**Strata (9):** machine-committee state (3) × |χ| tertile (3); allocation by Neyman with a floor of
30 real images per stratum. The committee = two additional architectures (different family from the
primary; e.g., a deterministic geometric tracer and an independently trained CNN) used ONLY as
stratifier/diagnostic per §1.

**Blinding (carried from HC-2, extended):** every image — real, synthetic, repeat — presented in
random parity with a sealed key; the human cannot distinguish synthetic from real or first-showing
from repeat; the key opens only after all 850 labels are in.

**Estimator (Repair 3 form — one global correction, stratum diagnostics):** per stratum, raw
agreement â_s between instrument sign and the human label (de-mirrored via key). Human reference
noise is corrected **globally**: ε̂ = the overall synthetic-injection error rate (absolute,
ground-truth-anchored, ~200 trials), with ε̂_rr as the consistency cross-check. Noise-corrected
stratum attenuation: **a_s = (â_s − ε̂) / (1 − 2·ε̂)**, then a = Σ w_s·a_s with population weights
w_s. Per-stratum synthetic error rates ε̂_syn,s (~22 trials each) are **published as diagnostics
only, never as per-stratum corrections** — 200 synthetics cannot support nine independent error
rates; any stratum diagnostic incompatible with the global ε̂ at > 2σ is flagged and feeds floor 4.
**`a` is, by definition and in every artifact that cites it, the HC-1H one-human,
synthetic-error-corrected attenuation estimate — it does not claim equivalence to a multi-human
truth-reference measurement, and it carries the synthetic-realism caveat (§5.2) wherever it is
printed** (Repair 4).

**σ_a — a formula, not a promise (Repair 2; corrected for the shared ε̂ at Revision 3):** the
binding rule is that σ_a is computed from **realized** quantities only. Because ε̂ is a **single
shared quantity**, its error moves every stratum coherently — the derivative of the final weighted
estimator with respect to ε̂ is **summed first, then squared** (never square-then-sum):
> σ_a² = Σ_s w_s²·Var(â_s)/(1−2ε̂)²  +  [ Σ_s w_s·(2â_s−1)/(1−2ε̂)² ]²·Var(ε̂)  (+ covariance ≥ 0),
with Var(â_s) and Var(ε̂) as conservative binomial (Wilson) variances at the realized counts n_s and
n_syn, and w_s the realized population weights. (The earlier diagonal form
Σ w_s²·[…]·Var(ε̂) — withdrawn — treats the shared ε̂ as nine independent errors and understates its
contribution by ~9× in variance, 3× in σ, for balanced strata.) No expected value of σ_a is frozen.
*Worked example, not binding:* at the planned budget with â ≈ 0.9-class agreement the corrected
form evaluates to roughly **0.017–0.023** (Kun's independent recomputation; my earlier ≈ 0.012 was
optimistic and is withdrawn). Propagation into F-6 is unchanged in mechanism: σ(2a−1) = 2σ_a into
σ_ours and both decision regions.

**Does HC-6 still clear? (Repair 1 — corrected arithmetic, my error owned):** the detection test
runs on D̂ against its null sd σ_D, with E[D̂] = (2a−1)·0.0408/3 under Longo's amplitude. The
condition is **linear** in (2a−1):
> (2a−1)·0.0408/3 ≥ (z_α + z_pow)·σ_D → (2a−1) ≥ 0.5810 → **a_gate ≈ 0.7905**
at N = 130,076 (Kun's value, using z = 3.2905 + 1.6449 = 4.9354; the strictly one-sided F-3
convention z = 3.0902 gives 0.7787 — the more conservative 0.7905 is adopted as the frozen gate
value). My earlier "a ≥ 0.873" paired the observed-frame A_eff with the corrected-frame σ_ours,
double-counting (2a−1); it is withdrawn as a break-even. **The 0.85 instrument-quality floor is
retained on its own justification** (floor 1b below): at a < 0.85 the correction factor 1/(2a−1)
exceeds 1.43, amplifying σ and the correlated-error residual beyond what this one-human reference
can bound. The gate therefore demands measured corrected agreement **â_c ≥ 0.85 + 1.645·σ_a
(formula, evaluated at realized σ_a)** — the quality floor binds, not the power break-even.
Synthetic sign accuracy ran 100%; real-image `a` is the unknown this protocol exists to measure —
if it lands below the floor, the gate doing its job is the design working, not failing.

**The new HC-5 floors (matched to the one-human construction; Repair 1 separates the two roles the
old 0.85 was silently playing):**
1. **(a) Power break-even: a_LB ≥ a_gate(N) = 0.7905 at N = 130,076** (recomputed at freeze by the
   corrected linear rule above), with a_LB = a − 1.645·σ_a at realized σ_a — this makes HC-5 and
   HC-6 one coherent condition. **(b) Instrument-quality floor: a_LB ≥ 0.85**, retained from the
   original design **as a quality floor with its own justification** (correction-factor
   amplification 1/(2a−1) ≤ 1.43; correlated-error residual headroom for a single-human reference)
   — explicitly NOT the HC-6 break-even. (b) is stricter and therefore binds.
2. **per-stratum a_s ≥ 0.70** (carried — difficulty-correlated failure still concentrates in the
   hardest stratum and still trips locally);
3. **reference validity: ε̂ ≤ 0.05 overall** — a reference this noisy cannot anchor the correction
   (safe failure direction: uncorrected noise *deflates* a);
4. **reference consistency: ε̂_rr compatible with ε̂ (within 2σ), and no stratum diagnostic
   ε̂_syn,s incompatible with the global ε̂ at > 2σ without a recorded disposition** —
   incompatibility means the synthetic set is not measuring the real error process.
Any floor failing → INCONCLUSIVE-BY-POWER, run does not start (unchanged consequence).

**HC-7 Hard protocol-integrity triggers (Repair 5 — triggers, not warnings):** each of the
following, if it occurs, is a hard INCONCLUSIVE (the measurement is void; the run does not start,
or an already-labelled batch is discarded and the event published): **(i)** missing or
unreconstructable stratum population counts (the weights w_s cannot be formed); **(ii)** broken
random-within-stratum sampling (any non-random selection into the human's queue); **(iii)** an
unsealed, prematurely opened, or compromised blinding key; **(iv)** machine or instrument signs
visible to the checker at any point before the key opens; **(v)** synthetic/repeat identity
exposure: if the checker can identify which items are synthetic, repeated, or mirrored repeats
before key opening, the affected batch is void and the protocol returns hard INCONCLUSIVE unless
the predeclared discard/replacement rule applies. *(Added at Revision 4 per Kun's re-gate: the
blinding assumption — human cannot distinguish synthetic from real or first-showing from repeat —
was load-bearing but unenforced; identity can leak with the key intact, via visually obvious
synthetics, recognisable repeat pairs, filenames, UI state, or session ordering.)*
**Predeclared discard/replacement rule (the only escape hatch for (v)):** the labelling interface
carries a **flag** action; if the checker flags specific items as suspected-identifiable *during
the session, before key opening*, those items are discarded, the flags logged, and fresh draws
from the same stratum and category substituted before the key opens. No other path repairs an
exposure: identity leakage discovered **after** key opening, or systematic exposure (a whole
session or category recognisable), is not item-discardable and returns hard INCONCLUSIVE for the
affected batch.

**§2b Optional pilot (Kun's offer, specified so Duho can choose; it protects his weekend):**
**150 labels** — 90 real (10 per stratum), 40 blind synthetics, 20 mirrored re-presentations —
under the identical blinding and session rules. **Its only possible outcomes are
PASS-TO-FULL-HC1H** (protocol executes cleanly; session ergonomics acceptable; ε̂ crude estimate
< 0.10; no HC-7 trigger) **or INCONCLUSIVE** (stop and redesign). **It cannot produce the final
`a`, cannot feed HC-6, and cannot substitute for the full 850-label design.**
**Carry-forward (corrected at Revision 3 — the original blanket carry-forward was
selection-then-reuse bias):** the pilot's pass criterion conditions on ε̂ < 0.10, so the pilot's
**40 synthetics are excluded from the final ε̂** — reusing data selected on ε̂ to estimate ε̂
biases it downward, which inflates `a`, the dangerous direction. Those 40 remain
protocol-integrity validation only. The final ε̂ comes from the full design's **200 fresh
synthetics**, untouched by any selection. The pilot's **90 real labels and 20 retests may still
carry forward** if the pilot passes with the sealed-key chain unbroken, because no pass criterion
references their values — the selection is value-blind with respect to them. **Governing
principle, frozen: no datum that a selection decision conditioned on may be reused in estimating
the quantity it was selected on.** The carry-forward is clean **only under the pass rule exactly
as written**: if any later revision makes the pilot pass criterion reference real-label agreement
values, the 90 real labels must be excluded like the synthetics; if it references retest
non-flip values, the 20 retests must be excluded likewise. A future editor cannot loosen the
pass rule without paying that cost. If a pilot is run, it is run first; the choice is Duho's.

## 3. The four candidate directions, dispositioned

1. **Shrink the load, keep the human** — adopted and inverted: the load *rises* to 850 total
   because one person now carries the whole reference, but Neyman allocation replaces
   proportional-with-floor so every label buys maximum σ_a reduction.
2. **Test–retest** — adopted as the *noise meter*, not the reference: mirrored re-presentation
   measures self-consistency without a second human. **What it forfeits:** stable idiosyncratic
   errors (confidently repeated misreadings) that an independent second human might catch.
   **Bounded by:** the synthetic injections (absolute check against ground truth — something the
   old three-human design never had), the safe-direction argument (stable errors uncorrelated with
   the instrument deflate `a`), and floor 2 (difficulty-correlated residue trips per-stratum).
   Honest residual in §5.
3. **Machine pre-screen, human on disagreements** — adopted *as stratification only*: the human
   sees hard cases disproportionately (Neyman sends them there) but also labels random easy-stratum
   samples, and reweighting by population counts removes the bias exactly. Human-only-on-hard-cases
   without the reweighting would indeed break `a`; that version is rejected.
4. **Independent architectures as diagnostics** — adopted verbatim: published beside `a`, never
   inside it.

## 4. The preregistration amendment, line by line

*(Targets `PREREG_LONGO_AMPLITUDE_TEST_20260814_CANDIDATE.md` §5; the 08-12 record is untouched.)*

**A1 — §5 summary line.** Current:
> "HC-1…HC-3 and HC-5 carry verbatim (N_hc = 500; 9 strata; randomized-parity blinding with sealed
> key; two checkers + third adjudicator; a ≥ 0.85 overall and no stratum < 0.70, else
> INCONCLUSIVE-BY-POWER)."
Replacement:
> "HC-1…HC-6 are replaced by the one-human protocol HC-1H
> (`LANA_ONE_HUMAN_ATTENUATION_20260814.md` §2, incorporated as frozen text): one human checker
> (Duho — the project's single permitted human), 850 blinded labels (500 real, 200 blind synthetic
> ground-truth injections, 150 mirrored re-presentations), 9 strata = machine-committee state ×
> |χ| tertile with Neyman allocation (floor 30 real/stratum), machine committee as
> stratifier/allocator/diagnostic only and never inside `a`."

**A2 — HC-3 (08-12 text incorporated by reference).** Current (08-12 lines 163–164):
> "HC-3 Checkers and adjudication: two independent checkers; disagreements go to a third blind
> checker; majority label is final. Checker identities and instructions frozen with this document."
Replacement:
> "HC-3 Checker: one human (Duho). No second checker exists or is claimed. Individual random error
> is measured, not adjudicated: by the mirrored re-presentation non-flip rate (ε̂_rr) and by blind
> synthetic ground-truth injections (ε̂_syn), both under the sealed key. Instructions frozen with
> this document; sessions ≤ 50 images; instrument signs never visible to the checker."

**A3 — HC-4.** Current (candidate):
> "HC-4 (amended): …propagated as σ(2a−1) = 2σ_a into σ_ours and both F-6 decision regions.
> Hand-check publications are per-stratum aggregates only (F-10); the per-object HC table and
> sealed key are retained unpublished and hash-committed."
Replacement:
> "HC-4: per-stratum raw agreement â_s is corrected for measured reference noise by the GLOBAL
> synthetic-injection error rate ε̂, a_s = (â_s − ε̂)/(1 − 2·ε̂) (per-stratum ε̂_syn,s are
> diagnostics only, never corrections; ε̂_rr is the consistency cross-check); a = Σ w_s·a_s with
> population weights. **a is the HC-1H one-human, synthetic-error-corrected attenuation estimate;
> it does not claim equivalence to a multi-human truth-reference measurement and carries the
> synthetic-realism caveat wherever printed.** σ_a is computed by the frozen formula
> σ_a² = Σ_s w_s²·Var(â_s)/(1−2ε̂)² + [Σ_s w_s·(2â_s−1)/(1−2ε̂)²]²·Var(ε̂) (+ covariance ≥ 0)
> — the shared ε̂'s derivative summed across strata before squaring, never squared per stratum —
> at realized counts with
> conservative binomial variances — no expected width is frozen; propagated as σ(2a−1) = 2σ_a into
> σ_ours and both F-6 decision regions (bands evaluated at the corrected a, printed with
> propagated widths). Hand-check publications are per-stratum aggregates only (F-10); the
> per-object HC table, the sealed key, and the synthetic-injection manifest are retained
> unpublished and hash-committed."

**A4 — HC-5.** Current (08-12 lines 169–170, incorporated):
> "HC-5 Validity floor (frozen): a ≥ 0.85 overall, and no stratum with a_s < 0.70. Failure →
> INCONCLUSIVE-BY-POWER (instrument not accurate enough for the narrowed target), run does not
> start."
Replacement:
> "HC-5 Validity floors (frozen, matched to the one-human reference): (1a) a_LB = a − 1.645·σ_a ≥
> a_gate(N), the power-gate break-even at the actual bound N by the corrected linear rule
> (2a−1)·0.0408/3 ≥ 4.9354·σ_D — a_gate = 0.7905 at N = 130,076, recomputed at freeze; (1b) the
> instrument-quality floor a_LB ≥ 0.85, retained on its own justification (correction-factor
> amplification ≤ 1.43; one-human correlated-error headroom) and explicitly not the HC-6
> break-even — (1b) binds; (2) no stratum with a_s < 0.70; (3) global ε̂ ≤ 0.05; (4) ε̂_rr
> compatible with ε̂ within 2σ, and stratum diagnostics without unresolved > 2σ incompatibility.
> Any failure → INCONCLUSIVE-BY-POWER, run does not start. HC-7 (hard protocol-integrity
> triggers): missing stratum population counts, broken random-within-stratum sampling, an unsealed
> or compromised key, machine/instrument signs visible to the checker, or synthetic/repeat
> identity exposure — if the checker can identify which items are synthetic, repeated, or mirrored
> repeats before key opening, the affected batch is void unless the predeclared in-session
> flag-discard-replace rule applies (`LANA_ONE_HUMAN_ATTENUATION_20260814.md` §2, incorporated) —
> → hard INCONCLUSIVE; the affected measurement is void."

**A5 — HC-6.** Current final sentence (candidate):
> "This gate is re-evaluated by the same analytical method at the hand-checked a before
> unblinding; failure → INCONCLUSIVE-BY-POWER, no run."
Replacement (one clause added):
> "This gate is re-evaluated by the same analytical method at the noise-corrected, one-sided-95%
> lower-bound hand-checked a (HC-4/HC-5.1) before unblinding; failure → INCONCLUSIVE-BY-POWER, no
> run."

No other frozen line references the checker count. (F-10.i's custody seats are crew seats, not
human checkers, and are untouched.)

## 5. Honest limits (what one human cannot give, at any budget)

1. **Stable confident misreadings on real images** — the human wrong the same way twice, on object
   classes where synthetics are least faithful — are the residual blind spot. They are bounded
   (safe-direction when uncorrelated with the instrument; per-stratum floor when
   difficulty-correlated) but not eliminated. A second independent human was the only direct
   detector of this class, and the constraint removes it permanently. This limit is stated in the
   published methods, not hidden.
2. **Synthetic realism gap:** ε̂_syn measures the human against generator images; its transfer to
   real hard cases is an assumption, tested only indirectly by floor 4 (ε̂_rr consistency). The
   generator-realism caveat already frozen in BS-3 carries here.
3. **Fatigue/drift:** one person, 850 images — mitigated by session caps and by placing the
   re-presentations late (drift shows up as a rising ε̂_rr across session index; reported).
4. If Duho cannot supply ~850 labels, the fallback is fewer real labels at the cost of σ_a — the
   gate arithmetic in §2 then demands a correspondingly higher measured a. There is no valid
   zero-human variant: with no human anywhere, `a` has no reference that fails independently of
   the instrument, and the power gate would be running on self-agreement. That version is refused.

**Nothing here is frozen, published, accepted, committed, or pushed. Kun gates this amendment;
Duho owns acceptance — and, uniquely for this document, also performs the measurement it designs.**

— Lana, 2026-08-14.
