Q1_ANSWER_REFUTED_COUNT_AND_REASONING

I have reviewed the Question 1 answer script (`b26_answer_q1.py`) and the corresponding logic in the record.

**1. The 18-Unpinned Count: REFUTED (REGEX BUG)**
The true number of unpinned entries is 19, not 18. Tori's parser uses an unanchored regex (`\d{1,2}`) on the first column of the map file. While this works for the main table, it completely fails on the correction table at the bottom, where the first column is the filename `1111.1017_clean.txt`. The regex extracts the "17" from the end of the filename and falsely registers Entry 17 as pinned. Entry 17 is missing.

**2. Claim 3 (Precision is irrelevant if hand-checked): REFUTED (TOO CLEVER)**
Tori argues that a verified screen is safe at any precision because checking every flag prevents misfiling. This ignores the fundamental economics of screening. If a screen has terrible precision (e.g., flagging 30 out of 33 papers), "checking every flag" means you are doing exactly the same amount of work as hand-reading the whole pool, but with the added overhead of running the screen. Low precision floods the reviewer, causing fatigue and negating the entire purpose of the screen.

**3. Claim 4 (Recall cannot be measured): REFUTED**
Tori claims recall cannot be measured because there is only one known obstruction. This is false. You can measure (or tightly estimate) recall by simply hand-auditing a random sample of the 30 *unflagged* papers. If none of the unflagged sample papers are obstructions, recall is demonstrably high. If the sample reveals missed obstructions, recall is poor. Checking the negative pile is standard practice; claiming it "cannot be measured" is an abdication.

**4. Claim 5 (The work is already done): CONFIRMED**
The 3 flagged corpus entries (22, 25, 6) have indeed been read by seats during previous gates. Entry 25 and 6 were correctly identified as false positives, and no tiers were incorrectly moved.

**5. The Reframe: REFUTED (EVASION)**
Answering a procedural question ("how should we sort?") by pointing to a logistical bottleneck ("we haven't downloaded them all yet") is an evasion. The remaining 33 papers still need sorting, and the missing 19 will need sorting once acquired. The decision is still required, and Tori dodged it.
