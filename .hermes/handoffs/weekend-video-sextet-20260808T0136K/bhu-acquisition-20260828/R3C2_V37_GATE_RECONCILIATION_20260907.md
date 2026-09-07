# R3C2 — two-seat gate on V37 (`5d839970…`), reconciled BY TOPIC (2026-09-07 09:20 KST)

Reports: `R3C2_GATE_V37_codex_20260907.md` (**PREREG_UNSOUND**; N1 non-cosmetic, F3 continued non-cosmetic, C1 cosmetic; NO_MASKED_STAGE=NO and
PRIOR_FINDINGS_CLOSED=NO, both on account of the kit accepting a crashed stage; written 08:59, wrapper absent at 09:05:04),
`R3C2_GATE_V37_kimi_20260907.md` (**PREREG_SOUND_WITH_REPAIRS**; no numbered findings, two cosmetics; written 09:11:49, pid gone observed 09:14:52).
Access lines verified against the master on both. Blind intact.

| topic | codex | kimi | disposition in V38 |
|---|---|---|---|
| `origin_search.files` / `.matches` order changes merged bytes AND flips C6 PASS→FAIL on auditor-only permutations | N1 | — | REPAIRED with codex's exact sentence: one shared canonical-search function (query preserved, entries sorted by canonical JSON, nothing dropped or altered) applied at `merge` before keys, digests, branch selection and serialisation, and on BOTH sides of the C6 comparison; enumerated as MOI source (g); auditor-only search permutation added to the combined property. Blanc's 09:07 GUARD: changed-entry, added-entry and deleted-entry negatives are retained and still FAIL after canonicalisation, so normalisation erases no evidence difference |
| the exact-failure rule reached the text but not every judge: general `check` omits the setup guard, treats the completion token as optional and matches by substring (a real traceback was credited); deletion probes accept an undeleted diagnostic when only the marker moves | F3 (continued) | — | REPAIRED per codex's replacement and Blanc 09:07: ONE exact-result evaluator for every judge, no optional fields, no substring matching; pinned complete expected rows; probes require the targeted diagnostic to be ABSENT; subcommands lacking a completion token gain one |
| exhibition run description stale (8 narrated, 11 delivered) | C1 | cosmetic 1 | CORRECTED PROSPECTIVELY in §3; execution records are not rewritten |
| `SyntaxError` missing from the setup-error recogniser — a fixture that fails to parse could read as a legitimate expected negative | — | cosmetic 2 | REPAIRED (same class as the credited traceback) |

**DISCLOSURE — a pinned kit file was mutated while the kimi seat was still live.** Between roughly 09:13 and 09:14:52 the lane applied its
V38 kit patch to `r3c2_staged_d1d7/r3c2_staged_tests.py`, a pinned, seat-visible input, while kimi (pid 69800) was still running. This
violated the standing rule and Blanc's 09:07 instruction to prepare in scratch. The coordinating Codex observed the mismatch
independently: seat packet 8/8 matched; the kit sheet matched 20/21 with only that file differing (expected
`2752a972b4fb88498088…`, observed `a3d709dfeaf28df9d0c33540efa02573609562b9ea4531c662b416cae722e365`); at 09:15:01 the process was gone
and the file restored to `2752a972…` with mtime 09:14:52. All 21 pins re-verify.

What the evidence establishes, stated no more strongly than it supports:

- kimi's report was written 09:11:49, BEFORE the window, and its bytes did not change afterwards.
- The seat's stdout continued to 09:14:33, INSIDE the window. The stdout exceeds the report by exactly 201 bytes, and those bytes are
  only the report's own path, `R3C2_V37_GATE_COMPLETE`, and `session_id: 20260907_084453_713d42`. No analytic content, no re-read and no
  judgement was emitted during the window.
- Therefore no output of substance could have been influenced. These artefacts CANNOT prove that the backend performed no file read in
  the interval; they establish only that no read could have changed any output, because no substantive output exists there. Backend
  read/execute timing is not retrievable from the lane, so the residual exposure is **unresolved but bounded exactly as above**. The
  phrases "unaffected" and "the whole interval was immutable" would overclaim and are not used.

**The first seat's findings stand entirely outside this window.** The codex V37 review had already completed (report 08:59, wrapper
absent 09:05:04) before the mutation, so its executed counterexamples — the general-check traceback acceptance, the undeleted-diagnostic
probe and the `origin_search` inventory-order verdict flip — are unaffected by it in any sense. kimi's negative-control experiments
exercised `moi_judge` and do not refute them: PREREG_SOUND_WITH_REPAIRS must not be read as answering the first seat.

**Sweep (2026-09-07 09:20 KST):** every finding label in both reports checked programmatically against the rows above — missing: none. kimi filed no
numbered label; its verdict token was read for its stated content (two cosmetics), each carried as a row.
