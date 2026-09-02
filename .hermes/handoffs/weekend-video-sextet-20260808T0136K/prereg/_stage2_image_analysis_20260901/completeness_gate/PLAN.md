# Definitive DR10-south catalogue crossmatch plan — V4

This lane is catalogue-only and never opens pixels. It uses the complete public
`ls_dr10.tractor_s` relation (2,825,807,500 rows in the captured TAP_SCHEMA
description) and selects only release/brick/object identity and sky position.
There is no magnitude, morphology, quality, vote, or nearest-neighbour filter.

## Evidence repair and route decision

Every backend HTTP exchange is captured under `artifacts/http/` as JSON with
request method, URL, non-secret parameters, status line, response headers, and
the first 4 KiB of the body as text and hex. The re-issued V2 POST to guessed
`https://datalab.noirlab.edu/tap/async` is captured in
`20260902T162240365658Z_0001.json`. It returned HTTP 200 and a UWS job document
at a redirected job URL, but no `Location`: V2's failure was an overly strict
client assumption, not an auth wall.

The route probes used the first ten pinned GZ1 positions and no credentials:

| route | result | rows | wall_s | cap evidence |
|---|---|---:|---:|---|
| a: advertised-base async + TAP_UPLOAD | failed; legacy URL returned HTML | 0 | 1.11 | none |
| b: advertised-base sync + inline upload | failed; legacy URL returned HTML | 0 | 1.11 | none |
| c: `/tap/sync`, no upload, q3c CASE + OR | worked | 12 | 1.80 | `MAXREC=10000`, `QUERY_STATUS=OK` |

The advertised route URLs were derived from the standard interface in the
capabilities XML (`http://datalab.noirlab.edu/ivoa-dal/tap/`), never guessed.
The raw q3c attempt established that Data Lab requires comparison to the string
literal `'true'`. `UNION` is unsupported and the requested CONTAINS fallback is
mis-translated for this table. Probe summaries and all raw responses remain in
`artifacts/`.

Route c is the first route that works anonymously, enumerates all catalogue
rows in every cone, and exposes truncation. The terminal VOTable
`QUERY_STATUS=OK` proves the response did not hit `MAXREC`; missing status,
`OVERFLOW`, `ERROR`, or any non-OK status is a hard refusal.

## Query and exact provenance

Each request selects a CASE-tagged `input_index` and the identity/position
columns from `ls_dr10.tractor_s`, with one indexed `q3c_radial_query` predicate
per input position joined by OR. This is a union of all-candidate 1-arcsec
cones, not nearest-neighbour matching. The server radius is one binary64 step
above 1 arcsec; the client applies the authoritative `<= 1.0` arcsec test.

CASE emits one tag when cones overlap. To preserve exact provenance, the client
recomputes each returned source against every submitted position, requires the
server tag to name one true membership, and expands the source to every true
`input_index`. Duplicate identity/provenance pairs and sources outside all cones
refuse the chunk.

## Chunking, dry run, and estimate

The 10-position successful probe was 2,266 query characters / 2,780 form bytes
and took 1.80 s. The chosen size is 100 positions: the real request was 21,268
query characters / 25,630 form bytes and completed in 5.120335625 s. The V3
manifest partitions indices 0..893211 exactly once into 8,933 chunks (100 each,
last 12). The prior 1,000-row V2 manifest is retained separately.

Exactly one real chunk ran end-to-end: chunk 0, rows_in=100, service rows=116,
exact output associations=116, cap=`QUERY_STATUS=OK (MAXREC=10000)`. Its query,
raw result, metadata and hashes are in `artifacts/chunk_0000_20260902T162958Z/`;
the HTTP exchange and append-only checkpoint are also retained. Conservatively
adding the complete two-second pacing allowance per chunk gives
`8933 * (5.120335625 + 2) / 3600 = 17.67 h`.

## Execution and proof obligations

Use one worker, at least two seconds between request creation, `Retry-After` for
429/5xx, otherwise exponential backoff with jitter. Each completed checkpoint
line is appended and fsynced only after cap validation, and binds the raw-result
SHA-256. Resume re-hashes the artifact, reparses its cap signal, and restores
candidate provenance; corruption, duplicate successful entries, gaps, overlaps,
schema drift, release drift, cap ambiguity, or truncation refuses completion.

Finalization must prove the exact 893,212-row input-index set, one terminal
disposition per GZ1 object, complete multi-candidate enumeration, collision
handling, pinned input hashes, the 1-arcsec inclusive rule, and terminal
dispositions for all 13,725 prior-unresolved OBJIDs.

## V4 executable finalization

`run_full.py` now performs those obligations as one worker. Before networking it
digest-checks GZ1 Tables 2/3, Tier A, and the parent; checks their exact row
counts/index set; and checks `prior_unresolved_13725.json` for exactly 13,725
unique integer OBJIDs. The latter is a canonical derived artifact (SHA-256
`73a1d8e10e15d0b501745b008be370afc82151472177e3a1ac334966bef1bafa`)
whose embedded provenance binds the parsed reconnaissance catalogue, accelerated
match result, brick table, and exact rectangle/absence rule. Its provenance also
records that one reported-set member is within 1 arcsec of the parent, an
inconsistency in the historical “outside-parent” shorthand that is not silently
edited out of the reported 13,725 set.

Every checkpoint is unique by chunk ID and re-hashes its raw VOTable. On full
coverage, the runner reconstructs candidates from all raw chunks and calls
`run_pinned_files()`. Only then can it emit timestamped §5 receipt and pair-list
files. `--max-chunks` bounds requests, `--resume` continues after verification,
and `--dry-finalise` reports and refuses any gap without a receipt.

The capabilities integration uses the advertised standard interface through URL
resolution. NOIRLab currently returns a stale `http/ivoa-dal` alias in the XML;
when the host agrees, the resolved capabilities response location supplies its
canonical service mirror. There is no requested-base string-concatenation or
fallback sync URL, and absence of the capability-derived endpoint refuses.

V4 test output: 30 tests ran in 11.632 s, all OK. The authorized live bound ran
three chunks (300 inputs, 354 associations) in 33.896302 s. Dry finalization then
refused the gap: 3/8,933 chunks and 300/893,212 input indices admitted; no
completeness receipt was emitted.
