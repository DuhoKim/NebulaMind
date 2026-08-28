#!/usr/bin/env python3
"""Build source-grounded visual proposals for the C41 UVLF worker-Yui lane.

This is not an official candidate renderer. It reads frozen source artifacts and
writes only review PNGs under this worker directory. No audio, TTS, shared tool,
storyboard-of-record, public video, or candidate bundle is touched.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from PIL import Image

ROOT = Path("/Users/duhokim/NebulaMind/NebulaMind")
SOURCE = ROOT / ".hermes/handoffs/c41-trackb-shape1-uvlf-20260804"
OUT_ROOT = (
    ROOT
    / ".hermes/handoffs/weekend-video-sextet-20260808T0136K"
    / "lane-c41-uvlf/worker-yui/visual_proposals"
)
OUT = OUT_ROOT / "v1"
EXPECTED = {
    SOURCE / "T1_CATALOG_MANIFEST.json": "50a7a5e81330ba2c251cb84b5e1bb0740a11aa5242e57ba47c96192c6d94b432",
    SOURCE / "T3_CENSUS_RESULTS.json": "4b21d432524a55bf5746fb3685e89360eaa33f143f68c042975f7259dd645ed7",
    SOURCE / "T3_CENSUS_SAMPLE.jsonl": "1cdb3de8738ecf1b80328c147a0dd25a159b147c1b76a1e7dd6473a16eddf5c5",
}

BG = "#0b0f1a"
PANEL = "#111827"
FG = "#eef2f7"
DIM = "#a7b2c7"
BLUE = "#76adff"
TEAL = "#55d6be"
AMBER = "#f2b567"
RED = "#ff7b7b"
GRID = "#314059"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def freeze_inputs() -> None:
    mismatches = []
    for path, expected in EXPECTED.items():
        actual = sha256(path)
        if actual != expected:
            mismatches.append(f"{path.name}: expected {expected}, got {actual}")
    if mismatches:
        raise SystemExit("SOURCE HASH DRIFT — refusing proposal build:\n" + "\n".join(mismatches))


def new_frame(title: str, kicker: str):
    fig = plt.figure(figsize=(19.2, 10.8), dpi=100, facecolor=BG)
    ax = fig.add_axes((0, 0, 1, 1))
    ax.set_xlim(0, 1920)
    ax.set_ylim(1080, 0)
    ax.axis("off")
    ax.text(94, 72, kicker.upper(), color=BLUE, fontsize=19, weight="bold")
    ax.text(94, 130, title, color=FG, fontsize=38, weight="bold", va="top")
    ax.text(
        94,
        1030,
        "WORKER-YUI VISUAL PROPOSAL • source-grounded • no audio • not an official candidate",
        color="#66748d",
        fontsize=13,
    )
    return fig, ax


def rounded_box(ax, xy, wh, title, value, body, color=BLUE, value_size=42):
    x, y = xy
    w, h = wh
    ax.add_patch(
        FancyBboxPatch(
            (x, y),
            w,
            h,
            boxstyle="round,pad=0.02,rounding_size=24",
            linewidth=2.4,
            edgecolor=color,
            facecolor=PANEL,
        )
    )
    ax.text(x + 34, y + 42, title.upper(), color=color, fontsize=17, weight="bold", va="top")
    ax.text(x + 34, y + 112, value, color=FG, fontsize=value_size, weight="bold", va="top")
    ax.text(x + 34, y + h - 45, body, color=DIM, fontsize=18, va="bottom", linespacing=1.4)


def save(fig, name: str) -> None:
    path = OUT / name
    fig.savefig(path, dpi=100, facecolor=BG)
    plt.close(fig)


def build_contact_sheet() -> None:
    paths = sorted(OUT.glob("state_*.png"))
    assert len(paths) == 7
    rows = (len(paths) + 1) // 2
    sheet = Image.new("RGB", (1280, rows * 360), BG)
    for index, path in enumerate(paths):
        frame = Image.open(path).convert("RGB").resize((640, 360), Image.Resampling.LANCZOS)
        sheet.paste(frame, ((index % 2) * 640, (index // 2) * 360))
    sheet.save(OUT / "contact_sheet.png")


def channel_frames(manifest: dict, results: dict) -> None:
    candidates = manifest["candidates"]
    name_reachable = sum(any(ch.startswith("name:") for ch in c["found_by_channels"]) for c in candidates)
    ucd_only = sum(c["found_by_channels"] == ["ucd:magAbs"] for c in candidates)
    assert len(candidates) == 112
    assert name_reachable == 20
    assert ucd_only == 92
    assert results["n_catalogs_counted"] == 67
    assert results["total_rows_in_slices"] == 6417
    counted_records = [record for record in results["catalogs"].values() if record["status"] == "counted"]
    assert len(counted_records) == 67
    assert sum(record["rows_in_slices"] > 0 for record in counted_records) == 27
    assert sum(record["rows_in_slices"] == 0 for record in counted_records) == 40

    fig, ax = new_frame(
        "A name-only query reaches 20 of 112 frozen VizieR tables",
        "Bright-end UV luminosity functions — VizieR search 1 of 3",
    )
    rounded_box(
        ax,
        (130, 280),
        (710, 410),
        "Column-name search",
        "20 of 112",
        "Frozen VizieR candidate tables reachable by\nMUV / M_UV / M1500 column-name patterns",
        color=AMBER,
    )
    ax.annotate("", xy=(1110, 485), xytext=(865, 485), arrowprops={"arrowstyle": "->", "lw": 3, "color": DIM})
    ax.text(1160, 450, "Most candidate tables are\nmissed by the name search", color=DIM, fontsize=25, va="center")
    ax.text(
        95,
        880,
        "Scope: frozen two-channel VizieR manifest; other archives and repositories were not exhaustively searched.",
        color=AMBER,
        fontsize=17,
        weight="bold",
    )
    ax.text(
        95,
        950,
        "Display source: NebulaMind Autonomous Research Lab (2026), §§3.1–3.2; VizieR column metadata.",
        color=DIM,
        fontsize=16,
    )
    save(fig, "state_01_name_channel.png")

    fig, ax = new_frame(
        "Physical-meaning metadata finds the other 92 tables",
        "Bright-end UV luminosity functions — VizieR search 2 of 3",
    )
    rounded_box(ax, (100, 270), (500, 410), "Name-reachable", "20", "Candidate tables", color=AMBER)
    rounded_box(
        ax,
        (710, 270),
        (600, 410),
        "Physical-meaning tags (UCD)",
        "+92",
        "Additional candidates found only via\nphys.magAbs physical-meaning tags",
        color=TEAL,
    )
    rounded_box(ax, (1420, 270), (400, 410), "Manifest", "112", "Candidate tables total", color=BLUE)
    for start, end in [((610, 475), (690, 475)), ((1320, 475), (1400, 475))]:
        ax.annotate("", xy=end, xytext=start, arrowprops={"arrowstyle": "->", "lw": 3, "color": DIM})
    ax.text(100, 760, "Partition shown: 20 name-reachable + 92 UCD-only = 112 candidates.", color=FG, fontsize=23, weight="bold")
    ax.text(
        100,
        820,
        "This is search reach, not scientific eligibility.",
        color=AMBER,
        fontsize=21,
        weight="bold",
    )
    ax.text(
        100,
        875,
        "Scope: frozen two-channel VizieR manifest; not an exhaustive search of every public repository.",
        color=DIM,
        fontsize=17,
    )
    ax.text(
        95,
        950,
        "Display source: NebulaMind Autonomous Research Lab (2026), §§3.1–3.2; VizieR column metadata.",
        color=DIM,
        fontsize=16,
    )
    save(fig, "state_02_ucd_partition.png")

    fig, ax = new_frame(
        "Eligibility separates candidates from countable catalogues",
        "Archival search flow — state 3 of 3",
    )
    xs = [70, 420, 770, 1120, 1470]
    values = ["112", "67", "34", "1", "10"]
    labels = [
        "candidate\ntables",
        "counted\ncatalogues",
        "disqualified\ncandidate tables",
        "pending candidate\ntable",
        "skipped candidate\ntables",
    ]
    bodies = ["", "", "", "", "no usable magnitude–\nredshift pair"]
    colors = [BLUE, TEAL, RED, AMBER, DIM]
    for x, value, label, body, color in zip(xs, values, labels, bodies, colors):
        rounded_box(ax, (x, 270), (300, 330), label, value, body, color=color, value_size=44)
    ax.text(95, 655, "Partition: 67 counted + 34 disqualified + 1 pending + 10 skipped = 112 candidates", color=DIM, fontsize=19)
    ax.text(95, 710, "67 counted catalogues  →  6,417 raw rows in the four frozen redshift slices", color=FG, fontsize=28, weight="bold")
    ax.text(95, 755, "Row provenance: 27 catalogues contribute rows; 40 counted catalogues contribute zero in the frozen slices.", color=DIM, fontsize=17)
    ax.text(
        95,
        815,
        "RAW COUNTS — no completeness, bandpass homogenization, cosmic-variance inference, or catalogue merging.",
        color=AMBER,
        fontsize=19,
        weight="bold",
    )
    ax.text(
        95,
        950,
        "Display source: NebulaMind Autonomous Research Lab (2026), §§3 and 5; VizieR archive census.",
        color=DIM,
        fontsize=16,
    )
    save(fig, "state_03_eligibility_funnel.png")


def evidence_plane_frames(rows: list[dict]) -> None:
    slice_rows = [row for row in rows if 10.0 <= row["z"] < 11.5]
    bright = [row for row in slice_rows if row["muv"] <= -20.0]
    other = [row for row in slice_rows if row["muv"] > -20.0]
    dominant_table = "J/A+A/704/A339/lephare"
    dominant = [row for row in slice_rows if row["table"] == dominant_table]
    non_dominant = [row for row in slice_rows if row["table"] != dominant_table]
    non_dominant_bright = [row for row in bright if row["table"] != dominant_table]
    assert len(slice_rows) == 453
    assert len(bright) == 176
    assert len(dominant) == 420
    assert len(non_dominant) == 33
    assert len({row["table"] for row in slice_rows}) == 6
    assert len(bright) - len(non_dominant_bright) == 161
    assert min(row["muv"] for row in slice_rows) >= -24.5
    assert max(row["muv"] for row in slice_rows) <= -9.5

    def draw_plane(name: str, state: int, highlight: bool, final: bool) -> None:
        fig = plt.figure(figsize=(19.2, 10.8), dpi=100, facecolor=BG)
        ax = fig.add_axes((0.09, 0.20, 0.62, 0.66), facecolor=PANEL)
        ax.set_xlim(10.0, 11.52)
        ax.set_ylim(-24.5, -9.5)
        ax.invert_yaxis()
        ax.set_xlabel("redshift z", color=FG, fontsize=22, labelpad=14)
        ax.set_ylabel("catalogued UV-like absolute magnitude (AB)", color=FG, fontsize=22, labelpad=16)
        ax.tick_params(colors=DIM, labelsize=17)
        ax.grid(color=GRID, alpha=0.55, linewidth=0.8)
        for spine in ax.spines.values():
            spine.set_color(GRID)
            spine.set_linewidth(1.5)
        ax.axvspan(10.0, 11.5, color=BLUE, alpha=0.035)
        ax.axvline(11.5, color=AMBER, linewidth=1.4, linestyle=(0, (2, 2)), alpha=0.9)
        ax.text(
            11.492,
            -23.9,
            "z = 11.5 excluded",
            color=AMBER,
            fontsize=11,
            rotation=90,
            ha="right",
            va="top",
        )
        if highlight:
            ax.scatter(
                [r["z"] for r in other],
                [r["muv"] for r in other],
                s=24,
                c="#6f7e96",
                alpha=0.42,
                edgecolors="none",
                label="other raw rows in slice",
            )
            ax.scatter(
                [r["z"] for r in bright],
                [r["muv"] for r in bright],
                s=34,
                c=AMBER,
                alpha=0.80,
                edgecolors="none",
                label="reported magnitude ≤ −20",
            )
            ax.scatter(
                [r["z"] for r in non_dominant],
                [r["muv"] for r in non_dominant],
                s=70,
                facecolors="none",
                edgecolors=TEAL,
                linewidths=1.35,
                marker="D",
                alpha=0.95,
                label="five other source tables",
            )
            ax.axhline(-20.0, color=AMBER, linewidth=3.0, linestyle="--")
            ax.text(
                11.47,
                -20.25,
                "reported-magnitude cut = −20",
                color=AMBER,
                fontsize=16,
                weight="bold",
                ha="right",
                bbox={"boxstyle": "round,pad=0.25", "facecolor": PANEL, "edgecolor": AMBER, "alpha": 0.92},
            )
            ax.legend(loc="lower right", frameon=True, facecolor=BG, edgecolor=GRID, labelcolor=FG, fontsize=15)
        else:
            ax.scatter(
                [r["z"] for r in dominant],
                [r["muv"] for r in dominant],
                s=26,
                c=BLUE,
                alpha=0.42,
                edgecolors="none",
                label="COSMOS2025 LePhare table (420)",
            )
            ax.scatter(
                [r["z"] for r in non_dominant],
                [r["muv"] for r in non_dominant],
                s=58,
                c=TEAL,
                alpha=0.82,
                edgecolors="none",
                marker="D",
                label="five other VizieR tables (33)",
            )
            ax.legend(loc="lower right", frameon=True, facecolor=BG, edgecolor=GRID, labelcolor=FG, fontsize=14)
        fig.text(0.09, 0.93, f"Evidence plane — state {state} of 3", color=BLUE, fontsize=19, weight="bold")
        fig.text(0.09, 0.885, "The frozen 10 ≤ z < 11.5 census slice", color=FG, fontsize=34, weight="bold")
        provenance = (
            "Provenance: dominant table supplies 420/453 rows and 161/176 bright rows; five other tables supply 33 rows."
            if highlight
            else "Provenance: VizieR J/A+A/704/A339/lephare supplies 420/453 rows; five other tables supply 33."
        )
        fig.text(0.09, 0.845, provenance, color=TEAL, fontsize=13, weight="bold")
        fig.text(
            0.755,
            0.885,
            "Each point = one frozen row\n{table, reported magnitude, z}\nNo jitter or smoothing",
            color=BLUE,
            fontsize=13,
        )
        fig.text(0.755, 0.79, "CENSUS ROWS", color=TEAL, fontsize=17, weight="bold")
        fig.text(0.755, 0.72, "453", color=FG, fontsize=54, weight="bold")
        fig.text(0.755, 0.665, "raw rows at any magnitude", color=DIM, fontsize=18)
        if highlight:
            fig.text(0.755, 0.55, "BRIGHT SUBSET", color=AMBER, fontsize=17, weight="bold")
            fig.text(0.755, 0.48, "176 / 453", color=FG, fontsize=46, weight="bold")
            fig.text(0.755, 0.425, "rows with reported M$_{UV}$-like ≤ −20", color=DIM, fontsize=15)
        if final:
            fig.text(0.755, 0.35, "PUBLISHED-LF DATA", color=RED, fontsize=17, weight="bold")
            fig.text(
                0.755,
                0.315,
                "No predefined-roster table met\nthe machine-readable\ndata requirements",
                color=FG,
                fontsize=15,
                weight="bold",
                linespacing=1.3,
                va="top",
            )
            fig.text(
                0.755,
                0.215,
                "For this slice: missing extractable LF data,\nnot zero galaxies or zero published LFs.",
                color=DIM,
                fontsize=13,
                linespacing=1.3,
                va="top",
            )
        fig.text(
            0.09,
            0.11,
            "Raw rows only — no completeness, density inference, bandpass homogenization, or catalogue merging.",
            color=AMBER,
            fontsize=16,
            weight="bold",
        )
        fig.text(
            0.09,
            0.067,
            "Display source: NebulaMind Lab (2026), Table 1 and §§5–6; VizieR J/A+A/704/A339/lephare + five tables.",
            color=DIM,
            fontsize=13,
        )
        fig.text(
            0.09,
            0.04,
            "The 453-row denominator is derived from the frozen census packet; an audience-reachable supplement is required before release.",
            color=DIM,
            fontsize=12,
        )
        fig.text(
            0.755,
            0.015,
            "WORKER-YUI PROPOSAL • not an official candidate",
            color="#66748d",
            fontsize=12,
        )
        save(fig, name)

    draw_plane("state_04_slice_plane_rows.png", 1, highlight=False, final=False)
    draw_plane("state_05_slice_plane_threshold.png", 2, highlight=True, final=False)
    draw_plane("state_06_slice_plane_boundary.png", 3, highlight=True, final=True)


def repair_frame() -> None:
    fig, ax = new_frame(
        "Close the gap with a self-describing data packet",
        "Reproducibility repair — final state",
    )
    rounded_box(
        ax,
        (70, 250),
        (540, 260),
        "Machine-readable table",
        "φ + uncertainty",
        "Luminosity-function value\nand uncertainty per bin",
        color=TEAL,
        value_size=31,
    )
    rounded_box(ax, (690, 250), (540, 260), "Bin geometry", "M$_{UV}$ edges + widths", "Explicit, not inferred from a figure", color=BLUE, value_size=29)
    rounded_box(ax, (1310, 250), (540, 260), "Redshift support", "interval + anchor", "Exact slice and effective redshift", color=AMBER, value_size=30)
    rounded_box(
        ax,
        (380, 555),
        (540, 260),
        "Conventions",
        "units + Hubble scaling",
        "Hubble-constant scaling\n(state the h convention)",
        color=BLUE,
        value_size=27,
    )
    rounded_box(
        ax,
        (1000, 555),
        (540, 260),
        "Transformations",
        "selection + corrections",
        "Completeness, interlopers, lensing,\nand any conversions",
        color=TEAL,
        value_size=27,
    )
    ax.text(
        95,
        865,
        "STUDY STATUS — human-cleared for Lab landing; not journal-refereed, independently validated, or a journal result.",
        color=RED,
        fontsize=16,
        weight="bold",
    )
    ax.text(95, 920, "PROCEDURE — not a new measurement", color=AMBER, fontsize=19, weight="bold")
    ax.text(
        95,
        965,
        "Display source: NebulaMind Lab (2026), §6, The Machine-Readable Bright End; C41 paper-specific review record.",
        color=DIM,
        fontsize=16,
    )
    save(fig, "state_07_reproducibility_packet.png")


def main() -> None:
    global OUT
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", default="v10", choices=("v1", "v2", "v3", "v4", "v5", "v6", "v7", "v8", "v9", "v10"))
    args = parser.parse_args()
    OUT = OUT_ROOT / args.version
    OUT.mkdir(parents=True, exist_ok=True)
    freeze_inputs()
    manifest = json.load((SOURCE / "T1_CATALOG_MANIFEST.json").open())
    results = json.load((SOURCE / "T3_CENSUS_RESULTS.json").open())
    rows = [json.loads(line) for line in (SOURCE / "T3_CENSUS_SAMPLE.jsonl").open()]
    assert len(rows) == 6417
    channel_frames(manifest, results)
    evidence_plane_frames(rows)
    repair_frame()
    build_contact_sheet()
    receipt = {
        "status": "PASS_VISUAL_PROPOSAL_BUILD_ONLY",
        "official_candidate": False,
        "tts_invoked": False,
        "inputs": {path.name: sha256(path) for path in EXPECTED},
        "assertions": {
            "candidate_tables": 112,
            "name_reachable": 20,
            "ucd_only": 92,
            "counted_catalogues": 67,
            "counted_catalogues_with_rows": 27,
            "counted_catalogues_with_zero_rows": 40,
            "raw_rows_all_slices": 6417,
            "slice_10_11_5_rows": 453,
            "slice_10_11_5_bright_muv_le_minus20": 176,
            "slice_10_11_5_source_tables": 6,
            "slice_10_11_5_dominant_table_rows": 420,
            "slice_10_11_5_dominant_table_bright_rows": 161,
        },
        "outputs": sorted(path.name for path in OUT.glob("state_*.png")),
        "boundary": "Worker-Yui proposal only; Hwao remains sole integrator/candidate/shared-tool/TTS writer.",
    }
    (OUT / "BUILD_RECEIPT.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
