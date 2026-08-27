# BS-2a REFEREE REPORT — KIMI seat

Subject: `BS2A_DESIGN_DRAFT_GPT.md` (871 lines). Brief: `BRIEF_BS2A_REVIEW.md`.

## Verdict

The draft's central move is correct and I verified it against the frozen record: the only
quantity presently available to play "confidence" is `abs(chi_net)`, thresholded by τ —
`YUI_PRODUCTION_ESTIMATOR_APPENDIX_20260812.md` line 82 freezes "Accept object x iff
**|χ_net(x)| > τ**" — and that quantity is handedness amplitude, so the current reason (d)
cannot satisfy V15 §2.7(3) no matter what it is renamed. REFUSE-with-named-prerequisites is
the only non-fabricating answer there, and the draft gives it. The partition, recompute
contract, production wiring and fixture battery are the right shape.

But the brief's hazard — nominal repairs that rename rather than bind — is present in the
draft's own evidence schema. The predicates are recomputed; the *evidence atoms* for the
execution reason (`execution_state`, `output_present`, `output_finite`, the attempt record)
are authored by the same outcome-bearing instrument process whose behaviour they describe,
and no independent producer, in-boundary mechanical deriver, or post-unblinding audit binds
their truth. The mark-it-EXCLUDED attack the slot exists to kill survives one level down,
through exactly two booleans and an attempt manifest whose "independence" is asserted, never
constructed. The draft also never addresses the R4 finding it was written under — that the
cutout checksums its evidence carries are, under the companion §6 scope, χ-bearing
verification oracles — and its quality-channel boundary bans named symbols while leaving the
producer's input signature undefined, through which χ is one subtraction away. **NOT CLEAR.**

## Numbered findings

### 1. BLOCKING — the execution-evidence atoms are outcome-process labels, and nothing in the design binds their truth

**Clause / field at issue.** `AcceptanceEvidenceV1` fields `execution_state`,
`output_present`, `output_finite`, `selected_attempt_index`, `execution_receipt_digest`,
`instrument_attempt_manifest_digest` (§3.3, lines 353–361); the R2 producer list, which
assigns "attempt and execution records" to "the pinned BS-9 instrument runner" (lines
67–68); §2.7 replacement items 4–6 (lines 259–278); R4's recompute contract (lines 97–135);
fixtures `BS2A-ATTEMPT-JOIN` and `BS2A-NONFINITE` (lines 594–597).

**Why it fails as a promise.** `validate_acceptance_partition_v1()` recomputes every
predicate *from* these atoms. It cannot recompute the atoms: the split-receipt barrier
(R6.2) rightly forbids the acceptance worker to open `SealedHandednessReceiptV1`, so no
party on the acceptance path ever compares the flags against the sealed output bytes before
the lock. The atoms' truth therefore rests entirely on their author — the same instrument
process that computes χ. A conforming runtime can run inference, see the sign, write
`output_finite=false` (or `execution_state=NO_COMPLETED_RECEIPT`) for an unwanted object and
`COMPLETED`/finite for a wanted one, enumerate a self-consistent attempt manifest, and pass
the recompute, the manifest join, and every digest. That is the CODEX-V11 3 / GPT56-V11 F3
hole — mark `EXCLUDED / instrument output non-finite` instead of `EXCLUDED / low
confidence` — relocated one level down into the evidence the recompute trusts. The design
knows the right pattern and applies it to bytes: `verify_cutout_bytes_v1()` runs "in an
independent verification process" (R2, line 66). For execution it uses the words
"independently enumerated attempt manifest" (§2.7(5), §3.3) but names the runner as the
record's producer and never constructs the independence. Fixture `BS2A-ATTEMPT-JOIN` tests
claim-versus-manifest consistency; no fixture tests flag-versus-reality, and under the
current construction none can — the fixture battery *exercises* P_EXEC, it does not
demonstrate that a false `output_finite` is refused.

