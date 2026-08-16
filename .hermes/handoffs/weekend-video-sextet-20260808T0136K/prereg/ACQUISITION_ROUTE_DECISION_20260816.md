# Acquisition route decision memo — Globus/NERSC DTN (A) vs public HTTPS portal (B)

**Lana (science / claim-boundary seat), 2026-08-16. Status: DECISION MEMO FOR DUHO — this
document decides nothing.** Adopting either route is Duho's call. Written offline: NO network
access was used; nothing was fetched, probed, transferred, or activated; no endpoint touched; no
real survey data exists in this lane. The frozen route binding
`TORI_ROUTE_BINDING_20260815.md` (SHA-256
`c7ed11c12ad7c26db8ce784b4d4d76c86694231d4eaab42b3ddca720a265d4cb`) is **not amended** by this
memo; if B is chosen it is amended by a successor binding and a new freeze, never edited in
place.

---

## 1. Why this memo exists

Every synthetic pre-transfer gate is closed. The critical path is data access, and the bound
route (A) requires something no agent can produce: NERSC access for Duho (the brief states
`cosmo` project access; the exact requirement — any NERSC account vs `cosmo` membership — is
itself worth confirming with NERSC, since it changes how hard A is). NERSC accounts come via a
PI adding you to a project or an ERCAP allocation; neither is quick or certain for a one-human
project. So the honest question is: what does the frozen custody design actually lose if the
same bytes come over public HTTPS instead — and under exactly what conditions is that loss
acceptable?

**The two routes:**

- **A — Globus / NERSC DTN (currently bound).** Source collection UUID
  `9d6d994a-6d04-11e5-ba46-22000b92c6ec`, CFS paths under
  `/global/cfs/cdirs/cosmo/data/legacysurvey/dr10/south/coadd/…`, source-side SHA-256 computed
  at NERSC, Globus task with `verify_checksum`, sealed pre-transfer manifest (binding §4, §5).
