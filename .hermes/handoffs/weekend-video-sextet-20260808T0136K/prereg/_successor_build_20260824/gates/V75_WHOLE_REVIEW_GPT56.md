NOT CLEAR

V75 repairs the literal V74 digest, render-buffer, and ordinary-startup claims, but the 138-field registry is still not an enumeration of the operative fields, the advertised isolated replay is not executable on the pinned runtime without reintroducing an unspecified dependency path, and the refusal checker still admits an active undeclared code. These are defects in the current bytes and referenced files, not re-findings of the brief's parked questions.

## Findings

### F1 — HIGH — the “environment fields extracted” claim registers one container while omitting all six runtime-created leaf fields

Draft §6.1 lines 663–684 says `ref/STRING_FIELD_REGISTRY.md` is generated from frozen v9's receipt envelope and environment fields and reaches 138 fields. The actual extraction does not do that. `ref/gen_string_field_registry.py` lines 155–162 parses only the outer `receipt()` envelope constructor and returns `envelope.environment` as one field. The registry therefore has one row at line 98 for `envelope.environment`, labelled `closed-vocab`, but no rows for its six decoded fields.

Frozen `ref/successor_ref_v9.py` lines 53–57 constructs that nested value at runtime with `python`, `python_major_minor`, `numpy`, `platform`, `machine`, and `byteorder`. Only three are members of `FROZEN_ENV` (line 50), and `receipt()` lines 208–224 calls `environment_record()` directly rather than `require_environment()`. In particular, `platform.machine()` supplies an unconstrained string to every authenticated receipt envelope. A strict verifier applying the registry has no leaf-field row or domain against which to reject it.

I imported the generator without running `main()`. Its own sets reported 37 prose-extracted fields plus 101 v9/synthetic fields = 138, while `envelope_fields()` returned only `envelope.slot`, `envelope.schema`, `envelope.environment`, `envelope.body_sha256`, and `envelope.envelope_sha256`. None of the six environment leaves is enumerated. Thus the V75 count repeats V74's payload-versus-envelope mistake one nesting level lower.

Required repair: extract the decoded environment schema recursively; register and constrain every leaf value; make the environment a canonical closed/digest-referenced body whose verifier rejects arbitrary `platform`/`machine` text; and add a control that inserts a new nested environment key and requires the generator to fail.

### F2 — HIGH — the nine non-slot “registry fields” are hard-coded class placeholders, not fields or digest references to extant per-class schemas

Draft §6.1 lines 586–587 makes non-χ status conditional on conformance to authenticated schemas and lines 668–677 claims the 138-field registry includes “the nine declared non-slot artifact classes as digest-refs to their per-class schemas.” The referenced generator does not parse any such schema. `ref/gen_string_field_registry.py` lines 164–167 hard-code nine class names in `NONSLOT`; line 172 unions those names into the field set unconditionally. Registry lines 101–109 then label each synthetic `nonslot.<class>` name a `digest-ref` with the qualification “where defined.” No schema path, schema digest, body field, or recursive field inventory is present.

This is mechanically defeatable. In memory I added an explicit backticked `free_text_detail` field to the draft's canonical archive seal-state schema at §6.1 clause 7 (line 736). `extract()` remained at 37 fields and did not see `free_text_detail`; the total would remain 138 and the generator would remain green because `nonslot.archive_seal_state_receipt` is injected independently of schema contents. A class-name placeholder therefore cannot enforce the claimed “field with no registry row is forbidden by default” rule.

The classification is also wrong on the document's own terms: the hard-coded set includes `cutout_completion_receipt`, `label_set_receipt`, and `adequacy_receipt`, while draft lines 686, 698, 704, and 712 expressly classify those artifacts as χ-bearing. Conversely, several non-slot schemas are only prose requirements or unresolved implementation items, so the alleged digest-ref currently points at no pinned canonical schema bytes.

Required repair: replace `NONSLOT` with structured, pinned per-class schema objects; recursively enumerate their actual fields and nested fields; require every class's live schema digest to exist and match before it can enter the non-χ list; and keep χ-bearing classes out of a registry whose title and enforcement claim are specifically non-χ.

### F3 — HIGH — `python -I -S` makes the production replay non-executable unless an unpinned dependency path is added back

Draft §11 lines 1315–1328 now requires replay under `python -I -S`, a cleared environment, and pinned cwd, then imports the pinned v9 module and computes all verdict cells under the production contract. On the exact host and interpreter used by the build, that launch cannot import NumPy. Running the referenced path exactly under the new flags:

`python3 -I -S ref/gain_counterfactual_path.py --help`

failed before argument handling with `ModuleNotFoundError: No module named 'numpy'` at `gain_counterfactual_path.py` line 47. A direct `python3 -I -S -c 'import numpy'` failed identically and showed a `sys.path` containing only the standard-library zip, stdlib, and `lib-dynload`. Frozen v9 itself imports NumPy at line 47, so no production-equal replay can proceed under the specified isolation.

Making it run requires adding a site-packages/vendor path or loading NumPy explicitly. V75 does not say which path, pin the imported package tree and compiled extensions, or attest loaded dependency origins/digests. “Interpreter binary and OS are trusted” does not cover an external NumPy installation, and “pinned working directory” does not supply it under isolated/no-site startup. The contract has therefore traded the pre-import hook window for either a guaranteed import failure or an unspecified bootstrap that can reintroduce the dependency-resolution degree of freedom.

Required repair: specify an executable sealed launcher, including the exact Python binary and an allowlisted, digest-pinned dependency closure (NumPy Python files and native extensions); load only from those absolute pinned locations; attest every loaded module origin/digest before computing; and add a positive control proving the real wrapper runs under the exact isolated command plus hostile-path negative controls.

