# A1 open questions — bounded author/researcher answers, 2026-09-07

Research and recommendations only. This document approves, adopts, signs off, or authorizes nothing. The independent review was neither opened nor changed. A1 itself was read and remains unchanged. References below are to original documents or implementation source actually opened, not the V15 clause-disposition extract. Relative paths resolve under the lane root:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_stage2_image_analysis_20260901`.

The questions are A1 lines 66–73. “Resolved” in this filename includes an explicit decision requirement or an uncomputable result, not a claim that all prerequisites are complete. Documentary pins are distinguished from newly computed file digests. No evaluation CSV, label, pixel, tensor, per-object outcome, journal/log, sandbox, git, or file under `_optionA_dev/` was opened; the required PYTHONPATH was set, but no package from it was imported.

## 1. Renderable population within the post-exclusion 7,410

**ANSWER — UNCOMPUTABLE within this task's access boundary.** 7,410 is the pre-renderability remainder, not an established renderable count. A numerical renderable count requires the actual post-exclusion identities with catalogue coordinates (or a provenance-bound brick assignment), the pinned survey-bricks table and no-r registry, and membership checks against both exclusion sets. The discovered guarded pool is `_optionA_dev/corpus_identity/guarded_pool.csv`, in the prohibited tree; the failed CSV includes human labels. Neither was opened. No eligible-ID artifact was identified by the filename search. This is missing admissible input for this computation, not a claim that the count cannot be computed elsewhere.

**EVIDENCE.** Original `OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V15_20260906.md` §1 lines 10–12 defines the failed set and catalogue-only renderability; E3(i), line 21, states the guarded pool and dry-run controls; §3b line 36 excludes the failed set and all 2,644 dry-run identities. A1 lines 28–30 explicitly distinguishes “exactly 7,410 before renderability” from the eligible subset. `AGREEMENT_RUN_INPUT_CONTRACT_20260907.md` lines 8–9 requires a derived eligible-ID file; lines 17–20 identifies the exclusion format and the CSV's label-bearing columns. Original resolver `miniprereg_pins/validation_resolver.py` lines 32–47 verifies the table digest and uses binary64 half-open coordinate bounds with exactly one hit. Computation C1 below outputs `post_exclusion_arithmetic = 7410`; this checks arithmetic only, not the source-file counts or disjointness. No renderable count was computed. Missing: a permitted label-free population/coordinate input and the pinned exclusion/derivation evidence, or an authorized catalogue-only production receipt plus its eligible-ID file.

**CONSEQUENCE FOR A1:** Keep lines 28–30 and the eligible-file placeholders unresolved until the lane owner supplies a catalogue-only derivation, numerical renderable count, exact filename and digest before C; do not substitute 7,410 as the eligible count.

## 2. Full failed-set and validation-gate pins

**ANSWER.** The original incorporated Tier-C V35 text supplies both complete pins:

- Failed selection CSV: `5643555c75670a695cd9144455a956440125c1019ebd1fb028a7ee21889014c7`.
- `miniprereg_pins/validation_gate.py`: `65e241cad76b6150f625ac5aad085ed528004153d8590f8c32b07895c0c75e5b`.

The first is a directly transcribed documentary pin, **not** a fresh hash of the current CSV. Current-byte verification of that label-bearing CSV is UNCOMPUTABLE under the no-evaluation-data restriction. The second was recomputed from code and matches. Neither pin is the digest of the still-to-be-produced failed-ID text file.

**EVIDENCE.** Original selection-rule V15 §1 line 10 names `VALIDATION_SELECTION_V29_20260905.csv` and abbreviates its hash; §5 line 45 abbreviates the gate hash. Original `MINI_PREREG_GZ_TIERC_DRAFT_V35_20260905.md` line 474, “Pinned artefacts of this clause,” gives the complete CSV pin; §9B.7a line 508 gives the complete gate pin and filename. C1 below gives the exact command and matching current gate hash. `AGREEMENT_RUN_INPUT_CONTRACT_20260907.md` lines 18–20 requires separate CSV and derived-ID-file digests.

**CONSEQUENCE FOR A1:** Replace line 16's abbreviated-source placeholder with the documented full CSV pin (mark current-byte verification pending), name and pin `miniprereg_pins/validation_gate.py` separately at line 25, and retain a distinct unresolved pin for the derived failed-ID file.

## 3. V15's incorporated validation denominator and calculation

**ANSWER.** Validation uses the **scored denominator m**, not the fixed drawn n: n = 2,000; r counts refusals; m = 2,000 − r; k counts machine-sign/GZ1-label matches among those m; p_raw = k/m; p_val = max(p_raw, 1 − p_raw). First fail if m < 1,900. Otherwise set K = int(round(p_val × m)) and compute the two-sided 95% Wilson lower endpoint at (K,m), z = 1.959963984540054:
`[p + z²/(2m) − z sqrt(p(1−p)/m + z²/(4m²))] / [1 + z²/m]`,
where p = K/m. PASS requires the endpoint strictly greater than 0.70. Algebraically the orientation numerator is max(k,m−k); the executed floating-point route is the p_val/round route just stated.

This differs deliberately from V15's tuning objective max(k,m−k)/400 and holdout max(k,m−k)/200. Carrying the fixed denominator 2,000 into validation would change the inherited statistic. The gate function itself accepts an n argument without enforcing n == 2,000; A1's caller must enforce the prescribed population and cannot treat the helper as a complete input validator. The gate's r interface does not classify failure causes or validate individual scores; the adapter must do that without counting a sentinel as a sign.

**EVIDENCE.** Original selection-rule V15 §5 line 45 incorporates the gate; §7 lines 53–55 states the development/holdout rules. Original Tier-C V35 §§9B.6–9B.7a, lines 496–508, supplies the definitions, refusal rule, floor and formula. Original `miniprereg_pins/validation_gate.py` lines 34–37 pins constants; lines 45–53 implements Wilson; lines 56–78 implements the exact input checks, floor, denominator, p_val, rounding and strict comparison. C1 recomputes its identity. No evaluation result or synthetic numerical example was needed or computed here.

**CONSEQUENCE FOR A1:** Replace the validation question in line 38 with the explicit scored-denominator formula and exact gate call above, preserving its distinction from the fixed tuning/holdout denominators and requiring caller enforcement of n = 2,000.

## 4. Does the later drand-only direction require chain-bound BLS?

**ANSWER.** Yes: actual signature verification and pinned chain identity are part of the recorded direction, so two-host agreement alone is insufficient. The direction requires the cryptographic property; it does not, by itself, approve an exact verifier filename/version or the historical exhibit as production code.

**EVIDENCE.** The original decision record was opened at the absolute path `/Users/duhokim/NebulaMind/NebulaMind/.hermes/CODEX_DUHO_DRAND_ONLY_DECISION_20260906.md`: lines 12–16 say to preserve “actual signature verification and pinned chain identity,” exclude observed exhibit rounds, and distinguish direction from final-version approval. The lane copy was also opened, but is not used in place of the original. Original relay `_tmp_relay_duho_drand_only.txt` lines 23–31 says “ACTUAL signature verification, pinned chain identity” and “the BLS signature must be verified, and the response bound to CHAIN_HASH.” In contrast, original V15 §3b line 38 says “The drand BLS proof is NOT verified” and authenticates through “≥ 2 of 4 pinned relay HOSTNAMES agreeing.” This is a substantive authentication difference between the inherited rule and the later direction, not evidence that the later direction preserves hostname-only authentication.

Original `PROPOSAL_DRAND_ONLY_SAMPLING_20260906.md` §§2–3, lines 13–17, specifies chain-qualified URLs; the pinned key, scheme and DST; verification over SHA-256(previous_signature || eight-byte big-endian round); and randomness = SHA-256(signature). Original exhibit `DRAND_ONLY_EXHIBIT_20260906.md` lines 12–48 reports tamper/wrong-key/unbound-path controls and the chain constants. These are historical documentary evidence, not a test rerun by this task. The chain hash recorded there is `8990e7a9aaed2ffed73dbd7092123d6f289930540d7651336225dc172e51b2ce`, with genesis 1595431050 and period 30. No verifier, dependency tree, or historical beacon response under the prohibited directory was opened.

**CONSEQUENCE FOR A1:** Replace line 36's hostname-only acceptance proposal with chain-bound BLS verification, round equality and signature-to-randomness binding, and expand line 26 to pin the chosen verifier/contract/dependencies before C while retaining prospective timing and the wait-or-abandon rule.

## 5. Exact immutable rendering/gate artifacts for the new manifest

**ANSWER — REQUIRES A DECISION BY THE LANE OWNER for the complete replacement execution inventory.** The retained rendering core and validation arithmetic are identifiable and their current code hashes match the original pins below; the new caller/adapter, scoring integration, environment closure and failure contract are not established by those pins. Listing only the core would leave A1's manifest incomplete. No production choice is made here.

| Required retained core | Current SHA-256, computed by C1 | Direct original authority |
|---|---|---|
| `study_renderer/__init__.py` | `659b763c83a948825d285e51671c28173b446f428bcd32d941811bf6cdaf5721` | Tier-C V39 §8.17a-iv, line 431 |
| `study_renderer/pixel_rejection_v2.py` | `075d73460645ab4c8353a468c8f3a7eabed8e9339198ea26f0dd51a35db02e54` | V39 §8.9a, line 351 |
| `study_renderer/renderer_v4.py` | `dad904ffb0dbc68fcb350be6fbee7ea57a5bf66503d61bf77a4272e0cb812b02` | V39 §8.17a, line 429 |
| `study_renderer/render_chain_v3.py` | `7835fda76591bfe5cd9fd4d3413654e212ed7a0f73a45da29b6cc324bbd0cf5e` | V39 §8.15b, line 391 |
| `miniprereg_pins/protected_region_v2.py` | `4b4fb5ca17953e0933bd5c2286ca23063247a472fbe2be5f4fc6d4a57e195faf` | V39 §8.14 line 373 and §9B.2d line 499 |
| `miniprereg_pins/validation_gate.py` | `65e241cad76b6150f625ac5aad085ed528004153d8590f8c32b07895c0c75e5b` | Tier-C V35 §9B.7a, line 508 |
| `miniprereg_pins/validation_resolver.py` — retain for plane-checksum verification if used; brick-resolution role stays with the input producer | `c3857ca8e530005df3be91fc1ae1a28b4dfe89621928b5de3f4ce66f53825ebc` | V39 §9B.2b, line 485 |

**EVIDENCE.** The table cites the original V39 text, not its change record or installation summary. Original code `study_renderer/render_chain_v3.py` lines 15–17 imports the named rejection, renderer and radius modules; lines 23–53 implements the chain; `study_renderer/__init__.py` line 9 exports renderer_v4. `miniprereg_pins/protected_region_v2.py` lines 41–44 gives the validation radius 23.0. `V39_INSTALLATION_RECEIPT_20260906.md` lines 24–45 is direct historical installation evidence, consistent with these bytes; it is not a fresh installation check.

Original V39 §8.15b line 391 explicitly says `scripts/stage2_render_validation.py` “is NOT an authorised path.” That script's actual lines 13–16 imports the old radius/rejection/renderer path, and lines 66–70 still uses the old exposure rejection. Likewise `scripts/stage2_gate_validation.py` lines 14–19 and 27–35 is an attempt-1 CE-ResNet/inference runner tied to historical paths, not a complete Fourier-winner validation adapter. Neither is silently promoted into the new manifest.

The owner must name and pin the exact replacement adapters/entry points and every local module/package initialiser they execute; the estimator and 96-search implementation; the winner/configuration, environment lock and executing interpreter/library binaries; tensor/label/integrity checks and refusal representation; score aggregation, repeat comparison, holdout/validation gates and result writer. Rendering also needs the specific input manifests, plane checksum pins, WCS/coordinate metadata and guarded access paths. Input production needs the eligible/failed/exclusion pins and derivation provenance. Original V15 E3(i) line 21 and E5 line 23 supplies the environment/input/custody obligations; §6 line 48 supplies preprocessing invariants. The resolver's original lines 16–20 identifies `scratch/survey-bricks-dr9-north.fits.gz` and the historical checksum manifest; a fresh draw must bind its own required bricks/plane digests rather than reuse an attempt-1 manifest by filename. None was opened.

For preserved scientific fixture provenance, the original V39 clauses also name `study_renderer/test_pixel_rejection_v2.py` (line 351), `study_renderer/test_render_chain_v3.py` (391), `study_renderer/test_renderer_v4.py` (429), and `miniprereg_pins/test_protected_region_v2.py` (373); V35 line 508 names `miniprereg_pins/test_validation_gate.py`. These references do not reinstate deferred broad test gates. The owner must explicitly decide which fixture/guard harnesses the new path actually executes and include their dependency pins accordingly.

**CONSEQUENCE FOR A1:** Expand lines 22–25 into separate artifact rows beginning with the proven core above, keep explicit unresolved rows for the replacement runtime closure, and require every render to use the retained V39 chain before C.

## 6. Render-refused identity at the scoring boundary

**ANSWER — REQUIRES A DECISION BY THE LANE OWNER.** Its statistical treatment is fixed: keep the identity in the selected set, never retry/replace/delete it, journal its refusal cause, and count it as unscored; it cannot become either orientation's match. The wire representation is not fixed by signed V15. It needs an explicit adapter/scorer contract, not an undocumented all-zero or all-NaN tensor.

**EVIDENCE.** Original V15 E3(i), line 21, requires every manifest identity to have a tensor and refuses a missing tensor; §7 lines 53–55 requires unscored handling and no removal/replacement. Original `OPTION_A_RUN_RECORD_20260906.md` line 33 explicitly identifies this collision: “TENSOR-MISSING refuses the manifest” while render can produce “no raster”; a sentinel convention “is a CLAUSE, not an adapter choice.” Original V39 §8.15b line 391 promises a tensor or REFUSED with cause, and actual `study_renderer/render_chain_v3.py` lines 50–53 returns REFUSED/reason without a tensor. These are compatible rendering obligations but an unresolved interface with the inherited all-tensors-required scoring manifest.

Recommendation for the owner: define a typed per-ID REFUSED record carrying cause and render-receipt binding, with the scorer bypassing tensor evaluation and recording UNSCORED; if a tensor sentinel is chosen to preserve the old loader, specify its exact shape, dtype, byte order and bytes/digest, an explicit refusal flag, provenance and reconciliation, and demonstrate it cannot contribute a score for any of the 96 configurations. Missing/corrupt ordinary tensors must still trigger input-integrity refusal, not be silently converted to legitimate render refusal. Preserve the distinct tuning/holdout and validation denominators from question 3. This paragraph is a recommendation, not an adopted representation. V39 §8.12 line 369 and §8.15c line 393 retain study-level DATA-INTEGRITY-FAIL routes; do not use a generic sentinel handler to downgrade every error into permissible attrition.

**CONSEQUENCE FOR A1:** Add the owner-selected refusal representation and cause/count reconciliation to line 38's scoring/input contract and line 40's unscored rule, and pin its adapter implementation before C.

## 7. V15 §10's imported V2 signing/precedence obligations

**ANSWER.** The imported clause has actual content; its title does not supply a blanket rule that any later proposal overrides earlier obligations.

**EVIDENCE.** Original selection-rule V15 §10 line 69 says “Signing and precedence — as V2 §10” and also lists one two-seat gate each on this rule, the pipeline amendment and V36. Original `OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V2_20260905.md` §10 line 64 states in full:

> This rule is a companion pre-commitment. It is signed by Duho's chat statement of its §17.2-style preimage digest (blank `DUHO SIGNATURE:` line), relayed by Blanc, recorded by Hwao; it is referenced by the V36 amendment (§9.1 identity) and by the pipeline amendment, both of which cite its digest. It is gated by two seats on different engines returning SIGNABLE before signature. Hwao does not sign; Blanc does not sign.

Thus the imported obligations are the companion status, exact preimage/digest statement by Duho, Blanc relay, Hwao record, digest cross-references from both companion amendments, and two different-engine seats before signature, with neither Blanc nor Hwao signing. The clause does not re-import V2's superseded two-candidate/two-further-attempt design.

There is a real procedural conflict to disclose: A1 line 59 proposes that “repeated two-seat package gates … are replaced by one independent amendment review,” whereas V2 line 64 requires “two seats on different engines returning SIGNABLE before signature.” A1 line 34's manifest commit establishes C; it does not itself supply the imported signature/relay/record. Original Tier-C V35 §§17.1–17.4 lines 750–758 makes the older blank-signature-line convention explicit. The later pipeline V39 §§17.1/17.3, lines 771 and 777, instead describes exact bytes with both signature fields permanently blank and approval UTC external; it allows the attested codex-conversation route. V39's procedure is documented for that pipeline amendment; its presence alone does not silently rewrite the selection-rule V15 §10 import.

The documentary answer needs no new Duho decision. The lane owner must recommend an explicit replacement signing/precedence clause for A1, identifying the review-count departure, final-byte approval evidence and companion-digest treatment; Duho retains final amendment authority. This task does not settle that future approval by implication or disturb the current independent review.

**CONSEQUENCE FOR A1:** Replace implicit §10 carry-over with an explicit proposed signing/precedence clause reconciling line 59's single review, line 34's C, final-byte approval/recording and companion digest references.

## 8. Conflicting seal-helper status statements

**ANSWER — REQUIRES A DECISION BY THE LANE OWNER, acting as history owner.** Preserve both statements and add a dated reconciliation supported by contemporaneous artifact/test/gating evidence; do not choose one by timestamp or erase either. Existence now would not establish when tests ran or whether gating permission had been given.

**EVIDENCE.** Both statements were read in original `OPTION_A_RUN_RECORD_20260906.md`:

- Line 30, 2026-09-06 10:59 KST: “gap 1 closed in code (NOT yet used)” names `_optionA_dev/seal_append.py` with full digest `7d393660c42706d4a59c05ed2cbc40b3dc15aab4e376aa1257cdf2636b00d8cb`, names the test-file digest, and states “6 tests OK warning-strict on a COPY of the real journal”; it separately says “Awaiting Blanc's ruling on whether it needs a seat before step 2.”
- Line 161, later state after the second step-1 collection: “the seal-append helper is not written, tested or digest-filed, and Blanc has not ruled on gating it”.

**Named conflict:** written/tested/digest-filed versus not written/tested/digest-filed. The two statements' unresolved gating permission is not itself contradictory and does not reconcile their artifact/test claims. Line 21 makes helper completion a prerequisite; lines 163–165 separately keep the successor/no-draw boundary. The file listing exposed helper filenames, but no helper, test, journal or review evidence was opened or run here; neither quoted digest/test count is presented as a fresh computation.

**CONSEQUENCE FOR A1:** Keep line 58's seal-helper deferral and line 40's chronology preservation, and add a reference to the history owner's prospective reconciliation without making the historical conflict disappear or treating it as permission for step 2.

## C1 — exact computation command and output

Executed from the lane root with the required interpreter and PYTHONPATH; `-B` prevents bytecode writes. Only the named source files were read, no code imported or run.

```sh
PYTHONPATH="$PWD/_optionA_dev/_venv_bls/lib/python3.9/site-packages" /Library/Developer/CommandLineTools/usr/bin/python3 -B - <<'PY'
from pathlib import Path
import hashlib
paths = [
'OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V15_20260906.md',
'MINI_PREREG_GZ_TIERC_DRAFT_V39_20260906.md',
'study_renderer/__init__.py',
'study_renderer/pixel_rejection_v2.py',
'study_renderer/renderer_v4.py',
'study_renderer/render_chain_v3.py',
'miniprereg_pins/protected_region_v2.py',
'miniprereg_pins/validation_gate.py',
'miniprereg_pins/validation_resolver.py',
]
for name in paths:
    print(hashlib.sha256(Path(name).read_bytes()).hexdigest(), name)
