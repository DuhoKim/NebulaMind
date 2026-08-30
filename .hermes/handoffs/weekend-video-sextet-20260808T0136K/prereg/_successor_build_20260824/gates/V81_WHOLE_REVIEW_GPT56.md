# GPT56 V81 whole-document adversarial referee report

## Verdict

**NOT CLEAR.** I read `gates/BRIEF_V81_REVIEW.md` first and verified the subject SHA-256 as `aa62779e73f7708f67e9cc4a45346529a7c0cc36e3c2d3901e11e7668bce6e62` before reading it. Eight repair-required defects survive. The highest-risk defects are an interpreter mode that can substitute executable bytecode while every V81 check named for the isolated replay still passes, and lifecycle repairs that either live outside the pinned lifecycle spec or still conflate the spec's distinct touch kinds. V81 also has not repaired the store-identity join or the retired-code activation defect it claims to have answered.

## Findings

### F1 — HIGH — `-X pycache_prefix` can substitute executable bytecode while all stated replay checks pass

V81 §11 lines 1333–1345 hashes the pinned source, imports it under an absolute interpreter with `-I -S`, forbids `-O`/`-OO`, and verifies only `sys.flags.optimize == 0`. That does not bind the complete interpreter invocation. Python 3.9 accepts `-X pycache_prefix=<attacker-controlled-root>` while still reporting `isolated=1`, `no_site=1`, and `optimize=0`; the option appears in `sys._xoptions`, which V81 never checks.

The pinned interpreter's own import machinery shows why this is executable rather than cosmetic. `_bootstrap_external.py:404-427` redirects the `.pyc` lookup under `sys.pycache_prefix`. Its ordinary timestamp-pyc validator at lines 593-618 authenticates only the source mtime and size, not V81's independently computed source SHA-256. A timestamp/size-matched pyc under the selected prefix can therefore supply code different from the source bytes V81 hashed. The later `sys.modules`/native-image census does not detect the substitution: the Python module is present under the expected name and source identity; its code object came from the cache.

This directly breaks the claim at §11 lines 1367–1378 that isolation removes every configuration rebinding vector short of owning the interpreter/OS. Required repair: bind/refuse the complete argument and `sys._xoptions` surface, disable bytecode reads or require checked-hash pycs tied to the pinned source, and verify the executed code object rather than only the source path/digest.

### F2 — HIGH — the deadline repair is load-bearing lifecycle semantics outside the pinned lifecycle spec

V81 line 621 says the request lifecycle has one home in `LIFECYCLE_GUARANTEE_SPEC.md`, the draft is derived from it, and a conflict is a draft defect. The spec's state list at lines 77–84 has no deadline, watchdog, clock, expiry transition, or liveness invariant. A byte search of the spec finds no `deadline`, `timeout`, or `stuck` at all.

V81 nevertheless answers CODEX-V80 F5 only in unlabelled draft prose at line 646: every request carries a `DEADLINE`, whose BS-2k value turns a live pending request into failure. That sentence is the only mechanism preventing the exact nonterminal request V80 found, so it is load-bearing lifecycle semantics. It is neither in the spec nor quoted under a G/N label. `tools/lifecycle_derivation_check.py:17-23,47-83` deliberately checks only G/N-labelled rows and admits that an unlabelled invariant is invisible; consequently it reports 0 problems on this divergence.

Even the draft sentence leaves the clock and restart semantics open: absolute versus relative time, monotonic source, start point, durable binding, and whether recovery can reset the deadline are unspecified. A wall-clock rollback or recovery-reset deadline can leave the request pending indefinitely while satisfying the literal “carries a DEADLINE.” The repair must be stated in the spec as an invariant/state transition with a monotonic, non-resettable time basis and then re-pinned/quoted; otherwise the claimed one-home derivation is false.

### F3 — HIGH — V81's render repair assigns one event to two distinct touch kinds

The lifecycle spec defines `CONVEYANCE` and `RENDER` as different kinds of bytes leaving a store (`LIFECYCLE_GUARANTEE_SPEC.md:12-19`). G3 says every event is exactly one touch's or one refusal's event, and G5 says every render has its own committed event (`:30-35`).

V81 line 634 calls the object a **“committed render event”** but says it asserts only **“CONVEYANCE TO THE INTERFACE”** and never that a frame was viewed. That does not repair the V80 counterexample; it renames a conveyance event as a render event. If the event is the conveyance touch, the later first display is the spec's distinct RENDER and needs G5's event. If it is the render event, a crash before first frame leaves no render for the event to truthfully record. G6 cannot resolve this because a session that never opens supplies no render commit/session pair.

Required repair: keep the store-to-interface conveyance and first display/render as distinct touch facts with their own event semantics, or change the spec's touch definitions and re-derive the crash table. One event cannot be both under the current G3/G5 bytes.

### F4 — HIGH — the monotone-presence join still cannot derive store identity from the event

