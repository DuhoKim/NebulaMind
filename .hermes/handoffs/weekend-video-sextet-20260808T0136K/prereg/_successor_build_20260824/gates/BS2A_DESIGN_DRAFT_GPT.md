# BS-2a acceptance design draft — GPT

Status: **DRAFT / NOT A FILLED BS-2a SLOT**

This is a design artifact, not a referee report. It does not modify the preregistration or
`successor_ref_v9.py`. It was drafted from the current §2.7, the BS-2a row, the full CODEX-V11
finding 3, the full GPT56-V11 finding F3, and the frozen v9 code.

The central design conclusion is a refusal, not a disguised acceptance:

> **REFUSE the current confidence exclusion as presently named.** The only frozen quantity that
> can presently play “confidence” is `abs(chi_net)`, with acceptance at
> `abs(chi_net) > tau`, where `tau = 4.4006456017494235`. That quantity is the magnitude of the
> handedness output itself. It therefore cannot satisfy §2.7's simultaneous requirement that an
> exclusion predicate be unable to read handedness amplitude. Renaming `abs(chi_net)` as
> `confidence` would reproduce the defect in a new vocabulary.

BS-2a can close only after one of the following is adopted in a fresh design revision and text/code
gate:

1. a separately produced, mirror-even quality quantity whose producer and data path cannot read
   `chi_net`, its sign, its magnitude, or axis-relative position, together with a synthetically
   frozen numeric threshold; or
2. removal of confidence-based exclusion, followed by a new calibration and power design that
   admits every finite instrument output, including zero and arbitrarily small magnitude.

This draft selects **(1) as the repair direction** and rejects (2), because (2) discards the
existing abstention/retention premise and would require re-establishing sign definition,
calibration and power from the ground up. It does **not** fabricate the missing mirror-even
quality producer or its numeric threshold. Until those exist, BS-2a remains unfilled and BS-6
remains blocked.

---

## 1. Requirement-by-requirement disposition

### R1 — the exact parent partition

**REPAIR.**

Artifact: `BS2AAcceptanceLedgerV1`.

Producer: `build_acceptance_ledger_v1()` in the future §0-pinned reference code, executed by a
separate isolated worker `acceptance_worker_v1.py`.

Verifier: `validate_acceptance_partition_v1()`; production `run_production_verdict()` must call it
before constructing or accepting a `SealedMask` and before reading any χ-bearing payload.

Failure: `AcceptanceContractError`. A missing parent ID, extra ID, duplicate ID, duplicate terminal
row, parent-digest mismatch, row-count other than 65,060, or any ID appearing other than exactly
once refuses the partition. It is not converted to a smaller study.

The equality checked is set equality against the independently pinned parent witness, not merely
`accepted_count + excluded_count == 65060`.

### R2 — evidence fields and types

**REPAIR.**

Artifact: `BS2AEvidenceBundleV1`, containing exactly one `AcceptanceEvidenceV1` record for each
parent ID. The normative schema is in §3 below.

Producers:

- parent projection: the pinned BS-2s parent producer;
- expected-cutout declaration: the BS-9 canonical cutout producer;
- actual-byte verification: `verify_cutout_bytes_v1()` in an independent verification process;
- attempt and execution records: the pinned BS-9 instrument runner;
- confidence record: the still-missing mirror-even quality producer described under R5;
- bundle: `build_acceptance_evidence_v1()`.

Verifier: `validate_acceptance_partition_v1()` recomputes the digest of every typed field and
refuses absent fields, malformed values, unjoined attempts, or disagreement between claimed and
recomputed values.

Failure: `AcceptanceContractError` with a stable error code and offending `objid`; it must not emit
χ, a sign, raw instrument output, RA/Dec, or axis-relative position in the error.

### R3 — exclusion predicates and the current closed list

**REFUSE the current list as presently instantiated; REPAIR its first three reasons.**

The first three reason families are right after they are made functions of typed evidence and
given deterministic precedence:

1. `CUTOUT_BYTE_INTEGRITY`
2. `CUTOUT_SHAPE_OR_DTYPE`
3. `INSTRUMENT_OUTPUT_ABSENT_OR_NONFINITE`

The fourth, `CONFIDENCE_BELOW_THRESHOLD`, is admissible only after R5's prerequisite exists. The
present `abs(chi_net) > tau` rule cannot fill it because it reads handedness amplitude exactly.

No “other”, free-text, operator, manual-review, morphology, visual-quality, scientific-interest,
sky-region, sign-balance, or post hoc failure reason is allowed. An additional reason requires a
new preregistration text and code gate before the first image byte.

### R4 — recomputation rather than labels

**REPAIR.**

Function:

```python
validate_acceptance_partition_v1(
    *,
    parent: ParentIdWitnessV1,
    evidence: BS2AEvidenceBundleV1,
    ledger: BS2AAcceptanceLedgerV1,
    design: BS2ADesignReceiptV1,
) -> ValidatedAcceptancePartitionV1
```

It takes no accepted flags, no exclusion-reason override, no χ-bearing receipt, no position array,
no axis, and no callback. It loads the design constants from the pinned `BS2ADesignReceiptV1`,
recomputes every raw predicate and the deterministic terminal decision, then compares the result
field-by-field with the supplied ledger.

