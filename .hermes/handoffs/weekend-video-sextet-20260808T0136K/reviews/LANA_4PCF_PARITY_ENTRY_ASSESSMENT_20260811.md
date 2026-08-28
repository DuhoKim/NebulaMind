# Lana — 4PCF parity: is there a tractable, non-circular entry point?

**Lana (science / claim-boundary seat), 2026-08-11.** New-direction question after Duho closed the Quaia
line (*"let's move on to other data, don't spill sweat on it"*). Candidate from Goru's inventory
(`GORU_COSMIC_ANISOTROPY_PUBLIC_DATA_INVENTORY_20260810T2340K.md`, probe 4): cosmological parity violation
in the galaxy four-point correlation function (4PCF), BOSS tetrahedra. **NOT_WORTH_DOING_YET is an
acceptable and previously-correct outcome. Nothing is committed; Duho decides after reading me and Kun.**

**Sourcing caution, stated first.** Everything below about the literature comes from my trained knowledge
(cutoff January 2026) and from Goru's overnight inventory, which is a triage, not a source-bound read. One
error is already visible: the inventory names the rebuttal side as "Ivanov, Oliver" — **Oliver Philcox is
on the *claim* side** (his ~3σ BOSS measurement), and to my knowledge the covariance rebuttal is led by
**Krolewski, May, Smith and collaborators**, with a further null-style reanalysis by **Adari & Slosar**.
We have institutional memory of a from-memory literature claim getting sha-pinned into a contract and
inverting a lane. So: every literature statement in this assessment is marked **[VERIFY]** where it is
load-bearing, and **no design may freeze until each is quoted from the primary paper.** This assessment is
for direction-setting, not for freezing.

---

## 0. Verdict up front

**There is exactly one narrow entry I can defend, and it is conditional on three checks that must pass
before anyone designs anything. If any check fails, the honest verdict is NOT_WORTH_DOING_YET.**

The one defensible entry: **a covariance-robustness reanalysis of the published BOSS parity-odd 4PCF data
products — no tetrahedron counting of our own, no new measurement.** The live dispute is (I assess, subject
to §1 verification) not about the measured data vector; it is about **what covariance to divide it by**.
Both sides have published data products (measured 4PCFs, mock 4PCF suites, analysis code). If those
products are verifiably public and sufficient, the question "how does the claimed significance move across
every published covariance construction, on identical inputs?" is computable on our hardware, is not the
same study as either side's paper, and produces a defensible narrow result whichever way it comes out.

Everything larger — an independent 4PCF measurement, a new systematics treatment, a DESI analysis — fails
the tractable/non-circular/not-already-said test today (§3). And the entry above dies if it turns out the
rebuttal papers already published exactly this cross-covariance table (§6, check B).

## 1. What exactly is disputed? (This determines everything else)

Three possible loci of dispute, with my assessment of where this one actually lives:

- **The measurement (the parity-odd 4PCF data vector itself)?** Largely NOT disputed, to my knowledge
  **[VERIFY]**. The rebuttal side reproduces the data vector; nobody claims the tetrahedron counts are
  wrong as counts. If verification contradicts this, the whole assessment changes — an unreproducible data
  vector would be a different (and worse) situation.
- **The covariance / significance estimate?** **The primary battlefield [VERIFY].** The detection
  significances (reported ~7σ in Hou–Slepian–Cahn CMASS; ~3σ in Philcox) divide the measured odd-parity
  vector by a covariance estimated from mock catalogues (MultiDark-Patchy). The rebuttal argument, as I
  understand it: the variance of a parity-odd 4PCF under the null is set by parity-**even** correlations up
  to the **8-point** function; approximate mocks do not carry realistic connected 8-point structure, so the
  covariance is underestimated and the significance inflated; alternative mock suites (e.g. GLAM) and
  data-driven estimates give materially lower significance. If that is right, the dispute is about a
  **statistical construction**, not about the sky.
- **The systematics treatment (fiber collisions, geometry, target selection)?** A real but, I assess,
  **secondary** channel **[VERIFY]** — raised by the rebuttal side as additional reasons for caution, and
  partially testable by them via weight variations. Goru's inventory foregrounds this channel (it is the
  one his maps-exist criterion sees), but the significance dispute would persist even with perfect
  systematics maps, because it lives in the covariance.

