# MEDIUM disclosure method — 2026-09-07

Authoring deliverable for V15 §6. This file specifies the implementation now;
it contains no real tuning evidence or authorization to execute a study stage.

## Governing text, read directly

[OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V15_20260906.md](../../OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V15_20260906.md),
§6, lines 47–48 (line 48 quoted verbatim):

> Rejecting maskbits: {1 BRIGHT, 3 SATUR_R, 6 ALLMASK_R, 10 BAILOUT, 13 CLUSTER}. Bit 11 MEDIUM is NOT rejecting; it is carried (§8.9d) and reported per raster as a covariate. Source pixels with nexp-r == 0 are REJECTING (replaced by the §8.9c lower median and flagged), in place of the present all-or-nothing §8.12 refusal — **this is a relaxation** of §8.12 (one unexposed pixel no longer refuses the raster), bounded by §8.14a's unchanged ceiling F ≤ 819 and unchanged protected radius r_T = 23 (a zero-exposure pixel inside 23 px still refuses). Replacement statistic unchanged. Fixture updated to assert the new set both ways. These rules are frozen by this rule's signature and by the pipeline amendment's; no preprocessing change of any kind is permitted afterwards, in particular none between the holdout result and attempt 2, and none after attempt 2. Supporting evidence: the DR9 definitions (semantics draft §2) and a LABEL-BLIND perturbation study specified here and run on the development TUNING set only: for every tuning object with MEDIUM-flagged pixels, compute chi with MEDIUM pixels (i) kept and (ii) replaced by the lower median, report the sign-flip rate; the rule above does not depend on the outcome (it is already fixed) — the study is a filed disclosure of what the relaxation costs the estimator. Seat B's position that the MEDIUM reading is an empirical claim, not a definitional one, is recorded as correct; this study is the answer.

V15 references §8.9c/§8.9d; these are not sections inside the 72-line V15
document. Their governing source is
[MINI_PREREG_GZ_TIERC_DRAFT_V35_20260905.md](../../MINI_PREREG_GZ_TIERC_DRAFT_V35_20260905.md).
The retained provisions read as follows, with V15 §6 overriding the old
rejection-bit set and the zero-exposure rule.

Line 334, §8.9c, verbatim:

> 8.9c **Rejected source pixels are replaced before reprojection**, so no contaminated value enters the bilinear operator. The replacement is the LOWER median of the accepted source pixels — for an even count the lower middle value, so the result is always an observed pixel value and never an average of two. A source with fewer than `16` accepted pixels yields `NO-ACCEPTED-PIXELS`, a `DATA-INTEGRITY-FAIL` under §13.4, because a median over a handful of survivors is not a background estimate. No interpolation, smoothing, inpainting or randomness is used.

Line 338, §8.9d, verbatim:

> 8.9d **Which OUTPUT pixels the contamination touched is read exactly, not propagated as a weight.** The renderer samples the integer planes — `maskbits` and `nexp` — by NEAREST NEIGHBOUR, which is an index selection rather than a resampling, and returns them as integers. The rendered `maskbits` plane therefore still carries true bit semantics, and an output pixel is FLAGGED if and only if its own rendered maskbits value has a rejecting bit set. No fractional contamination weight exists and none is needed.

[AGREEMENT_RUN_V15_CLAUSE_DISPOSITION_20260907.md](../../AGREEMENT_RUN_V15_CLAUSE_DISPOSITION_20260907.md),
line 81 retains the tuning-only label-blind MEDIUM perturbation/sign-flip
disclosure. V15 line 51 places development input access after adoption and
the prospective split; lines 52–54 fix the existing 96 configurations and
treat zero/nonfinite/nonrepeated scores as unscored.

## Fixed computation

The only public operation is
`medium_perturbation.produce_tuning_disclosure(objects, /)`.
It returns a JSON-compatible disclosure. It has no preprocessing, estimator,
configuration, winner, label, reader, output-path, or stage-selection argument.
Every input row must declare exactly `stage="tuning"`.

1. Validate the whole batch against the closed input schema before any
   rendering. Reject duplicate IDs, extra fields, nonnumeric planes, lazy
   readers, object arrays and non-tuning records.
2. On each source grid, use `pixel_rejection_v2.medium_mask` to find bit 11.
   No source MEDIUM pixels means no pair. Otherwise render the KEPT arm
   through `render_chain_v3.render_object`. The per-raster MEDIUM count is
   the renderer's nearest-neighbour integer-plane covariate. A zero output
   count means no pair, even if another part of the source brick has MEDIUM.
   A render failure before that count is available is retained as
   `ELIGIBILITY-UNRESOLVED`.
3. KEPT uses the original source image and the fixed V15 rejection rule:
   bits 1/3/6/10/13 or zero exposure. MEDIUM alone is retained. Pixels also
   carrying an ordinary rejection condition remain ordinarily rejected.
4. For REPLACED, let B be the existing ordinary rejection mask and M the
   existing bit-11 mask. Call
   `pixel_rejection_v2.replacement_value(image, B | M)`.
   Thus the accepted source population for this arm excludes both ordinary
   rejects and MEDIUM. The statistic is the global lower median, including
   its existing minimum of 16 accepted pixels. Copy the source image and set
   its MEDIUM pixels to this value BEFORE reprojection.
