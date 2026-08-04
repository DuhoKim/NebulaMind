#!/usr/bin/env python3
"""Merge independently drafted V2 narration objects into the canonical batch spec."""
from pathlib import Path
import json
import re

BASE = Path(__file__).resolve().parent
V1 = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/paper-videos-20260722T121412Z/paper_video_specs.json")
A = Path("/private/tmp/nebulamind_v2_scripts_a.json")
B = Path("/private/tmp/nebulamind_v2_scripts_b.json")
C = Path("/private/tmp/nebulamind_v2_scripts_c.json")
OUT = BASE / "paper_video_specs_v2.json"

v1 = json.loads(V1.read_text())
a = json.loads(A.read_text())
b = json.loads(B.read_text())["papers"]
c = [json.loads(C.read_text())]
proposals = {paper["key"]: paper for paper in [*a, *b, *c]}
old = {paper["key"]: paper for paper in v1["papers"]}

# Shared corrections discovered during independent source review.
proposals["z9-metallicity"]["scenes"][-1]["narration"] = (
    "The electron-temperature scale remains uncertain by zero point one to zero point two dex. "
    "The deficit’s direction survives checks, but its size is systematics-limited. "
    "This machine-generated draft is descriptive, not validated, and not a detection. Automated review is not journal or human peer review."
)
proposals["massive-abundance"]["scenes"][-1]["narration"] = (
    "At redshifts four to six, the counts do not require new cosmology once mass uncertainties are allowed. "
    "This machine-generated confrontation is descriptive, not validated; automated review is not journal or human peer review. Agreement within uncertainties does not confirm the simulation."
)
proposals["mzr-framework"]["scenes"][-1]["narration"] = (
    "This literature-based practitioner framework is not a new metallicity measurement; its thresholds summarize earlier work. "
    "The machine-generated draft is descriptive, not validated, and automated review is not journal or human peer review. It organizes evidence, not new data."
)
proposals["scaling-relations"]["scenes"][-1]["narration"] = (
    "Roughly zero point one dex of calibration uncertainty remains, and the low-mass nearby relation is extrapolated. Emission-line selection matters. "
    "This machine-generated manuscript uses public queries. Its status is descriptive and not validated; automated review is not journal or human peer review."
)
proposals["tng-validation"]["scenes"][4]["narration"] = (
    "A raw comparison can look reassuring because TNG starts low. After that starting residual is removed, its main-sequence growth reaches about one point three to one point six dex from redshift four to six. "
    "Observed galaxies rise only about zero point nine to one point zero dex."
)
proposals["tng-validation"]["scenes"][-1]["narration"] = (
    "The reproducible mismatch is over-strong star-formation growth; metallicity remains scale-limited. "
    "Selection, stellar-mass definitions, apertures, and a small redshift-six sample still matter. "
    "This machine-generated draft is descriptive, not validated; automated review is not journal or human peer review."
)
proposals["tng-validation"]["scenes"][-1]["source_lines"] = [
    "tng-validation.md:244-254",
    "tng-validation.md:276-289",
    "paper_video_specs.json:8-8",
    "paper_video_specs.json:388-396",
]

prefixes = {
    "z9-metallicity": "A slower, plain-English V2 explanation of the five core unlensed galaxies, the GN-z11 extension, the stacked cross-check, and the remaining abundance-scale uncertainty.",
    "scaling-relations": "A slower, plain-English V2 explanation of how star formation and gas metallicity change from SDSS to JWST, including calibration and selection caveats.",
    "massive-abundance": "A slower, plain-English V2 explanation of why stellar-mass uncertainties dissolve the redshift-four-to-six abundance tension while leaving the quiescent-galaxy residual unresolved.",
    "mzr-framework": "A slower, plain-English V2 explanation of calibration scale, aperture bias, diffuse ionized gas, and the framework needed for fair metallicity comparisons.",
    "tng-validation": "A slower, plain-English V2 explanation of calibration versus validation, TNG’s star-formation over-growth, and the scale-limited metallicity comparison.",
}

def words(text: str) -> int:
    return len(re.findall(r"[a-z0-9]+", text.lower().replace("’", "'")))

papers = []
tones = ["cyan", "magenta", "green"]
for key in [paper["key"] for paper in v1["papers"]]:
    proposal = proposals[key]
    original = old[key]
    scenes = proposal["scenes"]
    for scene in scenes:
        for i, card in enumerate(scene["cards"]):
            card.setdefault("tone", tones[i % len(tones)])
    title = original["youtube_title"] + " | Plain-English V2"
    if len(title) > 100:
        title = original["youtube_title"].replace("NebulaMind Paper: ", "NebulaMind: ") + " | Plain-English V2"
    description = (
        prefixes[key]
        + "\n\nNatural-paced Shimmer narration; manual English captions included.\n\n"
        + f"Read the manuscript: {original['source_url']}\n\n"
        + "Machine-generated by an autonomous research pipeline; descriptive, not validated; automated review is not journal or human peer review. "
        + ("This is not a formal statistical detection.\n\n" if key == "z9-metallicity" else "\n\n")
        + "NebulaMind Lab (autonomous run)\n#Astronomy #GalaxyEvolution #NebulaMind"
    )
    paper = {
        "key": key,
        "track": original["track"],
        "short_title": original["short_title"],
        "youtube_title": title,
        "source_url": original["source_url"],
        "pdf_path": str((BASE/"sources"/f"{key}.pdf").resolve()),
        "first_page_path": str((BASE/"sources"/f"{key}-first-page.png").resolve()),
        "description": description,
        "scenes": scenes,
    }
    counts = [words(scene["narration"]) for scene in scenes]
    if len(scenes) != 8 or any(not 26 <= count <= 52 for count in counts) or not 250 <= sum(counts) <= 340:
        raise RuntimeError(f"{key}: narration counts invalid {counts} total={sum(counts)}")
    if "not validated" not in scenes[-1]["narration"].lower() or "journal" not in scenes[-1]["narration"].lower():
        raise RuntimeError(f"{key}: spoken status boundary incomplete")
    if len(title) > 100 or len(description) > 5000:
        raise RuntimeError(f"{key}: metadata overflow")
    papers.append(paper)

spec = {
    "marker": "NEBULAMIND_FIVE_PAPER_VIDEO_SPECS_V2",
    "voice_provider": "openai_managed_nous_gateway",
    "voice_model": "gpt-4o-mini-tts",
    "voice": "shimmer",
    "provider_speed": 0.75,
    "post_tempo": 1.0,
    "target_wpm": [105, 125],
    "status_boundary": "Machine-generated by an autonomous research pipeline; descriptive, not validated; automated review is not journal or human peer review.",
    "papers": papers,
}
OUT.write_text(json.dumps(spec, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"path": str(OUT), "papers": [{"key": p["key"], "title": p["youtube_title"], "scene_words": [words(s["narration"]) for s in p["scenes"]], "total_words": sum(words(s["narration"]) for s in p["scenes"])} for p in papers]}, indent=2, ensure_ascii=False))
