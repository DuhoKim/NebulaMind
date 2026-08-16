# Handover — night of 2026-08-14

## State

The preregistration is **FROZEN, accepted by Duho, committed, pushed, and merged to main**.
- `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260814.md` — SHA-256
  `da2c6a21d994b9af7395347bf881075f855826ff859dd0415f15042f80ed3308` (read-only, 444)
- Freeze record: `PREREG_FREEZE_RECORD_20260814.md`
- Merged as `dc85980460ce` via PR #144; branch `feat/paper-workflow-v2`.

Ten binding slots: nine pass, **BS-1's licence limb failed and stays failed**. The output was
redesigned to need no derived catalogue rather than the permission being obtained. BS-11 (release
linter) added and filled.

**BS-5 synthetic absolute-sign anchor: PASS**, 32/32 both directions, no correction, convention
unchanged. Gated by Kun (`KUN_BS5_ANCHOR_GATE_20260814.md`).

## Built tonight, not yet gated

- `acquisition/` — cutout pipeline. **Build only; it has no network client at all** (AST-audited;
  `MockTransport` is the only `fetch` implementation). 14/14 tests, all three negative fixtures fire.
- `handcheck/` — blinded hand-check harness. 29/29 self-test checks on a full synthetic 500,
  plus an independent verifier at 33/33 that never imports the production module.

## Next steps, in order

1. Yui's `YUI_HANDCHECK_HARNESS_20260814.md` design doc (was in progress at 23:11).
2. Kun gates both builds. **Do not dispatch him until Yui's doc lands** — gating a moving target
   produces a receipt for a version that no longer exists.
3. Then the run, which is blocked on people, not code: HC-1..HC-5 needs **two independent checkers
   plus a third adjudicator** hand-classifying 500 blinded galaxies. `a < 0.85` overall or any
   stratum < 0.70 → INCONCLUSIVE-BY-POWER, no run.

## The line that still holds

The STOP rule is absolute and unlifted in practice: no real cutout has been fetched, no sky
statistic computed, K-8 not tripped. Duho authorised "run it"; the run could not start because the
tools did not exist. They exist now — running them is still his call.

## Morning video (built 2026-08-15 ~01:00)

`/Users/duhokim/HermesOps/cockpit/videos/status_20260815_prereg/where_the_work_stands_20260815.mp4`
3m 06s, narrated, 12 cards, every number verified against a cited receipt. Not uploaded.
Covers: the claim being tested, why it was frozen first, the licence failure and the output
redesign, the 32/32 sign anchor, and that the remaining step needs a human. Ends on the STOP rule.

---

## Overnight, 01:00–01:30

**HC-1H is CLEAN and ACCEPTED.**
- Kun: `PASS_HC1H_CLOSE_ON_EXACT_HASH` (`KUN_HC1H_CLOSE_20260814.md`, 01:05)
- Duho accepted 01:08, verbatim *"accept it, and run autonomously for rest of tonight"*
  → `HC1H_ACCEPTANCE_20260815.md`
- accepted artifact: `LANA_ONE_HUMAN_ATTENUATION_20260814.md`
  `b2590e4213e225f9869fe782cfe0f55d8d8979dcb470752836a5cd31a58453fd`

It took four revisions. Errors the gate chain caught: a power break-even wrong by 0.08 in `a`; a
variance formula understating sigma 3x; a pilot carry-forward that was selection-then-reuse bias; an
unenforced blinding assumption. **One relay failure was mine** — Kun's re-gate listed three required
repairs and I passed on two, having read only part of that document.

**Also gated:** Tori's acquisition pipeline — `PASS_ACQUISITION_BUILD_ONLY_GATE`
(`KUN_ACQUISITION_GATE_20260814.md`). Kun verified the no-network claim from the source himself:
the module imports no HTTP library at all; the single URL constant only builds a request record.

**In flight at 01:30**
- v2 preregistration candidate `PREREG_LONGO_AMPLITUDE_TEST_20260815_CANDIDATE.md`
  (`6ae6a58cd6d29511…`, 406 lines) — with Kun for gating
- Yui reworking the hand-check harness for HC-1H (it was built to the superseded HC-1 spec:
  wrong strata, no synthetic injections, no mirrored repeats, no HC-7 UI)

**Integrity:** the 08-14 frozen preregistration is untouched — `da2c6a21d994b9af…`, perms `444`.

**Waiting on Duho, in order**
1. Nothing yet — v2 is still gating. If it passes, it is frozen overnight per his authorisation.
2. **Pilot (150 labels) or full (850)** — §2b of the HC-1H document; this is his choice and nothing
   proceeds without it.
3. Authorising the acquisition run. Still the STOP-rule crossing.

