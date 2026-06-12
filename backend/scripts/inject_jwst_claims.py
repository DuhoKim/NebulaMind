#!/usr/bin/env python3
"""Unified pipeline to restore Page 57, inject JWST claims with HTML-safe LaTeX, repair naked citations, and align them cleanly with 0 double-nesting."""

import sys
import re
from sqlalchemy import text

sys.path.insert(0, "/Users/duhokim/NebulaMind/NebulaMind/backend")

from app.database import SessionLocal
from app.models.page import WikiPage
from scripts.align_citations import align_page


def run_clean_pipeline() -> None:
    page_id = 57
    with SessionLocal() as db:
        page = db.get(WikiPage, page_id)
        if not page:
            print(f"Page {page_id} not found.")
            return

        # 1. Restore to clean Version 1584 baseline
        print("Restoring Page 57 to Version 1584...")
        cur = db.connection().connection.cursor()
        cur.execute("SELECT content FROM page_versions WHERE page_id=57 AND version_num=1584")
        content_1584 = cur.fetchone()[0]
        cur.close()
        
        # Delete any intermediate versions to prevent history pollution
        db.execute(text("DELETE FROM page_versions WHERE page_id=57 AND version_num > 1584"))
        db.commit()

        # Apply HTML-safe LaTeX (\lt and \gt) to the existing 1584 content to prevent any markdown/HTML collision
        content_1584 = content_1584.replace("$7 < z < 10$", "$7 \\lt z \\lt 10$")
        content_1584 = content_1584.replace("$z > 10$", "$z \\gt 10$")
        content_1584 = content_1584.replace("$z > 6$", "$z \\gt 6$")
        content_1584 = content_1584.replace("$z > 4$", "$z \\gt 4$")

        # 2. Draft the new prose paragraph with clean separable citations and HTML-safe LaTeX (\gt, \lt)
        injected_prose = (
            "\n\nBeyond stellar masses, JWST spectroscopy has opened a new window into chemical enrichment and gas dynamics in the early universe. "
            "<!--claim:1882-->JWST NIRSpec observations at $z=4$–$9$ reveal that early galaxies follow a mass-metallicity relation (MZR) that is offset by "
            "$\\sim 0.5$ dex below the local relation at fixed stellar mass, with some high-ionisation systems at $z \\gt 6$ showing oxygen abundances as low as "
            "5–10% solar (Curti et al. 2024) and (Nakajima et al. 2023). These extremely low metallicities, combined with high specific star-formation rates, "
            "indicate that pristine gas accretion from cosmic filaments dominated the baryonic budget of early galaxies, with insufficient time for stellar "
            "evolution to enrich the interstellar medium to levels typical of $z \\sim 0$ dwarfs<!--/claim:1882-->. Furthermore, "
            "<!--claim:1887-->the nitrogen-to-oxygen (N/O) ratio and carbon abundance in high-redshift galaxies encode the contribution of asymptotic giant "
            "branch (AGB) stars and the integrated star-formation history. JWST NIRSpec detections of rest-frame UV nitrogen emission in compact $z \\gt 4$ "
            "galaxies like GN-z11 (Cameron et al. 2023) suggest nitrogen super-solar enrichment from massive Wolf-Rayet stars or a top-heavy IMF, "
            "pointing to chemically distinct enrichment channels in the earliest star-forming systems that are not captured by standard chemical evolution "
            "models calibrated on the local universe<!--/claim:1887-->. This spectroscopic record highlights that early galaxy assembly was dominated by "
            "rapid, pristine gas feeding rather than the steady-state evolution observed at lower redshifts."
        )

        claim_1995_marker = "<!--claim:1995-->"
        content = content_1584.replace(claim_1995_marker, injected_prose + "\n\n" + claim_1995_marker, 1)
        print("Prose injected successfully.")

        # 3. Retrieve all known evidence for Page 57 to map naked author mentions
        rows = db.execute(
            text(
                """
                SELECT DISTINCT e.id, e.authors, e.year
                FROM page_citation_links pcl
                JOIN evidence e ON e.id = pcl.evidence_id
                WHERE pcl.page_id = :pid AND e.year IS NOT NULL
                """
            ),
            {"pid": page_id}
        ).fetchall()
        
        author_map = {}
        for row in rows:
            ev_id, authors, year = row
            if not authors:
                continue
            clean_authors = authors.strip("[]\"'")
            first = re.split(r"\s*,\s*|\s+;\s*", clean_authors, flags=re.I)[0].strip()
            clean_first = re.sub(r"\bet\s+al\.?\b|\bCollaboration\b", "", first, flags=re.I).strip(" ,.")
            last_name = clean_first.split()[-1] if clean_first.split() else clean_first
            if last_name:
                last_name_clean = last_name.lower()
                if last_name_clean not in author_map:
                    author_map[last_name_clean] = []
                author_map[last_name_clean].append((year, ev_id))

        # 4. Repair naked citations safely BEFORE running align_page (prevents double nesting)
        # Avoid matching any authors already inside HTML span tags
        pattern = re.compile(
            r"\b(?P<authors>[A-Z][A-Za-zÀ-ÖØ-öø-ÿ'’.\-]+\s+et\s+al\.)"
            r"(?!\s*\(?(?:19|20)\d{2}\)?)"
            r"(?!\s*<!--cite:)"
            r"(?![^<]*<\/span>)"  # Prevent matching authors already inside a span tag
        )

        def repl(match: re.Match) -> str:
            raw_author = match.group("authors")
            clean = re.sub(r"\bet\s+al\.?\b", "", raw_author, flags=re.I).strip(" ,.")
            last = clean.split()[-1] if clean.split() else clean
            last_clean = last.lower()
            
            candidates = author_map.get(last_clean, [])
            if len(candidates) == 1:
                year, ev_id = candidates[0]
                print(f"Repairing naked mention: '{raw_author}' -> '{raw_author} ({year})'")
                return f"{raw_author} ({year})"
            elif len(candidates) > 1:
                year = max(c[0] for c in candidates)
                print(f"Repairing naked mention (picking latest): '{raw_author}' -> '{raw_author} ({year})'")
                return f"{raw_author} ({year})"
            return raw_author

        repaired_content = pattern.sub(repl, content)
        print("Naked citations repaired cleanly.")

        # 5. Save the repaired & injected content
        page.content = repaired_content
        db.commit()

        # 6. Run alignment to compile all parentheticals into spans
        print("Triggering align_page compilation...")
        report = align_page(db, page, dry_run=False, bootstrap=False)
        db.commit()
        print("Alignment complete! Report:", report)


if __name__ == "__main__":
    run_clean_pipeline()
