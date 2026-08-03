# Galaxy Evolution frontier scope correction — V5 handoff

Status: **SOURCE APPLIED · TESTED · BUILT · CANARY VERIFIED · NOT LIVE · RESTART REQUIRED**

Final receipt: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/frontier-scope-correction-20260802T154833Z/RECEIPT.json`  
Receipt SHA-256: `d160a85f4445f39cc05ec273d5f22d3d495d1803ee750520e864f7f36f7d014c`

## Result

- Broad 57-cluster GA+CO evidence corpus remains intact.
- Product scope is explicit and fail-closed: **8 core / 26 adjacent / 23 out of scope**.
- Strict core order: **41, 40, 35, 19, 56, 17, 46, 27**.
- Cluster 16 reionization/Ly-alpha PDF remains visible as **adjacent · supporting**.
- Mixed AGN, Gaia/APOGEE, stellar, transient, cosmology, and probe clusters do not enter the strict core ranking.
- The supporting measurement list is explicitly labeled **Core + adjacent**.
- No nonexistent backend study queue is claimed.

## Verification

- Focused TDD contract: PASS
- `npx tsc --noEmit`: PASS
- Isolated Next build: PASS (`aNNAOJzzSRMQDzgANAtuv`)
- Hydrated ranking canary: PASS
- Exact V5 screenshot: `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/frontier-scope-correction-20260802T154833Z/canary-ranking-v5.png`
- Independent Codex read-only review: PASS
- V5 rollback reverse-check: PASS

## Runtime boundary

Production still serves old build `lFt_UDNPmeNh2DCabbYZX`. The candidate build `aNNAOJzzSRMQDzgANAtuv` is staged and canary-tested but not swapped into the live runtime.

Fresh approval for the live build-swap/restart must be exactly:

`APPROVE GALAXY SCOPE LIVE BUILD-SWAP RESTART d160a85f4445f39cc05ec273d5f22d3d495d1803ee750520e864f7f36f7d014c`

The newer canonical worktree also accepts V5 via `git apply --check`, but no apply or Git operation occurred. Fresh approval for canonical source apply must be exactly:

`APPROVE GALAXY SCOPE CANONICAL APPLY d160a85f4445f39cc05ec273d5f22d3d495d1803ee750520e864f7f36f7d014c`

Commit/push/merge remain a later separate gate.

## Rollback custody

V5 reverse-check passed against the modified live source tree. Do not execute without a fresh rollback gate:

`git apply --reverse --check /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/frontier-scope-correction-20260802T154833Z/REVIEW_PATCH_V5.patch`
