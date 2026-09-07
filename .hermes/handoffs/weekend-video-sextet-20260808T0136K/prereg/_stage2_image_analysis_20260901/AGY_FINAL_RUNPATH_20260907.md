ACCESS_SHA=1c4f96fba5bae6c33154471dcaae4dd5db50df70a042a8c9226ad55eaab9e5ae

**1. BINDING CONSISTENCY**
Classification: **RESULT-INVALIDATING** (core bindings) and **EDITORIAL/HISTORICAL** (dated observations).
- `run_path.py`'s A1 pin exactly equals the final A1 file digest (`6b9ecc79210046fa4c6611953184ece75818214bf4e962e4ac2e308243616e9f`).
- CORE perfectly binds that exact same A1 file. CORE also properly binds the final `run_path.py` digest (`1c4f96fba5bae6c33154471dcaae4dd5db50df70a042a8c9226ad55eaab9e5ae`).
- Readiness (`ready_for_input_freeze = True`) derives validly from executing the consumer verification on CORE (`e9222abf13485a36017d09dbd5be4c50597478882acc773626102416f9a26710`), not from a stored or manually inserted flag.
- There are no stale pins affecting execution. The decision sheet's reference to an older CORE hash (`e32d...`) is explicitly marked as a "DATED OBSERVATION" at 19:01:19 KST. A1 explicitly notes its run_path pin is "unresolved in this fold". Dating is correctly used as the intended treatment for these historical values.

**2. THE COMPARISON ITSELF**
Classification: **RESULT-INVALIDATING**.
Everything is fully intact and stated correctly:
- Eligible population (11,837), exclusions, and the 7,283 post-exclusion population are correct.
- Exact draws (400 tuning, 200 holdout, 2,000 validation) are fixed, and shortfalls trigger a stop.
- The 96-choice tuning and winner separation remain strict, with a single holdout opening.
- The agreement statistic denominators are correct: fixed sizes for tuning (/400) and holdout (/200) with unscored counted as misses; for validation, it is the scored count $m$, with refusals excluded entirely.
- The SCORED-COUNT floors (380, 190, 1,900) correctly apply only *after* the estimator runs, never permitting smaller draws. 
- The one-further-attempt limit is clear.
Yes, the comparison this package describes would produce a completely trustworthy number.

**3. ADOPTION / APPROVAL CLAIMS**
Classification: **EDITORIAL/HISTORICAL**.
No document misstates what is ready or overclaims adoption/approval. The decision sheet correctly states "Duho has decided nothing" and "Readiness grants no run permission." A1 includes a clear "UNADOPTED DECISION TEMPLATE" and confirms this fold is "for a focused independent review, not a verdict or adoption." The refresh report also confirms "Nothing is adopted."

**4. REMAINING DEFECTS**
Classification: **RESULT-INVALIDATING**.
There is NO REMAINING RESULT-INVALIDATING DEFECT. The snapshot is consistent, the logic is sound, and all dependencies are properly reconciled.

VERDICT: SNAPSHOT-SOUND
