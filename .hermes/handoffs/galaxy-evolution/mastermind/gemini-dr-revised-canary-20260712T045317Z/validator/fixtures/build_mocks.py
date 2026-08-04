import json
from pathlib import Path

def generate_structured(filepath):
    lines = filepath.read_text().split('\n')
    blocks = []
    
    current_section = None
    headings = {
        "Calibration ledger", "Out-of-sample validation ledger",
        "Double-counting warnings", "Feedback-relevant observables map",
        "Gaps", "Links ledger",
        "1. Calibration ledger", "2. Out-of-sample validation ledger",
        "3. Double-counting warnings", "4. Feedback-relevant observables map",
        "5. Gaps",
    }
    
    for i, line in enumerate(lines):
        line_num = i + 1
        if not line.strip():
            continue
            
        # Determine block type
        links = []
        import re
        urls = re.findall(r'https?://[^\s\]]+', line)
        for u in urls:
            links.append({"url": u})
            
        rendered = line.strip().lstrip("#").strip()
        if rendered in headings:
            current_section = rendered
            blocks.append({
                "id": f"b_{line_num}",
                "type": "heading",
                "text": rendered,
                "links": links,
                "source_lines": [line_num],
                "section": current_section,
            })
        elif '\t' in line:
            # table row
            cells_text = line.split('\t')
            cells = [{"text": c.strip(), "links": [{"url": u} for u in re.findall(r'https?://[^\s\]]+', c)]} for c in cells_text]
            blocks.append({
                "id": f"row_{line_num}",
                "type": "table_row",
                "text": line,
                "links": links,
                "source_lines": [line_num],
                "cells": cells,
                "section": current_section,
            })
        else:
            blocks.append({
                "id": f"b_{line_num}",
                "type": "paragraph",
                "text": line,
                "links": links,
                "source_lines": [line_num],
                "section": current_section,
            })
            
    return {"blocks": blocks}

if __name__ == "__main__":
    fixtures_dir = Path(__file__).parent
    
    failed_path = fixtures_dir / "failed_c1.md"
    if failed_path.exists():
        failed_struct = generate_structured(failed_path)
        (fixtures_dir / "failed_c1_structured.json").write_text(json.dumps(failed_struct, indent=2))
        
    clean_path = fixtures_dir / "clean_c1.md"
    if clean_path.exists():
        clean_struct = generate_structured(clean_path)
        (fixtures_dir / "clean_c1_structured.json").write_text(json.dumps(clean_struct, indent=2))
