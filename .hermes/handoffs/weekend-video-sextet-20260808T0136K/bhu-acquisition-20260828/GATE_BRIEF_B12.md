# GATE BRIEF — B12, entry 51's primordial-black-hole route

You are an adversarial gate seat with fresh context. Your job is to REFUTE the claim below, not
to endorse it. Default to refuted if you cannot verify a step from the pinned sources yourself.

Working dir: `.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828`
Script: `b12_entry51_pbh_route.py` (runs 5/5, exit 0). Predecessor: `b11_entry51_measurement.py`.
Sources (read them, do not take my quotes on trust):
  `../bhu-reading-20260823/sources/0910.1181_clean.txt`   Poplawski (entry 51)
  `../bhu-reading-20260823/sources/2002.12778_clean.txt`  Carr, Kohri, Sendouda, Yokoyama, PBH review
  `../bhu-reading-20260823/sources/2604.10732_clean.txt`  CMS micro black hole search

## THE CLAIM

Entry 51 (Poplawski, ECKS torsion, minimum black-hole mass ~1e16 kg) is recorded in our
bibliography as a CALIBRATED-FALSIFIER whose only test route is the LHC, where a null "fires
nothing" and the gap to the floor is 39 decades. I claim that reading is too narrow:

**C1 (SCOPE).** Poplawski's floor is a bound on DENSITY that applies to any black hole, not a
statement about collider production. The LHC is his illustration. Therefore primordial black
holes are in scope.

**C2 (PLACEMENT).** The current open window in which PBHs could be all the dark matter is
1e17–1e23 g (Carr et al.). The floor, 1e16 kg = 1e19 g, lands INSIDE it, splitting it into a
forbidden band 1e17–1e19 g and an allowed band 1e19–1e23 g.

**C3 (CONSEQUENCE).** A PBH dark-matter detection in 1e17–1e19 g FIRES the falsifier. This route
is ~37 decades closer to the floor than the collider route and is open right now.

## ATTACK THESE SPECIFICALLY

1. **Is C1 real, or am I over-reading one sentence?** Does Poplawski anywhere restrict the floor
   to collider production, to a formation epoch, or to a particular mechanism? Does the ECKS
   density argument actually forbid a PBH that formed in the early universe at high density, or
   does it only forbid *forming* one at a collider? A PBH forms in a radiation-dominated era where
   the ambient density was itself enormous — does that change the argument?
2. **Is C2 the review's CURRENT claim?** I quote "the middle mass window has shifted to
   1e17–1e23 g". Check I am not quoting the review's *historical* sentence (which gives
   1e16–1e17 g and 1e20–1e26 g) as its present one. Check also whether the review elsewhere
   states that window is now excluded.
3. **The number I could not reproduce.** Inverting the paper's own rho_Ce ~ 1e51 kg/m^3 through
   rho = 3c^6/(32 pi G^3 M^2) gives 2.7e14 kg, not 1e16 kg — a factor of 37. I explicitly decline
   to call this an error. Am I right to decline? Can you find Poplawski's actual route to 1e16 kg?
   If the true floor is ~3e17 g the forbidden band nearly vanishes and C3 collapses. THIS IS THE
   MOST LOAD-BEARING UNCERTAINTY IN THE NOTE.
4. **Does "detection fires it" survive?** Is a PBH dark-matter detection in the forbidden band
   actually achievable, or is that band constrained in a way that makes detection impossible
   anyway — in which case the route is no better than the LHC one?
5. **Reproduce.** Run the script. Does any check claim more in its name than its predicate tests?

## VERDICT FORMAT

First line, one token: `ROUTE_CONFIRMED` / `ROUTE_REFUTED_<reason>` / `ROUTE_NARROWED_<reason>`.
Then per-attack findings. Write to `<C or A>GATE_B12_VERDICT.md` in this directory.
Say plainly what you could not verify.
