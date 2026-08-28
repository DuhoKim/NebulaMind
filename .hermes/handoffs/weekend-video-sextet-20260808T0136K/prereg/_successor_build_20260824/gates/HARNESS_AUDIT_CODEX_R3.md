# HARNESS AUDIT — CODEX R3

## Verdict

**NOT CLEAR.** `UNVERIFIABLE` is non-clean in the shipped CLI, so it is not a way to make a bad citation pass the gate. It is, however, trivially inducible and therefore can hide a real fabrication from the only outcome allowed to call it a document defect. More decisively, the shipped self-test remains green after the positive membership/`VERIFIED` branch is deleted, contrary to the R3 brief's claimed deletion probe. The parser also (a) diverges from the pinned spec on mixed grammars, (b) uses a contiguity proxy that misses duplicate and unparsed declarations, (c) scans past the findings-section boundary and verifies numbered non-findings, and (d) selects the wrong report family from live data while excluding the right one. A real `CODEX-V4 F9` in `GATE_CODEX_SUCCESSOR_V4.md` is consequently classified `FABRICATED` from the unrelated four-finding `GAIN_V4_REVIEW_CODEX.md`.

## Exact subject identities

I recomputed SHA-256 from the live bytes before adjudication. All four pins compare by exact 64-hex equality:

| subject | brief pin | recomputed | comparison |
|---|---|---|---|
| `/Users/duhokim/NebulaMind/NebulaMind/tools/prereg_lint.py` | `1b1f84b8537ef5bc11650b76061094056cd85d4c36ff7d4a14a940c1a4a0de9f` | `1b1f84b8537ef5bc11650b76061094056cd85d4c36ff7d4a14a940c1a4a0de9f` | MATCH |
| `../CITATION_CHECK_SPEC.md` | `5db2cf1cc3c2c23ba020ab2d13b87d6a4714ef3842b505de9c2fcb5d41570149` | `5db2cf1cc3c2c23ba020ab2d13b87d6a4714ef3842b505de9c2fcb5d41570149` | MATCH |
| `/Users/duhokim/NebulaMind/NebulaMind/tools/void_registry.py` | `4980701ce8695985d106f840ce8ebe6a9a5d06c15d51f40aff9544bc59046185` | `4980701ce8695985d106f840ce8ebe6a9a5d06c15d51f40aff9544bc59046185` | MATCH |
| `../ref/verdict_breakpoints.py` | `bd248c93984ffa2ed39cae16173df7b9535163e02c325109bfbb680bfcf39e56` | `bd248c93984ffa2ed39cae16173df7b9535163e02c325109bfbb680bfcf39e56` | MATCH |

## Findings

### F1 — BLOCKER — the citation battery stays green when the positive membership outcome is deleted, and its outcome assertions are not bound to the probe citation

`citation_outcome()` returns `VERIFIED` only at `prereg_lint.py:328-330`. I monkeypatched that semantic branch so every formerly `VERIFIED` citation returned `FABRICATED` with the same parsed numbers, leaving `FABRICATED`, `UNVERIFIABLE`, and `NO-REPORT` behavior otherwise unchanged. The shipped `self_test()` still returned **0** and printed all eight controls `OK`, including both citation controls.

That directly contradicts the R3 brief's load-bearing claim that deleting the membership test makes the citation battery red. There is no positive control asserting that a real cited member returns `VERIFIED`/silence. Every citation control is a negative mutation.

The control matching is also subject-unbound. At `prereg_lint.py:440` and `:467`, success means that *any* emitted tuple has the expected category and optional message substring. It does not require that the message name the mutation's seat/version/finding. I ran a stronger swapped-outcome probe:

- force the fabricated probe's `F97` to return `VERIFIED` (the probe itself is silently accepted);
- force the real baseline V34 citations that formerly returned `VERIFIED` to return `FABRICATED`.

The self-test again returned **0**, eight controls and zero failures. The real citations' wrong `declares findings` messages satisfied the fabricated control while its own F97 subject was accepted. The category-only `check_repair_citations` tuple at line 398 is even weaker: it supplies no outcome/message witness at all.

This is the exact category-versus-outcome residue requested in the brief: the two message substrings distinguish labels in the ordinary run, but the battery does not bind an asserted outcome to the citation the control inserted. A control can pass on the wrong citation and wrong outcome.