### F4 — MEDIUM — the one-retirement-per-fragment repair still lets a single active undeclared code borrow a generic retirement word

Draft §6.1 line 618 says the refusal checker was hardened, and `tools/refusal_vocabulary_check.py` lines 121–143 now rejects a retirement fragment containing more than one non-member token. That is not token-bound retirement. A fragment with one active non-member and any unnegated retirement word still passes because `RETIREMENT.search(frag)` is global to the fragment.

Against the exact live checker bytes, I appended each of these independently to its otherwise-clean `_fixture()`:

- `REFUSED-EVADE remains in force — the old code was deleted.`
- `REFUSED-EVADE remains active, although the prior vocabulary was superseded.`
- `The deleted-token example means REFUSED-EVADE remains in force.`

For all three, `check()` returned `[]`. The new em-dash control uses two non-member tokens, so it exercises only `len(nonmembers) > 1`; it cannot catch the one-token/generic-retirement form. An active twelfth code can therefore coexist with all eleven required members while the checker exits 0.

Required repair: accept retirement only through an affirmative grammar bound to that exact token and only for tokens in the explicit `RETIRED` map; generic words such as “deleted” or “superseded” elsewhere in the fragment must not exempt a token. Add the three one-token attacks above as controls.

## Failed attacks / checks that held

- Subject identity held before reading: sha256 `781b7f3f065ff20dc2cbee1ec4bf5bde944cfe3a85ffe75f5df2a83fe0e69054` exactly.
- The current refusal-checker digest held: live sha256 is `35fd85487c5d71b0f25f583d08894ccabf99c1cfbd17324803be15d00f280ba7`, matching draft line 618's prefix. The new blocking lint comparison also ran clean.
- The lifecycle-spec pin held: live sha256 is `c6d266129689e05ea3f78c11ac266a4bcea6a95489f85eb6fe64d5244e15d8f5`, matching draft line 623.
- The V75 buffer repair held against V74's two direct contradictions: the buffer now survives post-commit delivery through the view session, and the interface is required to retain no redisplayable surface after the session. The spec and draft agree on those current bytes. I found no separate G/N table-cell omission beyond the stated unimplemented BS-2k design.
- `tools/prereg_lint.py` exited 0 with 97 advisory legacy citations and 0 blocking findings. I did not re-report the option-D legacy corpus.
- `tools/refusal_vocabulary_check.py` exited 0 on V75; its self-test reported 23 controls, 0 failures, every code controlled. F4 is a new control the suite does not contain.
- `tools/lifecycle_derivation_check.py` exited 0 with 0 problems; its nine-control self-test had 0 failures.
- `tools/prereg_counts.py` recomputed 16 class P / 8 class E and found prose agreement.
- `tools/prereg_trace.py` included V74→V75, recomputed 74 transitions, and reported 0 problems.
- `tools/void_registry.py` parsed 54 antecedents over 20 §6.1 rows and exited 0. I did not re-open the parked semantic-coverage/partition question.
- Frozen v9 identity held at `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`. `ref/RAISE_SITE_CLASSIFICATION.md` still enumerates 112 rows and closes arithmetically at 25 CALLER + 60 INTEGRITY + 20 NUMERICAL + 3 PLANNING-INTERNAL + 1 TYPED-OUTCOME + 3 WRAPPER = 112. I did not re-find the parked per-call-site classification unit.

## Evidence ledger and scope

Read as content: `gates/BRIEF_V75_REVIEW.md` first; all 1,447 lines of the exact-hash V75 draft; `LIFECYCLE_GUARANTEE_SPEC.md`; `ref/RAISE_SITE_CLASSIFICATION.md`; `ref/STRING_FIELD_REGISTRY.md`; `ref/gen_string_field_registry.py`; the environment, schema, and receipt regions of frozen v9; `tools/refusal_vocabulary_check.py`; `tools/lifecycle_derivation_check.py`; `tools/prereg_lint.py`; and both V74 seat reports.

Executed: subject and referenced-file SHA-256 checks; V74→V75 byte diff; official lint; refusal checker and self-test; lifecycle checker and self-test; counts, trace, and VOID tools; in-memory registry inventory and archive-schema mutation; three in-memory retirement attacks; and exact `-I -S` import/replay probes. I did not run `ref/gen_string_field_registry.py`'s `main()` because it writes the registry and the brief forbids writes outside this report.

No draft, spec, reference code, checker, registry, or other file was modified. The only write is this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V75
VERDICT: NOT CLEAR
COUNT: 4
F1 | HIGH | REPAIR-REQUIRED | §6.1 lines 663–684; ref/gen_string_field_registry.py lines 155–162; ref/successor_ref_v9.py lines 50–64, 208–224 | The 138-field registry treats the runtime environment as one container and omits its six decoded leaf fields, including unconstrained platform text.
F2 | HIGH | REPAIR-REQUIRED | §6.1 lines 586–587, 668–686; ref/gen_string_field_registry.py lines 164–172 | The nine non-slot rows are hard-coded class placeholders, not field inventories or digest references to pinned per-class schemas.
F3 | HIGH | REPAIR-REQUIRED | §11 lines 1315–1328 | The mandated `python -I -S` replay cannot import NumPy on the pinned runtime without an unspecified, unpinned dependency bootstrap.
F4 | MEDIUM | REPAIR-REQUIRED | §6.1 line 618; tools/refusal_vocabulary_check.py lines 121–143 | A single active undeclared REFUSED token still borrows any generic retirement word in its fragment and passes the checker.
<!-- END FINDINGS-BLOCK -->