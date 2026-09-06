ACCESS_SHA=af7fa5408c51e292bde508a63c21bd511b8d0c9a3b56d41211f739b597913b91

AUTHORSHIP: beacon_v2/ and the builder boundary are Hwao's; codex authored the earlier builder field-validation code.

THE PROPERTY, judged first:
§3b's claim that the source decision is f(archived public bytes for T_pulse, pinned root) and is recomputable holds true. The input to the decision is fixed and checkable once published, without trusting the lane. The time of collection changes only availability (returns RETRY when before T_pulse), but it does not change the verdict or the seed. The exhibit (`exhibit_property.py`) actually exhibits this property by reproducing identical verdicts and seeds at two different clock times, returning identical outputs on both a synthetic record and the real filed RETRY record, outputting matching digests. The limits L1-L5 are completely and honestly stated.

THE FIVE HARD CONSTRAINTS — MET:
- C1 (public 00:15Z pulse excluded by name): MET. Clause §3b (1a), Code: `beacon_record_expedited.py:37,51,80` (`EXCLUDED_T_PULSE = ("2026-09-06T00:15:00Z",)`).
- C2 (same formula from the new approval time): MET. Clause §3b (2), Code: `beacon_record_expedited.py:40-43` (`DELAY_S = 600`).
- C3 (V15 and RETRY preserved, prospective supersession): MET. Clause §0 ("V15 REMAINS OPERATIVE... The signed V15 is here unchanged with its signature record and RETRY beacon record").
- C4 (the cost stated): MET. Clause §10 ("Costs, total: 600 development objects...").
- C5 (a reader can SEE approval before seed): MET. Clause §3b (1a) (W3, W5), Code: `approval_witness_v3.py:53,80,87`.

1. ACCEPTANCE SET under V19: [MINOR] 
There are no paths to ACCEPT other than (a) authenticable NIST for T_pulse with live equality, or (b) >=2 pinned relays agreeing retained+live for round_for(T_pulse) with the served, live-equal, T_pulse-timestamped NIST pulse failing authentication. The `nist_ok` check strictly enforces `live_ok`. This is fully guarded by the witness v3 check, the committed adoption check at the approval commit in `build_corpus_identity_v19.py`, and the complete committed driver-verified history.

2. REPAIR AUDIT of every V18 finding:
- wrong-time pulse -> RETRY: REPAIRED in `beacon_record_expedited.py`.
- late writer -> refused by server time: REPAIRED in `approval_witness_v3.py`.
- HTTP 404/500 -> RETRY: REPAIRED in `beacon_record_expedited.py`.
- simulated NIST recovery after a first ACCEPT -> COLLECTION-LOCKED: REPAIRED in `build_corpus_identity_v19.py`.
- driver with a RETRY-outcome identity -> refused: REPAIRED in `run_configurations_v3.py`.
- adoption file committed after the approval commit -> refused: REPAIRED in `build_corpus_identity_v19.py`.

3. DIFF CONFINEMENT V15->V19 and sentences of §3b/§3c/§7 vs executed behaviour:
Everything executed aligns precisely with the document's sentences. No unexpected diffs.

4. Test counts and file names in text TRUE:
All run counts strictly match the text: 37 for beacon_v2 (18+19), 18 for corpus_identity (9+5+4), 37 for fourier_chirality (20+17), negative probes 23. All pinned hashes reproduce perfectly.

5. The inherited V15 defect: disclosure exact?
Yes, the disclosure is exact and present in §0.

6. Anything aspirational or unexecuted?
Nothing is aspirational. All statements are mechanised and tested.

7. WHAT IS STILL MISSING for a pre-commitment approval:
Nothing is missing. 

VERDICT: SIGNABLE-AS-PRECOMMITMENT
