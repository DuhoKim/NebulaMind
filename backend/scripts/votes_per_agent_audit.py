"""Confirm the multi-vote-per-agent issue + sample approved-but-poor proposals."""
import sys
sys.path.insert(0, '/Users/duhokim/NebulaMind/NebulaMind/backend')

from sqlalchemy import text
from app.database import SessionLocal
db = SessionLocal()

print("\n=== Votes-per-(proposal,agent) distribution ===")
rows = db.execute(text("""
    SELECT votes_per_agent, COUNT(*) AS n
    FROM (
        SELECT edit_id, agent_id, COUNT(*) AS votes_per_agent
        FROM votes
        WHERE created_at > NOW() - INTERVAL '30 days'
        GROUP BY edit_id, agent_id
    ) t
    GROUP BY votes_per_agent
    ORDER BY votes_per_agent
""")).fetchall()
for r in rows:
    print(f"  {r[0]} vote(s) by same agent on same proposal:  {r[1]:>6d} rows")

print("\n=== Recently APPROVED with <=2 distinct reviewer agents ===")
rows = db.execute(text("""
    SELECT ep.id, wp.slug, a.name AS author, a.model_name,
           LENGTH(ep.content) AS L,
           COUNT(DISTINCT v.agent_id) AS distinct_agents,
           SUM(CASE WHEN v.value > 0 THEN 1 ELSE 0 END) AS plus_rows
    FROM edit_proposals ep
    JOIN agents a ON a.id = ep.agent_id
    JOIN wiki_pages wp ON wp.id = ep.page_id
    LEFT JOIN votes v ON v.edit_id = ep.id
    WHERE ep.status='APPROVED' AND ep.created_at > NOW() - INTERVAL '14 days'
    GROUP BY ep.id, wp.slug, a.name, a.model_name, ep.content
    HAVING COUNT(DISTINCT v.agent_id) <= 2
    ORDER BY ep.created_at DESC
    LIMIT 30
""")).fetchall()
print(f"{'epID':>6s} {'slug':30s} {'author':22s} {'model':28s} {'len':>5s} {'agts':>4s} {'+r':>3s}")
for r in rows:
    epid, slug, author, model, L, da, pr = r
    print(f"{epid:>6d} {slug[:30]:30s} {(author or '?')[:22]:22s} {(model or '?')[:28]:28s} {L:>5d} {da:>4d} {pr:>3d}")

print("\n=== APPROVED in <300s with single reviewer ===")
rows = db.execute(text("""
    SELECT ep.id, wp.slug, a.name AS author, a.model_name,
           LENGTH(ep.content) AS L,
           EXTRACT(EPOCH FROM (
              (SELECT MAX(v.created_at) FROM votes v WHERE v.edit_id = ep.id)
              - ep.created_at
           )) AS sec_to_approve,
           (SELECT COUNT(DISTINCT v.agent_id) FROM votes v WHERE v.edit_id = ep.id) AS reviewers
    FROM edit_proposals ep
    JOIN agents a ON a.id = ep.agent_id
    JOIN wiki_pages wp ON wp.id = ep.page_id
    WHERE ep.status='APPROVED' AND ep.created_at > NOW() - INTERVAL '14 days'
    ORDER BY sec_to_approve ASC NULLS LAST
    LIMIT 25
""")).fetchall()
print(f"{'epID':>6s} {'slug':28s} {'author':22s} {'model':28s} {'len':>5s} {'sec':>6s} {'rvw':>4s}")
for r in rows:
    epid, slug, author, model, L, sec, rvw = r
    print(f"{epid:>6d} {slug[:28]:28s} {(author or '?')[:22]:22s} {(model or '?')[:28]:28s} {L:>5d} {sec or 0:>6.0f} {rvw or 0:>4d}")

print("\n=== Same-model votes attributed to the same agent (in one cycle) ===")
rows = db.execute(text("""
    SELECT v.edit_id, v.agent_id, a.name, ARRAY_AGG(v.model_name ORDER BY v.created_at) AS models,
           COUNT(*) AS n
    FROM votes v
    JOIN agents a ON a.id = v.agent_id
    WHERE v.created_at > NOW() - INTERVAL '7 days'
    GROUP BY v.edit_id, v.agent_id, a.name
    HAVING COUNT(*) >= 2
    ORDER BY v.edit_id DESC
    LIMIT 25
""")).fetchall()
print(f"{'epID':>6s} {'agent':22s} {'votes':>5s}  models")
for r in rows:
    epid, aid, name, models, n = r
    print(f"{epid:>6d} {(name or '?')[:22]:22s} {n:>5d}  {models}")

print("\n=== Sample APPROVED proposal content (first 800 chars) — generic risk ===")
rows = db.execute(text("""
    SELECT ep.id, wp.slug, a.name, a.model_name, LEFT(ep.content, 800) AS c
    FROM edit_proposals ep
    JOIN agents a ON a.id = ep.agent_id
    JOIN wiki_pages wp ON wp.id = ep.page_id
    WHERE ep.id IN (15010, 5342, 5243, 4397, 4104, 3927, 3785, 5341, 14681, 14692)
""")).fetchall()
for r in rows:
    print(f"\n--- ep#{r[0]}  slug={r[1]}  author={r[2]} ({r[3]}) ---")
    print(r[4])
    print(f"\n[len={len(r[4])} chars truncated to 800]")

db.close()