It raises:

```python
class AcceptanceContractError(RuntimeError):
    code: AcceptanceErrorCode
    objid: Optional[int]
    fields: tuple[str, ...]
```

The exception representation is restricted to non-χ acceptance fields. Any disagreement in
status, reason, predicate bits, evidence digest, parent digest, attempt join, threshold digest,
row count, field type, or canonical serialization raises. There is no warning mode and no repair
mode in production.

`run_production_verdict()` must receive a `ValidatedAcceptancePartitionV1`, not a caller-created
mask or integer counts. `SealedMask` construction for production must be private to a factory that
accepts that validated partition. The current `n_receipts, n_parent` arguments and caller-supplied
accept flags are removed from the production signature.

### R5 — defined confidence quantity and one threshold home

**REFUSE until a prerequisite artifact exists.**

The present instrument defines:

```text
chi_net(x) = (f(x) - f(mirror(x))) / 2
current abstention quantity = abs(chi_net(x))
current threshold tau = 4.4006456017494235
```

That abstention quantity is handedness amplitude. It fails R6. It must not be copied into the new
acceptance evidence as `confidence`.

The prerequisite is a separately gated `QualityChannelDesignV1` with all of the following:

- one exact field name, `quality_score`;
- producer symbol `quality_score_v1()`;
- output type binary64 finite scalar on the closed interval `[0.0, 1.0]`;
- a source-level and runtime capability boundary proving the producer cannot call or receive
  `chi_net`, the handedness sign, `abs(chi_net)`, RA, Dec, `c = cos(theta)`, or `AXIS`;
- an exact mirror-even identity, including equality at the serialized-bit level:
  `quality_score_v1(x) == quality_score_v1(mirror(x))`;
- a frozen synthetic calibration manifest, objective and held-out receipt supporting one numeric
  `QUALITY_MIN`;
- behavior for equality: exclusion iff `quality_score < QUALITY_MIN`; equality is accepted;
- a frozen producer digest and fixtures.

The scalar's interpretation is “predeclared instrument-quality eligibility on a unit interval,”
not posterior probability of either handedness class and not a transformed χ magnitude. The
calibration authority is the named BS-2a producer, with Duho's freeze signature; an operator does
not set it at execution.

**Single home:** the numeric `QUALITY_MIN`, its comparison rule, calibration receipt digest and
producer digest live only in **BS-2a**. BS-3 retains instrument identity, handedness weights,
antisymmetry receipts and any historical description of `tau`, but must not contain an operative
acceptance threshold. If the old `tau` remains operative, the design is refused rather than
allowing two homes.

No numeric `QUALITY_MIN` is proposed here. Choosing one without the required synthetic quality
channel and calibration receipt would be fabrication.

### R6 — sign-blindness by construction

**REPAIR for the first three predicates; REFUSE to claim it for confidence until R5 exists.**

The construction has four independent barriers:

1. **Narrow type.** `AcceptanceEvidenceV1` has no handedness, χ, sign, amplitude, RA, Dec, `c`,
   axis, calibration-bin, or result-store locator field.
2. **Split receipts.** The instrument writes two separately typed outputs:
   `AcceptanceInstrumentReceiptV1` (attempt state, finite flag, output presence, quality score and
   non-χ digests) and `SealedHandednessReceiptV1` (χ/sign). The acceptance worker is permitted to
   open only the first type. A digest of the sealed receipt may be stored as an opaque execution
   binding, but the acceptance worker must not receive a path, decryption capability, payload, or
   callback that can resolve it.
3. **No geometry capability.** The parent input is a projection containing only `objid` and the
   parent witness digest. The worker receives neither the parent table with coordinates nor the
   `AXIS` constant.
4. **Pinned call graph.** A fixture inspects the reachable call graph and globals of
   `build_acceptance_evidence_v1()`, `derive_exclusion_predicates_v1()` and
   `validate_acceptance_partition_v1()`. Any reference to forbidden symbols or any generic
   dictionary/`**kwargs`/callback escape fails the BS-2a gate.

This is stronger than saying “the recompute is sign-blind.” The current v9 production runner is
not an example to copy: it accepts a receipt/mask path that can carry signs. The new acceptance
validator's inputs are incapable of carrying them.

The construction proves non-access, not statistical independence. Image quality can correlate
with sky location or galaxy morphology. That residual risk is named in §8.

### R7 — fixtures

**REPAIR.**

Artifact: `FIXTURES_BS2A_V1.out`, produced by `run_bs2a_fixtures_v1()` under the frozen environment
and sha-pinned in the BS-2a design receipt.

The required fixture battery is specified in §6. Missing fixture output, any `FAIL`, a digest
mismatch, or a source/call-graph probe that cannot run leaves BS-2a unfilled.

---

## 2. Replacement §2.7 text, ready to drop in

### §2.7 Acceptance and exclusion — derived partition, no caller labels

**Status of this subsection.** This rule is a class-P DESIGN prerequisite, BS-2a. It is not in
force until the text, schemas, code, isolated worker, fixtures and their exact digests are gated
and pinned before BS-6. BS-2f is only the later value artifact produced by those frozen bytes.

