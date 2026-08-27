# PREREG TEXT REFEREE, ROUND 2 — KIMI

Subject: `../PREREG_SUCCESSOR_DRAFT_V11_20260827.md` (601 lines, §0–§10; the brief's "490
lines" is stale — V10 was 490), reviewed as a fresh promise, not as a diff of V10.
Round: BRIEF_PREREG_TEXT_V11, 2026-08-27. I did not read `/Users/duhokim/NebulaMindData/`.
I read the round-1 reports only after forming my own reading of V11. Every digest, constant, fixture name and quoted number I assert as
*verified* was recomputed from the files on disk during this review; what I could not
recompute is under Testimony.

## What verifies (so the findings carry their weight)

- §0 pins, recomputed: `successor_ref_v9.py` sha256 `6a9abbbd…c148`, `closure_worker_v9.py`
  `28f8e1f9…5959`, `FIXTURES_V9_20260826.out` `fab32ba2…a8b5`, referee report
  `f2ee062b…2f01`, superseded V9 draft `b97ba35c…19b6` — all exact; the v9 code files are
  mode `-r--r--r--` on disk.
- The §2.4 repair (KIMI-V10 F3): code line 154 `PINNED_PLANNER_DIGEST =
  1617af00eb7398abd93cc2726dbfb1ecfb24d07bede4b84c128ef2442bf40cb4`; V11 now quotes
  `1617af00eb73…` — the repair is exact. The probe receipt's closure rows carry the same
  value. Universe pin `863e5ded…` / 366,912 bricks / release total 832,393 — all in the
  code and all match §2.4/§2.6/§10.
- The three numeric corrections, recomputed from the artifacts: **951** of 1,000 own
  p-values sit at the 4.99975e-05 floor of `STAGEP_EXACT_RECEIPT_20260826.json`
  (`p_own_by_trial` counted by me; 995 total successes, 5 failures), **2 of 12** audited
  boundary successes refuted with 10 confirmed (`FIXTURES_V9` line 25,
  `PWR-SELF-VERIFYING`), and the planner digest above. All three repairs are exact.
- Stage-P exact receipt: 995 successes vs the frozen x ≥ 962 rule, `passes_rule: true`,
  431.4 s, 20,000 perms × 1,000 trials, zero trials granted by exactly one null,
  harness sha `daed15c7…` == on-disk `stagep_exact.py`, oracle/selection input digests
  == on-disk files; `stagep_exact.log` agrees. Shared-null comparison z = 3.1220 matches
  §2.6, as do 3.1672/3.1957 (geometry receipt's round-8 FAIL section).
- Clopper–Pearson, my own recomputation (incomplete beta): x = 961 → LB 0.949366 (< 0.95,
  fails); x = 962 → LB 0.950487 (≥ 0.95, passes). The frozen integer is exactly the
  stated contract.
- §2.6 geometry vs `REAL_GEOMETRY_RESULT_20260825.md` and the receipt: 366,912 / 270,577 /
  96,335 / 832,393, Var(cosθ) 0.445201; 6,445 bricks, 65,060 raw, 53,005 retained,
  Var 0.754664, N_eq = 3·53,005·0.754664 = 120,002.88 (receipt: 120002.8798); declined
  run 60,308 / 208,407 / 0.0580 / 36,253 / 735.9 GB; 12,117/6,445 = 1.8801×;
  12,117 × 12.2 MB = 147.83 GB ≈ the quoted ≈147.8/148 GB; closure `plan_digest
  aaeaa9f3…b3f1` == probe receipt `derived_manifest` (objects 65,060, required 12,117,
  selected 6,445); 34/34 probes conforming, 13 verify hooks, nine known-open items — §7's
  BS-2m row matches the freeze record.
- §1 anchor, re-verified from the publisher's abstract page this round
  (doi:10.1016/j.physletb.2011.04.008): 15,158 spirals, "−0.0408 ± 0.011". Constants in
  the v9 bytes all match the text: `A_LONGO = +0.0408`, published −0.0408, `N_PERM =
  100,000`, `CP_PASS_X = 962`, p thresholds 0.001/0.05, `A_FLOOR = 0.85`, `RETENTION_LB =
  0.8572`, `FLOOR_MULT = 3.09`, `NEQ_MIN = 100,000`, `PWR_CONSERVATISM = 1.01`,
  `BRANCH_FALLBACK_DATE = "2026-09-05"`, `FROZEN_ENV` python 3.9 / numpy 1.26.4 / little.
- v7→v9 diff, for F7 below: confined to `closure_receipt()` (worker filename plus
  `worker_provenance` plumbing). Every primitive the exact harness touches
  (`_planning_mask`, `retained_counts`, `inject_signs`, `perm_record`, `sse`, and the
  stage/role/threshold constants) is byte-identical between the receipt's v7 subject
  (sha `6be341bd…` == on-disk v7) and the pinned v9 — so the 995/1000 transfers. That is
  my verification, not the text's disclosure.
- §6.1(5)'s checkable claim, checked by inspection: `REAL_GEOMETRY_RESULT_20260825.md`
  contains counts, geometry, selection and synthetic-injection power only — no real
  χ-derived quantity anywhere in it.
- Falsifiability structure (question 1), unchanged from V10 and still sound: the four
  outcome labels partition the space, boundary p-values fall into INCONCLUSIVE as
  declared, only pinned code emits a verdict, REJECTED-AT-LONGO-AMPLITUDE is a named,
  reachable failure of the claim.

## Numbered findings

### F1 — BLOCKING — §6.1(2) names an unblinding order that contradicts §6.1(1), §4, §5 and §7

**Section / sentence.** §6.1(2): "…may decrypt, query, render, summarise or inspect any
χ-bearing object or derivative **until the lock, unblinding and BS-5f have occurred in that
fixed order.**"

**Why it fails as a promise.** The listed order is lock → unblinding → BS-5f, and it is
wrong twice over against the document's own definitions. §6.1(1) defines the primary lock
as the moment at which, inter alia, "BS-5f's confirmatory power receipt exists" — so BS-5f
must *precede or coincide with* the lock, not follow unblinding. §4 states Stage C (BS-5f)
runs "after inference, **before unblinding**" and that a FAIL halts the run
pre-unblinding; §7's BS-5f row blocks "unblinding"; §5's runner "requires a BS-5f Stage-C
receipt bound to that exact mask digest … and only then runs the full
100,000-permutation record". The only order consistent with the rest of the document is
BS-5f → lock → unblinding. As written, (2) licenses an unblinding that precedes the
confirmatory power gate — the exact event §4 says must halt the run — and a person held to
this text can quote (2) against §4 with equal force. This is the operative sentence of the
flagship repair to the unanimous round-1 blocker, and it is internally inconsistent at
the point it governs. Conduct prose has no code to arbitrate it; §0's "code wins" rule
does not reach §6.1.

**Smallest sufficient repair.** Rewrite (2)'s final clause: "…until BS-5f's confirmatory
power receipt exists, the primary lock is sealed, and unblinding has occurred, in that
fixed order." One sentence; no mechanism change.

### F2 — BLOCKING — the header still calls the predecessor's 208,405 sealed χ "successor input"; §6.2 says "it is not an input"

**Section / sentence.** Header (line 22): "its verified 60,308-brick sample and 208,405
sealed χ measurements are archived as **successor input**." §6.2: "The archive is retained
as historical record and as a subject of §6.1; **it is not an input.**"

**Why it fails as a promise.** KIMI-V10 F2 blocked on this exact header phrase because
"successor input" assigns 208,405 already-measured outcomes an undefined role beside a
redesign whose legitimacy rests on outcome-blindness. V11 added §6.2 — a clean, complete
repair — and left the sentence it was repairing untouched. The document now asserts both
"X is input" and "X is not input" about the same sealed measurements, one in its second
paragraph and one in §6.2. A later reader justifying reuse quotes the header; a later
reader forbidding it quotes §6.2. A frozen promise cannot contain both. The repair was
aimed at the right target and did not reach it.

**Smallest sufficient repair.** Strike the header phrase: "…are archived as sealed
historical record; no predecessor χ measurement enters this run's analysis (§6.2)." One
clause; no mechanism change.

### F3 — MAJOR — §2.4 and §10 cite closure fixtures that exist in no pinned v9 artifact

**Section / sentence.** §2.4: "…a manifest omitting those neighbours is refused **by
name**: `CLOSURE-FROZEN-PLANNER`, `CLOSURE-RETIRED-REFUSES`, `CLOSURE-CATCHES-HISTORICAL`,
`CLOSURE-CALLER-TRUST` (3/3 — self-consistent shortened parent, shortened universe,
unpinned universe digest)." §10's repair table: "new fixture
`CLOSURE-PRODUCTION-USES-FROZEN` asserts the wiring by source inspection."

**Why it fails as a promise.** I searched the pinned fixture transcript
(`FIXTURES_V9_20260826.out`), the pinned probe suite (`closure_probe_suite_v9.py`), the
probe receipt, and every older transcript on disk. Of the four names in §2.4, only
`CLOSURE-RETIRED-REFUSES` exists in the v9 battery. `CLOSURE-FROZEN-PLANNER` appears only
in the V4/V5 transcripts and was dropped in V6+. `CLOSURE-CATCHES-HISTORICAL`,
`CLOSURE-CALLER-TRUST` and §10's `CLOSURE-PRODUCTION-USES-FROZEN` appear in no artifact
of any version — only in drafts and old gate prose. Worse, the v9 battery's only planner
check is digest-only (`CLOSURE-PINNED-PLANNER`); no pinned v9 check functionally runs the
planner over the two historical objects (which, as the mechanism referee noted, are not
rows of this run's parent), and no pinned v9 probe carries the "3/3" caller-trust battery
the parenthetical describes. The underlying claims are supported elsewhere (the probe
receipt's real-data 12,117 derivation; the referee's ad-hoc verification, carried in §10
as referee-confirmed) — but the sentence attributes them to named checks the frozen
mechanism does not carry. This is the same failure class as round-1 F3 (a citation naming
bytes the mechanism no longer uses), sitting in the very paragraph V11 rewrote to repair
that class, and all three seats missed it in V10, which carried the identical sentence.

**Smallest sufficient repair.** Cite what exists: `CLOSURE-PINNED-PLANNER` (digest), the
probe receipt's real-parent derivation, and the referee's ad-hoc functional verification
named as ad-hoc — or restore functional planner/caller-trust fixtures to the battery at
the next code revision and then cite them.

### F4 — MAJOR — §6.1 binds the powerful and names the holders, but leaves three compliant paths to early outcome knowledge

**Section / sentence.** §6.1(2): "**Who may hold read access.** Only named key holders,
recorded in BS-V's schema before any image byte. **No person or process able to alter this
text, fill or adjudicate a class-P slot, construct the accepted mask, or operate the lock
may** decrypt, query, render, summarise or inspect…" §6.1(3): "Every decryption, query and
read against the sealed store — successful or refused — appends to a log…" §6.1(4):
"Unauthorised access voids the run…"

**Why it fails as a promise.** The repair is real — holders named, the powerful barred,
logging required, void rule, a checkable sentence, redesign evidence named. It is no
longer an embargo. But as written it still prices in three paths:
(i) *The key-holder path.* The inspection ban is scoped to the powerful roles; the
read-access grant is to named key holders. A named holder outside those roles may read
any χ-bearing object before the lock: the read is logged (visible) but *authorised*, so
(4)'s void does not attach. The text permits by design the event it exists to prevent,
for exactly the people holding the keys.
(ii) *The producer path.* "Blind automation is permitted only where named here" names no
automation anywhere — not the instrument writing χ into the store, not the cutter, not
the Stage-C runner, not the ledger recompute — and the hand-check committee, the one
group that must render χ-bearing cutouts pre-unblinding to produce the BS-8f labels, is
not named either, and no store is declared for their χ-derived labels against (3)'s
checkable sentence ("no χ-derived artifact exists outside the sealed store before the
primary lock"). Either the audit labels live outside the seal (the sentence is false by
design) or the committee operates unaddressed by the covenant that governs everyone else.
(iii) *The log-bypass path.* The log records every decryption that flows through the
logged path; nothing states that decryption is *impossible* outside it (key escrow,
split custody, or a ceremony that is the only technical means of read). If a holder can
use a key directly, an unlogged read leaves no trace, and the text's own test — "what
would show it?" — has no answer for that case. The void rule cannot bite on an invisible
event.
A wriggler would not need to break a rule; each path is compliant with the letter.

**Smallest sufficient repair.** Three clauses: "No person, including key holders, may
decrypt or inspect any χ-bearing object or derivative before the lock; custody confers
capability for the lock ceremony only, and any pre-lock read, authorised or not, voids
the run." Name the permitted producers (instrument, cutter, Stage-C runner, ledger
recompute, hand-check committee) with the condition that their outputs enter the sealed
store directly and never leave it. State the technical means by which the log is complete
(or state plainly that completeness rests on custody and say who holds that risk).

### F5 — MAJOR — the §7 slot table drifted from the V11 repairs: three promised fields have no schema home

**Section / sentence.** §6.1(2): key holders "recorded in BS-V's schema before any image
byte." §6.1(3): the access-log digest "is receipted at BS-2f and again at BS-V." §2.7(5):
"The thresholds in (d) are pinned before any image byte, **in BS-3**…" Against §7: BS-V's
row reads "verdict + primary lock: `decide()` output, evaluated floor, path taken, mask
digest" — no key-holder roster, no log digest. BS-2f's row reads "sealed
accepted-position mask + sealed calibration boundaries" — no access-log digest. BS-3's
row reads "instrument identity: weights `83008c1c…`, τ = 4.4006456017494235, antisymmetry
identity" — no exclusion-confidence threshold.

**Why it fails as a promise.** Three V11 promises assign artifacts to slots whose declared
schemas do not contain them. A producer can fill BS-2f, BS-3 and BS-V in full conformance
with the table while omitting the log digest, the exclusion threshold and the key-holder
roster — and the gate reading the table would pass them. The repairs bound the conduct;
the table that a filler actually executes against was not updated to carry them. This is
the repair round's own defect shape: new obligations written in prose, not wired into the
schema they bind.

**Smallest sufficient repair.** Extend the three rows: BS-2f "+ access-log digest
(§6.1(3))"; BS-V "+ key-holder roster + access-log digest (§6.1(2–3))"; BS-3 "+ exclusion
confidence threshold (§2.7(d))".

### F6 — MAJOR — carried, unrepaired: §4's z* sentence is still contradicted by the pinned fixture (KIMI-V10 F6)

**Section / sentence.** §4: "across four geometries the measured z\* ranged
3.0376–3.1355, bracketing the normal 3.0902, and on the polar geometry this design
actually selects the normal threshold came out anti-conservative."

**Why it fails as a promise.** The pinned v9 fixture prints the four z\* values: 3.0694,
3.0010, 3.0020, 3.0260 — range 3.0010–3.0694, every one *below* 3.0902. They do not
bracket the normal value, and 3.0376/3.1355 appear in no artifact. The identical false
sentence also sits in the pinned code's own docstring (lines 1164–1166) — definitional
surface in a document that pins code by digest. The sentence's *conclusion* survives via
the same battery's `PWR-Z-STABLE` tail masses beyond z = 3.090 (0.00135, 0.00130,
0.00100, 0.00110 — three of four heavier than nominal), which the text never quotes.
V11's preamble claims three numeric corrections "because a preregistration that
misquotes its own receipts has no standing to demand accuracy of anyone else"; this is a
fourth, named in round 1, carried verbatim.

**Smallest sufficient repair.** Quote the artifact: "the four fixture geometries'
standardized 0.999 quantiles measured 3.0010–3.0694, and tail mass beyond the normal
3.0902 measured up to 0.00135 (`PWR-Z-STABLE`) — the normal threshold is not safe either
way." Carry the same edit into the code docstring at the next code revision.

### F7 — MAJOR — carried, unrepaired: the exact Stage-P receipt's subject is v7 bytes, and V11's disclosure still does not say so (KIMI-V10 F7; GPT56-V10 F3; CODEX-V10 5)

**Section / sentence.** §2.6: "`stagep_exact.py` is a measurement harness; the exact-null
Stage P is not implemented in the file §0 pins." §10: "it is measured, not accepted."

**Why it fails as a promise.** The receipt's `subject` is `../ref/successor_ref_v7.py`,
sha `6be341bd…` — not the v9 bytes §0 pins. "Not in the pinned code" and "measured
against a different, unpinned version of the reference" are different disclosures; the
text makes the first and withholds the second. I re-verified the gap is benign this
round: the v7→v9 diff is confined to `closure_receipt()`'s provenance plumbing, and every
primitive the harness calls is byte-identical, so the 995/1000 transfers to the pinned
bytes. But that is the referee's work, done twice now, and the promise should not require
the next reader to repeat it to trust the design's decisive number.

**Smallest sufficient repair.** One sentence in §2.6: "the harness ran against v7; every
primitive it calls is byte-identical to the pinned v9 (the v7→v9 diff is confined to
`closure_receipt()`), so the measurement applies to the pinned code; it remains
unrefereed and BS-5p stays unfillable until folded in."

### F8 — MAJOR — carried, unrepaired: the Branch-A availability event has no frozen probe (GPT56-V10 F5; CODEX-V10 3 ¶2)

**Section / sentence.** §2.1: Branch A is selected "iff the DR11 photo-z product exists
and is publicly retrievable at the resolution moment"; BS-1 is filled on "the day DR11
photo-z is confirmed available" or 2026-09-05.

**Why it fails as a promise.** V11 repaired CODEX 3's hard contradiction (Branch A now
voids the §0 pin and demands a fresh gate — good, and `BRANCH_FALLBACK_DATE` is pinned in
code) but not the epistemic event. "Exists," "publicly retrievable" and "confirmed" have
no frozen probe, endpoint set, schema check, retry/error policy, timestamp convention or
responsible witness. Before 2026-09-05, delaying or avoiding a check delays the earlier
event; a transient mirror or auth failure turns existence into apparent absence. An
operator can steer the branch while satisfying every word, and the choice changes which
preregistration exists. This is a researcher degree of freedom over the answer, exercised
before any image byte but after all measurements that make Branch B look settled.

