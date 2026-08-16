# TORI — guarded production adapter for the brick route

Date: 2026-08-16 00:05 KST; corner repair 01:03 KST (§0); round-2 cross-check extension 01:23 KST (§0.1); receipt content-hash identity 01:37 KST (§0.2); round-3 knife-edge repair + extension 02:47 KST (§0.3); resampler gate 12:24 KST (§0.4)
Owner: Tori lane (executed this session)
Status: **BUILT, SELF-TESTED, CORNER-REPAIRED, YUI CROSS-CHECK ROUND-1 29/29 + ROUND-2 4/4; NOT EXECUTABLE; ZERO TRANSFER**
Gate: corner repair gated `PASS_ADAPTER_CORNER_REPAIR`; round-2 coverage extension awaits review. Duho owns acceptance.

## 0.1. 2026-08-16 round-2 cross-check extension

After Kun passed the corner repair, a coverage gap was found in verification:
the cross-check receipt read 29/29 but covered only the round-1 fixture
manifest, while Yui's round-2 fixtures (`make_boundary_fixtures_round2.py`,
`60e3d662…aa15bc`) — RA-wrap seam crossing, selected-footprint declination
extremes (+32.25 and −89.875), distinct per-brick tangent points, and a
derived overlap-without-unique-crossing case — had never been run through the
adapter. A green receipt narrower than it looks is exactly the dangerous
shape, so:

- `cross_check_yui_boundary.py` now runs BOTH rounds. Round-2 loads Yui's
  pinned pre-generated tree (`generated_round2/`, hash-verified against its
  own manifest) read-only; neither fixture generator was touched.
- Counts are reported **separately** (`round1: 29/29`, `round2: 4/4`) and
  never merged into one total; the suite test asserts no merged count exists.
- The receipt now carries a written `scope` field stating in words which
  boundary classes are covered and which are not (pixel-value equality,
  Yui's round-2 west-side `primary_brick` convention, sub-pixel knife-edge
  inclusion at extreme declination, real-geometry/multiprocess/fitsio/
  resampler items for later gates).
- **No adapter defect was exposed**: `nm_brick_cutout_adapter.py` is
  byte-identical to the corner-repair artifact (`f3c71021…fb658a`). All four
  round-2 cases pass planning AND the full cut pipeline — at 0.125° from the
  south pole the PC-3 round trips still hold at ≤1e-6 px.
- One honest near-miss worth Kun's eye, named in the receipt scope rather
  than hidden: the adapter projects source boundary polygons into the object
  tangent frame, Yui's round-2 oracle clips the output polygon in source
  pixel coordinates. The two agree on every round-1 and round-2 case (margins
  are ≥ ~10 source pixels), but they are not proven equivalent at sub-pixel
  margins near the poles; a knife-edge polar fixture class would separate
  them if that ever needs closing.

## 0. 2026-08-16 corner-planning repair (Kun hold, five conditions)

Kun's cross-run of Yui's independently built boundary fixtures against this
adapter failed all eight corner cases at planning time: I had made a computed
rectangular unique-area primary a hard precondition, and it fired before the
stronger polygon source-set rule could run. The mechanism: Yui's grid shares
one TAN tangent point at (180°, −30°); rectangular (ra, dec) unique bounds
derived from edge-midpoint projections carry ~1e-4-deg seams away from the
tangent point, so an exact-corner object falls between all four rectangles.
The fixtures are correct; the precondition was wrong — and this defect class
is position-correlated by construction, which a dipole test reads as signal.

The repair, against his five conditions:

1. **Precondition removed.** `plan_object` now derives the source set by
   polygon intersection alone. The grouping primary is metadata, chosen by a
   documented replacement rule: nearest planned brick centre by angular
   separation, exact ties lexicographic. Rectangular containment is recorded
   as `unique_area_primary_bricknames` (possibly empty) and gates nothing.
   Planning is terminal only when NO source image intersects the output
   footprint (`FAILED_PLAN_NO_SOURCES`), i.e. after the complete intersecting
   source set has been proven empty.
2. **Cross-check re-run and passing.** Kun's unmodified scratch runner
   (`_tmp_kun_cross_adapter_fixtures_20260816.py`, `69115bc3…157ae7a`) now
   reports PASS 29/29, all eight corner cases included. Yui's fixtures were
   not modified.
