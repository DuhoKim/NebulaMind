# MINI-PREREGISTRATION — GZ1 × DESI TIER-C INTER-METHOD CONCORDANCE

**V11 CANONICAL, V1–V10 SUPERSEDED.**

Draft V11 for principal signature, 2026-09-02.

Status: **DRAFT; NOT YET FROZEN; NO MEASUREMENT AUTHORITY.**

This document is intentionally smaller than the parent preregistration. It governs one validation study and no flagship statistic.

## 1. Purpose, authority, and stop rule

1.1 The sole purpose is to measure inter-method concordance between the frozen DESI image instrument and high-confidence Galaxy Zoo 1 (GZ1) human vote labels on a new, outside-parent Tier-C sample.

1.2 This study is authorized in design by Duho's direction #55 of 2026-09-02, conditional on agy's verification: use Tier C only; keep the P0 blind untouched; hold and exclude Tier B; leave Tier A untouched.

1.3 The approximately 208 GiB acquisition is separately pre-authorized. Acquisition authorization is not measurement authorization.

1.4 No image may be rendered, no instrument output may be formed, and no real object may be labelled under this study until Duho signs the exact-hash text.

1.5 Catalogue-only construction, integrity verification, manifest construction, and completeness proof may precede signature only if they read no image pixels.

1.6 Any deviation from a frozen rule below stops the study. It is not repaired in place after any real image pixel or instrument output has been accessed.

1.7 A stopped or refused run reports the applicable non-ordinary verdict and does not silently drop affected objects, alter thresholds, or restart under a new convention.

## 2. Fixed input identities

2.1 GZ1 Table 2 is the official file `GalaxyZoo1_DR_table2.csv.gz`, locally staged as `scratch/gz1_t2.csv.gz`, with SHA-256 `5121e43f502856c9f73e31934a6e7d7282669c3ae065564a31f5d5115f45541d`.

2.2 GZ1 Table 3 is the official file `GalaxyZoo1_DR_table3.csv.gz`, locally staged as `scratch/gz1_t3.csv.gz`, with SHA-256 `282c8049e93c47b5343885210ace8ba5710e9914ce035a6b39061395436d9723`.

2.3 Table 2 must contain exactly 667,944 data rows and Table 3 exactly 225,268 data rows; their ordered concatenation contains exactly 893,212 rows.

2.4 Only fields `OBJID`, `RA`, `DEC`, `P_CW`, and `P_ACW` are used. No debiased, spiral, elliptical, uncertain, ancillary, GZ2, GZ DECaLS, GZ DESI, or model-predicted label enters this study.

2.5 Tier A is defined by `../_successor_build_20260824/acquire/positions_selected_cut.csv`, 49,211 data rows, SHA-256 `a20682c114508dbdd18ede6a56c61509ea9c16784aaca7eee61f76bf97cdd372`.

2.6 The protected parent is defined by `../_successor_build_20260824/acquire/positions_selected.csv`, 65,060 data rows, SHA-256 `425a42c3ea2a6004a08b52c27201dbf59546e88fef4f3d3ba6d2ffb5a3f70831`.

2.7 Tier B means parent members not in Tier A. Tier B is **HELD pending a principal ruling and EXCLUDED from this study**.

2.8 DESI catalogue candidates are all objects in the complete public DR10-south Tractor catalogue, release DR10, with no magnitude, flux, size, morphology, photo-z, or quality predicate.

2.9 The reconnaissance predicate `dered_mag_r < 20` was an accelerator only. It is prohibited from the definitive match and from every sample definition.

2.10 The verdict program is `miniprereg_pins/concordance_verdict.py`, SHA-256 `587870e9f35d2c096f68cd10a769ab9c7eee6580d8b9cdee580b521cae63b070`. Its fixture test is `miniprereg_pins/test_concordance_verdict.py`, SHA-256 `2373e122c458d3b0a2cda85560f87741a07bd99ea013922667d8c08e23f24f1d`.

2.11 The BS-4 fixture specification is `miniprereg_pins/bs4_sign_anchor_spec.md`, SHA-256 `c9aee6d6cdfba4722a396f55b27c8a7c58d5ecc7dbbd2da4414a969fe2b95f0b`.

2.12 The rendering configuration is `miniprereg_pins/render_config.json`, SHA-256 `8a6ba7984b5d4e1ae2b900943a2e1f842706bed6f367831884a992edb573ffa7`.

2.13 The seal-time software/environment record schema is `miniprereg_pins/env_record_schema.json`, SHA-256 `0607538bd41d49650e62ba33c833fe287f6e7df41cc0a6aaa6ca7c26932689b9`. The record produced at seal time has exactly four required top-level fields: `python_version` (the exact Python version string); `package_versions` (an object mapping every package used by the verdict program or renderer to its exact version); `os` (exact `system`, `release`, `version`, and `machine` strings); and `frozen_instrument_sha256` (the §9.1 digest). No additional top-level or `os` fields are allowed.

2.14 The published NERSC per-brick checksum source convention is the exact URL pattern `https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/coadd/<AAA>/<brick>/legacysurvey_dr10_south_coadd_<AAA>_<brick>.sha256sum`, where `<AAA>` is the first three characters of `<brick>`, and the exact checksum filename form is `legacysurvey_dr10_south_coadd_<AAA>_<brick>.sha256sum`. The pinned reference implementation is `miniprereg_pins/fetch_bricks_pinned.py`, SHA-256 `35fd6c246483757fee37bcff2a69abd5ec0ae27ec7b13137b3d4e1530af28c99`. At pin time it was byte-for-byte and hash-identical to the live acquisition copy `../_successor_build_20260824/acquire/fetch_bricks.py`, whose independently computed SHA-256 was also `35fd6c246483757fee37bcff2a69abd5ec0ae27ec7b13137b3d4e1530af28c99`; the live file and running fetch were not modified.

## 3. Coordinate parsing and angular match

3.1 GZ1 sexagesimal RA is parsed as `15 * (hours + minutes/60 + seconds/3600)` degrees.

3.2 GZ1 sexagesimal declination is parsed with the printed leading sign applied to the whole absolute quantity `degrees + arcminutes/60 + arcseconds/3600`.

3.3 DESI RA and declination are parsed as IEEE-754 binary64 degrees in ICRS.

3.4 Every coordinate and probability must exist, parse uniquely, and be finite. RA must satisfy `0 <= RA < 360`; declination must satisfy `-90 <= Dec <= 90`; each probability must satisfy `0 <= P <= 1`.

3.5 Angular separation is the great-circle separation on the unit sphere, computed in binary64 from ICRS coordinates.

3.6 The inclusive match radius is exactly 1.0 arcsecond. Equality at 1.0 arcsecond is accepted.

3.7 All candidate DESI objects at separation `<= 1.0 arcsecond` are enumerated. A nearest-neighbour query that returns only one candidate is not sufficient to prove uniqueness.

3.8 Duplicate `OBJID` rows within or across GZ1 Tables 2 and 3 are a catalogue integrity failure; none is resolved by table priority.

3.9 A GZ1 object with zero DR10-south candidates is unmatched and not eligible.

3.10 A GZ1 object with two or more DR10-south candidates inside 1.0 arcsecond is ambiguous and not eligible, even if one candidate is strictly nearer.

3.11 After rule 3.10, if two or more GZ1 objects point to the same DR10 object, all GZ1 objects in that collision component are ambiguous and not eligible. No closest, highest-vote, or table-priority winner is chosen.

3.12 The ambiguity exclusions are computed from coordinates and identifiers before `P_CW`, `P_ACW`, image pixels, or instrument outputs are consulted.

## 4. Exact disjoint Tier-C definition

4.1 Tier assignment priority is A, then B, then C, at the GZ1-object level.

4.2 For each GZ1 object, first enumerate all Tier-A candidates within 1.0 arcsecond. If at least one exists, assign that GZ1 object to A and stop.

4.3 Otherwise enumerate all Tier-B candidates within 1.0 arcsecond. If at least one exists, assign that GZ1 object to B and stop.

4.4 Otherwise apply the complete DR10-south matching and ambiguity rules in §3. A GZ1 object is Tier C only if it has exactly one DR10-south candidate and that DESI object survives the one-to-one collision rule.

4.5 Thus Tier C is disjoint both from the 49,211-object Tier-A mask and from every member of the 65,060-object protected parent at the inclusive 1.0-arcsec radius. A parent match excludes the GZ1 object even if another non-parent DESI candidate exists.

4.6 The protected-parent filter is applied before any image-path resolution, file opening, pixel access, rendering, instrument call, or label comparison.

4.7 The eligible GZ1 label is clockwise iff `P_CW >= 0.8` and `P_ACW < 0.8`.

4.8 The eligible GZ1 label is anticlockwise iff `P_ACW >= 0.8` and `P_CW < 0.8`.

4.9 The threshold is inclusive: equality at 0.8 qualifies.

4.10 If neither probability reaches 0.8, the object is below threshold and is not in the frozen analysis sample.

4.11 If both probabilities reach 0.8, the label is contradictory and the study refuses with `DATA-INTEGRITY-FAIL`; it is not broken by a larger probability.

4.12 No `P_CW + P_ACW` threshold, vote-count threshold, magnitude cut, or later visual-quality cut applies.

4.13 The final eligible unit is one unique pair `(GZ1_OBJID, DR10_RELEASE, DR10_BRICKID, DR10_OBJID)` satisfying every rule above.

4.14 Pair rows are canonically sorted by the integer value of `GZ1_OBJID`, then integer `DR10_BRICKID`, then integer `DR10_OBJID`.

## 5. Accelerator cure and completeness gate

