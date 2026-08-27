# CODEX referee report — BS-2a acceptance design

## Verdict

**NOT CLEAR.** The draft correctly refuses the current `abs(chi_net) > tau` rule, makes BS-2a explicitly unfilled, gives the terminal ledger a real exact-ID partition check, and removes caller labels from the intended production interface. But its selected replacement does not establish the property the brief asks for. Mirror-evenness does not prevent a quality score from being handedness amplitude—`abs(chi_net)` is itself mirror-even—and the future producer is still allowed to consume the pixels from which handedness and its amplitude are computed. The other acceptance channels also remain authored by outcome-bearing processes and are represented to the validator chiefly as booleans and opaque digests, so their truth cannot be recomputed by the proposed acceptance path. The fixture battery then holds those authored receipts fixed, which tests downstream non-reading rather than upstream non-encoding. BS-2a must remain refused.

## Numbered findings

### 1. BLOCKING — the proposed `quality_score` can still carry handedness amplitude

**Clause / field at issue.** R5 lines 152–178; R6 lines 180–207; `quality_score` and `quality_receipt_digest` in `AcceptanceEvidenceV1`; fixtures `BS2A-MIRROR-EVEN` and `BS2A-AMPlITUDE-NOT-QUALITY`; residual risks 2–3.

**Why it fails as a promise.** The proposed construction requires bit-exact `quality_score_v1(x) == quality_score_v1(mirror(x))` and prohibits named access to `chi_net`, its sign, `abs(chi_net)`, geometry and the axis. That does not make the scalar incapable of encoding or correlating with handedness amplitude. The draft's own rejected current quantity, `abs(chi_net)`, is mirror-even. A producer that receives the same image pixels can reimplement that magnitude under different symbols or learn a proxy from morphology without calling any forbidden symbol. Lines 814–817 expressly concede this and leave the target and training-data constitution undefined. Thus the selected repair direction repeats the field-name defect at the semantic level: it bans names and direct inputs, not information derivable from pixels.

**Smallest sufficient repair.** Under the current no-amplitude/no-correlation promise, remove confidence-based exclusion and redo calibration/power for all finite outputs. If a quality exclusion is scientifically indispensable, revise the promise openly before images: constrain the score to a fully specified upstream technical witness that is frozen before inference and cannot consume image content or any descendant of the handedness model; pin its complete producer, inputs, target/training constitution (if any), and threshold derivation; and state the narrower property actually established. A pixel-derived score may be mirror-even and non-sign-reading, but it cannot be promised incapable of correlation merely by construction.

### 2. BLOCKING — `output_present`, `output_finite`, execution state and attempt selection are labels the validator cannot independently recompute

**Clause / field at issue.** R2 lines 63–77; R4 lines 103–135; R6 lines 184–204; `execution_state`, `output_present`, `output_finite`, `selected_attempt_index`, `execution_receipt_digest`, and attempt-manifest digests in `AcceptanceEvidenceV1`; `P_EXEC` lines 493–501.

**Why it fails as a promise.** These fields are emitted by the pinned BS-9 instrument runner—the same outcome-bearing process that computes the sealed handedness result. The acceptance validator is prohibited from resolving that result and receives only claimed state/boolean fields plus opaque digests. It can check serialization, joins and digest consistency, but it cannot recompute whether an output was actually present or finite from those inputs. A self-consistent instrument receipt can therefore set `output_finite = False`, omit the execution receipt, or select an attempt as a function of a sign it has already seen; the downstream validator will faithfully recompute `P_EXEC` from the encoded label. An independently enumerated manifest proves which records exist, not that the outcome-bearing producer truthfully chose which records to emit or how it set their state.

**Smallest sufficient repair.** Name and pin an atomic instrument transaction that, before any result is exposed, deterministically emits (a) the sealed handedness payload and (b) a non-editable acceptance attestation derived by exact frozen code; bind both to one parent ID, cutout digest, attempt index and transaction ID. Give the acceptance validator a separately authenticated proof or attestation it can verify without trusting caller-authored booleans, and make the independent attempt enumerator close over every launched transaction. If no mechanism can prove the finite/present state while withholding the payload, refuse `INSTRUMENT_OUTPUT_ABSENT_OR_NONFINITE` as a claimed recomputable predicate rather than calling the booleans evidence.

### 3. BLOCKING — the cutout predicates retain writable post-image nomination channels

