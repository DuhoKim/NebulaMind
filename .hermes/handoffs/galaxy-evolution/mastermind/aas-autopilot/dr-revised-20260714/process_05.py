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
IN_TEX = f"{BASE}/round1/paper_05_r1.tex"
OUT_TEX = f"{BASE}/round2/paper_05_r2.tex"

with open(IN_TEX, 'r') as f:
    text = f.read()

# Mechanically extract the invariant lines (digit-bearing lines between Section 2 and before Figure 1)
invariant_span = text[text.find(r"\section{Shared parent sample and selection function}"):text.find(r"\begin{figure}")]
digit_lines = [line.strip() for line in invariant_span.split('\n') if re.search(r'\d', line) and line.strip()]
invariant_line_count = len(digit_lines)

# Apply minimal replacements (ZERO NEW CITATIONS)
s5_old = r"""\section{Interpretation and missing observables}\label{sec:missing}
SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page. The full proposal requires: radio jet morphology/age, cavity or shock energetics, hot-gas density, and calibrated jet-power estimates.

The radio/X-ray/group literature motivates environment-stratified follow-up, but the present result is only an optical BPT-AGN fraction versus an internal density proxy \citep{best2005,santoro2020,mcnamara2007,eckert2024}."""

s5_new = r"""\section{Interpretation and missing observables}\label{sec:missing}
SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page. The full proposal requires: radio jet morphology/age, cavity or shock energetics, hot-gas density, and calibrated jet-power estimates.

The radio/X-ray/group literature motivates environment-stratified follow-up, but the present result is only an optical BPT-AGN fraction versus an internal density proxy \citep{best2005,santoro2020,mcnamara2007,eckert2024}. The optical fibre measurement contains neither radio jet morphology or age, cavity or shock energetics, hot-gas density, nor calibrated jet power. The measured fraction difference is therefore a target-stratification result and cannot be interpreted as a mechanical coupling efficiency or a direct fueling-state measurement."""

new_text = text.replace(s5_old, s5_new)

if new_text == text:
    print("NO-OP ERROR: Replace failed.")
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
  "paper_id": "paper_05",
  "publish_commit_git_performed": False,
  "real_data_only": True,
  "review_feedback_applied": [
    "interpretation and missing observables boundary"
  ],
  "round": 2,
  "skipped_review_sources_or_claims": [
    {"source": "Gatto et al. 2024", "reason": "not added: identity and exact claim fit were not independently settled locally"},
    {"source": "Sankar et al. 2026", "reason": "not added: identity and exact claim fit were not independently settled locally"},
    {"source": "Kondapally et al. 2025", "reason": "not added: identity and exact claim fit were not independently settled locally"}
  ],
  "source_round1_dr_review": f"{BASE}/round1/dr-review-packets/paper_05_round1_review_dr_packet.md",
  "source_round1_dr_review_sha256": sha(f"{BASE}/round1/dr-review-packets/paper_05_round1_review_dr_packet.md"),
  "source_round1_tex": IN_TEX,
  "source_round1_tex_sha256": sha(IN_TEX),
  "writer": "WonE"
}

with open(f"{BASE}/round2/receipts/paper_05_sources.json", "w") as f:
    json.dump(receipt, f, indent=2, sort_keys=True)
    f.write("\n")
with open(f"{BASE}/round2/receipts/paper_05_revision.md", "w") as f:
    f.write("# Revision notes for paper_05\nPreserved invariants exactly and mechanically verified the protected span. Added no new sources or measurements. Folded the review's scope boundary into a minimal statement that the observed optical fraction difference is target stratification, not a measured mechanical coupling efficiency or fueling state.\n")

print(f"paper_05 processed successfully. Invariant line count: {invariant_line_count}")

# Linter and Compile checks
print("Running linter...")
lint_cmd = ["python3", "/Users/duhokim/NebulaMind/NebulaMind/tools/ge_tex_publishability_lint.py", "--json", OUT_TEX]
subprocess.run(lint_cmd, check=True)

print("Compiling...")
tmp_dir = "/tmp/wone-publishability-05"
subprocess.run(["mkdir", "-p", f"{tmp_dir}/aastex"], check=True)
subprocess.run(["cp", OUT_TEX, f"{tmp_dir}/aastex/"], check=True)
subprocess.run(["cp", f"{BASE}/../latex-publishability-repair/aastex7_style_stage/aastex702.cls", f"{tmp_dir}/aastex/"], check=True)
# Find exact figure source from ROUND1_TECTONIC_BUILDS.json
with open(f"{BASE}/round1/receipts/ROUND1_TECTONIC_BUILDS.json") as f:
    builds = json.load(f)["builds"]
    fig_src = next(b["figure_source"] for b in builds if b["paper_id"] == "paper_05")

subprocess.run(["rm", "-f", f"{tmp_dir}/figures"])
subprocess.run(["ln", "-s", fig_src, f"{tmp_dir}/figures"], check=True)

compile_cmd = ["tectonic", "--keep-logs", "--outdir", ".", "paper_05_r2.tex"]
proc = subprocess.run(compile_cmd, cwd=f"{tmp_dir}/aastex", capture_output=True, text=True)
if proc.returncode != 0:
    print(f"Compilation failed with code {proc.returncode}")
    print(proc.stdout)
    sys.exit(1)

log_output = (proc.stdout + proc.stderr).lower()
if "undefined" in log_output:
    print("Warning: 'undefined' found in tectonic log.")

pdf_path = f"{tmp_dir}/aastex/paper_05_r2.pdf"
if os.path.exists(pdf_path):
    print("Compilation SUCCESS.")
    print("PDF SHA256:", sha(pdf_path))
else:
    print("PDF not found!")
    sys.exit(1)
