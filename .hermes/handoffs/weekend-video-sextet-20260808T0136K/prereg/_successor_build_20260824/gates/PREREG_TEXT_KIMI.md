# PREREG TEXT REFEREE — KIMI

Subject: `../PREREG_SUCCESSOR_DRAFT_V10_20260825.md` (490 lines, §0–§10), reviewed as a promise.
Round: BRIEF_PREREG_TEXT_V10, 2026-08-27. I did not read `/Users/duhokim/NebulaMindData/`.
I did not read the sibling seats' reports (`PREREG_TEXT_CODEX.md`, `PREREG_TEXT_GPT56.md`);
every finding below is derived from the subject text and the artifacts the brief names. Every
digest, constant, fixture name and quoted number I assert as *verified* was recomputed from the
files on disk during this review. What I could not recompute is under Testimony.

## What verifies (so the findings carry their weight)

- §0 pins: `successor_ref_v9.py` sha256 `6a9abbbd…c148`, `closure_worker_v9.py` `28f8e1f9…5959`,
  `FIXTURES_V9_20260826.out` `fab32ba2…a8b5`, referee report `f2ee062b…2f01` — all recomputed,
  all exact. v9 files are mode `-r--r--r--` on disk.
- §1 anchor: the publisher's abstract page for doi:10.1016/j.physletb.2011.04.008 states
  "−0.0408 ± 0.011" and "approx. (l,b) = (52°, 68.5°)" — matches §1's quotation. The code's
  `AXIS` constant maps to galactic (l, b) = (51.9998°, 68.5001°) — the published axis to
  8.6×10⁻⁵ degrees. `A_LONGO = +0.0408`, `A_LONGO_PUBLISHED_SIGNED = −0.0408` (code lines 73–74).
- Every quoted constant matches the v9 bytes: `CP_PASS_X = 962`, `RETENTION_LB = 0.8572`,
  `NEQ_MIN = 100_000`, `L_PLAN_MARGIN = 1.2`, `FLOOR_MULT = 3.09`, `A_FLOOR = 0.85`,
  `P_REPRODUCED = 0.001`, `P_REJECT_MIN = 0.05`, `SIGMA_PUB = 0.011`, `N_PERM = 100_000`,
  `PINNED_UNIVERSE_BRICKS = 366_912`, `PINNED_UNIVERSE_SHA256 = 863e5ded…`,
  `PINNED_COUNT_TOTAL = 832_393`, boundary band ×10 (`BOUNDARY_HI = 10.0`), HC 3×9 cells,
  floors 10/cell and 30/stratum, budget 500, `CUTOUT_PIX 128 × 0.262″`, frozen env
  python 3.9 / numpy 1.26.4 / little-endian. The x ≥ 962 rule is *exactly* the stated
  Clopper–Pearson contract: x = 961 gives LB 0.949366 (< 0.95, fails), x = 962 gives
  LB 0.950487 (≥ 0.95, passes) — recomputed from the binomial sum.