**Not done, deliberately:** nothing pushed, published, or run against sky. No real galaxy touched.
K-8 untripped. Morning video: `/Users/duhokim/HermesOps/cockpit/videos/status_20260815_prereg/`.

---

## Morning summary — 03:21, night complete

**v2 preregistration is FROZEN.**
`PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815.md`
SHA-256 `62dad44dd92acf2781d2c8cf25161f7f344e3fe6f7fec35b7e04308bd1539c12`, mode 444.
Gate: `KUN_V2_PREREG_GATE2_20260815.md` — **PASS_V2_FREEZE_CLEAR_ON_EXACT_HASH**.
Freeze record: `PREREG_FREEZE_RECORD_20260815.md`.
Both predecessors preserved: 08-12 `ac43490054b15961…`, 08-14 `da2c6a21d994b9af…` (verified intact,
mode 444, at freeze time).

**Also completed overnight**
- Acquisition pipeline gated: **PASS_ACQUISITION_BUILD_ONLY_GATE**. No HTTP library is imported at
  all; `MockTransport` is the only `fetch`. Kun verified from source, not from Tori's own audit.
- Hand-check harness reworked for HC-1H: **27 tests OK**, `PASS_HC1H_SYNTHETIC_SELFTEST`, 80
  structural claims checked by a verifier that never imports the production module. A deliberately
  borderline `a = 0.849` returns INCONCLUSIVE rather than rounding into a pass.

**Two limits Yui states herself, worth reading before you label anything**
1. The self-test does **not** prove synthetic injections are perceptually indistinguishable from real
   cutouts — it equalises schema and dimensions only. HC-7 clause (v) makes that exposure a hard
   INCONCLUSIVE trigger, so the gap matters.
2. The replacement reserve is finite and fails closed: a checker who keeps flagging items can force
   INCONCLUSIVE. You are the checker.

**Committed locally as `199c316`, 46 files, 0.6 MB. NOT PUSHED** — every outward step has been
authorised individually and push was not.

**Waiting on you, in order**
1. **Pilot or full.** §2b pilot = 150 labels (90 real, 40 synthetic, 20 retests), returns only
   PASS-TO-FULL-HC1H or INCONCLUSIVE. Full = 850, sessions capped at 50. Nothing proceeds until you pick.
2. Push / PR / merge the v2 freeze, if you want it public like v1.
3. Authorise the acquisition run — still the STOP-rule crossing, and still downstream of the hand-check.