print('post_exclusion_arithmetic =', 12054 - 2000 - 2644)
PY
```

Output:

```text
fdd9eedd9938c2ba7df312cdc9b82a06612772ccc087e9365b33fd7d9d9a97d1 OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V15_20260906.md
ddc0cfb4139b7e1706f852cb5cdd7cb14293256fee8254cc71623bded172b2d0 MINI_PREREG_GZ_TIERC_DRAFT_V39_20260906.md
659b763c83a948825d285e51671c28173b446f428bcd32d941811bf6cdaf5721 study_renderer/__init__.py
075d73460645ab4c8353a468c8f3a7eabed8e9339198ea26f0dd51a35db02e54 study_renderer/pixel_rejection_v2.py
dad904ffb0dbc68fcb350be6fbee7ea57a5bf66503d61bf77a4272e0cb812b02 study_renderer/renderer_v4.py
7835fda76591bfe5cd9fd4d3413654e212ed7a0f73a45da29b6cc324bbd0cf5e study_renderer/render_chain_v3.py
4b4fb5ca17953e0933bd5c2286ca23063247a472fbe2be5f4fc6d4a57e195faf miniprereg_pins/protected_region_v2.py
65e241cad76b6150f625ac5aad085ed528004153d8590f8c32b07895c0c75e5b miniprereg_pins/validation_gate.py
c3857ca8e530005df3be91fc1ae1a28b4dfe89621928b5de3f4ce66f53825ebc miniprereg_pins/validation_resolver.py
post_exclusion_arithmetic = 7410
```

These are current full-byte file hashes, not approval statements. The V15 and V39 hashes match the identities printed in A1 and the original pipeline record. The failed CSV hash in question 2 is a direct original-document citation only, deliberately not included in C1.