5.1 Before sample freeze, the definitive crossmatch must be recomputed against the complete DR10-south Tractor release without any magnitude accelerator.

5.2 The 13,725 outside-parent GZ1 footprint positions unresolved by the reconnaissance accelerator, including the 561 then classed high-confidence, must each receive exactly one terminal catalogue disposition: `NO-DR10-WITHIN-1ARCSEC`, `ONE-DR10-WITHIN-1ARCSEC`, or `MULTIPLE-DR10-WITHIN-1ARCSEC`.

5.3 A count inferred from brick rectangles, an `r < 20` query, a lower bound, or absence from an accelerated result is not a terminal disposition.

5.4 The completeness receipt must bind the full GZ1 input digests, full DR10-south catalogue release identity, query/export artifacts and their hashes, software/environment identity, match radius, counts in every disposition, the complete list of the 13,725 prior unresolved OBJIDs, and their dispositions.

5.5 The receipt must prove that every one of the 893,212 GZ1 rows was considered exactly once before duplicate-integrity handling and that every unique valid GZ1 object has one terminal tier/match disposition.

5.6 It must also prove that candidate enumeration was complete inside 1.0 arcsecond, rather than merely returning a nearest row.

5.7 Any missing prior-unresolved OBJID, nonterminal position, duplicate terminal record, catalogue-partition gap, query truncation, magnitude predicate, or hash mismatch yields `COMPLETENESS-FAIL` and prevents sample freeze.

5.8 Only after the completeness receipt passes are the Tier-C pairs and the below-threshold/ambiguous/excluded counts frozen by SHA-256.

## 6. Sample freeze and deterministic split

6.1 The frozen sample manifest contains only the canonical pair identity, catalogue coordinates, `P_CW`, `P_ACW`, categorical GZ1 label, split assignment, required primary brick, and required neighbour bricks.

6.2 For each eligible object, compute `h = SHA256(ASCII base-10 string representation of the integer GZ1_OBJID with no sign, whitespace, or leading zero)`.

6.3 Interpret the 32 digest bytes as one unsigned big-endian integer.

6.4 The split modulus is 5. Residue `h mod 5 = 0` is the sign-mapping split. Residues `1, 2, 3, 4` are the estimation split.

6.5 Split membership is never rebalanced, stratified, redrawn, or changed for sample size, class balance, sky position, render success, or observed outcome.

6.6 The sample manifest SHA-256 and row count are written into a signed freeze record before any image pixel is accessed.

6.7 The two splits are disjoint by `GZ1_OBJID`, `DR10_OBJID`, and collision construction. No object contributes to both mapping and estimation.

## 7. Brick manifest, acquisition, and integrity

7.1 The sole ruled image source is the NERSC Legacy Surveys DR10-south coadd brick tree. Coordinate-native cutout services and substitute mirrors are not analysis sources.

7.2 Whole published R-band coadd brick files are acquired and cut locally.

7.3 The Tier-C brick manifest contains every primary and neighbour brick needed to form every frozen 128-by-128 cutout under §8.

7.4 The brick manifest is canonically UTF-8 serialized with LF endings, sorted by brick name, one record per file, and binds release, relative NERSC path, byte length, and published SHA-256.

7.5 The exact brick-manifest SHA-256 and record count are pinned in the sample freeze record before measurement.

7.6 Every acquired brick must match its per-brick published SHA-256 before it may enter rendering. Verification of only transport, size, FITS checksum, or a locally generated digest without comparison to the published value is invalid.

7.7 Required maskbits and R-band exposure-count (`nexp-r`) companions are included in the manifest and verified to their published hashes under the same rule. The exact exposure-count filename convention is `legacysurvey-<brick>-nexp-r.fits.fz`; the per-brick `.sha256sum` file lists it, as in the probed line `b9417ce52b9c7c208c7d029dbd7e97a126d8938ee732976905dd4cb9a0eb043c  legacysurvey-0001m010-nexp-r.fits.fz`.

7.8 Missing, extra, duplicate, substituted, or hash-mismatched required files yield `DATA-INTEGRITY-FAIL`; they do not remove an object from a split.

7.9 Acquisition and verification append one JSON object per attempted brick to the append-only acquisition journal `../_successor_build_20260824/acquire/tier_c_fetch_receipts.jsonl`; this acquisition journal has no predecessor-digest or current-receipt-digest fields. The allowed verdict vocabulary and exact receipt shapes are closed. An `OK`, `OK-NO-PUBLISHED-SHA`, or `SHA-MISMATCH-QUARANTINED` receipt has exactly the seven keys `brick`, `bytes`, `computed_sha256`, `published_sha256`, `url`, `utc`, and `verdict`. An `OK` receipt has non-null `published_sha256` equal to `computed_sha256`. An `OK-NO-PUBLISHED-SHA` receipt has null `published_sha256`; it explicitly does not count as an OK receipt for §7.11's acquisition-completion set condition and, exactly like any non-OK receipt, is admissible only if a later `OK` receipt exists for the same brick. `SHA-MISMATCH-QUARANTINED` is a non-OK verdict and has the same seven-key shape. A `FETCH-FAILED` receipt has exactly the five keys `brick`, `error`, `url`, `utc`, and `verdict` and is non-OK. Any other verdict value, any key set other than the one prescribed for its verdict, or any `OK` receipt whose `published_sha256` is null or differs from `computed_sha256` yields refusal as `malformed_journal_schema`. The pinned acquisition reference writes these shapes and verdicts at lines 136--153:

```python
        rec = {"utc": utc(), "brick": brick, "url": brick_url(brick)}
        try:
            pub = published_sha(brick, args.timeout)
            blob, _url = fetch(brick, args.timeout)
            got = hashlib.sha256(blob).hexdigest()
            rec.update(bytes=len(blob), published_sha256=pub, computed_sha256=got)
            if pub is not None and pub != got:
                (QUARANTINE / out.name).write_bytes(blob)
                rec["verdict"] = "SHA-MISMATCH-QUARANTINED"
                result = "fail"
            else:
                tmp = out.with_suffix(out.suffix + f".part{threading.get_ident()}")
                tmp.write_bytes(blob)
                tmp.replace(out)
                rec["verdict"] = "OK" if pub else "OK-NO-PUBLISHED-SHA"
                result = "ok"
        except Exception as e:
            rec.update(verdict="FETCH-FAILED", error=f"{type(e).__name__}: {e}")
```

7.10 The distinct seal journal governed by §16.3 is chained. Each canonical seal receipt binds timestamp, operation, relative path where applicable, expected digest where applicable, observed digest where applicable, byte count where applicable, status, predecessor receipt digest, and current receipt digest. Its receipt digest is SHA-256 over the canonical receipt body excluding its own `receipt_digest`; the chain predecessor of the first seal-journal record is 64 zeroes. Acquisition-journal records under §7.9 are not represented as chained seal-journal records merely by assertion.

7.11 Acquisition completion is the following set condition, not the exit of any one process run: the 17,947-element BRICK SET remains the ordered set in `tier_c_manifest_v1.json`, while the PLANE list per brick is pinned by `tier_c_manifest_v3.json` (`TIERC-MANIFEST-3`, SHA-256 `02e410b0ca512398ad21bdcf279a7ff77068a16d820c9eeffca4ba1ea339530c`) as image-r, maskbits, and nexp-r. For each of those three planes, the set of `brick` values having at least one receipt with `verdict == "OK"` in its per-plane journal—`tier_c_fetch_receipts.jsonl` for image-r and `tier_c_fetch_receipts_<plane>.jsonl` for maskbits and nexp-r—equals that same BRICK SET; no process matching `fetch_bricks[.]py --manifest` is running; and every OK receipt has `computed_sha256` equal to `published_sha256`. In each journal, any receipt with a verdict other than `OK` for a brick that lacks a later OK receipt causes refusal. A resumable journal may span multiple process runs: the image-r journal had 784 receipts when stopped for the 2026-09-02 15:25 KST restart and then resumed, and a brick already present and SHA-verified is skipped. At acquisition completion and before any pixel access, the freeze record pins (a) each plane's `journal_head_sha256`, exactly the SHA-256 of the whole per-plane acquisition-journal file at that moment, and (b) each plane's `receipt_count`, exactly its line count; all six values are also recorded in the seal receipt. Each `journal_head_sha256` supplied to the verdict program must equal item (a) for its plane, and mismatch yields `DATA-INTEGRITY-FAIL`.

Files of the superseded inverse-variance plane are KNOWN EXTRAS exactly when their filenames are carried by receipts of any verdict in the disclosed journal `../_successor_build_20260824/acquire/tier_c_fetch_receipts_invvar-r.jsonl`: they are never read, never hashed for the seal, and are excluded from the extra-file check; any file in `bricks_tier_c/` that is neither a manifest-v3 plane file nor a receipted known extra still yields `extra_brick_file` refusal, and because the journal is growing its digest is not pinned here but the seal receipt records its path, SHA-256, line count, and tolerated-known-extra count at seal time.

