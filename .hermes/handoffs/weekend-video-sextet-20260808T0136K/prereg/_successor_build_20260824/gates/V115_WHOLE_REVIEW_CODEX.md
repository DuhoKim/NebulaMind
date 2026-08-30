# V115 whole-document adversarial referee — CODEX

## Verdict

**NOT CLEAR.** The required subject digest matched before I read the draft. V115 closes the literal V114 gate-field, close-domain, pass-entry-evidence, export-binding, and trace-header defects, and the generated checks are green on their stated surfaces. The repair nevertheless leaves two lifecycle-integrity defects and one generator-control defect: pass records are not required to follow the closed five-gate order; the never-a-request repair contradicts T1's explicit obligation over fully decoded frames; and the new close-class echo accepts a widened four-token domain. The first two cannot ride the known-debt appendix because they determine which gate has actually passed and whether a termination-boundary execution violates T1. The third should not ride either: it is a control on an existing generator, is admissible under the scope freeze, and is exactly the mechanism intended to stop a closed vocabulary from widening silently.

## Subject identity and binding inputs

- Required V115 sha256, recomputed before reading: `8ed151b74f9b26892ea884557904acf4f7695b319389a5e7b241184fac3e07d7` — exact match.
- `LIFECYCLE_GUARANTEE_SPEC.md`: `a0c345aadcad2aaccc43b7635674d23f55d097e07d0d869dcb8495180fcdb8ad`, matching draft line 628.
- `ref/successor_ref_v9.py`: `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`, matching the draft and `ref/RAISE_SITE_CLASSIFICATION.md`.
- `tools/refusal_vocabulary_check.py`: `bf54a79bedca5dbb1d9db66de868c4e98dc6894dfcb236896495ffed8596437e`, matching draft line 623.

## Findings

### F1 — HIGH — REPAIR-REQUIRED — §6.1 lines 672, 1560–1564; spec §3d lines 142–196 — gate equality does not enforce the five-gate order

V115 binds a boundary to a gate and requires boundary → close/pass gate equality. That prevents the V114 cross-gate close substitution, but it does not require a pass record's gate to be the successor of its predecessor record's gate.

The normative machinery supplies:

- the ordered-looking list of five consultations: `BS-L` issuance, lock opening, `BS-7f`, `BS-V`, disclosure (draft lines 1560–1561);
- a pass record carrying `gate` and `predecessor_record_digest` (line 672);
- a statement that the “NEXT gate's pass verifies” the prior record, with fixtures only for duplicate gate token, a fork, a bad first predecessor, and a refusing pass emitting a record (line 1564);
- per-gate boundary alternation and boundary/pass gate equality (spec §3d and draft line 1564).

None states or fixtures the actual transition predicate:

`expected_gate(current.gate) == successor(previous.gate)`

Counterexample: after valid `BS-L`, opening, and `BS-7f` pass records, append a boundary with `gate=disclosure`, then a disclosure pass record whose `predecessor_record_digest` is the `BS-7f` pass. Boundary/pass equality holds; the predecessor hash is real; there is no duplicate gate; there is no fork; the first-record rule is irrelevant. The sequence skipped the `BS-V` verification pass. Row S separately requires a BS-V artifact, but artifact existence is not the omitted five-gate verification. The same defect permits a premature boundary/close to consume another gate's retry budget before that gate is due.

The only exact “one record per gate in the five-gate order” wording I found is in §10's V96→V97 historical findings-answer cell (line 1129), not in the live pass law. A historical repair claim is not the predicate or verifier contract that enforces it.

Required repair: define the five gate tokens as one ordered closed sequence; require the first gate's predecessor to be BS-2f and every later pass record's gate to equal the unique successor of the predecessor record's gate; reject omissions, permutations, repeats, and early boundaries for a not-yet-due gate. Add at least skip-BS-V, swap-BS-7f/BS-V, and premature-gate boundary fixtures. This is freeze-poisoning and debt-ineligible.

### F2 — HIGH — REPAIR-REQUIRED — spec T1 line 131 and §3d lines 142–150; draft §6.1 lines 640, 654 and §11 line 1564 — the W0 repair contradicts T1's own subject

