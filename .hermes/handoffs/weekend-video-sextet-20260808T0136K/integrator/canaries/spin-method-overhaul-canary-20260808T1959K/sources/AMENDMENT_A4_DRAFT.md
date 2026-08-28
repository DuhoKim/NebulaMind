# AMENDMENT A4 (DRAFT — at gate, not in force)

Target: **A3 §3's measurement scope** (T2's bias-study measurement), extended [E7]. The
earlier header named contract §2, which is not the provision T2 was performed under. Path:
contract §6[E3], **append-only**. Nothing frozen is edited.

Status: **FROZEN, IN FORCE** — gated at `KUN_A4_GATE.md` (PASS_WITH_EDITS, 7),
`KUN_A4_REGATE.md` (PASS_WITH_EDITS, 3) and `KUN_A4_GATE3.md` (**PASS**), all ten applied,
frozen 2026-08-07.

Three rounds. The first found the coordinator's INDIVIDUAL_FLIP bar mis-set so tightly that a
genuine wholesale flip would have fallen to MIXED — a mis-setting running AGAINST his own result —
while the single conjunct routing the adverse COMPOSITION branch carried no quantitative bar at
all and would have been judged post hoc by him. The second found an unbound reference-condition
choice and a Land claim smuggled back into a reading whose own §6 forbids it. The third passed.

Depends on the stack in force: contract `dc2ace67…`, A2 `2084eccf…`, A3.4 `c1ee9468…`,
A3.5 `63ee48d9…`, A3.6 `9ea8ce27…`, A3.7 `625e5e26…`, A3.8 `d2d494dd…`, A3.9 `817eec46…`.

## 1. Why this exists

`KUN_FRAME_REVIEW.md` confirmed a conflict this lane must not paper over: **Land et al. (2008)
report that the mirrored class-weights do NOT reverse, and conclude classifier bias. This lane
measured reversal at >6σ.** Same catalogue provenance, opposite answers.

The review also found the likely mechanism, in this lane's own recorded counters:

> at the 0.80 rung `mirrored_1 N_CW` (3,659) equals `monochrome N_ACW` (3,659) **to the object** —
> wholesale label-flipping among dominance-classified (visually clear) objects, exactly what
> image-following votes predict for that subpopulation, while Land's effectively-random cut
> (dominated by marginal objects, where the classifier S-preference lives) does not flip.

That is a hypothesis with a decisive test, and the test is **per-object paired counts** — which
the aggregate T2 artifact cannot supply. Two aggregate numbers agreeing in total can hide any
amount of per-object churn; only the pairing distinguishes "the same objects flipped" from "the
totals happen to match."

**Neither the frame question nor this one is resolved by argument.** A4 authorises the measurement
that would settle it.

## 2. What is authorised [A4-a]

**A per-object paired-flip measurement on payloads already fetched and pinned.** No new fetch, no
new host, no new file:

- Sources: `_gz_cache/table5.dat.gz`, `table6.dat.gz` (pinned in A3.6), and the already-cached
  `GalaxyZoo1_DR_table2.csv.gz` (contract §1). **Nothing is retrieved.**
- Matching by `objID`, as §3's pre-registration already requires.
- Output: a **McNemar-style paired contingency table** per condition pair per rung — for each
  object classified in both conditions, whether its dominant label is CW→CW, CW→ACW, ACW→CW, or
  ACW→ACW.
