# PREREGISTRATION DRAFT V85 — LONGO-AMPLITUDE TEST ON A LEVERAGE-CHOSEN FOOTPRINT

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
> **Carried-open items:** **BS-2v coverage still not independent of the converter**; **BS-2v still has no authenticated receipt schema a gate could reject against**; ~~**§6.1 Row L's signing path voids itself** (CODEX-V24-1)~~ — **CLOSED at V52** by principal ruling: the wrong-signature condition now exempts the freeze signature and the canonical opening authorization, the two acts the row itself mandates that it caught. Carried open for 25 drafts; **the repair makes the path executable, not verified** (CODEX-V52 F5 flagged this line as stale). **preamble lines contradicting the live unresolved status** (GPT56-V24-5).
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
(`DECISION_MEMO_DECLINE_TO_PROCEED_20260821.md`, EFFECTIVE, **current sha
`76cc25e5350a92d00d13eff2421ad392aec5ff2140d3b259763dd713ef352092`**; **the memo was amended by append after signing — commit `b202645cd` signed it at sha `b4a1f1fcaa9acbaa6b9efd3ebbe9496be8c1d83c690a012dc7a4f8520840374f`, and commit `ac603e4c2` corrected the signing time to 11:20:16 KST as authoritative, producing the current bytes. Earlier drafts pinned the pre-amendment digest, so the citation no longer matched the file at that path — GPT56-V49 F7. Both digests are recorded here because a signed decision memo that changed after signature must show the change, not just the latest state.**); its verified
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
is selected at BS-1 and recorded there. **For Branch B — the pinned branch — nothing else in this
document changes.** **For Branch A the opposite holds, and the earlier unqualified sentence contradicted §2.1's own text four lines later (GPT56-V49 F6):** Branch A voids the current §0 pin, carries over none of the DR10 universe, count-table, selection, parent or closure pins, and requires re-measuring all of them. The V11 commit that introduced this clause says so directly — Branch A *"is a new preregistration in everything but name"* — so the qualification is recovered from the record rather than chosen here.

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
> **STAGE P REMAINS DUAL-VALUED, AND THIS TEXT CANNOT FIX IT (V12, GPT56-V11 F4 and CODEX-V11 4 — **two seats, not three**;
> **KIMI is removed: its V11 F13 states the promise is *"now single-valued — the exact per-trial test"*, the opposite of this claim, and its F7 is a disclosure finding about the receipt's v7 subject. V42 corrected an earlier miscitation of KIMI F4 by substituting F7, which does not support it either — GPT56-V54 F4** — LEFT OPEN DELIBERATELY).** V11 declared in prose that this text promises the
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
- **Pre-statistic inconclusive halts:** **INCONCLUSIVE-BY-POWER** (produced by Row J, and the production runner's `N_eq` and Stage-C power guards), **INCONCLUSIVE-BY-CALIBRATION** (produced by Row J pre-unblinding, pre-verdict validator post-unblinding removal, or aggregate non-finite/degenerate failures excluding Row-I's missing allocated outputs — validated by `validate_calibration_aggregates` before the < 0.85 comparison, emitting the authenticated aggregate outcome), **INCONCLUSIVE-BY-MISSING-ALLOCATED-OUTPUT** (produced by Row I pre-BS-8f abort).
- **`INCONCLUSIVE-BY-NUMERICAL-FAILURE` — the class rule (principal ruling, 2026-08-29, option B).**
  **Stated as a condition, not a list of sites, because the sites are not all known.**
  **CONDITION.** Any computation performed by the pinned reference that (i) can fail when every argument satisfies that function's calling contract and the inputs are admissible, and (ii) whose failure is not already claimed by a more specific named outcome, **terminates the run in `INCONCLUSIVE-BY-NUMERICAL-FAILURE`.** This holds **at every phase** — pre-unblinding and post-unblinding alike. It is not a route for one row and not a route for one stage.
  **THE OVERLAP IS REAL, AND THIS SECTION WAS RULED ON TWICE, DIFFERENTLY — both rulings stand and the ground for each is recorded, exactly as for the catch-all reversal (principal ruling, 2026-08-30 10:46, option (c), superseding the make-them-disjoint ruling of 2026-08-29).** The 2026-08-29 ruling ordered the clauses made disjoint after precedence failed twice; **three partition constructions then died in three consecutive rounds, each on a REAL object that is computed by the run AND THEN sealed and verified — BS-2f, BS-8f, BS-5f — and three failures on genuinely dual-natured objects is what a genuine overlap looks like, which is the observation the new ruling adopted.** A computed-then-sealed artefact **honestly carries two failure meanings**: its failure can demonstrate a verification already passed to be false (the VOID meaning) and can be a computation that did not resolve (the numerical meaning). **Pretending one meaning away was the defect; the OPEN ORDERING RULE below says which side wins, and it is declared as an ordering, not disguised as a partition:**
  **THE ORDERING RULE.** For a post-unblinding failure on an artefact that is both computed and verified, **ask what the failure DEMONSTRATES** (the seats' distinction, adopted as the tiebreaker's rationale): if the failing state **contradicts what a completed verification certified** — a sealed digest no longer matching, a verified object now malformed — **`VOID` wins**, because the record is impeached; if the failure is a **value the run computed failing to resolve** — non-finite, degenerate, infeasible — **the inconclusive side wins**, because the record stands and the arithmetic does not. **Where both descriptions are true of one event, `VOID` wins**, because an impeached record cannot host an inconclusive halt.
  **The superseded partition's history, kept because the record is worth more than a clean diff (principal ruling, 2026-08-29; GPT56-V54 F1, HIGH):** V50 added the VOID antecedents to this rule's precedence to stop the two clauses claiming the same post-unblinding failures, **and the defect recurred at V54**, because precedence decides *which code wins* while both clauses still **describe the same events in the same phase**. A third ordering patch would have been the third attempt at the wrong kind of fix. **The two clauses are therefore made disjoint by what they are about, and the partition is stated here rather than the edit**, so a reader can take any post-unblinding failure and see which clause owns it **without consulting any rule of precedence**:
  **Ask one question about the failing quantity: was it PINNED, SEALED OR VERIFIED before this point, or did the run COMPUTE it?**
  — **A pinned, sealed or already-verified object that is now non-finite, degenerate, or otherwise not what its verification certified is `VOID`.** Such a value does not report a computation that failed; it reports that **an object the run was permitted to proceed on is not the object that was checked** — which is a deviation, and is claimed by `VOID-5-NONFINITE`, `VOID-5-DEGENERATE`, `VOID-5-DIGEST-DEVIATION`, `VOID-5-PROTOCOL-DEVIATION` or `VOID-5-FORBIDDEN-ACT`.
  — **A quantity the run computed from admissible inputs that is non-finite, degenerate, infeasible or out of domain is `INCONCLUSIVE-BY-NUMERICAL-FAILURE`** — or the more specific inconclusive code that names it. Nothing about the record is contradicted; the arithmetic did not resolve.
  **The two sets are exhaustive and exclusive, which is what makes this a partition and not a preference.** Exhaustive: every failing quantity either existed and was verified before the failure or was produced by the run. Exclusive: a pinned object is not computed by this run, and a quantity this run computed was not verified before unblinding. **The mixed case is decided by the same question, not by an exception** — a computed quantity *derived from* a pinned object is a computed quantity, and it is the pinned object itself, not its derivative, that VOID examines.
  **This NARROWS what `VOID` covers post-unblinding, deliberately.** A non-finite permutation statistic is no longer VOID merely by being non-finite post-unblinding; it is VOID only if the non-finiteness shows a sealed or pinned object wrong. **The misconduct conditions are untouched and remain `Any` phase** — forbidden acts and protocol/digest deviation catch a broken protocol independently of any numerical route, so nothing here lets a breach be reported as arithmetic. **This is the option-C ruling one level down: a computation that failed is not a protocol that was broken.**
  **HOW TO TELL WHETHER THIS REPAIR LANDED — the falsification test, stated because the previous two attempts both looked repaired.** Take any post-unblinding failure and resolve it with the question above alone. **If any case requires a precedence rule to decide, the sets are not disjoint and this repair has NOT landed** — and the fix is then the partition again, not a fourth ordering.
  **Specificity among the inconclusive codes is not precedence and is not affected.** It is carried by this rule's own CONDITION, clause (ii): `INCONCLUSIVE-BY-POWER` for the Stage-C and `N_eq` power guards, `INCONCLUSIVE-BY-CALIBRATION` for aggregate validation and `INCONCLUSIVE-BY-MISSING-ALLOCATED-OUTPUT` for Row I's abort each **name** a failure, so that failure is *already claimed* and this rule never reaches it. Those three sit on the same side of the partition as this code; they are more specific claimants, not a competing category. **Being silent where a specific code already fires is correct behaviour here, not a defect** — this rule exists to terminate branches that terminate nowhere. That distinction is what the V46 deletion was about and what makes this addition consistent with it.
  **PLANNING FAILURES ARE NOT RUN OUTCOMES (principal ruling, 2026-08-29; GPT56-V54 F3).** A failure that fires **before a run exists** — during plan construction — cannot be a run outcome of any kind: **nothing has started, so nothing can be voided and nothing can be declared inconclusive.** It stops the operator, and the operator has not yet begun. **The `NUMERICAL-PLANNING` class I created while classifying is therefore removed as an outcome class rather than legitimised here**, and its three sites are **moved, not deleted** — and **two of the three are `CALLER` while the third is not, which corrects a premise of the ruling rather than the ruling (GPT56-V63 F2, HIGH).** `local_pass` L963 and L973 report that no subset of bricks reaches `l_plan`, and `l_plan` is **supplied by the caller**, so those two are setup errors against a supplied target. **L986 is `MOVE_CAP` — an internal iteration cap that fires AFTER a feasible prefix has already been found, against a frozen module constant rather than any argument.** Calling it a caller error would have violated this section's own supplied-argument boundary, which is the boundary the ruling was applied under. **It is dispositioned `PLANNING-INTERNAL`, and that is deliberately NOT an outcome class:** it carries **no terminal consequence**, because a failure before a run exists cannot terminate a run. `NUMERICAL-PLANNING` was removed for **claiming to be an outcome**; this records a disposition for a **non-outcome**, which is the distinction the ledger has to be able to express. **Three sites hold it: L986, and — added at V69 on CODEX-V68 F3 — `_plan` L1331 and L1341, which raise the TYPED OUTCOME exception `InconclusiveByPower` AT PLANNING.** Before a run exists nothing can be declared inconclusive, so the typed exception there is the **operator-stop mechanism**, not a producer of the outcome class — `INCONCLUSIVE-BY-POWER` as a *run outcome* is produced only by the run-time guards §5 names (Row J, the Stage-C and `N_eq` guards). **The classifier had auto-typed these two by exception TYPE before any planning check ran, which is how the ruling's own boundary got violated by the ledger built to apply it.** The AST inventory's *"2 `InconclusiveByPower`"* remains true — it counts nodes by exception type, not by classification. and they still need a disposition. **The per-call-site ledger is where this ruling could have failed, and it was checked rather than assumed:** `ref/RAISE_CALLSITE_LEDGER.md` finds three reaching paths for each of the three sites — `build_plan → _plan → local_pass` and two fixture paths — and **none reaches them through `run_production_verdict`.** Consistent with that ledger's own stated limit, the call graph is name-based and a **lower bound**, so this is *no run-time path found*, not *no run-time path exists*. **If any of the three is ever shown reachable during a run, it goes back to the principal**: the ruling was about planning failures, not about those three line numbers.
  **THE BOUNDARY, and it is the load-bearing part of this repair.** A `raise` is a **caller error** — needing no run outcome — if it tests a property of an argument *as supplied*: its type, shape, field set, or admissibility. Such a failure cannot occur unless the caller violated the contract, and it is a defect in the caller rather than an outcome of the run. A `raise` is a **run outcome** if it tests a property of a value *computed from admissible data* — non-finite, degenerate, infeasible, out-of-domain. **The checkable test:** *could this raise fire while every argument satisfies the documented contract and the data is admissible?* If yes, it is a run outcome and must terminate in a named one. If no, it is a caller error and must not. **Getting this boundary wrong in either direction is the failure mode of this repair** — too wide and the rule swallows input validation; too narrow and real failures stay unterminated.
  **A THIRD STATUS: `UNREACHABLE-BY-CONSTRUCTION` (principal ruling, 2026-08-29).** The binary above has been revised twice and broken a third way, which is evidence that the *scheme* is the wrong shape rather than that the revisions were careless. A guard that **cannot fire at all** is neither a caller error nor a run outcome, and forcing it into two values will keep producing this.
  **PROMOTION REQUIRES A STRUCTURAL PROOF. MEASUREMENT IS CORROBORATION AND IS NEVER SUFFICIENT (principal ruling, 2026-08-29; GPT56-V54 F2, CODEX-V54 F1, both seats).** The earlier bar admitted three bases, of which the first was **an execution count alone**. CODEX stated the defect exactly, and the sentence belongs in the text rather than only in the fix: **the old bar *"lets non-exhaustive measurement-only sampling establish a status defined as impossible by construction."*** `UNREACHABLE-BY-CONSTRUCTION` asserts **impossibility**, and **no finite execution count can establish impossibility** — a measurement-only basis was incoherent with the status's own name.
  **The brief for the V54 round asked both seats whether the bar could be satisfied literally and still be wrong. Both said yes.** A bar that can be met in full by a claim that is false is not a bar, and that answer is the cleanest statement of the defect anyone produced.
  **What promotes a guard to this status, now:** a **structural argument** — a preceding condition that **provably subsumes** the guard, stated as **the specific earlier condition, per site**, not as the family it belongs to. **An execution count may be reported alongside it as corroboration, and it may never carry a promotion on its own.**
  **THE CATEGORY MAY STAY EMPTY FOREVER, AND THAT IS A REAL ANSWER — NOT A DEFECT TO BE FIXED BY LOOSENING THE BAR.** This sentence is here for the editor who finds a permanently empty category and reads it as an oversight. **A category that cannot be wrongly populated is worth more than one that can.** If no guard in this reference is ever provably unreachable, the correct record is that none is — and the correct response is to leave the category empty, not to restore a basis that lets sampling speak for proof.
  **NO SITE CURRENTLY HOLDS THIS STATUS. All five promotions are WITHDRAWN (GPT56-V53 F1, CODEX-V53
F1, both HIGH; CODEX-V53 F2).** The status exists — it was ruled — but nothing has yet met its
evidence bar, and the two attempts to populate it both failed.
  **What went wrong, because it is the reason the bar is written the way it is.** V52 claimed five of
`allocate_handcheck`'s eight guards were unreachable **without naming them**, while the ledger marked
all eight `NUMERICAL`. V53 named them and asserted L1401 was promoted on measurement. **Both seats
then showed L1401 is directly reachable**: `allocate_handcheck(cell_counts, budget)` takes `budget`
as an argument, and **the harness held it fixed at the frozen `HC_REAL_LABELS = 500`.** At
`budget = 200` with abundant objects, L1401 fires immediately. **A harness that freezes an argument
cannot observe the guards that argument controls, and non-observation under it is not unreachability
— it is a fact about the harness.**
  **THE WITHDRAWAL OF ALL FIVE STANDS ON THE RULE, NOT ON THE MEASUREMENT (principal ruling, 2026-08-29; CODEX-V54 F3).** The four remaining guards (L1411, L1435, L1437, L1439) did not fire across a large re-run with `budget` varied, **and that measurement is load-bearing for nothing.** Two reasons, and either alone is sufficient. **First, the rule:** they were withdrawn because a generic appeal to *"feasibility is decided before allocating"* is not the **per-site predecessor condition** this section requires (CODEX-V53 F2) — surviving a better harness is not meeting the bar. **Second, the basis:** with measurement-only promotion dropped above, no promotion can rest on an execution count at all. **And the harness itself was run ad hoc from a scratchpad and is not reproducible from this build** — the same defect as an unpinned constant, which is why a withdrawal resting on it would be weaker than it looks. **The count is recorded as history and carries no weight**; the text previously quoted it as both 80,000 and 60,000 in two places, a drift that no longer matters because nothing now depends on the number.
  **What a promotion must carry, stated so the third attempt is not a third failure:** (a) a harness
that **varies every argument in the callable's documented surface — and that RECORDS WHICH ARGUMENTS IT VARIED, with their ranges, in the receipt it produces.** A harness that cannot demonstrate which arguments it varied is the same object as a control that cannot fail. **This shape has now recurred three times in one day** — `budget` frozen in the gate harness, `n_perm` frozen in the feasibility harness, `budget` frozen again in the re-run — three parameters, three harnesses, one failure: **a harness cannot observe what it holds fixed.** It varies not only the values a particular
caller supplies, with the generator and count recorded; (b) for a structural claim, **the specific
earlier condition that subsumes this one**, named and per site — not the family it belongs to; and
(c) the positive control showing the harness reaches that family at all.
  **Evidence of unreachability is not proof of it, and the text must say what happens when a promotion is wrong.** If a guard marked `UNREACHABLE-BY-CONSTRUCTION` ever fires, **the classification is falsified, not the run**: the guard is a reachable numerical failure, it terminates in `INCONCLUSIVE-BY-NUMERICAL-FAILURE` under the default rule above, and the classification record must be corrected with the firing recorded as its cause. **This status is therefore a claim about the RECORD, never about routing** — being wrong about it produces a corrected record and a named outcome, not an unterminated branch. That property is what makes a third category safe here; without it, `UNREACHABLE` would become the place to put guards nobody wants to classify, which is the failure mode of every third category.
  **Known extent, reported as a range and not a number.** Counted by AST rather than by `grep` after GPT56-V49 F4 showed the grep wrong: the pinned reference carries **112 `Raise` nodes — 68 `RuntimeError`, 39 `ManifestClosureError`, 2 `InconclusiveByPower`, 1 `ValueError`, 1 `InconclusiveByCalibration`, 1 bare re-raise.** The earlier figure of 111 keyed on `RuntimeError|ValueError` and **missed all 39 `ManifestClosureError` sites**, a third of the total. **The corpus has since been read in full and the earlier partition is superseded** (GPT56-V52 F2, CODEX-V52 F2, which found 108/111/112 coexisting here). Every site is classified in `ref/RAISE_SITE_CLASSIFICATION.md`: **See `ref/RAISE_SITE_CLASSIFICATION.md` for the live totals — this sentence previously carried a hand-copied set that drifted from the generated table (GPT56-V56 F4, CODEX-V56 F6). The ledger is generated; a count copied beside it is a second source for one fact and will drift again.** **The numerical class is whatever `ref/RAISE_SITE_CLASSIFICATION.md` emits — at this revision, 20.** **The `NUMERICAL-PLANNING` class is gone from the ledger by the ruling above; L963 and L973 are `CALLER` and L986 is `PLANNING-INTERNAL`.** **This sentence said all three were `CALLER` for three revisions after L986 moved (GPT56-V66 F5, CODEX-V66 F6) — the drift recorded here, occurring in the sentence written to record it. The ledger is generated and this sentence is hand-written; that asymmetry is the whole mechanism, and the only durable fix is to quote the ledger rather than restate it.** **§5 quotes the generated ledger and does not restate it (GPT56-V59 F7, CODEX-V59 F5):** a number copied beside a generated table is a second source for one fact, and it has now drifted three times — 22 against an eight-site marking, 21 against 20, and the header against its own body. **The ledger is authoritative; if this sentence and the table disagree, the table is right.** All eight `allocate_handcheck` guards are included, since no promotion now stands; **`accuracy_from_handcheck`'s agreement-count check (L1464) was moved to `CALLER` — it tests a supplied count's admissibility, so classifying it `NUMERICAL` violated this section's own boundary (CODEX-V54 F2)** — or 18 if the three remaining flagged domain checks read as caller errors too. **§5 and the ledger must agree, and they have disagreed in both directions across V52 and V53** (22 against an eight-site marking, then 17 against a partly-stale §11). The ledger is regenerated with this draft. **The earlier figures — 29 caller, 31 run-time, 48 unread, and the range 31–79 — are withdrawn**, not merely superseded: they were produced by regex partitions that missed the 39 `ManifestClosureError` sites entirely. Four branches are *demonstrated* reachable by execution (`calibration_bins`' degenerate bins, and three of `allocate_handcheck`'s eight feasibility failures under the frozen constants). **The rule is written as a condition so that it covers sites without enumerating them**; if it needed a list, it would be the patch-per-instance habit wearing a rule's clothing.
  **THIS OUTCOME WAS RULED ON TWICE, DIFFERENTLY, AND BOTH RULINGS STAND.** On 2026-08-29 the principal ruled **option D** and `INCONCLUSIVE-BY-COMPUTATION` was **deleted** at V46 — on the ground that it was a **redundant claimant** on failures `INCONCLUSIVE-BY-POWER` already terminated. Later the same day he ruled **option B** and this code was **added** — on the ground that Row F's branches, the `allocate_handcheck` feasibility failures and the post-unblinding decision path (`_finite`, `w_profile`, `sigma_ours_scalar`, `sigma_ours_profile`) are **genuinely unterminated** and claimed by nothing. **A deletion for redundancy and an addition for absence are not a reversal**, and this paragraph exists because a reader six months from now will otherwise see a code removed and a code added within hours and reasonably conclude the record contradicts itself. **The first ruling was made against a two-branch problem; the second was made after the extent was measured.**
- **A deleted outcome, recorded once because the record is worth more than a clean diff.** V40–V45 carried **`INCONCLUSIVE-BY-COMPUTATION`**, a pre-unblinding numerical route. **It was removed at V46 because it could not be produced on the failures it named.** §4's Stage-C branch declares `INCONCLUSIVE-BY-POWER` on every FAIL, so ordering a second code after that guard made it unreachable, and ordering it before would have taken failures POWER already claims (GPT56-V43 F1, CODEX-V43 F1; GPT56-V44 F1, CODEX-V44 F1). **An outcome that cannot fire is a promise this text cannot keep.**
  **This is not a reversal of the option C ruling.** That ruling required a pre-unblinding numerical failure to *route to an inconclusive code alongside the calibration one*. **That route already existed** and still does — Stage C and the `N_eq` floor through `INCONCLUSIVE-BY-POWER`, the aggregates through `INCONCLUSIVE-BY-CALIBRATION`. (**An earlier version of this sentence also routed a per-object non-finite instrument output through §2.7's exclusion reason (c). That was false — reason (c) is *catalogue quality*, and §2.7 defers instrument non-finiteness to post-unblinding handling. It is removed here rather than left standing beside its own retraction — GPT56-V49 F3.**) The added code was never a new route; it was a **second claimant** on routes already terminated, which is what produced first an overlap and then a dead branch. The principal ruled on 2026-08-29 that `INCONCLUSIVE-BY-POWER` is the code his earlier ruling meant.
  **A completeness argument was offered here at V46 and is RETRACTED.** It claimed that every pre-unblinding numerical failure already terminates in a named outcome, resting on two premises the seats were asked to test. **Both failed** (GPT56-V46 F1/F2, CODEX-V46 F1/F2). First, it said a per-object non-finite instrument output falls to §2.7's exclusion reason (c); **reason (c) is catalogue quality**, and §2.7 defers instrument absence and non-finiteness to post-unblinding handling instead. Second, it enumerated the §6.1 rows and missed **Row F**, whose degenerate-bin and infeasible-allocation FAIL branches are executable and carry **no named outcome** — so Row R's default-forbidden clause does not close the set the way the argument required.
  **The general point survives and is worth keeping: a closed enumeration is an argument, an open one is only a failure to find something.** What failed was not that principle but my application of it — the enumeration was assembled with a keyword filter that silently dropped Row F, which is the same narrow-pattern-in-the-absence-direction error this document has been correcting all along, committed inside the argument about when absence may be asserted.
  **What that leaves open is recorded, not papered over:** whether every pre-unblinding numerical failure has an executable route to a named outcome is **UNRESOLVED** — see `OPEN_QUESTION_PRE_UNBLINDING_NUMERICAL_ROUTES.md`. **The deletion of the redundant code stands on the principal's ruling, not on this retracted argument.**
  **Why there is no rerun, recorded so it is not reintroduced.** V40 carried a five-step rerun allowance. Both seats found three HIGH defects in it: the halt was simultaneously terminal and retryable, contradicting §6.1 Row J's one-outcome contract; the rerun was either deterministic repetition or an unbound fork, with an attempt log that had no authenticated schema or verifier to make its own prohibition enforceable; and its attempt cap was declared mandatory before BS-6 with no dependency edge (GPT56-V40 F1/F2/F3, CODEX-V40 F1/F2/F3). **A terminal halt removes the contradiction rather than building machinery to sustain it**, and dissolves all three: no seed schedule, no attempt log, no verifier, no cap, no additional slot. **Class counts stay 16/8.**
- **`TERMINATED-UNNAMEABLE-REFUSAL-CLASS` (principal ruling, 2026-08-30, option (a) on the rulings collision):** produced when a catch-all `class_key` recurs after the first real χ. **A third thing — neither `VOID` (nothing is impeached) nor `INCONCLUSIVE` (nothing failed to resolve)**: the run ends because its custody layer failed in a way this preregistration cannot lawfully name mid-run, the §6.3 void rule and the naming obligation both standing untouched. The naming is owed to the successor preregistration's freeze review.
- **Accounting refusals (produced by Row P or the pre-verdict validator):** **INCONCLUSIVE-BY-MISSING-RECORD**, **INCONCLUSIVE-BY-DUPLICATE**, **INCONCLUSIVE-BY-ORPHAN**, **INCONCLUSIVE-BY-MALFORMED** (from Row P).
- **VOID:** triggered, **at any phase**, by **forbidden acts** and by **protocol/digest deviation**; and, **post-unblinding only**, by a **non-finite or degenerate value in a permutation, statistic or protocol object that was pinned, sealed or verified before that point** — a value contradicting what its verification certified, and **not** merely a failed computation on admissible inputs, which is `INCONCLUSIVE-BY-NUMERICAL-FAILURE` under the partition stated above. **This category is not yet executable.**
  **What moved and what did not (principal ruling of 2026-08-29 on CODEX-V38 F2, option C).** The *numerical* conditions — non-finite and degenerate, across the permutation, statistic and protocol subjects — are now explicitly **post-unblinding**, matching the phases §7.1 has carried since V24. **The *misconduct* conditions did not move and are not narrowed: forbidden acts and protocol/digest deviation remain `Any`**, exactly as `VOID-5-FORBIDDEN-ACT`, `VOID-5-PROTOCOL-DEVIATION` and `VOID-5-DIGEST-DEVIATION` record them. The distinction is the basis of the ruling: **a computation that failed is not a protocol that was broken.** A pre-unblinding numerical failure **does not void the run** — it terminates it through the pre-statistic inconclusive codes above; a pre-unblinding forbidden act or protocol deviation still voids it.

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
**Recorded limit (CODEX-V63 F4), because this text must not claim more than the guard does:** the
guard compares **two caller-supplied integers** and refuses when they differ. It **does not verify a
parent-to-receipt partition** — it does not check that the receipts correspond one-to-one to the
parent objects, only that a count agrees with a count. **Any equal pair of integers satisfies it**, so
it detects a short run and not a substituted, duplicated or misjoined one. **It is a count check, not a
completeness proof, and nothing downstream may read it as one.** This is the same shape as
`require_authorization`'s recorded limit above, found the same way, and it is recorded rather than
repaired because `successor_ref_v9.py` stays frozen at `6a9abbbd`.

## §6 Conduct

- **Disclosure.** Nothing derived from any real χ value — value, sign, summary, label, or count of signs — is published, spoken, or written outside the sealed stores defined in §6.1 before the primary lock, **with exactly one exception: the permitted aggregate surface defined in §6.1's scope paragraph, which leaves the sealed stores only as the BS-2f, BS-8f, and BS-5f receipts, on the paths the table names, and is the only pre-lock χ-derived export this text allows.** After unblinding, disclosure waits for BS-V (§7). The predecessor's §4/condition-2 breach is why this clause exists. What binds *access* is §6.1, and §6.1 is the normative object of this section.

### §6.1 The blinding covenant — one lifecycle table, and the table is normative

**Scope — what is χ-bearing.** A *χ-bearing object* is: any cutout produced for this run; any per-object instrument output — a χ value, sign, amplitude, confidence value, and every per-object execution measurement receipt, which carries those fields; any per-object hand-check label or per-object human–instrument agreement; any derivative of these that is not on the permitted aggregate surface below; and the predecessor's sealed archive of 208,405 χ measurements (§6.2) — outcome knowledge on overlapping sky, governed by §6.2's seal-state rule and enforceable mediation. The *permitted aggregate surface* — χ-derived but defined as not χ-bearing — is exactly: the BS-2f mask fields (brickid, objid, position, acceptance flag, calibration-bin label, boundaries, digests — never a χ sign), the BS-8f aggregate record (â, σ_a, a_LB, the per-bin {â_b, σ_ab, a_LB_b}, ε̂, and the full Cov_a — aggregates over the hand-check sample, never a per-object value), and the BS-5f Stage-C receipt (PASS/FAIL and the permitted Stage-C scalar output, never a per-object calibration label).

**Non-χ-bearing receipt and log classes — a closed list, defined by schema, and the list is exhaustive.** 
An artifact is non-χ-bearing only if it conforms to one of these authenticated schemas, none of which can carry a per-object outcome value or a digest of a payload containing one: 
(i) a slot receipt under the pinned `SLOT_SCHEMA` as conformed by this revision's code items — namely BS-1, BS-1b, BS-2a, BS-2v, BS-2c, BS-2k, BS-2m, BS-2o, BS-3, BS-3g, BS-4, BS-5p, BS-2s, BS-6, BS-7p, BS-8p, BS-9, BS-2f, BS-8f, BS-5f, and BS-L (BS-7f, the post-unblinding adequacy receipt, and BS-V are explicitly post-unblinding χ-bearing receipts and are removed from this list); 
(ii) the access log under its BS-2k event schema (timestamp, actor, table row, operation, object identity, success/refusal, refusal reason, running chain digest — identities and flags, never payload bytes). **The refusal-reason field carries exactly one code from the set below and nothing else: no free text, no appended detail, no formatted values** (principal ruling of 2026-08-29 on GPT56-V49 F1, as revised at 22:18 that day — see the non-closure ruling below).
  **THE PRINCIPLE, REBUILT (principal ruling, 2026-08-30 10:46, on CODEX-V64 F2 — the four availability codes describe the object's STORAGE STATE, and the old never-describe-the-object sentence condemned its own ruled codes): a refusal reason may describe the request, the authorisation state, and the object's STORAGE STATE — absent, unreadable, incomplete, digest-mismatched. It may never carry anything CONTENT-DERIVED: no measured property, no χ-derived value, nothing computed FROM the bytes. And the dependency is stated plainly, because it is what makes storage-state codes safe AT ALL: they are non-leaking ONLY because the read schedule is precommitted and χ-blind — WHICH object was being read carries no information when the traversal was fixed before any χ existed.** A reason such as *"instrument confidence below threshold"* is χ-derived and is excluded **by construction, not by discipline**. **An editor proposing a ninth code must satisfy this test, not merely match the style of the eight.**
  **THE SET IS NOT CLOSED, AND THE CATCH-ALL IS TAKEN (principal ruling, 2026-08-29 22:18 KST). The no-catch-all decision of 19:52 is FORMALLY REVERSED, not suspended.** **Eleven codes.**
  **Authorisation (5):** `REFUSED-ROW-NOT-AUTHORISED` (the requesting row has no stated surface covering this operation); `REFUSED-OUTSIDE-STATED-SURFACE` (authorised row, act outside its declared surface); `REFUSED-PRECONDITION-UNVERIFIED` (a required prior artifact is absent or fails its verifier); `REFUSED-PHASE-NOT-REACHED`; `REFUSED-LOCK-OR-CEREMONY-STATE` (the ceremony state does not permit this — **naming *which* state is finer than the refusal needs, and finer than needed is the same defect as free text in smaller units**).
  **Availability and mediator behaviour (4):** `REFUSED-OBJECT-ABSENT`; `REFUSED-OBJECT-UNREADABLE`; `REFUSED-OBJECT-INCOMPLETE`; `REFUSED-INTEGRITY-MISMATCH` — **flagged and UNRESOLVED, see below.**
  **Write conformance (1):** `REFUSED-SCHEMA-NONCONFORMING`. **It was proposed for deletion and the deletion is defeated:** Rows C2 and H write **non-slot, field-constrained** objects **through Row B**, and V62 scoped `receipt_strict()` to producers of artefacts whose slot is in `SLOT_SCHEMA` — **so my own scoping repair removed the basis for deleting this code**, and the alternative was leaving a real class of writes with no code that names their refusal.
  **Catch-all (1):** `REFUSED-UNCLASSIFIED`. **It carries a code and nothing else** — the reason field's no-free-text rule binds it exactly as it binds the other ten, and a catch-all with room to explain would be free text with extra steps.
  **THE GUARD, and it is the operative part of taking a catch-all. Every emission of `REFUSED-UNCLASSIFIED` is a DEFECT TO BE ENUMERATED, never a routine outcome** — a catch-all whose count is never reviewed **becomes** the vocabulary, which is the objection I raised against my own proposal.
  **THE ENUMERATION CANNOT HAPPEN AT FREEZE, and saying so is a correction to the mechanism rather than to the ruling (GPT56-V64 F2, CODEX-V64 F3, both HIGH).** The freeze is **P0**; every refusal happens **P1 or later**. **A freeze-time review cannot police emissions that do not exist yet** — the guard as worded was temporally impossible, and both seats said so.
  **IT ATTACHES TO THE PRE-UNBLINDING LOCK CHECKPOINT INSTEAD**, which is the first point at which the run's refusals exist and are still repairable, and which Row B's own cell already produces: *"its running checkpoint receipted at BS-2f, the pre-unblinding lock checkpoint receipt."*
  **THE BLOCKING INVARIANT, stated as a consequence rather than an intention: `BS-L` MAY NOT BE ISSUED while any `REFUSED-UNCLASSIFIED` event in the access-log chain is unenumerated.** The enumeration is part of the lock checkpoint: **one entry per emission**, each carrying the emission's `class_key` = (table row, operation) — **this sentence said "lifecycle state" for three revisions after the schema was shown not to carry it (CODEX-V69 F4)** — and **each named or explained by a person**.
  **AND EXPLANATION ALONE CANNOT DISCHARGE A RECURRING CLASS (CODEX-V66 F4, HIGH).** A class that fires every run can be explained every run and remain formally enumerated forever — **which is the catch-all becoming the vocabulary by the exact route the guard was written to block, while passing it.** So: **if the same class of catch-all emission recurs, explanation stops discharging it, and the vocabulary must be RE-DERIVED to name that class** — the set is not closed, so naming a recurring class is the maintenance the set was designed to accept. **Until it is named, the enumeration is incomplete and the gate stays shut.** **A defect you can explain repeatedly is a defect you have decided to keep.**
  **THE CLASS KEY IS COMPUTED, NOT ASSIGNED — because a class you may name is a class you may rename (GPT56-V67 F4, CODEX-V67 F4, both HIGH).** Two emissions are the same class **iff their `class_key`s are equal**, and `class_key` = **(table row, operation)** — **and `operation` is a token from the BS-2k event schema's CLOSED operation set, fixed at provisioning (CODEX-V70 F6: an unbounded operation string would make the key splittable by phrasing, which is the relabelling attack one field down)** — **and only those two, because they are the fields the closed event schema actually carries.** V68 keyed on lifecycle state as well, and both seats showed the schema has no such field (GPT56-V68 F3, CODEX-V68 F4) — a verifier cannot recompute a key from data the chain does not hold, and **adding the field would change what the log records, which is not authorised. The coarsening is the safe direction: a coarser key merges more emissions into one class, so the recurrence rule fires sooner, not later.** **Relabelling cannot split a class because the label is not in the key**; the enumeration verifier **recomputes the key from the event** and refuses an entry whose stored key mismatches, and **refuses a second `EXPLAINED` disposition for the same key within the run** — the second occurrence demands `NAMED-AS-DEFECT` and the vocabulary re-derivation that naming requires. **Neither token discharges on its own say-so (GPT56-V68 F4):** a `NAMED-AS-DEFECT` entry must carry the **digest of the re-derived vocabulary revision that names the class**, and the verifier refuses the entry if no revision exists at that digest **or if the revision's text does not contain this entry's `class_key` — existence is not naming (CODEX-V72 F4) — or if the revision's digest EQUALS the prior vocabulary revision's digest — a re-derivation that changed nothing named nothing (GPT56-V77 F7) — **and a CHANGED revision containing only the bare key still discharged vacuously (CODEX-V78 F4), so the naming is a checkable TEMPLATE: the revision must carry a line `NAMES-CLASS: <class_key> AS <token>` where the token is a member of the revised set **and the token's own definition in that revision contains the `class_key` — a template naming an unrelated existing member proved nothing about the recurring failure (CODEX-V79 F5)**; the verifier matches the template, the key, the membership, and the key's presence inside the named token's definition, which makes "the revision names the class" a parse instead of a hope.** What the predicate checks is that the key appears; whether the naming is adequate to the failures under it is the re-deriver's testimony, named as such like every other testimony here**; an `EXPLAINED` entry's `explanation_ref` must **resolve to a signed explanation artifact in the lock-checkpoint materials**, and a dangling reference is refused. **A disposition that cannot be followed to its object is the citation-chain defect in a new coat.** **And the recurrence rule is WITHIN-RUN, stated as a limit rather than discovered as one (GPT56-V68 F5):** both verifier passes read this run's chain, and no prior-run key history exists to consult. Cross-run recurrence is real and this mechanism cannot see it; **what closes that is an obligation on any successor preregistration — its freeze review must read this run's enumeration, **and a class explained in ANY prior run counts as RECURRING there — with the domain made honest (GPT56/CODEX-V83 F4: "any prior run" had no authenticated history): each preregistration LISTS its known predecessors (this one lists V3-pred), the duty runs over the LISTED predecessors' surviving enumerations, and a run that died before recording its failures contributes nothing — a NAMED limit, because a run that failed too early to record its failures cannot teach (GPT56-V82 F3)** — recorded here so the successor inherits the duty rather than the blindness.** **The key is facts about the request, not judgements about it, which is what makes the recurrence rule enforceable rather than aspirational.**
  **THE KEY IS THE TRIGGER GRANULARITY, NOT THE NAMING GRANULARITY (GPT56-V69 F5).** `(row, operation)` deliberately merges unlike defects — that is what coarse means — so when the rule fires, **the re-derivation does not name the key, it names what it FINDS**: the entries carry the `(chain_position, event_digest)` of every joined emission, the re-deriver reads those emissions from the chain, and **names every distinct failure it finds there — one class or several**. A merged key forcing one re-derivation that names two defects is the mechanism working, not failing: **the key decides WHEN the vocabulary must be revisited; the chain decides WHAT the revisit must name.**
  **An unenumerated catch-all emission therefore blocks the primary lock, and the run cannot proceed to unblinding with it outstanding.**
  **AND THE LOCK ALONE DOES NOT COVER IT, which I found while checking this repair rather than after a round found it.** The lock checkpoint is **P6**; Row B operates *"from BS-2k's completion through unblinding"*, so **refusals can occur in the P6 → P7 window, after the checkpoint that was supposed to enumerate them.** A single checkpoint anchors the obligation to one instant and leaves everything after it uncovered — the same defect as anchoring it at freeze, moved later rather than removed. **The obligation is therefore CONTINUOUS: every `REFUSED-UNCLASSIFIED` event must be enumerated before the next gate that follows it, and BOTH `BS-L` and the opening of the lock at unblinding are blocked while any is outstanding.** **A guard anchored to one moment is a guard with an after.**
  **AND A CONTINUOUS OBLIGATION WITH NO VERIFIER IS PROSE (GPT56-V66 F3, CODEX-V66 F3, both HIGH).** V66 said the obligation was continuous and named nothing that checks it, so a post-`BS-L` catch-all event still reached the opening: **no verifier consulted a fresh enumeration, and the guard's own control in `tools/refusal_vocabulary_check.py` matched the phrase "BS-L" rather than the mechanism** — the phrase-matching defect the checker was rewritten to remove, reproduced in the control written to remove it.
  **THE ENUMERATION VERIFIER, named and separately pinned.** It recomputes, **from the access-log chain itself**, the set of `REFUSED-UNCLASSIFIED` events, and **refuses unless every one of them carries an enumeration entry**. It never accepts a producer's summary of its own emissions.
  **It is consulted TWICE, and the second consultation is the one V66 was missing:** once at **`BS-L` issuance**, and again **at the opening of the lock**, over the chain **as it stands at that moment**. **An enumeration that was complete at `BS-L` does not discharge an event appended after it** — the second pass is against a fresh chain, not a remembered result. **Either refusal blocks its gate.**
  **WHERE POST-`BS-L` ENTRIES LIVE, because the checkpoint materials are digested and signed by `BS-L` itself and cannot be appended to afterwards (GPT56-V69 F4).** Entries recorded after `BS-L` go to an **authenticated continuation segment outside the sealed checkpoint materials** — each entry is **independently authenticated** by the enumerator's signature and its `(chain_position, event_digest)` join into the chain, so it needs no seal from the artifact it postdates. The opening pass reads **checkpoint entries plus continuation entries** against the chain as it then stands — **with a TEMPORAL PARTITION (CODEX-V82 F3): a continuation entry may join ONLY an event appended AFTER `BS-L` issuance; every pre-`BS-L` emission must be enumerated in the SEALED checkpoint materials, and a continuation entry claiming a pre-`BS-L` `chain_position` is REFUSED. **And the partition has no seam (GPT56/CODEX-V83 F3: an event during issuance itself fit neither side): Row B is a single serialised writer, and checkpoint-seal-through-issuance-completion is ONE serialised step of that writer — no event can be appended during it by construction, so the boundary is a point, not a window.** **And the signed EXPLANATION artifacts follow their entries (GPT56-V70 F2, CODEX-V70 F4): a post-`BS-L` `EXPLAINED` entry's explanation lives in the same authenticated continuation — independently signed, named by its `(chain_position, event_digest)` — because an artifact cannot be placed inside materials already sealed.** The V70 text sent post-seal entries to the continuation and left their explanations pointing at a sealed surface — the same defect, one reference deeper.
  **AND THE OPENING PASS IS NOT THE LAST GATE, because a catch-all can be appended DURING opening and unsealing, after that pass has run (CODEX-V69 F3).** The continuous rule already says every emission is enumerated **before the next gate that follows it**; its post-opening instantiation is now named rather than implied: **the P8 and P9 gates — BS-7f, BS-V, and disclosure — each require a fresh enumeration-verifier pass over the chain as it stands at that gate.** A catch-all emitted during the opening ceremony therefore blocks at BS-7f, not never. **A guard anchored to one moment is a guard with an after — the rule that found the P6→P7 hole, applied to the hole after P7.**
  **THE ENTRY, ITS PRODUCER, ITS JOIN AND ITS WIRING — because a verifier with no object to verify is a name (GPT56-V67 F3, CODEX-V67 F3, both HIGH).** An **ENUMERATION ENTRY** is an authenticated record with exactly these fields: `chain_position` (the event's index in the access-log chain) · `event_digest` (the chain's running digest at that position) · `class_key` (**computed, defined below**) · `disposition` (exactly one of `NAMED-AS-DEFECT` · `EXPLAINED`) · `rederivation_digest` (**required exactly when the disposition is `NAMED-AS-DEFECT`**: the digest of the re-derived vocabulary revision that names this class — the verifier refuses the entry if no revision exists at that digest, and refuses the field's presence under `EXPLAINED`) · `explanation_ref` (**required exactly when the disposition is `EXPLAINED`**: **the sha256 of the canonical explanation body — a digest-ref, because V72 introduced this field as an unbounded identifier in the same revision that declared the string rule (GPT56-V72 F3)**, and **the explanation artifact is itself CLOSED-VOCABULARY under the string rule (GPT56-V71 F4, CODEX-V71 F4): a `cause` token from the declared set, **which is an ORDERED PRECEDENCE, not a menu: `VERIFIED-TIMEOUT` is a typo trap — the order is `VERIFIER-TIMEOUT` > `WORKER-CRASH` > `DEADLOCK` > `LEASE-LOST` > `STORE-UNAVAILABLE`, and when more than one truthfully applies the highest-precedence one is MANDATORY. Determinism removes the SELECTOR (GPT56-V77 F8) — and what it does not remove is stated rather than claimed away (CODEX-V78 F3): WHICH causes apply can itself correlate with what the process was touching, so the token carries a residual channel of at most log₂5 bits per catch-all emission through applicability. That residual is bounded by the guard that already exists — every emission is an enumerated defect reviewed at the gates, so patterned use is the review's to catch — and it is the price of the token having diagnostic content at all. A channel you cannot remove without destroying the field's purpose is a NAMED RESIDUAL, like N3** — plus bounded numeric parameters (durations, counts) — NO free prose pre-unblinding. A failure inexpressible in that vocabulary CANNOT be `EXPLAINED` and must be `NAMED-AS-DEFECT`**, which is the honest outcome for a failure nobody can name from a closed list. **THE canonical byte encoding — ONE encoding for every canonical body, defined by the frozen constructor rather than per body (GPT56-V78 F3, CODEX-V78 F6: bodies were digest-refs to encodings that were named per-body and written for some): a canonical body is the concatenation of v9's `field(name, payload)` records — 4-byte little-endian name length, UTF-8 name, 8-byte little-endian payload length, payload — in the body's declared field order. **And the PAYLOAD encodings are declared, because framing bytes without defining them left every logical value's serialization open (CODEX-V79 F6): raw bytes as themselves; text as UTF-8; integers as decimal ASCII; digests as lowercase hex ASCII; any structured or nested value as canonical JSON — **made UNIQUE, because sorted-compact alone is not (GPT56-V81 F7, CODEX-V81 F7): keys sorted bytewise, compact separators, UTF-8 with strings NFC-normalised, escapes minimal (only JSON-mandatory ones), integers only — floats are FORBIDDEN in structured payloads, real values living in dedicated decimal-ASCII fields — no leading zeros, no `+`, `-0` forbidden; **escape hex is LOWERCASE, and an object whose keys collide AFTER NFC normalisation is REFUSED as invalid rather than silently merged (CODEX-V82 F4)** — v9's envelope convention, tightened to one byte string per value.** The explanation body's order is `(chain_position, event_digest, cause, parameters…)`, parameters sorted by name (GPT56-V77 F3). **The opening authorization's canonical body is CLAUSE 6's, and V79's three-field declaration here is WITHDRAWN — it invented a second, incompatible body for an object Clause 6 had already bound (GPT56-V79 F2, CODEX-V79 F2, verbatim-convergent; one object, one body): the field order is Clause 6's enumeration — `(bsl_digest, store_identity_main, store_identity_committee, destination, ceremony_id, phase, signer_identity, schema_version)`. **AND THE V80 WITHDRAWAL GOT THE LAST FIELD WRONG TOO — it substituted `timestamp` for Clause 6's `schema/version`, a second wrong correction on the same object (GPT56-V80 F1, CODEX-V80 F3), which is §8 item 9's citation-chain shape exactly: a correction that is itself unverified is not a correction. This one is verified against Clause 6's bytes.** The freeze-signature, lock and entry bodies already declare theirs; `provenance_record` remains SCHEMA-PENDING and says so. The artifact names the `(chain_position, event_digest)` it explains — an unbound explanation can discharge any emission it is pointed at (GPT56-V69 F3, CODEX-V69 F4) — and the verifier checks `cause` membership, parameter bounds, the join, **and consistency of `cause` with the entry's `class_key`; what it cannot check is whether the cause is what actually happened, which is TESTIMONY, signed and named as such** — GPT56-V71 F5) · the enumerator's signature — **which binds a named signer, not a mark (CODEX-V71 F3): a detached signature over the CANONICAL ENTRY BODY (the fields above in canonical field-order encoding, the same discipline as BS-L's lock body), under the enumerator keypair PROVISIONED AT BS-2k and recorded in its design artifacts. The verifier refuses a signature by any unprovisioned key, over any non-canonical body, or lacking the signer identity the BS-2k roster carries.** A signature with no trust root is a checkbox. **V69's field list carried neither conditional field while the prose demanded both — the schema and the prose were two statements of one fact, drifted apart in the revision that added the requirement.** **The JOIN is `(chain_position, event_digest)`** — both already exist in the chain, so **nothing new enters the access log**; entries live in the **lock-checkpoint materials**, produced under Row B's existing checkpoint duty. **THE WIRING:** §5's BS-L verification guard extends — **`BS-L` may not issue without an enumeration-verifier PASS over the chain at issuance, and the opening authorization's verifier requires a FRESH PASS at opening**; §11 carries the build item for `gates/enumeration_verifier.py`, separately pinned, which **recomputes the emission set and every `class_key` from the chain itself and never accepts a producer's summary of its own emissions**. **AND THE LIMIT OF THE LINT, stated because three consecutive revisions phrase-matched here:** `tools/refusal_vocabulary_check.py` verifies that **this text states** the mechanism. **It cannot verify the mechanism exists.** Existence is established by the §11 item and its gate round, and a green lint says nothing about it. That is what makes the guard executable: **it is not a promise to review, it is a gate that will not open.**
  **Deliberately not made a VOID condition.** Blocking the lock stops the run **repairably**; voiding it does not. The ruling asked that catch-all use be a defect to be enumerated, **and a defect that halts until it is enumerated is that, where a defect that destroys the run is something stronger than was ruled.** If the principal wants the stronger form, it is one sentence — but it is his sentence.
  **WHY THE SET IS NOT CLOSED — two derivations, both broken, and that is the finding.** The first argued closure from §6.1's closed row table; **both seats broke it in one round** (GPT56-V56 F1/F2, CODEX-V56 F1/F3) — an authorised read of a permitted but **missing or unreadable** cutout is a refusal none of the eight codes covered, so a routine I/O failure would have voided the study. **The enumeration missed a CLASS, not a member.** The principal ordered the derivation redone from scratch rather than extended by a ninth code, and the second attempt derived two axes — *not permitted* and *permitted but unavailable* — resting on the claim that **"permitted" is binary and evaluated before the attempt.** **Both seats broke that too, in different directions.** CODEX found an **escape**: permission can be **undecided**, because Row B must verify Row D's authenticated stage-completion artifact and that verifier can time out or die **before returning a verdict** — the access completes neither, and is adjudicated neither. GPT56 found an **overlap**: field-constrained writes need permission facts learned **during** the transfer. **And the miss was self-inflicted — the requirement below names "timed out" among the failures to cover, and that word did not appear once in the derivation written against it.**
  **THE SEQUENCE IS WHY THIS RULING HOLDS, and it belongs in the record rather than in a note.** The catch-all was ruled **after** the second derivation was attacked, **not against it**. Had it been decided against an argument that had only been written, it would have collapsed exactly as the first one did and we would have learned that in the following round. **Two independent derivations broken within an hour of being written is evidence about the surface, not about the two arguments** — and once closure cannot be shown, the escape hatch stops being a concession and becomes the honest answer, while a routine verifier timeout stops voiding the study.
  **THE PRINCIPLE STILL BINDS EVERY CODE INCLUDING THE CATCH-ALL**, and it is the test the codes must pass rather than a style guide: a reason may describe the request and the authorisation state and **may never describe the object**. REFUSED-IDENTITY-OUTSIDE-PERMITTED-SET — written here **without code formatting deliberately, so it is not read as a member of the set, and so the checker does not count it as one** — was **deleted, not reworded** — *"outside the permitted set"* already **is** *"outside the stated surface"*, so it was redundant **and** leaking, and rewording would have kept a code that publishes a membership answer. **CODEX's generalisation governs every candidate: request-shaped codes can still reveal object membership or bounds.**
  **`REFUSED-INTEGRITY-MISMATCH` IS RESOLVED: THE REFUSAL OWNS IT (principal ruling, 2026-08-30 10:46).** A read-time digest mismatch on a sealed object is **logged as this refusal and the run CONTINUES** — chosen over halt-for-a-human and over void, on the same philosophy as the catch-all: log honestly, review at freeze. **Two guards, written in as ruled: (i) every mismatch is enumerated at freeze, and ANY UNEXPLAINED MISMATCH AT FREEZE BLOCKS THE FREEZE; (ii) the phase-Any digest-deviation VOID antecedent is SCOPED by ruling 1's ordering rule** — the wording, reported as asked: *a read-time mismatch DEMONSTRATES only that the bytes served now differ from the bytes certified; it does not by itself impeach the certification, so the refusal side owns it. `VOID-5-DIGEST-DEVIATION` claims the mismatch that impeaches the record — a re-verification of the stored object itself failing, a checkpoint that does not extend its predecessor — where what failed is the certification, not a read.* Nothing observable at emission distinguishes fault from tampering — both seats established that — **and the freeze-time enumeration is where the distinction is adjudicated by a person, with the freeze blocked until it is.** The earlier flagged state and CODEX's competition finding for one event. **Left open rather than resolved:** getting it wrong toward VOID is how the earlier over-strict concern arose, and getting it wrong the other way logs tampering as a fault.
  **A POST-χ RECURRING CATCH-ALL CLASS TERMINATES THE RUN (principal ruling, 2026-08-30 10:46, option (a) on the rulings collision: naming a recurring class requires re-deriving the vocabulary, and the §6.3 void rule forbids any post-χ change to a binding rule — both laws STAND, and the collision becomes a stated terminal outcome).** The ending is **its own named thing — `TERMINATED-UNNAMEABLE-REFUSAL-CLASS` — not a `VOID` and not an `INCONCLUSIVE`**, because forcing it into either family would recreate the two-claimants defect this document has now been ruled out of twice. It is produced when a catch-all `class_key` recurs after the first real χ; the record stands (nothing is impeached), the arithmetic is untouched (nothing failed to resolve) — **the run ends because its custody layer failed in a way this preregistration cannot lawfully name mid-run. The naming is owed to the successor preregistration's freeze review.**
  **What this set does NOT repair, recorded so the catch-all cannot absorb it.** The catch-all makes an undecided permission **loggable**; it does not make it **decided**. That is a covenant defect and it is repaired by the request lifecycle clause below, not here.
  **The set is DERIVED FROM §6.1, not constant — and it is not closed, so this is a maintenance rule rather than a closure claim.** When §6.1 gains a row, a surface or a precondition, the vocabulary is **re-derived as a whole, never extended by hand**; the difference from before is that a re-derivation no longer has to prove it caught everything, because the catch-all carries what it misses and the continuous enumeration and its verifier surface it (this sentence said "freeze-time" for two revisions after the mechanism moved to run-time gates — GPT56-V67 F7, CODEX-V67 F8).
  refusal-vocabulary-derivation: **DELIBERATELY NOT PINNED.** The derivation this fingerprint was built to protect **does not exist** — closure is not claimed, so there is no closure argument for a fingerprint to detect the invalidation of. **Two digests are involved and V59 labelled one wrongly (GPT56-V59 F5, CODEX-V59 F4):** `fd6d6d7e99dcb5ca…` is the corrected **row fingerprint** of §6.1's gate-bearing columns; `5ee5967580443f57…` is the sha256 of `tools/refusal_vocabulary_check.py` **itself**, **recomputed after the last edit to that file in this revision, which is the only order that survives.** **V64 carried `c2ccebbcb4730944…` here, which was that file's digest BEFORE V64 rewrote it in the same revision (GPT56-V64 F5, CODEX-V64 F7) — a digest for a file changed in the act of citing it. The lesson is narrow and it repeated INSIDE this repair: V66's first draft of this sentence carried `acb38c401e00b075…`, which was the checker's digest before V66 extended it with the mechanism controls R06 and R07 — so the sentence correcting a stale digest went stale while being written. A digest quoted for a file the same revision edits must be recomputed AFTER the last edit to that file, and the only order that survives is to compute it last.** **Both values were right; the sentence was wrong.** The checker now checks that this text STATES the eleven-code set and the catch-all guard — a lint verifies text, and its member-parse and contradiction scan were hardened at V71 after a seat defeated both by Markdown formatting (GPT56-V70 F4) — and **states no closure claim**, because a control that reports health about a claim nobody makes is worse than no control.

**REQUEST LIFECYCLE — Row B decides permission durably, and every state has one terminal treatment (repairing CODEX-VOCAB F1 and GPT56-VOCAB F1, both HIGH).** The derivation above assumed permission is *"evaluated before the attempt."* **The covenant nowhere imposed that ordering, and it is false in two ways** — a permission check can die before deciding, and a write's conformance cannot be judged before its payload is read. **Asserting the ordering is what failed; stating the machine is the repair.**
  **THE LIFECYCLE IS SPECIFIED IN `LIFECYCLE_GUARANTEE_SPEC.md` AND THIS TEXT IS DERIVED FROM IT — after the same object failed THREE consecutive rounds (V67 F1/F2, V68 F1/F2, V69 F1/F2), which is this lane's stop-patching threshold, invoked here as it was for the citation check.** The third failure was the most familiar shape in this corpus: **V69 deleted the `TRANSFER` state in one paragraph and this sentence still declared it** (GPT56-V69 F1, CODEX-V69 F1) — a deletion that did not delete. **The state machine now has ONE home, the spec, and this declaration quotes it:** `RECEIVED` → `PENDING-AUTHORISATION` → (writes only: `PENDING-SURFACE-CHECK`, because a field-constrained write's conformance cannot be known until Row B decodes the payload) → **one commit, refusal or touch** → (conveyance only: delivery, outside the custody claim). **There is no `TRANSFER` state.** The spec carries the full invariant table — five crash windows × four readers — and its guarantees G1–G5 and non-guarantees N1–N3, **with G2 and G3 restated at V71 because their V70 wording contradicted refusal events outright — an event with no store effect violated "one touch per event", and G2 said nothing about its truth (GPT56-V70 F1, CODEX-V70 F1, the first finding scored against the spec itself): a refusal event truthfully records that NO effect occurred, and every event is exactly one touch's or one refusal's, never both, never neither**; **a conflict between this draft and the spec is a defect in the draft.**
  **THE GUARANTEE — QUOTED FROM THE SPEC BY DIGEST, NOT RESTATED (GPT56-V71 F1, CODEX-V71 F1).** V71 amended the spec's G2/G3 and left this block carrying the V70-broken wording — the exact one-round death the derivation claim was warned about, arrived in mirror form: the warning said do not fix the draft and leave the spec behind; V71 fixed the spec and left the draft behind. **The derivation is now a CHECK, not a claim**: `tools/lifecycle_derivation_check.py` fails when the pin below goes stale or any quoted invariant body diverges from the spec's bytes — a spec edit breaks the pin until the draft re-pins, which forces the re-derivation instead of permitting the drift. **This class of finding is now impossible rather than unlikely, which is the difference between a predicate and a name.**
  lifecycle-spec: sha256 `6984d62f548f1d37ff1f70f3f80e475c25988c15beec0abb76ec72170b1fcd69`
  **G1 — **No unlogged touch**: no bytes leave or land in a sealed store without a committed event**
  **G2 — **No false event**: a touch event's outcome field is true of the store effect it records; **a refusal event truthfully records that a request was refused and NO store effect occurred — AND its reason token is true of the refusal: a request with no completed permission verdict may carry only `REFUSED-UNCLASSIFIED`, and any specific code asserts its condition was actually established (GPT56-V71 F2: without this, a false specific code bypasses the catch-all enumeration entirely)**
  **WHAT CAN CHECK THAT — refined at V79 because both halves of the V78 split were too coarse (GPT56-V78 F4: immutable chain history can make a false `OBJECT-ABSENT` audit-provable, so availability is not uniformly testimony; CODEX-V78 F5: a normative truth condition with no CONSUMING verifier is prose). Per code: the five authorisation codes are RECOMPUTABLE from the chain and pinned artifacts; **`REFUSED-SCHEMA-NONCONFORMING` is NOT — the chain is payload-free by design, so nobody can recompute what the refused payload contained: it is TESTIMONY, and V80's table put it on the wrong side (GPT56-V80 F2)**; `REFUSED-OBJECT-ABSENT` is **contradiction-surfacing from history** — a prior committed touch proves PAST presence, not present absence's falsity (GPT56-V79 F3, CODEX-V79 F3, verbatim-convergent); but the stores are append-only and mutation is forbidden, so presence is monotone, and **history + a later ABSENT proves the DISJUNCTION: either the code is false or a forbidden removal occurred — both audit-findings, neither silent, and the audit surfaces the contradiction rather than adjudicating it. The join is on (STORE identity, brickid, objid) — store identity derived from the event's row and stated surface — because brickid/objid alone can pair touches of different objects in different stores (CODEX-V80 F4)**; `REFUSED-OBJECT-UNREADABLE`, `-INCOMPLETE` and `-INTEGRITY-MISMATCH` assert store states no later reader can replay and are testimony; `REFUSED-UNCLASSIFIED` is checked by the enumeration machinery. **The CONSUMER is named: the §11 audit pass — the enumeration verifier's sibling clause — recomputes every recomputable condition and the history-falsifiable one for EVERY specific refusal in the chain, at the same five gates.** The original statement (GPT56-V77 F5): codes whose conditions are RECOMPUTABLE from the chain and pinned artifacts — row surfaces, phase, lock state, precondition existence — are audit-checkable post hoc, and the auditor recomputes them; the availability codes assert store states no later reader can replay, and their truth is TESTIMONY under Row B's signature, named as such. A false specific code in the recomputable class is detectable; in the testimony class it is attributable. Neither is silent**
  **G3 — **One TOUCH event per touch** — and **every touch event is either exactly one touch's event or a refusal's event; no event is both, and no event is neither** (V70's wording said "one touch per event", which contradicted refusal events outright — GPT56-V70 F1, CODEX-V70 F1, the round's first finding against this spec)**
  **G4 — **No double decision**: one request never yields two events**
  **G5 — **Render = touch.** Every render is its own touch with its own committed event. **Row G's *"any unlogged view"* void clause is a consumer of G5, not an exception to N1**
  **And what it does NOT guarantee, with equal weight:**
  **N1 — **Delivery is outside the custody claim** — the event records the store effect, never the requester's receipt or the human's perception**
  **N2 — **RETIRED BY RULING (2026-08-30 10:46): the WRITE-AHEAD ARRIVAL RECEIPT makes every real request durably visible** — arrival is logged BEFORE any processing, as a second event class the principal explicitly authorised, so no request can vanish and the lifecycle promise becomes true instead of narrowed. Kept in the table as the record of what was a non-guarantee for eleven revisions**
  **N3 — **The log can over-report delivery, never under-report a touch**
  **THE CONSTRUCTION, derived from the guarantee.** A **TOUCH COMMIT** is one atomic commit in the BS-2k transactional domain comprising: the **store effect** (bytes leaving the store into Row B's committed buffer, or a validated write landing in the store), the **one event carrying that effect's true outcome**, and **Row B's identifier binding**. A **REFUSAL COMMIT** is the same commit with no store effect — an event and a binding. **DELIVERY is a separate act after the touch commit, executed from Row B's committed buffer** — and the retry allowance is **CONVEYANCE-ONLY, stated where the allowance lives because both seats found the unscoped sentence re-authorising what G5 forbids (GPT56-V73 F1, CODEX-V73 F7)**: re-sending a **conveyance** buffer to the same row is the same conveyance of the same authorised touch, not a second touch and never a second event; **a RENDER is never re-sent — every re-display is a new touch commit under G5, and a render buffer lives from its commit until its VIEW SESSION ends, then is destroyed** (CODEX-V74 F2). **And a committed render event asserts CONVEYANCE TO THE INTERFACE — bytes left the store — never that a human saw a frame (GPT56-V80 F3: a crash before first frame leaves a committed event and no view, which is a TRUE event about a conveyance whose session never opened; the no-session buffer path already destroys it at request end, and Row G's unlogged-view clause is untouched because no view occurred).** **And the sealed interface renders exclusively from Row B conveyances and holds NO redisplayable surface beyond the live session** (GPT56-V74 F3: a compositor restore after occlusion would create G6's new view with no G5 commit; occlude-and-restore must produce a second committed render event or no image — a BS-2k interface requirement with fixtures).
  **THE CORNERS NOW ENUMERATE, which is what stating the guarantee buys:**
  — **Death before any commit**: no effect, no event, no binding, no bytes moved — G1–G4 hold vacuously; this is N2.
  — **Death at the commit**: it is atomic; there is no partial state to enumerate.
  — **Death after commit, before or during delivery**: the event is TRUE — the store effect happened — and the requester may have nothing. **That is N1, accepted, and it is the only over-report this design permits.** Delivery retries from the committed buffer without a new event (G3).
  — **Bytes escaping an aborted commit**: impossible by construction — **the requester receives only from the committed buffer, and an aborted commit never produces one.**
  — **A write dying in validation**: the payload sits in Row B's pre-commit staging; no store effect occurred; N2.
  — **A change of terminal fact after the event**: **cannot exist.** The terminal fact IS the store effect, committed with its event in the same transaction. V68's `TRANSFER` state — a post-verdict period in which the outcome could still change — **is deleted, and its death rule with it**: there is no state after the commit whose failure alters anything the log claims (GPT56-V68 F2, CODEX-V68 F2).
  **What remains of the state machine:** `RECEIVED` → `PENDING-AUTHORISATION` → (writes: `PENDING-SURFACE-CHECK`) → **one commit, refusal or touch** → (reads: delivery from the committed buffer, outside the custody claim). **The contract is a requirement on the BS-2k design artifacts (§7 Row A) and §11 carries its implementation item; until BS-2k is filled with a design meeting it, this lifecycle is specified and not yet operative.**
  **WHAT A REQUEST IS, because "never re-decided" is unenforceable without it (CODEX-V66 F2, HIGH).** Row B assigns every received request an **internal identifier** on receipt, held in Row B's own recovery state and **not written to the access log** — nothing here changes what the log records. **A legal retry is a NEW request with a NEW identifier and produces its OWN event**, which is correct: the covenant requires *"exactly one event per touch"*, and a retry is a second touch. **What is forbidden is one request producing two events**, and identity is what makes that statement testable. **Repeated touches of the same object are expected and are not redecision.**
  **ONE DECISION PER REQUEST, AND ROW B OWNS RECOVERY.** Row B is a **single serialised writer** with **at most one decision in flight per request**. On recovery Row B consults its **committed bindings**, which the touch commit made atomic with the events: a request **with no binding never happened** and may be re-processed; a request **with a binding is never re-decided**. **A worker may not consult the chain instead — recomputing custody from the file being recovered is the hash-chain-launders-tampering shape.** **A worker that has lost its lease may not append** — the lease is Row B's, and losing it means the work is abandoned, not resumed.
  **WHAT THIS DID NOT FIX IS NOW FIXED BY RULING (2026-08-30 10:46): the WRITE-AHEAD ARRIVAL RECEIPT is the second event class, and changing what the log records is exactly what the principal authorised.** Arrival is durably logged before any processing, so a request in flight when Row B died has its arrival event — eleven revisions of the invisible pre-verdict death end as a logged arrival with no terminal event, a state recovery and the auditor can SEE and the deadline machinery closes. Spec §1c carries the class; N2 is retired in the table as history. **What the rules above do achieve without it:** no request is both undecided and delivered, and none is decided twice. **What remains:** a crash between decide-and-append is indistinguishable from a request that never arrived. **That is a real residue and it is stated as one.**
  **TERMINAL TREATMENT, fixed per state — and the fix distinguishes WHO died, which V68 did not.** A request whose **processing fails while Row B survives** — a worker timeout, a deadlock, a lost verifier — receives a **refusal commit carrying `REFUSED-UNCLASSIFIED`**: Row B is alive to append it, and the request ends logged. **And "fails" cannot be outwaited (CODEX-V80 F5): every request carries a DEADLINE — now specified in the spec's §3b as lifecycle semantics with its single home there (GPT56-V81 F2, CODEX-V81 F4: V81 put the deadline in this draft and not in the pinned spec, violating the single-home rule with the very repair that extended the lifecycle): a BS-2k design constant on the MONOTONIC clock, fixed at receipt, never reset — after which a live pending request IS a failure and receives that refusal commit.** A request in flight **when Row B itself dies before any commit** is **the N2 residue: invisible, and said to be so** rather than papered over: no clause can make a dead writer log. **There is no `TRANSFER` death rule because there is no `TRANSFER` state**: after the commit the terminal fact is already true and logged, and a delivery failure changes nothing the log claims. **`REFUSED-UNCLASSIFIED` is where undecided permission lands, and the continuous enumeration above — verified at `BS-L` issuance and again at the opening — is what keeps that visible instead of routine.**
  **A tension recorded rather than resolved:** a verifier timeout is **foreseeable**, and routing a foreseeable class into a category defined as a defect-to-be-enumerated is in tension with itself. **The clean answer is probably a named pre-decision state rather than a catch-all entry** — but that is a code, and adding one is close to the instruction that the set not be extended by hand, so it is flagged for the principal and not taken here.
  **Not authorised and not done:** nothing above changes what the access log records beyond the refusal-reason field, and no second custody surface is created. The lifecycle is a constraint on **when Row B decides and logs**, not on **what it writes**.

**THE ACCESS SCHEDULE IS PRECOMMITTED AND χ-BLIND (principal ruling, 2026-08-29 22:49, on converging findings from both seats).** **§2.7(3) constrains the EXCLUSION PREDICATES. It does not constrain the ACCESS SCHEDULE, and the χ-blindness this covenant relied on was inherited from it — an inheritance that does not reach.** GPT56 states the gap exactly: **the universe of eligible objects is χ-blind; the set and sequence actually requested are not.** CODEX states the consequence: ***a sign-blind exclusion rule is not a substitute for a sign-blind access schedule.***
  **What was found, and it was found against this table rather than against a general theory.** A conforming Row D runner may read object 1, compute its χ-derived output inside the sealed store, and choose object 2 over object 3 as its next read on the strength of that output; if the chosen cutout is absent or unreadable, **the access log records the refused object's identity, and that identity reveals which χ-dependent branch was taken.** The same shape reaches Row G with a human: view an allocated cutout, let the visual impression decide which allocated object to request next. **Row G required no fixed traversal, no fixed order and no precommitted schedule, and Row D's stated surface imposed none.**
  **THE RULE, and it FORBIDS rather than observes.** For **every row that may read a χ-bearing object**, the **object set and its complete traversal — order, multiplicity, retries and stopping — are PRECOMMITTED and χ-BLIND**, and **Row B refuses any request that is not the next unserved position in the applicable traversal.** **This is a prohibition on the covenant, not a description of current practice.** Nothing built today is adaptive — the cutout runner has no retry, no re-request and no reordering, and Row G's sequence is constructed by the hand-check design rather than by the checker — **but the covenant PERMITTED adaptivity, and permission is what leaks.** A clause that merely recorded that nobody currently exercises it would leave the channel open to the first implementation that did.
  **The traversal is DERIVED from objects already pinned; it is not a new artifact and creates no new slot.** For Row D it is the accepted sample in canonical `(brickid, objid)` order. For Row G it is the sealed allocation in the order the hand-check presentation design fixes — **that design already builds the sequence**, because its interleaved blind synthetics and its mirrored re-presentations at randomised later positions cannot survive a subject who chooses what to see next. **Multiplicity is part of the traversal**: a position may appear more than once, and it appears where the design puts it, not where a reader asks for it. **Re-viewing the CURRENT object is unrestricted IN SCHEDULE TERMS and logged in CUSTODY terms — the two rules were colliding and the collision dissolves by G5 (GPT56-V69 F2, CODEX-V69 F2; `LIFECYCLE_GUARANTEE_SPEC.md` §5).** A re-render is not a request for a *different* object, so it never violates the traversal — **and every render is its own touch with its own committed event**, which is what Row G's *"any unlogged view"* void clause always required: V69's delivery carve-out was correct for machine conveyance and **over-broad in covering renders**. **G6 — **A view is the display session of one render commit**: it ends at the first of position advance, interface clear, or any interruption of continuous display — visibility loss, blanking, occlusion, navigation away; duration alone does not multiply views, nothing displayed after an interruption is the same view, and commit↔session ownership is one-to-one — each render commit opens at most one session and every session is opened by exactly one commit**
  (CODEX-V72 F3 found the V72 sentence here paraphrasing the boundary in unlabelled prose — it named only two session-enders after the spec gained the interruption clause — which is exactly the checker's stated blind spot; the sentence is now a LABELLED quote the hardened checker binds, and the checker itself is wired into the lint as blocking, per GPT56-V72 F1). Within a session, dwell and magnification of the already-rendered frame move no store bytes and are the same logged view. **And the committed buffer is governed, not a χ-bearing holding surface**: renders get **no buffer reuse** — each re-render re-conveys under its own commit — and a conveyance buffer is destroyed on delivery completion or request end, its bounds a **BS-2k design requirement with fixtures**. **Retries are a fixed per-position attempt limit frozen in this preregistration**, so a transient storage failure is retried the same number of times everywhere and the count reveals nothing; the limit's value is a preregistered parameter fixed at freeze. **Stopping is the traversal being exhausted**; there is no early stop, and `require_complete_sample()`'s refusal of a partial run already says why.
  **THE ONE EXEMPTION — `flag → discard → replace`, AND IT IS RECORDED AS A FINDING, NOT AS A PERMISSION (principal ruling, 2026-08-29 22:49).** HC-1H's predeclared escape hatch lets the checker flag items as **suspected-identifiable** during a session, before key opening; those items are discarded and fresh draws from the same stratum and category are substituted. **That makes the realised set depend on an in-session, content-derived judgement, and it is exempt from the rule above.** **It stays exactly as HC-1H writes it, unmodified.**
  **WHY it does not leak, stated because an unexplained exemption invites a later editor to widen it or delete it, and both would be wrong for reasons nobody could reconstruct.** The principal's finding: **recognising a specific galaxy and judging its handedness are separate judgements, and nothing about handedness is visible in the image.** The flag responds to **identity** cues — *this looks synthetic*, *I have seen this before* — and **no instrument signs are visible to the checker at any point**. **The exemption rests on that finding, from the person who designed the procedure, and not on convenience.**
  **THE DEPENDENCY, written so it can be CHECKED rather than assumed — and written this way because the last dependency of this kind was assumed and the seats found it unpaid.** The exemption holds **only while flagging is uncorrelated with handedness**. **If a different interface, visible orientation cues, or a checker who also sees instrument output ever makes flagging handedness-sensitive, the exemption FAILS and the discard record becomes a χ channel.** **This is a condition to be preserved, not a fact that stays true by itself.**
  **How it is checked:** the exemption is **bound to the pinned digest of the Row G interface specification**, exactly as Row L's signature exemption is bound to canonical body digests rather than to a name. **Any change to that interface — to what the checker can see, to how items are displayed, or to what else the checker holds — changes the digest and LAPSES THE EXEMPTION**, and the hand check may not proceed under it until the finding is re-established by the principal. **An exemption bound to a name would widen with the name; bound to a digest it cannot widen silently.**

(iii) the producer checksum list (§2.5), exclusively for source images; 
(iv) fixtures and their transcripts, synthetic by construction; **(iv-b) the enumeration entries, their continuation segment, and their signed explanation artifacts (CODEX-V70 F3 — the pre-unblinding enumeration verifier must read these, and the closed-list default would have made them χ-bearing and unreadable): entries carry only positions, digests, closed tokens and signatures; explanations are bound by the same principle as refusal reasons — they may describe the request and the authorisation state and NEVER the object, and an explanation describing measured properties is itself a violation to be refused;** 
(v) the authenticated **acceptance-evidence projection** containing **only narrowly enumerated authenticated predicate bits** (e.g., `parent_attempt_present`, `byte_integrity_pass`, `canonical_shape_pass`), each mechanically recomputable by a separately pinned independent verifier. **All cutout digests stay inside the sealed boundary and are never exported.** No execution completion/non-finite status, no caller-authored status, and no free-form identifier may be exported. Every legal value is mechanically fixed. Attempt identity must be derived from a canonical source and serialization. Confidence is explicitly excluded from this projection and deferred to post-unblinding.

**THE STRING RULE IS AN ENUMERATED REGISTRY, NOT A UNIVERSAL SENTENCE (CODEX-V72 F2, GPT56-V72 F3 —
the V72 sentence was universal and the corpus already contained counterexamples: existing non-χ slot
receipts whose schemas constrain names but not value domains, and `explanation_ref` itself, which the
rule's own revision introduced unbounded. A universal claim written in one sitting is the anywhere/
never defect this register keeps cataloguing).** The rule survives as the DEFAULT, enumerated:
**`ref/STRING_FIELD_REGISTRY.md`, generated by `ref/gen_string_field_registry.py` from the schema
blocks themselves AND from frozen v9's `SLOT_SCHEMA`, its receipt ENVELOPE constructor, the enumerator signature, the non-slot artifact classes and **the environment's leaf fields — with the COUNT quoted from `ref/_registry_counts.txt` and from nowhere else: V77 still hand-said "nine" and "145" in this very sentence after declaring the counts generator-owned (GPT56-V77 F11, CODEX-V77 F5)** (V74's 123 omitted the envelope/environment fields v9 wraps every receipt in, the signature itself, and the non-slot classes — GPT56-V74 F1, CODEX-V74 F1; and the signature is constrained to a **deterministic scheme mandated at BS-2k**, because a valid ECDSA signature still carries a nonce — a covert channel wearing a validity proof). **The environment's six leaves are classified honestly — and at V77 the three value-unpinned ones (`python`, `platform`, `machine`) gained a REAL encoding bound, because "bounded-encoding" with no declared bound was a contradiction inside one registry row (GPT56-V76 F1, CODEX-V76 F2): **printable ASCII, ≤ 64 bytes, refused by the successor-layer envelope verifier** — unpinned in VALUE, since any conforming interpreter string passes, and bounded in ENCODING, which is what the column claims. Both halves are now true, and the residual surface (value freedom within the bound) stays named. And the non-slot rows stop being pseudo-fields (GPT56-V75 F2, CODEX-V75 F1): the inventoried classes are field-by-field in the registry itself and the rest are honest `SCHEMA-PENDING` stubs. **The COUNTS are the generator's, quoted from `ref/_registry_counts.txt`, never hand-written — V76 said "nine classes, six pending" and the generator then said ten and seven — a HISTORICAL value; the live counts are whatever `ref/_registry_counts.txt` says now, and GPT56-V81 F8 caught this sentence reading as current one revision after pending moved to eight (GPT56-V76 F3, CODEX-V76 F1), the hand-copied-count drift on the surface built while writing about that drift. The declared CANONICAL BODIES the extraction had missed — freeze-signature body, lock body, opening authorization, entry body, explanation body, provenance record — are registry rows now.** The registry records its generating draft and **the lint blocks when that is not the draft under lint** (CODEX-V75 F3): the first registry
enumerated only the draft-declared schemas and omitted all 86 fields of the EXISTING slot receipts
(GPT56-V73 F2, CODEX-V73 F1), the universal-sentence defect surviving into the enumeration built to
replace it. `BS-1b.provenance`, the free-prose field GPT56 named, is now a digest-ref. Stale
registry rows now EXIT NONZERO (CODEX-V73 F4): a stale row is extractor/schema drift — the signal
that caught the digit-blind bug — and a zero exit made that omission nonblocking** — the generator extracts every field token from the declared field lists, so it
cannot silently omit a field the way a keyword filter omitted Row F; **a field with no registry row
is FORBIDDEN BY DEFAULT and the generator exits nonzero on it.** Each row carries the field's
constraint — `closed-vocab` · `bounded-encoding` · `digest-ref` — and where it is declared.
**`explanation_ref` is repaired to `digest-ref`: it is the sha256 of the canonical explanation body,
not an arbitrary identifier** (GPT56-V72 F3). **Value-domain enforcement for slot receipts is a
successor-layer obligation carried by `receipt_strict()` and the verifiers, since frozen v9 checks
names only** (CODEX-V72 F2); §11 carries the item. **And the honest limit, stated rather than
discovered:** bounded numerics still carry bits — a duration is a number — so the registry bounds
CAPACITY and cannot zero it; what it removes is free prose, which is unbounded capacity plus
deniability.

**Everything else is χ-bearing by default**: any artifact not on this list and not on the permitted surface; every per-object execution measurement receipt wherever it sits; the cutout-completion receipt; any opaque digest of χ-bearing bytes — a digest whose preimage's schema is not on this list or the permitted surface, the acceptance ledger's measurement digest among them, because such a digest is a verification oracle for a guessed outcome; the label-set receipt, which is χ-bearing and remains in the committee store; BS-7f, the post-unblinding adequacy receipt, and BS-V receipts; and any schema that permits outcome payloads. Doubt resolves toward χ-bearing.

**The sealed stores.** The *main sealed store* holds cutouts, instrument outputs, the cutout-completion receipt, and the acceptance ledger. The *committee sealed store* holds the hand-check labels and the label-set receipt. A third χ-bearing store — the predecessor archive — is governed by §6.2's seal-state rule and Row B's enforceable mediation. All three stores are provisioned at **BS-2k** (class-P DESIGN slot). Gates and referees are external witnesses: their inputs are the closed list of non-χ-bearing receipt classes and fixtures only, and no gate input is χ-bearing.

**The phase line.** P0 freeze → P1 BS-6, first image byte → P2 cutout production, pre-inference integrity projection, exact-parent C2 stage-completion, and instrument inference → P3 BS-2f → P4 BS-8f → P5 BS-5f → P6 BS-L, **the primary lock** → P7 unblinding → P8 BS-7f, post-unblinding adequacy receipt, and BS-V → P9 disclosure. 

**THE TABLE.** Each row is one permitted actor or process. Any pre-unblinding touch of a χ-bearing object by any person or process not in this table, or outside a row's stated surface, is forbidden by default.

| # | actor / process — identity | may touch (read → write) | when | authorized by (must exist first) | emits (receipt this act produces) | what voids the run |
|---|---|---|---|---|---|---|
| A | **Custody provisioner** | creates the two new stores' containers and brings the predecessor archive under the mediator; generates, splits and escrows the keys; generates Duho's signing keypair and binds its public half; installs the mediator (row B); records the predecessor archive's identity, its existing holder roster and its seal state by non-content metadata operation → writes the BS-2k design artifacts. **Never reads a χ value**. | P0 | — | BS-2k | any read of archive contents; any key share retained outside the escrow; any store, key or wrapper existing outside the receipt; failure to enforce mediation as a gate condition |
| B | **Store mediator / log writer** | the only path by which any row's stated read or write reaches **any of the three** sealed stores' bytes; conveys bytes strictly as the conduit of another row's stated surface → appends a WRITE-AHEAD ARRIVAL event on receipt of every request, before any processing (principal ruling, 2026-08-30 — the second event class he authorised), and exactly one TOUCH event per touch, success or refusal. **Row B must refuse and log any Row D touch until it verifies an authenticated C2 exact-parent stage-completion artifact.** | from BS-2k's completion through unblinding | BS-2k | the access-log chain; its running checkpoint receipted at BS-2f, the pre-unblinding lock checkpoint receipted at BS-L, and the final post-unblinding checkpoint | any byte delivered outside the requesting row's stated surface; any unlogged touch; a refusal left unlogged; allowing Row D before C2 completion |
| C | **Cutout producer** | reads release image bytes → writes cutouts into the main sealed store, via row B; never reads any sealed object | P1–P2, after BS-6 | BS-6 and BS-9 | **the χ-bearing cutout-completion receipt, appended to the main store** | any cutout or derivative outside the store; any human view of a cutout outside row G's interface |
| C2 | **Cutout integrity verifier** — `verify_cutout_integrity` symbol and digest to be pinned at BS-2a (**DESIGN, defined, UNFILLED**). A hermetic worker, capability allowlist, and blindness fixture are required. | reads **only** cutouts via row B and fixed parent lists. Computes and writes the separate authenticated **acceptance-evidence projection** exporting only authenticated predicate bits (`parent_attempt_present`, `byte_integrity_pass`, `canonical_shape_pass`), and an **exact-parent stage-completion artifact** closing the omission channel. Recomputes all cutout digests inside the sealed boundary; never exports them. | P2, after row C, before row D | BS-2a (design), the cutout-completion receipt | the acceptance-evidence projections, one per parent object, and the stage-completion artifact | executing the classifier; emitting any field outside the schema |
| D | **Instrument runner** | reads cutouts and the cutout-completion receipt (authenticating it against the pinned verifier) → writes per-object χ-bearing measurement receipts (χ, sign, amplitude, confidence) into the store only | P2, after row C2 | BS-3, BS-9, the cutout-completion receipt, and **the authenticated C2 exact-parent stage-completion artifact** | the per-object measurement receipts in the store | any χ-derived value emitted outside the store |
| D2 | **Stratum-index producer** (principal ruling, 2026-08-30 10:46, strata option A — χ-derived strata ACCEPTED; this row is the producer the widened Row F surfaced as missing) | **MAY READ χ**: reads instrument outputs and cutouts via row B, runs the two committee architectures, computes machine-committee state × χ tertile per object → writes the **sealed, pinned, independently verified stratum-index artifact** into the main store, via row B | P2–P3, after row D, before BS-2f | BS-3, BS-9, row D's receipts existing | the χ-bearing stratum-index artifact and its receipt | any stratum output outside the store; any write after BS-2f; **any path by which this artifact reaches `calibration_bins()` — the typed/capability barrier: the artifact is readable by Row F's ALLOCATION constructor only, and BS-2f's boundary verifier recomputes bin boundaries from positions alone and refuses inequality, so a stratum-contaminated boundary cannot verify** |
| E | **Acceptance-ledger recompute** | reads **only the separate authenticated acceptance-evidence projections** in the main store (predicate bits only), the fixed parent lists, and the authenticated catalogue-quality evidence fields (exact authenticated fields `flux_ivar_r`, `psfsize_r`, `nobs_r` from source digest `61214b59d7b35a1e5004a39c6381d08b354ec1f7be6af6b60b23474d02ec28a3`, joined one-to-one on keys `brickid`, `objid`, verified by the BS-2a pinned verifier, failing nonfatally as an ordinary exclusion) — and computes the structural §2.7(2) predicates and catalogue-quality exclusion from it, **excluding instrument absence/non-finiteness and instrument confidence, which remain dropped from the pre-lock structural exclusion**. Does not read the cutout-completion receipt. → atomically writes both the append-only evidence ledger and the realised partition, ensuring the **P3 sealed mask genuinely holds 49,211 rows**. | P2–P3, after complete inference | BS-2a (design), and exactly one verified acceptance-evidence projection per parent object | the realised-partition record (N = 49,211), bound by BS-2f | reading any field outside the evidence schema |
| F | **Calibration-bin sealing** | **for BIN CONSTRUCTION: the accepted partition's positions and acceptance flags only (χ-free)** on the genuinely 49,211-row mask; **for the HAND-CHECK ALLOCATION ONLY: additionally the per-object HC stratum index, WHICH IS χ-BEARING** (widened by principal ruling, 2026-08-29 — see §6.3) → writes sealed boundaries, bin labels, and the hand-check allocation | P3, at BS-2f | BS-8p and the realised partition | the sealed boundary and allocation record | any χ-bearing input to bin construction; **for the allocation: any stratum input OTHER than the verified BS-SI artifact** (void clause amended to the row's real inputs — principal ruling, 2026-08-30, strata option A) |
| G | **Hand-check committee** | views χ-bearing cutouts **of the allocated sample only**, rendered through the sealed interface → each label leaves the member only through that same interface to row H | after BS-8p; complete before BS-8f | BS-8p, the sealed allocation, and the sample's cutouts existing | the member co-signatures carried by the label-set receipt | a member holding any other role; any label, tally, description or impression exported outside the interface; any view outside the allocated sample; any unlogged view |
| H | **Label-ingestion writer** | receives labels from row G through the interface → writes them, as one label set, into the committee sealed store, and writes the **χ-bearing label-set receipt** | with row G, completing before BS-8f | BS-8p | **the χ-bearing label-set receipt** | any write path outside the pinned interface; any intermediate persistence between entry and write; any field beyond the pinned label schema; exporting the receipt's digest |
| I | **Calibration computation** | reads the sealed label set, the corresponding instrument outputs, AND the **χ-bearing label-set receipt**, inside the stores. **Must fail the run before BS-8f if any allocated object lacks a usable finite instrument output.** (Cost: this failure evaluates a pre-lock instrument fact and aborts, leaking that at least one allocated object was missing/non-finite, which we accept as an unavoidable consequence of refusing the pre-lock supervisor.) → writes **only** the BS-8f aggregate fields | P4 | the completed label-set receipt in the store | BS-8f | any per-object label, sign or agreement leaving the stores; any field beyond the BS-8f schema; **failing to abort when an allocated output is missing/non-finite** |
| J | **Stage-C runner** | reads the sealed BS-2f mask (χ-free) and the BS-8f aggregates; injects synthetic signs only — **never reads a real χ**. **Before running Stage C, Row J evaluates the calibration accuracy lower bound `a_LB_b < 0.85` from the BS-8f aggregate (V15 lines 566–567). If `a_LB_b < 0.85`, it emits `INCONCLUSIVE-BY-CALIBRATION` and halts the run pre-unblinding. On PASS, Row J must then verify exactly `N_TRIALS = 1_000` and the frozen Stage-C implementation/protocol digest *before* running or issuing BS-5f.** BS-5f binds that calibration PASS and verification, and certifies **only** the locked pre-attrition BS-2f population and is **insufficient** for a changed final mask. (Post-unblinding attrition requires a separately named post-unblinding adequacy receipt under Row P.) **Any locked Stage-C FAIL emits `INCONCLUSIVE-BY-POWER` and halts the run, explicitly including (a) fewer than 962 of 1,000 passing trials (`../ref/successor_ref_v9.py` lines 77–78) and (b) the self-verification `refuted` or `nonconservative` fail-closed return at reference lines 1275–1277. The complementary PASS branches are the sole route to BS-5f → BS-L.** → writes the Stage-C receipt | P5, before BS-L | BS-2f and BS-8f | BS-5f | reading any real χ; continuing the run after a calibration or Stage-C FAIL; **any deviation from the pinned 1,000-trial protocol or the frozen Stage-C implementation** |
| K | **Key holders** | touch nothing before the lock; custody exists for the lock ceremony and later audit only — **holding a key is custody, never licence** | — | BS-2k | none | any **pre-unblinding** read by any holder |
| L | **Duho** | signs the freeze; designates holders at BS-2k; signs BS-L's canonical lock digest; creates the canonical opening authorization; opens the lock by signature | P0, P6, P7 | for the freeze: every class-P slot receipted and the gates passed; for BS-L: clause 3(a)'s preconditions | the freeze signature; the BS-L detached signature; the opening authorization | any **pre-unblinding** access to a χ-bearing object; opening the lock before a verified BS-L exists; signing anything but the canonical lock digest, **except the two signatures this row itself mandates: the freeze signature (P0) and the canonical opening authorization (P7)**, **each identified by its canonical body digest and not by its name** — see §11's freeze-signature specification — the BS-L detached signature is *over* the canonical lock digest and was never caught by this condition. **No other signature is exempt, and the exemption is by named object rather than by category: an exemption for "signatures generally" would be broad enough to be the hole it closes.** **(Principal ruling 2026-08-29, on CODEX-V24 F1 raised again as CODEX-V49 F1 — twenty-five drafts carried open.) What this does NOT do:** it makes the signing path **executable**, not **verified**. Both seat findings were self-voiding contradictions — the row required acts its own void condition punished — not claims about custody strength. Nothing here establishes that the signatures are sound, only that performing the required ones no longer voids the run. |
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
  **ROW F'S READ SURFACE IS WIDENED TO WHAT ITS EMISSION REQUIRES, AND THE INPUT IS χ-BEARING
  (principal ruling, 2026-08-29).** Row F was stated to read *"positions and acceptance flags only"*
  and to emit a **3 × 9** allocation. **Positions and flags cannot produce a nine-way stratum index**,
  so the row promised an output it had no inputs for — a defect independent of what the strata mean.
  **The direction was to name the input the emission actually needs and not to pick one that keeps the
  row looking clean.** It is the **per-object HC stratum index**, and **both of its axes are
  χ-derived**: the |χ| tertile is the primary instrument's own per-object output, and the
  machine-committee state is the agreement of two classifiers **about handedness**, which this
  document's own rule — *doubt resolves toward χ-bearing* — settles. **So the expected escape, that
  dropping the |χ| axis makes the stratification χ-free, does not exist: there is no χ-free version of
  HC-1H's stratification that keeps its structure.**
  **What widening buys, which is the reason for widening rather than narrowing the emission.** The
  χ-bearing input is now **visible in the row and inside the covenant's scope**, at a moment when it
  can be repaired, instead of arriving at freeze with the quotation. **And Row F's void clause becomes
  load-bearing rather than vacuous**: it voids on *"any χ-bearing input to **bin construction**"*, and
  the row now genuinely holds a χ-bearing input — so the clause states the separation it always
  implied. **The stratum index may reach the allocation and may never reach `calibration_bins()`.**
  **What this does NOT settle, and it is with the principal.** Whether this study's strata should BE
  χ-derived is his decision, not a consequence of this repair. Establishing the cost was mine and it is
  done: **validity survives a redefinition** — `a = Σ w_s·a_s` uses population weights with a **global**
  noise correction, so it estimates the same quantity under any partition, and HC-1H says as much
  itself (*"a bad allocation costs efficiency, never validity"*). **The costs are elsewhere:**
  `N_HC_STRATA = 9` and `HC_MIN_PER_STRATUM = 30` are **frozen constants in `successor_ref_v9.py`**, so
  a different stratum count cannot be expressed without unfreezing; **σ_a would rise, and σ_a is exactly
  what the power floor tests**, so an efficiency cost can still convert a passing gate into
  `INCONCLUSIVE-BY-CALIBRATION` or `INCONCLUSIVE-BY-POWER`; and the natural χ-free substitute axis is
  image quality, which §2.7 measures as **correlated with the axis under test** — coupling the
  calibration to the signal geometry. **`FINDING_ROW_F_STRATA.md` holds the working.**
  **AND THE WIDENING DID ITS JOB IMMEDIATELY: NO COVENANT ROW PRODUCES THE INDEX (GPT56-V67 F6,
  CODEX-V67 F7, both HIGH).** Row D emits only the **primary** instrument's receipts; **nothing in the
  table runs the two committee architectures or writes a canonical stratum-assignment artifact**; and
  the table is exhaustive, so an unnamed producer falls to Row R and is forbidden. **This is the
  dependency surfacing NOW instead of at freeze, which is what the widening was for.** Closing it
  requires a new producer row or an expanded surface on an existing one — **either changes what the
  study permits, so the options and their costs are FILED rather than built**:
  `OPEN_QUESTION_STRATUM_PRODUCER.md`, **coupled to the strata decision**, because what the producer
  computes depends on what the strata are ruled to be. **Until both land, the hand-check allocation
  CANNOT BE CONSTRUCTED — a blocker, not a gap.**
  **AND THE BIN/ALLOCATION SEPARATION IS ENFORCED BY RECOMPUTATION, NOT BY PROMISE.** Both seats
  executed `calibration_bins()` on stratum indices successfully — it accepts any numeric array, and
  frozen v9 cannot gain a type. **A promised separation with no predicate is a name without a
  predicate, one level down in the code.** The predicate: **BS-2f's verifier recomputes the boundaries
  from the full sealed accepted-partition positions — χ-free, already pinned — and refuses unless the
  sealed boundaries EQUAL that recomputation.** Boundaries constructed from an input that CHANGED them differ from the full-set recomputation and
  are refused. **Stated at its true strength (CODEX-V68 F6): this predicate certifies the ARTIFACT —
  that the sealed boundaries are exactly the χ-free artifact — not the PROCESS.** A χ-conditioned
  input that happened to change nothing produces the same boundaries and passes; **what it cannot do
  is move a boundary undetected, which is the only way χ-influence could reach anything downstream of
  the artifact.** Influence that changed nothing remains forbidden by Row F's void clause as a
  conduct matter — witnessed, not verified — **and a product check being unable to prove process
  purity is a limit of product checks, said here rather than discovered again.** **The barrier is
  verification, not typing, because v9 is frozen; §11 carries the build item.**
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
> and a fresh text gate, not a receipt insertion**. On today's count: **BS-2a, BS-2k, `BS-3g`, and the `BS-2v` VOID converter are DESIGN slots.** One of seventeen class-P slots is filled (BS-2m). There are 8 class-E slots. (These class counts are emitted from the table by `tools/prereg_counts.py` and are not to be hand-edited.)

| slot | producer | content | code symbol | blocks |
|---|---|---|---|---|
| BS-1 | Duho | release branch A/B + provenance; branch-invariance evidence | — | everything |
| BS-1b | Hwao | photo-z product paths, columns, join keys, predicate-5 provenance | — | BS-2c |
| BS-2a **DESIGN, CLASS P — UNFILLED** | Hwao | **acceptance design**: the absolute, frozen thresholds (flux_ivar_r > 8.4000532, psfsize_r < 1.5699703, nobs_r >= 3). Gated as text AND code **before any image byte**. **Quality-predicate component gated and pinned 2026-08-28:** `ref/bs2a_quality_gate.py` sha256 `dfbd63d146b472f194f74d01b313874f23c9a4264f26903b22837ae32aa18508` — the predicate, its authenticated evidence schema and its verifier, **CLEAR from GPT56 and CODEX at round 6**, both scoped "CLEAR for FREEZING the quality-predicate component; not a fill authorization". **Recorded limit, which does not transfer as the word "verified":** sound against forgery (neither seat could make it accept a receipt it should reject; one strict single-deletion sweep over the 26 unique checks, all 26 caught by a named control with zero crash-only credits and zero undetected; the 325-case pairwise sweep was **filter-derived from real control outputs, with six pairs literally source-mutated and re-executed** — GPT56 did not run all 325 at round 6, and the row must not read as 325 executed source deletions by both seats; all five frozen constants recomputed without importing the module) but **not hardened against arbitrary hostile input** — four crash sites were repaired across rounds 3–6 and GPT56 found a fifth outside the boundary at round 6. What bounds that: no builder-produced row reached a crash in the 65,060-row type/schema census, and every observed crash exited nonzero. **Consumers must gate on exit status:** a post-verification emit failure can print the true `MATCH` summary and *then* exit 1, so a consumer treating `MATCH` on stdout as success can be misled. **The slot stays UNFILLED:** `verify_cutout_integrity` (Row C2), the confidence threshold, retry and failure semantics, the ledger schema, and §6.3(9)'s adversarial producer fixtures under transformed cutouts are not built, and those fixtures need cutouts, which BS-6 blocks. | `run_production_verdict`, pre-verdict validator | BS-2f, BS-6 |
| BS-2k ⚠ **DESIGN** | Duho | **custody provisioner**: creates stores, escrows keys, installs mediator, records archive seal state | — | BS-6 |
| BS-2v ⚠ **DESIGN, CLASS P — UNRESOLVED** | Hwao | **`VOID` conversion**: handle every enumerated void antecedent. The normative registry in §7.1 must be **pinned by digest in the preregistration itself** (as a `registry_digest` field bound in the slot schema), and the gate must compare the converter's emitted IDs and the exercised fixture IDs **against that pinned digest's contents**, which the converter does not author and cannot alter. Missing, duplicate, extra, or non-`VOID` conversion for any ID fails the gate on mismatch. **The reason previously given here was false and is corrected (principal ruling, 2026-08-29 21:50; GPT56-V53 F2).** It said the registry cannot be pinned before the converter exists. **Both seats cleared that mechanism at the VOID gate round:** §7.1's content comes from this document's own normative clauses, the converter *handles* those IDs rather than authoring them, and digesting the canonical rows while storing the digest in this row creates no fixed point. **A false blocker must not survive into a freeze.** **The slot nonetheless remains UNRESOLVED and UNFILLED**, for the reason CODEX established at that same round: **pinning is necessary, not sufficient** — the converter, the receipt schema, the verifier behaviour and the adversarial fixtures are all undelivered. **Correcting the reason is not progress toward BS-6**, and this row must not be read as such; a stale blocker replaced by a silent one would be worse than leaving it. | `VOID_converter` | BS-6 |
| BS-2c | Hwao + blind double | universe manifest, per-brick counts, zero rows, closure proofs, ceilings, pinned `c_j` bytes | `validate_count_oracle` | BS-2o |
| BS-2o | Hwao + blind double | full traversal order + per-prefix ledger | `greedy_ledger`, `ledger_digest` | BS-5p |
| BS-5p | Hwao | L_min_plan, L_plan, retained basis, x ≥ 962 rule, addresses | `stage_power`, `build_plan` | BS-2s |
| BS-2s | Hwao + blind double | selected set, L_ret, L_raw, N_eq, fixtures, Stage-P re-pass | `local_pass`, `build_plan` | BS-2m |
| BS-2m ✅ **FILLED 2026-08-26** | Hwao | **manifest closure**: required set from the frozen cutout planner, counts, refusal on any difference. Receipt: `gates/FREEZE_CLOSURE_V9_20260826.md` — mechanism frozen at v9 (`successor_ref_v9.py` `6a9abbbd…`, `closure_worker_v9.py` `28f8e1f9…`), 34/34 probes, referee `gates/CLOSURE_V9_KIMI.md` **CLEAR** (one seat; two seats refused by their provider). Derived closure: 65,060 objects → 6,445 selected → **12,117 required bricks**, `plan_digest aaeaa9f3…`, reproduced independently three times. Nine items carried open in the freeze record. | `close_manifest`, `closure_receipt` | manifest freeze |
| BS-3 | Hwao | instrument identity: weights `83008c1c…`, τ = 4.4006456017494235, antisymmetry identity | — | BS-9 |
| BS-SI **DESIGN, CLASS P — UNFILLED** | Row D2 | **the stratum-index artifact's receipt** (principal ruling, 2026-08-30, strata option A): per-object machine-committee state × χ tertile, sealed and pinned, with an **independent verifier** that recomputes the index from row D's receipts and the committee outputs and refuses mismatch. Its schema is written when the slot is filled (the SCHEMA-PENDING discipline); until then **no stratum-index artifact may be emitted, which blocks BS-2f's allocation and BS-8p**. **The typed/capability barrier is this row's load-bearing clause: the artifact is consumable by the allocation constructor ONLY, and the BS-2f boundary verifier's positions-only recomputation refuses any stratum-contaminated boundary.** | `allocate_handcheck` (consumer) | BS-2f (allocation), BS-8p |
| BS-3g **DESIGN, CLASS P — UNFILLED** | Hwao | **sensitivity-gradient control.** Added in V37 under principal authorisation of 2026-08-29 to carry the precondition §1 asserts but no dependency edge enforced. Binds the seven things §1 requires of it *before* BS-6: **statistic, sample, positional stratification, uncertainty, bound, acceptance rule, and failure consequence.** The threat it bounds is a nonzero global offset multiplied by a sky gradient in sensitivity — the one route the antisymmetry identity does **not** close (§1). **What exists:** the estimator and its verifier are built and CLEAR from both seats at gain v6 (`ref/gain_gradient_estimator.py` sha256 `e227029713396a92…`, `gates/verify_mu_gamma.py` sha256 `e33d9275d8078743…`), γ̂ = slope/intercept from a single GLS fit with the delta-method Jacobian, and the vector kernel is frozen in `ref/gain_gradient_kernel.py`. **Why the slot is nonetheless UNFILLED:** the completeness semantics are **settled** — the principal ruled this a real gate on 2026-08-29 and selected the **executable joint counterfactual path**, so holding the observed `p` fixed is rejected and the control is not a stated limitation. `ref/gain_counterfactual_path.py` carries each allowed perturbation through the production permutation record and decision helper, so amplitude and significance move together. **THE MAPPING FAMILY IS RULED AND THE SLOT IS STILL UNFILLED, which is not a contradiction.** The principal ruled on 2026-08-29 (`OPEN_QUESTION_GAIN_SIGN_MAPPING.md`): **option A — position-dependent accuracy `a(c) = a₀ + γ·(c − c̄)` with signs redrawn under it, the same shape production already uses in `inject_signs` — reduced to one verdict by WORST CASE OVER DRAWS.** **What is still missing is the draw set**: A is stochastic, so its counterfactual is a distribution rather than a vector, and **a mapping family is not a preregistered mapping** — the count `n_draws`, the generator and the stopping rule are part of the mapping's identity and are not yet frozen (§11 specifies the four receipt fields that make them checkable). **`mapping_id` therefore stays at the literal `MAPPING-NOT-PREREGISTERED`**, because naming A now would name something that does not yet exist. The module ships no mapping and refuses to run without one. **Option B — the deterministic adversarial flip — is DISCARDED AS THE GATE MAPPING by that ruling, and is NOT retired from the record.** A pre-committed feasibility run (`FEASIBILITY_PRECOMMIT_2_GAIN_OPTION_B.md`, committed blind at `13e48e3c4`, positive control and deletion probe passing before anything was read) found `f*` between **0.000406 and 0.000996 — 20 to 49 flipped signs out of 49,211** overturn the verdict, against a pre-registered threshold of `f* < 0.01`. **The cause is a thin margin, not a quirk of the mapping:** the rejection branch needs `|Â| + 3σ < A_LONGO` and the baseline sits at 0.03531 against 0.0408. **That is one fixture at one calibration**, and the margin depends on `N` and on calibration accuracy, **so the margin must be re-derived at the real calibration before B is discarded in this text on evidence rather than by ruling.** **Stated in advance, so it cannot be chosen afterwards: if the worst case over draws also crosses a verdict boundary at a γ within the bound, that is EVIDENCE ABOUT THE DESIGN — that this margin is too thin at this `N` and calibration for any adversarial-family gate — and it is reported as such. It is not a cue to look for a fourth mapping.** **γ̂ remains unmeasured**, and no measurement of it is authorised here. **This row creates a dependency edge; it does not fill a slot, license an image byte, or assert the control works.** **ONLY `invariance_outcome = HELD` CAN FILL THIS SLOT AND DISCHARGE THE BS-6 EDGE (CODEX-V67 F5, HIGH): a verifier-valid `FAILED` receipt is a TRUE RECORD THAT BLOCKS — it is the pre-stated evidence-about-the-design outcome and goes to the principal — and `NOT-EVALUATED` discharges nothing. A control that failed cannot discharge the gate it exists to guard, and V67 never said so.** | `gain_gradient_estimator`, `verify_mu_gamma` (both built, not bound) | BS-6 |
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

**RESOLVED at V40 by principal ruling of 2026-08-29 (CODEX-V38 F2, HIGH; option C).** §5 line 493 previously stated the VOID trigger for *"permutation/statistic/protocol non-finite/degenerate failures"* with **no phase qualifier**, while these antecedents are scoped `Post-unblinding` — leaving a pre-unblinding permutation failure voided by the prose and matched by no antecedent, reachable because Stage C permutes pre-unblinding on synthetic signs. **The ruling qualified the prose rather than the phases:** the numerical conditions read post-unblinding, and pre-unblinding numerical failures terminate the run through the existing pre-statistic inconclusive codes (`INCONCLUSIVE-BY-POWER`, `INCONCLUSIVE-BY-CALIBRATION`). The V40 rerun allowance was deleted at V43 (option A) and the redundant `INCONCLUSIVE-BY-COMPUTATION` code at V46 (option D); **neither reverses the option C ruling, which the existing routes satisfy.** **The misconduct conditions were deliberately left untouched at `Any`.** **No registry row changed, so `registry_digest` is unmoved** — the prose was brought to the registry, not the registry to the prose.

**WHAT `VOID-5-NONFINITE` AND `VOID-5-DEGENERATE` COVER WAS NARROWED AT V63, and the registry must not be read at its old width.** Their phase cell is unchanged. What changed is §5's partition: post-unblinding, these two antecedents fire on a non-finite or degenerate value **in an object that was pinned, sealed or verified before that point** — a value contradicting what its verification certified — and **not** on a quantity the run computed from admissible inputs, which terminates in `INCONCLUSIVE-BY-NUMERICAL-FAILURE` instead. **This registry carries the IDs and phases; §5 carries what they are about, so a reader who consults only the table will get the width wrong.** The narrowing is a principal ruling (2026-08-29) on GPT56-V54 F1, and it exists because ordering the two clauses left them describing the same events twice.

**Three coverage gaps closed in V37, under principal authorisation of 2026-08-29** (principal decision of 2026-08-29 relayed by Blanc, recorded as `PRINCIPAL-20260829-VOID-OPTION-A` in `gates/FINDINGS_MAP.md`; `DECISIONS_FOR_DUHO.md` is the plain-language index that framed the options and is **not** the record of the ruling — CODEX-V38 F3). §5's prose voids on conditions the registry did not name: a **degenerate** (finite but collapsed) failure, distinct from a non-finite one; and a **digest** deviation, which the registry named only as a *protocol* deviation. Both are now separate antecedents rather than undeclared aliases, because an ambiguity in a registry about to be pinned by digest is itself the defect. §2.7's prose voids on a threshold **chosen or moved**; the ID covered *moved* only and now covers both.

**The §2.7 phase is settled from the authorship record, and the cell is unchanged at `Post-first-real-χ`.** The clause entered at V11 (commit `4d99d1d93`, 2026-08-27), written to answer GPT56 F2 and CODEX 1. **Authorship evidence, stated at its real strength (CODEX-V38 F4):** every commit in this repository carries the principal's git identity, so **commit metadata does not prove which agent wrote the words.** What supports lane authorship is the commit body itself — written in the first person, adjudicating referee findings by name and admitting its own errors (*"KIMI F3, and it was mine"*) — together with its `Co-Authored-By` model trailer. That is strong evidence, **not proof**, and the principal declined the question on the same basis. V11's own §2.7 preamble states what "inference" means: the acceptance freedom is *"the largest remaining researcher degree of freedom **because it is exercised after image inference exists** and it moves both the signs and the geometry."* **"Inference exists" is image inference having produced real output — the first real χ.** The document's ordering confirms real χ exists *before* unblinding, not after: §6's conduct table Row J *"never reads a real χ"* yet can halt the run **pre-unblinding**, and §6's disclosure bullet (*"Nothing derived from any real χ value … before the primary lock"*) forbids pre-lock χ-derived disclosure — both presuppose real χ sitting in the sealed stores pre-lock. (**These citations have now been wrong twice**: V38 named §6.1/§6.2, and V39's repair replaced them with absolute line numbers that were already stale by V40 — GPT56-V40 F6. **Line numbers shift on every revision and must not be used as citations**; both references are now by section and quoted content, which survive renumbering.) `Post-first-real-χ` is therefore **earlier and broader** than `Post-unblinding`, and is the instant the clause names. §6.3's void rule is anchored at the same instant, so the registry and §6.3 agree rather than compete.

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
| `VOID-6.1L-WRONG-SIGNATURE` | §6.1 Row L | P0, P6, P7 | VOID |
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
9. **A correction that is itself unverified is not a correction (found 2026-08-29 — and this one is
   ours, not the predecessor's).** V42 repaired a wrong citation of KIMI by substituting **another
   wrong one**: `KIMI-V11 F4` became `F7`, and F7 is a disclosure finding about the receipt's v7
   subject, while KIMI's F13 states the opposite of the claim it was cited for. **The substitution
   read as a repair, was recorded as one, and survived twelve drafts** until it was caught by hand at
   V54 (GPT56-V54 F4). Every other entry in this register is a defect this text inherited; this one
   the lane committed, and it is here because it is the argument for the mechanical check rather than
   a resolution to be more careful. **Fixed by `tools/citation_block_check.py`**, which verifies a
   repair citation against the cited report's **declared** `FINDINGS-BLOCK` instead of recovering
   findings from prose — the recovery approach failed three adversarial rounds and reported
   `FABRICATED` against real citations, which is worse than not checking. **Its limit is stated
   rather than hidden:** it is wired into the lint as **advisory**, and the legacy corpus predating
   the block returns `NO_BLOCK` — a refusal to decide, deliberately kept distinct from a parse
   failure — under the principal's option-D ruling to verify citations that carry a **repair
   announcement** rather than every mention.

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
| V83 → V84 | `7bc71ce4787f1d81` | `6ec2bc2bdabcd12c` | §11 (+12/−2), §6.1 (+3/−3), (preamble) (+1/−1), §10 (+1/−0) | no row-count change | GPT56-V83-1, CODEX-V83-1, GPT56-V83-2, CODEX-V83-2, GPT56-V83-3, CODEX-V83-3, GPT56-V83-4, CODEX-V83-4, GPT56-V83-5, CODEX-V83-5, GPT56-V83-6, CODEX-V83-6, GPT56-V83-7, CODEX-V83-7 |
| V82 → V83 | `12d54356b4fde6b0` | `7bc71ce4787f1d81` | §11 (+9/−4), §6.1 (+5/−5), (preamble) (+1/−1), §10 (+1/−0) | no row-count change | GPT56-V82-1, CODEX-V82-1, CODEX-V82-2, CODEX-V82-3, CODEX-V82-4, CODEX-V82-5, GPT56-V82-2, GPT56-V82-3, CODEX-V82-6, CODEX-V82-7 |
| V81 → V82 | `aa62779e73f7708f` | `12d54356b4fde6b0` | §11 (+18/−9), §6.1 (+5/−5), (preamble) (+1/−1), §10 (+1/−0) | no row-count change | GPT56-V81-1, CODEX-V81-2, CODEX-V81-3, CODEX-V81-1, GPT56-V81-2, CODEX-V81-4, GPT56-V81-3, GPT56-V81-4, CODEX-V81-5, GPT56-V81-5, GPT56-V81-7, CODEX-V81-7, GPT56-V81-6, GPT56-V81-8, CODEX-V81-8, CODEX-V81-6-FILED |
| V80 → V81 | `a9d5d0a2214fe4b1` | `aa62779e73f7708f` | §11 (+16/−2), §6.1 (+5/−5), (preamble) (+1/−1), §10 (+1/−0) | no row-count change | GPT56-V80-1, CODEX-V80-3, GPT56-V80-2, GPT56-V80-3, GPT56-V80-4, CODEX-V80-1, GPT56-V80-5, CODEX-V80-2, CODEX-V80-4, CODEX-V80-5, CODEX-V80-6 |
| V79 → V80 | `01d3877a2973fff9` | `a9d5d0a2214fe4b1` | §11 (+12/−4), §6.1 (+4/−4), (preamble) (+1/−1), §10 (+1/−0) | no row-count change | GPT56-V79-1, CODEX-V79-1, GPT56-V79-2, CODEX-V79-2, GPT56-V79-3, CODEX-V79-3, GPT56-V79-4, CODEX-V79-4, CODEX-V79-5, CODEX-V79-6, CODEX-V79-7 |
| V78 → V79 | `b4a9c69d9389e662` | `01d3877a2973fff9` | §11 (+11/−3), §6.1 (+4/−4), (preamble) (+1/−1), §10 (+1/−0) | no row-count change | GPT56-V78-1, CODEX-V78-1, CODEX-V78-2, GPT56-V78-2, CODEX-V78-3, GPT56-V78-4, CODEX-V78-5, GPT56-V78-3, CODEX-V78-6, CODEX-V78-4, GPT56-V78-5 |
| V77 → V78 | `d2d61a274c8c0739` | `b4a9c69d9389e662` | §11 (+11/−4), §6.1 (+7/−6), (preamble) (+1/−1), §10 (+1/−0) | no row-count change | GPT56-V77-1, CODEX-V77-2, GPT56-V77-2, CODEX-V77-3, GPT56-V77-3, CODEX-V77-1, GPT56-V77-4, GPT56-V77-5, GPT56-V77-6, GPT56-V77-7, GPT56-V77-8, GPT56-V77-9, CODEX-V77-4, GPT56-V77-10, GPT56-V77-11, CODEX-V77-5 |
| V76 → V77 | `2aa58d40bfedfc70` | `d2d61a274c8c0739` | §11 (+7/−3), §6.1 (+2/−2), (preamble) (+1/−1), §10 (+1/−0) | no row-count change | GPT56-V76-1, CODEX-V76-2, GPT56-V76-3, CODEX-V76-1, GPT56-V76-2, GPT56-V76-4, CODEX-V76-3 |
| V75 → V76 | `781b7f3f065ff20d` | `2aa58d40bfedfc70` | §11 (+8/−3), §6.1 (+4/−4), (preamble) (+1/−1), §10 (+1/−0) | no row-count change | GPT56-V75-1, CODEX-V75-2, GPT56-V75-2, CODEX-V75-1, GPT56-V75-3, CODEX-V75-4, CODEX-V75-5, CODEX-V75-3, GPT56-V75-4, CODEX-V75-6 |
| V74 → V75 | `d229952d5046e9cc` | `781b7f3f065ff20d` | §11 (+9/−5), §6.1 (+4/−4), (preamble) (+1/−1), §10 (+1/−0) | no row-count change | GPT56-V74-1, CODEX-V74-1, GPT56-V74-2, CODEX-V74-4, GPT56-V74-3, CODEX-V74-2, CODEX-V74-3, GPT56-V74-4, CODEX-V74-5 |
| V73 → V74 | `d48c3000aa50d804` | `d229952d5046e9cc` | §6.1 (+7/−2), §11 (+6/−3), (preamble) (+1/−1), §10 (+1/−0) | no row-count change | GPT56-V73-2, CODEX-V73-1, CODEX-V73-4, GPT56-V73-3, CODEX-V73-2, CODEX-V73-5, GPT56-V73-4, CODEX-V73-6, GPT56-V73-1, CODEX-V73-7, CODEX-V73-3 |
| V72 → V73 | `66fcc42c6de59cfd` | `d48c3000aa50d804` | §11 (+34/−13), §6.1 (+23/−16), (preamble) (+1/−1), §10 (+1/−0) | no row-count change | GPT56-V72-1, GPT56-V72-2, CODEX-V72-3, CODEX-V72-2, GPT56-V72-3, CODEX-V72-1, FIVE-ROUND-FREEZE, CODEX-V72-7, GPT56-V72-4, CODEX-V72-4, GPT56-V72-5, CODEX-V72-6, CODEX-V72-8 |
| V71 → V72 | `7a8e7151e4063e5e` | `66fcc42c6de59cfd` | §6.1 (+25/−10), §11 (+24/−7), (preamble) (+1/−1), §10 (+1/−0) | no row-count change | GPT56-V71-1, CODEX-V71-1, GPT56-V71-2, GPT56-V71-3, CODEX-V71-2, GPT56-V71-4, CODEX-V71-4, GPT56-V71-5, CODEX-V71-3, GPT56-V71-6, CODEX-V71-5, CODEX-V71-6, GPT56-V71-7 |
| V70 → V71 | `a1deae2e44b51a73` | `7a8e7151e4063e5e` | §11 (+34/−9), §6.1 (+6/−6), (preamble) (+1/−1), §10 (+1/−0) | no row-count change | GPT56-V70-1, CODEX-V70-1, CODEX-V70-2, GPT56-V70-2, CODEX-V70-4, CODEX-V70-3, GPT56-V70-3, CODEX-V70-5, CODEX-V70-6, GPT56-V70-5, CODEX-V70-7, CODEX-V70-8, GPT56-V70-4 |
| V69 → V70 | `d52844620fbda2e5` | `a1deae2e44b51a73` | §11 (+25/−2), §6.1 (+7/−4), (preamble) (+1/−1), §10 (+1/−0) | no row-count change | THREE-FAILURE-THRESHOLD (LIFECYCLE_GUARANTEE_SPEC.md written; draft derived from it), GPT56-V69-1, CODEX-V69-1, GPT56-V69-2, CODEX-V69-2, GPT56-V69-3, CODEX-V69-4, GPT56-V69-4, CODEX-V69-3, GPT56-V69-5, CODEX-V69-5, GPT56-V69-6, CODEX-V69-6, CODEX-V69-7 |
| V68 → V69 | `010f5ece044e67a1` | `d52844620fbda2e5` | §11 (+30/−4), §6.1 (+20/−10), §6.3 (+9/−4), (preamble) (+1/−1), §5 (+1/−1), §10 (+1/−0) | no row-count change | GPT56-V68-1, CODEX-V68-1, GPT56-V68-2, CODEX-V68-2, GPT56-V68-3, CODEX-V68-4, GPT56-V68-4, GPT56-V68-5, CODEX-V68-3, CODEX-V68-5, CODEX-V68-6, CODEX-V68-7, CODEX-V68-8 |
| V67 → V68 | `3dbf4af7fab34e1f` | `010f5ece044e67a1` | §6.1 (+11/−8), §6.3 (+19/−0), §11 (+14/−5), (preamble) (+1/−1), §7 (+1/−1), §10 (+1/−0) | no row-count change | GPT56-V67-1, CODEX-V67-1, GPT56-V67-2, CODEX-V67-2, GPT56-V67-3, CODEX-V67-3, GPT56-V67-4, CODEX-V67-4, GPT56-V67-5, CODEX-V67-6, CODEX-V67-5, GPT56-V67-6, CODEX-V67-7, GPT56-V67-7, CODEX-V67-8 |
| V66 → V67 | `92b589e635228be8` | `3dbf4af7fab34e1f` | §6.3 (+28/−0), §6.1 (+14/−5), §11 (+4/−1), (preamble) (+1/−1), §5 (+1/−1), §10 (+1/−0) | no row-count change | GPT56-V66-2, CODEX-V66-1, CODEX-V66-2, GPT56-V66-3, CODEX-V66-3, CODEX-V66-4, GPT56-V66-4, CODEX-V66-5, GPT56-V66-5, CODEX-V66-6, PRINCIPAL-20260829-ROWF-WIDEN |
| V65 → V66 | `29dd690d356effaf` | `92b589e635228be8` | §6.1 (+12/−3), §11 (+14/−2), §10 (+1/−0) | no row-count change | GPT56-V64-1, CODEX-V64-1, GPT56-V64-2, CODEX-V64-3, GPT56-V64-3, CODEX-V64-5, CODEX-V64-4, GPT56-V64-4, CODEX-V64-6, GPT56-V64-5, CODEX-V64-7 |
| V64 → V65 | `af171440cd2d31c6` | `29dd690d356effaf` | §6.1 (+9/−0), (preamble) (+1/−1), §10 (+1/−0) | no row-count change | PRINCIPAL-20260829-CHI-BLIND-ACCESS-SCHEDULE, PRINCIPAL-20260829-FLAG-RULE-NO-CONNECTION |
| V63 → V64 | `8b224c684ea4cdf0` | `af171440cd2d31c6` | §11 (+36/−5), §6.1 (+22/−8), §5 (+9/−1), (preamble) (+1/−1), §10 (+1/−0) | no row-count change | PRINCIPAL-20260829-CATCHALL-NON-CLOSURE, CODEX-VOCAB-1, GPT56-VOCAB-1, GPT56-V63-2, GPT56-V63-4, GPT56-V63-5, CODEX-V63-2, CODEX-V63-3, CODEX-V63-4 |
| V62 → V63 | `70c0bcfa95dbec37` | `8b224c684ea4cdf0` | §11 (+31/−4), §5 (+17/−13), §8 (+15/−0), (preamble) (+1/−1), §7 (+1/−1), §7.1 (+2/−0), §10 (+1/−0) | no row-count change | PRINCIPAL-20260829-UNREACHABLE-DROP-BASIS-I, PRINCIPAL-20260829-VOID-PARTITION, PRINCIPAL-20260829-PLANNING-NOT-AN-OUTCOME, PRINCIPAL-20260829-WITHDRAWAL-ON-RULE, PRINCIPAL-20260829-GAIN-MAPPING-OPTION-A-WORST-CASE, HWAO-REGISTER-CITATION-CHAIN |
| V61 → V62 | `e2941fa2d1cdc042` | `70c0bcfa95dbec37` | (preamble) (+1/−1), §5 (+1/−1), §6.1 (+1/−1), §11 (+1/−1), §10 (+1/−0) | no row-count change | GPT56-V59-1, CODEX-V59-2, GPT56-V59-5, CODEX-V59-4, GPT56-V59-7, CODEX-V59-5 |
| V60 → V61 | `8d434674f61b3046` | `e2941fa2d1cdc042` | §6.1 (+1/−1), §7 (+1/−1), §7.1 (+1/−1), §11 (+9/−1), §10 (+1/−0) | no row-count change | PRINCIPAL-20260829-ROWL-PHASES, PRINCIPAL-20260829-FREEZE-SIG-BODY, PRINCIPAL-20260829-BS2V-REASON |
| V59 → V60 | `9257411511b39de6` | `8d434674f61b3046` | §11 (+6/−2), §10 (+1/−0) | no row-count change | GPT56-V59-3, CODEX-V59-3 |
| V58 → V59 | `4df6afe904688940` | `9257411511b39de6` | §11 (+22/−1), §10 (+1/−0) | no row-count change | CODEX-V56-2 half two |
| V57 → V58 | `a2c48d0cfe7511b6` | `4df6afe904688940` | §11 (+18/−4), §10 (+1/−0) | no row-count change | PRINCIPAL-20260829-BS3G-SCHEMA |
| V56 → V57 | `c0743b40698e75b6` | `a2c48d0cfe7511b6` | §6.1 (+5/−3), §5 (+1/−1), §10 (+1/−0) | no row-count change | PRINCIPAL-20260829-REDO-DERIVATION, GPT56-V56-4/5, CODEX-V56-5/6 |
| V55 → V56 | `8e5c193c6b9c4032` | `c0743b40698e75b6` | §6.1 (+7/−1), §10 (+1/−0) | no row-count change | PRINCIPAL-20260829-REFUSAL-VOCABULARY-OPTION-A |
| V54 → V55 | `b0ccbecc46e21677` | `8e5c193c6b9c4032` | §2.6 (+1/−1), §5 (+1/−1), §10 (+1/−0) | no row-count change | GPT56-V54-4, CODEX-V54-2, GPT56-V54-5 |
| V53 → V54 | `cc4e289578b129e4` | `b0ccbecc46e21677` | §5 (+6/−4), §11 (+1/−1), §10 (+1/−0) | no row-count change | GPT56-V53-1, CODEX-V53-1, CODEX-V53-2, GPT56-V53-3, CODEX-V53-3 |
| V52 → V53 | `a825e5d2045721c4` | `cc4e289578b129e4` | §5 (+4/−3), preamble (+1/−1), §10 (+1/−0) | no row-count change | GPT56-V52-1, CODEX-V52-1, GPT56-V52-2, CODEX-V52-2, CODEX-V52-5 |
| V51 → V52 | `e007e9cb940de135` | `a825e5d2045721c4` | §5 (+2/−1), §6.1 (+1/−1), §10 (+1/−0) | no row-count change | PRINCIPAL-20260829-ROWL-QUALIFY, PRINCIPAL-20260829-THIRD-STATUS |
| V50 → V51 | `e3d0d65cca545040` | `e007e9cb940de135` | §1 (+1/−1), §2.1 (+1/−1), §10 (+1/−0) | no row-count change | GPT56-V49-6, GPT56-V49-7 |
| V49 → V50 | `d8a9501e0653dd84` | `e3d0d65cca545040` | §5 (+5/−3), §11 (+1/−1), §10 (+1/−0) | no row-count change | GPT56-V49-2, GPT56-V49-3, GPT56-V49-4, CODEX-V49-2, CODEX-V49-3 |
| V48 → V49 | `8d2e68f7f52db126` | `d8a9501e0653dd84` | §5 (+7/−0), §11 (+1/−1), §10 (+1/−0) | no row-count change | PRINCIPAL-20260829-NUMERICAL-OPTION-B-RERULED |
| V47 → V48 | `bc0fd1f0aa9537f2` | `8d2e68f7f52db126` | §11 (+1/−0), §10 (+1/−0) | no row-count change | GPT56-V46-1 partial (exception-to-outcome conversion) |
| V46 → V47 | `c5afba31f909dcda` | `bc0fd1f0aa9537f2` | §5 (+4/−3), §10 (+1/−0) | no row-count change | GPT56-V46-1, CODEX-V46-1, GPT56-V46-2, CODEX-V46-2 (completeness argument retracted) |
| V45 → V46 | `4fcc9c3460abfe2d` | `c5afba31f909dcda` | §5 (+3/−2), §7.1 (+1/−1), §11 (+0/−1), §10 (+1/−0) | no row-count change | PRINCIPAL-20260829-COMPUTATION-OPTION-D |
| V44 → V45 | `4faa2564ba093ae4` | `4fcc9c3460abfe2d` | §11 (+1/−1), §10 (+1/−0) | no row-count change | GPT56-V44-2, CODEX-V44-2 |
| V43 → V44 | `7b2e9a701c38c570` | `4faa2564ba093ae4` | §5 (+2/−2), §7 (+1/−1), §10 (+1/−1), §11 (+1/−0) | no row-count change | GPT56-V43-1, CODEX-V43-1, GPT56-V43-2, CODEX-V43-2, GPT56-V43-3 |
| V42 → V43 | `6c9cc2fca67d5aff` | `7b2e9a701c38c570` | §5 (+2/−6), §7.1 (+1/−1), §10 (+1/−0) | no row-count change | PRINCIPAL-20260829-RERUN-OPTION-A (the rerun allowance deleted; the halt is terminal), GPT56-V40-5 (calibration/computation overlap) |
| V41 → V42 | `5270452ff9a54caf` | `6c9cc2fca67d5aff` | §2 (+1/−1), §10 (+1/−0) | no row-count change | HWAO-HANDCHECK-20260829 (a miscited seat finding, found by hand-verifying the pre-format prose citations) |
| V40 → V41 | `531d3f40f06130e7` | `5270452ff9a54caf` | §6.1 (+1/−1), §7.1 (+1/−1), §11 (+1/−0), §10 (+1/−0) | no row-count change | GPT56-V40-4, CODEX-V40-4, GPT56-V40-6 |
| V39 → V40 | `221c6a08cd794e5b` | `531d3f40f06130e7` | §5 (+9/−1), §7.1 (+1/−1), §10 (+1/−0) | no row-count change | PRINCIPAL-20260829-VOID5-OPTION-C |
| V38 → V39 | `b5776d287a22cff7` | `221c6a08cd794e5b` | §7 (+1/−1), §7.1 (+3/−2), §10 (+1/−0) | no row-count change | GPT56-V38-1, CODEX-V38-1, CODEX-V38-3, CODEX-V38-4 |
| V37 → V38 | `62dd8a7525c39912` | `b5776d287a22cff7` | §5 (+1/−1), §7.1 (+2/−1), §10 (+1/−0) | no row-count change | PRINCIPAL-20260829-2.7-REFUSED-AS-PUT, PRINCIPAL-20260829-AUTH-DEPRIORITISED |
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

- **Exception-to-outcome conversion (the class rule's implementation):** Classify **every failure path** in the pinned reference by §5's boundary test — **not merely every `raise` statement (CODEX-V49 F2)**. A `raise` is where a failure surfaces, not where it is necessarily decided: a helper may raise on behalf of its caller, and the same condition may reach different callers with different admissibility contracts, so the classification attaches to the **path** and must be recorded per call site rather than per raise — *could it fire while every argument satisfies the contract and the data is admissible?* — and record the verdict per site. Every site answering yes must convert to exactly one named outcome, defaulting to `INCONCLUSIVE-BY-NUMERICAL-FAILURE` where no specific code claims it. **The classification is per-site and must be read, not pattern-matched**. **Every one of the 112 nodes is classified in `ref/RAISE_SITE_CLASSIFICATION.md`; no site is unread and the earlier range is withdrawn** (GPT56-V53 F3, CODEX-V53 F3 — §11 carried the 48-unread status after §5 had superseded it). Specify and implement the conversion from a **raised exception in the pinned reference** to a **named outcome**. The pinned `successor_ref_v9.py` carries **112 `Raise` nodes counted by AST** — 68 `RuntimeError`, **39 `ManifestClosureError`**, 2 `InconclusiveByPower`, 1 `ValueError`, 1 `InconclusiveByCalibration`, 1 bare re-raise. **Only 3 raise a typed outcome exception**; the rest raise errors no outcome claims. **A `grep` keyed on `RuntimeError|ValueError` misses the 39 `ManifestClosureError` sites — a third of the total — which is how the earlier 111 figure arose.** **A named outcome nothing can produce is not a route.** Each raise site must be classified as either (i) an inadmissible-input guard, which is a caller error and needs no run outcome, or (ii) a reachable run-time failure, which must convert to exactly one named outcome. **The classification is per-site and must be read, not pattern-matched** — a keyword pass over the row prose cannot see these, because the failure modes live in the code and not in the text. **This item does not decide which outcome any branch receives**; it requires that every reachable failure have one.
- **Aggregate validation:** Implement `validate_calibration_aggregates` to validate calibration aggregates as finite and non-degenerate (excluding the Row-I missing-output case) before the `< 0.85` comparison, and emit the authenticated outcome. Add its fixture.
- **Post-unblinding adequacy validator:** Implement a named validator that authenticates the adequacy receipt, independently recomputes the exact-parent terminal partition and final-mask digest from pinned evidence, checks exact binding to the mask passed to the runner, and refuses before `perm_record()` on every non-passing adequacy branch. Add positive and negative fixtures, including an `INCONCLUSIVE` receipt that proves no statistic call occurs.
- **Receipt construction is bound to a strict constructor, and unknown slots are refused (CODEX-V56 F2 half two).** `receipt()` in the pinned reference enforces exact fields **only** when the slot is in `SLOT_SCHEMA`; an unknown slot receives a canonical-looking envelope over arbitrary fields. Executed against the pinned bytes, `{'per_object_chi': b'+1'}` is **ACCEPTED** for every absent slot. **Five are absent: BS-3g (until its entry lands), BS-2a, BS-2k, BS-L and BS-2v.**
  **The binding, which is what closes it — the wrapper alone does not.** Implement `receipt_strict(slot, fields)` in the successor layer: it refuses any slot absent from the pinned `SLOT_SCHEMA` before delegating, and **v9 is not modified** (`6a9abbbd…` stands). **Every producer of a SLOT RECEIPT — that is, of an artefact whose slot appears in `SLOT_SCHEMA` — must construct it through `receipt_strict()` and through nothing else.** **Scoped at V62 (CODEX-V59 F2, GPT56-V59 F1, both HIGH), because the V59 wording said *every producer named in §6.1 and §7* and was unsatisfiable.** Seven rows emit artefacts that are not slot receipts at all — Row B's access-log chain, Row C's cutout-completion receipt, Row C2's acceptance-evidence projections, Row H's label-set receipt, Row O's unblinding receipt, Row P's adequacy receipt, Row Q's archive seal-state receipt — and `receipt_strict()` refuses unknown slots **by design**, so routing a non-slot artefact through it would refuse it by construction. **V59's own STOP condition fired on this, and it was the wording rather than an unbindable producer: no slot-receipt producer has been found that cannot be redirected, so this is not a path back to unfreezing v9, which stays at `6a9abbbd`.** The seven non-slot classes keep the authenticated schemas §6.1 already assigns them; **what is forbidden is emitting a slot receipt outside the strict constructor.** **BS-7p, which is in `SLOT_SCHEMA` and still named the permissive `receipt()`, is bound by this clause.** A wrapper protects only its callers, so an unbound producer leaves the permissive path reachable — the binding is the repair, the wrapper is only its mechanism.
  **And a verifier that makes a permissive-path receipt detectable after the fact**, not merely discouraged: a separately pinned checker that refuses any receipt whose `slot` is absent from the pinned `SLOT_SCHEMA`, and whose field set differs from that slot's entry in either direction. **Without it, a receipt built by calling `v9.receipt()` directly is indistinguishable from a conforming one** — the envelope is canonical either way.
  **Until an absent slot has a `SLOT_SCHEMA` entry, NO receipt may be emitted for it.** That makes each missing entry a **blocker on filling that slot** rather than a silent hole, and it is why the four remaining entries are not specified here: BS-2a is DESIGN/UNFILLED, BS-2v is UNRESOLVED, and **specifying a field set for a slot whose content is undecided would pin the wrong thing.** Each entry is written as part of filling its slot, under the same two constraints BS-3g met — types an independent implementer can verify against, and a demonstration that no field can carry a per-object quantity.
  **If any producer cannot be routed through the strict constructor, that is a STOP**: it would mean the permissive path is reachable by a route the document cannot bind, and only the frozen reference could close it. **That is the one path back to the unfreeze question and it is the principal's.**
- **Canonical freeze-signature body and verifier — SPECIFIED (principal ruling, 2026-08-29 21:50; CODEX-V53 F4).** V52 exempted *"the freeze signature"* from Row L's wrong-signature VOID condition by **name**, and there was no canonical freeze-signature body, field set or verifier saying which signed bytes qualify — so the exemption covered whatever a signer chose to call by that name.
  **The lesson, because it applies to every by-name exemption in this document:** I wrote that exemption narrow on purpose, on the ground that *"an exemption for signatures generally would be broad enough to be the hole it closes."* **The breadth arrived anyway, through the definition rather than through the category.** **Naming an object is not narrowing when the object has no canonical form** — a by-name exemption is only as narrow as the definition of the thing it names, and if that definition is absent the exemption is unbounded however specific the name looks.
  **The canonical freeze-signature body** is the concatenation, in this order, of: the §0 pinned code digest; the `PINNED_PARENT_SHA256`; the `PINNED_SELECTION_BRICKS` count; the §7 class counts as emitted by `tools/prereg_counts.py`; and the draft's own sha256. Its **body digest** is the SHA-256 of that concatenation under the same canonical field encoding BS-L's lock body uses.
  **The exemption attaches to that digest, not to the name.** A signature over the canonical freeze body is exempt; a signature over anything else is not, whatever it is called. **Verifier:** a separately pinned checker that recomputes the body from the five pinned components, refuses unless the signed digest equals the recomputed one, and refuses any signature claiming freeze exemption whose subject is not that digest.
  **What this does NOT undo:** the self-voiding contradiction closed at V52 is genuinely closed — the row no longer punishes the acts it mandates. **What was open is that one of the two exempted acts was under-specified, and that is what this closes.** And the phase widening at V61 (`P0, P6, P7`) **does not re-catch the exempt signatures**: the exemption is by body digest and holds at every phase, so widening changes only *when the condition is live*, never *what it catches*. **A wrong signature at P0 or P7 still voids the run** — only the two canonical bodies are exempt.
  **Why P7-only was wrong, not merely changed:** after the exemption, P7 was the phase at which **nothing the condition could catch remained** — a guard registered exactly where it had nothing to guard, while signing at P0 and P6 went unwatched. **That is the same shape as the outcome deleted this afternoon for being unreachable**, and CODEX has now found two phase defects in this row family; a third is likelier than not.
- **`BS-3g` sensitivity-gradient receipt — SPECIFIED (principal instruction, 2026-08-29 20:35).**
  **`SLOT_SCHEMA['BS-3g']` is exactly these twenty fields, no more and no fewer:**
  `mask_sha256` · `calibration_sha256` · `perturbation_manifest_sha256` · `kernel_sha256` ·
  `estimator_sha256` · `verifier_sha256` · `mapping_id` · `gamma_hat` · `sigma_gamma` ·
  `gamma_bound` · `invariance_outcome` · `n_perturbations` · `n_draws` · `draw_generator_id` ·
  `draw_master_seed` · `draw_verdict_digest` · `baseline_verdict` · `delta_gamma_max` ·
  `counterfactual_path_sha256` ·
  `replay_harness_sha256`.
  **WHERE THIS ENTRY LIVES, because "specified" and "pinned" are not the same and a seat read the gap correctly (GPT56-V63 F4, HIGH).** `successor_ref_v9.py` is **FROZEN**, its `SLOT_SCHEMA` does not contain `BS-3g`, and it **cannot gain one** — so `v9.receipt()` enforces no field set for this slot and would accept arbitrary fields. **That is not repaired by adding the entry to v9; it is repaired by the binding.** This entry is `SLOT_SCHEMA['BS-3g']` **in the successor layer's pinned schema**, the one `receipt_strict()` reads, and **BS-3g's producer is bound to `receipt_strict()` and to nothing else** under the V62 clause. **A BS-3g receipt emitted through `v9.receipt()` is a protocol deviation and voids the run**, and until the successor-layer entry is pinned **no BS-3g receipt may be emitted at all** — the same fill-blocker rule the four deliberately-absent slots carry. **Specification is not enforcement, and the sentence above is the specification; the binding is the enforcement.**
  **✅ THE DRAW DISCIPLINE IS UNFROZEN (principal's BS-3g sitting, 2026-08-30 10:46 — every defining parameter is now ruled or committed, so the five-round freeze's structural reason is gone and the patch loop may resume against a complete spec):** `n_draws = 99` (ruled — the 99th-percentile worst case); **draw variates COMMON RANDOM** (ruled — one stream per draw across every γ, so a flip is the gradient's doing; the built assumption is now preregistered); **the bound is an A-PRIORI FROZEN RANGE, not measurement-derived** (ruled — five rounds of self-declared-bound findings close; `k_γ` is MOOT under this shape; the endpoints ±0.25 are PROPOSED from the instrument's preregistered calibration constraints in `PROPOSAL_GAMMA_RANGE.md` and await ratification — the one item still open); **seed, generator and Δγ are COMMITTED in `ref/DRAW_MECHANICS_COMMIT_20260830.md` before any verdict is seen** (delegated; master seed 20260830 by calendar, generator the frozen environment's own PCG64, Δγ = 0.01). **The freeze banner below is kept as history:** The reason is structural, not carelessness to be patched
  harder: **the object's defining parameters are AWAITING THE PRINCIPAL** — `n_draws`, the master
  seed, the generator, `Δγ`, `k_γ`, the bound's shape, and what "the same draw" MEANS across γ are
  all in his file, and text built over an unruled spec keeps failing in the direction of whichever
  assumption it silently made. **Until the BS-3g sitting lands: the draw-discipline text is repaired
  only where a fix is RE-DERIVABLE from rules already in force (consistency drift, conformance
  logic); design findings against it are RECORDED, not patched; and it is EXCLUDED from referee
  briefs' attack surface with this paragraph as the stated reason.** BS-3g emission was already
  blocked on the unset parameters; this banner adds nothing to what is blocked and only stops the
  patch loop.
  **The last four are the DRAW SET, added at V63 under the principal's ruling of 2026-08-29** —
  option **A** (position-dependent accuracy, signs redrawn) with **worst case over draws** as the
  reduction policy — and under the first condition he attached to it: **the draw set must be defined
  before the worst case is, and it must be checkable.** Mapping A is stochastic, so the
  counterfactual is a **distribution** over sign vectors rather than a vector, and **the worst case
  over draws is monotone in the number of draws**: with an unfixed count the gate deepens the longer
  it runs and becomes a function of how long it ran rather than of the design. **Fixing the draw set
  is therefore part of fixing the gate's strictness, not a parameter beneath it.** Every field is an
  aggregate over the run; **none is per-object**, which the class-P contract forbids.
  **The first three were added at V60 (GPT56-V59 F3, CODEX-V59 F3, both HIGH).** The nine-field
  version bound the *code* the control ran and said nothing about the *data* it ran on, so **a
  conforming receipt could certify a different sample, or a favourable subset, and be
  indistinguishable from one covering the whole mask.** Binding the code and not the input is a
  schema that authenticates the instrument and not the measurement.
  **Field definitions, written so a verifier can be implemented by someone who did not write this
  schema.** `mask_sha256` — 64-character lowercase hex, the digest of the sealed mask the control
  was evaluated on, **which must equal the `mask_digest` pinned by BS-2f**. A subset of the mask
  has a different digest, so **a receipt cannot certify a favourable subset while claiming the
  sample** — the equality is the binding, not the field's presence. `calibration_sha256` — the
  digest of the calibration actually used (`a_b`, `a_lb_b`, `cov_a` in canonical order). It is
  bound because **the invariance margin depends on the calibration**: the option-B retry showed
  the rejection branch sitting at `|Â|+3σ = 0.0353` against `A_LONGO = 0.0408`, a margin of
  0.0055, so a receipt that does not say which calibration produced it cannot be checked against
  the bound it claims. `perturbation_manifest_sha256` — the digest of the canonical, ordered list
  of γ values evaluated, **serialized as ascending decimal ASCII, shortest round-trip representation,
  one value per line, `\n`-separated, no trailing separator, UTF-8 — a digest over an unstated byte
  serialization was not reproducible by an independent implementer (GPT56-V77 F10)**; **this is what makes `n_perturbations` checkable rather than asserted**,
  since a count alone cannot distinguish a full sweep from a favourable handful. `replay_harness_sha256` — **the digest of the replay harness that carries every no-caller/type-exact/compile-from-buffer/flags/load-census obligation this section states: an unpinned harness was the one executable left outside the receipt, so the repairs lived in a file nothing named (CODEX-V81 F1); the verifier refuses a receipt whose harness digest differs from the frozen expected value — **and that value is a LITERAL this document cannot carry yet, because the artifact it digests does not exist (GPT56/CODEX-V83 F1): the harness is `gates/replay_harness.py`, a REQUIRED build item in §11's inventory, and its expected digest is a class-P value SET WHEN THE ARTIFACT IS BUILT and frozen at freeze — UNSET now, one more named blocker on BS-3g emission, exactly like `n_draws`. A pin without an artifact was a name; a named artifact with an unset pin is a blocker, which is the honest state** (CODEX-V82 F2's regress answer stands: the freeze is where the pin's authority stops). Clause (a) recomputes all FIVE module digests — the harness joined the four and the clause said four for one revision.**
  **THE MANIFEST MUST SPAN THE BOUND, because digesting a list does not make the list adequate
  (CODEX-V64 F4, HIGH).** A manifest containing the single value `γ = 0` satisfied every check V64
  stated — it is canonical, it is ordered, its digest recomputes, and `n_perturbations` equals its
  length — **while evaluating no perturbation at all and reporting `HELD`.** The digest bound the
  manifest to the receipt and nothing bound the manifest to the question. **The manifest must contain
  both endpoints `−gamma_bound` and `+gamma_bound` and at least three distinct values**, and the
  verifier **refuses any manifest whose largest `|γ|` is less than `gamma_bound`, **refuses any point with
  `|γ| > gamma_bound`** — a conforming manifest could otherwise carry out-of-bound points and report
  a failure the allowed range never produced (CODEX-V70 F8) — and refuses the
  singleton `{0}` by name; refuses any manifest not containing BOTH endpoints `−gamma_bound` and
  `+gamma_bound`; refuses fewer than three distinct values; refuses any adjacent gap exceeding the
  frozen `Δγ`; and refuses any receipt whose `delta_gamma_max` differs from the frozen class-P
  value** — every constraint the prose states, restated as a refusal the verifier executes. **An invariance test that never perturbs anything is not a weak test; it
  is not a test.**
  **AND SPANNING IS NOT RESOLVING — the honest limit, stated rather than engineered away (GPT56-V66 F4, CODEX-V66 F5, both HIGH).** A three-value manifest containing both endpoints **can step over an interior γ at which the verdict flips** and report `HELD`. **No finite manifest can prove that no interior flip exists**, and pretending otherwise by adding points would be the same claim with a bigger number behind it.
  **What the test therefore establishes, said exactly.** **A flip found anywhere is DECISIVE**: it demonstrates the verdict is not invariant under an allowed gradient, and `invariance_outcome` is `FAILED`. **`HELD` means only that no flip was found ON THE EVALUATED GRID** — it is bounded by the grid's resolution and is **not** a proof of invariance. **The asymmetry is real and is the honest shape of the control:** this test can refute invariance and cannot establish it.
  **The resolution is preregistered, not chosen afterwards.** The manifest is a grid of **stated maximum spacing `Δγ`**, a class-P parameter **CURRENTLY UNSET** and therefore **a further blocker on BS-3g emission**, alongside `n_draws`, `draw_master_seed` and the empty generator set. **`Δγ` is where the strength of the `HELD` claim is set, so it is a preregistered choice and not an implementation detail** — the same reasoning that made `n_draws` the gate's strictness. `kernel_sha256`, `estimator_sha256`, `verifier_sha256` — 64-character lowercase hex
  SHA-256 of `ref/gain_gradient_kernel.py`, `ref/gain_gradient_estimator.py` and
  `gates/verify_mu_gamma.py` as pinned at the revision that emits the receipt. `mapping_id` — the
  stable identifier of the **preregistered** γ → counterfactual sign-vector/calibration mapping;
  until one is preregistered the only admissible value is the literal `MAPPING-NOT-PREREGISTERED`,
  and a receipt carrying it **cannot discharge the BS-6 edge**. `gamma_hat`, `sigma_gamma` — finite IEEE-754 doubles, decimal, the estimated gradient and its
  standard error. `gamma_bound` — **RULED (2026-08-30): the A-PRIORI FROZEN RANGE's endpoint, not a
  measurement-derived value — `k_γ` is MOOT under this shape, and five rounds of
  self-declared-bound findings close because the origin is the instrument's preregistered
  calibration constraints, outside the thing bounded. The verifier refuses any receipt whose
  `gamma_bound` differs from the RATIFIED endpoint (proposed ±0.25, `PROPOSAL_GAMMA_RANGE.md`,
  awaiting ratification — the one item the sitting created).** V68 let the
  receipt author declare the bound, **which is `require_authorization`'s shape — a thing checked only
  against the author's own inputs (CODEX-V68 F7). A bound needs an origin outside the thing it
  bounds**: here the origin is the measurement itself plus a frozen constant, and the measurement is
  already recomputed from the frozen kernel by clause (b), so the author chooses nothing.
  **WHAT THE FORMULA GUARANTEES, STATED AT THE SECOND RECURRENCE RATHER THAN THE THIRD (GPT56-V69 F6,
  CODEX-V69 F6, convergent — this object's second consecutive round, and the lifecycle just showed
  what a third costs).** `|γ̂| + k_γ·σ_γ` is a **sampling-error bound**: it bounds the true gradient
  **only under three named conditions** — **(i) the linear response model**, which is §1's
  preregistered threat shape (a nonlinear sensitivity response is out-of-model **by the threat
  definition, not by oversight**; if the instrument's response is curved the control tests the wrong
  family, and that is a limitation of the preregistered threat, carried as such); **(ii) an unbiased
  estimator**, resting on the gain-v6 controls, which exercised bias fixtures — named as the
  evidence, not as proof; **(iii) an honest σ**, the delta-method value the verifier recomputes.
  **Under violation of any of the three the formula is NOT a bound, and no receipt field can make it
  one.** **The invariance outcome is therefore conditional and says so**: `HELD` certifies
  no-flip-on-the-grid **given the model**, exactly as `HELD` is already bounded by grid resolution.
  **THE SHAPE CHOICE UNDERNEATH IS THE PRINCIPAL'S, flagged before it becomes a third-round object:**
  a **measurement-derived bound** (this formula) tracks the instrument but inherits its failure
  modes; an **a-priori frozen bound** (a fixed γ range from the threat model) is immune to estimator
  pathology but may sweep a range the real instrument never occupies, making the control conservative
  or vacuous. **Which claim the control should make is a decision about the study, and it joins the
  BS-3g parameter sitting** (`DECISIONS_FOR_DUHO.md`).
  **WHAT THE GATE IS FOR — the chain composed in one place, before this object earns its third
  round.** The bound statement places the TRUE gradient inside `[−gamma_bound, +gamma_bound]` with
  stated confidence, under its three named conditions. The manifest spans exactly that interval — no
  out-of-bound points, both endpoints, resolution `Δγ`. The within-draw rule isolates the gradient's
  effect from redraw noise (given the variate semantics above). Composed: **`HELD` asserts that the
  systematic which actually exists cannot have flipped this draw set's verdicts, up to grid
  resolution, conditional on the model — and `FAILED` anywhere in the interval is decisive.** The
  acceptance region IS implied by the bound statement; neither stands without the other's
  conditions, and both say so. `invariance_outcome` — exactly one token from
  the closed set `HELD` · `FAILED`. **`NOT-EVALUATED` is DELETED (CODEX-V72 F7): it required zero evaluated cells while the schema's own bounds (`n_perturbations ≥ 1`, a ≥3-value manifest) and clause (e)'s count closure make zero-cell receipts non-conformant — an outcome no conforming receipt can carry is a promise the schema cannot keep, the `INCONCLUSIVE-BY-COMPUTATION` argument one layer down. A control that was never evaluated emits NO receipt.** `n_perturbations` — a non-negative integer, the
  count of perturbations evaluated. `n_draws` — a positive integer, **fixed before any draw is
  generated**, the number of sign-vector draws the worst case is taken over. It must be stated with
  **what it means**: the maximum of `n_draws` exchangeable draws sits at the `D/(D+1)` expected
  quantile of the draw distribution, so this integer **is** the gate's strictness and must be chosen
  as such. `draw_generator_id` — the stable identifier of the named draw-generating algorithm and its
  seed-derivation rule, so draw `i` is reproducible from the master seed alone. **AND WHAT "THE SAME
  DRAW" MEANS ACROSS γ IS A PREREGISTRATION SEMANTICS CHOICE, NOT A GENERATOR DETAIL (CODEX-V71 F6):
  under COMMON RANDOM VARIATES, draw `i` uses one uniform stream for every γ, so cell `(i, j)` and
  `(i, 0)` differ only by the gradient and the within-draw comparison isolates it; under INDEPENDENT
  redraw per γ, the comparison is contaminated by redraw noise and a flip may be noise, not gradient.
  The within-draw rule was built assuming the first; assuming is not preregistering. The choice is
  CLASS-P, UNSET, a further blocker on BS-3g emission, and it sits beside `n_draws` in the
  principal's file because it decides what a draw IS.** `draw_master_seed` —
  the single frozen seed the whole draw set derives from; **no seed may be selected after any verdict
  has been seen**, which is the failure mode named when this mapping was first raised as a question.
  `draw_verdict_digest` — the digest over the **ordered per-draw verdict sequence**, so a verifier who
  did not write the harness can replay the draw set and confirm the reported worst case is the worst
  of exactly those `n_draws` verdicts. **A worst-case claim whose draw set cannot be replayed is an
  assertion, not a measurement.** `baseline_verdict` — the unperturbed verdict at γ = 0, from the same
  closed token set the run outcomes use; **"worst" is meaningless without the thing it is worse than.**
  **And the baseline has the same outside-origin obligation as the bound (CODEX-V69 F5): the manifest
  MUST contain the point `γ = 0`, and the verifier RECOMPUTES the γ = 0 column by replay and refuses
  any receipt that disagrees with it.** A producer-chosen baseline lets `HELD` be measured against a
  verdict nothing produced — `require_authorization`'s shape at the reference point instead of the
  bound.
  **THE COMPARISON IS WITHIN-DRAW, because one scalar baseline confounds draw noise with gradient
  sensitivity (GPT56-V70 F5, HIGH).** The redraw is stochastic, so the γ = 0 column may legitimately
  vary across draws; a single scalar compared against every cell would report that noise as a
  gradient effect. **`HELD` holds iff for every draw `i` and every perturbation `j`,
  `verdict(i, j) = verdict(i, 0)`** — the gradient either moves a given draw's verdict or it does
  not, which is the question the control asks. `baseline_verdict` carries the γ = 0 token **when that
  column is constant**, and the literal `PER-DRAW` otherwise; either way the verifier's replay of the
  γ = 0 column governs and the field is informational.
  **THE VERDICT-PRODUCING COMPUTATION IS BOUND, not just its output (CODEX-V70 F7, HIGH).**
  `draw_verdict_digest` authenticates the chosen output; it does not bind the computation that chose
  it — `ref/gain_counterfactual_path.py` exposes `stage`, `prefix`, `trial` and `n_perm` as caller
  inputs **and defaults `n_perm` to 2,000 against a production contract of 100,000**, so a producer
  could keep all fields fixed while choosing a permutation resolution that changes the matrix.
  **THE REPLAY CONSTRUCTS ITS OWN INPUTS AND ACCEPTS NO CALLER OBJECTS (GPT56-V80 F4, CODEX-V80 F1:
  the composition proof fell to two caller-supplied surfaces — an unpinned mapping callback that can
  load and unload modules before the end snapshot, and a `SealedMask` SUBCLASS whose method dispatch
  runs arbitrary code under the original digest, since v9's `require_any_mask` accepts any
  `isinstance`). The replay harness builds the mask from the pinned artifacts itself, TYPE-EXACT —
  `type(m) is SealedMask`, never `isinstance` — and invokes NO mapping callback: today
  `MAPPING-NOT-PREREGISTERED` means no callable exists to call, and when a mapping is preregistered
  it enters as a pinned module in the manifest, not as an argument. Caller-supplied executables were
  the entire remaining code surface, and now there are none.**
  **`counterfactual_path_sha256` pins the wrapper — and the wrapper is not what computes (GPT56-V72
  F5): the verifier must ALSO assert that the `successor_ref_v9` module actually imported hashes to the
  frozen `6a9abbbd…` — **and the assert runs in an ISOLATED interpreter, because a merely fresh one still runs inherited
  machinery before the pinned import (GPT56-V74 F2, CODEX-V74 F4: site hooks, `sitecustomize`,
  `PYTHONSTARTUP`, path-injected import hooks all execute first). **THE TWO PINNED MODULES ARE COMPILED FROM THE VERIFIED BYTES THEMSELVES — one mechanism that
  kills three attacks at once (GPT56-V81 F1: `-X pycache_prefix` substitutes timestamp-matched
  bytecode while every flag check passes; CODEX-V81 F2: hash-then-import leaves a
  verified-bytes/consumed-bytes swap window; CODEX-V81 F3: a code object compiled with
  `optimize=1` strips the assert though `sys.flags.optimize == 0`). The harness reads v9 and the
  counterfactual path ONCE into memory, hashes THOSE buffers against the pins, and
  `compile(buffer, optimize=0)`-executes them into fresh module namespaces — **IN ORDER, WITH
  PRE-BINDING (GPT56-V82 F1, CODEX-V82 F1: the path buffer's own top reads `import
  successor_ref_v9`, which would re-enter the import machinery and read the disk a second time —
  the mechanism defeated by its subject's first line): the harness executes the verified v9 buffer
  FIRST, registers the resulting module object as `sys.modules['successor_ref_v9']`, and only then
  executes the path buffer, whose import statement now binds to the already-verified in-memory
  module and touches no disk.** No import machinery for the pinned pair,
  no bytecode cache, no second read, and the optimize level is an argument we set, not a flag we
  trust.** The dependency roots still travel the import machinery, so their digests are
  **re-verified after computation** — and **the window INSIDE the platform loader's reads is named
  into the trust declaration (GPT56/CODEX-V83 F2: a swap-import-restore race around the loader's own
  read defeats before-and-after hashing, and no userland check can close a race against the loader
  it is running on): an adversary who can race the platform loader owns the machine, which the
  declaration already concedes for the linker and kernel — each closure level names the next, and
  the loader's read window is now named rather than implied.** **OPTIMIZATION IS
  ALSO FORBIDDEN AT LAUNCH (GPT56-V80 F5, CODEX-V80 F2): no `-O`/`-OO`, `PYTHONOPTIMIZE` dead with
  the cleared environment, `-B` set and `sys.pycache_prefix` checked `None`, `sys.flags.optimize`
  checked `0`** — belt for the interpreter's own behaviour, with the compile-from-buffer as the
  spine — and the assert-as-guard stays a recorded v9 limit. The replay process is launched under **the interpreter's
  ABSOLUTE PATH as recorded in BS-7p's `environment` field — a bare `python` is PATH-rebindable before isolation begins (CODEX-V75 F4)** —
  with `-I -S`, a cleared environment, a pinned working directory, **and an explicit `sys.path` set
  to the pinned dependency roots, because `-S` skips site and NumPy does not import from nowhere
  (GPT56-V75 F3: the isolation flags without a specified bootstrap were an unimportable mandate).
  And the pins are RECEIPTABLE, not asserted (GPT56-V76 F2)**: **BS-7p's `environment` field carries a
  canonical sub-schema — `interpreter_path` (absolute), `interpreter_sha256`, and `dependency_roots`
  as an ordered list of (path, digest) pairs, **and `dynamic_load_manifest` — the linker-resolved
  transitive closure of shared objects the interpreter and roots load, recorded as ordered (path,
  digest) pairs at freeze (GPT56-V77 F2, CODEX-V77 F3: listed-root hashing without the native
  closure left omitted `.so`/`.dylib` dependencies able to alter verdict computation while every
  listed digest matched)** — under the canonical field-order encoding, and a separately pinned
  verifier recomputes interpreter, roots and closure digests from disk and refuses mismatch. **And the manifest is not only recorded — it is ENFORCED AT REPLAY END (GPT56-V78 F1, CODEX-V78
  F1: a freeze-time snapshot neither closed nor forbade verdict-affecting loads first requested
  AFTER replay starts — a lazily-imported submodule or a runtime `dlopen` arrived outside it):
  after the verdict computation completes and before the result is accepted, the replay process
  enumerates its actually-loaded objects — `sys.modules` for Python, the loader's image list for
  native objects — and REFUSES its own result if any loaded object is outside the manifest.** **V79 claimed the frozen bytes contain no dynamic-load constructs, and both seats showed the
  claim FALSE — v9's `_frozen_planner()` (L269–277) loads the frozen cutout planner via
  `importlib.util` (GPT56-V79 F1, CODEX-V79 F1, verbatim-convergent). The corrected statement is
  the checked one: v9 contains EXACTLY ONE dynamic-load site, it loads a module that pins its own
  adapter digest and raises on mismatch, and it is UNREACHABLE from the verdict path — the call
  graph from `run_production_verdict` reaches neither `_frozen_planner` nor `frozen_plan_object`
  (AST-verified over the frozen bytes at V80), and `gain_counterfactual_path.py` imports neither
  `importlib` nor `ctypes`. So on the REPLAY path a late load remains a violation, never a need —
  and the load-then-unload gap closes by composition, not by the snapshot: under `-I -S` with a
  cleared environment, the only code running before the end-snapshot is the pinned code, whose own
  bytes are what the AST audit covers; an unload requires an unloader, and there is nowhere for one
  to live.** **What remains above the manifest is the linker ITSELF
  and the kernel, which are the trust declaration — each closure level names the next as trusted,
  and this one is where the naming stops.** The roots join the frozen environment `require_environment` checks — the record that
  pins `numpy 1.26.4` now names where it loads from, checkably. It hashes the pinned file, imports
  it, computes. **And the trust boundary is stated
  rather than implied: the interpreter binary and the OS are trusted BY DECLARATION, exactly as they
  are for v9's own runtime — an adversary who owns the interpreter owns every check ever written in
  it, and no flag repairs that.** What the isolation removes is every rebinding vector that rides
  configuration rather than ownership. Every verdict
  cell must be produced under the PRODUCTION permutation contract — `n_perm = 100,000`, the frozen stage/trial/address parameters §3
  and §5 pin, no overrides — and the verifier replays cells under exactly those parameters and
  refuses mismatch.** The compute cost is real and is the price of the verdicts being production
  verdicts; **if the principal wants a cheaper counterfactual resolution, that is a preregistered
  parameter for the BS-3g sitting, not a producer's default.** `delta_gamma_max` — a finite positive
  IEEE-754 double, decimal: the maximum adjacent spacing of the perturbation manifest, **which must
  equal the frozen class-P value** — added because V67 put the grid-resolution rule in prose and left
  it out of the schema and the verifier (GPT56-V67 F5, CODEX-V67 F6), **which is the describe-versus-
  compute law violated in the section that cites it.**
  **FOUR GAPS IN THE DRAW SET, CLOSED HERE, because replayability alone does not make this checkable.**
  **(1) PRE-COMMITMENT — a receipt cannot prove its own draws were chosen blind (CODEX-V63 F2, HIGH).**
  Replaying a draw set proves the reported worst is the worst **of that set**; it proves nothing about
  when the set was chosen, and **adaptive off-record selection — trying seeds quietly and reporting the
  one that passes — satisfies every field and the verifier.** **The repair is not another receipt field:
  `n_draws` and `draw_master_seed` are FROZEN IN THIS PREREGISTRATION at freeze**, covered by the freeze
  signature and by §6.3's void rule, and the verifier **refuses unless the receipt's values equal the
  frozen ones**.
  **AND NEITHER VALUE EXISTS YET, WHICH V64 CLAIMED PAST (GPT56-V64 F3, CODEX-V64 F5, both HIGH).** V64
  said pre-commitment was witnessed by the freeze while **no frozen value was written anywhere**, so
  the verifier had nothing to compare against and the mechanism was a description of a mechanism.
  **`n_draws` and `draw_master_seed` are class-P values, CURRENTLY UNSET, and their absence is a
  BLOCKER of exactly the kind the four empty `SLOT_SCHEMA` entries carry: NO BS-3g RECEIPT MAY BE
  EMITTED WHILE EITHER IS UNSET.** `n_draws`'s value is a preregistered parameter with the principal —
  it **is** the gate's strictness, since the maximum of `D` exchangeable draws sits at the `D/(D+1)`
  expected quantile. **A blocker is the honest state of an unmade decision; a claim that the freeze
  witnesses a value nobody has written is not.**
  **THE CLOSED SETS THE VERIFIER COMPARES AGAINST, declared here because V64 named them and never
  declared them.** `mapping_id` admits exactly one value — the literal `MAPPING-NOT-PREREGISTERED` —
  until a mapping including its draw set is preregistered, **and a receipt carrying it cannot discharge
  the BS-6 edge**. `draw_generator_id` admits values from a **closed set that is CURRENTLY EMPTY**: no
  generator is named, so **no admissible value exists and this too blocks emission.** Naming one is a
  preregistered choice and is made at freeze, not here. Pre-commitment is then witnessed by the freeze rather than asserted by the artefact it
  is supposed to constrain — **a receipt attesting to its own priority is the same defect as a hash
  chain attesting to its own custody.**
  **(2) ADDRESSING AND SERIALIZATION (GPT56-V63 F5, HIGH).** The evaluation is a **matrix**, not a list:
  draw `i ∈ [1, n_draws]` × perturbation `j ∈ [1, n_perturbations]` in the pinned manifest's order.
  `draw_verdict_digest` is the SHA-256 of the verdict tokens serialized in **row-major `(i, j)` order,
  one token per cell, `\n`-separated, no trailing separator, UTF-8** — stated because a digest over an
  unstated serialization is not reproducible by anyone who did not write the producer.
  **(3) THE CATEGORICAL WORST-CASE RULE (GPT56-V63 F5).** Verdicts are **categorical**, so "worst" needs
  a rule and inventing an ordering over outcome names would be a modelling choice smuggled into a
  reduction. **There is no ordering: `invariance_outcome` is `HELD` if and only if every cell `(i, j)` equals its own draw's `(i, 0)` cell, and `FAILED` otherwise** — this sentence carried the scalar-baseline form for two revisions after the within-draw rule replaced it (CODEX-V72 F1), the third scalar survivor and the reason the whole draw-discipline block is now frozen below. That is what the control is for — whether any allowed
  gradient moves the verdict — and it makes the worst case a comparison rather than a ranking.
  **(4) BOUNDED ENCODINGS (CODEX-V63 F3, MEDIUM).** Unbounded identifier, seed and count encodings can
  carry an object-indexed payload, which would defeat this row's own no-per-object-field property.
  **`draw_generator_id` and `mapping_id` take values from closed enumerated sets** declared in this
  document; **`draw_master_seed` is a decimal integer in `[0, 2^64 − 1]`**; **`n_draws` and
  `n_perturbations` are decimal integers in `[1, 10^6]`**. **Any value outside its stated encoding is
  refused, and the bound is what makes "no field can carry a per-object payload" a property of the
  schema rather than an undertaking.**
  **Producer:** the sensitivity-gradient control runner, which must call the estimator and verifier
  whose digests it reports; a receipt whose `estimator_sha256` does not match the module actually
  executed is a protocol deviation and voids the run under §5.
  **Independent verifier:** a separately pinned checker that (a0) **refuses unless `mask_sha256`
  equals the `mask_digest` BS-2f pinned**, recomputes `calibration_sha256` from the calibration
  actually bound, recomputes `perturbation_manifest_sha256` from the manifest, and **refuses unless
  `n_perturbations` equals the manifest's length** — a count that disagrees with its own manifest
  is the subset case this repair exists to catch; (a) recomputes **all five** module digests — kernel, estimator, verifier, `counterfactual_path_sha256` **and `replay_harness_sha256` (added at V82 while this clause said four — the same one-revision lag GPT56-V71 F6 caught when the fourth joined; CODEX-V82 F2)** —, (b) recomputes `gamma_hat` and `sigma_gamma` from the frozen kernel and refuses
  on any mismatch beyond exact equality, (c) refuses any `invariance_outcome` outside the closed set,
  and (d) refuses `mapping_id` values not naming a preregistered mapping; and **(e) enforces the draw
  set — it recomputes `draw_verdict_digest` by regenerating all `n_draws` draws from
  `draw_master_seed` under `draw_generator_id`, refuses any receipt whose evaluated count differs from
  `n_draws` in either direction, and refuses unless `invariance_outcome` is `HELD` exactly when **every cell `(i, j)` equals its own
  draw's `(i, 0)` cell** — this clause compared against the scalar baseline for one revision after
  the within-draw rule replaced it (CODEX-V71 F5); **it independently refuses unless `n_draws` and
  `draw_master_seed` equal the values frozen in this preregistration**, and refuses any field whose
  encoding falls outside its stated bound; and **(f) evaluates DISCHARGE separately from validity: a
  receipt discharges the BS-6 edge only if `invariance_outcome` is `HELD`; a `FAILED` receipt is a
  valid record that does not fill the slot** (CODEX-V67 F5); and **(g) makes the outcome a total
  function of the evaluation rather than a choice: every conforming receipt has evaluated cells, and
  must carry `HELD` if every cell `(i, j)` equals its draw's `(i, 0)` and `FAILED` otherwise (CODEX-V68
  F8; the zero-cell branch died with `NOT-EVALUATED`, CODEX-V72 F7).** **The stopping rule is exactly `n_draws` draws, all evaluated: not "until it fails",
  which always fails eventually, and not "until it passes", which is worse. A run that evaluates fewer
  or more is void, not a smaller or larger gate.** **It must not accept the
  producer's own report of any quantity it can recompute.**
  **Failure behaviour:** any refusal above emits **no** receipt — the slot stays UNFILLED. A missing
  or non-conforming BS-3g receipt leaves the `blocks BS-6` edge undischarged, and **BS-6 does not
  open**. There is no partial or provisional BS-3g receipt.
  **WHY THIS RECEIPT CANNOT CARRY A PER-OBJECT FIELD, which §6.1's non-χ-bearing claim rests on.**
  Every field above is a **fixed-width scalar, a digest, a closed-vocabulary token, or a count**. **The three fields added at V60 are digests over aggregates and deserve the test explicitly, since they are derived from object data:** `mask_sha256` digests positions and acceptance flags which §6.1 already classes χ-free and which **BS-2f already publishes as `mask_digest`**, so it discloses nothing BS-2f does not; `calibration_sha256` digests per-bin accuracies, which are aggregates over bins and not over objects; `perturbation_manifest_sha256` digests a list of γ values, which are properties of the perturbation and not of any object. **A digest over a whole artefact is not an object-indexed field, and none of the three can be inverted to a per-object quantity.**
  **No field is array-valued, none is indexed by object, and none admits a per-object quantity** —
  there is no field a χ value, sign, amplitude, confidence or object identifier could occupy without
  violating its stated type. And because `receipt()` refuses a slot in `SLOT_SCHEMA` whose field set
  differs from the pinned one in **either** direction, an extra field cannot be smuggled in beside
  them. **This is a property of the field list, checkable by reading it, not an undertaking by the
  producer.**
  **Known limit, stated rather than left implicit:** this reasoning holds only for slots **present
  in `SLOT_SCHEMA`. `receipt()` does not enforce field sets for absent slots**, and five are absent
  (BS-3g until this entry lands, BS-2a, BS-2k, BS-L, BS-2v) — see
  `ANSWER_RECEIPT_UNKNOWN_SLOT_AND_V9.md`. **Adding BS-3g to the schema is what makes the paragraph
  above true of BS-3g**; the other four remain unprotected until they are added and every producer is
  bound to a constructor that refuses unknown slots.
- **Value-domain enforcement for slot receipts (CODEX-V72 F2).** Frozen v9's `receipt()` and
  `SLOT_SCHEMA` constrain field NAMES; nothing constrains what bytes a named field carries, so an
  authorised non-χ receipt could carry object-indexed prose in a conforming field. **`receipt_strict()`
  and every slot verifier validate VALUE DOMAINS against `ref/STRING_FIELD_REGISTRY.md`** — generated
  from the schema blocks by `ref/gen_string_field_registry.py`, a field with no row forbidden by
  default, the generator exiting nonzero on an unclassified field so the battery blocks instead of
  shipping an omission.
- **Replay harness (`gates/replay_harness.py`) — REQUIRED, DOES NOT EXIST (GPT56/CODEX-V83 F1).**
  Carries every replay obligation §11 states: no-caller-objects, type-exact mask construction,
  compile-from-verified-buffer with pre-binding, optimize=0, flags and pycache checks, the
  loaded-object census, root re-verification. Its sha256 is the class-P expected value for
  `replay_harness_sha256`, set when built, frozen at freeze — UNSET until then, blocking BS-3g.
- **Enumeration verifier (`gates/enumeration_verifier.py`) — REQUIRED, DOES NOT EXIST (CODEX-V68 F5
  found §6.1 claiming this item while §11 carried nothing; the claim without the item is the
  self-describing-prose defect in the inventory built to prevent it).** Separately pinned. Recomputes
  from the access-log chain: the set of `REFUSED-UNCLASSIFIED` events, each entry's `class_key` =
  (table row, operation), the per-key `EXPLAINED` count (≤ 1 within the run), the resolution of every
  `explanation_ref` and every `NAMED-AS-DEFECT` re-derivation digest. Refuses on any unenumerated
  emission, dangling reference, or second `EXPLAINED` — **and on any ORPHAN ENTRY: the entry↔emission
  relation is a BIJECTION checked in both directions, because a one-way check let an entry join a
  non-catch-all or nonexistent event and count toward completeness (GPT56-V72 F4).** Consulted at **five gates, each over the chain as it then stands: `BS-L` issuance, the lock
  opening, then `BS-7f`, then `BS-V`, then disclosure** — V70 named the post-opening gates in §6.1 and this
  inventory item still said two (GPT56-V70 F3, CODEX-V70 F5), the claim-without-the-item defect
  scored against the item built to fix it. It reads checkpoint AND continuation entries, and their
  explanation artifacts, under the (iv-b) constraint. Never accepts a producer's summary of its own emissions.
- **Atomic touch commit domain — a BS-2k DESIGN REQUIREMENT with fixtures (same finding).** The
  BS-2k design artifacts must specify the transactional domain in which store effect, event and
  identifier binding commit atomically, with fixtures demonstrating: an aborted commit leaves no
  committed buffer; a committed touch's event outcome equals its store effect; delivery retry
  produces no second event; recovery from bindings re-decides nothing.
- **BS-2f boundary recomputation verifier (same finding).** Recomputes `calibration_bins()` over the
  full sealed accepted-partition positions and refuses unless the sealed boundaries equal the
  recomputation exactly; certifies the artifact, not the process, per §6.3.
- **`VOID` conversion:** Implement a converter (`BS-2v`) that handles every enumerated void antecedent. It must define a canonical closed antecedent registry with stable IDs and exact source/phase/failure-effect for each `VOID` branch. The receipt must conform to a **canonical authenticated receipt schema**, including: registry digest, converter implementation digest, ordered normative IDs, exercised IDs, uniqueness and count closure, per-ID source/phase/failure-effect, and result classification (all authenticated). The gate must compare the converter's emitted IDs and the exercised fixture IDs against the pinned §7.1 digest's contents. Missing, duplicate, extra, or non-`VOID` conversion for any ID fails the gate. This is a pre-BS-6 dependency.
