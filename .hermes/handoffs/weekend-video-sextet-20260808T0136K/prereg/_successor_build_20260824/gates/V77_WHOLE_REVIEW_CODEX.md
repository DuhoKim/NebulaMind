# V77 whole-document review — CODEX

## Verdict

**NOT CLEAR.** I verified the subject at sha256 `d2d61a274c8c0739b4cd1b597265f7d7a1580d19a150b420235af9ca7901cfee` before reading it. Five repair-required defects survive: one canonical digest-ref has no canonical body; the new BS-7p bootstrap sub-schema is missing from the supposedly exhaustive string registry; the bootstrap verifier has no transitive load-closure rule; the retired-token checker can be defeated by an unlisted activation phrase; and the draft still carries the stale registry counts it says it removed.

## Findings

### F1 — HIGH — `canonical.provenance_record` is a registry row for a body the draft never defines

V77 §6.1 line 669 says six canonical bodies, including the provenance record, are now registry rows. `ref/STRING_FIELD_REGISTRY.md` lines 95–100 accordingly classify `canonical.provenance_record` as a `digest-ref` with a “canonical field-order encoding.” But the draft contains no `canonical provenance`, no `provenance_record`, and no ordered provenance field set. The only live statements are that `BS-1b.provenance` is now a digest-ref (line 672) and that BS-1/BS-1b carry provenance (lines 902–903). A digest-ref to an undefined preimage does not constrain what gets digested.

This is not an extraction success. `ref/gen_string_field_registry.py` lines 195–197 hand-add all six names through the `CANONICAL` constant; they are not extracted from a schema block. Importing the generator without writing files confirmed `canonical.provenance_record` is absent from `extract(draft)` while present in `CANONICAL`. Thus deleting or never writing the body cannot produce a missing-row failure. The claimed default-forbidden mechanism is bypassed by the generator itself.

Required repair: define the provenance record's exact ordered fields, canonical encoding, and verifier, and make the generator derive the row from that definition; otherwise classify the body/schema as pending rather than `digest-ref`.

### F2 — HIGH — the V77 BS-7p environment sub-schema falls completely outside the string registry

V77 §11 lines 1326–1330 newly defines `BS-7p.environment` as a canonical sub-schema with `interpreter_path`, `interpreter_sha256`, and ordered `dependency_roots` `(path, digest)` pairs. None of those three field names occurs in `ref/STRING_FIELD_REGISTRY.md`, and `gen_string_field_registry.extract()` returns false for all three. Instead, the registry's line 67 still classifies the entire `BS-7p.environment` field as `closed-vocab` with the note “declared clause/env sets.” That is false of a structured record containing arbitrary absolute paths and an ordered list.

The path values are exactly the kind of string-bearing leaves §6.1 lines 663–684 says must be closed or bounded. They have neither a closed set nor an encoding/length bound in the new sub-schema. The generator does not see nested schema fields, so it exits zero while omitting them. The “field with no registry row is forbidden by default” claim therefore does not bind this V77 addition.

Required repair: enumerate every nested bootstrap field, including the path and digest components of every root entry, with value-domain and serialization constraints; teach the generator to extract the nested sub-schema rather than retaining the obsolete scalar `BS-7p.environment` classification.

### F3 — HIGH — hashing listed roots does not pin the code and data the dynamic loader actually maps

V77 §11 lines 1326–1339 says the isolated replay pins the interpreter plus dependency roots and that this removes every rebinding vector short of owning the interpreter/OS. The stated verifier only recomputes the interpreter and the roots the receipt lists. It never proves that the list is load-complete, never defines a canonical directory/tree digest or symlink policy, and never rejects a loaded object outside those roots.

A conforming receipt can therefore list and correctly hash the Python package roots while an extension loads a BLAS/shared library, plugin, locale resource, or `ctypes` target from an unlisted mutable path. Changing that target changes computation without changing `interpreter_sha256` or any listed-root digest. This is not covered by the declared interpreter/OS trust boundary when the omitted object is a third-party library rather than an OS component. On this host, for example, NumPy's `_multiarray_umath` is a Mach-O extension whose loader dependencies include `@loader_path/../.dylibs/libopenblas64_.0.dylib`; that particular relative target can be covered by a sufficiently broad NumPy root, but nothing in V77 requires that root choice or checks the general transitive closure. The verifier sees only its declared list, not dyld's actual view.

Required repair: define canonical root/tree hashing, symlink handling, and a transitive import/dynamic-load closure; record or independently trace all mapped non-OS objects and refuse any outside the pinned roots or an explicit frozen OS allowlist.