- **B — public HTTPS.** `portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/…`. DR10 is public
  data, and the portal path visibly mirrors the same CFS tree, so the *bytes on offer* should be
  identical. The binding currently **forbids** this route explicitly (§5: "portal HTTP, wildcard
  expansion, range requests, or public cutout calls are forbidden"). That prohibition was a
  deliberate custody choice, and this memo treats it as such — B is adoptable only by openly
  amending it, not by reinterpreting it.

Either way the downstream plan is identical: bulk bricks in, frozen local 128×128 r-band
cutting, amended PC-3/PC-4 on our code. **B changes only the byte-delivery channel.** Binding
§§6–10 (brick mapping, local-cut procedure, PC-3, PC-4, code-gap obligations) are
route-independent and carry unchanged under either choice.

## 2. What each custody clause actually buys, and what survives under B

| Clause (binding §) | What it buys | Under B |
|---|---|---|
| Explicit file batch; no wildcards; no recursive transfer (§5) | The input set is exactly the approved list — nothing rides in on a glob | **Survives.** An explicit per-file URL list driven by the sealed manifest is the same discipline. Never a crawler, never a directory mirror. |
| Per-file byte size verification (§5.1, §5.3) | Truncation detection | **Survives.** Record expected size in the manifest; require `Content-Length` agreement and received-byte count equality; terminal on mismatch. |
| Per-file SHA-256 verification (§5.1, §5.3) | Bit-exact identity of each input | **Conditionally survives** — only if a *source-side reference digest* exists. See §3; this is the crux. |
| `verify_checksum`, `sync_level=checksum`, `skip_source_errors=false` (§5.2) | Globus-native transit verification, safe restart, no silent skip | **Does not survive as a protocol feature.** These are Globus task options. Equivalent behavior must be *reimplemented and receipted* in the downloader: digest re-verification after any resume, retry-then-terminal on mismatch, no skip path in the code at all. |
| Terminal failure on a missing required file (§5.1) | The working set is complete or the gate closes | **Survives.** HTTP 404/403 on a manifest file = terminal for the batch, exactly as a missing CFS file is under A. |
| Sealed pre-transfer manifest, hash approved before bytes move (§5.1, §11 step 5) | Nobody — including us — can quietly widen or swap the input set after approval | **Survives intact.** The manifest records URLs instead of CFS paths; the seal-then-approve-then-fetch order is unchanged. |
| Source-side SHA-256 computed AT the source (§4.2, §5.1) | See below — this is the one that matters | **Does not survive as our own act.** It can be *replaced* by a survey-published digest, if one exists — §3. |

### The source-side hash, precisely

**What it protects.** A digest computed on the CFS filesystem at NERSC is a fixation of the
source bytes that never travels with the data. It buys three things:

1. **Transfer-independent corruption detection.** Any transit corruption, truncation, partial
   write, or destination-side alteration shows up as digest inequality against a reference the
   transfer could not have altered.
2. **The §4.2 byte-binding.** DR10.1 replaced affected coadds *in place* under the `dr10` paths,
   so path, filename, and release label prove nothing about version. A source-side digest at a
   recorded timestamp pins *which bytes* the study consumed, and makes any later in-place
   replacement legible as a different input requiring a new manifest and re-gate. This is the
   clause the whole DR10.1 versioning argument rests on.
3. **Drift detection.** If the source tree changes between manifest sealing and transfer, the
   transferred bytes mismatch the sealed digest and the gate closes.

**What it does not protect — do not let it inflate into a security argument.** It is custody
(fixation), not provenance (attestation). If the source tree is wrong, stale, or was tampered
with *before* we hashed it, the digest faithfully seals the wrong bytes. It trusts the compute
environment that ran the hash and the path resolution at that instant. It does not authenticate
the files as genuine DR10.1 science products, and it does nothing about choosing the wrong file
list. Route A holds no advantage over B on any of those failure modes.

**What B has without it.** HTTPS/TLS already provides per-connection integrity, and a careful
client catches truncation via length checks — so "the bytes got mangled in flight" is largely
covered by the channel itself. What hashing-only-what-you-received *cannot* do is items 2 and 3:
there is no transfer-independent evidence of what the source bytes were, so "the source changed"
and "my transfer corrupted" are indistinguishable without refetching, and the §4.2 byte-binding
clause **cannot be satisfied as written**. The honest custody claim degrades to "these are the
bytes host H served me over TLS at time T" — stateable, but weaker, and not what the frozen
design promises. (Fetching twice and comparing proves only channel consistency, not source
fixation; it is not a substitute and I do not propose it as one.)

## 3. The one fact Duho must verify — I cannot

**Does the survey publish per-file SHA-256 manifests for the DR10 South coadd tree, and do they
match the current (DR10.1-replaced) bytes?** I have no network and did not check. Do not let
anyone assert this from memory — this project has already once frozen a directional literature
claim written from memory and paid for it.

If such manifests exist, they *are* source-side digests — computed at NERSC by the data owners —
and route B recovers items 1–3 above, arguably with better provenance than our own hashing job
(it is the survey's attestation, not ours). Three sub-conditions, all mandatory:

- **Coverage:** the published manifests must cover every required product — the
  `legacysurvey-<BRICKNAME>-image-r.fits.fz` bricks *and* the
  `survey-bricks-dr10-south.fits.gz` geometry sidecar (binding §4.3). Partial coverage means a
  hybrid custody story; treat any uncovered required file as route-B-blocking.
- **Freshness vs DR10.1:** verify the checksum files postdate (or were regenerated with) the
  in-place DR10.1 replacements. Spot-check at least one brick named on the DR10 known-issues
  page as replaced. Note the failure asymmetry: a *stale checksum against current bytes*
  mismatches and fails closed (safe); the hazard is the portal serving *pre-replacement bytes
  that its stale checksum confirms* — internally consistent but not the latest bytes §4.2
  requires. The known-issues brick list is the cross-check for that.
- **Pin the manifests themselves:** each checksum file's URL, bytes, and SHA-256 go into the
  sealed pre-transfer manifest *before* any image byte moves. The trust root becomes
  (survey-published manifest + TLS + portal host identity), stated openly in the successor
  binding.

**Where to look:** the portal directory listings themselves
(`portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/coadd/<AAA>/<BRICKNAME>/` — earlier
Legacy Surveys releases shipped per-directory checksum files; verify the DR10 pattern rather
than assuming it), the DR10 files documentation at `legacysurvey.org/dr10/files/`, and — the
documented precedent for this exact kind of question — the `decam-legacy-survey` group, where
the May 2025 "NERSC cutout service?" thread lives. One post asking "are the published
sha256sums current with the DR10.1 replacements?" is cheap and in-scope for a human.

While verifying, two cheap A-side checks in the same session: whether the DTN collection truly
requires `cosmo` membership (vs any NERSC account), and whether the survey maintains a public
Globus guest collection — either would unblock A without an allocation.

## 4. Scale and the operational risk B adds

The 08-15 decision memo bounds the transfer at **~2.93 TB across 270,577 `image-r` files, plus
margin bricks**. Route A exists precisely because NERSC documents Globus/DTN as the mechanism
for transfers of this size; the same record quotes NERSC network operations blocking traffic
*"when they see what looks like DOS."* 270k sequential HTTPS requests against the portal is
exactly the shape that gets blocked — and a mid-transfer block is not just delay: resumption
must re-verify digests, and a block mid-batch is a custody event to receipt, not to retry
around.

If B is chosen, the successor binding must therefore also freeze a **pacing rule** (bounded
request rate, bounded concurrency, off-peak windows, immediate stop on the first 429/403/block
with a receipt and a human decision before resumption — the same lesson as our documented
throttle-pacing practice elsewhere). Full-file GETs only; the existing prohibition on range
requests stays. This is a real cost of B: days of polite wall-clock rather than a DTN's hours,
and a dependency on NERSC's tolerance rather than its blessing.

## 5. Recommendation

> **B (public HTTPS) is acceptable IF the survey publishes per-file SHA-256 manifests covering
> every required product (image-r bricks and the survey-bricks sidecar) and verified current
> against the DR10.1 in-place replacements — otherwise A (obtain NERSC access), because without
> a published source-side digest, route B cannot satisfy the §4.2 byte-binding as designed, and
> that clause is what the whole DR10.1 versioning argument rests on.**

Secondary conditions on B, both mandatory: the frozen pacing rule of §4 above, and the full
amendment list of §6 below executed as a successor binding + new freeze. If the published
manifests exist but fail the freshness cross-check, treat that as "manifests absent" — do not
rationalize a partially-verified custody story.

If the manifests do not exist and NERSC access is genuinely unobtainable, the honest fallback
ordering is: (1) ask the survey (the `decam-legacy-survey` group) to publish or point to current
checksums — cheap, documented-precedent channel; (2) only then consider a further-degraded
custody design, which would need its own decision memo and Kun gate — this memo does not
pre-authorize it.

## 6. If B is chosen: exact amendments to the route binding, by section

A binding is amended openly, never quietly reinterpreted. Every item below lands in a successor
to `TORI_ROUTE_BINDING_20260815.md`, written by Tori, gated by Kun, frozen with a new hash:

- **§1 (Verdict):** delivery mechanism reworded from Globus/DTN bulk transfer to explicit-batch
  HTTPS retrieval from the portal tree. "Bulk bricks, then guarded local cutting" is unchanged.
- **§4.2 (byte-binding):** "source-side SHA-256 … computed at NERSC before transfer" becomes
  "survey-published per-file SHA-256, whose checksum files are themselves pinned (URL, bytes,
  digest) in the sealed manifest before transfer, freshness-verified against the DR10.1
  known-issues replacement list." Source modification timestamp becomes the HTTP
  `Last-Modified` value, recorded as weaker evidence and labeled as such.
- **§5 (header + prohibition):** the source collection UUID is removed; the prohibition is
  re-scoped, not deleted — still forbidden: recursive/wildcard retrieval, range requests, and
  public cutout-service calls; newly permitted: explicit per-file full-file HTTPS GET of
  manifest-listed URLs from the portal tree, under the frozen pacing rule.
- **§5.1 (sealed manifest):** "absolute CFS source path" → absolute source URL + portal host;
  "source SHA-256 computed at NERSC" → survey-published SHA-256 + provenance record of the
  checksum file it came from. All other fields (release tag, destination path, brickname,
  product, reason, object-ID binding, format version) carry unchanged.
- **§5.2 (task fields):** the Globus task receipt is replaced by a downloader receipt: per-file
  HTTP status, `Content-Length` vs bytes received, TLS peer identity, retry counts,
  digest-verify result, pacing-rule parameters and observed rate, any 429/403/block events, zero
  skipped files, terminal-on-first-missing-file. The three Globus options are replaced by named
  reimplemented equivalents (digest re-verification after any resume; no skip code path).
- **§5.3 (destination acceptance):** carries essentially unchanged — expected path and size,
  local SHA-256 equal to the approved manifest digest, FITS opened only after equality, atomic
  rename of the complete staging root, append-only receipt.
- **§11 (gate sequence):** steps 1–4, 8, 9 unchanged. Step 5: Duho approves the URL manifest
  hash, byte total, and pacing plan. Step 6: paced explicit-batch HTTPS retrieval replaces the
  Globus task. Step 7: unchanged in substance (per-file digest equality against the sealed
  manifest).
- **§§6, 7, 8, 9, 10:** **no amendment.** Brick mapping, margin rule, local-cut procedure,
  PC-3, PC-4, and the code-gap obligations are delivery-channel-independent. Kun's
  reproducibility gate on the guarded adapter (§11 step 3) is identical work under either route.
- **§12/§13:** historical receipts of the 08-15 lane; not amended. The successor binding issues
  its own zero-transfer receipt at write time.

**Process, stated explicitly per the brief:** adopting B is Duho's decision. It requires a new
successor route binding and a **new freeze with a new SHA-256** — plus Kun's gate on the
successor — not an edit to the frozen, sha-pinned `TORI_ROUTE_BINDING_20260815.md`, which
survives byte-for-byte as the record of what was previously bound and why. The same holds in
reverse: if Duho obtains NERSC access, route A proceeds under the existing binding with no
amendment at all — which is itself an argument to spend a few days on the access question before
amending anything.

## 7. Boundary receipt

Network calls made: 0. Files fetched: 0. Endpoints activated: 0. Transfers: 0. Survey data
touched: 0. Sky statistic: none exists; K-8 untripped. Route binding amended: no. Commit/push:
none. Inputs read, with hashes verified where pinned: `TORI_ROUTE_BINDING_20260815.md`
(`c7ed11c1…`, matches), `ACQUISITION_ROUTE_DECISION_20260815.md`,
`_tmp_lana_acquisition_route_decision_brief_20260816.md`. The next step after Duho's
verification in §3 would still not touch real galaxies: it is either an access request or a
successor binding draft. Kun gates; Duho owns acceptance.

— Lana, 2026-08-16.
