#!/usr/bin/env python3
"""Supplement Gate-B OUP citations via read-only ADS bibliographic queries."""
from __future__ import annotations

import hashlib
import json
import os
import re
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote, urlparse

import fitz
import requests

PACKET = Path(__file__).resolve().parents[1]
MAP = json.loads((PACKET / "sources/SOURCE_INDEX_MAP.json").read_text())
LOG = PACKET / "sources/FETCH_LOG.jsonl"
RAW = PACKET / "sources/raw"
TEXT = PACKET / "sources/text"
META = PACKET / "sources/metadata"
TOKEN = os.getenv("ADS_API_KEY") or os.getenv("ADS_API_TOKEN") or os.getenv("ADS_DEV_KEY")
UA = "NebulaMindSourceVerifier/1.0 (read-only research verification; contact: local operator)"
OUP_RE = re.compile(r"academic\.oup\.com/mnras/article(?:-abstract)?/(\d+)/[^/]+/([^/?]+)/", re.I)
ARXIV_ID_RE = re.compile(r"(?:arXiv:|arXiv\.)?(\d{4}\.\d{4,5})", re.I)
last_host: dict[str, float] = {}
host_failures: dict[str, int] = defaultdict(int)
fetches = 0


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def append_log(rec: dict) -> None:
    with LOG.open("a") as fh:
        fh.write(json.dumps(rec, ensure_ascii=False, separators=(",", ":")) + "\n")


def fetch(url: str, index: int, label: str, purpose: str, ads: bool = False) -> dict:
    global fetches
    host = urlparse(url).netloc.lower()
    elapsed = time.monotonic() - last_host.get(host, 0)
    if elapsed < 2:
        time.sleep(2 - elapsed)
    headers = {"User-Agent": UA, "Accept": "application/json,text/html,application/pdf;q=0.9,*/*;q=0.5"}
    if ads:
        if not TOKEN:
            raise RuntimeError("ADS token not configured")
        headers["Authorization"] = "Bearer " + TOKEN
    started = now(); fetches += 1
    try:
        resp = requests.get(url, headers=headers, timeout=60, allow_redirects=True)
        last_host[host] = time.monotonic()
        data = resp.content; ctype = resp.headers.get("content-type", "").split(";", 1)[0].lower()
        ext = ".pdf" if "pdf" in ctype or resp.url.lower().split("?", 1)[0].endswith(".pdf") else ".json" if "json" in ctype else ".html"
        h = digest(data); raw = RAW / f"idx{index:02d}_{label}_{h[:12]}{ext}"; raw.write_bytes(data)
        rec = {"utc": started, "method": "GET", "host": host, "index": index, "label": label, "purpose": purpose,
               "requested_url": url, "final_url": resp.url, "status": int(resp.status_code), "bytes": len(data), "sha256": h,
               "content_type": ctype, "raw_path": raw.relative_to(PACKET).as_posix(), "auth": "ADS_CONFIGURED_BOOLEAN_ONLY" if ads else "NONE",
               "cache_reuse": False}
        append_log(rec); return rec
    except Exception as exc:
        last_host[host] = time.monotonic(); host_failures[host] += 1
        rec = {"utc": started, "method": "GET", "host": host, "index": index, "label": label, "purpose": purpose,
               "requested_url": url, "final_url": "", "status": 0, "bytes": 0, "sha256": digest(b""), "content_type": "", "raw_path": "",
               "auth": "ADS_CONFIGURED_BOOLEAN_ONLY" if ads else "NONE", "cache_reuse": False,
               "error": f"{type(exc).__name__}: {str(exc)[:240]}"}
        append_log(rec); return rec


def save_pdf_text(rec: dict, index: int) -> dict:
    if rec.get("status") != 200 or not rec.get("raw_path"):
        return {"text_path": "", "text_chars": 0, "pages": 0}
    data = (PACKET / rec["raw_path"]).read_bytes()
    try:
        doc = fitz.open(stream=data, filetype="pdf")
        text = "\n\n".join(str(p.get_text("text")) for p in doc)
        h = digest(text.encode()); out = TEXT / f"idx{index:02d}_ads_arxiv_pdf_{h[:12]}.txt"; out.write_text(text)
        return {"text_path": out.relative_to(PACKET).as_posix(), "text_chars": len(text), "text_sha256": h, "pages": doc.page_count}
    except Exception as exc:
        return {"text_path": "", "text_chars": 0, "pages": 0, "extract_error": f"{type(exc).__name__}: {str(exc)[:200]}"}


