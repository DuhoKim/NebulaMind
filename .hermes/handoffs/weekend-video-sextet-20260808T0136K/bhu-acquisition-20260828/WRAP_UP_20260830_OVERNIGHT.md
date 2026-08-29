# BHU lane — overnight wrap-up, 2026-08-29 ~23:40 → 2026-08-30 ~01:00 KST

**Read cold, this file AFTER `WRAP_UP_20260829_FULL_DAY.md`** — that file covers the day through
the question-1 answer and the miss-rate audit's launch; this one covers the census that followed.
Both stand without recollection. The register (`HARNESS_DEFECT_REGISTER.md`, classes through 1ag)
and `OPEN_QUESTIONS_FOR_DUHO.md` are the other two load-bearing files.

## The one-paragraph version

The obstruction-content census of the unflagged readable corpus is **closed**: every readable BHU
paper has now been adjudicated under the one preregistered rule (b28's), every verdict gated, in
five batches (b29 sample, b33, b36, b37, b38). The screen **leaks** — the preregistered random
sample I scored zero actually held **2–3 misses** (entries 5, 37, ±49), and the census closer found
**two more dual papers** (52, 53) whose headline result is an existence exclusion. Four not-located
papers were recovered from arXiv by exact-title search (15, 17, 20, 28 — readable now 38, not
located 13), one metadata error was fixed (entry 20's authors belonged to a different paper), and
the proof-owner of a cited no-go was pinned (Bronnikov 2001). **No tier changed all night.** Three
tier questions sit with Duho: **5** (entry 5), **6** (entry 51's dual shape — the keystone), **7**
(entries 52/53, same shape as 6).

## What a cold reader must not re-derive

- **"Zero misses in eleven" is WITHDRAWN** (b29 → gates). Entries 5 and 37 are misses under the
  preregistered rule; entry 49 is a third under the rule as written (proof delegated to entry 48,
  which is paywalled and unread). Corrected bound: up to a third–half of the unflagged pile.
- **"A verified screen is safe at any precision" is REFUTED** — checking flags cannot see a paper
  that was never flagged. Recorded against the question-1 answer, not reversing it.
- **Batch 3's draw claim is WITHDRAWN** (uncommitted `choice()`); batches thereafter commit the
  executable draw first (b35) or take the whole remainder (b37).
- **Entry 51's Papapetrou theorem is a rigorous derivation** — both seats agree; they split only on
  the tier disposition (question 6). Precise proven domain is in the entry's prose.
- **Entry 38's "we proved this in [15]" is unsupported** — [15] is entry 57, read in full by both
  seats: it restricts to outside the horizon and never says "black hole". Entry 38's own §4 carries
  the narrow warrant.
- **Entries 52/53 headline "a closed universe exists only when …"** — verified in both abstracts;
  the eighth narrow-pattern miss (no "exists only when" in my pattern).

## Infrastructure a restart should use

- **`check.py`** — pre-commit control: full battery + negative-assertion sweep. **Gate commits on
  its exit** (`python3 check.py && git commit …`); I committed past a red control once (1f0087ee7)
  because the chain gated on a grep instead.
- Register classes **1ae–1ag**: line-wrap-defeated verification greps (use short fragments);
  four false-positive classes in one document matcher; a control not invoked ≙ no control.
- Census artifacts: `b28` (preregistration), `b29` (result, corrected), `b31` (census frame),
  `b33/b36/b37/b38` (batches + gates), `b35` (committed draw pattern).

## Open with Duho (nothing else blocks)

Questions **5, 6, 7** in `OPEN_QUESTIONS_FOR_DUHO.md` — all tier calls. Answering **6** settles the
dual-paper convention that decides 7 and likely informs 5. Separately: three papers need his
library login (Popławski PLB 690, Silk Science 277, Farhi & Guth PLB 183), and entry 19 is MDPI
open-access, fetchable by the browser route used for entries 25/26.