- **The reference conditions are named, because there are two, not one [E1]:** each mirrored set
  is paired against **`normal`** (the primary pairing, matching T3's baseline) and, separately,
  against **`monochrome`** (the control pairing, which isolates mirroring from the colour change).
  Four pairings per rung: mirrored_1×normal, mirrored_2×normal, mirrored_1×monochrome,
  mirrored_2×monochrome. "The unmirrored condition" was singular and ambiguous.
- **Which pairings the reading fires on, fixed now [E1-residual]:** the reading fires on the
  **primary pairs only — mirrored_N × normal**. The **mirrored_N × monochrome pairs are
  REPORTED, NEVER READ**: T3 carries no monochrome cell, so §4's `ΔA_T3` bar is undefined for
  them, and a bar that does not exist cannot be applied. They are published in the artifact as a
  control diagnostic and no band is computed from them.
- **Post-hoc pair selection is barred in words, not merely implied by "primary" [E1-residual]:**
  the coordinator may not, after seeing the tables, elect to read the control pairs, blend them,
  or substitute them for a primary pair that returned an adverse band. If the primary and control
  pairs disagree in the *direction* of their flip counts, that disagreement is **recorded as a
  finding** and the primary reading still stands as computed — it is not resolved by preference.
- Reported alongside: how many objects are classified in one condition but not the other, and how
  many in neither. **Unpaired objects are reported, never silently dropped** — the same rule §3
  [E4] applies to coverage.

## 3. What this measures, and what it cannot [A4-b]

- **It measures:** whether the aggregate reversal is carried by objects individually changing
  label, or by composition change (different objects passing the cut in each condition).
- **It does NOT measure:** the frame. A paired flip is equally consistent with as-seen storage of
  a genuine image flip and with de-mirrored storage of a classifier preference. **A4 cannot
  resolve FRAME_UNSTATED and does not claim to** — the frame is a fact about the archive's
  records, not about the numbers.
- **It does NOT re-measure T2.** T2's counts stand; this is a new quantity on the same rows.
- **It does NOT reconcile with Land by itself.** Land's estimator is unweighted class-weight
  averages on a differently-weighted subsample. Whether a paired result explains his null is a
  further step and is not authorised here.

## 4. Pre-registered readings, written before the measurement runs [A4-c]

Let `b` = objects CW in the reference condition and ACW in the mirrored one, `c` = the reverse,
`n_pair` = objects classified in both, `f = (b+c)/n_pair` the flip fraction, and
`r = min(b,c)/max(b,c)` the imbalance.

**The paired swing and its proper error, pinned before the run [E3]:**

    ΔA_paired = 2(c − b) / n_pair
    SE_paired = 2·sqrt(b + c) / n_pair        (McNemar; exact, not the conservative quadrature)

The paired table makes the true paired SE estimable **for the first time in this lane** — A3 §3
[ED(i)] was forced onto independent quadrature precisely because the covariance could not be
estimated from aggregate counters. Nothing here revises T3's σ; it applies to A4's own quantity.

- **COMPOSITION** — the flip is not carried by individuals: `f < 0.25` **AND**
  **`|ΔA_paired| < 0.5 × ΔA_T3` or `|ΔA_paired| < 2·SE_paired`, whichever is the weaker
  requirement** [E3], where `ΔA_T3` is the swing already recorded in T3 for that mirror-set × rung
  cell (0.107–0.112). *The earlier draft left "not reproduced" with no quantitative bar — so the
  single decision routing COMPOSITION versus MIXED would have been judged post hoc by the
  coordinator, whose interest in avoiding COMPOSITION is recorded in this very section. That was
  the one motivated-direction hole in the amendment and it is now closed with a number.*
  Reading: **the lane's >6σ reversal is substantially a selection effect of the dominance cut**,
  and T3's reading must carry that finding in every artifact. [E5] No statement about Land follows
  — §6 forbids Land-comparative phrasing whatever A4 returns, and §3 disclaims reconciliation;
  Land's null is left to the further gated step §3 names.
- **INDIVIDUAL_FLIP** — the flip is carried by individuals: `f > 0.60` **AND `r < 0.90`** [E4].
  *Re-derived from this lane's own arithmetic rather than guessed: since ΔA_paired = 2f(1−r)/(1+r),
  reproducing T3's recorded ΔA ≈ 0.107–0.112 requires r ≈ 0.83 at f = 0.60 and r ≈ 0.89 at f = 1.0.
  The earlier bar of r < 0.5 fires only when the paired swing overshoots the recorded aggregate
  roughly fourfold — so a genuine wholesale individual flip would have fallen to MIXED. That
  mis-setting ran AGAINST the coordinator's own result; it is corrected in the direction the
  arithmetic dictates, not the direction that favours him.*
  Reading: objects genuinely change label under mirroring in this subpopulation. **This does NOT
  vindicate the gloss** — it is consistent with either frame — and no Land-comparative phrasing
  becomes available.
- **MIXED** — anything else, including the intermediate band. Reading: both mechanisms
  contribute, quantified, no single-cause claim permitted.
- **UNEVALUABLE** — `n_pair` too small at a rung (< 500), or the objID sets do not support pairing.
  No reading at that cell. **[E6, extended to every axis] If ANY required cell — rung, mirror set,
  or reference pairing — is UNEVALUABLE while its counterpart returns a band, the lane's reading is
  UNEVALUABLE: not that band, and not MIXED.** A data-less cell is an absence of evidence on
  whichever axis it sits, and calling it "disagreement" would launder it into evidence that both
  mechanisms contribute. Every required cell must return a band before any band issues.

A reading issues only if **both rungs agree** (A3 §3 [ED(ii)]) **and both mirror sets agree in
band, not merely in direction** [E2, importing A3 §3 [E3]]. Either disagreement is MIXED. The
mirror sets share one payload, so their agreement is a consistency check, not independent
confirmation — the same conditionality A3.8 attached to T3 applies here.

**Recorded asymmetry:** COMPOSITION is adverse to this lane's headline result — it would say the
>6σ reversal is substantially an artefact of which objects the cut admits. INDIVIDUAL_FLIP is
non-adverse. The thresholds above are set **before** the measurement, and the coordinator's
interest is stated so it cannot be characterised afterwards.

## 5. Protocol

- Reviewed-script protocol in full: a new script, gated before execution, tag bumped as the final
  act, chain-pinned. **A3.8 and A3.9 join `PINS` at this micro-delta** [A3.5 §4], as both freeze
  records require.
- A3.8's verdict-record review applies unchanged to A4's reading: reviewer fixed by rule and named
  before the run, order ledgered, branch quoting the artifact, silence is REVIEW_INCOMPLETE.
- The measurement runs only after its script clears review. Nothing about this amendment
  authorises running anything today.

## 6. What this amendment does NOT do

- Does not fetch, does not widen the host or file enumeration, does not touch a pin.
- Does not edit or re-hash any frozen artifact, including T2 and T3.
- Does not lift the standing prohibition: while FRAME_UNSTATED stands, **no Land-comparative
  phrasing in any artifact, paper, video, dashboard or summary**, whatever A4 returns.
- Does not close the coverage shortfall, the two-rung ladder, the self-anchored pins, or the
  partial mirror-set independence.
- **Does not transport [E7-residual].** Nothing in A4 feeds the science ladder, the [E11] primary
  endpoint, or D3. A4 measures the *instrument's* bias-study sample and stays there. Any transport
  of an A4-derived correction to the science sample is a further gated step under A3 §4 — a
  measurement of the instrument is not a correction to the sky.