1. **Parent closure is set equality.** The BS-2s parent witness contains exactly 65,060 unique
   object IDs and its independently pinned digest. BS-2a's evidence bundle and terminal ledger
   must each contain exactly that ID set, once per ID, with no duplicate, omission or extra ID.
   `accepted_count + excluded_count = 65,060` is necessary but not sufficient.

2. **One typed evidence record per parent object.** `AcceptanceEvidenceV1` carries the parent ID and
   witness digest; expected and actual cutout checksums, shapes and dtypes; cutout-attempt state;
   the independently joined instrument attempt and execution receipt; output-present and
   finite-output flags; and, only after the quality-channel prerequisite is gated, its finite
   `quality_score` and producer receipt digest. Every record has a canonical evidence digest.
   Nullable fields are allowed only in the failure states enumerated by the schema; null is never
   an operator label.

3. **The closed predicate list.** Production recomputes these raw predicates from evidence alone:

   ```text
   P_BYTE  = expected checksum absent OR actual checksum absent
             OR actual checksum != expected checksum
   P_SHAPE = not P_BYTE AND
             (actual tensor shape != (1, 128, 128) OR actual dtype != '<f4')
   P_EXEC  = not P_BYTE AND not P_SHAPE AND
             (no joined successful execution receipt OR output absent OR output non-finite)
   P_QUAL  = not P_BYTE AND not P_SHAPE AND not P_EXEC AND
             quality_score < QUALITY_MIN
   ```

   `P_QUAL` is prohibited until `quality_score_v1()` and numeric `QUALITY_MIN` satisfy BS-2a. The
   current `abs(chi_net) > tau` abstention rule cannot fill this field because it is handedness
   amplitude.

4. **One deterministic terminal row.** Status is `ACCEPTED` iff all four predicates are false.
   Otherwise status is `EXCLUDED`, with the first true reason in this fixed precedence:
   `CUTOUT_BYTE_INTEGRITY`, `CUTOUT_SHAPE_OR_DTYPE`,
   `INSTRUMENT_OUTPUT_ABSENT_OR_NONFINITE`, `CONFIDENCE_BELOW_THRESHOLD`. The ledger also stores
   all four predicate bits, so precedence cannot conceal a second failure. No other reason or
   manual override exists.

5. **Retries are deterministic and outcome-blind.** Acquisition permits at most three total
   attempts for a missing or checksum-failing cutout. Instrument execution permits at most two
   total attempts only for process-level absence of a completed execution receipt. Attempt
   indices are fixed integers starting at zero; the first successful attempt by index is the
   selected receipt. A non-finite output or below-threshold quality score is terminal and is not
   retried. Re-execution to seek a different sign, magnitude, confidence or status voids the run.
   Every attempt, including failures, is in the independently enumerated attempt manifest.

6. **Labels are checked, never trusted.** `validate_acceptance_partition_v1(parent, evidence,
   ledger, design)` recomputes all predicate bits, terminal statuses, reasons, row digests and set
   digests. It raises `AcceptanceContractError` on any mismatch or missing artifact.
   `run_production_verdict()` accepts only the resulting `ValidatedAcceptancePartitionV1`; it no
   longer accepts caller-supplied acceptance flags or the integer pair `n_receipts, n_parent`.

7. **Blindness is a type and capability property.** The acceptance evidence and worker contain no
   χ, handedness sign, handedness amplitude, RA, Dec, `cos(theta)`, axis, calibration bin, or
   resolvable χ-bearing receipt. The handedness payload is a distinct sealed type inaccessible to
   the acceptance worker. Source/call-graph fixtures refuse any forbidden field, symbol, callback
   or generic payload escape. The quality channel must additionally be mirror-even bit-exactly
   and must be produced without receiving any handedness field.

8. **Digest custody.** The BS-2a design receipt pins the schemas, code, worker, quality-channel
   design, numeric threshold and fixtures. The realized BS-2f receipt binds the parent witness,
   evidence bundle, terminal ledger, accepted and excluded set digests, attempt-manifest digests,
   quality-design digest and validated-partition digest. A digest supplied alongside caller-made
   data is not custody; the production validator loads the pinned design witness itself.

9. **Failure consequence.** Missing BS-2a, missing evidence, an incomplete attempt join, any
   mismatch, any forbidden capability, or any post-first-image change to the rule refuses BS-2f
   and blocks Stage C and verdict production. It never silently reduces the parent.

---

## 3. Exact data contracts

### 3.1 Scalar aliases

```python
ObjId = int                  # range: 0 .. 2**63-1; canonical little-endian signed i8
Digest256 = str              # exactly 64 lowercase hexadecimal ASCII characters
Shape3 = tuple[int, int, int]
DTypeCode = Literal["<f4"]
AttemptIndex = int           # non-negative, acquisition 0..2; instrument 0..1
```

Booleans are canonical single bytes `b"0"` or `b"1"`; they are not integers. Optional values use
an explicit presence byte followed by the canonical value. JSON `null`, NaN spellings and
implementation-defined tuple/string representations are not canonical serialization.

### 3.2 `ParentIdWitnessV1`

