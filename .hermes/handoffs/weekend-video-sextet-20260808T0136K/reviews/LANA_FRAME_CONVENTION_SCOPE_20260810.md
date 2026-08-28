# LANA — scoping: what settling the FRAME_UNSTATED convention would require

**Scoping only.** This defines what a resolution would take. It resolves nothing, states no convention,
asserts no result / asymmetry / direction / sign / parity, and unblocks nothing by itself. Filed
**2026-08-10 10:45 KST**. Primary text quoted verbatim from the freeze-pinned sources; the forbidden scope
of `lanes/spin/SOURCE_FREEZE.json` still binds.

## RECOMMENDATION (read this first)

**Do not spend effort chasing the frame convention now. Record FRAME_UNSTATED as the terminal, honest
outcome it already is.** Three facts make the cost/benefit clearly negative:

1. **The rule is documentary-only (my ruling, §2 below), so no empirical test can unblock it** — however
   decisive — without Duho first granting an amendment that changes the evidence standard.
2. **The two most on-point documents are already exhausted and silent** (Lintott et al. 2011, the GZ1 data
   release; Land et al. 2008, the bias study), and A3.9 §5 already declares *"this avenue is closed: no
   third source is authorised by this amendment."* So **either path — documentary or empirical — requires
   Duho to grant a new amendment.** There is no cost-free move.
3. **Even a full resolution unblocks nothing on its own** — FRAME_UNSTATED is one of four blockers (§6),
   and `BLOCK_SUBSTANTIVE_RESULT_RENDER` stands until all four clear; the forbidden scope binds regardless.

If Duho nonetheless wants to pursue it, the **cheaper first probe is documentary** (Path A, §5) —
Lintott et al. 2008 and the SDSS/CasJobs GZ1 table schema, which have not been read — but with eyes open
that a hit is unlikely, since the papers whose whole job is these tables were already silent. The
**empirical route (Path B) should be opened only if Duho explicitly wants to change the evidence
standard**, and even then it produces a *finding*, not an *establishment*, unless the amendment says so.
Rough cost: Path A ~half a day and low-yield; Path B a heavier governance decision on top of compute.

---

## 1. What is unresolved — exact fields, exact question

The stored **mirrored-condition direction fields**, verbatim from the freeze-pinned CDS ReadMe
(`_gz_cache/ReadMe`, table5.dat / table6.dat column notes):
- `pcS1` — *"Mirrored 1 fraction of votes for ClockWise"*; `paS1` — *"Mirrored 1 fraction of votes for
  AntiClockWise"*
- `pcS2` — *"Mirrored 2 fraction of votes for ClockWise"*; `paS2` — *"Mirrored 2 fraction of votes for
  AntiClockWise"*
- `pcSm` — *"Monochrome fraction of votes for ClockWise"*; `paSm` — *"Monochrome fraction of votes for
  AntiClockWise"*

The exact question, verbatim from `AMENDMENT_A3.9_DRAFT.md` §3: *"In what frame are the mirrored-condition
direction fields (pcS1/paS1/pcS2/paS2) recorded — as seen in the mirrored image presented to the
classifier, or de-mirrored to the sky frame?"*

**Why it matters (in my terms).** The ReadMe tells us these fields are *fractions of votes for
ClockWise/AntiClockWise*, but never states the orientation of the stored value. Under one convention a
mirrored image's vote is stored as-displayed; under the other it is stored rotated back to the sky. Those
two conventions carry **opposite signs** for the same field. So if the stored sense is unknown, an
apparent handedness excess has **no trustworthy sign** — and with no trustworthy sign, no sky, dipole,
parity, or cosmological reading can be formed from it at all. The field values are not in doubt; their
*meaning* is. (No such reading is asserted anywhere here; the point is precisely that none can be.)

## 2. THE CRUX RULING — does A3.9 §5 admit only documentary evidence, or also empirical?

**Ruling: DOCUMENTARY-ONLY. An empirical determination cannot establish the frame or unblock FRAME_UNSTATED
under A3.9 as frozen — no matter how decisive.** This is a ruling from the frozen text, not an assumption.

The text is explicit. A3.9 §4 (the evidence standard): *"A verbatim quotation is required. A branch may
not rest on a paraphrase, a recollection, or an inference from a figure."* and *"An inference is not a
quotation. If the papers describe the mirroring procedure without stating the archival convention, the
honest reading is that the frame remains unestablished, however strongly the procedure suggests one."*
A3.9 §5 (defines "establishes"): *"a passage establishes the frame only if it is a verbatim statement of
the recording or archival convention of the mirrored-condition direction fields — i.e. of how the stored
values are oriented. A quoted description of the mirroring procedure … is a real quotation and so passes
§4's paraphrase bar, but it is not an establishment."*

