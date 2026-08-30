SCAN_AND_CUSTODY_CONFIRMED

I have audited both B42 v2 and B44. The image-based scan receipt and the git custody checks are completely sound.

**1. Entry 32's Acquisition (B42 v2): CONFIRMED**
I independently rendered page 1 of the pinned `ads_1994ApJ_423_659_brown_bethe.pdf` file (using fitz at 120 dpi) and examined the output image. I confirm your visual reading entirely: the journal header reads "The Astrophysical Journal, 423:659-664, 1994 March 10", the byline is exactly "G. E. Brown and H. A. Bethe", and the abstract explicitly states $M_{\text{max}} \simeq 1.5 M_\odot$, the $\sim 1.84 M_\odot$ stabilization, and $M_{\text{cutoff}} = 25 \pm 5 M_\odot$. 
The `b42` script handles the `SCAN` class responsibly by explicitly asserting PDF magic and SHA256 checksums rather than overclaiming machine containment on an image. The edit to the bibliography record is highly faithful, fully disclosing that the checks are visual and not greppable.

**2. The Pin Custody Hole (B44): CONFIRMED**
I verified via `git ls-files` that the nine previously disk-only pins (including the Entry 44 morning repair PDF and Entry 57's ARMA PDF) are now securely tracked in the repository. 
I audited the two enumeration routes in `b44_pin_custody.py`. The backtick regex and the explicit addition of the prose-cited `1309.1487.pdf` comprehensively cover the stated filenames. The script correctly identifies the one uncatchable class: citations made purely in prose without stating a filename (e.g., "the PDF for entry X").
Finally, I wrote an independent check to test the permissive collision rule (`any(...) for h in hits`). I found that there are exactly zero basename collisions for any cited artifact across the tree today. Thus, the permissive rule is not hiding any un-tracked duplicates.
