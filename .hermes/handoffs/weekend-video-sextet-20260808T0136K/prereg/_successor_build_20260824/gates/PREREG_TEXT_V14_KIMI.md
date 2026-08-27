# PREREG TEXT REFEREE, ROUND 4 — KIMI

Subject: `../PREREG_SUCCESSOR_DRAFT_V14_20260827.md` (699 lines; self-titled "V13" on line 1 —
see F8), read as a fresh promise per the brief's instruction. Round: BRIEF_PREREG_TEXT_V14,
2026-08-27. I did not read `/Users/duhokim/NebulaMindData/`. I read the three round-3 reports
before forming findings, and every digest, constant, fixture name and quoted number I assert as
*verified* was recomputed from the files on disk during this review; what I could not recompute
is under Testimony.

## What verifies (so the findings carry their weight)

- §0 pins, recomputed: `successor_ref_v9.py` sha256 `6a9abbbd…c148`, `closure_worker_v9.py`
  `28f8e1f9…5959`, `FIXTURES_V9_20260826.out` `fab32ba2…a8b5`, referee report
  `CLOSURE_V9_KIMI.md` `f2ee062b…2f01` — all exact; both v9 code files mode `-r--r--r--`.
  v4–v7 present on disk.
- In-code constants re-read from the pinned bytes: `A_LONGO = 0.0408`,
  `A_LONGO_PUBLISHED_SIGNED = −0.0408`, `N_PERM = 100,000`, `CP_PASS_X = 962`,
  `A_FLOOR = 0.85`, `RETENTION_LB = 0.8572`, `FLOOR_MULT = 3.09`, `NEQ_MIN = 100,000`,
  `PWR_CONSERVATISM = 1.01`, `MC_CAL_PERM = 20,000`, `CUTOUT_PIX = 128`,
  `CUTOUT_PIXSCALE_ARCSEC = 0.262`, `BRANCH_FALLBACK_DATE = "2026-09-05"`, FROZEN_ENV
  3.9/1.26.4/little. All match the text.
- Clopper–Pearson, own recomputation (scipy): x = 961 → LB 0.949366 (fails); x = 962 → LB
  0.9504871 (passes); x = 995 → LB 0.9895159. The frozen integer is exactly the stated contract.
- §2.6 geometry vs `REAL_GEOMETRY_RESULT_20260825.md`: 366,912 / 270,577 / 96,335 / 832,393,
  Var(cosθ) 0.445201; final table 6,445 / 65,060 / 53,005 / 0.754664 / N_eq 120,002.9
  (receipt: 120002.8798 = 3·53,005·0.754664); round-8 values 3.1220 / 3.1672 / 3.1957 exact;
  the 997/1000 retraction and the 995/1000 exact re-run are present as §2.6 describes.
- Closure chain: V9 probe receipt carries 65,060 → 6,445 → 12,117 required,
  `plan_digest aaeaa9f3…b3f1` == §2.6/§7; summary conforming = 34; freeze record matches
  (34/34, 13 hooks, 12,117, same digest). 12,117/6,445 = 1.8801×; 12,117 × 12.2 MB = 147.83 GB
  ≈ the quoted ≈147.8/148 GB.
- Exact Stage-P receipt: `exact.successes` 995, `passes_rule: true`, 431.4 s; 1,000 p-values,
  995 < 1e-3, **951** at exactly 1/20,001 = 4.999750012499375e-05, 5 ≥ 1e-3;
  `granted_only_by_own` and `granted_only_by_shared` both empty; shared z = 3.1220; harness sha
  `daed15c7…` == on-disk `stagep_exact.py`; geometry fields match §2.6.
- The receipt's subject is `../ref/successor_ref_v7.py` sha `6be341bd…` == on-disk v7. The
  v7→v9 diff is 19 lines, all inside `closure_receipt()` (worker filename bump +
  `worker_provenance` plumbing); every Stage-P primitive is byte-identical, so the 995/1000
  transfers to the pinned bytes. (My verification, third round running — see F7.)
- §2.4 pins in the pinned code: `PINNED_PLANNER_DIGEST = 1617af00eb73…` (line 154),
  `PINNED_UNIVERSE_SHA256 = 863e5ded…`, `PINNED_UNIVERSE_BRICKS = 366,912` — all match the
  text. V10 did quote `36bbbf250215…` (1 occurrence) — §2.4's provenance parenthetical is
  accurate. Fixture battery: `PWR-SELF-VERIFYING` "audited 12, confirmed 10, refuted 2" ==
  §4; `PWR-CALIBRATED-ALONE-INSUFFICIENT` 21/22 == §4; transcript ends `ALL FIXTURES PASS`.
- §6.1(6)'s checkable claim, re-inspected: `REAL_GEOMETRY_RESULT_20260825.md` contains counts,
  geometry, selection and synthetic-injection power only — no χ-derived quantity anywhere.
- The four advertised V14 repair targets, checked: §2.7 numbering is now 1–7 in order
  (repaired); the orphaned blind-automation sentence is out of the blockquote and inside
  §6.1(3) (repaired); BS-2a is in the Class-P table with the threshold's naming authority
  added (that half landed); §6.1(2)'s ban text is now universal (that sentence landed). What
  did **not** land is the subject of F1–F5.

## The four advertised repairs, aimed at as the brief asks

