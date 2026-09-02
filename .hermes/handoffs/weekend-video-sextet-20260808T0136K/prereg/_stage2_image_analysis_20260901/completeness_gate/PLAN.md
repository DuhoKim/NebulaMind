# Definitive DR10-south catalogue crossmatch plan

This plan is catalogue-only. It must not open the R-band FITS files already held
in `bricks_tier_c/`; those files are coadd images and do not contain the Tractor
source catalogue required by MINI_PREREG_GZ_TIERC_DRAFT_V9_20260902.md §5.

## What reconnaissance established, and what it did not

`CODEX_GZ_SPIN_RECON_20260902.md` joined the two official GZ1 tables, parsed the
coordinates, excluded the protected parent/Tier-A positions, and used DR10-south
catalogue results to establish useful overlap, high-confidence, brick, storage,
and covariate counts. It explicitly described the resulting Tier-C counts as a
verified lower bound with a brick-footprint ceiling, not as a complete match.

The supporting `scratch/gz_catalogue_recon.py` first assigned GZ1 positions to
DR10-south brick rectangles and exported Tractor rows in batches of 500 brick
IDs with `t.dered_mag_r < 20`. It later used a server-side 1-arcsec join for
selected positions. `scratch/get_bricks.py` restricted work to high-confidence,
outside-parent positions that passed a nearest-brick rectangle test and issued
OR-ed cone predicates, primarily to enumerate brick names. `scratch/calc_footprint.py`
computed a rectangle-based footprint ceiling. These were appropriate query- and
storage-volume accelerators for reconnaissance. They cannot establish §5
completeness: a faint Tractor source could be absent from the `r<20` export;
rectangle membership is not a source match; nearest-row operations do not
enumerate ambiguity; and absence from any accelerated product is not a terminal
catalogue disposition. In particular, the 13,725 prior-unresolved positions
remain unresolved until the definitive run.

## Chosen definitive source and query

Use NOIRLab Astro Data Lab's DR10 public catalogue service and its complete
DR10-south Tractor relation, confirmed by the 2026-09-03 probe as
`ls_dr10.tractor_s`. TAP_SCHEMA describes it as the DR10 southern-region Tractor
catalogue with **2,825,807,500 rows**; all required columns and `ls_id` are
present. Before live execution, record a small metadata-only schema
response proving the selected relation, release field/value, row count exposed
by the service, and relevant columns. The run must select only identity and
position columns (`release`, `brickid`, `objid`, `brickname`, `ra`, `dec`, and
`ls_id` if supplied). It must contain no magnitude, flux, morphology, size,
photo-z, quality, or vote predicate.

Upload each GZ1 chunk as a table with a stable zero-based `input_index`, integer
`OBJID`, and parsed binary64 `ra`, `dec`. Perform one server-side positional join:

```sql
SELECT g.input_index, t.release, t.brickid, t.objid, t.brickname, t.ra, t.dec
FROM TAP_UPLOAD.gz_chunk AS g
JOIN ls_dr10.tractor AS t
  ON 1 = CONTAINS(
       POINT('ICRS', t.ra, t.dec),
       CIRCLE('ICRS', g.ra, g.dec, 1.0/3600.0))
ORDER BY g.input_index, t.brickid, t.objid
```

If the service supports its documented q3c join rather than ADQL geometry, use
the equivalent inclusive-radius predicate and record the exact SQL. The client
recomputes every returned separation in IEEE-754 binary64 with the preregistered
great-circle formula and applies `<= 1.0` arcsec. A conservative server query
radius may be one binary64 step above 1 arcsec so server rounding cannot omit a
boundary candidate; the client remains authoritative at exactly 1 arcsec. This
is an all-candidate join, never a nearest-neighbour query. The service query
plan/schema and the absence of a result cap must be captured.

## Chunking, pacing, and expected runtime

Submit 1,000 GZ1 positions per asynchronous TAP job (894 chunks for 893,212
rows). Use one job at a time initially and at most two concurrent jobs only if
the published service guidance and observed responses permit it. Pace job
creation by at least two seconds, honor `Retry-After`, use exponential backoff
with jitter for 429/5xx responses, and poll no faster than every five seconds.
Each result must include a service-reported row count and complete/end-of-stream
status; any overflow/truncation warning refuses the chunk. At an expected
30--90 seconds per 1,000-position spatial join, one worker takes about 7.5--22.5
hours plus retries; budget **12--30 wall-clock hours** for a polite definitive
run. Two explicitly permitted workers would likely take 6--15 hours.

The 2026-09-03 dry run used a conservative 50-row sub-chunk. The capabilities-
advertised legacy base resolved to an HTML frontend, while the requested TAP
service's `/tap/async` child returned no UWS job Location after **7.09 s**. It
produced no result rows and no cap/truncation assertion. This is a failed
submission time, not an observed per-chunk query time, so the earlier runtime
estimate cannot responsibly be revised numerically. The definitive run is
blocked until a working async upload endpoint is supplied or the complete local
partition fallback is used.

If TAP upload/crossmatch is unavailable or unreliable, the fallback is a local
sweep over the complete NERSC DR10-south per-brick Tractor catalogues under the
published `.../dr10/south/tractor/<AAA>/tractor-<brick>.fits` tree. Download a
catalogue partition manifest and every relevant/full south Tractor file, hash
each artifact, prove the brick partition against the DR10-south bricks manifest,
then enumerate sources in neighbouring bricks before applying the client
radius. This is substantially more I/O and requires an authoritative partition
manifest; the image coadds on disk are not a substitute.

## Artifacts, resume, and proof

Before submission, write a canonical chunk manifest partitioning input indices
`0..893211` exactly once. For every chunk retain the uploaded table, exact query,
TAP job URL/ID, phase log, raw result bytes, response metadata, row count, and
SHA-256. An append-only checkpoint records artifact hashes only after a job has
completed without truncation. Resume verifies all hashes and reuses completed
chunks; an interrupted or corrupt chunk is resubmitted under a new attempt ID,
while only one successful attempt may be admitted. Finalization refuses overlaps,
gaps, reordered/unknown input indices, unsuccessful jobs, schema drift, release
drift, caps, truncation, or hashes that do not reproduce.

The §5 receipt binds both official GZ1 digests, the Tier-A and parent digests,
the exact DR10 source/release metadata, chunk manifest, every query/export hash,
software/environment identity, and the 1.0-arcsec inclusive rule. It reports
funnel counts from 893,212 physical input rows through parsing, duplicate check,
A/B priority exclusion, zero/one/multiple DR10 candidates, collision exclusion,
probability disposition, and final Tier-C pairs. It proves row-once coverage by
the exact `input_index` set and one terminal tier/match disposition per unique
valid GZ1 object. It proves candidate completeness by requiring every admitted
chunk to be an uncapped all-candidate cone join over the complete relation and
by binding the raw multirow exports, not only selected nearest matches. The
complete pinned list of 13,725 prior-unresolved OBJIDs is embedded with exactly
one of `NO-DR10-WITHIN-1ARCSEC`, `ONE-DR10-WITHIN-1ARCSEC`, or
`MULTIPLE-DR10-WITHIN-1ARCSEC`; any missing, duplicate, or nonterminal entry is
`COMPLETENESS-FAIL`.

The single biggest risk is **silent server-side truncation or resource limits on
the large spatial join**. Small chunks, asynchronous completion metadata, raw
artifact retention, explicit cap checks, and refusal rather than inference are
the mitigation; if the service cannot give that proof, use the locally complete
per-brick Tractor fallback.
