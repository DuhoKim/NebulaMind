#!/usr/bin/env python3
"""A13 -- the selection-bias control. Blanc:

    "If you picked the most promising opposite-error candidates and all nine failed, the null is
     strong. If you picked the ones that were easiest to check, it is weak, and the distinction is
     invisible from the outcome. Write down the rule you have actually been selecting by, then
     draw two or three entries at RANDOM from the remaining pool and run them."

THE RULE I HAVE ACTUALLY BEEN SELECTING BY, written before the draw and without flattery:

  entry 21  the bibliography's own rank 4, and its question was stated as a binary
  entry 26  I had just pinned it, and its ABSTRACT PROMISED a prediction
  entry 25  rank 3 primary, just pinned
  entry 22  rank 5, CONSISTENCY-ONLY + audit-worthiness HIGH, and a no-go theorem
  entry 52  OUR OWN METHODS_NOTE already flagged it as holding a number and threshold
  entry 23  rank 3, named by the bibliography as supplying entry 25's "falsifiable edge"
  entry 8   rank-1 spine, chosen specifically to leave the Gaztanaga line

Honestly stated, that is TWO rules braided together:
  (A) highest prior of concealing a testable claim -- bibliography rank, audit-worthiness,
      abstracts promising predictions, our own prior flags. This biases TOWARD finding the
      opposite error, so nulls here make the null STRONGER.
  (B) availability -- four of nine were papers I had pinned hours earlier, and I favoured papers
      with rich, claim-dense abstracts because they are faster to adjudicate. This biases toward
      EASY-TO-CHECK, and nulls here make the null WEAKER.

I cannot separate (A) from (B) by introspection, and the outcome looks identical either way.
Hence the draw.

SEED PROVENANCE. The seed is the git HEAD sha at draw time, passed in as argv[1]. It is fixed by
the commit history before the draw happens, so I cannot have chosen it after seeing which entries
came up. Recorded here so the draw is reproducible and auditable.
"""
import random, sys, os, json

# pinned AND unaudited, from ENTRY_SOURCE_MAP extensions minus everything examined to date
POOL = {
    1:"1111.1017", 9:"arxiv_1007.0587", 10:"arxiv_1111.4595", 11:"arxiv_1410.3881",
    12:"arxiv-2509.11468v2", 24:"2104.00521", 27:"2204.11608", 36:"smoller_temple_2000",
    37:"0210105", 38:"math-ph_0302036", 39:"1105.6127", 40:"2008.02136", 41:"2007.11556",
    43:"2304.12018", 44:"1309.1487", 45:"2210.15186", 49:"blau_guendelman_guth_1987",
    53:"1906.11824", 55:"2007.06664", 57:"smoller_temple_1997",
}
AUDITED = [6, 7, 8, 21, 22, 23, 25, 26, 31, 51, 52, 54]

seed_hex = sys.argv[1] if len(sys.argv) > 1 else "0"
seed = int(seed_hex[:12], 16)
rng = random.Random(seed)
draw = sorted(rng.sample(sorted(POOL), 3))

print("=" * 92); print("A13 -- RANDOM DRAW, selection-bias control"); print("=" * 92)
print(f"\nseed source : git HEAD sha = {seed_hex}")
print(f"seed value  : int('{seed_hex[:12]}', 16) = {seed}")
print(f"pool        : {len(POOL)} pinned + unaudited entries")
print(f"              {sorted(POOL)}")
print(f"already done: {AUDITED}  ({len(AUDITED)} entries, all hand-picked)")
print(f"\nDRAWN: {draw}")
for e in draw:
    print(f"   entry {e:<3} -> {POOL[e]}_clean.txt")
print("""
WHAT THIS CONTROLS FOR, and what it does not

CONTROLS FOR: my picking. If these three also come back tier-unchanged, the null is a statement
about the corpus rather than about which entries I chose to look at.

DOES NOT CONTROL FOR: the pool. Every entry here is one that was PINNED, and pinning was itself
driven by the bibliography's ranked list. So this is a random draw from a non-random pool. The
19 still-unpinned entries are not represented at all, and they are disproportionately the
paywalled and low-audit-worthiness ones. Stated so the result is not read as stronger than it is.

n = 3. Three nulls will not prove anything on their own; they can only fail to break the pattern.
One tier change here would be worth more than all nine confirmations.
""")
json.dump({"seed_hex": seed_hex, "seed": seed, "pool": sorted(POOL), "drawn": draw},
          open("_random_draw.json", "w"), indent=1)
print(f"draw recorded to _random_draw.json")
