NOT CLEAR

V76 answers several literal V75 defects, but the two advertised honesty conversions still overstate what their referenced machinery constrains, and the isolated replay remains under-specified at the receipt boundary. The current registry calls three runtime strings “bounded” without declaring or enforcing any bound; its claimed nine/six non-slot inventory is actually ten/seven; and the frozen BS-7p schema has no authenticated leaves for the absolute interpreter or dependency closure that §11 says it records. Separately, the known-retired repair still allows a retired code to be reactivated in the same fragment as a historical retirement word while the checker exits clean.

## Findings

### F1 — HIGH — RECORDED-UNPINNED is honest about pinning but falsely claims a bounded encoding

Draft §6.1 lines 663–684 says every registered string field has one of three constraints and describes `python`, `platform`, and `machine` as RECORDED-UNPINNED but bounded by their encodings. The generated registry lines 102–105 labels all three `bounded-encoding`. The generator does not declare a maximum length, grammar, member set, or canonical restricted representation for any of them; it merely assigns that label in `V9_CONSTRAINTS` (generator lines 78–90).

Frozen v9 supplies the values at runtime from `sys.version.split()[0]`, `sys.platform`, and `platform.machine()` (lines 53–57). `require_environment()` checks only `python_major_minor`, `numpy`, and `byteorder` (lines 60–65). Every receipt then JSON-serializes the unchecked leaves into `envelope.environment` (lines 220–224). Its `field()` encoding has an eight-byte payload-length prefix but no accepted payload bound or refusal predicate (lines 180–182). A representable length is not the registry's promised bounded encoding: no stated bound prevents one of these fields from carrying an object-indexed payload, and no verifier can reject one as out of range.

This breaks the repair at its stated strength. “Recorded-unpinned” accurately admits that the values are not fixed, but it does not turn unconstrained interpreter text into the registry's `bounded-encoding` class. Trusting the interpreter/OS by declaration is a trust boundary, not a value-domain constraint on authenticated receipt bytes.

Required repair: either (a) specify exact grammars and hard byte limits and make the successor verifier enforce them, (b) close each leaf to an explicit freeze-time member, or (c) classify them as a genuine fourth residual kind and retract the three-kind/string-capacity claim. Add controls that substitute oversized and object-indexed values and require refusal.

### F2 — HIGH — the “pinned end-to-end” bootstrap has no receiptable interpreter/dependency identity

Draft §11 lines 1320–1326 requires an absolute interpreter path “recorded in BS-7p's `environment` field,” explicit pinned dependency roots, and says those roots and their contents join the frozen `require_environment` checks. But the operative v9 schema has only the single opaque field `BS-7p.environment` (v9 line 200); `receipt()` checks field names and non-emptiness, not a nested environment schema (lines 208–224). The registry itself classifies `BS-7p.environment` as `closed-vocab` with the note “declared clause/env sets” (registry line 67), yet no member set or authenticated subfields are declared for interpreter path, interpreter digest, dependency-root paths, root-content digests, loaded module origins, or native-extension identities.

The claimed check also does not exist in the frozen function it names: v9's `FROZEN_ENV` has only `python_major_minor`, `numpy`, and `byteorder`, and `require_environment()` compares only those three (v9 lines 49–65). V9 is explicitly frozen and cannot acquire the promised dependency-root checks. No successor-layer inventory item specifies a replacement environment schema or exact verifier fields. BS-7p is listed as an ordinary class-P slot, not a DESIGN slot (§7 lines 892–918), so leaving the schema design to fill time is not a value insertion.

Consequently an absolute path plus explicit `sys.path` can be described in prose while the authenticated receipt boundary cannot distinguish it from a different interpreter/dependency closure. The replay bootstrap is not pinned end-to-end until those identities are exact fields with independently recomputed values.

Required repair: specify a canonical successor-layer BS-7p environment sub-schema now, including absolute interpreter identity (and whether path, executable digest, or both bind), dependency-root manifests and content digests, module/native-extension origin attestations, and the verifier that recomputes them before replay. Reclassify BS-7p as DESIGN if those choices are intentionally still open.

### F3 — MEDIUM — the advertised nine/six non-slot honesty conversion is arithmetically false

Draft §6.1 line 669 says the registry covers “the nine non-slot artifact classes,” with three inventoried field-by-field and six `SCHEMA-PENDING` stubs. The referenced generator's `NONSLOT` tuple actually contains ten classes: access log, enumeration surface, acceptance projection, cutout completion, stage completion, label set, unblinding, adequacy, archive seal state, and lock checkpoint (generator lines 97–112 and 185–189). Seven, not six, are assigned `SCHEMA-PENDING`. The generated registry confirms seven pending rows at lines 109–116.

I imported the exact generator without its write-producing `main()` and obtained `NONSLOT_COUNT 10` and `SCHEMA_PENDING_COUNT 7`. Its ordinary run still reports “fields found 145, classified 145, stale 0” because the contradiction is in the hand-written inventory and prose count, not in its missing/stale comparison. The newly added `lock_checkpoint_receipt` is the tenth/seventh item and is invisible to the asserted closure count.

This is not merely a header typo: the conversion's argument is that every not-yet-enumerable class is honestly surfaced and blocked by its defining slot. An incorrect class inventory leaves the reader unable to tell whether the tenth class was deliberately admitted, which slot blocks it, and why the prose still says six stubs.

Required repair: make the count derived from `NONSLOT`, state ten classes/seven pending on the current design, and attach each pending class to its exact defining/blocking slot. Add a control that fails when the prose cardinality differs from the generated inventory.

### F4 — MEDIUM — a known retired token can be reactivated while the retired-token checker passes

