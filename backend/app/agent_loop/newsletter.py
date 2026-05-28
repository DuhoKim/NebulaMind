"""Newsletter digest task — sends daily/weekly emails to subscribers (Mon–Fri only)."""
import json
import datetime as dt

import resend

from app.config import settings
from app.database import SessionLocal
from app.models.subscriber import Subscriber
from app.models.arxiv import ArxivPaper
from app.agent_loop.worker import celery_app


def _clean_author_name(raw: str) -> str:
    import re
    name = re.sub(r'\s*\(.*', '', raw)
    name = re.sub(r"\\['`^~=.]?\{?([a-zA-Z])\}?", r'\1', name)
    return name.strip()


TRACK_CONFIG = {
    "news":   {"icon": "📰", "label": "News",   "color": "#22c55e", "desc": "External astronomy & space news"},
    "data":   {"icon": "📦", "label": "Data",   "color": "#3b82f6", "desc": "Data releases, proposals & facility updates"},
    "papers": {"icon": "📄", "label": "Papers", "color": "#5B2D8E", "desc": "Peer-reviewed published papers"},
}

KIND_LABELS = {
    "release":        "📦 Data Release",
    "proposal_call":  "📋 Proposal Call",
    "milestone":      "🏆 Milestone",
    "facility_news":  "🔭 Facility News",
    "other":          "📋 Facility Update",
    "first_light":    "💡 First Light",
    "news":           "📰 News",
    "press_release":  "📢 Press Release",
    "refereed_paper": "📄 Published Paper",
}

CAT_LABELS = {
    "astro-ph.GA": "🌀 Galaxies",
    "astro-ph.CO": "🔵 Cosmology",
    "astro-ph.HE": "⚡ High Energy",
    "astro-ph.SR": "☀️ Solar & Stellar",
    "astro-ph.EP": "🪐 Planetary",
    "astro-ph.IM": "🔧 Instrumentation",
}


_TRACK_SQL = {
    "news": "fni.track = 'results'",
    "data": "fni.track IN ('data', 'facility')",
    "papers": "fni.track = 'highlights' AND fni.kind = 'refereed_paper' AND fni.paper_doi IS NOT NULL",
}


def _fetch_track_items(db, track: str, n: int = 5) -> list:
    from sqlalchemy import text
    where = _TRACK_SQL.get(track)
    if not where:
        return []
    rows = db.execute(text(f"""
        SELECT fni.title, fni.summary, fni.kind, fni.source_url, fni.occurs_at,
               fni.occurs_at_confidence, fni.data_portal_urls,
               fp.short_name AS facility_name
        FROM facility_news_items fni
        LEFT JOIN facility_profiles fp ON fp.id = fni.facility_id
        WHERE {where}
        ORDER BY fni.featured DESC, fni.created_at DESC
        LIMIT :n
    """), {"n": n}).fetchall()
    return [dict(r._mapping) for r in rows]


def _render_track_items_html(track: str, items: list) -> str:
    if not items:
        return ""
    cfg = TRACK_CONFIG[track]
    color = cfg["color"]
    cards = ""
    for item in items:
        kind_label = KIND_LABELS.get(item["kind"], item["kind"])
        if item.get("source_url"):
            title_html = f'<a href="{item["source_url"]}" style="color:#1A3A5C;font-weight:600;font-size:14px;text-decoration:none;">{item["title"]}</a>'
        else:
            title_html = f'<span style="color:#1A3A5C;font-weight:600;font-size:14px;">{item["title"]}</span>'
        cards += f"""
        <div style="padding:5px 0;border-bottom:1px solid #f0f0f0;">
          {title_html}
          <span style="color:#aaa;font-size:11px;margin-left:6px;">{kind_label}</span>
        </div>
        """
    return f"""
    <div style="margin:20px 0;">
      <h2 style="color:#1A3A5C;font-size:16px;margin:0 0 10px;padding:8px 12px;background:{color}18;border-radius:6px;border-left:4px solid {color};">
        {cfg['icon']} {cfg['label']}
        <span style="font-size:12px;color:#888;font-weight:400;margin-left:8px;">{cfg['desc']}</span>
      </h2>
      {cards}
    </div>
    """