These three loci need very different work: re-measurement (heavy compute + heavy method cost), covariance
study (published-products arithmetic, tractable), systematics study (pipeline reconstruction, heavy and
partly non-public). **Only the covariance locus is within our reach, and it happens to be where I assess
the live dispute sits.** That alignment is why an entry exists at all.

## 2. Is this Mittal–Singal again — a dispute about what the papers publish?

**No — and this is the decisive difference.** The Mittal–Singal disagreement was unresolvable from the
published record: no code, no mask memberships, no stated O(1) correction; our honest terminal deliverable
was a methods note, and Duho has had one of those. Here, to my knowledge **[VERIFY per item in §6]**:
the BOSS LSS catalogues and randoms are public; the imaging-systematics maps are public (Goru verified the
class); the claim-side analysis code is public (Philcox's `encore`; the Slepian-group 4PCF code); the mock
suites exist publicly in some form; and at least part of the measured 4PCF data products and mock 4PCF
suites were released with the papers. **The dispute is substantive-statistical, not custodial.** That means
the failure mode "we can only write another methods note" is avoidable here — but *only* if we actually
compute something, which is what §4 scopes minimally.

## 3. What would a genuine contribution look like? Four options, ranked honestly

1. **Independent full measurement of the BOSS parity-odd 4PCF.** Not worth it. It re-does what two groups
   already agree on (the data vector), at the highest compute and mathematical entry cost (the
   isotropic-function basis of Cahn–Slepian is genuinely heavy; Goru's "trillions of tetrahedra" barrier is
   real for naive counting, mitigated but not erased by the harmonic-decomposition codes). It would say
   nothing not already said.
2. **A systematics test neither side ran.** Unlikely to exist within reach. The rebuttal side's program is
   precisely a systematics-and-covariance sweep **[VERIFY scope]**; finding an untested knob would require
   first reconstructing their pipeline — see 3.
3. **Reconstruction of one side's pipeline.** Blocked by compute, not by publication: a defensible
   covariance requires processing O(10³) mock catalogues through a 4PCF pipeline. That is cluster work, not
   Mac Studio work. And DESI's own collaboration analysis of DR1 (in progress or imminent to my knowledge
   **[VERIFY status — this is a kill-switch]**) will do this with better data and internal-systematics
   access we can never match. Racing a collaboration on its own data is the definition of sweat Duho said
   not to spill.
4. **The narrow entry: significance-vs-covariance on published products only.** Assemble the released
   measured data vectors and every released mock-4PCF suite / covariance construction from both sides;
   recompute the detection statistic for every (data vector, covariance) pairing on identical conventions;
   report the significance as a *function of covariance choice*, with the compression/regularisation
   choices (eigenvalue cuts, number of mocks vs number of bins) made explicit and varied. No new
   tetrahedra. No new systematics claims. The deliverable is a table and its reading: either the claimed
   signal's significance is robust across published covariance constructions, or it is not — and both are
   real results *about the published record's own products*, stated without adjudicating the sky.

## 4. The smallest version that still says something real

**Study title (working):** *The BOSS parity-odd 4PCF detection significance as a function of published
covariance construction.*
**Inputs:** released 4PCF data vectors (claim side); released mock 4PCF suites (Patchy-based, GLAM-based,
and any data-driven constructions the rebuttal released); the papers' stated compression conventions.
**Computation:** χ²/rank-statistic evaluation across the pairing grid; eigen-spectrum diagnostics of each
covariance; sensitivity of significance to mock count and bin compression. Workstation-scale.
**Boundary (pre-committed):** the study adjudicates *nothing about parity in the universe*. Its permitted
claim has the same shape as the methods note's: *from the published products, the reported significance
{is / is not} stable under the covariance constructions the record itself contains.* If the answer is
"not stable," that is a statement about the record, not a refutation of parity violation; if "stable,"
it is not a confirmation of parity violation. Kun gates that boundary exactly as he did the note's.
**Why it is not redundant (to be confirmed at §6-B):** the rebuttal compares its own covariance against
the original; to my knowledge no single artifact evaluates *all* published constructions on *identical*
data-vector conventions with the compression choices varied openly. If §6-B finds that artifact exists,
this study dies and NOT_WORTH_DOING_YET stands.

**Effort estimate, honest:** the mathematics of the isotropic basis must be understood well enough to not
misuse the products (~the entry cost Goru flagged, reduced but real); the computation itself is small. The
risk is front-loaded in the two reads (§6-A, §6-B), which are bounded: two claim papers, two-three rebuttal
papers, their data-release pages.

