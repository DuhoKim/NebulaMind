# BHU lane — full-day wrap-up, 2026-08-30 (COLD-READABLE, supersedes WRAP_UP_20260830_OVERNIGHT.md)

Written for a session with zero recollection. The files ARE the memory — this one plus the
bibliography, the register, and OPEN_QUESTIONS are the whole state.

## OVERNIGHT 2026-08-30→31 — FOUNDATION RECEIPTS (newest; for the 07:00 handover)

Quiet-hold was lifted for the night (Duho via Blanc, 22:08 KST: "flip Tori too"). The relay named
two items — the **Farhi & Guth full read** and the **PLB 690 pair disposition** — but BOTH were
already done earlier today (entry 48: `b45` 8/8, `AGATE_B45`+`CGATE_B45`, tier obstruction under
Q8; PLB 690 pair: `b49` 11/11, `CGATE_B49` ring-holds). No new source had landed — the "entry 48
source in the sources folder" is the 12:55 KEK scan already read. Same recurring stale
reading-plan pointer; the source-side annotation for it is in OPEN_QUESTIONS §5.

With the named queue already closed, worked the next genuine free-access category — **converting
the corpus's foundations from seat testimony into pinned, self-computing receipts** (no seat gate;
all in the battery, which went **69 → 72**):
- **`b56`** — entry 22's PUBLICATION fact (PRD 114, 044077) was "a seat's APS lookup, not a
  document"; now bound to a pinned Crossref record (`crossref_10.1103_qs86-npwk_entry22.json`).
- **`b57`** (5/5) — **corpus-wide publication audit**: before tonight NO entry had a pinned
  Crossref document. Fetched all 58 DOIs; **58/58 resolve to a published journal-article** with the
  claimed venue and volume (zero preprints-as-published, zero transcription errors). Receipt:
  `crossref_publication_audit.jsonl`. This is the "published journal papers only" base-layer rule,
  now receipted instead of asserted.
- **`b58`** (2/2) — **pin hash custody**: b44 proved cited pin *filenames* exist+tracked but never
  checked *content*; b58 confirms all 21 cited sha256 prefixes hash-match real file bytes (111
  pinned files), including the drift-prone Elsevier PDFs. Zero corruption.