def _render_paper_simple_html(paper) -> str:
    import re as _re
    authors = json.loads(paper.authors) if paper.authors else []
    if authors:
        raw = authors[0]
        name = _re.sub(r'\s*\(.*', '', raw)
        name = _re.sub(r"\\['`^~=.]?\{?([a-zA-Z])\}?", r'\1', name)
        first = name.strip()
        author_str = f"{first} et al." if len(authors) > 1 else first
    else:
        author_str = ""
    return f"""
    <div style="padding:5px 0;border-bottom:1px solid #f0f0f0;">
      <a href="{paper.url}" style="color:#1A3A5C;font-weight:600;font-size:14px;text-decoration:none;">{paper.title}</a>
      <span style="color:#888;font-size:11px;display:block;">{author_str} · {CAT_LABELS.get(paper.category, paper.category)}</span>
    </div>
    """


def _render_papers_track_html(published_papers: list, papers_by_cat: dict) -> str:
    """Render Papers track: peer-reviewed published papers + subscriber arXiv preprints by category."""
    cfg = TRACK_CONFIG["papers"]
    color = cfg["color"]

    published_html = ""
    for item in published_papers:
        kind_label = KIND_LABELS.get(item["kind"], item["kind"])
        if item.get("source_url"):
            title_html = f'<a href="{item["source_url"]}" style="color:#1A3A5C;font-weight:600;font-size:14px;text-decoration:none;">{item["title"]}</a>'
        else:
            title_html = f'<span style="color:#1A3A5C;font-weight:600;font-size:14px;">{item["title"]}</span>'
        published_html += f"""
        <div style="padding:5px 0;border-bottom:1px solid #f0f0f0;">
          {title_html}
          <span style="color:#aaa;font-size:11px;margin-left:6px;">{kind_label}</span>
        </div>
        """

    arxiv_html = ""
    for cat, papers in papers_by_cat.items():
        if not papers:
            continue
        label = CAT_LABELS.get(cat, cat)
        papers_html = "".join(_render_paper_simple_html(p) for p in papers[:5])
        arxiv_html += f"""
        <div style="margin-bottom:12px;">
          <h3 style="color:#1A3A5C;font-size:14px;margin:12px 0 6px;font-weight:600;">{label}</h3>
          {papers_html}
        </div>
        """

    if not published_html and not arxiv_html:
        return ""

    arxiv_section = ""
    if arxiv_html:
        arxiv_section = f"""
        <div>
          <h3 style="color:#1A3A5C;font-size:13px;margin:12px 0 6px;font-weight:600;color:#888;">📑 Recent arXiv preprints in your categories</h3>
          {arxiv_html}
        </div>
        """

    divider = '<hr style="border:none;border-top:1px solid #e8e4f7;margin:12px 0;">' if published_html and arxiv_html else ""

    return f"""
    <div style="margin:20px 0;">
      <h2 style="color:#1A3A5C;font-size:16px;margin:0 0 10px;padding:8px 12px;background:{color}18;border-radius:6px;border-left:4px solid {color};">
        {cfg['icon']} {cfg['label']}
        <span style="font-size:12px;color:#888;font-weight:400;margin-left:8px;">{cfg['desc']}</span>
      </h2>
      {published_html}
      {divider}
      {arxiv_section}
    </div>
    """