The live script has three historically distinct Git blobs. Read-only Git returned `3f994f8d2112660e21d73a4f3651c71feef16bbb` at commit `888c0a2ff59bb7c4b50be3a3892ea2561ab2a125` (2026-09-01 19:39:54 KST, the first #52 launch), `8e3dedd3aa777a3e437c6963ddc73f1da8fb9472` at commit `06a242163d42588dff3aa0a40cdd86778f51ea48` (2026-09-01 19:43:59 KST, four workers), and `df704bed1c5fd872cf9dee9f4be2e88f64bb94a0` at Tier-C GO commit `ad21829fad8b805f5d32d99c74ad4d1cce92071b` (2026-09-02 14:30:32 KST); `HEAD` still returns `df704bed1c5fd872cf9dee9f4be2e88f64bb94a0`, and the live file equals that blob. Read-only `git show -s --format=%cI ad21829fa` returned `2026-09-02T14:30:32+09:00`, whose exact UTC committer instant is `2026-09-02T05:30:32Z`. The Tier-C journal's first receipt is `2026-09-02T05:27:44Z` (14:27:44 KST), 2 minutes 48 seconds before that instant. A read-only JSON parse of the live journal counted exactly 42 receipts whose `utc` value is strictly less than `2026-09-02T05:30:32Z`. Git does not witness which working-tree bytes ran during those minutes.

The real read-only Git output was:

```text
ad21829fad8b805f5d32d99c74ad4d1cce92071b  2026-09-02 14:30:32 +0900
06a242163d42588dff3aa0a40cdd86778f51ea48  2026-09-01 19:43:59 +0900
888c0a2ff59bb7c4b50be3a3892ea2561ab2a125  2026-09-01 19:39:54 +0900
3f994f8d2112660e21d73a4f3651c71feef16bbb
8e3dedd3aa777a3e437c6963ddc73f1da8fb9472
df704bed1c5fd872cf9dee9f4be2e88f64bb94a0
df704bed1c5fd872cf9dee9f4be2e88f64bb94a0
100644 df704bed1c5fd872cf9dee9f4be2e88f64bb94a0 0	../_successor_build_20260824/acquire/fetch_bricks.py
```

The command-line argv is the witness for that gap. The Tier-C command is `fetch_bricks.py --manifest tier_c_manifest_v1.json --dest bricks_tier_c --journal tier_c_fetch_receipts.jsonl --workers 4 --delay 0.5`. Read-only `git diff 06a242163..ad21829fa -- ../_successor_build_20260824/acquire/fetch_bricks.py` shows that only the `df704bed...` content adds the accepted arguments, including these exact argparse lines:

```python
ap.add_argument("--manifest", type=Path, default=MANIFEST,
                help="brick-list JSON (defaults to the original #52 closure; "
                     "Tier-C acquisition authorized 2026-09-02 passes its own)")
ap.add_argument("--dest", type=Path, default=DEST,
                help="destination directory (Tier C uses its own so the #52 "
                     "closure's zero-extra-files invariant stays checkable)")
ap.add_argument("--journal", type=Path, default=JOURNAL,
                help="receipt journal (one per authorization)")
```

The earlier blobs would have rejected that command line, so the 42 pre-commit receipts could only have been written by the `df704bed...` content already in the working tree. The 15:25 KST resumption ran after `ad21829fa` committed that blob.

At freeze, the seal seat MUST execute a programmatic content-integrity check independent of the acquisition script and append its result as a chained seal receipt under §§7.10 and 16.3. Paced politely, the seal seat independently re-fetches from the NERSC source every manifest brick's published checksum file using the exact §2.14 URL convention. The convention is shown by the pinned acquisition reference's `published_sha()` implementation (lines 57--65):

```python
def published_sha(brick, timeout):
    """Read the brick directory's published checksum file; return the sha for
    the r-band image, or None if the listing does not provide one."""
    aaa = brick[:3]
    for name in (f"legacysurvey_dr10_south_coadd_{aaa}_{brick}.sha256sum",
                 f"legacysurvey-{brick}.sha256sum", "checksums.sha256"):
        url = f"{BASE}/{brick[:3]}/{brick}/{name}"
        try:
            with urllib.request.urlopen(
```

For the seal check, no fallback name is allowed: for each manifest brick `<brick>` with `<AAA>` equal to its first three characters, the fetched filename MUST be `legacysurvey_dr10_south_coadd_<AAA>_<brick>.sha256sum` at the §2.14 URL. In `tier_c_manifest_v1.json` brick order and `tier_c_manifest_v3.json` plane order, the seal seat extracts the checksum lines for that brick's image-r, maskbits, and nexp-r files, preserves each fetched line's bytes with exactly one terminating LF, concatenates all 53,841 lines, and records `published_checksum_lines_sha256`, the SHA-256 of that concatenation, in the chained seal receipt. This single digest binds all 53,841 freshly fetched published values.

For every brick and each of its three manifest planes, the check MUST establish that (i) a final OK receipt exists in that plane's journal, (ii) the plane file exists in `bricks_tier_c/`, (iii) SHA-256 recomputed from that on-disk file at freeze equals the freshly fetched NERSC published value, and (iv) the receipt's `computed_sha256` and `published_sha256` both equal that same freshly fetched value. The receipt copy is only a cross-check and is never the authority for the published value. The chained receipt MUST record `manifest_count`, `files_checked` (which MUST equal 17,947 completed three-plane bricks), `plane_file_count` (which MUST equal 53,841), `mismatches` (which MUST equal 0), each plane's `journal_head_sha256` and `receipt_count`, `published_checksum_refetch_complete`, `published_checksum_disagreements` (which MUST equal 0), and `published_checksum_lines_sha256`. Any checksum-file fetch failure, missing or malformed checksum line, published-value disagreement, missing receipt, missing file, mismatch, unequal count, or absent receipt field yields `DATA-INTEGRITY-FAIL` before any pixel access. This gate makes the acquisition scripts untrusted by construction: script custody is supplementary rather than necessary to content integrity.

The freeze-time Git custody receipt remains mandatory for the resumed run and freeze state, but it does not witness the first 2 minutes 48 seconds, which are covered by the argv witness and the freeze-time content re-hash. Read-only `git ls-files -s -- ../_successor_build_20260824/acquire/fetch_bricks.py` returned exactly `100644 df704bed1c5fd872cf9dee9f4be2e88f64bb94a0 0\t../_successor_build_20260824/acquire/fetch_bricks.py`, and `git cat-file -p df704bed1c5fd872cf9dee9f4be2e88f64bb94a0 | shasum -a 256` returned `35fd6c246483757fee37bcff2a69abd5ec0ae27ec7b13137b3d4e1530af28c99  -`, equal to the §2.14 live-file and pinned-copy SHA-256 values. At freeze, the seal seat MUST append a chained receipt recording the blob ID returned by `git ls-files -s` at that moment, the SHA-256 of the live file, the SHA-256 of the pinned copy, and the exit status of `git diff --quiet -- ../_successor_build_20260824/acquire/fetch_bricks.py`. The study refuses with `DATA-INTEGRITY-FAIL` unless the Git blob hashes to the same SHA-256 as both files, all three SHA-256 values are identical, and the diff exit status is zero. Absence of any required acquisition-completion witness, freeze-record value, seal-receipt value, or equality also yields `DATA-INTEGRITY-FAIL` before any pixel access.

## 8. Frozen geometry and rendering

8.1 Each scientific raster is exactly 128 by 128 pixels and subtends exactly
33.536 by 33.536 arcseconds at 0.262 arcsecond per pixel.

8.2 The output is a TAN WCS centered on the exact catalogue `(RA, Dec)` parsed as binary64; coordinate rounding to a source pixel is prohibited.

8.3 In FITS one-based pixel-center convention, `NAXIS1=NAXIS2=128`, `CRPIX1=CRPIX2=64.5`, `CRVAL1=RA`, and `CRVAL2=Dec`.

8.4 The output CD matrix in degrees per pixel is exactly `CD1_1=-0.262/3600`, `CD1_2=0`, `CD2_1=0`, `CD2_2=+0.262/3600`.

8.5 There is no object-dependent rotation. The display and instrument raster are north-up and east-left.

8.6 Parity is strictly preserved through WCS transforms, array-axis conversion, storage, display, and model input. The instrument's explicit mirror is the sole chirality-changing transform.

8.7 An effective source-to-output Jacobian with the wrong parity refuses the cutout and yields `WRONG-PARITY-REFUSAL`; it is never corrected by a flip.

8.8 All required neighbouring bricks are stitched before reprojection. A home-brick seam is not an exclusion reason.

8.9 Exactly one deterministic bilinear reprojection maps the stitched inputs to the output WCS. Binary64 accumulation is materialized once as float32.

8.10 Resizing, further interpolation, rotation, transpose, PSF homogenization, padding, wrapping, reflection, intensity-conditioned source choice, and chirality-conditioned processing are prohibited.

8.11 The identical reprojected raster is supplied to the unmirrored branch and to the instrument's exact mirror operation; the mirrored branch is not separately reprojected.

8.12 Every output pixel requires valid image, maskbits, and exposure-count coverage (`nexp-r` > 0) from the verified stitched inputs. Any missing or non-finite required value yields `DATA-INTEGRITY-FAIL` for the study, not an object-level deletion.

8.13 The prose constants in this §8 and the pinned `miniprereg_pins/render_config.json` must agree exactly. Any disagreement refuses the run before pixel access.

## 9. Frozen instrument and machine sign

9.1 The sole instrument is `../_successor_build_20260824/ref/successor_ref_v9.py`, SHA-256 `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`.

9.2 Those bytes are run as-is. Any edit, patch, copied modification, monkey patch, changed weight, alternate implementation, or replacement invalidates the entire study and yields `INSTRUMENT-INTEGRITY-FAIL`.

9.3 Before every invocation, the file digest is recomputed and compared to the pin. The environment demanded by the frozen instrument is used unchanged.

9.4 The instrument score is its frozen antisymmetric quantity `chi(x) = (w(x) - w(mirror(x)))/2`.

9.5 The raw machine sign is `+1` iff `chi > 0` and `-1` iff `chi < 0`.

9.6 `chi = 0`, a missing output, a non-finite output, wrong shape, exception, or nondeterministic repeat is `MEASUREMENT-FAIL` for the study. There is no tie-breaker, epsilon, abstention deletion, or retry with altered data.

9.7 One exact rerun of every object with the identical raster and environment must reproduce the binary64 `chi` bytes; disagreement yields `NONDETERMINISTIC-INSTRUMENT` and stops.

## 10. Absolute anchor, relative mapping, and ordering

10.1 Before any real image is opened, the frozen BS-4 synthetic absolute-sign anchor in §2.11 is run through the pinned rendering and instrument chain and must pass its frozen expected absolute sign convention. In this study the anchor proves that the rendering+instrument chain preserves absolute sign before any GZ comparison is made; it does not validate GZ1 or establish truth.

10.1a The canonical parent preregistration, `../_successor_build_20260824/PREREG_SUCCESSOR_DRAFT_V134_20260831.md`, lines 124--129, was re-verified by quote-diff and is imported below with identical characters and wording:

> **Sign, stated so it cannot be inverted by a later reader.** Longo's published amplitude
> carries a MINUS sign in his convention. Our East-of-North winding convention maps it to
> **+0.0408** (V3-pred F-5), and the code constant `A_LONGO = +0.0408` is our-convention while
> `A_LONGO_PUBLISHED_SIGNED = −0.0408` records his. The mandatory synthetic absolute-sign
> anchor (BS-4) re-establishes the mapping empirically before any real image; the fixture
> `BATTERY-SIGN` demonstrates that an injected **−0.0408** sky is never called REPRODUCED.

10.1b Therefore this study uses the East-of-North convention, `A_LONGO = +0.0408` in our convention, and `A_LONGO_PUBLISHED_SIGNED = -0.0408` in Longo's. The mandatory `BATTERY-SIGN` criterion is that an injected `-0.0408` sky is never called `REPRODUCED-LONGO` (the parent's enumerated REPRODUCED verdict); failure is `ABSOLUTE-ANCHOR-FAIL`.

