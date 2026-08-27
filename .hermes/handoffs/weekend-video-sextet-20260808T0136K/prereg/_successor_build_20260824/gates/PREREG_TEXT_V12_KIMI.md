# PREREG TEXT REFEREE, ROUND 3 — KIMI

Subject: `../PREREG_SUCCESSOR_DRAFT_V12_20260827.md` (655 lines, §0–§10), read as a fresh
promise per the brief's instruction — a fixed sentence is a new sentence. Round:
BRIEF_PREREG_TEXT_V12, 2026-08-27. I did not read `/Users/duhokim/NebulaMindData/`. I read
the round-2 reports (all three seats) before forming this round's findings, and every digest,
constant, fixture name and quoted number I assert as *verified* was recomputed from the files
on disk during this review; what I could not recompute is under Testimony.

## What verifies (so the findings carry their weight)

- §0 pins, recomputed: `successor_ref_v9.py` sha256 `6a9abbbd…c148`, `closure_worker_v9.py`
  `28f8e1f9…5959`, `FIXTURES_V9_20260826.out` `fab32ba2…a8b5` — all exact; both v9 code files
  are mode `-r--r--r--`. Referee report `CLOSURE_V9_KIMI.md` sha `f2ee062b…2f01` exact.
  v4–v7 present on disk.
- In-code constants, re-read from the pinned bytes: `A_LONGO = 0.0408`,
  `A_LONGO_PUBLISHED_SIGNED = −0.0408`, `N_PERM = 100,000`, `CP_PASS_X = 962`,
  `A_FLOOR = 0.85`, `RETENTION_LB = 0.8572`, `FLOOR_MULT = 3.09`, `NEQ_MIN = 100,000`,
  `PWR_CONSERVATISM = 1.01`, `MC_CAL_PERM = 20,000`, `CUTOUT_PIX = 128`,
  `CUTOUT_PIXSCALE_ARCSEC = 0.262`, `BRANCH_FALLBACK_DATE = "2026-09-05"`, FROZEN_ENV
  3.9/1.26.4/little. All match the text.
- The tested axis: `AXIS = [−0.676971771271432, −0.509846551777774, +0.530816083537352]`
  converts to ICRS RA,Dec = (216.98444°, +32.06061°); Longo's published (l, b) = (52°, 68.5°)
  converts (rotation checked against astropy) to (216.98443°, +32.06061°) — angular distance
  ~1e-6 deg. The pin IS the published axis. Substance sound.
- Clopper–Pearson, own recomputation: x = 961 → LB 0.949366 (fails); x = 962 → LB 0.950487
  (passes). The frozen integer is exactly the stated contract.
- §2.6 geometry vs `REAL_GEOMETRY_RESULT_20260825.md`: 366,912 / 270,577 / 96,335 /
  832,393, Var(cosθ) 0.445201; 6,445 bricks, 65,060 raw, 53,005 retained, Var 0.754664,
  N_eq = 120,002.9 (receipt: 120002.8798 = 3·53,005·0.754664); declined run 60,308 /
  208,407 / 0.0580 / 36,253 / 735.9 GB; round-8 values 3.1220 / 3.1672 / 3.1957 exact.
  12,117/6,445 = 1.8801×; 12,117 × 12.2 MB = 147.83 GB ≈ the quoted ≈147.8/148 GB.
- Closure chain: V9 probe receipt carries `derived_manifest` = 65,060 objects → 6,445
  selected → 12,117 required, `plan_digest aaeaa9f3…b3f1` == §2.6/§7; 34 run / 34 conforming,
  13/13 verify hooks, 9 not-covered items — §7's BS-2m row matches the artifacts.