3. **Terminal failures preserved.** Missing planned source, digest mismatch,
   invalid/distorted headers, truncated FITS, zero coverage, invalid-pixel
   cap, and output tamper all still fail terminally — re-proven by the same
   tests plus the new `FAILED_PLAN_NO_SOURCES` test. Nothing was loosened
   except the one precondition; the empty-planned-set case still refuses to
   cut.
4. **PC-3/PC-4 unchanged and atomic** to output acceptance (Kun's gate
   already confirmed the wiring; no code in those paths was touched).
5. **Cross-check recorded as an adapter receipt.**
   `cross_check_yui_boundary.py` regenerates Yui's fixture tree read-only,
   runs all 29 objects through plan + local cut, and writes
   `CROSS_CHECK_YUI_BOUNDARY_RECEIPT.json` binding the adapter, Yui-generator,
   and objects.json hashes. The adapter suite runs it as a test, so any future
   adapter change that breaks the boundary contract fails the suite.

Neighbour reason classification (edge vs corner) now tolerates rectangular-
bound seams up to `REASON_CLASSIFICATION_TOLERANCE_DEG = 1e-3` — explicitly
metadata for manifest grouping, never a selection rule. No fixture of Yui's is
believed wrong; no open geometry question is raised against her set.

## 0.2. 2026-08-16 receipt content-hash identity (HOLD_RECEIPT_HASH_MISMATCH)

Kun's round-2 re-gate failed because the cross-check receipt is a generated
output rewritten on every run: it was deterministic modulo `recorded_utc` but
had no stable identity a gate could pin. Identity fix only — no counts,
comparison logic, scope declarations, or `not_covered` entries changed:

- The receipt now carries a top-level `content_sha256`: SHA-256 of its own
  content serialized canonically (`json.dumps(..., sort_keys=True,
  separators=(',',':'))`) with exactly `recorded_utc` and `content_sha256`
  excluded. The exclusion list is declared in the artifact as
  `content_hash_excludes` (which is itself inside the hash) — nothing else is
  excluded.
- Proof, two consecutive runs with no code or fixture change:
  - run 1: `recorded_utc = 2026-08-15T16:36:55Z`
  - run 2: `recorded_utc = 2026-08-15T16:37:10Z`
  - both: `content_sha256 =
    6a0a4e40653f79128af9359c25614f432ee1d00702e554047d07721bf4e08744`,
    round-1 29/29 and round-2 4/4, still separate, never summed.
- The suite test now recomputes `content_sha256` from the written receipt and
  runs the cross-check twice, asserting the hash reproduces — so the identity
  contract is enforced on every run, not remembered.
- Pinned inputs unmoved: adapter `f3c71021…fb658a` (byte-identical),
  round-1 fixtures `24f55943…3404d`, round-2 fixtures `60e3d662…aa15bc`.
- New artifact hashes: `cross_check_yui_boundary.py`
  `0ebc1eeba1f15ae3171e5abc8b03243e665d900bcb51c93d2f348af417a61db1`,
  `test_nm_brick_cutout_adapter.py`
  `8fe1ab22abf5e901d412150d79c99284277439c42777fc2bb6b61698811524fd`.

Pin rule for the gate: pin the receipt's `content_sha256`
(`6a0a4e40…e08744`), not the file bytes — the file legitimately differs
between runs only in `recorded_utc`.

## 0.3. 2026-08-16 round-3 extreme-declination knife-edge repair + extension

Yui's round-3 fixtures (`make_boundary_fixtures_round3.py`, `6b410fb4…5e5e62`;
pinned pre-generated tree `generated_round3/`, hash-verified) place objects on
signed sub-pixel offset ladders (−10, −0.25, exact 0, +0.25, +1 candidate-
source pixels, solved to 1e-8 px) at both selected-footprint declination
extremes. Crossing them against the adapter found **one real planning
defect**, exactly in the class the round-2 scope had named as unproven:

- `dec_min_exact_boundary` (dec −89.875, zero-area tangency): the adapter
  planned the candidate; the contract (positive intersection area) excludes
  it. Mechanism: the adapter projected the 3600-px SOURCE boundary polygon
  into the object tangent frame and used an inclusive touch-counts test; near
  the pole the chord approximation of the projected source square cannot
  resolve a 1e-8-px tangency. The other nine cases, including all ±0.25-px
  ladder steps, already matched.

