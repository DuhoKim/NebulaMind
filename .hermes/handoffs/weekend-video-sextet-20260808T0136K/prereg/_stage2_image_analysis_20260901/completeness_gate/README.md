# Catalogue-only completeness gate

V4 implements a one-worker, artifact-backed NOIRLab Data Lab synchronous TAP
backend. It issues no-upload, OR-ed all-candidate q3c cone queries against
`ls_dr10.tractor_s`; it never reads pixels.

The selected chunk size is 100 (8,933 chunks for 893,212 rows). Every HTTP
exchange is captured in `artifacts/http/`. Every successful chunk retains its
ADQL, raw VOTable, metadata, cap signal and SHA-256, followed by an fsynced
append-only checkpoint. Resume verifies hashes and reconstructs candidates.

Completeness is admitted only for a terminal `QUERY_STATUS=OK` response with
`MAXREC=10000`. Overflow, a missing cap signal, non-OK status, bad provenance,
duplicates, gaps, or hash drift causes `COMPLETENESS-FAIL`. CASE tags plus
client-side membership expansion preserve exact provenance for overlapping
input cones.

The route evidence and rationale are in `PLAN.md`. The sole real dry run is
chunk 0: 100 inputs, 116 outputs, 5.120335625 s, cap
`QUERY_STATUS=OK (MAXREC=10000)`. The conservative full-run estimate including
two seconds of pacing per chunk is 17.67 hours. No full run was started.

`run_full.py` is the single full-run entry point. It verifies all four pinned
inputs and the pinned 13,725-entry prior-unresolved list, iterates the canonical
manifest, and hash-verifies every checkpoint on resume. It finalizes only after
all 8,933 chunks prove exact coverage, then writes timestamped completeness and
Tier-C-pair files. It never reads pixels.

```sh
./run_full.py                         # new full run
./run_full.py --resume                # hash-verified continuation
./run_full.py --max-chunks 3          # bounded execution
./run_full.py --resume --dry-finalise # report coverage; never receipt a gap
```

The sync endpoint is resolved from the standard interface exposed by the TAP
capabilities response. A missing advertised endpoint refuses; no caller-base
`/sync` fallback exists.

Run tests from this directory:

```sh
python3 -m unittest -v test_completeness_gate.py test_tap_source.py test_run_full.py
```

Latest result: **30/30 passed** in 11.632 s. Coverage includes overflow refusal,
missing-cap refusal, exact overlap provenance, hash-verified resume, HTTP raw
capture, backoff, canonical manifest partitioning, a five-chunk runner with an
orphaned killed attempt, finalization-gap refusal, prior-count refusal, and one
DR10 row attributed to both positions inside 1 arcsec.

The authorized live V4 bound admitted chunks 0--2: 300 inputs, 354 output
associations, 33.896302 s. The following dry-finalise refused the 8,930-chunk /
892,912-input gap and emitted no completeness receipt.

This work does not modify acquisition state, bricks, journals, pins, seals,
preregistration V1–V9, referee reports, or Git state.