- Exact Stage-P receipt: 995 successes vs x ≥ 962, `passes_rule: true`, 431.4 s, 1,000 ×
  20,000; zero trials granted by exactly one null (both disagreement lists empty); harness
  sha `daed15c7…` == on-disk `stagep_exact.py`; `inputs.oracle`/`inputs.selection` ==
  on-disk `real_oracle_dr10.npz` / `real_selection_reduced.npz` (==
  `real_selection_swapped.npz`, consistent with "the swap phase leaves the real selection
  unchanged"). Shared-null comparison z = 3.1220 matches.
- Floor count, recomputed from the receipt's own `p_own_by_trial`: **951** trials sit at
  4.999750012499375e-05 = 1/20,001, the plus-one resolution floor; 5 trials above 1e-3;
  995 + 5 = 1,000. V12's "951" is correct.
- §2.4 planner/universe pins in the pinned code: `PINNED_PLANNER_DIGEST = 1617af00eb73…`
  (line 154), `PINNED_UNIVERSE_SHA256 = 863e5ded…`, `PINNED_UNIVERSE_BRICKS = 366,912` — all
  match the text. Fixture `CLOSURE-PINNED-PLANNER` PASS carries the same digest.
- v7 (receipt subject) on disk: sha `6be341bd…` == the receipt's `subject.sha256_12`. The
  v7→v9 diff is 14 lines in 3 hunks, all inside `closure_receipt()` (worker filename bump +
  `worker_provenance` plumbing); every Stage-P primitive is byte-identical, so the 995/1000
  transfers to the pinned bytes. (My verification, as last round — see F8 below.)
- §6.1(5)'s checkable claim, re-inspected this round: `REAL_GEOMETRY_RESULT_20260825.md`
  contains counts, geometry, selection and synthetic-injection power only — no χ-derived
  quantity anywhere in it.
- Arithmetic: 0.1836734693877551 = 9/49 = (3/7)², i.e. e < 3/7 ⟺ b/a > 0.4 ✓; BS-7f's
  "800,000-byte payload" = 100,000 × f8 ✓; PWR-SELF-VERIFYING "audited 12, confirmed 10,
  refuted 2" == §4's "2 of 12 (10 confirmed)" ✓; PWR-CALIBRATED-ALONE-INSUFFICIENT "21/22"
  == §4 ✓.

## The three advertised repairs, aimed at as the brief asks

**§6.1(2), the event order.** The sentence itself is repaired: "until BS-5f's confirmatory
power receipt exists, then the primary lock is sealed, then unblinding occurs — in that
order" is the only order consistent with §6.1(1) (the lock requires BS-5f to exist), §4
(Stage C after inference, before unblinding, halt on FAIL), §5 (the only verdict path
requires a BS-5f receipt bound to the mask digest) and §7's BS-5f row (blocks unblinding).
But it is **not consistent everywhere**: one other clause still implies a different order —
§7's BS-V row. See F1.

**The header.** Repaired and verified. "Successor input" now attaches only to the
60,308-brick sample; the 208,405 sealed χ measurements are "NOT an input to this study —
see §6.2, which governs." I searched the whole text for a third statement about them: the
only other mentions are §6.2 itself ("not an input") and §2.6's declined-run recap ("208,407
objects"), which assigns no role. No contradicting statement stands. The 208,405-vs-208,407
reconciliation (two WAITING objects, §8(1)) remains unwritten — minor, carried.

**§2.7(4)(5)(6), the truth of a reason.** The mechanism V11 lacked is now specified at the
text level: evidence-carrying ledger, mandatory recomputation of every predicate with
refusal on disagreement, a defined (not merely thresholded) confidence quantity, and the
acceptance design made a gated slot (BS-2a) with BS-2f demoted to value-only. As a
specification this answers CODEX-V11 3's attack. But the repaired clause set is not
single-valued about where its decisive constant lives, nor about what class its own design
slot has — see F2. An operator can still choose the answer through it in one specific way:
treat the (d) threshold as already pinned by BS-3's quoted τ and bypass the BS-2a design
gate. BS-2a's boundary is drawn in the right place (threshold + retry semantics + evidence
schema + ledger schema + recomputation code + fixtures, before any image byte, BS-6 depends
on it); the text contradicts itself about that boundary in two other sentences.

## Ruling on the deliberately-open Stage-P blocker (the brief asked for a ruling)

