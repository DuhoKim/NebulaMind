# KUN_FRAME_REVIEW.md — Independent verdict review, frame question (A3.8 §3, per frozen A3.9)

Reviewer: KUN (adversarial critic / reproducibility-forensics seat; findings-only).
Lane: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/spin-parity-census-20260805T1922K
Drafted record under review: VERDICT_RECORD_FRAME_DRAFT.md (sha256 b33d6468e71c1699…, as opened).

## FIRST-OPENED LEDGER (binding-order compliance)

Order rule: source texts first, own branch, THEN the drafted record. A branch filed after the
drafted record was opened is a comparison and does not clear. Actual first-opened order:

1. 2026-08-06T15:53Z — sha256 verification of receipt files (no content opened):
   - _lit_cache/lintott2011.pdf = 875ed17bf1f42cbe144c7c31ae0e41d4bfb2be00f7f6fb0a5679c08ca6b9c582
   - _lit_cache/land2008.pdf = a4f5e81eb58c21d0fbe0aa4d0edda0e2e24e01dd6b7726bb01d97b6580721df0
   - AMENDMENT_A3.9_DRAFT.md = 817eec46269643e636082b76412ed550b29ffd44119f5adec1d42cf5bb2c972a
   - FRAME_RETRIEVAL_BRIEF.md and VERDICT_RECORD_FRAME_DRAFT.md hashed, NOT opened.
2. 2026-08-06T15:54Z — _lit_cache/lintott2011.txt OPENED FIRST (full 3,529-line read, batches).
3. 2026-08-06T15:54Z — _lit_cache/land2008.txt OPENED (full 858-line read; completed 15:56Z).
4. 2026-08-06T15:57Z — keyword sweep #1 of both texts (mirror/frame/convention/swap/as seen/
   as displayed/de-mirror/record/stored/archiv).
5. 2026-08-06T15:58Z — OWN BRANCH REACHED AND WRITTEN to this file (skeleton). No coordinator
   document opened before this point; the only rule text in hand at branch time was the A3.9 §5
   definition and [E5] as quoted inside the binding order itself.
6. 2026-08-06T15:59Z — AMENDMENT_A3.9_DRAFT.md (frozen rulebook) opened, read first; then
   VERDICT_RECORD_FRAME_DRAFT.md opened (drafted record) — both AFTER the branch was locked.
7. 2026-08-06T16:00Z — keyword sweep #2 (flip/reflect/orient/handed/chiral); then coordinator
   summaries FRAME_RETRIEVAL_BRIEF.md (444) and _KUN_FRAME_REVIEW_BRIEF.md opened.
8. 2026-08-06T16:01Z — lane artifacts opened: T2_MIRROR_BIAS.json, T2_MIRROR_LOG.txt,
   LANA_T3_REDERIVATION.md; _gz_cache listing.
9. 2026-08-06T16:02Z — _gz_cache/ReadMe opened (header lines 1–9; table5 field labels).

## RECEIPTS (quoted as ordered)

- lintott2011.pdf sha256 875ed17bf1f42cbe144c7c31ae0e41d4bfb2be00f7f6fb0a5679c08ca6b9c582 (arXiv:1007.3265v4, arxiv.org, 401,378 B, HTTP 200)
- land2008.pdf sha256 a4f5e81eb58c21d0fbe0aa4d0edda0e2e24e01dd6b7726bb01d97b6580721df0 (arXiv:0803.3247v4, arxiv.org, 402,170 B, HTTP 200)
- A3.9 (frozen) sha256 817eec46269643e636082b76412ed550b29ffd44119f5adec1d42cf5bb2c972a — full 64-hex match to the order; its §4/§5 text as opened matches the order's paraphrase verbatim in substance.

## 1. THE FRAME — own branch: FRAME_UNSTATED (reached pre-draft, before the record was opened)

