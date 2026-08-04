import os
import re

base_dir = "/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution"
methods = ["packet-gated-paper-to-wiki-reconciliation", "source-first-paper-adjudication", "debate-map-to-wiki-rebuild"]
m_names = ["M1", "M2", "M3"]

expected_h2 = [
    "Overview: Galaxy Evolution as a Regulated Baryon Cycle",
    "Dark Matter Halos & Structure Formation",
    "Gas Supply, Star Formation & Feedback",
    "AGN Feedback & Quenching",
    "Environment, Morphology & Structural Growth",
    "Chemical Enrichment & Cosmic Timing",
    "High-Redshift & Reionization Frontier",
    "Observational Evidence & Surveys",
    "Synthesis & Open Tensions"
]

print("=== START RERUN CROSSCHECK ===")

for i, m in enumerate(methods):
    print(f"\n--- {m_names[i]} ---")
    d = os.path.join(base_dir, m)
    old_html = os.path.join(d, "wiki-page.html")
    new_html = os.path.join(d, "same-format-rebuild", "wiki-format-preview-20260707T064500Z.html")
    md_file = os.path.join(d, "same-format-rebuild", "page-content-20260707T064500Z.md")
    
    # Verify no old overwrite
    if os.path.exists(old_html):
        print("Old wiki-page.html exists: PASS (Not overwritten)")
    else:
        print("Old wiki-page.html exists: FAIL (Missing)")
        
    with open(new_html, "r") as f:
        html = f.read()
    with open(md_file, "r") as f:
        md = f.read()

    # MD H2 Check
    md_h2s = re.findall(r'^##\s+(.*)', md, re.MULTILINE)
    if md_h2s == expected_h2:
        print("MD H2 Order: PASS")
    else:
        print(f"MD H2 Order: FAIL (Found {len(md_h2s)}: {md_h2s})")

    # HTML H2 Count
    html_h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', html)
    html_h2s = [h.replace("&amp;", "&") for h in html_h2s]
    print(f"HTML raw <h2 count: {len(html_h2s)}")
    
    if m_names[i] in ["M2", "M3"]:
        if "<h3>Contents</h3>" in html and "<h2>Contents</h2>" not in html:
            print("Contents header check: PASS (is h3)")
        else:
            print("Contents header check: FAIL (not h3 or h2 present)")
    else:
        if "<h2>Contents</h2>" not in html:
            print("TOC h2 issue: PASS (none found)")
        else:
            print("TOC h2 issue: FAIL")

    # Reader / Evidence
    if "Reader" in html and "Evidence" in html:
        print("Reader/Evidence controls: PASS")
    else:
        print("Reader/Evidence controls: FAIL")

    # Live History/Sources
    has_history = "/wiki/galaxy-evolution/history" in html and not ("disabled" in html.lower() or "preview-only" in html.lower())
    if not has_history:
        print("History link check: PASS (no live routes)")
    else:
        print("History link check: FAIL")

    # Marker profile in MD
    open_claims = set(re.findall(r'<!--claim:(\d+)-->', md))
    close_claims = set(re.findall(r'<!--/claim:(\d+)-->', md))
    cites = set(re.findall(r'<!--cite:(.*?)-->', md))
    unmatched = re.findall(r'<!--cite-unmatched:(.*?)-->', md)
    
    print(f"MD Claims: {len(open_claims)} (matched: {open_claims == close_claims})")
    if m_names[i] == "M2":
        print(f"MD M2 Claim set: {sorted(list(map(int, open_claims)))}")
    print(f"MD Cites: {len(cites)}")
    print(f"MD Unmatched: {len(unmatched)}")

print("\n=== END RERUN CROSSCHECK ===")
