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
IN_TEX = f"{BASE}/round1/paper_08_r1.tex"
OUT_TEX = f"{BASE}/round2/paper_08_r2.tex"

with open(IN_TEX, 'r') as f:
    text = f.read()

# Mechanically extract the invariant lines (digit-bearing lines between Section 2 and before Figure 1)
invariant_span = text[text.find(r"\section{Shared parent sample and selection function}"):text.find(r"\begin{figure}")]
digit_lines = [line.strip() for line in invariant_span.split('\n') if re.search(r'\d', line) and line.strip()]
invariant_line_count = len(digit_lines)

# Section 4 and 6 are left byte-for-byte unchanged.
# Replace section 5 and 5.1 ONLY, plus the bibliography addition.

s5_old = r"""\section{Interpretation and missing observables}\label{sec:missing}
SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page. The full proposal requires: CO or dust-based molecular gas masses, aperture-matched SFRs, morphology, and environment labels.

Gas-fraction and depletion-time claims require CO/HI or equivalent gas masses plus aperture-matched SFRs; optical H$\alpha$ proxy values alone cannot distinguish gas depletion from low efficiency \citep{coldgass1,coldgass2,xcoldgass2017,xgass2018}."""

s5_new = r"""\section{Interpretation and missing observables}\label{sec:missing}
SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page. The full proposal requires: CO or dust-based molecular gas masses, aperture-matched SFRs, morphology, and environment labels.

Gas-fraction and depletion-time claims require CO/HI or equivalent gas masses plus aperture-matched SFRs; optical H$\alpha$ proxy values alone cannot distinguish gas depletion from low efficiency \citep{coldgass1,coldgass2,xcoldgass2017,xgass2018}. The current BPT fraction describes the optical ionization state of this selected denominator; it is not a measurement of cumulative feedback history \citep{bluck2023}."""

if text.count(s5_old) != 1:
    print("REPLACEMENT ERROR: expected exactly one Section 5 source block")
    sys.exit(1)
new_text = text.replace(s5_old, s5_new)
if new_text == text:
    print("NO-OP ERROR: Replace failed for s5.")
    sys.exit(1)

s51_old = r"""\subsection{Literature Context and Missing Observables}

Optical dust/emission proxies can organize follow-up but retain substantial scatter and cannot replace direct cold-gas masses \citep{scholte2023}. Gas fraction and star-formation efficiency can both decline away from the main sequence, so an H$\alpha$ deficit does not isolate either mechanism \citep{piotrowska2020}. Do not turn either source into a molecular-gas measurement for these SDSS targets."""

s51_new = r"""\subsection{Literature Context and Missing Observables}

Optical dust/emission proxies can organize follow-up but retain substantial scatter and cannot replace direct cold-gas masses \citep{scholte2023}. Gas fraction and star-formation efficiency can both decline away from the main sequence, so an H$\alpha$ deficit does not isolate either mechanism \citep{piotrowska2020}. The optical denominator supplies neither cold-gas mass nor aperture-matched gas/SFR maps, so it cannot determine whether gas supply or efficiency is lower \citep{scholte2023,piotrowska2020}. Do not turn either source into a molecular-gas measurement for these SDSS targets."""

if new_text.count(s51_old) != 1:
    print("REPLACEMENT ERROR: expected exactly one Section 5.1 source block")
    sys.exit(1)
new_text = new_text.replace(s51_old, s51_new)
if new_text == text.replace(s5_old, s5_new):
    print("NO-OP ERROR: Replace failed for s51.")
    sys.exit(1)

# Add bibitem
bib_old = r"\end{thebibliography}"
bib_new = r"\bibitem[Bluck et al.(2023)]{bluck2023} Bluck, A.~F.~L., Piotrowska, J.~M., \& Maiolino, R. 2023, ApJ, 944, 108" + "\n\\end{thebibliography}"
if new_text.count(bib_old) != 1:
    print("BIBLIOGRAPHY ERROR: insertion point is not unique")
    sys.exit(1)
