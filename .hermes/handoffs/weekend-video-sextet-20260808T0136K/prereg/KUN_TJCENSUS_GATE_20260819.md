PASS_TJUNCTION_CENSUS

# KUN T-JUNCTION CENSUS GATE -- 2026-08-19

## Verdict

**PASS_TJUNCTION_CENSUS.** The sidecar SHA is verified before any FITS open,
the band definition cites the round-5 offsets faithfully and pins them by
hash, my own independent recompute reproduces the headline numbers exactly,
a seeded 500-brick sample is fully consistent with the deliverable's
per-brick and per-event outputs, and the non-derivability of object-level
counts is stated plainly in all three output surfaces. No repairs required.

## Sidecar SHA checked before use

- `compute_tjunction_census.py` calls `custody_geometry_path()` as the first
  statement of `main()` (line 103), which parses
  `_tori_transfer_20260819/execution_package/SIDECAR_CUSTODY_20260819.md`,
  requires the custody digest to equal the hardcoded
  `863e5ded7a4aae7abcb5df76f322f35cf89945483715ff6d1874c88f5a072d9a`, rehashes
  the local file, and only afterwards opens the FITS (line 119). Fail-closed
  on any mismatch.
- I independently rehashed the sidecar: observed
  `863e5ded7a4aae7abcb5df76f322f35cf89945483715ff6d1874c88f5a072d9a`, matching
  the custody record, the survey-published digest quoted there, and the
  summary's `inputs.geometry_sha256`.
- The round-5 generator is likewise SHA-pinned (`498659bf...`, matches my
  measurement) and the round-1 generator hash `24f55943bffabb855c2c6396d792e19ed4350449809bd22a63f59d3b6fa3404d`
  matches the resampler-gate record. Working-set CSV SHA `78ee99d6824bf4f5126b9ffd9eb622ad8201df2c64c3f232d99c1791b5f36b74`
  matches the summary.

## Band definition fidelity to round 5

- `make_boundary_fixtures_round5.py:176-186` is exactly the
  `LADDER_REQUESTS_PIXELS` dict: offsets -10, -0.25, 0, +0.25, +1 pixels on
  each axis, shared exact case. `:613-617` is the `junction_ladder_contract`
  naming the same offsets. `make_boundary_fixtures.py:24` is
  `PIXEL_SCALE_ARCSEC = 0.262`. All three citations in the report are
  line-accurate.
- The compute script does not trust the citation: it AST-extracts the ladder
  and asserts it equals the required dict verbatim, then asserts the envelope
  resolves to [-10,+1] pixels (lines 79-98). The recorded band
  (-2.62 to +0.262 arcsec, width 2.882 arcsec) follows.

## Independent recompute (my own code) + seeded 500-brick sample

I wrote a separate implementation (no import of the deliverable's script),
re-enumerated every three-cell meet from the rehashed sidecar, and receipted
the run (seed `20260819`, `RandomState.choice` over sorted working names,
replace=False; sample bricknames SHA-256
`969bd125f55496c59c5f352df28ef32e795f8fc248a464192175c2e5e5a7c75d`).

Full-set recompute vs headline:

| quantity                | headline              | my recompute          |
|-------------------------|-----------------------|-----------------------|
| unique events           | 132,108               | 132,108               |
| junction segments       | 359,607               | 359,607               |
| bricks with >=1 junction| 60,308                | 60,308                |
| band area deg^2         | 0.07715143987107126   | 0.07715143987107126   |
| AREA denominator deg^2  | 3742.6027260480428    | 3742.6027260480428    |
| area fraction           | 2.0614381359289613e-05| 2.0614381359289613e-05|

- Full event-key set (ra, dec, orientation) equality between my recompute
  and the deliverable's 132,108-row events CSV: **true**.
- 500-brick sample: per-brick segment counts and band areas match the
  deliverable's per-brick CSV with **0 mismatches**; sample segment sum
  2,978 = 2,978; sample-incident events 2,956 = 2,956, none missing, none
  extra; sample band area `0.0006400682237654348` deg^2 identical both ways.
- Sample area fraction `2.0627340067317836e-05` vs headline
  `2.0614381359289613e-05`: within sampling variation for 500/60,308 bricks.
- Arithmetic cross-checks on the summary: per-brick count distribution
  {1:1, 2:10, 3:611, 4:134, 5:187, 6:59273, 7:92} sums to 60,308 bricks and
  weights to 359,607 segments; orientations 65,785 + 66,323 = 132,108.
- I also re-ran the deliverable's `verify_tjunction_census.py`: **PASS**
  (inventory hashes verified, all 132,108 event topologies checked, per-brick
  reduction 359,607 / 60,308, fraction reproduced).

## Object-level non-derivability stated plainly

- DONE doc line 12: "Object-level touching counts are NOT derivable because
  parent-object positions were deleted by design."
- Report "Custody and scope ceiling": the same sentence in bold, plus the
  ceiling framing ("manifest-gate answer's ceiling, not an object count").
- `tjunction_census_summary.json`:
  `definitions.object_level_touching_counts =
  "NOT_DERIVABLE_POSITIONS_DELETED_BY_DESIGN"`, `limits.parent_object_positions_used
  = false`, `limits.object_count_interpretation_allowed = false`.
- Code reading confirms no parent-position input exists in the compute path
  (sidecar geometry + working-set CSV only), so the statement is structural,
  not aspirational. The 359,607 segment / 132,108 unique-event distinction is
  itself stated explicitly to prevent incidence/event ambiguity.

## Boundaries

Findings-only. No network used by this gate; `portal.nersc.gov` never
contacted (the sidecar URL appears only as a quoted custody string). No
writes outside my own gate artifacts; all deliverable, fixture, sidecar, and
working-set files only read. No database, cockpit, publication, or git
action. This pass covers brick-geometry census correctness only; it asserts
nothing about object-level touching counts, which remain non-derivable by
design.
