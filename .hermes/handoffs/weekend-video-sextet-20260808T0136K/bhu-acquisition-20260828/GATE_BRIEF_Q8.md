# Gate brief — question 8's ruling and implementation (the Q1–7 closure pattern)

**What happened.** Duho returned question 8 with the verbatim delegation "answer question 8"
(via Blanc's relay; the same pattern as questions 1–7, all ratified this morning). I ruled it:
**entry 48 → THEORETICAL-OBSTRUCTION** (option A), implementation committed at 4a5683e49.

**The ruling's stated basis, for you to attack:**
1. the adopted ownership-of-proof convention — the tier goes to the paper presenting the no-go
   derivation; both seats' B45 verdicts confirmed entry 48 owns it in-text;
2. the operative-contribution test — the exclusion is the title, abstract, and §II's result;
3. the read is double-gated (AGATE_B45 confirmed; CGATE_B45 narrowed-confirmed, repairs applied).
The PREPRINT-not-VoR caveat travels with the tier, and a REVISIT clause is printed: the tier is
reopened if the PLB 183, 149 version-of-record comparison ever shows a material difference.

**The implementation, all in one commit:**
- entry 48's Testability line (token format `**THEORETICAL-OBSTRUCTION**` closing immediately —
  the first edit buried the token inside the bold and every parser missed it; the battery
  caught that before commit and it is disclosed in the commit message);
- the class tally recomputed: 4 CF / 7 QD / 3 PROSPECT / 32 CONSISTENCY-ONLY /
  **3 THEORETICAL-OBSTRUCTION (22, 5, 48)** / 2 UNREAD (42, 47) = 51, with a supersession note;
- five battery scripts moved in the same change (the 1ab discipline): b45's tier check now
  asserts the ruled state; b43/b46/b47 assert the current set {22,5,48}; **b41 is
  FRAME-SCOPED** — its census metrics now compute over obs ∩ READABLE so the closed census's
  1-of-2 miss rate and 1-of-3 precision are untouched (entry 48 was tiered post-census, outside
  the readable-39 frame, and never in the screen's pool — printed in its output);
- question 8's closure in OPEN_QUESTIONS_FOR_DUHO.md (standard format: verbatim instruction,
  ruling, basis, caveat, what changed, revert cost); the originally-filed question archived.

**Your task:**
1. Is the ruling sound under the corpus's own conventions — or does the preprint-not-VoR status
   defeat tier assignment despite the revisit clause? (Option B's case: zero risk of tiering
   off a preprint. Say plainly if you would have held.)
2. Is the frame-scoping of b41 honest — or does adding entry 48 to the corpus-wide obstruction
   set while keeping 1-of-2 as "the" miss rate misrepresent anything? Run
   `python3 b41_census_coverage.py` and audit the printed disclosure.
3. Check the tally arithmetic against the actual Testability markers (parse them yourself).
4. Check the closure record's fidelity (OPEN_QUESTIONS): is the basis as stated, the cost
   honest, the archived section clearly non-open?
5. Predicate audit of the five changed checks as usual.

**Verdict file:** `<A|C>GATE_Q8_VERDICT.md`, first line a single token
(e.g. `Q8_RULING_CONFIRMED` / `Q8_REFUTED_<REASON>` / `Q8_NARROWED_<REASON>`).
