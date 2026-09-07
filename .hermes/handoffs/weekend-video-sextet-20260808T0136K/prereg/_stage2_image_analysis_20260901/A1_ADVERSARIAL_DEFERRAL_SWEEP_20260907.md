# ADVERSARIAL RE-SWEEP OF EVERY DEFERRED ROW (2026-09-07 12:21 KST; Blanc 12:19 item 3)
The reviewer found one deferred item that was load-bearing. Blanc's inference is right: one hit means the first sweep was not adversarial. So I re-asked every deferred row ONE question, in the reviewer's own form — **can a party who has seen the data still get a better number, and would anyone be able to tell?** — instead of "is this needed to compute the answer".

| deferred item | the attack, if it is deferred | verdict |
|---|---|---|
| **Third-party anchor for the manifest commit** | Backdate the local commit to a round that already exists; grind seeds until the split is favourable. Nobody can tell, because the only timestamp is ours. | **MOVED → ESSENTIAL** (the reviewer's FATAL) |
| **Anchoring of the attempts register and the holdout opening** | Every attempt is recorded in a file WE hold. Open the holdout, dislike the number, delete the entry, re-draw, report the second. The "one holdout, attempts recorded" rule is stated by the same party it constrains — exactly the hole the reviewer found in the clock, one room over. | **MOVED → ESSENTIAL** (found by this sweep) |
| Per-entry publication, chained seals, blob-equality, origin/ancestry checks | These defend against a hostile party rewriting a long published history. Our history is one manifest and a handful of attempt records; anchoring those covers it. | stays deferred |
| Composed provenance mode; NSD / precedence / input-boundary apparatus | Hardens a loader against adversarial EVIDENCE. This run's inputs are fixed files with digests, checked on read. | stays deferred |
| The 132 differential controls, table verification, fail-first kit AS RUN GATES | They gate the selection INSTRUMENT's refusal behaviour, not the number. The six selection checks stay. | stays deferred |
| `verify_split` | Reproducibility is essential, but it is already had: the selection is deterministic from a recorded seed and anyone can re-run it. This was a second checker of the same fact. | stays deferred |
| Holdout FLAG machinery, seal-append helper, step 2 orchestration | The RULE (open once) is essential and stays; the machinery is not, and its evidence is now the anchored attempts record. | stays deferred |
| Legacy builders/driver, CORPUS-IDENTITY-2 / BEACON-RECORD-3 schemas, NIST collector and PKI probes | Removed sources and superseded formats; nothing about the agreement number depends on them. | stays deferred |

## THE MINIMAL SUFFICIENT ANCHOR — the cheapest mechanism that closes both holes
The requirement is only: **something not under my control fixes a digest at a time verifiably before the named drand round exists.** Not chained seals; a timestamp problem gets a timestamp answer. Either of these suffices, and the run records which was used:
- **(a) A pushed commit.** The manifest commit is pushed to the public remote; the remote's server records the push time. One read of that server-side timestamp is the evidence — no per-entry publication, no receipts, no history chain.
- **(b) An external statement of the digest.** The manifest digest is stated in the chat channel by someone who is not the lane owner (the convention already used for signing), whose provider timestamps it.
Precision needed is coarse: rounds are 30 s apart and the margin is 10 minutes, so a push or message timestamp is ample. **The same anchor covers the attempts register**: each attempt record — draw, abort, re-draw, holdout opening — is pushed when it happens, so a deleted attempt leaves a hole an outsider can see. That is per-entry publication reduced to its load-bearing minimum: one push per attempt, nothing chained.