**Smallest sufficient repair.** (i) Name and pin an execution supervisor independent of the
inference process: it observes process exit and receipt-file existence, and computes
presence/finiteness as a mechanical function of the sealed output bytes inside the sealed
boundary; make that supervisor the producer of the attempt manifest and the execution-state
atoms, and pin its digest in `BS2ADesignReceiptV1`. (ii) Schedule a mandatory
post-unblinding audit recomputing every object's flags from the sealed outputs against the
acceptance receipts, with any mismatch voiding the verdict, named in the replacement §2.7.
(iii) Add producer-side fixtures: a false `output_finite` written over finite sealed bytes,
a failure attempt omitted from the manifest, and a manufactured process death followed by
retry — each must refuse at (i) or be caught at (ii).

### 2. MAJOR — the evidence schema carries cutout digests that the companion §6 scope classifies as χ-bearing oracles, and the draft is silent

**Clause / field at issue.** `expected_cutout_sha256`, `actual_cutout_sha256` (§3.3, lines
341, 347) and, transitively, the per-row `evidence_digest` and the R6.2 optional
sealed-receipt digest (lines 191–193); R6 barrier 1 (line 186); §2.7 replacement item 7
(lines 280–285); `SECTION6_DRAFT_AGY_R4.md` scope lines 29 and 50–56 and row E; GPT56-R4
finding 1.

**Why it fails as a promise.** The R4 scope — the text this lane is converging on for the
blinding covenant — defines every cutout as χ-bearing and "any opaque digest of χ-bearing
bytes" as χ-bearing, because it is a verification oracle for a guessed outcome. The
acceptance worker reading `actual_cutout_sha256` therefore reads a χ-bearing object under
that scope, and the per-object evidence bundle, if exported as the non-χ artifact the
design's own typing makes it, exports digests of χ-bearing bytes. The draft's R6.1 barrier
("no handedness, χ, sign, amplitude … field") is a field-name property — precisely the move
both R4 referees rejected when they found the acceptance projection not blind by
construction, and the review brief says that finding "lands directly on this draft."
Substantively the checksums are safe *as a decision*: they enter only through equality, the
expected value is declared before inference, and the sign-swap fixture's invariance is
unaffected. What fails is the draft's unexamined assertion of §6 compatibility and the
export/read authorization of the bundle. I also note the attack that makes this more than
classification hygiene: the predecessor archive holds outcome knowledge on overlapping sky,
and an operator guided by it could corrupt cutout *transport* selectively to manufacture
P_BYTE exclusions; the attempt manifest and the three-attempt cap bound this and make it
visible, which is the right posture, but it belongs in the residual list alongside the
oracle question.

