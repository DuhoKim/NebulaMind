# TORI route binding SUCCESSOR — public HTTPS explicit-batch bricks (route B), then guarded local cutting

Date: 2026-08-17 13:47 KST; amended 2026-08-17 (v2) after Kun's
`HOLD_IMAGE_METADATA_SCOPE` (`KUN_SUCCESSOR_BINDING_GATE_20260817.md`): the
pre-approval image-metadata gap is closed by an **approved byte ceiling**
design (§5.1.1, §11 step 5) rather than a full per-file metadata pass — the
reasoning is recorded in Named Difficulties item 2.
Owner: Tori, bounded paper route binding (successor draft)
Decision authority: Duho
Execution acceptance: Duho and Kun
Status: **DRAFT PROPOSAL — NOT BINDING. NOT EXECUTABLE. ZERO TRANSFER.**

> **This document is a proposal.** It becomes binding only after Kun gates it
> and Duho accepts and freezes it (new SHA-256, mode 444). Until then nothing
> in it authorizes a manifest, a retrieval, an endpoint, or a run.

## 0. Supersession mechanics and justification

### 0.1 What this document is

This is the successor to `TORI_ROUTE_BINDING_20260815.md` (SHA-256
`c7ed11c12ad7c26db8ce784b4d4d76c86694231d4eaab42b3ddca720a265d4cb`, mode 444).
The frozen binding is **not edited**: it stands byte-for-byte as the record of
what was previously bound and why, including its deliberate prohibition of
portal HTTP. This successor supersedes it by executing, exactly, the §6
amendment list of `ACQUISITION_ROUTE_DECISION_20260816.md`. Section numbers
below mirror the frozen binding so every clause can be diffed against its
predecessor; sections marked NO AMENDMENT are carried by reference,
byte-unchanged in force.

### 0.2 Why route B — recorded so no future reader must reconstruct it

Duho chose route B on measured facts, not assumption:

1. **Route A (Globus/NERSC DTN) is blocked by measurement.** The NERSC DTN
   cosmo collection (`cb7bdf79-dfd8-4d50-a6bd-5bec2a505935`) stops at an
   identity wall: *"You are required to authenticate with an identity from
   NERSC (nersc.gov)."* No consent was granted, no identity linked, zero bytes
   moved (`GLOBUS_ANONYMOUS_ACCESS_TEST_20260816.md`). Whether a bare NERSC
   account would suffice (vs `cosmo` membership) remains untested and is moot:
   the weaker condition is already unmet.
2. **Route B's custody condition is satisfied on both limbs.** The frozen
   binding's prohibition of portal HTTP existed because route B, without a
   source-side digest, could not satisfy the §4.2 byte-binding. That premise
   has been dissolved by measurement:
   - **Coverage:** the survey publishes one checksum file per brick directory
     (`legacysurvey_dr10_south_coadd_<AAA>_<BRICKNAME>.sha256sum`), 58 entries
     for a full-band brick including `image-r`
     (`CHECKSUM_MANIFEST_FINDING_20260816.md` — including its CORRECTION
     section, which retracts the earlier "no coverage" finding and records the
     truncated-enumeration error that produced it).
   - **Currency:** **closed favourably by direct measurement**
     (`CHECKSUM_FRESHNESS_RESOLVED_20260817.md`): two DR10.1-replaced bricks
     from widely separated keyspace ranges (`0037m392`, `2393m140`) carry
     digests written 26 Jul 2023, days after their images were regenerated on
     18–19 Jul 2023, while an untouched control in the same `AAA` as the
     first (`0030m167`) retains its Nov 2022 digest. That
     is a targeted re-hash of the replaced set. The silent-verification hazard
     named in the decision memo §3 does not obtain for DR10.1.

   These survey-published digests are source-side digests computed by the data
   owners at NERSC — arguably better provenance than our own hashing job would
   have been. **This is why the prohibition is lifted as legitimate custody,
   not accepted as degraded custody.**
