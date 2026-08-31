# BS-2k CONSTANTS SHEET + ROSTERS — DECISION PACKET (proposal, 2026-08-31)

**In plain words.** You asked me to propose the two things still on your desk that
have shapes I can draft: the run's operating constants (clocks, queues, retries —
none of them touches χ or the science; they say how patient the machinery is
before it calls something a failure) and the two people-lists (who may sign human
reviews, and who holds the sealed keys). **Nothing here commits until you sign.**
Every number below is DERIVED from inequalities already frozen in the draft/spec —
the derivation is shown, so you can check the arithmetic, not trust me. Reply
"constants and rosters approved as proposed" to take the whole packet, or amend
line-by-line by ID ("C4 = 32, R1 = option B, rest as proposed").

**What signing does:** the values enter the BS-2k provisioning materials and are
frozen under your P0 signature with everything else. **What each amendment costs:**
nothing — these are proposals; changed values just have to keep satisfying the
frozen inequalities, and I will re-derive and re-present if an amendment breaks one.

---

## Part 1 — the constants (C1–C11)

All times are decimal nanoseconds on the monotonic clock, quantized to `g` (C1),
as the spec requires. "The inequality" column is the frozen constraint the value
must satisfy; every recommended value satisfies its constraints with stated margin.

| ID | constant | recommended | plain meaning | the frozen constraint |
|---|---|---|---|---|
| C1 | `g` (reading quantum) | **1,000,000 ns (1 ms)** | clock readings round to this grain | quantization + the named timing-channel bounds |
| C2 | `commit_bound` | **1,000,000,000 ns (1 s)** | a transactional commit must land or abort within this | `D > commit_bound`; staleness ≤ one `commit_bound` |
| C3 | `budget` (head processing) | **5,000,000,000 ns (5 s)** | Row B's per-request processing cap; an overrun head takes the catch-all at its turn | feeds the full-drain inequality (C6) |
| C4 | `Q` (queue bound) | **16** | the provisioned bound on serialized backlog | feeds C6 and C7 |
| C5 | `detection` | **2,000,000,000 ns (2 s)** | how fast an overdue request is noticed (poll period bound) | feeds C7 |
| C6 | `D` (decide-within deadline) | **120,000,000,000 ns (120 s)** | every request decided within this of arrival | `D > commit_bound` ✓ and `D ≥ Q·(budget + commit_bound) + commit_bound` = 16·6 s + 1 s = **97 s ≤ 120 s** ✓ (margin ≈ 24%) |
| C7 | `enforcement_lag` | **30,000,000,000 ns (30 s)** | the extra allowance for the deadline refusal itself | `≥ detection + Q·commit_bound` = 2 + 16 = **18 s ≤ 30 s** ✓ (margin ≈ 67%) |
| C8 | `GATE_PASS_BUDGET` | **10,000,000,000 ns (10 s)** | how long a verification pass may hold admission | quantized to `g`; W0 worst case = 5 gates × C9 × (C8 + 2g) ≈ **150 s** per full gate sequence — bounded and named |
| C9 | `PASS_RETRY_MAX` | **3** | consecutive failed gate passes before exhaustion | derived count from close records; a pass record resets |
| C10 | `R_max` | **2** | renders per object per member (constant multiplicity by padding) | spec: `R_max ≥ 2` — this IS the floor |
| C11 | `A_max` | **3** | closed abort pairs before a drain member is skipped and listed | pair-counted by the verifier; "cannot land after A_max attempts is the platform failing" |
| — | `M_max` | **3 (ALREADY COMMITTED)** | recurrence flag threshold | restated for completeness — no action |

