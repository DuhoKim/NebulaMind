REISSUED 2026-09-07 12:22:15 KST — supersedes the decision sheet now in Duho's hands.

The proposed run produces one number: machine–human GZ1 chirality agreement on unseen images, allowing one overall sign reversal, with an uncertainty interval whose lower end must exceed 0.70.

**Why the row moved:** without an outside timestamp, whoever prepares the sample could look at the seed first and quietly retry until the split looks good. The same person could open the test set, dislike the answer, and try again without it showing.

| SAFEGUARDS ESSENTIAL TO THE COMPARISON | MACHINERY THAT CAN BE REMOVED OR DEFERRED |
|---|---|
| Fixed eligible list, coverage rules and file fingerprints — defines the population. | Repeated coverage tests and failed-ID extraction; keep origins and fingerprints. |
| Repeatable seed-to-order selection — makes the sample reproducible. | Old builders/driver, record formats and split-check helper. |
| Future public drand seed — prevents choosing a known seed. | NIST source, authentication and 24-hour fallback wait. |
| Separate tuning, holdout and fresh sets; freeze the winner — prevents test-driven changes. | Holdout flag, seal-append helper and step 2 orchestration. |
| Exclude 2,644 seen and 2,000 failed identities — keeps evaluation unseen. | Additional publication witnesses and per-entry publication machinery, history chains, receipts and combined evidence checks. |
| An outside timestamp for the manifest and for every attempt — exposes quiet retries. | Chained seals, blob-equality and origin/ancestry checks beyond these minimal anchors. |
| Fixed 2,000 draw, 1,900 scored minimum and interval bar — fixes the passing rule. | Adversarial evidence-loader checks; keep file validity checks. |
| Record and push every draw, abort, redraw and holdout opening — exposes missing attempts. | 132 controls, table checks and fail-first package as run gates; keep six selection checks. |
| Fixed measurement/search and protected fresh-image access — keeps the result independent. | Repeated review rounds; A1 proposes one independent review. |

1. Settle A1's remaining open questions, complete its independent review and obtain the separate owner decision before any draw or opening.
2. Fix the eligible file, exclusions, method, code and fingerprints; commit the manifest.
3. Anchor the manifest: a pushed commit whose server-side timestamp a third party records, OR a digest statement by someone other than the lane owner. Record which was used and keep the reference and outside timestamp.
4. Name and record the first drand round at least **ten minutes after that anchor**, before it occurs; a missed deadline stops. Verify its signature and agreement from two hosts; select 400 tuning, 200 holdout and 2,000 fresh images, saving lists before access.
5. Push every attempt record when it happens, one push per attempt, and use the same anchor rule and evidence as the manifest; a missing record leaves a visible hole. Record, push and anchor the holdout opening before access.
6. Tune the fixed 96 choices (380 scored minimum), freeze the winner, open holdout once (190 scored minimum; interval lower end > 0.70), only after it passes, evaluate protected fresh images once. Only one further validation attempt; report agreement, interval, failures and unscored counts without replacement or retry.

Deferred means out of scope for this run, not deleted and not disproved. Its records remain; safeguards beyond the minimal anchors remain deferred.