- §2.6 geometry, recomputed from `real/real_oracle_dr10.npz` + `real/real_selection_swapped.npz`
  (digests match the Stage-P receipt's `inputs`): 6,445 bricks, 65,060 raw, 53,005 retained,
  Var(cosθ) = 0.7546638985, N_eq = 3·n·Var = 3·sse = 120,002.88. The text's two N_eq formulas
  (`3·L_ret` in §2.3, `3·n·Var(c)` in the runner) are the same number — no hidden discrepancy.
  12,117 / 6,445 = 1.880×. 12,117 × 12.2 MB = 147.8 GB. Declined-run row (60,308 / 208,407 /
  0.0580 / 36,253 / 735.9 GB) matches the geometry receipt.
- Closure receipt (`CLOSURE_PROBE_V9_RECEIPT_20260826.json`): required_count 12,117,
  selected 6,445, objects 65,060, `plan_digest aaeaa9f3…b3f1`, 34 probes, summary
  `non_conforming: []` — matches §7's BS-2m row and the freeze record, including "nine items".
- Stage-P exact receipt: 995 successes vs the 962 rule, `passes_rule: true`, 431.4 s,
  perms 20,000, trials 1,000, zero trials granted by exactly one null, harness sha
  `daed15c7…` == on-disk `stagep_exact.py`, oracle/selection input digests == on-disk files.
- §3/§4 mechanics, read in the code: plus-one one-sided p with exact-≥ ties and non-finite
  fail-closed (`perm_record`), `Var(β̂) = Var_pop(s)/((N−1)·Var_pop(c))` (`perm_sigma_exact`),
  two `rng.random()` calls per object and no binomial (`inject_signs`), deflation by
  `PWR_CONSERVATISM = 1.01`, adjudication `≤ 0.03 → SCALAR`, any `a_LB_b < 0.85` raises the
  calibration halt *before* the permutation record (runner line 1609) — as §5/§6 state.
- Falsifiability structure (question 1): the outcome space is fully partitioned and
  boundary-closed — p = 0.001 exactly is not `< 0.001`, p = 0.05 exactly is not `> 0.05`, both
  land in INCONCLUSIVE as §5 declares. Only pinned code emits a verdict; the void rule bans
  post-χ edits. REJECTED-AT-LONGO-AMPLITUDE is a named, reachable failure of the claim. The
  promise can fail, and the failure sentences are unambiguous.

## Numbered findings

### F1 — BLOCKING — the blinding clause binds disclosure, not access; the "primary lock" is never defined

**Section / sentence.** §6: "Nothing derived from any real χ value — value, sign, summary, or
count of signs — is published, spoken, or written outside the sealed results store before the
primary lock." §7 BS-V names "verdict + primary lock" as a class-E slot.

**Why it fails as a promise.** Every word of this clause is about *publication*. A person can
open the sealed store, read every predecessor and successor χ, keep the observation entirely
inside the store, and comply with every word. Nothing binds *access*: the text names no role
holders, requires no access log, and never defines what the primary lock mechanically is — its
definition is deferred to BS-V, a class-E slot whose content arrives at execution time, too
late to referee. Asked "what would show it if someone had looked?", the text's honest answer
is: nothing — there is no access-log requirement whose absence or gap would evidence a look.
This is the document whose entire evidentiary value is that outcomes were not seen; a promise
about not-*speaking* is weaker than the promise the design needs, which is not-*knowing*. The
geometry receipt's "no χ was read" is author testimony about conduct (see Testimony), not a
binding, auditable non-access mechanism — and the text currently offers nothing stronger.

**Smallest sufficient repair.** Extend §6 with: (i) named roles holding sealed-store read
access; (ii) an append-only access log, receipted at BS-2f and BS-V; (iii) a definition of the
primary lock (what it seals, who can open it, what proves it held) bound into BS-V's schema
now, not at execution; (iv) the checkable sentence "no χ-derived artifact exists outside the
sealed store before the primary lock."

### F2 — BLOCKING — the predecessor's 208,405 sealed χ are assigned an undefined role

**Section / sentence.** Header: "its verified 60,308-brick sample and 208,405 sealed χ
measurements are archived as successor input."

**Why it fails as a promise.** "Successor input" says *that* the sealed measurements are input
without saying *to what*. The successor's footprint and the predecessor's overlap (same survey,
same sky); if any predecessor χ is reused for overlapping objects, the successor's blinding
story inherits every access question of F1 through a side door the text never mentions; if none
is reused, the promise needs one sentence saying so, because right now a reader cannot tell
whether 208,405 already-measured χ values are part of this run's analysis or inert archive.
The redesign's legitimacy rests on the redesign having been geometry-driven; leaving the
predecessor measurements' role undefined leaves the largest possible ambiguity sitting next to
that claim.

**Smallest sufficient repair.** One sentence in §2 (or the header): either "no predecessor χ
measurement enters this run's analysis; every χ is measured fresh under this text" — or, if
reuse is intended, the explicit reuse contract and its blinding safeguards.

### F3 — BLOCKING — §2.4 quotes a planner digest the frozen v9 code no longer pins

**Section / sentence.** §2.4: "BS-2m binds to
`_objmanifest_20260820/build_object_manifest.py::plan_candidate_bricks` with its pinned adapter,
digest `36bbbf250215…`."

**Why it fails as a promise.** `36bbbf250215…` is the *superseded* digest — the value the
pre-v9 narrower fingerprint produced, the same value the closure attacks held constant while
substituting execution (`CLOSURE_CODEX.md`, `CLOSURE_GPT56.md`). Round 9 widened
`frozen_planner_digest()` precisely because of that, and the v9 pin is
`1617af00eb7398abd93cc2726dbfb1ecfb24d07bede4b84c128ef2442bf40cb4` — code line 154
(`PINNED_PLANNER_DIGEST`), the v9 fixture line `CLOSURE-PINNED-PLANNER (1617af00eb73…)`, and
every closure row in the probe receipt (before and after the plan). `36bbbf250215` appears
nowhere in the frozen code, the worker, the suite, or the freeze record. This is the fourth
instance of the class the brief says was found and fixed three times on 2026-08-26 — a pin in
the text naming bytes the frozen mechanism no longer uses — sitting in the one section that
narrates why stale pins are fatal. By the text's own rule ("the prose is the defect") this is a
defect; by the document family's own history it must not be signed.

**Smallest sufficient repair.** Update the sentence to the v9 pin `1617af00eb73…` (or strike
the inline digest and cite `FREEZE_CLOSURE_V9_20260826.md` + the code constant).

### F4 — MAJOR — "995 of the 1,000 own p-values also sit at 5.00e-05" does not match the receipt

**Section / sentence.** §2.6 (mirrored in `REAL_GEOMETRY_RESULT_20260825.md` "Stated limits").

**Why it fails as a promise.** The receipt (`STAGEP_EXACT_RECEIPT_20260826.json`,
`p_own_by_trial`, all 1,000 entries counted) shows **951** trials at the 1/20001 floor
(4.99975e-05), with 995 total successes — 44 successes carry p ∈ [1.0e-04, 8.5e-04]. "995 sit
at the floor" conflates the success count with the floor count. The claim's purpose
("lower bounds, 20× below the 1e-3 test, verdict unaffected") survives at 951 — but a
preregistration that quotes a measured value its own cited receipt contradicts teaches the
next reader to stop trusting the quotations, which is the exact erosion this document exists
to prevent.

**Smallest sufficient repair.** "995 of 1,000 trials pass; 951 of the 1,000 own p-values sit at
the 5.00e-05 resolution floor."

### F5 — MAJOR — "refuted 2 of 7 boundary successes" matches no version of the fixture it cites

**Section / sentence.** §4: "on a fixture sized to sit near 50% power the mechanism **refuted
2 of 7 boundary successes** and failed the stage closed (`PWR-SELF-VERIFYING`)."

**Why it fails as a promise.** Every fixture transcript on disk — V4, V5, V6, V7, V8 and V9 —
reads "stage_power audited **12** boundary trials, confirmed **10**, refuted **2**". The figure
is deterministic (seeded streams); "2 of 7" appears in no artifact in the lane. The refuted
count (2) is right; the denominator is wrong against the named fixture. Same failure shape as
F4: a measured value quoted from a named artifact that the artifact contradicts.

**Smallest sufficient repair.** "refuted 2 of 12 audited boundary successes (10 confirmed)".

### F6 — MAJOR — "measured z* ranged 3.0376–3.1355, bracketing the normal 3.0902" is contradicted by the pinned fixture

**Section / sentence.** §4: "across four geometries the measured z\* ranged 3.0376–3.1355,
bracketing the normal 3.0902, and on the polar geometry this design actually selects the normal
threshold came out anti-conservative." (The same range sits in the v9 code's own
`reference_null_z` docstring.)

