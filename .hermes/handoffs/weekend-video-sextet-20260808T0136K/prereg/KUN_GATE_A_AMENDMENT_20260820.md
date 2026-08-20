HOLD_PREK8_AMENDMENT

# Kun gate seat (kimi, Nous route) — pre-K-8 amendment gate
# Document gated: AMENDMENT_PREK8_20260820.md
# SHA-256 e832a341f4c9c3937b8fcafc42d6dd7c15ca1e6ea32e5c9ae21856ab50e1380c (recomputed at gate: match, 562 lines)
# Receipt: CSEAT_AMENDMENT_DONE.md. Fresh one-shot; findings-only; no network; local files + python3 only.
# Verdict: HOLD with four numbered repairs. Three are precision repairs to claims the
# amendment itself makes. One is substantive: AM-C.1 as drafted is not implementable against
# the pinned harness (line-pin error hides that), and the AM-B pool source as frozen in AM-B.1
# is not the pool the rehearsal actually exercised. Both are fixable tonight. Nothing here
# authorises anything; Duho owns acceptance and the freeze.

================================================================================
## CHECK 1 — AM-A ORIGIN CLAIM: "already frozen by BS-5 §3, merely confirmed"

VERDICT: TRUE AS TO THE SCIENTIFIC DEFINITION; MISSTATED AS TO THE OPERATIONAL POLARITY.
The amendment's own text is careful, but its load-bearing sentence overclaims.

What BS-5 §3 (LANA_BS5_LONGO_SIGN_20260814.md, SHA b7c32dcf… matches the amendment's pin,
§3 lines 55–58 verified verbatim) actually froze:

    sign(χ) = +1 for counter-clockwise apparent winding (↺ = Longo-Left);
    sign(χ) = −1 for clockwise (↻ = Longo-Right), East-of-North on the analysis raster.

So the *scientific* convention — what sign(χ)=+1 means in the sky — WAS frozen by BS-5 §3 and
the rehearsal did not choose it. On that clause the amendment is accurate.

But BS-5 §3 itself opens: "The prereg leaves the **polarity of sign(χ) unset** (I-2 defines χ
up to sign); BS-5 fixes it" — and BS-5 adopted the (L−R) polarity explicitly as "a deliberate,
documented polarity choice" (§4) under the BS-5 fill rule. The frozen V3 F-5 says the same:
"convention filled at BS-5 by quotation." So what was frozen was a *chosen* mapping, and the
*operational* fact — that the frozen production weights 83008c1c… realize that mapping with
DIRECT rather than inverted polarity — was not frozen anywhere before tonight. The amendment
says this itself at §1.1: "What was not written down anywhere is the operational fact…"

The amendment's chain-conclusion sentence — "The rehearsal did not *choose* the polarity; it
*confirmed* the one BS-5 already froze" — is TRUE for the scientific convention and FALSE for
the operational polarity if read to cover both. The rehearsal (1,896/2,000 direct, 104
inverted, 0 exact zeros) measured and CONFIRMED the operational polarity; it could have come
out inverted, in which case a correction on synthetics would have been required before the
crossing. That is a confirmation of a binary fact, not a choice — and AM-A.2 is right to freeze
it — but the document must not blur "BS-5 froze the definition" into "BS-5 froze the weights'
polarity." The first is true; the second is what tonight adds. The distinction the amendment
says "matters" is real; it must be stated exactly.

REPAIR 1 (precision, no design change): rewrite the chain conclusion and AM-A.2's framing so
that "what BS-5 froze" is always qualified as the *scientific sign convention* (the meaning of
sign(χ)=+1), and "what AM-A.2 adds" is always qualified as the *operational polarity* (that
the frozen weights realize it directly). As drafted, an external reader could take the
amendment to claim the operational polarity was already frozen on 2026-08-14; it was not.

================================================================================
## CHECK 2 — AM-A ARITHMETIC: polarity mapping vs V3 F-6 decision regions

VERDICT: PASS. Recomputed.

- Longo: A ≡ (R−L)/(R+L) = −0.0408 (BS-5 §1–§2 quotations verified in the pinned document;
  R=↻=CW, L=↺=CCW). Negative ⟹ L > R ⟹ excess of counter-clockwise toward n̂_L = (52°, 68.5°).
