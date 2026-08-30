# V114 whole-document referee — CODEX

## Verdict

**NOT CLEAR.** I read `gates/BRIEF_V114_REVIEW.md` first and obtained the required subject digest before reading the draft:

`721e41ebfbbb6653615dea2da3be7b4c4d0b5a931d4692097fccc2973070c3aa`

The generated count, lifecycle-quote, refusal-vocabulary, raise-ledger, non-χ-surface, trace, and repair-ledger checks are internally green. Those checks do not close the new pass-law defects. The V114 `VERIFICATION-CLOSE` cannot prove which gate owns the boundary it purports to close; its new record kind is absent from the domain-kind registry despite the draft's domain-tag claim; and the pass-entry predicate is hidden Row-B state despite the spec's log-sequence law. Independently, the completed successor export is not bound by the terminal human review and has no later gate to verify it. These are verifiability/custody defects, not harmless annotations. They must not ride into a known-debt appendix: doing so would freeze a retry counter that can be reassigned across gates and a successor-facing artifact whose bytes are outside the closing human signature.

## Findings

### F1 — HIGH — A close can attribute another gate's boundary to itself

`LIFECYCLE_GUARANTEE_SPEC.md:187–199` makes the new retry count gate-specific: every unsuccessful boundary is closed; the alternation law is “per gate”; and the consecutive count is “the gate's close records since its last pass record.” But the actual exhaustive schema at `PREREG_SUCCESSOR_DRAFT_V114_20260830.md:674` is asymmetric:

- `VERIFICATION-BOUNDARY = (kind, boot_epoch, monotonic_reading)`
- `VERIFICATION-CLOSE = (kind, gate, boundary_position, close_class, boot_epoch, monotonic_reading)`

The boundary has no `gate`; only the later close asserts one. `ref/NONCHI_SURFACE.md:22,25` confirms the generated field sets rather than repairing them. Therefore a close can point `boundary_position` at a real boundary opened for gate A while declaring `gate=B`. The chain proves that a boundary existed at the position, but not that B owned it. That lets a verifier move an aborted/expired pair between gate counters, evade a cap by charging another gate, or exhaust the wrong gate. Epoch closure does not help: `ABORTED-BY-RESTART` repeats the same self-attributed `gate` field.

Required repair: bind the gate identity in the boundary itself and require exact equality across boundary, close/pass record, and the five-gate order. Add cross-gate substitution fixtures, including a restart close aimed at another gate's boundary. This class cannot safely become known debt because it defeats the byte-derived cap V114 was added to establish.

### F2 — HIGH — `VERIFICATION-CLOSE` is claimed domain-tagged but is absent from the domain-kind registry

Draft §6.1 item (ii-g), line 674, admits `VERIFICATION-CLOSE` and then says the admitted record kinds are “domain-tagged.” Yet `ref/DOMAIN_KINDS.md:5–32` lists `attempt-close`, `attempt-start`, `verification-boundary`, and `verification-read`, but no `verification-close`. The generator input agrees: `ref/gen_domain_kinds.py:25–46` declares the four predecessor kinds and omits `verification-close`.

I ran:

`python3 ref/gen_domain_kinds.py PREREG_SUCCESSOR_DRAFT_V114_20260830.md --check`

It nevertheless returned `domain kinds --check: byte-equal, all sites covered`. That green result is expected from the omission: the generator checks its `DECLARED` set and digest-ref sites; a new non-digest-bearing canonical record omitted from `DECLARED` is invisible. This is the V112 generator-input failure shape on the new V114 record itself.

Required repair: add `verification-close` to the declared domain-kind source and its generated output, bind it to the real preimage site, and add a seeded control deleting this exact new kind while leaving its schema admission intact. A canonical retry-count record with no registered domain separation is a freeze-poisoning integrity defect, not appendix-safe debt.

### F3 — HIGH — Pass entry depends on unreceipted decoder state, contrary to the log-sequence law