**Why it fails as a promise.** The pinned v9 fixture prints the four z\* values:
3.0694, 3.0010, 3.0020, 3.0260 — range **3.0010–3.0694**, every one *below* 3.0902. They do not
bracket the normal value, and 3.1355 appears in no artifact. The sentence's *conclusion* —
no fixed normal threshold is safe — does survive, via the same battery's `PWR-Z-STABLE` tail
masses beyond z = 3.090 (0.00135, 0.00130, 0.00100, 0.00110: three of four heavier than the
nominal 0.001), which the text never quotes. So the argument stands and its quoted evidence is
wrong: a measured range asserted in the text (and in the pinned code's prose) that the pinned
measurement contradicts. In a document that pins code by digest, prose inside the pinned file
is part of the promise's surface too.

**Smallest sufficient repair.** Quote the artifact: "the four fixture geometries' standardized
0.999 quantiles measured 3.0010–3.0694, and tail mass beyond the normal 3.0902 measured up to
0.00135 (`PWR-Z-STABLE`) — the normal threshold is not safe either way." Carry the same edit
into the code docstring at the next code revision (it does not change bytes that define
mechanism, but the docstring should not outlive the correction).

### F7 — MAJOR — the exact Stage-P receipt's subject is v7 bytes; the text's disclosure doesn't say so

**Section / sentence.** §2.6: "`stagep_exact.py` is a measurement harness; the exact-null
Stage P is not implemented in the file §0 pins."

**Why it fails as a promise.** The receipt's `subject` is `../ref/successor_ref_v7.py`, sha
`6be341bd…` — not the v9 bytes §0 pins. The disclosure says "not in the pinned code"; it does
not say the measurement ran against a *different, unpinned version* of the reference. I verified
the gap is benign: every function and constant the harness touches (`_planning_mask`,
`retained_counts`, `inject_signs`, `perm_record`, `reference_null_z`, `calibrated_p`, `sse`,
`rng_at`, and the stage/role/threshold constants) is byte-identical between v7 and v9, so the
995/1000 transfers unchanged. But "I checked and it transfers" is the referee's work, not the
text's — the promise should not require the next reader to diff two code versions to trust its
decisive number.

**Smallest sufficient repair.** One sentence: "the harness ran against v7; every primitive it
calls is byte-identical to the pinned v9 (enumerated), so the measurement applies to the pinned
code; it remains unrefereed and BS-5p stays unfillable until folded in."

### F8 — MAJOR — no failure disposition for permanently unmeasurable parent objects

**Section / sentence.** §5: "`require_complete_sample()` refuses unless every parent object has
a measurement receipt — a partial run is not a smaller run, it is a different experiment."

**Why it fails as a promise.** The text makes any shortfall fatal to the run and then says
nothing about the exit. If some parent objects turn out permanently unmeasurable (corrupt
images, failed cutouts, a brick that never passes transport), the team faces: halt forever,
amend (void under §6), or decline and redraft. That decision would be made in the room, after
real data exist — the exact situation a preregistration exists to pre-empt, and the exact shape
the predecessor stalled on (two objects WAITING, chain dead two short). The void rule plus the
decline precedent imply an answer, but a promise held by people not in the room cannot depend
on implication from a sibling document's fate.

**Smallest sufficient repair.** One paragraph: "if any parent object is permanently
unmeasurable, the run cannot complete; no amendment to shrink the parent is permitted
post-first-χ; the run is declined and any successor requires a new preregistration."

### F9 — MINOR — §0's definitional claim overstates coverage at production scale

**Section / sentence.** §0: "Every operational mechanism of this preregistration — geometry,
ledger, selection chain, … — is DEFINED by the code bytes of" v9. §2.3: "at production scale
the result is exactly what the frozen procedure returns."

**Why it fails as a promise.** Two of the named mechanisms do not live in the pinned bytes at
the point of use: the selection at production scale is computed by *unpinned* vectorized
equivalents (the pinned `greedy_ledger()`/`local_pass()` are O(n²) and "will not run at
270,577 bricks" — §2.6's own disclosure; equivalence is statistical: 40/30/400-case batteries,
not proven in general — §10), and the exact Stage P exists only in a harness (F7). "The result
is exactly what the frozen procedure returns" asserts an identity that cannot be executed, let
alone checked, at production scale; what actually binds the artifact is the after-the-fact
digest pin (CLOSURE-PINNED-SELECTION). The disclosures exist, but a reader of §0 and §2.3 alone
is told the code *is* the mechanism at the one scale where it isn't.

**Smallest sufficient repair.** One sentence in §0 (or §2.3): "at production scale the
selection artifact is produced by vectorized equivalents validated on the stated batteries and
bound by output digest at BS-2s; the frozen chain remains the normative definition, not the
executed one."

### F10 — MINOR — the text never says what a null result does not establish

**Section / sentence.** §1: "It does not test A ≈ 0.02, Shamir, BHU, or whether the sky is
isotropic." §5 defines REJECTED-AT-LONGO-AMPLITUDE's region; nothing more is said about it.

**Why it fails as a promise.** The companion essay (`WHAT_IS_AT_STAKE_20260827.md`) states the
limits almost verbatim — a null would not prove isotropy, would not exclude a smaller
amplitude, would not settle other researchers' claims — but the essay is not the promise. In
the prereg itself, "does not exclude smaller amplitudes" exists only implicitly in the region
definition, and the other two limits only implicitly in §1's claim boundary. Interpretation
limits are precisely what a preregistration binds; the author demonstrably knows them and the
binding document doesn't carry them. (Relatedly: a strong *opposite*-sign detection — p < 0.001
with Â < 0 — lands in INCONCLUSIVE under §5's partition; the partition is closed and
pre-declared, which is what matters, but the text could say in one clause that this outcome is
a strong anti-Longo result, not an absence of one.)

