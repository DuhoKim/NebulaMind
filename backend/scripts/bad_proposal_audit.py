"""
Audit the agent-loop bad-content problem across ALL pages.

Goal: find the root cause of generic LLM garbage ("Galaxy evolution is a complex
and dynamic field...") flooding the wiki via auto-approved proposals.
"""
from collections import Counter, defaultdict
from datetime import datetime, timedelta
import re

import sys
sys.path.insert(0, '/Users/duhokim/NebulaMind/NebulaMind/backend')

from sqlalchemy import text
from app.database import SessionLocal

db = SessionLocal()

# Generic-content fingerprints. If a proposal/page contains these, it is
# almost certainly LLM filler.
GENERIC_PATTERNS = [
    r"\bis a complex and dynamic\b",
    r"\bcomplex and dynamic field\b",
    r"\bplays a crucial role\b",
    r"\bis a fascinating area\b",
    r"\bin the field of astronomy\b",
    r"\bvarious aspects\b",
    r"\bnumerous studies\b",
    r"\bmany factors\b",
    r"\bIn conclusion,\b",
    r"\bIn summary,\b",
    r"\bIt is important to note\b",
    r"\bResearchers have found\b",
    r"\bOverall,\b",
    r"\bunderstanding\s+\w+\s+is\s+(crucial|essential|important)",
]
GENERIC_RX = re.compile("|".join(GENERIC_PATTERNS), re.IGNORECASE)


def count_generic_hits(s: str) -> int:
    if not s:
        return 0
    return len(GENERIC_RX.findall(s))


print("\n========================================================")
print("  PART 1 — Recent EditProposal volume & status breakdown")
print("========================================================\n")

# Volume over last 30 days, grouped by status
rows = db.execute(text("""
    SELECT status, COUNT(*)
    FROM edit_proposals
    WHERE created_at > NOW() - INTERVAL '30 days'
    GROUP BY status
    ORDER BY COUNT(*) DESC
""")).fetchall()
print(f"{'status':12s} {'count':>8s}")
for st, n in rows:
    print(f"{st:12s} {n:>8d}")


print("\n========================================================")
print("  PART 2 — Per-agent proposal stats (last 30d)")
print("========================================================\n")

rows = db.execute(text("""
    SELECT
      a.id, a.name, a.model_name, a.role,
      COUNT(ep.id)                                   AS proposals,
      COUNT(*) FILTER (WHERE ep.status='APPROVED')   AS approved,
      COUNT(*) FILTER (WHERE ep.status='REJECTED')   AS rejected,
      COUNT(*) FILTER (WHERE ep.status='PENDING')    AS pending,
      AVG(LENGTH(ep.content))::int                   AS avg_len,
      MIN(LENGTH(ep.content))                        AS min_len,
      MAX(LENGTH(ep.content))                        AS max_len
    FROM edit_proposals ep
    JOIN agents a ON a.id = ep.agent_id
    WHERE ep.created_at > NOW() - INTERVAL '30 days'
    GROUP BY a.id, a.name, a.model_name, a.role
    ORDER BY COUNT(ep.id) DESC
""")).fetchall()
print(f"{'agent':25s} {'model':30s} {'prop':>5s} {'app':>5s} {'rej':>5s} {'pen':>5s} {'avgL':>6s} {'minL':>6s} {'maxL':>6s}")
for r in rows:
    aid, name, model, role, prop, app, rej, pen, avgl, minl, maxl = r
    print(f"{name[:25]:25s} {(model or '?')[:30]:30s} {prop:>5d} {app:>5d} {rej:>5d} {pen:>5d} {avgl or 0:>6d} {minl or 0:>6d} {maxl or 0:>6d}")


print("\n========================================================")
print("  PART 3 — Proposals with generic LLM fingerprints")
print("========================================================\n")

# Pull all recent proposals and run regex
rows = db.execute(text("""
    SELECT ep.id, ep.page_id, ep.agent_id, ep.status, ep.content, ep.created_at,
           a.name, a.model_name, wp.slug, wp.title
    FROM edit_proposals ep
    JOIN agents a ON a.id = ep.agent_id
    JOIN wiki_pages wp ON wp.id = ep.page_id
    WHERE ep.created_at > NOW() - INTERVAL '30 days'
    ORDER BY ep.created_at DESC
""")).fetchall()

by_agent_generic = Counter()
by_agent_total = Counter()
generic_proposals = []  # (id, agent, model, slug, len, hits, status)
for r in rows:
    epid, pid, aid, status, content, ts, name, model, slug, title = r
    hits = count_generic_hits(content or "")
    by_agent_total[(name, model or "?")] += 1
    if hits >= 1:
        by_agent_generic[(name, model or "?")] += 1
        generic_proposals.append((epid, name, model or "?", slug, len(content or ""), hits, status, ts))