5. Pass that copy, the ORIGINAL maskbits and nexp, and the SAME WCS through
   the SAME render chain. This diagnostic never invents a rejecting bit.
   The chain still executes ordinary replacement, one bilinear reprojection,
   nearest-neighbour integer carriage, F≤819, r_T=23, the protected-region
   refusal, and §8.15 normalization/casting. Its ordinary cleaning obtains
   the same replacement scalar: adding copies of a lower median to its
   accepted population leaves that lower median unchanged.
6. Decode each successful chain tensor as 128×128 little-endian float32.
   Use `fourier_chirality.Estimator.chi` for both arms and repeat each
   evaluation on a copy, comparing binary32 patterns. No Fourier estimator,
   reprojection, rejection test, median, or normalization is reimplemented.
   The label-requiring `run_path.score_object` is deliberately not called.
7. Two repeatable, finite, nonzero chi values give an eligible pair.
   `sign_flipped` is true exactly when their signs differ; it is false
   when the signs agree. A tie, nonfinite value, nonrepeat, score exception
   or rendering refusal gives an unscored pair with reasons and a null
   flip indicator. No retry, object replacement, or deletion occurs.

The two-arm rule above is fixed in source. Both arms are mandatory; neither
can be chosen as a production preprocessing variant based on the disclosure.
MEDIUM remains nonrejecting in the actual scientific pipeline.

## Configuration scope and reporting

V15 §6 names chi without specifying one of §7's 96 configurations. The
producer therefore mechanically discloses ALL 96 existing configurations,
in `enumerate_configs()` order, with no subset, default-only choice, winner
input, ranking, or selection. This is a disclosure across the already-fixed
grid; it adds no search choice.

For every MEDIUM object and every configuration, report both chi values,
their binary32 and repeat patterns, score statuses/reasons, signs, eligibility
and flip indicator. Also retain source/output MEDIUM counts, the perturbation
median, and each arm's render receipt (including tensor digest but not tensor
bytes). Objects without MEDIUM retain an empty pair list.

For EACH configuration separately:

- `eligible_objects` is the number of MEDIUM objects with two comparable signs.
- `flips` is the number whose signs differ.
- `sign_flip_rate = flips / eligible_objects`.
- A zero denominator yields null, never zero percent.
- Retain unscored-pair counts and the batch's unresolved-eligibility count.
  A rate with excluded unscored/unresolved objects is marked INCOMPLETE;
  it is a rate among comparable objects, not a full-corpus conclusion.

The report never pools the 96 configurations into an object denominator.
There is no unique single-configuration rate or scientific winner chosen by
this module. No p-value, agreement with labels, tuning objective, or
production-rule change is computed.

## Label-blind input and execution boundary

The batch is an exact built-in tuple. Rows are exact built-in dicts with ONLY
`objid, stage, image, maskbits, nexp, wcs, ra, dec, brick`.
Unknown fields are rejected before their values are read. Pixel planes must
be exact NumPy ndarrays with plain real/integer dtypes; object/structured
arrays, memmap subclasses and conversion hooks are refused.

WCS input is an exact dict with ONLY numeric `crpix` and `crval` pairs
and a numeric 2×2 `cd` tuple. Astropy constructs the distortion-free
RA---TAN/DEC--TAN transform in degrees. No FITS header, WCS object with
arbitrary attributes, catalogue row, path, inventory, label map, or callback
can be supplied in its place. The future upstream caller must ensure that
this numeric representation is lossless for its source WCS; non-TAN or
distorted WCS has no representation in this API and must not be truncated
to fit. No actual source WCS was opened in this authoring task.

The producer imports only the numeric renderer/scorer components, NumPy,
Astropy WCS and os for fixed thread settings. It does not import run_path,
the approval recorder, the selector, or any catalogue/label loader. It has
no runtime file, network or subprocess operation and cannot request a missing
input. It returns the disclosure to its caller for later filing.

The synthetic suite checks label arguments and extra label fields are refused
without inspecting their sentinel values; nested label-bearing metadata,
lazy readers and array-conversion hooks are refused. An audit hook then
denies ALL file opens, sockets and subprocess events during a real two-arm,
96-configuration computation, which succeeds without any such event.

This is a closed computational input boundary, not a claim that Python is an
OS sandbox. Arbitrary code mutation, hostile monkey-patching, or encoding a
label as an ordinary numeric pixel is outside that boundary. Code identity
must be fixed before study use. Import-time renderer loading reads its fixed
geometry JSON; it does not read study data.

## Chronology and explicit limits

**Real tuning evidence is produced only at the tuning stage, after adoption
and the seed.** This authoring task executes synthetic rasters only. It does
not create a sample, seed, round, anchor, holdout, real disclosure result, or
approval.

The function validates a tuning-only schema; it cannot establish adoption,
chronology, actual draw membership, completeness of the 400-object input,
source-checksum provenance or WCS-extraction fidelity from numeric inputs
alone. Those belong to the later authorized tuning caller. No existing
run_path code or manifest was changed, and run_path does not yet call this
new function automatically.

The code makes these operational conventions explicit because §6 does not
spell them out: all 96 configurations are disclosed rather than guessing a
single configuration; source pixels accepted for the replacement median
exclude MEDIUM; output-mask carriage determines object membership; unscored
pairs remain visible and do not become false nonflips. It would require a
new scientific instruction to claim that §6 prescribes some different
single-configuration aggregate or a denominator that assigns signs to
unscored measurements. No outcome-dependent option was added to resolve
those gaps.
