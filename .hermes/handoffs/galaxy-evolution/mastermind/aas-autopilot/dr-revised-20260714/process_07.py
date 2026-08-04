import os
import json
import hashlib
import re
import subprocess
import sys

def sha(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

BASE = "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/dr-revised-20260714"
IN_TEX = f"{BASE}/round1/paper_07_r1.tex"
OUT_TEX = f"{BASE}/round2/paper_07_r2.tex"

with open(IN_TEX, 'r') as f:
    text = f.read()

# Mechanically extract the invariant lines (digit-bearing lines between Section 2 and before Figure 1)
invariant_span = text[text.find(r"\section{Shared parent sample and selection function}"):text.find(r"\begin{figure}")]
digit_lines = [line.strip() for line in invariant_span.split('\n') if re.search(r'\d', line) and line.strip()]
invariant_line_count = len(digit_lines)

# Apply minimal replacements (ZERO NEW CITATIONS)
s51_old = r"""\subsection{Literature Context and Missing Observables}

An optical ionized-gas census is tracer- and definition-dependent and cannot recover neutral/molecular mass loading \citep{escott2025}. Radio detection can change observed ionized-outflow incidence, motivating radio follow-up without changing this optical prevalence \citep{davies2024}. Beam smearing and unresolved rotation block galaxy-wide outflow claims from a single aperture \citep{holden2024}."""

s51_new = r"""\subsection{Literature Context and Missing Observables}

An optical ionized-gas census is tracer- and definition-dependent and cannot recover neutral/molecular mass loading \citep{veilleux2005,cicone2014,rupke2018}. Radio detection can change observed ionized-outflow incidence, motivating radio follow-up without changing this optical prevalence \citep{escott2025}. JWST observations at cosmic noon found neutral-gas outflow rates that can match or exceed ionized-gas rates, motivating a separate neutral tracer in any future common-denominator census \citep{davies2024}. Beam smearing and unresolved rotation block galaxy-wide outflow claims from a single aperture \citep{holden2024}."""

if text.count(s51_old) != 1:
    print("REPLACEMENT ERROR: expected exactly one Section 5.1 source block")
    sys.exit(1)
new_text = text.replace(s51_old, s51_new)

if new_text == text:
    print("NO-OP ERROR: Replace failed for s51.")
    sys.exit(1)

# Verify invariants mechanically
new_invariant_span = new_text[new_text.find(r"\section{Shared parent sample and selection function}"):new_text.find(r"\begin{figure}")]
new_digit_lines = [line.strip() for line in new_invariant_span.split('\n') if re.search(r'\d', line) and line.strip()]

if new_digit_lines != digit_lines:
    print("ERROR: Invariants altered!")
    sys.exit(1)

cites = {key.strip() for group in re.findall(r"\\cite[tp]?\{([^}]+)\}", new_text) for key in group.split(",")}
bibitems = re.findall(r"\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}", new_text)
if len(bibitems) != len(set(bibitems)) or cites != set(bibitems):
    print("ERROR: citation/bibliography one-to-one validation failed")
    sys.exit(1)

# Write out
with open(OUT_TEX, 'w') as f:
    f.write(new_text)

# Generate Receipt
import datetime
now = datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z")

receipt = {
  "added_or_corrected_sources": [],
  "analysis_measurements_recomputed": False,
  "association_not_causal": True,
  "broker_touched": False,
  "browser_or_account_touched": False,
  "drafts_only": True,
  "generated_utc": now,
  "local_only": True,
  "measured_invariant_line_count": invariant_line_count,
  "measured_invariants_preserved_exact": True,
  "output_tex": OUT_TEX,
  "output_tex_sha256": sha(OUT_TEX),
  "paper_id": "paper_07",
  "publish_commit_git_performed": False,
  "real_data_only": True,
  "review_feedback_applied": [
    "literature-context correction for escott2025 and davies2024 claim roles"
  ],
  "round": 2,
  "skipped_review_sources_or_claims": [
    {"source": "Holden et al. (2025)", "reason": "not added: identity and exact claim fit were not independently settled locally"},
    {"source": "Bessiere et al. (2024)", "reason": "not added: no source-dependent conclusion assertion was imported without a citation"},
    {"source": "Speranza et al. (2024)", "reason": "not added: identity and exact claim fit were not independently settled locally"}
  ],
  "source_round1_dr_review": f"{BASE}/round1/dr-review-packets/paper_07_round1_review_dr_packet.md",
  "source_round1_dr_review_sha256": sha(f"{BASE}/round1/dr-review-packets/paper_07_round1_review_dr_packet.md"),
  "source_round1_tex": IN_TEX,
  "source_round1_tex_sha256": sha(IN_TEX),
  "writer": "WonE"
}

with open(f"{BASE}/round2/receipts/paper_07_sources.json", "w") as f:
    json.dump(receipt, f, indent=2, sort_keys=True)
    f.write("\n")
with open(f"{BASE}/round2/receipts/paper_07_revision.md", "w") as f:
    f.write("# Revision notes for paper_07\nPreserved invariants exactly and mechanically verified the protected span. Added no new sources. Corrected the claim roles of existing citations in Section 5.1: Escott et al. supports the radio-detection context, Davies et al. supports a separate neutral-gas tracer, and the optical multiphase limitation is bounded by existing review sources. No source-dependent conclusion assertion was imported from a skipped citation.\n")

print(f"paper_07 processed successfully. Invariant line count: {invariant_line_count}")

# Linter and Compile checks
print("Running linter...")
lint_cmd = ["python3", "/Users/duhokim/NebulaMind/NebulaMind/tools/ge_tex_publishability_lint.py", "--json", OUT_TEX]
subprocess.run(lint_cmd, check=True)

print("Compiling...")
tmp_dir = "/tmp/wone-publishability-07"
subprocess.run(["mkdir", "-p", f"{tmp_dir}/aastex"], check=True)
subprocess.run(["cp", OUT_TEX, f"{tmp_dir}/aastex/"], check=True)
subprocess.run(["cp", f"{BASE}/../latex-publishability-repair/aastex7_style_stage/aastex702.cls", f"{tmp_dir}/aastex/"], check=True)
# Find exact figure source from ROUND1_TECTONIC_BUILDS.json
with open(f"{BASE}/round1/receipts/ROUND1_TECTONIC_BUILDS.json") as f:
    builds = json.load(f)["builds"]
    fig_src = next(b["figure_source"] for b in builds if b["paper_id"] == "paper_07")

subprocess.run(["rm", "-f", f"{tmp_dir}/figures"])
subprocess.run(["ln", "-s", fig_src, f"{tmp_dir}/figures"], check=True)

compile_cmd = ["tectonic", "--keep-logs", "--outdir", ".", "paper_07_r2.tex"]
proc = subprocess.run(compile_cmd, cwd=f"{tmp_dir}/aastex", capture_output=True, text=True)
if proc.returncode != 0:
    print(f"Compilation failed with code {proc.returncode}")
    print(proc.stdout)
    sys.exit(1)

log_output = (proc.stdout + proc.stderr).lower()
if "undefined" in log_output:
    print("Warning: 'undefined' found in tectonic log.")

pdf_path = f"{tmp_dir}/aastex/paper_07_r2.pdf"
if os.path.exists(pdf_path):
    print("Compilation SUCCESS.")
    print("PDF SHA256:", sha(pdf_path))
else:
    print("PDF not found!")
    sys.exit(1)