**After these, the clean free-access queue is exhausted.** The one remaining free-access item is
**entry 54's Ω_K testimony** (record: "the cited DESI analysis *assumes* Ω_K = 0 — a seat's
testimony, not verified here; Tier UNCHANGED"). It is **seat-gated, not a solo receipt**: resolving
"assumes vs. constrains" needs a seat's read of the DESI/ACT papers entry 54 cites, and it is
falsifier-adjacent (the family's curvature prediction), so per Duho's overnight protocol it is left
for a seat/the tick rather than adjudicated solo. Tier-neutral, low priority. Everything else is
institutional-parked (holdouts 42/47, Silk registration, pre-2010 VoRs).

> **[2026-09-01 UPDATE — this "one remaining free-access item" is now CLOSED; do NOT re-dispatch
> it.]** Entry 54's Ω_K testimony was resolved the same day it was written: **B59-VERIFIED
> 2026-08-30** (agy + codex both `SOURCE_OVERSTATES_ACT_DESI_TIER_UNCHANGED`; ACT DR6 / DESI 2024-VI
> / DESI DR2 / Di Valentino 2020 abstracts pinned) — the "assumes vs. constrains" question is
> settled (DESI *fits* Ω_k and finds no preference, doesn't merely assume; the source's
> "same-direction trend" gloss overstates and for DESI reverses the sign), and **B61-VERIFIED**
> (curvature falsifier LIVE-but-UNFIRED, both seats). Bibliography §0 entry-54 block, lines
> ~904–919; **tier UNCHANGED. No open free-access audit item remains.** Also since read+tiered:
> holdouts 42 → CONSISTENCY-ONLY, 47 → PROSPECT (Duho 42a/47a, 2026-09-01); Silk 1997
> purchased + pinned 2026-08-31. The only parked acquisitions are the **5 pre-2010 paywalled
> versions-of-record on Duho's fetch** (Pathria, Good, Stuckey, Knutsen, Frolov–Markov–Mukhanov).

## What this lane is

An adversarial audit of the **black-hole-universe (BHU) published bibliography** — 58 numbered
entries = **51 BHU papers + 7 support-role papers**. Each paper is read against ONE preregistered
rule (b28): *does it PROVE that no member of a stated model class satisfies a stated conjunction,
refutable by counterexample not measurement?* Every adjudication is gated by two independent
adversarial seats (agy = Gemini 3.1 Pro via tmux `agy-meter:0.0`; codex = gpt-5.6-sol via
`codex-meter:0.0`), verdicts written to `<A|C>GATE_*_VERDICT.md`. A pre-commit control
`check.py` runs the whole battery (63 scripts today) + a negative-assertion sweep; commits are
gated on it (`python3 check.py && grep … && git commit …`).

Key paths (all relative to the repo root `/Users/duhokim/NebulaMind/NebulaMind`):
- lane / scripts / gate briefs / verdicts: `.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-acquisition-20260828/`
- the record: `.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-published-bibliography-20260819/BHU_PUBLISHED_BIBLIOGRAPHY.md`
- pinned sources: `.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-reading-20260823/sources/`
- defect register: `HARNESS_DEFECT_REGISTER.md` (classes through 1ai)
- open items for Duho: `OPEN_QUESTIONS_FOR_DUHO.md`

## FINAL CORPUS STATE (parsed from the record, not recited)

| tier | count | which |
|---|---|---|
| CONSISTENCY-ONLY | 32 | — |
| QUALITATIVE-DIRECTIONAL | 7 | — |
| CALIBRATED-FALSIFIER | 4 | **7, 44 FIRED · 31, 51 LIVE** |
| THEORETICAL-OBSTRUCTION | 3 | **5, 22, 48** |
| PROSPECT | 3 | incl. 16 |
| UNREAD | 2 | **42, 47 only** |
| support (no tier) | 7 | 29, 30, 32, 33, 34, 35, 58 |

**58 total. Every READABLE paper is read, adjudicated, and double-gated.** The only unread are
42 and 47, both Purchase-only (see holdouts). Battery: 63 checks green.

## THE DAY'S ARC

1. **Census closed and survived audit.** Proved 39/39 readable papers adjudicated by
   receipt-bound set arithmetic (b41). Refuted by BOTH seats on different holes, repaired across
   FIVE versions (v1→v5) until the refuting seat confirmed. Measured the screen's miss rate
   nobody had: **1 of 2** (missed entry 5), precision 1 of 3 flags — over the closed readable-39
   frame.
2. **All EIGHT delegated questions closed** (Duho returns each with "answer question N", the
   established delegation pattern; each ruled-and-gated in OPEN_QUESTIONS format). The last,
   **Q8: entry 48 (Farhi & Guth) → THEORETICAL-OBSTRUCTION** — the cleanest proof-owner in the
   collection; preprint caveat + revisit-on-VoR clause printed.
3. **The obstruction/escape web completed end-to-end, every link source-owned:** classical no-go
   (48) ↔ limiting-curvature escape (13/14, read today) ↔ quantum-tunneling escape (50, read
   today) ↔ modern continuation (16). Entry 48's theorem is STRONGER than the corpus had it
   (null EC, not WEC).
4. **The free-frontier acquisition sweep** (Blanc's 5 routes) took the twelve-paper wall mostly
   down at zero cost — KEK scanned-preprints and SCOAP3 gold-OA delivered where arXiv could not.
5. **Entry 51's PLB 690 sourced end-to-end** through Duho's browser: version-of-record +
   2013 erratum. VoR is word-for-word identical to the arXiv preprint on every mass-floor number
   (so "10^16 kg is an error" is NOT a version artifact); the erratum corrects the Papapetrou
   ring machinery (Eqs 21/26/29) NOT the floor — both seats ran the corrected Eq. (29) and
   confirmed the ring exclusion HOLDS.

## ACQUISITION TALLY (all pinned + force-added past the .pdf gitignore; receipts in ACQUISITION_ROUTES_20260830.md)

| entry | paper | route | pin (sha256 prefix) | read/gated |
|---|---|---|---|---|
| 48 | Farhi & Guth, PLB 183 (1987) | KEK scan (KEKSCAN 2000-36-705) | `farhi_guth_mitctp1400_kekscan_2000_36_705.pdf` 573ff9751cec | READ, double-gated, TIER=obstruction (Q8) |
| 14 | Frolov-Markov-Mukhanov, PRD 41 (1990) | KEK scan of ICTP IC/88/91 | `frolov_markov_mukhanov_ic8891_kekscan_2000_33_351.pdf` 1dcb755eb0af | READ, double-gated (CONSISTENCY-ONLY) |
| 50 | Farhi-Guth-Guven, NPB 339 (1990) | KEK scan (CTP-1690) | `farhi_guth_guven_ctp1690_kekscan_2000_36_692.pdf` 32e93d710705 | READ, double-gated (CONSISTENCY-ONLY) |
| 32 | Brown & Bethe, ApJ 423 (1994) | ADS full page scan | `ads_1994ApJ_423_659_brown_bethe.pdf` 4b1cbae677de | byline read visually, double-gated |
| 33 | Harada-Yamawaki pair | arXiv ar5iv + abs | `ar5iv_0010207.html`, `arxiv_0302103_abs.html` | support-layer byline closed |
| 16 | Pourhassan, NPB 1020 (2025) | ScienceDirect SCOAP3 gold-OA (Chrome) — the **version of record** | `pourhassan_2025_npb1020_117160_scoap3.pdf` 2d11feddb342 | READ, double-gated (PROSPECT); single-author (et-al was wrong) |
| 51 | Poplawski PLB 690 (2010) **VoR** | ScienceDirect Open Archive (Chrome) | `poplawski_plb690_73_2010_vor.pdf` 747bce6d54d4* | compared to preprint (identical), gated |
| 51 | Poplawski PLB 690 **2013 erratum** | ScienceDirect (Chrome) | `poplawski_plb690_erratum_2013.pdf` dafedba1ce9e | read, both seats confirm ring exclusion holds |

\* Elsevier stamps a per-download timestamp so the VoR/erratum hashes DRIFT between fetches;
content is verified by page-1 identity + number-for-number comparison, not a stable byte hash.

Browser-acquisition mechanics learned (register + ACQUISITION_ROUTES): Chrome's native
PDF-viewer download arrow beats the multi-download JS guard (programmatic `a.click()` is blocked
after the first); Elsevier signed S3 URLs live ~5 min — re-mint immediately before the click;
`~/Downloads` is SSH-readable from this Studio, `~/Desktop` is TCC-blocked to every agent path;
bulk byte-pull through the browser extension is output-filter-blocked and was NOT circumvented.

## HOLDOUTS — Duho only, nothing solo-actionable (full table in OPEN_QUESTIONS_FOR_DUHO.md)

| entry | paper | journal, year | cheapest lawful route |
|---|---|---|---|
| 42 | Gonzalez-Diaz | PLB 261, 1991 | interlibrary document-copy (pre-2010 PLB = Purchase-only) |
| 47 | Sato-Kodama-Sasaki-Maeda | PLB 108, 1982 | interlibrary document-copy |
| 1 | Pathria | Nature, 1972 | interlibrary document-copy |
| 2 | Good | Physics Today, 1972 | interlibrary document-copy |
| 3 | Stuckey | Am. J. Phys., 1994 | author email or ILL |
| 4 | Knutsen | Grav. Cosmol., 2009 | interlibrary document-copy |
| 18 | Dymnikova | Gen. Rel. Grav., 1992 | author email or ILL |
| — | Silk (entry 31's last critic) | Science 277, 1997 | free WITH free registration at science.org — account creation is Duho's |
| — | 48/50 VoR comparisons | PLB 183 / NPB 339 | Purchase-only (pre-2010) — preprints already held+read; ILL if wanted |

Never list price; ILL is a few thousand won/item. Entries 42 and 47 are the only two that are
BOTH unread AND holdout — the rest are already read from preprint/scan and the holdout is only a
version-of-record nicety.

## REGISTER STATUS

`HARNESS_DEFECT_REGISTER.md` current through class **1ai**. Today added:
- **1ah** — the record cited PDF pins git was silently dropping (`.hermes/**` re-admits by
  extension, `.pdf` absent); NINE force-added, `b44_pin_custody.py` now guards it in the battery.
- **1ai** — appended new state while leaving the old state standing (three CGATE catches: entries
  48, 50, 16 each had "unread/unverified" left above the read record); fix = grep the same block
  for superseded phrases on any state change; battery checks assert their absence.
- Plus the download-channel write-up in ACQUISITION_ROUTES (base64/hex output filter + CSP +
  Desktop TCC = same wall three ways, stopped per the failure rule, not circumvented).

## STATUS MARKERS

- `OPEN_QUESTIONS_FOR_DUHO.md`: **OPEN — none.** All eight delegated questions closed. Standing
  dependency = the holdout table above (his ILL/registration calls). The Chrome-click item is
  DONE (entries 16 + PLB 690 pair acquired through it).
- Front commit at wrap time: see `git log -1`. The day ran ~98 commits; the last content commit
  before this wrap was `35866c415` (erratum gate closure) → `62113908f` (evening wrap section).

## SUPPORT-LAYER CONTENT VERIFICATION — SWEEP CLOSED 2026-08-30

The 7 support entries (29, 30, 32, 33, 34, 35, 58) were BYLINE-verified (b42) and pinned, but
their CONTENT — the specific measurement/mechanism each SUPPLIES to a falsifier — had never been
bound to the source. This sweep bound every one. **No support paper contradicted what its
falsifier imports** (the STOP-for-Duho trigger never fired); the checks are self-computing string-
presence (no seat gate), added to the battery (b50–b55), which is green at **69**.

| entry | paper | load-bearing claim bound to source | check |
|---|---|---|---|
| 29 | Demorest 2010 + Fonseca 2021 | PSR J1614-2230 = 1.97 ± 0.04 M⊙ and PSR J0740+6620 = 2.08 M⊙ — the two ~2 M⊙ pulsars operating entry 7's CNS falsifier; bound to pinned full texts (was byline-only) | b52 6/6 |
| 30 | Brown-Lee-Rho Phys.Rept. 2008 | the 4% double-NS asymmetry limb (Sec 3.2) + 0.1–0.2 M⊙ He-red-giant proviso, verbatim | b50 4/4 |
| 32 | Brown-Bethe ApJ 423 1994 | **cannot be text-bound** — 6-page image scan, no OCR layer; bound by CUSTODY + honest image-only status (M_max≈1.5 stays VISUALLY attested, never machine-greppable) | b55 3/3 |
| 33 | Harada-Yamawaki PRL 2001 | the vector-manifestation prediction "gauge coupling approaching to zero" near chiral restoration — moves link (1) of entry 7's chain from ASSUMED-FROM-CITATION to source-verified | b53 4/4 |
| 34 | Ferdman 2020 | masses 1.62/1.27 ± 0.03 M⊙ + He-star/ultra-stripped channel, verbatim | b51 (34 leg) |
| 35 | Tauris 2017 | **derived-not-quoted catch:** Tauris supplies the framework (Case BB, recycling, hypercritical/Eddington) but the ΔM_NS ≈ 0.0134 M⊙ TOTAL is the auditor's Track-B-gated SUM, NOT a Tauris quote — record relabelled | b51 (35 leg) |
| 58 | Longo 2011 PLB 699 | **acquired this session at zero cost** (arXiv 1104.2815 abs page, was byline-only/no pin): dipole asymmetry −0.0408 ± 0.011 (chance 7.9×10⁻⁴), axis (l,b)≈(52°,68.5°) near WMAP, SDSS 15158-spiral sample — the amplitude the DESI spin-parity campaign tests | b54 5/5 |

Two findings worth the eye: **(35)** the only derived-vs-quoted distinction — a total that reads
like a source number but is the gated Track-B derivation, now labelled so; **(58)** a free arXiv
acquisition that upgraded a byline-only entry to a content pin. Neither is a discrepancy; both are
recorded honestly.

## AFTER THE SUPPORT SWEEP / IF IT STALLS

Nothing else is solo-actionable and no question is open. On the next tick:
1. **Quiet-hold check** — `git fetch` for incoming commits; `ssh duhokim@100.75.47.116 'find
   ~/Downloads -name "*.pdf" -mmin -30'` for a new drop. If both empty → one-line "staying
   stopped", nothing else.
2. **If Duho supplies a holdout PDF** (42/47/1/2/3/4/18/Silk, or a 48/50 VoR): pin+hash+force-add,
   clean-extract, read under the b28 rule, dispatch both gates, record, commit. For 42 and 47
   that MOVES them out of UNREAD → a tier is a STOP-for-Duho item (write to OPEN_QUESTIONS).
3. **If Duho reopens acquisition**: the browser route works (native download arrow, re-mint the
   signed URL ≤5 min before the click, pull from `~/Downloads` over SSH).

Do NOT re-attempt the blocked bulk-byte-pull channel (failure rule; written up). Do NOT chase the
Desktop-saved files (TCC-blocked). Do NOT manufacture work — idling beats it.

## TICK NOTE 2026-08-31 — Downloads drop-check host is unreachable (failure-rule write-up)

`ssh duhokim@100.75.47.116 'ls ~/Downloads/*.pdf'` timed out on TWO consecutive ticks
(`Operation timed out`, port 22): the drop-host (Duho's laptop) is asleep or off-tailnet. Per the
failure rule I am NOT SSH-retrying it a third time on following ticks — the drop-check is suspended
until a positive signal the host is back (a Duho message, or the host answering again). Transient
environment, not a lane defect: a holdout PDF (42/47/Silk) dropped now is simply invisible until the
laptop rejoins the tailnet, at which point a later tick's check picks it up. Everything else is
unchanged this tick: branch in sync with origin (0 0), `/lab/bhu` live (pin 117a5273b), corpus
complete + gated, OPEN_QUESTIONS empty.
