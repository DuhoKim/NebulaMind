# V112 whole-document adversarial review — GPT56

## Verdict

**NOT CLEAR.** I read `gates/BRIEF_V112_REVIEW.md` first and, before reading the subject, independently obtained the required SHA-256 `22cf104327282adc4367b2f98b589ab4d2c89a3c3145a694743e46bbb671e1c7`. V112 closes several V111 surface declarations, but the identity repair is contradicted by its generated registry and is not consumed by the verifier contract; the new generated-surface checker is demonstrably blind to some of the drift it claims to make impossible; the admission hold conflicts with the already-mandatory receipt-note unit and has no enforceable timeout; the current-transition trace check fails; and two newly ruled terminal artifacts have no canonical value on ordinary lifecycle paths.

## Findings

### F1 — HIGH — the generated string registry still defines `request_digest` as the forbidden full-frame digest

The normative V112 identity changed, but its generated registry did not. `LIFECYCLE_GUARANTEE_SPEC.md:73` and draft `§6.1` Row B (`PREREG_SUCCESSOR_DRAFT_V112_20260830.md:713`) define `request_digest` as SHA-256 of the payload-free, domain-tagged identity envelope `(origin_row, frame_sequence, operation, object_identity)` only; `ref/DOMAIN_KINDS.md:32` also classifies `arrival.request_digest` as `TAGGED: identity-envelope`. In direct contradiction, `ref/gen_string_field_registry.py:224-227` still says it is the SHA-256 of the **complete framed wire unit**, domain-tagged `wire-frame`. The live registry check nevertheless reports `301 classified`, zero stale rows. This is not historical prose: §6.1 makes `ref/STRING_FIELD_REGISTRY.md` the value-domain contract consumed by `receipt_strict()` and the successor-layer verifiers. The repaired non-χ identity therefore has two incompatible live definitions.

**Required repair:** change the registry source row and regenerated artifact to the identity-envelope preimage, add a semantic control for that exact preimage/domain tag, and rerun the registry/non-χ battery.

### F2 — HIGH — the verifier never recomputes `request_digest` from the envelope it claims is the request identity

Draft `§6.1` Row B (`:713`) calls `request_digest` the request's own identity, while the enumeration-verifier contract at `:1564` checks only per-row strict increase of `frame_sequence`, absence of duplicate `request_digest`, key/terminal joins, and terminal equality on `(row, operation, object identity)`. It never requires

`request_digest == sha256(NMPR1:identity-envelope || canonical(row, frame_sequence, operation, object_identity))`

and never states that `origin_row` equals the arrival's `row`. Two arrivals with sequences 1 and 2 and arbitrary distinct 64-hex values `d1`, `d2` satisfy every named duplicate/sequence fixture even though neither digest is the preimage declared by the spec. Thus the new identity is present but not consumed—the exact oracle-without-verification shape V112 claims to have killed.

**Required repair:** make envelope recomputation and `origin_row == row` explicit verifier obligations with wrong-digest and row-alias fixtures.

### F3 — HIGH — the required V111→V112 sidecar mapping is not parseable by the trace checker

Draft `§10` (`:1075-1078`) requires the current transition to be mapped and checked in `gates/FINDINGS_MAP.md`. The file contains a human heading and prose at `gates/FINDINGS_MAP.md:107-139`, but the actual contract rejects it:

`python3 tools/prereg_trace.py <build> --check PREREG_SUCCESSOR_DRAFT_V112_20260830.md`

exits 1 with `SIDECAR MISSING: V111 → V112 is the current transition and is not mapped in gates/FINDINGS_MAP.md`. Its self-test also fails on the real subject for that reason. The repair ledger being complete does not satisfy this separately stated current-transition contract.

**Required repair:** express V111→V112 in the exact sidecar grammar `prereg_trace.py` consumes, then require both the live check and self-test to pass.

### F4 — MEDIUM — `gen_nonchi_surface.py` does not make a fifth integration lag impossible

Draft `§6.1(ii-g)` (`:674`) claims the generated admission check means “a fifth instance cannot exist unnoticed.” The generator does not support that claim. `ref/gen_nonchi_surface.py:99-120` checks a literal probe and, only for `restate=True`, field-name occurrence in the following 3,000 characters. Yet `vbound` is declared `restate=False` at `:62`, although it is not one of the quoted T-tuples for which the docstring justifies field blindness. Two in-memory attacks both stayed green: (1) retaining the literal `(ii-g) **the VERIFICATION-READ record` probe while appending “HISTORICAL ONLY; this paragraph no longer admits these records”; and (2) replacing the sole exact `VERIFICATION-BOUNDARY (kind, boot_epoch, monotonic_reading)` tuple with “schema retired.” Baseline and both mutations returned zero problems. This is a deletion probe, not a semantic/rewording or tuple-drift guard.