Strict application of A3.9 §5: an ESTABLISHMENT is a verbatim statement of the recording or
archival convention of the stored direction fields (pcS1/paS1/pcS2/paS2 = ReadMe table5 "Mirrored
1/2 fraction of votes for ClockWise/AntiClockWise"; pcSm/paSm = table6 monochrome). A quoted
description of the mirroring PROCEDURE is not one.

My independent search of both documents (full reads + two disjoint keyword sweeps):

- LINTOTT 2011 — silent. Every mirror-bearing passage is procedural:
  (i) the bias-study introduction ("mirrored and greyscale images were introduced to the site
  from 28 November 2007") — §2.1, confirmed as §2.1 by Lintott's own internal cross-reference at
  §4 ("As discussed in Section 2.1, while the introduction of mirrored and monochrome images…");
  (ii) §4's combination statement ("the measurements obtained during this bias study have thus
  not been combined with the main data set"); (iii) Table 5 note ("Galaxies were shown mirrored
  about the vertical and diagonal axes ('Mirrored' and 'Mirrored 2'). For each transformation we
  provide the total number of votes (Nvote) and vote fractions … as defined in the comments for
  Table 2"); (iv) Table 6 note; (v) Table 7 note. None states whether stored CW/ACW for mirrored
  images are as-displayed or de-mirrored. No occurrence of frame/convention/swap/as-seen/
  de-mirror language anywhere in the text.
- LAND 2008 — silent as an establishment source. All mirror passages describe the experiment
  (91,303 objects; monochrome + vertically mirrored + diagonally mirrored; mirror votes combined)
  or state an analysis expectation ("we … expect to see this average class-weights to switch over
  for the mirrored images", §2.2). Land publishes no catalogue fields. Per [E5] Land alone cannot
  establish regardless.
- FRAME_CONFLICT does not fire: it requires two papers stating different conventions; neither
  states any (and A3.9 struck the ReadMe-conflict clause — silence cannot be contradicted).
- REVIEW_INCOMPLETE does not fire: both documents retrieved whole with five-field receipts
  (verified against the receipt JSONs and the order's sha256 prefixes), so [E2]'s whole-retrieval
  bar is met; Lintott is not internally self-contradictory on the point — it says nothing on the
  point, which is UNSTATED, not the fits-none net.
- Recorded so the silence claim is not confused with an uninformative-data claim: the printed
  Table 5/6 rows contain objects whose stored CW/ACW flip wholesale between Monochrome and
  Mirrored blocks (e.g. ObjID 587731186203951111: Monochrome CW 0.883/ACW 0.025 vs Mirrored CW
  0.033/ACW 0.91) — data-level evidence consistent with as-seen recording, but an inference from
  data is not a verbatim establishment and does not move the branch under §5.

Checks the order asked for, on the drafter's use of the rules:
- [E5] used correctly, not hidden behind. The draft argues BOTH independent prongs for Land
  (inference-is-not-quotation [§4 ¶2] AND Land-alone-cannot [E5]), and affirmatively discloses the
  strongest as-seen evidence — that Land's switch-over expectation is coherent only under an
  as-seen working frame. Concealing that passage would have served FRAME_UNSTATED; the drafter
  printed it instead. That is the opposite of hiding behind the rule.
- Under-reading check (the draft asked: "must check whether I under-read Lintott to avoid
  FRAME_DEMIRRORED"): I searched Lintott specifically for any sky-frame/de-mirror/normalised-
  direction statement. None exists. No under-reading found.
- Completeness nit (not a branch defect): the draft's Lintott quotation set ("the only ones
  bearing on the bias-study columns") omits the §4 combination statement and the Table 6/Table 7
  notes. My enumeration covers them; none bears on the frame. Silence conclusion unchanged.
- Citation nit: the draft labels Land's switch-over passage "(§4)"; the passage is in Land §2.2
  (The Bias Study) — Land's §4 is Conclusions. The quotation itself is verbatim-exact (verified
  character-for-character, including Land's grammatical glitch "this average class-weights").
  The draft's "§2.1" label for the Lintott sentence is CORRECT (Lintott §4 self-cites it as §2.1).
- Reviewer-naming verified: FRAME_RETRIEVAL_BRIEF.md (mode 444, names KUN) predates the PDF
  payload receipts at file-timestamp granularity (brief 00:49; payloads 00:50 KST).
- Identifier cross-checks verified independently: Land retrieved = arXiv:0803.3247v4, matching
  A2's frozen record (0803.3247v4 = MNRAS 388, 1686; also Lintott's own reference list entry);
  Lintott title matches the cached ReadMe header (lines 1–4, J/MNRAS/410/166, 2011MNRAS.410..166L).

## 2. THE CONFLICT FINDING — checked hard

Quotations verified verbatim against the receipt-pinned source:
- Land body (§2.2): "(5.5%, 6.0%) for the monochrome images … we find average class-weights of
  (5.6%, 5.9%) for the mirrored images - which still displays a significantly higher S-wise
  average weight, at ∼ 3σ." — exact. Full-precision table values behind the rounding:
  monochrome 5.525/6.032 → mirrored 5.646/5.942 (Land Table 2).
- Land Table 2 caption: "the average class=2,3 weights do not reverse between the monochrome and
  mirrored images, therefore indicating that there is a bias effect in the data." — exact.
- The lane's side: T2_MIRROR_BIAS.json counters (verified against the artifact), re-derived by
  Lana to REVERSES at |ΔA|/σ = 6.45–6.95 across both rungs (0.80/0.60) and both mirror sets:
  A_normal = −0.0679/−0.0612 flips to A_mirrored ≈ +0.040–0.046, monochrome ≈ normal (−0.066).

Is the drafter's framing honest — genuine empirical conflict, or fully explained and overstated?

MY VERDICT ON THE FRAMING: HONEST. It is a genuine empirical conflict at the level of the
recorded numbers, and it is NOT fully explained on the current record — though the explanation
class is live, concrete, and unverified. Reasons:

(a) The two numbers answer different questions on differently-weighted populations. Land's
    Table 2 is a population-average class-weight swap test over an effectively-random re-weighted
    subsample (Land footnotes 3–4); the lane's is a dominance-thresholded sign test over the
    77.6% zooSpec-matched — hence superclean-heavy — subset (T2 coverage 0.77555, N=70,810).
    "Same 91,303-object sample" is true in provenance, not in weighting.
(b) Land's own paper demonstrates that the answer is estimator/population-sensitive ON THIS SAME
    SAMPLE: averages do not swap (5.5,6.0 → 5.6,5.9 — but note the +0.21pp partial move in the
    mirror direction inside Land's own table); clean counts move toward parity without flipping
    ((839,923) → (864,905)); the before-AND-after cut lands on exact parity ((739,739) — "the
    bias effect can account for the excess exactly"). Three cuts, three strengths of the effect.
    A fourth cut flipping sign (this lane's) is surprising but not a logical contradiction.
(c) A concrete form of the population explanation is visible in the lane's own counters:
    mirrored_1 N_CW at 0.80 (3,659) equals monochrome N_ACW (3,659) to the object — wholesale
    label-flipping among dominance-classified (i.e. visually clear) objects, exactly what
    image-following votes predict for that subpopulation, while Land's effectively-random cut
    (dominated by marginal objects, where the classifier S-preference lives) does not flip.
    Recorded as an observation only: the per-object paired flip counts that would quantify this
    are the gated new measurement the draft correctly says nothing here authorises.
(d) Because (a)–(c) are plausible but undemonstrated, the draft is right to record the finding
    adversely and prominently ("far more serious than the frame question"; "a consequence I am
    not entitled to dodge"), and right to forbid itself Land-comparative phrasing. Not
    understated. Not materially overstated either: it lists the candidate reconciliations itself
    and marks every one "none verified."
(e) Two phrasing flags, neither self-serving: (i) "a direct empirical conflict, not a difference
    of interpretation" over-asserts — whether the conflict survives estimator harmonisation is
    precisely the unverified step, and the draft says so one sentence later, so the over-assertion
    is self-correcting and runs AGAINST the drafter's own reading; (ii) the reconciliation bullet
    "Land uses vote-weighted average class-weights" mislabels the weighting — Land's Table 2 uses
    UNWEIGHTED votes ("we herein use the unweighted results", Land §2) with the superclean portion
    up-weighted to emulate a random subsample (footnote 3). The load-bearing claim (Land's
    statistic is not this lane's statistic) is correct either way.
(f) Draft's reconciliation facts verified against the artifacts: 77.6% matched subset (T2:
    70,810/91,303 = 0.77555); n_below_nvote = 759 in the normal leg, 0 in all three bias legs
    (T2 counters; Lana §4.2.3); "Land's own statistic is not this lane's statistic" (Lana §4.3
    (vi)). All check out.

## 3. OVER-CLAIM / UNDER-CLAIM AUDIT

- More than the frozen rules allow: NOTHING FOUND. The drafted branch is one of the four
  pre-registered outcomes; the stated consequences match A3.9 §5 UNSTATED and [E6]'s fenced
  instrument reading with no Land-comparative phrasing; the separate conflict finding adjusts no
  measurement, threshold, or pin and defers action to a new gated amendment — a noticing, not a
  prohibited "use" of the literature for another question (suppressing an adverse noticing from a
  lawfully retrieved document would be the worse violation).
- Less than the evidence requires: the branch is not under-claimed — silence is complete in both
  documents and the draft does not manufacture FRAME_CONFLICT out of it (A3.9's struck clause
  respected). What is under-delivered is citation hygiene, itemised in §1 above: Land "(§4)" →
  §2.2; the Lintott quotation set should enumerate the §4/Table 6/Table 7 notes when making a
  silence claim; "vote-weighted" → unweighted-with-reweighting. None moves the branch; all should
  be fixed before the record is finalised.

## VERDICT

Own branch (reached from the source texts before the drafted record was opened, ledger above):
FRAME_UNSTATED. The drafted record branches FRAME_UNSTATED. On review of the drafter's rule use,
quotations, silence claim, conflict framing, and claim bounds as itemised above:

FRAME REVIEW: AGREES FRAME_UNSTATED