V115 honestly demotes the no-decoded-frame pass-entry precondition to a Row-B implementation obligation with testimony plus a fixture. It then tries to make the chain law independent of that hidden state by saying that, if the obligation is violated and termination lands mid-hold, the decoded frame is not a request, dies as W0 residue, and is “NOT a T1 contradiction, because T1's ordering obligations attach to requests and this frame never was one” (spec §3d line 149; derived draft text at lines 654 and 1564).

That explanation contradicts the quoted T1 bytes. T1 does not limit this ordering obligation to an already-existing request. It expressly says, between requests, **“any fully decoded frame in Row B's hands completes its arrival commit first”** before drain-start (spec line 131, quoted into draft line 640). The counterexample V115 names — a fully decoded frame in hand, boundary appended contrary to the obligation, then a termination unit — is therefore a violation of T1's explicit frame-order clause even though §1c declines to call the frame a request.

Calling the frame W0 residue can bound the lifecycle consequence; it cannot make the execution non-violative of the T1 sentence whose grammatical subject is the fully decoded frame. The present text gives the same execution two incompatible statuses: violation of the pass-entry implementation obligation/T1 frame ordering, but “not a T1 contradiction.” That ambiguity matters at the gate: the chain is declared legal from records alone, while the only evidence of the T1 violation is the same writer's testimony/fixture surface.

Required repair: choose one contract. Either (a) keep T1's decoded-frame-first guarantee and state that this execution violates T1/BS-2k even though its externally visible residue is W0 and the chain alone cannot detect it, or (b) amend T1 so decoded-frame priority is explicitly a non-guaranteed courtesy whose failure is W0 residue. Do not preserve T1's universal frame obligation and then scope it to requests in the exception analysis. Because T1 is a lifecycle invariant used at termination, this cannot safely become known debt.

### F3 — MEDIUM — REPAIR-REQUIRED — draft §6.1 line 674; `ref/gen_string_field_registry.py` lines 708–723 — the close-class echo accepts vocabulary widening

The live draft now gives the intended exact domains:

- `ATTEMPT-CLOSE.close_class = {ABORTED, ABORTED-BY-RESTART}`
- `VERIFICATION-CLOSE.close_class = {ABORTED, EXPIRED, ABORTED-BY-RESTART}`

But the new CLOSE-CLASS DOMAIN ECHO does not enforce either exact set. It checks only that the verification-close note contains the substring `EXPIRED`, that the attempt-close note does not contain `EXPIRED`, and that both qualified field names occur in the draft. It never compares either note to an exact token set or cardinality.

I tested the attack in memory, without changing a file: I loaded `gen_string_field_registry.py`, changed only the `vclose.close_class` constraint note from the three-token domain to the same note plus `STALLED`, and called `crosscheck_declared()` on the exact V115 bytes. Result:

`close-class findings after widening vclose domain: []`

`widening accepted by echo: True`

The brief's specific four-token counterexample therefore passes the control. The same pattern permits another non-EXPIRED token in the attempt-close domain. This matters because line 674 calls both sets closed, and the retry derivation depends on exact close classes rather than “contains the one special member.”

Required repair: parse and compare the exact qualified token sets (or declare them once as machine-readable constants and derive prose/registry from those constants), and seed controls for both addition and deletion in both domains. At minimum, `{ABORTED, EXPIRED, STALLED, ABORTED-BY-RESTART}` must fail for verification-close and `{ABORTED, STALLED, ABORTED-BY-RESTART}` must fail for attempt-close. This is an existing-generator control repair and should land before the appendix freeze.

## Failed attacks and holdings

