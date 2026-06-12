"""Mirror official survey logos into frontend/public/survey-logos.

Reads remote logo_url values from the live surveys table and rewrites successful
downloads to same-origin /survey-logos/{slug}.{ext} paths.
"""
from __future__ import annotations

import mimetypes
import re
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from sqlalchemy import text

ROOT = Path(__file__).resolve().parents[2]
FRONTEND_LOGO_DIR = ROOT / "frontend" / "public" / "survey-logos"
BACKEND_DIR = ROOT / "backend"

if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from app.database import SessionLocal  # noqa: E402


CONTENT_TYPE_EXT = {
    "image/png": ".png",
    "image/jpeg": ".jpg",
    "image/jpg": ".jpg",
    "image/svg+xml": ".svg",
    "image/webp": ".webp",
    "image/gif": ".gif",
}


def _extension_for(content_type: str, url: str) -> str:
    media_type = content_type.split(";", 1)[0].strip().lower()
    if media_type in CONTENT_TYPE_EXT:
        return CONTENT_TYPE_EXT[media_type]

    suffix = Path(urlparse(url).path).suffix.lower()
    if suffix in {".png", ".jpg", ".jpeg", ".svg", ".webp", ".gif"}:
        return ".jpg" if suffix == ".jpeg" else suffix

    guessed = mimetypes.guess_extension(media_type)
    return ".jpg" if guessed == ".jpe" else (guessed or ".img")


def _sanitize_svg(data: bytes) -> bytes:
    text_data = data.decode("utf-8", errors="ignore")
    text_data = re.sub(r"<script\\b[^>]*>.*?</script>", "", text_data, flags=re.I | re.S)
    return text_data.encode("utf-8")


def fetch_logo(url: str) -> tuple[bytes, str, str]:
    req = Request(
        url,
        headers={
            "User-Agent": "NebulaMindLogoMirror/1.0 (+https://nebulamind.net)",
            "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/jpeg,image/*,*/*;q=0.8",
        },
    )
    with urlopen(req, timeout=10) as resp:
        content_type = resp.headers.get("Content-Type", "")
        media_type = content_type.split(";", 1)[0].strip().lower()
        if not media_type.startswith("image/"):
            raise ValueError(f"non-image content type: {content_type or 'unknown'}")
        data = resp.read()
        ext = _extension_for(content_type, url)
        if ext == ".svg":
            data = _sanitize_svg(data)
        return data, content_type, ext


def main() -> int:
    FRONTEND_LOGO_DIR.mkdir(parents=True, exist_ok=True)

    with SessionLocal() as db:
        rows = db.execute(
            text(
                """
                SELECT slug, logo_url
                FROM surveys
                WHERE logo_url LIKE 'http%'
                ORDER BY slug
                """
            )
        ).fetchall()

        print(f"Found {len(rows)} remote survey logos to mirror")
        successes = 0
        failures = 0

        for row in rows:
            slug = row.slug
            remote_url = row.logo_url
            try:
                data, content_type, ext = fetch_logo(remote_url)
                output_path = FRONTEND_LOGO_DIR / f"{slug}{ext}"
                output_path.write_bytes(data)
                local_url = f"/survey-logos/{slug}{ext}"
                db.execute(
                    text("UPDATE surveys SET logo_url = :local_url WHERE slug = :slug"),
                    {"local_url": local_url, "slug": slug},
                )
                db.commit()
                successes += 1
                print(f"OK   {slug:<12} {len(data):>8} bytes  {content_type:<32} {local_url}")
            except (HTTPError, URLError, TimeoutError, ValueError, OSError) as exc:
                db.execute(
                    text("UPDATE surveys SET logo_url = NULL WHERE slug = :slug"),
                    {"slug": slug},
                )
                db.commit()
                failures += 1
                print(f"FAIL {slug:<12} {remote_url}  ({exc})")

        print(f"Mirroring complete: {successes} succeeded, {failures} failed")
        return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