new_text = new_text.replace(bib_old, bib_new)

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
  "added_or_corrected_sources": [
    {
      "citation": "Bluck et al. 2023",
      "identifier": "DOI:10.3847/1538-4357/acac7c ; arXiv:2301.03677",
      "key": "bluck2023",
      "verification": "Identity settled in the paper_06 review; exact bibitem copied from paper_06 and claim bounded to current versus cumulative feedback history"
    }
  ],
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
  "paper_id": "paper_08",
  "publish_commit_git_performed": False,
  "real_data_only": True,
  "review_feedback_applied": [
    "Clarified BPT fraction as optical ionization state, not cumulative feedback history",
    "Clarified optical denominator cannot separate gas supply vs efficiency"
  ],
  "round": 2,
  "skipped_review_sources_or_claims": [
    {"source": "Lin et al. (2026)", "reason": "not added: identity and exact claim fit were not independently settled locally"},
    {"source": "Weibel et al. (2025)", "reason": "not added: identity and exact claim fit were not independently settled locally"},
    {"source": "Goubert et al. (2024)", "reason": "not added: identity and exact claim fit were not independently settled locally"},
    {"source": "Pan et al. (2024)", "reason": "not added: identity and exact claim fit were not independently settled locally"}
  ],
  "source_round1_dr_review": f"{BASE}/round1/dr-review-packets/paper_08_round1_review_dr_packet.md",
  "source_round1_dr_review_sha256": sha(f"{BASE}/round1/dr-review-packets/paper_08_round1_review_dr_packet.md"),
  "source_round1_tex": IN_TEX,
  "source_round1_tex_sha256": sha(IN_TEX),
  "writer": "WonE"
}

with open(f"{BASE}/round2/receipts/paper_08_sources.json", "w") as f:
    json.dump(receipt, f, indent=2, sort_keys=True)
    f.write("\n")
with open(f"{BASE}/round2/receipts/paper_08_revision.md", "w") as f:
    f.write("# Revision notes for paper_08\nPreserved invariants exactly, mechanically verified invariant span lines. Section 4 and 6 left byte-for-byte unchanged. Added exactly one source (bluck2023) to Section 5, clarifying the optical ionization state vs cumulative feedback history. Expanded caveat in Section 5.1 bounded by scholte2023/piotrowska2020. Skipped uncertain review sources.\n")

print(f"paper_08 processed successfully. Invariant line count: {invariant_line_count}")

# Linter and Compile checks
print("Running linter...")
lint_cmd = ["python3", "/Users/duhokim/NebulaMind/NebulaMind/tools/ge_tex_publishability_lint.py", "--json", OUT_TEX]
subprocess.run(lint_cmd, check=True)

print("Compiling...")
tmp_dir = "/tmp/wone-publishability-08"
subprocess.run(["mkdir", "-p", f"{tmp_dir}/aastex"], check=True)
subprocess.run(["cp", OUT_TEX, f"{tmp_dir}/aastex/"], check=True)
subprocess.run(["cp", f"{BASE}/../latex-publishability-repair/aastex7_style_stage/aastex702.cls", f"{tmp_dir}/aastex/"], check=True)
# Find exact figure source from ROUND1_TECTONIC_BUILDS.json
with open(f"{BASE}/round1/receipts/ROUND1_TECTONIC_BUILDS.json") as f:
    builds = json.load(f)["builds"]
    fig_src = next(b["figure_source"] for b in builds if b["paper_id"] == "paper_08")

subprocess.run(["rm", "-f", f"{tmp_dir}/figures"])
subprocess.run(["ln", "-s", fig_src, f"{tmp_dir}/figures"], check=True)

compile_cmd = ["tectonic", "--keep-logs", "--outdir", ".", "paper_08_r2.tex"]
proc = subprocess.run(compile_cmd, cwd=f"{tmp_dir}/aastex", capture_output=True, text=True)
if proc.returncode != 0:
    print(f"Compilation failed with code {proc.returncode}")
    print(proc.stdout)
    sys.exit(1)

log_output = (proc.stdout + proc.stderr).lower()
if "undefined" in log_output:
    print("Warning: 'undefined' found in tectonic log.")

pdf_path = f"{tmp_dir}/aastex/paper_08_r2.pdf"
if os.path.exists(pdf_path):
    print("Compilation SUCCESS.")
    print("PDF SHA256:", sha(pdf_path))
else:
    print("PDF not found!")
    sys.exit(1)