10.2 BS-4's input digest, expected sign convention, instrument digest, environment, output digest, and PASS must be written to the journal.

10.3 A BS-4 failure yields `ABSOLUTE-ANCHOR-FAIL`; no real image is opened.

10.4 Only after BS-4 passes are real mapping-split images opened and measured.

10.5 On the mapping split, first encode GZ1 screen labels as `g=+1` for clockwise and `g=-1` for anticlockwise.

10.6 Compute the raw same-sign proportion `p_map = count(machine_sign = g) / n_map`.

10.7 Define mapping strength `d_map = abs(2*p_map - 1)`.

10.8 The fixed mapping margin is 0.10.

10.9 A relative mapping is chosen iff `d_map >= 0.10`. Equality at 0.10 chooses a mapping.

10.10 If `p_map > 0.5`, signed GZ label is `s=g`. If `p_map < 0.5`, signed GZ label is `s=-g`.

10.11 If `p_map = 0.5`, then `d_map=0`, so the rule necessarily reports `UNDETERMINED-SIGN`.

10.12 If `d_map < 0.10`, report `UNDETERMINED-SIGN` and stop before opening or measuring any estimation-split image.

10.13 Mapping-split agreement is used only to choose or refuse the relative mapping. It is not pooled into the reported concordance estimand.

## 11. Sample adequacy

11.1 The mapping split requires at least `n_map = 100` successfully prescribed objects and the estimation split requires at least `n_est = 400`.

11.2 These floors are fixed from the two-sided 95% Wilson interval at worst-case `p=0.5`: its approximate half-width is at most 0.098 for n=100 and at most
0.049 for n=400, using `z=1.959963984540054`.

11.3 Adequacy is evaluated on the frozen eligible split before measurement. Because no post-measurement deletion is permitted, any later missing result is a failure verdict, not a reduced denominator.

11.4 If either frozen split misses its floor, report `INSUFFICIENT-SAMPLE` and open no real image.

## 12. Estimands and uncertainty

12.1 The primary estimand is the signed inter-method agreement rate on the estimation split: `p_hat = count(machine_sign = signed_GZ_label) / n_est`.

12.2 The numerator and denominator include every frozen estimation-split object.

12.3 The complementary rate is `q_hat = 1 - p_hat` and means signed inter-method disagreement, not an error rate against truth.

12.4 The sign-invariant robustness statistic is `R = abs(2*p_hat - 1)`.

12.5 Report the two-sided 95% Wilson score interval for `p_hat` with `z=1.959963984540054`:

`center = (p_hat + z^2/(2*n_est)) / (1 + z^2/n_est)`;

`half = z/(1 + z^2/n_est) * sqrt(p_hat*(1-p_hat)/n_est + z^2/(4*n_est^2))`;

`CI95 = [center-half, center+half]`.

12.6 Report the complementary interval as `[1-CI95_upper, 1-CI95_lower]`.

12.7 No bootstrap, continuity correction, multiplicity adjustment, weighting, covariate adjustment, subgroup selection, or alternative interval is primary.

12.8 Counts by GZ1 class and split may be reported descriptively if fixed in the completion schema; no subgroup concordance claim is authorized.

## 13. Verdicts and numeric bands

13.1 Verdict precedence is the order listed below; the first applicable verdict is final and no later ordinary verdict is formed.

13.2 `VOID-BLIND-VIOLATION`: any protected Tier-A or parent object is rendered, measured, labelled, or exposed to a pixel-access path.

13.3 `COMPLETENESS-FAIL`: the complete no-magnitude crossmatch or its receipt does not satisfy §5.

13.4 `DATA-INTEGRITY-FAIL`: any required catalogue, manifest, brick, companion, coordinate, probability, pixel, hash, or receipt input is missing, malformed, non-finite, contradictory, or mismatched.

13.5 `INSTRUMENT-INTEGRITY-FAIL`: the instrument bytes or required environment do not equal the frozen identity.

13.6 `WRONG-PARITY-REFUSAL`: any effective geometry has wrong parity.

13.7 `ABSOLUTE-ANCHOR-FAIL`: BS-4 does not pass before real image access.

13.8 `INSUFFICIENT-SAMPLE`: `n_map < 100` or `n_est < 400` at sample freeze.

13.9 `MEASUREMENT-FAIL`: any prescribed instrument result is missing, zero, non-finite, malformed, or throws an exception.

13.10 `NONDETERMINISTIC-INSTRUMENT`: an exact repeat differs.

13.11 `UNDETERMINED-SIGN`: `abs(2*p_map-1) < 0.10`.

13.12 If none of 13.2--13.11 applies, the ordinary numeric verdict is:

- `CONCORDANT`: `0.70 <= p_hat <= 1.00`;

- `INTERMEDIATE-CONCORDANCE`: `0.30 < p_hat < 0.70`;

- `DISCORDANT`: `0.00 <= p_hat <= 0.30`.

13.13 Boundary equality at 0.70 is `CONCORDANT`; boundary equality at 0.30 is `DISCORDANT`.

13.14 Every ordinary verdict prints `n_map`, `p_map`, mapping orientation, `d_map`, `n_est`, agreement numerator, `p_hat`, Wilson lower and upper bounds, `q_hat`, its interval, and `R`.

13.15 The words concordant and discordant describe methods, not truth accuracy.

## 14. Claims boundary

14.1 This study measures **INTER-METHOD CONCORDANCE** on its own selected, matched, high-confidence, renderable Tier-C population.

14.2 It does not measure either method's accuracy against true handedness.

14.3 It does not apportion disagreements between the instrument, GZ1 humans, shared ambiguity, correlated errors, parity conventions, or selection effects.

14.4 It does not estimate, calibrate, validate, or modify `a-hat` (`â`) or any attenuation parameter.

14.5 It does not modify, reopen, validate, rescue, or supply labels to the frozen flagship run.

14.6 It does not transfer to Tier A, Tier B, the 65,060 parent, the 49,211 mask, all GZ1, all DR10-south, any other survey, or any other selection.

14.7 It does not establish parity truth merely because BS-4 and GZ1 agree; shared or correlated parity errors remain possible.

14.8 It does not authorize a sky dipole, anisotropy, population prevalence, class-balance, or causal claim.

## 15. Blind protection and void condition

15.1 No object in the 49,211-object Tier-A mask is rendered, measured, labelled, or allowed to reach any image-opening function under this study.

15.2 No object anywhere in the 65,060-object protected parent is rendered, measured, labelled, or allowed to reach any image-opening function.

15.3 The Tier-A/Tier-B exclusion filter is executed and receipted before any pixel path is resolved or opened.

15.4 A machine guard compares every requested identity and coordinate against both protected pins at the inclusive 1.0-arcsec radius and refuses before open.

15.5 Any violation, including accidental access, voids the entire study as `VOID-BLIND-VIOLATION`; deleting logs or outputs cannot cure it.

15.6 Tier B remains **HELD pending a principal ruling** and is excluded even if it would increase sample size or mapping strength.

15.7 Tier A remains untouched and the P0 blind remains intact.

## 16. Custody, sealing, and receipts

16.1 Before pixel access, seal by SHA-256: this signed preregistration and freeze record; GZ1 files; Tier-A and parent pins; completeness receipt; canonical crossmatch candidates; exclusions; frozen pair manifest; split manifest; Tier-C brick manifest; published checksum source; instrument; BS-4 fixture; rendering configuration; software lock/environment record; and verdict program.

16.2 The verdict program is mechanical transcription only of §§10--13 and is sealed before pixels. A discrepancy between it and this text is a defect and stops the study; prose governs until a newly signed preregistration exists.