**Repair (adapter, not fixtures — all three generators unmoved):**

1. Planning inclusion now projects the OUTPUT nine-point boundary into each
   candidate source's own TAN pixel plane, clips it against the exact source
   pixel-edge box (Sutherland–Hodgman), and includes iff clipped area
   > `INTERSECTION_AREA_THRESHOLD_SOURCE_PIX2 = 1e-8` px². Same §6.2
   nine-point rule, evaluated in the frame where the ~33-arcsec output
   polygon projects near-rigidly at any declination (chord error ~1e-6 px vs
   curvature-limited in the reverse direction). Exact zero-area tangency is
   excluded — such a source contributes zero pixels, so exclusion cannot
   truncate anything. Per-brick clipped areas are now recorded in the plan.
2. The renderer's contribution window is aligned to the fixture oracle's
   bilinear-support rule: an output pixel centre must lie within the source's
   interior pixel-centre window [1, N]. This prevents over-crediting
   coverage where interpolation support does not exist; the production
   window is re-proven at the resampler gate.
3. Verified against Kun's three failure modes for the planned-vs-contributing
   split (the +1 / +0.25 cases): the candidate is (a) kept in the planned set
   — never dropped; (b) NOT counted as contributing — coverage min and max
   are 1 from the primary alone, zero uncovered pixels; (c) recorded as
   zero-pixel-touch and the cut COMPLETES — planned-but-not-contributing is
   never an error. The cross-check now compares planned, opened, AND
   contributing/zero-touch sets against Yui's declared expectations wherever
   the fixture states them.

Results: round-1 **29/29**, round-2 **4/4**, round-3 **10/10** — separate
blocks, never summed. Full suite 30/30 with the new rule (round-1 corner and
margin semantics unchanged). Content-hash identity intact: excludes exactly
`['content_sha256','recorded_utc']`; two consecutive runs gave
`recorded_utc` 2026-08-15T17:46:37Z / 17:46:51Z with identical
`content_sha256 = 1eba47d8cef18d84941e6a85ffca010717825b7134cf8be72656b53f6a7561c7`.

Artifact hashes after this repair (supersede §0.2's):
`nm_brick_cutout_adapter.py`
`cd18ead45f4b77f2c1aaa505d5bce9c401f02eda4bd2e5cdfdb8c2bbe8f58128` (moved —
the repair is in the adapter, reported per the brief),
`cross_check_yui_boundary.py`
`74ad048178df66a5025d5516514d233d6d3eeedabe916b80088e5cd2315a80ad`,
`test_nm_brick_cutout_adapter.py`
`bffcd9d26cb72d0ab232e8ebd20b39e46b807cc7a623ebb8804dcc8cabdc3d45`.
Fixture pins unmoved: `24f55943…`, `60e3d662…`, `6b410fb4…`.

## 0.4. 2026-08-16 resampler gate — pixel-value equality closed

The deferred gap: all prior rounds verified planning, coverage, and source
sets, never pixel values (nearest-neighbour stand-in vs bilinear oracles).

**What changed:**

1. The adapter renderer is now a **bilinear resampler with the oracle's exact
   interpolation rule**: support window = output pixel centre within the
   source's interior pixel-centre window [1, N]; 0-based `x0 = floor(sx-1)`,
   `x1 = min(x0+1, N-1)` (edge clamp); float64 accumulation; mean over
   coverage; float32 output. Contribution semantics unchanged from the
   round-3 alignment.
2. The cross-check now stages **Yui's exact brick pixel data** — decompressed
   from her fixture trees and verified against her recorded per-brick
   `data_sha256` before staging — and compares the adapter's output arrays
   against her expected arrays (also hash-verified), per round, reported as a
   per-round `pixel_agreement` block. Counts remain separate, never merged.

**Results (all PASS):** round-1 29/29, round-2 4/4, round-3 10/10;
pixel agreement round-1 5 compared / 24 skipped, max abs error
`1.9073486328125e-06` vs tolerance 5e-6; round-2 4/4 compared, max
`7.62939453125e-06` vs 1e-5; round-3 10/10 compared, max
`7.62939453125e-06` vs 1e-5.

**Tolerance and its justification (not tuned to pass):**

- The bounds are **Yui's pre-declared numbers**, published in her fixture
  modules before this gate: 5e-6 (round-1 `render_fixture_oracle`
  `adapter_comparison_absolute_tolerance`) and 1e-5 (rounds-2/3
  `VALUE_TOLERANCE`).
- Exact float32 bit-equality is unreachable **in principle**: her expected
  arrays are analytic (float64 sky pattern at output-pixel world coordinates)
  while any real resampler interpolates float32-quantized rasters. The
  measured residuals sit exactly at that quantization floor:
  `7.62939453125e-06 = 2^-17` is **one float32 ulp** for values in [64, 128)
  — the fixture patterns run ~100–120 — and round-1's `1.907e-06 = 2^-19` is
  the corresponding scale at pattern values ~20. The residual is therefore
  fully accounted for by float32 quantization of the source rasters, with
  bilinear truncation and TAN-math differences (~1e-12 px) below it.

**Round-1 partial comparison, stated not papered over:** Yui's round-1 bricks
share ONE tangent plane (her declared approximation); the adapter's
production-shaped source model is per-brick TAN, displacing neighbour-brick
sampling by up to ~1.4 px at 0.25° from the shared tangent point. Value
comparison on the 24 neighbour-involving round-1 cases would measure that
fixture-model gap, not the resampler, so they are skipped with this reason
recorded in the receipt; the 5 centre-brick-only cases (where the models
coincide identically) are compared at 5e-6. Rounds 2–3 use distinct per-brick
tangent points and are value-compared in full. **No open question against any
fixture**: the oracle and adapter agree on every comparable case.

**What this gate does NOT claim (item 6):** equivalence with the hash-pinned
Imagine/astrometry.net production resampler kernel. That claim is only
meaningful against **Yui's dependency lock** (separate deliverable, in
progress) and is referenced there, not asserted here — this gate proves
oracle-bilinear semantics on synthetic rasters.

