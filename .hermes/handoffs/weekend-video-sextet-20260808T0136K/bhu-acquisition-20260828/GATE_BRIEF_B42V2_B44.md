# Gate brief — B42 v2 (entry 32's scan receipt) + B44 (pin custody)

Two related artifacts, one round (commit 920d998d5):

**1. Entry 32's acquisition.** Brown & Bethe, ApJ 423, 659 (1994) — pre-arXiv, previously
Crossref-testimony only. The NASA ADS classic scan was fetched (articles.adsabs.harvard.edu,
direct PDF route) and pinned as
`../bhu-theory-phase3-cns-20260821/sources/ads_1994ApJ_423_659_brown_bethe.pdf`
(sha256 4b1cbae677de…, 6 pp, image-only — NO text layer). My byline verification is VISUAL:
I rendered page 1 and read the journal header ("The Astrophysical Journal, 423:659–664, 1994
March 10"), the full title, the byline "G. E. Brown and H. A. Bethe", and the abstract carrying
the cited numbers (M_max ≃ 1.5 M⊙; stabilization to ~1.84 M⊙; M_cutoff = 25 ± 5 M⊙).
`b42_support_byline_sweep.py` v2 records entry 32 as a SCAN class whose check asserts pin
existence + PDF magic + sha — and explicitly does NOT pretend machine containment on an image.
**Attack:** render page 1 yourself (fitz/pixmap at ~120 dpi) and verify or refute my visual
reading; audit whether b42's SCAN handling overclaims anywhere; check the record edit in entry
32's bibliography block for fidelity.

**2. The custody hole the pin exposed (defect 1ah).** The shared .gitignore re-admits `.hermes`
files by extension and `.pdf` is absent — NINE record-cited pins were disk-only, including
entry 44's morning repair artifact (d551b99e4 shipped the record, git dropped the PDF) and
entry 57's ARMA paper (the one read "in full, all 39 PDF pages" at B32). All nine were
force-added in 920d998d5; `b44_pin_custody.py` joins the battery: every cited artifact filename
that exists on disk must be git-tracked (backticked sweep + known prose-cited list, permissive
on basename collisions — stated).
**Attack:** verify the nine are actually in the commit (git ls-files); audit b44's two
enumeration routes and its stated missed class (prose-cited with no filename); is the
permissive collision rule hiding anything today?

**Verdict file:** `<A|C>GATE_B42V2_VERDICT.md`, first line a single token
(e.g. `SCAN_AND_CUSTODY_CONFIRMED` / `..._REFUTED_<REASON>` / `..._NARROWED_<REASON>`).