**§6.1(2), the key-holder loophole — the sentence landed; its own final clause overshot and
voids the exceptions the same section authorizes.** "No person and no process may decrypt,
query, render, summarise or inspect any χ-bearing object or derivative" is universal in fact;
no other clause carves anyone out beyond §6.1(3)'s enumerated exceptions (§6.2 doesn't; Duho's
opening right is post-lock). But the repair universalized the *void* without carving the
exceptions: (2)'s final sentence — "An authorised pre-lock read voids the run exactly as an
unauthorised one does" — and (5) — "**Any** pre-lock access voids the run — authorised or not"
— read literally against (3), which calls the hand-check committee "**the one authorised
pre-lock human view**" and names four processes that "may touch χ-bearing objects before the
lock". The one authorised human view voids the run under (2) and (5); so does every named
process's mandated touch. The ban is universal and so is the void, and the two together
swallow the exception list. See F1.

**§6.1(3), the exceptions — the set is not complete, the symbols are not named, and the
committee's isolation is contradicted by the slot table.** See F4.

**§6.1(1) and §7, the lock/verdict cycle — the sequence still cannot be executed and receipted
end to end.** The prose order is right (BS-5f blocks BS-L; BS-L blocks unblinding; BS-V
follows), but five load-bearing defects stand, including the two the V13 blockquote claims to
have eliminated. See F2.

**§7, BS-2a's class — moved to Class P, authority added; the threshold still has two homes and
the slot count is wrong three ways.** See F3 and F8.

**Housekeeping:** numbering and the orphaned sentence are repaired. The "stale BS-V's schema"
is **not** repaired where it is live: §7's BS-V row still reads "**verdict + primary lock**"
and §10 still names "the BS-V primary lock" as an open item. Details in F2.

## Numbered findings

### F1 — BLOCKING — NEW IN V14, repair-introduced: §6.1(2)'s final sentence and §6.1(5) void the very exceptions §6.1(3) authorizes

**Section / sentences.** §6.1(3): the committee is "**the one authorised pre-lock human
view**"; the four blind-automation processes "may touch χ-bearing objects before the lock… A
process not on this list may not run before the lock." §6.1(2), final sentence (new in V14):
"**An authorised pre-lock read voids the run exactly as an unauthorised one does.**" §6.1(5)
(rewritten in V14): "**Any pre-lock access voids the run** — authorised or not, disclosed or
not, and whether or not the accessor believed it harmless."

**Why it fails as a promise.** (3) authorizes exactly two kinds of pre-lock access: the four
processes' touches and the committee's view. (2)'s last sentence voids any *authorised*
pre-lock read; (5) voids *any* pre-lock access, "authorised or not". The committee's mandated
view of χ-bearing cutouts is an authorised pre-lock human view — so under (2) and (5) it voids
the run it exists to enable. The acceptance-ledger recompute reads instrument receipts
(χ-bearing) — a pre-lock read — and voids the run under (5). A person held to this text must
choose which clause to relax to produce BS-8f at all: obey (3) and void under (5), or obey (5)
and never produce the labels Stage C requires. Choosing which clause wins is an
outcome-adjacent discretion exercised after the geometry is known — the exact failure class
the covenant exists to eliminate. V12's (4) ("**Unauthorised** access voids the run") was
consistent with exceptions; V14's universalization repaired the loophole and broke the
carve-out. This is the round-4 instance of the lane's pattern: the repair landed on the
finding's mechanism and introduced a new contradiction at its boundary.

**Smallest sufficient repair.** Scope the void: "(5) Any pre-lock access **outside the
exceptions enumerated in (3)** voids the run — authorised or not, disclosed or not…" and
strike (2)'s final sentence or replace it with "no authorisation other than (3)'s exists, and
anything outside (3) voids the run, claimed authority notwithstanding." Two clauses.

### F2 — BLOCKING — carried (KIMI-V12 F1 / GPT56-V12 F2 / CODEX-V12 1), half-repaired: the lock/verdict cycle still cannot be executed or receipted end to end — five defects, two of them the exact ones the V13 blockquote claims eliminated

The prose order is now correct everywhere in §6.1. Executing it fails at five independent
points, each verified against the text and the pinned code this round:

(a) **Two operative definitions of the primary lock stand.** §6.1(1): the lock "is NOT the
verdict receipt… sealed by its own signed receipt, **BS-L**." §7's Class-E table, BS-V row:
"**verdict + primary lock**: `decide()` output, evaluated floor, path taken, mask digest".
§10's disclosure list: "the **BS-V primary lock**". The binding slot table still fuses the
lock into the post-unblinding verdict receipt — KIMI-V12 F1's target sentence, unrepaired —
and §10 agrees with it against §6.1. The brief listed this as housekeeping surfaced while
repairing; it is live in two places, not surfaced-and-fixed. A gate reading §7 against §6.1
cannot say which receipt seals the lock.

(b) **BS-L is unreceiptable under §0.** BS-L has code symbol "—", no entry in the pinned
`SLOT_SCHEMA` (verified: only BS-2f, BS-5f, BS-V, BS-3 exist), and §7's own classification
sentence — "BS-2f, BS-5p, BS-8p and BS-9 are DESIGN slots" — omits it. If BS-L is a VALUE slot
it needs a frozen schema, which exists nowhere; if it is a DESIGN slot it must be listed,
which it is not; §7's DESIGN definition says filling one "requires a new text revision and a
fresh text gate, not a receipt insertion". Under §0's code-precedence rule no conforming BS-L
receipt can be emitted at all. The covenant's load-bearing artifact cannot be produced by the
document that demands it.

