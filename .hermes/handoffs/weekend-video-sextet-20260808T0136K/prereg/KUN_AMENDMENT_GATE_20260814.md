# KUN_AMENDMENT_GATE_20260814

Timestamp: 2026-08-14 KST

Brief: `prereg/_tmp_KUN_AMENDMENT_GATE_BRIEF.md`

Artifacts gated, with hashes recomputed from disk:

- `prereg/PREREG_LONGO_AMPLITUDE_TEST_20260814_CANDIDATE.md` — `70d6862069fb2d87f8510c0265df941d7e165324db93fc7be918d3758400be1c`
- `prereg/release_linter/nm_release_lint.py` — `7ff18bfc9272bcbb924b77cb81f2b37c45a130c2b1c5ba1fbc9b95baaab323ac`
- `prereg/release_linter/SELFTEST.md` — `c23bed0d42865961bba1240dbcb52fb496281d044afa766a64c6a07253f66706`
- `prereg/release_linter/test_nm_release_lint.py` — `4316567c26b68296fcc870534dea66b56f34cf5167bc78e16b11576d8bf309cb`
- `prereg/release_linter/YUI_RELEASE_LINTER_20260814.md` — `1c47e8d9c4b4c1ff1af0ebb29d97c2b39c8a22d8e45b2342df32ecd67e07b29b`
- preserved 08-12 draft, `prereg/PREREG_LONGO_AMPLITUDE_TEST_20260812.md` — `ac43490054b159610385b8faac28dc4e3178161fadd97d66aa0418a1186b7590`

Boundary: documentation/gate only. I did not inspect sky data, rows, positions, images,
chirality labels, or sky statistics. I did not freeze, publish, accept, commit, or push anything.

## Verdict

**PASS THE AMENDMENT DIRECTION AND LINTER IMPLEMENTATION; HOLD THE FREEZE CANDIDATE FOR A NARROW
TEXT REPAIR.**

The amended design now carries the core aggregate-only output boundary correctly. The release
linter exists, is hash-pinned, passes its unit tests and synthetic self-test, and is the right
construction for a new binding slot. But the candidate cannot be frozen as written because it still
lists **BS-11 as OPEN**, and because three operational limits are binding only in the linter report,
not in the preregistration itself.

This is a fixable assembly defect, not a reason to reopen the science design.

## Verification Run

I reran:

- `python3 prereg/release_linter/nm_release_lint.py --self-test`
  - result: `PASS_SYNTHETIC_SELFTEST`, `fixtures=22/22`
- from `prereg/release_linter`: `python3 -m unittest test_nm_release_lint.py`
  - result: `36` tests, `OK`

An initial root-level unit-test invocation failed because `test_nm_release_lint.py` imports
`nm_release_lint` as a local module. Rerunning from the linter directory is the correct invocation
and passed.

## 1. Nine Redesign Blockers

1. **Exact preregistration amendment absent** — **CLOSED IN SUBSTANCE, OPEN IN ASSEMBLY.** The
   candidate now integrates F-10, the rewritten BS-1, the corrected what-is-lost table, safe
   commitment language, and the data-availability sentence. It cannot freeze until the BS-11 row is
   filled rather than marked OPEN.
2. **Old BS-1 text still fails until rewritten** — **CLOSED.** The candidate explicitly says old
   BS-1 remains failed and replaces it with aggregate-only validity text. It does not falsely claim
   derived-catalogue publication permission.
3. **Release manifest/linter absent** — **CLOSED AS AN ARTIFACT, OPEN IN THE REGISTER.** The linter
   exists and passes tests. The preregistration still says BS-11 is OPEN.
4. **Assembled freeze document absent** — **CLOSED.** The 2026-08-14 candidate is the assembled
   freeze candidate, subject to the narrow repairs here.
5. **BS-8 wording** — **CLOSED.** The candidate says analytical evaluation of the pinned harness
   logic, not a literal custom-parameter rerun.
6. **BS-4 warning placement** — **CLOSED.** The sparse-secondary warning appears in §3 I-2 and is
   explicitly required at the BS-4 slot.
7. **BS-3 zero-case distinction** — **CLOSED.** The nonzero 1,000-probe identity witness and the
   signed-zero edge probe are separated.
8. **BS-6 `TYPE` wording** — **CLOSED.** The candidate calls it an automated Tractor source-type /
   point-source exclusion, and forbids visual-morphology or chirality-label language.
9. **BS-10 locator cleanup** — **NOT A FREEZE BLOCKER AS WRITTEN, BUT REMAINS PUBLICATION-FACING
   CLEANUP.** The candidate treats BS-10 as informational and preserves K-14. If the preregistration
   itself becomes a public citation artifact, the published-journal locator should be made exact;
   it is not needed to freeze the Longo-amplitude preregistration because Shamir remains
   non-decision-language only.

## 2. BS-11

**BS-11 is the right construction.** The output boundary has enough operational content that a
machine-enforced release gate should be a binding slot, not an informal later checklist.

The fill rule should be:

> Before any public release, the complete proposed release package, plus every prior or concurrent
> public release in this study's cumulative release registry, must pass the pinned
> `nm_release_lint.py` at SHA-256 `7ff18bfc9272bcbb924b77cb81f2b37c45a130c2b1c5ba1fbc9b95baaab323ac`;
> the linter self-test must report `PASS_SYNTHETIC_SELFTEST fixtures=22/22`; the unit suite must
> pass 36/36; any linter REJECT, self-test mismatch, unlisted file, manifest mismatch, or missing
> cumulative-release registry is a release HOLD.

Validity range:

- valid only for schema version 1 packages described in `YUI_RELEASE_LINTER_20260814.md`;
- valid only for aggregate-only packages, not per-object releases;
- valid only as an engineering release gate, not legal advice, publication authority, freeze, or
  acceptance;
- valid only if run on the complete cumulative package context, not an isolated directory.

The delivered linter satisfies the implementation side of BS-11. The preregistration does not yet
fill the slot; it says `BS-11 (NEW) | OPEN`.

## 3. Future/Cumulative Release Policy

**Blocking repair.**

Yui's limits document correctly says the linter cannot see outside or future releases and therefore
needs a stateful external release-history registry. The preregistration says the linter runs over
the "complete package" and applies F-10 cumulatively, but it does not clearly bind the future policy:

> every future release must be linted against the cumulative published set, never in isolation.

This cannot live only in `YUI_RELEASE_LINTER_20260814.md`. It must be in F-10.f or BS-11 because it
governs future publication behavior. Otherwise a later release can pass the linter in isolation and
still create a differencing or reconstruction channel across versions.

Required preregistration sentence:

> Every future public release, correction, supplement, figure-data package, video data appendix, or
> replacement package must be linted against the cumulative release-history registry for this study,
> including all prior and concurrent public artifacts; an isolated-package ACCEPT is insufficient
> for publication.

## 4. False Manifest And Freeze-Attestation Limits

**Blocking repair.**

The linter honestly says it cannot detect deliberately false manifest semantics and cannot know
whether freeze attestations were true when made. Those are not just machine limits; they are human
custody responsibilities.

The preregistration should assign them explicitly:

- **release steward / custody seat:** verifies the manifest truth against the actual files and
  release intent before running the linter;
- **freeze steward / custody seat:** verifies and records that schema/cell freeze attestations were
  true before any real-sky statistic;
- **science/claim seat:** verifies that accepted files do not make scientific or legal claims beyond
  the manifest and linter scope.

Without that assignment, the document risks laundering semantic truth through a tool that only
checks declarations and parseable bytes.

## 5. ACCEPT Semantics

**Needs one preregistration sentence, but the linter report itself is honest.**

Yui states the correct meaning:

> ACCEPT means no implemented deterministic release rule fired on this exact hash-pinned package.

The preregistration currently says the linter "rejects" listed violation classes and that hand
judgment does not substitute. It does not explicitly overclaim ACCEPT as licensed, safe, frozen, or
accepted, but it also does not carry the honest ACCEPT semantics in the preregistration itself.

Required sentence:

> Linter ACCEPT means only that no implemented deterministic release rule fired on the exact
> hash-pinned cumulative package supplied to it; it is not a licence determination, a proof against
> every reconstruction attack, a freeze, publication approval, or Duho acceptance.

## 6. Does The Linter Actually Cover The Intended Classes?

**Yes, for a deterministic engineering linter.**

The implemented rules and tests cover the requested concrete hazard classes:

- row identifiers, coordinates, URLs, per-object derived columns, disguised object tables, embedded
  object records;
- dynamic interfaces, non-frozen package/table attestations, unlisted files, bad hashes, symlinked
  manifest;
- unsupported quantities, survey-attribute re-tabulations, suspicious payload names, JSON-like
  values in scalar columns;
- related aggregate cell systems, refinement attacks, cumulative cell-budget overflow;
- source-image route declarations;
- masked low-k behavior and unmasked `k < 50`.

This is not a proof of non-reconstructability in the mathematical sense. It is a concrete,
fail-closed release-control tool with documented limits. That is sufficient for BS-11 if the
human/cumulative responsibilities above are bound in the preregistration.

## 7. What Still Blocks Freeze?

Freeze is blocked by three nameable text repairs:

1. Fill BS-11 in the binding-slot table instead of leaving it OPEN, using the pinned linter hashes,
   self-test result, unit-test result, validity range, and failure rule.
2. Add the cumulative-release-history policy to F-10.f or BS-11: every future release is linted
   against the cumulative published set, never in isolation.
3. Add named custody responsibilities for manifest truth and historical freeze-attestation truth,
   plus the honest linter ACCEPT semantics.

After those repairs, I see no remaining substantive blocker to freezing the preregistration
candidate. The repairs are wording/assembly repairs, but they are blocking because they define how
publication is controlled later.

## Plain Answer For Duho

The redesigned aggregate-only preregistration is now basically there, and the linter is real. I
would not freeze these exact bytes because the document still says BS-11 is open and leaves future
cumulative-release enforcement in the linter report rather than in the preregistration. Fix those
three sentences/rows, then this can return for final exact-hash confirmation.

No run, result, publication, freeze, acceptance, commit, or push follows from this gate.
