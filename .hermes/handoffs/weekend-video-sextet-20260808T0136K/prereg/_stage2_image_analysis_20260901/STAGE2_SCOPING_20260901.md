# STAGE-TWO SCOPING — the image-analysis preregistration

**Opened 2026-09-01 on the principal's direction** ("START THE STAGE-TWO
SUCCESSOR PREREGISTRATION", human direction #30), immediately after stage one
banked clean at its pre-image boundary (`_successor_build_20260824/run/
STAGE_ONE_TERMINAL_20260901.md`).

**Build dir:** `prereg/_stage2_image_analysis_20260901/`

## 1. What stage two is for

Stage one froze and validated the **pre-image** half — sampling, instrument
identity, robustness machinery — and deliberately left the **image-analysis
design** as DESIGN/UNFILLED. Stage two preregisters exactly that, carried
through to the actual handedness-dipole estimator and result:

- **BS-2a** — the acceptance / exclusion predicate on cutouts.
- **BS-9** — input-path rebinding onto real DESI Legacy cutouts, plus the R1–R5
  machinery that is **absent from the stage-one reference entirely**.
- **BS-8p** — the hand-check allocation over the realized strata.
- …through to **the estimator and the verdict** (the science stage one exists to
  make possible: the handedness dipole and its adjudication).

**Stage one is NOT re-litigated.** It is the foundation and it is frozen.

## 2. What stage two INHERITS FROZEN (do not redesign, do not re-measure)

From the P0-signed package (manifest `d1be4a3b…`, signature verified three ways):

- **v9** at `6a9abbbd…` — the frozen reference: permutation record, adjudication,
  `calibration_bins`, `allocate_handcheck`, the receipt discipline, the frozen
  constants (N_CAL_BINS 3, N_HC_STRATA 9, floors 10/30, HC_REAL_LABELS 500,
  N_PERM 100,000, τ, A_LONGO).
- **The sample**: Branch B (DR10.1), the 49,211-object authenticated mask,
  6,104 bricks, the traversal/plan/selection receipts (BS-2o/5p/2s), the
  universe pins (`863e5ded…`, 366,912 bricks, 832,393 total).
- **Measured green results**: Stage-P 984/1000 and re-pass 996/1000; instrument
  antisymmetry 1000/1000 PASS; the synthetic sign anchor PASS; the 5,049-cell
  machinery robustness rehearsal (zero flips, with its honest fixture-scope
  caveat).
- **Instrument identity**: weights `83008c1c…`, τ = 4.4006456017494235.
- **The thirteen pinned tools** (decoder, enumeration verifier, replay harness,
  count-oracle harness, terminal-review machinery, stratum pair, BS-2f boundary
  verifier, void converter, …) and the **three blind commitments** (draw
  mechanics, mapping conventions, BS-2k constants).
