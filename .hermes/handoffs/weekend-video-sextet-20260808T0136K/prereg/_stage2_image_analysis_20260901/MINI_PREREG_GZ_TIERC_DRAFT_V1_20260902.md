# MINI-PREREGISTRATION — GZ1 × DESI TIER-C INTER-METHOD CONCORDANCE

Draft V1 for principal signature, 2026-09-02.

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

6.2 For each eligible object, compute `h = SHA256(ASCII decimal GZ1_OBJID with no sign, whitespace, or leading zero)`.

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

7.7 Required maskbits and R-band inverse-variance companions are included in the manifest and verified to their published hashes under the same rule.

7.8 Missing, extra, duplicate, substituted, or hash-mismatched required files yield `DATA-INTEGRITY-FAIL`; they do not remove an object from a split.

7.9 Acquisition and verification append one canonical JSON receipt per event to an append-only JSONL receipt journal. Each receipt binds timestamp, operation, relative path, expected digest, observed digest, byte count, status, predecessor receipt digest, and current receipt digest.

7.10 The receipt digest is SHA-256 over the canonical receipt body excluding its own `receipt_digest`; the chain predecessor of the first record is 64 zeroes.

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

8.12 Every output pixel requires valid image, maskbits, and inverse-variance coverage from the verified stitched inputs. Any missing or non-finite required value yields `DATA-INTEGRITY-FAIL` for the study, not an object-level deletion.

## 9. Frozen instrument and machine sign

9.1 The sole instrument is `../_successor_build_20260824/ref/successor_ref_v9.py`, SHA-256 `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`.

9.2 Those bytes are run as-is. Any edit, patch, copied modification, monkey patch, changed weight, alternate implementation, or replacement invalidates the entire study and yields `INSTRUMENT-INTEGRITY-FAIL`.

9.3 Before every invocation, the file digest is recomputed and compared to the pin. The environment demanded by the frozen instrument is used unchanged.

9.4 The instrument score is its frozen antisymmetric quantity `chi(x) = (w(x) - w(mirror(x)))/2`.

9.5 The raw machine sign is `+1` iff `chi > 0` and `-1` iff `chi < 0`.

9.6 `chi = 0`, a missing output, a non-finite output, wrong shape, exception, or nondeterministic repeat is `MEASUREMENT-FAIL` for the study. There is no tie-breaker, epsilon, abstention deletion, or retry with altered data.

9.7 One exact rerun of every object with the identical raster and environment must reproduce the binary64 `chi` bytes; disagreement yields `NONDETERMINISTIC-INSTRUMENT` and stops.

## 10. Absolute anchor, relative mapping, and ordering

10.1 Before any real image is opened, the frozen BS-4 synthetic absolute-sign anchor is run through the pinned instrument and must pass its frozen expected absolute sign convention.

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

16.3 Journal every file verification, guard decision, image open, render, instrument call, repeat call, BS-4 event, mapping computation, estimation computation, refusal, and verdict in the chained receipt journal of §7.

16.4 Per-object rows and instrument outputs remain sealed private artifacts. Aggregate completion and verdict receipts may be released.

16.5 The completion receipt contains at minimum: all pins from 16.1; journal head and record count; all catalogue funnel counts; ambiguity counts; resolution of all 13,725 prior unresolved positions; eligible and split counts; brick and companion counts; integrity totals; protected-guard totals; BS-4 result; mapping statistics; estimation statistics; Wilson interval; complementary rate and interval; robustness statistic; final verdict; start/end UTC timestamps; and the identity of the executing custodian.

16.6 The completion receipt is canonical JSON: UTF-8, sorted keys, no insignificant whitespace, LF terminated, JSON finite numbers only, and no duplicate keys.

16.7 Its `verdict_block` has the exact closed field set `schema_version`, `verdict`, `n_map`, `k_map_raw_same`, `p_map`, `mapping`, `mapping_strength`, `n_est`, `k_agree`, `p_agree`, `wilson95_low`, `wilson95_high`, `q_disagree`, `q_wilson95_low`, `q_wilson95_high`, `robustness`, `prereg_sha256`, `sample_manifest_sha256`, `brick_manifest_sha256`, `instrument_sha256`, and `journal_head_sha256`.

16.8 `schema_version` is exactly `GZ-TIERC-VERDICT-1`. The allowed `verdict` vocabulary is exactly the tokens in §13.

16.9 For a non-ordinary verdict, inapplicable numeric fields are JSON `null`; fabricated zeroes are prohibited. All applicable values must recompute exactly from the sealed rows under this document.