```python
@dataclass(frozen=True)
class ParentIdWitnessV1:
    schema: Literal["bs2a-parent-ids/v1"]
    parent_digest: Digest256
    parent_count: int                 # must equal 65_060
    objids: tuple[ObjId, ...]          # strictly increasing, unique
    objids_digest: Digest256
    producer_receipt_digest: Digest256
```

The projection contains no brick ID or position. The producer derives it from the pinned parent;
the acceptance worker cannot accept a caller-supplied projection without matching all external
witness digests.

### 3.3 `AcceptanceEvidenceV1`

```python
@dataclass(frozen=True)
class AcceptanceEvidenceV1:
    schema: Literal["bs2a-evidence-row/v1"]
    objid: ObjId
    parent_digest: Digest256

    expected_cutout_sha256: Optional[Digest256]
    expected_tensor_shape: Shape3          # exactly (1, 128, 128)
    expected_dtype: DTypeCode              # exactly "<f4"
    cutout_attempt_count: int              # 1..3
    cutout_attempt_manifest_digest: Digest256

    actual_cutout_sha256: Optional[Digest256]
    actual_tensor_shape: Optional[Shape3]
    actual_dtype: Optional[DTypeCode]
    actual_byte_count: Optional[int]        # non-negative if present
    cutout_verifier_receipt_digest: Digest256

    instrument_attempt_count: int           # 0..2; zero only when cutout gate failed
    instrument_attempt_manifest_digest: Digest256
    selected_attempt_index: Optional[AttemptIndex]
    execution_receipt_digest: Optional[Digest256]
    execution_state: Literal[
        "NOT_RUN_CUTOUT_FAILED", "NO_COMPLETED_RECEIPT", "COMPLETED"
    ]
    output_present: bool
    output_finite: bool

    quality_score: Optional[float]           # binary64, finite, 0 <= q <= 1
    quality_receipt_digest: Optional[Digest256]
    quality_design_digest: Optional[Digest256]

    evidence_digest: Digest256
```

Nullability rules:

- `expected_cutout_sha256` may be null only if the canonical cutout producer failed to declare an
  expected output after all three attempts; this makes `P_BYTE` true.
- Actual cutout checksum/shape/dtype/byte count are all present together or all null together.
- Instrument fields are not allowed to claim `COMPLETED` unless the selected attempt exists in the
  independently enumerated attempt manifest and its receipt digest matches.
- `output_present == False` requires `output_finite == False` and null quality fields.
- `output_finite == False` requires null quality fields.
- Quality fields are all present together or all null together. Once R5 is filled, a completed,
  present, finite output requires all quality fields.
- No χ, sign, amplitude or object geometry field is permitted. Exact-field schema validation
  refuses extras.

### 3.4 Raw recomputation result

```python
@dataclass(frozen=True)
class DerivedAcceptanceV1:
    objid: ObjId
    p_byte: bool
    p_shape: bool
    p_exec: bool
    p_quality: bool
    status: Literal["ACCEPTED", "EXCLUDED"]
    reason: Literal[
        "NONE",
        "CUTOUT_BYTE_INTEGRITY",
        "CUTOUT_SHAPE_OR_DTYPE",
        "INSTRUMENT_OUTPUT_ABSENT_OR_NONFINITE",
        "CONFIDENCE_BELOW_THRESHOLD",
    ]
    evidence_digest: Digest256
    design_digest: Digest256
    row_digest: Digest256
```

`reason == "NONE"` iff status is `ACCEPTED`. No free text is serialized into the normative row.

### 3.5 Ledger and validated partition

```python
@dataclass(frozen=True)
class BS2AAcceptanceLedgerV1:
    schema: Literal["bs2a-ledger/v1"]
    parent_digest: Digest256
    evidence_bundle_digest: Digest256
    design_digest: Digest256
    rows: tuple[DerivedAcceptanceV1, ...]   # strictly increasing objid
    accepted_count: int
    excluded_count: int
    accepted_ids_digest: Digest256
    excluded_ids_digest: Digest256
    ledger_digest: Digest256

@dataclass(frozen=True)
class ValidatedAcceptancePartitionV1:
    schema: Literal["bs2a-validated-partition/v1"]
    parent_digest: Digest256
    evidence_bundle_digest: Digest256
    ledger_digest: Digest256
    design_digest: Digest256
    accepted_objids: tuple[ObjId, ...]
    excluded_objids: tuple[ObjId, ...]
    validated_partition_digest: Digest256
```

Construction of `ValidatedAcceptancePartitionV1` is private to the validator. A public dataclass
constructor or deserializer that lets a caller mint it is prohibited.

### 3.6 `BS2ADesignReceiptV1`

```python
@dataclass(frozen=True)
class BS2ADesignReceiptV1:
    schema: Literal["bs2a-design/v1"]
    parent_schema_digest: Digest256
    evidence_schema_digest: Digest256
    ledger_schema_digest: Digest256
    worker_sha256: Digest256
    reference_code_sha256: Digest256
    quality_design_digest: Digest256
    quality_producer_sha256: Digest256
    quality_min_f8le: bytes                 # exactly 8 bytes; finite value in [0, 1]
    quality_calibration_receipt_digest: Digest256
    retry_policy_digest: Digest256
    forbidden_capability_fixture_digest: Digest256
    fixtures_sha256: Digest256
    environment_digest: Digest256
    envelope_sha256: Digest256
```