V81 line 626 repairs CODEX-V80 F4 by declaring the audit join `(STORE identity, brickid, objid)` and saying store identity is “derived from the event's row and stated surface.” But the event schema at lines 589 and 695-716 still has no store-identity field, and the declared derivation is not functional.

Several rows' stated surfaces touch more than one store. Row I (line 706) reads the committee-store label set and the corresponding main-store instrument outputs. Row O (line 712) decrypts both sealed stores. The same row and an ordinary read/decrypt operation therefore do not select one store. The event's `object identity` remains only brickid/objid (`ref/STRING_FIELD_REGISTRY.md:174`), and the operation vocabulary is not specified to encode a store.

Counterexample: a prior Row-I touch proves an object exists in the main store; a later Row-I `REFUSED-OBJECT-ABSENT` truthfully concerns the committee store under the same brickid/objid. The audit manufactures V81's disjunction—false code or forbidden removal—even though neither occurred. The repair needs an authenticated store/object namespace in each event, or a per-row/per-operation proof that yields exactly one store; the current “derived” assertion is not such a proof.

### F5 — HIGH — the exhaustive string registry omits the actual signature fields

V81 requires several signature values in non-χ artifacts: the independently signed continuation/explanation surface at line 608, Row L's freeze/lock/opening signatures at line 709, the BS-L detached signature at line 726, and Clause 6's opening-authorization signature envelope at line 735. The registry lists canonical **bodies** for those objects but contains only one signature field, `entry.signature` (`ref/STRING_FIELD_REGISTRY.md:99-107`). It has no `lock.signature`, `freeze.signature`, `opening_authorization.signature`, explanation signature, or associated signature-envelope leaf.

The omission is structural in the generator. `ref/gen_string_field_registry.py:141-145,266` manually adds only `entry.signature`; its CANONICAL set at lines 247-249 adds body names, not detached-signature fields. Thus the generator can report 177 classified fields while never seeing the signature bytes the draft requires.

This defeats §6.1 lines 664–678's claim that every string-bearing field in every non-χ artifact is enumerated and that missing fields fail by default. It also leaves the nonce/covert-channel argument applied to only one of several signatures. Every actual signature/envelope field must be represented with an exact deterministic scheme and encoding, or the registry's scope must be narrowed honestly.

### F6 — MEDIUM — the retired-token checker still accepts direct reactivation

V81's brief says the right token boundary was repaired and advertises 30 passing controls. The boundary repair holds for the tested suffixed token, but the operative retired-code rule remains a finite activation-word heuristic (`tools/refusal_vocabulary_check.py:121-160`).

Against the actual V81 bytes, appending either sentence in memory produced `check(...) == []`:

- `REFUSED-LOCK-NOT-OPEN was retired but is required for every P7 opening.`
- `REFUSED-CEREMONY-CONSUMED was superseded but is authoritative at replay.`

Both fragments contain the retirement word required for exemption; neither “required” nor “authoritative” is in `ACTIVATION`. They plainly reactivate a retired code and still pass R01. This is the unrepaired half of CODEX-V80 F6 and directly answers the V81 brief's invitation to reactivate without a finite listed word. A canonical machine-readable tombstone grammar is needed; an open-ended English activation list cannot establish absence.

### F7 — MEDIUM — “canonical JSON” is not canonical under the declared rules

V81 line 610 defines structured/nested payloads as “canonical JSON — sorted keys, compact separators, UTF-8.” That does not select unique bytes. The same logical string `é` serializes as either UTF-8 bytes for the character or the JSON escape `\u00e9`; both resulting JSON documents are compact, sorted, and themselves UTF-8. The common Python implementation also serializes equal JSON-number values `1` and `1.0` as different bytes. No Unicode normalization, escape policy (`ensure_ascii`), number grammar, negative-zero rule, or rejection of non-finite numbers is specified.

Therefore two independent implementers can sign different bytes for the same structured value while each follows the stated rule. This breaks the “ONE encoding for every canonical body” claim and can affect entry, explanation, opening, lock, and provenance digest references. The draft needs a real canonicalization standard or an exact byte algorithm covering strings and numbers, not only key order and separators.

### F8 — LOW — the draft's generated pending count is already stale

V81 line 670 says counts come from `ref/_registry_counts.txt` “and from nowhere else,” then hand-states that “the generator says ten and seven.” The referenced file's current bytes are:

`total=177 nonslot=10 pending=8`

The generated registry confirms eight `SCHEMA-PENDING` rows: `canonical.provenance_record` plus seven non-slot classes (`ref/STRING_FIELD_REGISTRY.md:104,126-133`). The prose therefore disagrees with its named source in the same sentence that prohibits hand-copying the count. This does not by itself change a gate, but it is a concrete byte-level registry status error and should be corrected mechanically.

## Failed attacks / checks that held