**Smallest sufficient repair.** Freeze the probe: named authoritative URLs/products, the
schema/version check that constitutes "exists", retry window and transient-error
treatment, timestamp/zone, signed raw-response receipt; BS-1 a pure function of that
receipt.

### F9 — MAJOR — carried, now thrice requested: no binding interpretation of what an answer means (KIMI-V10 F10; GPT56-V10 F4; CODEX-V10 4)

**Section / sentence.** §1: "It does not test A ≈ 0.02, Shamir, BHU, or whether the sky is
isotropic." §5 defines the four outcome labels and stops.

**Why it fails as a promise.** All three round-1 seats asked for this paragraph; the
brief's question 7 asks it again. The text never states that REJECTED-AT-LONGO-AMPLITUDE
excludes the published amplitude at the published axis under this design's sensitivity —
and nothing more: not isotropy, not smaller amplitudes, not other axes or other
researchers' claims. It never states that every INCONCLUSIVE* supports neither
reproduction nor rejection. It never states that "REPRODUCED" means 3σ compatibility with
the published estimate (a precise Â = 0.020 at p < 0.001 is REPRODUCED-LONGO under the
frozen regions — defensible, but only if the label's meaning is bound). And a precise
opposite-sign result (Â < 0, p < 0.001) lands in INCONCLUSIVE — a strong anti-Longo
result wearing a label that reads as "no result", with no sentence saying so. The
companion essay (`WHAT_IS_AT_STAKE_20260827.md`) carries these limits almost verbatim;
the promise does not. A later summary can quote the registered outcome verbatim and
overread it, and nothing in the binding text forbids the overreading.

**Smallest sufficient repair.** Two sentences in §5 plus the BS-V results template:
"REJECTED-AT-LONGO-AMPLITUDE excludes the published amplitude at the published axis under
this design's sensitivity. It does not establish isotropy, does not exclude amplitudes
below this design's floor, and does not speak to other researchers' distinct claims; no
INCONCLUSIVE* outcome supports either reproduction or rejection, and a precise
opposite-sign estimate is a strong anti-Longo result, not an absence of one."

### F10 — MINOR — carried (CODEX-V10 6, remainder): undefined class-E judgment calls outside the repaired lock

**Section / sentence.** §7 BS-8f: "…full Cov_a, **integrity triggers**"; §2.5/BS-6:
checksum list "cross-checked" with no mismatch/retry disposition; §6: HC "committee,
sealed keys, HC-5, HC-6" carried "by quotation at freeze" (BS-8p).

**Why it fails as a promise.** §6.1(1) repaired the largest piece (the lock definition).
The rest remain choices exercised after images or labels exist: which integrity event
halts, how a missing/mismatched producer checksum is handled, committee adjudication and
key custody. BS-8p and BS-9 are now DESIGN slots requiring fresh gates, which covers the
rule-making at gate time — but the fields' semantics are still unfrozen here.

**Smallest sufficient repair.** Enumerate integrity triggers and outcomes, the
checksum-mismatch/retry policy, and the committee/adjudication rules in the pre-freeze
text or their slot schemas, with each failure mapped to void / halt-inconclusive /
repairable.

### F11 — MINOR — carried (CODEX-V10 7; GPT56-V10 F6 part): §2.6's closing sentence still overstates what the measurements do

**Section / sentence.** §2.6: "**These fill the class-P inputs** that six gate rounds said
could not be closed by writing alone."

**Why it fails as a promise.** Under V11's own VALUE/DESIGN language, the §2.6
measurements fill nothing: BS-5p and BS-2f are DESIGN slots these values cannot fill, and
the only filled slot (BS-2m) is not a §2.6 product. Eleven of twelve class-P slots stand
unfilled; the sentence reads as if the geometry run stocked the table.

**Smallest sufficient repair.** "These provide measured candidate values for still-
unfilled class-P slots; one of twelve is filled (BS-2m)."

### F12 — MINOR — carried (CODEX-V10 8): §0 names the fixture transcript without its digest

**Section / sentence.** §0: "fixture output `ref/FIXTURES_V9_20260826.out`" — no sha,
between two full-sha pins.

**Why it fails as a promise.** A reader following only the definition section cannot tell
which transcript was frozen. Recomputed this round:
`fab32ba24cedcedf7fe601c3a8d9dbde13f57b1c9bf2e0b88963bcfebc33a8b5`.

**Smallest sufficient repair.** Add the digest and state whether the transcript is
normative or validation evidence.

### F13 — MINOR — §4 carries the superseded shared-null contract with no in-section demotion marker

**Section / sentence.** §4: "Stage P therefore measures the standardized permutation null
once per prefix … and judges all 1,000 trials against that full empirical tail, with each
trial's statistic deflated by PWR_CONSERVATISM…" — the operative-looking mechanism text,
unmarked. The supersession lives only in §2.6's blockquote ("§4's shared-null contract is
superseded and is retained below only as the description of what the currently pinned
code does").

**Why it fails as a promise.** The promise is now single-valued — the exact per-trial
test — and BS-5p is correctly a DESIGN slot that cannot be filled from the existing
receipt, so GPT56-V10 F3 / CODEX-V10 5 are substantively repaired. But a reader of §4
alone meets a different counting path presented as the stage's definition, and the
self-verification machinery (boundary re-confirmation, deflation) is left ambiguous
between "superseded" and "surviving". The PASS rule (x ≥ 962) is route-neutral and
survives cleanly; nothing else in §4 says which route it serves.

**Smallest sufficient repair.** One sentence at §4's Stage-P head: "the counting path
below describes the currently pinned code and is superseded by §2.6's exact per-trial
promise; the x ≥ 962 rule stands."

### F14 — MINOR bundle (carried; small, same-edit repairs)

- **KIMI-V10 F9 unrepaired.** §0's "every operational mechanism … is DEFINED by the code
  bytes" and §2.3's "the result is exactly what the frozen procedure returns" still cover
  the production scale at which the pinned O(n²) chain cannot execute (§2.6's own
  disclosure: vectorized equivalents, 40/30/400-case batteries, "not proven in general").
  One sentence in §0: at production scale the artifact is produced by validated
  equivalents and bound by output digest at BS-2s; the frozen chain is the normative
  definition, not the executed one.
- **KIMI-V10 F11 unrepaired.** No public deposit or external timestamp for the freeze is
  specified; custody remains git + the lane's own gates as witnesses. One clause naming
  the deposit cited in BS-V's receipt.
- **Receipt disagreement unflagged.** §2.6 now says 951 at the floor (correct);
  `REAL_GEOMETRY_RESULT_20260825.md`'s "Stated limits" still says 995. Receipts are
  historical and should not be rewritten — add a one-line flag in §2.6 that the cited
  receipt's stated-limits figure is superseded by its own `p_own_by_trial` (951).
- **208,405 vs 208,407, still unreconciled.** Header: "208,405 sealed χ measurements";
  §2.6's declined-run row: "208,407 objects". Consistent with the two-WAITING narrative
  (208,407 raw − 2 = 208,405 sealed); the text never says so. One parenthetical.
- **`RETENTION_LB = 0.8572` provenance still unstated.** Frozen and verified; the promise
  never says where it came from. One clause.
- **BATTERY-POS quoted as "p = 2.2e-21"** (§5) vs the fixture's "p = 2.23e-21".
  Truncation, not error; quote the fixture's digits.
- **No "no secondary endpoints" sentence.** `explore_verdict()` exists in code; the text
  never states that no analysis outside `run_production_verdict()` will be presented as
  the preregistered result. One sentence.

## Answers to the brief's eight questions, compressed

1. **Can it fail?** Yes — unchanged from V10 and still sound: the outcome space is
   partitioned and boundary-closed, only pinned code emits the label, the void rule bans
   post-χ edits, and REJECTED-AT-LONGO-AMPLITUDE is a reachable, named failure. The soft
   spot is interpretive (F9), not structural.
2. **Degrees of freedom.** The release fork's date is bound in code but its trigger event
   is not (F8). Acceptance/exclusion is now closed at the text level (§2.7: partition
   identity, closed reason list, sign-blind predicates, ledger recompute, pre-image
   thresholds) — I could not find an operator path through it as written; its
   implementation is a disclosed DESIGN slot. The residual open choices are the eleven
   unfilled slots (declared, producer-named) plus the disclosed set — and the covenant
   paths in F4 and the schema drift in F5, which are new this round.
3. **Circularity.** None in the forbidden direction, as in V10: Stage P injects at the
   frozen amplitude on count-derived geometry; Stage C runs on the sealed sign-free mask;
   the detection floor is a frozen formula evaluated at a named measured point; the
   selection is geometry-and-counts only. No boundary rule depends on the data it judges.
4. **Numbers vs artifacts.** The three advertised corrections verify exactly (951; 2 of
   12; `1617af00eb73…`). The brief said to assume more remain: F6 (z\* range, carried)
   and F3 (dead fixture names, new) are them. Everything else quoted that I could
   recompute — digests, geometry, closure, CP boundary, arithmetic — verifies.
5. **Is the blinding real?** Structurally much stronger than V10: lock defined, holders
   named, powerful barred, log required, void on unauthorised access, redesign evidence
   checkable — and I checked the redesign record: no χ-derived quantity in it. But the
   covenant's operative sentence contradicts the document's own chronology (F1), its
   scope leaves a compliant read path for the very key holders it names (F4), and the
   header still assigns the predecessor's sealed outcomes an input role §6.2 denies
   (F2). What would show a look today: the log, for paths that flow through it; nothing,
   for a holder who bypasses it.
6. **Honest incompleteness.** Still mostly exemplary — the draft banner, VALUE/DESIGN
   distinction with a 1/12 count at the table, the retraction chain, "measured, not
   accepted". The exceptions are F11 ("fill the class-P inputs"), F7 (the v7-subject gap
   inside an honest disclosure) and the carried F9-in-§0 overstatement (F14).