Every field is required. In particular, a design receipt cannot be emitted with placeholders or
null quality fields. That is why this draft does not claim to fill BS-2a.

---

## 4. Predicate implementation and deterministic precedence

```python
def derive_exclusion_predicates_v1(
    row: AcceptanceEvidenceV1,
    design: LoadedPinnedBS2ADesignV1,
) -> DerivedAcceptanceV1:
    require_exact_evidence_schema(row)
    require_row_digest(row)
    require_parent_binding(row, design)
    require_attempt_joins(row, design)

    p_byte = (
        row.expected_cutout_sha256 is None
        or row.actual_cutout_sha256 is None
        or row.actual_cutout_sha256 != row.expected_cutout_sha256
    )

    p_shape = (
        not p_byte
        and (
            row.actual_tensor_shape != (1, 128, 128)
            or row.actual_dtype != "<f4"
        )
    )

    p_exec = (
        not p_byte
        and not p_shape
        and (
            row.execution_state != "COMPLETED"
            or row.execution_receipt_digest is None
            or not row.output_present
            or not row.output_finite
        )
    )

    require_quality_design_filled(design)  # BS-2a cannot run without it
    p_quality = (
        not p_byte
        and not p_shape
        and not p_exec
        and require_quality_score(row) < design.quality_min
    )

    bits = (p_byte, p_shape, p_exec, p_quality)
    if not any(bits):
        status, reason = "ACCEPTED", "NONE"
    else:
        status = "EXCLUDED"
        reason = (
            "CUTOUT_BYTE_INTEGRITY" if p_byte else
            "CUTOUT_SHAPE_OR_DTYPE" if p_shape else
            "INSTRUMENT_OUTPUT_ABSENT_OR_NONFINITE" if p_exec else
            "CONFIDENCE_BELOW_THRESHOLD"
        )

    return canonically_digest_derived_row(...)
```

All four predicate bits are computed. The short-circuit guards prevent absent downstream fields
from being misreported as additional reasons when an upstream stage could not run. The fixed
reason precedence is therefore diagnostic ordering, not operator choice.

---

## 5. Production integration contract

The future production signature is:

```python
def run_production_verdict(
    partition: ValidatedAcceptancePartitionV1,
    sealed_results: SealedHandednessStoreV1,
    cal: CalibrationReceiptV1,
    *,
    authorization: PinnedAuthorizationV1,
    stage_c_receipt: BS5FReceiptV1,
) -> VerdictReceiptV1:
    ...
```

Mandatory order:

1. `require_environment()`.
2. `require_authorization()`.
3. `require_validated_partition_v1(partition)`; this reloads the pinned BS-2a design receipt and
   verifies the validated-partition digest.
4. `join_sealed_results_to_accepted_ids_v1(partition, sealed_results)`; exact set equality is
   required, and no excluded result may enter.
5. construct the `SealedMask` privately from accepted IDs and separately loaded positions;
   caller-supplied accept flags are not an input.
6. require BS-5f against that exact mask digest.
7. continue with the existing calibration, power and permutation guards.

The acceptance validator must run before any production function resolves a χ-bearing payload.
The validator receives only an opaque sealed-results binding digest, if needed to prove execution
identity; it never receives a store locator or key.

`require_complete_sample(n_receipts, n_parent)` is retired from production. It may remain only as a
historical or test helper whose return cannot satisfy any production type.

---

## 6. Required synthetic fixtures

All fixture names and expected outcomes are binding.

### Partition and schema

- `BS2A-PARENT-EXACT`: a 12-ID synthetic parent, evidence and ledger pass.
- `BS2A-PARENT-MISSING`: omit one ID while preserving self-consistent counts/digests; refuse.
- `BS2A-PARENT-EXTRA`: add one non-parent ID; refuse.
- `BS2A-PARENT-DUPLICATE`: duplicate one ID and omit another so row count is unchanged; refuse.
- `BS2A-COUNTS-NOT-SETS`: accepted plus excluded count equals parent count but ID sets differ;
  refuse.
- `BS2A-EXTRA-FIELD`: add `chi`, `sign`, `ra`, `dec`, `c`, `axis_distance` and an unknown generic
  field one at a time; all refuse exact schema.
- `BS2A-NONCANONICAL`: uppercase digest, NaN, infinity, wrong endian float, integer boolean and
  malformed optional encoding; all refuse.

### Evidence and reasons

- `BS2A-BYTE-MISSING`: null expected or actual checksum yields exactly `P_BYTE` and the byte reason.
- `BS2A-BYTE-MISMATCH`: unequal checksums refuse any ledger claiming accepted.
- `BS2A-SHAPE`: `(1,127,128)`, `(128,128)`, wrong dtype and transposed layout each yield the shape
  reason after byte integrity passes.
- `BS2A-ATTEMPT-JOIN`: a claimed absent output with a successful independently listed receipt, and
  a claimed successful output absent from the attempt manifest, both refuse.
