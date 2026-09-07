# BOUNDED CODEX TASK — publisher-text verification of PRD 85, 107502 (2012) (Tori, 2026-09-07)

A claim that two PUBLISHED papers disagree must rest on published bytes. `SOURCES_20260907.md` already establishes that
GRG 53, 18's publisher full text was read directly. Give the PRD paper the same treatment.

## Boundaries
- Write ONLY under `bounce/`. No pinned census file, no kit, no census version. No Hwao data.
- The APS version of record is the target: publisher text, NOT a mirror, NOT arXiv, NOT an HTML scrape of a third-party site.
  If the publisher text cannot be reached, say so explicitly and state exactly what you could and could not obtain — do not
  substitute a mirror and call it the published version.

## Establish and quote
1. N. Popławski, "Nonsingular, big-bounce cosmology from spinor-torsion coupling", Phys. Rev. D 85, 107502 (2012):
   DOI, exact version (published/erratum?), and whether any ERRATUM or later correction exists for it — check the DOI landing
   page and the journal's erratum listing. An erratum, if one exists, is decisive for our question.
2. Quote VERBATIM, with equation numbers: the sentence defining the tilde convention; Eq. (10); Eq. (11); Eq. (12). Give the page
   numbers. State whether the pressure correction that Eq. (12) implies for the EFFECTIVE TOTAL pressure is +alpha n^2 or
   -alpha n^2, quoting the line you read it from.
3. Same treatment for the formalism anchor: Hehl, von der Heyde, Kerlick & Nester, Rev. Mod. Phys. 48, 393 (1976). Quote the
   equations giving the COMBINED (effective) energy-momentum tensor with the terms quadratic in spin, with equation numbers, and
   the resulting effective energy density and pressure of an unpolarised spin fluid if the paper prints them.
4. Record access evidence for each: URL, HTTP status, bytes, local path and sha256 of anything saved under `bounce/`.

## Output: `bounce/PRD_PUBLISHER_VERIFY_20260907.md`
End with a table: source | publisher text obtained? | erratum? | tilde convention quoted | effective pressure correction sign.
Print the file's sha256 and your access-evidence lines as your final answer. Do not analyse the physics; quote and record only.