- Our convention (BS-5 §3): sign(χ)=+1 ⟺ CCW = Longo-Left, so D̂ is the (L−R)-weighted dipole
  and the same physical effect is +0.0408. The (R−L)→(L−R) polarity swap negates exactly once:
  −(−0.0408) = +0.0408. Consistent with F-5's frozen target (V3 line 139: Â(n̂_L) = +0.0408).
- F-6 REPRODUCED-LONGO (V3 line 142): p<0.001 AND sign per F-5 AND |Â_c − 0.0408| ≤ 3σ_comb.
  At BS-9 σ_ours=0.004805, σ_pub=0.011: σ_comb=0.012004, 3σ_comb=0.0360. An inverted-polarity
  true effect would sit at Â_c ≈ −0.0408, i.e. |−0.0408−0.0408| = 0.0816 > 0.0360 even at
  σ_ours=0 (3σ_pub=0.033). The band therefore discriminates sign: a wrong-sign result cannot
  land in REPRODUCED. AM-A.3's requirement (positive Â_c AND inside the band) is entailed by
  the frozen band itself — it is a correct reading, not a new constraint.
- F-6 REJECTED-AT-LONGO-AMPLITUDE is magnitude-only ((|Â_c|+3σ_ours) < 0.0408) and unaffected.
- Link 4 discrimination: 1,896 vs 104 against a 50/50 polarity null is z ≈ −40; the polarity
  is a discrete, settled fact. The amendment's justification stands.

No arithmetic defect found.

================================================================================
## CHECK 3 — AM-B: Jeffreys formula, byte-for-byte reproduction, HC-4 firewall

VERDICT: FORMULA AND REPRODUCTION — PASS against the attempt3_hold priors file. FIREWALL —
PASS (verified in code). BUT the cited file path resolves to a DIFFERENT file than the one the
amendment's numbers come from, AND the frozen pool source is not the pool the rehearsal
exercised. Two repairs.

3a. Formula recompute — PASS. The frozen rule
    a_s^prior = (c_s + ½)/(m_s + 1) = Decimal(2c_s+1)/Decimal(2(m_s+1)) at prec 28 (Python
    decimal module-default context precision verified = 28)
reproduces ALL NINE strings in
    _rehearsal_20260820/attempt3_hold/hc1h_neyman_priors.json (SHA 4b6b7130…)
byte-for-byte. I did not trust the report table: I rebuilt (m_s, c_s) from the raw attempt3
artifacts — synthetic_truth.jsonl, hc1h_real_population.jsonl, committee_results.jsonl,
global-rank |χ| tertiles — and recomputed every prior. All nine match the file strings:
    agree-confident|0: m=582 c=492 -> 0.8447684391080617495711835334  ✓
    agree-confident|1: m=571 c=571 -> 0.9991258741258741258741258741  ✓
    agree-confident|2: m=596 c=596 -> 0.9991624790619765494137353434  ✓
    disagree|0:        m=50  c=40  -> 0.7941176470588235294117647059  ✓
    disagree|1:        m=35  c=35  -> 0.9861111111111111111111111111  ✓
    disagree|2:        m=35  c=35  -> 0.9861111111111111111111111111  ✓
    low-confidence|0:  m=35  c=31  -> 0.875                            ✓
    low-confidence|1:  m=61  c=61  -> 0.9919354838709677419354838710  ✓
    low-confidence|2:  m=35  c=35  -> 0.9861111111111111111111111111  ✓
The never-degenerate bound 1/(2(m+1)) ≤ (2c+1)/(2(m+1)) ≤ (2m+1)/(2(m+1)) ∈ (0,1) verified;
nm_handcheck.py:3205's zero-information refusal is unreachable under this rule, as claimed.

3b. REPAIR 2 (citation defect): the amendment §2.3 says "the rehearsal's
`hc1h_neyman_priors.json`" and the rehearsal report's own artifact map points at
`_rehearsal_20260820/hc1h_neyman_priors.json`. That root path NOW holds a different file
(SHA e9f47597…, written 18:49 by the LATER N=20,000 natural-campaign rerun,
KICKOFF_GPT1_REHEARSAL2/GPT1_REHEARSAL_DONE), whose nine strings are entirely different and
do NOT match the values the amendment quotes. The values the amendment verifies against live
only at `_rehearsal_20260820/attempt3_hold/hc1h_neyman_priors.json`. The root file was
overwritten after the pinned rehearsal report (31d54b9d…) was sealed. Every reference must be
re-pointed to the attempt3_hold path with its SHA, and the amendment should note that the root
path is stale/overwritten, so a future reader does not "verify" the claim against the wrong
file and conclude it fails. (For the record: the late N=20,000 file is itself
Jeffreys-consistent at its own populations — the formula is stable across both runs — but that
is not the file the amendment pins.)

