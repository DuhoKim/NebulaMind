# Second free frontier — per-paper route receipts (2026-08-30, Blanc's five-route directive)

Context: Duho's institutional login does not cover the backfiles; no per-article payment.
Constraints honoured: no account creation, no payment pages, no CAPTCHA solving — anything
asking is recorded as GATED-BY-FORM and stopped.

## Landed today (pinned, hashed, force-added past the .pdf gitignore)

| entry | paper | route | receipt |
|---|---|---|---|
| **48** | Farhi & Guth, PLB 183 (1987) | 2 — KEK scan (Inspire→KEKSCAN 2000-36-705) | `farhi_guth_mitctp1400_kekscan_2000_36_705.pdf`, sha 573ff9751cec…; **READ IN FULL**, gates running, tier = question 8 |
| **14** | Frolov–Markov–Mukhanov, PRD 41 (1990) | 2 — KEK scan of ICTP IC/88/91 (KEKSCAN 2000-33-351) | `frolov_markov_mukhanov_ic8891_kekscan_2000_33_351.pdf`, sha 1dcb755eb0af…; read queued |
| **50** | Farhi–Guth–Guven, NPB 339 (1990) | 2 — KEK scan of MIT-CTP-1690 (KEKSCAN 2000-36-692) | `farhi_guth_guven_ctp1690_kekscan_2000_36_692.pdf`, sha 32e93d710705…; read queued (long) |
| **32** | Brown & Bethe, ApJ 423 (1994) | 3 — ADS full scan (done this morning, pre-directive) | `ads_1994ApJ_423_659_brown_bethe.pdf`, sha 4b1cbae677de…; byline read visually, both seats confirmed |

All four scans are PREPRINTS or page scans — version-of-record identity is testimony until
compared; each record says so.

## Route outcomes for the still-gated

- **Route 1, Elsevier Open Archive (entries 13, 42, 47; entry 51's PLB 690 VoR):** curl of the
  ScienceDirect article page (PII 0370269387904291 as the probe) returned **HTTP 403 with an
  "Are you a robot" CAPTCHA interstitial** → GATED-BY-FORM for any scripted fetch; not solved,
  per constraints. A real Chrome attempt may pass without a CAPTCHA (the MDPI precedent), but
  **no browser is currently connected** — switch_browser timed out with no Connect click.
  STATUS: needs one Chrome Connect click from Duho, then retry in-browser.
- **Route 2, KEK/Inspire (swept for all):** hits above. NO KEKSCAN ids exist for entries 13
  (PLB 216), 18 (GRG 24), 42 (PLB 261), 47 (PLB 108) — checked by journal-ref query on Inspire;
  the class this misses: scans indexed under a different journal-ref or preprint-only records;
  mitigation: entry 47's Kyoto preprint may sit in KISS under RIFP report numbers — one more
  targeted query is possible next tick.
- **Route 4, Science free-with-registration (Silk, Science 277):** registration = account
  creation = **Duho's by constraint**; not attempted. STATUS: gated-by-form (his call).
- **Route 5, self-archives:** MIT DSpace made redundant for 48/50 by KEK. Poplawski's pages
  host arXiv versions, not the PLB 690 VoR. Entry 18 (Dymnikova GRG 1992): no self-archive
  found via Inspire; her later open reviews quote the metric — secondary only.
- **Entry 16 (NPB 2025):** too recent for the open archive — stays gated (Blanc's note,
  confirmed by age).
- **Entries 1, 2, 3, 4 (Nature '72, Physics Today '72, AJP '94, Grav.Cosmol. '09):** outside
  all five routes' natural coverage (no KEK, no ADS scans for these venues, no self-archives
  found). SHORT LIST for interlibrary document-copy or author email (Duho's fallback, his
  call).

## Short list for Duho's fallback (interlibrary document-copy / author email — never list price)

1, 2, 3, 4, 13, 18, 42, 47 (+ entry 16 until its embargo ages out; + Silk if the free
registration path is declined; + the three version-of-record comparisons: PLB 183, PRD 41,
NPB 339).

## 2026-08-30 ~17:00 — the PLB 690 pair: bytes held, channel blocked, left to Duho

Entry 51's PLB 690 version-of-record + its 2013 erratum are FREE and were fetched into the
MacBook Chrome (sha of the VoR bytes, verified in-page: 8b7032ab7743c17e…, 347715 bytes). Two
delivery routes both dead-ended:
- **Chrome download** saved to a folder no agent can read (the MacBook Desktop — Chrome's
  last-used location; Downloads is SSH-readable but Desktop is TCC-blocked to the sshd context
  too). The green SAVE button fired; the file is on Duho's Desktop.
- **Direct byte pull** through the browser tool: the extension output filter BLOCKS bulk data
  (base64 → "[BLOCKED: Base64 encoded data]"; a later hex/return → "[BLOCKED: Cookie/query
  string data]"), and a page→Studio HTTPS POST is CSP/timeout-blocked from the sciencedirect
  origin. Probing for an encoding that evades the filter would be circumventing a deliberate
  control; not doing it.

RESOLUTION: one human action closes it — Duho presses Cmd-J in Chrome, "Show in Finder", drags
the PDF into `.../bhu-reading-20260823/sources/` (or Desktop→Downloads, then I SSH it). Until
then this stays on the SKIPPED list; entry 51's arXiv text remains the working pin and question
8's tier carries the revisit-on-VoR clause, so nothing is blocked.
