# Morning decision sheet — option A selection rule V15 (for Duho, via Blanc) — 2026-09-06

**Where things stand, in plain words.** The rule that says how we will pick and test the new galaxy-shape instrument, without anyone peeking at the answer first, passed both independent referees last night (V15, 02:05 KST). Fifteen drafts were written; thirteen were refused; this one cleared. Nothing has been signed, frozen, downloaded or looked at. Everything is committed and pushed. Four things are yours to decide; the lane does nothing until you do.

## 1. Sign V15, or not?
- **(a) Sign it as is.** Say in chat: `V15 signed: fdd9eedd9938c2ba7df312cdc9b82a06612772ccc087e9365b33fd7d9d9a97d1 at <UTC time>`. The lane fills the two signature lines, recomputes the preimage (stops on mismatch), and the ten-minute beacon clock starts from your UTC.
- **(b) Ask for one more check first.** Codex wrote the beacon code AND refereed the document that pins it (it disclosed this). Agy did not write any of it and also passed it. If you want a third, non-authoring referee on the code alone before signing, say so; that is one seat run, not a V16.
- **(c) Don't sign; stop option A here.** The register already records 15 drafts / 0 signed; the paper branch "what the paper says" file covers this outcome.

## 2. The custodian account
The rule requires a separate account (`nmcustody`, permissions 700) to hold the frozen sample so no working account can read it. It does not exist yet. **(a)** you create it this morning (about five minutes; steps in CUSTODY_REQUIREMENT_SEPARATE_ACCOUNT_20260905.md), or **(b)** you drop the requirement (that needs a V16, which re-opens the gate).

## 3. Branch protection on GitHub
The freeze witness relies on a pushed commit that nobody can rewrite. Only you can turn on server-side branch protection for `feat/paper-workflow-v2` (Settings → Branches → protect, disallow force-push and deletion). **(a)** do it, or **(b)** accept a weaker witness (also a V16).

## 4. The NIST beacon finding
NIST's live random-number pulses carry a 512-byte signature under a 2048-bit certificate. Under the rule as written that pulse is refused, so the rule would wait 24 hours and fall back to the drand beacon (four pinned relays, two must agree). **(a)** keep the rule as written and accept the 24-hour delay, or **(b)** amend to accept NIST despite the mismatch (a V16; the referees would have to agree the mismatch is benign), or **(c)** drop the beacon and use a simpler public seed (a V16).

## What does NOT change with any answer
No frozen pixel is looked at. The 0.70 threshold and the 1,900 floor stay. Every attempt stays on file. The pipeline fix stays a separate amendment.

**Fastest path to a run:** 1(a) + 2(a) + 3(a) + 4(a). Then the lane's first real step is the beacon read at your signing time plus ten minutes, and the fresh validation draw the day after.

Files: `V15_GATE_OUTCOME_SIGNABLE_NOT_SIGNED_20260906.md` (gate record), `OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V15_20260906.md` (the rule), `ATTEMPTS_REGISTER_20260905.md` (all fifteen attempts), `HWAO_LANE_STATE_20260905.md` (lane state).
