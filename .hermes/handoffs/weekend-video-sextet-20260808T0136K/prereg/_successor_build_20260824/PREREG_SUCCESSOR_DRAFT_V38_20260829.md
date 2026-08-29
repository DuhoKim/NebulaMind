# PREREGISTRATION DRAFT V38 — LONGO-AMPLITUDE TEST ON A LEVERAGE-CHOSEN FOOTPRINT

> **V27 is a repair of V26.** It repairs `PREREG_SUCCESSOR_DRAFT_V26_20260827.md`, sha256
> `2eec8da41ee69374fcc9c3fca2de150b29c04ca7b921848e908fa97a20bffd52` — independently verified.
> Both seats verified the capability inventory by parsing the pinned source. The guard sentence at lines 458-461 is repaired here.
> Its Part 1 is byte-identical to the R14 §6 body both referee seats credited.
>
> The fold was **instructed and initiated at 21:48 KST on 2026-08-27, before any verdict existed.**
> The referee round ran in parallel with the assembly. When the verdicts landed
> during the assembly:
> - **CODEX, 21:52:33 KST — CLEAR.** No blocking finding; Part 2 completeness holds at
>   fold-instruction level. One **LOW / NON-BLOCKING** note: Part 5 line 159 uses a stale status
>   label for the R14 completeness finding. CODEX states this does not weaken any required edit.
> - **GPT56, 21:53:46 KST — NOT CLEAR.** One **HIGH / BLOCKING** finding: **the canonical
>   unblinding-receipt schema is still absent from the asserted-complete Part 2 list.**
> - Both agree four of the five R14 seams are **CLOSED** — §7 count and DESIGN inventory, §5
>   guard seam, §2.5 producer-checksum narrowing, and the Clause 10 / §10 repair-trace seam.
>   The canonical receipt/schema seam is **narrowed but not closed**: the slot-schema portion is
>   done; the unblinding-receipt schema itself is still omitted.
>
> The final bytes of V16 were written **after** applying the GPT56 schema-inventory repair, not before the verdicts existed.
>
> The GPT56 blocker is **closed at document-contract level by this edit** — the schema and its authenticated
> fields are now required work in §11 — while the **implementation remains UNRESOLVED** with findings
> 1, 2, 2b and 3 pending the **DESIGN, defined, UNFILLED** BS-2a design.
>
> **Linter note:** The earlier `prereg_lint.py` BS-2f finding was a **false positive in the
> linter, not a defect in this document**: the flagged sentence is the fold record quoting what V15
> said, and BS-2f correctly sits in Class E. The linter has been corrected and V16 now lints clean.
>
> **Carried-open items:** **BS-2v coverage still not independent of the converter**; **BS-2v still has no authenticated receipt schema a gate could reject against**; **§6.1 Row L's signing path voids itself** (CODEX-V24-1); **preamble lines contradicting the live unresolved status** (GPT56-V24-5).
>
> **V13 repairs the executable-order and slot-placement blockers of the third text review
> (2026-08-27), and does NOT repair the Stage-P blocker, which needs a code change and a
> decision that is not mine — see §4.** GPT56 and CODEX both ruled that V12's posture of
> declaring Stage P openly dual-valued is honest draft status and **not** an acceptable
> preregistration promise. I asked them to rule on exactly that and they did. KIMI's round-3
> report had not landed when this revision was written; anything it adds folds into V14.
>
> **V12 repaired three of the four BLOCKING findings of the second text review (2026-08-27).**
> Three seats read V11 as a fresh subject and all three returned NOT CLEAR again — with every
> blocker landing in the V11 repairs rather than in anything V10 had survived. Reports:
> `gates/PREREG_TEXT_V11_{KIMI,GPT56,CODEX}.md`. **The fourth blocker is deliberately left open
> and is named in §4; it cannot be repaired by editing this text.**
>
> **V11 repaired the six BLOCKING findings of the first text review (2026-08-27).** Three seats —
> KIMI, GPT56 and CODEX — refereed this document as a promise for the first time and all three
> returned NOT CLEAR (`gates/PREREG_TEXT_{KIMI,GPT56,CODEX}.md`). Every repair below names the
> finding it answers. Three numeric errors they found are corrected in place and flagged, because
> a preregistration that misquotes its own receipts has no standing to demand accuracy of anyone
> else.

> **THIS IS A DRAFT. NOTHING IN IT IS IN FORCE.** Drafting was authorized by Duho on
> 2026-08-25 (~12:2x KST, relayed by Blanc): *"Draft the prereg now."* That authorization
> covers **WRITING this frozen promise only** — selection rule, estimator binding, decision
> regions, power requirement, blinding clauses. It authorizes **no run, no fetch, no data
> touch**. This text goes through its own adversarial gates before any real datum is touched,
> exactly as its predecessor's discipline required. It becomes a preregistration only when
> every class-P slot holds a receipt, the gates pass, and Duho signs the freeze.

Hwao, 2026-08-25 18:00 KST. Supersedes V9 (sha `b97ba35c…`, REVISE from both seats; kept).
Predecessor status: **DECLINED BY SIGNATURE 2026-08-25**
(`DECISION_MEMO_DECLINE_TO_PROCEED_20260821.md`, EFFECTIVE, sha
`b4a1f1fcaa9acbaa6b9efd3ebbe9496be8c1d83c690a012dc7a4f8520840374f`); its verified
60,308-brick sample is archived as successor input. Its **208,405 sealed χ measurements are
NOT an input to this study** — see §6.2, which governs. (V12, repairing KIMI-V11 F2 /
GPT56-V11 F2 / CODEX-V11 2: V11 added §6.2 saying the measurements are not an input and left
this sentence calling them one, eight lines from the top of the document.)

## §0 Definition by reference implementation

Every operational mechanism of this preregistration — geometry, ledger, selection chain,
retention, manifest closure, mask typing, randomness addressing, injection, permutation
contract, estimators, sigmas, calibration, the decision function, the run guards, and all
digest serializations — is DEFINED by the code bytes of

- **`ref/successor_ref_v9.py`, sha256 `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`**
- the custody boundary it calls, **`ref/closure_worker_v9.py`, sha256
  `28f8e1f9a8c7bd3d4cf1aabf71a7dfae5f9a1da6b92a6f09fd9c65bfc7ea5959`**
- fixture output **`ref/FIXTURES_V9_20260826.out`**

> **THE PIN WAS STALE AND IS NOW PROVISIONAL (2026-08-26).** This section pinned
> `successor_ref_v4.py` at sha `0b312c96…` from 2026-08-25 17:47. That file was rewritten the
> same evening and four times since; the bytes named here defined nothing that existed. A
> document that defines every mechanism by code bytes fails completely when the pin drifts, and
> it drifted within hours of being written.
>
> The pin names v9, and **as of 2026-08-26 23:08 KST it is not provisional**: those exact bytes
> carry a completed referee verdict (`gates/CLOSURE_V9_KIMI.md`, **CLEAR**, sha `f2ee062b…`) and
> are held read-only under `gates/FREEZE_CLOSURE_V9_20260826.md`, which supersedes the v8 freeze
> without rewriting it. v9 differs from v8 by one repair: the worker's interpreter state is
> carried into every receipt, so two claims that were false at the v8 freeze are true and
> probe-checked. That verdict
> is **one seat**: the codex and gpt56 seats were refused by their provider's safety filter, so
> this is a narrower review than the panel intended, and the freeze record says so in its own
> text. v4 through v7 remain on disk unchanged so each round's referee reports stay legible
> against the digests they pin.

Prose states claims, thresholds, chronology, authority and conduct. **Where prose and code
could be read to disagree, the code is the definition and the prose is the defect.** The
frozen environment is asserted by `require_environment()` (python 3.9, numpy 1.26.4,
little-endian); receipts carry `environment_record()`; fixture digests are valid under that
environment. Supersedes V5–V9 and refs v1–v3, all retained for provenance.

Sources: `SUCCESSOR_SCOPE_20260821.md` incl. Amendment 1; predecessor
`PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md` (sha `b06901c8…`, "V3-pred"); its
selection receipt `LANA_BS6_PHOTOMETRIC_CUTS_20260814.md` (sha `5ff7f454…`, "BS6-pred").

## §1 Claim boundary, target, axis, and citation anchors

**Target, cited and verified from source 2026-08-25** (not from memory — the anchor-block
law): Michael J. Longo, *"Detection of a Dipole in the Handedness of Spiral Galaxies with
Redshifts z ~ 0.04"*, Physics Letters B (2011), **doi:10.1016/j.physletb.2011.04.008**,
bibcode **2011PhLB..699..224L**, arXiv:1104.2815. Its abstract states the dipole amplitude
as **"−0.0408 ± 0.011"** from **15,158** spirals, axis **"approximately (l, b) = (52°,
68.5°)"**.

**Counter-anchor, cited and verified directly from the source abstract:** Kate Land, Anže Slosar, Chris Lintott, Dan Andreescu, Steven Bamford, Phil Murray, Robert Nichol, M. Jordan Raddick, Kevin Schawinski, Alex Szalay, Daniel Thomas, Jan Vandenberg, **"Galaxy Zoo: The large-scale spin statistics of spiral galaxies in the Sloan Digital Sky Survey"**, 2008, arXiv:0803.3247. ~37,000 SDSS spirals. The abstract states the winding sense is **"consistent with statistical isotropy"**, with **"no significant dipole signal, and thus no evidence for overall preferred handedness"**, and — after establishing and correcting for a level of bias — that previous studies **"may also be affected and explained by a bias effect."** This published null predates Longo (2011) and is on a comparable sample.

**Bias magnitude (why the instrument is antisymmetric by architecture):** McAdam & Shamir describe *"that large difference of ∼15%"* between the original Galaxy Zoo 1 manual annotation counts, attributed to *"bias of the human perception or the user interface, rather than a reflection of the real distribution of spiral galaxies in the sky"* (read from arXiv:2302.06530's body text; Land's own body text was not read, and no raw counts for it are given there — the figure is a relative difference between two annotation counts, so it does not share a denominator with a normalised dipole amplitude). **No ratio between that figure and Longo's 0.0408 is asserted here, and none is available:** a uniform classification preference is direction-independent, an intercept, whereas the tested dipole is a slope in cosθ, and the centred estimator absorbs the intercept (`gates/FRAMING_LEVERAGE_IS_IDENTIFIABILITY_20260828.md`). **What that figure motivates is the instrument's architecture, not a calibration of it.** It is a property of *human* annotation. This study measures with an automated instrument defined as `χ(x) = (w(x) − w(mirror(x)))/2`, for which `χ(mirror(x)) = −χ(x)` holds *for any* weights; the parity-even response — the whole class of bias the Galaxy Zoo figure exemplifies — is therefore **zero by architecture, receipted bit-exact at `max|χ(mirror(x)) + χ(x)| = 0.0` on 1000/1000 synthetic spirals**, acceptance is handedness-blind because `|χ(mirror(x))| = |χ(x)|`, and **a spatially uniform parity-even classification preference contributes no centred dipole slope under the exact mirror construction** (`paper/PAPER_DRAFT_SPIN_INSTRUMENT_20260812.md` §2). **That is the whole of what the identity enforces.** An earlier draft said a biased or broken `w` "cannot create" a signal; both seats refuted it and the document contradicted it three sentences later. A classifier responding to parity-odd raster artefacts, to upstream non-equivariant processing, or to sensitivity that varies with position can produce a dipole-like slope under a null sky — which is exactly why the three surviving routes below are named rather than dismissed. **BS-3's `antisymmetry_receipt` verifies that identity. It does not measure sky-position dependence and this preregistration does not claim it does** — stratifying a quantity that is identically zero returns zero in every bin. **The threats that survive the architecture are different in kind**, and §2.3 of that instrument description names them: chirality introduced upstream of the analysis raster, sample selection by a non-equivariant process, and a nonzero global offset multiplied by a sky gradient in sensitivity — *"which must be bounded by an explicit control, not assumed away."* **That explicit control is DESIGN, UNFILLED:** its statistic, sample, positional stratification, uncertainty, bound, acceptance rule and failure consequence are not bound by this document, and must be bound before BS-6. **As of V37 that precondition is carried by a named slot — `BS-3g` (class P, DESIGN/UNFILLED), which blocks BS-6 in §7.** Before V37 this sentence asserted a precondition that no dependency edge enforced: every enumerated class-P slot could have been filled and every gate passed with this control still unbuilt, and nothing in the document would have noticed (GPT56-V34-1). Note also that Land's sample is SDSS while this study is defined on the DESI Legacy Surveys — a closely related task, not the same survey.