3c. REPAIR 3 (substantive — the frozen rule does not match the exercised rule): AM-B.1 freezes
priors counted over "the entire frozen synthetic injection pool," and §4 item 1 states
correctly that this is a judgment, not a derivation. But the pool the rehearsal ACTUALLY ran
through the unmodified allocator — and the pool that reproduces the byte-for-byte strings the
amendment touts — is the 2,000-object SELECTED CAMPAIGN, not the 12,000-candidate pool. My
reconstruction above proves it: the campaign-binned (m_s, c_s) reproduce all nine strings; the
report's own stratum populations (582/571/596, 50/35/35, 35/61/35) are the campaign
populations. So the amendment's two load-bearing sentences pull against each other: "reproduces
every prior byte-for-byte" (true only for the campaign pool) versus "computed over the entire
frozen synthetic pool" (frozen, but never exercised). One of these must move:
    (i) freeze the campaign pool as the prior source (matches the exercised evidence), or
   (ii) keep the full-pool freeze but re-run the allocator end-to-end on full-pool priors and
        replace the byte-for-byte verification with values from THAT run.
The amendment's justification for the full pool (selection-independence; larger m_s) is sound,
and I do not oppose the choice — but "demonstrated to be exactly executable by the existing
pinned code path" is presently demonstrated for a DIFFERENT pool than the one frozen. As
written this is exactly the kind of gap F-9 exists to close.

3d. Firewall — PASS. I traced the computation path in the pinned harness
(nm_handcheck.py; note the amendment pins cc88fa5e… while the working copy now hashes
65c04377… — the file changed after the rehearsal; see RULING (ii)). The flow is:
    neyman_prior_rates (JSON) -> allocate_neyman (:3178) -> weights = N_s·√(rate(1−rate))
    -> real_allocation = {integer n_s} -> sealed key document (:1018 records the rates) ->
    labels counted -> hc1h_statistics (:1457).
Inside hc1h_statistics, attenuation a = Σ w_s·a_s with a_s = (â_s − ε̂)/(1−2ε̂), â_s from HUMAN
labels (real_counts), ε̂ = Fraction(synthetic_errors, synthetic_trials) as ONE global rate,
w_s = population/population_total. The string "prior" does not appear in hc1h_statistics,
hc1h_verdict, or anywhere on the estimate path; the only "prior*" symbols elsewhere are
adjudication prior-LABELS (a display field) and the sealed-commitment recording. The priors
touch exactly one thing: the integer n_s. AM-B.2's firewall claim is TRUE in the pinned code.
The "wrong prior is harmless" argument is also correct: stratified estimator with population
weights is unbiased for any allocation given random within-stratum sampling; a bad prior widens
σ_a (safe direction) and cannot bias a.

================================================================================
## CHECK 4 — AM-C: merge ladder determinism, scope, single evaluation, AM-C.3 both branches

VERDICT: LADDER AS WRITTEN — deterministic, within-state, terminating; AM-C.3 both branches
specified. IMPLEMENTABILITY — FAILS against the pinned harness (see RULING ii). One repair.

4a. Determinism — verified by exhaustive simulation, not by reading. I implemented AM-C.1's
ladder exactly as written (per committee state: while a surviving cell has N<30 and ≥2 cells
survive, take the deficient cell of smallest population — tie smallest tertile index — and
merge it into the surviving cell at minimal tertile-index distance — tie smaller population,
then smaller tertile index) and ran it over:
  - all 262,144 configurations of {0,1,29,30} populations across the 9 cells, and
  - 20,000 random population draws.