Smallest sufficient repair: call `citation_outcome()` directly on isolated one-report fixtures and assert exact `(outcome, numbers)` tuples for positive membership, absent membership, unrecognisable grammar, mixed grammar under the governing policy, and no report. If the full-document path is also tested, require the diagnostic to name the exact inserted seat/version/finding and ensure the unmutated baseline contributes no citation message.

### F2 — HIGH — `UNVERIFIABLE` is a hard stop but can be deliberately induced to hide a fabrication, and code diverges from the pinned mixed-grammar spec

A synthetic report containing:

```markdown
## Findings
### F1 — first
### Finding 2 — second
```

and a citation to `F97` returned `('UNVERIFIABLE', set())`, not `FABRICATED`. The reason is mechanical: `declared_findings()` treats any two nonempty grammar recognisers as mixed and returns unverifiable at `prereg_lint.py:312-313`. Thus adding one declaration in a second supported grammar moves every fabricated number in that report out of the only category permitted to call it a document defect.

This does **not** make the linter clean: `check_repair_citations()` emits an inconsistency at lines 262-266, and `main()` exits 1. Therefore `UNVERIFIABLE` is honest as an epistemic hard-stop outcome, not a bypass to certification. But it is a way to avoid the promised defect classification, and it is trivially author-inducible rather than reserved for genuinely opaque syntax.

The treatment also diverges from the pinned pre-code spec. `CITATION_CHECK_SPEC.md:39-40` requires acceptance when a report declares the finding in any actually used grammar, “including a report mixing grammars”; lines 71-72 require a mixed-grammar positive to `VERIFY`. The code makes every mixed report `UNVERIFIABLE`. The spec's line 55 permits outcome 3 when forms mix **inconsistently**; the code does not test inconsistency, only multiplicity. The brief's newer statement that mixed reports are unverifiable does not erase the requested pinned-spec divergence.

Smallest sufficient repair: settle the contradictory mixed-grammar policy in the pinned spec, then encode consistency structurally. A consistent union of declaration forms should not become unverifiable merely because two supported forms coexist; an inconsistent or ambiguous mixture should.

### F3 — HIGH — contiguity is not a valid proxy for complete, internally consistent parsing, and the findings region is unbounded

I constructed the requested counterexamples against `declared_findings()`:

1. **False recognition despite internal inconsistency.** Two declarations both numbered `### F1` returned `('recognised', {1})`. The set comprehension at lines 308-311 discards duplicates before the contiguity check, so duplicate numbering passes as internally consistent.
2. **False recognition despite incomplete parsing.** `### F1` followed by a real second declaration in an unfamiliar form, `### Issue 2`, returned `('recognised', {1})`. A citation to finding 2 then returned `FABRICATED`. Missing the trailing next number leaves the recognised subset perfectly contiguous; contiguity cannot prove complete parsing.
3. **False verification from outside the findings section.** `## Findings; ### F1 — real; ## Failed attacks; ### F2 — not a finding` returned `('recognised', {1,2})`, and citation F2 returned `VERIFIED`. At line 306 the region begins after the first heading containing “finding” and runs to end of file; there is no equal-or-shallower section close. Contiguity actively blesses the overmatch.
4. **False unverifiable on a complete non-1-based declaration set.** `### F1` and `### F3` returns unverifiable by design. That is conservative, but it does not distinguish a parser miss from an author deliberately retaining stable finding IDs. The code has no evidence for which occurred.

The first three are enough to reject the claim at `prereg_lint.py:299-301` that contiguous numbering from 1 establishes recognisable, internally consistent parsing. The third also reopens the R2 numbered-non-finding defect through a narrower same-grammar path: a numbered heading after the section boundary is still accepted.

Smallest sufficient repair: parse and close one structural findings section; retain declaration occurrences rather than immediately reducing to a set; reject duplicates explicitly; and do not use contiguity as evidence that no supported or unsupported declaration was missed. If completeness cannot be established, return `UNVERIFIABLE` rather than `FABRICATED`.

### F4 — HIGH — the fifth narrower-than-data pattern is report-family selection; it produces a live false `FABRICATED`