An empirical determination — inferring the convention from how the stored fields behave in the data — is
by construction *"an inference,"* the exact thing §4 excludes. It is not *"a verbatim statement of the …
archival convention."* Under A3.9 it therefore cannot fire FRAME_AS_SEEN or FRAME_DEMIRRORED; the most a
decisive empirical result could be is a recorded *finding*, which does not move the branch.

**Consequence for the honest path — and I am naming it, not assuming it:** because the rule is
documentary-only, and because A3.9 §5's FRAME_UNSTATED disposition already states *"this avenue is closed:
no third source is authorised by this amendment"* (and §7: *"Any third source needs its own gate"*), the
current state is **terminal under A3.9**. Reopening it requires an **explicit amendment from Duho**, of one
of two kinds:
- **(A) a documentary-widening amendment** — authorises named additional documents + hosts under the same
  verbatim-establishment standard; or
- **(B) an evidence-standard amendment** — changes §4/§5 to admit an empirical determination as an
  establishment. This would *reverse a bar the lane set deliberately*: §4 records that *"On 2026-08-06 this
  lane froze a directional claim about the literature written from memory, and had to amend it after the
  primary source said the opposite — AMENDMENT_A2,"* which is why verbatim-only exists. Loosening it is a
  governance decision, not a technicality.

So the answer to the order's fork is unambiguous: **documentary-only.** An empirical answer cannot unblock
this as the rule stands; the honest paths are to find the document (Path A) or to obtain an explicit
amendment (Path A or B). I do not assume either — I rule the current rule documentary-only and hand Duho
the two amendment options with their costs.

## 3. Documentary sources — status, and what would count as a hit

A **hit** in every case is a *verbatim passage stating how the stored values of `pcS1/paS1/pcS2/paS2` are
oriented* (as-displayed-in-the-mirror vs de-mirrored-to-sky). A passage describing only the mirroring
**procedure** is **not** a hit (A3.9 §5). Precision on the order's list:

**Already exhausted (do not re-spend):**
- **CDS/VizieR ReadMe, incl. the column notes themselves** — *established SILENT* on the frame across
  three disjoint full-file searches (A3.9 §1; `KUN_FRAME_REVIEW.md`). The column notes give the field
  meaning (*"fraction of votes for ClockWise"*) but state no recording orientation. This is checked, not
  open.
- **Lintott et al. 2011** (MNRAS 410, 166, bibcode `2011MNRAS.410..166L`, the GZ1 data-release paper) —
  retrieved whole under A3.9 §2, **silent**; every mirror-bearing passage is procedural (Kun §1).
- **Land et al. 2008** (arXiv:0803.3247v4 = MNRAS 388, 1686, the bias study) — retrieved whole,
  **silent as an establishment**; it describes its experiment, not the archive's storage decision.

**Not yet read (each would require a widening amendment before it may be fetched for this question):**
- **Lintott et al. 2008** (MNRAS 389, 1179, *"Galaxy Zoo: morphologies…"*, the first GZ1 paper) — hit: a
  verbatim statement of the stored-field orientation. Plausibility: low-moderate (predates the mirrored
  data release; likely procedural).
- **The SDSS SkyServer / CasJobs GZ1 table schema and its column documentation** (the database the ReadMe
  was derived from) — hit: a schema note stating orientation of the stored direction columns. This is the
  most likely place a *storage* convention (as opposed to a *procedure*) would be recorded, and it has not
  been consulted. Best single documentary target.
- **Bamford et al. 2009** (MNRAS 393, 1324) — hit: same. Plausibility: low (bias/environment focus).
- **Willett et al. 2013** (MNRAS 435, 2835, GZ2 data release) — hit *only* if it verbatim states the GZ1
  convention; a GZ2 convention does not establish GZ1's and would risk a cross-dataset error.
- **The Galaxy Zoo team's public data-description pages** — hit: a verbatim orientation statement; weak as
  a "document of record."

Note: authorising any of these is exactly the *"third source"* A3.9 §5 says needs *"its own gate"* — so
even the documentary route is not free of an amendment.

## 4. The empirical route — defined (admissible ONLY under a §4/§5 amendment; asserts no result)

Defined so Duho can weigh whether it is worth an amendment. **It is not admissible under the current rule
(§2), and nothing here states an outcome.**