**Smallest sufficient repair.** Two sentences in §5: "REJECTED-AT-LONGO-AMPLITUDE excludes the
published amplitude at the published axis under this design's sensitivity. It does not
establish isotropy, does not exclude amplitudes below this design's floor, and does not speak
to other researchers' distinct claims."

### F11 — MINOR — no public deposit or external timestamp for the freeze is specified

**Section / sentence.** §6 Custody: "deliverables sha-pinned at gate dispatch by the gate's own
report (an external witness) and committed to git."

**Why it fails as a promise.** A preregistration's force is provable prior existence.
"Committed to git" on a private repository, witnessed by the lane's own gates, is weak evidence
of *when* the promise existed — the witnesses are the participants. The header says the text
"becomes a preregistration only when every class-P slot holds a receipt, the gates pass, and
Duho signs the freeze"; where the world can see that signed artifact, with a timestamp no
participant controls, is never said.

**Smallest sufficient repair.** One clause naming the deposit (public repo, archive service, or
third-party timestamp) whose record of the freeze is itself cited in BS-V's receipt.

### F12 — TRIVIAL bundle (small, same-edit repairs)

- **208,405 vs 208,407.** Header: "208,405 sealed χ measurements"; §2.6's declined-run row:
  "208,407 objects". Consistent with the two-WAITING-objects narrative (208,407 raw − 2 =
  208,405 sealed), but the text never reconciles the figures and a reader sees a contradiction.
  Add a parenthetical.
