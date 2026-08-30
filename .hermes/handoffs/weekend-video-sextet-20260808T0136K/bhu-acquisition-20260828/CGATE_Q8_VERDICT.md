Q8_NARROWED_B41_PRINTS_WRONG_DENOMINATOR_AND_CLOSURE_MISSTATES_CHANGE_COUNT

# CGATE Q8 verdict

The substantive ruling is sound: entry 48 should remain `THEORETICAL-OBSTRUCTION`. The implementation needs a narrow but mandatory repair because B41's displayed miss-rate denominator contradicts its own frame calculation, and the closure/commit claim that five battery scripts moved is false. I also narrow the stated revert cost, which omits the tally and battery edits that a reversion would require.

I read the Q8 brief, both B45 gate verdicts, the live entry-48 record, the question-8 closure and archive, commit `4a5683e49`, and every script actually changed by that commit. I reran the changed battery scripts and independently parsed all Testability markers.

## 1. Ruling and preprint status

I would not have held entry 48 at an unclassified `READ` state merely because the held artifact is the MIT preprint rather than the PLB version of record.

Under this corpus's adopted rule, the relevant questions are proof ownership and operative contribution. Both are unusually clear here:

- Farhi and Guth do not merely cite Penrose. They construct the anti-trapped surface, compute the two null expansions, state the null-convergence condition, and verify the theorem's hypotheses for the specified laboratory class.
- The class exclusion is the paper's title, abstract claim, and central Section II result.
- Both B45 seats independently confirmed the derivation after full visual reads of the six-sheet scan. CGATE's two narrowings concerned a stale record sentence and the exact spherical-symmetry proviso, not the existence or ownership of the theorem. Those repairs are now present in entry 48.

A source-identical version-of-record comparison would be preferable, but absence of that comparison is an evidence-strength caveat, not a reason to pretend the held primary author manuscript is unread or incapable of supporting classification. The live record prominently identifies the artifact as a preprint, limits the theorem correctly, and promises reconsideration if the VoR materially differs. Option A is therefore the proportionate ruling.

The revisit clause should be understood as a control, not proof that content identity is already established. A later material difference could change the record or tier.

## 2. B41 frame-scoping

The conceptual frame-scoping is honest if—and only if—the result is always labelled as a historical metric for the closed readable-39 census. Entry 48 was outside that frozen frame and outside the screen's source pool. It cannot retroactively be a hit or miss in that experiment. Intersecting the current obstruction labels with the frozen `READABLE` set is therefore correct for reproducing the closed-frame result:

- obstruction labels in the frozen frame: `{5, 22}`;
- screen hit: `{22}`;
- screen miss: `{5}`;
- historical paper-tier miss rate: `1 of 2`;
- historical precision: `1 of 3` flags.

The script's disclosure is unusually explicit that entry 48 is outside the frame and the screen pool. That part does not conceal a new miss.

However, the implementation contains a direct reporting bug. The code correctly defines:

`obs_frame = obs & READABLE`

and calculates `hits` and `missed` from `obs_frame`, but prints:

`len(missed) of len(obs)`

where `obs` is the corpus-wide current set `{5, 22, 48}`. Running the script therefore prints:

`PAPER-TIER miss rate on the receipted census : 1 of 3 (hit [22], missed [5])`

and then immediately passes a predicate labelled:

`miss rate 1 of 2`.

That is internally contradictory. The displayed denominator must be `len(obs_frame)`, not `len(obs)`. The script's `14/14` green result fails to catch its own false output because the final predicate checks `hits` and `missed` but never checks the printed denominator.

After repair, any use outside B41 must call this the **closed readable-39 frame miss rate**, not the present corpus-wide miss rate. No current corpus-wide rate is measured unless the screen pool and evaluation frame are deliberately extended to include entry 48 and any other post-census reads.

## 3. Independent tally

I parsed the first machine Testability marker from every numbered entry before `## Ranked:`. There are 58 numbered records: 51 BHU papers with markers and seven support-role entries without markers (`29, 30, 32, 33, 34, 35, 58`). The 51 markers are:

