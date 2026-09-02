# CODEX — STAGE-TWO REOPEN ANALYSIS (2026-09-02)

## BOTTOM LINE

**No: local possession of all 12,117 bricks does not reopen the frozen science.** It removes the transport/data-access risk and makes a future image run operationally possible, but the frozen design still requires a realised human hand-check calibration aggregate (BS-8f), tests every per-bin lower bound before Stage C and before any real statistic, and halts with `INCONCLUSIVE-BY-CALIBRATION` if any bound is below 0.85. The text gives no calibrated-statistic, raw-null, or existence-only escape branch. The principal's reading of frozen line 417 is correct.

One factual premise of the closure is overturned: GZ1 does **not** lack overlap with this DR10-south retained mask. I measured 16,604 of the 49,211 mask rows within 1.0 arcsec of an official GZ1 Table 2/3 object (16,600 unique GZ1 objects). Of those rows, 13,347 have a nonzero CW or ACW vote fraction, 1,040 have `P_CW + P_ACW > 0.5`, and 363 have `P_CW >= 0.8` or `P_ACW >= 0.8`. That is real coverage, not an estimate. It still does not satisfy the frozen calibration route: the frozen actors, allocation, labels, ingestion, estimator, and BS-8f producer are the hand-check protocol, with no external-catalogue substitution. The new pixels could support a scientifically sensible *new* empirical sign-mapping study, but that study is not an admissible operation or calibration source under this frozen text. Verdict: **DOES-NOT-REOPEN**.

## Q1. What is `â` actually required for?

### Governing order

The ordering is unambiguous.

> **FT-01 — lines 416–417:** “**Estimand.** A sign-symmetric classifier of accuracy a gives `E[s_obs|c] = (2a−1)·A_L·c`.  
> Scalar path: `Â_L = β̂/(2â−1)`. Profile path (frozen fallback, §6): `Â_L = β̂/ŵ` with `w_profile()` under **unit weight per accepted object**. The branch predicate (after BS-8f, before any real statistic, explicitly tied to `adjudicate_path()`) first checks the calibration floor: any `a_LB_b < 0.85` emits an immediate pre-unblinding `INCONCLUSIVE-BY-CALIBRATION` and halts. Only on the complement does the spread test apply: spread `<= 0.03` selects the scalar path, and spread failure only (`> 0.03`) selects the profile path. Profile is not a failure.”

The same requirement is independently restated at the Stage-C boundary:

> **FT-02 — lines 477–482:** “**Pre-Stage-C Calibration Gate:** Before running Stage C, the measured calibration bound must be checked. If any bin's `a_LB_b < 0.85`, it emits an immediate pre-unblinding `INCONCLUSIVE-BY-CALIBRATION` and the run halts. Only if all bins satisfy `a_LB_b >= 0.85` may Stage C run.  
> **Stage C (class E, BS-5f; after inference, before unblinding).** The same frozen generator, addresses and pass rule, run on the **sealed accepted-position mask** (BS-2f: brickid, objid, position, acceptance flag, calibration-bin label — never a χ sign), with the measured a_LB (scalar) or {a_LB_b} (profile) from BS-8f.”

Thus line 417 is correctly read: the floor precedes both scalar/profile selection and every real statistic. No null statistic is emitted on the failing branch.

### Exhaustive frozen consumers

“Amplitude” below means load-bearing for estimating or adjudicating the Longo amplitude. “Null/existence” means load-bearing for whether the frozen real-sky permutation/null statistic may exist or be emitted. A consumer can be both.