3. **The release stays DR10.1** per `DR10_1_RETAINED_DECISION_20260817.md`;
   Dustin Lang's suggestion to use DR11 is a separate, large decision the
   frozen parent set does not permit implicitly, and it is not taken here.

### 0.3 What route B costs, stated up front

Route B trades a DTN's hours for **weeks of polite retrieval** under the
frozen pacing rule of §5.4, and it depends on NERSC's tolerance rather than
its blessing. NERSC network operations are documented as blocking traffic
*"when they see what looks like DOS"*, and ~270k sequential HTTPS requests is
that shape. The pacing rule is therefore frozen with concrete values and a
stop-on-first-block custody discipline; it is not optional and not slow by
accident.

## 1. Verdict (AMENDED)

Duho selected the bulk route in its route-B form: retrieve the exact DR10.1
South r-band brick images needed by the frozen parent set by **explicit-batch
HTTPS retrieval from the NERSC portal tree**
(`https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/...`), then make
the frozen 128 × 128 float32 r-band cutouts locally with the gated adapter.
"Bulk bricks, then guarded local cutting" is unchanged from the frozen
binding; only the byte-delivery channel is amended.

This successor replaces only the acquisition route referenced by §6 of
`PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md`. It does not change the
frozen input contract, sample, estimator, thresholds, exclusions,
interpretation, or stopping rules.

The route is not yet open. Kun's gate on this successor, Duho's acceptance and
freeze, the manifest-only gate with its requirements (§11 step 4), and Duho's
explicit approval of the URL manifest hash, byte total, AND pacing plan (§11
step 5) are all mandatory before any retrieval begins.

## 2. Frozen custody of this successor's inputs

