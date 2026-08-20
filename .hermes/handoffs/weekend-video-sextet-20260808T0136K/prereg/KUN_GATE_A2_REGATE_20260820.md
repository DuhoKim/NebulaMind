PASS_PREK8_AMENDMENT

# Kun gate seat (kimi, Nous route) — pre-K-8 amendment RE-GATE (Revision 2)
# Document gated: AMENDMENT_PREK8_20260820.md, Revision 2
# SHA-256 161547400e47ed66df616ba14756d9ab066c547f54b39bc161e6b4eaa26478c0 (recomputed at gate:
# match, 860 lines; Revision 1 was e832a341…, 562 lines). Repair receipt: CSEAT_AMEND_REPAIR_DONE.md.
# Prior gate: KUN_GATE_A_AMENDMENT_20260820.md (HOLD, four numbered repairs).
# Fresh one-shot; findings-only; no network; local files + python3 + local git object store only.
# Scope discipline: I re-gate ONLY the four repairs plus the integrity sweep. I do NOT re-litigate
# the firewall proof, the merge-ladder determinism simulation, the weakening check, or the three
# rulings — those passed and stand. Verdict: PASS. Nothing here authorises anything; Duho owns
# acceptance and the freeze.

================================================================================
## R1 — origin claim no longer lets "already frozen" cover the OPERATIONAL polarity

VERDICT: LANDED. The old framing does not survive anywhere.

Swept the full text for every construction that could blur the two freezes:
  grep -i "already frozen|already froze|was frozen|were frozen|did not choose|confirmed|merely|
           just confirm|confirmed the one"
Read every hit in context.

- §1.1 (lines 91–121) now separates the two by name: the SCIENTIFIC sign convention ("frozen
  2026-08-14 by BS-5 §3… AM-A.1 restates it") versus the OPERATIONAL polarity ("This was frozen
  nowhere before 2026-08-20. AM-A.2 freezes it, and AM-A.2 is new."). Line 120–121 states the
  guard sentence verbatim: "No sentence in this document may be read as claiming the operational
  polarity was frozen on 2026-08-14. It was not."
- The chain conclusion (§1.2, lines 172–184) is split into two bullets — scientific convention
  frozen 2026-08-14; operational polarity measured (Link 4) and frozen nowhere before 2026-08-20 —
  and adds "A confirmation of a binary fact is not a choice — but neither is it a pre-existing
  freeze."
- AM-A.2's header (§1.4, line 195) reads "the OPERATIONAL polarity (NEW — first freeze of this
  fact)" and line 202: "Origin: NOT previously frozen. First frozen by this amendment."
- Link 4 (line 156) now states it could have come out inverted, requiring a synthetic-side
  correction before the crossing.
- The only surviving "already-frozen" hit (line 540) refers to the HC-5 INCONCLUSIVE-BY-POWER
  consequence, not the polarity — correct usage. Every "frozen" hit otherwise attaches to frozen
  text/file/rule/pool/weights/V3/BS-5, none to the operational polarity as pre-existing.