### F4 — MEDIUM — the finite activation-word guard accepts a retired code made mandatory again

V77 §6.1 line 618 claims the retired-token contradiction scan was hardened, and `tools/refusal_vocabulary_check.py` lines 121–144 makes a retirement fragment illegal only when its finite `ACTIVATION` regex matches. I ran the actual `check()` against the exact V77 bytes plus this one sentence in memory:

`REFUSED-LOCK-NOT-OPEN was deleted but is now mandatory.`

The checker returned `[]`. `REFUSED-LOCK-NOT-OPEN` is in `RETIRED`; “deleted” grants the exemption; “now mandatory” restores normative force but matches none of `reinstat|restored|reactivat|is active|in force|hereby|applies again|governs`. The same construction works with other modal wording. The closed operative vocabulary can therefore diverge from the checker's dict while the checker and lint stay green.

Required repair: do not try to close activation semantics with a finite synonym list. Accept retired-token mentions only in a narrowly canonical tombstone form, or reject any additional normative/modal material in a fragment containing a retired token.

### F5 — LOW — V77 retains the hand-copied registry counts it says were removed

V77 §6.1 line 669 first describes “the nine non-slot artifact classes” and “145 fields,” then later on the same physical line says the counts are quoted from the generator, never hand-written, and that the generator says ten and seven. The generated `ref/_registry_counts.txt` is `total=151 nonslot=10 pending=7`; the registry itself has 151 rows. Thus the repaired paragraph simultaneously states the old and new inventories. This directly contradicts the V77 repair claim in the brief and is the same second-source drift the paragraph says it eliminates.

Required repair: remove the stale “nine” and “145” assertions or replace the entire prose count with a single generated quotation.

## Attacks that held

- The required subject digest matched both before reading and after the attack pass.
- `tools/prereg_lint.py` exited 0 with 16 class-P / 8 class-E and 97 advisory, 0 blocking findings. I did not re-report the legacy citation advisories.
- `tools/refusal_vocabulary_check.py` passed V77 and its own 25-control self-test. That green result is not credited for activation completeness because F4 is a new concrete counterexample.
- `tools/lifecycle_derivation_check.py` passed V77 and its 9-control self-test; the lifecycle-spec pin matched `22c65dcfe4272b8e2e69d30746275c05b75c06a855157b2db0e5b2c8498c2c27`.
- The three ≤64-byte interpreter strings do provide a real capacity bound. If the adversary already owns the interpreter, their chosen values buy no capability beyond the draft's explicit interpreter trust declaration; I therefore do not score the mere 64-byte channel separately.
- I did not re-derive any parked issue or attack the draw discipline excluded by the brief.

## Evidence ledger and scope

Read in full: `gates/BRIEF_V77_REVIEW.md`; exact V77 draft bytes; `LIFECYCLE_GUARANTEE_SPEC.md`; `ref/RAISE_SITE_CLASSIFICATION.md`; `tools/refusal_vocabulary_check.py`; `tools/lifecycle_derivation_check.py`; `ref/STRING_FIELD_REGISTRY.md`; `ref/gen_string_field_registry.py`; `ref/_registry_counts.txt`. Recomputed the hashes of V77, the lifecycle spec, frozen v9, and the refusal checker. Ran the lint, refusal checker and self-test, lifecycle checker and self-test, in-memory retired-token mutation, generator extraction probes, registry/count comparison, and a read-only Mach-O dependency inspection. No draft, checker, registry, reference, or other project file was modified; this report is the only write.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V77
VERDICT: NOT CLEAR
COUNT: 5
F1 | HIGH | REPAIR-REQUIRED | §6.1 line 669; registry lines 95–100; generator lines 195–197 | canonical.provenance_record is force-added to the registry although no canonical provenance body or field-order encoding exists
F2 | HIGH | REPAIR-REQUIRED | §6.1 lines 663–681; §11 lines 1326–1330; registry line 67 | BS-7p's nested interpreter/root fields are absent from the exhaustive string registry and environment is falsely classified closed-vocab
F3 | HIGH | REPAIR-REQUIRED | §11 lines 1326–1339 | listed-root hashing has no canonical tree or transitive dynamic-load closure, so unpinned loaded objects can affect replay
F4 | MEDIUM | REPAIR-REQUIRED | §6.1 line 618; tools/refusal_vocabulary_check.py lines 121–144 | a retired code made “now mandatory” evades the finite activation regex and passes the checker
F5 | LOW | REPAIR-REQUIRED | §6.1 line 669 | the paragraph still says nine non-slot classes and 145 fields while the generated counts are 10, 7 pending, and 151 total
<!-- END FINDINGS-BLOCK -->