16.3 Journal every seal-time file verification, guard decision, image open, render, instrument call, repeat call, BS-4 event, mapping computation, estimation computation, refusal, and verdict in the chained seal journal whose receipt schema and digest rule are defined in §7.10. This seal journal is distinct from the unchained acquisition JSONL journal with the exact seven-key schema in §7.9.

16.4 Per-object rows and instrument outputs remain sealed private artifacts. Aggregate completion and verdict receipts may be released.

16.5 The completion receipt contains at minimum: all pins from 16.1; journal head and record count; all catalogue funnel counts; ambiguity counts; resolution of all 13,725 prior unresolved positions; eligible and split counts; brick and companion counts; integrity totals; protected-guard totals; BS-4 result; mapping statistics; estimation statistics; Wilson interval; complementary rate and interval; robustness statistic; final verdict; start/end UTC timestamps; and the identity of the executing custodian.

16.6 The completion receipt is canonical JSON: UTF-8, sorted keys, no insignificant whitespace, LF terminated, JSON finite numbers only, and no duplicate keys.

16.7 Its `verdict_block` has the exact closed field set `schema_version`, `verdict`, `n_map`, `k_map_raw_same`, `p_map`, `mapping`, `mapping_strength`, `n_est`, `k_agree`, `p_agree`, `wilson95_low`, `wilson95_high`, `q_disagree`, `q_wilson95_low`, `q_wilson95_high`, `robustness`, `prereg_sha256`, `sample_manifest_sha256`, `brick_manifest_sha256`, `instrument_sha256`, and `journal_head_sha256`. Every key is present in every output and no extra key is permitted. A defined `mapping` is exactly `SAME` for §10.10's `s=g` orientation or `INVERTED` for its `s=-g` orientation. On a refusal, only a count, mapping, or estimand field that is undefined because its computation stage was not reached is JSON `null`; the five SHA-256 identity fields remain populated when the input schema and digests are valid. If the input object or a required digest itself is malformed, those untrusted identity fields are undefined and therefore JSON `null`.

16.7a `prereg_sha256` is exactly the SHA-256 of the signed preregistration file: this document, at the version Duho signed, computed over the §17.1--17.4 preimage in which the entire `DUHO SIGNATURE:` line is replaced by `DUHO SIGNATURE:` immediately followed by LF, the file is UTF-8 with LF line endings and ends in LF, and nothing else is blanked, normalized, or excluded. The seat running the seal computes it at seal time, before any pixel access, records it in the freeze record, supplies it to the verdict program as input, and the program echoes it unchanged in the verdict block. It can never be the digest of a later revision; any mismatch voids the run.

16.7b The verdict-program input is exactly one JSON object with the following exact top-level key set and types: `blind_violation`, `completeness_pass`, `data_integrity_pass`, `instrument_integrity_pass`, `wrong_parity`, `absolute_anchor_pass`, `measurement_pass`, and `deterministic_pass` are JSON booleans; `objects` is a JSON list; and `prereg_sha256`, `sample_manifest_sha256`, `brick_manifest_sha256`, `instrument_sha256`, and `journal_head_sha256` are lowercase 64-character SHA-256 hexadecimal strings. Every element of `objects` is exactly one JSON object with the following exact key set and types: `gz1_objid` is a non-negative JSON integer, `gz_label` is the JSON integer `+1` or `-1` under §10.5 and §9.5, and `machine_sign` is the JSON integer `+1` or `-1` under §9.5. Every listed key is mandatory; no extra top-level or row key is permitted. Any deviation in key set or type, including a Boolean used as an integer, yields `DATA-INTEGRITY-FAIL`.

16.7c `data_integrity_pass` is true if and only if the §7.11 seal receipt shows `files_checked == manifest_count == 17947`, `mismatches == 0`, complete published-checksum re-fetch with `published_checksum_refetch_complete == true` and `published_checksum_disagreements == 0`, the §7.11 Git custody receipt passed, and the §7.11 acquisition-completion set condition held; otherwise it is false. The seal seat MUST pass that derived value. A run whose seal receipt is absent or inconsistent with the passed Boolean is void.

16.7d `completeness_pass` is true if and only if the §5 completeness receipt satisfies every condition in §5, including the complete no-magnitude crossmatch and all required terminal dispositions; otherwise it is false, and the seal seat MUST pass that derived value.

16.7e `instrument_integrity_pass` is true if and only if every §9 instrument-byte digest and required-environment check passes for every invocation; otherwise it is false, and the seal seat MUST pass that derived value.

16.7f `blind_violation` is true if and only if any event prohibited by §15 occurred or any §15 guard receipt records protected-object access; if all required §15 guard checks passed and no such event occurred it is false, and the seal seat MUST pass that derived value.

16.7g `wrong_parity` is true if and only if the prescribed §8 geometry check finds an effective source-to-output Jacobian with wrong parity; if every prescribed parity check passes it is false, and the seal seat MUST pass that derived value.

16.7h `absolute_anchor_pass` is true if and only if the §10/BS-4 anchor, including its rendering-and-instrument-chain and `BATTERY-SIGN` requirements, passed and was receipted before any real pixel access; otherwise it is false, and the seal seat MUST pass that derived value.

16.7i `measurement_pass` is true if and only if every prescribed object has exactly one §9.5 nonzero finite, correctly shaped machine-sign result with no missing output or exception and no prohibited object deletion; otherwise it is false, and the seal seat MUST pass that derived value.

16.7j `deterministic_pass` is true if and only if every exact rerun required by §9.7 reproduces the original binary64 `chi` bytes for every prescribed object; otherwise it is false, and the seal seat MUST pass that derived value.

16.8 `schema_version` is exactly `GZ-TIERC-VERDICT-1`. The allowed `verdict` vocabulary is exactly the tokens in §13.

16.9 For a non-ordinary verdict, inapplicable numeric fields are JSON `null`; fabricated zeroes are prohibited. All applicable values must recompute exactly from the sealed rows under this document.

16.10 The pinned verdict program writes exactly one canonical JSON object plus LF to stdout; that object is the complete §16.7 `verdict_block`, populated from its sealed rows, refusal gates, and five required SHA-256 input identities. A standalone verifier must recompute split membership, all counts, mapping, estimands, Wilson intervals, numeric band, receipt chain, and all referenced SHA-256 values. Any mismatch yields `DATA-INTEGRITY-FAIL`.

16.11 The final verdict block is therefore machine-checkable and not a narrative judgment.

16.12 Verdict-program fixture receipt: `python3 miniprereg_pins/test_concordance_verdict.py` produced:

```text
.............
----------------------------------------------------------------------
Ran 13 tests in 0.084s

OK
```

This fixture receipt is the real output of the most recent run and may change in each version; refreshing it is an authorized version change.

The V7 pin audit independently re-hashed all six unchanged §2 pinned files and confirmed the §2.10, §2.11, §2.12, §2.13, and §2.14 digests exactly as printed. It also re-hashed the unchanged live acquisition source and confirmed its §2.14 digest and byte-identity pin. No pinned file changed and no placeholder is present.

## 17. Freeze procedure and change control

17.1 Duho first fills `SIGNATURE UTC`, then states, in the Blanc chat channel, the exact 64-hex SHA-256 digest of the resulting file computed with the value after `DUHO SIGNATURE:` blank, while retaining that literal field and all following lines, plus that UTC time. Blanc relays Duho's statement verbatim as a `RELAY FROM DUHO` message, and Hwao records it in the freeze record together with the relay text. This statement is Duho's signature. No SSH key, detached signature, or digest helper is required; a helper may be used to preview the digest but is not part of the signature. This is the P0 blank-signature-line convention.

17.2 For hashing, the blank line is exactly `DUHO SIGNATURE:` followed immediately by LF. The file is UTF-8 with LF line endings and ends in LF.

17.3 The freeze record holds the digest, the UTC time Duho stated, Blanc's verbatim relay text, and the relay timestamp. The line after `DUHO SIGNATURE:` in the file may carry the digest and UTC as stated because verification replaces that entire line with the blank form before hashing.

17.4 No field other than `DUHO SIGNATURE:` is blanked, normalized, or excluded when reconstructing the hash preimage.

17.5 Duho's signature freezes every constant, threshold, source, order, exclusion, formula, verdict, and custody rule in this document.

17.6 Any proposed change after signature requires a new version, a disclosed diff, a new blank-line digest, and, before Duho's signature, a fresh hostile referee report on the full revised text returning exactly `SIGNABLE`. A revision signed without that fresh `SIGNABLE` report is void. Only then may a new Duho signature authorize any further real image access. If real pixels or outputs were already seen, the present study is closed; the change cannot retroactively rescue it.

17.7 A chat statement of a digest that does not equal the recomputed blank-signature-line digest of the file is not a signature and freezes nothing. The operative order is Duho's chat statement, then Blanc's verbatim relay, then Hwao's freeze record; any discrepancy among the three voids the signature. Because the repository does not contain cryptographic proof of the original chat statement, verifying the signature from the repository alone requires trusting that the freeze record accurately captured the relay. If the external chat history is lost, the chain of trust rests entirely on the recorded relay; this is an explicit custody limit of this mechanism, accepted by Duho's ruling 'b'.

## 18. Referee dispositions