**C1 — g = 1 ms.** The natural scale of OS scheduling noise: coarser would make the
±2g hold-release slack humanly visible; finer buys nothing and the spec's channel
accounting only needs g named, not minimized. The named channel widths at these
values, stated honestly per the draft's own discipline (bounded and NAMED, never
claimed zero): per decision log₂(⌈D/g⌉+1) = log₂(120,001) ≈ **16.9 bits**; per
refusal stretch log₂(⌈budget/g⌉+1) = log₂(5,001) ≈ **12.3 bits**. These are the
widths the gate review already expects to see; they shrink only by coarsening g
or shortening D, both of which cost ergonomics.

**C2 — commit_bound = 1 s.** The stores are local files/DBs behind one serialized
writer; a commit that cannot land in a second is not slow, it is failing, and the
spec's abort-always-available semantics want a bound tight enough that the abort
path actually fires. Everything downstream (staleness, the substantive predicate
D − commit_bound = 119 s) inherits this.

**C3 — budget = 5 s.** One request = one bounded unit of local work (a conveyance,
a store touch). 5 s is generous for local I/O yet small against D, so a slow head
converts to the catch-all refusal long before it can push the tail past its own
predicate — that is the cascade design working, not an error path.

**C4 — Q = 16.** Row B is the single writer; the writers feeding it are few (the
run's own actors, not the public). 16 bounds the drain arithmetic without
inflating D: doubling Q to 32 would push the D floor to 193 s and buy nothing —
a backlog of 16 on this architecture already means something is wrong, and the
head-budget cascade is the designed response.

**C5 — detection = 2 s.** The overdue-notice loop's period bound. It only feeds
C7's floor; 2 s is comfortably implementable with a plain poll and keeps the
refusal-tier window tight.

**C6 — D = 120 s.** The floor from the full-queue-drain inequality is 97 s; 120 s
adds ~24% margin and is a round, auditable figure. The two acceptance predicates
land at: touches timely by **119 s** (D − commit_bound), refusals by **150 s**
(D + enforcement_lag). A request unanswered for two minutes on local machinery is
a genuine failure — the deadline should say so rather than stretch.

**C7 — enforcement_lag = 30 s.** Floor 18 s (detection + Q·commit_bound), margin
67% for the storm case the backlog inequality models. Larger widens the refusal
window for no benefit; smaller risks the enforcement itself going overdue, which
is the exact defect (CODEX-V95 F3) this constant exists to close.

**C8 — GATE_PASS_BUDGET = 10 s.** A gate pass reads the chain as it stands and
runs the verifier passes — seconds of local compute even late in a run. The
release-by-inequality rule means an over-budget pass costs only its own retry;
the cumulative wire-wait worst case at these values is ≈150 s per full five-gate
sequence, which the spec requires be named: it is, here.

**C9 — PASS_RETRY_MAX = 3.** Three consecutive closed attempts at one gate
(abort/expiry in any mix) is a platform storm, not a transient; the right response
is surfacing, not grinding. Matches the retry family (C11, X1) so the whole sheet
has one retry philosophy.

**C10 — R_max = 2.** The spec's own floor, and the floor is right: every extra
render inflates the access log by one commit per object per member and widens the
padding cost, while 2 already gives every member exactly one replay after an
interruption. The exhaustion halt (TERMINATED-BY-LABEL-EXHAUSTION) stays the rare
storm case the spec designed it to be. Not χ-coupled — no shopping concern.

**C11 — A_max = 3.** The draft's own words: a commit that cannot land after A_max
bounded attempts is the platform failing. Three closed abort pairs is enough to
rule out transients and short enough that the drain never loops; the member is
skipped and honestly listed in `failed_members`.

**Blind-commit discipline, stated.** None of these constants is χ-derived or
outcome-coupled; committing them now — before any run data exists — with these
written reasons satisfies the blind discipline. There is nothing to shop: no value
here can move a verdict, only the patience of the machinery.

---

## Part 2 — the reviewer roster (R1)

The frozen schema: `(kind, roster_entries)`, count-prefixed, identity-sorted
`(reviewer_identity, reviewer_pubkey)` pairs, committed WITHIN THE P0-FROZEN
BS-2k PROVISIONING MATERIALS — so the roster's authority chain ends at your
freeze signature, and changing it later is a re-freeze, never an edit. Machine
keys are excluded by rule: the enumerator and sealed-interface keypairs are
provisioned separately and are NOT roster members.

- **Option A — minimal (RECOMMENDED): one entry, you.**
  `(Duho Kim, <your-pubkey>)`. The roster's function is the human signature over
  review records (mismatch dispositions, the freeze-review duties), and every
  human waypoint this preregistration has — P0, P6, P7, P9 — is already you. A
  roster naming a second human who will never actually produce a keypair and sign
  is the fictional-authority defect this corpus kills on sight; the honest roster
  matches the real trust structure. **Cost, stated plainly:** adding a reviewer
  later requires a re-freeze.
- **Option B — you plus one real second reviewer.** `(Duho Kim, <pubkey>)` +
  `(<name>, <pubkey>)` of a colleague who will genuinely hold a key and sign
  mismatch reviews. Two-person review is stronger — but only if the second person
  is real, reachable at run time, and actually signs; supply the name and pubkey
  before P0 and the packet absorbs it as an amendment.

**Recommendation: A**, unless you have a specific real second in mind today.

---

## Part 3 — the custody / escrow holder roster (R2)

From Row A's frozen obligations: the custody provisioner creates stores, escrows
keys, installs the mediator, records the archive seal state; the seal-state
schema binds the **holder-roster digest**; no holder or run host may possess a
raw-store read path outside the pinned mediator, and a key share retained outside
the escrow is banned outright.

- **Option A — minimal (RECOMMENDED): you as sole custody holder.** The
  holder-roster digest binds exactly one identity; all sealed key material lives
  in the escrow under the recorded seal state; every access is through the pinned
  mediator. **Honest note:** single-holder custody protects against process and
  machine compromise — the actual threat model here — and NOT against the holder
  himself; but you already hold P0, so splitting keys against yourself adds
  ceremony, not security.
- **Option B — you plus a second share-holder (2-of-2, or 2-of-3 with a cold
  share).** Real protection only if the second holder is genuinely independent
  and available at unseal time; otherwise it converts a security ceremony into an
  availability risk on your own run.

**Recommendation: A** with the honest note on the record.

---

## Part 4 — surfaced by the sweep, proposed here so nothing dangles (X1–X2)

- **X1 — conveyance retry limit = 3.** The draft freezes "a fixed per-position
  attempt limit … the limit's value is a preregistered parameter fixed at freeze"
  and values it nowhere. Proposed 3, the sheet's one retry philosophy (C9, C11):
  every position retries a transient storage failure the same three times, so the
  count reveals nothing.
- **X2 — the CLOSED operation set: fixed by EXTRACTION, not by a hand list.** The
  class-key `operation` tokens must come from "the BS-2k event schema's CLOSED
  operation set, fixed at provisioning." Proposing the same no-second-registry
  discipline every other set in this build uses: at provisioning, the set is
  extracted from the §6.1 row table's own operation column by the pinned
  extraction tool, digested, and committed — a hand-written duplicate list would
  be the divergent-registry defect. You are signing the DISCIPLINE here; the
  extracted membership gets its digest at provisioning and any mismatch refuses.

---

## Signature block

- **Take everything:** reply *"constants and rosters approved as proposed"* —
  C1–C11 + R1-A + R2-A + X1 + X2 enter the BS-2k provisioning materials, frozen
  at P0.
- **Amend by ID:** e.g. *"C6 = 180 s, R1 = option B (name, pubkey follows), rest
  as proposed"* — I re-derive the touched inequalities, re-present only if
  something breaks, otherwise the amended packet is the packet.
- **Nothing here touches:** the Sep-5 BS-1 rule, the P0 signature itself, v9
  (frozen at `6a9abbbd…` throughout), or anything χ-bearing.