- **The ruling record**: γ Γ=0.25, terminal signature, map widening,
  exhaustion→ABSTAIN, stopping rule, FORM freeze-with-disclosure, mapping
  architecture + confirmation, BS-1 early resolution, the BS-6 cycle ruling
  (whose relocated real BS-3g sweep is stage two's to run once BS-8f exists),
  and this stage-one terminal.

## 3. What is NEWLY OPEN (stage two's actual design work)

Enumerated so nothing is smuggled in later as "obvious":

**A. Acceptance / exclusion (BS-2a)**
1. The exclusion predicate on cutouts beyond the frozen catalogue thresholds —
   what disqualifies a rendered cutout (artifacts, blends, edge/coverage, source
   confusion)?
2. Its evidence schema and ledger schema (what is recorded per object, per
   decision).
3. `verify_cutout_integrity` (Row C2) — the integrity check's definition.
4. Confidence threshold, retry semantics, failure semantics.
5. Adversarial producer fixtures under transformed cutouts (the frozen row
   demands them; they need cutouts, hence stage two).

**B. Input-path rebinding (BS-9)**
6. The production single-band HDU/plane input function: source array shape,
   dtype, normalization, channel ordering, tensor layout into the frozen
   instrument.
7. **R1–R5**: the five checks are NAMED in stage one's schema but their
   definitions do not exist — stage two must define and implement them.
8. The gated replacement runner (the predecessor's acquisition code is expressly
   prohibited — a new one is required).
9. Cutout geometry: pixel scale 0.262"/px is frozen; the cutout size, centering,
   and rotation convention are open.

**C. Hand-check protocol (BS-8p, Rows G/H)**
10. The allocation over realized 3×9 cells (the method is frozen —
    `allocate_handcheck`; the realized cells come from the stratum artifact).
11. The BS-SI stratum-index schema (SCHEMA-PENDING in stage one, fills at P2–P3).
12. The committee protocol details stage one carried by quotation only:
    the rendering surface, R_max = 2 padding behavior in practice, the sealed
    interface, ABSTAIN handling, checker instructions.

**D. The estimator and verdict (the science)**
13. The handedness-dipole estimator's exact form on the labeled/instrument
    output — stage one froze `perm_record`/adjudication and the A_LONGO
    comparison; stage two must state precisely what quantity is estimated and how
    the hand-check calibration enters (BS-8f's `a = (raw − ε)/(1 − 2ε)` family is
    inherited; its application is stage two's to specify).
14. The pre-unblinding lock content and the unblinding sequence for THIS stage.
15. What constitutes the result, and the failure/inconclusive branches.

**E. Process**
16. Does stage two get its own freeze signature (P0′) and its own gate ladder?
    (Recommended: yes — same discipline, its own manifest and signature.)
17. Does the relocated real BS-3g sweep run under stage two's freeze, per the
    stage-one BS-6 cycle ruling? (Recommended: yes — it needs BS-8f, which is
    stage two's.)

## 4. THE CHOICES THAT ARE DUHO'S TO RULE

Surfaced through Blanc as each arises, exactly like stage one's rulings — with
options, plain words, and a recommendation:

- **R1 — the estimator form** (item 13): what quantity, how calibration enters,
  what the verdict thresholds are.
- **R2 — acceptance thresholds** (items 1, 4): what disqualifies a cutout and
  how strict; the confidence threshold.
- **R3 — the hand-check protocol** (items 10–12): committee composition
  (himself alone, as stage one's rosters? more?), the rendering surface, checker
  instructions, ABSTAIN policy.
- **R4 — cutout geometry** (item 9): size/centering/rotation convention.
- **R5 — scope of stage two's freeze** (items 16–17): its own P0′ and ladder;
  whether BS-3g rides stage two.

Nothing in section 3 is decided by me alone where it bears on the science: the
stage-one pattern holds — blind commitments where a value must be picked before
data, and the principal rules anything that shapes the result.

## 5. Method and pacing (burn-honest)

**Fable is at 98% weekly, resetting Friday 2026-09-05 (~4 days).** The stage-one
author+referee grind consumed the bulk of this week's Fable and **cannot be
repeated on the ~2% remaining.** Therefore:

- **Now (Fable-minimal):** this scoping doc; the ruling-question list; dispatch.
- **Heavy work on seats:** codex/agy/kimi draft, referee, and build. Fable is
  coordination, judgment on verdicts, and the principal's rulings only.
- **The Fable-heavy grind (author↔referee convergence rounds, the way stage one
  was written) PACES AGAINST THE FRIDAY RESET** — the real drafting begins in
  earnest after the reset unless the principal directs otherwise.
- **If a stage-two step would blow the ceiling, I stop and say so** rather than
  degrade quality silently. Per the principal's instruction, Hwao's Fable is
  protected last; Tori's sweep pauses first — that is his call to make, not
  mine, and I will surface the tradeoff rather than assume it.

## 6. Immediate next steps (seat work, no Fable grind)

1. **codex**: inventory what real DESI Legacy cutout access actually requires
   (endpoints, formats, the coadd tree for Branch B DR10.1, byte ceilings) —
   READ-ONLY reconnaissance, no transport, so BS-9's design starts from facts.
2. **codex**: draft the R1–R5 candidate definitions from what the stage-one text
   says they must accomplish (the five checks' *purpose* is inferable even where
   their definitions are absent) — as a proposal for referee, not a fill.
3. **agy**: adversarially review this scoping doc — what design question is
   missing from section 3 that stage two will need and would otherwise smuggle
   in later?
4. **Hwao**: assemble R1–R5 (the principal's ruling questions) into a plain-words
   decision packet as each becomes ripe.
