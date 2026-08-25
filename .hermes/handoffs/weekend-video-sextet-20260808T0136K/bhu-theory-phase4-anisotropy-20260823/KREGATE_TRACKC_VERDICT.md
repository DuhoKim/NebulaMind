HOLD_PHASE_SUMMARY_OMITS_C2_MORPHOLOGY_FINDING

# Regate verdict — Phase 4 Track C, Amendment 1 + Amendment 2 (kimi seat, 2026-08-25 14:02 KST)

Scope: regate of TRACK_C_VERDICT.md as amended (Amendment 1, 11:15 KST; Amendment 2,
11:28 KST) against the five conversion conditions of KGATE_TRACKC_VERDICT.md (11:20 KST),
which held HOLD_C2_SCALE_TEST_DRIFT_AND_KC2_KC3_BREACH against the pre-amendment verdict.
Method: independent byte-level verification — label extraction and comparison scripted, token
greps across the verdict, the freeze, and both pinned harvests, git custody check. No track
file modified. The named grounds of the original HOLD (criterion-2 drift, K-C2 breach, K-C3
breach) are ALL discharged; one conversion condition stands unmet, so the HOLD persists on a
narrow, trivially repairable residue.

Custody (recomputed this regate):
- TRACK_C_VERDICT.md sha256 5a327348f2296c208a17a4da8b0b955be35ed487322b058b53170978b3bea352,
  committed: 0cf5bdef8 (Amendment 1) and 50ce984e7 (Amendment 2, "labels conformed
  byte-for-byte, and the gates' split recorded"); working tree clean for that path.
- TRACK_C_BRIEF.md unchanged since registration commit ae0af84b (sha 1b4fd2e4…2a661, pinned
  in TRACK_C_GO_RECORD.md) — the registered criteria were never altered; the drift was in the
  execution, exactly what the pre-registration exists to catch.

## Conversion conditions from KGATE_TRACKC_VERDICT.md, item by item

### 1. Registered criterion-2 test restored; GAPs instead of passes; "reachable" deleted — DISCHARGED

The registered test (TRACK_C_BRIEF.md:29, "SCALE: its angular size must correspond to ℓ ≲ 10")
is restored as correspondence, not inclusion (Amendment 1, "C2 rerun under the REGISTERED
criterion 2"). The operative table's scale row is GAP on all seven B3 rows. "reachable"
survives only at line 25, inside the superseded pre-amendment text, under Amendment 1's
explicit header "supersedes the conflicting content above". I re-verified the gap calls
against the freeze: no B3 row carries an angular-size value establishing correspondence to
ℓ ≲ 10 (B3.1's "5–10% at ℓ ≲ 40" is a deficit strength over a broader range — inclusion is
not correspondence, per my Attack 1; the GAP call is the correct K-C2 disposition).

### 2. Genuinely per-row table; each row's statistic class as stated in the freeze; B3.1 "full-sky" dropped — DISCHARGED

B3.5/B3.6/B3.7 are split into their own columns. B3.1's "full-sky spectrum statistic" label
is explicitly withdrawn (Amendment 1). Amendment 2 replaces every header label with the
freeze's own row label, and I verified this byte-for-byte by script: all seven labels match
TRACK_B_FREEZE.md:77–83 exactly (B3.1 "Low-ℓ power deficit", B3.2 "Low large-angle variance
LTP", B3.3 "Optimized variance estimator LTP", B3.4 "Cut-sky S½ missing correlations", B3.5
"COUNTER: quadrupole not anomalous", B3.6 "COUNTER: Bayesian odds", B3.7 "COUNTER: estimator
dependence"). Every added characterization — "TT", "real-space temperature-map", "cumulative
posterior", "two-point correlation statistic" — is withdrawn. The localization and patch FAILs
now rest on what the frozen labels and values themselves describe, which is exactly the basis
on which my Attack 2 independently re-derived every FAIL. The codex regate's sole residue is
therefore also discharged.

### 3. K-C2 compliance line corrected; scale gap named; "θ > 60°" removed — DISCHARGED

Amendment 1's corrected compliance section names the gap as the rule requires: "the
scale-correspondence evidence is ABSENT from the freeze for all seven B3 rows — named here as
gaps". The imported "θ > 60°" is gone from the operative text (grep: it appears only at
superseded line 25). I re-confirmed its absence from the frozen record: 0 occurrences in
TRACK_B_FREEZE.md, 0 in HARVEST_CMB_BOUNDS.md, 0 in HARVEST_H0_ANISOTROPY.md.

### 4. Photon-channel and pre-horizon qualifiers re-attached; z_c bound to A3_RECEIPT — DISCHARGED

The corrected summary now carries "a hiding condition FOR DIRECT POST-RECOMBINATION PHOTONS ON
WHOLLY-INTERIOR PATHS, PRE-HORIZON EPOCHS ONLY (Track A Amendment 1 scope)" — K-C3 scope
restored in the document's most quotable section. The z_c = √N law is now "supported by
A3_RECEIPT.md's derivation, gate-verified to 1e-6, and claimed on that receipt, not on the
verdict set" — I re-verified A3_RECEIPT.md:4–9 (derivation of z_c(center) = √N(η_e), checked
against the A2 solver to 1e-6) and A3_RECEIPT.md:59–61 (the law named). This is precisely the
sharpening my Attack 5 nit recommended; my rejection of codex's "appears nowhere" sub-point
was a defense of the item's support, and the amended form satisfies both seats.

### 5. C2 NOT-MORPHOLOGY-COMPATIBLE finding added to the phase summary — NOT DISCHARGED (RESIDUE)

The corrected phase summary still never names the confrontation's central new finding. Its
final clause reads "this confrontation's verdict that the branch stays CONSISTENCY-ONLY on
today's record, with the path to more named (TOV-side optics), not implied" — the C1 outcome,
not the C2 finding. Token check across the summary block: the only morphology string in it is
"the single-cap PROSPECT morphology", a different item (the PROSPECT filing). The finding
itself is correctly stated in the C2 sections of both amendments ("Finding unchanged … NOT
MORPHOLOGY-COMPATIBLE on the frozen record"), but conversion condition 5 required it in the
phase summary, because under the GO_RECORD's sequencing note (no verdict enters the overnight
report unless passed) that summary is the likely quotable text. As amended, the quotable text
still omits the phase's central new result. Advisory-grade at discovery, but it was written
into the conversion contract as item 5, and only the named gate artifacts bind a regate.

## The recorded gate disagreement — accurate, and moot in effect as stated

Amendment 2's record of my two rejections is accurate: I held the z_c = √N law IS supported
by the gated record via A3_RECEIPT.md (contra codex's "appears nowhere"), and that
"8-corruption-proof" was defensible as proof against exactly those eight frozen corruption
classes. Both were rejections of codex sub-points about the ORIGINAL wording, not objections
to amendment. Amendment 1 adopted the sharper form each gate preferred (z_c cited to
A3_RECEIPT; "EIGHT EMBEDDED CORRUPTION CASES ALL FAIL (a finite battery, not a proof of
corruption-proofness)" — I re-ran verifier v8 at the original gate and reproduced all eight
failing plus 50/50 PASS, receipt in _tmp_kgate_trackc_v8rerun.txt). I concur with Amendment
2's characterization: the disagreements are moot in effect, and a split between gates is
correctly preserved as a fact of the record rather than adjudicated by the author.

## Carried non-blocking nit (not gate-worthy, fix at next routine edit)

C1 still announces its template "verbatim from the brief" while substituting the brief's
parenthetical — "(the phase's durable product)" became "(x_off < x_max(t_obs), Track A's gated
product)". Substance preserved and arguably sharper; the amendments do not touch C1 and the
nit stands exactly as recorded in my Attack 1. Non-blocking then, non-blocking now.

