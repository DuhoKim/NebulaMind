#!/usr/bin/env python3
"""Targeted replacement to wrap all fragmented math and comparison operators (like >, ~, ∝) on Page 57 inside solid, self-contained LaTeX blocks."""

import sys
import re

sys.path.insert(0, "/Users/duhokim/NebulaMind/NebulaMind/backend")

from app.database import SessionLocal
from app.models.page import WikiPage
from scripts.align_citations import align_page


def fix_remaining_math(page_id: int) -> None:
    with SessionLocal() as db:
        page = db.get(WikiPage, page_id)
        if not page:
            print(f"Page {page_id} not found.")
            return

        content = page.content or ""
        
        # We replace the exact raw paragraph text with a mathematically clean version
        # where comparisons, limits, and units are safely enclosed inside $ ... $
        replacements = [
            (r"M★\s*>\s*10¹¹\s*M☉", r"$M_\\star \\gt 10^{11}\\,M_\\odot$"),
            (r"\$L_{\\text{1\.4}}\$\s*>\s*10²⁴\s*W\s*Hz⁻¹", r"$L_{\\text{1.4}} \\gt 10^{24}\\,\\text{W}\\,\\text{Hz}^{-1}$"),
            (r"M★\s*~\s*10¹¹·⁵\s*M☉", r"$M_\\star \\sim 10^{11.5}\\,M_\\odot$"),
            (r"\bz\s*~\s*1\b", r"$z \\sim 1$"),
            (r"M★\s*~\s*10¹⁰·⁵\s*M☉", r"$M_\\star \\sim 10^{10.5}\\,M_\\odot$"),
            # Clean up any accidental double backslashes
            (r"\\\\text", r"\\text"),
            (r"\\\\gt", r"\\gt"),
            (r"\\\\sim", r"\\sim"),
            (r"\\\\star", r"\\star"),
            (r"\\\\odot", r"\\odot"),
        ]

        new_content = content
        for pattern, repl in replacements:
            new_content = re.sub(pattern, repl, new_content)

        if new_content != content:
            page.content = new_content
            db.commit()
            print("Successfully updated database content with self-contained LaTeX blocks. Re-aligning page...")
            
            # Re-compile citation alignments
            report = align_page(db, page, dry_run=False, bootstrap=False)
            db.commit()
            print("Alignment report:", report)
        else:
            print("No targeted fragmented math was found.")


if __name__ == "__main__":
    fix_remaining_math(57)
