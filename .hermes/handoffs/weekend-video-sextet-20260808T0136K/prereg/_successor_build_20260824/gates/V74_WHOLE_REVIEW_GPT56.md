NOT CLEAR

V74 still makes three security/derivation claims that its own bytes do not support, plus one lifecycle guarantee that fails on an ordinary cached-display path. The mechanical battery is green, but it does not exercise these surfaces.

## Findings

### F1 — HIGH — the 123-field registry omits an exact schema field and leaves a signature-shaped χ channel

Draft §6.1 line 610 declares an ENUMERATION ENTRY to be an authenticated record with “exactly these fields” and ends that field list with “the enumerator's signature.” The generated `ref/STRING_FIELD_REGISTRY.md` has no signature row. This is not a stale-output accident: `ref/gen_string_field_registry.py` lines 128–130 deliberately match the entry only through the literal delimiter `· the enumerator`, then extract backticked snake-case tokens. The non-backticked signature field lies beyond the extraction boundary.

I imported the generator without calling `main()` and ran its extractor in memory. It reported 37 draft fields plus 86 frozen-v9 fields = the advertised 123, while each of `enumerator's signature` and `signature` tested absent. The source line itself tested present for `enumerator's signature` and present for the regex's terminating delimiter. Thus “123 classified” proves closure only over the extractor's projection, not over the declared schema.

This is not merely a missing documentation row. A signature is a byte/string-bearing field, and the draft does not pin its scheme, canonical encoding, fixed width, deterministic signing rule, or uniqueness. A randomized or malleable signature can choose among multiple valid byte strings for the same body and carry a covert per-object payload while still authenticating successfully. That directly breaks §6.1 lines 586–587 (“none … can carry a per-object outcome value”) and lines 663–677 (“a field with no registry row is forbidden by default”). The omission also affects the signed explanation artifact named in line 610.

Required repair: extract schemas from a structured source rather than prose regexes; include every signature/envelope field in the registry; pin the signature scheme and canonical encoding; require deterministic or otherwise unique/non-malleable signatures over a canonical body; and add a control that mutates/removes every non-backticked field, including the signature. Regenerate and re-gate the registry.

### F2 — HIGH — “fresh interpreter” does not close the rebinding window because inherited Python startup and imports run before the pinned module

Draft §11 lines 1314–1323 says a new process “hashes the pinned file, imports it, and computes, with no code running before the import” and concludes that “A fresh process leaves no moment in which rebinding code can have run.” That conclusion is false for an ordinary Python child.

A live child showed `site preloaded: True` before user computation and a user-writable site-packages path on `sys.path`. Python can execute `sitecustomize`/`.pth` startup code and inherited import hooks before the verifier imports `successor_ref_v9`; `PYTHONPATH` and related environment variables can alter resolution as well. Hashing only `successor_ref_v9.py` does not bind its imported modules or the live objects assigned to its globals. A startup/import hook can therefore install a loader or patch imported dependencies while the v9 file still hashes to the required `6a9abbbd…`.

This is exactly the inherited-environment seam the brief asked to break. “Fresh process” removes prior in-process monkeypatch state; it does not make the process hermetic.

Required repair: specify and test a hermetic child launch, at minimum isolated/no-site startup (`-I -S` or an equivalent sealed launcher), a cleared/allowlisted environment, a fixed interpreter executable/build, an explicit read-only import path, and pinned bytes for every imported executable dependency used by the replay. After import, the child must attest the loaded module origins/digests and the identities/origins of verdict-critical callables before computing. Add hostile `PYTHONPATH`, `sitecustomize`, `.pth`, and meta-path-loader controls.

### F3 — HIGH — G5/G6 can be bypassed by compositor restoration of an already-delivered frame

`LIFECYCLE_GUARANTEE_SPEC.md` line 34 says a view ends on occlusion or any visibility interruption and that nothing displayed after the interruption is the same view. Lines 66–68 place a committed render in the post-commit/delivery windows; lines 102–112 require display after the interruption to be a new view and a new render commit. Draft §6.1 lines 652–653 repeats that rule and says each re-render is logged.

An ordinary window compositor breaks the implication. Row G can commit and display a frame; another window can occlude it; removing the occluder can reveal the compositor's already-delivered cached surface without any new sealed-store read, Row B conveyance, interface render call, or touch commit. By G6 this is a new view, but no mechanism creates G5's required event. N1 does not repair it: N1 permits unrecorded human perception after delivery, while G6 deliberately classifies the post-interruption display as a new view and Row G voids an unlogged view. The text has defined the boundary but has not controlled the surface that crosses it.

The current §11 “Atomic touch commit domain” fixtures cover aborted buffers, outcome equality, delivery retry, and recovery, but no compositor/visibility lifecycle. The lifecycle can therefore satisfy every Row B transaction rule and still expose a new unlogged view.