| Input | SHA-256 |
|---|---|
| predecessor `TORI_ROUTE_BINDING_20260815.md` (frozen, unedited) | `c7ed11c12ad7c26db8ce784b4d4d76c86694231d4eaab42b3ddca720a265d4cb` |
| `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md` (frozen, mode 444) | `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7` |
| `ACQUISITION_ROUTE_DECISION_20260816.md` (Lana's memo; §6 executed here) | `def682f1bc5243d2fecc53f2e875772907c98bc7a25290e957e525d245d772c6` |
| `GLOBUS_ANONYMOUS_ACCESS_TEST_20260816.md` (route A blocked, measured) | `09cafb4d3acba4f5c85c97f1f5ac54274bea577d94da7189347580f7a2389e21` |
| `CHECKSUM_MANIFEST_FINDING_20260816.md` (coverage, incl. CORRECTION) | `6b2df83f6a127564dbcff9495cbe39eddfa700df7f08e8325184d36f6ceefa97` |
| `CHECKSUM_FRESHNESS_RESOLVED_20260817.md` (currency, R3 closed) | `d7071cde9fe086c49a117825847c8249a8aac6e423e3d114df34a788f14403e9` |
| `MANIFEST_GATE_REQUIREMENTS_20260816.md` (R1/R2/R3/R4) | `8b802e307519a6c53af0e59d5ae09207f7d94fdf76791c919829db8e45a89bea` |
| `DR10_1_RETAINED_DECISION_20260817.md` (release stays DR10.1) | `6f1b7ebe3191831a551ab560ebc0de30cb56f8b697d60fb84a34ad408fc59d9d` |

The frozen V3 image contract carries unchanged: one band `r`; exactly
`128 × 128`; float32 to the estimator; `0.262 arcsec/pixel`; no route-induced
resize, crop, rotation, clipping, normalization, or band combination; coadd
nanomaggies per pixel.

## 3. Required primary-thread quotations — NO AMENDMENT

Carried unchanged from the frozen binding §3. The thread record supports
local brick-cached cutting; it is delivery-channel-independent.

## 4. Exact survey product and source location

### 4.1 Pixel product (AMENDED: URL replaces CFS path)

Product: latest DR10.1-replaced bytes in the DR10 South coadd tree, r-band
stacked image. For every source brick `BRICKNAME`, define
`AAA = BRICKNAME[0:3]` and require exactly:

`https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/coadd/<AAA>/<BRICKNAME>/legacysurvey-<BRICKNAME>-image-r.fits.fz`

The portal tree visibly mirrors the CFS tree the frozen binding named; the
bytes on offer are the same files. Image geometry (TAN, 3600 × 3600, 0.262
arcsec/pixel, nanomaggies, compressed image HDU 1) carries unchanged.

### 4.2 Byte-binding for "DR10.1" (AMENDED — the crux clause)

DR10.1 replaced affected coadds in place; path, filename, and release label
prove nothing about version. Under this successor each source file is bound by:

- the **survey-published per-file SHA-256**, taken from that brick's published
  checksum file
  (`legacysurvey_dr10_south_coadd_<AAA>_<BRICKNAME>.sha256sum`), whose own
  URL, byte size, and SHA-256 are pinned in the sealed manifest **before any
  image byte moves** — the checksum files are themselves custody inputs;
- checksum currency verified against the DR10.1 replacement evidence
  (`CHECKSUM_FRESHNESS_RESOLVED_20260817.md`), with a **standing
  re-verification at manifest time** (§11 step 4c) because that finding
  measures the tree as it stood on 2026-08-17 and any future in-place fix
  would reopen it;
- source byte size, **recorded at retrieval time**: the image response's
  `Content-Length`, required equal to received bytes (§5.2). The published
  checksum files carry digests and filenames only — **no sizes** — so no
  pre-approval per-file size exists under route B; the pre-approval scale
  control is the approved byte ceiling of §5.1.1 instead;
- the HTTP **`Last-Modified`** value, likewise **recorded at retrieval
  time**, in place of the CFS modification timestamp and **explicitly
  labelled WEAKER EVIDENCE**: it is a server header, not filesystem metadata
  we observed, and it participates in the record as corroboration, never as
  the binding itself. The binding is the digest.

A later byte change at the same URL is a different input and requires a new
source manifest and re-gate — unchanged in force from the predecessor. The
trust root under route B is stated openly: **survey-published checksum files
+ TLS channel integrity + portal host identity.**

### 4.3 Geometry sidecar (AMENDED: URL; digest coverage noted)

`https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/survey-bricks-dr10-south.fits.gz`,
bound by its survey-published digest in
`dr10/south/legacysurvey_dr10_south.sha256sum` (verified to exist and to
postdate the sidecar file). Its source digest, size, URL, and local SHA-256
are mandatory manifest fields, as before.

## 5. Retrieval custody (AMENDED throughout)

The Globus source collection UUID is **removed** — no collection, no
endpoint, no DTN. The prohibition of the frozen binding §5 is **re-scoped,
not deleted**:

- **Still forbidden:** recursive retrieval; wildcard expansion at execution
  time; directory mirroring or crawling; HTTP range requests; public
  cutout-service calls; any retrieval of a URL not listed in the approved
  sealed manifest.
- **Newly permitted, exhaustively:** (i) explicit per-file, full-file HTTPS
  `GET` of manifest-listed URLs from the portal tree, under the frozen pacing
  rule of §5.4; and (ii) the bounded, receipted `HEAD`-only size sample of
  §5.1.1 (1,024 manifest-listed image URLs, no body bytes, never a range
  request) at §11 step 4d. Nothing else. A `HEAD` request is not a licence
  for range requests, which remain forbidden.

### 5.1 Pre-transfer sealed manifest (AMENDED fields)

Before any image retrieval, write and hash a sorted manifest with one record
per file:

- `release = dr10.1-latest-byte-bound`;
- **absolute source URL and portal host** (replaces collection UUID + CFS
  path);
- destination relative path;
- brickname and `AAA`;
- product `image-r` or geometry sidecar;
- **survey-published SHA-256, plus a provenance record of the checksum file
  it came from** (that file's URL, bytes, digest, and retrieval receipt).
  The checksum harvest supplies **digests only**: the published `.sha256sum`
  files carry digests and filenames, no sizes. Per-file byte size and
  `Last-Modified` are NOT sealed-manifest fields under route B — they are
  recorded at retrieval time (§4.2, §5.2); the sealed manifest instead
  carries the batch-level approved byte ceiling and its sampling receipt
  (§5.1.1);
- reason: primary brick, edge neighbour, corner neighbour, or geometry
  sidecar;
- sorted list or hash of private object IDs requiring the source file;
- **coverage class (new, per R2):** `required` or `absent-by-coverage` — see
  §11 step 4b;
- manifest format version and creation time.

No source file may be added after the manifest hash is approved. A
`required` file that is missing is terminal, not skippable;
`absent-by-coverage` shapes the working set and is counted, never silently
skipped (§11 step 4b).

### 5.1.1 Approved byte ceiling and the size-sample metadata operation (NEW)

Under route A the pre-approval byte total was free (a filesystem stat at
NERSC). Under route B no survey-published size record exists, so an exact
pre-approval total would cost a full per-file metadata pass (~270k image-URL
`HEAD` requests) whose product is a server header with no custody standing —
it is the same uncorroborated `Content-Length` the retrieval itself must
re-verify, attested by nobody, and binding nothing (the digest binds). This
successor therefore replaces the exact pre-approval total with an
**enforceable approved byte ceiling**:

1. **Size sample (the only pre-approval image-URL operation authorized).**
   At §11 step 4d, issue `HEAD` requests — **no body transferred, HEAD only,
   never a range request** — against exactly **1,024** manifest-listed image
   URLs, stratified across the `AAA` keyspace of the working set, under the
   §5.4 tier-2 pacing (~20 minutes). Each request is receipted (§5.2
   metadata section). No other image-URL request of any kind is permitted
   before §11 step 6.
2. **Ceiling derivation, frozen:** `approved_byte_ceiling = (sample mean
   size) × (required file count) × 1.25`, recorded in the sealed manifest
   with the full sampling receipt (brick list, per-brick `Content-Length`,
   mean, standard error, derivation).
3. **Enforcement:** during retrieval, cumulative received bytes crossing the
   approved ceiling is a **terminal custody event** — stop, receipt, and a
   human decision by Duho, exactly like a block (§5.4.6). The campaign is
   structurally incapable of exceeding what Duho authorized.

What this trades, stated plainly: Duho approves an exact file count and an
enforceable byte bound rather than an exact byte total. The bound is
*stronger in one respect* than the predecessor's total — the frozen design
recorded the total in the receipt but had no mechanism forcing the transfer
to stay under it — and weaker in another: the a-priori number is an estimate
(±25% margin), not a census.

### 5.2 Downloader receipt (AMENDED: replaces the Globus task receipt)

The receipt covers **every network phase — the checksum harvest (§11.4a),
the size-sample metadata operation (§5.1.1), and the image retrieval — not
only the retrieval**. It must record, per file and per batch:

- per-file HTTP status; `Content-Length` vs bytes received (equality
  required); TLS peer identity (certificate subject/issuer/fingerprint of the
  portal host); retry count; digest-verify result against the sealed
  manifest;
- for the metadata phase: per-request method (`HEAD` only), URL, status, and
  reported `Content-Length` — zero body bytes;
- cumulative received bytes against the approved byte ceiling, with the
  §5.1.1.3 terminal custody event on crossing it;
- pacing parameters in force and the observed request rate and bandwidth;
- any 429, 403, block, throttle, or challenge event — each one a custody
  event with its own receipt (§5.4), never silently retried around;
- file count, total bytes, start/completion timestamps, terminal status;
- **zero skipped files** and **terminal-on-first-missing-required-file**.

The three Globus options of the frozen binding are replaced by **named
reimplemented equivalents**, which the downloader build must prove at its own
gate:

| Globus option (frozen §5.2) | Route-B equivalent (named, mandatory) |
|---|---|
| `verify_checksum = true` | post-receipt SHA-256 of every file against the sealed manifest digest; mismatch terminal |
| `sync_level = checksum` | **digest re-verification after any resume** — every file present at restart is re-hashed against the manifest before being counted; nothing is trusted from a prior interrupted session |
| `skip_source_errors = false` | **no skip code path exists at all** in the downloader — a required-file failure is terminal for the batch shard, structurally, not by configuration |

### 5.3 Destination acceptance — carries essentially unchanged

Receive files under a manifest-specific staging directory. For every file:
expected relative path and byte size; local SHA-256 equal to the approved
manifest digest; FITS opened only after digest equality (then only through
the gated read stage); atomic rename of the complete staging root only after
every record passes; append-only destination receipt. Extra files, missing
required files, checksum mismatch, a changed manifest, or a nonzero skipped
count closes the gate and preserves no accepted production root.

### 5.4 Pacing rule (NEW — frozen values, not judgement)

Scale: ~2.93 TB across 270,577 `image-r` files plus margin bricks. This
volume as unpaced sequential HTTPS is the traffic shape NERSC operations
block. The following values are **frozen**; changing any of them requires a
successor amendment, not run-time judgement:

1. **Concurrency: 1.** Strictly serial; one connection; no pipelining.
2. **Request spacing:**
   - image files: next request no sooner than **max(2.0 s after the previous
     request started, completion of the previous transfer)**;
   - checksum/metadata files (~6 KB each): next request no sooner than
     **1.0 s** after the previous started.
   (Ancestry: the gated build-only acquisition pipeline froze 5.0 s serial
   against a compute-backed cutout service; a static-file portal justifies
   the lighter interval, and Kun/Duho may tighten these at the gate.)
3. **Bandwidth ceiling: 25 MB/s** sustained.
4. **Retrieval windows:** bulk retrieval only 20:00–08:00 US/Pacific on
   weekdays, any hour on weekends (NERSC-local off-peak).
5. **Transient network errors** (timeouts, resets without a block signal):
   backoff ladder 30 s / 60 s / 120 s, then terminal for that file — carried
   from the gated predecessor.
6. **STOP-ON-FIRST-BLOCK:** the first 429, 403, block page, challenge, or
   rate-limit signal of any kind halts the entire campaign immediately. It is
   **a custody event to receipt, not something to retry around**: write the
   receipt (timestamp, URL, response, pacing state), and resumption requires
   a **human decision by Duho** — with digest re-verification of everything
   already on disk (§5.2) — never an automatic retry.

**Honest wall-clock statement.** The pacing floor is ~270,577 × 2.0 s ≈ 150
hours for the image campaign, plus ~75 hours for the checksum harvest
(§11 step 4a), plus ~20 minutes for the 1,024-request size sample (§5.1.1) —
before transfer time and window restrictions. (A full per-file image-metadata
pass was considered and rejected precisely because it would have added
another ~75–150 hours of requests for a number with no custody standing; see
Named Difficulties item 2.) Within the frozen windows the total is
realistically **on the order of a month of polite retrieval, versus hours on
a DTN.** That cost is accepted as part of choosing route B; nobody later gets
to treat the pacing rule as optional because it is slow.

## 6–10. Brick mapping, margin rule, local-cut procedure, PC-3, PC-4, code-gap obligations — NO AMENDMENT

These sections are delivery-channel-independent and carry **byte-unchanged in
force** from the frozen binding. Status note (informational, amending
nothing): the §10 implementation obligations have since been discharged and
gated on synthetic fixtures — the guarded adapter
(`nm_brick_cutout_adapter.py`, `267b2a93…`, stdlib-only through seven gates),
the pinned read/decompression stage (`readstage/nm_brick_read_stage.py`), the
five-round Yui cross-check (29/4/10/3/9, separately counted), and the
multiprocessing determinism harness. The environment/dependency lock remains
Yui's open deliverable and is unchanged by this successor.

## 11. Gate sequence (AMENDED steps 4, 5, 6; others carried)

No steps may be collapsed:

1. **Paper acceptance:** Duho accepts this successor route wording. — carried.
2. **Build gate.** — carried (discharged on synthetics; see §6–10 note).
3. **Kun reproducibility gate.** — carried (standing).
4. **Manifest-only gate — AMENDED, with a named deviation.** Under route A
   this step was "compute the working set and sealed manifest; transfer
   nothing." Under route B, sealing the manifest **requires retrieving the
   per-brick checksum files first**, which is itself a network campaign of
   ~the working-set cardinality. This successor re-scopes the step openly
   rather than pretending otherwise — **no image byte moves in step 4, but
   checksum/metadata retrieval is permitted under the §5.4 pacing rule**:
   - **(a) Checksum harvest:** retrieve the `.sha256sum` file of every brick
     in the complete working set (primaries and all margin bricks), paced per
     §5.4 tier-2, each pinned (URL, bytes, digest) into the manifest.
   - **(b) Coverage census (R1 + R2 of
     `MANIFEST_GATE_REQUIREMENTS_20260816.md`, incorporated here):** from the
     harvested checksum files, verify r-band coverage for **every margin
     brick, not just primaries** (r-band is not universal: sampled i/WISE-only
     bricks carry 31-entry manifests and no `image-r`). Classify every
     required brick `required` vs `absent-by-coverage` in the sealed record —
     the first stays terminal-if-missing, the second shapes the working set.
     Report **aggregate counts only** (objects with complete r-band margin
     sets vs not; no rows, no positions, no sky statistic) **before manifest
     approval**. A non-zero incomplete count is not automatically fatal but
     must be quantified, disclosed, and its position-correlation assessed
     before approval.
   - **(c) Digest-currency re-verification (R3 standing check):** re-confirm,
     on the tree as it stands at manifest time, that replaced-brick digests
     still postdate their images (the 2026-08-17 measurement is of that day's
     tree; a future in-place fix would reopen the question).
   - **(d) Size sample (§5.1.1):** the 1,024-request stratified image-URL
     `HEAD` sample, paced per §5.4 tier-2 and receipted, deriving the
     approved byte ceiling. This is the only image-URL operation permitted
     before step 6, and it transfers no body bytes.
   - (R4 of the same document is satisfied by this successor existing and
     being gated **before** the manifest gate runs — recorded here.)
5. **Retrieval approval — AMENDED:** Duho explicitly approves the URL
   manifest hash, destination, **exact file count, the approved byte ceiling
   with its sampling receipt (§5.1.1)**, and **the pacing plan** (§5.4 values
   restated in the approval record). The ceiling is enforceable during
   retrieval, not advisory.
6. **Paced explicit-batch HTTPS retrieval — AMENDED:** replaces the Globus
   task; §5.2 receipt mandatory; §5.4 governs throughout.
7. **Destination acceptance:** per-file digest equality against the sealed
   manifest — carried unchanged in substance.
8. **Local-cut canary.** — carried.
9. **Production approval.** — carried.

Until step 5, no image byte may be requested. Until step 8 passes, no
production shard may run.

## 12. Zero-transfer receipt of this drafting lane

This lane performed document drafting and hash verification only.

- network calls: 0; files fetched: 0; endpoints activated: 0; consents: 0
- image bytes retrieved: 0; checksum files retrieved by this lane: 0
- manifests built or sealed: 0; retrievals executed: 0
- catalogue rows/positions read: 0; sky statistics: 0
- `TORI_ROUTE_BINDING_20260815.md`: **unmodified**, hash verified
  `c7ed11c1…` before and after drafting; mode 444
- frozen V3 prereg: unmodified, hash verified
- commit/push/publication/acceptance: 0

## 13. Exact next action

Kun gates this successor against the frozen binding and the §6 amendment
list. On Kun's pass, Duho accepts and freezes it (new SHA-256, mode 444);
only then does the §11 step-4 manifest-only gate become runnable. Nothing
before that point — and nothing in step 4 itself — touches an image byte or
a real galaxy.

## Named difficulties (per the drafting brief: reported, not papered over)

1. **§11 step 4 could not carry cleanly.** The frozen "manifest-only gate:
   transfer nothing" is impossible under route B as literally written,
   because the source digests live in ~one checksum file per brick and must
   be fetched to be pinned. The re-scope (no image bytes; paced
   checksum/metadata retrieval permitted) is stated openly in §11.4 rather
   than absorbed silently; Kun should gate that re-scope as a deliberate
   custody change, and the added ~75-hour paced harvest is included in the
   wall-clock statement.
2. **§5.1 "source byte size and modification time" cannot exist pre-approval
   under route B at all** (Kun's `HOLD_IMAGE_METADATA_SCOPE`): the published
   checksum files carry digests and filenames only, and the v1 draft's
   derivation of sizes "from the checksum harvest" was simply wrong — a
   checksum file's `Content-Length` is its own size, not the image's.
   **Decision record for the repair.** Two designs were on the table:
   (a) authorize a full per-file image-`HEAD` pass so the exact byte total
   exists pre-approval (Kun's repair instruction); (b) drop the exact
   pre-approval total and make approval bind a file count plus an enforceable
   byte ceiling (his named alternative). This successor takes **(b),
   hardened**, for three reasons. First, the full pass buys a number with no
   custody standing: image `Content-Length` via `HEAD` is the same
   uncorroborated, unattested server header the retrieval GET returns and
   must re-verify anyway — it binds nothing (the digest binds), and it can
   change between `HEAD` and `GET`. Second, it costs ~270k additional
   requests against the very host whose tolerance is this route's scarcest
   resource — spending the politeness budget to compute a courtesy figure
   inverts the pacing rule's purpose. (The suggested combined per-brick sweep
   does not halve this: pacing is per request, and checksum-`GET` plus
   image-`HEAD` is the same two requests per brick as two passes.) Third, the
   ceiling is *enforceable* where the predecessor's exact total was
   informational: retrieval structurally cannot exceed what Duho approved
   (§5.1.1.3), which the frozen design never guaranteed. What is genuinely
   lost and stated as lost: the a-priori figure is an estimate with a frozen
   +25% margin, not a census. Per-file sizes and `Last-Modified` are recorded
   at retrieval time, the latter still labelled weaker evidence, digest
   carrying the binding alone.
3. **The pacing values are frozen but not survey-blessed.** 2.0 s / 1.0 s /
   1-connection / 25 MB/s / off-peak are our politeness constants, grounded
   in the gated predecessor's precedent and the static-file cost profile —
   not in any NERSC-published rate limit, because none is published. If the
   survey or NERSC ever states a preferred rate, that statement supersedes
   these values downward (stricter) without re-gate, but never upward.

## Sources

[1] `ACQUISITION_ROUTE_DECISION_20260816.md` §6 (amendment list executed
here), §4 (scale and DOS-shape risk), §5 (conditional recommendation).
[2] `GLOBUS_ANONYMOUS_ACCESS_TEST_20260816.md` (route A identity wall,
measured 2026-08-16).
[3] `CHECKSUM_MANIFEST_FINDING_20260816.md` including its CORRECTION
(per-brick checksum coverage; the truncated-enumeration error mechanism).
[4] `CHECKSUM_FRESHNESS_RESOLVED_20260817.md` (R3 closed favourably by
RELEASE=10002 brick sampling).
[5] `MANIFEST_GATE_REQUIREMENTS_20260816.md` (R1, R2, R4 incorporated at §11
step 4; R3 as standing re-verification).
[6] `DR10_1_RETAINED_DECISION_20260817.md` (release retention).
[7] `TORI_ROUTE_BINDING_20260815.md` (frozen predecessor; all NO-AMENDMENT
sections carried from it).