**Identity:** `content_hash_excludes` still exactly
`['content_sha256','recorded_utc']`; two consecutive runs gave `recorded_utc`
2026-08-16T03:21:45Z / 03:22:38Z with identical
`content_sha256 = a8a5e998549c6b66732591b5ca0c3b5fbf37b076ac29080c33bea99a16cde586`.

**Artifact hashes (supersede §0.3's):**
`nm_brick_cutout_adapter.py`
`267b2a93d2a61f65b281aeb3b04dd874d7add058797b10f593cb3efb4066006f`,
`cross_check_yui_boundary.py`
`e4168e331148feb9d348e30dcd10427f572492dfbedab141b745b8e3c34c691d`,
`test_nm_brick_cutout_adapter.py`
`d077ef35846340b31694…` (full value in SELFTEST.md).
Fixture pins unmoved: `24f55943…`, `60e3d662…`, `6b410fb4…`; frozen V3
unchanged.

## 1. What this is

`nm_brick_cutout_adapter.py` is the build-gate deliverable for route binding
§11 step 2: the guarded local-cut adapter for the "Globus DR10.1 South bricks,
then cut locally" route, with synthetic fixtures only. It implements, offline:

1. **Brick mapping and the margin rule (§6.2)** — exact output TAN WCS, exact
   3600×3600 source TAN WCS per geometry row, pinned nine-point pixel-edge
   boundary polygons (0.5 / mid+0.5 / N+0.5 on each axis), and an inclusive
   polygon-intersection test in the gnomonic plane about the object. Primary,
   edge-neighbour, and corner-neighbour reasons are classified from unique-area
   adjacency; the 16.768" scalar is never used as the selection rule. Candidate,
   planned, opened, contributing, and zero-pixel-touch sets are recorded
   separately per output.
2. **The frozen cutting procedure (§7)** — 128×128, single band r, float32,
   the exact §7.2 WCS constants, nanomaggies, no route-induced transform, and
   work sorted by primary brick id / working-set signature so input order
   cannot change any output byte (proven by test).
3. **PC-3 as amended (§8)** — per-output receipt: exact constants, CRVAL→
   (64.5, 64.5) within 1e-6 px, negative determinant bound to the CD-term
   product, +1" RA decreases x / +1" Dec increases y, nine round-trip probes
   ≤1e-6 px, coverage plane hashed with minimum ≥1, and full source-set
   accounting. The pinned `validate_wcs_parity.py` is reused, not reimplemented
   (see §4 below for Kun's caveat).
4. **PC-4 twice (§9)** — the hash-pinned `fail_closed_wcs.py` policy runs on
   raw header cards **before any TAN object is constructed**, once per source
   header and again per synthesized output header, extended through this
   reviewed successor adapter with: duplicate-keyword, alternate-WCS-suffix,
   DP/DQ lookup-distortion, swapped-axes, exact-TAN-CTYPE, mixed CD+PC/CDELT,
   missing CRVAL/CRPIX, and nonfinite-coefficient rejections, plus a
   North-up/East-left parity requirement. No default-zero recovery path exists;
   the gate runs before anything resembling the Imagine `hdr.get('CD…', 0.)`
   fallback could.
5. **Transfer manifest + custody (§5)** — a sealed, sorted, tamper-evident
   dry-run manifest with per-file SHA-256, byte size, mtime, reason class,
   object binding (list, or hash above 1000 keys), the geometry sidecar bound
   by digest, and a Globus task *template* carrying `verify_checksum=true`,
   `sync_level=checksum`, `skip_source_errors=false`, `submitted=false`. A
   missing required file is terminal at seal time, not skippable. Cutting is
   resumable through an atomic `state.json` plus a hash-chained event log;
   a skipped object is a logged, counted event, never a silent gap. The
   270,577-file scale is addressed by per-object state keys, streamed 1 MiB
   hashing, and O(planned-set) work per object; resume-after-interrupt was
   proven byte-lossless by test.

## 2. The hard boundary, verified from source by test

The module is structurally incapable of transferring or fetching:

- imports are exactly `__future__, argparse, hashlib, importlib.util, json,
  math, re, struct, sys, datetime, pathlib, typing` — no `requests`, `urllib`,
  `httpx`, `socket`, `http.client`, no Globus SDK, no `subprocess`, no `os`;
- there is no fetch(), submit(), download(), upload(), or transport class —
  where the predecessor `nm_acquire_cutouts.py` still had a `MockTransport`,
  this adapter has **no transport abstraction at all**: sources are local
  synthetic files it validates by digest, and the manifest is a sealed record
  that nothing in the module can issue;
- the CLI exposes only `--dry-run` (manifest-only) and exits with
  `BUILD_ONLY_STOP` otherwise;
- `test_static_source_has_no_transport` re-proves the import set by AST scan on
  every run, so any future edit that adds a transport fails the suite.

## 3. Deliverables and custody

| File | SHA-256 (post-repair, 2026-08-16 01:03 KST) |
|---|---|
| `nm_brick_cutout_adapter.py` | `f3c71021f9e01051363dad5a0bd5128b5f398234b5f37c552d267fade7fb658a` |
| `test_nm_brick_cutout_adapter.py` | `9b8b6fd0706bb81651b0c928554a1e3f4c663717d1f0689dabbe696b3fb9e39c` |
| `cross_check_yui_boundary.py` | `8a1a77b61a71adb36699e56ba05167736425760935c4534a1b80fb946432e4ab` |

(Pre-repair adapter `3422f249…ec4913` is the artifact Kun's hold gated; it is
superseded by the hash above.)

Pinned inputs (verified at import and by test):

- route binding `TORI_ROUTE_BINDING_20260815.md`
  `c7ed11c12ad7c26db8ce784b4d4d76c86694231d4eaab42b3ddca720a265d4cb`
- frozen `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md` (mode 444, unmodified)
  `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`
- `yui_bs5_sign_anchor_20260814/validate_wcs_parity.py`
  `7bf0201917e7722ee9545c9c11b6cc1cbdec345504e3f29fa1aeb01e58edaa55`
- `_tori_bs7_distortion_evidence/fail_closed_wcs.py`
  `cae1b1b7ef4e25000ad5d8c906647216b1425638ac737b4ea7363ca948760569`

Self-test: `SELFTEST.md` — 27/27 tests pass, Python 3.9.6, all fixtures
synthetic, all boundary counters zero.

## 4. Kun's PC-3 validator caveat, answered

Kun's caveat: `validate_wcs_parity.py` was built for a different regime —
confirm it is valid for headers **we synthesise**, or state precisely what
extra check is needed.

Finding: the pinned validator is a **position-free synthetic template**. It
supplies three things that remain valid for synthesized headers: the 2×2
algebra (`determinant_2x2`, `multiply_2x2`), the frozen row-order transform
convention, and the predicate set for the North-up/East-left template. It
never sees an actual header, so by itself it cannot validate a header we
synthesise — and it says so (`does_not_substitute_for_future_per_object_pc3`).

The precise extra checks needed, all implemented in `pc3_output_receipt` and
run on the **staged output bytes as written** (so post-generation tampering is
caught, which the tamper test proves):

1. exact §7.2 keyword-by-keyword constant equality on the parsed header;
2. determinant equality with the product of the frozen CD terms (finite,
   nonzero, negative — not just sign);
3. CRVAL→(64.5, 64.5) centre mapping within 1e-6 px;
4. +1" RA / +1" Dec perturbation direction tests;
5. pixel→sky→pixel round trips at the centre, the four near-corner pixel
   centres, and the four pixel-edge corners, ≤1e-6 px;
6. PC-4 (pinned policy + successor extensions) re-run on the same parsed
   output header, ahead of any WCS object construction.

The header-derived matrix is still pushed through the pinned validator's
row-order transform and predicates, so the frozen convention anchor is the
pinned code, not a re-derivation.

One further finding while binding the determinant: the route binding's §7.2
human-readable literal `-5.296604938271605e-09` is one unit in the last place
away from the true double-precision product of its own frozen CD terms,
`-5.2966049382716055e-09`. The adapter binds to the CD-term product (the CD
terms are the byte-bound constants); flagging the literal for Kun rather than
silently adopting either value.

## 5. Limits — what this build does NOT establish

These are declared in every COMPLETED receipt and are obligations of the
environment-lock and later gates, not silent gaps:

1. **Renderer stand-in.** Rendering is a deterministic nearest-neighbour
   sampler sufficient to prove planning, coverage accounting, zero-coverage
   rejection, and atomic acceptance. Production must use the hash-pinned
   Imagine/astrometry.net resampler (§7.1 code custody) inside the locked
   environment, and the fixture matrix must be re-run there (Kun re-gate).
   Weighted accumulation per the pinned implementation replaces the mean.
2. **FITS read path stand-in.** Synthetic bricks are uncompressed primary-HDU
   FITS read by a pure-stdlib parser; production reads `.fits.fz` image HDU 1
   via pinned fitsio. The custody order (digest before open, gate before
   parse) carries over unchanged; the byte-level reader does not.
3. **No dependency/container lock.** This module is deliberately
   stdlib-only, which makes the no-transport property provable, but the
   environment lock (astrometry.net, legacypipe, fitsio, numpy, scipy,
   Python, OCI digest) is a separate mandatory deliverable before execution.
4. **Manifest digests are synthetic.** Real source-side SHA-256, sizes, and
   mtimes must come from NERSC at the manifest-only gate (§11 step 4); every
   synthetic record carries `synthetic_stand_in: true` so it cannot be
   mistaken for source custody.
5. **Fixture geometry is a synthetic grid.** The margin rule is exercised on
   an equatorial 0.25° grid including an RA-wrap case; declination-extreme
   rows of the real DR10 South brick table (§8.3) must be exercised at the
   canary gate with the real geometry sidecar. Multi-process scheduling
   determinism (§8.3 last item) is likewise deferred to the locked
   environment; this build proves input-order determinism single-process.
6. **The invalid-fraction cap is a BINDING SLOT.** The adapter takes it as an
   explicit required parameter and records it; its frozen value belongs to
   Yui's input-function receipt, not to this adapter.

## 6. Zero-transfer receipt

- Globus endpoints activated: 0; tasks submitted: 0; manifests executed: 0
- survey files listed or fetched: 0; real cutouts generated: 0
- catalogue rows or positions read: 0; sky statistics: 0
- publication/acceptance/commit/push: 0

Branch at build: `feat/paper-workflow-v2` (no commit made).

## 7. Exact next action

Kun reproducibility gate over this directory: reproduce the deliverable
hashes, re-run the suite, and adversarially check §4 and §5 above —
especially whether the successor PC-4 extensions and the declared stand-ins
are acceptable seams for the environment-lock gate. No manifest against the
real parent set, and no Globus anything, until §11 steps 3–5 pass.