- **V114 gate ownership repair held locally.** Boundary now carries `gate`; cross-gate close substitution and foreign-restart-close no longer satisfy boundary/close equality. F1 is the next layer: global pass order, not local ownership.
- **Completed export binding held.** The lifecycle spec's completed terminal-review body now contains `successor_export_digest`; the ceremony regenerates the export from SUCCEXP and refuses absent, duplicate, or byte-mismatched exports before signing. `ref/gen_string_field_registry.py` carries `revbody.successor_export_digest` and the completed-form fields.
- **Close domains are single-valued in the current draft.** F3 attacks the claimed control against future drift, not the current three-/two-token prose.
- **Counts held.** `tools/prereg_counts.py` independently computed 16 class P / 9 class E and reported prose agreement.
- **Trace claim repair held.** `tools/prereg_trace.py ... --check V115` reported 114 computed transitions and 0 problems; line 1199 now accurately limits verification to digest columns and row presence and calls the section/count cells historical as-written.
- **Lifecycle pin and labelled derivation held.** The spec digest matched the draft and `tools/lifecycle_derivation_check.py` reported 0 problems. F2 is a semantic contradiction inside the spec's own T1/§3d reasoning, not quote drift.
- **Non-χ admission and domain-kind integration held on the declared inventories.** `gen_nonchi_surface.py --check` was byte-equal with 0 problems; its self-test returned 6/6. `gen_domain_kinds.py ... --check` was byte-equal and all sites covered. `verification-close` is present in the current declared kind map.
- **Refusal vocabulary held its stated limited contract.** Live check: 0 problems; self-test: 43 controls, 0 failures, every code controlled. I also reactivated a retired token with a wording outside the finite ACTIVATION list; the checker can be evaded as its own lines 129–135 explicitly admit. I do not score that declared heuristic limit because I found no such reactivation in V115 and the draft does not claim semantic completeness for it.
- **RAISE classification matched the referenced bytes.** `gen_raise_classification.py --check` was byte-equal; the frozen reference hash matched. I read the 113-site table and targeted the numerical/caller boundary against the reference functions. The already-referred per-raise/per-call-site unit limitation was not re-derived as a new finding.
- **Oldest-quiet §2 clause re-derived: §2.4 manifest closure held.** The live clause does not trust a parent plus its own digest: it binds the parent to BS-2s, the universe to external digest/cardinality, and cutout size to a frozen constant; the historical neighbour-brick counterexamples are named. I found no new caller-supplied answer that restores the shortened-parent escape.
- **Grid-before-ratification attack held.** Γ is ratified, but more importantly a pre-ratification/pre-build BS-3g receipt could not discharge BS-6: the successor-layer schema and replay harness remain required blockers, a missing/nonconforming receipt leaves the edge closed, and the mapping sentinel cannot discharge it.
- **Successor-export duplicate-in-one-commit attack held.** The completed ceremony explicitly refuses duplicates; the clean export is co-committed with the disclosure pass and its exact digest is in the completed human-signed body.

## Evidence and write-scope ledger

Content read in full or targeted form: `gates/BRIEF_V115_REVIEW.md`; exact-hash V115 draft; `LIFECYCLE_GUARANTEE_SPEC.md`; `ref/RAISE_SITE_CLASSIFICATION.md`; targeted `ref/successor_ref_v9.py`; `tools/refusal_vocabulary_check.py`; `ref/gen_raise_classification.py`; `ref/gen_nonchi_surface.py`; `ref/gen_string_field_registry.py`; `ref/gen_domain_kinds.py`; `tools/prereg_lint.py`; `tools/prereg_trace.py`; V114 referee reports only to verify the named repairs; and the V114→V115 byte diff.

Read-only executions: sha256 recomputation; prereg lint (97 legacy advisories, 0 blocking); prereg counts; refusal-vocabulary live check/self-test; lifecycle derivation check; raise-ledger `--check`; non-χ surface `--check`/self-test; domain-kinds `--check`; trace `--check`; repair-ledger `--check`; exact in-memory close-domain mutation; targeted AST/text searches. No draft, spec, source, generator, registry, checker, or ledger was modified. The only intended write is this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V115
VERDICT: NOT CLEAR
COUNT: 3
F1 | HIGH | REPAIR-REQUIRED | §6.1 lines 672, 1560–1564; spec §3d lines 142–196 | Boundary/pass gate equality does not require pass records to follow the closed five-gate order, so a verification gate can be skipped
F2 | HIGH | REPAIR-REQUIRED | spec T1 line 131 and §3d lines 142–150; draft §6.1 lines 640, 654 and §11 line 1564 | The W0 repair says T1 applies only to requests although T1 expressly orders every fully decoded frame to commit before drain-start
F3 | MEDIUM | REPAIR-REQUIRED | draft §6.1 line 674; ref/gen_string_field_registry.py lines 708–723 | The close-class echo accepts a fourth verification-close token and therefore does not enforce either claimed closed domain
<!-- END FINDINGS-BLOCK -->
