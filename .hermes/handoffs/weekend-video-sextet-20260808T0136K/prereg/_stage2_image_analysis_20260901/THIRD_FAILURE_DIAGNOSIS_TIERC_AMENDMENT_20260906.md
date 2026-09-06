# THIRD-FAILURE DIAGNOSIS — Tier-C pipeline amendment V36 → V37 → V38, all refused by codex (agy passed all three) — 12:42 KST

**Rule engaged:** three consecutive refusals of the same amendment track. STOPPED. No V39 is drafted until Blanc releases the track (the 01:49 precedent: a narrow release for ONE completing round) or Duho rules.

## Why three rounds, honestly
Each round repaired everything the previous report named and was refused on what the repair exposed next: V36 amended the helper but not the renderer that refused zero exposure; V37 amended the renderer and found two defects INSIDE THE SIGNED V35 (integer-truncated radius; §8.14a promising a protection §8.9d never gave) plus the §2.15 cascade; V38 repaired those and was refused on (a) one unchanged V35 clause (§9B.2d) that still presents the superseded helper as live and (b) a checker blind spot for relative imports that codex bypassed in a scratch copy. The pattern: a signed 822-line document with 248 registered clauses and 77 pins cannot be amended by touching only the clauses named — every unchanged clause that *describes* a changed mechanism is a live contradiction, and the mechanical register and checker cannot see semantic ones. Codex's reports are the semantic pass; each has been correct.

## What V39 would contain (small, exact — one round if released)
1. §9B.2d: historicise the "implements r_t_main exactly … 30 at 4.0" assertion; both paths use `protected_region_v2` and its §8.14 fixture; add §9B.2d to the clause list; rebuild the register.
2. Checker v4: record `from . import name as alias` (ImportFrom with level > 0, module None) as importing `name`; regression test with codex's exact mutation (must FAIL while the real candidate passes); §2.15 sentence naming absolute and relative imports; test count corrected (31).
3. Retention: carry the two checker-v2 digests (df0ad5680011886e71c0871f28a9194a342b5539ec76fd8c45743757c6acba62; 3433fa4a99e8068ecfcaecb0f4e8e57d8e59dc81a9f241ee81eabfe94d44d95d) and name V37 as their authority; qualify "V35 is the pin authority" to files V35 actually pinned.
4. Exactness: §8.9 synchronised with §8.9d's boundary; §17.7 "recorded attestation or relay"; installation paragraph "three defect diagnostics plus the checker header and footer"; §8.17a "three executable lines (comments differ)"; a fractional-WCS regression test added to the render-chain fixture; the anchor-suite sandbox limit stated in the brief.
Nothing in this list touches the frozen predicate, the radius formula, the approval procedure or any threshold.

## What is NOT affected
Option A V18 (sampling amendment) is on a separate track: agy SIGNABLE; codex pending. V35 and V15 remain operative on paper; no identity, draw, fetch, render or pixel under any of them.
