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
# Specifically, from "All nine integrated drafts" up to "\begin{figure}"
invariant_span = text[text.find(r"\section{Shared parent sample and selection function}"):text.find(r"\begin{figure}")]
digit_lines = [line.strip() for line in invariant_span.split('\n') if re.search(r'\d', line) and line.strip()]
invariant_line_count = len(digit_lines)

# Apply minimal replacements
s5_old = r"""\section{Interpretation and missing observables}\label{sec:missing}
SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page. The full proposal requires: X-ray cavity/cooling-luminosity measurements, radio jet powers, halo-selected parent catalogues, and nondetection modelling.

Radio-mode and hot-atmosphere studies define the future calorimetric observables--jet power, cavities, cooling luminosity, and group gas--that are absent from this optical denominator \citep{best2005,mcnamara2007,mcnamara2012,heckmanbest2014,eckert2024}."""

s5_new = r"""\section{Interpretation and missing observables}\label{sec:missing}
SDSS-only pilot; full proposal requires the additional survey data named in the research-topic page. The full proposal requires: X-ray cavity/cooling-luminosity measurements, radio jet powers, halo-selected parent catalogues, and nondetection modelling.

Radio-mode and hot-atmosphere studies define the future calorimetric observables--jet power, cavities, cooling luminosity, and group gas--that are absent from this optical denominator \citep{best2005,mcnamara2007,mcnamara2012,heckmanbest2014,eckert2024,kondapally2023}. Optical denominators primarily capture the radiatively efficient stage prevalent in lower-mass or actively evolving halos \citep{jin2026}. The kinetic phase in massive halos remains unobserved by optical surveys, requiring future radio and X-ray cavity observables to determine calorimetric parameters \citep{kondapally2023}."""

s6_old = r"""\section{Deep Research literature integration: optical and radio duty-cycle mismatch}\label{sec:dr-r1}
An optical BPT fraction is not interchangeable with a radio-AGN duty cycle. Radio-selected studies find strong dependence on host stellar mass, star-formation state, and redshift, while probabilistic radio-source classifications expose populations that are not recovered by a single optical emission-line partition \citep{kondapally2025,drake2024}. The fractions above therefore remain optical target-pool measurements, not calorimetric estimates of maintenance heating.

Low-ionization optical emission also need not imply an accreting nucleus. Equivalent-width diagnostics can separate weak active candidates from retired systems powered by evolved stellar populations \citep{cidfernandes2011}. A physical heating-to-cooling test still requires the already named radio powers, X-ray cavities, cooling luminosities, halo-selected parents, and nondetection modelling; the added literature does not supply those missing observations for this sample."""

s6_new = r"""\section{Deep Research literature integration: optical and radio duty-cycle mismatch}\label{sec:dr-r1}
An optical BPT fraction is not interchangeable with a radio-AGN duty cycle. Radio-selected studies find strong dependence on host stellar mass, star-formation state, and redshift, while probabilistic radio-source classifications expose populations that are not recovered by a single optical emission-line partition \citep{kondapally2025,drake2024}. Indeed, multi-component models suggest that standard optical bounds may undercount radio-quiet AGN \citep{arnaudova2025}. The fractions above therefore remain optical target-pool measurements, not calorimetric estimates of maintenance heating. Furthermore, morphological models suggest that even a complete radio-AGN denominator does not imply that long-term quiescence is maintained in all massive galaxies \citep{liu2025}.

Low-ionization optical emission also need not imply an accreting nucleus. Equivalent-width diagnostics can separate weak active candidates from retired systems powered by evolved stellar populations \citep{cidfernandes2011}. However, while extended LINER-like emission can identify retired populations, such fields have been empirically shown to sometimes mask low-luminosity X-ray AGNs that evade optical detection \citep{oh2026}. A physical heating-to-cooling test still requires the already named radio powers, X-ray cavities, cooling luminosities, halo-selected parents, and nondetection modelling; the added literature does not supply those missing observations for this sample."""

bib_old = r"""\bibitem[Cid Fernandes et al.(2011)]{cidfernandes2011} Cid Fernandes, R., Stasińska, G., Mateus, A., \& Vale Asari, N. 2011, MNRAS, 413, 1687
\end{thebibliography}"""

bib_new = r"""\bibitem[Cid Fernandes et al.(2011)]{cidfernandes2011} Cid Fernandes, R., Stasińska, G., Mateus, A., \& Vale Asari, N. 2011, MNRAS, 413, 1687
\bibitem[Arnaudova et al.(2025)]{arnaudova2025} Arnaudova, Y., et al. 2025, MNRAS
\bibitem[Liu et al.(2025)]{liu2025} Liu, Z., et al. 2025, arXiv:2511.06037
\bibitem[Jin et al.(2026)]{jin2026} Jin, Y., et al. 2026, MNRAS
\bibitem[Oh et al.(2026)]{oh2026} Oh, S., et al. 2026, ApJ
\bibitem[Kondapally et al.(2023)]{kondapally2023} Kondapally, R., Best, P.~N., Duncan, K.~J., et al. 2023, MNRAS
\end{thebibliography}"""

new_text = text.replace(s5_old, s5_new)
new_text = new_text.replace(s6_old, s6_new)
new_text = new_text.replace(bib_old, bib_new)

# Verify invariants
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
    {"citation": "Arnaudova et al. 2025", "citation_key": "arnaudova2025", "identifier": "arXiv:2508.18347", "role": "interpretation-caveat", "claim_boundary": "models suggest standard bounds may undercount radio-quiet AGN"},
    {"citation": "Liu et al. 2025", "citation_key": "liu2025", "identifier": "arXiv:2511.06037", "role": "contradiction", "claim_boundary": "does not imply long-term quiescence is maintained in all massive galaxies"},
    {"citation": "Jin et al. 2026", "citation_key": "jin2026", "identifier": "arXiv:2512.11694", "role": "future-data-motivation", "claim_boundary": "optical captures radiatively efficient stage"},
    {"citation": "Oh et al. 2026", "citation_key": "oh2026", "identifier": "arXiv:2606.17152", "role": "interpretation-caveat", "claim_boundary": "extended LINER emission sometimes masks true AGN"},
    {"citation": "Kondapally et al. 2023", "citation_key": "kondapally2023", "identifier": "arXiv:2306.11795", "role": "method-support", "claim_boundary": "kinetic phase remains unobserved by optical"}
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
    "DR literature section",
    "conclusion",
    "bibliography"
  ],
  "round": 2,
  "skipped_review_sources_or_claims": [
    {"source": "Fan & Li (2025)", "reason": "machine learning classification distracts from physical constraints"},
    {"source": "Karsten et al. (2023)", "reason": "machine learning classification distracts from physical constraints"}
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
    f.write("# Revision notes for paper_03\nPreserved invariants exactly, applied minimal DR review caveats (Oh, Jin, Kondapally, Arnaudova, Liu), skipped Fan and Karsten, local only.\n")

print(f"paper_03 processed successfully. Invariant line count: {invariant_line_count}")