- `BS2A-NONFINITE`: NaN, positive infinity and negative infinity instrument outputs each produce
  the execution reason, without serializing the value into the acceptance evidence.
- `BS2A-QUALITY-BOUNDARY`: `nextafter(QUALITY_MIN, -inf)` excludes; exact equality and
  `nextafter(QUALITY_MIN, +inf)` accept, all using canonical binary64 bytes.
- `BS2A-MULTIPLE-FAILURES`: corrupt bytes plus missing execution plus absent quality sets only the
  gated raw bits allowed by upstream reachability and chooses the fixed first reason.
- `BS2A-FALSE-REASON`: for each reason, attach it to evidence for which its predicate is false;
  refuse.
- `BS2A-FALSE-ACCEPT`: mark a failing row accepted; refuse.
- `BS2A-FALSE-EXCLUDE`: mark a passing row excluded; refuse.

### Retries

- `BS2A-CUTOUT-RETRY-ORDER`: attempts 0 and 1 fail, 2 succeeds; attempt 2 is selected.
- `BS2A-CUTOUT-RETRY-CAP`: a fourth acquisition attempt exists; refuse the manifest.
- `BS2A-EXEC-RETRY-ORDER`: attempt 0 has no completed receipt and 1 completes; 1 is selected.
- `BS2A-NO-RETRY-NONFINITE`: an attempt after a completed non-finite output refuses as an
  unauthorized retry.
- `BS2A-NO-RETRY-QUALITY`: an attempt after a completed below-threshold quality result refuses.
- `BS2A-NO-BEST-OF`: two successful receipts or selection of a later receipt when an earlier
  successful one exists refuses.

### Recompute and production wiring

- `BS2A-RECOMPUTES`: mutate each supplied status, reason, predicate bit and evidence digest; every
  mutation refuses.
- `BS2A-NO-INTEGER-GUARD`: source inspection proves production no longer accepts
  `n_receipts, n_parent` as completeness evidence.
- `BS2A-NO-ACCEPT-FLAGS`: source inspection proves the production signature and mask factory expose
  no acceptance-flag argument.
- `BS2A-PROD-CALLS-VALIDATOR`: reachable call-graph inspection proves
  `run_production_verdict()` calls `require_validated_partition_v1()` before resolving sealed
  results.
- `BS2A-TYPE-CANNOT-MINT`: caller construction/deserialization of
  `ValidatedAcceptancePartitionV1` refuses.

### Blindness by construction

- `BS2A-FORBIDDEN-FIELDS`: exact schema excludes every χ, sign, amplitude and geometry field.
- `BS2A-FORBIDDEN-CALL-GRAPH`: reachable globals and callables contain none of `chi_net`, `abs_chi`,
  sign helpers, `AXIS`, `cos_theta`, position loaders, sealed-store openers, callbacks, `eval`,
  `exec`, generic dictionary payloads or `**kwargs`.
- `BS2A-SPLIT-RECEIPT`: acceptance worker cannot deserialize, locate or open a
  `SealedHandednessReceiptV1` even when handed its digest.
- `BS2A-MIRROR-EVEN`: bit-exact equality of `quality_score_v1(x)` and
  `quality_score_v1(mirror(x))` over the full frozen synthetic quality fixture manifest,
  including symmetric, near-symmetric, positive-winding and negative-winding pairs.
- `BS2A-SIGN-SWAP-INVARIANT`: replacing sealed χ with its negative under an unchanged acceptance
  receipt leaves every evidence byte, predicate, status, reason and partition digest unchanged.
- `BS2A-AXIS-PERMUTATION-INVARIANT`: permuting synthetic RA/Dec or changing a test-only axis while
  holding permitted evidence fixed leaves every acceptance byte unchanged; the production worker
  itself has no such inputs.
- `BS2A-AMPlITUDE-NOT-QUALITY` (literal fixture name preserved despite capitalization): mutate
  `abs(chi_net)` while holding the quality receipt fixed; acceptance is unchanged, and attempting
  to derive quality from that mutation fails the call-graph gate.

### Custody

- `BS2A-PINNED-DESIGN`: changing threshold bytes, schema bytes, worker bytes, quality-producer bytes
  or fixture bytes moves the design digest and refuses production.
- `BS2A-CALLER-TRUST`: a self-consistent caller-made evidence/ledger/design digest chain that does
  not match the externally pinned BS-2a witness refuses.
- `BS2A-WORKER-ISOLATED`: the production validator runs in the pinned isolated interpreter and
  returns its own code/environment provenance.

---

## 7. Conforming edits required elsewhere

These are edits the eventual design revision must make. This draft does not apply them.

### §0 — definition by code

- Pin the new reference code and `acceptance_worker_v1.py` bytes.
- Pin `FIXTURES_BS2A_V1.out` and the quality-channel fixture output.
- Add `BS2ADesignReceiptV1`, all acceptance types, canonical serialization,
  `derive_exclusion_predicates_v1()`, `build_acceptance_evidence_v1()`,
  `build_acceptance_ledger_v1()`, `validate_acceptance_partition_v1()` and the production mask
  factory to the normative code surface.
- Remove the claim that v9 implements this. It does not.

