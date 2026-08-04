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
IN_TEX = f"{BASE}/round1/paper_04_r1.tex"
OUT_TEX = f"{BASE}/round2/paper_04_r2.tex"

with open(IN_TEX, 'r') as f:
    text = f.read()

# Mechanically extract the invariant lines (digit-bearing lines between Section 2 and before Figure 1)
invariant_span = text[text.find(r"\section{Shared parent sample and selection function}"):text.find(r"\begin{figure}")]
digit_lines = [line.strip() for line in invariant_span.split('\n') if re.search(r'\d', line) and line.strip()]
invariant_line_count = len(digit_lines)

# Apply minimal replacements (ZERO NEW CITATIONS)
s6_old = r"""\section{Deep Research literature integration: resolved and multiphase escape tests}\label{sec:dr-r1}
Ionized-gas disturbances and reduced star formation need not be causally coupled. In a low-redshift type-2 quasar sample, resolved line-profile analysis found widespread warm-ionized outflow signatures without a corresponding correlation between the measured gas kinematics and star-formation rate on the scales probed \citep{bessiere2024}. That comparison reinforces the present draft's existing restriction: a high-excitation SDSS denominator cannot establish that an outflow caused the catalog-sSFR difference.

Escape and recycling require measurements that the single fibre does not contain. Resolved kinematics can compare an outflow with a host potential \citep{zheng2023}, while subarcsecond CO observations show that even a compact radio jet can alter molecular-gas excitation and turbulence \citep{audibert2023}. These are methodological examples for future follow-up, not measurements of the 4,440 candidates here; the current result remains an optical target list."""

s6_new = r"""\section{Deep Research literature integration: resolved and multiphase escape tests}\label{sec:dr-r1}
Ionized-gas disturbances and reduced star formation need not be causally coupled. In a low-redshift type-2 quasar sample, resolved line-profile analysis found widespread warm-ionized outflow signatures without a corresponding correlation between the measured gas kinematics and star-formation rate on the scales probed \citep{bessiere2024}. That comparison reinforces the present draft's existing restriction: a high-excitation SDSS denominator cannot establish that an outflow caused the catalog-sSFR difference.

Escape and recycling require measurements that the single fibre does not contain. Resolved kinematics can compare an outflow with a host potential \citep{zheng2023}, while subarcsecond CO observations show that even a compact radio jet can alter molecular-gas excitation and turbulence \citep{audibert2023}. The present single-fibre optical data provide neither spatial outflow extent nor multiphase velocity coverage, so they cannot distinguish escape from recycling for this sample. These are methodological examples for future follow-up, not measurements of the 4,440 candidates here; the current result remains an optical target list."""

new_text = text.replace(s6_old, s6_new)

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
  "paper_id": "paper_04",
  "publish_commit_git_performed": False,
  "real_data_only": True,
  "review_feedback_applied": [
    "DR literature section"
  ],
  "round": 2,
  "skipped_review_sources_or_claims": [
    {"source": "Holden et al. 2025", "reason": "not added: identity and exact claim fit were not independently settled locally"},
    {"source": "Holden & Tadhunter 2024", "reason": "not added: identity and exact claim fit were not independently settled locally"},
    {"source": "Venturi et al. 2023", "reason": "not added: identity and exact claim fit were not independently settled locally"},
    {"source": "Ilha et al. 2024", "reason": "not added: identity and exact claim fit were not independently settled locally"}
  ],
  "source_round1_dr_review": f"{BASE}/round1/dr-review-packets/paper_04_round1_review_dr_packet.md",
  "source_round1_dr_review_sha256": sha(f"{BASE}/round1/dr-review-packets/paper_04_round1_review_dr_packet.md"),
  "source_round1_tex": IN_TEX,
  "source_round1_tex_sha256": sha(IN_TEX),
  "writer": "WonE"
}

with open(f"{BASE}/round2/receipts/paper_04_sources.json", "w") as f:
    json.dump(receipt, f, indent=2, sort_keys=True)
    f.write("\n")
with open(f"{BASE}/round2/receipts/paper_04_revision.md", "w") as f:
    f.write("# Revision notes for paper_04\nPreserved invariants exactly and mechanically verified the protected span. Added no new sources. Folded the review's scope boundary into a minimal statement of observables absent from the current single-fibre optical data; no external beam-smearing or coupling-efficiency claim was imported.\n")

print(f"paper_04 processed successfully. Invariant line count: {invariant_line_count}")

# Linter and Compile checks
print("Running linter...")
lint_cmd = ["python3", "/Users/duhokim/NebulaMind/NebulaMind/tools/ge_tex_publishability_lint.py", "--json", OUT_TEX]
subprocess.run(lint_cmd, check=True)

print("Compiling...")
tmp_dir = "/tmp/wone-publishability-04"
subprocess.run(["mkdir", "-p", f"{tmp_dir}/aastex"], check=True)
subprocess.run(["cp", OUT_TEX, f"{tmp_dir}/aastex/"], check=True)
subprocess.run(["cp", f"{BASE}/../latex-publishability-repair/aastex7_style_stage/aastex702.cls", f"{tmp_dir}/aastex/"], check=True)
# Find exact figure source from ROUND1_TECTONIC_BUILDS.json
with open(f"{BASE}/round1/receipts/ROUND1_TECTONIC_BUILDS.json") as f:
    builds = json.load(f)["builds"]
    fig_src = next(b["figure_source"] for b in builds if b["paper_id"] == "paper_04")

subprocess.run(["rm", "-f", f"{tmp_dir}/figures"])
subprocess.run(["ln", "-s", fig_src, f"{tmp_dir}/figures"], check=True)

compile_cmd = ["tectonic", "--keep-logs", "--outdir", ".", "paper_04_r2.tex"]
proc = subprocess.run(compile_cmd, cwd=f"{tmp_dir}/aastex", capture_output=True, text=True)
if proc.returncode != 0:
    print(f"Compilation failed with code {proc.returncode}")
    print(proc.stdout)
    sys.exit(1)

log_output = (proc.stdout + proc.stderr).lower()
if "undefined" in log_output:
    print("Warning: 'undefined' found in tectonic log.")

pdf_path = f"{tmp_dir}/aastex/paper_04_r2.pdf"
if os.path.exists(pdf_path):
    print("Compilation SUCCESS.")
    print("PDF SHA256:", sha(pdf_path))
else:
    print("PDF not found!")
    sys.exit(1)
