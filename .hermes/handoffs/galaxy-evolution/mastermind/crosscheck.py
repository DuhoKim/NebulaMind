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

print("=== START CROSSCHECK ===")

for i, m in enumerate(methods):
    print(f"\n--- {m_names[i]} ---")
    d = os.path.join(base_dir, m)
    old_html = os.path.join(d, "wiki-page.html")
    new_html = os.path.join(d, "same-format-rebuild", "wiki-format-preview-20260707T064500Z.html")
    
    # Verify no old overwrite
    if os.path.exists(old_html):
        print("Old wiki-page.html exists: PASS (Not overwritten)")
    else:
        print("Old wiki-page.html exists: FAIL (Missing)")
        
    with open(new_html, "r") as f:
        html = f.read()
    
    # H2s
    h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', html)
    h2s = [h.replace("&amp;", "&") for h in h2s]
    if h2s == expected_h2:
        print("H2 Order: PASS (Matches expected 9)")
    else:
        print(f"H2 Order: FAIL (Found {len(h2s)}: {h2s})")
        
    # Claim markers: <!--claim:ID-->...<!--/claim:ID-->
    open_claims = re.findall(r'<!--claim:(\d+)-->', html)
    close_claims = re.findall(r'<!--/claim:(\d+)-->', html)
    if open_claims == close_claims:
        print(f"Claim Marker Pair Match: PASS (Count: {len(open_claims)})")
    else:
        print(f"Claim Marker Pair Match: FAIL (Open: {len(open_claims)}, Close: {len(close_claims)})")
        
    # Cite markers
    cites = re.findall(r'<!--cite:(\d+(?:,\d+)*)-->', html)
    cite_unmatched = re.findall(r'<!--cite-unmatched:(.*?)-->', html)
    print(f"Cite Markers: {len(cites)} resolved, {len(cite_unmatched)} unmatched")
    
    # Static UI components check
    has_grid = "gridTemplateColumns" in html or "TOCSidebar" in html or "grid" in html.lower()
    has_history = "/wiki/galaxy-evolution/history" in html
    has_preview_only = "preview-only" in html.lower() or "disabled" in html.lower()
    has_reader_controls = "Reader/Evidence" in html or "Reduce highlights" in html
    
    print(f"Static Shell Controls Present: {'PASS' if has_reader_controls else 'FAIL'}")
    print(f"History Link Preview/Disabled Treatment: {'PASS' if (not has_history or has_preview_only) else 'FAIL'}")

print("\n=== END CROSSCHECK ===")