### §2.5 and BS-6 — acquisition

- State the fixed three-attempt cutout policy and the exact attempt-manifest producer.
- Require an expected-cutout declaration and independent actual-byte verifier per parent ID.
- Make BS-6 depend on a filled BS-2a design receipt, as the current dependency intends.

### §3 / admissible input

- State that production `SealedMask` objects can be made only by the private factory from a
  `ValidatedAcceptancePartitionV1` plus the separately pinned position witness.
- Remove caller acceptance flags from the production constructor/API.
- Keep χ-bearing and acceptance receipts as non-interchangeable types.

### §5 — production verdict

Replace the current completeness sentence and signature description. The current
`require_complete_sample()` comparison of two integers is not completeness. State that
`run_production_verdict()` requires the externally validated exact parent partition and then joins
sealed results to exactly the accepted ID set.

### §6.1 — blind automation

- Name `acceptance_worker_v1.py::validate_acceptance_partition_v1` as the acceptance recompute
  process only after that exact symbol exists and is pinned.
- Restrict it to `AcceptanceInstrumentReceiptV1`; do not authorize it to read generic instrument
  receipts carrying signs.
- Do not claim sign-blindness merely because its output omits signs.

### §7 — slot table

Replace the BS-2a row with:

| slot | producer | content | code symbol | blocks |
|---|---|---|---|---|
| BS-2a ⚠ DESIGN, CLASS P | Hwao drafts; named quality-channel producer measures synthetic calibration; Duho signs freeze; text-and-code referees gate | Parent/evidence/ledger schemas; fixed retry semantics; separately gated mirror-even `quality_score`; numeric `QUALITY_MIN` and its sole threshold home; isolated recomputation worker; exact partition validator; forbidden-capability and synthetic fixtures; all code/artifact/environment digests | `build_acceptance_evidence_v1`, `derive_exclusion_predicates_v1`, `validate_acceptance_partition_v1`, `run_bs2a_fixtures_v1` | BS-2f, BS-6 |

Replace the BS-2f row with:

| BS-2f | frozen BS-2a producer | value-only realized evidence bundle, terminal ledger, exact accepted/excluded ID partition, accepted-position mask and calibration boundaries; all bound to the BS-2a design and parent witnesses | `validate_acceptance_partition_v1`, private sealed-mask factory | Stage C |

Update BS-3 so it is not a second home for an operative acceptance threshold. If historical `tau`
remains documented there, label it historical/non-operative under this successor design. If the
study instead elects to keep `abs(chi_net) > tau`, R6 must be amended openly and freshly gated;
BS-2a cannot claim the present sign-blind contract.

### §7 class-P status sentence

Count BS-2a as unfilled until all required non-placeholder fields of `BS2ADesignReceiptV1` exist.
A schema, prose draft or threshold-selection procedure without the numeric threshold and producer
bytes is not a filled design slot.

### Fixture and receipt tables

- Add the BS-2a fixture transcript digest and isolated-worker digest.
- Add parent witness, evidence bundle, ledger, accepted set, excluded set, attempt manifests,
  quality design and validated partition digests to BS-2f.
- Add an explicit schema version to each receipt. A generic `successor_ref_v3/1` envelope is not
  sufficient to distinguish the new acceptance contract.

---

## 8. Choices made, with rejected alternatives

1. **Exact ID-set equality, not count equality.** Rejected: checking only 65,060 total rows or
   accepted-plus-excluded counts. Those checks permit one duplicated ID to replace one omitted ID.

2. **One row per parent with all raw predicate bits.** Rejected: separate accepted and excluded
   files with only a reason label. Split files make cross-file omission/duplication easier and do
   not preserve evidence for false-reason recomputation.

3. **Fixed reason precedence.** Rejected: requiring exactly one raw predicate to be true. A corrupt
   cutout naturally prevents downstream execution; multiple-stage failure states exist. Fixed
   precedence gives one terminal reason without pretending other evidence states cannot coexist.

4. **Strict `< QUALITY_MIN` exclusion; equality accepted.** Rejected: `<=` or prose such as “below
   threshold” with no boundary rule. The selected rule follows the literal word “below” and makes
   the floating-point boundary fixtureable.

5. **Threshold home in BS-2a.** Rejected: duplicating it in BS-3 and BS-2a. Acceptance design owns
   every parameter that changes the terminal partition. BS-3 may identify the instrument but does
   not own the partition threshold.

6. **No reuse of `abs(chi_net)` as confidence.** Rejected: renaming the current abstention
   magnitude. It directly violates the required inability to read handedness amplitude.

7. **Separate mirror-even quality channel as the repair direction.** Rejected: removing all
   confidence exclusion now. That would invalidate the accepted-sign accuracy, retention,
   calibration and power premises and leave exact-zero sign behavior unsettled.

8. **No fabricated `QUALITY_MIN`.** Rejected: copying `tau`, choosing 0.5 by convention, or picking
   a value from desired retention. The threshold requires its named synthetic calibration receipt
   and authority before it can become a constant.