The spec's global law at `LIFECYCLE_GUARANTEE_SPEC.md:28–38` says every liveness, orphan, ordering, or staleness predicate is stated over log positions and records, never over motion/activity/completion. But §3d lines 149–159 permits a boundary only when “no fully-decoded-uncommitted frame sits in Row B's hands” and relies on decoding being paused after entry. The only boundary bytes admitted by draft line 674 are `(kind, boot_epoch, monotonic_reading)`. They contain neither a decoder-empty assertion, an input/frame watermark, nor a commitment to the receive/decode queue; §11 names no independent record or verifier that can reconstruct the predicate.

Counterexample: Row B has decoded frame X but has not committed X's ARRIVAL, appends a boundary anyway, then a termination unit arrives. The resulting chain is indistinguishable from the claimed legal empty-decoder entry, although T1 would have required X's arrival before closure. The verifier can check post-boundary syntax but cannot establish the premise that makes the “vacuous by construction” argument true.

Required repair: make pass entry receiptable from an authenticated queue/frame watermark (or redesign the transition so legality follows from records alone), name its consumer, and fixture a boundary appended with one decoded-uncommitted frame. Testimony by the same Row B that violated the precondition is not independent closure. This is not safe known debt because it reopens the lost-request/termination-order corner the lifecycle spec exists to eliminate.

### F4 — HIGH — The completed successor export has no closing verifier or human binding

`LIFECYCLE_GUARANTEE_SPEC.md:133` and draft §11 line 1563 say a clean/completed export is emitted in the same atomic commit as the disclosure pass record. Draft line 1563 then says “EVERY later gate pass VERIFIES-AND-CONSUMES” the export. On the completed path disclosure is the fifth and last gate, so there is no later gate.

The terminal ceremony does not repair this. The completed terminal-review body at `LIFECYCLE_GUARANTEE_SPEC.md:112` is exactly:

`(kind, disclosure_record_digest, recomputed_head, verifier_digest, transcript_digest)`

It contains no successor-export digest. The export body at draft lines 671 and 1563 is separately:

`(kind, sealed_enumeration_digest, continuation_segment_digest, terminal_head, freeze_signature_digest, flagged_keys)`

and is signed under the enumerator keypair—the same machine trust domain the terminal human review was introduced to bracket. Atomic co-commit proves all-or-nothing existence, not byte equality or semantic derivation: a bad export can be co-committed beside a valid disclosure record, after which the ceremony signs only the disclosure record/head. The successor is instructed to read the export first, but no closing human signature binds those export bytes.

Required repair: include a digest of the exact completed export in the recomputed terminal-review body (and recomputation transcript), or create an equally independent post-disclosure verification/consumption step. The terminal ceremony must refuse absent, duplicate, or byte-mismatched exports. This cannot be known debt: it would make the freeze consume successor-facing machine testimony outside its claimed closing waypoint.

### F5 — MEDIUM — The exhaustive admission gives `close_class` two incompatible domains

Draft line 674 first defines `VERIFICATION-CLOSE.close_class` as the three-token set `{ABORTED, EXPIRED, ABORTED-BY-RESTART}`. In the same exhaustive item, after describing all five record kinds, it later states unqualified that “`close_class` [is] the closed two-token set `{ABORTED, ABORTED-BY-RESTART}`.” That two-token domain is intended for `ATTEMPT-CLOSE`, as `ref/STRING_FIELD_REGISTRY.md:106–108,271–276` makes clear, but the normative draft does not qualify it and thus simultaneously excludes `EXPIRED` from the new record whose expiry pairs the retry cap counts.

The generated registry chose the intended interpretation; it cannot erase the contradictory source prose. Required repair: qualify both fields everywhere as `ATTEMPT-CLOSE.close_class` and `VERIFICATION-CLOSE.close_class`, with their distinct domains, and add a source-level field-domain echo that fails on an unqualified shared field name.

## Failed attacks / checks that held