In every case: it terminates; no committee state ever loses its last cell identity (a state
collapses to at minimum one stratum); population is conserved within each state; and whenever
≥2 cells survive, all survivors are ≥30. The tie-breaks are total and deterministic — no
discretion survives. Within-committee-state-only is structural (the loop is per-state; no
cross-state merge target exists). 3 ≤ |S| ≤ 9 holds; 30·|S| ≤ 270 < 500, so the frozen Neyman
total and floor remain feasible on the merged set. Single evaluation on the complete population
before any preparation call is stated at §3.3 and is consistent with Hwao's partial-tertile
prohibition (cutpoints computed once on the complete accepted population, then the ladder runs
on those fixed counts). No defect in the rule AS WRITTEN.

4b. AM-C.3 precedence — both branches fully specified. Branch 1 (gated, hash-pinned merge
implementation exists at the crossing -> AM-C.1 governs) and branch 2 (not -> AM-C.2 governs:
any real cell N_s<30 HOLDS the hand-check and declares INCONCLUSIVE-BY-POWER under HC-5) are
each closed, and the trigger condition ("does the gated, hash-pinned implementation exist?") is
a pre-crossing fact independent of any real χ, population count, or label. No discretion
survives the crossing. This is correctly constructed.

4c. REPAIR 4 (substantive — the implementability claim is false as evidenced): §3.4 item 4
rests on "HC1H_STRATA is a hardcoded nine-tuple (nm_handcheck.py:45–46)." At the pinned SHA the
definition is at line 49 (built from HC1H_STATES × range(3) via committee_state_vocabulary.py);
lines 45–46 in the CURRENT file are that definition, but the CURRENT file is not the pinned
file. More importantly, the hardcoding is far deeper than the tuple. Verified hard nine-stratum
assumptions the merge must cross:
  - hc1h_statistics (:1468–1472) RAISES unless real_counts, stratum_populations, AND
    synthetic_counts are each EXACTLY set(HC1H_STRATA) — "require exactly nine accepted strata."
  - hc1h_verdict (:1417–1418) RAISES unless stratum_rates is exactly the nine — "requires
    exactly nine committee-state by chi strata."
  - allocate_neyman (:3187–3188) RAISES unless prior_rates keys == sorted(populations) — so
    under a merge, EITHER the populations map OR the priors keys change, and the harness's own
    :1018 recording iterates HC1H_STRATA for the sealed commitment.
  - the balanced injection allocator (:597–599), the repeat sampling (:807), the sealed
    stratum_populations, and the public projection all iterate HC1H_STRATA.
So a conforming merge implementation is not "support a merged stratum map" — it requires
RE-OPENING the hash-pinned harness's nine-stratum invariant in at least the statistics, verdict,
and commitment paths. That is a real change to a gated program, as §3.4 item 4 concedes — but
§3.4 item 4 UNDERSTATES it, and the line-pin error (45–46 vs the pinned 49) is a symptom that
the cited evidence was read off the wrong file revision. The precedence rule (AM-C.3) survives
this — it correctly makes the merge conditional on a gated implementation existing — but the
amendment must not present the change as localized to a tuple. See RULING (ii) for the gate
consequence.

================================================================================
## CHECK 5 — WEAKENING CHECK: does the amendment weaken any existing guarantee?

VERDICT: NO WEAKENING FOUND, with one dependency flagged.

- F-9 (V3 156–157): untouched; the amendment restates it as its own premise and AM-A.4 routes
  post-crossing defects INTO F-9 void rather than around it. Strengthened, not weakened.
- F-10 output rules: untouched in every limb. AM-C.1's P7 change (|S| strata + merge record)
  moves cell counts UP (merging raises k toward F-10.c's k≥50), keeps the table aggregate-only
  and rowless, and adds the pre-merge populations and full merge record. It changes the SHAPE
  of one output line but does not weaken any F-10 guardrail. HC-4's own frozen sentence —
  "publications are per-stratum aggregates only (F-10)" — is preserved. (See RULING i.)
- HC-3: untouched (one human, error measured not adjudicated, sessions ≤50, signs never
  visible). AM-B's priors do not enter a, so HC-3's "machine never inside a" boundary holds.
- HC-4: untouched and expressly firewalled by AM-B.2; verified in code (check 3d). a, σ_a
  (shared-ε̂ derivative summed before squaring), and the population-weight form all unchanged.
  NOTE: AM-C.1 says HC-4 "runs over S" — consistent with HC-4's text, which is written over
  "strata," not over "nine"; but see RULING (ii) — the CODE disagrees even though the TEXT does
  not, and that disagreement is the implementability gap, not a weakening of HC-4's formula.
- Sealed key / HC-1H blinding / random parity / HC-7 triggers: untouched. AM-B records priors
  INSIDE the sealed commitment (:1018), which the amendment correctly notes makes the freeze
  post-hoc verifiable.
- K-8: untouched and honoured as a one-way door; the amendment is explicit that it authorises
  no crossing, no real χ, no fetch, no label.
- AM-A.3 does not loosen F-6: requiring positive Â_c is entailed by the frozen band (check 2),
  so it constrains rather than relaxes.

================================================================================
## RULINGS ON THE THREE ESCALATED QUESTIONS
("What Kun must rule on" — ruled separately and explicitly.)

### (i) P7 "9 strata" wording change — RULED: APPROVE, as a shape change, not a weakening.

P7 (V3 lines 414–415) freezes "per-stratum attenuation aggregates (9 strata, Wilson intervals;
never the per-label rows — 850 under HC-1H)." AM-C.1 changes this to "|S| strata plus the
pre-merge populations and the full merge record."