- **`RETENTION_LB = 0.8572` has no stated provenance.** Frozen, consistent, and quoted — but
  the promise never says where the constant came from (presumably the predecessor's measured
  retention). One clause.
- **BATTERY-POS "p = 2.2e-21"** (§5) vs the fixture's "p = 2.23e-21". Truncation, not error;
  quote the fixture's digits.
- **No "no secondary endpoints" sentence.** `explore_verdict()` exists in code for synthetic
  work; the text never states that no analysis outside `run_production_verdict()` will be
  presented as the preregistered result. §6's "no claim stronger than its check" gestures;
  one sentence closes it.

## Answers to the brief's eight questions, compressed

1. **Can it fail?** Yes. REPRODUCED / REJECTED / INCONCLUSIVE / the two halts partition the
   space; boundary p-values land in INCONCLUSIVE as declared; only pinned code emits the label;
   the void rule bans post-χ edits. The falsification sentence (§5, REJECTED-AT-LONGO-
   AMPLITUDE) and the reproduction sentence (§5, REPRODUCED-LONGO) are each unambiguous to a
   wriggler. Soft spot named in F10 (anti-Longo significance reads as "INCONCLUSIVE").
2. **Degrees of freedom.** The release fork is genuinely bound (iff-criterion, 2026-09-05,
   branch-invariance receipt, gated amendment to wait longer). All calibration values are
   measured-but-frozen-formula; evaluation points are named (§3). Thresholds, floors, counts
   and the 962 rule are frozen constants and verify. The residual open choices are the eleven
   unfilled slots (declared, producer-named) plus the disclosed set (exact Stage P, vectorized
   equivalence, `Cov(β̂, â) = 0`, clean-room spec, BS-9 schema, BS-V lock) — and the two the
   text does *not* disclose cleanly: F8's unmeasurable-object exit and F9's
   frozen-vs-executed selection. The ≈148 GB planning ceiling was adjusted to the measured
   closure on 2026-08-26 — disclosed, pre-χ, planning-only; BS-6 binds the real ceiling later.