**Clause / field at issue.** R2 producers lines 63–74; replacement §2.7 items 2–3; `expected_cutout_sha256`, `actual_cutout_sha256`, verifier receipt and attempt-manifest fields; nullability rule lines 370–382; residual risk 4.

**Why it fails as a promise.** `P_BYTE` excludes when either checksum is null, while the expected declaration may itself be null after producer failure. The draft does not require the expected declaration and actual-byte verification manifests to be complete, immutable and sealed before instrument inference, and it places no outcome-capability boundary around the BS-9 cutout producer or `verify_cutout_bytes_v1()`. Consequently a producer that can see or later learn the result can selectively withhold an expected checksum, withhold an actual verification, or emit a mismatching witness. The resulting exclusion is a deterministic function of the evidence row, but the evidence row is still a nomination channel. Calling the verifier a separate process does not establish that it ran before inference or lacked access to result stores. Residual risk 4 acknowledges the missing universal expected-byte witness but treats it as optional strengthening even though null expectation directly changes the partition.

**Smallest sufficient repair.** Before the instrument can run, require one complete, exact-parent cutout manifest containing the expected and independently recomputed actual byte witnesses, attempt closure, canonical shape/dtype/byte count and an immutable stage-completion receipt. Pin a named verifier that reads the stored bytes and the externally fixed parent, prove it has no instrument/result capability, and make BS-9 inference refuse to start until that receipt is sealed. An absent expected declaration must fail the pre-inference acquisition stage for the whole run or arise under a separately frozen, mechanically exhaustive rule; it must not remain a per-object field an outcome-bearing process can author later.

### 4. HIGH — “at most” retry caps leave the stopping decision discretionary

**Clause / field at issue.** Replacement §2.7 item 5 lines 266–272; attempt-count fields and nullability rules; retry fixtures lines 607–616; choices 9–10.

**Why it fails as a promise.** The text says acquisition and execution “permit” at most three and two attempts. It fixes the maximum and first-success selection but does not require the next eligible retry. An operator can stop acquisition after one missing/checksum-failing attempt rather than run attempts 1 and 2, or stop execution after attempt 0 has no completed receipt rather than run attempt 1. `cutout_attempt_count` explicitly allows 1–3, and no listed fixture refuses premature exhaustion. This moves acceptance while respecting the cap, the manifest, and first-success ordering. It is especially dangerous because the draft allows expected-checksum nullability only “after all three attempts” in prose but supplies no transition invariant that enforces all three.

**Smallest sufficient repair.** Freeze a total retry state machine: after each retry-eligible failure the next index is mandatory until success or the exact cap, and early manifest termination refuses the run rather than excluding the object. Add `CUTOUT-PREMATURE-STOP` and `EXEC-PREMATURE-STOP` fixtures, and require the independent enumerator to prove contiguous indices and terminal-state legality. Launch/retry decisions must occur before any sealed handedness result can be resolved.

### 5. HIGH — the actual parent witness is asserted external but is not pinned by the design contract

**Clause / field at issue.** R1 lines 41–54; `ParentIdWitnessV1`; validator signature; `BS2ADesignReceiptV1` lines 440–463; digest-custody item 8.

**Why it fails as a promise.** The validator accepts a `parent` argument, and the prose repeatedly invokes an “independently pinned parent witness.” But `BS2ADesignReceiptV1` contains only `parent_schema_digest`; it contains neither the actual parent witness digest nor `objids_digest`, parent producer receipt digest, or a named external slot/loader identity. A caller can therefore present a structurally valid 65,060-ID witness and a self-consistent evidence/ledger chain unless some unstated external mechanism supplies the missing value pin. Set equality is real only relative to the parent set actually loaded; the exact data contract does not bind which set that must be.

**Smallest sufficient repair.** Add the exact `ParentIdWitnessV1` artifact digest, its `objids_digest`, producer receipt digest and named externally pinned slot/loader to the design receipt (or identify an already frozen artifact and pin its exact digest by reference). The production validator must load that witness itself and refuse a caller-supplied substitute before validating rows.

### 6. HIGH — the blindness fixtures hold the suspect evidence fixed and therefore cannot detect upstream encoding