def arxiv_from_doc(doc: dict) -> str:
    for value in doc.get("identifier", []) + doc.get("doi", []):
        m = ARXIV_ID_RE.search(str(value))
        if m:
            return m.group(1)
    return ""


def main() -> None:
    if not TOKEN:
        raise SystemExit("ADS token missing")
    outputs = []
    query_cache: dict[str, tuple[dict, dict]] = {}
    arxiv_cache: dict[str, tuple[dict, dict]] = {}
    for item in MAP["indices"]:
        idx = int(item["index"]); url = item["url"]
        m = OUP_RE.search(url)
        if not m:
            continue
        volume, page_or_slug = m.groups()
        if page_or_slug.isdigit():
            query = f"bibstem:MNRAS volume:{volume} page:{page_or_slug}"
        else:
            query = f"doi:10.1093/mnras/{page_or_slug}"
        if query in query_cache:
            ads_rec, payload = query_cache[query]
            ads_rec = dict(ads_rec); ads_rec["cache_reuse"] = True
        else:
            fields = "bibcode,title,abstract,doi,identifier,author,year,pub,volume,page,property"
            endpoint = "https://api.adsabs.harvard.edu/v1/search/query?q=" + quote(query) + "&fl=" + quote(fields) + "&rows=5"
            ads_rec = fetch(endpoint, idx, "ads_oup_resolve", "read_only_bibliographic_resolution", ads=True)
            payload = json.loads((PACKET / ads_rec["raw_path"]).read_text()) if ads_rec.get("raw_path") and ads_rec.get("status") == 200 else {}
            query_cache[query] = (ads_rec, payload)
        docs = payload.get("response", {}).get("docs", [])
        doc = docs[0] if docs else {}
        arxiv_id = arxiv_from_doc(doc)
        pdf_rec = {}; text_meta = {}
        if arxiv_id:
            if arxiv_id in arxiv_cache:
                pdf_rec, text_meta = arxiv_cache[arxiv_id]
                pdf_rec = dict(pdf_rec); pdf_rec["cache_reuse"] = True
            else:
                pdf_rec = fetch(f"https://arxiv.org/pdf/{arxiv_id}", idx, "ads_arxiv_pdf", "primary_full_text")
                text_meta = save_pdf_text(pdf_rec, idx)
                arxiv_cache[arxiv_id] = (pdf_rec, text_meta)
        out = {"schema": "NM_GATE_B_ADS_OUP_RESOLUTION_V1", "index": idx, "captured_url": url, "ads_query": query,
               "ads_record": ads_rec, "num_found": payload.get("response", {}).get("numFound", 0), "selected_doc": doc,
               "arxiv_id": arxiv_id, "pdf_record": pdf_rec, "pdf_text": text_meta}
        path = META / f"index_{idx:02d}_ads_resolved.json"; path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
        outputs.append(out)
    summary = {"schema": "NM_GATE_B_ADS_OUP_RESOLUTION_SUMMARY_V1", "completed_utc": now(), "ads_token_present_boolean": bool(TOKEN),
               "oup_indices": len(outputs), "fetches_made": fetches, "resolved_docs": sum(bool(x["selected_doc"]) for x in outputs),
               "arxiv_full_text_routes": sum(bool(x["pdf_text"].get("text_chars")) for x in outputs), "host_failures": dict(host_failures),
               "indices": [{"index": x["index"], "num_found": x["num_found"], "title": (x["selected_doc"].get("title") or [""])[0],
                            "doi": x["selected_doc"].get("doi", []), "arxiv_id": x["arxiv_id"], "text_chars": x["pdf_text"].get("text_chars", 0)} for x in outputs]}
    (PACKET / "sources/ADS_OUP_RESOLUTION_SUMMARY.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "DONE", "oup_indices": len(outputs), "fetches": fetches, "resolved_docs": summary["resolved_docs"],
                      "arxiv_full_text_routes": summary["arxiv_full_text_routes"]}, indent=2))


if __name__ == "__main__":
    main()
