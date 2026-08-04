#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, cast

import pymupdf

BASE = Path(__file__).resolve().parent
SOURCE_DIR = BASE / "sources-v4"
FIGURE_DIR = SOURCE_DIR / "figures"
FREEZE = BASE / "V4_SOURCE_FREEZE.json"

SOURCES = [
    {
        "key": "z9-metallicity",
        "url": "https://nebulamind.net/studies/z9-10-unlensed-metallicity-deficit.pdf",
        "expected_sha256": "37c7795175ead264403a68c882c15b4d39e2c203836e9c829a13e67110fc24e8",
    },
    {
        "key": "scaling-relations",
        "url": "https://nebulamind.net/agent-reports/research-frontiers/galaxy-evolution-highz-scaling-relations-draft.pdf",
        "expected_sha256": "e878fff31192d3bfa1677e6784d3bf3901aa9bb95522d3dd801ea0ed6a145f0b",
    },
    {
        "key": "massive-abundance",
        "url": "https://nebulamind.net/agent-reports/research-frontiers/tng-massive-galaxy-abundance-systematics.pdf",
        "expected_sha256": "189a2764a0b8e310802fb31bd53db3a64be49ac6411fe5f5b38af62cefa23f5d",
    },
    {
        "key": "mzr-framework",
        "url": "https://nebulamind.net/agent-reports/research-frontiers/mzr-aperture-calibration-framework.pdf",
        "expected_sha256": "bb0869aa02afd311d91605d60e3613e88bead425a088dd1bea844c6ff9b0e59e",
    },
    {
        "key": "tng-validation",
        "url": "https://nebulamind.net/agent-reports/research-frontiers/galaxy-evolution-tng-validation-draft.pdf",
        "expected_sha256": "086654e747f13626d853d404557292bd0238f5536ee2173669f2674d37ad62ef",
    },
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def atomic_json(path: Path, value: dict[str, Any]) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")
    os.replace(temporary, path)


def download(source: dict[str, str], destination: Path) -> None:
    request = urllib.request.Request(source["url"], headers={"User-Agent": "NebulaMind-V4-source-freezer/1.0"})
    with tempfile.NamedTemporaryFile(dir=destination.parent, delete=False) as temporary:
        temporary_path = Path(temporary.name)
        with urllib.request.urlopen(request, timeout=90) as response:
            while True:
                chunk = response.read(1024 * 1024)
                if not chunk:
                    break
                temporary.write(chunk)
    try:
        observed = sha256(temporary_path)
        if observed != source["expected_sha256"]:
            raise RuntimeError(
                f"{source['key']}: live PDF drifted during freeze; "
                f"expected {source['expected_sha256']}, observed {observed}"
            )
        os.replace(temporary_path, destination)
    finally:
        temporary_path.unlink(missing_ok=True)


def caption_excerpt(text: str, start: int, limit: int = 900) -> str:
    tail = text[start:start + limit]
    paragraphs = re.split(r"\n\s*\n", tail, maxsplit=1)
    excerpt = re.sub(r"\s+", " ", paragraphs[0]).strip()
    return excerpt[:limit].strip()


def locate_caption_rect(page: pymupdf.Page, label: str) -> pymupdf.Rect | None:
    candidates = page.search_for(label)
    if candidates:
        return min(candidates, key=lambda rect: rect.y0)
    prefix = label.rsplit(".", 1)[0]
    candidates = page.search_for(prefix)
    return min(candidates, key=lambda rect: rect.y0) if candidates else None


def figure_crop(page: pymupdf.Page, caption_rect: pymupdf.Rect | None) -> tuple[pymupdf.Rect, dict[str, Any]] | None:
    caption_y = caption_rect.y0 if caption_rect else page.rect.height
    infos = page.get_image_info(xrefs=True)
    viable: list[tuple[float, dict[str, Any]]] = []
    for info in infos:
        bbox = pymupdf.Rect(info["bbox"])
        if bbox.width < 80 or bbox.height < 70:
            continue
        if bbox.y0 >= caption_y + 8:
            continue
        distance = max(0.0, caption_y - bbox.y1)
        area = bbox.width * bbox.height
        score = area / (1.0 + distance / 120.0)
        viable.append((score, info))
    if not viable:
        return None
    info = max(viable, key=lambda pair: pair[0])[1]
    bbox = pymupdf.Rect(info["bbox"])
    bbox.x0 = max(page.rect.x0, bbox.x0 - 8)
    bbox.y0 = max(page.rect.y0, bbox.y0 - 8)
    bbox.x1 = min(page.rect.x1, bbox.x1 + 8)
    bbox.y1 = min(page.rect.y1, bbox.y1 + 8)
    return bbox, info


def extract(source: dict[str, str]) -> dict[str, Any]:
    key = source["key"]
    pdf = SOURCE_DIR / f"{key}.pdf"
    download(source, pdf)
    document = pymupdf.open(pdf)
    page_texts: list[str] = []
    figures: list[dict[str, Any]] = []
    tables: list[dict[str, Any]] = []
    seen_figures: set[str] = set()
    seen_tables: set[str] = set()

    for page_index in range(document.page_count):
        page = document[page_index]
        text = cast(str, page.get_text("text", sort=True))
        page_texts.append(f"## PAGE {page_index + 1}\n\n{text.strip()}\n")
        for match in re.finditer(r"\b(?:Figure|Fig\.)\s*(\d+)\s*\.", text, re.IGNORECASE):
            number = match.group(1)
            if number in seen_figures:
                continue
            seen_figures.add(number)
            label = f"Figure {number}."
            caption_rect = locate_caption_rect(page, label)
            crop = figure_crop(page, caption_rect)
            item: dict[str, Any] = {
                "number": number,
                "page": page_index + 1,
                "caption": caption_excerpt(text, match.start()),
                "caption_sha256": hashlib.sha256(caption_excerpt(text, match.start()).encode("utf-8")).hexdigest(),
                "caption_bbox_points": (
                    [round(caption_rect.x0, 3), round(caption_rect.y0, 3), round(caption_rect.x1, 3), round(caption_rect.y1, 3)]
                    if caption_rect else None
                ),
            }
            if crop:
                bbox, info = crop
                pixmap = page.get_pixmap(matrix=pymupdf.Matrix(3, 3), clip=bbox, alpha=False)
                image_path = FIGURE_DIR / f"{key}-figure-{number}-page-{page_index + 1}.png"
                pixmap.save(image_path)
                item.update({
                    "crop_path": str(image_path),
                    "crop_sha256": sha256(image_path),
                    "crop_bbox_points": [round(value, 3) for value in bbox],
                    "rendered_pixel_size": [pixmap.width, pixmap.height],
                    "source_object_pixel_size": [info.get("width"), info.get("height")],
                    "source_xref": info.get("xref"),
                })
            else:
                item.update({
                    "crop_path": None,
                    "crop_bbox_points": None,
                    "rendered_pixel_size": None,
                    "source_object_pixel_size": None,
                    "source_xref": None,
                    "inventory_note": "No embedded raster object was reliably associated; inspect vector/full-page source manually.",
                })
            figures.append(item)

        for match in re.finditer(r"\bTable\s*(\d+)\s*\.", text, re.IGNORECASE):
            number = match.group(1)
            if number in seen_tables:
                continue
            seen_tables.add(number)
            tables.append({
                "number": number,
                "page": page_index + 1,
                "caption": caption_excerpt(text, match.start()),
            })

    text_path = SOURCE_DIR / f"{key}.md"
    text_path.write_text(
        f"# CURRENT V4 SOURCE EXTRACT — {key}\n\n"
        f"Source URL: {source['url']}\n\n"
        + "\n".join(page_texts),
        encoding="utf-8",
    )
    return {
        "key": key,
        "url": source["url"],
        "pdf_path": str(pdf),
        "pdf_sha256": sha256(pdf),
        "pdf_bytes": pdf.stat().st_size,
        "page_count": document.page_count,
        "text_path": str(text_path),
        "text_sha256": sha256(text_path),
        "figure_count": len(figures),
        "figures": figures,
        "table_count": len(tables),
        "tables": tables,
    }


def main() -> None:
    SOURCE_DIR.mkdir(parents=True, exist_ok=True)
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)
    rows = [extract(source) for source in SOURCES]
    value = {
        "marker": "NEBULAMIND_FIVE_PAPER_V4_CURRENT_SOURCE_FREEZE_COMPLETE",
        "generated_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "paper_count": len(rows),
        "all_expected_live_hashes_matched": all(
            row["pdf_sha256"] == source["expected_sha256"] for row, source in zip(rows, SOURCES)
        ),
        "rows": rows,
        "previous_v2_v3_source_mutations": False,
        "youtube_mutations": False,
        "website_mutations": False,
        "git_mutations": False,
        "runtime_mutations": False,
    }
    atomic_json(FREEZE, value)
    print(json.dumps({
        "status": "PASS",
        "marker": value["marker"],
        "freeze": str(FREEZE),
        "rows": [{"key": row["key"], "pages": row["page_count"], "figures": row["figure_count"], "tables": row["table_count"]} for row in rows],
    }, indent=2))


if __name__ == "__main__":
    main()