7. **Null-result overclaim.** No overclaim anywhere — the gap remains omission (F9), now
   asked by all three seats and by the brief itself.
8. **Missing entirely.** The interpretation paragraph (F9), the availability probe (F8),
   the public deposit (F14), the committee's place in the covenant (F4) — none needs the
   machinery reopened, and all are invisible if you only referee the machinery.

The brief's five known-wrong items: confirmed accurate as stated; none understated. On
item 5, one shading: the one-seat verdict's own first line is "**CLEAR** — with
conditions named below"; V11 §0/§7 quote it as CLEAR while carrying the nine conditions
in the same rows — disclosed, but the quote is stronger than the artifact's verdict line
by one qualifier.

## Testimony (asserted in the text or receipts; not independently verified by me)

- The predecessor documents quoted by sha (V3-pred `b06901c8…`, BS6-pred `5ff7f454…`,
  decline memo `b4a1f1fc…`): existence and contents outside the review set; the eight
  Cut-6 predicates' byte-identity to BS6-pred accepted, not checked. The 208,405 sealed
  count itself (the two-WAITING reconciliation is narrative).
- BS-3 instrument values (weights `83008c1c…`, τ = 4.4006456017494235, antisymmetry
  identity) — unfilled slot, quoted in the table.
- "DR11 pages exist; no photo-z product is present" (measured 2026-08-24) — author's
  measurement; F8 exists because the probe that would change this is unfrozen.
