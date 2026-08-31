# STAGE-V2 VERIFY (AGY) — Round 2 — 2026-09-01

**Narrow pass on codex's `bs2k_stage_v2.py` repaired regions (R1, R2, R3).**

The repairs successfully integrate the real API path, dynamically extract the archive identity, and parse the X2 tokens. The required 12/12 and 9/9 fixture counts pass. However, critical new defects were introduced in these exact repaired regions.

### Findings

1. **R1: Mediator Boundary Test Bypassed (False Positive)**
   In `boundary_test.py`, the boundary test attempts to trigger the non-mediated request refusal by passing `"../.boundary-probe"` to `stage.mediator_read()`. This triggers a refusal due to the `".." ` lexical path traversal check, NOT because it represents an unallowed raw store root. The test fails to genuinely verify that unallowed roots are rejected.
2. **R1: Symlink Traversal Vulnerability**
   In `bs2k_stage_v2.py`, `mediator_read()` relies on a naive lexical check (`".." in Path(relative).parts`) to prevent path traversal. It does not resolve symlinks in the `relative` path. If an attacker passes a symlink pointing outside the store, `(root / relative).read_bytes()` will blindly follow it, breaching the isolation boundary.
3. **R2: Archive Identity Fails Open on Missing Pin**
   In `archive_identity()`, if `v9_literal("PINNED_PARENT_RECEIPTS_SHA256")` returns `None` (e.g., if the constant is removed from the v9 script), the code silently skips the drift check (`if pinned_digest is not None...`). This fails open, allowing a tampered `v9` script to completely bypass the archive identity pinning.
4. **R2: Shallow AST Parser Mismatch**
   The `v9_literal()` parser only inspects `tree.body` at the absolute top-level of the AST, ignoring assignments in nested blocks. Crucially, it returns the *first* matching assignment it encounters, completely mismatching Python's runtime execution semantics which use the *last* assignment.
5. **R3: Self-Referential Integrity Bypass**
   In `x2_material()`, the script validates the extracted tokens against the stated digest *within the same markdown file*. However, it never pins or validates the cryptographic hash of the markdown file itself (`x2_commit_digest`). An attacker can modify both the tokens and the stated digest within the markdown file to seamlessly bypass the check.

SEAT: AGY
VERSION: STAGEV2-VERIFY-V2
VERDICT: DEFECTIVE
COUNT: 5
F-lines: NONE
