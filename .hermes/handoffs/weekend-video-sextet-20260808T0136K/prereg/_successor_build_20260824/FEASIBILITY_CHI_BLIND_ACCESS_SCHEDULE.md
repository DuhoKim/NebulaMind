**STATUS: ANSWER — for the principal, via Blanc. Asked 22:24 KST: does anything in the acquisition plan
actually REQUIRE choosing the next object on the strength of a previous object's χ-derived output?**
**This reports what is, not what should be done. It contains no recommendation and does not choose
between (a), (b) and (c).**

# Is the adaptivity load-bearing?

## The answer in three lines

- **Row D — NO, and this is established from code, not inference.** The runner has no retry, no
  re-request and no reordering of any kind, and the directory states it "contains no acquisition or
  selection query."
- **Row G — NO for choosing what to view next, which the design forbids; YES for ONE mechanism,
  `flag → discard → replace`, which HC-1H calls "the only escape hatch" for identity exposure.**
- **Stopping rules — nothing stops early on results so far in a way that selects a next object, but
  three preregistered halts do depend on χ-derived aggregates, and one of them is the §2b pilot.**

---

## 1. Row D — the cutout pipeline

**How this was established: by reading the code that exists** — `_cutout_runner_20260820/cutout_runner.py`,
`incremental_wrapper.py` and the directory's `README.md` — **not from the conduct table.**

- **There is no acquisition or selection query in it at all.** The README states the scope: *"local/offline
  composition only. This directory contains no acquisition or selection query. It accepts an explicit
  `ra,dec,ls_id` CSV and an explicit receipt-pinned brick manifest."*
- **The read set is exactly the supplied list.** The runner refuses unless
  `set(manifest) == {position.ls_id for position in positions}` — no object may be added or dropped.
- **The order is the order it is given.** `for position in positions:` over the CSV as read; the
  incremental wrapper takes `sorted(set(objects) - done)[:BATCH_LIMIT]` — **sorted by identifier**, and
  its selection depends only on **whether** an output already exists, never on that output's value.
- **There is no retry.** A per-object failure is caught, `failures += 1`, and the loop advances. No
  backoff, no re-request, no requeue.
- **Nothing is downstream of a computed per-object output.**

**Two limits on this answer, stated rather than smoothed.** This is the **composition layer**; the
acquisition step that fetches bricks is not in the lane, so I can say nothing about code that does not
exist. And **BS-3, Row D's authorising instrument slot, is not delivered** — so this runner is not
established as the pinned Row D implementation. **What is established: nothing that exists is adaptive,
and nothing in Row D's stated surface asks for adaptivity.**

## 2. Row G — the hand check

**How this was established: from HC-1H's defining artifact** — `LANA_ONE_HUMAN_ATTENUATION_20260814.md`,
accepted 2026-08-15 at SHA-256 `b2590e42…` per `HC1H_ACCEPTANCE_20260815.md` — **read directly, because
the draft carries these rules only "by quotation at freeze" and they are not quoted in it yet.**

**Choosing what to view next is not merely unnecessary here — the design forbids it.** HC-1H is *one
human checker, 850 blinded labels*: 500 real, **200 blind synthetic injections "interleaved unmarked"**,
and **150 mirrored re-presentations "in randomized later positions"**, with *"every image — real,
synthetic, repeat — presented in random parity with a sealed key"* and *"the key opens only after all
850 labels are in."* Sessions are capped at ≤ 50 images and the re-presentations are deliberately placed
late so drift shows as a rising ε̂_rr across session index. **The sequence is constructed by the design.
The blinding assumption — that the checker cannot tell synthetic from real or first-showing from repeat
— is called "load-bearing" in that document, and a checker who chose their own order would be selecting
which items get re-shown.**

### The one mechanism that IS load-bearing, named exactly

**`flag → discard → replace`.** HC-1H, verbatim: *"the labelling interface carries a **flag** action; if
the checker flags specific items as suspected-identifiable during the session, before key opening, those
items are discarded, the flags logged, and **fresh draws from the same stratum and category substituted**
before the key opens."*

**So the set actually labelled depends on the checker's in-session, content-derived judgements.** The
allocated universe is fixed; the realised set is not.

**What it would cost to give it up, in the source's own terms.** It is *"the only escape hatch"* for
HC-7 trigger (v), identity exposure. HC-1H: *"No other path repairs an exposure: identity leakage
discovered after key opening, or systematic exposure (a whole session or category recognisable), is not
item-discardable and returns **hard INCONCLUSIVE for the affected batch**."* **Removing the flag rule
converts a repairable in-session problem into a run-level inconclusive**, and the rule was added
deliberately — at Revision 4, on Kun's re-gate, because the blinding assumption *"was load-bearing but
unenforced."*

**What I have NOT established, and will not assert either way:** whether exercising that flag actually
carries χ. The flag responds to *identity* cues — "this looks synthetic", "I have seen this before" —
not to handedness, and *"no instrument signs [are] visible at any point."* But the checker forms a
handedness judgement on every image and flags after viewing, so I cannot rule out that the propensity to
flag correlates with image properties that also correlate with χ. **That is a question about human
judgement that I cannot settle by reading files, and it is the part that would need the person who
designed the procedure.**

## 3. Stopping rules

**How this was established: from the draft's conduct table and from HC-1H.**

- **No early stop on the labelling itself.** *"The key opens only after all 850 labels are in."* The
  incremental wrapper stops a round when it resolves nothing new — a **stall detector**, not a result
  criterion.
- **The §2b optional pilot is a genuine continue/stop gate on χ-derived aggregates.** 150 labels
  returning only `PASS-TO-FULL-HC1H` or `INCONCLUSIVE`, on *"protocol executes cleanly; session
  ergonomics acceptable; **ε̂ crude estimate < 0.10**; no HC-7 trigger."* It decides **whether to
  continue at all**, never which object comes next — and it is preregistered.
- **Two preregistered halts already depend on χ-derived aggregates and are already accepted as such.**
  Row I must fail the run before BS-8f if any allocated object lacks a usable finite instrument output —
  the draft already records the cost: *"leaking that at least one allocated object was
  missing/non-finite, which we accept."* And Row J halts on `a_LB_b < 0.85`.
- **Worth noting because it is the same class, already handled:** HC-1H's carry-forward was corrected at
  Revision 3 precisely because *"a criterion referencing real-label agreement or retest non-flip values
  would exclude those labels too."* **The designers have met this problem once and fixed it.**

## 4. Other places to look — you asked, so here are the ones beyond your three

- **Row C2** reads *"only cutouts via row B and **fixed parent lists**"* — fixed by construction.
- **Row I** reads the sealed label set and the instrument outputs corresponding to it; its read set is
  the **sealed allocation**. Fixed.
- **Row F, the allocation itself — and here I found something I could not resolve.** §6.3 says the 3 × 9
  allocation uses *"V3-pred's nine HC strata"*, and HC-1H defines those strata as **machine-committee
  state (3) × |χ| tertile (3)**. But Row F's cell says it *"reads the accepted partition's positions and
  acceptance flags only **(χ-free)**"* and voids the run on *"any χ-bearing input to bin construction."*
  **Those cannot both hold if the HC strata are |χ|-tertile-defined.** If the allocation is χ-derived,
  then the *universe* Row G sees is χ-conditioned before any question of sequence arises — which is
  upstream of the leak under discussion. **I am flagging this, not asserting it:** it may be that this
  draft redefined the strata, and I have not found where it says so.

---

**Nothing in this report is evidence about the sky.** No χ has been read. **v9 stays frozen at
`6a9abbbd`; BS-6 and the first image byte remain blocked.**