## What converts this HOLD to PASS_TRACK_C_AMENDED

One clause in the phase summary naming the C2 finding with its registered caveats — e.g.
"…; and this confrontation's central new finding: NOT MORPHOLOGY-COMPATIBLE on the frozen
record (localized-anomaly literature unfrozen and unreached; any compatible reading would be
PROSPECT-grade)". No other change is required. The confrontation's bottom line is unchanged
and independently reproduced by this seat: CONSISTENCY-ONLY with the quantified sufficiency
surface; NOT MORPHOLOGY-COMPATIBLE on the frozen record; B2 AVAILABLE-BUT-UNENGAGED. A
one-clause summary amendment enters regate directly; the residue is record-completeness in
the quotable text, not substance.

## What this regate confirms about the process

Two engines independently converged on the same drift, the same K-C2/K-C3 breaches, and the
same repairs; the brief's bytes never moved; the execution corrected under gate pressure
without touching the registered criteria. The pre-registration did the work it was built to
do. The original HOLD's named grounds are fully discharged — this regate's HOLD rests solely
on the unmet conversion item above.

## Gate boundary

This regate adjudicates only TRACK_C_VERDICT.md as amended against KGATE_TRACKC_VERDICT.md's
conversion conditions. It does not re-open the amended Track A gate or the Track B freeze
(both verified closed at the original gate), does not adjudicate any literature dispute, and
does not authorize the bibliography/lane-2/deck steps in brief C5.3, which remain gated on
BOTH engines passing the verdict. The codex seat's regate of Amendment 2 is its own record.
