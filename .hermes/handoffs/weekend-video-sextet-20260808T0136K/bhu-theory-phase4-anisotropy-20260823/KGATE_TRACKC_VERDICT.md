HOLD_C2_SCALE_TEST_DRIFT_AND_KC2_KC3_BREACH

# Gate verdict — Phase 4 Track C adversarial gate (kimi seat, 2026-08-25 11:20 KST)

Gate: same kickoff as the codex gate (mandate: REFUTE TRACK_C_VERDICT.md against the
pre-registered TRACK_C_BRIEF.md, frozen TRACK_B_FREEZE.md, gated TRACK_A_VERDICT.md +
Amendment 1). Verdict written to KGATE_TRACKC_VERDICT.md per coordinator override (codex
gate owns GATE_TRACKC_VERDICT.md). Method: independent custody re-computation, per-row
re-classification of every C2 cell against the frozen record, re-execution of the frozen
verifier, and a line-by-line summary audit. Evidence: _tmp_kgate_trackc_v8rerun.txt in this
directory. No track file modified. The codex gate's verdict (a HOLD) landed while this gate
was running; every point of agreement below was independently re-derived against the
artifacts (commands quoted), and two codex sub-points are explicitly REJECTED (Attack 5).

Custody (all recomputed, none accepted from the artifact under review):
- TRACK_C_BRIEF.md sha256 = 1b4fd2e4…2a661 — matches the TRACK_C_GO_RECORD.md pin exactly;
  git shows the brief unchanged since registration commit ae0af84b (no diff to HEAD, clean
  working tree for that path). Pre-registration intact.
- All five v8 freeze pins match current bytes (both harvests, b_verify_quotes.py,
  b_verify_ledger.json, b_binding_map.json). The ledger's 11:00 mtime is a deterministic
  rewrite — my re-run reproduced 50/50 PASS, exit 0, all eight corruption classes failing,
  and the ledger sha unchanged (6106ab88…, receipt in _tmp_kgate_trackc_v8rerun.txt).
- GO_RECORD's precondition claims verified from the artifacts: REGATE5_TRACKB_VERDICT.md
  first line PASS_TRACK_B_FREEZE, mtime 2026-08-25 10:49:32 as recorded; KGATE_TRACKB first
  line PASS_TRACK_B_FREEZE. REGATE3_TRACKA = PASS_TRACK_A_AMENDED. Two engines on both
  inputs: closed.

## Attack 1 — post-registration criterion drift: FOUND in the C2 scale row (blocking)

The registered criterion 2 reads: "SCALE: its angular size must correspond to ℓ ≲ 10 (the
cap's near-threshold range)" (TRACK_C_BRIEF.md:29, bytes pinned above). The verdict's C2
table header substitutes a different test — "scale (ℓ ≲ 10 reachable)" — and awards passes
on grounds the registered test does not admit: B3.1 passes because "ℓ ≲ 40 range includes
it", B3.3 passes because "ℓmax 26" includes it, B3.2 passes on the qualitative phrase
"large angles", and B3.5–B3.7 take a bare grouped "pass" with no scale evidence cited.
Inclusion inside a broader estimator range is not correspondence of the anomaly's angular
size to ℓ ≲ 10, and a pass with no cited evidence is not a judgment under a pre-registered
criterion. This drift happened after a go whose record states "no criterion changes after
this go without a fresh gate and a fresh go" — the one thing the go froze was the criteria.

Direction-of-bias analysis (why this does not rescue the document): the weakening biases
TOWARD compatibility, against the verdict's own finding, so it cannot have manufactured the
NOT-MORPHOLOGY-COMPATIBLE result; and the finding is independently robust (Attack 2). But
the C2 table is itself a registered deliverable (brief C5.1), and as written it records a
substituted test with passes the registered test does not support. That is a blocking
record defect in a track whose stated point is pre-registration discipline.

