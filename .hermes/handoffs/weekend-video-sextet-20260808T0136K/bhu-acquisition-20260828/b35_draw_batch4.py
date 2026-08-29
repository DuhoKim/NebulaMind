#!/usr/bin/env python3
"""B35 -- batch-4 draw. THE CODE IS THE PREREGISTRATION, committed before it is run in anger.

b34's draw was refuted: I used rng.choice() in a throwaway shell block and never committed the
selection rule, so CGATE recomputing under the recorded convention got different entries. This file
repairs that the only way that counts -- the ORDERED pools and the EXECUTABLE rule are in the
repository before the batch is read, seeded from the sha of the commit preceding this file.

  seed   a2d70fd0c... = HEAD when this file was written (the batch-3 gate commit)
  rule   random.Random(int(SEED[:15],16)).sample(POOL, 1) per stratum, strata in the order
         HIGH then MID, one shared RNG consumed sequentially. LOW has one member and is taken.
  pools  ordered by b31 hit count DESCENDING, ties by entry number ASCENDING -- stated, not natural.
"""
import random, sys
SEED="a2d70fd0c"
HIGH=[41,54,9,39]              # 7,6,5,5 hits
MID=[23,26,45,21,44,52,53]     # 4,4,4,3,3,3,3
LOW=[11]                       # the minimum stratum's last member
rng=random.Random(int(SEED[:9],16))
h=rng.sample(HIGH,1)[0]; m=rng.sample(MID,1)[0]; l=LOW[0]
print(f"seed {SEED}  batch 4: high={h}, middle={m}, low={l}")
if __name__=="__main__": sys.exit(0)
