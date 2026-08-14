# Yui — machine-enforced aggregate-only release linter

**Date:** 2026-08-14 KST  
**Deliverable:** `prereg/release_linter/nm_release_lint.py`  
**Machine self-test:** **PASS_SYNTHETIC_SELFTEST, 22/22 fixtures**  
**Boundary:** engineering release gate only; not legal advice, publication authority, freeze, or acceptance.

## 1. Controlling contract

The checker implements the package-wide boundary in:

- `TORI_OUTPUT_LICENCE_CLEARANCE_20260814.md:126-145`, directly measured SHA-256 `47702d3708a0729735196d899b302bb2350a3eaf599c260508aafe911ae4c5c5`;
- `KUN_REDESIGN_REGATE_20260814.md:48-75`, directly measured SHA-256 `833157852b40f4e317f9f4c4714305c2abf31726a67ceb3a7bb19216aa14d0a7`;
- `_tmp_YUI_RELEASE_LINTER_BRIEF.md`, directly measured SHA-256 `2d48040395c9d58099c63366c59b64033bebf0cb2a564514b8d826d00d32748d`.

Tori's six conditions are controlling. Lana's numeric limits are evaluated as additional conservative guardrails only when custody and the six controlling families have no finding. A numeric pass is never treated as a legal safe harbor.

## 2. Invocation and exit contract

Lint a complete proposed release directory:

`python3 nm_release_lint.py /path/to/package`

Machine-readable output:

`python3 nm_release_lint.py /path/to/package --json`

Run the deterministic synthetic fixture matrix and write its receipt:

`python3 nm_release_lint.py --self-test --write-selftest SELFTEST.md`

Exit values:

- `0`: package ACCEPT, or self-test fully matched expectations;
- `1`: self-test mismatch or harness error;
- `2`: package REJECT;
- argparse's nonzero usage exit: malformed command.

Unknown role/type, malformed or symlinked manifest, missing or unlisted file, bad hash, payload symlink, unparseable table/non-table structured payload, unclassified quantity, or incomplete/unrecognized image route is a REJECT.

## 3. Package manifest contract

Every package must have one `release_manifest.json` with schema version 1. The schema is closed: unknown top-level, file-entry, cell-system, or column fields fail rather than becoming a channel for undeclared rows. The manifest must:

- list every package file exactly once, excluding the manifest itself;
- pin every listed file with a full lowercase SHA-256;
- classify each file as `documentation`, `code`, `environment`, `commitment`, `table`, or `image`;
- attest `schema_frozen_before_statistics: true` and `cells_frozen_before_statistics: true`;
- attest `dynamic_query_interface: false` and `unlimited_slicing: false`.

Version 1 parses tables only as strict UTF-8 CSV. A table entry must declare its exact ordered columns, table kind, object-independent/frozen status, and a cell-system object containing nonempty `id`, `domain`, `family`, `axes`, and `partition_kind` fields. Each column must use a closed role, quantity-class, and scalar data-type vocabulary; role, class, and type must agree, and the CSV header must exactly match the declaration.

`whole_sample_scan` is a separate table kind. It must declare `membership_partition: false` and an integer `whole_sample_n >= 50`; its result fields must be whole-sample statistics, uncertainties, or controls. It is not counted as a released object-cell system. It remains finite at no more than 5,000 scan points.

## 4. Machine-enforced rules

### R1 — Rowless

The checker rejects:

- identifier/source column names including `objid`, object/source IDs, `ls_id`, `brickid`, brick name, release, row hash, catalogue/target IDs, and source fields;
- direct coordinate columns including RA/Dec and common equatorial/Galactic/longitude/latitude spellings;
- per-object label, score, confidence, embedding, chirality/handedness, prediction, probability, or cutout/source URL fields;
- URL-like values inside tables;
- pairs of axis/result/control/uncertainty columns with at least three rows, high uniqueness, at least six decimal places, material span, and RA/Dec-like numeric ranges—even when mislabeled as study quantities;
- comma/tab/pipe row shapes with object-like headers appearing anywhere in any allowed non-table text payload, not only at line one;
- embedded object-like literal records in JSON environment/commitment files and Python code, concrete object-field assignments in allowed text/code/config formats, and more than 100 hash literals outside the bounded artifact-commitment route;
- malformed or catalogue-scale `.sha256` commitment payloads (more than 100 canonical artifact commitments);
- any package file omitted from the complete manifest.

