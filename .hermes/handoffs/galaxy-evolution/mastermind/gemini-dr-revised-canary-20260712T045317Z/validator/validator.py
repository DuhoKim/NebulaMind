import re

def validate_document(innertext, structured, spec=None):
    if spec is None:
        spec = {"marker": "GEMINI_WEB_JOINT_C1_OUTPUT_DONE_20260711T100139Z", "bidirectional_c7": False, "req_id": "", "model": ""}
        
    findings = []
    blocks = structured.get("blocks", [])
    
    def add_finding(clause, status, code, source_refs, evidence):
        findings.append({
            "clause": clause, "status": status, "code": code,
            "source_refs": source_refs, "evidence": evidence
        })

    # C1: exact first four nonblank rendered lines for a pinned contract.
    if spec.get("req_id") and spec.get("model"):
        header_lines = [line.strip() for line in innertext.splitlines() if line.strip()][:4]
        expected_title = spec.get("title", f"Joint C1R answer — {spec['req_id']}")
        header_ok = (
            len(header_lines) == 4
            and header_lines[0].lstrip("# ") == expected_title
            and re.fullmatch(r"Run date \(UTC\): \d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", header_lines[1])
            and header_lines[2] == f"Model: {spec['model']}"
            and re.fullmatch(r"Simulations covered: \d+", header_lines[3])
        )
        if not header_ok:
            add_finding("C1", "FAIL", "BAD_HEADER", [], "Header mismatched req/model/sims")
        else:
            add_finding("C1", "PASS", "HEADER_OK", [], "")
    else:
        add_finding("C1", "PASS", "NO_SPEC_PROVIDED", [], "")

    # C2: Order and empty (GAP/empty cell)
    expected_sections = spec.get("expected_sections") or [
        "Calibration ledger", "Out-of-sample validation ledger",
        "Double-counting warnings", "Feedback-relevant observables map",
        "Gaps", "Links ledger"
    ]
    s_idx = -1
    c2_order_ok = True
    c2_missing = set(expected_sections)
    
    for b in blocks:
        text = b.get("text", "").strip()
        if text in expected_sections:
            c2_missing.discard(text)
            idx = expected_sections.index(text)
            if idx > s_idx: s_idx = idx
            else: c2_order_ok = False
            
        if b.get("type") == "table_row":
            for i, cell in enumerate(b.get("cells", [])):
                cell_text = cell.get("text", "").strip()
                if not cell_text:
                    add_finding("C2", "FAIL", "EMPTY_TABLE_CELL", [b.get("id"), i], "Empty cell")
                    c2_order_ok = False
                if (
                    b.get("section") == "4. Feedback-relevant observables map"
                    and cell_text.startswith("NOT_REPORTED")
                    and "NONE_FOUND" not in cell_text
                ):
                    add_finding("C2", "FAIL", "MISSING_NONE_FOUND", [b.get("id"), i], cell_text)
                    c2_order_ok = False
                    
        if text.startswith("GAP:"):
            if "http" not in text and "ASSERTED_ABSENCE_NOT_SYSTEMATICALLY_VERIFIED" not in text:
                add_finding("C2", "FAIL", "GAP_MISSING_VERIFICATION", [b.get("id")], text[:50])
                c2_order_ok = False
                
    if not c2_order_ok or c2_missing:
        add_finding("C2", "FAIL", "BAD_STRUCTURE", [], f"Order bad or missing: {c2_missing}")
    else:
        add_finding("C2", "PASS", "STRUCTURE_OK", [], "")

    # C3: Quantitative claims without uncertainty
    c3_pass = True
    in_ledger = False
    for b in blocks:
        text = b.get("text", "")
        if "Links ledger" in text: in_ledger = True
        if in_ledger: continue
        
        if any(x in text for x in ["REQ_", "Run date (UTC):", "Model:", "Simulations covered:", spec.get("marker", "NONE")]): continue
        is_table_header = any(x in text for x in ["Simulation (method-paper citation)", "Simulation\tObservable", "Simulation\tQuenched fractions"])
        if is_table_header: continue
        if b.get("type") == "heading": continue
        
        if b.get("type") in ["paragraph", "table_row"]:
            text_no_url = re.sub(r'https?://[^\s\]]+', '', text)
            text_no_url = re.sub(r'\[.*?\]', '', text_no_url) # citations
            text_no_url = re.sub(r'\bFIRE-2\b', '', text_no_url)
            text_no_url = re.sub(r'\bTNG50\b', '', text_no_url)
            text_no_url = re.sub(r'\bIllustrisTNG100\b', '', text_no_url)
            
            numbers = re.findall(r'\b\d+(?:\.\d+)?(?:e[-+]?\d+)?\b', text_no_url)
            has_quant = bool(re.search(r'\d+\^\d+|\d+\.\d+', text_no_url)) or len(numbers) > 0
            if has_quant:
                if "±" not in text and "+/-" not in text and "UNCERTAINTY_NOT_QUOTED_BY_SOURCE" not in text:
                    add_finding("C3", "FAIL", "BARE_QUANTITY", [b.get("id")], text[:50])
                    c3_pass = False
                elif "UNCERTAINTY_NOT_QUOTED_BY_SOURCE" in text or "±" in text or "+/-" in text:
                    add_finding("C3", "MANUAL_REVIEW_REQUIRED", "UNCERTAINTY_CHECK", [b.get("id")], text[:50])
                    c3_pass = False
    
    if c3_pass: add_finding("C3", "PASS", "NO_QUANTITIES", [], "")

    # C4: Uncited calibration/validation
    c4_pass = True
    in_ledger = False
    for b in blocks:
        text = b.get("text", "")
        if "Links ledger" in text: in_ledger = True
        if in_ledger: continue
        if any(x in text for x in ["REQ_", "Run date (UTC):", "Model:", "Simulations covered:", spec.get("marker", "NONE")]): continue
        is_table_header = any(x in text for x in ["Simulation (method-paper citation)", "Simulation\tObservable", "Simulation\tQuenched fractions"])
        if is_table_header: continue
        
        has_calib_kw = bool(re.search(r'\b(calibrated|validation|tuned|calibrations)\b', text, re.IGNORECASE))
        
        if b.get("type") == "paragraph" and has_calib_kw:
            if "UNCITED_NOT_USABLE" not in text and not b.get("links") and "[" not in text:
                add_finding("C4", "FAIL", "UNCITED_CLAIM", [b.get("id")], text[:50])
                c4_pass = False
            else:
                add_finding("C4", "MANUAL_REVIEW_REQUIRED", "CITED_CLAIM_REVIEW", [b.get("id")], text[:50])
                c4_pass = False
                
        elif b.get("type") == "table_row":
            section = b.get("section", "")
            for i, cell in enumerate(b.get("cells", [])):
                ctext = cell.get("text", "")
                section_one_claim = (
                    section == "1. Calibration ledger"
                    and i in {1, 2, 3, 4}
                    and ctext.strip() != "NONE_FOUND"
                )
                has_cell_calib = section_one_claim or bool(
                    re.search(r'\b(calibrated|calibration|validation|validated|tuned|emergent)\b', ctext, re.IGNORECASE)
                )
                if has_cell_calib and len(ctext.split()) > 3:
                    if "UNCITED_NOT_USABLE" not in ctext and not cell.get("links") and "[" not in ctext:
                        add_finding("C4", "FAIL", "UNCITED_CELL_CLAIM", [b.get("id"), i], ctext[:50])
                        c4_pass = False
                    else:
                        add_finding("C4", "MANUAL_REVIEW_REQUIRED", "CITED_CELL_CLAIM_REVIEW", [b.get("id"), i], ctext[:50])
                        c4_pass = False
                        
    if c4_pass: add_finding("C4", "PASS", "NO_C4_ISSUES", [], "")

    # C5: Banned words
    banned_words = [
        r'\bestablish\b', r'\bestablishes\b', r'\bestablished\b', r'\bestablishing\b',
        r'\bproves\b', r'\bproven\b', r'confirms that', r'\bsettles\b', r'settled question',
        r'resolves the debate', r'\bdefinitively\b', r'\bconclusively\b', r'is now known',
        r'demonstrates that .* causes'
    ]
    c5_pass = True
    in_ledger = False
    for b in blocks:
        text = b.get("text", "")
        if "Links ledger" in text: in_ledger = True
        if in_ledger: continue
        for bw in banned_words:
            if re.search(bw, text, re.IGNORECASE):
                if '"' in text:
                    add_finding("C5", "MANUAL_REVIEW_REQUIRED", "ATTRIBUTED_QUOTE", [b.get("id")], text[:50])
                    c5_pass = False
                else:
                    add_finding("C5", "FAIL", "BANNED_OWN_VOICE", [b.get("id")], text[:50])
                    c5_pass = False
                    
    if c5_pass: add_finding("C5", "PASS", "NO_BANNED_WORDS", [], "")

    # C6: Comparability/qualifier tags
    c6_pass = True
    in_ledger = False
    for b in blocks:
        text = b.get("text", "")
        if "Links ledger" in text: in_ledger = True
        if in_ledger: continue
        is_table_header = any(x in text for x in ["Simulation (method-paper citation)", "Simulation\tObservable", "Simulation\tQuenched fractions"])
        if is_table_header: continue
        
        is_c1r_validation_row = (
            b.get("type") == "table_row"
            and b.get("section") == "2. Out-of-sample validation ledger"
        )
        is_legacy_validation_row = (
            b.get("type") == "table_row"
            and not b.get("section")
            and ("Agreement" in text or "Tension" in text)
        )
        if is_c1r_validation_row or is_legacy_validation_row:
            cells = b.get("cells", [])
            comp_index = 3 if is_c1r_validation_row else 2
            comp_cell = cells[comp_index].get("text", "").strip() if len(cells) > comp_index else ""
            allowed = {"MATCHED_SELECTIONS", "NON_COMMENSURABLE_UNMATCHED_SELECTIONS"}
            if comp_cell not in allowed:
                add_finding("C6", "FAIL", "MISSING_COMPARABILITY", [b.get("id"), comp_index], comp_cell or text[:50])
                c6_pass = False
            else:
                add_finding("C6", "MANUAL_REVIEW_REQUIRED", "SEMANTIC_QUALIFIER", [b.get("id"), comp_index], comp_cell)
                c6_pass = False
                
        if "fraction" in text.lower() or "incidence" in text.lower():
            qualifier_match = re.search(
                r'TRACER=([^;\s][^;]*);\s*SELECTION=([^;\s][^;]*);\s*'
                r'DENOMINATOR=([^;\s][^;]*);\s*REDSHIFT=([^;)\n\s][^;)\n]*)',
                text,
            )
            if not qualifier_match:
                add_finding("C6", "FAIL", "MISSING_QUALIFIER", [b.get("id")], text[:50])
                c6_pass = False
            else:
                add_finding("C6", "MANUAL_REVIEW_REQUIRED", "SEMANTIC_QUALIFIER", [b.get("id")], text[:50])
                c6_pass = False

        if b.get("type") not in {"heading", "table_header"}:
            simulation_pattern = spec.get(
                "simulation_pattern",
                r"\b(?:simulation|simulated|SIMBA|ASTRID|ROMULUS|FIRE(?:-\d+)?|IllustrisTNG\d*|EAGLE|FLAMINGO|BAHAMAS)\b",
            )
            comparison_candidate = (
                re.search(simulation_pattern, text, re.IGNORECASE)
                and re.search(r"\b(?:observed|observations?|observational|survey|empirical)\b", text, re.IGNORECASE)
                and re.search(
                    r"\b(?:agrees?|agreement|tension|reproduces?|underpredicts?|offset|discrepancy|consistent|comparison)\b",
                    text,
                    re.IGNORECASE,
                )
            )
            has_comparability = (
                "MATCHED_SELECTIONS" in text
                or "NON_COMMENSURABLE_UNMATCHED_SELECTIONS" in text
            )
            if comparison_candidate and not has_comparability:
                add_finding("C6", "FAIL", "UNLABELED_COMPARISON", [b.get("id")], text[:80])
                c6_pass = False
            elif comparison_candidate:
                add_finding("C6", "MANUAL_REVIEW_REQUIRED", "COMPARISON_LABEL_REVIEW", [b.get("id")], text[:80])
                c6_pass = False
                
    if c6_pass: add_finding("C6", "PASS", "NO_C6_ISSUES", [], "")

    # C7: generic URL-set
    body_urls = set()
    ledger_urls = set()
    in_ledger = False
    for b in blocks:
        text = b.get("text", "")
        if "Links ledger" in text: in_ledger = True
            
        urls = [link["url"] for link in b.get("links", [])]
        urls += re.findall(r'https?://[^\s\]]+', text)
        
        def norm(u):
            u = u.strip().strip(".,;:)'\"")
            u = re.sub(r'(arxiv\.org)/(?:abs|html)/(\d+\.\d+)(?:v\d+)?', r'\1/abs/\2', u)
            return u
            
        norm_urls = set(norm(u) for u in urls)
        if in_ledger: ledger_urls.update(norm_urls)
        else: body_urls.update(norm_urls)
            
    missing_from_ledger = body_urls - ledger_urls
    if missing_from_ledger: add_finding("C7", "FAIL", "MISSING_FROM_LEDGER", [], str(missing_from_ledger))
    else:
        if spec.get("bidirectional_c7") and (ledger_urls - body_urls):
            add_finding("C7", "FAIL", "MISSING_FROM_BODY", [], str(ledger_urls - body_urls))
        else:
            add_finding("C7", "PASS", "LINKS_OK", [], "")

    # C8: marker once/final
    marker = spec.get("marker", "")
    if marker:
        lines = innertext.strip().split("\n")
        count = innertext.count(marker)
        if count == 1 and lines[-1].strip() == marker: add_finding("C8", "PASS", "MARKER_OK", [], "")
        else: add_finding("C8", "FAIL", "MARKER_BAD", [], "")
    else: add_finding("C8", "PASS", "NO_MARKER", [], "")

    overall = "PASS"
    for f in findings:
        if f["status"] == "FAIL": overall = "FAIL"; break
        elif f["status"] == "MANUAL_REVIEW_REQUIRED" and overall != "FAIL": overall = "MANUAL_REVIEW_REQUIRED"
            
    return {"overall": overall, "findings": findings}
