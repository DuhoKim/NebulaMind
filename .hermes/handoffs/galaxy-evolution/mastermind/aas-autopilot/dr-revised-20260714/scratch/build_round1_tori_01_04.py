import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot")
ROUND = ROOT / "dr-revised-20260714/round1"
RECEIPTS = ROUND / "receipts"
MANIFEST = json.loads((ROUND / "ROUND1_INPUTS.json").read_text())

ADDITIONS = {
    1: {
        "section": r"""\section{Deep Research literature integration: aperture and classification limits}\label{sec:dr-r1}
Fixed-aperture spectroscopy does not by itself establish a global star-formation state. Empirical SDSS aperture-correction work and spatially resolved MaNGA profiles show why central and galaxy-wide star-formation diagnostics must be distinguished \citep{duartepuertas2017,belfiore2018}. These studies therefore sharpen, rather than relax, the existing boundary: the matched catalog-sSFR offset remains an association inside the selected optical denominator and cannot be read as a measurement of galaxy-wide quenching.

The broad BPT branch also mixes excitation sources. Equivalent-width information such as the WHAN framework can separate weak accretion candidates from systems whose low-ionization emission is compatible with retired stellar populations \citep{cidfernandes2011}. A later physical analysis should therefore add aperture fraction, resolved structure, and equivalent-width controls before interpreting the optical subclasses; none of those missing observables is supplied by the present SDSS-only pilot.
""",
        "sources": [
            {"source_number": 2, "citation_key": "duartepuertas2017", "citation": "Duarte Puertas et al. (2017), A&A, 599, A71", "identifier": "DOI:10.1051/0004-6361/201629044; arXiv:1611.07935", "role": "method-support", "verification_url": "https://doi.org/10.1051/0004-6361/201629044", "verification_result": "resolved to Aperture-free star formation rate of SDSS star-forming galaxies; author/year/volume/article matched"},
            {"source_number": 3, "citation_key": "belfiore2018", "citation": "Belfiore et al. (2018), MNRAS, 477, 3014", "identifier": "DOI:10.1093/mnras/sty768; ADS:2018MNRAS.477.3014B", "role": "interpretation-caveat", "verification_url": "https://doi.org/10.1093/mnras/sty768", "verification_result": "resolved to SDSS IV MaNGA -- sSFR profiles and the slow quenching of discs in green valley galaxies; metadata matched"},
            {"source_number": 5, "citation_key": "cidfernandes2011", "citation": "Cid Fernandes et al. (2011), MNRAS, 413, 1687", "identifier": "DOI:10.1111/j.1365-2966.2011.18244.x; arXiv:1012.4426", "role": "method-support", "verification_url": "https://doi.org/10.1111/j.1365-2966.2011.18244.x", "verification_result": "resolved to comprehensive classification of galaxies in the Sloan Digital Sky Survey: how to tell true from fake AGN?; metadata matched"},
        ],
        "bibitems": r"""\bibitem[Duarte Puertas et al.(2017)]{duartepuertas2017} Duarte Puertas, S., Vilchez, J.~M., Iglesias-Páramo, J., et al. 2017, A\&A, 599, A71
\bibitem[Belfiore et al.(2018)]{belfiore2018} Belfiore, F., Maiolino, R., Bundy, K., et al. 2018, MNRAS, 477, 3014
\bibitem[Cid Fernandes et al.(2011)]{cidfernandes2011} Cid Fernandes, R., Stasińska, G., Mateus, A., \& Vale Asari, N. 2011, MNRAS, 413, 1687
""",
        "special_skips": {6: "identifier inconsistency in packet: DOI 10.1093/mnras/stac546 does not match the cited MNRAS 512, 1052 paper", 13: "packet identifier/title evidence is internally inconsistent across captured anchors", 14: "packet year/arXiv evidence is internally inconsistent across captured anchors"},
    },
    2: {
        "section": r"""\section{Deep Research literature integration: density-proxy limits}\label{sec:dr-r1}
Projected neighbour ranks are useful empirical environment coordinates, but their physical interpretation depends on spectroscopic completeness and projection. SDSS light-cone work documents that fibre assignment can remove close angular pairs, so a nearest-neighbour statistic in a spectroscopic sample must not be treated as an unbiased reconstruction of the densest environments \citep{dongpaez2024}. This caveat applies to the proxy, not to the unchanged high-minus-low comparison reported above.

Separating ram pressure, starvation, and preprocessing requires more than a projected rank. Group/cluster studies use central--satellite classification and projected phase space to connect galaxy location to an infall history \citep{oxland2024}. Those quantities are absent here. The present result therefore remains a mass-adjusted association within the emission-line denominator and is a target-selection input for a later halo- and phase-space-resolved analysis.
""",
        "sources": [
            {"source_number": 2, "citation_key": "dongpaez2024", "citation": "Dong-Páez et al. (2024), MNRAS, 528, 7236", "identifier": "DOI:10.1093/mnras/stae062; arXiv:2208.00540", "role": "interpretation-caveat", "verification_url": "https://doi.org/10.1093/mnras/stae062", "verification_result": "resolved to Uchuu--SDSS galaxy light-cones: a clustering, redshift space distortion and baryonic acoustic oscillation study; metadata matched"},
            {"source_number": 4, "citation_key": "oxland2024", "citation": "Oxland et al. (2024), MNRAS, 529, 3651", "identifier": "DOI:10.1093/mnras/stae747", "role": "future-data-motivation", "verification_url": "https://doi.org/10.1093/mnras/stae747", "verification_result": "resolved to Satellite quenching and morphological transformation of galaxies in groups and clusters; metadata matched"},
        ],
        "bibitems": r"""\bibitem[Dong-Páez et al.(2024)]{dongpaez2024} Dong-Páez, C.~A., Smith, A., Szewciw, A.~O., et al. 2024, MNRAS, 528, 7236
\bibitem[Oxland et al.(2024)]{oxland2024} Oxland, M., Parker, L.~C., de Carvalho, R.~R., \& Sampaio, V.~M. 2024, MNRAS, 529, 3651
""",
        "special_skips": {8: "no source-specific checkable identifier in the packet", 11: "citation given only indirectly via another packet source", 13: "citation given only indirectly via another packet source", 15: "citation given only indirectly and with inconsistent arXiv context", 19: "citation given only indirectly via another packet source", 20: "future-volume metadata not independently settled for round 1"},
    },
    3: {
        "section": r"""\section{Deep Research literature integration: optical and radio duty-cycle mismatch}\label{sec:dr-r1}
An optical BPT fraction is not interchangeable with a radio-AGN duty cycle. Radio-selected studies find strong dependence on host stellar mass, star-formation state, and redshift, while probabilistic radio-source classifications expose populations that are not recovered by a single optical emission-line partition \citep{kondapally2025,drake2024}. The fractions above therefore remain optical target-pool measurements, not calorimetric estimates of maintenance heating.

Low-ionization optical emission also need not imply an accreting nucleus. Equivalent-width diagnostics can separate weak active candidates from retired systems powered by evolved stellar populations \citep{cidfernandes2011}. A physical heating-to-cooling test still requires the already named radio powers, X-ray cavities, cooling luminosities, halo-selected parents, and nondetection modelling; the added literature does not supply those missing observations for this sample.
""",
        "sources": [
            {"source_number": 2, "citation_key": "kondapally2025", "citation": "Kondapally et al. (2025), MNRAS, 536, 554", "identifier": "DOI:10.1093/mnras/stae2567; arXiv:2411.08104", "role": "interpretation-caveat", "verification_url": "https://doi.org/10.1093/mnras/stae2567", "verification_result": "resolved to Radio-AGN activity across the galaxy population: dependence on stellar mass, star formation rate, and redshift; metadata matched"},
            {"source_number": 3, "citation_key": "drake2024", "citation": "Drake et al. (2024), MNRAS, 534, 1107", "identifier": "DOI:10.1093/mnras/stae2117; arXiv:2409.11465", "role": "interpretation-caveat", "verification_url": "https://doi.org/10.1093/mnras/stae2117", "verification_result": "resolved to LoTSS DR2 probabilistic spectral source classifications and faint radio source demographics; metadata matched"},
            {"source_number": 5, "citation_key": "cidfernandes2011", "citation": "Cid Fernandes et al. (2011), MNRAS, 413, 1687", "identifier": "DOI:10.1111/j.1365-2966.2011.18244.x; arXiv:1012.4426", "role": "interpretation-caveat", "verification_url": "https://doi.org/10.1111/j.1365-2966.2011.18244.x", "verification_result": "resolved to comprehensive classification of galaxies in the Sloan Digital Sky Survey: how to tell true from fake AGN?; metadata matched"},
        ],
        "bibitems": r"""\bibitem[Kondapally et al.(2025)]{kondapally2025} Kondapally, R., Best, P.~N., Duncan, K.~J., et al. 2025, MNRAS, 536, 554
\bibitem[Drake et al.(2024)]{drake2024} Drake, A.~B., Smith, D.~J.~B., Hardcastle, M.~J., et al. 2024, MNRAS, 534, 1107
\bibitem[Cid Fernandes et al.(2011)]{cidfernandes2011} Cid Fernandes, R., Stasińska, G., Mateus, A., \& Vale Asari, N. 2011, MNRAS, 413, 1687
""",
        "special_skips": {4: "outside round-1 priority and not needed after two settled radio-demography sources", 6: "preprint-only and unnecessary after verified foundational equivalent-width source", 10: "post-cutoff preprint metadata not settled", 11: "anonymous/ambiguous authorship and post-cutoff preprint"},
    },
    4: {
        "section": r"""\section{Deep Research literature integration: resolved and multiphase escape tests}\label{sec:dr-r1}
Ionized-gas disturbances and reduced star formation need not be causally coupled. In a low-redshift type-2 quasar sample, resolved line-profile analysis found widespread warm-ionized outflow signatures without a corresponding correlation between the measured gas kinematics and star-formation rate on the scales probed \citep{bessiere2024}. That comparison reinforces the present draft's existing restriction: a high-excitation SDSS denominator cannot establish that an outflow caused the catalog-sSFR difference.

Escape and recycling require measurements that the single fibre does not contain. Resolved kinematics can compare an outflow with a host potential \citep{zheng2023}, while subarcsecond CO observations show that even a compact radio jet can alter molecular-gas excitation and turbulence \citep{audibert2023}. These are methodological examples for future follow-up, not measurements of the 4,440 candidates here; the current result remains an optical target list.
""",
        "sources": [
            {"source_number": 5, "citation_key": "bessiere2024", "citation": "Bessiere et al. (2024), A&A, 689, A271", "identifier": "DOI:10.1051/0004-6361/202348795", "role": "interpretation-caveat", "verification_url": "https://doi.org/10.1051/0004-6361/202348795", "verification_result": "resolved to QSOFEED: Relationship between star formation and active galactic nuclei feedback; abstract and metadata matched"},
            {"source_number": 7, "citation_key": "zheng2023", "citation": "Zheng et al. (2023), MNRAS, 523, 3274", "identifier": "DOI:10.1093/mnras/stad1642", "role": "future-data-motivation", "verification_url": "https://doi.org/10.1093/mnras/stad1642", "verification_result": "resolved to an escaping outflow in a galaxy with an intermediate-mass black hole; metadata matched"},
            {"source_number": 11, "citation_key": "audibert2023", "citation": "Audibert et al. (2023), A&A, 671, L12", "identifier": "DOI:10.1051/0004-6361/202345964", "role": "future-data-motivation", "verification_url": "https://doi.org/10.1051/0004-6361/202345964", "verification_result": "resolved to Jet-induced molecular gas excitation and turbulence in the Teacup; abstract and metadata matched"},
        ],
        "bibitems": r"""\bibitem[Bessiere et al.(2024)]{bessiere2024} Bessiere, P.~S., Ramos Almeida, C., Holden, L.~R., Tadhunter, C.~N., \& Canalizo, G. 2024, A\&A, 689, A271
\bibitem[Zheng et al.(2023)]{zheng2023} Zheng, Z., et al. 2023, MNRAS, 523, 3274
\bibitem[Audibert et al.(2023)]{audibert2023} Audibert, A., Ramos Almeida, C., García-Burillo, S., et al. 2023, A\&A, 671, L12
""",
        "special_skips": {1: "packet DOI 10.3390/galaxies12020019 resolves to an unrelated cosmic-ray review, not the cited Harrison and Ramos Almeida AGN-feedback review", 13: "packet year and arXiv identifier conflict", 16: "packet DOI resolves to a different article than the cited source", 18: "packet DOI 10.1093/mnras/stad1163 resolves to an unrelated stellar-wind X-ray paper", 19: "packet DOI resolves to an unrelated infrared background-subtraction paper", 20: "packet DOI 10.1093/mnras/stad3920 resolves to an unrelated globular-cluster paper", 25: "packet DOI did not resolve; excluded rather than repaired speculatively"},
    },
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def original_lines_preserved(source, output):
    original = source.splitlines(keepends=True)
    revised = output.splitlines(keepends=True)
    cursor = 0
    for line in revised:
        if cursor < len(original) and line == original[cursor]:
            cursor += 1
    return cursor == len(original)


def main():
    RECEIPTS.mkdir(parents=True, exist_ok=True)
    candidates = json.loads((ROUND / "ROUND1_PACKET_SOURCE_CANDIDATES.json").read_text())
    by_paper = {row["paper_id"]: row for row in candidates["papers"]}
    generated = []
    for paper in range(1, 5):
        item = MANIFEST["inputs"][paper - 1]
        source_path = Path(item["source_tex"])
        packet_path = Path(item["source_packet"])
        output_path = Path(item["round1_output"])
        source = source_path.read_text()
        cfg = ADDITIONS[paper]
        if "\\section{Reproducibility and safety}" not in source:
            raise RuntimeError(f"paper_{paper:02d}: missing insertion anchor")
        if "\\end{thebibliography}" not in source:
            raise RuntimeError(f"paper_{paper:02d}: missing bibliography anchor")
        revised = source.replace("\\section{Reproducibility and safety}", cfg["section"] + "\n\\section{Reproducibility and safety}", 1)
        revised = revised.replace("\\end{thebibliography}", "\n" + cfg["bibitems"] + "\\end{thebibliography}", 1)
        if not original_lines_preserved(source, revised):
            raise RuntimeError(f"paper_{paper:02d}: original line sequence changed")
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(revised)
        selected = {row["source_number"] for row in cfg["sources"]}
        skipped = []
        for row in by_paper[f"paper_{paper:02d}"]["sources"]:
            if row["source_number"] in selected:
                continue
            skipped.append({
                "source_number": row["source_number"],
                "citation": row["citation"],
                "identifier": row["identifier"],
                "reason": cfg.get("special_skips", {}).get(row["source_number"], "not selected after round-1 verification: redundant, lower-priority, or unnecessary for the minimal additive integration"),
            })
        receipt = {
            "paper_id": f"paper_{paper:02d}",
            "round": 1,
            "writer": "Tori",
            "source_tex": str(source_path),
            "source_tex_sha256": sha(source_path),
            "source_packet": str(packet_path),
            "source_packet_sha256": sha(packet_path),
            "output_tex": str(output_path),
            "output_tex_sha256": sha(output_path),
            "original_lines_preserved_in_order": original_lines_preserved(source, revised),
            "original_measurement_text_changed": False,
            "added_sources": cfg["sources"],
            "skipped_sources": skipped,
            "association_not_causal": True,
            "real_data_only": True,
            "drafts_only": True,
            "dr_reference_only": True,
            "auto_apply_authorized": False,
            "generated_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        }
        receipt_path = RECEIPTS / f"paper_{paper:02d}_sources.json"
        receipt_path.write_text(json.dumps(receipt, indent=2, ensure_ascii=False, sort_keys=True) + "\n")
        note = (
            f"# paper_{paper:02d} round-1 revision\n\n"
            f"- Writer: Tori\n- Output: `{output_path}`\n- Output SHA-256: `{receipt['output_tex_sha256']}`\n"
            f"- Added source keys: `{', '.join(row['citation_key'] for row in cfg['sources'])}`\n"
            f"- Added sources: {len(cfg['sources'])}; skipped packet candidates: {len(skipped)}.\n"
            "- Every original line remains byte-for-byte in its original order; no original measurement, table value, figure caption, or claim-boundary sentence changed.\n"
            "- Added prose is literature framing only: association-not-causal, real-data-only, and drafts-only.\n"
            "- No browser/DR submit, broker-ledger append, DB/API/wiki/trust, deploy, git, publish, billing, credential, or account-setting action occurred.\n"
        )
        note_path = RECEIPTS / f"paper_{paper:02d}_revision.md"
        note_path.write_text(note)
        generated.append({"paper_id": receipt["paper_id"], "output": str(output_path), "sha256": receipt["output_tex_sha256"], "added": len(cfg["sources"]), "skipped": len(skipped)})
    print(json.dumps({"status": "TORI_ROUND1_01_04_COMPLETE", "generated": generated}, sort_keys=True))


if __name__ == "__main__":
    main()