print(f"Total proposals scanned: {len(rows)}")
print(f"Proposals matching ≥1 generic-LLM pattern: {len(generic_proposals)} "
      f"({100*len(generic_proposals)/max(1,len(rows)):.1f}%)\n")

print("Per-agent generic share:")
print(f"{'agent':25s} {'model':30s} {'gen':>5s} {'tot':>5s} {'pct':>6s}")
for (name, model), tot in sorted(by_agent_total.items(), key=lambda x: -x[1]):
    gen = by_agent_generic[(name, model)]
    print(f"{name[:25]:25s} {model[:30]:30s} {gen:>5d} {tot:>5d} {100*gen/tot:>5.1f}%")

print(f"\nTop 25 worst generic proposals (most filler hits):")
generic_proposals.sort(key=lambda x: (-x[5], x[4]))
print(f"{'epID':>6s} {'agent':20s} {'model':25s} {'slug':30s} {'len':>5s} {'hits':>4s} {'status':10s}")
for ep in generic_proposals[:25]:
    epid, name, model, slug, ln, hits, status, ts = ep
    print(f"{epid:>6d} {name[:20]:20s} {model[:25]:25s} {slug[:30]:30s} {ln:>5d} {hits:>4d} {status:10s}")


print("\n========================================================")
print("  PART 4 — Short approved proposals (likely shortenings)")
print("========================================================\n")

rows = db.execute(text("""
    SELECT ep.id, ep.page_id, ep.agent_id, LENGTH(ep.content) AS L,
           a.name, a.model_name, wp.slug, wp.title, ep.created_at
    FROM edit_proposals ep
    JOIN agents a ON a.id = ep.agent_id
    JOIN wiki_pages wp ON wp.id = ep.page_id
    WHERE ep.status = 'APPROVED'
      AND ep.created_at > NOW() - INTERVAL '30 days'
      AND LENGTH(ep.content) < 3000
    ORDER BY LENGTH(ep.content) ASC
    LIMIT 30
""")).fetchall()
print(f"{'epID':>6s} {'len':>6s} {'agent':25s} {'model':25s} {'slug':30s}")
for r in rows:
    epid, pid, aid, L, name, model, slug, title, ts = r
    print(f"{epid:>6d} {L:>6d} {(name or '?')[:25]:25s} {(model or '?')[:25]:25s} {slug[:30]:30s}")


print("\n========================================================")
print("  PART 5 — Voting concentration (last 30d)")
print("========================================================\n")

# Who votes the most, and what % of their votes are +1 vs -1
rows = db.execute(text("""
    SELECT a.name, a.model_name, COUNT(*) AS n,
           SUM(CASE WHEN v.value > 0 THEN 1 ELSE 0 END)     AS plus,
           SUM(CASE WHEN v.value < 0 THEN 1 ELSE 0 END)     AS minus,
           SUM(CASE WHEN v.value = 0 THEN 1 ELSE 0 END)     AS zero
    FROM votes v
    JOIN agents a ON a.id = v.agent_id
    WHERE v.created_at > NOW() - INTERVAL '30 days'
    GROUP BY a.name, a.model_name
    ORDER BY COUNT(*) DESC
""")).fetchall()
print(f"{'voter':25s} {'model':30s} {'votes':>7s} {'+':>5s} {'-':>5s} {'0':>5s} {'+%':>6s}")
for r in rows:
    name, model, n, plus, minus, zero = r
    pct = 100 * (plus or 0) / max(1, n)
    print(f"{(name or '?')[:25]:25s} {(model or '?')[:30]:30s} {n:>7d} {plus or 0:>5d} {minus or 0:>5d} {zero or 0:>5d} {pct:>5.1f}%")


print("\n========================================================")
print("  PART 6 — Reciprocal voting (echo chamber)")
print("========================================================\n")