**Untouched:** no real galaxy, no sky statistic, K-8 untripped, nothing published.
**Video:** `/Users/duhokim/HermesOps/cockpit/videos/status_20260815_prereg/where_the_work_stands_20260815.mp4`
(3m 06s, narrated; describes the design and the licence redesign, and predates tonight's HC-1H freeze).

---

## Acquisition strategy — 10:55–12:41, autonomous

**Status: no acquisition route is open. `HOLD EXECUTION`.** Nothing fetched; no transport exists.

### The finding that reframes it

The frozen route and the frozen estimator disagree about the input.
`TORI_SURVEY_ROUTE_BINDING_20260812.md:141` freezes `size=256`, `bands=grz`.
`YUI_PRODUCTION_ESTIMATOR_APPENDIX_20260812.md:55` freezes ResNet-18, **single channel, 128×128**.
The route fetches **12× more pixel data than the model can consume**. Kun's ruling: **PC-1 is what
is wrong** — "changing the estimator is a separate scientific decision, not an acquisition
optimization."

### Corrected arithmetic (Kun recomputed all of it independently)

| route | count basis | bytes |
|---|---:|---:|
| 256×256 grz cutouts — **as currently frozen** | 832,393 objects | **654.6 GB** |
| 128×128 grz cutouts | 832,393 objects | 163.7 GB |
| **128×128 one-band cutouts — recommended** | 832,393 objects | **54.6 GB** |
| one-band bricks (Goru's measured compressed size) | 270,577 files | 3.2 TB |
| grz bricks (same basis) | 811,731 files | 9.7 TB |

**My two errors, corrected by the lanes:** I estimated bricks at 38 TB assuming one uncompressed
file per brick — Goru measured by HTTP HEAD that bands are separate `.fits.fz` files and `image-r` is
11.4 MB. And I claimed bricks meant ~3× fewer requests — Tori found one file *per filter*, so grz is
811,731 files against 832,393 cutouts, no advantage. Bricks remain ~59× the one-band cutout payload.

### The non-arithmetic constraint

Goru, from primary documentation: the survey **explicitly discourages** bulk automated use of the
cutout service and asks large jobs to use **Globus**. Tori independently proposed asking the operator
to approve a batch plan before 832,393 calls. Two lanes, no contact, same conclusion.

### What a PC-1 amendment must do

Fix the input contract to **128×128, one band, float32**, freeze the band and the complete
nanomaggy→estimator normalisation on synthetics only, and state what PC-3 parity and PC-4
fail-closed require **if cutting ever moves local** — that transfers WCS custody onto our code and
must be re-verified, not assumed.

### Also gated

`KUN_HARNESS_GATE_20260815.md` — **PASS_HC1H_HARNESS_WITH_OPERATING_BOUNDARIES**. The borderline
`a = 0.849` uses `Decimal` with unrounded comparison, so the no-rounding guard is structural. Sealed
key written mode `0600` to the private root only, verified from source.

### Waiting on Duho

1. **Approve the PC-1 amendment direction** (128×128 one-band) — nothing proceeds without it.
2. **Decide the operator query.** Even at 54.6 GB, 832,393 calls against a service that discourages
   bulk use is a question to ask NOIRLab, not to answer ourselves.
3. Then, and only then, a real transport — which means deleting the `BUILD_ONLY_STOP` guard Kun
   certified, and gating that deletion.

**Not done, deliberately:** no fetch, no transport, no amendment written, nothing pushed.
K-8 untripped. The STOP rule holds.

---

# STATUS — night of 2026-08-15 → 16, autonomous run (03:27 KST)

## Headline

**The corner defect was found only by crossing two independently-built components,
neither author having run the other's work.** Yui's fixture oracle and Tori's adapter
each passed their own suites completely. Crossed, all eight exact/beyond-corner cases
failed at planning time — `expected exactly one primary brick, found 0` — before
rendering was ever reached. No amount of additional self-testing on either side would
have surfaced it.

## What the cross-check found

The adapter required exactly one computed rectangular unique-area primary before
polygon source-set planning could run. That precondition cannot hold at exact- or
beyond-corner geometry. Repaired: polygon intersection is now the sole source-selection
rule, and the rectangular primary is metadata that no longer decides whether pixels are
available.

## Does the adapter pass now

Yes, across three separately-counted blocks — never summed:

| block | cases | covers |
|---|---|---|
| round-1 | 29/29 | shared-tangent 3×3 grid, edge + corner ladder at dec −30 |
| round-2 | 4/4 | RA-wrap seam, declination extremes, distinct tangent points, overlap-only |
| round-3 | 10/10 | sub-pixel knife edge at +32.25 and −89.875 |

Round-3's hardest case: at the `+1` and `+0.25` offsets the candidate has positive
polygon intersection area but contributes no output pixel centres, so planned and
contributing sets legitimately differ. Checked against all three failure modes — kept
in the planned set (no under-planning), not counted as contributing (no phantom
coverage), and completes rather than erroring.

Adapter suite 30/30; fixture suites 17/17 across all three rounds.

## Kun's five pre-transfer gaps

| # | gap | state |
|---|---|---|
| 1 | exact/beyond-corner source-set cases | **CLOSED** — 8/8, gated |
| 2 | RA-wrap source planning | **CLOSED** — round-2, crossed, gated |
| 3 | declination-extreme planning | coarse **CLOSED** + gated; sub-pixel crossed 10/10 but **NOT YET GATED** |
| 4 | distinct per-brick tangent-point geometry | **CLOSED** — round-2, crossed, gated |
| 5 | overlap scalar 128 → ~130 px, or polygon replacement | **LIKELY closed** by the polygon repair — **not formally ruled** |

## Stated plainly: what did NOT complete

- **Kun never gated round-3.** Tori delivered the crossed result at 02:48; Kun went idle
  without re-gating it. Rounds 1 and 2 carry Kun's signature; round-3 carries only
  Tori's own cross-run and Yui's oracle. Treat round-3 as measured-but-unwitnessed.
- **Gap 5 was never formally ruled.** A grep found no surviving 128/130 overlap scalar
  and 16 polygon references, which is consistent with closure — but a grep is not a
  gate, and this exact pattern produced false passes earlier in this session.
- Pixel-value equality is still excluded. The adapter declares a nearest-neighbour
  renderer stand-in against a bilinear Astropy oracle; equality belongs to the resampler
  gate, after the pinned resampler replaces the stand-in.

## Waiting on Duho, in order

1. **Globus endpoint access — yours alone.** Nothing here can proceed to real data
   without it, and no agent should attempt it.
2. **Whether to have Kun gate round-3 and rule on gap 5.** Kun is idle and ready; this
   is ~5 minutes of work and closes the last two open items on the pre-transfer list.
3. **Whether round-3's ten cases are sufficient**, or the ladder should widen further
   before a source manifest is discussed.

Dependency/container lock is explicitly a **later tier** — Kun placed it before
production cutting, not before the transfer manifest. It is not on tonight's critical path.

## Boundary state

`BUILD_ONLY_STOP` intact. Zero cutouts fetched, zero sky statistics, no endpoint
activated, no source manifest against the real parent set, K-8 untripped. Committed
locally as `6e8fcd5` on `feat/paper-workflow-v2` — **not pushed, not published, not
accepted**. Frozen V3 prereg untouched.

---

# STATUS — 2026-08-16 autopilot (14:21 KST)

## Pixel-value equality is closed — the last deferred synthetic gap

`KUN_RESAMPLER_GATE_20260816.md` → **PASS_PIXEL_VALUE_EQUALITY** (adapter `267b2a93d2a6`).

The nearest-neighbour stand-in is gone. The adapter now carries oracle-bilinear semantics and is
compared against Yui's expected arrays by value:

| round | cases | pixels compared | skipped | max abs error | pre-declared bound |
|---|---|---|---|---|---|
| 1 | 29/29 | 5 | 24 | 1.907e-06 | 5e-6 |
| 2 | 4/4 | 4 | 0 | — | 1e-5 |
| 3 | 10/10 | 10 | 0 | 7.629e-06 | 1e-5 |

**The tolerance was not fitted, and this is checkable rather than trusted.** Both bounds are
declared *inside* the fixture generators, which are hash-pinned at `24f55943…` / `60e3d662…` /
`6b410fb4…` and unchanged since before the gate — so they cannot have been tuned to the adapter's
output. The residual arithmetic is exact: float32 ulp at 100.0 is `7.6293945e-06` = 2⁻¹⁷, matching
round-3's `7.629e-06` to one ulp; round-1's `1.907e-06` = 2⁻¹⁹. That is source-raster quantization,
not accumulated interpolation error.

**Round-1 skips 24 of 29 at pixel level, by declared geometry, not by filter.** Round-1's sources
share one tangent plane, which displaces neighbour-brick sampling by ~1.4 px; comparing there would
measure Yui's approximation rather than the resampler. Kun ruled it acceptable *and verified the
mechanism* — he read the source and confirmed `primary_only` is the sole filter, rather than
trusting the receipt's `cases_skipped: 0`. Rounds 2 and 3 use distinct per-brick tangent points and
compare every case with zero skips, so they are the meaningful neighbour-sampling value tests.

**Adapter remains stdlib-only** — verified import by import. numpy/astropy are oracle and test
scope, never adapter runtime.

## What is NOT closed, and is not claimed

- **Production-kernel equivalence.** This gate proves adapter-vs-oracle agreement, not agreement
  with the real Imagine/astrometry.net kernel. Explicitly a later gate.
- **The dependency lock is a measurement, not a rebuild.** `YUI_DEPENDENCY_ENVIRONMENT_LOCK_20260816.json`
  (`6e0c9ae2c414`) records the environment honestly and states its own limits: it does not provide
  an exact offline rebuild. Do not cite it as a container lock.
- Remaining production tier, unchanged: multiprocessing scheduling determinism; production
  `.fits.fz` image-HDU-1 read path; three-source T-junction if it occurs in real DR10 South
  geometry.

## Acquisition route — decision memo ready

`ACQUISITION_ROUTE_DECISION_20260816.md` (`def682f1bc52`). Recommendation, conditional as asked:

> **B (public HTTPS) is acceptable IF the survey publishes per-file SHA-256 manifests covering every
> required product, verified current against the DR10.1 in-place replacements — otherwise A (obtain
> NERSC access).**

**The one fact only a human can check:** does the survey publish per-file SHA-256 manifests for the
DR10 South coadd tree, and do they match the current DR10.1-replaced bytes? Look at the portal
directory listings, `legacysurvey.org/dr10/files/`, and the `decam-legacy-survey` group.

The failure asymmetry Lana identified matters: a stale checksum against current bytes *fails closed*
and is safe. The hazard is the portal serving **pre-replacement bytes that its own stale checksum
confirms** — internally consistent, but not the bytes §4.2 requires. The DR10 known-issues brick
list is the cross-check.

Two cheap A-side checks worth doing in the same sitting: whether the DTN collection needs `cosmo`
membership or just any NERSC account, and whether the survey runs a public Globus guest collection.
Either would unblock route A with no allocation.

Adopting B requires a **new freeze**, not an edit in place. Section 6 of the memo lists the exact
clauses to amend.

## Waiting on Duho, in order

1. **Verify the checksum-manifest question above** — it decides A vs B, and nothing else moves until
   it is answered. Do not accept an answer given from memory.
2. **Finish Globus Connect Personal** — you were mid-install. Destination collection did not exist
   as of this checkpoint.
3. **NERSC `cosmo` access**, if the answer to 1 sends us to route A.

## Boundary state

`BUILD_ONLY_STOP` intact. Zero cutouts, zero sky statistics, no endpoint activated, no network
reached, no package installed, K-8 untripped. Nothing pushed or published.
