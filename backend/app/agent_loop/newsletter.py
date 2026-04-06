"""Newsletter digest task — sends daily/weekly emails to subscribers."""
import json
import datetime as dt

import resend

from app.config import settings
from app.database import SessionLocal
from app.models.subscriber import Subscriber
from app.models.arxiv import ArxivPaper
from app.agent_loop.worker import celery_app


def _render_paper_html(paper) -> str:
    authors = json.loads(paper.authors) if paper.authors else []
    author_str = authors[0] + " et al." if len(authors) > 1 else (authors[0] if authors else "")
    related = json.loads(paper.related_pages) if paper.related_pages else []
    related_html = " ".join(
        f'<a href="https://nebulamind.net/wiki/{slug}" style="color:#5B2D8E;font-size:12px;text-decoration:none;">📄 {slug.replace("-", " ").title()}</a>'
        for slug in related[:3]
    )
    # One-line summary, max 120 chars
    summary = (paper.abstract_summary or "")[:120]
    if paper.abstract_summary and len(paper.abstract_summary) > 120:
        summary += "..."
    return f"""
    <div style="background:#f9f7ff;padding:12px;border-radius:8px;margin:8px 0;border-left:3px solid #5B2D8E;">
      <a href="{paper.url}" target="_blank" style="color:#1A3A5C;font-weight:600;text-decoration:none;font-size:14px;">{paper.title}</a>
      <p style="color:#888;font-size:11px;margin:3px 0;">{author_str} · {paper.category}</p>
      <p style="font-size:13px;color:#333;margin:4px 0;font-weight:500;">{summary}</p>
      {f'<div style="margin-top:4px;">{related_html}</div>' if related_html else ''}
    </div>
    """


def _render_digest_html(papers_by_cat: dict, unsubscribe_url: str) -> str:
    sections = ""
    cat_labels = {
        "astro-ph.GA": "🌀 Galaxies",
        "astro-ph.CO": "🔵 Cosmology",
        "astro-ph.HE": "⚡ High Energy",
        "astro-ph.SR": "☀️ Solar & Stellar",
        "astro-ph.EP": "🪐 Planetary",
        "astro-ph.IM": "🔧 Instrumentation",
    }
    for cat, papers in papers_by_cat.items():
        if not papers:
            continue
        label = cat_labels.get(cat, cat)
        papers_html = "".join(_render_paper_html(p) for p in papers[:5])
        sections += f"""
        <h2 style="color:#1A3A5C;font-size:16px;margin:20px 0 8px;">{label}</h2>
        {papers_html}
        """

    today = dt.date.today().isoformat()
    return f"""
    <div style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;max-width:600px;margin:0 auto;padding:20px;background:#fff;">
      <div style="text-align:center;margin-bottom:20px;">
        <h1 style="color:#5B2D8E;margin:0;">🌌 NebulaMind Daily</h1>
        <p style="color:#888;font-size:13px;margin:4px 0;">Your daily dose of the cosmos — {today}</p>
      </div>
      <hr style="border:1px solid #eee;">
      {sections}
      <hr style="border:1px solid #eee;margin-top:24px;">
      <div style="text-align:center;padding:16px 0;">
        <a href="https://nebulamind.net/research" style="background:#5B2D8E;color:#fff;padding:10px 24px;border-radius:6px;text-decoration:none;font-size:14px;">
          🔭 Explore More on NebulaMind
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
    """Send daily newsletter to all active daily subscribers."""
    if not settings.RESEND_API_KEY:
        print("[newsletter] RESEND_API_KEY not set, skipping")
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

            if not papers_by_cat:
                continue

            total = sum(len(p) for p in papers_by_cat.values())
            unsub_url = f"https://nebulamind.net/api/unsubscribe?token={sub.unsubscribe_token}"
            html = _render_digest_html(papers_by_cat, unsub_url)

            try:
                resend.Emails.send({
                    "from": "NebulaMind <onboarding@resend.dev>",
                    "to": [sub.email],
                    "subject": f"🔭 NebulaMind Daily — {total} new papers ({today})",
                    "html": html,
                })
                print(f"[newsletter] Sent to {sub.email} ({total} papers)")
            except Exception as e:
                print(f"[newsletter] Failed for {sub.email}: {e}")
    finally:
        db.close()
