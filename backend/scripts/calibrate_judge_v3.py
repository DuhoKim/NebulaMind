"""
P1 judge calibration — 3 force=True calls against page 57 with judge_v3-14b
(temp=0.1, N=3, anonymized prompt, harder rubric). Pass if stddev ≤ 0.7.
"""
import statistics
import time
import sys

from app.database import SessionLocal
from app.models.claim import Claim
from app.models.page import WikiPage
from app.agent_loop.autowiki.judge import judge_page, PROMPT_VERSION, _N

PAGE_ID = 57


def _claims_text(claims):
    return "\n".join(f"[{c.claim_type}] {c.text}" for c in claims[:40])


def main() -> int:
    print(f"=== judge calibration === PROMPT_VERSION={PROMPT_VERSION} _N={_N}")
    with SessionLocal() as db:
        page = db.query(WikiPage).filter(WikiPage.id == PAGE_ID).first()
        if not page:
            print(f"FAIL: page {PAGE_ID} not found")
            return 1
        claims = db.query(Claim).filter(Claim.page_id == PAGE_ID).order_by(Claim.created_at).all()
        claims_text = _claims_text(claims)
        print(f"page id={PAGE_ID} slug={page.slug} content_chars={len(page.content or '')} "
              f"claims={len(claims)}")

        utilities = []
        rubric_runs = []
        wall_times = []
        for i in range(1, 4):
            t0 = time.monotonic()
            result = judge_page(
                page_id=PAGE_ID,
                content=page.content,
                hero_facts=page.hero_facts,
                claims_text=claims_text,
                force=True,
            )
            wall = time.monotonic() - t0
            utilities.append(result.utility)
            wall_times.append(wall)
            rubric_runs.append(result.raw_scores)
            print(f"call {i}: wall={wall:.1f}s utility={result.utility:.4f} "
                  f"model={result.model_used} n_raw={len(result.raw_scores)}")
            for j, raw in enumerate(result.raw_scores, 1):
                print(f"  sample {j}: " + " ".join(
                    f"{k}={raw.get(k, '?')}" for k in (
                        "findings_clarity", "open_questions_q",
                        "evidence_depth", "frontier_signal", "noise_penalty"
                    )
                ))
            print(f"  rationale: {result.rationale[:200]}")

    mean = statistics.mean(utilities)
    pop_std = statistics.pstdev(utilities) if len(utilities) >= 2 else 0.0
    samp_std = statistics.stdev(utilities) if len(utilities) >= 2 else 0.0
    print()
    print(f"utilities: {utilities}")
    print(f"mean={mean:.4f} pop_stddev={pop_std:.4f} sample_stddev={samp_std:.4f}")
    print(f"wall mean={statistics.mean(wall_times):.1f}s "
          f"total={sum(wall_times):.1f}s")

    gate = max(pop_std, samp_std)
    print()
    if gate <= 0.7:
        print(f"GATE PASS (max stddev {gate:.4f} ≤ 0.7)")
        return 0
    else:
        print(f"GATE FAIL (max stddev {gate:.4f} > 0.7)")
        return 2


if __name__ == "__main__":
    sys.exit(main())