The exact sentence the prior gate flagged ("The rehearsal did not choose the polarity; it confirmed
the one BS-5 already froze") is GONE. No sentence now lets "already frozen" reach the operational
polarity. REPAIR 1 SATISFIED.

================================================================================
## R2 — byte-for-byte verification re-pointed; root overwrite recorded

VERDICT: LANDED. File SHA, quoted values, and the overwrite note all verified independently.

- Pinned path: §2.3 (lines 390–391) now pins
  `_rehearsal_20260820/attempt3_hold/hc1h_neyman_priors.json`, SHA 4b6b7130…
  Independent recompute: `shasum -a 256` on that file =
  4b6b713044734a26af4fc27ee4a21ba72da9c19f807c63c366aace30bf5828df — MATCHES.
- Quoted values actually present: the file contains all three strings the amendment quotes —
  agree-confident|0 = 0.8447684391080617495711835334, agree-confident|2 =
  0.9991624790619765494137353434, low-confidence|0 = 0.875 — and the other six.
- Formula re-derived (not trusted): at Python decimal default prec 28,
  Decimal(2c+1)/Decimal(2(m+1)) on (492,582), (596,596), (31,35) reproduces all three quoted
  strings byte-for-byte. Jeffreys at prec 28 confirmed.
- Root overwrite: §2.3 lines 399–407 carry the boxed CITATION WARNING that the root
  `_rehearsal_20260820/hc1h_neyman_priors.json` was OVERWRITTEN by the later N=20,000 rerun, now
  hashes e9f47597…, and does NOT contain the quoted values. Independent recompute of the root file:
  SHA e9f47597afccd525e2d0aee4dbbb411d50c8457e8a407a331b8c2df33436d1c7 — MATCHES the warning, and
  its nine strings are entirely different (e.g. agree-confident|0 = 0.9724… vs the quoted
  0.8447…). The warning is accurate.

REPAIR 2 SATISFIED.

================================================================================
## R3 — pool-source contradiction resolved in ONE direction

VERDICT: LANDED. Resolved in one direction only, stated explicitly, no reading leaves both alive.

DIRECTION CHOSEN: the FULL-POOL freeze STANDS (the 12,000-candidate frozen synthetic injection
pool remains the prior source); the campaign alternative is rejected as non-executable.

- §2.3.1 (lines 409–441) is dedicated to the resolution. Line 417: "Resolved: the full-pool freeze
  STANDS; the byte-for-byte claim is downgraded to what it proves; and AM-B.3 adds the missing
  demonstration."
- The resolution is not left as a live choice. Lines 421–427 argue option (i) (freeze the
  2,000-object campaign) is "not executable in production at all": in production the campaign IS
  the accepted real population, no real object carries a truth_sign, so c_s (defined as agreement
  with truth_sign) is undefined over real rows — freezing the campaign would freeze a rule that
  cannot run, surfacing only after the crossing where F-9 forbids repair. This removes the choice
  rather than re-making it.
- AM-B.1's prior-source definition (line 371) is unambiguous: m_s counts objects in "the frozen
  synthetic injection pool." §5 item 1 (lines 771–777) reclassifies it from "a judgment, not a
  derivation" to a derivation ("the full pool is the only source that survives contact with
  production") and states the narrowed residual honestly: the pool source has never been exercised
  end-to-end, which AM-B.3 closes.
- The overclaimed byte-for-byte sentence from Revision 1 ("demonstrated to be exactly executable
  by the existing pinned code path") is expressly WITHDRAWN (line 441), and the claim is
  downgraded to what it proves (the formula and its Decimal serialization, lines 433–437).

EVIDENCE SUPPORT: the chosen direction is the correct one. My Check 3a/3c reconstruction in the
prior gate proved the nine strings reproduce only from the campaign populations
(582/571/596, 50/35/35, 35/61/35); those populations are synthetic and carry truth_sign. Real rows
genuinely carry no truth label — that is the entire premise of HC-1H — so c_s is indeed undefined
over them and the campaign cannot be a production prior source. The full pool is the only source
that survives contact with production, and AM-B.3 (§2.5) imposes a binding pre-crossing end-to-end
demonstration to close the residual. No surviving sentence keeps both the campaign and the full
pool alive as prior source. REPAIR 3 SATISFIED.

================================================================================
## R4 — HC1H_STRATA pin corrected; merge surface named in full; new-revision gate stated

VERDICT: LANDED. Pin, acknowledgement, five-site surface, and the new-revision/AM-C.2 statement
all verified against the git object store and the working copy.

- Pin correction and wrong-revision acknowledgement: §3.7 (lines 669–717) acknowledges the
  citation-revision error and corrects it FROM THE GIT OBJECT STORE. It states lines 45–46 are
  correct for the pinned cc88fa5e… and line 49 belongs to the current 65c04377….
  INDEPENDENTLY VERIFIED:
    git show 199c3168:…/prereg/handcheck/nm_handcheck.py | shasum -a 256
      -> cc88fa5ee6e7d7f2ab32ad4b7b0d7d843f9a77ed777c11d259755197eda03bbc (matches the pinned SHA)
      line 45 = HC1H_STATES = ("agree-confident","disagree","low-confidence")
      line 46 = HC1H_STRATA = tuple(f"{state}|{chi}" …)   <- HC1H_STRATA at 46 in the pinned rev
    current working copy shasum -> 65c04377…
      line 42 = from committee_state_vocabulary import HC1H_STATES
      line 49 = HC1H_STRATA = tuple(f"{state}|{chi}" …)   <- HC1H_STRATA at 49 in the current rev
  So the amendment's §3.7 attribution is correct, and (as it concedes) the prior gate's Ruling (ii)
  had the line attribution inverted — 45–46 is the pinned revision, 49 the current. The amendment
  records this correction with evidence rather than silently adopting it. The material finding
  (revision-ambiguous bare line numbers; merge surface far larger than a tuple) is the prior
  gate's and is accepted in full.
- Merge surface named in full: §3.4 item 4 (lines 612–639) names all five nine-stratum invariants
  in a table — hc1h_statistics, hc1h_verdict, allocate_neyman key-match, balanced injection
  allocator, sealed-commitment recording — with line numbers in BOTH revisions.
  INDEPENDENTLY VERIFIED at the stated lines in both revisions:
    hc1h_statistics nine-strata check   pinned 1450–1454 / current 1468–1472  (RAISES unless exactly nine)
    hc1h_verdict nine-strata check      pinned 1399–1400 / current 1417–1418  (RAISES unless exactly nine)
    allocate_neyman key match           pinned 3169–3170 / current 3187–3188  (set(prior_rates)==keys)
    balanced injection allocator        pinned 576 ff.   / current 597–599    (iterates HC1H_STRATA)
    sealed-commitment recording         pinned 1000      / current 1018       (writes neyman_prior_rates over HC1H_STRATA)
  All five resolve exactly as tabulated. (Repeat sampling at pinned 789 / current 807 also noted.)
- New hash-pinned revision + AM-C.2 governs: §3.4 (lines 633–639) states a conforming merge is "a
  NEW hash-pinned harness revision, requiring its own fixtures proving the AM-C.1 ladder
  byte-for-byte and its own Kun gate… It cannot be represented as a patch against the current pin.
  Until such a gated revision exists and is hash-pinned, AM-C.2 governs." §3.5 AM-C.3 (lines
  646–657) freezes both branches and states the crossing is not held hostage; AM-C.2 is the
  operative branch today.

REPAIR 4 SATISFIED.

================================================================================
## INTEGRITY SWEEP — is the ~300-line growth repairs + recorded rulings ONLY?

VERDICT: CLEAN. No new parameter, no changed threshold, no weakened guarantee, nothing silently
added beyond the four repairs and the three adjudications. This was the check that mattered most;
I attacked it as a smuggle surface.

Method: enumerated every AM-x parameter block and section header; extracted every numeric literal;
cross-checked each against the frozen sources; flagged every "NEW"/"withdrawn"/"downgraded"
marker and confirmed each maps to a numbered repair or a ruling.

(a) Freeze surface fully accounted for. The AM-x blocks are: AM-A.1 (restatement, not new), A.2
(new — the amendment's stated purpose), A.3, A.4, A.5 (expressly "not an amendment," a reading),
A.6 (NEW — Ruling iii), AM-B.1, B.2, B.3 (NEW — Repair 3, and expressly "a verification
requirement, not a parameter," line 488), AM-C.1, C.2, C.3. Every element flagged NEW is exactly
one of {AM-A.6 (Ruling iii), AM-B.3 (Repair 3)} or a repair section. Nothing else claims novelty.

(b) No new or changed threshold. Every numeric literal is one of:
  - frozen constants restated from V3/BS-9/LANA: 0.0408, σ_pub=0.011, σ_ours=0.004805, F-6 bands,
    a_s ≥ 0.70 (HC-5.2), k ≥ 50 (F-10.c), 500 real / 850 labels, 30 floor, 0.7905, 130_076 — all
    cross-checked against PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md and unchanged;
  - rehearsal receipt numbers carried from Revision 1 / the prior gate: 94.8%, 1,896/2,000, the
    nine prior strings, 28/8/11, ≥ 35, and the gate's derived σ_comb=0.012004, 3σ=0.0360, 0.0816,
    w_s≈0.00012, 208,407, ±0.00015, σ_a≈0.017–0.023 — none introduced as a parameter;
  - N=20,000 — the recorded rerun that overwrote the root priors file (a fact, not a parameter).
  No number is a new freeze; no frozen number was altered.

(c) No weakened guarantee. The "It does not change, weaken, relax, or reinterpret" list (§0,
lines 64–82) is intact and now scopes AM-A.6 as a custody exclusion that "adds an exclusion; it
removes no guarantee." The weakening-check conclusion (§4, lines 759–763) stands: F-9 strengthened
not weakened; F-10 untouched in every limb; HC-3/HC-4/sealed-key/HC-7/K-8 untouched; AM-A.3
constrains rather than relaxes F-6. AM-A.6 only removes objects and adds a funnel line — it grants
nothing. The only wording change to frozen output text is P7's "9 strata" → "|S| strata (3 ≤ |S| ≤
9) plus the pre-merge populations and the full merge record," which is Ruling (i)'s APPROVED shape
change, conditional on Ruling (ii) — i.e. a recorded adjudication, not smuggled scope.

(d) Growth is repairs + rulings. The ~298 added lines map to: §1.1/1.2 R1 rewrite; §1.7 AM-A.6
(Ruling iii); §2.3 R2 citation warning; §2.3.1 R3 + §2.5 AM-B.3; §3.4 five-site table + §3.7 R4;
§4 adjudications block; §5 reclassifications; §6 execution order. All are the four repairs or the
three recorded rulings. Nothing outside those categories was added.

(e) Frozen anchors untouched (re-verified at gate):
  V3        b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7  mode 444  MATCH
  BS-5      b7c32dcf12d9e147e5dee6a8262d925b61011615f2ee1d75d687600abb0a72ca            MATCH
  rehearsal 31d54b9d1ea14fb86f31ca1700a0a72ba3fa40c3d1945c7bd962361abf8877c1            MATCH
  priors    4b6b713044734a26af4fc27ee4a21ba72da9c19f807c63c366aace30bf5828df            MATCH

INTEGRITY SWEEP: PASS.

================================================================================
## NON-BLOCKING OBSERVATIONS (not repairs; do not gate on these)

1. The prior gate's Ruling (ii) line-pin attribution was itself inverted (45–46 is the PINNED
   revision, 49 the current one); the amendment's §3.7 is correct and records the correction with
   object-store evidence. The material finding stands regardless of direction. Noted for the
   record; it does not change the verdict.
2. §5 item 6 (NEW) flags a real open item: the working tree has drifted to 65c04377… while the
   rehearsal's evidence base was produced against cc88fa5e…, so AM-B.3's demonstration and
   AM-C.3's precondition must be evaluated against whatever revision is hash-pinned AT the
   crossing. This is correctly recorded as open and is plumbing/re-gate scope, not an amendment
   defect.
3. AM-A.5 (sign(0)=0) remains offered as a reading of F-1, not an amendment; the prior gate did
   not rule on it and it remains open for Kun. Not a blocker to this re-gate.

## BOUNDARY
Real chirality labels computed: 0 · real χ read: 0 · real cutouts/tensors/positions/rows read: 0 ·
sky statistics: 0 · frozen files modified: 0 (V3 re-verified b06901c8…, mode 444; BS-5 b7c32dcf…;
rehearsal report 31d54b9d…; priors 4b6b7130…) · network calls: 0 ·
publication/acceptance/freeze/commit/push: 0. Computation performed: SHA-256 recomputation; grep
sweeps; decimal arithmetic at default prec 28; read-only extraction of one historical blob from
the local git object store (no checkout, no branch/index change); read-only line verification of
the pinned and current harness. Files written: this report only.

Kun gates; Duho owns acceptance and the freeze. All four repairs landed; the integrity sweep is
clean. The amendment is ready to be gated PASS.

— Kun gate seat (kimi, Nous route), 2026-08-20.
