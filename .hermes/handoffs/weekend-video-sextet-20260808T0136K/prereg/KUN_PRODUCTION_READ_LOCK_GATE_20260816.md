PASS_PRODUCTION_READ_LOCK

# KUN PRODUCTION-READ ENVIRONMENT LOCK GATE -- 2026-08-16

## Verdict

**PASS_PRODUCTION_READ_LOCK.**

The production-read environment lock is correctly calibrated as a measured
offline environment record, not as an exact rebuild bundle and not as
production authorization. It covers the readstage source, moved cross-runner,
unchanged adapter, fixture generators/tests, installed third-party package
trees, and Astropy tiled-compression decoder module bytes.

This remains build-only and synthetic-only. It authorizes no network, no real
survey data, no source manifest against the real parent set, no sky statistic,
no rows/positions/images/chirality, no publication, no accepted status, no
commit, and no push.

## The 1321/0 Question

Astropy's `record_hash_validation.declared_sha256_matched: 1321` and
`declared_sha256_mismatched: 0` establish installed-file consistency against
Astropy's installed `RECORD`: the files whose RECORD entries declare SHA-256
hashes match those declarations, with no declared-hash mismatch.

It does **not** authenticate the original wheel/sdist distribution. A
substituted distribution could carry a self-consistent `RECORD`; this lock
would then verify consistency of that installed tree, not provenance back to an
independent package archive. The lock says this plainly:

- `original_install_artifact_sha256: null`
- `original_install_artifact_status`: unavailable offline because dist-info
  RECORD hashes installed files but does not preserve original archive bytes
- `exact_offline_rebuild_possible: false`
- `reproducible_from_lock_alone: false`

So `1321/0` is a useful drift/tamper check on the current installed tree, not a
supply-chain authenticity proof. I do not find wording in the lock that claims
more than that.

## Hashes Measured

- brief `prereg/_tmp_kun_prodlock_gate_brief_20260816.md`
  - SHA-256 `03cb24eb18ebf52ff4a20824a876e448f0488895b7a9b498b36d212b0c74f8eb`
- production-read lock `prereg/YUI_PRODUCTION_READ_ENVIRONMENT_LOCK_20260816.json`
  - file SHA-256 `01398e324446b4ce0681d3f6a3fa2b7b494f2f024ac2c556e40de09da169166a`
  - internal `content_sha256`
    `86cf7c7aa07ee236d05e691598c216d1e037d347ebcfb1b5ea63d462bb11fbc7`
- adapter `prereg/adapter/nm_brick_cutout_adapter.py`
  - SHA-256 `267b2a93d2a61f65b281aeb3b04dd874d7add058797b10f593cb3efb4066006f`
- moved cross-runner `prereg/adapter/cross_check_yui_boundary.py`
  - SHA-256 `3bb84cefe44eea4a49b8d8ef7bad6a64a92137d67731606e4bccbe33703f9436`
- readstage `prereg/readstage/nm_brick_read_stage.py`
  - SHA-256 `6662c8c74d71b81216149596d65deeaa39c07a19a57e50ba9bbe4ac22d478b0a`
- readstage test `prereg/readstage/test_nm_brick_read_stage.py`
  - SHA-256 `dd669e434de0319d237f53a16792c3a9c0a2b61457b84ea81a01d9d71c325790`

The old lock `prereg/YUI_DEPENDENCY_ENVIRONMENT_LOCK_20260816.json` is present
and now has status `SUPERSEDED_BY_PRODUCTION_READ_ENVIRONMENT_LOCK`.

## Item 1 -- Claim Level

The claim level matches reality:

- `claim_level`: `MEASUREMENT_NOT_EXACT_REBUILD_OR_PRODUCTION_AUTHORIZATION`
- `reproducible_from_lock_alone: false`
- `exact_offline_rebuild_possible: false`
- `network_access_alone_sufficient_for_bit_exact_rebuild: false`
- `production_reliance_authorized: false`

That is neither under-claimed nor over-claimed. It is exactly the boundary this
record can support: current-environment verification and drift detection, not
self-contained reconstruction and not a real-data go signal.

## Item 2 -- Dependency Boundary

The dependency-boundary ruling is faithfully encoded.

The lock states:

- `invariant_kind: module-and-input-contract`
- `whole_process_third_party_free: false`
- `stdlib_only_invariant_applies_to: ["adapter/nm_brick_cutout_adapter.py"]`
- `readstage_direct_third_party_dependencies: ["astropy", "numpy"]`
- cross-runner process note: adapter calls may run in a process containing
  third-party packages without changing the adapter module/input-contract
  invariant.

That matches my readstage gate. The adapter remains stdlib-only at its module
and staged-input contract boundary; the readstage owns the decoder dependency.

## Item 3 -- Coverage

The lock includes the required source artifacts and their hashes match disk:

- adapter `267b2a93...`
- moved cross-runner `3bb84cef...`
- readstage `6662c8c7...`
- readstage test `dd669e43...`
- adapter test
- round-1/2/3/4 fixture generators
- round-1/2/3/4 fixture tests

I recomputed all `13` `source_artifacts` entries against disk; there were no
missing files and no hash mismatches.

The decoder module fingerprints also match disk:

- Astropy version `6.0.1`
- NumPy version `1.26.4`
- `compressed.py`
- `_tiled_compression.py`
- `_compression.cpython-39-darwin.so`
- `__init__.py`
- module-set fingerprint `1d9cc08c32e7b9edae77671e912d51a489115fbc49d9c936c4267dce9b5314a5`

All four decoder module entries had matching file size and SHA-256 on disk.

## Item 4 -- Supersession

Supersession is correctly recorded.

The new lock names:

- superseded path `YUI_DEPENDENCY_ENVIRONMENT_LOCK_20260816.json`
- pre-supersession file SHA-256
  `6e0c9ae2c414f0659c1dda5fba4f42bb417924fb64bb0bb08fb60d6d0f6e24ab`
- pre-supersession content SHA-256
  `d729a7824ae5d139f461bd1a4d69b27486c053af1984421cf1c2305175ae1f05`
- pre-supersession status
  `PASS_OFFLINE_ENVIRONMENT_MEASURED_WITH_REBUILD_GAPS`

The old lock is retained, not deleted, and its current top-level status is
`SUPERSEDED_BY_PRODUCTION_READ_ENVIRONMENT_LOCK`.

Historical reports still mention the old lock because they were written before
the reissue; I do not treat those as current authority. In the current lock
chain, the successor is the current environment record.

## Item 5 -- Identity

The identity discipline is correct.

- `content_hash_excludes`: `["content_sha256", "recorded_utc"]`
- that exclusion list is itself inside the hashed body
- recomputed content SHA-256:
  `86cf7c7aa07ee236d05e691598c216d1e037d347ebcfb1b5ea63d462bb11fbc7`
- recorded content SHA-256:
  `86cf7c7aa07ee236d05e691598c216d1e037d347ebcfb1b5ea63d462bb11fbc7`

I did not regenerate the lock because the brief did not require rebuilding it
and no network/install/fetch is authorized. The lock itself records the
two-build identity contract. The artifact I inspected has internally correct
content identity.

## Remaining Boundary

This pass closes the production-read environment-lock gate as a measured
environment record. It does not turn the synthetic readstage pass into
production reliance. Real route artifacts, real `.fits.fz` container variation,
transfer behavior, real source manifests, and any real image reads remain
separate gates.