**Clause / field at issue.** `BS2A-FORBIDDEN-CALL-GRAPH`, `BS2A-MIRROR-EVEN`, `BS2A-SIGN-SWAP-INVARIANT`, `BS2A-AXIS-PERMUTATION-INVARIANT`, and `BS2A-AMPlITUDE-NOT-QUALITY`, lines 632–650.

**Why it fails as a promise.** The sign-swap fixture changes sealed χ “under an unchanged acceptance receipt”; the axis fixture changes geometry “while holding permitted evidence fixed”; and the amplitude fixture changes `abs(chi_net)` “while holding the quality receipt fixed.” Those tests assume the property under review. They show only that the downstream predicate code does not open the sealed payload after the projection has already been authored. They do not rerun the projection, instrument-state producer, cutout verifier or quality producer and therefore cannot reveal sign encoded in confidence, execution state, attempt identity, missingness or a digest choice. The call-graph blacklist is likewise syntactic: aliases, an equivalent computation, a model proxy, dynamic import, subprocess or permitted pixel access can carry the same information without a forbidden symbol.

**Smallest sufficient repair.** Make every invariance fixture end-to-end: regenerate the acceptance receipt and ledger through the exact pinned production producers after each controlled sign/amplitude/axis perturbation, then compare every byte. Exercise the real isolated worker under an allowlist sandbox for imports, filesystem, network and process capabilities; inspect semantic data flow, not only names in reachable globals. Include adversarial producers that encode the synthetic sign through every writable field and require the verifier to reject each one. These fixtures still cannot prove absence of statistical correlation for a pixel-derived score; that limitation must be resolved as finding 1 states.

### 7. MEDIUM — the byte-integrity contract carries `actual_byte_count` but never uses it

**Clause / field at issue.** `actual_byte_count` and its nullability in `AcceptanceEvidenceV1`; `P_BYTE` / `P_SHAPE` lines 242–253 and 479–491; shape fixtures lines 588–603.

**Why it fails as a promise.** A present `actual_byte_count` is constrained only to be non-negative. Neither `P_BYTE` nor `P_SHAPE` checks that it equals the canonical byte length implied by `(1, 128, 128)` and `<f4`, and no listed fixture supplies a correct claimed shape/dtype with an inconsistent byte count. The evidence digest can therefore authenticate an internally contradictory row that is accepted. More generally, the predicate hard-codes shape/dtype but does not state the exact consistency relation between parsed tensor, serialized bytes, checksum and byte count.

**Smallest sufficient repair.** Define one canonical cutout byte representation and require the verifier to recompute checksum, parsed shape, dtype and exact byte count from those same bytes. Add the exact byte-length equality to the predicate or schema invariant, make its failure map deterministically to the closed byte/shape reason, and add inconsistent-count and parser/serialization disagreement fixtures.

## Checks that held

1. The draft honestly refuses the current `abs(chi_net)` confidence rule and does not fabricate `QUALITY_MIN`.
2. The ledger design checks exact parent-ID set equality, uniqueness and one terminal row rather than relying on accepted-plus-excluded counts alone.
3. The validator is intended to recompute predicate bits, status and reason and to raise `AcceptanceContractError` on any supplied-ledger disagreement; there is no warning or production repair mode.
4. The reason list is closed, precedence is deterministic, all raw reachable predicate bits are retained, and manual/visual/scientific-interest exclusions are expressly forbidden.
5. The intended production signature consumes a validator-created partition rather than caller acceptance flags or `n_receipts, n_parent` count testimony.
6. The threshold has one proposed operative home in BS-2a, with the historical `tau` required to become non-operative elsewhere. The draft correctly leaves BS-2a unfilled until one numeric threshold and its producer/calibration bytes exist.

## Testimony

I reviewed `BRIEF_BS2A_REVIEW.md`, all 871 lines of `BS2A_DESIGN_DRAFT_GPT.md`, current V15 §2.7, the prior CODEX §6 R4 finding that motivated this pass, and the relevant symbol/signature surface of frozen `successor_ref_v9.py`. I did not inspect any image, cutout byte, χ value, sealed payload, attempt manifest, parent witness value artifact, credential, key, or `/Users/duhokim/NebulaMindData/`. I did not establish that any proposed future schema, producer, worker, sandbox, receipt, attestation, fixture or quality model exists or behaves as described; the subject labels them future work and BS-2a unfilled. I made no claim about realized partition counts beyond the fixed 65,060 parent count stated in the supplied artifacts. I modified only this report.

**NOT CLEAR**