**The literature is split:** A later reanalysis (Darius McAdam & Lior Shamir, *"Reanalysis of the spin direction distribution of Galaxy Zoo SDSS spiral galaxies"*, [arXiv:2302.06530](https://arxiv.org/abs/2302.06530)) reports a parity-violation probability *"lower than 0.01"* and a cosine-dependence *"dipole axis with statistical strength of 2.33σ to 3.97σ"*. **Stated precisely, because the distinction matters:** for Land's mirrored-image control specifically, that reanalysis reports P∼0.13 and P∼0.21 and says *"these probabilities are not considered statistically significant, which can possibly result from the low number of galaxies, but the direction and magnitude of the distribution also does not conflict with the observed distribution."* **The reanalysis therefore does not establish that Land's post-mirror residual is significant**; its significant results come from its own separate analyses. This split is recorded as context for why the question is contested, and this preregistration does not adjudicate it.

**Sign, stated so it cannot be inverted by a later reader.** Longo's published amplitude
carries a MINUS sign in his convention. Our East-of-North winding convention maps it to
**+0.0408** (V3-pred F-5), and the code constant `A_LONGO = +0.0408` is our-convention while
`A_LONGO_PUBLISHED_SIGNED = −0.0408` records his. The mandatory synthetic absolute-sign
anchor (BS-4) re-establishes the mapping empirically before any real image; the fixture
`BATTERY-SIGN` demonstrates that an injected **−0.0408** sky is never called REPRODUCED.

This tests that published amplitude at that published axis. It does not test A ≈ 0.02,
Shamir, BHU, or whether the sky is isotropic. **Fixed-axis.** The machine axis is the `AXIS`
constant; all coordinate pairs are display-only; frames are ICRS wherever coordinates appear.

## §2 Population, release choice-point, selection chain, manifest closure

### §2.1 The release choice-point — BOUND, both branches specified, resolved on its date

The DR11-vs-DR10.1 fork stays **open inside this frozen text as a bound choice-point**, so
the data decision slots in on its date without reopening frozen wording. Exactly one branch
is selected at BS-1 and recorded there; nothing else in this document changes with the
branch.

- **Branch A — DR11.** Selected iff the DR11 photo-z product exists and is publicly
  retrievable at the resolution moment. Inputs: DR11 south sweep catalogs, DR11 photo-z
  product, DR11 survey-bricks manifest, DR11 coadd image tree.
- **Branch B — DR10.1.** Selected otherwise. Inputs: the corresponding DR10.1 products.
> **THE FROZEN DEFINITION IS NOT BRANCH-NEUTRAL, AND V10 IMPLIED IT WAS (V11, repairing
> CODEX 3).** §0's normative code and every measurement in §2.6 are specific to **DR10 south,
> Branch B**: the pinned geometry sidecar, the count table, the selection, the parent and the
> 12,117-brick closure are all DR10 artifacts. If Branch A is selected, **none of those pins
> carries over.** Branch A requires re-measuring the universe, count table, selection, parent
> and closure on DR11, re-pinning §0, re-running the fixtures, and a fresh text gate before
> freeze — it is a new preregistration in everything but name. This text does not pretend
> otherwise, and BS-1 selecting Branch A therefore voids the current §0 pin rather than merely
> setting a flag.

- **Resolution rule.** BS-1 is filled on the earlier of (i) the day DR11 photo-z is confirmed
  available, or (ii) **2026-09-05**. On (ii) with photo-z still absent, Branch B is selected
  and the choice-point closes; waiting further requires a gated amendment.
- **Branch-invariance requirement.** BS-1's receipt must show that every downstream artifact
  named in §7 is produced by the same code path under either branch, differing only in the
  recorded input paths/versions. Any branch-specific logic is a defect, not a configuration.
- Status at drafting (MEASURED 2026-08-24): DR11 pages exist; no photo-z product is present.

### §2.2 Galaxy cuts — the eight predecessor Cut-6 predicates, restated from BS6-pred

`brick_primary = 1`; `maskbits = 0`; `type <> 'PSF'` (BS6-pred §3(b) disclosure carried);
`flux_r > 0`; photo-z join with `0 ≤ z_phot_median < 0.15` (predecessor product
`ls_dr10.photo_z`; the branch's product is receipted at BS-1b);
`POWER(shape_e1,2)+POWER(shape_e2,2) < 0.1836734693877551` (executable form, byte-identical
to BS6-pred; ⟺ b/a > 0.4, V3-pred I-5); `dered_mag_r < 17.7`; `shape_r > 1.5`. No
surface-brightness cut exists (documented absence, BS6-pred §3(a)).

### §2.3 Count oracle → order ledger → threshold → selection (acyclic, code-defined)

`build_plan()` performs the whole chain in one frozen call: **BS-2c** count oracle (complete
per-brick eligible counts left-joined onto an independently enumerated release brick-universe
manifest, zero rows materialized, validated by `validate_count_oracle()` which refuses on a
single missing or extra brick and on any grouped/ungrouped disagreement; counting is
server-side, row payloads are never fetched for counting; the query texts, endpoint and a
request/byte ceiling are pinned before the first query, and the `c_j` values are computed once
by `cos_theta()` and pinned as `'<f8'` bytes) → **BS-2o** threshold-free order ledger
(`greedy_ledger()`, positive-raw-count bricks only) → **BS-5p** planning power sets
`L_min_plan` and `L_plan = 1.2 × L_min_plan` → **BS-2s** selection (`local_pass()`).

**Raw versus retained, stated once and enforced in code:** raw counts drive the ledger and
the exact-mode boundary; **retained counts drive every threshold** — `L_ret`, the
`N_eq = 3·L_ret ≥ 100,000` floor, `L_plan`, and the reduction. Retention is the frozen
per-brick integer `floor(0.8572 × n)`.

**Selection claim discipline (Scope Amendment 1):** for candidate universes of ≤ 16
positive-count bricks the code's exact enumeration IS the algorithm, so minimum cardinality
holds by construction (all five adversarial gate counterexamples are fixtures and pass); at
production scale the result is exactly what the frozen procedure returns and **no minimality
or global-optimality claim attaches to it**. Contiguous-BRICKID selection remains banned.

### §2.4 Manifest closure — a frozen property, carried from the predecessor's own defect

**The property.** The selection defines the parent; **the parent's cutout geometry defines
the required brick set, INCLUDING neighbour bricks at the footprint edge**; the image
manifest may be frozen **only after that closure is computed**, and its count is recorded in
the receipt. A brick enumeration that closes over "bricks my objects sit in" is not closure.

**The check (BS-2m, class P, pre-freeze).** The planner is IMPLEMENTED in the reference code
(`plan_object_bricks`, footprint-edge neighbour rule included), and `close_manifest()` is the
single production entry point: it takes the frozen parent table plus its digest and **derives
every object's required bricks itself**. There is no argument through which a caller can hand
it an answer. It refuses on a parent-digest mismatch (an omitted or altered object changes the
digest), on any object planning zero bricks, and on a difference of even one brick in either
direction; it emits `parent_digest`, `planner_digest`, `plan_digest`, `required_count`,
`manifest_count` and the missing/extra bricknames into the receipt, so a future gate reads
numbers rather than an assurance.

**Round 6 then showed the seam had moved, not closed** — a caller could supply a shortened
parent *with a matching regenerated digest*, a shortened brick universe, or a zero cutout
half-size, and pass. That is the hash-chain lesson: a digest supplied alongside its own data
proves consistency, never custody. `close_manifest()` now binds to **external witnesses it
cannot regenerate**: the release brick universe must match the pinned digest `863e5ded…` and
the pinned cardinality 366,912; the parent digest must equal the one carried by the **BS-2s
selection receipt**; and the cutout half-size is a frozen constant derived from
`CUTOUT_PIX × CUTOUT_PIXSCALE_ARCSEC`, with no override parameter.

**Round 7 then found the planner itself was wrong, and this is the most important correction
in this document.** V8 shipped a *reimplemented* cutout planner. Run against the real
survey-bricks table it returned only the home brick for both historical objects —
reproducing the exact 60,308-vs-60,310 enumeration failure it existed to prevent — and its
fixtures passed only because they ran on a synthetic grid whose neighbour relationships this
author had constructed. Round 6's instruction to "pin and implement the cutout planner" was
read as *write a new one*; the frozen planner was already in the lane and correct.

**The reimplementation is RETIRED (it raises if called).** BS-2m binds to
`_objmanifest_20260820/build_object_manifest.py::plan_candidate_bricks` with its pinned
adapter, digest `1617af00eb73…` (the v9 pin; V10 quoted `36bbbf250215…`, which the frozen code no longer pins — KIMI F3). Verified against the real sidecar: object 10997315463551936
→ `['3385m885', '3471m885']`, object 10995116744378804 → `['2857m870', '2894m872',
'2902m870']`. The closure fixtures now run on the **real** brick table and the **real**
historical objects, and a manifest omitting those neighbours is refused **by name**:
`CLOSURE-FROZEN-PLANNER`, `CLOSURE-RETIRED-REFUSES`, `CLOSURE-CATCHES-HISTORICAL`,
`CLOSURE-CALLER-TRUST` (3/3 — self-consistent shortened parent, shortened universe, unpinned
universe digest).

### §2.5 Acquisition

Catalog row payloads are fetched only for the selected bricks, paced and receipted, under the
ceiling fixed at BS-2c. **Image bytes only after freeze**, only for the closed manifest, under
BS-6, three streams from the start, with the producer checksum list exclusively for source image transport at BS-6 cross-checked as the
predecessor's transport proved (60,308/60,308, zero problems).

### §2.6 The real geometry, measured (Branch B, DR10)

Run 2026-08-25 under Duho's catalog-only authorization; in the event **no fetch was needed**,
both inputs being already-acquired authorized artifacts. Receipt:
`real/REAL_GEOMETRY_RESULT_20260825.md`.

- Count oracle: universe **366,912** bricks, **270,577** with objects, **96,335** zero rows
  materialized, **832,393 / 832,393** objects placed, none outside the universe;
  count-weighted **Var(cosθ) = 0.445201**, independently reproducing the scope note's frozen
  0.4452.
- Selection **through the complete frozen reduction — removals AND the swap-then-removal
  phase** (round 8 found the swap phase missing; adding it leaves this result unchanged):
  **6,445 bricks**, **65,060 raw objects**,
  53,005 retained, **Var(cosθ) = 0.754664**, **N_eq = 120,002.9**. The
  declined run used 60,308 bricks / 208,407 objects / Var 0.0580 / N_eq 36,253 / 735.9 GB.
- **The images required are NOT the selected bricks: 12,117 bricks, ≈148 GB.** This line
  previously read "~76.8 GB of images", which was the selected 6,445 bricks priced as if they
  were the download. They are not. Each galaxy's cutout can require neighbouring bricks outside
  the selection, and the measured closure over the 65,060-object parent is **12,117 distinct
  bricks — 1.880× the selection** (`plan_digest aaeaa9f3…`, reproduced independently three
  times: by the closure itself, and twice by direct enumeration that never called it). At the
  predecessor's measured 12.2 MB/brick that is ≈147.8 GB, and Duho raised the planning ceiling
  to match on 2026-08-26.
- Stating it plainly because the draft got it wrong: **assuming the manifest equals the
  selection is the exact defect BS-2m exists to catch**, and it was sitting in this section's
  own summary line. The predecessor died of the same confusion at a smaller scale — a manifest
  of 60,308 against an analysis needing 60,310.
> **STAGE P REMAINS DUAL-VALUED, AND THIS TEXT CANNOT FIX IT (V12, KIMI/GPT56-V11 F4,
> CODEX-V11 4 — LEFT OPEN DELIBERATELY).** V11 declared in prose that this text promises the
> exact per-trial test. Three seats pointed out that the declaration does not bind: **§0 says
> the pinned code defines every mechanism and code beats prose**, and the pinned v9 code
> implements the shared-null route. So the document still has two operative definitions and a
> later operator could point at either. **No wording change closes this.** It closes one of two
> ways, and the choice is not mine: implement the exact per-trial test in the code §0 pins —
> with its own fixtures and its own gate — or amend §0's precedence rule. Until one of those
> happens this is an open blocker, stated here rather than papered over, and **BS-5p cannot be
> filled either way.**
>
> **WHICH STAGE-P TEST THIS TEXT PREFERS (V11, superseded in force by the paragraph above).** V10 named two: §4
> described the shared-null route with a 1% deflation and sampled own-null checks, while §2.6
> reported the exact per-trial route. A later operator could have pointed at either. **This text
> promises the EXACT per-trial test: every trial judged against its own 20,000-permutation null,
> no shared reference null in the counting path.** §4's shared-null contract is superseded and
> is retained below only as the description of what the currently pinned code does. That gap is
> the point: **BS-5p cannot be filled from the existing measurement receipt.** Filling it
> requires implementing the exact route in the code §0 pins, pinning its permutation count,
> plus-one rule, random addressing and serialization, adding fixtures, gating it, and re-running
> under those exact bytes. This is a design-and-implementation slot, not a value slot.

- **Stage P on the reduced set (SUPERSEDED / NON-APPLICABLE TO THE 49,211 MASK): 995/1000 against the x ≥ 962 rule** — measured
  2026-08-26 with **every trial judged against its own 20,000-permutation null**, so no shared
  reference null appears in the counting path
  (`real/stagep_exact.py`, receipt `real/STAGEP_EXACT_RECEIPT_20260826.json`, 431 s on 20
  workers). Geometry: the 6,445-brick reduced set, n = 53,005, Var(cosθ) = 0.754664,
  N_eq = 120,003.
  - **The earlier 997/1000 PASS is retracted**, not restated. It was measured on the
    PRE-reduction geometry and, decisively, before the conservatism check existed. That check,
    added in round 8, found the shared reference null was **not** conservative on this geometry:
    2 of 8 sampled trials had their own critical value above it (3.1672 and 3.1957 against
    3.1220) with a residual margin of only 1%.
  - What the exact re-run adds beyond the number: **zero trials disagree**. No trial was granted
    by the shared null and refused by its own, or the reverse. The round-8 finding stands as a
    finding and changed no verdict on this geometry, which means the earlier FAIL was a failure
    of the justification rather than of the result — a distinction that could only be settled by
    running it.
  - **Not yet in the definitional code.** `stagep_exact.py` is a measurement harness; the
    exact-null Stage P is not implemented in the file §0 pins. BS-5p is not fillable until it
    is, with its own fixtures and its own gate. 951 of the 1,000 own p-values sit at
    `5.00e-05`, the resolution floor of a 20,000-permutation estimate — lower bounds, 20× below
    the 1e-3 test, so the verdict is unaffected but they are not measured values.
- Disclosed: the pinned `greedy_ledger()` and `local_pass()` are O(n²) in Python and will not
  run at 270,577 bricks. The vectorized equivalents used at scale are proven identical to them
  on 40 (order) and 30 (reduction) random cases; making the frozen implementations scale is
  open work, not a claim.

BS-5p cannot be filled until Stage P is rerun on the actual post-exclusion mask.


## §2.7 Acceptance and exclusion — V11, repairing GPT56 F2 and CODEX 1

Two referees found the same hole independently, and CODEX called it the largest remaining
researcher degree of freedom because it is exercised **after** image inference exists and it
moves both the signs and the geometry. The text required "a measurement receipt for every parent
object" and never said which receipts become **accepted analysis rows**. A conforming operator
could produce all 65,060 receipts, mark an outcome-dependent subset accepted, drop the rest, and
proceed if what remained passed.

**The rule is fixed here, before any image byte.**

1. **Every parent object ends in exactly one terminal status.** The 65,060 object IDs of the
   pinned parent partition into `ACCEPTED` and `EXCLUDED` with no remainder and no duplicates.
   A parent-to-mask accounting identity is a receipt condition, not a convention:
   `|ACCEPTED| + |EXCLUDED| = 65,060`, every ID appearing exactly once.
2. **Exclusion reasons are enumerated here and nowhere else.** An object may be excluded pre-lock only
   for: (a) the cutout is missing or fails its byte-integrity check; (b) the cutout is
   incomplete at the frozen tensor shape; (c) catalogue quality. Instrument absence/non-finiteness and confidence threshold
   exclusions are deferred to post-unblinding handling. **Rule: BS-5f certifies only the locked pre-attrition BS-2f mask. Because any post-unblinding removal immediately terminates the run with `INCONCLUSIVE-BY-CALIBRATION`, there is no post-attrition Stage-C re-evaluation.** **No other reason is admissible.** A reason not on this list requires a new text.
3. **Every exclusion predicate must be sign-blind by construction.** None of (a)–(c) may read,
   derive from, or be conditioned on the handedness output, its sign, its amplitude, or the
   object's sky position relative to the tested axis. Where a predicate could see handedness it
   must be shown blind by construction, not asserted blind.
4. **The ledger is the producer, and every predicate is recomputed from evidence — not from
   the operator's label.** BS-2f is derived from an append-only ledger carrying, per object ID,
   one terminal status, one reason, and the **evidence that decides it**: the expected cutout
   checksum and tensor shape, and the actual checksum and shape. `run_production_verdict()` — or a
   mandatory pre-verdict validator it calls — must **recompute every predicate from that
   evidence and refuse any status, reason or evidence that disagrees.** The ledger binds to the
   parent digest and to per-object evidence digests, not merely to its own set digests.

   > **V12 CORRECTION (CODEX-V11 3 / GPT56-V11 F3).** V11 closed the *vocabulary* of exclusion
   > reasons and left the *truth* of a reason unbound. Recomputing "accepted = rows labelled
   > ACCEPTED" only replays an operator's labels: a conforming operator could mark an unwanted
   > object `EXCLUDED / confidence below threshold`, mark a wanted one `ACCEPTED`, and satisfy
   > the partition, the closed reason list and both set digests. "Machine-checkable" did not say
   > who checks it, from which pinned fields, or that a false reason is refused. It does now.

5. **The confidence quantity is defined, not merely thresholded.** Row P state (7) is the
   outcome-adjacent one, because confidence is an instrument output. The frozen definition must
   name the field or function that produces it, and the exclusion path must be shown — by
   construction, not assertion — unable to read handedness, its sign, its amplitude, or the
   object's position relative to the tested axis. An "absent output" may not be asserted: it is
   established by joining the ledger against the independently fixed attempt/receipt record.

6. **Acceptance design is its own class-P slot, and it closes before BS-6.** The numeric
   confidence threshold, retry and failure semantics, the evidence schema for reasons (a)–(b),
   the ledger schema, the recomputation code and its fixtures are a **DESIGN** slot
   (**BS-2a**), gated as text and code before any image byte. **BS-2f then becomes a value-only
   realised partition produced by that frozen code**, and BS-6 — the first image byte — depends
   on BS-2a being filled.
7. **The exclusion predicate (BS-2a) is DESIGN, defined, UNFILLED.** It uses three absolute, frozen thresholds measured by the DESI survey before this study existed:
   - `flux_ivar_r > 8.4000532`
   - `psfsize_r < 1.5699703`
   - `nobs_r >= 3`
   (Source `acquire/quality_selected.csv`, sha256 `61214b59d7b35a1e5004a39c6381d08b354ec1f7be6af6b60b23474d02ec28a3`; receipt `acquire/quality_cut_receipt.json`).
   
   These columns were measured by the DESI survey before this study existed. The predicate is **outcome-blind with respect to this study's unobserved χ**: its columns and absolute thresholds were fixed **without reading χ and before any image byte**, so it cannot be tuned post hoc. Whether the predicate is independent of handedness *conditional on position* — the property the dipole estimator actually needs — is **not established**. Either preregister a check for it, or record it as a **stated assumption with its risk**.
   
   These thresholds were fixed before any image byte, which makes the predicate preregistered rather than chosen. This defines a **distinct closed catalogue-quality exclusion reason** with authenticated evidence fields. It is NOT a redefinition of the parent catalogue. V9's `PINNED_PARENT_SHA256`, `PINNED_PARENT_ROWS = 65_060` and `PINNED_SELECTION_BRICKS = 6_445` are unchanged and must stay unchanged so no later reader mistakes this for a new sample.
   
   The frozen predicate is applied before BS-2f so the **P3 sealed mask genuinely holds 49,211 rows** while the **65,060-row parent identity stays unchanged**. Post-unblinding instrument-confidence handling is kept separate. A threshold chosen or moved after inference exists voids the run.

   **Outcome-blind is not the same as systematics-neutral, and this cut is not neutral.** Measured on the frozen `AXIS` with `successor_ref_v9.py`'s own `cos_theta()`: `corr(psfsize_r, cos θ)` is **+0.3659** in the 65,060-object parent, **+0.4188** in the 49,211 retained, and **+0.0964** in the 15,849 excluded. **The cut raised the seeing–position coupling in the sample that will actually be analysed**, by +0.0529; hemisphere contrast of the tested axis in the retained sample is 0.8104σ of `psfsize_r`. This is not an artefact of truncating `psfsize_r`: applying only the `flux_ivar_r` and `nobs_r` criteria, leaving `psfsize_r` entirely unrestricted, already gives **+0.4386** on 53,161 objects, and the population those two criteria remove sits at **+0.0589** on 11,899 objects with a *wider* `psfsize_r` spread than the parent (sd 0.2352 vs 0.1760) — so range restriction does not explain it. The depth and coverage criteria removed a population whose seeing was largely independent of position, and that population would have diluted precisely the systematic of concern. **This is why the sensitivity-gradient control is a prerequisite and not a refinement** (`gates/GAIN_GRADIENT_CONTROL_DESIGN_20260828.md`). **It is not a reason to revisit the cut.** The predicate is frozen; re-choosing thresholds on a systematics argument *after* measuring the systematic would be exactly the post-hoc selection the freeze exists to prevent. **This does not test conditional independence**, because handedness remains unread: a correlation between image quality and position says nothing about whether selection is independent of handedness *given* position. What it does show is that any violation of that assumption would project through a stronger seeing–position coupling in the retained mask than in the parent. That raises the **consequence** of a violation, not its likelihood, and it is why the sensitivity-gradient control is separately preregistered (`gates/GAIN_GRADIENT_CONTROL_DESIGN_20260828.md`) rather than why the predicate should change.

## §3 Statistics

Code-defined: `beta_slope()` (raw centred slope β̂; the full-sky constant `3·D̂` appears
nowhere); `perm_record()` (production Monte-Carlo permutation, **n_perm = 100,000**,
plus-one one-sided p at Longo's oriented sign, ties by exact float ≥, non-finite fails
closed, σ_β = `np.std(ddof=1)`); `perm_sigma_exact()` (the EXACT permutation sd,
`Var(β̂) = Var_pop(s)/((N−1)·Var_pop(c))`, verified against exhaustive enumeration by fixture
`PERM-SIGMA-EXACT`).

**Estimand.** A sign-symmetric classifier of accuracy a gives `E[s_obs|c] = (2a−1)·A_L·c`.
Scalar path: `Â_L = β̂/(2â−1)`. Profile path (frozen fallback, §6): `Â_L = β̂/ŵ` with `w_profile()` under **unit weight per accepted object**. The branch predicate (after BS-8f, before any real statistic, explicitly tied to `adjudicate_path()`) first checks the calibration floor: any `a_LB_b < 0.85` emits an immediate pre-unblinding `INCONCLUSIVE-BY-CALIBRATION` and halts. Only on the complement does the spread test apply: spread `<= 0.03` selects the scalar path, and spread failure only (`> 0.03`) selects the profile path. Profile is not a failure. 

**Uncertainties.** `sigma_ours_scalar(σ_β, β̂, a*, σ_a)` and
`sigma_ours_profile(σ_β, β̂, ŵ, w_gradient(), Cov_a)`, both fail-closed on non-finite or
degenerate input. **Cov_a is the FULL covariance matrix of {â_b} including the shared
synthetic-error term**, produced by `accuracy_from_handcheck()` — a mandatory BS-8f field,
not a supplied assumption. Decision bands evaluate at â / {â_b}; **the detection floor
evaluates at a_LB / {a_LB_b}** — each evaluation point is named where it is used.
`σ_comb = sqrt(σ_pub² + σ_ours(â)²)`, σ_pub = 0.011.

**Declared assumption (Testimony at freeze):** `Cov(β̂, â) = 0` and `Cov(β̂, {â_b}) = 0` —
the audit's agreement indicators versus permutation-null variability conditional on the mask.
Declared, not proven.

**Admissible input.** `SealedMask` and `FixtureMask` are **distinct, non-interchangeable
types**; production entry points call `require_sealed()` and refuse a fixture by type
regardless of its contents. A `SealedMask` requires the sealed calibration boundaries and
**recomputes bin labels from them** — a caller's disagreeing labels are refused, not trusted —
validates sign-vector length exactly, refuses any non-accepted row, sorts canonically by
(brickid, objid), and binds kind, schema, boundaries and acceptance flags into its digest, so
identical arrays under different provenance do not collide. Fixtures: `MASK-REFUSALS` (5/5:
fixture-to-production, bare vector, wrong sign length, disagreeing bins, non-accepted row) and
`MASK-KIND-IN-DIGEST`.

## §4 Power gate, two stages, with an equality contract

**Stage P (class P, BS-5p).** Injection is `inject_signs()` (two `rng.random()` calls per
object in canonical order; `Generator.binomial` is banned; accepts a scalar accuracy or a
per-bin vector). Planning objects are retained counts at brick centres. Floor a = 0.85.
Success = one-sided p < 0.001. **PASS rule: 1,000 trials, one-sided 95% Clopper–Pearson lower
bound ≥ 0.95, i.e. `x ≥ 962` successes** (the frozen integer; 961 fails).

**The power null, measured rather than assumed.** Running 1,000 × 100,000 full permutations
per prefix is not executable at production scale (a gate measured the nested kernel at ≈ 9
hours per prefix). Stage P therefore measures the **standardized permutation null once per
prefix** (`reference_null_z()`, 20,000 permutations) and judges all 1,000 trials against that
full empirical tail, with each trial's statistic **deflated by PWR_CONSERVATISM** so the
decision demands more evidence than the raw statistic provides.

A normal-tail approximation was tried first and **rejected on measurement**: across four
geometries the measured z\* ranged 3.0376–3.1355, bracketing the normal 3.0902, and on the
**polar geometry this design actually selects** the normal threshold came out
anti-conservative. A fixture-tuned inflation factor would have been fitting, not a contract.

Round 6 found that a measured null plus a fixed deflation is still **not conservative by
construction** — the same 1,000 skies could turn a FAIL into a PASS. The repair is not a
larger fudge factor. **Stage P now verifies itself**: every calibrated success landing within
10× of the decision threshold is re-tested against an independent full permutation run, and a
single unconfirmed success **fails the stage closed**. Far-from-boundary successes need no
confirmation, which is what keeps it affordable.

This is checked, and it bites: on a fixture sized to sit near 50% power the mechanism
**refuted 2 of 12 audited boundary successes (10 confirmed) and failed the stage closed** (`PWR-SELF-VERIFYING`),
while `PWR-CALIBRATED-ALONE-INSUFFICIENT` reproduces the round-6 finding directly (calibrated
decisions alone confirmed in only 21 of 22 cases). **Measured on the real REDUCED geometry (§2.6, SUPERSEDED / NON-APPLICABLE TO THE 49,211 MASK): 995/1000, with every
trial judged against its own null rather than a shared reference (2026-08-26). The earlier
997/1000 on the pre-reduction geometry is retracted. BS-5p cannot be filled until Stage P is rerun on the actual post-exclusion mask.** **Production decisions
never use this path**: the production runner always executes the full 100,000-permutation
record on the sealed mask.

**Pre-Stage-C Calibration Gate:** Before running Stage C, the measured calibration bound must be checked. If any bin's `a_LB_b < 0.85`, it emits an immediate pre-unblinding `INCONCLUSIVE-BY-CALIBRATION` and the run halts. Only if all bins satisfy `a_LB_b >= 0.85` may Stage C run.

**Stage C (class E, BS-5f; after inference, before unblinding).** The same frozen generator,
addresses and pass rule, run on the **sealed accepted-position mask** (BS-2f: brickid, objid,
position, acceptance flag, calibration-bin label — never a χ sign), with the measured a_LB
(scalar) or {a_LB_b} (profile) from BS-8f. 

**Post-exclusion population:**
The statistic is computed on the post-exclusion population, so that is the population §4 and BS-5f must describe.
- pre-exclusion N = 65,060 Var = 0.7561 N_eq = 147,578
- post-exclusion N = 49,211 Var = 0.7517 N_eq = 110,983 floor 100,000 — PASS

Quoting 147,578 would describe a population that will never be analysed — which is the exact defect that got the predecessor declined. The two-ended split moves as a fact about the sample and not a threshold failure: 48.0/52.0 → 40.8/59.2 because `psfsize_r` correlates with cos θ at +0.37. The gate is N_eq and it passes; this is a change in the sample's character that a reader is entitled to see.

FAIL → **INCONCLUSIVE-BY-POWER declared before unblinding; the run halts; no real-sky statistic is ever formed.** **BS-5f certifies only the locked pre-attrition BS-2f mask (N = 49,211, N_eq = 110,983). Because any post-unblinding removal immediately terminates the run with `INCONCLUSIVE-BY-CALIBRATION`, there is no post-attrition Stage-C reevaluation.**

## §5 Decision regions — computed, never read off a table

`run_production_verdict()` is the **only** production path to a verdict. It exposes **no
permutation injection, no permutation-count override, and no stage/trial/mask-kind override**;
it calls `require_environment()`, `require_authorization()`, `require_complete_sample()` and
`require_sealed()`. **Required but unimplemented guards:** the runner must require and verify the canonical BS-L artifact and the one-use unblinding receipt, verify the exact final-mask binding and post-unblinding ledger recomputation before forming any statistic, and refuse before forming any statistic if the adequacy tree emits an `INCONCLUSIVE` result. It derives
the N_eq floor from the mask's own geometry, and only then runs the full 100,000-permutation
record before the pure decision helper. Synthetic exploration lives in the separately named
`explore_verdict()`. (Both V6 gates monkeypatched every guard and still extracted a verdict
from the V6 code through a test seam; fixtures `PROD-NO-SEAMS`, `PROD-CALLS-GUARDS` and
`PROD-REFUSES` close that.) The canonical registry is explicitly split by cardinality. The **canonical study-run lifecycle outcome registry** emits exactly one outcome per **run**, not per function call. The producing phase or process for each category is named below:

- **Numeric verdicts (produced by the numeric decision helper):** **REPRODUCED-LONGO** (p < **0.001** AND Longo's sign AND |Â_L − 0.0408| ≤ 3·σ_comb AND Â_L ≥ the evaluated floor), **REJECTED-AT-LONGO-AMPLITUDE** (p > **0.05** AND (|Â_L| + 3·σ_ours(â)) < **0.0408**), **INCONCLUSIVE** (any other numeric outcome).
- **Pre-statistic inconclusive halts:** **INCONCLUSIVE-BY-POWER** (produced by Row J, and the production runner's `N_eq` and Stage-C power guards), **INCONCLUSIVE-BY-CALIBRATION** (produced by Row J pre-unblinding, pre-verdict validator post-unblinding removal, or aggregate non-finite/degenerate failures excluding Row-I's missing allocated outputs — validated by `validate_calibration_aggregates` before the < 0.85 comparison, emitting the authenticated aggregate outcome), and **INCONCLUSIVE-BY-MISSING-ALLOCATED-OUTPUT** (produced by Row I pre-BS-8f abort).
- **Accounting refusals (produced by Row P or the pre-verdict validator):** **INCONCLUSIVE-BY-MISSING-RECORD**, **INCONCLUSIVE-BY-DUPLICATE**, **INCONCLUSIVE-BY-ORPHAN**, **INCONCLUSIVE-BY-MALFORMED** (from Row P).
- **VOID:** triggered by forbidden acts, protocol/digest deviation, or permutation/statistic/protocol non-finite/degenerate failures. **This category is not yet executable.**

`run_production_verdict()` returns exactly: the numeric outcomes and its two `INCONCLUSIVE-BY-POWER` branches (Stage-C failure and `N_eq` floor). **Unresolved required implementation:** BS-L verification, authenticated one-use unblinding-receipt verification, exact final-mask binding verification, post-unblinding ledger recomputation, adequacy-tree `INCONCLUSIVE` refusal before any statistic, Row-I emission, the Row-J calibration guard, per-attempt emission, and `VOID` conversion.

**Per-attempt states (zero or more per run, never a run outcome):** The adequacy receipt records exactly one terminal state per attempt: **EXCLUDED-BY-ABSENCE**, **EXCLUDED-BY-NONFINITE**, **EXCLUDED-BY-CONFIDENCE**, or **ACCEPTED-FINITE**. Catalogue quality is carried only as an already-resolved pre-lock status that cannot constitute a P8 removal. Any `EXCLUDED-BY-*` state deterministically emits the single run-level `INCONCLUSIVE-BY-CALIBRATION` outcome.

**Verdict Path (Row P) Post-Unblinding Consequence:** Row P must execute an exact set-equality join against the pinned attempt-set identity governed by the BS-2a design digest, using `brickid` and `objid` as fixed join keys, and produce the canonical post-unblinding adequacy receipt. Precedence states are explicit: zero records, duplicate records, extra records, or malformed records trigger an unconditional refusal; absent, non-finite, and low-confidence measurements are dropped; all others are accepted-finite. Adequacy decisions follow an ordered tree: First, calibration applicability: any post-unblinding removal immediately emits `INCONCLUSIVE-BY-CALIBRATION` and **no Stage-C rerun is performed**. Second, Row P binds the already-verified pre-unblinding calibration PASS (`a_LB_b >= 0.85`), relying on the locked BS-5f and BS-L verification.

**Detection floor (V3-pred F-7):** `3.09 · σ_ours(a_LB)`, printed in the results table. No
Â_L below the evaluated floor is nameable REPRODUCED regardless of the band.

**Validation battery, carried from the lapsed build spec at its named boundaries** (V6's
version was weakened and both gates said so): A = 0 must never return REPRODUCED
(`BATTERY-A0`); A = −0.0408 must not return REPRODUCED (`BATTERY-SIGN`); **A = +0.0408 at a
powered N must return REPRODUCED-LONGO** (`BATTERY-POS`, measured Â_L = 0.04243, p = 2.2e-21);
and an under-powered geometry must yield INCONCLUSIVE-BY-POWER **derived from N_eq**, never
from a caller-supplied boolean (`BATTERY-NEQ`).

**Run guards, also carried from the lapsed spec:** `require_authorization()` refuses real
data without an authorization file pinned to a SHA-256 (that authorization does not exist and
must not be written yet). **Recorded limit (CODEX-V34-2), because this text must not claim more than
the guard does:** the runner takes both the authorization path and its SHA-256 **from its caller** and
checks only that they agree with each other. There is no authorization schema, signer, study
identity, permitted operation, run identity, or independently frozen expected digest, so **any
existing file presented alongside its own digest satisfies it** — demonstrated by executing the
pinned `successor_ref_v9.py` against a referee brief, which passed. **It is a file-integrity check,
not a test of authority, and nothing downstream may read it as one.** It is **not** a live path to an
unauthorised run: BS-6 and the first image byte are blocked by other means. A typed authenticated
authorization record is **deliberately not built here** (principal direction, 2026-08-29), and
`successor_ref_v9.py` remains frozen; `require_complete_sample()` refuses unless every parent object has
a measurement receipt — a partial run is not a smaller run, it is a different experiment.

## §6 Conduct

- **Disclosure.** Nothing derived from any real χ value — value, sign, summary, label, or count of signs — is published, spoken, or written outside the sealed stores defined in §6.1 before the primary lock, **with exactly one exception: the permitted aggregate surface defined in §6.1's scope paragraph, which leaves the sealed stores only as the BS-2f, BS-8f, and BS-5f receipts, on the paths the table names, and is the only pre-lock χ-derived export this text allows.** After unblinding, disclosure waits for BS-V (§7). The predecessor's §4/condition-2 breach is why this clause exists. What binds *access* is §6.1, and §6.1 is the normative object of this section.

### §6.1 The blinding covenant — one lifecycle table, and the table is normative

**Scope — what is χ-bearing.** A *χ-bearing object* is: any cutout produced for this run; any per-object instrument output — a χ value, sign, amplitude, confidence value, and every per-object execution measurement receipt, which carries those fields; any per-object hand-check label or per-object human–instrument agreement; any derivative of these that is not on the permitted aggregate surface below; and the predecessor's sealed archive of 208,405 χ measurements (§6.2) — outcome knowledge on overlapping sky, governed by §6.2's seal-state rule and enforceable mediation. The *permitted aggregate surface* — χ-derived but defined as not χ-bearing — is exactly: the BS-2f mask fields (brickid, objid, position, acceptance flag, calibration-bin label, boundaries, digests — never a χ sign), the BS-8f aggregate record (â, σ_a, a_LB, the per-bin {â_b, σ_ab, a_LB_b}, ε̂, and the full Cov_a — aggregates over the hand-check sample, never a per-object value), and the BS-5f Stage-C receipt (PASS/FAIL and the permitted Stage-C scalar output, never a per-object calibration label).

**Non-χ-bearing receipt and log classes — a closed list, defined by schema, and the list is exhaustive.** 
An artifact is non-χ-bearing only if it conforms to one of these authenticated schemas, none of which can carry a per-object outcome value or a digest of a payload containing one: 
(i) a slot receipt under the pinned `SLOT_SCHEMA` as conformed by this revision's code items — namely BS-1, BS-1b, BS-2a, BS-2v, BS-2c, BS-2k, BS-2m, BS-2o, BS-3, BS-4, BS-5p, BS-2s, BS-6, BS-7p, BS-8p, BS-9, BS-2f, BS-8f, BS-5f, and BS-L (BS-7f, the post-unblinding adequacy receipt, and BS-V are explicitly post-unblinding χ-bearing receipts and are removed from this list); 
(ii) the access log under its BS-2k event schema (timestamp, actor, table row, operation, object identity, success/refusal, refusal reason, running chain digest — identities and flags, never payload bytes); 
(iii) the producer checksum list (§2.5), exclusively for source images; 
(iv) fixtures and their transcripts, synthetic by construction; 
(v) the authenticated **acceptance-evidence projection** containing **only narrowly enumerated authenticated predicate bits** (e.g., `parent_attempt_present`, `byte_integrity_pass`, `canonical_shape_pass`), each mechanically recomputable by a separately pinned independent verifier. **All cutout digests stay inside the sealed boundary and are never exported.** No execution completion/non-finite status, no caller-authored status, and no free-form identifier may be exported. Every legal value is mechanically fixed. Attempt identity must be derived from a canonical source and serialization. Confidence is explicitly excluded from this projection and deferred to post-unblinding.

**Everything else is χ-bearing by default**: any artifact not on this list and not on the permitted surface; every per-object execution measurement receipt wherever it sits; the cutout-completion receipt; any opaque digest of χ-bearing bytes — a digest whose preimage's schema is not on this list or the permitted surface, the acceptance ledger's measurement digest among them, because such a digest is a verification oracle for a guessed outcome; the label-set receipt, which is χ-bearing and remains in the committee store; BS-7f, the post-unblinding adequacy receipt, and BS-V receipts; and any schema that permits outcome payloads. Doubt resolves toward χ-bearing.

**The sealed stores.** The *main sealed store* holds cutouts, instrument outputs, the cutout-completion receipt, and the acceptance ledger. The *committee sealed store* holds the hand-check labels and the label-set receipt. A third χ-bearing store — the predecessor archive — is governed by §6.2's seal-state rule and Row B's enforceable mediation. All three stores are provisioned at **BS-2k** (class-P DESIGN slot). Gates and referees are external witnesses: their inputs are the closed list of non-χ-bearing receipt classes and fixtures only, and no gate input is χ-bearing.

**The phase line.** P0 freeze → P1 BS-6, first image byte → P2 cutout production, pre-inference integrity projection, exact-parent C2 stage-completion, and instrument inference → P3 BS-2f → P4 BS-8f → P5 BS-5f → P6 BS-L, **the primary lock** → P7 unblinding → P8 BS-7f, post-unblinding adequacy receipt, and BS-V → P9 disclosure. 

**THE TABLE.** Each row is one permitted actor or process. Any pre-unblinding touch of a χ-bearing object by any person or process not in this table, or outside a row's stated surface, is forbidden by default.

| # | actor / process — identity | may touch (read → write) | when | authorized by (must exist first) | emits (receipt this act produces) | what voids the run |
|---|---|---|---|---|---|---|
| A | **Custody provisioner** | creates the two new stores' containers and brings the predecessor archive under the mediator; generates, splits and escrows the keys; generates Duho's signing keypair and binds its public half; installs the mediator (row B); records the predecessor archive's identity, its existing holder roster and its seal state by non-content metadata operation → writes the BS-2k design artifacts. **Never reads a χ value**. | P0 | — | BS-2k | any read of archive contents; any key share retained outside the escrow; any store, key or wrapper existing outside the receipt; failure to enforce mediation as a gate condition |
| B | **Store mediator / log writer** | the only path by which any row's stated read or write reaches **any of the three** sealed stores' bytes; conveys bytes strictly as the conduit of another row's stated surface → appends exactly one event per touch, success or refusal. **Row B must refuse and log any Row D touch until it verifies an authenticated C2 exact-parent stage-completion artifact.** | from BS-2k's completion through unblinding | BS-2k | the access-log chain; its running checkpoint receipted at BS-2f, the pre-unblinding lock checkpoint receipted at BS-L, and the final post-unblinding checkpoint | any byte delivered outside the requesting row's stated surface; any unlogged touch; a refusal left unlogged; allowing Row D before C2 completion |
| C | **Cutout producer** | reads release image bytes → writes cutouts into the main sealed store, via row B; never reads any sealed object | P1–P2, after BS-6 | BS-6 and BS-9 | **the χ-bearing cutout-completion receipt, appended to the main store** | any cutout or derivative outside the store; any human view of a cutout outside row G's interface |
| C2 | **Cutout integrity verifier** — `verify_cutout_integrity` symbol and digest to be pinned at BS-2a (**DESIGN, defined, UNFILLED**). A hermetic worker, capability allowlist, and blindness fixture are required. | reads **only** cutouts via row B and fixed parent lists. Computes and writes the separate authenticated **acceptance-evidence projection** exporting only authenticated predicate bits (`parent_attempt_present`, `byte_integrity_pass`, `canonical_shape_pass`), and an **exact-parent stage-completion artifact** closing the omission channel. Recomputes all cutout digests inside the sealed boundary; never exports them. | P2, after row C, before row D | BS-2a (design), the cutout-completion receipt | the acceptance-evidence projections, one per parent object, and the stage-completion artifact | executing the classifier; emitting any field outside the schema |
| D | **Instrument runner** | reads cutouts and the cutout-completion receipt (authenticating it against the pinned verifier) → writes per-object χ-bearing measurement receipts (χ, sign, amplitude, confidence) into the store only | P2, after row C2 | BS-3, BS-9, the cutout-completion receipt, and **the authenticated C2 exact-parent stage-completion artifact** | the per-object measurement receipts in the store | any χ-derived value emitted outside the store |
| E | **Acceptance-ledger recompute** | reads **only the separate authenticated acceptance-evidence projections** in the main store (predicate bits only), the fixed parent lists, and the authenticated catalogue-quality evidence fields (exact authenticated fields `flux_ivar_r`, `psfsize_r`, `nobs_r` from source digest `61214b59d7b35a1e5004a39c6381d08b354ec1f7be6af6b60b23474d02ec28a3`, joined one-to-one on keys `brickid`, `objid`, verified by the BS-2a pinned verifier, failing nonfatally as an ordinary exclusion) — and computes the structural §2.7(2) predicates and catalogue-quality exclusion from it, **excluding instrument absence/non-finiteness and instrument confidence, which remain dropped from the pre-lock structural exclusion**. Does not read the cutout-completion receipt. → atomically writes both the append-only evidence ledger and the realised partition, ensuring the **P3 sealed mask genuinely holds 49,211 rows**. | P2–P3, after complete inference | BS-2a (design), and exactly one verified acceptance-evidence projection per parent object | the realised-partition record (N = 49,211), bound by BS-2f | reading any field outside the evidence schema |
| F | **Calibration-bin sealing** | reads the accepted partition's positions and acceptance flags only (χ-free) on the genuinely 49,211-row mask → writes sealed boundaries, bin labels, and the hand-check allocation | P3, at BS-2f | BS-8p and the realised partition | the sealed boundary and allocation record | any χ-bearing input to bin construction |
| G | **Hand-check committee** | views χ-bearing cutouts **of the allocated sample only**, rendered through the sealed interface → each label leaves the member only through that same interface to row H | after BS-8p; complete before BS-8f | BS-8p, the sealed allocation, and the sample's cutouts existing | the member co-signatures carried by the label-set receipt | a member holding any other role; any label, tally, description or impression exported outside the interface; any view outside the allocated sample; any unlogged view |
| H | **Label-ingestion writer** | receives labels from row G through the interface → writes them, as one label set, into the committee sealed store, and writes the **χ-bearing label-set receipt** | with row G, completing before BS-8f | BS-8p | **the χ-bearing label-set receipt** | any write path outside the pinned interface; any intermediate persistence between entry and write; any field beyond the pinned label schema; exporting the receipt's digest |
| I | **Calibration computation** | reads the sealed label set, the corresponding instrument outputs, AND the **χ-bearing label-set receipt**, inside the stores. **Must fail the run before BS-8f if any allocated object lacks a usable finite instrument output.** (Cost: this failure evaluates a pre-lock instrument fact and aborts, leaking that at least one allocated object was missing/non-finite, which we accept as an unavoidable consequence of refusing the pre-lock supervisor.) → writes **only** the BS-8f aggregate fields | P4 | the completed label-set receipt in the store | BS-8f | any per-object label, sign or agreement leaving the stores; any field beyond the BS-8f schema; **failing to abort when an allocated output is missing/non-finite** |
| J | **Stage-C runner** | reads the sealed BS-2f mask (χ-free) and the BS-8f aggregates; injects synthetic signs only — **never reads a real χ**. **Before running Stage C, Row J evaluates the calibration accuracy lower bound `a_LB_b < 0.85` from the BS-8f aggregate (V15 lines 566–567). If `a_LB_b < 0.85`, it emits `INCONCLUSIVE-BY-CALIBRATION` and halts the run pre-unblinding. On PASS, Row J must then verify exactly `N_TRIALS = 1_000` and the frozen Stage-C implementation/protocol digest *before* running or issuing BS-5f.** BS-5f binds that calibration PASS and verification, and certifies **only** the locked pre-attrition BS-2f population and is **insufficient** for a changed final mask. (Post-unblinding attrition requires a separately named post-unblinding adequacy receipt under Row P.) **Any locked Stage-C FAIL emits `INCONCLUSIVE-BY-POWER` and halts the run, explicitly including (a) fewer than 962 of 1,000 passing trials (`../ref/successor_ref_v9.py` lines 77–78) and (b) the self-verification `refuted` or `nonconservative` fail-closed return at reference lines 1275–1277. The complementary PASS branches are the sole route to BS-5f → BS-L.** → writes the Stage-C receipt | P5, before BS-L | BS-2f and BS-8f | BS-5f | reading any real χ; continuing the run after a calibration or Stage-C FAIL; **any deviation from the pinned 1,000-trial protocol or the frozen Stage-C implementation** |
| K | **Key holders** | touch nothing before the lock; custody exists for the lock ceremony and later audit only — **holding a key is custody, never licence** | — | BS-2k | none | any **pre-unblinding** read by any holder |
| L | **Duho** | signs the freeze; designates holders at BS-2k; signs BS-L's canonical lock digest; creates the canonical opening authorization; opens the lock by signature | P0, P6, P7 | for the freeze: every class-P slot receipted and the gates passed; for BS-L: clause 3(a)'s preconditions | the freeze signature; the BS-L detached signature; the opening authorization | any **pre-unblinding** access to a χ-bearing object; opening the lock before a verified BS-L exists; signing anything but the canonical lock digest |
| M | **Hwao** | reads the closed list of non-χ-bearing receipt classes → writes the slot receipts §7 assigns | throughout | §7's producer-of-record assignments | the slots' receipts | any **pre-unblinding** access to a χ-bearing object |
| N | **The lock ceremony** | reads the digests BS-L binds → writes the BS-L artifact | P6, after BS-5f, before unblinding | clause 3(a)'s preconditions | BS-L | a BS-L artifact missing any schema field; a lock with no log; a signature over anything but the canonical body digest |
| O | **Unsealing service** | reconstructs key use for this ceremony only and decrypts both sealed stores into the declared post-unblinding working location. Requires and verifies the canonical opening authorization. | P7 only; runs exactly once | a passing `verify_lock()` and Duho's **canonical opening authorization** | the **unblinding receipt** | any invocation before a verified BS-L; any replay of the opening authorization; any decrypted byte outside the declared working location |
| P | **Verdict path** | **post-unblinding only**: reads the real χ vector via a **pinned post-unblinding exact-parent join** against the independently fixed attempt set governed by the BS-2a design digest, using `brickid` and `objid` as fixed join keys. **Silent inner-join loss is forbidden.** Row P assigns exactly one fixed consequence to every attempt in a closed set of states, applied in this precedence order: (1) zero records (emits `INCONCLUSIVE-BY-MISSING-RECORD`), (2) duplicate records — more than one measurement for a parent is unconditional refusal (`INCONCLUSIVE-BY-DUPLICATE`), (3) extra records (`INCONCLUSIVE-BY-ORPHAN`), (4) malformed records (`INCONCLUSIVE-BY-MALFORMED`), (5) absent measurement (dropped; `EXCLUDED-BY-ABSENCE`), (6) non-finite measurement (dropped; `EXCLUDED-BY-NONFINITE`), (7) low confidence (dropped; `EXCLUDED-BY-CONFIDENCE`), (8) accepted-finite. Catalogue quality is carried only as an already-resolved pre-lock status that cannot constitute a P8 removal. **No discretionary retry.** This exact set-equality closure produces the canonical **post-unblinding adequacy receipt**, binding the parent-set digest, old BS-2f mask digest, complete terminal-state partition, final-mask digest, calibration applicability, the already-verified pre-unblinding calibration PASS, locked Stage-C PASS, protocol digest, and verifier result. (The adequacy receipt must not branch on a Stage-C or calibration FAIL that BS-L excludes.) **Adequacy decisions follow an ordered tree:** First, calibration applicability: any post-unblinding removal immediately emits `INCONCLUSIVE-BY-CALIBRATION` and **no Stage-C rerun is performed**. Second, Row P binds the already-verified pre-unblinding calibration PASS (`a_LB_b >= 0.85`), relying on the locked BS-5f and BS-L verification rather than re-evaluating the threshold. These consequences are fixed before any real χ is read, citing §6.3 which voids any post-first-real-χ change to a decision threshold. | P8, after unblinding | the unblinding receipt and a verified BS-L | the **post-unblinding adequacy receipt**, then BS-7f, then BS-V | any execution before unblinding; any verdict produced outside this symbol; **silent inner-join loss; discretionary retry** |
| Q | **Archive seal-state checker** | reads archive metadata by non-content metadata operation | P3, P6 | BS-2k | the archive seal-state receipt | any read of archive contents |
| R | **Every other person and every other process** | nothing χ-bearing pre-unblinding; the default is forbidden | pre-unblinding | — | — | any pre-unblinding access |
| S | **Disclosure and Publication** | **post-unblinding only**: exports the result after the verdict receipt exists | P9 | BS-V | the published result | any export before BS-V |

**Clauses.**

1. **The ban is universal and binds access, not merely disclosure.** No person and no process may decrypt, query, render, summarise or inspect any χ-bearing object or derivative before unblinding, except within a table row's stated surface. The ban names no roles because it has none: it binds Duho, Hwao, every key holder, every committee member outside row G's surface, and every process alike.

2. **The exceptions are the table's rows, or they do not exist.** No process that touches a χ-bearing object may run before the lock unless a row names it. BS-2a is **DESIGN, defined, UNFILLED**, so processes requiring it (Rows C2, E) cannot run yet.

3. **The primary lock (BS-L) is executable and receiptable.**
   (a) *Class and preconditions.* BS-L is a **class-E** slot. Its preconditions are: the freeze is in force, and BS-5f's Stage-C receipt exists. BS-L certifies no set containing itself.
   (b) *The lock artifact — a detached signature over a canonical body.* BS-L's canonical body names exactly, in canonical order: the roster digest, the accepted-mask digest, the calibration-record digest, the Stage-C receipt digest, the decision-input digests, **the ordered manifest of every class-P slot receipt, gate reports, and Duho's freeze signature**, the **pre-unblinding lock checkpoint** together with the chain segment demonstrating it extends BS-2f's, the **archive seal-state receipt**, the environment record, and Duho's signer identity. The canonical body's digest is what Duho signs. The detached signature and the signer identity are carried in the outer artifact, outside the signed body.
   (c) *Sequence, producers and verification.* The sequence BS-5f → BS-L → unblinding → BS-7f → BS-V is recorded through named producers. The pinned verifier `verify_lock()` checks schema completeness, every digest binding, BS-5f's complementary calibration PASS and Stage-C PASS, the manifest of freeze completeness (verifying those bound bytes rather than re-resolving filenames), the lock checkpoint's extension of BS-2f, and the archive seal-state transition (Clause 7). **Failure refuses unblinding and refuses the verdict path.**
   (d) *The gate on the only verdict path.* The production runner must require a verified BS-L. **These mechanisms are run guards and digest serializations, which §0's enumeration assigns to the pinned code**. This §6 replacement and every Part 2 seam are **one atomic candidate revision**.
   (e) *Receipt authenticity.* Canonical receipts must carry and authenticate their decoded fields.

4. **Access is logged and mediated.** An append-only log covers all three sealed stores. Enforceable mediation is a **BS-2k gate condition**: no holder or run host may possess a raw-store read path outside the pinned mediator; the gate must identify and test that boundary, and inability to enforce it makes BS-2k unfillable. A **pre-unblinding lock checkpoint** is taken immediately before canonicalizing BS-L; the chain continues through issuance, opening, and unsealing to a **genuinely final post-unblinding checkpoint**, carried in the unblinding receipt.

5. **The void rule.** Any pre-unblinding touch of a χ-bearing object outside the table voids the run. Access inside a table row, within its stated surface, after its stated authorization exists and producing its stated emission, does not void it (e.g. BS-L issuance and opening).

6. **Opening authorization.** The canonical opening-authorization body and signature envelope binds exactly: the BS-L digest, both store identities, the declared post-unblinding destination, a unique one-use ceremony identifier, phase P7, Duho's signer identity (bound to the BS-2k public key), and the schema/version. Row O's pinned verifier authenticates those exact fields and atomically refuses an already-consumed ceremony identifier.

7. **Archive seal-state transition.** The canonical authenticated seal-state schema binds archive identity, seal identifier/version, holder-roster digest, checkpoint predecessor digest, and monotonic event/epoch data. The permitted transition relation from BS-2k → BS-2f → lock checkpoint is identity and intact-state equality. BS-2f compares against BS-2k; BS-L compares against BS-2f. `verify_lock()` refuses any nonconforming transition.

8. **What is checkable about the redesign's blindness.** The retrospective-custody question must be resolved before freeze, and **if it is unresolved at freeze time the run is refused.**

9. **Adversarial Fixtures (BS-2a gate):** The BS-2a gate must run adversarial producer fixtures against the C2 implementation that actively attempt to encode a synthetic sign through every writable and missingness channel. These fixtures must rerun the real producer under transformed cutouts and must fail.

10. **Branch termination.** Every branch of every row must terminate in one stated outcome, because a branch whose consequence depends on a judgement made later is not terminated. An unterminated branch is where the meaning gets chosen after the data is visible, which is the failure this preregistration exists to prevent. *`VOID` reverse reachability is unresolved; therefore clause 10 is not yet executable, and **BS-6 and the first image byte remain blocked** until a pinned producer or conversion handles **every enumerated void antecedent**.* Clause 10 phases and effects must treat catalogue-quality exclusion as occurring before BS-2f, separating it from post-unblinding instrument confidence handling.

### §6.2 The predecessor's sealed measurements

The declined study's 208,405 sealed χ measurements are archived. **No predecessor χ measurement enters this run's analysis.** The archive is retained as historical record; **no row in §6.1's table reads it.** Its governance is seal-state and enforceable mediation: BS-2k records the archive's identity, roster, and a receipted seal state via non-content metadata operation (Row A), and the archive is explicitly brought under Row B's mediator. Any attempted read of the archive's contents will be blocked by the mediator and logged, or, if the mediator is bypassed, **may leave no trace at all — an observational read need not append, delete, reorder or modify any record, so the chain can stay cryptographically valid while containing no evidence of it.** Detection is therefore NOT claimed. This is precisely why BS-2k must demonstrate **exclusive** mediation before freeze; if exclusive mediation cannot be established, BS-2k is unfillable and the archive cannot enter the run's custody claim. That seal state is re-receipted at BS-2f and at the pre-unblinding lock checkpoint (Row Q), subject to the transition equality rule in Clause 7. A broken seal state is a custody failure.

### §6.3 General conduct clauses

- **No strata in the estimator.** The centred slope needs no tertiles; the one-shot strata
  hazard is retired by design.
- **Calibration.** Bin-construction algorithm and the 3 × 9 joint allocation with V3-pred's
  nine HC strata are frozen in code (`calibration_bins()`, `assign_bins()`,
  `allocate_handcheck()` — proportional, largest remainder, explicit tie rule, and BOTH
  inherited floors enforced: ≥ 10 per non-empty joint cell **and ≥ 30 real labels per live
  inherited HC stratum** (V6 enforced only the first; a gate produced a formally-filled but
  invalid sample). Infeasible floors FAIL rather than shrink. `calibration_bins()` states and
  IMPLEMENTS one tie rule and refuses degenerate bins. Numeric boundaries are instantiated and
  sealed at **BS-2f** from positions and flags only. **BS-8f** reports â, σ_a, a_LB, per-bin
  â_b, σ_ab, a_LB_b, ε̂ and the full Cov_a via `accuracy_from_handcheck()`, which implements
  **the inherited HC-1H estimator** `a = (raw − ε)/(1 − 2ε)` with the shared-ε derivative
  propagated — so Cov_a's off-diagonal is a real shared-error term, not an additive constant.
  (V6 returned the raw agreement rate and both gates caught it.) **Admissibility (`adjudicate_path()`):**
  `max_b |â_b − â| ≤ 0.03` AND every `a_LB_b ≥ 0.85` → scalar path; spread failure only →
  profile path; any `a_LB_b < 0.85` → **INCONCLUSIVE-BY-CALIBRATION, pre-unblinding halt.**
  V3-pred's HC-1H measurement and validity rules (committee, sealed keys, HC-5, HC-6) are
  carried by quotation at freeze.
- **Void rule.** Any post-first-real-χ change to ANY binding rule, parameter, algorithm, slot
  schema, randomness/serialization contract, reference-code byte, or decision threshold in
  this preregistration voids the run; only the mechanical filling of predeclared class-E
  values by their frozen producers is exempt. Post-read amendments cannot cure a void.
- **One change per iteration** (external-practice adoption, 2026-08-25): every gated revision
  of this text changes one thing per finding. The coverage contract requires predecessor-only in-band mappings, plus an external pinned artifact for the current transition (or another non-self-referential design). Historical mappings are explicitly exempted: V1→V15 cite nothing. The V24→V25 mapping must cite only findings the delta demonstrably answers.
- **No claim stronger than its check.** Gate-state sentences never exceed the cited
  artifact's first line.
- **Custody.** Receipts with digests; deliverables sha-pinned at gate dispatch by the gate's
  own report (an external witness) and committed to git; self-referential hash chains are not
  custody; describe-vs-compute discipline throughout.
- **Blind double, honestly scoped** (gpt56-V5 F6 / codex-V5 F3): because §0 makes the code
  bodies normative, a second implementation cannot be required to reproduce body-defined bytes
  without reading them. Therefore: the second product is a **clean-room reimplementation from
  this constitution plus a published per-function normative specification** (op order stated),
  and it is gated against the reference on the fixture battery. Where the spec is insufficient
  to reproduce a digest, that is a **spec defect to be repaired**, not an agreement failure.
  Divergence in any integer, sequence, or verdict is a STOP recorded as a finding — never
  reconciled by editing either implementation toward the other.


### The fold record

**a. What was folded.** `SECTION6_DRAFT_AGY_R15.md`, sha256
`d2c388a451d076f880c879e888ee7901331adc62142245a285b8ff932d67f01a`, folded 2026-08-27.

**b. Under what authority, and against what referee state.** The fold was **instructed and initiated at 21:48 KST on 2026-08-27, before any verdict existed.** The referee round ran in parallel with the assembly.

**c. What the referees had established when the verdicts landed during the assembly (21:52:33 and 21:53:46 KST):**
- GPT56 returned **CLEAR** on R12 and again on R13, with no blocking finding.
- Both seats confirmed R14 **closes** the R13 asserted-versus-executable defect at document-contract
  level, by taking route (b): BS-5f's Stage-C schema unchanged, pinned `verify_lock()` required to
  resolve the BS-L-bound BS-8f bytes and independently recompute `all(a_LB_b >= 0.85)`. GPT56 ruled
  route (a) **not better**.
- **Clause 10 was audited in both directions — forward termination and reverse reachability — by
  GPT56 on R12 and R13, and CODEX's independent clause-10 audit on R13 concurred** that the partition
  is single-valued and correctly seated at P5, after BS-8f exists and before Stage C, BS-5f, BS-L and
  unblinding. This is the strongest evidence §6 carries.
- R15 changes **Part 2 only**; a mechanical diff confirms Part 1 is byte-identical to the R14 body
  both seats credited.

The final bytes of V16 were written **after** applying the GPT56 schema-inventory repair, not before the verdicts existed.

**d. The exception this fold carries — OPEN unless R15's verdicts close it.** Both R14 seats blocked
on one thing and only one: **Part 2 asserts it lists every conforming edit outside §6, and did not.**
**Part 2 is the fold instruction** — an incomplete list means §6 lands correct while the surrounding
document silently does not receive changes it needs: the section right, the draft around it wrong.
List each of the five named seams and mark it **OPEN** unless R15 demonstrably closes it:
1. **§7 count and DESIGN inventory** — V15 lines 595–600 said "One of twelve class-P slots is filled"
   and listed BS-2f, BS-5p, BS-8p, BS-9, against fourteen parsed class-P rows and BS-2f being
   value-only per V15 lines 341–342 and 624 *(CODEX)*.
2. **Canonical receipt and schema seams** behind Part 1's invocation of the pinned `SLOT_SCHEMA`
   *(CODEX)*.
3. **§5 guard seam** — V15 lines 429–434 requires only a mask-bound BS-5f before the verdict
   calculation *(CODEX)*.
4. **§2.5 producer-checksum narrowing** and the Clause 10 / §6.3 / §10 repair-trace implications
   *(CODEX)*.
5. **Exact pinned `SLOT_SCHEMA` entries and canonical receipt fields for BS-2a, BS-2k and BS-L**,
   confirmed absent from the pinned implementation by programmatic set comparison *(GPT56)*.

**e. Carried open, not closed by this fold.** Findings 1, 2, 2b and 3 remain **UNRESOLVED** pending
the DESIGN, defined, UNFILLED BS-2a slot. **BS-2a is DESIGN, defined, UNFILLED.** Rows C2 and E cannot run. **BS-6
and the first image byte remain blocked.** The `verify_lock()` calibration-PASS implementation is
required work and is **not implemented** — naming it was the repair; writing it was out of scope.

**f. Known design consequence, with the principal.** Any single post-unblinding removal emits
`INCONCLUSIVE-BY-CALIBRATION`. No attrition rate exists in the frozen record, so the probability is
unknown; what is established is that one removal suffices.


## §7 Binding slots (producer · inputs available at that time · schema · code symbol · blocks)

**Class P — freeze prerequisites**

> **VALUE slots versus DESIGN slots (V11).** Referees noted that calling every empty slot
> "filling" treats substantive design choices as clerical completion. A **VALUE** slot needs a
> measured number under a schema that is already frozen. A **DESIGN** slot still needs a rule or
> an implementation that can change the answer, and **filling one requires a new text revision
> and a fresh text gate, not a receipt insertion**. On today's count: **BS-2a, BS-2k, and the `BS-2v` VOID converter are DESIGN slots.** One of sixteen class-P slots is filled (BS-2m). There are 8 class-E slots. (These class counts are emitted from the table by `tools/prereg_counts.py` and are not to be hand-edited.)

| slot | producer | content | code symbol | blocks |
|---|---|---|---|---|
| BS-1 | Duho | release branch A/B + provenance; branch-invariance evidence | — | everything |
| BS-1b | Hwao | photo-z product paths, columns, join keys, predicate-5 provenance | — | BS-2c |
| BS-2a **DESIGN, CLASS P — UNFILLED** | Hwao | **acceptance design**: the absolute, frozen thresholds (flux_ivar_r > 8.4000532, psfsize_r < 1.5699703, nobs_r >= 3). Gated as text AND code **before any image byte**. **Quality-predicate component gated and pinned 2026-08-28:** `ref/bs2a_quality_gate.py` sha256 `dfbd63d146b472f194f74d01b313874f23c9a4264f26903b22837ae32aa18508` — the predicate, its authenticated evidence schema and its verifier, **CLEAR from GPT56 and CODEX at round 6**, both scoped "CLEAR for FREEZING the quality-predicate component; not a fill authorization". **Recorded limit, which does not transfer as the word "verified":** sound against forgery (neither seat could make it accept a receipt it should reject; one strict single-deletion sweep over the 26 unique checks, all 26 caught by a named control with zero crash-only credits and zero undetected; the 325-case pairwise sweep was **filter-derived from real control outputs, with six pairs literally source-mutated and re-executed** — GPT56 did not run all 325 at round 6, and the row must not read as 325 executed source deletions by both seats; all five frozen constants recomputed without importing the module) but **not hardened against arbitrary hostile input** — four crash sites were repaired across rounds 3–6 and GPT56 found a fifth outside the boundary at round 6. What bounds that: no builder-produced row reached a crash in the 65,060-row type/schema census, and every observed crash exited nonzero. **Consumers must gate on exit status:** a post-verification emit failure can print the true `MATCH` summary and *then* exit 1, so a consumer treating `MATCH` on stdout as success can be misled. **The slot stays UNFILLED:** `verify_cutout_integrity` (Row C2), the confidence threshold, retry and failure semantics, the ledger schema, and §6.3(9)'s adversarial producer fixtures under transformed cutouts are not built, and those fixtures need cutouts, which BS-6 blocks. | `run_production_verdict`, pre-verdict validator | BS-2f, BS-6 |
| BS-2k ⚠ **DESIGN** | Duho | **custody provisioner**: creates stores, escrows keys, installs mediator, records archive seal state | — | BS-6 |
| BS-2v ⚠ **DESIGN, CLASS P — UNRESOLVED** | Hwao | **`VOID` conversion**: handle every enumerated void antecedent. The normative registry in §7.1 must be **pinned by digest in the preregistration itself** (as a `registry_digest` field bound in the slot schema), and the gate must compare the converter's emitted IDs and the exercised fixture IDs **against that pinned digest's contents**, which the converter does not author and cannot alter. Missing, duplicate, extra, or non-`VOID` conversion for any ID fails the gate on mismatch. Because the registry cannot be pinned before the converter exists, this gate is marked **unresolved** — a third round of rewording will not make a self-comparison independent. | `VOID_converter` | BS-6 |
| BS-2c | Hwao + blind double | universe manifest, per-brick counts, zero rows, closure proofs, ceilings, pinned `c_j` bytes | `validate_count_oracle` | BS-2o |
| BS-2o | Hwao + blind double | full traversal order + per-prefix ledger | `greedy_ledger`, `ledger_digest` | BS-5p |
| BS-5p | Hwao | L_min_plan, L_plan, retained basis, x ≥ 962 rule, addresses | `stage_power`, `build_plan` | BS-2s |
| BS-2s | Hwao + blind double | selected set, L_ret, L_raw, N_eq, fixtures, Stage-P re-pass | `local_pass`, `build_plan` | BS-2m |
| BS-2m ✅ **FILLED 2026-08-26** | Hwao | **manifest closure**: required set from the frozen cutout planner, counts, refusal on any difference. Receipt: `gates/FREEZE_CLOSURE_V9_20260826.md` — mechanism frozen at v9 (`successor_ref_v9.py` `6a9abbbd…`, `closure_worker_v9.py` `28f8e1f9…`), 34/34 probes, referee `gates/CLOSURE_V9_KIMI.md` **CLEAR** (one seat; two seats refused by their provider). Derived closure: 65,060 objects → 6,445 selected → **12,117 required bricks**, `plan_digest aaeaa9f3…`, reproduced independently three times. Nine items carried open in the freeze record. | `close_manifest`, `closure_receipt` | manifest freeze |
| BS-3 | Hwao | instrument identity: weights `83008c1c…`, τ = 4.4006456017494235, antisymmetry identity | — | BS-9 |
| BS-3g **DESIGN, CLASS P — UNFILLED** | Hwao | **sensitivity-gradient control.** Added in V37 under principal authorisation of 2026-08-29 to carry the precondition §1 asserts but no dependency edge enforced. Binds the seven things §1 requires of it *before* BS-6: **statistic, sample, positional stratification, uncertainty, bound, acceptance rule, and failure consequence.** The threat it bounds is a nonzero global offset multiplied by a sky gradient in sensitivity — the one route the antisymmetry identity does **not** close (§1). **What exists:** the estimator and its verifier are built and CLEAR from both seats at gain v6 (`ref/gain_gradient_estimator.py` sha256 `e227029713396a92…`, `gates/verify_mu_gamma.py` sha256 `e33d9275d8078743…`), γ̂ = slope/intercept from a single GLS fit with the delta-method Jacobian, and the vector kernel is frozen in `ref/gain_gradient_kernel.py`. **Why the slot is nonetheless UNFILLED:** the control's completeness semantics are an open fork — whether the invariance rule holds the observed `p` fixed, freezes an executable joint counterfactual, or is withdrawn to a stated limitation — and that choice is with the principal (`OPEN_QUESTION_T_COMPLETENESS.md`). **γ̂ remains unmeasured**, and no measurement of it is authorised here. **This row creates a dependency edge; it does not fill a slot, license an image byte, or assert the control works.** | `gain_gradient_estimator`, `verify_mu_gamma` (both built, not bound) | BS-6 |
| BS-9 | Hwao + gpt seat | **input-path rebinding**: branch-specific single-band HDU/plane schema, production input function (code + hash + tensor layout), full R1–R5 rerun through it, gated replacement runner. `nm_acquire_cutouts.py` remains PROHIBITED (V3-pred lines 374–386); predecessor R1–R5 receipts are historical context, never evidence for this run's path | — | BS-6 |
| BS-4 | Hwao | synthetic absolute-sign anchor rerun under this text | `inject_signs`, `decide` | unblinding |
| BS-7p | Hwao | randomness/serialization declaration + frozen fixture battery + boundary p-values + environment | `receipt`, `run_fixtures` | BS-6 |
| BS-8p | Hwao | HC-1H rules by quotation + measurement plan + 3 × 9 allocation | `allocate_handcheck` | BS-8f |

**Class E — execution gates**

| slot | producer | content | blocks |
|---|---|---|---|
| BS-6 | Hwao | image transport approval: closed manifest sha, byte ceiling, producer checksum list | first image byte |
| BS-2f | Hwao | sealed accepted-position mask (N = 49,211) + sealed calibration boundaries — **value-only: the realised partition produced by BS-2a's frozen code, applying catalogue-quality exclusions** | Stage C |
| BS-8f | Hwao + hand-check committee | â, σ_a, a_LB, per-bin values, full Cov_a, integrity triggers | Stage C |
| BS-5f | Hwao | Stage-C confirmatory power receipt on the post-exclusion population (N = 49,211, N_eq = 110,983) | BS-L |
| BS-L | Duho signs | **pre-unblinding lock**: content per §6.1 clause 3(b) | unblinding |
| Unblinding receipt | Unsealing service | post-unblinding artifact: reconstructs key use, decrypts sealed stores into working location | verdict path |
| BS-7f | Hwao | production permutation record: β̂_obs, canonical 800,000-byte payload digest, p, environment | verdict |
| BS-V | Hwao | **verdict only — NOT the lock** (V15; the lock is BS-L, see §6.1(1)): `decide()` output, evaluated floor, path taken, mask digest | disclosure |

### §7.1 Canonical VOID Antecedent Registry

This registry enumerates the exact stable IDs, sources, phases, and failure effects for every `VOID` antecedent required by §5 and §6.

**What the checker proves, and what it does not.** `tools/void_registry.py` establishes that this registry is well-formed and **NAME-complete** against the §6.1 row table: every defined row is named by some antecedent ID (V05) and no antecedent names an undefined row (V06). It does **not** establish *semantic* coverage — that an antecedent naming a row actually covers that row's forbidden column. An antecedent could name row S and describe something else and the checker would still report row S covered. **Read "all rows covered" as name-coverage only**; it is not a verification of meaning, and nothing downstream may treat it as one.

**Three coverage gaps closed in V37, under principal authorisation of 2026-08-29** (recorded in `DECISIONS_FOR_DUHO.md` decision 1, option A). §5's prose voids on conditions the registry did not name: a **degenerate** (finite but collapsed) failure, distinct from a non-finite one; and a **digest** deviation, which the registry named only as a *protocol* deviation. Both are now separate antecedents rather than undeclared aliases, because an ambiguity in a registry about to be pinned by digest is itself the defect. §2.7's prose voids on a threshold **chosen or moved**; the ID covered *moved* only and now covers both.

**The §2.7 phase is settled from the authorship record, and the cell is unchanged at `Post-first-real-χ`.** The clause entered at V11 (commit `4d99d1d93`, 2026-08-27), authored by this lane to answer GPT56 F2 and CODEX 1. V11's own §2.7 preamble states what "inference" means: the acceptance freedom is *"the largest remaining researcher degree of freedom **because it is exercised after image inference exists** and it moves both the signs and the geometry."* **"Inference exists" is image inference having produced real output — the first real χ.** The document's ordering confirms real χ exists *before* unblinding, not after: §6.1 Row J *"never reads a real χ"* yet can halt the run **pre-unblinding**, and §6.2 forbids χ-derived disclosure *"before the primary lock"* — both presuppose real χ sitting in the sealed stores pre-lock. `Post-first-real-χ` is therefore **earlier and broader** than `Post-unblinding`, and is the instant the clause names. §6.3's void rule is anchored at the same instant, so the registry and §6.3 agree rather than compete.

**Recorded because it was checked and is not obvious:** an earlier reading proposed `Post-unblinding` on the argument that unblinding precedes the first real χ. **That is wrong** — it confused when χ is *read* (Row P, post-unblinding) with when χ *exists*. The record was consulted precisely because the phase is a question of authorship intent rather than policy, and it determined the answer. **One narrow window remains observed but not legislated here:** between the first image byte and the first real χ, a threshold change is outside this antecedent's phase, though §2.7(5) independently pins those thresholds *"before any image byte"*. Naming a new antecedent for that window would be new policy, not recovery, and is not done.

| Antecedent ID | Source | Phase | Failure Effect |
|---|---|---|---|
| `VOID-5-FORBIDDEN-ACT` | §5 | Any | VOID |
| `VOID-5-PROTOCOL-DEVIATION` | §5 | Any | VOID |
| `VOID-5-DIGEST-DEVIATION` | §5 | Any | VOID |
| `VOID-5-NONFINITE` | §5 | Post-unblinding | VOID |
| `VOID-5-DEGENERATE` | §5 | Post-unblinding | VOID |
| `VOID-2.7-THRESHOLD-CHOSEN-OR-MOVED` | §2.7 | Post-first-real-χ | VOID |
| `VOID-6.3-BINDING-CHANGE` | §6.3 | Post-first-real-χ | VOID |
| `VOID-6.1A-ARCHIVE-READ` | §6.1 Row A | Pre-unblinding | VOID |
| `VOID-6.1A-KEY-RETAINED` | §6.1 Row A | P0 | VOID |
| `VOID-6.1A-STORE-OUTSIDE` | §6.1 Row A | P0 | VOID |
| `VOID-6.1A-MEDIATION-FAIL` | §6.1 Row A | P0 | VOID |
| `VOID-6.1B-BYTE-OUTSIDE` | §6.1 Row B | Any | VOID |
| `VOID-6.1B-UNLOGGED-TOUCH` | §6.1 Row B | Any | VOID |
| `VOID-6.1B-UNLOGGED-REFUSAL` | §6.1 Row B | Any | VOID |
| `VOID-6.1B-D-BEFORE-C2` | §6.1 Row B | P2 | VOID |
| `VOID-6.1C-CUTOUT-OUTSIDE` | §6.1 Row C | P1–P2 | VOID |
| `VOID-6.1C-HUMAN-VIEW` | §6.1 Row C | P1–P2 | VOID |
| `VOID-6.1C2-CLASSIFIER` | §6.1 Row C2 | P2 | VOID |
| `VOID-6.1C2-FIELD-OUTSIDE` | §6.1 Row C2 | P2 | VOID |
| `VOID-6.1D-CHI-EMITTED` | §6.1 Row D | P2 | VOID |
| `VOID-6.1E-FIELD-OUTSIDE` | §6.1 Row E | P2–P3 | VOID |
| `VOID-6.1F-CHI-INPUT` | §6.1 Row F | P3 | VOID |
| `VOID-6.1G-OTHER-ROLE` | §6.1 Row G | After BS-8p | VOID |
| `VOID-6.1G-EXPORT-OUTSIDE` | §6.1 Row G | After BS-8p | VOID |
| `VOID-6.1G-VIEW-OUTSIDE` | §6.1 Row G | After BS-8p | VOID |
| `VOID-6.1G-UNLOGGED-VIEW` | §6.1 Row G | After BS-8p | VOID |
| `VOID-6.1H-WRITE-OUTSIDE` | §6.1 Row H | Before BS-8f | VOID |
| `VOID-6.1H-INTERMEDIATE-PERSISTENCE` | §6.1 Row H | Before BS-8f | VOID |
| `VOID-6.1H-FIELD-BEYOND` | §6.1 Row H | Before BS-8f | VOID |
| `VOID-6.1H-EXPORT-DIGEST` | §6.1 Row H | Before BS-8f | VOID |
| `VOID-6.1I-LEAVING-STORE` | §6.1 Row I | P4 | VOID |
| `VOID-6.1I-FIELD-BEYOND` | §6.1 Row I | P4 | VOID |
| `VOID-6.1I-FAIL-ABORT` | §6.1 Row I | P4 | VOID |
| `VOID-6.1J-READ-CHI` | §6.1 Row J | P5 | VOID |
| `VOID-6.1J-CONTINUE-FAIL` | §6.1 Row J | P5 | VOID |
| `VOID-6.1J-DEVIATION` | §6.1 Row J | P5 | VOID |
| `VOID-6.1K-PRE-UNBLINDING-READ` | §6.1 Row K | Pre-unblinding | VOID |
| `VOID-6.1L-PRE-UNBLINDING-ACCESS` | §6.1 Row L | Pre-unblinding | VOID |
| `VOID-6.1L-EARLY-OPEN` | §6.1 Row L | P7 | VOID |
| `VOID-6.1L-WRONG-SIGNATURE` | §6.1 Row L | P7 | VOID |
| `VOID-6.1M-PRE-UNBLINDING-ACCESS` | §6.1 Row M | Pre-unblinding | VOID |
| `VOID-6.1N-MISSING-FIELD` | §6.1 Row N | P6 | VOID |
| `VOID-6.1N-NO-LOG` | §6.1 Row N | P6 | VOID |
| `VOID-6.1N-WRONG-SIGNATURE` | §6.1 Row N | P6 | VOID |
| `VOID-6.1O-EARLY-INVOCATION` | §6.1 Row O | P7 | VOID |
| `VOID-6.1O-REPLAY` | §6.1 Row O | P7 | VOID |
| `VOID-6.1O-DECRYPT-OUTSIDE` | §6.1 Row O | P7 | VOID |
| `VOID-6.1P-EARLY-EXECUTION` | §6.1 Row P | P8 | VOID |
| `VOID-6.1P-VERDICT-OUTSIDE` | §6.1 Row P | P8 | VOID |
| `VOID-6.1P-SILENT-LOSS` | §6.1 Row P | P8 | VOID |
| `VOID-6.1P-RETRY` | §6.1 Row P | P8 | VOID |
| `VOID-6.1Q-READ-ARCHIVE` | §6.1 Row Q | P3, P6 | VOID |
| `VOID-6.1R-PRE-UNBLINDING-ACCESS` | §6.1 Row R | Pre-unblinding | VOID |
| `VOID-6.1S-EARLY-EXPORT` | §6.1 Row S | P9 | VOID |

## §8 Inherited defects this text is built to prevent (named, so its gate can confirm each fix)

1. **Manifest-versus-parent gap (found 2026-08-25).** The predecessor's 60,308-brick manifest
   was frozen from an enumeration that did not close over the parent's neighbour
   requirements. **ls_id 10997315463551936** (dec −88.59) requires brick **3471m885**; **ls_id
   10995116744378804** (dec −87.13) requires brick **2857m870**. Both bricks exist in the
   release and appear in the producer's r-band checksum list; neither was in the manifest; the
   parent needed **60,310**. The cutter held both objects WAITING — fail-closed, the system
   working — but nothing detected the shortfall until the chain stalled two objects short at
   the end. **Fixed by §2.4 + BS-2m**, whose fixtures replay this exact shape and report the
   two bricknames.
2. **Footprint-blind power.** A uniform-sphere power calculation certified a footprint it
   never inspected. **Fixed by §4**: accepted-sample geometry is a named input; Stage C
   accepts only the sealed mask.
3. **Full-sky normalisation constant.** `3·D̂` inflated by 42.76% on the real footprint.
   **Fixed by §3**: the centred slope needs no footprint constant, and `3·D̂` is banned.
4. **Attenuation-versus-target mismatch.** Comparing a raw, attenuated slope to the undiluted
   published amplitude could formally REJECT a true signal. **Fixed by §3** (β̂ / Â_L split).
5. **Unreachable significance threshold.** Plus-one Monte-Carlo p at 999 permutations can
   never fall below 0.001; the predecessor's validator passed on that impossibility.
   **Fixed by §3/§4** (n_perm = 100,000; resolution demonstrated on both sides).
6. **Silent axis divergence.** Two "blind-double" implementations used axes 3.72 arcmin apart.
   **Fixed by §1/§0** (one pinned unit vector, display-only coordinates).
7. **Count-based stopping rule on ordered brick IDs.** Guaranteed a geometric cap.
   **Fixed by §2.3** (leverage stopping rule; contiguous selection banned).
8. **Verdict by human reading.** No implementation of the decision regions existed.
   **Fixed by §5** (`decide()` is the only verdict producer).

## §9 Academic-gates fields (external-practice adoption, 2026-08-25)

Citations carry bibcode/DOI (§1) and are verified from source at freeze, not from memory.
Coordinate frame (ICRS) and the axis representation are named wherever coordinates appear.
Data releases are named with version and branch (§2.1). Every catalog query is archived
VERBATIM as a runnable script in its receipt — no natural-language or MCP output enters a
receipt unreconstructed. Seeds, permutation counts, and environment are pinned (§0, §3–§4).
Checksums: producer-supplied digests are cross-checked against our bytes (§2.5).

## §10 Gate plan and repair trace

The checker contract is as follows:
- transitions whose destination is **earlier than this draft** — checked **in-band**, against the §10 table itself, each row carrying its own result digest;
- the transition whose destination **is this draft** — the current transition, mapped and checked in `gates/FINDINGS_MAP.md`;
- transitions whose destination is **later than this draft** — **out of scope; a draft is not answerable for transitions that postdate it**;
- **V1→V15** — exempt by a named rule in the checker.

Each written row must carry its own result digest — not any digest found elsewhere.

| transition | predecessor sha256 (16) | result sha256 (16) | sections changed (+added/−removed) | §7 row counts | findings answered |
|---|---|---|---|---|---|
| V1 → V2 | `2a775bcb2d206ad0` | `8362166cc0329457` | §2 (+14/−16), §3 (+16/−12), §6 (+13/−12), §5 (+10/−7), (preamble) (+6/−5), §7 (+5/−5), §4 (+5/−4), §9 (+5/−3), §8 (+1/−1) | no row-count change | **— none cited —** |
| V2 → V3 | `8362166cc0329457` | `1c4788c5555a9f7e` | §2 (+30/−22), §3 (+21/−18), §6 (+24/−14), §7 (+19/−8), §4 (+18/−8), (preamble) (+13/−8), §1 (+14/−6), §9 (+10/−8), §5 (+9/−8), §8 (+6/−4) | class-P rows 0 → 8; class-E rows 0 → 4 | **— none cited —** |
| V3 → V4 | `1c4788c5555a9f7e` | `1ea8bb8d8e236049` | §2 (+58/−24), §3 (+33/−20), §6 (+23/−22), §4 (+22/−18), §7 (+16/−12), (preamble) (+13/−12), §9 (+17/−8), §8 (+6/−7), §1 (+5/−7), §5 (+6/−5) | class-P rows 8 → 10 | **— none cited —** |
| V4 → V5 | `1ea8bb8d8e236049` | `1c283bbf6dd7bd59` | §2 (+46/−62), §6 (+26/−27), §3 (+15/−34), §7 (+20/−24), §9 (+15/−17), (preamble) (+22/−9), §4 (+8/−21), §5 (+8/−11), §1 (+5/−12), §8 (+5/−5) | class-P rows 10 → 0; class-E rows 4 → 0 | **— none cited —** |
| V5 → V6 | `1c283bbf6dd7bd59` | `9f40dfb0c1f2d56b` | §6 (+33/−26), §2 (+2/−45), §7 (+25/−21), §3 (+25/−14), (preamble) (+12/−24), §4 (+24/−9), §8 (+26/−6), §5 (+22/−7), §1 (+18/−5), §9 (+8/−15), §10 (+23/−0), §2.1 (+19/−0), §2.3 (+19/−0), §0 (+15/−0), §2.4 (+15/−0), §2.2 (+6/−0), §2.5 (+6/−0) | class-P rows 0 → 12; class-E rows 0 → 6 | **— none cited —** |
| V6 → V7 | `9f40dfb0c1f2d56b` | `f15b0b4dad9d5c56` | §10 (+29/−20), §4 (+18/−9), §5 (+16/−6), §2.4 (+14/−7), §3 (+9/−5), §6 (+9/−3), §0 (+3/−3), (preamble) (+3/−2) | no row-count change | **— none cited —** |
| V7 → V8 | `f15b0b4dad9d5c56` | `faea9047682e9de6` | §10 (+20/−26), §2.6 (+21/−0), §4 (+14/−6), §2.4 (+10/−3), §0 (+3/−3), (preamble) (+2/−2), §2.5 (+1/−0) | no row-count change | **— none cited —** |
| V8 → V9 | `faea9047682e9de6` | `b97ba35c8d1eeb66` | §10 (+18/−19), §2.4 (+19/−4), §2.6 (+11/−8), §0 (+3/−3), (preamble) (+2/−2) | no row-count change | **— none cited —** |
| V9 → V10 | `b97ba35c8d1eeb66` | `d6703db149dca28c` | §2.6 (+37/−6), §10 (+23/−15), §0 (+22/−3), §4 (+3/−2), (preamble) (+2/−2), §7 (+1/−1) | no row-count change | **— none cited —** |
| V10 → V11 | `d6703db149dca28c` | `bcab646794c6eca9` | §2.7 (+34/−0), §6.1 (+32/−0), §2.6 (+13/−1), §2.1 (+10/−0), (preamble) (+8/−1), §6.2 (+8/−0), §7 (+7/−0), §2.4 (+1/−1), §4 (+1/−1), §6 (+1/−0) | no row-count change | **— none cited —** |
| V11 → V12 | `bcab646794c6eca9` | `7633bc7a6b49da82` | §2.7 (+29/−5), (preamble) (+12/−3), §2.6 (+12/−1), §6.1 (+11/−2), §7 (+2/−1) | class-E rows 6 → 7 | **— none cited —** |
| V12 → V13 | `7633bc7a6b49da82` | `80adc0210973617b` | §6.1 (+19/−8), (preamble) (+9/−2), §2.7 (+2/−2), §7 (+2/−1) | class-P rows 12 → 14; class-E rows 7 → 6 | **— none cited —** |
| V13 → V14 | `80adc0210973617b` | `0b25608836b58997` | §6.1 (+36/−11), §2.7 (+3/−3) | no row-count change | **— none cited —** |
| V14 → V15 | `0b25608836b58997` | `efb27c619c063f8f` | §7 (+1/−1), §10 (+1/−1) | no row-count change | **— none cited —** |
| V15 → V16 | `efb27c619c063f8f` | `1b9b9486736bf734` | §6.1 (+62/−70), §6.2 (+4/−45), The fold record (+48/−0), (preamble) (+30/−1), §2.7 (+7/−9), §6.3 (+11/−0), §7 (+6/−5), §11 (+9/−0), §5 (+3/−1), §6 (+1/−3), §10 (+3/−0), §2.5 (+1/−1) | class-E rows 6 → 8 | FOLD — §6 replaced from SECTION6_DRAFT_AGY_R15 (d2c388a4) on principal's instruction 21:48 |
| V16 → V17 | `1b9b9486736bf734` | `1a0a259a91f5a73a` | §6.3 (+38/−7), (preamble) (+8/−6), §5 (+6/−6), §4 (+3/−1), §2.7 (+1/−2), §3 (+1/−2), §2.6 (+1/−1), §6.1 (+1/−1), §7 (+1/−1) | no row-count change | GPT56-V16-1, GPT56-V16-2, GPT56-V16-3, GPT56-V16-4, CODEX-V16-1, CODEX-V16-2, CODEX-V16-3 |
| V17 → V18 | `1a0a259a91f5a73a` | `ce144dc23ba8605d` | §10 (+21/−1), §5 (+4/−4), The fold record (+4/−4), (preamble) (+3/−3), §2.7 (+2/−2), §3 (+1/−1) | no row-count change | GPT56-V17-1, GPT56-V17-2, GPT56-V17-3, CODEX-V17-1, CODEX-V17-2, CODEX-V17-3, CODEX-V17-4 |
| V18 → V19 | `ce144dc23ba8605d` | `b7deb106eb81b3e1` | §5 (+7/−5), §10 (+9/−3), (preamble) (+3/−3) | no row-count change | GPT56-V18-1, CODEX-V18-1, CODEX-V18-2 |
| V19 → V20 | `b7deb106eb81b3e1` | `607df3dd5b022a29` | §10 (+11/−1), (preamble) (+3/−3), §5 (+3/−3), §11 (+2/−0) | no row-count change | GPT56-V19-1, CODEX-V19-1 |
| V20 → V21 | `607df3dd5b022a29` | `8386d5f0b3cdc8ed` | §10 (+9/−1), (preamble) (+4/−3), §5 (+2/−2), §6.1 (+1/−1), §7 (+1/−0), §11 (+1/−0) | class-P rows 14 → 15 | GPT56-V20-1, GPT56-V20-2, GPT56-V20-3, CODEX-V20-1, CODEX-V20-2 |
| V21 → V22 | `8386d5f0b3cdc8ed` | `9b09416685e966cc` | §10 (+9/−1), (preamble) (+3/−3), §7 (+2/−2), §11 (+2/−1), §5 (+1/−1) | no row-count change | GPT56-V21-1, GPT56-V21-2, GPT56-V21-3, CODEX-V21-1, CODEX-V21-2, CODEX-V21-3, CODEX-V21-4 |
| V22 → V23 | `9b09416685e966cc` | `134433199c85ea45` | §7.1 (+59/−0), §10 (+11/−3), (preamble) (+3/−3), §7 (+2/−1), §6.1 (+1/−1) | no row-count change | CODEX-V22-1 (class-E count 8 not 7), CODEX-V22-2, CODEX-V22-3, CODEX-V22-4, GPT56-V22-1, GPT56-V22-2, GPT56-V22-3 |
| V23 → V24 | `134433199c85ea45` | `6d722dc51316a2db` | §10 (+26/−87), (preamble) (+3/−3), §7 (+2/−2), §11 (+1/−1) | no row-count change | CODEX-V23-1, CODEX-V23-2, CODEX-V23-3, GPT56-V23-1, GPT56-V23-2, GPT56-V23-3, plus BLANC-20260828 (compute the counts and the trace) |
| V24 → V25 | `6d722dc51316a2db` | `50f2e53256cc7970` | §10 (+27/−26), §2.7 (+11/−4), §4 (+10/−2), (preamble) (+3/−5), §6.1 (+2/−2), §7 (+2/−2) | no row-count change | BS2A-ADOPTION-20260828 (quality-cut exclusion predicate; principal's instruction), GPT56-V24-1, GPT56-V24-2, CODEX-V24-4, CODEX-V24-5, CODEX-V24-6 |
| V25 → V26 | `50f2e53256cc7970` | `2eec8da41ee69374` | §6.1 (+6/−6), (preamble) (+4/−4), §2.7 (+4/−4), §7 (+2/−2), §6.3 (+1/−2), §5 (+1/−1), The fold record (+1/−1), §11 (+1/−1) | no row-count change | GPT56-V25-1, GPT56-V25-2, CODEX-V25-1, CODEX-V25-2, CODEX-V25-3, CODEX-V25-4 |
| V26 → V27 | `2eec8da41ee69374` | `e801a18bb7c489f0` | (preamble) (+4/−4), §2.6 (+2/−2), §2.7 (+2/−2), §4 (+2/−2), §6.1 (+2/−2), §5 (+1/−1), §10 (+2/−0), §7.1 (+0/−1) | no row-count change | GPT56-V26-1, GPT56-V26-2, GPT56-V26-3, CODEX-V26-1, CODEX-V26-2, CODEX-V26-4 |
| V27 → V28 | `e801a18bb7c489f0` | `82cd8ac3690fb87b` | §10 (+19/−12), (preamble) (+1/−1) | no row-count change | GPT56-V27-1, GPT56-V27-2, GPT56-V27-3, CODEX-V27-1 |
| V28 → V29 | `82cd8ac3690fb87b` | `542ee7d93dec457a` | §10 (+5/−3), (preamble) (+1/−1) | no row-count change | CODEX-V28-1 (current-transition scope rule) |
| V29 → V30 | `542ee7d93dec457a` | `e81becce1b19d88a` | §1 (+6/−0), (preamble) (+1/−1) | no row-count change | PRINCIPAL-20260828-LAND-NULL (human direction: "add the land 2008 null to the prereg motivation"; no referee finding — the change answers an instruction, and inventing a finding ID for it would be a lie) |
| V30 → V31 | `e81becce1b19d88a` | `ce1b6914eae0d36b` | §1 (+2/−2), (preamble) (+1/−1), §10 (+2/−0) | no row-count change | GPT56-V30-1, GPT56-V30-2, GPT56-V30-3, CODEX-V30-1, CODEX-V30-2 |
| V31 → V32 | `ce1b6914eae0d36b` | `02a922167bcb7708` | (preamble) (+1/−1), §1 (+1/−1), §2.7 (+2/−0), §10 (+1/−0) | no row-count change | GPT56-V31-1, CODEX-V31-1, plus PRINCIPAL-20260828-COUPLING (human direction: "the cut raised the coupling — flag it in §2.7"; measured figures, not a referee finding) |
| V32 → V33 | `02a922167bcb7708` | `b247f40281df3c23` | (preamble) (+1/−1), §2.7 (+1/−1), §10 (+1/−0) | no row-count change | GPT56-V32-6, CODEX-V32-5 (§2.7 conditional-independence overreach). The five gain-control findings — GPT56-V32-1..5, CODEX-V32-1..4 — were repaired in gates/GAIN_GRADIENT_CONTROL_DESIGN_20260828.md, which is a sidecar and not part of this document's bytes. |
| V33 → V34 | `b247f40281df3c23` | `1c45d32d5f360ab4` | (preamble) (+1/−1), §7 (+1/−1), §10 (+1/−0) | no row-count change | BS2A-R6-CLEAR-20260828 (the quality-predicate component cleared its code gate at round 6 from both seats and is pinned by digest in the BS-2a row, with its recorded robustness limit; the slot remains DESIGN, UNFILLED and no class count moves) |
| V36 → V37 | `e4d7b175ac270f4c` | `62dd8a7525c39912` | §1 (+1/−1), §5 (+0/−0), §7 (+1/−0), §7.1 (+6/−1), §10 (+1/−0) | **15/8 → 16/8** (BS-3g added) | PRINCIPAL-20260829-VOID-OPTION-A, PRINCIPAL-20260829-BS6-OPTION-A (on GPT56-V34-1 and the three §7.1 coverage gaps) |
| V35 → V36 | `b80d50afe076fe8d` | `e4d7b175ac270f4c` | (preamble) (+1/−1), §7 (+1/−1), §10 (+1/−0) | no row-count change | GPT56-V35-1, CODEX-V35-1 (§7 line 698: the doubled 26-probe phrase and the missing process-exit qualification) |
| V34 → V35 | `1c45d32d5f360ab4` | `b80d50afe076fe8d` | (preamble) (+1/−1), §1 (+1/−1), §6.2 (+1/−1), §7 (+1/−1), §10 (+1/−0) | no row-count change | GPT56-V34-2, CODEX-V34-3 (the antisymmetry identity does not forbid a biased w creating a signal), CODEX-V34-1 (an unlogged archive read need not break the chain), CODEX-V34-4 (the BS-2a pin overstated the pairwise probe evidence) |

*Byte-level columns generated by `tools/prereg_trace.py` — digests by sha256, sections and line counts by diff, row counts by parsing the §7 table. The **findings answered** column is human-supplied from `gates/FINDINGS_MAP.md` and is NOT generated: which finding a change answers is a judgement, and the tool refuses to make it. The tool does enforce it — a transition that changes a normative section while citing no finding is a failure, which is how §6.3's finding→change obligation is checked rather than asserted.*

*A draft cannot describe the transition that created it: the row for V(n−1) → V(n) would change V(n)'s bytes and therefore its own digest. Each draft's table covers transitions up to its predecessor; the transition that produced it appears in the next draft. This is a property of self-reference, not an omission.*

Next: both referee seats on this text, the corrected code, and the real-geometry receipt.
**Undecided and untouched:** the methods-note question and the strata question.

## §11 Code-side inventory for the next atomic revision

- **`SLOT_SCHEMA` entries (Row A, Row N):** Add one explicit code-side item requiring exact pinned `SLOT_SCHEMA` entries and canonical receipt fields for **BS-L and BS-2k**. Name the **BS-2a** schema addition as required work deferred with the DESIGN, defined, UNFILLED BS-2a design. Bind those schema bytes into the implementation/schema digest item. A general `SLOT_SCHEMA` update to capture access-log checkpoints and archive seal-state digests for BS-2f/BS-L. **Do not change BS-5f** (route b stands).
- **`verify_lock()` enforcement (route b):** Require the pinned `verify_lock()` to resolve the BS-L-bound BS-8f bytes and independently recompute `all(a_LB_b >= 0.85)`. Pin the implementation/schema digest for this route. Add a negative fixture demonstrating that a low-bound BS-8f cannot produce a passing lock.
- **Row-J calibration guard:** Implement the guard to emit `INCONCLUSIVE-BY-CALIBRATION` and halt pre-unblinding if `a_LB_b < 0.85`.
- **Row B access mediation:** Implement Row B's hard block on Row D prior to C2's exact-parent stage-completion receipt verification. Implement the enforceable-mediation gate checks.
- **Row C2 and Integrity:** Implement the hermetic worker profile allowlist and adversarial producer fixtures for C2. Implement `recompute_acceptance_ledger` to compute statuses and reasons from the evidence projections, atomically writing the evidence ledger and realised partition.
- **Unblinding-receipt schema:** Require the **canonical unblinding-receipt schema and its exact authenticated fields**, including at minimum: the **BS-L identity and checkpoint**; the **complete extending chain segment**; the **terminal unsealing events**; the **final post-unblinding checkpoint**; the **declared destination**; the **one-use ceremony identity and replay state**. Bind those schema bytes into the **pinned implementation/schema digest** §11 already requires, and state that **`verify_unblinding_receipt()` must authenticate exactly those fields**. Implementation is **UNRESOLVED** until delivered.
- **Verifiers (Row O, Q):** Implement `verify_unblinding_receipt`, `verify_archive_seal`, and the opening-authorization / replay verifier.

- **Aggregate validation:** Implement `validate_calibration_aggregates` to validate calibration aggregates as finite and non-degenerate (excluding the Row-I missing-output case) before the `< 0.85` comparison, and emit the authenticated outcome. Add its fixture.
- **Post-unblinding adequacy validator:** Implement a named validator that authenticates the adequacy receipt, independently recomputes the exact-parent terminal partition and final-mask digest from pinned evidence, checks exact binding to the mask passed to the runner, and refuses before `perm_record()` on every non-passing adequacy branch. Add positive and negative fixtures, including an `INCONCLUSIVE` receipt that proves no statistic call occurs.
- **`VOID` conversion:** Implement a converter (`BS-2v`) that handles every enumerated void antecedent. It must define a canonical closed antecedent registry with stable IDs and exact source/phase/failure-effect for each `VOID` branch. The receipt must conform to a **canonical authenticated receipt schema**, including: registry digest, converter implementation digest, ordered normative IDs, exercised IDs, uniqueness and count closure, per-ID source/phase/failure-effect, and result classification (all authenticated). The gate must compare the converter's emitted IDs and the exercised fixture IDs against the pinned §7.1 digest's contents. Missing, duplicate, extra, or non-`VOID` conversion for any ID fails the gate. This is a pre-BS-6 dependency.