**Test.** Restrict to objects carrying both a mirrored-condition direction field and the unmirrored
(normal-leg / monochrome) direction field, and examine the **sign of the correlation** between the
mirrored-stored clockwise fraction (`pcS1`) and the unmirrored clockwise fraction, per object.
**Falsifiable prediction, by convention:**
- **FRAME_AS_SEEN** (stored as displayed in the mirrored image): mirroring flips apparent handedness, so a
  truly-clockwise galaxy tends to be voted anticlockwise when mirrored → the correlation is **negative**.
- **FRAME_DEMIRRORED** (stored rotated back to the sky frame): both fields refer to the same sky-frame
  handedness → the correlation is **positive**.
The prediction is a *sign*, opposite under the two conventions — which is what makes it, in principle, a
discriminating test.

**What would make it inconclusive:** low per-object vote counts making the per-object sign unresolvable;
the classifier handedness bias (the very effect under study) inducing its own correlation structure that
confounds the sign; a correlation near zero, consistent with neither cleanly; or an overlap subset too
small or unrepresentative to generalise. **This ground was already touched** — `t2_mirror_bias.py` /
`T2_MIRROR_BIAS.json` exist in the lane and implement a mirror-vs-normal comparison on the matched subset —
**but its output is a result and is out of scope for this document; I state no value, sign, or direction
from it.** Under §2's ruling that output is a finding, not an establishment, regardless of how it came out.

## 5. Cost and time per path

- **Path C — accept FRAME_UNSTATED as terminal (recommended): ~zero.** §5's UNSTATED disposition is
  already written: the lane's only publishable statement is the fenced conditional instrument reading of
  `LANA_T3_REDERIVATION.md` §4.3, **conditional on an unverified convention**, with **no Land-comparative
  phrasing anywhere** — *"not 'contradicts', not 'confirms', not 'in tension with'."* This is a legitimate,
  honest fail-closed outcome, not a failure.
- **Path A — documentary-widening amendment: ~half a day, low-yield.** Draft amendment (name the SDSS/CasJobs
  schema + Lintott 2008 + hosts, verbatim standard) → Kun gate → whole retrieval with five-field receipts →
  verbatim search → independent verdict review. Likelihood of a hit: low-moderate (the two most on-point
  documents were already silent). Risk: another FRAME_UNSTATED after the spend.
- **Path B — evidence-standard amendment (empirical): heavier, governance-first.** Draft an amendment
  reversing the verbatim-only bar → gate → run/verify the §4 test → independent review. Compute is small
  (test largely built); the real cost is the governance decision to loosen the exact rule that A2 was
  created to enforce, plus the risk the test returns inconclusive.

## 6. What settling FRAME_UNSTATED would and would NOT unblock

**It would unblock nothing on its own.** FRAME_UNSTATED is one of **four** blockers under the freeze's
`BLOCK_SUBSTANTIVE_RESULT_RENDER; ALLOW_METHOD_ONLY_CANARY` decision. The other three stand regardless:
- **STATUS_RESULT_MISMATCH** — the A3.8 post-run independent verdict-record review of `T4_PAIRED_FLIP.json`
  is unperformed.
- **WORKFLOW_STATUS_NOT_RELEASE_READY** — evidence-freeze, receipts, referee, and video stages pending.
- **LATER_FREEZE_EXCLUDES_NEW_POINTERS** — the later weekend freeze excludes new pointers.

So even a clean FRAME_AS_SEEN or FRAME_DEMIRRORED leaves the substantive-result render blocked until all
four clear, and **the forbidden scope still binds** — no T3/T4 headline or result figures, no dipole-axis
interpretation, no cosmological parity violation, no GRB/SN Ia/dark-energy/quasar/H0 context, no
black-hole-universe cosmology support, no new DESI Legacy or Ganalyzer claim. What settling the frame
*would* do is remove the **deepest interpretive** blocker — it would give the result a trustworthy sign,
so that (only in combination with clearing the other three, and within the forbidden fence) a
sign-dependent reading could later be formed. Alone, it changes the meaning that *could* be stated, not
what *may* be rendered.

---
**Bottom line for Duho's decision:** the frame is genuinely unresolved at the level of the six named
fields; the rule that governs it is documentary-only, so nothing short of a document or an amendment moves
it; the best documents are already silent; and settling it unblocks nothing by itself. My recommendation is
to accept FRAME_UNSTATED as the honest terminal state (Path C, zero cost) unless Duho specifically wants to
authorise a single low-cost documentary probe of the SDSS/CasJobs schema (Path A) before closing it. I have
resolved nothing and stated no convention; this only scopes the decision.