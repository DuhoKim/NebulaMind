ASSESSED_READPATH_SCOPE

# KUN ROUND-4 READ-PATH SCOPING ASSESSMENT -- 2026-08-16

## Verdict

**ASSESSED_READPATH_SCOPE.**

Round-4 has not been crossed against the adapter, and I do not treat it as a
coverage pass. The current adapter cannot read the production-shaped `.fits.fz`
fixture format. It has only ever read uncompressed primary-HDU float32 rasters.

This is an architecture gap, not a failure of the earlier round-1/2/3 gates.
The next repair should decide the read-path architecture before any round-4
adapter coverage gate is attempted.

No network, no real survey data, no source manifest, no sky statistic, no real
rows/positions/images/chirality, no publication, no accepted status, no commit,
and no push are authorized.

## Hashes Measured

- brief `prereg/_tmp_kun_round4_readpath_brief_20260816.md`
  - SHA-256 `18ef88c4e4625703ad2b32ae8b234848b9bb3f779e13d40d903a2908fa10775a`
- adapter `prereg/adapter/nm_brick_cutout_adapter.py`
  - SHA-256 `267b2a93d2a61f65b281aeb3b04dd874d7add058797b10f593cb3efb4066006f`
- cross-runner `prereg/adapter/cross_check_yui_boundary.py`
  - SHA-256 `e4168e331148feb9d348e30dcd10427f572492dfbedab141b745b8e3c34c691d`
- round-4 fixture generator `prereg/boundary_fixtures/make_boundary_fixtures_round4.py`
  - SHA-256 `d6c193841ff8ff52f1188ae1d48bbe5ea8c89bf553c542ad176f70189b7b7533`
- round-4 tests `prereg/boundary_fixtures/test_boundary_fixtures_round4.py`
  - SHA-256 `97be43190812eafd4745dc175442aff88254a030cd6272ebbd143cf5d660972e`
- round-4 generated manifest
  `prereg/boundary_fixtures/generated_round4/fixture_manifest.json`
  - SHA-256 `82b1ccf7190426eaf8482be3d2abbbb9ae238b62e518940d7f10fc72add214ff`
- round-1 fixture generator
  - SHA-256 `24f55943bffabb855c2c6396d792e19ed4350449809bd22a63f59d3b6fa3404d`
- round-2 fixture generator
  - SHA-256 `60e3d662d72fbc87e0c82889b4f9174c033882b8f9a2019011c5104bb4aa15bc`
- round-3 fixture generator
  - SHA-256 `6b410fb40def2869d4f3431f029654d8fa7cacd20741dca5a84b12409d5e5e62`

The pinned round-1, round-2, and round-3 generators are unchanged from the
resampler gate.

## Fixture Validity

I ran the full fixture suite:

- command from `prereg/boundary_fixtures`:
  `python3 -m unittest test_boundary_fixtures test_boundary_fixtures_round2 test_boundary_fixtures_round3 test_boundary_fixtures_round4`
- result: `22/22` passed

Round-4 manifest summary:

- schema `yui-boundary-fixtures-round4-v1`
- compression `RICE_1`
- tile shape `[100, 100]`
- quantize level `-1e-07`
- `primary_hdu_empty`: true
- `image_hdu_index`: `1`
- `object_count`: `3`
- `brick_count`: `5`
- scope says this tests the production-shaped `.fits.fz` HDU-1 read path and
  does not validate the production adapter.

## Can the Current Adapter Read It?

No.

The adapter source path `SyntheticBrickSource` reads the first FITS header from
the file, passes those raw cards into `fail_closed_header_gate`, and then
requires:

- `SIMPLE` true
- `BITPIX == -32`
- `NAXIS == 2`
- `NAXIS1 == 3600`
- `NAXIS2 == 3600`
- raw raster bytes immediately after that primary header

That is the uncompressed primary-HDU raster model.

Round-4 files are production-shaped: empty primary HDU plus compressed image in
HDU 1. The real dimensions are in `ZNAXIS1/ZNAXIS2`; the primary is not a
float32 celestial image, and the HDU-1 payload is a RICE-compressed binary table
rather than raw float32 raster bytes.

I also ran a negative synthetic probe by passing one round-4 fixture source to
`SyntheticBrickSource`. It failed closed as:

- `WcsRejectedError`
- `source:synthetic-round3-knife-dec-max-west-image-r.fits.fz: non-celestial axes`

That is expected for the empty primary. It confirms the current adapter does
not reach or decode HDU 1.

## Architecture Recommendation

Do not write an in-house RICE_1 decoder inside the stdlib-only adapter unless
there is an explicit decision to make codec correctness our burden. That would
be a large, new, error-prone surface exactly where a silent read-path error can
become a position-correlated image defect.

Do not quietly add `astropy`, `fitsio`, or an Imagine dependency to the adapter
while still claiming the stdlib-only invariant. If the adapter imports a
third-party FITS decoder, the invariant must be retired and the dependency
lock becomes part of the adapter gate.

The cleanest architecture is to keep the adapter's core planning, WCS gating,
PC-3/PC-4 receipt, and bilinear cut semantics stdlib-only, but move production
`.fits.fz` decoding into a separate, explicitly pinned read/decompression
stage. That stage should:

- open HDU 1 with a hash-pinned FITS decoder;
- verify `ZIMAGE`, `ZCMPTYPE=RICE_1`, `ZBITPIX=-32`, and `ZNAXIS1/2=3600`;
- verify the decompressed float32 array shape and source WCS cards against the
  geometry sidecar;
- emit either a canonical uncompressed raster handoff or an explicitly hashed
  in-memory array contract for the adapter;
- produce a receipt tying source file hash, raw HDU-1 header hash,
  decompressed array hash, decoder environment lock, and the adapter input
  bytes.

Then round-4 should be crossed against that interface. If Tori instead chooses
to make the adapter read `.fits.fz` directly, the next gate must be a new
adapter-dependency and codec gate, not a continuation of the stdlib-only pass.

## Earlier Gates

Nothing in round-4 invalidates the earlier corner-repair, round-2, round-3, or
resampler gates. Those gates covered synthetic planning/source-set/coverage and
pixel-value equality for uncompressed staged rasters. The round-1/2/3 fixture
generators are unchanged.

Round-4 changes the container/read path, not the already-gated geometry cases.
If round-4 re-expressions of round-1 or round-3 disagree with their originals,
that would be a fixture/oracle finding to investigate, not evidence that the
current adapter has already passed production `.fits.fz` handling.

## Scope Boundary

This assessment authorizes only the next architecture repair and a later
round-4 cross-runner gate. It does not authorize any real DR10 read, source
manifest, production cutout, sky statistic, or chirality work.
