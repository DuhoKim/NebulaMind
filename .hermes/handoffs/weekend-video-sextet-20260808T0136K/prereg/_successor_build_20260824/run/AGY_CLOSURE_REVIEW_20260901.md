The judgment is SOUND.

1. `local_pass` evaluates theoretical retention prior to fetch using `floor(0.8572 × n_raw)`, while the post-cut mask is evaluated on actual rows after the BS-2a quality cut. Bricks that lose all rows to the cut naturally fall out of the mask. Therefore, `local_pass` output was indeed never supposed to equal the post-cut mask, and `stagep_rerun.py`'s `got_ids == want_ids` check is an over-strict constraint. 

2. The two-query structure does not threaten any frozen requirement. It is explicitly mandated by the BS-2c oracle requirements: "counting is server-side, row payloads are never fetched for counting". 

3. The 476142 discrepancy (predicate/epoch drift between queries) does not threaten any frozen requirement. The counting path and the fetch are decoupled by design, and the exactness of the test is preserved because the mandatory Stage-P re-pass explicitly evaluates against the final, authenticated post-exclusion mask.

SEAT: AGY
VERSION: CLOSURE-REVIEW-V1
VERDICT: SOUND
COUNT: 0
F-lines: NONE
