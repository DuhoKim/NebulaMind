# STAGE-TWO SCOPING — the image-analysis preregistration

> **v2, CORRECTED after AGY-SCOPING-REVIEW-V1 (DEFECTIVE, 19).** My v1 asked the
> principal to rule on matters stage one already froze, and omitted mandatory
> design obligations from six covenant rows. Both corrections are applied below;
> the review is the authority on what was wrong. Verified verbatim from the
> frozen bytes before correcting: the estimator IS frozen (`Â_L = β̂/(2â−1)`
> scalar, `Â_L = β̂/ŵ` profile) and the pre-lock exclusion list IS closed to
> three reasons — "No other reason is admissible. A reason not on this list
> requires a new text."

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

**A′. Row-derived obligations agy found missing from v1 (all newly open)**
18. **Row C** — the cutout-completion receipt's definition/schema.
19. **Row C2** — the hermetic worker, capability allowlist and blindness fixture;
    the acceptance-evidence projection schema; the exact-parent
    stage-completion artifact schema.
20. **Row D** — the per-object χ-bearing measurement receipt schema.
21. **Row D2 / BS-SI** — the TWO committee architectures, the machine-committee
    state logic, and the independent verifier that recomputes the index from Row
    D receipts and refuses mismatch. (agy: "catastrophically omitted" in v1.)
22. **Row H** — the χ-bearing label-set receipt schema and the label-set store.
23. **BS-2a / BS-9** — their SLOT_SCHEMA entries and canonical receipt field
    definitions (stage one has the names, not the schemas).

**E. Process**
16. Does stage two get its own freeze signature (P0′) and its own gate ladder?
    (Recommended: yes — same discipline, its own manifest and signature.)
17. Does the relocated real BS-3g sweep run under stage two's freeze, per the
    stage-one BS-6 cycle ruling? (Recommended: yes — it needs BS-8f, which is
    stage two's.)

## 4. THE CHOICES THAT ARE DUHO'S TO RULE — CORRECTED

agy struck four of my five v1 questions as already-frozen or already-ruled, and
it was right (verified against the bytes). What survives, plus what the
reconnaissance surfaced:

- **R-A — RULED 2026-09-01 (direction #31), verbatim: "Path 2 — NERSC coadd
  bricks (Recommended)".** Stage two acquires imagery from the **NERSC coadd
  brick tree** (`portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/coadd/
  <AAA>/<brick>/legacysurvey-<brick>-image-r.fits.fz`): whole survey tiles are
  pulled and cutouts are cut **locally**, so the lane holds the actual DESI
  bricks — self-contained, durable provenance, with the per-brick SHA-256 lists
  as native integrity anchors and the frozen neighbor-brick closure rule already
  in force. The ~148 GB volume is accepted over the lighter cutout-service path.
  **Consequences for the design: R-B and R-C now design against Path 2
  specifically** — the local cutter is stage two's own producer (the predecessor
  runner stays prohibited), the byte ceiling covers brick transport plus
  retained cutouts, and the manifest carries one row per masked object plus a
  separate source-brick table so shared brick hashes are unambiguous. **No real
  image byte is touched until R-C is separately authorized.**
  *(superseded question, kept for the record:)* — **the image ACCESS PATH.** Path 1 (Legacy Survey viewer `fits-cutout`,
  coordinate-native, server-side cutouts) vs Path 2 (NERSC coadd tree,
  brick-native, whole tile-compressed FITS cut locally). Genuinely open, bears
  on provenance/verifiability/volume (~1–13 GB by cutout size vs ~148 GB
  predecessor-scale full-brick), and no published rate limit exists for Path 1
  — 49,211 requests need a preregistered pace. **His call.**
- **R-B — cutout GEOMETRY.** Size (px), centering/rounding, orientation, and
  the resampling prohibition-or-kernel. Frozen: 0.262″/px only. **His call.**
- **R-C — the AUTHORIZED PROBE.** The FITS HDU/dtype/WCS/edge contract cannot
  be known from documentation; pinning it requires touching real image bytes
  ONCE, under an authorization that stage one's boundary reserves to him.
  **His call** (and it is the gate that unblocks BS-9's design).
- **R-D — hand-check committee COMPOSITION and rendering surface** (Row G):
  who checks, and what they see. NOT the ABSTAIN policy — already ruled
  2026-08-30.
- **R-E — stage two's own freeze scope**: its own P0′ signature and gate
  ladder. (Recommended: yes.)

**Struck from v1 as already settled — do NOT re-ask:** the estimator form and
calibration entry (frozen: `Â_L = β̂/(2â−1)` / `β̂/ŵ`); the verdict thresholds
and calibration floor (frozen: `a_LB_b < 0.85`, Row J); the acceptance/exclusion
REASONS (frozen closed list of three; "No other reason is admissible" — what
stage two designs is the *machinery* implementing them, not the list); the
ABSTAIN policy (ruled); BS-3g's sequence (ruled — it runs in stage two once
BS-8f exists).

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

1. **codex**: DONE — `CODEX_CUTOUT_RECON_20260901.md`, documentation-only, NO
   image byte touched (agy's sequencing finding is satisfied by construction:
   the boundary was in the dispatch and the report states no cutout was
   requested and no FITS opened). Anything further that would need real bytes
   is R-C, the principal's authorized probe.
2. **codex**: draft the R1–R5 candidate definitions from what the stage-one text
   says they must accomplish (the five checks' *purpose* is inferable even where
   their definitions are absent) — as a proposal for referee, not a fill.
3. **agy**: adversarially review this scoping doc — what design question is
   missing from section 3 that stage two will need and would otherwise smuggle
   in later?
4. **Hwao**: assemble R1–R5 (the principal's ruling questions) into a plain-words
   decision packet as each becomes ripe.