def _render_digest_html(papers_by_cat: dict, unsubscribe_url: str,
                        news_items: list = None,
                        data_items: list = None,
                        paper_highlights: list = None) -> str:
    """Render full newsletter HTML with 3-track layout: News | Data | Papers."""
    today = dt.date.today().isoformat()

    news_html = _render_track_items_html("news", news_items or [])
    data_html = _render_track_items_html("data", data_items or [])
    papers_html = _render_papers_track_html(paper_highlights or [], papers_by_cat)  # paper_highlights = published papers only

    return f"""
    <div style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;max-width:600px;margin:0 auto;padding:20px;background:#fff;">
      <div style="text-align:center;margin-bottom:20px;">
        <h1 style="color:#5B2D8E;margin:0;">🌌 NebulaMind Daily</h1>
        <p style="color:#888;font-size:13px;margin:4px 0;">Your daily dose of the cosmos — {today}</p>
        <div style="display:flex;justify-content:center;gap:20px;margin-top:10px;">
          <a href="https://nebulamind.net/news#news" style="color:#22c55e;font-size:12px;text-decoration:none;font-weight:500;">📰 News</a>
          <a href="https://nebulamind.net/news#data" style="color:#3b82f6;font-size:12px;text-decoration:none;font-weight:500;">📦 Data</a>
          <a href="https://nebulamind.net/newsletter" style="color:#5B2D8E;font-size:12px;text-decoration:none;font-weight:500;">📄 Papers</a>
        </div>
      </div>
      <hr style="border:1px solid #eee;">

      {news_html}
      {data_html}
      {papers_html}

      <hr style="border:1px solid #eee;margin-top:24px;">
      <div style="text-align:center;padding:16px 0;">
        <a href="https://nebulamind.net/calendar" style="background:#5B2D8E;color:#fff;padding:10px 24px;border-radius:6px;text-decoration:none;font-size:14px;display:inline-block;margin-bottom:10px;">
          📅 View Full Calendar
        </a>
        <br>
        <a href="https://nebulamind.net/research" style="color:#5B2D8E;font-size:13px;text-decoration:none;">
          🔭 Explore Research on NebulaMind
        </a>
      </div>
      <p style="color:#aaa;font-size:11px;text-align:center;margin-top:20px;">
        NebulaMind — The Universe, Explored by AI<br>
        <a href="{unsubscribe_url}" style="color:#aaa;">Unsubscribe</a> ·
        <a href="https://nebulamind.net" style="color:#5B2D8E;">nebulamind.net</a>
      </p>
    </div>
    """


@celery_app.task
def send_daily_digest():
    """Send daily newsletter to all active daily subscribers (Mon–Fri only)."""
    if not settings.RESEND_API_KEY:
        print("[newsletter] RESEND_API_KEY not set, skipping")
        return

    # Skip weekends (Mon=0 … Fri=4; Sat=5, Sun=6)
    if dt.date.today().weekday() >= 5:
        print(f"[newsletter] Weekend ({dt.date.today().strftime('%A')}) — skipping")
        return

    resend.api_key = settings.RESEND_API_KEY
    db = SessionLocal()
    try:
        subscribers = db.query(Subscriber).filter(
            Subscriber.is_active.is_(True),
            Subscriber.frequency == "daily",
        ).all()

        if not subscribers:
            print("[newsletter] No daily subscribers")
            return

        today = dt.date.today().isoformat()
        yesterday = (dt.date.today() - dt.timedelta(days=1)).isoformat()

        # Fetch all 3 tracks once for all subscribers
        news_items = _fetch_track_items(db, "news", n=5)
        data_items = _fetch_track_items(db, "data", n=8)
        paper_highlights = _fetch_track_items(db, "papers", n=5)

        for sub in subscribers:
            cats = json.loads(sub.categories) if sub.categories else ["astro-ph.GA"]
            papers_by_cat = {}
            for cat in cats:
                papers = (
                    db.query(ArxivPaper)
                    .filter(ArxivPaper.category == cat, ArxivPaper.submitted >= yesterday)
                    .order_by(ArxivPaper.created_at.desc())
                    .limit(5)
                    .all()
                )
                if papers:
                    papers_by_cat[cat] = papers

            if not papers_by_cat and not news_items and not data_items:
                continue

            total_papers = sum(len(p) for p in papers_by_cat.values())
            unsub_url = f"https://nebulamind.net/api/unsubscribe?token={sub.unsubscribe_token}"
            html = _render_digest_html(
                papers_by_cat, unsub_url,
                news_items=news_items,
                data_items=data_items,
                paper_highlights=paper_highlights,
            )

            try:
                resend.Emails.send({
                    "from": "NebulaMind <onboarding@resend.dev>",
                    "to": [sub.email],
                    "subject": f"🔭 NebulaMind Daily — {total_papers} new papers ({today})",
                    "html": html,
                })
                print(f"[newsletter] Sent to {sub.email} ({total_papers} papers)")
            except Exception as e:
                print(f"[newsletter] Failed for {sub.email}: {e}")
    finally:
        db.close()
