# G4b Test DB and Cache Disposal Proposal

## Prerequisites
- Verify disposable-test provenance.
- Explicit, separate future G4b approval required.
- NO ACTION NOW.

## Exact Closed-World Scope
Test DB files count: 18.
Pytest cache directories censused: 10.
Ordinary future G4b cache scope: 2 primary-checkout directories.
Protected/worktree cache scope held for path-specific Hwao adjudication: 8 directories.

**Test DB files:**
- `test_cross_page_paper_footprint.db` (Type: -rw-r--r--, Size: 503808)
- `test_page_source_surface_fallbacks.db` (Type: -rw-r--r--, Size: 503808)
- `test_paper_profile.db` (Type: -rw-r--r--, Size: 503808)
- `test_trust_stage3c_prep.db` (Type: -rw-r--r--, Size: 540672)
- `test.db` (Type: -rw-r--r--, Size: 540672)
- `test_jury_trust_mutation.db` (Type: -rw-r--r--, Size: 503808)
- `test_promote_provisional_evidence.db` (Type: -rw-r--r--, Size: 503808)
- `test_global_paper_directory.db` (Type: -rw-r--r--, Size: 503808)
- `backend/test_cross_page_paper_footprint.db` (Type: -rw-r--r--, Size: 561152)
- `backend/test_page_source_surface_fallbacks.db` (Type: -rw-r--r--, Size: 561152)
- `backend/test_paper_profile.db` (Type: -rw-r--r--, Size: 561152)
- `backend/test_trust_debate_stance_caps.db` (Type: -rw-r--r--, Size: 503808)
- `backend/test_trust_stage3c_prep.db` (Type: -rw-r--r--, Size: 561152)
- `backend/test_pages_api_hardening.db` (Type: -rw-r--r--, Size: 561152)
- `backend/test.db` (Type: -rw-------, Size: 561152)
- `backend/test_jury_trust_mutation.db` (Type: -rw-r--r--, Size: 561152)
- `backend/test_promote_provisional_evidence.db` (Type: -rw-r--r--, Size: 561152)
- `backend/test_global_paper_directory.db` (Type: -rw-r--r--, Size: 561152)

**Ordinary future G4b cache candidates (2):**
- `.pytest_cache` (Descendants: 7, Bytes: 14973)
- `backend/.pytest_cache` (Descendants: 7, Bytes: 35990)

**Protected/worktree cache paths — HELD, not part of blanket G4b (8):**
- `.claude/worktrees/remove-newsletter-beat/backend/.pytest_cache` (Descendants: 6, Bytes: 5291)
- `.claude/worktrees/gemini-app-usage-gauge/.pytest_cache` (Descendants: 7, Bytes: 10544)
- `.claude/worktrees/gemini-app-usage-gauge/backend/.pytest_cache` (Descendants: 6, Bytes: 5291)
- `.hermes/handoffs/browser-concurrency/studio-simultaneous-web-viability-test-20260714T034720Z/.pytest_cache` (Descendants: 7, Bytes: 4386)
- `.hermes/handoffs/galaxy-evolution/mastermind/gemini-dr-revised-canary-20260712T045317Z/validator/.pytest_cache` (Descendants: 7, Bytes: 3521)
- `.hermes/handoffs/galaxy-evolution/mastermind/goru-deep-research-capture-dev-20260712T030531Z/.pytest_cache` (Descendants: 7, Bytes: 1370)
- `.hermes/handoffs/galaxy-evolution/mastermind/gemini-dr-next-phase-canary-20260712T033422Z/.pytest_cache` (Descendants: 7, Bytes: 1993)
- `.hermes/handoffs/galaxy-evolution/mastermind/gemini-dr-c1r-chip-validator-repair-20260713T010203Z/.pytest_cache` (Descendants: 7, Bytes: 1480)

These eight paths require separate, path-specific Hwao adjudication and approval lines. They must not be moved or deleted under a blanket G4b approval. The cache inside the sealed revised-canary packet is presumptively retained because that packet is immutable.

## Stop Rules (Metadata Drift/Identity)
- Action stops if any test DB file or cache directory changes identity, type, or metadata before action.
- Action stops if a proposed command includes any of the eight protected/worktree cache paths without its own path-specific Hwao adjudication and explicit approval.

## Verification
- Zero repo-local `test*.db` files.
- Zero primary-checkout actionable `.pytest_cache` dirs (`.pytest_cache`, `backend/.pytest_cache`).
- The eight held protected/worktree cache paths remain unchanged unless separately adjudicated and approved.
- No source/test deletion.
- Unchanged HEAD/branch.

## Rollback
- Quarantine manifest and restore before any later delete and dwell period.

GORU_PHASE4_G4B_PACKET_COMPLETE_20260722