## 5. Circularity traps, named in advance

1. **Parity-even-by-construction mocks.** Every mock suite in this literature is parity-even by
   construction; a mock-based covariance is therefore a *null* covariance. That is legitimate for null
   testing — but it means no mock-covariance analysis can ever "find" parity violation in the covariance
   itself, and any study that treats mock-agreement as evidence about the sky assumes the null it tests.
   Our narrow entry must present mock covariances as *constructions*, never as ground truth.
2. **Data-driven covariance absorbing the signal.** A covariance estimated from the data (jackknife,
   sub-sampling) partially contains whatever parity-odd signal exists; dividing the signal by itself
   deflates significance by construction. The rebuttal-side constructions must be checked for this before
   we present "significance drops" as neutral arithmetic — otherwise we launder a circular deflation as a
   finding. Both directions of this trap get a named column in the deliverable.
3. **Systematics weights derived under isotropy.** BOSS imaging weights are regressions of observed density
   on property maps, derived assuming residual density fluctuations are noise. Any pipeline that re-derives
   or re-applies weights and then tests for a spatial asymmetry partially assumes its conclusion — the
   same trap class as the Quaia selection function. Our narrow entry avoids re-deriving weights entirely
   (published products only), which is a reason to *keep* it narrow.
4. **Geometry/edge correction validated on parity-even mocks.** The survey-geometry correction that keeps
   even-parity leakage out of odd multipoles is itself validated on parity-even mocks. A reconstruction
   study would inherit that; our products-only study must state it as a shared assumption of both sides,
   not silently accept it as resolved.
5. **The spin-handedness association.** The 4PCF tetrahedron chirality (3D positions) and galaxy spin
   handedness (2D image chirality) are **unrelated observables**; the connection to Duho's standing
   interest is thematic, not physical. That interest is personal and is **not a corpus frontier**; per
   standing rule it must not be dressed as one, and no motivation section of any future design may cite it
   as scientific grounding. I flag it here so nobody else has to.

## 6. Preconditions — all three must pass before any design brief exists

- **A. Primary reads (Lana).** The claim papers (Hou–Slepian–Cahn; Philcox) and the rebuttal papers
  (Krolewski et al.; Adari–Slosar; any I am missing — the inventory's "Ivanov, Oliver" naming must be
  resolved against the actual literature) read at the primary source, with §1's locus-of-dispute
  assessment confirmed or corrected **by quotation, not memory**. If the dispute turns out to live in the
  measurement or the systematics rather than the covariance, the entry point dies.
- **B. Redundancy check (Lana, during the same reads).** Confirm no published artifact already evaluates
  all covariance constructions on identical conventions. If it exists, NOT_WORTH_DOING_YET.
- **C. Custody check (Tori).** Verify the actual public existence, completeness and licence of: the
  released 4PCF data vectors; the mock 4PCF suites from each side; the analysis codes. Exact paths, DOIs,
  checksums — the Mittal–Singal standard. If the products needed for the pairing grid are not actually
  public (papers gesturing at "available on request" do not count), the entry dies and the honest verdict
  is that this probe, too, is **not measurable-as-disputed from public products**, which would itself be
  worth one paragraph in the lane record, not a study.
- **D. (Kill-switch, checked with C.) DESI DR1 parity status.** If a DESI collaboration parity-4PCF
  analysis is already published or imminent with a covariance program, the BOSS-products study shrinks
  from "useful narrow contribution" to "footnote to a superseded dataset" and should not be started.

## 7. Plain answer to the question asked

Is there a study we could actually do, non-circular, saying something not already said? **Conditionally
yes — one, and only the narrow one:** significance-vs-covariance on published products, boundary-limited
to statements about the record, gated by the four checks above. It is tractable on our hardware, it is not
a re-run of the closed dipole question on new data, it is not a second methods note (it computes), and its
circularity traps are nameable and avoidable because we touch no selection function and derive no weights.

If any precondition fails, the honest verdict is **NOT_WORTH_DOING_YET**, and what would have to change is
concrete: either the collaborations publish the missing products (C), or DESI's parity result lands and
creates a *new* published record worth assessing (D) — at which point the right instrument might again be
an attributability note rather than a study, and Duho can decide then whether he wants another one.

— Lana, 2026-08-11. Assessment only: nothing designed, nothing frozen, no data touched. Next honest step
is §6-A/B (my primary reads) and §6-C (Tori's custody check), in either order, before any design brief.
