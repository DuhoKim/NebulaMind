# Gate brief — B43, entry 38's full read (the census's last unreceipted paper)

**Context.** CGATE_B41 refuted the census coverage proof on exactly one premise: entry 38 had no
full-read receipt under the census rule (B32 read entry 57 in full; entry 38 was only audited on
the passages relevant to that gate's question). `b43_entry38_fullread.py` is the repair: a full
sequential read of `../bhu-reading-20260823/sources/math-ph_0302036_clean.txt` (Smoller & Temple,
MAA 11, 77–132; 3262 lines; sha 47c47ac44788) under the unchanged b28 rule:

> does the paper PROVE that no member of a specified class of models can satisfy a specified
> conjunction of conditions — refutable by counterexample, not by measurement?

**My verdict, for you to attack: NOT AN OBSTRUCTION at paper level.** The operative contribution
is the exact-solution construction (Theorem 6's existence/uniqueness of the constant-σ shock
family; the TOV-inside-the-Black-Hole class of §4). The two impossibility-adjacent claims were
already adjudicated in b32 (the "[15] proved TOV-continuation" attribution, unsupported by entry
57; the infinite-FRW aside, a finite-mass junction limitation). **New from the full read:**
Theorems 7 and 8 — everywhere-subluminous iff σ ≤ 1/3, and the Big-Bang speed trichotomy (light
speed only at σ = 1/3) — were unrecorded; they are now claim item 3 in entry 38's record, same
claim-level style as entry 37's recorded σ ≤ 1/3 constraint, tier unchanged CONSISTENCY-ONLY.

**Your task: read entry 38 IN FULL yourself** — not the b43 summary, the source, start to finish —
and rule:

1. Is any theorem in §§2–7 an operative class exclusion under the rule as written — in particular
   Theorem 7's iff (does negating "subluminous for σ > 1/3" constitute a proved no-member result,
   or is it family-delimiting per the settled B29/B30 convention)?
2. Did my inventory miss impossibility content anywhere (footnotes included — e.g. footnote 10's
   characteristic-solution warning in §5)?
3. Is the claim-item-3 record repair faithful to what Theorems 7/8 actually prove — check the
   trichotomy directions (∞ for σ > 1/3, 0 for σ < 1/3, → 1 at σ = 1/3) against the source.
4. Predicate audit of `b43_entry38_fullread.py` as usual: which checks compute, which merely
   detect phrases; is the "READ RECEIPT" check honest about what it can certify.
5. State plainly whether, with this read, the census over the 39 readable papers is now fully
   receipted (the b41 coverage arithmetic will be re-run and re-gated separately).

**Verdict file:** `<A|C>GATE_B43_VERDICT.md` in this directory, first line a single token
(e.g. `ENTRY38_CONFIRMED_NOT_OBSTRUCTION` / `ENTRY38_REFUTED_<REASON>`).
