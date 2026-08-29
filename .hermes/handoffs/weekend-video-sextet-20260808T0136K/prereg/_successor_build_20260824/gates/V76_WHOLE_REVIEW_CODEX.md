# CODEX — V76 whole-document adversarial referee

## Verdict

**NOT CLEAR.** The pinned subject digest is correct, and the lifecycle pin, quoted G/N rows, class counts, reference-code pin, refusal-checker pin, and current lint execution all reproduce. The new honesty conversions do not, however, close the string surface they are offered to close. The registry generator omits already-declared canonical schemas while claiming mechanical completeness, three supposedly bounded environment leaves have no bounds, and the known-retired parser can be made to accept an explicit reactivation of a retired code. These are defects in load-bearing pre-unblinding controls, not objections to the parked questions.

## Findings

### F1 — HIGH — REPAIR-REQUIRED — the registry generator does not enumerate the declared schema surface

The universal statement at §6.1 lines 663–684 was replaced by an allegedly mechanical registry. Line 669 says it covers “the nine non-slot artifact classes” and line 674 says the generator “extracts every field token from the declared field lists” so omission is impossible. The bytes do not support either claim.

`ref/gen_string_field_registry.py` has only five draft extractors (lines 160–174): the BS-3g “exactly these … fields” block, the access-log parenthesis, the ENUMERATION ENTRY block, `cause`, and the three projection bits. It does not parse other canonical field lists already present in the draft, including:

- BS-L’s canonical body at §6.1 line 725;
- the opening-authorization body at line 734 (`BS-L digest`, both store identities, destination, ceremony identifier, phase, signer identity, schema/version);
- the archive seal-state schema at line 736;
- the unblinding-receipt exact authenticated fields at §11 line 1158.

The generated `ref/STRING_FIELD_REGISTRY.md` has no rows for the opening-authorization ceremony identifier, destination, store identities, or signer identity. Those strings therefore escape the claimed closed/bounded/digest-ref trichotomy without creating a FORBIDDEN-BY-DEFAULT row or a nonzero generator exit.

The inventory arithmetic is independently false. Read-only recomputation of the generator’s own constants returned 145 total rows, but `NONSLOT` contains **10** classes, not nine. Of those, **7** are `SCHEMA-PENDING`, not the six claimed in the V76 change description and §6.1 narrative: cutout completion, stage completion, label set, unblinding, adequacy, archive seal state, and lock checkpoint. Three inventoried plus seven pending equals ten.

This is not merely a prose count slip. A canonical opening authorization is an operative non-slot artifact consumed at P7, and its declared string fields are invisible to the control that is said to forbid invisible fields. Repair requires enumerating every already-declared artifact/schema field (or parsing all schema declarations through a single explicit syntax), adding the missing non-slot classes, and making a control prove that each declared artifact class has field-level coverage or an honestly blocking stub.

### F2 — HIGH — REPAIR-REQUIRED — `RECORDED-UNPINNED` is relabelled as bounded without any bound

The V76 honesty conversion at §6.1 lines 663–684 says `python`, `platform`, and `machine` are residual, unpinned surfaces, but still places them in the registry’s `bounded-encoding` class. The actual registry rows 102–105 state no maximum length, grammar, canonical encoding, or finite member set. The generator comments make the substitution explicit: lines 78–90 call the leaves “bounded only by their encodings,” but an encoding such as UTF-8 bounds representation, not message length or channel capacity.

The frozen source confirms the absence of a predicate. `successor_ref_v9.py` lines 53–64 records `sys.version.split()[0]`, `sys.platform`, and `platform.machine()`, while `require_environment()` compares only `python_major_minor`, `numpy`, and `byteorder`. No check constrains the three recorded leaves. They are included in every receipt envelope and hence enter pre-unblinding manifests and the BS-L environment record. “Recorded-unpinned” is honest about reproducibility but does not satisfy the separate string rule the same paragraph claims: these are a third kind, unbounded/unclosed recorded text.

The repair is not to call the residue honest again. Either (a) freeze exact values; (b) specify and enforce a canonical finite grammar and maximum byte length for each leaf; or (c) remove the leaves from the non-χ envelope and retain only a digest of a separately governed environment object. Until one of those happens, the registry’s no-third-kind claim is false and the environment remains an unbounded pre-lock string surface.

### F3 — MEDIUM — REPAIR-REQUIRED — the known-retired check accepts an explicit reactivation

The draft’s §6.1 retirement discussion and `tools/refusal_vocabulary_check.py` lines 115–142 claim that only known retired tokens receive an exemption and that activation/deletion is detected in both directions. The parser decides retirement from the presence of a retirement word anywhere in the same punctuation fragment. It does not detect a later semantic reversal in that fragment.

I ran the checker’s own clean fixture with this appended line:

> `REFUSED-LOCK-NOT-OPEN was deleted once but is now active and permitted.`

`check()` returned `[]`: no R01 and no other problem. The token is in `RETIRED`, `deleted` satisfies `RETIREMENT`, and the later “now active and permitted” is ignored. Thus draft prose and the checker dictionary can diverge while the checker exits clean; the retired side wins even when the sentence expressly restores the code. This directly defeats the brief’s requested punctuation/nesting/retirement attack and the claimed blocking invariant.

Repair by parsing retirement as an affirmative terminal disposition, not mere word presence: reject restoration/activation language in the same fragment, or more safely permit retired tokens only in a rigid machine-readable retirement declaration whose complete body is checked. Add the exact sentence above as a positive control expecting R01.

## Repairs and claims that held under attack (not findings)

- **HELD — subject identity.** Recomputed SHA-256 is `2aa58d40bfedfc701f7e951eec16c6e9c0753b889cced73d905e9821407469b9` before reading and again before report finalization.
- **HELD — lifecycle bytes and labelled derivation.** `LIFECYCLE_GUARANTEE_SPEC.md` hashes to `22c65dcfe4272b8e2e69d30746275c05b75c06a855157b2db0e5b2c8498c2c27`; `lifecycle_derivation_check.py` reports 0 problems and its 9 controls report 0 failures. I found no labelled G/N divergence.
- **HELD — frozen reference identity.** `ref/successor_ref_v9.py` hashes to the pinned `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`.
- **HELD — current eleven-code draft instance.** `tools/refusal_vocabulary_check.py` hashes to the draft’s `a9c8b89499812d67…`, reports 0 problems on V76, and its 24-control self-test reports 0 failures. F3 attacks what the controls fail to model, not the current eleven members as printed.
- **HELD — current registry regeneration state.** A read-only reproduction of the generator’s extraction/classification sets found 145 unique rows, 0 unclassified, and 0 stale. F1 is that the extraction universe is incomplete, not that its chosen universe fails closure.
- **HELD — class inventory and lint exit.** `prereg_lint.py` parsed 16 class-P / 8 class-E rows and exited 0 with 97 advisory, 0 blocking findings. Per the brief I did not re-report the legacy citation advisories.
- **HELD — BS-3g appears in the §6.1 non-χ slot list and has a named §11 schema/producer/verifier obligation.** The remaining implementation is openly unfinished; I did not count the parked BS-3g lifecycle issue or draw-discipline questions as new findings.

## Evidence ledger and scope

Files read as content: `gates/BRIEF_V76_REVIEW.md`; the complete 1,453-line V76 draft; `LIFECYCLE_GUARANTEE_SPEC.md`; `ref/RAISE_SITE_CLASSIFICATION.md`; `ref/STRING_FIELD_REGISTRY.md`; `ref/gen_string_field_registry.py`; the relevant `environment_record`, `require_environment`, `SLOT_SCHEMA`, and `receipt` regions of `ref/successor_ref_v9.py`; `tools/refusal_vocabulary_check.py`; and `tools/lifecycle_derivation_check.py`.

Commands/checks executed read-only: SHA-256 over the subject, lifecycle spec, refusal checker, v9 reference, and registry; refusal checker on V76 and `--self-test`; lifecycle derivation checker on V76/spec and `--self-test`; `prereg_lint.py` on V76; a Python import-based recomputation of registry found/missing/stale sets; and three synthetic retirement strings passed directly to `check()` without writing fixtures. I did not run `ref/gen_string_field_registry.py` as a script because its `main()` overwrites the registry, which the assignment forbids.

Deliberate exclusions: the parked availability-code identity leak, durable pre-verdict state, Row-F strata/producer pair, VOID partition, BS-3g cycle/draw discipline, call-site-vs-raise classification unit, freeze-signature residue, gain mapping, and `require_authorization`. I did not modify the draft, spec, checkers, registries, reference implementation, or any artifact other than this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V76
VERDICT: NOT CLEAR
COUNT: 3
F1 | HIGH | REPAIR-REQUIRED | §6.1 lines 663–684; §6.1 lines 725/734/736; §11 line 1158 | Registry extraction misses declared canonical schemas and miscounts its non-slot/pending surface.
F2 | HIGH | REPAIR-REQUIRED | §6.1 lines 663–684; ref/successor_ref_v9.py lines 53–64 | Three RECORDED-UNPINNED environment strings are called bounded although no byte, grammar, or value bound exists.
F3 | MEDIUM | REPAIR-REQUIRED | §6.1 lines 591–618; tools/refusal_vocabulary_check.py lines 115–142 | A known retired code can be explicitly reactivated in the same fragment while the checker exits clean.
<!-- END FINDINGS-BLOCK -->