### R2 — Fixed and finite

The checker requires package and per-table pre-statistic freeze attestations, object-independent cells, closed table kinds, and classified cell systems. It rejects dynamic query interfaces, unlimited slicing, adaptive/object-dependent cells, and whole-sample scans that claim to partition object membership.

### R3 — Study-result only

Every table column must have a recognized role, quantity class, and scalar data type, and the triple must be compatible. Released result/uncertainty/control fields are numeric only; masks are booleans; support counts are integers; cell IDs and scan axes use bounded scalar forms. Every CSV cell is checked against that declaration, including finite-number and JSON-like string rejection. Allowed released result classes are study estimands/counts, instrument summaries, uncertainties, controls, masks, cell definitions, and whole-sample scan statistics. Result names are also checked against the schema-version-pinned finite registry (`mean_sign`, accepted-count/instrument fields, approved confusion-matrix counts, whole-sample statistic, and named uncertainty/control forms); an arbitrary alias such as `foo` fails even when assigned an allowed class. Unknown classes, types, or result names fail closed.

A separate name detector rejects aggregate re-tabulations of survey magnitude, redshift, size/radius, flux, and colour fields even if the manifest falsely labels such a column as a study estimand. Generic payload/blob/row/raw/data/source/value names also fail rather than accepting arbitrary content under an allowed quantity class.

### R4 — Non-reconstructable cumulatively

The checker compares ordinary tables across the complete package. Public self-declared domain/axis strings cannot prove disjoint object membership, so every pair of ordinary cell-system tables is conservatively treated as potentially related whenever they share a released quantity. Renaming a domain or axis therefore cannot turn the detector off. Shared released quantities include the support count `k` itself.

Potentially related systems releasing a shared quantity produce `E_R4_RELATED_CELL_SYSTEMS`. Thus the synthetic Nside=32 plus relabeled Nside=64 same-quantity attack is rejected despite deliberately different domain/axis strings. When systems are monotone refinements of one family, the finer system is also inspected; an unmasked or unverifiable finest cell below `k=50` produces `E_R4_REFINEMENT_K`.

### R5 — Non-substitutive cumulatively

The checker builds the union of aggregate cell IDs for each ordinary cell system and sums those unique cells across the package. More than **5,000 unique ordinary cells package-wide** is a REJECT. This prevents a publisher from evading the ceiling by splitting cells among multiple individually small files.

It also rejects empty/duplicate aggregate cell IDs and catalogue-scale/per-brick lookup shapes. A table with at least 100,000 rows, a per-brick family, or brick-key columns receives `E_R5_CATALOGUE_SCALE`. The exact 270,577-row synthetic fixture proves that detector runs over the full input.

Because the controlling package-wide ceiling is itself 5,000, it subsumes the ordinary per-table 5,000-cell guard: a single over-limit table fails R5 before the subordinate numeric stage.

### R6 — Separate image compliance

PNG/JPEG extension and magic bytes must agree. Every image must declare whether it contains source pixels.

- Original/synthetic result graphics with no source pixels must declare an allowed origin.
- A source-pixel image must match the closed Legacy Surveys route: recognized Legacy layer, exact `CC-BY-4.0` ID, exact Creative Commons 4.0 URL, exact `Legacy Surveys / D. Lang (Perimeter Institute)` credit, visible-credit flag, and either `unmodified` or `modified_and_indicated` status. Arbitrary nonempty strings do not pass.

A compliant image never clears a table finding; all findings remain controlling.

### Numeric guardrails, after R1–R6/custody pass

For each ordinary table:

- exactly one integer, nonnegative `support_k` field;
- exactly one boolean mask field;
- unmasked cell `k >= 50`;
- any masked cell must blank every released result, uncertainty, and control value;
- no ordinary table above 5,000 cells.

Sub-threshold masked cells may retain their synthetic support count for machine checking, but every released result/uncertainty/control value must be blank.

## 5. Self-test evidence

