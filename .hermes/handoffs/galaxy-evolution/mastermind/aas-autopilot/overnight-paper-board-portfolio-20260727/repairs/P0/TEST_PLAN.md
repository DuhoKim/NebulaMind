# P0 Correction Test Plan

Status: `PREPARED_ONLY_NOT_RUN`

## RED/GREEN contract

`red_test_only.patch` adds `frontend/scripts/test-p0-correction-state.mjs` and changes no production/source representation.

Expected RED against the frozen current source:

- Fails on at least the abstract’s “place all three datasets on a single” or “consistent with observations once abundance scales are matched” string.
- May also report the Lisiecki citation, dead review metadata, or stale merit-note strings.
- A syntax/import failure is not an acceptable RED; the assertion must fail for the old P0 claim state.

`green_source_only.patch` proposes only the minimal source representations needed to satisfy that contract.

Expected GREEN marker:

`P0_CORRECTION_STATE_PASS`

## Execution sequence after explicit approval

1. Recheck all four frozen source hashes from `exact_diff.json`.
2. Require `git apply --check red_test_only.patch`, `green_source_only.patch`, and `exact_diff.patch` to pass.
3. Apply RED only.
4. Run `node frontend/scripts/test-p0-correction-state.mjs`; require assertion failure on stale P0 state.
5. Apply GREEN.
6. Re-run the test; require exit 0 and the exact marker.
7. Compile TeX in an isolated temporary directory with the two pinned figure files.
8. Run `pdfinfo`, `pdftotext -layout`, and 300-dpi page renders.
9. Run `npx tsc --noEmit` from `frontend/` only after the source/test gate allows it.
10. Run the focused neighboring paper-surface tests, including `npm run test:paper-videos` and any existing Paper Board contract test discovered at apply time.
11. Run `git diff --check` over the four closed-world paths.
12. Compare applied file hashes to the proposed hashes in `exact_diff.json`.

## Fail-closed conditions

- Source authority was not explicitly repinned.
- Current source hash differs from the manifest.
- RED passes unexpectedly or fails for syntax/path reasons.
- TeX does not compile cleanly.
- Figure source hash changes.
- Rendered content clips or the PDF/text representations disagree.
- An independent reviewer requires another writable path.

No test, compile, render, TypeScript check, or build was run during packet preparation.
