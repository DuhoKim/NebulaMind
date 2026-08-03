# Account-safe manuscript work — Tasks 1 and 2 complete

Generated: 2026-07-15 08:52 KST

Status: `ACCOUNT_SAFE_LOCAL_WORK_COMPLETE`

## Safety boundary

This run used local file reads/writes, local validation, and local Tectonic compilation only. It made no Deep Research request, browser or account action, broker query/reset/write, database/wiki/trust/deploy/publish action, or git commit/push. The frozen broker was left untouched. Papers 03–08 DR review and all further DR remain held for the separate account and a fresh Duho gate.

## Task 1 — round-2 reviewed papers

| Paper | Writer | Round-2 TeX SHA-256 | Exact measured numeric lines checked | Validation | Tectonic |
|---|---|---|---:|---|---|
| 01 | Tori | `7bd0890dfc31ea9411fa23b959f74433f0dc649a2c3a4894e68a52e89a79fac7` | 21 | PASS | clean, 4 pages |
| 02 | Tori | `9eebccae4a7f89e1a86c866e9af7eea3830ee9ddebc3f9194f9a3a9d1ff7cd4c` | 18 | PASS | clean, 3 pages |
| 09 | WonE; Tori integration review | `c970abdc99a34705758dd852515ecc99e0c0867809a98fb08ca5396e495e7df1` | 16 | PASS | clean, 3 pages |

### Paper 01

- Tightened the abstract, matched-offset figure caption, literature section, and conclusion.
- Added review-verified, bounded uses of Zibetti et al. (2026), de Mellos et al. (2024), and Gatto et al. (2025).
- Did not adopt the review's overstrong claim that the catalog offset is proven to be an artifact; the revision states estimator dependence and preserves uncertainty about the physical explanation.

### Paper 02

- Defined the reported quenched fraction as an emission-line-denominator catalog fraction, not a total-population fraction.
- Removed the claim that fibre-collision caveats do not affect the high/low comparison.
- Added bounded citations for the Goubert correction, Nandi & Pandey, O'Kane et al., and Sampaio et al.
- Did not adopt the unsupported lower-limit direction or the speculative Atalebe terminology.

### Paper 09

- Corrected the unusable Nanni et al. `MNRAS, 518, 2605` mapping to verified iMaNGA Paper II: `MNRAS, 522, 5479`.
- Added Hirschmann et al. (2023) and Vijayan et al. (2023) for nebular-emission and dust/geometry forward-modelling requirements.
- Skipped the unsettled Gawade preprint.
- Replaced the inherited generic RP-1 conclusion with a paper-09-specific, selection-conditional forward-modelling conclusion.

Round-2 validation found zero undefined citations, zero duplicate bibliography keys, balanced braces/environments, matching source/review/output hashes, and exact preservation of all checked measured numeric lines.

## Task 2 — all nine round-1 drafts

`tools/ge_tex_publishability_lint.py` scanned all nine files.

- Citation-specific lint errors: **0** (`missing_bibitem_count = 0`).
- Tectonic builds: **9/9 clean**.
- Undefined citation warnings: **0**.
- Undefined reference warnings: **0**.
- Every round-1 source SHA remained unchanged after compilation.

| Paper | Build | Pages | PDF SHA-256 |
|---|---|---:|---|
| 01 | clean | 4 | `294dc0f3153a13c096144b2b32b8756ddd3e3fa3d0db1ca1bc79a1021e4975fb` |
| 02 | clean | 3 | `19d3b6ca54e0601f4ee597ac8f5401ec9d3ad2d272da27f681d021d3e9e31b69` |
| 03 | clean | 3 | `fa00895b818a9e5e4b71cd6cff661fe3f75213c0b5b83589a27cedd47843bbea` |
| 04 | clean | 3 | `9e7c7daa43b5b7541c03b360ab1faf0aeb96df83f738b5bd7b93de20ecdab391` |
| 05 | clean | 3 | `5b653490848f874dba67713e2659cc4c35df6e74498d05d941f736095459fd36` |
| 06 | clean | 3 | `c409947d656ac5b16b00c39bbd36fbd820b7364db24a49891e64247f37a8194b` |
| 07 | clean | 3 | `c6c729491541805e01ea5466687f9023b75abe29396b8c8ef5c9282ce8205d7e` |
| 08 | clean | 3 | `1153f1aee332cf49b05a35479b984550343ba86ea02f8c20ce96d7d0cf296ac9` |
| 09 | clean | 3 | `7499ae3597522018f1453353dfaf7bf3a2b2d78bed96f81d082137a948477659` |

The linter still reports 18 inherited, non-citation publishability errors: nine `aastex631`-versus-`aastex702` class findings and nine workflow-phrase findings (`No public page`). It also reports 81 inherited warnings: 43 unused bibliography items, 29 flat `>=`/`<=` operators, and nine empty bibliography-width arguments. These existed in the banked manuscript base and were not introduced by the DR citation additions. Under the requested scope, the banked round-1 TeX was not rewritten for those packaging/style issues.

## Durable receipts

- `round2/receipts/ROUND2_VALIDATION.json`
- `round2/receipts/ROUND2_TECTONIC_BUILDS.json`
- `round2/receipts/ROUND2_PUBLISHABILITY_LINT.json`
- `round1/receipts/ROUND1_VALIDATION.json`
- `round1/receipts/ROUND1_TECTONIC_BUILDS.json`
- `round1/receipts/ROUND1_PUBLISHABILITY_LINT.json`
- Per-paper round-2 source and revision receipts under `round2/receipts/`.

No next DR action is active.