**Required repair:** make every non-quote-bound record row field-echoed; bind admission polarity/operative status rather than literal presence; add rewording, negation, and `vbound` tuple-deletion controls.

### F5 — HIGH — the gate hold and the mandatory mid-drain `RECEIPT-NOTE` cannot both obey their ordering laws

Spec T1 (`LIFECYCLE_GUARANTEE_SPEC.md:131`) requires a TERMINATED condition firing during `DRAIN-OPEN` to append its receipt and a distinct `RECEIPT-NOTE` as the indivisible store→log unit. The new gate hold (`draft:1564`) says the boundary is Row B's last ordinary append and that the **only** records before the pass record are pass-owned records, with one exception: a TERMINATED receipt landing with its **drain-start**, which aborts and re-boundaries the pass. A second TERMINATED condition during `DRAIN-OPEN` cannot append another drain-start. Its mandatory receipt-note is neither pass-owned nor the named exception. Appending it makes the hold interval malformed; delaying it until after the gate action violates T1's immediate indivisible unit and permits a gate decision against stale receipt-store state.

**Required repair:** explicitly include every termination unit (`drain-start` or `receipt-note`) as an abort-and-reboundary event, and fixture the DRAIN-OPEN/receipt-note case.

### F6 — MEDIUM — the admission hold's “budget” has no enforcing transition or failure consequence

The last sentence of the boundary contract (`draft:1564`) says the hold duration “is bounded by the BS-2k GATE-PASS BUDGET, a stated design obligation with its fixture.” No value, authenticated start/end readings, abort transition, terminal treatment, or verifier refusal is specified. A verifier that hangs after `VERIFICATION-BOUNDARY` can therefore hold all ordinary arrivals indefinitely; the request deadlines do not help because the draft deliberately starts D only after the held frame's arrival commit. A fixture cannot make a timeout law true.

**Required repair:** define the budget as a BS-2k constant, record its clock evidence, specify who aborts the pass and releases/re-boundaries admission on expiry, and name the gate/run consequence. Also state the cumulative bound for consecutive gate passes.

### F7 — HIGH — the ruled terminal-review body cannot encode a normally completed run

`TERMINAL_SIGNATURE_RULING_20260830.md:12-20` and `LIFECYCLE_GUARANTEE_SPEC.md:112` require the run-end P9 signature over `(kind, terminal_checkpoint_digest, drain_start_position, recomputed_head, verifier_digest, transcript_digest)`. But spec T3 (`:133`) defines the terminal checkpoint only for a TERMINATED-family drain, and a clean completed run reaches P9 disclosure without any drain-start or terminal checkpoint. The registry (`ref/STRING_FIELD_REGISTRY.md:215-220`) gives both fields ordinary digest/integer domains; no absent sentinel, completed-run alternative body, or final-checkpoint substitution exists. Thus the new fourth human waypoint is undefined on the ordinary completed path it principally exists to close.

**Required repair:** define distinct canonical completed/terminated terminal-review bodies (domain-separated), or define explicit canonical absent values and verifier rules, and add both lifecycle fixtures.

### F8 — MEDIUM — “unique JSON” still admits two byte strings for one value

The canonical-body rule in `draft §6.1` (`:614`) permits JSON-mandatory escapes, requires lowercase hex, and calls the result unique, but never chooses short escapes over equivalent Unicode escapes. JSON strings containing a newline can be encoded as `"\n"` or `"\u000a"`; both obey UTF-8, NFC, mandatory escaping, lowercase hex, compact separators, and decode to the same logical value. A direct Python `json.loads` comparison confirmed logical equality and byte inequality. The promised one-byte-string-per-value property therefore fails.

**Required repair:** prescribe one escape form per control character (for example RFC 8785/JCS rules, including mandatory short escapes where defined) and add equivalent-escape collision fixtures.

### F9 — HIGH — a pre-BS-L terminated run cannot construct the successor export's `sealed_enumeration_digest`