16.10 A standalone verifier must recompute split membership, all counts, mapping, estimands, Wilson intervals, numeric band, receipt chain, and all referenced SHA-256 values. Any mismatch yields `DATA-INTEGRITY-FAIL`.

16.11 The final verdict block is therefore machine-checkable and not a narrative judgment.

## 17. Freeze procedure and change control

17.1 Duho first fills `SIGNATURE UTC`, then signs the SHA-256 of the resulting file computed with the value after `DUHO SIGNATURE:` blank, while retaining that literal field and all following lines. This is the P0 blank-signature-line convention.

17.2 For hashing, the blank line is exactly `DUHO SIGNATURE:` followed immediately by LF. The file is UTF-8 with LF line endings and ends in LF.

17.3 The signed digest and detached signature are recorded in the freeze record. The signature may also be copied after `DUHO SIGNATURE:` because verification replaces that entire line with the blank form before hashing.

17.4 No field other than `DUHO SIGNATURE:` is blanked, normalized, or excluded when reconstructing the hash preimage.

17.5 Duho's signature freezes every constant, threshold, source, order, exclusion, formula, verdict, and custody rule in this document.

17.6 Any proposed change after signature requires a new version, a disclosed diff, a new blank-line digest, and a new Duho signature before any further real image access. If real pixels or outputs were already seen, the present study is closed; the change cannot retroactively rescue it.

## 18. Frozen rule count register

The `COUNT` trailer counts the following 96 load-bearing constants or rules:

01 purpose; 02 Tier-C-only scope; 03 signature-before-measurement; 04 deviation stop; 05 GZ1 Table-2 identity; 06 GZ1 Table-3 identity; 07 GZ1 row counts; 08 allowed GZ1 fields; 09 Tier-A pin; 10 parent pin; 11 Tier-B hold; 12 complete DR10-south universe; 13 no magnitude accelerator; 14 RA parser; 15 Dec parser; 16 finite coordinate domains; 17 spherical separation; 18 1.0-arcsec inclusive; 19 enumerate all candidates; 20 duplicate-GZ integrity rule; 21 zero-candidate rule; 22 multi-DESI ambiguity rule; 23 multi-GZ collision rule; 24 ambiguity before labels; 25 tier priority A/B/C; 26 A exclusion; 27 B exclusion; 28 exact Tier-C pair; 29 parent-before-pixels guard; 30 CW threshold; 31 ACW threshold; 32 0.8 inclusive; 33 neither-threshold exclusion; 34 both-threshold refusal; 35 no auxiliary label cut; 36 canonical pair sort; 37 complete rematch; 38 resolve 13,725; 39 terminal disposition vocabulary; 40 no footprint inference; 41 completeness receipt contents; 42 all-GZ1 coverage proof; 43 candidate-completeness proof; 44 completeness-fail triggers; 45 freeze after completeness; 46 split SHA-256 preimage; 47 big-endian interpretation; 48 modulus 5; 49 residue-zero mapping split; 50 residues-one-through-four estimation split; 51 no split rebalance; 52 pre-pixel sample hash; 53 split disjointness; 54 NERSC path; 55 whole R-band bricks; 56 neighbour-complete manifest; 57 canonical brick manifest; 58 manifest pin at freeze; 59 published per-brick SHA-256; 60 companion inclusion; 61 integrity failure does not delete; 62 chained JSONL journal; 63 128-square geometry; 64 0.262 arcsec/pixel; 65 CRPIX 64.5; 66 exact CD matrix; 67 north-up/east-left; 68 strict parity; 69 wrong-Jacobian refusal; 70 stitch-neighbours-first; 71 one bilinear reprojection; 72 prohibited transforms; 73 identical mirror-branch raster; 74 complete companion coverage; 75 instrument path and SHA; 76 run as-is/edit voids; 77 per-call digest/environment; 78 frozen chi definition; 79 strict nonzero machine sign; 80 zero/nonfinite failure; 81 exact deterministic repeat; 82 BS-4 first; 83 BS-4 failure stop; 84 GZ sign encoding; 85 mapping proportion; 86 mapping margin 0.10; 87 mapping choice orientation; 88 undetermined-sign stop; 89 mapping not pooled; 90 adequacy floors 100/400; 91 Wilson z constant; 92 primary agreement estimand; 93 complementary rate; 94 robustness statistic; 95 verdict precedence/bands; 96 claims, blind, custody, machine-checkability, and signature-change boundary.

## 19. Signature block

Principal: Duho Kim

Decision requested: freeze and authorize this validation measurement exactly as written after all pre-pixel completeness and integrity gates pass.

SIGNATURE UTC:

DUHO SIGNATURE:

SEAT: CODEX
VERSION: MINI-PREREG-DRAFT-V1
COUNT: 96
