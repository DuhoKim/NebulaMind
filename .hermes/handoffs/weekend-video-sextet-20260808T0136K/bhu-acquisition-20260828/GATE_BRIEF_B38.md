# GATE BRIEF — B38, acquisitions batch (entries 15, 17, 20, 28)

Fresh context, adversarial. `b38_acquisitions_batch.py` (4/4). Four papers newly acquired (arXiv
API searched by exact title — no ids from memory), pinned with title checks, screened (none flags),
and adjudicated under the b28 rule. **Re-read all four; default to disagreeing** — my solo miss
rate is 2-of-11 (B29) plus 2-of-9 (B37).

Sources in `../bhu-reading-20260823/sources/`: 15 → `hep-th_0103019_clean.txt`;
17 → `1909.07129_clean.txt`; 20 → `gr-qc_0611022_clean.txt`; 28 → `2411.14673_clean.txt`.

## MY VERDICTS — ALL FOUR NOT-OBSTRUCTION
Reasons in b38's docstring. Entry 20 additionally CITES a charged-solution impossibility owned by
its ref [16] — recorded under ownership-of-proof, tier untouched.

## ATTACK
1. **Entry 20 is the risky one.** A solutions catalogue can hide owned theorems: check whether any
   of its structural results ("a regular centre can only be located in an R region"; horizon-count
   constraints) is *derived in this paper* over a stated class rather than cited or classificatory.
   Also identify ref [16] — if it is a corpus entry, say which; if not, it is an acquisition lead.
2. **Entry 17's matching claim** — "the effective matter content on the boundary allows for the
   matching" — is the inverse of entry 5's result. Does the paper *prove* the matching requires the
   boundary tensor (an exclusion of smooth matching, entry-5 shape), or assume it?
3. **Entries 15 and 28**: full reads; both were cleared partly on closings.
4. **The identity checks**: re-verify each file is the paper its entry names (b27's false-match
   lesson).
5. Predicate audit.

## VERDICT
One token: `ACQ_CONFIRMED` / `ACQ_REFUTED_<what>` / `ACQ_NARROWED_<what>`.
Write to `<C or A>GATE_B38_VERDICT.md` here. List which papers you read in full.
