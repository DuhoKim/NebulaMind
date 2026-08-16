# Checksum-manifest verification — the §3 question, answered

**2026-08-16. Verified by direct inspection at Duho's instruction, not from memory.**
Method: HTTP HEAD and directory listings only. Zero data bytes fetched, zero FITS files
downloaded, no endpoint activated, no transfer. The two `.sha256sum` files read in full are 289 and
294 bytes respectively.

## Question

`ACQUISITION_ROUTE_DECISION_20260816.md` §3: *does the survey publish per-file SHA-256 manifests
covering every required product, current against the DR10.1 in-place replacements?*

## Answer: NO — coverage fails

Two published checksum files exist, and both cover only top-level catalogue/summary products:

**`dr10/legacysurvey_dr10.sha256sum`** — 294 B, Last-Modified 2022-11-23. Three entries:
`ccds-annotated-decam-dr10.fits.gz`, `survey-ccds-decam-dr10.fits.gz`,
`survey-ccds-decam-dr10.kd.fits`.

**`dr10/south/legacysurvey_dr10_south.sha256sum`** — 289 B, Last-Modified 2023-12-22. Three entries:
`dr10-south-depth.fits.gz`, `dr10-south-depth-summary.fits.gz`,
**`survey-bricks-dr10-south.fits.gz`**.

| required product | published digest? |
|---|---|
| `survey-bricks-dr10-south.fits.gz` (geometry sidecar, binding §4.3) | **YES** — covered |
| `legacysurvey-<BRICK>-image-r.fits.fz` (270,577 files — the data) | **NO** — zero coverage |

There is no checksum file at `dr10/south/coadd/`, none at the `<AAA>/` level, and none inside brick
directories. A brick directory was listed in full: it contains the science products
(`legacysurvey-0001m002-image-r.fits.fz` among them) with no accompanying digest of any kind.
The earlier-release per-directory checksum pattern Lana flagged as worth checking **does not hold
for DR10**.

## Consequence — route B is blocked

Lana's coverage sub-condition is explicit: *"Partial coverage means a hybrid custody story; treat
any uncovered required file as route-B-blocking."* The uncovered product is not incidental — it is
the entire image dataset. The §4.2 byte-binding cannot be satisfied for a single brick under
route B.

**The conditional recommendation therefore resolves to route A: obtain NERSC access.**

## Freshness — not the binding constraint, but recorded

The sidecar's digest appears internally current: `survey-bricks-dr10-south.fits.gz` is
Last-Modified 2023-12-15 and its checksum file 2023-12-22, so the digest postdates the file. A
sampled brick `legacysurvey-0001m002-image-r.fits.fz` is Last-Modified 2022-06-17 — but a single
un-replaced brick proves nothing about the DR10.1 replacement set, and with no brick digests
published the freshness question is moot for the bricks. It was never reached: coverage failed first.

## What this does NOT establish

- It does not prove NERSC access is obtainable. That remains unanswered and is Duho's.
- It does not authorize anything. No manifest, no transfer, no endpoint, no sky.
- It does not amend `TORI_ROUTE_BINDING_20260815.md`, which stands frozen and unmodified —
  and under route A requires no amendment at all.
- The bricks having no published digest is a fact about the survey, not a defect in our design.

## Remaining live option before conceding

Lana's fallback ordering §5 is now the active path: ask the survey (`decam-legacy-survey` group)
whether current per-file checksums exist or can be published. Cheap, documented-precedent channel,
and it would reopen route B properly rather than degrading custody quietly.

Two A-side questions still worth asking in the same sitting: whether the NERSC DTN collection
requires `cosmo` membership or merely any NERSC account, and whether a public Globus guest
collection exists. Either would unblock A without an allocation.

## Boundary receipt

Network: directory listings and HEAD requests only, plus two checksum files totalling 583 bytes.
Data bytes fetched: 0. FITS files downloaded: 0. Endpoints activated: 0. Transfers: 0. Sky
statistic: none. K-8 untripped. Route binding: unamended. No commit, no push, no publication.

## Update — query sent 2026-08-16