Spec T3 (`LIFECYCLE_GUARANTEE_SPEC.md:133`) requires every terminated run's successor export in the terminal checkpoint's own atomic drain-close step. The export schema (`draft:642`, `:671`, `:1564`) requires `sealed_enumeration_digest`. But the sealed enumeration set is defined as part of BS-L's signed checkpoint materials (`draft:612`, Clause 3(b) at `:743`). TERMINATED-family conditions can fire before BS-L; on that path no BS-L sealed-entry set exists, and no canonical empty/pre-lock set or alternate export body is defined. “Emit export with checkpoint or neither” does not supply the missing preimage.

**Required repair:** define a canonical terminal-time enumeration set for pre-BS-L termination (with its cut and authentication) or a domain-separated pre-lock export body, then fixture termination before and after BS-L.

## Failed attacks / controls that held

- The subject digest matched exactly; the lifecycle-spec, v9, closure-worker, and refusal-checker pins also matched their quoted digests.
- `prereg_counts.py` independently returned 16 class P / 9 class E and found the prose consistent.
- `prereg_lint.py` exited 0 with 97 legacy advisories and 0 blocking findings; its eight controls passed.
- `refusal_vocabulary_check.py` returned 0 problems and 43/43 controls; I did not re-report its explicitly documented finite activation-tripwire limit as a new semantic guarantee.
- `gen_nonchi_surface.py --check` was byte-equal with zero live problems and its four seeded controls passed; F4 is the stronger rewording/field-drift attack those controls do not exercise.
- `lifecycle_derivation_check.py` returned 0 problems; the quoted lifecycle rows are byte-synchronised.
- `gates/gen_repair_ledger.py --check` returned complete and byte-equal.
- `ref/RAISE_SITE_CLASSIFICATION.md` closes 113 enumerated sites (112 raises plus the production assert) with the stated class counts; I did not re-derive the parked call-site-granularity debt.
- The ratified gamma arithmetic closes: Γ=0.25, 50 steps, Δγ=0.01, 51 points, j₀=25; I found no additional draw-grid defect beyond the openly unbuilt mapping/harness blockers.
- Pair closure held against the simple close/decision crash attacks: successful decisions are themselves closes; dangling starts are closed by the next epoch before a new start. The new failure is the independent gate-hold/receipt-note composition in F5.

## Evidence and scope

Read as content: the V112 draft, `LIFECYCLE_GUARANTEE_SPEC.md`, both V111 reports, `REPAIR_LEDGER.md`, `FINDINGS_MAP.md`, `RAISE_SITE_CLASSIFICATION.md`, `gen_nonchi_surface.py`, `gen_string_field_registry.py`, generated string/domain registries, both principal ruling files, and `tools/refusal_vocabulary_check.py`. Executed only read-only hashes, check modes, self-tests, counts, lint, trace, and in-memory mutation probes. I did not modify the subject, spec, generators, registries, ledger, or any file outside this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V112
VERDICT: NOT CLEAR
COUNT: 9
F1 | HIGH | REPAIR-REQUIRED | §6.1 lines 669/713; gen_string_field_registry.py 224-227 | request_digest registry still specifies the forbidden full-frame wire digest
F2 | HIGH | REPAIR-REQUIRED | §6.1 lines 713/1564 | verifier does not recompute request_digest from the declared identity envelope
F3 | HIGH | REPAIR-REQUIRED | §10 lines 1075-1078; FINDINGS_MAP 107-139 | prereg_trace rejects the required V111-to-V112 current-transition sidecar as missing
F4 | MEDIUM | REPAIR-REQUIRED | §6.1 line 674; gen_nonchi_surface.py 61-65,99-120 | generated non-chi admission is blind to rewording and vbound tuple drift
F5 | HIGH | REPAIR-REQUIRED | lifecycle spec T1 line 131; §11 line 1564 | admission hold excludes the mandatory mid-drain receipt-note unit
F6 | MEDIUM | REPAIR-REQUIRED | §11 line 1564 | gate-pass budget has no value, enforcement transition, or failure consequence
F7 | HIGH | REPAIR-REQUIRED | lifecycle spec lines 112/133 | terminal-review body has no canonical completed-run values
F8 | MEDIUM | REPAIR-REQUIRED | §6.1 line 614 | canonical JSON permits short and Unicode escapes for the same logical string
F9 | HIGH | REPAIR-REQUIRED | lifecycle spec T3 line 133; §6.1 lines 612/642/671 | pre-BS-L termination has no sealed-enumeration preimage for the mandatory successor export
<!-- END FINDINGS-BLOCK -->