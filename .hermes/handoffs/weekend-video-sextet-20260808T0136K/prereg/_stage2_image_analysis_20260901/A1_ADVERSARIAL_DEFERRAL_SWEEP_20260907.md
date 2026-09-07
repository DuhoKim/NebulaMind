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

# PAIRWISE SWEEP (2026-09-07 13:03 KST; Blanc 13:03) — a ledger read row by row cannot see an interaction between rows
The two fatal losses were survivable alone and fatal together. That is a property of the FORM, so the deferred column is now swept in PAIRS. Seven deferred rows → 21 pairs, all recorded, nulls included, because a recorded null is what makes this evidence.
D1 per-entry publication / chained seals / blob-equality / ancestry (beyond one push per attempt) · D2 composed provenance mode · D3 NSD / precedence / input-boundary apparatus · D4 the 132 controls, table verification and fail-first kit as run gates · D5 `verify_split` · D6 holdout flag machinery, seal-append helper, step 2 orchestration · D7 legacy builders/driver, CORPUS-IDENTITY-2 / BEACON-RECORD-3 schemas, NIST collector and PKI probes

| pair | if BOTH are absent, what can someone who wants a particular answer do? |
|---|---|
| **D1+D5** | **ATTACK FOUND.** Anchor a manifest, then swap an input file afterwards and pass the NEW digest to the selection call. Every local check agrees with itself; the anchor only proves that SOME digest existed early, not that THIS run used it, and no independent re-derivation of the split exists to contradict it. |
| **D1+D4** | **ATTACK FOUND (same guarantee, other half).** With no control gates and no published per-attempt content, the drawn id lists exist only in our copy: claim ids that do not follow from the seed and nothing an outsider holds can contradict them. |
| D1+D2 | NO ATTACK FOUND — composed provenance re-checks evidence paths that this run does not use; the anchor covers ordering. |
| D1+D3 | NO ATTACK FOUND — D3 hardens a loader against hostile evidence; inputs here are fixed local files checked by digest on read. |
| D1+D6 | NO ATTACK FOUND — the holdout-opening evidence is the anchored attempt record, which is now essential; the flag machinery adds nothing an outsider can check. |
| D1+D7 | NO ATTACK FOUND — legacy schemas and removed NIST tooling bear on formats and a source this run does not use. |
| D2+D3 | NO ATTACK FOUND — both defend against adversarial evidence; the inputs are ours and pinned. |
| D2+D4 | NO ATTACK FOUND — neither bears on when inputs were fixed, who saw what, or how many attempts are visible. |
| D2+D5 | NO ATTACK FOUND — re-derivation by an outsider replaces both, given the anchored content required below. |
| D2+D6, D2+D7 | NO ATTACK FOUND. |
| D3+D4 | NO ATTACK FOUND — instrument hardening on both sides; the number's meaning does not rest on either. |
| D3+D5, D3+D6, D3+D7 | NO ATTACK FOUND. |
| **D4+D5** | **ATTACK FOUND, contained.** A biased or broken ordering would go uncaught by gates AND unverified by a second checker — BUT only if the drawn ids and the seed are not published; with the anchored content required below, any outsider re-runs the deterministic selection and compares. Contained, not eliminated: it depends on that content being anchored. |
| D4+D6, D4+D7, D5+D6, D5+D7, D6+D7 | NO ATTACK FOUND. |
| **triple D1+D4+D5** | The same shape as the pairs above: nobody re-derives anything and nothing published contradicts us. Same single mitigation. |

## WHAT THE PAIRWISE SWEEP ADDS — two requirements on the ANCHOR'S CONTENT, no new machinery
1. **THE ANCHORED MANIFEST IS THE AUTHORITY.** The run and its record must be checkable against the digest that was PUBLISHED at anchor time, not against a local copy of the manifest. A reviewer reads the anchor, then the run record, and compares. Without this, anchoring proves only that some manifest existed early.
2. **EACH ANCHORED RECORD MUST CARRY ENOUGH TO RE-DERIVE**: the seed and its round, the digests of the three input files, the digest of `select_sample.py`, and **the digest of the drawn id lists**. Then any outsider re-runs the deterministic selection and compares — which is what makes D4 and D5 safe to defer.
Both are content requirements on records we already publish. Neither restores chained seals, per-entry publication of everything, composed provenance or the control gates: the deferred column stands as it is.