- The subject SHA-256 matched before reading and again after the review. The pinned bytes also matched: lifecycle spec `eeead2285f6a905cd2e92b7ab853de4f383b6000d25d3428b10e5d7bb2f3bf49`; frozen v9 `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`; refusal checker `b37fe6e30412a29ef87b67684ab230338e4d90cc3c2199296783db17ca480ea6`.
- `tools/prereg_lint.py` exited 0 with 97 advisory and 0 blocking findings; I did not report the principal-ruled legacy citation advisories.
- The lint self-test passed all eight controls. `tools/prereg_counts.py` reproduced 16 class P / 8 class E.
- `tools/prereg_trace.py --check` reproduced 80 transitions with 0 problems, and all three scope-rule controls passed.
- `tools/void_registry.py` reproduced 54 antecedents and its six-control self-test passed; I treated that as name coverage only, as the draft requires.
- `tools/lifecycle_derivation_check.py` reported 0 problems and all nine controls passed. F2 attacks its stated unlabelled-text blind spot, not its G/N byte comparison.
- `tools/refusal_vocabulary_check.py` reported 0 problems and its 30-control self-test passed. The right-boundary attack now produces R01; F6 is the surviving semantic-activation path.
- The Clause-6 opening body now consistently ends in `schema_version`; the V80 timestamp substitution is repaired.
- The type-exact mask requirement and no-callback requirement, as prose requirements for the future harness, defeat the two exact caller surfaces found in V80. I did not count the present old callback API as a fresh finding because BS-3g emission remains blocked and the V81 requirement explicitly replaces it.
- The `sys.flags.optimize == 0` check closes the specific `-O`/`-OO` route from V80. F1 is a different interpreter configuration vector with optimization still zero.
- I did not re-derive the parked VOID partition, durable pre-verdict/N2 state, strata/producer pair, known identity-field χ leak, integrity-mismatch collision, BS-3g lifecycle cycle, draw discipline, `require_authorization`, per-raise/per-call-site referral, or other principal-referred items.

## Evidence and scope

Read in content: the V81 brief first; exact V81 draft bytes; `LIFECYCLE_GUARANTEE_SPEC.md`; `ref/RAISE_SITE_CLASSIFICATION.md`; `ref/RAISE_CALLSITE_LEDGER.md`; `ref/successor_ref_v9.py`; `ref/gain_counterfactual_path.py`; `ref/STRING_FIELD_REGISTRY.md`; `ref/gen_string_field_registry.py`; `tools/refusal_vocabulary_check.py`; `tools/lifecycle_derivation_check.py`; `tools/prereg_lint.py`; and both V80 referee reports. Executed read-only: digest recomputation; lint/count/trace/lifecycle/VOID/refusal checks and self-tests; in-memory retired-token probes; exact V80→V81 diff; interpreter-flag inspection; and canonical-JSON counterexamples. I modified no draft, spec, reference, checker, registry, or any file outside this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V81
VERDICT: NOT CLEAR
COUNT: 8
F1 | HIGH | REPAIR-REQUIRED | §11 L1333-L1345, L1367-L1378; Python 3.9 _bootstrap_external.py L404-L427, L593-L618 | Unbound -X pycache_prefix can substitute timestamp-matched executable bytecode while isolation and optimize checks pass.
F2 | HIGH | REPAIR-REQUIRED | §6.1 L621, L646; LIFECYCLE_GUARANTEE_SPEC.md L77-L84; lifecycle_derivation_check.py L17-L23 | The deadline is load-bearing lifecycle semantics absent from the pinned spec and invisible to the derivation checker.
F3 | HIGH | REPAIR-REQUIRED | §6.1 L634; LIFECYCLE_GUARANTEE_SPEC.md L12-L19, L30-L35 | A “render event” is defined to assert conveyance, assigning one event to two distinct touch kinds and leaving first display unlogged.
F4 | HIGH | REPAIR-REQUIRED | §6.1 L589, L626, Rows I/O L706/L712; STRING_FIELD_REGISTRY.md L174 | Store identity cannot be derived from row/surface when one row touches multiple stores, so the monotone-presence join still manufactures contradictions.
F5 | HIGH | REPAIR-REQUIRED | §6.1 L608, L709, L726, L735; STRING_FIELD_REGISTRY.md L99-L107; gen_string_field_registry.py L141-L145, L247-L266 | The exhaustive string registry inventories canonical bodies but omits the lock, freeze, opening, explanation, and other actual signature fields.
F6 | MEDIUM | REPAIR-REQUIRED | tools/refusal_vocabulary_check.py L121-L160 | Retired codes reactivate with “required” or “authoritative” while the finite activation-word checker remains green.
F7 | MEDIUM | REPAIR-REQUIRED | §6.1 L610 | Sorted-key compact UTF-8 JSON is not a unique canonical encoding for escapes, Unicode, or numbers.
F8 | LOW | REPAIR-REQUIRED | §6.1 L670; ref/_registry_counts.txt L1; STRING_FIELD_REGISTRY.md L104, L126-L133 | Prose says ten non-slot/seven pending while the generated source says ten/eight.
<!-- END FINDINGS-BLOCK -->