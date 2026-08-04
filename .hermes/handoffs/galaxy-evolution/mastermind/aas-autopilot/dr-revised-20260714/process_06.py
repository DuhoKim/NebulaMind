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
IN_TEX = f"{BASE}/round1/paper_06_r1.tex"
OUT_TEX = f"{BASE}/round2/paper_06_r2.tex"

with open(IN_TEX, 'r') as f:
    text = f.read()

# Mechanically extract the invariant lines (digit-bearing lines between Section 2 and before Figure 1)
invariant_span = text[text.find(r"\section{Shared parent sample and selection function}"):text.find(r"\begin{figure}")]
digit_lines = [line.strip() for line in invariant_span.split('\n') if re.search(r'\d', line) and line.strip()]
invariant_line_count = len(digit_lines)

# Section 4 is untouched.
# Replace section 5 and 5.1 ONLY.

s5_old = r"""\section{Interpretation and missing observables}\label{sec:missing}
SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page. The full proposal requires: gas fractions, baryon deficits, halo masses, stellar-feedback observables, and high-redshift extensions.

Mass, color bimodality, halo shock, central/satellite, and black-hole-mass studies define variables that must be added before attributing a mass vector to a physical feedback transition \citep{kauffmann2003mass,baldry2004,peng2010,peng2012,dekel2006,bluck2023,piotrowska2022}.


\subsection{Literature Context and Missing Observables}

Time-integrated quenching predictors are not equivalent to an instantaneous optical AGN state. The added source only motivates a caveat; it does not identify a physical transition mass in this sample \citep{bluck2023}."""

s5_new = r"""\section{Interpretation and missing observables}\label{sec:missing}
SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page. The full proposal requires: gas fractions, baryon deficits, halo masses, stellar-feedback observables, and high-redshift extensions.

Mass, color bimodality, halo shock, central/satellite, and black-hole-mass studies define variables that must be added before attributing a mass vector to a physical feedback transition \citep{kauffmann2003mass,baldry2004,peng2010,peng2012,dekel2006,bluck2023,piotrowska2022}. Because the current cache lacks group/central-satellite labels, the mass-bin association cannot separate internal mass-linked from environmental trends \citep{peng2010,peng2012}. The analysis also does not measure time-integrated feedback energy, so instantaneous optical classification remains a selection variable rather than a physical transition marker \citep{bluck2023,piotrowska2022}.


\subsection{Literature Context and Missing Observables}

Time-integrated quenching predictors are not equivalent to an instantaneous optical AGN state. These existing sources motivate a caveat; they do not identify a physical transition mass in this sample \citep{bluck2023,piotrowska2022}."""

if text.count(s5_old) != 1:
    print("REPLACEMENT ERROR: expected exactly one Section 5 source block")
    sys.exit(1)
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
  "paper_id": "paper_06",
  "publish_commit_git_performed": False,
  "real_data_only": True,
  "review_feedback_applied": [
    "interpretation and missing-observables boundary", "literature-context boundary"
  ],
  "round": 2,
  "skipped_review_sources_or_claims": [
    {"source": "Scharre et al. 2024", "reason": "not added: identity and exact claim fit were not independently settled locally"},
    {"source": "Mishra et al. 2026", "reason": "not added: identity and exact claim fit were not independently settled locally"},
    {"source": "Goubert et al. 2024", "reason": "not added: identity and exact claim fit were not independently settled locally"},
    {"source": "Visser-Zadvornyi et al. 2025", "reason": "not added: identity and exact claim fit were not independently settled locally"},
    {"source": "Baker et al. 2024", "reason": "not added: identity and exact claim fit were not independently settled locally"}
  ],
  "source_round1_dr_review": f"{BASE}/round1/dr-review-packets/paper_06_round1_review_dr_packet.md",
  "source_round1_dr_review_sha256": sha(f"{BASE}/round1/dr-review-packets/paper_06_round1_review_dr_packet.md"),
  "source_round1_tex": IN_TEX,
  "source_round1_tex_sha256": sha(IN_TEX),
  "writer": "WonE"
}

with open(f"{BASE}/round2/receipts/paper_06_sources.json", "w") as f:
    json.dump(receipt, f, indent=2, sort_keys=True)
    f.write("\n")
with open(f"{BASE}/round2/receipts/paper_06_revision.md", "w") as f:
    f.write("# Revision notes for paper_06\nPreserved invariants exactly, mechanically verified invariant span lines. ZERO new sources added. Folded physical caveats directly into Section 5/5.1 using existing sources (piotrowska2022, bluck2023, peng2010, peng2012) to clarify that instantaneous optical classification is a selection variable, and the mass-bin association cannot separate internal from environmental trends.\n")

print(f"paper_06 processed successfully. Invariant line count: {invariant_line_count}")

# Linter and Compile checks
print("Running linter...")
lint_cmd = ["python3", "/Users/duhokim/NebulaMind/NebulaMind/tools/ge_tex_publishability_lint.py", "--json", OUT_TEX]
subprocess.run(lint_cmd, check=True)

print("Compiling...")
tmp_dir = "/tmp/wone-publishability-06"
subprocess.run(["mkdir", "-p", f"{tmp_dir}/aastex"], check=True)
subprocess.run(["cp", OUT_TEX, f"{tmp_dir}/aastex/"], check=True)
subprocess.run(["cp", f"{BASE}/../latex-publishability-repair/aastex7_style_stage/aastex702.cls", f"{tmp_dir}/aastex/"], check=True)
# Find exact figure source from ROUND1_TECTONIC_BUILDS.json
with open(f"{BASE}/round1/receipts/ROUND1_TECTONIC_BUILDS.json") as f:
    builds = json.load(f)["builds"]
    fig_src = next(b["figure_source"] for b in builds if b["paper_id"] == "paper_06")

subprocess.run(["rm", "-f", f"{tmp_dir}/figures"])
subprocess.run(["ln", "-s", fig_src, f"{tmp_dir}/figures"], check=True)

compile_cmd = ["tectonic", "--keep-logs", "--outdir", ".", "paper_06_r2.tex"]
proc = subprocess.run(compile_cmd, cwd=f"{tmp_dir}/aastex", capture_output=True, text=True)
if proc.returncode != 0:
    print(f"Compilation failed with code {proc.returncode}")
    print(proc.stdout)
    sys.exit(1)

log_output = (proc.stdout + proc.stderr).lower()
if "undefined" in log_output:
    print("Warning: 'undefined' found in tectonic log.")

pdf_path = f"{tmp_dir}/aastex/paper_06_r2.pdf"
if os.path.exists(pdf_path):
    print("Compilation SUCCESS.")
    print("PDF SHA256:", sha(pdf_path))
else:
    print("PDF not found!")
    sys.exit(1)