| Frozen consumer | Exact role | Amplitude | Null / existence | Neither |
|---|---|:---:|:---:|:---:|
| BS-8f aggregate | Produces `â`, per-bin accuracies/lower bounds, error term, and covariance from the hand check. | yes | yes, because all later real-statistic access is gated on it | no |
| Calibration-floor halt | Tests every `a_LB_b` before branch selection and Stage C. | yes | yes | no |
| Scalar/profile adjudication | Accuracy spread selects scalar versus profile; profile uses the per-bin response profile. | yes | indirectly, only after the floor admits the run | no |
| Point estimate | Scalar divides `β̂` by `2â−1`; profile divides by `ŵ`. | yes | no algebraic need, but unreachable without gate PASS | no |
| Uncertainty and covariance | Propagates `σ_a`/full `Cov_a`, including the shared synthetic-error term. | yes | no | no |
| Decision bands and detection floor | Bands evaluate at point estimates; the detection floor evaluates at lower bounds. | yes | no | no |
| Stage-C power | Injects signs using measured lower-bound accuracy/profile before any real statistic. | no direct estimate | yes | no |
| BS-L lock | Independently recomputes that all per-bin bounds pass. | no direct estimate | yes, as a pre-unblinding lock condition | no |
| Post-unblinding adequacy | Binds the already-verified calibration PASS; any removal makes calibration inapplicable and halts. | yes | yes | no |
| Permitted pre-lock aggregate surface | Allows only BS-8f aggregates, never per-object calibration values, to leave sealed storage. | no | no | yes (custody/disclosure consumer) |

The aggregate's required content and computation are explicit:

> **FT-03 — lines 792–800:** “**BS-8f** reports â, σ_a, a_LB, per-bin â_b, σ_ab, a_LB_b, ε̂ and the full Cov_a via `accuracy_from_handcheck()`, which implements **the inherited HC-1H estimator** `a = (raw − ε)/(1 − 2ε)` with the shared-ε derivative propagated — so Cov_a's off-diagonal is a real shared-error term, not an additive constant. (V6 returned the raw agreement rate and both gates caught it.) **Admissibility (`adjudicate_path()`):** `max_b |â_b − â| ≤ 0.03` AND every `a_LB_b ≥ 0.85` → scalar path; spread failure only → profile path; any `a_LB_b < 0.85` → **INCONCLUSIVE-BY-CALIBRATION, pre-unblinding halt.** V3-pred's HC-1H measurement and validity rules (committee, sealed keys, HC-5, HC-6) are carried by quotation at freeze.”

The uncertainty consumers are likewise explicit:

> **FT-04 — lines 419–425:** “**Uncertainties.** `sigma_ours_scalar(σ_β, β̂, a*, σ_a)` and `sigma_ours_profile(σ_β, β̂, ŵ, w_gradient(), Cov_a)`, both fail-closed on non-finite or degenerate input. **Cov_a is the FULL covariance matrix of {â_b} including the shared synthetic-error term**, produced by `accuracy_from_handcheck()` — a mandatory BS-8f field, not a supplied assumption. Decision bands evaluate at â / {â_b}; **the detection floor evaluates at a_LB / {a_LB_b}** — each evaluation point is named where it is used. `σ_comb = sqrt(σ_pub² + σ_ours(â)²)`, σ_pub = 0.011.”

The numeric decisions consume the calibrated amplitude and uncertainty:

> **FT-05 — lines 505–506:** “**Numeric verdicts (produced by the numeric decision helper):** **REPRODUCED-LONGO** (p < **0.001** AND Longo's sign AND |Â_L − 0.0408| ≤ 3·σ_comb AND Â_L ≥ the evaluated floor), **REJECTED-AT-LONGO-AMPLITUDE** (p > **0.05** AND (|Â_L| + 3·σ_ours(â)) < **0.0408**), **INCONCLUSIVE** (any other numeric outcome).  
> **Pre-statistic inconclusive halts:** **INCONCLUSIVE-BY-POWER** (produced by Row J, and the production runner's `N_eq` and Stage-C power guards), **INCONCLUSIVE-BY-CALIBRATION** (produced by Row J pre-unblinding, pre-verdict validator post-unblinding removal, or aggregate non-finite/degenerate failures excluding Row-I's missing allocated outputs — validated by `validate_calibration_aggregates` before the < 0.85 comparison, emitting the authenticated aggregate outcome), **INCONCLUSIVE-BY-MISSING-ALLOCATED-OUTPUT** (produced by Row I pre-BS-8f abort).”

The lock consumer is not merely aspirational; it is named as required implementation:

> **FT-06 — lines 1243–1244:** “**`verify_lock()` enforcement (route b):** Require the pinned `verify_lock()` to resolve the BS-L-bound BS-8f bytes and independently recompute `all(a_LB_b >= 0.85)`. Pin the implementation/schema digest for this route. Add a negative fixture demonstrating that a low-bound BS-8f cannot produce a passing lock.  
> **Row-J calibration guard:** Implement the guard to emit `INCONCLUSIVE-BY-CALIBRATION` and halt pre-unblinding if `a_LB_b < 0.85`.”

Post-unblinding applicability is another independent consumer:

> **FT-07 — lines 561–563:** “**Per-attempt states (zero or more per run, never a run outcome):** The adequacy receipt records exactly one terminal state per attempt: **EXCLUDED-BY-ABSENCE**, **EXCLUDED-BY-NONFINITE**, **EXCLUDED-BY-CONFIDENCE**, or **ACCEPTED-FINITE**. Catalogue quality is carried only as an already-resolved pre-lock status that cannot constitute a P8 removal. Any `EXCLUDED-BY-*` state deterministically emits the single run-level `INCONCLUSIVE-BY-CALIBRATION` outcome.  
> **Verdict Path (Row P) Post-Unblinding Consequence:** Row P must execute an exact set-equality join against the pinned attempt-set identity governed by the BS-2a design digest, using `brickid` and `objid` as fixed join keys, and produce the canonical post-unblinding adequacy receipt. Precedence states are explicit: zero records, duplicate records, extra records, or malformed records trigger an unconditional refusal; absent, non-finite, and low-confidence measurements are dropped; all others are accepted-finite. Adequacy decisions follow an ordered tree: First, calibration applicability: any post-unblinding removal immediately emits `INCONCLUSIVE-BY-CALIBRATION` and **no Stage-C rerun is performed**. Second, Row P binds the already-verified pre-unblinding calibration PASS (`a_LB_b >= 0.85`), relying on the locked BS-5f and BS-L verification.”

Finally, BS-8f is also a custody/disclosure object:

> **FT-08 — line 603:** “The *permitted aggregate surface* — χ-derived but defined as not χ-bearing — is exactly: the BS-2f mask fields (brickid, objid, position, acceptance flag, calibration-bin label, boundaries, digests — never a χ sign), the BS-8f aggregate record (â, σ_a, a_LB, the per-bin {â_b, σ_ab, a_LB_b}, ε̂, and the full Cov_a — aggregates over the hand-check sample, never a per-object value), and the BS-5f Stage-C receipt (PASS/FAIL and the permitted Stage-C scalar output, never a per-object calibration label).”

## Q2. Does a claim survive without `â`?

**Algebraically, yes; preregistrationally, no.** If accuracy is strictly above chance, `β̂ = 0` iff `Â_L = 0`. But the frozen design does not define an “accuracy-above-chance only” branch, a raw-`β̂` existence verdict, or a null-only disclosure. It defines one production verdict path and requires it to refuse before any statistic when the adequacy tree is inconclusive:

> **FT-09 — lines 495–500:** “`run_production_verdict()` is the **only** production path to a verdict. It exposes **no permutation injection, no permutation-count override, and no stage/trial/mask-kind override**; it calls `require_environment()`, `require_authorization()`, `require_complete_sample()` and `require_sealed()`. **Required but unimplemented guards:** the runner must require and verify the canonical BS-L artifact and the one-use unblinding receipt, verify the exact final-mask binding and post-unblinding ledger recomputation before forming any statistic, and refuse before forming any statistic if the adequacy tree emits an `INCONCLUSIVE` result. It derives the N_eq floor from the mask's own geometry, and only then runs the full 100,000-permutation record before the pure decision helper.”

The no-statistic consequence is stated expressly for a failed pre-statistic gate:

> **FT-10 — line 491:** “FAIL → **INCONCLUSIVE-BY-POWER declared before unblinding; the run halts; no real-sky statistic is ever formed.** **BS-5f certifies only the locked pre-attrition BS-2f mask (N = 49,211, N_eq = 110,983). Because any post-unblinding removal immediately terminates the run with `INCONCLUSIVE-BY-CALIBRATION`, there is no post-attrition Stage-C reevaluation.**”

`INCONCLUSIVE-BY-CALIBRATION` **is** a preregistered, reportable run outcome: FT-05 registers it as a “pre-statistic inconclusive halt,” and FT-02 states its producer and timing. What may accompany it is tightly bounded. Before the primary lock, no real-χ-derived value, sign, summary, label, or sign count may be disclosed, except the enumerated aggregate surface:

> **FT-11 — line 599:** “**Disclosure.** Nothing derived from any real χ value — value, sign, summary, label, or count of signs — is published, spoken, or written outside the sealed stores defined in §6.1 before the primary lock, **with exactly one exception: the permitted aggregate surface defined in §6.1's scope paragraph, which leaves the sealed stores only as the BS-2f, BS-8f, and BS-5f receipts, on the paths the table names, and is the only pre-lock χ-derived export this text allows.** After unblinding, disclosure waits for BS-V (§7).”

Therefore a report may say that the preregistered calibration gate failed, identify the named terminal outcome, and report authenticated permitted aggregate fields in BS-8f (including `â`, bounds, and covariance) if that valid record exists. It may not append a raw `β̂`, p-value, sign count, “consistent with zero,” “nonzero handedness exists,” or any other real-sky inferential claim. Statistical principle does not create a frozen branch that the text omitted.

## Q3. Does local data open any new route to `â`?

### Q3a. Retained mask located

I used:

`../_successor_build_20260824/acquire/positions_selected_cut.csv`

Checks performed without reading any FITS science pixels:

- 49,212 CSV lines = one header + **49,211 data rows**.
- Columns: `ls_id,brickid,objid,ra,dec,shape_e1,shape_e2`.
- SHA-256: `a20682c114508dbdd18ede6a56c61509ea9c16784aaca7eee61f76bf97cdd372`.
- The matching local receipt, `quality_cut_receipt.json`, records `n_before: 65060`, `n_after: 49211`, and the same output digest.

The frozen text independently identifies the post-cut mask:

> **FT-12 — lines 401–403:** “This defines a **distinct closed catalogue-quality exclusion reason** with authenticated evidence fields. It is NOT a redefinition of the parent catalogue. V9's `PINNED_PARENT_SHA256`, `PINNED_PARENT_ROWS = 65_060` and `PINNED_SELECTION_BRICKS = 6_445` are unchanged and must stay unchanged so no later reader mistakes this for a new sample.  
> The frozen predicate is applied before BS-2f so the **P3 sealed mask genuinely holds 49,211 rows** while the **65,060-row parent identity stays unchanged**. Post-unblinding instrument-confidence handling is kept separate. A threshold chosen or moved after inference exists voids the run.”

### Q3b. Measured GZ1 overlap

I fetched the official modest-size catalogues from the Galaxy Zoo data release:

- `GalaxyZoo1_DR_table2.csv.gz`: 667,944 rows; SHA-256 `5121e43f502856c9f73e31934a6e7d7282669c3ae065564a31f5d5115f45541d`.
- `GalaxyZoo1_DR_table3.csv.gz`: 225,268 rows; SHA-256 `282c8049e93c47b5343885210ace8ba5710e9914ce035a6b39061395436d9723`.
- Combined: 893,212 rows and 893,212 unique GZ1 `OBJID`s.
- Source: <https://data.galaxyzoo.org/> (the release page states that GZ1 volunteers classified clockwise and anticlockwise spirals and links Tables 2 and 3).

Method: parse GZ1 sexagesimal J2000 coordinates, nearest-neighbour spherical match from every retained-mask row, accept separation `<= 1.0 arcsec`. This threshold is stated because positional crossmatching is not an identity join and has no threshold-free “exact count.” The result is an exact count under the declared rule, not an estimate.

| Quantity | Measured count |
|---|---:|
| retained-mask rows matched within 1.0″ | **16,604** |
| unique GZ1 objects among those matches | **16,600** |
| from GZ1 Table 2 / Table 3 | 14,574 / 2,030 |
| matched rows with `P_CW + P_ACW > 0` | **13,347** |
| matched rows with `P_CW + P_ACW > 0.5` | **1,040** |
| matched rows with `P_CW >= 0.8` or `P_ACW >= 0.8` | **363** |

Threshold sensitivity (mask-row counts) is 16,488 at 0.5″, 16,637 at 1.5″, and 16,658 at 2.0″. This shows why the 1.0″ rule must travel with the number. **The closure statement that GZ1 “lacks coverage of DR10.1-south” is false for this retained mask.** It may have meant that GZ1 lacks *complete or population-representative* coverage; that narrower proposition was not what it said and was not tested here.

Coverage still does not make these labels a frozen BS-8f source. The frozen allocation requires minimum cell/stratum coverage:

> **FT-13 — lines 785–790:** “**Calibration.** Bin-construction algorithm and the 3 × 9 joint allocation with V3-pred's nine HC strata are frozen in code (`calibration_bins()`, `assign_bins()`, `allocate_handcheck()` — proportional, largest remainder, explicit tie rule, and BOTH inherited floors enforced: ≥ 10 per non-empty joint cell **and ≥ 30 real labels per live inherited HC stratum** (V6 enforced only the first; a gate produced a formally-filled but invalid sample). Infeasible floors FAIL rather than shrink.”

I did **not** test those allocation floors on GZ1 because the frozen text provides no external-label allocation/ingestion path, and doing so would not cure that absence.

### Q3c. Screen sign, empirical anchoring, and admissibility

As a matter of measurement design, holding the actual pixels could permit an empirical mapping: re-render matched GZ1 objects through a fixed north-up/east-left, parity-preserving pipeline; compare the release's CW/ACW vote convention with the rendered apparent winding; and precommit the mapping and disagreement rule. That would answer the screen-convention question empirically.

**But it is not admissible in this frozen run.** The text does not say “a published sign anchor is required.” Instead, it freezes a different empirical anchor—synthetics before any real image—and a different real-object calibration source—the allocated hand-check committee. The sign anchor is:

> **FT-14 — lines 124–129:** “**Sign, stated so it cannot be inverted by a later reader.** Longo's published amplitude carries a MINUS sign in his convention. Our East-of-North winding convention maps it to **+0.0408** (V3-pred F-5), and the code constant `A_LONGO = +0.0408` is our-convention while `A_LONGO_PUBLISHED_SIGNED = −0.0408` records his. The mandatory synthetic absolute-sign anchor (BS-4) re-establishes the mapping empirically before any real image; the fixture `BATTERY-SIGN` demonstrates that an injected **−0.0408** sky is never called REPRODUCED.”

The only admitted real-label actor is the committee, on its allocated sample:

> **FT-15 — lines 735–737:** “**Hand-check committee** | views χ-bearing cutouts **of the allocated sample only**, rendered through the sealed interface → each label leaves the member only through that same interface to row H”  
> “**Label-ingestion writer** | receives labels from row G through the interface → writes them, as one label set, into the committee sealed store, and writes the **χ-bearing label-set receipt**”  
> “**Calibration computation** | reads the sealed label set, the corresponding instrument outputs, AND the **χ-bearing label-set receipt**, inside the stores.”

The conduct table makes that list exclusive:

> **FT-16 — lines 721–723:** “**The phase line.** P0 freeze → P1 BS-6, first image byte → P2 cutout production, pre-inference integrity projection, exact-parent C2 stage-completion, and instrument inference → P3 BS-2f → P4 BS-8f → P5 BS-5f → P6 BS-L, **the primary lock** → P7 unblinding → P8 BS-7f, post-unblinding adequacy receipt, and BS-V → P9 disclosure.  
> **THE TABLE.** Each row is one permitted actor or process. Any pre-unblinding touch of a χ-bearing object by any person or process not in this table, or outside a row's stated surface, is forbidden by default.”

Therefore: the closure's demand for a **published** anchor is not itself a frozen-text requirement; an empirical anchor is conceptually possible. But substituting a new GZ1 comparison for BS-4 or for Rows G–I would add an actor, data source, label schema, match rule, and calibration path after P0. The frozen text forbids that route. Pixels change feasibility, not admissibility.

### Q3d. Other direction catalogues

There is another published catalogue-sized data set with per-object winding directions over the DESI Legacy Survey footprint: Lior Shamir, “Analysis of spin directions of galaxies in the DESI Legacy Survey,” MNRAS 516 (2022), 2281–2291, DOI 10.1093/mnras/stac2372. The paper describes 1,287,094 DR8 Legacy Survey objects assigned clockwise/counterclockwise directions by the Ganalyzer algorithm. Its data-availability statement says the annotated DESI Legacy Survey data are available **upon reasonable request**, not as a direct public download: <https://academic.oup.com/mnras/article/516/2/2281/6678564>.

So the answer is not “none,” but this route is **NOT VERIFIED for exact overlap** because the per-object catalogue was not directly obtainable in this task; obtaining it requires a request to the author and then a declared positional/object crossmatch to the 49,211-row mask. More importantly, it is machine annotation, not the frozen human hand-check, so it cannot populate `a` even if overlap is large. The official 8.67M Galaxy Zoo DESI catalogue also overlaps the Legacy footprint but consists of deep-learning model predictions, not human per-object direction truth; it likewise cannot fill Rows G–I.

## Q4. How far can the pipeline run with zero human labels?

### Strict answer for the lane as it exists now

**It stops before the first image byte.** The completed acquisition was authorized only for acquisition, and the frozen text still has pre-image design/authorization dependencies. The run guard states:

> **FT-17 — lines 583–587:** “It is **not** a live path to an unauthorised run: BS-6 and the first image byte are blocked by other means. A typed authenticated authorization record is **deliberately not built here** (principal direction, 2026-08-29), and `successor_ref_v9.py` remains frozen; `require_complete_sample()` refuses unless every parent object has a measurement receipt — a partial run is not a smaller run, it is a different experiment.”

The gate inventory confirms the boundary:

> **FT-18 — lines 943–951:** “**Class E — execution gates**”  
> “| BS-6 | Hwao | image transport approval: closed manifest sha, byte ceiling, producer checksum list | first image byte |  
> | BS-2f | Hwao | sealed accepted-position mask (N = 49,211) + sealed calibration boundaries — **value-only: the realised partition produced by BS-2a's frozen code, applying catalogue-quality exclusions** | Stage C |  
> | BS-8f | Hwao + hand-check committee | â, σ_a, a_LB, per-bin values, full Cov_a, integrity triggers | Stage C |  
> | BS-5f | Hwao | Stage-C confirmatory power receipt on the post-exclusion population (N = 49,211, N_eq = 110,983) | BS-L |  
> | BS-L | Duho signs | **pre-unblinding lock**: content per §6.1 clause 3(b) | unblinding |”

What is executable without labels *and without science-pixel reads* is therefore:

1. Verify the retained catalogue mask, quality-cut receipt, object/brick closure, acquisition manifest, per-brick published checksums, and local file presence.
2. Produce or re-verify catalogue/transport artifacts: mask counts/digests, 12,117-brick closure, checksum ledger, missing/extra-file report, byte total, and acquisition provenance.
3. Stop at **BS-6 / P1, first image byte**. No cutout production, C2 cutout-integrity projection, instrument inference, χ, stratum index, or handedness label is currently authorized or gate-admissible.

These artifacts have standalone value as durable provenance and readiness evidence, and they falsified the closure's no-GZ1-coverage premise. They have no standalone handedness-science value: they contain positions, quality metadata, coverage, and byte integrity, not a real-sky handedness statistic.

### Counterfactual ceiling if all existing pre-image gates were validly filled

This distinction matters: local pixels would then allow a **zero-human execution prefix**, but still not a completed image half. In frozen execution order it would be:

1. Row C: cutout production into the sealed store.
2. Row C2: cutout-integrity verification and exact-parent stage-completion artifact.
3. Row D: instrument inference and sealed per-object measurement receipts.
4. Row D2: machine-committee state × χ-tertile stratum-index artifact.
5. Row E: realised acceptance partition / 49,211-row mask.
6. Row F: calibration-bin boundaries and hand-check allocation.
7. **Stop at Row G, Hand-check committee**, because zero human labels cannot produce the label set; consequently Rows H–I cannot produce BS-8f, Row J cannot pass the pre-Stage-C calibration gate, and no real statistic can be formed.

The frozen execution sequence and dependencies are stated directly:

> **FT-19 — lines 729–734:** “**Cutout producer** | reads release image bytes → writes cutouts into the main sealed store, via row B; never reads any sealed object”  
> “**Cutout integrity verifier** — `verify_cutout_integrity` symbol and digest to be pinned at BS-2a (**DESIGN, defined, UNFILLED**).”  
> “**Instrument runner** | reads cutouts and the cutout-completion receipt (authenticating it against the pinned verifier) → writes per-object χ-bearing measurement receipts (χ, sign, amplitude, confidence) into the store only”  
> “**Stratum-index producer** (principal ruling, 2026-08-30 10:46, strata option A — χ-derived strata ACCEPTED; this row is the producer the widened Row F surfaced as missing)”  
> “**Acceptance-ledger recompute** | reads **only the separate authenticated acceptance-evidence projections** in the main store”  
> “**Calibration-bin sealing** | **for BIN CONSTRUCTION: the accepted partition's positions and acceptance flags only (χ-free)** on the genuinely 49,211-row mask; **for the HAND-CHECK ALLOCATION ONLY: additionally the per-object HC stratum index, WHICH IS χ-BEARING**”

The exact human wall is then explicit:

> **FT-20 — lines 735–738:** “**Hand-check committee** | views χ-bearing cutouts **of the allocated sample only**, rendered through the sealed interface → each label leaves the member only through that same interface to row H”  
> “**Label-ingestion writer** | receives labels from row G through the interface → writes them, as one label set, into the committee sealed store, and writes the **χ-bearing label-set receipt**”  
> “**Calibration computation** | reads the sealed label set, the corresponding instrument outputs, AND the **χ-bearing label-set receipt**, inside the stores.”  
> “**Stage-C runner** | reads the sealed BS-2f mask (χ-free) and the BS-8f aggregates; injects synthetic signs only — **never reads a real χ**. **Before running Stage C, Row J evaluates the calibration accuracy lower bound `a_LB_b < 0.85` from the BS-8f aggregate (V15 lines 566–567). If `a_LB_b < 0.85`, it emits `INCONCLUSIVE-BY-CALIBRATION` and halts the run pre-unblinding.**”

The acquisition therefore changes the pipeline from “pixels unavailable” to “pixels locally ready behind gates.” It does not move either the current first-byte gate or the ultimate Row-G human-calibration wall.

SEAT: CODEX
VERSION: REOPEN-ANALYSIS-V1
VERDICT: DOES-NOT-REOPEN
COUNT: 20