**Smallest sufficient repair.** Choose one construction and state it: (a) the in-store byte
verifier compares expected/actual bytes and exports only the pass/fail bits P_BYTE consumes
(GPT56-R4's repair), with both digests remaining in the sealed store; or (b) amend the §6
scope to carve out pinned-producer cutout commitments from the digest-oracle rule, gated
alongside BS-2a. Extend `BS2A-FORBIDDEN-FIELDS` to prove whichever construction is chosen,
and name the transport-corruption channel in §9 with its binding (manifest + cap +
BS-2f reason counts).

### 3. MAJOR — the quality-channel boundary forbids named symbols, not the information that reconstructs χ

**Clause / field at issue.** The R5 prerequisite contract (lines 152–164), especially the
capability boundary at lines 157–158; R6 barrier 4 and `BS2A-FORBIDDEN-CALL-GRAPH` (lines
197–200, 635–637); the absent input signature of `quality_score_v1()`.

**Why it fails as a promise.** The boundary bans the producer from calling or receiving
`chi_net`, the sign, `abs(chi_net)`, RA, Dec, `c = cos(theta)`, and `AXIS`. It never names
what the producer *does* receive. A conforming `quality_score_v1()` handed the instrument's
two activations `f(x)` and `f(mirror(x))` — neither a forbidden symbol — recovers `2χ` by
one subtraction and `|χ|` by one `abs`, passes every named call-graph ban, and reintroduces
amplitude thresholding as "quality." Mirror-even bit-exactness does not block this: `|χ|` is
itself mirror-even, so an amplitude proxy satisfies the identity `q(x) == q(mirror(x))`
exactly. This is the brief's named defect in symbol-versus-information form: the contract
enumerates forbidden field names without constraining what inputs may flow to the producer.
The draft's own residual 3 (a learned channel can reconstruct amplitude from pixels)
concedes the general case; the prerequisite contract must make the specific case a gate,
not a risk.

**Smallest sufficient repair.** Pin the exact input signature of `quality_score_v1()` —
cutout bytes and pinned quality constants only, with no instrument-process output of any
kind — and require a data-flow proof (reachable inputs, not reachable symbol names) that
nothing it receives derives from the χ path. Add producer-side fixtures: a producer
implemented over the two activations must fail the capability gate; and an
amplitude-reconstruction test showing the frozen producer's score cannot beat a pinned null
baseline at predicting `|χ|` on the synthetic manifest, or the channel is refused. State in
R5 that mirror-evenness is necessary but not sufficient, so the filler of
`QualityChannelDesignV1` is held to the information boundary.

### 4. MINOR — production custody: two validator names, and the partition's external pin reference is never stated

**Clause / field at issue.** R4 names `validate_acceptance_partition_v1()` and says
production must call it (lines 46–47, 101–111); §5 step 3 has production call
`require_validated_partition_v1()`, which "reloads the pinned BS-2a design receipt and
verifies the validated-partition digest" (lines 553–554); §2.7 item 8 (lines 287–291);
fixture `BS2A-CALLER-TRUST` (lines 656–657).

**Why it fails as a promise.** Two different symbols are named for the production-side
check, and neither sentence says what the validated-partition digest is verified *against*.
The design never states that production loads the BS-2s/BS-2f receipts and refuses unless
`parent_digest`, `evidence_bundle_digest`, `ledger_digest` and the validated-partition
digest equal the pinned witnesses. As written, the real validator run over caller-fabricated
evidence under the real (matching) design mints a genuine `ValidatedAcceptancePartitionV1`
that satisfies every stated check; only the downstream BS-5f mask-digest requirement binds
anything, and it binds only the accepted ID set — not the reasons, not the evidence. That
binding is probably sufficient for verdict integrity, but the draft should say it is the
mechanism, not leave it to be discovered.

**Smallest sufficient repair.** Use one symbol name; state explicitly that production loads
the pinned BS-2s/BS-2f witnesses and requires digest equality for parent, evidence bundle,
ledger and validated partition; name the BS-5f mask-digest check as the verdict-path binding
for the accepted set; add the fixture: real design + fabricated evidence + mismatched BS-2f
pin refuses.

### 5. MINOR — the retry-veto channel is bounded, but its closure rests on unpinned determinism

**Clause / field at issue.** §2.7 replacement item 5 (lines 266–272); §8 item 9 (lines
770–774); residual 6 (lines 829–832).

**Why it fails as a promise.** Two execution attempts for "process-level absence of a
completed execution receipt" admit a selective one-veto channel — kill attempt 0 after its
output exists, keep attempt 1 — which is worthless only if repeated inference on identical
bytes is bit-identical. The draft assumes determinism ("deterministic inference under frozen
bytes should not be searched") but pins no determinism receipt. The frozen record supplies
one: I-4 requires bit-exact `χ(mirror(x)) = −χ(x)` over a 1,000-probe grid
(`PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md` lines 247–251), which is unattainable
under nondeterministic execution. The channel is therefore closed in the frozen instrument,
but the draft neither cites that closure nor makes the attempt manifest's producer
independent of the process it records (finding 1).

**Smallest sufficient repair.** Cite I-4 (and its successor-side identity receipt) as the
determinism pin in §2.7 item 5 or §8 item 9; add a BS-9-side repeated-inference
bit-identity receipt to the BS-2a prerequisite list; with finding 1's supervisor,
"process-level absence" becomes attested rather than asserted.

### 6. NIT — contract elisions and an unexplained binding fixture name

**Clause / field at issue.** The production signature line 543 (`authorization:
Pinned...nV1`); `canonically_digest_derived_row(...)` (line 524); fixture name
`BS2A-AMPlITUDE-NOT-QUALITY` (line 648), whose capitalization the draft says is "preserved"
without naming the source it is preserved from.

**Why it fails as a promise.** The drafting brief requires a contract implementable
"without further decisions"; a literal ellipsis in the production signature and a battery
whose names are declared binding ("All fixture names and expected outcomes are binding,"
line 573) but whose irregular capitalization has no stated provenance invite divergent
implementations that then disagree on the pin.

**Smallest sufficient repair.** Fill the signature; state the fixture name's provenance or
correct it before the names freeze.

## The brief's seven questions, answered

1. **Is the partition real?** As designed, yes: set equality against the independently
   pinned BS-2s parent witness, exactly one row per ID, duplicates/extras/omissions/wrong
   count all refused, and count-equality explicitly insufficient with a fixture
   (`BS2A-COUNTS-NOT-SETS`) that demonstrates the distinction. Verifiable rather than
   asserted — once finding 4's external pin reference is stated.
2. **Is every predicate a function of evidence alone?** The predicates, yes; the evidence
   atoms for reason (c), no — finding 1. Production refuses a status that disagrees with
   *evidence* via full recompute and `AcceptanceContractError` with a non-χ error
   representation; what it cannot refuse today is evidence that disagrees with *reality*.
3. **Is the confidence quantity defined, and incapable of carrying an outcome?** It is not
   defined, and the draft is right to refuse to define it: the only frozen candidate,
   `abs(chi_net) > τ`, *is* handedness amplitude (verified at YUI appendix line 82 and the
   frozen I-1/I-4 text), so renaming it would reproduce the defect in new vocabulary —
   exactly as the draft says. The placeholder contract (mirror-even bit-exact + capability
   boundary + [0,1] + synthetic calibration) blocks naive encoding but, as drafted, not
   activation-level reconstruction (finding 3); correlation through pixels and morphology
   is admitted in §9 and cannot be closed by construction, only bounded by the calibration
   constitution that does not yet exist. This is the correct posture and the correct
   consequence: BS-2a unfilled, BS-6 blocked.
4. **Does the threshold have exactly one home?** In the replacement text, yes: `QUALITY_MIN`
   lives only in the BS-2a design receipt; BS-3 becomes historical; two-home operation is
   explicitly refused. Verified the defect it repairs: V15 §2.7(2)(d) and §2.7(7) pin the
   threshold in BS-3 while §7's BS-2a row claims it, and v9 `SLOT_SCHEMA["BS-3"]` still
   carries `tau` operatively. One nit: the conforming edits never name the code consequence
   (annotate or guard `SLOT_SCHEMA["BS-3"]` so no acceptance path can read `BS-3.tau`).
5. **Is the closed list right?** Yes, once finding 1 is repaired: the three mechanical
   reasons plus a refused fourth are the right shape; no admissible reason can see
   handedness; and I found no omitted reason that must exist — quality-producer failure and
   schema violations fail closed at run level rather than becoming reasons, which is
   correct. The rejection of "remove confidence exclusion entirely" is sound: it would
   leave the frozen signed-zero behaviour unsettled and discard the retention/calibration
   premises (§8.7).
6. **Would the fixtures demonstrate any of this?** The consumer-side invariance fixtures
   (`BS2A-SIGN-SWAP-INVARIANT`, `BS2A-AXIS-PERMUTATION-INVARIANT`,
   `BS2A-AMPlITUDE-NOT-QUALITY`) genuinely demonstrate that the acceptance path's outputs do
   not depend on sealed χ — under frozen receipts. They cannot demonstrate producer-side
   truth: a receipt whose author encoded outcome into the flags or the quality score passes
   all three. The battery needs the producer-side fixtures named in findings 1 and 3 before
   it demonstrates, rather than exercises, the blindness claim.
7. **What does it leave to be decided after images exist?** Nothing decisional, and the
   draft enforces that on itself: the §10 checklist holds BS-2a unfilled until
   `QualityChannelDesignV1`, numeric `QUALITY_MIN`, schemas, worker, fixtures and both gates
   exist, all before BS-6 and the first image byte. BS-2f is values, not decisions. This is
   the draft's strongest discipline and it is stated, not implied.

## Checks that held (positive evidence)

1. **The central refusal is verified, not asserted.** YUI appendix line 82 freezes
   acceptance as `|χ_net(x)| > τ` on values; the frozen prereg's I-1 pins τ =
   4.4006456017494235 in BS-3 and I-4 pins the antisymmetry identity. V15 §2.7(3) requires
   exclusion predicates unable to read amplitude. Reason (d) as presently instantiated is
   self-contradictory; the draft's refusal is the only honest disposition.
2. **The v9 gap claims are accurate.** `run_production_verdict()` takes `n_receipts,
   n_parent` (`successor_ref_v9.py:1591–1592`); `require_complete_sample()` compares two
   integers (1647–1649); `SealedMask` accepts caller-supplied `accept` flags checked only
   for 0/1 membership (1033–1040) and binds the sign vector into its digest (1056–1063) —
   confirming residual risk 8's sign-binding claim and the need for a sign-free partition
   digest distinct from the analysis-mask digest.
3. **The threshold's two homes are confirmed in the current text** (V15 lines 309, 344–345
   versus line 606; BS-3 row line 613; v9 line 198), and the draft's single-home move plus
   refusal of operative dual residence closes it.
4. **The tensor contract matches the frozen input contract**: (1, 128, 128) float32
   little-endian C-order (`PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md` lines
   368–369) equals §3.3's `Shape3`/`"<f4"`.
5. **Internal consistency of the predicate machinery**: nullability rules make
   checksum-present imply shape/dtype present; the short-circuit guards fail closed
   (`None != (1, 128, 128)` excludes rather than passing); §2.7 item 4's precedence matches
   §4's code; `reason == "NONE"` iff `ACCEPTED`; attempt-count ranges match the retry caps
   (1..3 acquisition, 0..2 execution); the boundary rule (`< QUALITY_MIN` excludes,
   equality accepts) plus canonical binary64 and `nextafter` fixtures makes the comparison
   portable rather than tolerance-dependent.
6. **The rejected alternatives are reasoned, not rhetorical** (§8): set-over-count,
   one-row-per-parent with all predicate bits, fixed precedence, strict `<`, no fabricated
   `QUALITY_MIN`, no reuse of `abs(chi_net)`, opaque digest without locator,
   validator-minted production type — each names the attack it refuses.

## Mechanical and evidence checks

- Read: the review brief; `BS2A_DESIGN_DRAFT_GPT.md` in full; the drafting brief
  `BRIEF_DRAFT_BS2A.md`; V15 §2.7, §6.1 and the §7 slot table; `PREREG_TEXT_V11_CODEX.md`
  finding 3 and `PREREG_TEXT_V11_GPT56.md` F3 in full; both R4 referee reports and the R4
  draft's scope/table; `successor_ref_v9.py` (production verdict, sample guard, mask
  construction/digest, SLOT_SCHEMA); the frozen prereg instrument section and the YUI
  estimator appendix's acceptance-threshold section.