Smaller drift, non-blocking: C1 announces its template "verbatim from the brief" but
replaces the brief's parenthetical "(the phase's durable product)" with "(x_off <
x_max(t_obs), Track A's gated product)". Substance preserved and arguably sharper; the
"verbatim" label is imprecise. C1's template selection and C3's AVAILABLE-BUT-UNENGAGED
record are otherwise faithful to the brief; the "A3(c)" citation for the uncalibrated
dipole checks out (A3_RECEIPT.md observable (c): "NOT CALIBRATED; recorded as such").

## Attack 2 — per-row statistic classes in the C2 table: every FAIL independently
confirmed (finding stands); three presentation defects (one blocking-adjacent)

I re-derived each row's class from the frozen table and, where needed, the pinned harvest
quotes. The finding — criteria 1 and 3 fail on every frozen row — survives independent
re-derivation:

- B3.1 (Planck 2013 XV, "power deficit of 5–10% at ℓ ≲ 40"): a low-ℓ SPECTRUM deficit.
  Not a single localized region; FAIL on criteria 1/3 sound. Defect: the cell's
  "full-sky" qualifier appears nowhere in the frozen record for this row (freeze:
  "Low-ℓ power deficit"; harvest: "the low-ℓ spectrum"). Over-classification beyond the
  frozen record — same evidence-rule breach class as the blocking K-C2 item below.
- B3.2 (Planck 2018 VII): map-variance statistic ("Low large-angle variance LTP") —
  supported by the frozen record. FAIL sound.
- B3.3 (Billi+ 2024): "Optimized variance estimator LTP" — supported. FAIL sound.
  (The cell's ℓmax 26 is not in the freeze table but IS in the pinned harvest quote —
  "The minimum value of the LTP is reached at ℓmax = 26" — so within the frozen record.)
- B3.4 (Copi+ 2015): "cut-sky S½ missing correlations" — a cut-sky two-point statistic,
  supported ("lower-tail p-values of the cut-sky S₁/₂ statistic"). FAIL sound.
- B3.5 / B3.6 / B3.7: the verdict groups them as one column labeled "same statistic
  classes". They are not one class: B3.5 is a quadrupole cumulative result plus a
  full-sky C(θ) interval; B3.6 is Bayesian odds ("1 in 10 or 1 in 20"); B3.7 is
  estimator/mask-dependent S₁/₂ p-values (8% vs 0.065%). The shared, decisive property —
  none is a localized patch around one axis — holds per row, so each grouped FAIL is
  individually sound; but the label is inaccurate and the grouping does not deliver the
  brief's per-row evidence (C5.1). Presentation defect, finding unaffected.

Criterion 4 (no-dispute survival): the verdict's passes are justified — the finding rests
on statistic CLASS, which both sides of the frozen dispute accept. No circularity.

## Attack 3 — scope excess vs gated Track A + Amendment 1: body clean; phase summary
breaches K-C3 (blocking)

The verdict body stays inside the gated scope: "sufficiency does not exclude, and
uncalibrated does not constrain"; no necessity claim, no exclusion claim, no post-horizon
claim, no non-photon messenger, no σ=1/3 model digits beyond the brief's own registered
ℓ ≲ 10 criterion. The C1 fact-check ("no frozen observation engages a crossing
signature") matches the brief's own pre-registered expectation. Clean.

The phase summary does not: "the sufficiency surface x_max(t) — the branch's first
quantified hiding condition" drops the two qualifiers Amendment 1 attaches to the result —
unobservable TO DIRECT POST-RECOMBINATION PHOTONS whose complete paths remain interior
(item 2), valid for pre-horizon observer epochs t_obs ≤ t_crit only (item 4). K-C3
requires photon-channel-only, pre-horizon-only language in the verdict; an unqualified
"hiding condition" in the document's most quotable section is broader than the gated
result. Blocking, and trivially repairable.

## Attack 4 — kill-criteria compliance: K-C1 and K-C4 hold; K-C2's printed compliance
claim is false (blocking)

- K-C1 HOLDS. I checked every C2 cell: each FAIL/PASS rests on statistic class, not on
  any significance claim. No frozen dispute was resolved or leaned on.
- K-C2 BREACHED as printed. The verdict claims "no number outside the freeze was used".
  Two counterexamples: (i) the B3.4 scale cell justifies its pass with "θ > 60°" — grep
  across BOTH pinned harvests and TRACK_B_FREEZE.md finds no "60°" anywhere in the frozen
  record (it is the standard S₁/₂ domain, true, but imported silently); (ii) where the
  freeze supplies no per-row scale correspondence (B3.2; B3.5–B3.7), K-C2 requires naming
  a gap — the verdict awarded passes instead. A compliance ledger that prints a false
  sentence is itself the breach. The affected cells do not touch the finding (criteria
  1/3 fail regardless), so this is a record-discipline blocker, not a result blocker.
- K-C3 BREACHED in the phase summary (Attack 3).
- K-C4 HOLDS. The published bibliography tree
  (../bhu-published-bibliography-20260819/) was last modified 2026-08-23 23:07 — untouched
  today; no branch-9 change preceded the gates.

## Attack 5 — phase summary, line by line: two items supported despite codex's
objections; one scope breach (above); one omission

- "a verified strict-model geometry (blind-double A1; two §6 bounds hit from inside)" —
  SUPPORTED. KGATE_TRACKA verified both §6 bounds from inside (t_crit/t_vis = 3.6175 ∈
  [1.8448, 4.4817]; √N0 = 1.5794 ∈ (1, 4.5]) and re-confirmed the blind double.
- "the z_c = √N law" — SUPPORTED, contra codex's "appears nowhere" objection. The string
  is absent from TRACK_A_VERDICT.md, but the law is one of the gated record's confirmed
  analytic laws: A3_RECEIPT.md:7 ("z_c(center) = √N(η_e)"), re-derived by both Track A
  gates, and inside Amendment 1's own summary ("four confirmed analytic laws"). The
  gated record taken with its receipts supports the item. Nit: cite A3_RECEIPT for
  sharpness.
- "the sufficiency surface x_max(t) — the branch's first quantified hiding condition" —
  SCOPE BREACH as printed (Attack 3): add the photon-channel and pre-horizon qualifiers.
- "the single-cap PROSPECT morphology" — SUPPORTED (PROSPECT contingent on TOV optics,
  per C1 and the brief).
- "an 8-corruption-proof frozen bounds apparatus" — SUPPORTED as compounded, contra
  codex. The freeze records exactly eight corruption classes tested and failing; I
  re-ran v8 and reproduced all eight failing through the row path plus 50/50 PASS
  (receipt on file). "8-corruption-proof" asserts proof against those eight, not
  omniscience. Nit: "8-class-corruption-tested" would be sharper.
- "the branch stays CONSISTENCY-ONLY on today's record, with the honest path to more
  named (TOV-side optics)" — SUPPORTED.
- OMISSION (advisory): the summary never names the confrontation's central new finding —
  NOT MORPHOLOGY-COMPATIBLE on the frozen record. Under the sequencing note (verdict
  enters the overnight report only after passing gates), this summary is the likely
  quotable text; repair should name the C2 finding explicitly.

## Failed attacks (positive evidence)

Tried to falsify the bottom-line finding per row — every row's criteria-1/3 failure
re-derived from the frozen record; finding stands. Tried to show the brief drifted after
registration — bytes pinned and stable since ae0af84b. Tried to show the freeze moved
after REGATE5 — all five pins match; the verifier re-run is byte-deterministic. Tried to
break the 8-class corruption claim by re-execution — all eight fail, genuine passes.
Tried to find necessity/exclusion language or non-photon channels in the verdict body —
none. Tried to find a K-C1 dispute lean — none; the finding is significance-independent.
Tried to find a bibliography change ahead of the gates (K-C4) — none. Tried to sustain
codex's z_c = √N and "8-corruption-proof" objections — both fail (above).

## What converts this HOLD to a PASS (amendment cycle, brief C5.2)

1. Restore the registered criterion-2 test in the C2 table: judge correspondence to
   ℓ ≲ 10 per row from frozen evidence only; where the freeze supplies none, record
   "GAP (K-C2)" instead of a pass; delete "reachable".
2. Make the table genuinely per-row for B3.5/B3.6/B3.7 with each row's own statistic
   class as stated in the freeze; drop or freeze-source B3.1's "full-sky".
3. Correct the K-C2 compliance line: name the scale-evidence gap; remove the imported
   "θ > 60°" or move it to a named-gap note.
4. Re-attach the photon-channel and pre-horizon qualifiers to "hiding condition" in the
   phase summary (and cite A3_RECEIPT for z_c = √N).
5. Add the C2 NOT-MORPHOLOGY-COMPATIBLE finding to the phase summary.

Expected outcome after repair: an UNCHANGED bottom line — this gate independently
reproduced the confrontation's findings (CONSISTENCY-ONLY with the sufficiency surface;
NOT MORPHOLOGY-COMPATIBLE on the frozen record; B2 available-but-unengaged). The HOLD is
about the verdict document's pre-registered discipline, not the confrontation's
conclusion.

## Gate boundary

This HOLD concerns the Track C verdict document only. It does not re-open the amended
Track A gate or the Track B freeze (both verified closed above), does not adjudicate any
literature dispute, and does not authorize the bibliography/lane-2/deck steps in brief
C5.3, which remain gated on both engines passing a repaired verdict.