3. **Circularity.** None found in the forbidden direction. Stage P injects synthetic skies at
   the frozen amplitude and floor on count-derived geometry; Stage C runs on the sealed mask
   (positions/flags/bins — never a χ sign) with measured a_LB; the detection floor is a frozen
   formula evaluated at a measured point, named as such in §3. No boundary *rule* depends on
   the data it judges; the one data-dependent *value* (a_LB) is class-E with a frozen producer
   and pre-unblinding timing. The selection is geometry-and-counts only.
4. **Numbers vs artifacts.** The overwhelming majority verify (list at top). Four do not:
   F3 (superseded planner digest), F4 (995 vs 951 at the floor), F5 (2 of 7 vs 2 of 12),
   F6 (z\* range contradicted by the pinned fixture). The brief said to assume more stale
   figures remain; there were, and they are these.
5. **Blinding.** Real in structure (type system, Stage-C-before-statistic ordering, void rule,
   custody) and supported in conduct (geometry-only inputs; no χ artifact exists in the review
   set) — but not binding at the point that matters: F1 (access, lock, log) and F2
   (predecessor χ role). What would show a look today: nothing.
6. **Honest incompleteness.** Mostly exemplary — the draft banner, the 11/12 slot table, the
   retraction handling in §2.6, and §10's measured-not-accepted language are all straight. The
   exceptions are F9 (§0/§2.3 read more finished than §2.6/§10 disclose) and F7 (the v7-subject
   gap inside an otherwise honest disclosure).
7. **Null-result overclaim.** No overclaim of mechanism or scope anywhere; §1's boundary is
   correctly narrow. The gap is omission, not commission (F10).
8. **Missing entirely.** F1's access discipline, F2's predecessor-χ role, F8's failure
   disposition, F11's public deposit — all four are text-level, none needs the machinery
   reopened, and all four are invisible if you only referee the machinery.

The brief's five known-wrong items: confirmed accurate as stated; none understated. On item 3
(selection artifact has no producer receipt): still true — the closure pins the artifact's
bytes (CLOSURE-PINNED-SELECTION) but nothing proves those bytes were *produced by* the
described algorithm rather than merely presented to it; the freeze record's own item 8 says
the same. On item 5 (one referee seat for the mechanism): the text carries the narrowing
honestly in §0 and §7.

## Testimony (asserted in the text or receipts; not independently verified by me)

- Longo's sample size "15,158 spirals" (amplitude, axis, DOI and bibcode verified from the
  publisher's abstract page; the count was not re-verified against the paper body).
- The predecessor documents quoted by sha (V3-pred `b06901c8…`, BS6-pred `5ff7f454…`, decline
  memo `b4a1f1fc…`): existence and contents outside my review set; the eight Cut-6 predicates'
  byte-identity to BS6-pred accepted, not checked.
- BS-3 instrument values (weights `83008c1c…`, τ = 4.4006456017494235, antisymmetry identity) —
  unfilled slot.
- "DR11 pages exist; no photo-z product is present" (measured 2026-08-24) — author's
  measurement.
- Equivalence batteries: 40 (order), 30 (reduction), 400 (swap phase, "referee's own seed and
  regime") cases with zero mismatches — stated in the geometry receipt and §10; no independent
  receipt in the named set.
- "12,117 reproduced independently three times" — the closure row is in the probe receipt; the
  two direct enumerations are asserted in §2.6/§7 and the mechanism referee's report.
- 12.2 MB/brick unit price and the 735.9 GB declined download — predecessor-era figures.
- The authorization and conduct narrative (drafting authorization, catalog-only authorization,
  "no χ was read", the 2026-08-26 ceiling raise, provider refusals of the two mechanism seats)
  — conduct testimony; nothing in the artifacts contradicts it, and F1 exists precisely because
  testimony is all there is on access.
- The exact Stage-P run's machine claims (20 workers, 431.4 s) — receipt-carried.

## Verdict

The promise's skeleton is sound: falsifiable regions, frozen constants that verify, honest
retractions, real custody. It is not yet sound enough to sign. Three findings block the freeze
— **F1** (blinding binds disclosure, not access; primary lock undefined), **F2** (the
predecessor's 208,405 sealed χ have no declared role), **F3** (§2.4 quotes a planner digest the
frozen v9 code no longer pins). All three are text repairs; none requires reopening the frozen
mechanism. F4–F8 must be repaired in the same revision; F9–F12 should be.

**NOT CLEAR**
