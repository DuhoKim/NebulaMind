# BHU lane — full-day wrap-up, 2026-08-30 (COLD-READABLE, supersedes WRAP_UP_20260830_OVERNIGHT.md)

Written for a session with zero recollection. The files ARE the memory — this one plus the
bibliography, the register, and OPEN_QUESTIONS are the whole state.

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

## WHAT THE NEXT SESSION PICKS UP FIRST

Nothing is solo-actionable and no question is open. On the next tick:
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
