# FINAL BYTES — **VERDICT: FINAL-NOT-SOUND** (2026-09-07 17:59 KST). The readiness gate reads a SENTENCE, not evidence. That is my design error.
Reviewer agy / Gemini, ACCESS PROVEN for the current A1 `2465294f…`; exit artefacts first: stderr 0 bytes, stdout 2,681 bytes, rc 0 — completed, not a timeout.

## FATAL 2 IS THE ONE THAT MATTERS: READINESS WAS ENGINEERED, AND I BUILT THE MECHANISM
`input_readiness` (`run_path.py:306–329`) does not evaluate the runtime evidence against the registry's requirement. It checks whether A1's text contains the exact substrings mapped to `True` in `A1_OBLIGATION_STATEMENTS`. **So rewording A1 flips readiness.**
I insisted the flag must "fall out of the predicate, never be hand-set" — and then made the predicate a PROSE PARSER. A declaration and a discharge are different things, and I wired the gate to the declaration. Every protection I layered on top (registry completeness, the A1 digest pin, the refusal set) is intact and was defeated anyway, because they all guard a sentence. **My ordering rule — work, then statement, then re-pin, then predicate — cannot bind when the predicate's input IS the statement.**

## FATAL 1: THE OBLIGATION WAS DECLARED DISCHARGED, NOT DISCHARGED
Its text requires "reproducible byte binding for selected import artifacts AND OS shared-cache images". The implementation binds cache-resident images by OS-reported identity — UUID, OS build, path, LC_UUID — and **A1 line 49 openly says this is "not byte binding for a cache-resident image"**. The document states the requirement is unmet in the same breath as marking it met.

## MAJOR 3: THE DISCLOSURE I FORBADE WEAKENING WAS WEAKENED
The re-pin widened the TOCTOU disclosure that this reviewer had previously found ACCURATE — now disclaiming custom loaders, in-memory mutation and unobserved native reads, and adding that "no cross-process bit-exactness, scientific correctness, adoption or execution authority follows". My brief said in terms: do not weaken it. Revert to the reviewed wording.

## MAJOR 4: THE TESTS TEST WHAT WAS BUILT, NOT WHAT WAS REQUIRED
145 pass, and they exercise the UUID and OS-build checks that exist. **A mutation of a cache-resident library's bytes, with UUID and OS build unchanged, passes every one of them.** Fail-first evidence proves a change of behaviour; it cannot prove the behaviour is the required one.

## NOT BROKEN (checked): the MEDIUM producer, the CORE registers, the completeness checks, the counts, the exhaustive 96-configuration search.

## WHAT MUST HAPPEN — and one of these is a real decision, not a repair
1. **Readiness must be computed from EVIDENCE the code evaluates, never from A1's prose.** The prose cross-check may remain as a consistency check; it may not be the resolution criterion.
2. **Either** achieve actual byte binding for cache-resident images — the shared cache is a file on disk and loaded images have mapped ranges, so this may well be attainable — **or** amend the OBLIGATION TEXT to require what is actually achievable, stating plainly what that leaves undetectable. The second is a scientific decision that gets reviewed as one, not a prose edit slipped past a parser.
3. **Restore the TOCTOU disclosure** to its reviewed wording.
Readiness returns to FALSE until then. The packet assembler refuses. Nothing is presented to Duho.