| Finding | Disposition |
|---|---|
| F1 FATAL | CLOSED by F4: the rebuilt and pinned verdict program emits the complete closed §16.7 JSON object, including every estimand and identity field; §16 states the defined `null` cases and binds stdout directly to `verdict_block`. |
| F2 FATAL | CLOSED by F8: canonical V134 lines 124--129 were quote-diffed, are quoted verbatim in §10, and carry East-of-North, both signed `0.0408` constants, BATTERY-SIGN refusal, and this study's pre-GZ rendering+instrument-chain meaning; the pinned BS-4 specification carries the same constants. |
| F3 MINOR | §6.2 now uses agy's exact required GZ1_OBJID formatting wording. |
| F4 FATAL | CLOSED: `concordance_verdict.py` now emits one canonical JSON object with exactly all 21 §16.7 fields and no extras; ordinary outputs carry all estimands, while §16.7 precisely limits refusal-time `null` values. |
| F5 MAJOR | CLOSED: the pinned fixture now has one test for each of the eight Boolean refusal gates read by the program and a test for the exact closed stdout key set; the real 13-test run is pasted in §16.12. |
| F6 MAJOR | CLOSED: the live `fetch_bricks.py` was copied byte-for-byte to `miniprereg_pins/fetch_bricks_pinned.py` and that static path is pinned in §2.14; both copies independently hashed to the ruled digest at pin time, without modifying the live file or running fetch. |
| F7 FATAL | CLOSED: §17.6 requires a fresh hostile full-text referee report returning `SIGNABLE` before Duho may sign any post-signature revision, and declares a bypassing signature void; frozen rule 97 registers this boundary. |
| F8 MINOR | CLOSED: §10.1a cites canonical V134; a quote-diff re-verified that its lines 124--129 are character-identical to the imported block. |
| F9 FATAL | CLOSED AS CONVENTION ONLY; the referee's “hallucinated instruction” characterization is rejected because Hwao's V2 brief did specify `COUNT: <pins in V2>`. V3 returns to V1's convention: the trailer counts the §19 frozen-rule register, whose introduction is restored and whose new rule 97 records F7. |
| F10 FATAL | CLOSED: §16.7a defines `prereg_sha256` exactly over the signed V4 §17.1--17.4 preimage, assigns seal-time pre-pixel computation to the seat running the seal, requires freeze-record storage, verdict-program input and unchanged echo, and voids any mismatch or later-revision digest. |
| F11 FATAL | CLOSED: §§7.9--7.11 retain the exact 17,947-brick completion set and journal bindings; §7.11 now requires the seal seat to independently re-fetch every ruled NERSC checksum file, bind all 17,947 fetched values by one ordered-lines digest, re-hash every on-disk brick against the fresh value, and cross-check both receipt digests. Section 16.7c binds every required result to `data_integrity_pass`. |
| F12 MINOR | CLOSED: §19 is in clause order and now registers all 178 load-bearing clauses in §§1--17, including the eight F20 Boolean-derivation clauses; the trailer count equals 178. |
| F13 FATAL | CLOSED: §16.7b states the exact 14-key top-level input schema and exact three-key object-row schema, with the types and fail-closed behavior enforced by the unchanged pinned verdict program. |
| F14 FATAL | CLOSED: §7.11 gives the true three-blob chronology, the exact `ad21829fa` UTC committer instant, the independently counted 42-receipt pre-commit gap, and the argv witness without treating Git as a witness to working-tree bytes during that gap. The independent fresh-source disk re-hash makes the script untrusted by construction, while the chained Git custody receipt still binds the resumed run and freeze state. |
| F15 MINOR | CLOSED under the coordinator's ruling: §16.12 states that the fixture receipt is the real most-recent-run output and that refreshing it each version is authorized; V7 records the fresh 13-test result at 0.084s. |
| F16 FATAL | CLOSED: §7.11 records all three true blobs and commits, the first receipt and 42-receipt/2-minute-48-second pre-commit gap at the exact `2026-09-02T05:30:32Z` committer instant, the exact Tier-C argv, the three argparse additions unique to `df704bed...`, and the post-commit 15:25 KST resumption; it states precisely that Git does not witness which working-tree bytes ran during the gap. |
| F17 FATAL | CLOSED: §7.11 mandates a freeze-time, seal-seat programmatic disk re-hash of every manifest brick against independently re-fetched NERSC values, records the ordered 17,947-line binding digest and all completeness/disagreement fields in a chained receipt, and refuses before pixels on any missing or unequal input. Section 16.7c makes `data_integrity_pass` true if and only if that receipt, Git custody, and completion set all pass. |
| F18 FATAL | CLOSED: a read-only JSON parse counted 42 live-journal receipts with `utc < "2026-09-02T05:30:32Z"`; §7.11 uses 42 everywhere and derives the cutoff from the exact `git show -s --format=%cI ad21829fa` result converted to UTC. |
| F19 FATAL | CLOSED: §7.11 quotes `published_sha()` lines 57--65 to show the URL convention, then requires a polite independent freeze-time fetch of each exact §2.14 checksum file, an ordered-lines aggregate digest, on-disk comparison to each fresh published value, and receipt values only as cross-checks; any fetch failure, missing line, or disagreement refuses before pixels. |
| F20 FATAL | CLOSED by option (b), without changing the pinned verdict program: §§16.7c--16.7j define the if-and-only-if receipt derivation of every Boolean input, require the seal seat to pass each derived value, and make an absent or inconsistent data-integrity receipt void. |
| F21 MINOR | CLOSED: §7.11 now says exactly, “Git does not witness which working-tree bytes ran during those minutes.” |
| V8 | §17 signature mechanism changed to chat signature by Duho's ruling “b” (Blanc relay 2026-09-02 17:20 KST); ruling “a” (validation only, nothing feeds the flagship) stands. |
| F22 FATAL | CLOSED in V9: §17.7 explicitly states that repository-only verification requires trusting the freeze record's capture of Blanc's relay and that loss of the external chat history leaves the chain of trust entirely on the recorded relay, an explicit custody limit accepted by Duho's ruling 'b'. |
| V10 | §7.9 corrected after the first real seal-gate run (07:46 KST) refused the journal's `FETCH-FAILED` receipt; four pinned-script verdicts described exactly; discovered under Duho's overnight ruling “Hwao a”. |
| V11 | Coverage plane inverse-variance → exposure count by Duho's ruling 'b' (Blanc relay 2026-09-03 15:20 KST), then repaired before signature under Hwao's DISCLOSED KNOWN EXTRAS ruling: receipted superseded invvar-r files remain untouched and are excluded only from the extra-file check. Ruling 'a' (validation only) and every other clause remain unchanged. |

## 19. Frozen rule register

The `COUNT` trailer counts the following 180 load-bearing constants or rules, rebuilt sequentially in clause order. Each entry identifies its cited clause; the cited clause's full text is the registered rule:

001 §1.1 — The sole purpose is to measure inter-method concordance between the frozen DESI image instrument…; 002 §1.2 — This study is authorized in design by Duho's direction #55 of 2026-09-02, conditional on…; 003 §1.3 — The approximately 208 GiB acquisition is separately pre-authorized. Acquisition authorization is not measurement authorization.; 004 §1.4 — No image may be rendered, no instrument output may be formed, and no real…; 005 §1.5 — Catalogue-only construction, integrity verification, manifest construction, and completeness proof may precede signature only if…; 006 §1.6 — Any deviation from a frozen rule below stops the study. It is not repaired…; 007 §1.7 — A stopped or refused run reports the applicable non-ordinary verdict and does not silently…; 008 §2.1 — GZ1 Table 2 is the official file GalaxyZoo1_DR_table2.csv.gz, locally staged as scratch/gz1_t2.csv.gz, with SHA-256…; 009 §2.2 — GZ1 Table 3 is the official file GalaxyZoo1_DR_table3.csv.gz, locally staged as scratch/gz1_t3.csv.gz, with SHA-256…; 010 §2.3 — Table 2 must contain exactly 667,944 data rows and Table 3 exactly 225,268 data…; 011 §2.4 — Only fields OBJID, RA, DEC, P_CW, and P_ACW are used. No debiased, spiral, elliptical,…; 012 §2.5 — Tier A is defined by ../_successor_build_20260824/acquire/positions_selected_cut.csv, 49,211 data rows, SHA-256 a20682c114508dbdd18ede6a56c61509ea9c16784aaca7eee61f76bf97cdd372.; 013 §2.6 — The protected parent is defined by ../_successor_build_20260824/acquire/positions_selected.csv, 65,060 data rows, SHA-256 425a42c3ea2a6004a08b52c27201dbf59546e88fef4f3d3ba6d2ffb5a3f70831.; 014 §2.7 — Tier B means parent members not in Tier A. Tier B is HELD pending…; 015 §2.8 — DESI catalogue candidates are all objects in the complete public DR10-south Tractor catalogue, release…; 016 §2.9 — The reconnaissance predicate dered_mag_r < 20 was an accelerator only. It is prohibited from…; 017 §2.10 — The verdict program is miniprereg_pins/concordance_verdict.py, SHA-256 587870e9f35d2c096f68cd10a769ab9c7eee6580d8b9cdee580b521cae63b070. Its fixture test is miniprereg_pins/test_concordance_verdict.py, SHA-256 2373e122c458d3b0a2cda85560f87741a07bd99ea013922667d8c08e23f24f1d.; 018 §2.11 — The BS-4 fixture specification is miniprereg_pins/bs4_sign_anchor_spec.md, SHA-256 c9aee6d6cdfba4722a396f55b27c8a7c58d5ecc7dbbd2da4414a969fe2b95f0b.; 019 §2.12 — The rendering configuration is miniprereg_pins/render_config.json, SHA-256 8a6ba7984b5d4e1ae2b900943a2e1f842706bed6f367831884a992edb573ffa7.; 020 §2.13 — The seal-time software/environment record schema is miniprereg_pins/env_record_schema.json, SHA-256 0607538bd41d49650e62ba33c833fe287f6e7df41cc0a6aaa6ca7c26932689b9. The record produced at seal…; 021 §2.14 — The published NERSC per-brick checksum source convention is the exact URL pattern https://portal.nersc.gov/cfs/cosmo/data/legacysurvey/dr10/south/coadd/<AAA>/<brick>/legacysurvey_dr10_south_coadd_<AAA>_<brick>.sha256sum, where…; 022 §3.1 — GZ1 sexagesimal RA is parsed as 15 (hours + minutes/60 + seconds/3600) degrees.; 023 §3.2 — GZ1 sexagesimal declination is parsed with the printed leading sign applied to the whole…; 024 §3.3 — DESI RA and declination are parsed as IEEE-754 binary64 degrees in ICRS.; 025 §3.4 — Every coordinate and probability must exist, parse uniquely, and be finite. RA must satisfy…; 026 §3.5 — Angular separation is the great-circle separation on the unit sphere, computed in binary64 from…; 027 §3.6 — The inclusive match radius is exactly 1.0 arcsecond. Equality at 1.0 arcsecond is accepted.; 028 §3.7 — All candidate DESI objects at separation <= 1.0 arcsecond are enumerated. A nearest-neighbour query…; 029 §3.8 — Duplicate OBJID rows within or across GZ1 Tables 2 and 3 are a catalogue…; 030 §3.9 — A GZ1 object with zero DR10-south candidates is unmatched and not eligible.; 031 §3.10 — A GZ1 object with two or more DR10-south candidates inside 1.0 arcsecond is ambiguous…; 032 §3.11 — After rule 3.10, if two or more GZ1 objects point to the same DR10…; 033 §3.12 — The ambiguity exclusions are computed from coordinates and identifiers before P_CW, P_ACW, image pixels,…; 034 §4.1 — Tier assignment priority is A, then B, then C, at the GZ1-object level.; 035 §4.2 — For each GZ1 object, first enumerate all Tier-A candidates within 1.0 arcsecond. If at…; 036 §4.3 — Otherwise enumerate all Tier-B candidates within 1.0 arcsecond. If at least one exists, assign…; 037 §4.4 — Otherwise apply the complete DR10-south matching and ambiguity rules in §3. A GZ1 object…; 038 §4.5 — Thus Tier C is disjoint both from the 49,211-object Tier-A mask and from every…; 039 §4.6 — The protected-parent filter is applied before any image-path resolution, file opening, pixel access, rendering,…; 040 §4.7 — The eligible GZ1 label is clockwise iff P_CW >= 0.8 and P_ACW < 0.8.; 041 §4.8 — The eligible GZ1 label is anticlockwise iff P_ACW >= 0.8 and P_CW < 0.8.; 042 §4.9 — The threshold is inclusive: equality at 0.8 qualifies.; 043 §4.10 — If neither probability reaches 0.8, the object is below threshold and is not in…; 044 §4.11 — If both probabilities reach 0.8, the label is contradictory and the study refuses with…; 045 §4.12 — No P_CW + P_ACW threshold, vote-count threshold, magnitude cut, or later visual-quality cut applies.; 046 §4.13 — The final eligible unit is one unique pair (GZ1_OBJID, DR10_RELEASE, DR10_BRICKID, DR10_OBJID) satisfying every…; 047 §4.14 — Pair rows are canonically sorted by the integer value of GZ1_OBJID, then integer DR10_BRICKID,…; 048 §5.1 — Before sample freeze, the definitive crossmatch must be recomputed against the complete DR10-south Tractor…; 049 §5.2 — The 13,725 outside-parent GZ1 footprint positions unresolved by the reconnaissance accelerator, including the 561…; 050 §5.3 — A count inferred from brick rectangles, an r < 20 query, a lower bound,…; 051 §5.4 — The completeness receipt must bind the full GZ1 input digests, full DR10-south catalogue release…; 052 §5.5 — The receipt must prove that every one of the 893,212 GZ1 rows was considered…; 053 §5.6 — It must also prove that candidate enumeration was complete inside 1.0 arcsecond, rather than…; 054 §5.7 — Any missing prior-unresolved OBJID, nonterminal position, duplicate terminal record, catalogue-partition gap, query truncation, magnitude…; 055 §5.8 — Only after the completeness receipt passes are the Tier-C pairs and the below-threshold/ambiguous/excluded counts…; 056 §6.1 — The frozen sample manifest contains only the canonical pair identity, catalogue coordinates, P_CW, P_ACW,…; 057 §6.2 — For each eligible object, compute h = SHA256(ASCII base-10 string representation of the integer…; 058 §6.3 — Interpret the 32 digest bytes as one unsigned big-endian integer.; 059 §6.4 — The split modulus is 5. Residue h mod 5 = 0 is the sign-mapping…; 060 §6.5 — Split membership is never rebalanced, stratified, redrawn, or changed for sample size, class balance,…; 061 §6.6 — The sample manifest SHA-256 and row count are written into a signed freeze record…; 062 §6.7 — The two splits are disjoint by GZ1_OBJID, DR10_OBJID, and collision construction. No object contributes…; 063 §7.1 — The sole ruled image source is the NERSC Legacy Surveys DR10-south coadd brick tree.…; 064 §7.2 — Whole published R-band coadd brick files are acquired and cut locally.; 065 §7.3 — The Tier-C brick manifest contains every primary and neighbour brick needed to form every…; 066 §7.4 — The brick manifest is canonically UTF-8 serialized with LF endings, sorted by brick name,…; 067 §7.5 — The exact brick-manifest SHA-256 and record count are pinned in the sample freeze record…; 068 §7.6 — Every acquired brick must match its per-brick published SHA-256 before it may enter rendering.…; 069 §7.7 — Required maskbits and R-band exposure-count (`nexp-r`) companions are included in the manifest and verified to their published hashes under the same rule; exact filename convention and a probed checksum line are quoted.; 070 §7.8 — Missing, extra, duplicate, substituted, or hash-mismatched required files yield DATA-INTEGRITY-FAIL; they do not remove…; 071 §7.9 — Acquisition and verification append one JSON object per attempted brick; exactly four verdicts use their prescribed seven-key or five-key receipt shape, and OK-NO-PUBLISHED-SHA is non-OK for completion…; 072 §7.10 — The distinct seal journal governed by §16.3 is chained. Each canonical seal receipt binds…; 073 §7.11 — The 17,947-brick v1 set and v3 three-plane list govern per-plane completion journals, mandatory freeze-time disk re-hash of all three files per brick, and one binding digest over all 53,841 fetched checksum lines.; 074 §7.11 — Receipted superseded invvar-r files are disclosed known extras excluded only from the seal extra-file check; the growing journal is identified and hashed and counted at seal time, while every unreceipted extra still refuses.; 075 §8.1 — Each scientific raster is exactly 128 by 128 pixels and subtends exactly 33.536 by…; 076 §8.2 — The output is a TAN WCS centered on the exact catalogue (RA, Dec) parsed…; 077 §8.3 — In FITS one-based pixel-center convention, NAXIS1=NAXIS2=128, CRPIX1=CRPIX2=64.5, CRVAL1=RA, and CRVAL2=Dec.; 078 §8.4 — The output CD matrix in degrees per pixel is exactly CD1_1=-0.262/3600, CD1_2=0, CD2_1=0, CD2_2=+0.262/3600.; 079 §8.5 — There is no object-dependent rotation. The display and instrument raster are north-up and east-left.; 080 §8.6 — Parity is strictly preserved through WCS transforms, array-axis conversion, storage, display, and model input.…; 081 §8.7 — An effective source-to-output Jacobian with the wrong parity refuses the cutout and yields WRONG-PARITY-REFUSAL;…; 082 §8.8 — All required neighbouring bricks are stitched before reprojection. A home-brick seam is not an…; 083 §8.9 — Exactly one deterministic bilinear reprojection maps the stitched inputs to the output WCS. Binary64…; 084 §8.10 — Resizing, further interpolation, rotation, transpose, PSF homogenization, padding, wrapping, reflection, intensity-conditioned source choice, and…; 085 §8.11 — The identical reprojected raster is supplied to the unmirrored branch and to the instrument's…; 086 §8.12 — Every output pixel requires valid image, maskbits, and exposure-count coverage (`nexp-r` > 0) from the verified stitched inputs; missing or non-finite required values fail the study.; 087 §8.13 — The prose constants in this §8 and the pinned miniprereg_pins/render_config.json must agree exactly. Any…; 088 §9.1 — The sole instrument is ../_successor_build_20260824/ref/successor_ref_v9.py, SHA-256 6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148.; 089 §9.2 — Those bytes are run as-is. Any edit, patch, copied modification, monkey patch, changed weight,…; 090 §9.3 — Before every invocation, the file digest is recomputed and compared to the pin. The…; 091 §9.4 — The instrument score is its frozen antisymmetric quantity chi(x) = (w(x) - w(mirror(x)))/2.; 092 §9.5 — The raw machine sign is +1 iff chi > 0 and -1 iff chi…; 093 §9.6 — chi = 0, a missing output, a non-finite output, wrong shape, exception, or nondeterministic…; 094 §9.7 — One exact rerun of every object with the identical raster and environment must reproduce…; 095 §10.1 — Before any real image is opened, the frozen BS-4 synthetic absolute-sign anchor in §2.11…; 096 §10.1a — The canonical parent preregistration, ../_successor_build_20260824/PREREG_SUCCESSOR_DRAFT_V134_20260831.md, lines 124--129, was re-verified by quote-diff and is imported…; 097 §10.1b — Therefore this study uses the East-of-North convention, A_LONGO = +0.0408 in our convention, and…; 098 §10.2 — BS-4's input digest, expected sign convention, instrument digest, environment, output digest, and PASS must…; 099 §10.3 — A BS-4 failure yields ABSOLUTE-ANCHOR-FAIL; no real image is opened.; 100 §10.4 — Only after BS-4 passes are real mapping-split images opened and measured.; 101 §10.5 — On the mapping split, first encode GZ1 screen labels as g=+1 for clockwise and…; 102 §10.6 — Compute the raw same-sign proportion p_map = count(machine_sign = g) / n_map.; 103 §10.7 — Define mapping strength d_map = abs(2p_map - 1).; 104 §10.8 — The fixed mapping margin is 0.10.; 105 §10.9 — A relative mapping is chosen iff d_map >= 0.10. Equality at 0.10 chooses a…; 106 §10.10 — If p_map > 0.5, signed GZ label is s=g. If p_map < 0.5, signed…; 107 §10.11 — If p_map = 0.5, then d_map=0, so the rule necessarily reports UNDETERMINED-SIGN.; 108 §10.12 — If d_map < 0.10, report UNDETERMINED-SIGN and stop before opening or measuring any estimation-split…; 109 §10.13 — Mapping-split agreement is used only to choose or refuse the relative mapping. It is…; 110 §11.1 — The mapping split requires at least n_map = 100 successfully prescribed objects and the…; 111 §11.2 — These floors are fixed from the two-sided 95% Wilson interval at worst-case p=0.5: its…; 112 §11.3 — Adequacy is evaluated on the frozen eligible split before measurement. Because no post-measurement deletion…; 113 §11.4 — If either frozen split misses its floor, report INSUFFICIENT-SAMPLE and open no real image.; 114 §12.1 — The primary estimand is the signed inter-method agreement rate on the estimation split: p_hat…; 115 §12.2 — The numerator and denominator include every frozen estimation-split object.; 116 §12.3 — The complementary rate is q_hat = 1 - p_hat and means signed inter-method disagreement,…; 117 §12.4 — The sign-invariant robustness statistic is R = abs(2p_hat - 1).; 118 §12.5 — Report the two-sided 95% Wilson score interval for p_hat with z=1.959963984540054:; 119 §12.6 — Report the complementary interval as [1-CI95_upper, 1-CI95_lower].; 120 §12.7 — No bootstrap, continuity correction, multiplicity adjustment, weighting, covariate adjustment, subgroup selection, or alternative interval…; 121 §12.8 — Counts by GZ1 class and split may be reported descriptively if fixed in the…; 122 §13.1 — Verdict precedence is the order listed below; the first applicable verdict is final and…; 123 §13.2 — VOID-BLIND-VIOLATION: any protected Tier-A or parent object is rendered, measured, labelled, or exposed to…; 124 §13.3 — COMPLETENESS-FAIL: the complete no-magnitude crossmatch or its receipt does not satisfy §5.; 125 §13.4 — DATA-INTEGRITY-FAIL: any required catalogue, manifest, brick, companion, coordinate, probability, pixel, hash, or receipt input…; 126 §13.5 — INSTRUMENT-INTEGRITY-FAIL: the instrument bytes or required environment do not equal the frozen identity.; 127 §13.6 — WRONG-PARITY-REFUSAL: any effective geometry has wrong parity.; 128 §13.7 — ABSOLUTE-ANCHOR-FAIL: BS-4 does not pass before real image access.; 129 §13.8 — INSUFFICIENT-SAMPLE: n_map < 100 or n_est < 400 at sample freeze.; 130 §13.9 — MEASUREMENT-FAIL: any prescribed instrument result is missing, zero, non-finite, malformed, or throws an exception.; 131 §13.10 — NONDETERMINISTIC-INSTRUMENT: an exact repeat differs.; 132 §13.11 — UNDETERMINED-SIGN: abs(2p_map-1) < 0.10.; 133 §13.12 — If none of 13.2--13.11 applies, the ordinary numeric verdict is:; 134 §13.13 — Boundary equality at 0.70 is CONCORDANT; boundary equality at 0.30 is DISCORDANT.; 135 §13.14 — Every ordinary verdict prints n_map, p_map, mapping orientation, d_map, n_est, agreement numerator, p_hat, Wilson…; 136 §13.15 — The words concordant and discordant describe methods, not truth accuracy.; 137 §14.1 — This study measures INTER-METHOD CONCORDANCE on its own selected, matched, high-confidence, renderable Tier-C population.; 138 §14.2 — It does not measure either method's accuracy against true handedness.; 139 §14.3 — It does not apportion disagreements between the instrument, GZ1 humans, shared ambiguity, correlated errors,…; 140 §14.4 — It does not estimate, calibrate, validate, or modify a-hat (â) or any attenuation parameter.; 141 §14.5 — It does not modify, reopen, validate, rescue, or supply labels to the frozen flagship…; 142 §14.6 — It does not transfer to Tier A, Tier B, the 65,060 parent, the 49,211…; 143 §14.7 — It does not establish parity truth merely because BS-4 and GZ1 agree; shared or…; 144 §14.8 — It does not authorize a sky dipole, anisotropy, population prevalence, class-balance, or causal claim.; 145 §15.1 — No object in the 49,211-object Tier-A mask is rendered, measured, labelled, or allowed to…; 146 §15.2 — No object anywhere in the 65,060-object protected parent is rendered, measured, labelled, or allowed…; 147 §15.3 — The Tier-A/Tier-B exclusion filter is executed and receipted before any pixel path is resolved…; 148 §15.4 — A machine guard compares every requested identity and coordinate against both protected pins at…; 149 §15.5 — Any violation, including accidental access, voids the entire study as VOID-BLIND-VIOLATION; deleting logs or…; 150 §15.6 — Tier B remains HELD pending a principal ruling and is excluded even if it…; 151 §15.7 — Tier A remains untouched and the P0 blind remains intact.; 152 §16.1 — Before pixel access, seal by SHA-256: this signed preregistration and freeze record; GZ1 files;…; 153 §16.2 — The verdict program is mechanical transcription only of §§10--13 and is sealed before pixels.…; 154 §16.3 — Journal every seal-time file verification, guard decision, image open, render, instrument call, repeat call,…; 155 §16.4 — Per-object rows and instrument outputs remain sealed private artifacts. Aggregate completion and verdict receipts…; 156 §16.5 — The completion receipt contains at minimum: all pins from 16.1; journal head and record…; 157 §16.6 — The completion receipt is canonical JSON: UTF-8, sorted keys, no insignificant whitespace, LF terminated,…; 158 §16.7 — Its verdict_block has the exact closed field set schema_version, verdict, n_map, k_map_raw_same, p_map, mapping,…; 159 §16.7a — prereg_sha256 is exactly the SHA-256 of the signed preregistration file: this document, at the…; 160 §16.7b — The verdict-program input is exactly one JSON object with the following exact top-level key…; 161 §16.7c — data_integrity_pass is true if and only if the §7.11 seal receipt, Git custody receipt, and acquisition-completion set condition all satisfy the exact ruled conditions; otherwise false, with absent or inconsistent receipt making the run void.; 162 §16.7d — completeness_pass is derived if and only if every §5 completeness condition passes.; 163 §16.7e — instrument_integrity_pass is derived if and only if every §9 byte and environment check passes.; 164 §16.7f — blind_violation is derived if and only if a §15 prohibited event or protected-access guard receipt exists.; 165 §16.7g — wrong_parity is derived if and only if a §8 prescribed geometry check finds wrong effective parity.; 166 §16.7h — absolute_anchor_pass is derived if and only if every §10/BS-4 requirement passes before real pixels.; 167 §16.7i — measurement_pass is derived if and only if every prescribed object has its valid §9 result without deletion.; 168 §16.7j — deterministic_pass is derived if and only if every §9.7 rerun reproduces the binary64 chi bytes.; 169 §16.8 — schema_version is exactly GZ-TIERC-VERDICT-1. The allowed verdict vocabulary is exactly the tokens in §13.; 170 §16.9 — For a non-ordinary verdict, inapplicable numeric fields are JSON null; fabricated zeroes are prohibited.…; 171 §16.10 — The pinned verdict program writes exactly one canonical JSON object plus LF to stdout;…; 172 §16.11 — The final verdict block is therefore machine-checkable and not a narrative judgment.; 173 §16.12 — The real most-recent-run fixture output is receipted and its version-by-version refresh is authorized:; 174 §17.1 — Duho first fills SIGNATURE UTC, then states, in the Blanc chat channel, the exact 64-hex SHA-256…; 175 §17.2 — For hashing, the blank line is exactly DUHO SIGNATURE: followed immediately by LF. The…; 176 §17.3 — The freeze record holds the digest, the UTC time Duho stated, Blanc's verbatim relay text, and…; 177 §17.4 — No field other than DUHO SIGNATURE: is blanked, normalized, or excluded when reconstructing the…; 178 §17.5 — Duho's signature freezes every constant, threshold, source, order, exclusion, formula, verdict, and custody rule…; 179 §17.6 — Any proposed change after signature requires a new version, a disclosed diff, a new….; 180 §17.7 — A mismatched chat digest freezes nothing; repository-only verification trusts the recorded relay, and loss of external chat leaves the chain of trust entirely on that relay as an explicit custody limit….

## 20. Signature block

Principal: Duho Kim

Decision requested: freeze and authorize this validation measurement exactly as written after all pre-pixel completeness and integrity gates pass.

SIGNATURE UTC: 2026-09-03T07:05:00Z

DUHO SIGNATURE: 622d08a0c475b21edf3d8d53c569fd2ff7e840a9cfbabf3f384e1d16948042f3 at 2026-09-03T07:05:00Z (chat signature via Blanc relay, §17.1)

SEAT: CODEX
VERSION: MINI-PREREG-DRAFT-V11
COUNT: 180
