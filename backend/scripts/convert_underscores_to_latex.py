#!/usr/bin/env python3
"""Convert plain-text underscores (which break Markdown engines) on Page 57 into standard HTML-safe LaTeX math blocks."""

import sys
import re

sys.path.insert(0, "/Users/duhokim/NebulaMind/NebulaMind/backend")

from app.database import SessionLocal
from app.models.page import WikiPage
from scripts.align_citations import align_page


def convert_underscores(page_id: int) -> None:
    with SessionLocal() as db:
        page = db.get(WikiPage, page_id)
        if not page:
            print(f"Page {page_id} not found.")
            return

        content = page.content or ""
        
        # Define replacements for variables that are not wrapped in LaTeX
        # We target specific plain text occurrences that break the markdown engine
        replacements = [
            (r"\bM_halo\b", r"$M_{\\text{halo}}$"),
            (r"\bM_h\b", r"$M_{\\text{h}}$"),
            (r"\bM_200c\b", r"$M_{\\text{200c}}$"),
            (r"\bv_max\b", r"$v_{\\text{max}}$"),
            (r"\bV_max\b", r"$V_{\\text{max}}$"),
            (r"\bT_vir\b", r"$T_{\\text{vir}}$"),
            (r"\bt_cool/t_drag\b", r"$t_{\\text{cool}}/t_{\\text{drag}}$"),
            (r"\bt_cool\b", r"$t_{\\text{cool}}$"),
            (r"\bt_drag\b", r"$t_{\\text{drag}}$"),
            (r"\bτ_KH\b", r"$\\tau_{\\text{KH}}$"),
            (r"\bτ_cross\b", r"$\\tau_{\\text{cross}}$"),
            (r"\bf_gas\b", r"$f_{\\text{gas}}$"),
            (r"\bv_c\b", r"$v_{\\text{c}}$"),
            (r"\bv_out\b", r"$v_{\\text{out}}$"),
            (r"\bM_gas\b", r"$M_{\\text{gas}}$"),
            (r"\bτ_dep\b", r"$\\tau_{\\text{dep}}$"),
            (r"\bM_bar\b", r"$M_{\\text{bar}}$"),
            (r"\bV_rot\b", r"$V_{\\text{rot}}$"),
            (r"\ba_0\b", r"$a_0$"),
            (r"\bf_b\b", r"$f_{\\text{b}}$"),
            (r"\bL_1.4\b", r"$L_{\\text{1.4}}$"),
            (r"\bL_AGN\b", r"$L_{\\text{AGN}}$"),
            (r"\bL_bol\b", r"$L_{\\text{bol}}$"),
            (r"\bM_BH\b", r"$M_{\\text{BH}}$"),
            (r"\bR_e\b", r"$R_{\\text{e}}$"),
            (r"\bM_sat/M_central\b", r"$M_{\\text{sat}}/M_{\\text{central}}$"),
            (r"\bM_sat\b", r"$M_{\\text{sat}}$"),
            (r"\bM_central\b", r"$M_{\\text{central}}$"),
            (r"\bM_UV\b", r"$M_{\\text{UV}}$"),
            (r"M★/M_h", r"$M_\\star/M_{\\text{h}}$"),
            # Clean up double backslashes in math to be safe
            (r"\\\\text", r"\\text"),
            (r"\\\\tau", r"\\tau"),
            (r"\\\\sim", r"\\sim"),
            (r"\\\\gt", r"\\gt"),
            (r"\\\\lt", r"\\lt"),
        ]

        new_content = content
        for pattern, repl in replacements:
            new_content = re.sub(pattern, repl, new_content)
        
        # Replace occurrences of plain underscores that might be part of list omissions or database dumps
        # (e.g. "omitted_owned_claim_ids" should be left alone, we only target physics variables)

        if new_content != content:
            page.content = new_content
            db.commit()
            print("Successfully updated database content with converted LaTeX variables. Re-aligning page...")
            
            # Run alignment to preserve citation span alignment under the new text structure
            report = align_page(db, page, dry_run=False, bootstrap=False)
            db.commit()
            print("Alignment report:", report)
        else:
            print("No unconverted underscores were found.")


if __name__ == "__main__":
    convert_underscores(57)
