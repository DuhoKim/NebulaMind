# FINDING — limb B could not hold the corpus: seat B died without a report (2026-09-06 14:06 KST; Blanc's 14:05 KST note)

**What died.** Seat B of the 10:14:56 KST dispatch (kimi-k3 via moonshot, kernel-sandboxed, working directory with the 89 pinned
texts flat; pid 31872), the limb-B seat of the run that had already been voided by the 10:17 design abort. It ran for about 3 h 45 min
and was gone by ~14:01 KST. **No `SEAT_REPORT.md` was written and nothing was filed as a result; nothing from it enters any tally.** CORRECTION (14:07 KST, from the
archived tree's listing, not from reading the files): the seat DID write `candidates.json` (1.5 MB), `exclusions.json` (211 KB) and
`ledger.json` (2.4 MB) at 13:24 KST, a 7 MB numeral index at 10:18, and about fifty helper scripts (`_seat_*.py`, `_frag11_*`) between
10:16 and 13:43 — it reached limb A's enumeration and was building and repairing the input ledger, and had begun attempting arithmetic
(`_seat_attempt.py`, 13:34), when a later pass that re-read texts "COMPLETELY" in sets exhausted the session. These artefacts are void
under the 10:17 abort and stay unread; their existence is recorded because it bears on the options below. Its tree is archived unread (`/Users/duhokim/HermesOps/r3c2_run_20260906r_VOID_1017`, inventory `_tmp_VOID_20260906_1017_inventory.md`).

**The seat's own log, verbatim (`_tmp_r3c2_run_Br_kimi.stdout`):**
```
  🔀 [set 1] delegating 3 tasks
[subagent-2] ⚡ Interrupted during API call.
  ✗ [set 1 · 3/3] Extract every candidate quantitative cla  (891.84s)
[subagent-1] ⚡ Interrupted during API call.
  ✗ [set 1 · 2/3] Extract every candidate quantitative cla  (948.76s)
  ✓ [set 1 · 1/3] Extract every candidate quantitative cla  (1575.37s)
  🔀 [set 2] delegating 2 tasks
  ✓ [set 2 · 1/2] Extract candidate quantitative claims an  (1821.37s)
  ✓ [set 2 · 2/2] Extract candidate quantitative claims an  (1848.88s)
  🔀 [set 3] delegating 2 tasks
  ✓ [set 3 · 1/2] Extract candidate quantitative claims an  (1688.95s)
  ✓ [set 3 · 2/2] Extract candidate quantitative claims an  (1807.51s)
  🔀 [set 4] delegating 3 tasks
  ✓ [set 4 · 3/3] Read these 11 source files COMPLETELY (e  (1178.29s)
[subagent-0] ⚡ Interrupted during API call.
  ✗ [set 4 · 1/3] Read these 11 source files COMPLETELY (e  (1218.3s)
  ✓ [set 4 · 2/3] Read these 11 source files COMPLETELY (e  (1346.06s)
Context compression timed out without reducing this conversation. No messages were dropped. Start a fresh session with /new, or check auxiliary.compression before retrying /compress.
```

**How the seat worked, from its own log.** It did not read linearly: it delegated "Extract every candidate quantitative claim" to two or
three parallel subagents per set of texts (sets 1–3), two of which were interrupted during API calls in set 1, then in set 4 switched to
"Read these 11 source files COMPLETELY" — the pass that killed the session. So the seat itself invented a chunked, delegated reading
with no sealed intermediate state and no preregistered join; the design gave it no such structure.

**How far it got.** The seat organised the 89 texts into sets of 11 and read them "COMPLETELY" set by set; the log shows set 4's
second batch completing (1346 s) and its first batch interrupted (1218 s) during an API call, then the engine's own message that
context compression timed out without reducing the conversation and that a fresh session would be needed. Reading roughly a third to
a half of the corpus consumed the session. It never reached limb B's arithmetic.

**Is this the risk the run plan named?** Yes, exactly: "one seat session may not hold the whole corpus" was the plan's largest
uncertainty (§2 of `R3C2_RUN_PLAN_20260906.md`) and abort A4 was written for it. This seat belonged to a run already voided, so no
limb is lost; but the evidence is real and applies to any re-run.

**Would a straight re-run hit the same wall? My judgement: yes, though not necessarily at the same point.** The seat got through
enumeration by improvising subagent chunks and died on a whole-corpus re-read; a re-run might improvise differently and die elsewhere,
or produce an unrepeatable path to a report. Either way the design would be relying on an unrecorded, unpinned reading strategy the
seat made up — which is the finding. The corpus is 89 texts, 106,676 non-blank lines, several million
tokens of source text before any reasoning. No session of kimi-k3 will hold it. Seat A (codex-cli 0.153.4, gpt-6-astra) has NOT been
tested on it — both of its runs today stopped in the first two minutes on scope, before reading a source — so its capacity is
unknown, but the arithmetic of the corpus size against any advertised context window I know of says the same. The plan's A4 rule
("one fresh re-dispatch, then stop") would spend another 4 hours to learn this again. Do not re-dispatch a limb on the current design.

**The census cannot produce a result until the reading problem is solved.** The design as signed (V23) and as amended in draft
(V24h) assumes one seat, one session, reads everything and emits one candidate file. That assumption is false on the engines we have.

## Options for Duho, costed — and whether each changes the DESIGN (V23 amendment + his approval) or only the EXECUTION

| option | what it is | what it preserves / breaks | design or execution | cost |
|---|---|---|---|---|
| **A. Chunked reading, sealed intermediate state, mechanical join** | each seat reads the corpus in N sessions (e.g. 8 batches of ~11 texts, matching what the seat itself did); every session receives the SAME packet and brief plus the list of its texts, prints its own ACCESS_SHA, emits a per-batch candidate/exclusion/input ledger and report; the lane joins the batches MECHANICALLY (a pinned `join` subcommand: concatenate, renumber candidate ids by text, recompute the declared counts) and runs `census` over the union; C6 audits across the union | preserves: the §1 rule is per passage, the arithmetic per claim, origin per input — none needs memory of other texts; two engines stay independent; the join is deterministic and printed. **Breaks the sentence "one seat reads everything" and its consequence: cross-text consistency of judgement is no longer guaranteed by one memory** — a seat may classify a borderline numeral differently in batch 2 and batch 7. Mitigation: the packet is identical every session; the two-seat reconciliation and the C6 audit are already the design's answer to inconsistency | **DESIGN** — C1's single-file schema, the dispatch record (one ACCESS_SHA per session), §9's split rule and C6's frame need one amendment (V25): "a seat is a sequence of sessions under one packet; the join is mechanical and pinned" | one lane day to amend + gate (the machinery exists: `census` already recomputes counts over any file); run: 8 sessions × 2 seats × ~25 min ≈ 7 h of seat time, parallelisable per seat |
| **B. A larger-context engine** | swap seat B (and/or A) to an engine with the largest window available | does not solve it: the corpus exceeds every window we have; a larger window fails later, not never. Also changes the two-engines pin (execution) | EXECUTION only (tooling pin) — but **not a solution** | none to the design; another lost run to learn it |
| **C. Split the corpus across sessions per limb, one session per text-group, no join step** | each session files its own complete census over its subset, the study reports 8 sub-censuses | breaks "one census, one denominator": the class precedence, the 10% dispute rule and C6's sample are all defined over ONE denominator | DESIGN, and a worse one than A — it is A without the join | as A, but the result is not the preregistered object |
| **D. Mechanical pre-selection of candidate passages** | a pinned scanner (like the lane's second route) extracts numeral-bearing lines with context; seats read only those, not whole papers | reduces reading by ~10×, but §1's rule ("a numeral the paper asserts as a result of its own") needs the surrounding text to decide inclusion; a pre-filter's misses are invisible to the seats and the second route loses its independence | DESIGN — changes what a seat reads and adds a new control (scanner recall) | cheaper run, weaker census; not recommended by the lane |
| **E. Smaller corpus** | restrict the census to a preregistered subset (e.g. the 30 CONSISTENCY-ONLY entries, or the entries with a tiered claim) | keeps one-seat-one-session; changes the study's object | DESIGN and a change of question | his call entirely |

**My recommendation (judgement):** A. It is the only option that keeps the preregistered object (one census, one denominator, two
independent engines, one mechanical join, C6 over the union) and it matches what the seat spontaneously did (sets of 11). It needs a
V25 amendment of a few sentences and one C0 + gate, then his approval. B is not a fix; C and D are A minus its safeguards; E is a
different study.

**What is needed from him:** the word on A (or another option), before any limb is dispatched again.