`SELFTEST.md` was written by the linter itself, not composed by hand. It records **22/22 exact expected-versus-actual matches**, zero bad fixtures unexpectedly accepted, and zero good fixtures falsely rejected. Every fixture requires exact equality between the expected and actual finding-code sets; an unexpected extra detector is a mismatch too.

Required BAD shapes proved to reject:

- per-object identifier/label/score rows;
- exact 270,577-row synthetic per-brick table;
- RA/Dec and generic object-precision float-pair coordinates;
- Nside=32 plus domain/axis-relabeled Nside=64 same-quantity differencing pair;
- monotone refinement with a finest unmasked `k < 50` cell;
- two individually sub-5,000 tables totaling 5,001 cells;
- mean survey magnitude per cell;
- unmasked `k=49` cell;
- dynamic interface;
- missing source-image route and a separately complete-but-bogus asserted route;
- symlinked manifest;
- cached object rows embedded in environment JSON;
- JSON object content placed in a string-valued quantity column;
- unknown file type, unknown quantity, and unlisted auxiliary file.

Required GOOD shapes proved to accept:

- S1-style Nside=32 sparse-footprint masked maps with **4,096** released synthetic cells, accepted count, abstention, mean sign, and sensitivity (not a claim that all 12,288 full-sky Nside=32 pixels are releasable);
- exactly 67 fixed partition aggregates;
- exactly nine hand-check strata;
- exactly 3,072 Nside=16 whole-sample scan points.

Unit/contract tests: **36/36 PASS**, including adversarial-review regressions and positive tests for query aliases/explicit synthetic code fixtures, after RED-to-GREEN development. The fixture run is deterministic, network-free, and uses synthetic values only. Temporary fixture paths use `_tmp_nm_release_linter_*` and are removed automatically.

## 6. Honest limits — what this linter cannot prove

Rules 4 and 5 are not decidable in general. This checker implements concrete conservative detectors; it does not claim a proof of non-reconstructability or non-substitutability.

It cannot detect all of the following:

1. deliberately false manifest semantics not contradicted by parseable content; relabeling domain/axis strings no longer bypasses the within-package shared-quantity detector, but arbitrary semantic lies remain possible;
2. arbitrary encodings, encryption, steganography, adversarially renamed survey attributes, or executable/generated row payloads that are not visible as the concrete JSON/Python/text structures the scanner recognizes;
3. reconstruction attacks that require outside releases, unpublished context, or a future version not supplied in the package being linted; this invocation is a single-snapshot gate, so a stateful external release-history registry remains required for longitudinal cumulative enforcement;
4. nonlinear combinations whose information leakage is not represented by shared declared quantities/cell systems;
5. whether freeze attestations were historically true—it can require and hash-pin the declaration, not observe the past;
6. whether an image's exact claimed layer/licence/credit metadata is factually or legally correct, whether the pixels really come from that layer, or whether the credit is visibly rendered in a future publication—it checks the closed declaration and file signature only;
7. whether an aggregate is scientifically valid, statistically correct, or publication-worthy;
8. a legal determination that a package is licensed.

Accordingly, ACCEPT means: **no implemented deterministic release rule fired on this exact hash-pinned package**. It does not mean “safe under every possible reconstruction attack,” “licensed,” “frozen,” or “accepted for publication.” Kun's re-gate and human semantic/legal review remain required.

## 7. Artifact custody and boundary

Direct hashes at the completed self-test run:

- `nm_release_lint.py`: `7ff18bfc9272bcbb924b77cb81f2b37c45a130c2b1c5ba1fbc9b95baaab323ac`;
- `test_nm_release_lint.py`: `4316567c26b68296fcc870534dea66b56f34cf5167bc78e16b11576d8bf309cb`;
- `SELFTEST.md`: `c23bed0d42865961bba1240dbcb52fb496281d044afa766a64c6a07253f66706`.

Only synthetic fixtures were created. Real catalogue/object rows, positions, survey bricks, images, chirality or morphology labels, and real-sky statistics used: **zero**. Network, database writes, publication, freeze, acceptance, commit, push, merge, or cockpit change: **none**.

**Kun gates this blocker. Duho owns acceptance.**
