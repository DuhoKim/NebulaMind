# Catalogue-only completeness gate

V3 implements a one-worker, artifact-backed NOIRLab Data Lab synchronous TAP
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

Run tests from this directory:

```sh
python3 -m unittest -v test_completeness_gate.py test_tap_source.py
```

Latest result: **26/26 passed** in 3.574 s. Coverage includes overflow refusal,
missing-cap refusal, exact overlap provenance, hash-verified resume, HTTP raw
capture, backoff, canonical manifest partitioning, and all original gate tests.

This work does not modify acquisition state, bricks, journals, pins, seals,
preregistration V1–V9, referee reports, or Git state.