Required repair: make the sealed interface own the display-surface lifecycle. On every visibility loss, occlusion, navigation away, app backgrounding, display sleep, or equivalent interruption it must destroy/blank all cached frame surfaces; restoration must require fresh acquisition through Row B and a new touch commit before pixels can reappear. Add fixtures at the actual compositor/window boundary for occlude→reveal, background→foreground, display sleep→wake, navigation away→back, and crash/restart with a cached surface.

### F4 — MEDIUM — the draft's claimed current refusal-checker digest is stale again

Draft §6.1 line 618 says `29e85d4a38d89c61…` is the sha256 of `tools/refusal_vocabulary_check.py` itself, “recomputed after the last edit to that file in this revision,” and spends the same paragraph explaining that computing the digest last is the only order that survives.

The referenced file's current sha256 is:

`1db25971dda678a1f40f80841ecf5591c8e706d07aa53eaf7d4e2238713d5c6e`

It does not begin `29e85d4a38d89c61`. The lint remains green because this prose digest is not checked as a pin. This is the exact stale-self-description failure the paragraph claims to have eliminated.

Required repair: replace or delete the hand-copied digest claim. If retained, make the lint recompute it from the referenced file; do not keep an unchecked prefix in prose.

## Failed attacks / checks that held

- Subject identity held: `d229952d5046e9cc3827e81e371b49ef7bcb887daae22c1cef58208f3b243835` exactly.
- Companion pin held: live `LIFECYCLE_GUARANTEE_SPEC.md` sha256 is `ca24b6dd994a70b8396f58d8370fa4389a05500b2266402b9de8e3bd44ca8fe3`, matching draft line 623.
- Frozen v9 pin held: live `ref/successor_ref_v9.py` sha256 is `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`.
- `prereg_lint.py` exited 0 with 97 advisory and 0 blocking findings; I did not re-report the principal-ruled legacy citations.
- `refusal_vocabulary_check.py` exited 0 on V74; its self-test reported 22 controls, 0 failures, every code controlled. The finding above is outside those controls: the tool's prose digest is stale, not its eleven-code parse.
- `lifecycle_derivation_check.py` exited 0 with 0 problems; its self-test reported 9 controls, 0 failures. The compositor path is a semantic/enforcement hole, not a quote mismatch.
- `prereg_counts.py` recomputed 16 class P / 8 class E and found prose agreement.
- `prereg_trace.py` recomputed 73 transitions and found 0 problems.
- Independent AST enumeration found 112 `Raise` nodes. `RAISE_SITE_CLASSIFICATION.md` has 112 rows with closure 25 CALLER + 60 INTEGRITY + 20 NUMERICAL + 3 PLANNING-INTERNAL + 1 TYPED-OUTCOME + 3 WRAPPER = 112. I found no count omission and did not reopen the parked per-call-site unit issue.

## Evidence ledger and scope

Content read: `gates/BRIEF_V74_REVIEW.md`; the pinned V74 draft; `LIFECYCLE_GUARANTEE_SPEC.md`; `ref/RAISE_SITE_CLASSIFICATION.md`; `ref/STRING_FIELD_REGISTRY.md`; `ref/gen_string_field_registry.py`; relevant frozen-v9 regions; `tools/refusal_vocabulary_check.py`; checker usage/source needed to invoke lifecycle and trace correctly.

Commands/checks: subject and referenced-file SHA-256 recomputation; all checker runs listed above; in-memory generator extraction; AST raise recount; ledger class recount; live Python startup/module-path inspection. One initial lifecycle invocation omitted its required SPEC argument and exited with usage 2; one initial trace invocation supplied the draft where a directory was required and found no pairs. Both were corrected with the tools' documented forms, producing the results above.

No draft or referenced file was modified. The only intended write is this report.

## Uncertainties

I did not execute the absent successor-layer receipt constructor, enumeration verifier, or BS-2k lifecycle implementation; the draft itself says they do not exist. F1 and F3 therefore attack the preregistered contracts, not an implementation. F2 identifies degrees of freedom the contract currently leaves open; a future launcher could happen to be hermetic, but the current text does not require enough to make that true. The parked principal questions listed in the brief were not re-derived.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V74
VERDICT: NOT CLEAR
COUNT: 4
F1 | HIGH | REPAIR-REQUIRED | §6.1 lines 586-610, 663-677; ref/gen_string_field_registry.py lines 120-134 | The 123-field registry omits the exact enumerator-signature field and leaves a valid-signature covert channel.
F2 | HIGH | REPAIR-REQUIRED | §11 lines 1314-1323 | A fresh Python process still runs inherited startup/import code before v9, so the pinned-file replay remains rebindable.
F3 | HIGH | REPAIR-REQUIRED | LIFECYCLE_GUARANTEE_SPEC.md lines 34, 66-68, 102-120; §6.1 lines 652-653 | Compositor restoration after occlusion creates a G6-new view without a G5-new touch commit.
F4 | MEDIUM | REPAIR-REQUIRED | §6.1 line 618 | The claimed post-edit refusal-checker digest prefix 29e85d4a… disagrees with the live file's 1db25971… sha256.
<!-- END FINDINGS-BLOCK -->