- Subject identity held: sha256 matched the brief before reading.
- The companion pin held: `LIFECYCLE_GUARANTEE_SPEC.md` recomputed to `6845b868a8e6546a55c9a41e42e6cc3fecd4a8467f88dd01d6551c776fb877db`, matching draft line 628.
- Frozen reference identity held: `ref/successor_ref_v9.py` recomputed to `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`, matching `ref/RAISE_SITE_CLASSIFICATION.md:3`.
- `ref/gen_raise_classification.py --check` was byte-equal. I also read the 113-site table and its implicit-exception addendum. Its known per-raise/per-call-site limitation remains expressly referred by the brief; I do not renumber that parked defect here.
- `tools/refusal_vocabulary_check.py` recomputed to `bf54a79bedca5dbb1d9db66de868c4e98dc6894dfcb236896495ffed8596437e`, matching draft line 623. It returned 0 problems on V114; its self-test returned 43 controls, 0 failures, every code controlled. The operative eleven members were present and I found no new active `REFUSED-*` member. The checker's finite semantic-activation limit is stated honestly in its own lines 129–135, so a green result was not treated as a semantic proof.
- Counts held: `tools/prereg_counts.py` independently obtained 16 class P / 9 class E and reported prose agreement.
- Lifecycle labelled-byte derivation held: `tools/lifecycle_derivation_check.py DRAFT SPEC` returned 0 problems; its self-test returned 11 controls, 0 failures. F3 is outside that check's labelled-quote comparison.
- Non-χ generation held on its own declared surface: `ref/gen_nonchi_surface.py ... --check` was byte-equal with 0 problems. F1 attacks the semantics of the generated schemas, not output drift.
- Repair ledger held: `gates/gen_repair_ledger.py --check` returned complete and byte-equal.
- The 2g arithmetic attack did not break the stated upper envelope: with boundary readings rounded up, arrival readings rounded down, quantized budget, and strict `>`, the supremum is bounded by `budget + 2g`. Same-epoch release and restart abort are stated separately.
- The overlapping-five-holds attack did not produce a clean counterexample: §3d's legal-append list makes a second gate's boundary illegal while the first hold is open. The text should preferably say “globally one open boundary,” but I do not score a semantic hole there.

## Evidence and scope ledger

Content read: `gates/BRIEF_V114_REVIEW.md`; the exact-hash V114 draft; `LIFECYCLE_GUARANTEE_SPEC.md`; `ref/RAISE_SITE_CLASSIFICATION.md`; `ref/RAISE_CALLSITE_LEDGER.md`; `ref/successor_ref_v9.py` targeted regions; `tools/refusal_vocabulary_check.py`; `tools/lifecycle_derivation_check.py`; `ref/gen_domain_kinds.py`; `ref/DOMAIN_KINDS.md`; `ref/gen_nonchi_surface.py`; `ref/NONCHI_SURFACE.md`; `ref/gen_string_field_registry.py`; `ref/STRING_FIELD_REGISTRY.md`; `ref/_registry_counts.txt`; and relevant generated/checker scripts.

Commands executed read-only: sha256 recomputation; prereg counts; refusal-vocabulary check and self-test; lifecycle derivation check and self-test; raise-classification `--check`; non-χ-surface `--check`; domain-kinds `--check`; repair-ledger `--check`; targeted AST/text searches. No draft, spec, reference, generator, registry, or ledger file was modified. The only write is this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V114
VERDICT: NOT CLEAR
COUNT: 5
F1 | HIGH | REPAIR-REQUIRED | Spec §3d lines 187–199; Draft §6.1 line 674 | VERIFICATION-CLOSE self-attributes a gate that its referenced boundary does not bind
F2 | HIGH | REPAIR-REQUIRED | Draft §6.1 line 674; ref/DOMAIN_KINDS.md lines 5–32 | New VERIFICATION-CLOSE is claimed domain-tagged but absent from the generated domain-kind source and output
F3 | HIGH | REPAIR-REQUIRED | Spec §0b lines 28–38 and §3d lines 149–159; Draft §6.1 line 674 | Pass entry relies on hidden decoded-frame state that no record or verifier can establish
F4 | HIGH | REPAIR-REQUIRED | Spec §3b line 112 and §3c line 133; Draft §11 line 1563 | Completed successor export is neither in the terminal human-signed body nor checked by any later gate
F5 | MEDIUM | REPAIR-REQUIRED | Draft §6.1 line 674 | One exhaustive schema item gives close_class both a three-token and unqualified two-token domain
<!-- END FINDINGS-BLOCK -->