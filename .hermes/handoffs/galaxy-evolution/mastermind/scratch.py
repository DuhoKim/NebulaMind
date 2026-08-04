import re
import json

base_dir = "/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution"
manifest_status_key = "status"

methods = {
    "M1": {
        "html": f"{base_dir}/packet-gated-paper-to-wiki-reconciliation/wiki-page.html",
        "md": f"{base_dir}/packet-gated-paper-to-wiki-reconciliation/pgr-same-format-draft-20260707T005045Z.md",
        "manifest": f"{base_dir}/packet-gated-paper-to-wiki-reconciliation/manifest.json",
        "allowed_chips": {2905, 2906, 2907, 2908, 2909, 2910, 2911, 2912, 2913, 2914, 2915, 2916, 2917, 2918, 2919, 2920, 2921, 2922, 2923, 2925, 2926, 2929, 2930, 2931, 2932, 2933, 2934, 2935, 2936, 2946}
    },
    "M2": {
        "html": f"{base_dir}/source-first-paper-adjudication/wiki-page.html",
        "md": f"{base_dir}/source-first-paper-adjudication/galaxy-evolution-same-format-draft.md",
        "manifest": f"{base_dir}/source-first-paper-adjudication/manifest.json",
        "allowed_chips": {2942, 2943, 2944, 2945, 2946, 2947}
    },
    "M3": {
        "html": f"{base_dir}/debate-map-to-wiki-rebuild/wiki-page.html",
        "md": f"{base_dir}/debate-map-to-wiki-rebuild/m3-p2-same-format-draft-20260707T050500Z.md",
        "manifest": f"{base_dir}/debate-map-to-wiki-rebuild/manifest.json",
        "allowed_chips": set()
    }
}

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

print("=== SCRIPT START ===")

for m, paths in methods.items():
    print(f"\n--- {m} ---")
    
    # HTML Parsing
    with open(paths["html"], "r") as f:
        html = f.read()
    
    # H2s (ignoring provenance headers that might be added, wait, we need to check the 9 binding H2s)
    h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', html)
    # clean entities
    h2s = [h.replace("&amp;", "&") for h in h2s]
    # filter to the ones that might match binding
    binding_h2s = [h for h in h2s if h in expected_h2]
    print(f"H2 Count: {len(binding_h2s)} binding (Total: {len(h2s)})")
    if binding_h2s == expected_h2:
        print("Binding H2 Order: OK (Matches expected 9)")
    else:
        print("Binding H2 Order: MISMATCH")
        print(binding_h2s)

    # Claims
    if m == "M1":
        claims = re.findall(r'data-claim="(\d+)"', html)
    elif m == "M2":
        claims = re.findall(r'data-claim-id="(\d+)"', html)
    else:
        claims = re.findall(r'data-claim-id="(\d+)"', html) + re.findall(r'data-claim="(\d+)"', html)
    
    claims_set = set(map(int, claims))
    print(f"Claim Marker Count: {len(claims)} (Unique: {len(claims_set)})")
    print(f"Claim IDs: {sorted(list(claims_set))}")
    
    # Leakage
    leakage = claims_set - paths["allowed_chips"]
    if leakage:
        print(f"LEAKAGE DETECTED: {leakage}")
    else:
        print("Leakage: NONE")

    # Cites
    cites = re.findall(r'>e:(\d+)<', html)
    cites_set = set(map(int, cites))
    print(f"Cite Marker Count: {len(cites)} (Unique: {len(cites_set)})")
    if cites_set:
        print(f"Cite IDs: {sorted(list(cites_set))}")

    # Links
    links = re.findall(r'<a\s+href=', html)
    print(f"Link Count: {len(links)}")

    # MD Parsing
    with open(paths["md"], "r") as f:
        md = f.read()
    
    paragraphs = len([p for p in md.split("\n\n") if p.strip()])
    words = len(md.split())
    print(f"MD Word Count: {words}")
    print(f"MD Paragraph Count: {paragraphs}")

    # Manifest Status
    with open(paths["manifest"], "r") as f:
        manifest = json.load(f)
    
    manifest_status = manifest.get("status", "NOT_FOUND")
    print(f"Manifest Status: {manifest_status}")
    
    # HTML Status Check
    if "NOT_PUBLISHED" in html or "DRAFT_PREPARED_STATIC_NOT_PUBLISHED" in html:
        print("HTML Status: Contains NOT_PUBLISHED variant")
    else:
        print("HTML Status: NO PUBLISHED STATE MARKER FOUND")

print("\n=== SCRIPT END ===")