- 4 `CALIBRATED-FALSIFIER`;
- 7 `QUALITATIVE-DIRECTIONAL`;
- 3 `PROSPECT`;
- 32 `CONSISTENCY-ONLY`;
- 3 `THEORETICAL-OBSTRUCTION`: entries `5, 22, 48`;
- 2 `UNREAD`: entries `42, 47`.

The sum is `4 + 7 + 3 + 32 + 3 + 2 = 51`. The headline tally and named obstruction/unread sets are correct.

## 4. Closure fidelity and cost

The closure is clearly non-open. The file begins `OPEN — none`, labels question 8 `CLOSED 2026-08-30`, and places the original question under an explicit `ARCHIVED` heading. A reasonable reader cannot mistake it for a pending decision.

Its substantive basis is faithful to the gate record. AGATE confirmed the read and proof; CGATE narrowed while confirming the theorem, then the two requested repairs were applied. The preprint caveat and revisit condition are present in the live entry.

Two implementation statements are inaccurate:

1. The closure and commit message say **five battery scripts** moved in the same change. `git show --stat 4a5683e49` shows four Python scripts: `b41_census_coverage.py`, `b45_entry48_fullread.py`, `b46_entry14_fullread.py`, and `b47_entry50_fullread.py`. The other changed files are the bibliography and open-questions record. There is no fifth changed battery script in that commit.
2. The closure says the cost of being wrong is “one tier edit back, plus this closure's correction.” A clean revert would also require recomputing the class tally and restoring or revising the four obstruction-set/frame assertions. The change is still small and bounded, but the stated cost omits real consistency edits.

The archived original option A says its cost was “none that I can see.” Because it is visibly archived as the pre-decision proposal, that stale estimate is historical rather than a live implementation claim. The live closure should nevertheless state the actual bounded ripple.

## 5. Predicate audit of the changed checks

Commit `4a5683e49` changed four scripts, not five. All four execute successfully in the current tree: B41 `14/14`, B45 `8/8`, B46 `8/8`, and B47 `10/10`. Their relevant changed predicates have these limits.

### B41

The parsed-state predicate correctly requires both `(obs & READABLE) == {5, 22}` and `obs == {5, 22, 48}`. The final metric predicate correctly checks `hits == [22]`, `missed == [5]`, and three frozen flags. But neither predicate binds the human-readable denominator. Thus the script can—and does—print `1 of 3` while passing a check that announces `1 of 2`. This is the load-bearing predicate failure in Q8.

The frame sets are frozen constants and receipt bindings, so B41 reproduces the historical census rather than measuring the expanded corpus. That is legitimate because it is disclosed, but the result must not be presented without the frame label.

### B45

The new tier predicate parses entry 48's marker and checks generic `question 8` and `REVISITED` strings in its block. The obstruction-set predicate independently parses all exact machine markers and correctly requires `{5, 22, 48}`. These checks establish the implemented state, not whether the ruling is justified, whether the delegation was authorized, or whether the VoR matches the preprint.

The record predicate remains a phrase-presence test. It does not semantically validate every delimitation, but it now reaches the two CGATE repairs (`secondary corroboration only` and the parent-symmetry proviso).

### B46 and B47

Their Q8 changes only update the independently parsed obstruction-set assertion from `{5,22}` to `{5,22,48}`. That is a valid consistency check, but it does not test entry 48's theorem or Q8 reasoning. B47's separate predicates concern entry 50, and B46's concern entry 14.

### Missing closure/tally predicates

None of the changed scripts checks:

- the headline six-class tally against all 51 markers;
- that the archived question is unmistakably non-open;
- the closure's claim about the number of changed battery scripts;
- the stated revert cost;
- the exact B41 denominator printed to users; or
- consistency between `1 of 2` in the passing predicate and the preceding output line.

Those omissions explain why all scripts pass despite the two concrete implementation errors.

## Required disposition

Keep entry 48 as `THEORETICAL-OBSTRUCTION` with the preprint/VoR caveat and revisit clause. Keep the independently verified class tally. Repair B41 to print `len(obs_frame)` so its disclosed historical metric is `1 of 2`, and label that metric as the closed readable-39 frame wherever repeated. Correct “five battery scripts” to “four” in the live closure (and commit-accounting prose where editable), and expand the live revert-cost sentence to include the tally and consistency predicates.
