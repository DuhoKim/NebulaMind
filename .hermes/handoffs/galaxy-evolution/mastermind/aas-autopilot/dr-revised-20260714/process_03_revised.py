import os
import json
import hashlib
import re

def sha(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

BASE = "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/dr-revised-20260714"
IN_TEX = f"{BASE}/round1/paper_03_r1.tex"
OUT_TEX = f"{BASE}/round2/paper_03_r2.tex"

with open(IN_TEX, 'r') as f:
    text = f.read()

# Mechanically extract the invariant lines (digit-bearing lines between Section 2 and before Figure 1)
invariant_span = text[text.find(r"\section{Shared parent sample and selection function}"):text.find(r"\begin{figure}")]
digit_lines = [line.strip() for line in invariant_span.split('\n') if re.search(r'\d', line) and line.strip()]
invariant_line_count = len(digit_lines)

# Apply minimal, conservative replacements
s5_old = r"""\section{Interpretation and missing observables}\label{sec:missing}
SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page. The full proposal requires: X-ray cavity/cooling-luminosity measurements, radio jet powers, halo-selected parent catalogues, and nondetection modelling.

Radio-mode and hot-atmosphere studies define the future calorimetric observables--jet power, cavities, cooling luminosity, and group gas--that are absent from this optical denominator \citep{best2005,mcnamara2007,mcnamara2012,heckmanbest2014,eckert2024}."""

s5_new = r"""\section{Interpretation and missing observables}\label{sec:missing}
SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page. The full proposal requires: X-ray cavity/cooling-luminosity measurements, radio jet powers, halo-selected parent catalogues, and nondetection modelling.

Radio-mode and hot-atmosphere studies define the future calorimetric observables--jet power, cavities, cooling luminosity, and group gas--that are absent from this optical denominator \citep{best2005,mcnamara2007,mcnamara2012,heckmanbest2014,eckert2024}. Radio luminosity-function and kinetic-power work is future context and does not turn this optical denominator into calorimetry \citep{kondapally2023}."""

bib_old = r"""\bibitem[Cid Fernandes et al.(2011)]{cidfernandes2011} Cid Fernandes, R., Stasińska, G., Mateus, A., \& Vale Asari, N. 2011, MNRAS, 413, 1687
\end{thebibliography}"""

bib_new = r"""\bibitem[Cid Fernandes et al.(2011)]{cidfernandes2011} Cid Fernandes, R., Stasińska, G., Mateus, A., \& Vale Asari, N. 2011, MNRAS, 413, 1687
\bibitem[Kondapally et al.(2023)]{kondapally2023} Kondapally, R., Best, P.~N., Raouf, M., et al. 2023, MNRAS, 523, 5292
\end{thebibliography}"""

new_text = text.replace(s5_old, s5_new)
new_text = new_text.replace(bib_old, bib_new)

assert new_text != text, "Expected paper_03 revision did not apply"
assert new_text.count(r"\citep{kondapally2023}") == 1, "Expected exactly one new kondapally2023 citation"
assert new_text.count(r"{kondapally2023}") == 2, "Expected exactly one cite and one bibitem for kondapally2023"

# Verify invariants mechanically
new_invariant_span = new_text[new_text.find(r"\section{Shared parent sample and selection function}"):new_text.find(r"\begin{figure}")]
new_digit_lines = [line.strip() for line in new_invariant_span.split('\n') if re.search(r'\d', line) and line.strip()]

assert new_digit_lines == digit_lines, "Invariants altered!"

# Write out
with open(OUT_TEX, 'w') as f:
    f.write(new_text)

# Generate Receipt
import datetime
now = datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z")

receipt = {
  "added_or_corrected_sources": [
    {"citation": "Kondapally et al. (2023), MNRAS 523, 5292", "citation_key": "kondapally2023", "identifier": "DOI:10.1093/mnras/stad1813; arXiv:2306.11795", "role": "interpretation-caveat", "claim_boundary": "radio luminosity-function and kinetic-power work is future context and does not turn this optical denominator into calorimetry"}
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
  "paper_id": "paper_03",
  "publish_commit_git_performed": False,
  "real_data_only": True,
  "review_feedback_applied": [
    "interpretation and missing observables boundary",
    "bibliography"
  ],
  "round": 2,
  "skipped_review_sources_or_claims": [
    {"source": "Arnaudova et al.", "reason": "identity/fit uncertainty"},
    {"source": "Liu et al.", "reason": "identity/fit uncertainty"},
    {"source": "Jin et al.", "reason": "identity/fit uncertainty"},
    {"source": "Oh et al.", "reason": "identity/fit uncertainty"},
    {"source": "Fan & Li", "reason": "identity/fit uncertainty"},
    {"source": "Karsten et al.", "reason": "identity/fit uncertainty"}
  ],
  "source_round1_dr_review": f"{BASE}/round1/dr-review-packets/paper_03_round1_review_dr_packet.md",
  "source_round1_dr_review_sha256": sha(f"{BASE}/round1/dr-review-packets/paper_03_round1_review_dr_packet.md"),
  "source_round1_tex": IN_TEX,
  "source_round1_tex_sha256": sha(IN_TEX),
  "writer": "WonE"
}

with open(f"{BASE}/round2/receipts/paper_03_sources.json", "w") as f:
    json.dump(receipt, f, indent=2, sort_keys=True)
    f.write("\n")
with open(f"{BASE}/round2/receipts/paper_03_revision.md", "w") as f:
    f.write("# Revision notes for paper_03\nPreserved invariants exactly, mechanically verified invariant span lines. Added only kondapally2023 with strict claim boundary. Skipped all uncertain or future/unsupported sources. Conclusion remains unchanged. Local operations only.\n")

print(f"paper_03 processed successfully. Invariant line count: {invariant_line_count}")