The V76 repair narrows retirement exemption to tokens present in the checker’s `RETIRED` dict, but it still treats any unnegated retirement word anywhere in the same punctuation fragment as retirement of that token (`tools/refusal_vocabulary_check.py` lines 121–142). It does not check whether later words in the fragment reactivate the token.

Against the exact checker bytes, I appended each sentence independently to its otherwise-clean `_fixture()`:

- `REFUSED-LOCK-NOT-OPEN was deleted yesterday but is now active again.`
- `REFUSED-LOCK-NOT-OPEN is active here, although it was deleted before.`

`check()` returned `[]` for both. `REFUSED-LOCK-NOT-OPEN` is in `RETIRED`, each fragment contains the unnegated word `deleted`, and there is only one non-member token, so the exemption fires despite the affirmative activation. The self-test's negated-retirement and two-token controls do not exercise this grammar.

The current draft's own occurrence is historical and does not activate the token; the defect is in the blocking rule the draft relies on to prevent prose/checker divergence. A future edit can restore a retired code while preserving a true statement that it was once deleted.

Required repair: parse an affirmative retirement assertion bound to that exact token and reject any same-fragment activation/revival language after it; simpler and safer, permit retired mentions only in a mechanically delimited history form. Add both sentences above as R01 controls.

## Failed attacks / checks that held

- Subject identity held before reading: sha256 `2aa58d40bfedfc701f7e951eec16c6e9c0753b889cced73d905e9821407469b9` exactly.
- Companion/source pins held: lifecycle spec `22c65dcfe4272b8e2e69d30746275c05b75c06a855157b2db0e5b2c8498c2c27`; refusal checker `a9c8b89499812d67a6efb0922850eee08ca22adec4c100bce15969eb689738ee`; frozen v9 `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`.
- `tools/prereg_lint.py` exited 0 with 97 legacy citation advisories and 0 blocking findings. Per the brief, those advisories are not findings.
- `tools/refusal_vocabulary_check.py` exited 0 on V76; its self-test reported 24 controls, 0 failures, every code controlled. F4 is a missing activation-after-retirement control.
- `tools/lifecycle_derivation_check.py` exited 0 with 0 problems; its nine-control self-test had 0 failures. The spec pin and labelled full-body G/N quotes, including the added G6 one-to-one rule, are byte-consistent.
- The V75 simultaneous-two-session attack is closed textually: G6 now says each render commit opens at most one session and every session is opened by exactly one commit. I did not find an additional contradiction beyond the expressly unimplemented BS-2k design.
- `tools/prereg_counts.py` recomputed 16 class P / 8 class E and found prose agreement.
- `tools/prereg_trace.py . --check V76` recomputed 75 transitions and reported 0 problems.
- `tools/void_registry.py` parsed 54 antecedents over 20 §6.1 rows; its six-control self-test had 0 failures. I did not re-report the parked semantic VOID/numerical partition.
- `ref/RAISE_SITE_CLASSIFICATION.md` contains 112 rows and closes as 26 CALLER + 59 INTEGRITY + 20 NUMERICAL + 3 PLANNING-INTERNAL + 1 TYPED-OUTCOME + 3 WRAPPER. The prior `require_complete_sample` site is now CALLER. I did not re-derive the parked per-raise/per-call-site unit issue.
- BS-3g is present in the closed non-χ list, has a nineteen-field successor schema specification, a named producer/verifier obligation, and remains emission-blocked until the successor entry is pinned. I found no new receipting edge beyond the deliberately frozen draw-discipline surface.

## Evidence ledger and scope

Read as content: `gates/BRIEF_V76_REVIEW.md` first; then, only after the matching digest, all 1,453 lines of V76; `LIFECYCLE_GUARANTEE_SPEC.md`; `ref/RAISE_SITE_CLASSIFICATION.md`; frozen `ref/successor_ref_v9.py` environment/serialization/schema/receipt regions; `ref/STRING_FIELD_REGISTRY.md`; `ref/gen_string_field_registry.py`; `tools/refusal_vocabulary_check.py`; `tools/lifecycle_derivation_check.py`; `tools/prereg_lint.py`; and both V75 whole-review reports.

Executed: SHA-256 recomputation; lint; refusal checker and self-test; lifecycle checker and self-test; counts, trace, and VOID checks; independent AST/table recount of all 112 raise rows; read-only in-memory generator inventory; and two in-memory retired-token activation attacks. The registry generator's ordinary command was also invoked once; it regenerated byte-identical registry content, and `git diff` remained empty. No draft, spec, reference code, checker, registry bytes, or file outside this report were changed.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V76
VERDICT: NOT CLEAR
COUNT: 4
F1 | HIGH | REPAIR-REQUIRED | §6.1 lines 663–684; registry lines 101–106; v9 lines 49–65, 180–182, 220–224 | RECORDED-UNPINNED admits three runtime strings are unchecked but falsely classifies them as bounded encodings without any declared or enforced bound.
F2 | HIGH | REPAIR-REQUIRED | §7 lines 892–918; §11 lines 1320–1326; v9 lines 49–65, 200, 208–224 | The absolute-interpreter and dependency-root bootstrap has no canonical BS-7p subfields or verifier, so its claimed end-to-end pins are not receiptable.
F3 | MEDIUM | REPAIR-REQUIRED | §6.1 lines 663–677; generator lines 97–112, 185–189; registry lines 107–116 | The claimed nine non-slot classes with six pending schemas are actually ten classes with seven pending schemas.
F4 | MEDIUM | REPAIR-REQUIRED | §6.1 line 618; tools/refusal_vocabulary_check.py lines 121–142 | A known retired token can be declared active again in the same fragment as a historical retirement word while the blocking checker returns clean.
<!-- END FINDINGS-BLOCK -->