- Recomputed: no arithmetic of mine is load-bearing; all numeric claims above are quoted
  from the cited files (65,060; τ = 4.4006456017494235; (1, 128, 128); 1..3 / 0..2 attempt
  ranges).
- Independence note: while grepping for the provenance of the fixture name
  `BS2A-AMPlITUDE-NOT-QUALITY`, the search returned a handful of lines from the two sibling
  referee reports (`BS2A_REVIEW_GPT56.md`, `BS2A_REVIEW_CODEX.md`). I did not open or read
  either report; findings 1–6 above were drafted from the primary sources before that
  glimpse, and any convergence with a sibling is independent.

## Testimony

Not independently verified: the existence, behaviour or eventual inputs of any
`quality_score_v1()` or `QualityChannelDesignV1`; any calibration manifest, objective or
held-out receipt; the independence of any real attempt manifest or execution supervisor
(none exists to inspect); the current status of the successor-side I-4 identity receipt;
whether the §6 R4 scope will be amended, replaced or frozen as written; the provenance of
the fixture-name capitalization; BS-9 runner internals beyond the v9 SLOT_SCHEMA entry;
whether `require_validated_partition_v1` and `validate_acceptance_partition_v1` are intended
as one symbol. I did not inspect any image, cutout, χ value, sealed-store payload,
predecessor-archive content, key, credential, access log, or `/Users/duhokim/NebulaMindData/`,
and I ran no code against the frozen reference beyond reading it.

**NOT CLEAR**