9. **Three acquisition attempts, two process-failure execution attempts.** Rejected: unlimited
   retries, operator-triggered retries, and retrying low confidence/non-finite output. Unlimited or
   outcome-triggered reruns create a best-of-N selection channel. The asymmetric caps reflect that
   byte transport can be transient, while deterministic inference under frozen bytes should not be
   searched for a preferred result.

10. **First successful attempt by index.** Rejected: last success, highest quality, majority sign,
    or operator-selected receipt. Every rejected rule allows post-output choice.

11. **Quality equality is accepted.** Rejected: platform-dependent tolerance around the threshold.
    Canonical binary64 and `nextafter` fixtures make exact comparison portable under the frozen
    environment.

12. **Narrow typed receipts and a split sealed result.** Rejected: a generic execution receipt
    carrying χ plus a promise that the validator ignores it. Possession of the generic receipt is
    the capability to read signs; omission from output is not blindness.

13. **Opaque sealed-result digest without locator.** Rejected: passing a path and asking the worker
    not to open it. A path plus available decryption capability defeats construction-level
    blindness.

14. **Validator-created production type.** Rejected: a public constructor around a `validated=True`
    boolean. That merely moves the caller label into a type wrapper.

15. **All predicate and wiring fixtures are mandatory.** Rejected: testing only happy paths or only
    set digests. The original defect survives both.

16. **No manual-review exclusion.** Rejected: visual inspection or discretionary “bad image” flags.
    Those are outcome-adjacent and cannot be reconstructed from the closed evidence schema.

---

## 9. Residual risks carried by this design

1. **The quality channel does not yet exist.** This is the principal residual and an explicit
   blocker, not deferred clerical work. The design cannot be frozen or run as written until its
   producer, training/calibration constitution, numeric threshold and fixtures are gated.

2. **Mirror-even is not the same as causally independent of morphology.** A quality score can be
   invariant under mirroring and still correlate with arm strength, apparent size, redshift,
   surface brightness, observing conditions or other features that vary across the footprint.
   The construction prevents direct access to χ/sign/axis fields; it does not prove the accepted
   geometry is free of all astrophysical selection effects.

3. **A learned quality channel can hide an amplitude proxy.** The call-graph boundary prevents
   reading `abs(chi_net)`, but a model trained on related targets could reconstruct it from pixels.
   The future `QualityChannelDesignV1` therefore needs an explicit target and training-data
   constitution. This draft refuses to invent those details.

4. **Expected checksum nullability is weaker than a universal independent expected-byte witness.**
   If the canonical cutout producer itself cannot declare an expected checksum, the design records
   that failure and excludes the object. A stronger design would have a clean-room second cutout
   implementation produce an expected byte digest for every object; that is substantially more
   work and is not presently available.

5. **Independent-process custody remains an implementation obligation.** In-process module globals,
   paths and mutable constructors are nomination channels. The isolated worker and external pins
   must be implemented and gated, not merely named here.

6. **Retry caps are policy choices.** Three acquisition attempts and two execution attempts are not
   scientifically forced. They close discretion but may turn transient infrastructure failures
   into exclusions. The attempt manifests make that effect measurable after lock; changing caps
   after the first image byte remains forbidden.

7. **Excluding byte/execution failures can still alter geometry.** The design makes those exclusions
   deterministic and auditable; it does not make missingness random. BS-2f and Stage C must report
   reason counts and accepted geometry without exposing χ before lock.

8. **The current v9 mask type binds signs into its digest.** The future acceptance partition digest
   must remain sign-free, while a later sealed analysis-mask digest may bind signs. Conflating
   those two digests would recreate the §6.1 contradiction noted in the drafting brief.

9. **Canonicalization must be independently specified.** Python dataclass/JSON representations are
   not a digest specification. The implementation revision must publish byte-level field framing,
   endianness, optional encoding, ordering and schema tags, then test them under a clean-room
   implementation.

10. **This design does not repair unrelated preregistration blockers.** Stage P, custody/lock,
    branch adjudication and other open slots remain outside BS-2a. Filling BS-2a would not imply the
    full preregistration is freezeable.

---

## 10. Implementation acceptance checklist for the next drafting step

BS-2a remains unfilled unless every answer is “present and digest-pinned”:

- [ ] `QualityChannelDesignV1` exists with a non-χ target and producer.
- [ ] `quality_score_v1()` exists and has the prohibited-capability proof.
- [ ] Numeric `QUALITY_MIN` exists from the named frozen synthetic calibration.
- [ ] BS-3 no longer supplies a second operative acceptance threshold.
- [ ] All schemas in §3 exist as exact-field types with canonical serialization.
- [ ] `acceptance_worker_v1.py` exists as the isolated custody boundary.
- [ ] `derive_exclusion_predicates_v1()` and `validate_acceptance_partition_v1()` exist.
- [ ] Production no longer accepts integer completeness or caller acceptance flags.
- [ ] The full §6 fixture battery passes under pinned bytes.
- [ ] The replacement §2.7 and conforming edits receive a fresh text gate.
- [ ] The code, worker, fixtures, environment and design receipt receive a fresh code gate.
- [ ] All of the above occur before BS-6 and before the first image byte.

Until then the correct BS-2a state is **REFUSED / UNFILLED**, and the correct operational
consequence is **BS-6 BLOCKED**.