**Stating it openly is an acceptable posture for a document that is not yet frozen.** Three
reasons. (i) It is self-binding, not decorative: the header makes freeze conditional on
every class-P slot holding a receipt, BS-5p is class-P, and the banner states BS-5p "cannot
be filled either way" — so freeze is mechanically blocked until the principal chooses one of
the two named closures. An open defect that blocks the freeze condition cannot be silently
lived with. (ii) The banner names why no wording can close it (§0's precedence rule plus the
pinned code's shared-null implementation), names both closure routes, and assigns the choice
to its owner. That is the honest alternative to papering. (iii) The dual-valuedness is
between prose and code, and the text says which wins today (code) and which must win before
freeze (the exact route) — a reader is not left guessing.

Two conditions on that ruling. First, the same posture must be applied consistently to the
same kind of defect — and it is not: BS-2a, also a design slot whose machinery is not in the
pinned code, is tabulated class-E, which does NOT block freeze (F2). Second, the declaration
sits in §2.6's blockquote while §4 — the section titled "Power gate" — still presents the
shared-null route in operative present tense with no in-section marker, and even reports the
exact-route result inside that presentation. The brief says the openness is "stated as open
in §4"; it is not — it is stated in §2.6, and a reader of §4 alone still meets a single
operative route. (Carried KIMI-V11 F13; one sentence at §4's head.)

Confession for the record: my V11 F13 judged this promise "single-valued" and the
supersession substantively repaired. GPT56-V11 F4 and CODEX-V11 4 were right and I was
wrong: a prose declaration cannot bind while §0 makes the pinned code the definition and the
pinned code implements the other route. V12's open banner is the correct posture, and V12's
blockquote cites "KIMI/GPT56-V11 F4" for the finding — for this seat the citation is wrong
(my F4 was the covenant finding; my Stage-P item was F13). Small, but the repair trace is
the document's accountability surface (F12).

## Numbered findings

### F1 — BLOCKING — §7's BS-V row still fuses the verdict into the lock's sealing receipt, so the repaired order cannot be executed as written

**Section / sentences.** §6.1(2), repaired: "…until BS-5f's confirmatory power receipt
exists, then the primary lock is sealed, then unblinding occurs — in that order." §6.1(1):
the lock "is sealed by a signed BS-V receipt naming the digests of the accepted mask, the
calibration record and those inputs." §7: "| BS-V | Hwao | **verdict + primary lock**:
`decide()` output, evaluated floor, path taken, mask digest | disclosure |."

**Why it fails as a promise.** The order sentence is now correct, but the receipt that must
execute it contains the event it must precede. BS-V's declared content includes `decide()`
output — the verdict — which exists only after unblinding, since §5's
`run_production_verdict()` is what produces it and it requires the unblinded mask. So the
signed BS-V receipt that §6.1(1) makes the lock's sealing instrument cannot be completed
before unblinding, and §6.1(2)'s "the primary lock is sealed, then unblinding occurs" is
uninstantiable against the slot table. A person held to this text can quote §7's BS-V row
against §6.1(2) with the same equal force V11's sentence had against §4: the lock ceremony
necessarily completes after unblinding, therefore the stated order is aspirational, therefore
the access ban's endpoint is negotiable. The brief asked whether any other clause still
implies a different order: yes, this one. I verified in the pinned code that the fusion is
not merely tabular: `run_production_verdict()` (v9 lines 1591–1625) guards environment,
authorization, complete sample, sealed mask, and a BS-5f receipt bound to the mask digest —
and nothing else. The lock has no code hook on the only verdict path; the code route is
BS-5f → verdict directly. Conduct prose has no code to arbitrate it, and the one code path
that could enforce the order does not. GPT56-V11 F1 named this exact seam ("BS-V cannot both
record key holders before the first image byte and be the post-unblinding verdict receipt")
and proposed the split; V12 repaired the order sentence and left the schema it must land in
untouched. Note this also leaves §6.1(2)'s key-holder roster — "recorded in BS-V's schema
before any image byte" — assigned to a receipt whose other content cannot exist before
unblinding (carried KIMI-V11 F5, re-verified: BS-V's row still has no roster field and no
access-log-digest field, and BS-2f's row has no log-digest field though §6.1(3) receipts the
log digest there).

**Smallest sufficient repair.** Split BS-V in §7: **BS-V1, lock seal (pre-unblinding, blocks
unblinding)** — accepted-mask digest, calibration digest, decision-input digests, key-holder
roster, access-log digest, Duho's signature; **BS-V2, verdict (post-unblinding, blocks
disclosure)** — `decide()` output, evaluated floor, path taken, mask digest. Point §6.1(1)'s
"sealed by" at BS-V1, and add one line to §5's guard list: the runner requires a BS-V1
receipt bound to the mask digest exactly as it requires BS-5f's. Text-only; no mechanism
change.

### F2 — BLOCKING — the §2.7 repair is dual-valued about where the (d) threshold lives and what class BS-2a has; the list also carries two items numbered 5

**Section / sentences.** §2.7(2)(d): exclusion only for "the instrument's confidence … below
the threshold pinned in **BS-3** for this run." §2.7's retained clause, still numbered **5**:
"The thresholds in (d) are pinned before any image byte, **in BS-3**, with the same force as
any other frozen constant." New §2.7(6): "The numeric confidence threshold, retry and
failure semantics, the evidence schema for reasons (a)–(d), the ledger schema, the
recomputation code and its fixtures are a DESIGN slot (**BS-2a**)" — and calls it "its own
**class-P** slot." §7's BS-2a row ("the numeric confidence threshold, retry/failure
semantics, …") sits in the **Class E** table. §7's BS-3 row: "instrument identity: weights
`83008c1c…`, τ = 4.4006456017494235, antisymmetry identity."

**Why it fails as a promise.** The repair's own load-bearing constant is assigned to two
different slots. Read (2)(d) and the second "5.": the exclusion threshold is pinned in BS-3
— a class-P slot whose §7 row already quotes a numeric τ, and whose pinned code schema I
verified is `("weights_sha256", "tau", "antisymmetry_receipt")` (v9 line 198) with no field
for an exclusion threshold. Read (6) and §7's BS-2a row: the same threshold is future design
work gated as text and code. These are materially different conformance targets: under the
first, an operator can declare the (d) threshold already frozen by BS-3's quoted τ and fill
BS-2a without ever designing it — bypassing the very gate the repair exists to create, and
changing the realised partition, which is the answer. Under the second, BS-3's row is
misquoted in §2.7. A gate cannot check conformance against both. And the class contradiction
decides whether the hole survives freeze: if BS-2a is class-P as (6) says, the header's
freeze condition ("every class-P slot holds a receipt") blocks freeze until the acceptance
machinery exists; as tabulated class-E, the text can be frozen with its anti-cherry-picking
machinery undesigned — and §7's own DESIGN definition says filling one "requires a new text
revision and a fresh text gate," i.e. the frozen text would be revised post-freeze to
receive it. The duplicate item number (1,2,3,4,5,6,**5**) is the mechanical scar of the same
unfinished edit, and it breaks every cross-reference to "§2.7(5)" — including the brief's
own. This is the round-3 instance of the lane's pattern: the repair landed on the finding's
mechanism and introduced a new dual-valuedness at its boundary — exactly what V12's §2.6
banner says cannot stand for Stage P, standing here unmarked.

**Smallest sufficient repair.** Renumber the second "5." to 7. Strike "pinned in BS-3" from
(2)(d) and the renumbered (7); name BS-2a as the threshold's only home (or, if τ is intended
to be the (d) threshold, say so explicitly and move its pin inside BS-2a's design gate).
Move BS-2a's §7 row to class-P — it must close before BS-6 anyway — or state in §7 that
freeze requires BS-2a despite its class. Three sentences and a table row.

### F3 — BLOCKING — §6.1(2)'s prohibition still scopes to the powerful, so a named key holder outside the listed roles may read χ before the lock, authorised and merely logged

**Section / sentences.** §6.1(2), unchanged in this component: "**Who may hold read access.**
Only named key holders, recorded in BS-V's schema before any image byte. **No person or
process able to alter this text, fill or adjudicate a class-P slot, construct the accepted
mask, or operate the lock may** decrypt, query, render, summarise or inspect any χ-bearing
object or derivative until …" §6.1(4): "Unauthorised access voids the run."

**Why it fails as a promise.** The ban binds only the four powerful roles; the read-access
grant is to named key holders. A named holder outside those roles may decrypt and inspect
any χ-bearing object before the lock while complying with every word: the read is logged
(visible) but *authorised*, so (4)'s void does not attach. The clause exists to prevent
pre-unblinding outcome knowledge; it prices in exactly that event for exactly the people
holding the keys, and the roster that defines who they are is itself filled after the
geometry is known. This was half of CODEX-V11 1 and GPT56-V11 F1 — the half V12's §6.1
blockquote claims repaired ("KIMI-V11 F1 / GPT56-V11 F1 / CODEX-V11 1, unanimous") and did
not touch; the order half landed, this half did not. The blinding is the study's whole
licence — §6.1(5) makes the redesign's legitimacy rest on outcome-blindness — and the
covenant's operative scope still permits a compliant pre-lock read. Two smaller seams ride
with it (carried KIMI-V11 F4(ii)/(iii), still unrepaired): "blind automation is permitted
only where named here" names no automation anywhere — not the instrument writing χ, not the
cutter, not the Stage-C runner, not the ledger recompute — and the hand-check committee, the
one group that must render χ-bearing cutouts pre-unblinding to produce the BS-8f labels, is
named nowhere, with no store declared for their χ-derived labels against (3)'s checkable
sentence; and the log records only decryption that flows through the logged path, with no
statement that read is technically impossible outside it, so the void rule cannot bite on an
unlogged event.

**Smallest sufficient repair.** "No person, including every named key holder, may decrypt,
query, render, summarise or inspect any χ-bearing object or derivative before the lock;
custody confers capability for the lock ceremony only; any pre-lock human read, authorised
or not, voids the run." Name the permitted producers (instrument, cutter, Stage-C runner,
ledger recompute, hand-check committee) with the condition that their outputs enter the
sealed store at creation and never leave it. State the technical means by which the log is
complete, or state plainly that completeness rests on custody and name who holds that risk.

### F4 — MAJOR — carried, re-verified: §2.4 and §10 still cite closure checks that exist in no pinned v9 artifact (KIMI-V11 F3)

**Section / sentences.** §2.4: "a manifest omitting those neighbours is refused **by name**:
`CLOSURE-FROZEN-PLANNER`, `CLOSURE-RETIRED-REFUSES`, `CLOSURE-CATCHES-HISTORICAL`,
`CLOSURE-CALLER-TRUST` (3/3 — …)." §10: "new fixture `CLOSURE-PRODUCTION-USES-FROZEN`
asserts the wiring by source inspection."

**Why it fails as a promise.** I searched the pinned fixture transcript, the pinned probe
suite (`closure_probe_suite_v9.py`), the V9 probe receipt, and both pinned code files. Of
the four names in §2.4, only `CLOSURE-RETIRED-REFUSES` exists in any v9 artifact.
`CLOSURE-FROZEN-PLANNER`, `CLOSURE-CATCHES-HISTORICAL`, `CLOSURE-CALLER-TRUST` and §10's
`CLOSURE-PRODUCTION-USES-FROZEN` appear in none. The v9 battery's only planner check is
digest-only (`CLOSURE-PINNED-PLANNER`); no pinned v9 check functionally runs the planner
over the two historical objects, and no pinned probe carries the "3/3" caller-trust battery
the parenthetical describes. The underlying claims are supported elsewhere (the probe
receipt's real-data 12,117 derivation, verified above) — but the sentence attributes them to
named checks the frozen mechanism does not carry. A preregistration that cites non-existent
evidence at the paragraph it rewrote to repair that exact failure class has the same defect
twice.

**Smallest sufficient repair.** Cite what exists: `CLOSURE-PINNED-PLANNER` (digest), the
probe receipt's real-parent derivation, and the referee's functional verification named as
ad-hoc — or restore the functional fixtures at the next code revision and then cite them.

### F5 — MAJOR — carried, re-verified: §4's z\* sentence is still contradicted by the pinned fixture, and the same false sentence sits in the pinned code's docstring (KIMI-V11 F6 / CODEX-V11 5)

**Section / sentence.** §4: "across four geometries the measured z\* ranged 3.0376–3.1355,
bracketing the normal 3.0902, and on the polar geometry this design actually selects the
normal threshold came out anti-conservative."

**Why it fails as a promise.** The pinned v9 fixture prints z\* = 3.0694, 3.0010, 3.0020,
3.0260 — range 3.0010–3.0694, every one *below* 3.0902. They do not bracket the normal
value; 3.0376 and 3.1355 appear in no artifact; and the identical sentence sits in
`reference_null_z()`'s docstring in the pinned code (v9 lines ~1163–1167) — definitional
surface in a document that pins code by digest. The conclusion survives via the same
battery's `PWR-Z-STABLE` tail masses beyond z = 3.090 (0.00135, 0.00130, 0.00100, 0.00110 —
three of four heavier than nominal), which the text never quotes. V12's preamble repeats the
standing argument — a preregistration that misquotes its own receipts has no standing to
demand accuracy of anyone else — and carries this misquote in both the text and the pinned
code.

**Smallest sufficient repair.** Quote the artifact: "the four fixture geometries'
standardized 0.999 quantiles measured 3.0010–3.0694, all below the normal 3.0902, and tail
mass beyond 3.090 measured up to 0.00135 (`PWR-Z-STABLE`) — the normal threshold is not
safe either way." Carry the same edit into the code docstring at the next code revision.

### F6 — MAJOR — carried: no binding interpretation of what an answer means (KIMI-V11 F9 / GPT56-V11 F5; the brief's question 7, now asked three rounds running)

**Section / sentences.** §1: "It does not test A ≈ 0.02, Shamir, BHU, or whether the sky is
isotropic." §5 defines the four outcome labels and stops.

**Why it fails as a promise.** The text never states that REJECTED-AT-LONGO-AMPLITUDE
excludes the published amplitude at the published axis under this design's sensitivity and
nothing more — not isotropy, not smaller amplitudes, not other axes, not other researchers'
claims. It never states that every INCONCLUSIVE* supports neither reproduction nor
rejection. It never states that a precise opposite-sign result (Â < 0, p < 0.001) lands in
INCONCLUSIVE — a strong anti-Longo result wearing a label that reads as "no result". The
brief states these limits in its own question 7; the promise still does not contain them,
and a later summary can quote the registered outcome verbatim and overread it with nothing
in the binding text forbidding the overreading.

**Smallest sufficient repair.** Two sentences in §5 plus the BS-V2 results template:
"REJECTED-AT-LONGO-AMPLITUDE excludes the published amplitude at the published axis under
this design's sensitivity. It does not establish isotropy, does not exclude amplitudes below
this design's floor, and does not speak to other researchers' distinct claims; no
INCONCLUSIVE* outcome supports either reproduction or rejection, and a precise opposite-sign
estimate is a strong anti-Longo result, not an absence of one."

### F7 — MAJOR — carried: the Branch-A availability event still has no frozen probe (KIMI-V11 F8 / GPT56-V11 F6)

**Section / sentences.** §2.1: Branch A is selected "iff the DR11 photo-z product exists and
is publicly retrievable at the resolution moment"; BS-1 fills on "the day DR11 photo-z is
confirmed available" or 2026-09-05 (`BRANCH_FALLBACK_DATE` verified pinned in code).

**Why it fails as a promise.** "Exists," "publicly retrievable" and "confirmed" have no
frozen probe, endpoint set, schema check, retry/error policy, timestamp convention or
witness. Before the fallback date, delaying or avoiding a check delays the earlier event; a
transient mirror or auth failure turns existence into apparent absence. An operator can
steer the branch while satisfying every word — and V11 now correctly makes the branch choice
outcome-bearing (Branch A voids the §0 pin and demands a fresh gate), which raises, not
lowers, the premium on the trigger being frozen.

**Smallest sufficient repair.** Freeze the probe: named authoritative URLs/products, the
schema/version check that constitutes "exists", retry window and transient-error treatment,
timestamp/zone, signed raw-response receipt; BS-1 a pure function of that receipt.

### F8 — MAJOR — carried: the exact Stage-P receipt's subject is v7 bytes, and V12's disclosure still does not say so (KIMI-V11 F7 / GPT56-V10 F3 / CODEX-V10 5)

**Section / sentences.** §2.6: "`stagep_exact.py` is a measurement harness; the exact-null
Stage P is not implemented in the file §0 pins." §10: "it is measured, not accepted."

**Why it fails as a promise.** The receipt's `subject.path` is `../ref/successor_ref_v7.py`,
sha `6be341bd…` — not the v9 bytes §0 pins. "Not in the pinned code" and "measured against a
different, unpinned version of the reference" are different disclosures; the text makes the
first and withholds the second, and the receipt's own stated-limits line discloses the v7
subject while the text's does not. I re-verified this round that the gap is benign: the
v7→v9 diff is 14 lines confined to `closure_receipt()`, every primitive the harness calls is
byte-identical, so the 995/1000 transfers to the pinned bytes. That is the referee's work,
done three times now; the promise should not require the next reader to repeat it to trust
the design's decisive number.

**Smallest sufficient repair.** One sentence in §2.6: "the harness ran against v7; every
primitive it calls is byte-identical to the pinned v9 (the v7→v9 diff is confined to
`closure_receipt()`), so the measurement applies to the pinned code; it remains unrefereed
and BS-5p stays unfillable until folded in."

### F9 — MINOR bundle (small, same-edit repairs; carried unless noted)

- **Repair-trace miscitation (new).** V12's §2.6 blockquote cites "KIMI/GPT56-V11 F4" for
  the Stage-P finding; my V11 F4 was the covenant finding — the Stage-P item here was F13.
  The trace is the document's accountability surface (§6: "every gated revision of this text
  changes one thing per finding, and the §10 trace maps finding → change"). Correct the
  citation.
- **"5.00e-05" vs the receipt's 4.999750012499375e-05** (§2.6). The count 951 is right; the
  floor value quoted is the rounded one, and the receipt's own stated-limits line still says
  "995 … sit at 5.00e-05" against its own data (951 at 1/20,001). Quote the plus-one floor
  and add the one-line flag that the receipt's stated-limits figure is superseded by its own
  `p_own_by_trial`.
- **BATTERY-POS quoted as "p = 2.2e-21"** (§5) vs the fixture's "p = 2.23e-21". Quote the
  fixture's digits.
- **208,405 vs 208,407, still unreconciled.** Header/§6.2: "208,405 sealed χ measurements";
  §2.6's declined-run row: "208,407 objects". Consistent with §8(1)'s two-WAITING narrative
  (208,407 − 2 = 208,405); the text never says so. One parenthetical.
- **§0 quotes the one-seat verdict as "CLEAR"**; the artifact's first line is "**CLEAR** —
  with conditions named below". §6's own rule: gate-state sentences never exceed the cited
  artifact's first line. Add the qualifier.
- **§2.6's closing "These fill the class-P inputs…"** (carried KIMI-V11 F11): under the
  document's own VALUE/DESIGN language the §2.6 measurements fill nothing; one of twelve is
  filled (BS-2m), not a §2.6 product. Reword.
- **§0 names the fixture transcript without its digest** (carried KIMI-V11 F12). Recomputed:
  `fab32ba24cedcedf7fe601c3a8d9dbde13f57b1c9bf2e0b88963bcfebc33a8b5`. Add it and state
  whether the transcript is normative or validation evidence.
- **§7's DESIGN-count sentence omits BS-2a** ("BS-2f, BS-5p, BS-8p and BS-9 are DESIGN
  slots") while BS-2a's own row says DESIGN — the same sentence would have caught F2's class
  contradiction. Update the count when F2 is repaired.
- **The tested axis is never quoted or tolerance-bound in the text.** §1 tests "that
  published axis" and makes `AXIS` definitional; I verified the pin equals the published
  (52°, 68.5°) to ~1e-6 deg, but no sentence binds that mapping or a tolerance, and Longo's
  own value is "approximately". One sentence: "AXIS is the ICRS Cartesian of (l, b) =
  (52°, 68.5°) and differs from that published value by less than 0.1°."
- **Carried minors, unrepaired and still correct:** `RETENTION_LB = 0.8572` provenance
  unstated; no public-deposit/external-timestamp clause for the freeze; no
  no-secondary-endpoints sentence (`explore_verdict()` exists; nothing says no analysis
  outside `run_production_verdict()` will be presented as the preregistered result); §0's
  "every operational mechanism … DEFINED by the code bytes" still covers the production
  scale at which the pinned O(n²) chain cannot execute (§2.6's own disclosure); §10's
  class-E judgment calls (integrity triggers, checksum-mismatch disposition, committee
  adjudication) remain unfrozen in text or schema.

## Answers to the brief's eight questions, compressed

1. **Can it fail?** Yes — the outcome space is partitioned and boundary-closed
   (0.001 ≤ p ≤ 0.05 is explicitly INCONCLUSIVE; ties by exact float ≥; plus-one p), only
   the pinned code emits a label, REJECTED-AT-LONGO-AMPLITUDE is a named reachable failure,
   and BATTERY-A0/-SIGN/-POS/-NEQ are pinned demonstrations. The soft spots are the
   interpretation omission (F6) and the two dual-valued seams (F1, F2), not the structure.
2. **Degrees of freedom.** Enumerated: the branch fork's date is bound in code but its
   trigger event is not (F7); the exclusion threshold's home is contradicted (F2); the
   Stage-P route is openly dual (declared, freeze-blocking — ruled acceptable above);
   acceptance design is open as BS-2a (declared, but mis-classed — F2); the key-holder
   roster is open until BS-V's schema exists (F1); eleven unfilled slots are declared with
   named producers; integrity triggers / checksum-mismatch / committee adjudication remain
   unfrozen (F9 bundle). Each is either declared-and-freeze-blocking or named above; none is
   hidden.
3. **Circularity.** None in the forbidden direction. Stage P injects at the frozen amplitude
   on count-derived geometry; Stage C runs on the sealed sign-free mask; the detection floor
   is a frozen formula evaluated at a named measured point (a_LB from blind hand-check,
   pre-unblinding); the N_eq floor is a frozen constant derived by code from the mask's own
   geometry; the decision regions are fixed numbers. No threshold or boundary depends on the
   data it will judge.
4. **Numbers vs artifacts.** Everything I could recompute verifies (list at top) except the
   named stale items: the z\* range (F5, in text and pinned docstring), the dead fixture
   names (F4), "5.00e-05" vs 4.99975e-05 with the receipt's stated-limits line unflagged,
   p = 2.2e-21 vs 2.23e-21, and 208,405 vs 208,407 unreconciled. The three advertised
   2026-08-26 fixes (stale pin, retracted 997, download size) are present and correct.
5. **Is the blinding real?** Structurally strong and getting stronger: lock defined, holders
   named, the powerful barred, logging required, void on unauthorised access, a checkable
   sentence, redesign evidence named and inspected (no χ-derived quantity in it). But the
   order cannot be executed against the slot table (F1), the key-holder read path survives
   (F3), and the producers/committee are unaddressed with the log's completeness unstated
   (F3). What would show a look today: the log, for paths that flow through it; nothing, for
   a holder who bypasses it.
6. **Honest incompleteness.** Mostly exemplary: the draft banner, 1-of-12 at the table, the
   VALUE/DESIGN distinction, the retraction chain, "measured, not accepted", the open Stage-P
   banner. Exceptions: "These fill the class-P inputs", the bare-CLEAR quote, the v7-subject
   nondisclosure (F8), and the preamble's claim to have repaired the unanimous §6.1 finding
   when its custody half survived (F3).
7. **Null-result overclaim.** No overclaim anywhere in the text. The gap is the omission:
   the three limits the brief itself states (not isotropy, not smaller amplitudes, not other
   researchers' claims) are still not in the binding text (F6). `WHAT_IS_AT_STAKE_20260827.md`
   carries them; the promise does not.
8. **Missing entirely.** The interpretation paragraph (F6); the availability probe (F7); the
   axis-tolerance sentence, the reporting commitment (nothing commits the verdict to be
   reported whatever it is), a sunset for the run if slots cannot be filled, the
   no-secondary-endpoints sentence, and the public deposit (all F9 bundle); and a committee
   store inside the covenant (F3). None needs the machinery reopened; all are invisible if
   you only referee the machinery.

The brief's five known-wrong items: confirmed accurate as stated; none understated — with one
shading carried from last round: the one-seat verdict's first line is "**CLEAR** — with
conditions named below", and §0/§7 quote it as CLEAR while carrying the nine open items in
the same rows (disclosed, but the quote exceeds the artifact's verdict line by one
qualifier).

## Testimony (asserted in the text or receipts; not independently verified by me)

- BS-3 instrument values (weights `83008c1c…`, τ = 4.4006456017494235, antisymmetry
  identity) — unfilled slot, quoted in the table; the string `83008c1c` appears in drafts
  and referee reports only, in no receipt I could find.
- The predecessor documents quoted by sha (V3-pred `b06901c8…`, BS6-pred `5ff7f454…`,
  decline memo `b4a1f1fc…`): existence and contents outside the review set; the eight Cut-6
  predicates' byte-identity to BS6-pred accepted, not checked. The 208,405 sealed count
  itself (the two-WAITING reconciliation is narrative).
- "DR11 pages exist; no photo-z product is present" (measured 2026-08-24) — author's
  measurement; F7 exists because the probe that would change this is unfrozen.
- Equivalence batteries: 40 (order), 30 (reduction), 400 (swap phase, referee's own seed and
  regime) cases, zero mismatches — stated in the geometry receipt and §10; no independent
  receipt in the named set.
- "12,117 reproduced independently three times" — the closure row is in the probe receipt
  (verified); the two direct enumerations are asserted in §2.6/§7 and the mechanism
  referee's report.
- 12.2 MB/brick unit price and the 735.9 GB declined download — predecessor-era figures.
- The conduct narrative (drafting authorization, catalog-only authorization, "no χ was
  read", the 2026-08-26 ceiling raise, provider refusals of the two mechanism seats, the
  fork status) — conduct testimony; nothing in the artifacts contradicts it.
- "v4 through v7 remain on disk unchanged" — the files are present; v7 re-digested this
  round (`6be341bd…`, matches the receipt); v4–v6 content-unchanged accepted from the
  mechanism referee's spot checks, not re-digested by me.
- §8(3)'s "42.76%" inflation figure — predecessor-era, not recomputed.

## Verdict

The three advertised repairs all landed on their targets, and one is complete: the header is
now single-valued about the predecessor's sealed measurements, and I could find no third
statement. But the other two repairs each carry a defect at the point they govern, and the
third blocker I must name was inside the finding the order repair claims to close. **F1**:
§7's BS-V row still fuses the post-unblinding verdict into the receipt that seals the lock,
so the repaired BS-5f → lock → unblinding order cannot be executed as written, and the only
code path to a verdict has no lock gate. **F2**: the §2.7 repair assigns the exclusion
threshold to BS-3 in two sentences and to BS-2a in two others, calls BS-2a class-P while
tabulating it class-E, and numbers two items 5 — the truth of a reason is still not
single-valued at its decisive constant. **F3**: §6.1(2) still permits a named key holder
outside the listed roles to read χ before the lock, authorised and merely logged, so the
covenant still prices in the event it exists to prevent. All three are text-level repairs —
a slot split, three sentences and a table row, one clause — and none requires reopening the
frozen mechanism. F4–F8 must be repaired in the same revision; the F9 bundle should be. The
deliberately-open Stage-P blocker is, as ruled above, an acceptable posture for an unfrozen
document — self-binding through the freeze condition — provided the same posture is extended
to BS-2a and the marker is raised into §4.

Blocking findings: **F1** (the BS-V fusion makes the repaired lock order uninstantiable),
**F2** (the §2.7 threshold is dual-valued BS-3-vs-BS-2a and BS-2a's class contradicts
itself), **F3** (the key-holder pre-lock read path survives).

**NOT CLEAR**