(c) **The roster timing defect moved from BS-V to BS-L verbatim.** §6.1(2): "Key holders are
named in **BS-L's roster** before any image byte." §7: BS-L is "Blocked by BS-5f" — and BS-5f
is class E, produced after inference (§4: Stage C "after inference, before unblinding"),
which requires image bytes (BS-6 → cutouts → instrument → BS-2f → BS-8f → BS-5f). So the
artifact that carries the roster exists only after image bytes, while the text requires the
roster named inside it before image bytes. No pre-image artifact anywhere in §7 carries a
key-holder roster. The V13 correction blockquote names this exact defect as repaired — "It
also made 'key holders recorded in BS-V's schema before any image byte' unreceiptable, since
the only BS-V artifact is the later verdict" — and re-created it one-for-one: the only BS-L
artifact is the lock-time receipt. The roster that defines who holds the keys can still be
filled after the geometry is known, which was the substance of KIMI-V12 F3's tail.

(d) **The access-log digest has no home at BS-2f.** §6.1(4): "a log whose digest is receipted
at BS-2f and again at BS-L." The pinned `SLOT_SCHEMA` gives BS-2f exactly `(brickid, objid,
c, accept_flag, bin, boundaries, mask_digest)` and the pinned `receipt()` refuses wrong fields
(fixture `RECEIPT-SCHEMA`). A BS-2f receipt carrying the log digest is refused by the pinned
code; one without it violates §6.1(4). Carried from round 3, unrepaired.

(e) **The only code path to a verdict has no lock gate.** Verified in the pinned bytes
(`run_production_verdict()`, v9 lines 1591–1625): guards are environment, authorization,
complete sample, sealed mask, and a canonical BS-5f receipt bound to the mask digest — then
the verdict. Nothing requires BS-L; §5's prose guard list matches the code and names no lock
receipt. The code route is BS-5f → verdict directly, and the text's own blockquote concedes
"conduct prose has no code to arbitrate it: §0's 'code wins' rule does not reach §6". The
event whose absence the covenant cannot survive has no mechanism on the only path that
produces it.

**Why it fails as a promise.** The brief's question — "can that sequence now be executed and
receipted end to end?" — has answer no at five points. A future operator cannot instantiate
BS-L (b), cannot receipt the roster when required (c), cannot receipt the log digest where
required (d), can quote §7/§10 against §6.1 on which receipt seals the lock (a), and can reach
a verdict with no lock on the path (e).

**Smallest sufficient repair.** In the same revision: fix §7's BS-V row to verdict-only and
§10's "BS-V primary lock" mention; declare BS-L a DESIGN slot in §7's classification sentence
with its schema, roster, and log-digest fields to be pinned in code before freeze (or pin the
schema now); add a pre-image roster designation to an existing pre-image slot (BS-3 or BS-2a)
that BS-L binds by digest, and reword §6.1(2) to name that artifact; extend BS-2f's pinned
schema with the access-log digest or move that receipt point to BS-L alone; and add to §5's
guard list that the runner requires a BS-L receipt bound to the mask digest exactly as it
requires BS-5f's — flagged as requiring the next code revision, which the Stage-P closure
already forces.

### F3 — BLOCKING — carried (KIMI-V12 F2), half-repaired: the (d) exclusion threshold still has two homes, and one of them cannot hold it

**Section / sentences.** §2.7(2)(d): exclusion only for "the instrument's confidence … below
the threshold **pinned in BS-3** for this run." §2.7(7) (renumbered, content unchanged): "The
thresholds in (d) are pinned before any image byte, **in BS-3**, with the same force as any
other frozen constant." §2.7(6): "The **numeric confidence threshold**, retry and failure
semantics, … are a **DESIGN** slot (**BS-2a**)". §7 BS-2a row (Class P): "the numeric
confidence threshold **and the named authority that sets it**…". §7 BS-3 row: "instrument
identity: weights `83008c1c…`, τ = 4.4006456017494235, antisymmetry identity" — no threshold
field; the pinned `SLOT_SCHEMA` gives BS-3 exactly `(weights_sha256, tau,
antisymmetry_receipt)` (v9 line 198).

**Why it fails as a promise.** The class contradiction is repaired — BS-2a sits in Class P
with the naming authority added, as the brief says. The threshold's home is not: two slots
still claim the same constant, and the pinned BS-3 schema has no field to receive it, so
"pinned in BS-3 for this run" is unreceiptable under §0 while "designed in BS-2a" is future
work. An operator can declare the (d) threshold already frozen by BS-3's quoted τ, fill BS-2a
without designing it, and bypass the only gate that exists to prevent an outcome-shaped
partition — changing the accepted set, which changes the answer. KIMI-V12 F2's repair
instruction was explicit ("Strike 'pinned in BS-3' from (2)(d) and the renumbered (7)"); V13
renumbered the list and V14 left both sentences standing. Second round unrepaired.

**Smallest sufficient repair.** Strike "pinned in BS-3" from §2.7(2)(d) and §2.7(7); name
BS-2a as the threshold's only home (or, if BS-3's τ is intended to be it, say so explicitly
and move its pin inside BS-2a's design gate with the schema field added).

### F4 — BLOCKING — NEW IN V14, inside the §6.1(3) repair: the exception set is not the complete set, its members are not symbol-identified as claimed, and the committee's isolation is contradicted by the slot table

**Section / sentences.** §6.1(3): "The only processes that may touch χ-bearing objects before
the lock are the instrument that writes χ, the cutout producer, the Stage-C runner, and §2.7's
acceptance-ledger recompute… and **each is identified by the pinned code symbol implementing
it**. A process not on this list may not run before the lock." And: "Its members may hold no
other role in this study and take no part in filling, adjudicating or locking." §7, Class E:
"| BS-8f | **Hwao + hand-check committee** | â, σ_a, a_LB, per-bin values, full Cov_a,
integrity triggers | Stage C |." §3: "Cov_a is the FULL covariance matrix … produced by
`accuracy_from_handcheck()` — a mandatory BS-8f field."

**Why it fails as a promise.** Three independent defects, all verified against the document
this round:

(i) **The identification sentence is false.** I searched §6.1 for the symbols: none is named
there — the section's only code-formatted token is `decide()` inside a historical blockquote.
Document-wide: the instrument's writer symbol exists nowhere (BS-3's row has code symbol "—";
the instrument is future BS-3/BS-9 work and is not in the pinned code at all); the cutout
producer's symbol exists nowhere (BS-9's row "—"; `nm_acquire_cutouts.py` is named only as
PROHIBITED); the Stage-C runner's symbol is never named (§4 describes Stage C as "the same
frozen generator" without naming one; BS-5f's class-E row has no symbol column). Only the
ledger recompute is symbol-identified (BS-2a's row: `run_production_verdict`, pre-verdict
validator). The sentence claiming all four are identified by pinned symbol is a
claimed-repair sentence that does not survive contact with its own document — and under §0,
three of the four "pinned" processes have no pinned existence.

(ii) **The set is incomplete, and the omission makes the lock unreachable.** BS-8f must be
produced before BS-5f, which must exist before BS-L. Producing BS-8f requires
`accuracy_from_handcheck()` to read the committee's χ-derived labels — a process touching
χ-bearing derivatives before the lock, named nowhere in (3). Under (3)'s own sentence, "a
process not on this list may not run before the lock", the calibration estimator may not run;
without it BS-8f cannot exist; without BS-8f no BS-5f; without BS-5f no lock. The study cannot
reach its own primary lock while complying with the covenant. (The committee's
label-ingestion path — whatever writes their labels into the sealed store — is a second
unnamed pre-lock process on the same critical path.)

(iii) **The committee's isolation is not real.** (3) bars its members from "any other role in
this study" and from "filling"; §7 names the committee co-producer — with Hwao — of BS-8f, a
slot it thereby fills. The two sentences cannot both be complied with, and which one yields
decides whether the one group that sees χ before unblinding also helps produce the
calibration record that sets the decision bands.

**Smallest sufficient repair.** Name the four processes by the pinned code symbols that
implement them (and where the implementation is future BS-3/BS-9 work, say so instead of
claiming a pin); add the calibration estimator and the label-ingestion writer to the
exception list with the same write-only-into-the-sealed-store condition; and reconcile the
isolation clause with the BS-8f row — either the committee labels and is done (Hwao alone
produces BS-8f from the sealed labels via the named estimator) or the bar on "filling" is
restated to name which slot they may touch.

### F5 — MAJOR — carried, re-verified: §2.4 and §10 still cite closure checks that exist in no pinned v9 artifact (KIMI-V12 F4)

**Section / sentences.** §2.4: "a manifest omitting those neighbours is refused **by name**:
`CLOSURE-FROZEN-PLANNER`, `CLOSURE-RETIRED-REFUSES`, `CLOSURE-CATCHES-HISTORICAL`,
`CLOSURE-CALLER-TRUST` (3/3 — …)." §10: "new fixture `CLOSURE-PRODUCTION-USES-FROZEN` asserts
the wiring by source inspection."

**Why it fails as a promise.** Re-grepped this round across the pinned fixture transcript, the
pinned probe suite (`closure_probe_suite_v9.py`) and the V9 probe receipt: of the four names
in §2.4, only `CLOSURE-RETIRED-REFUSES` exists in any v9 artifact; the other three, and §10's
`CLOSURE-PRODUCTION-USES-FROZEN`, occur in **zero** (count verified: 0, 0, 0 files). The v9
battery's only planner check is digest-only (`CLOSURE-PINNED-PLANNER`); no pinned v9 check
functionally runs the planner over the two historical objects, and no pinned artifact carries
the "(3/3)" caller-trust battery. The underlying claims are supported elsewhere (the probe
receipt's real-data 12,117 derivation, verified above) — but the sentence attributes them to
named checks the frozen mechanism does not carry. Third round: a preregistration citing
non-existent evidence at the paragraph it keeps rewriting to repair that exact failure class.

**Smallest sufficient repair.** Cite what exists: `CLOSURE-PINNED-PLANNER` (digest), the probe
receipt's real-parent derivation, and the referee's functional verification named as ad-hoc —
or restore the functional fixtures at the next code revision and then cite them.

### F6 — MAJOR — carried, re-verified: §4's z\* sentence is still contradicted by the pinned fixture, and the same false sentence sits in the pinned code's docstring (KIMI-V12 F5 / KIMI-V11 F6 / CODEX-V11 5)

**Section / sentence.** §4: "across four geometries the measured z\* ranged 3.0376–3.1355,
bracketing the normal 3.0902, and on the polar geometry this design actually selects the
normal threshold came out anti-conservative."

**Why it fails as a promise.** The pinned v9 fixture prints z\* = 3.0694, 3.0010, 3.0020,
3.0260 — range 3.0010–3.0694, every one **below** 3.0902. They do not bracket the normal
value; 3.0376 and 3.1355 appear in no artifact; and the identical sentence sits in
`reference_null_z()`'s docstring in the pinned code (v9, the docstring at lines ~1163–1167) —
definitional surface in a document that pins code by digest. The conclusion survives via the
same battery's `PWR-Z-STABLE` tail masses beyond z = 3.090 (0.00135, 0.00130, 0.00100,
0.00110 — three of four heavier than nominal), which the text never quotes. Fourth round this
misquote stands in both the text and the pinned code.

**Smallest sufficient repair.** Quote the artifact: "the four fixture geometries' standardized
0.999 quantiles measured 3.0010–3.0694, all below the normal 3.0902, and tail mass beyond
3.090 measured up to 0.00135 (`PWR-Z-STABLE`) — the normal threshold is not safe either way."
Carry the same edit into the code docstring at the next code revision.

### F7 — MAJOR — carried, re-verified: the exact Stage-P receipt's subject is v7 bytes, and V14's disclosure still does not say so (KIMI-V12 F8 / KIMI-V11 F7)

**Section / sentences.** §2.6: "`stagep_exact.py` is a measurement harness; the exact-null
Stage P is not implemented in the file §0 pins." §10: "it is measured, not accepted."

**Why it fails as a promise.** The receipt's `subject.path` is `../ref/successor_ref_v7.py`,
sha `6be341bd…` — verified against the on-disk v7 this round — not the v9 bytes §0 pins. "Not
in the pinned code" and "measured against a different, unpinned version of the reference" are
different disclosures; the text makes the first and withholds the second, and the receipt's
own stated-limits line discloses the v7 subject while the text's does not. I re-verified the
mitigation: the v7→v9 diff is 19 lines confined to `closure_receipt()`; every primitive the
harness calls is byte-identical, so the 995/1000 transfers to the pinned bytes. That is the
referee's work, done three times; the promise should not require the next reader to repeat it
to trust the design's decisive number.

**Smallest sufficient repair.** One sentence in §2.6: "the harness ran against v7; every
primitive it calls is byte-identical to the pinned v9 (the v7→v9 diff is confined to
`closure_receipt()`), so the measurement applies to the pinned code; it remains unrefereed and
BS-5p stays unfillable until folded in."

### F8 — MAJOR — NEW: the document misnames itself, its predecessor, its slot count and its slot classes — at the freeze boundary where self-naming is load-bearing

**Section / sentences.** Line 1: "# PREREGISTRATION DRAFT **V13**" (the file is V14; there is
no V14 version statement anywhere in the header, whose newest blockquote describes V13 and
says "anything [KIMI's round-3 report] adds folds into V14" — true when written, now history
describing a revision the reader is holding). Line 31: "Supersedes **V9**". §7: "**One of
twelve class-P slots** is filled (BS-2m)" above a Class-P table with **14 rows** (BS-1, BS-1b,
BS-2a, BS-L, BS-2c, BS-2o, BS-5p, BS-2s, BS-2m, BS-3, BS-9, BS-4, BS-7p, BS-8p — counted);
the brief to this round says "Fifteen class-P slots" — the prose, the table and the brief give
three different counts. The same §7 sentence: "BS-2f, BS-5p, BS-8p and BS-9 are DESIGN slots"
— omitting BS-2a (whose own row says DESIGN, moved in V13), omitting BS-L (unclassifiable
under either class, F2(b)), and including BS-2f, whose row now says "**value-only**: the
realised partition produced by BS-2a's frozen code, not a new rule" — contradicting §2.7's
own closing line, which still calls BS-2f "a design-and-implementation slot rather than a
value slot (see §7)". §2.6's closing: "These fill the class-P inputs that six gate rounds said
could not be closed by writing alone" — the measurements fill no slot under the document's own
VALUE/DESIGN language (carried KIMI-V11 F11), and "six gate rounds" is stale by several
rounds.

**Why it fails as a promise.** The header's freeze condition is "every class-P slot holds a
receipt". The table defines the set and controls (14) — so the freeze set is determinable and
this is not blocking — but a document that cannot state its own version, the count of its
freeze prerequisites, or the classes of the slots it tabulates cannot be conformance-checked
without the reader silently repairing it first, and §6's own conduct rules ("one change per
iteration… the §10 trace maps finding → change"; "no claim stronger than its check") make the
repair-trace surface exactly where these misstatements sit. The BS-2f DESIGN/value
contradiction is the freeze-relevant half: §2.7 says BS-2f is design-and-implementation while
§7's table and §2.7(6) say value-only — one document, two classes for the same slot.

**Smallest sufficient repair.** Retitle to V14 with a one-blockquote V14 statement and correct
the supersedes line; rewrite the §7 classification sentence from the table ("fourteen class-P
slots, one filled (BS-2m); DESIGN: BS-2a, BS-2f's producer BS-2a…, BS-5p, BS-8p, BS-9, BS-L")
so the prose and the table say the same thing; strike or reword §2.6's closing line; and make
§2.7's closing sentence agree with the table on BS-2f.

### F9 — MAJOR — carried: no binding interpretation of what an answer means (KIMI-V12 F6 / GPT56-V12 F5; the brief's question 7, fourth round running)

**Section / sentences.** §1: "It does not test A ≈ 0.02, Shamir, BHU, or whether the sky is
isotropic." §5 defines the four outcome labels and stops.

**Why it fails as a promise.** Verified again this round: those are the text's only isotropy /
interpretation sentences. The text never states that REJECTED-AT-LONGO-AMPLITUDE excludes the
published amplitude at the published axis under this design's sensitivity and nothing more —
not isotropy, not smaller amplitudes, not other axes, not other researchers' claims. It never
states that every INCONCLUSIVE* supports neither reproduction nor rejection. It never states
that a precise opposite-sign result (Â < 0, p < 0.001) lands in INCONCLUSIVE — a strong
anti-Longo result wearing a label that reads as "no result". The brief states these limits in
its own question 7; the promise still does not contain them, and a later summary can quote the
registered outcome verbatim and overread it with nothing in the binding text forbidding the
overreading. `WHAT_IS_AT_STAKE_20260827.md` carries them; the promise does not.

**Smallest sufficient repair.** Two sentences in §5 plus the BS-V results template, along the
lines both seats drafted last round.

### F10 — MAJOR — carried: the Branch-A availability event still has no frozen probe (KIMI-V12 F7 / GPT56-V12 F6 / KIMI-V11 F8)

**Section / sentences.** §2.1: Branch A is selected "iff the DR11 photo-z product exists and
is publicly retrievable at the resolution moment"; BS-1 fills on "the day DR11 photo-z is
confirmed available" or 2026-09-05 (`BRANCH_FALLBACK_DATE` verified pinned at code line 1665).

**Why it fails as a promise.** Re-verified: the pinned `resolve_branch()` accepts a
caller-supplied `photoz_available` boolean and validates only date shape/order (v9 lines
1665–1685). "Exists", "publicly retrievable" and "confirmed" have no frozen probe, endpoint
set, schema check, retry/error policy, timestamp convention or witness. Before the fallback
date, delaying or avoiding a check delays the earlier event; a transient mirror or auth
failure turns existence into apparent absence. An operator can steer the branch — which §2.1
correctly makes outcome-bearing (Branch A voids the §0 pin and demands a fresh gate) — while
satisfying every word.

**Smallest sufficient repair.** Freeze the probe: named authoritative URLs/products, the
schema/version check that constitutes "exists", retry window and transient-error treatment,
timestamp/zone, signed raw-response receipt; BS-1 a pure function of that receipt.

### F11 — MAJOR — carried (GPT56-V12 F4): §6.1(6) says artifact contents "establish" the historical redesign was blind; they cannot

**Section / sentences.** §6.1(6): "What establishes that the redesign was blind… The record of
that choice (`real/REAL_GEOMETRY_RESULT_20260825.md`, the selection artifacts and their
digests) contains no χ-derived quantity, and that is checkable by inspection."

**Why it fails as a promise.** I re-inspected the named record: it does contain no χ-derived
quantity — the checkable sentence is true. What it establishes is one-directional: finding a
χ-derived quantity would prove breach, but not finding one does not prove no designer read the
predecessor's sealed store before writing a geometry-only artifact. The geometry choice
predates this text; the covenant's logging begins with it. The clause's own title —
"What establishes that the redesign was blind" — overclaims its content, and §6's "no claim
stronger than its check" is the document's own rule against exactly this. GPT56's proposed
repair (a retrospective custody/attestation receipt over the design window, or downgrading the
claim to unverified testimony) stands unaddressed.

**Smallest sufficient repair.** Downgrade the verb: "what is checkable is that the redesign
record carries no outcome-derived quantity; if any is ever found the licence fails. That the
redesign was in fact blind rests on attestation, named here with its evidence class." Or
produce the retrospective custody receipt GPT56 specified.

### F12 — MINOR bundle (small, same-edit repairs; carried unless noted, all re-verified this round)

- **Bare-CLEAR quote vs the artifact's verdict line** (§0, §7 BS-2m row): the artifact's
  verdict is "**CLEAR** — with conditions named below" (CLOSURE_V9_KIMI.md line 5); §0 and §7
  quote "CLEAR". §6's own rule: gate-state sentences never exceed the cited artifact's verdict
  line. Add the qualifier.
- **The cited geometry receipt still carries the stale floor count**: its "STAGE P RESTORED"
  stated-limits line reads "995 of the 1,000 own p-values sit at `5.00e-05`" — my
  recomputation from the receipt's own `p_own_by_trial`: **951** at 1/20,001, 995 below 1e-3.
  V14 §2.6 says 951 (right) while citing an artifact that says 995 (wrong) (GPT56-V12 F7,
  unrepaired). Also §2.6 quotes the floor as "5.00e-05"; the exact value is
  4.999750012499375e-05.
- **BATTERY-POS quoted as "p = 2.2e-21"** (§5) vs the fixture's "p = 2.23e-21". Quote the
  fixture's digits.
- **208,405 vs 208,407, still unreconciled.** Header/§6.2: "208,405 sealed χ measurements";
  §2.6's declined-run row: "208,407 objects". Consistent with §8(1)'s two-WAITING narrative;
  the text never says so. One parenthetical.
- **§0 names the fixture transcript without its digest or normative status** (carried
  KIMI-V11 F12). Recomputed: `fab32ba24cedcedf7fe601c3a8d9dbde13f57b1c9bf2e0b88963bcfebc33a8b5`.
- **The tested axis is never quoted or tolerance-bound in the text** (carried): §1 makes
  `AXIS` definitional and Longo's own value is "approximately"; no sentence binds the mapping
  or a tolerance.
- **Missing commitments, still absent from the binding text** (carried): the reporting
  commitment (nothing commits the verdict, whatever it is, to be reported); the
  no-secondary-endpoints sentence (`explore_verdict()` exists; nothing bars presenting
  non-`run_production_verdict()` analysis as the preregistered result); public-deposit /
  external-timestamp of the freeze; a sunset for the run if slots cannot be filled;
  `RETENTION_LB = 0.8572` provenance; §10's class-E judgment calls (integrity triggers,
  checksum-mismatch disposition, committee adjudication) unfrozen in text or schema.
- **§0's definitional reach vs the O(n²) disclosure** (carried): "every operational mechanism
  … DEFINED by the code bytes" still covers production scale, where §2.6 discloses the pinned
  `greedy_ledger()`/`local_pass()` cannot execute and vectorized equivalents are "proven" only
  on 40/30/400 sampled cases.

## The deliberately-open Stage-P blocker — ruling requested by the brief

I do not treat its openness as repaired, and I do not re-litigate the round-3 ruling the
principal accepted (honest draft status; not a freezeable promise while the pinned code
implements the shared-null route). The brief asked whether leaving it open invalidates
anything else I would otherwise pass. **Yes, two things beyond BS-5p itself.** First, §4's
Stage C — the lock's only pre-unblinding gate — runs "the same frozen generator, addresses and
pass rule" as Stage P, i.e. the same shared-null machinery whose route is unresolved; so the
BS-5f → BS-L → unblinding sequence this round's repair claims executable is dual-valued at its
first link, before any of F2's receipt defects. Second, the slot chain BS-5p → BS-2s → BS-2m
puts the one filled class-P slot downstream of the unfillable one, so BS-2m's "FILLED" rests
on values (6,445 / 65,060 / 12,117) produced by the route the document has not chosen between.
Both are disclosed nowhere in those terms. And on the brief's own verdict rubric — CLEAR =
"sound enough to be frozen once its slots are filled" — the open blocker alone forces NOT
CLEAR, because BS-5p is expressly unfillable under the pinned bytes: the state the rubric
describes cannot obtain. My F1–F4 are independent of that and would force the same verdict on
a text whose Stage-P route was already closed.

## Answers to the brief's eight questions, compressed

1. **Can it fail?** Yes — the outcome space is partitioned and boundary-closed (0.001 ≤ p ≤
   0.05 is explicitly INCONCLUSIVE; ties by exact float ≥; plus-one p), only the pinned code
   emits a label, REJECTED-AT-LONGO-AMPLITUDE is a named reachable failure, and BATTERY-A0 /
   -SIGN / -POS / -NEQ are pinned demonstrations (all re-verified). The soft spots are the
   interpretation omission (F9) and the dual-valued seams (F2, F3), not the structure.
2. **Degrees of freedom.** Open after seeing data, and their status: the exclusion threshold's
   home (F3 — contradicted, not closed); which §6.1 clause yields so BS-8f can exist (F1 — new,
   contradiction); which receipt seals the lock and when the roster is named (F2 — open);
   which processes may run pre-lock (F4 — the list is under-inclusive, so an operator must add
   to it); the branch trigger event (F10 — caller boolean); the Stage-P route (declared open,
   freeze-blocking); acceptance design (BS-2a — declared DESIGN, correctly classed now);
   integrity triggers / checksum-mismatch / committee adjudication (F12 — unfrozen). Each is
   declared or named; F1, F3 and F4 are not honestly declared — two are contradictions and one
   is a false identification sentence.
3. **Circularity.** None in the forbidden direction: Stage P injects at the frozen amplitude
   on count-derived geometry; Stage C runs on the sealed sign-free mask with calibration
   measured pre-unblinding; the detection floor is a frozen formula evaluated at a named
   measured point; the N_eq floor is derived by code from the mask's own geometry; the
   decision regions are fixed numbers. The residual risks are procedural, not numeric (F3's
   threshold authority, F10's branch trigger).
4. **Numbers vs artifacts.** Everything I could recompute verifies (list at top) except the
   named stale items: the z\* range in text and pinned docstring (F6), the dead fixture names
   (F5), the geometry receipt's "995 … sit at 5.00e-05" against its own data's 951 (F12),
   p = 2.2e-21 vs 2.23e-21, "5.00e-05" vs 4.99975e-05, 208,405 vs 208,407, the bare-CLEAR
   quote, and — new this round — "one of twelve" against a 14-row table (F8). The three
   advertised 2026-08-26 fixes (stale pin, retracted 997, download size) are present and
   correct.
5. **Is the blinding real?** Structurally stronger than any prior round: a universal ban, an
   enumerated exception list, a committee named, logging required, void on any access, a
   checkable sentence, redesign evidence named and inspected clean. But the void clause
   swallows its own exceptions (F1), the exception list omits the calibration path the lock
   depends on (F4), the roster has no pre-image home (F2(c)), and the log's completeness still
   rests on custody with no stated technical means — a holder decrypting outside the logged
   path leaves no entry, and nothing would show it. What would show a look today: the log, for
   paths that flow through it; nothing, for a holder who bypasses it.
6. **Honest incompleteness.** The draft banner, the VALUE/DESIGN distinction, the retraction
   chain, "measured, not accepted", and the open Stage-P banner remain exemplary in kind. But
   this round the document misstates its own version (V13 on line 1), its slot count (twelve
   vs 14), its predecessor line (V9), one artifact's verdict (bare CLEAR), one receipt's floor
   count by citation, and one repair's own mechanism ("each is identified by the pinned code
   symbol" — false). It reads more repaired than it is at exactly the sentences that claim
   repair.
7. **Null-result overclaim.** No overclaim anywhere in the text. The gap remains the omission:
   the three limits the brief itself states are still not in the binding text (F9).
8. **Missing entirely.** Beyond F9–F11 and the F12 list: **the sealed store and the keys have
   no provenance.** No slot provisions the sealed results store, generates the keys, splits or
   escrows them, or stands up the logging wrapper — the covenant's entire subject matter comes
   into existence off-stage between BS-6 and BS-L, and the one artifact that might carry it
   (BS-2a, acceptance design) is scoped elsewhere. A preregistration whose blinding rests on a
   store and keys should say whose job creating them is, by when, receipted how. Also still
   missing: the reporting commitment, the availability probe (F10), the interpretation clause
   (F9), retrospective custody evidence for the redesign window (F11), a sunset, a public
   deposit, and the no-secondary-endpoints sentence. None needs the machinery reopened; all
   are invisible if you only referee the machinery.

The brief's five known-wrong items: confirmed accurate as stated; none understated — with the
standing shading that the one-seat verdict quoted in support is "CLEAR — with conditions named
below", and the open Stage-P blocker propagates further than the brief's list states (Stage C
and the filled BS-2m both sit on the unchosen route, per my ruling above).

## Testimony (asserted in the text or receipts; not independently verified by me)

- BS-3 instrument values (weights `83008c1c…`, τ = 4.4006456017494235, antisymmetry identity)
  — unfilled slot, quoted in the table; `83008c1c` appears in no receipt under `real/` or
  `gates/*.json` (re-grepped this round).
- The predecessor documents quoted by sha (V3-pred `b06901c8…`, BS6-pred `5ff7f454…`, decline
  memo `b4a1f1fc…`): existence and contents outside the review set; the eight Cut-6
  predicates' byte-identity to BS6-pred accepted, not checked. The 208,405 sealed count itself.
- "DR11 pages exist; no photo-z product is present" (measured 2026-08-24) — author's
  measurement; F10 exists because the probe that would change this is unfrozen.
- The frozen planner's source file (`_objmanifest_20260820/build_object_manifest.py`) is not
  in this tree; its digest is verified via the code pin and `CLOSURE-PINNED-PLANNER`, its
  behaviour via the probe receipt's real-data derivation, not by my re-execution.
- Equivalence batteries: 40 (order), 30 (reduction), 400 (swap phase) cases, zero mismatches —
  stated in the geometry receipt and §10; no independent receipt in the named set.
- "12,117 reproduced independently three times" — the closure derivation is in the probe
  receipt (verified); the two direct enumerations are asserted in §2.6/§7.
- 12.2 MB/brick unit price and the 735.9 GB declined download — predecessor-era figures.
- The conduct narrative (drafting authorization, catalog-only authorization, "no χ was read",
  the 2026-08-26 ceiling raise, provider refusals of the two mechanism seats, the fork status)
  — conduct testimony; nothing in the artifacts contradicts it.
- "v4 through v7 remain on disk unchanged" — files present; v7 re-digested this round
  (`6be341bd…`, matches the receipt); v4–v6 content-unchanged accepted, not re-digested.
- §8(3)'s "42.76%" inflation figure — predecessor-era, not recomputed.

## Verdict

One advertised repair landed whole (BS-2a's class and the numbering housekeeping), one landed
as a sentence and broke its own boundary (the universal ban, F1), and two did not land where
they govern: the lock/verdict cycle is unreceiptable at five verified points including the two
the V13 blockquote names as repaired (F2), and the §6.1(3) exception list is simultaneously
over-broad in its void, under-inclusive for the calibration path, falsely symbol-identified,
and contradicted on the committee's isolation (F1, F3, F4). The deliberately-open Stage-P
blocker is not treated as repaired; left open, it also dual-values Stage C and the filled
BS-2m's input chain, and on the brief's own rubric it alone prevents the "once its slots are
filled" state from obtaining. F5–F11 must be repaired in the same revision; the F12 bundle
should be. All blocking repairs are text-level except those that ride the already-forced next
code revision (BS-L schema/gate, BS-2f schema field, the docstring misquote).

Blocking findings: **F1** (§6.1(2)/(5) void the exceptions §6.1(3) authorizes — the committee's
mandated view and the named processes' touches void the run under the text's letter), **F2**
(the BS-5f → BS-L → unblinding → BS-V sequence cannot be executed or receipted end to end:
BS-V still carries "primary lock" in §7 and §10, BS-L has no class or schema, the roster has
no pre-image home, the log digest has no BS-2f field, and the only verdict path has no lock
gate), **F3** (the (d) exclusion threshold is still homed in both BS-3 and BS-2a, and BS-3's
pinned schema cannot hold it), **F4** (the exception set omits the calibration path the lock
depends on, its members are not symbol-identified as claimed, and the committee is barred from
a role §7 assigns it).

**NOT CLEAR**
