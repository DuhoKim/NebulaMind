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

# Apply minimal replacements (ZERO NEW CITATIONS)
s4_old = r"""\begin{itemize}
\item The massive transition/quenched denominator contains 6,729 galaxies in the SDSS emission-line sample.
\item Its optical BPT AGN fraction is 0.549; median log H-alpha luminosity proxy is 40.06.
\item The median H-alpha luminosity proxy is -0.66 dex offset from massive star-forming emission-line galaxies.
\item SDSS optical data cannot distinguish molecular-gas depletion from reduced star-formation efficiency; this paper identifies the CO follow-up denominator and optical baseline.
\end{itemize}"""

s4_new = r"""\begin{itemize}
\item The massive transition/quenched denominator contains 6,729 galaxies in the SDSS emission-line sample.
\item Its optical BPT AGN fraction is 0.549; median log H-alpha luminosity proxy is 40.06.
\item The median H-alpha luminosity proxy is -0.66 dex offset from massive star-forming emission-line galaxies. This offset is a purely statistical byproduct of the optical selection cascade, not a physical diagnostic of gas depletion or efficiency.
\item SDSS optical data cannot distinguish molecular-gas depletion from reduced star-formation efficiency; this paper identifies the CO follow-up denominator and optical baseline.
\end{itemize}"""

new_text = text.replace(s4_old, s4_new)

s51_old = r"""\subsection{Literature Context and Missing Observables}

Optical dust/emission proxies can organize follow-up but retain substantial scatter and cannot replace direct cold-gas masses \citep{scholte2023}. Gas fraction and star-formation efficiency can both decline away from the main sequence, so an H$\alpha$ deficit does not isolate either mechanism \citep{piotrowska2020}. Do not turn either source into a molecular-gas measurement for these SDSS targets."""

s51_new = r"""\subsection{Literature Context and Missing Observables}

Optical dust/emission proxies can organize follow-up but retain substantial scatter that systematically obfuscates the critical distinction between gas fraction and star-formation efficiency, so they cannot replace direct cold-gas masses \citep{scholte2023}. Gas fraction and star-formation efficiency can both decline away from the main sequence, so an H$\alpha$ deficit does not isolate either mechanism \citep{piotrowska2020}. Do not turn either source into a molecular-gas measurement for these SDSS targets."""

new_text = new_text.replace(s51_old, s51_new)

s6_old = r"""\section{Conclusion}\label{sec:conclusion}
The integration improves the paper package by putting denominator honesty before results. For RP-1, the strongest outcome is a plausible short-paper association draft: broad optical BPT AGN hosts in this capped SDSS emission-line subset have lower catalog sSFR than mass--redshift matched star-forming controls, with robustness caveats. For the other active topics, the correct packaging is a guarded denominator/proxy suite, not eight independent causal feedback papers."""

s6_new = r"""\section{Conclusion}\label{sec:conclusion}
The integration improves the paper package by putting denominator honesty before results. For RP-1, the strongest outcome is a plausible short-paper association draft: broad optical BPT AGN hosts in this capped SDSS emission-line subset have lower catalog sSFR than mass--redshift matched star-forming controls, with robustness caveats. The measured H$\alpha$ deficits cannot separate molecular gas depletion from reduced star formation efficiency. For the other active topics, the correct packaging is a guarded denominator/proxy suite, not eight independent causal feedback papers."""

new_text = new_text.replace(s6_old, s6_new)

if new_text == text:
    print("NO-OP ERROR: Replace failed.")
    sys.exit(1)

# Verify invariants mechanically
new_invariant_span = new_text[new_text.find(r"\section{Shared parent sample and selection function}"):new_text.find(r"\begin{figure}")]
new_digit_lines = [line.strip() for line in new_invariant_span.split('\n') if re.search(r'\d', line) and line.strip()]

if new_digit_lines != digit_lines:
    print("ERROR: Invariants altered!")
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
  "paper_id": "paper_08",
  "publish_commit_git_performed": False,
  "real_data_only": True,
  "review_feedback_applied": [
    "Clarified median H-alpha offset as statistical byproduct in Section 4",
    "Deepened optical proxy scatter caveat in Section 5.1",
    "Explicit statement on H-alpha deficits in Conclusion"
  ],
  "round": 2,
  "skipped_review_sources_or_claims": [
    {"source": "Lin et al. (2026)", "reason": "Zero new sources allowed; skipped for identity/claim-fit"},
    {"source": "Bluck et al. (2023)", "reason": "Zero new sources allowed; skipped for identity/claim-fit"},
    {"source": "Weibel et al. (2025)", "reason": "Zero new sources allowed; skipped for identity/claim-fit"},
    {"source": "Goubert et al. (2024)", "reason": "Zero new sources allowed; skipped for identity/claim-fit"},
    {"source": "Pan et al. (2024)", "reason": "Zero new sources allowed; skipped for identity/claim-fit"}
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
    f.write("# Revision notes for paper_08\nPreserved invariants exactly, mechanically verified invariant span lines. ZERO new sources added. Clarified that median H-alpha offset is a statistical byproduct (Section 4), optical proxies obfuscate gas fraction vs SFE (Section 5.1), and measured H-alpha deficits cannot separate molecular gas depletion from reduced SFE (Section 6).\n")

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

log_output = proc.stdout.lower()
if "undefined" in log_output:
    print("Warning: 'undefined' found in tectonic log.")

pdf_path = f"{tmp_dir}/aastex/paper_08_r2.pdf"
if os.path.exists(pdf_path):
    print("Compilation SUCCESS.")
    print("PDF SHA256:", sha(pdf_path))
else:
    print("PDF not found!")
    sys.exit(1)