# Pairs (voter -> author): how many +1 votes did voter cast on author's proposals?
rows = db.execute(text("""
    SELECT va.name AS voter,
           aa.name AS author,
           SUM(CASE WHEN v.value > 0 THEN 1 ELSE 0 END) AS plus_votes,
           COUNT(*) AS total_votes
    FROM votes v
    JOIN edit_proposals ep ON ep.id = v.edit_id
    JOIN agents va  ON va.id = v.agent_id
    JOIN agents aa  ON aa.id = ep.agent_id
    WHERE v.created_at > NOW() - INTERVAL '30 days'
      AND va.id != aa.id
    GROUP BY va.name, aa.name
    HAVING SUM(CASE WHEN v.value > 0 THEN 1 ELSE 0 END) >= 3
    ORDER BY plus_votes DESC
    LIMIT 40
""")).fetchall()
print(f"{'voter':25s} {'author':25s} {'+votes':>7s} {'total':>6s}")
for r in rows:
    voter, author, plus, total = r
    print(f"{(voter or '?')[:25]:25s} {(author or '?')[:25]:25s} {plus:>7d} {total:>6d}")


print("\n========================================================")
print("  PART 7 — Pages shortened: wiki_pages.content vs prev PageVersion")
print("========================================================\n")

# For each page, compare current length to longest historical version length.
rows = db.execute(text("""
    WITH page_max AS (
        SELECT pv.page_id, MAX(LENGTH(pv.content)) AS max_hist
        FROM page_versions pv
        GROUP BY pv.page_id
    )
    SELECT wp.id, wp.slug, wp.title, LENGTH(wp.content) AS cur_len,
           pm.max_hist,
           wp.updated_at
    FROM wiki_pages wp
    LEFT JOIN page_max pm ON pm.page_id = wp.id
    WHERE pm.max_hist IS NOT NULL
      AND LENGTH(wp.content) < pm.max_hist * 0.7    -- shrank by >30%
    ORDER BY (pm.max_hist - LENGTH(wp.content)) DESC
    LIMIT 30
""")).fetchall()
print(f"{'pid':>4s} {'slug':35s} {'cur':>6s} {'hist':>6s} {'lost':>6s} {'pct':>5s}")
for r in rows:
    pid, slug, title, cur, hist, ts = r
    lost = hist - cur
    pct = 100 * cur / hist
    print(f"{pid:>4d} {slug[:35]:35s} {cur:>6d} {hist:>6d} {lost:>6d} {pct:>4.0f}%")


print("\n========================================================")
print("  PART 8 — Pages where current content has GENERIC fingerprints")
print("========================================================\n")

rows = db.execute(text("""
    SELECT id, slug, title, content, LENGTH(content) AS L, do_not_renovate, updated_at
    FROM wiki_pages
    WHERE content IS NOT NULL
    ORDER BY updated_at DESC NULLS LAST
""")).fetchall()
poisoned = []
for r in rows:
    pid, slug, title, content, L, dnr, ts = r
    h = count_generic_hits(content)
    if h >= 2:
        poisoned.append((pid, slug, L, h, dnr, ts))
print(f"Pages with >=2 generic fingerprints in current content: {len(poisoned)}")
print(f"{'pid':>4s} {'slug':35s} {'len':>6s} {'hits':>4s} {'DNR':>4s} {'updated_at'}")
for p in poisoned[:40]:
    pid, slug, L, h, dnr, ts = p
    print(f"{pid:>4d} {slug[:35]:35s} {L:>6d} {h:>4d} {str(dnr):>4s} {ts}")


print("\n========================================================")
print("  PART 9 — Vote-to-approval timing (echo chamber speed)")
print("========================================================\n")

# How fast do approved proposals collect their votes?
rows = db.execute(text("""
    SELECT ep.id, wp.slug, a.name AS author, a.model_name AS author_model,
           ep.created_at,
           (SELECT MIN(v.created_at) FROM votes v WHERE v.edit_id = ep.id) AS first_vote,
           (SELECT MAX(v.created_at) FROM votes v WHERE v.edit_id = ep.id) AS last_vote,
           (SELECT COUNT(*) FROM votes v WHERE v.edit_id = ep.id AND v.value > 0) AS plus_votes
    FROM edit_proposals ep
    JOIN agents a ON a.id = ep.agent_id
    JOIN wiki_pages wp ON wp.id = ep.page_id
    WHERE ep.status='APPROVED'
      AND ep.created_at > NOW() - INTERVAL '30 days'
    ORDER BY ep.created_at DESC
    LIMIT 30
""")).fetchall()
print(f"{'epID':>6s} {'slug':25s} {'author':20s} {'author_model':25s} {'+':>3s} {'sec_to_approve':>14s}")
for r in rows:
    epid, slug, author, amod, ts, fv, lv, pv = r
    delta = "?"
    if lv and ts:
        d = (lv - ts).total_seconds()
        delta = f"{d:.0f}s"
    print(f"{epid:>6d} {slug[:25]:25s} {(author or '?')[:20]:20s} {(amod or '?')[:25]:25s} {pv or 0:>3d} {delta:>14s}")

db.close()