Duho sent the query to `decam-legacy-survey@googlegroups.com` (subject: *"DR10: per-file checksums
for the coadd brick images?"*), asking three things: whether per-brick checksums exist or could be
published; whether the covered files' digests postdate the DR10.1 in-place replacements; and
whether Globus/DTN requires `cosmo` membership or a public collection serves the DR10 tree.

Lana's §5 fallback path is therefore executed, not merely available. Route selection now waits on an
external reply. A first post from a new member may sit in Google Groups moderation, so silence in
the short term is not a negative result.

**What each outcome means:**

- per-brick checksums exist or get published → route B reopens, and the successor binding of
  memo §6 becomes the work;
- no per-brick checksums, but DTN needs only a NERSC account (or a public Globus collection
  exists) → route A proceeds under the existing frozen binding with **no amendment at all**;
- no per-brick checksums and `cosmo` membership required → access becomes the sole blocker and
  the degraded-custody question returns, which memo §5 explicitly does not pre-authorize.

Nothing about this changes the build state: all five pre-transfer gaps remain gated and closed.

---

# CORRECTION — 2026-08-16, after Dustin Lang's reply. THE FINDING ABOVE IS WRONG.

**Per-brick checksums DO exist. Everything above that says otherwise is retracted.**

Dustin Lang (Legacy Surveys) replied 2.5 hours after the query and named the exact path:

    .../dr10/south/coadd/000/0001m002/legacysurvey_dr10_south_coadd_000_0001m002.sha256sum

Verified directly: HTTP 200, 6,039 bytes, **58 entries**, including
`legacysurvey-0001m002-image-r.fits.fz`. One checksum file per brick directory, covering every
product in it.

## How the error happened — mechanism, so it is not repeated

The brick directory listing has **60 entries. The checksum file is entry 60, the last one.**
`legacysurvey_` (underscore, `0x5F`) sorts after `legacysurvey-` (hyphen, `0x2D`), so all 58 data
files precede it alphabetically.

I printed **lines 2–30** and concluded no digests existed. I then reported *"I listed a brick
directory in full"* — which was false. Half the directory was never looked at, and the one file
that mattered was in the half I skipped.

This is the same error class the whole gate discipline exists to catch: **a partial view reported
as a complete one.** A truncating pipe is exactly as dangerous as a keyword check that matches a
prohibition, and I have now made both errors in one session. The lesson is not "look at more
lines" — it is that any absence claim must state the enumeration bound it was drawn from. "No
checksum file in lines 2–30 of 60" is a fact; "no checksum file" was not.

## Consequences — the route decision flips

Lana's coverage sub-condition is **satisfied**, not failed. Route B is **not** blocked.
`ACQUISITION_ROUTE_DECISION_20260816.md` §5 resolves toward B, subject to its remaining conditions:

- **Freshness is now the live question and is UNANSWERED.** Dustin did not address question 2.
  Sampled: `image-r` Last-Modified 2022-06-17, its checksum 2022-11-18 — the digest postdates that
  file, which is reassuring for this brick and proves nothing about bricks replaced in place by
  DR10.1. The hazard named in the memo stands: pre-replacement bytes confirmed by their own stale
  checksum verify cleanly while not being current. The DR10 known-issues replacement list remains
  the cross-check, and a replaced brick must be sampled before this is called closed.
- The pacing rule and the §6 amendment list still apply. Adopting B still requires a successor
  binding and a new freeze.

## Two further facts from the same reply

1. **DR11 has been released**, "expands the area significantly", and Dustin suggests using it
   instead of DR10. The frozen parent set, the 208,407 count, the feasibility arithmetic and the
   route binding are all built on DR10.1. Switching releases is not a data-source swap — it would
   invalidate the frozen selection. **This is Duho's decision and it is a large one.** Do not treat
   "newer is better" as obvious.
2. **Anonymous Globus access may be available.** He supplied a file-manager link for the cosmo
   collection and said "I think it should be accessible anonymously (though this may change)".
   If true, route A needs no NERSC allocation at all — which would make A cheap again, and A
   requires no amendment to the frozen binding.

## Status of this document

Sections above the CORRECTION line are retained as the record of what was measured and concluded,
and are **superseded**. The operative conclusions are in this section.
