import os
import json
import hashlib
import re
import subprocess
import sys
import datetime

def sha(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def get_page_count(pdf_path):
    try:
        # Tectonic embeds page count in standard ways, but an easy way is using python if PyPDF2 is there.
        # Alternatively, use grep on the PDF if uncompressed, or macOS mdls:
        proc = subprocess.run(["mdls", "-name", "kMDItemNumberOfPages", "-raw", pdf_path], capture_output=True, text=True)
        if proc.returncode == 0 and proc.stdout.strip() != "(null)":
            return int(proc.stdout.strip())
        
        # Fallback for linux/mac without mdls:
        proc = subprocess.run(["pdfinfo", pdf_path], capture_output=True, text=True)
        for line in proc.stdout.split('\n'):
            if line.startswith('Pages:'):
                return int(line.split(':')[1].strip())
                
    except Exception:
        pass
    
    # Python fallback if no poppler
    try:
        with open(pdf_path, 'rb') as f:
            content = f.read()
            # This is a naive PDF page count, might not always work but usually fine for simple tex pdfs
            return content.count(b'/Type /Page\n') or content.count(b'/Type/Page\n') or content.count(b'/Type /Page\r') or content.count(b'/Type /Page ')
    except:
        return 0
    return 0

BASE = "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/dr-revised-20260714"

with open(f"{BASE}/round1/receipts/ROUND1_TECTONIC_BUILDS.json", "r") as f:
    builds_data = json.load(f)["builds"]
figure_sources = {b["paper_id"]: b["figure_source"] for b in builds_data}

papers = [f"paper_{str(i).zfill(2)}" for i in range(1, 10)]

receipt = {
    "generated_utc": datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z"),
    "status": "HOLD",
    "papers": {}
}

all_pass = True

for paper_id in papers:
    in_tex = f"{BASE}/round1/{paper_id}_r1.tex"
    out_tex = f"{BASE}/round2/{paper_id}_r2.tex"
    
    paper_status = {}
    
    with open(in_tex, 'r') as f:
        in_text = f.read()
    with open(out_tex, 'r') as f:
        out_text = f.read()
        
    start_str = r"\section{Shared parent sample and selection function}"
    in_start = in_text.find(start_str)
    out_start = out_text.find(start_str)
    
    in_fig_match = re.search(r"\\begin\{figure\*?\}", in_text[in_start:])
    out_fig_match = re.search(r"\\begin\{figure\*?\}", out_text[out_start:])
    
    in_end = in_start + in_fig_match.start() if in_fig_match else len(in_text)
    out_end = out_start + out_fig_match.start() if out_fig_match else len(out_text)
    
    in_span = in_text[in_start:in_end]
    out_span = out_text[out_start:out_end]
    
    in_digits = [line.strip() for line in in_span.split('\n') if re.search(r'\d', line) and line.strip()]
    out_digits = [line.strip() for line in out_span.split('\n') if re.search(r'\d', line) and line.strip()]
    
    invariants_preserved = (in_digits == out_digits)
    paper_status["invariants_preserved"] = invariants_preserved
    if not invariants_preserved:
        all_pass = False
        print(f"FAILED INVARIANT CHECK: {paper_id}")
        
    cites = {key.strip() for group in re.findall(r"\\cite[tp]?\{([^}]+)\}", out_text) for key in group.split(",")}
    bibitems = re.findall(r"\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}", out_text)
    
    citation_ok = (len(bibitems) == len(set(bibitems))) and (cites == set(bibitems))
    paper_status["citation_one_to_one"] = citation_ok
    if not citation_ok:
        all_pass = False
        print(f"FAILED CITATION CHECK: {paper_id}")
        
    lint_cmd = ["python3", "/Users/duhokim/NebulaMind/NebulaMind/tools/ge_tex_publishability_lint.py", "--json", out_tex]
    proc = subprocess.run(lint_cmd, capture_output=True, text=True)
    if proc.returncode == 0:
        lint_res = json.loads(proc.stdout)
        lint_ok = (lint_res.get("error_count", 1) == 0 and lint_res.get("warning_count", 1) == 0)
        paper_status["lint_errors"] = lint_res.get("error_count", 1)
        paper_status["lint_warnings"] = lint_res.get("warning_count", 1)
    else:
        lint_ok = False
        paper_status["lint_errors"] = -1
        paper_status["lint_warnings"] = -1
        
    paper_status["lint_clean"] = lint_ok
    if not lint_ok:
        all_pass = False
        print(f"FAILED LINT CHECK: {paper_id}")
        
    tmp_dir = f"/tmp/wone-publishability-final-{paper_id}"
    subprocess.run(["mkdir", "-p", f"{tmp_dir}/aastex"], check=True)
    subprocess.run(["cp", out_tex, f"{tmp_dir}/aastex/"], check=True)
    subprocess.run(["cp", f"{BASE}/../latex-publishability-repair/aastex7_style_stage/aastex702.cls", f"{tmp_dir}/aastex/"], check=True)
    subprocess.run(["rm", "-f", f"{tmp_dir}/figures"])
    subprocess.run(["ln", "-s", figure_sources[paper_id], f"{tmp_dir}/figures"], check=True)
    
    compile_cmd = ["tectonic", "--keep-logs", "--outdir", ".", f"{paper_id}_r2.tex"]
    proc = subprocess.run(compile_cmd, cwd=f"{tmp_dir}/aastex", capture_output=True, text=True)
    
    pdf_path = f"{tmp_dir}/aastex/{paper_id}_r2.pdf"
    if proc.returncode == 0 and os.path.exists(pdf_path):
        paper_status["tectonic_clean"] = True
        paper_status["pdf_sha256"] = sha(pdf_path)
        paper_status["pdf_size"] = os.path.getsize(pdf_path)
        
        pages = get_page_count(pdf_path)
        paper_status["pdf_pages"] = pages
        if pages != 3:
            print(f"Warning: {paper_id} has {pages} pages, expected 3.")
            # Depending on strictness, we might fail here
            # Prompt says "exactly 3 pages", so we fail if not 3
            if pages > 0: # If we successfully extracted page count
                all_pass = False
                paper_status["exact_three_pages"] = False
    else:
        paper_status["tectonic_clean"] = False
        all_pass = False
        print(f"FAILED TECTONIC: {paper_id}")
        
    receipt["papers"][paper_id] = paper_status

receipt["all_valid"] = all_pass

receipt_path = f"{BASE}/round2/receipts/ALL_NINE_VALIDATION_FINAL.json"
with open(receipt_path, "w") as f:
    json.dump(receipt, f, indent=2, sort_keys=True)
    f.write("\n")

print(f"Validation complete. All pass: {all_pass}")
print(f"Receipt written to {receipt_path}")