Ruling: the "9" in P7 is a SHAPE descriptor, not a load-bearing validity constant; the
load-bearing words are "per-stratum," "aggregates," and "never the per-label rows." Merging
raises every affected cell count (toward F-10.c's k≥50, not away from it), keeps the output
rowless and aggregate-only, and ADDS information (the merge record) rather than removing any
guarantee. HC-4 is written over "strata," so the estimator's form is preserved. I therefore
approve the wording change to "|S| strata (3 ≤ |S| ≤ 9) plus the pre-merge populations and the
full merge record." This approval is CONDITIONAL on RULING (ii): if no gated merge
implementation exists at the crossing, AM-C.2 governs and P7's "9 strata" stands unchanged
(because the run holds before any P7 exists). I decline the amendment's fallback framing only
insofar as it implies declining the wording change forces AM-C.2 unconditionally — the wording
change is approved; what governs is the implementation precondition, not the wording.

### (ii) Can the merge implementation be gated before the crossing, given HC1H_STRATA is a
### hardcoded nine-tuple at nm_handcheck.py:45–46? — RULED: YES in principle, but NOT on the
### evidence presented, and the line-pin is wrong at the pinned SHA.

Two facts first. (a) The pin is wrong: at the rehearsal-pinned harness SHA cc88fa5e…,
HC1H_STRATA is defined at line 49, not 45–46; lines 45–46 hold it in the CURRENT working copy
(SHA 65c04377…), which is a DIFFERENT, post-rehearsal revision. The amendment read the wrong
file revision for its load-bearing engineering claim. (b) The tuple is the least of it: the
nine-stratum requirement is enforced as a hard invariant in hc1h_statistics, hc1h_verdict,
allocate_neyman's key-match, the balanced injection allocator, and the sealed-commitment
recording (check 4c). A conforming merge crosses all of them.

Ruling: a merge CAN be gated before the crossing — there is no logical bar, and AM-C.3's
precondition is exactly the right test — but only as a NEW, separately-gated harness revision
with its own hash, its own fixtures proving the merge ladder byte-for-byte against AM-C.1, and
its own Kun gate; NOT as a patch represented as "supporting a merged stratum map" against the
current pin. Given the crossing timeline (Hwao's brief puts real-χ authorization after the
plumbing re-gates), this is achievable but not free. Until that gated revision EXISTS and is
hash-pinned, AM-C.2 governs by AM-C.3's own rule — and that is the safe default. I do not
recommend holding the crossing hostage to the merge implementation; AM-C.2 is a complete,
frozen, executable fallback.

### (iii) Is AM-A.4's FAIL_CLOSED consequence entailed by PC-1/PC-4, or a new freeze? — RULED:
### NOT ENTAILED. It is an ADDITION and must be frozen explicitly tonight.

Read PC-1/PC-4 (carried verbatim from the 08-12 draft into V3 §6):
  - PC-1 (as amended 2026-08-15) bars any post-delivery rotate / reproject / interpolate /
    resize / WCS transform — the "no further resampling of any kind" rule — and freezes the
    input contract. It forbids US from reorienting a delivered raster.
  - PC-3 requires per-object parity LOGGING (CD/PC·CDELT determinant, row-order determinant,
    combined pixel→sky sign, winding East-of-North). Logging, not gating.
  - PC-4 is the DISTORTION policy: fail-closed on SIP/PV/CPDIS/DET2IM keywords, or a tested
    local-Jacobian-sign receipt; no silent linear-determinant fallback. Its fail-closed branch
    is keyed to DISTORTION KEYWORDS, not to the PC-3 parity value.

Nothing in PC-1…PC-5 says "a delivered raster whose logged PC-3 parity is not the anchored
North-up / East-left reversing parity is excluded." PC-1 stops us from FIXING such a raster;
PC-3 makes us RECORD its parity; PC-4 fails closed on a DIFFERENT axis (distortion). The
amendment's own §1.6 consequence — such a raster is FAIL_CLOSED and excluded, never reoriented —
is the missing middle: it converts PC-3's log into a gate and PC-1's prohibition into an
exclusion. That is a real addition, and the amendment is right (§4 item 4) to flag that it
believes it entailed but submits it if not.

Ruling: NOT entailed. FREEZE IT NOW as an explicit addition, before the crossing. It is
well-formed, conservative (exclusion only, never reorientation), and closes the one hole AM-A.4
otherwise leaves: a real raster arriving with the wrong parity would currently be LOGGED and
then consumed, silently inverting every sign downstream. Because PC-1 forbids reorientation and
F-9 forbids post-crossing repair, the only safe pre-crossing rule is fail-closed exclusion.
Freeze it.

(For completeness on the receipt the amendment cites: YUI_BS5_SIGN_ANCHOR_20260814.md validates
the SYNTHETIC anchor raster's parity and states at its own line 56 that it does NOT substitute
for per-object PC-3 receipts on a real run — consistent with this ruling: the real-path parity
gate is presently unwritten.)

================================================================================
## REPAIRS REQUIRED (numbered, blocking)

1. (Check 1) Qualify the origin claim everywhere: BS-5 froze the SCIENTIFIC sign convention;
   AM-A.2 adds the OPERATIONAL polarity of the frozen weights. Remove any sentence that lets
   "already frozen" cover the operational polarity.
2. (Check 3b) Re-point the byte-for-byte verification to
   `_rehearsal_20260820/attempt3_hold/hc1h_neyman_priors.json` (SHA 4b6b7130…) and note that
   the root `_rehearsal_20260820/hc1h_neyman_priors.json` was overwritten by the later N=20,000
   rerun and does NOT contain the quoted values.
3. (Check 3c) Resolve the pool-source contradiction: either freeze the 2,000-object campaign as
   the prior source (matching the exercised evidence) or keep the full-pool freeze and re-verify
   end-to-end on full-pool priors. As frozen, AM-B.1's pool source is not the pool the
   byte-for-byte claim is demonstrated on.
4. (Check 4c / Ruling ii) Correct the HC1H_STRATA line-pin (49 at the pinned SHA, not 45–46)
   and restate §3.4 item 4 to name the ACTUAL merge surface: hc1h_statistics, hc1h_verdict,
   allocate_neyman key-match, the balanced injection allocator, and the sealed-commitment
   recording — not just the tuple. Make explicit that a conforming merge is a new hash-pinned
   harness revision requiring its own gate, and that AM-C.2 governs until it exists.

## NON-BLOCKING NOTE (not a repair)
The amendment's §3.6 item 3 pilot-mode floor observation is correct: pilot allocates 10 per
stratum at :710 without calling allocate_neyman, so a stratum < 10 members would under-fill
silently and surface as a count mismatch at :839. That is plumbing (a separate gate per the
kickoff), not a preregistration parameter, and is out of scope here.

## BOUNDARY
Real chirality labels computed: 0 · real χ read: 0 · real cutouts/tensors/positions/rows read:
0 · sky statistics: 0 · frozen files modified: 0 (V3 re-verified b06901c8…, mode 444; BS-5
re-verified b7c32dcf…) · network calls: 0 · publication/acceptance/freeze/commit/push: 0.
Computation performed: decimal/fraction arithmetic on rehearsal receipt numbers, exhaustive
merge-ladder simulation, and read-only code tracing of the pinned harness. Files written: this
report only.

Kun gates; Duho owns acceptance and the freeze. Repairs 1–4 are required before this amendment
can be gated PASS.

— Kun gate seat (kimi, Nous route), 2026-08-20.