`_reports_for()` at `prereg_lint.py:279-284` admits a seat/version file only when its filename contains `REVIEW` or exactly equals `PREREG_TEXT_V<ver>_<seat>.md`. The live gate directory contains 22 seat/version reports excluded by that naming guard, including `GATE_CODEX_SUCCESSOR_V4.md`, `CLOSURE_V5_CODEX.md`, and the GATE V2–V10 series. `GATE_CODEX_SUCCESSOR_V4.md:23-25` is unambiguously a CODEX V4 report with `## Numbered findings` and finding 1; it continues through finding 10.

At the same time, `_reports_for(., 'CODEX', '4')` selects only `GAIN_V4_REVIEW_CODEX.md`, an unrelated V4-subject report whose parser result is recognised findings `{1,2,3,4}`. Direct outcomes were:

- `CODEX-V4 F1` → `VERIFIED` from the wrong GAIN report;
- `CODEX-V4 F9` → `FABRICATED {1,2,3,4}` even though GATE CODEX V4 really declares finding 9;
- `CODEX-V4 F10` → the same false `FABRICATED`.

This is narrower than the data in report selection and broader than identity in the citation key. The syntax `SEAT-Vn Fk` does not identify the reviewed subject, while the directory has multiple report families reusing Vn. A filename heuristic cannot safely choose which one the correction cites. It again uses a narrow pattern to manufacture absence, contrary to the pinned spec's generating rule.

Smallest sufficient repair: make the citation carry an immutable report identity (exact relative path plus SHA-256, or a unique report ID), and parse only that report. Do not infer report identity from seat/version and filename substrings. Without that identity, multiple candidate reports including any unrecognisable candidate must prevent `FABRICATED`.

## Required self-tests and executions

I ran every R3-required self-test independently from the assigned absolute gate directory with `PYTHONDONTWRITEBYTECODE=1`:

- `prereg_lint.py ...V34... --gates . --self-test` — exit 0; 8 controls, 0 failures. F1 demonstrates that this green result is not probative for positive membership or subject-bound outcomes.
- `prereg_trace.py .. --check ...V34... --self-test` — exit 0; real subject clean; 3 scope rules, 0 failures.
- `void_registry.py ...V34... --self-test` — exit 0; 52 antecedents; 6 controls, 0 failures. The visible label is now “row loses its naming antecedent.”
- `bs2a_quality_gate.py --self-test` — exit 0; 36 controls; all 26 checks exercised; 0 failures.
- `gain_gradient_estimator.py --self-test` — exit 0; all exact-recovery, old-normalisation, and G01–G09 controls held; 0 failures. The deliberate hostile numeric cases emitted the expected NumPy overflow warnings before refusal.
- `verdict_breakpoints.py --self-test` — exit 0; 48 transcription points, 10 breakpoints including 5 p-gate points, T01/T02 refusals, no declared orphan; 0 failures.

I also ran normal V34 lint: exit 0; 23 §7 rows (15 P, 8 E), 22 BS identifiers, and “no inconsistencies found.” Per the brief I did not redo the already-cleared trace refactor or V34 citation-reality adjudication.

## Failed attacks / what held

- All four pinned subject identities matched exactly.
- `UNVERIFIABLE` is emitted as a linter finding and causes exit 1; it is not silently treated as verified or clean.
- The fabricated F97 and current CODEX-V21 F4 mutations produce their intended ordinary-run message outcomes before monkeypatching.
- A numbering hole `{1,3}` is conservatively returned as unverifiable.
- The version matcher retains the R2 numeric boundary; no V1/V11 substring regression was found.
- `void_registry`'s public control label now says naming, and the verdict orphan regex accepts both single- and double-quoted literal `refuse()` calls.
- All six required self-tests exited 0; the blockers are semantic coverage and identity, not red production commands.

## Scope, parked decisions, and write custody

I did not re-litigate `OPEN_QUESTION_VOID_REGISTRY_COMPLETENESS.md` or `OPEN_QUESTION_T_COMPLETENESS.md`. Nothing here fills a slot, touches BS-6, or revisits the cleared `prereg_trace` refactor or V34 citation reality. Adversarial report fixtures were created in automatically removed temporary directories or in memory. Targeted pre-write `git status --short` over the four pinned subjects and this report path was empty. No pinned subject was modified; this report is the sole intended write.

**NOT CLEAR**