- Equivalence batteries: 40 (order), 30 (reduction), 400 (swap phase, referee's own seed
  and regime) cases, zero mismatches — stated in the geometry receipt and §10; no
  independent receipt in the named set.
- "12,117 reproduced independently three times" — the closure row is in the probe
  receipt; the two direct enumerations are asserted in §2.6/§7 and the mechanism
  referee's report.
- 12.2 MB/brick unit price and the 735.9 GB declined download — predecessor-era figures.
- The conduct narrative (drafting authorization, catalog-only authorization, "no χ was
  read", the 2026-08-26 ceiling raise, provider refusals of the two mechanism seats, the
  2026-09-05 fork status) — conduct testimony; nothing in the artifacts contradicts it.
- "V4 through v7 remain on disk unchanged" — the files are present; content-unchanged
  accepted from the mechanism referee's spot checks, not re-digested by me this round.

## Verdict

The six advertised repairs are real and, where numeric, exact: the planner digest, 951,
and 2-of-12 all verify; §2.7 closes the acceptance hole at the text level; the Stage-P
promise is single-valued with BS-5p correctly a DESIGN slot; §2.1's Branch A now voids
the pin rather than pretending neutrality; §6.1 is blinding in structure, not merely an
embargo. But the repair round did what this lane's repair rounds do — it introduced new
defects at the points it touched. Two are blocking: **F1** (§6.1(2) names an unblinding
order that contradicts §6.1(1), §4, §5 and §7, placing the power gate after unblinding)
and **F2** (the header still calls the predecessor's 208,405 sealed χ "successor input"
while §6.2 says they are not an input — the round-1 blocker survives in the document's
second paragraph). Both are one-sentence text repairs; neither requires reopening the
frozen mechanism. F3–F9 must be repaired in the same revision; F10–F14 should be.

**NOT CLEAR**
