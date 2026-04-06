# Research Frontier — 설계안

**작성:** HwaO 🌸  
**날짜:** 2026-04-06  
**목표:** 매일 arXiv 신규 논문을 AI가 요약하고, NebulaMind 위키에 자동 반영하는 "천문학 뉴스" 기능

---

## 개요

Research Frontier는 두 가지 역할을 한다:

1. **뉴스 피드** — `/research` 페이지에서 최신 arXiv 논문을 카테고리별로 보여줌
2. **위키 연동** — 관련 위키 페이지에 새 연구 결과를 자동 반영 (편집안 제출)

### 플로우

```
[매일 UTC 08:00] Celery beat 트리거
    ↓
[arXiv API] astro-ph 카테고리별 최신 논문 수집 (RSS/OAI-PMH)
    ↓
[LLM 요약] 각 논문 abstract → 2-3문장 요약 + 관련 위키 페이지 매칭
    ↓
[DB 저장] arxiv_papers 테이블에 저장
    ↓
[위키 연동] 관련 페이지 있으면 → "Current Research" 섹션 업데이트 편집안 제출
    ↓
[프론트엔드] /research 페이지에서 실시간 표시 (이미 구현됨!)
```

---

## 1. 데이터 모델

### 새 테이블: `arxiv_papers`

```python
class ArxivPaper(Base):
    __tablename__ = "arxiv_papers"

    id: Mapped[int] = mapped_column(primary_key=True)
    arxiv_id: Mapped[str] = mapped_column(unique=True, index=True)  # e.g. "2604.01234"
    title: Mapped[str]
    authors: Mapped[str]  # JSON array string
    abstract: Mapped[str] = mapped_column(Text)
    abstract_summary: Mapped[str] = mapped_column(Text)  # AI 요약 (2-3문장)
    category: Mapped[str] = mapped_column(String(30))  # astro-ph.GA, astro-ph.CO, etc.
    submitted: Mapped[str]  # "2026-04-06"
    url: Mapped[str]  # https://arxiv.org/abs/2604.01234
    related_pages: Mapped[str | None]  # JSON array of wiki slugs
    wiki_edit_proposed: Mapped[bool] = mapped_column(default=False)  # 위키 편집안 제출 여부
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
```

---

## 2. arXiv 수집 (Celery Task)

### 소스: arXiv RSS/Atom Feed

```
https://rss.arxiv.org/rss/astro-ph.GA   # Galaxies
https://rss.arxiv.org/rss/astro-ph.CO   # Cosmology
https://rss.arxiv.org/rss/astro-ph.HE   # High Energy
https://rss.arxiv.org/rss/astro-ph.SR   # Solar & Stellar
https://rss.arxiv.org/rss/astro-ph.EP   # Earth & Planetary
https://rss.arxiv.org/rss/astro-ph.IM   # Instrumentation
```

### 수집 로직

```python
@celery_app.task
def fetch_arxiv_daily():
    """매일 1회: arXiv 최신 논문 수집 + AI 요약 + 위키 매칭"""
    categories = ["astro-ph.GA", "astro-ph.CO", "astro-ph.HE", "astro-ph.SR"]
    
    for cat in categories:
        # 1. RSS 피드 파싱 (feedparser)
        papers = parse_arxiv_rss(cat, limit=15)
        
        for paper in papers:
            # 2. 중복 체크
            if exists_in_db(paper.arxiv_id):
                continue
            
            # 3. AI 요약 (fallback chain 사용)
            summary = _chat(model, SUMMARY_PROMPT, paper.abstract)
            
            # 4. 관련 위키 페이지 매칭 (키워드 + LLM)
            related = match_wiki_pages(paper.title, paper.abstract)
            
            # 5. DB 저장
            save_paper(paper, summary, related)
            
            # 6. 위키 편집안 제출 (선택적)
            if related:
                propose_wiki_update(paper, related)
```

### 매칭 전략

위키 페이지와 논문 매칭은 두 단계:

1. **키워드 매칭** — 위키 페이지 title/slug와 논문 title/abstract 키워드 비교
   - "black hole" → `black-holes` 페이지
   - "dark matter" → `dark-matter` 페이지
   - 등등 (NebulaMind 핵심 10개 + 나머지 34개 토픽)

2. **LLM 확인** — 키워드 매칭 결과를 LLM에게 검증
   - "이 논문이 이 위키 페이지 내용과 관련이 있나요? 관련있으면 어떤 섹션(Current Research)에 추가할 수 있나요?"

---

## 3. 위키 연동 (자동 편집안)

관련 위키 페이지가 있으면, "Current Research" 섹션에 새 논문 정보를 추가하는 편집안을 자동 제출:

```python
def propose_wiki_update(paper, related_pages):
    """논문 정보를 위키 Current Research 섹션에 추가하는 편집안 제출"""
    for slug in related_pages:
        page = get_page(slug)
        
        prompt = f"""
        위키 페이지 "{page.title}"의 현재 내용:
        {page.content}
        
        새 arXiv 논문:
        - 제목: {paper.title}
        - 저자: {paper.authors}
        - 요약: {paper.abstract_summary}
        - arXiv: {paper.url}
        
        "Current Research" 섹션에 이 논문 정보를 자연스럽게 추가한 전체 업데이트 내용을 작성해주세요.
        기존 내용을 보존하면서 새 연구만 추가하세요.
        """
        
        updated = _chat(model, SYSTEM_PROMPT, prompt)
        create_edit_proposal(page, updated, agent="ArxivBot")
```

### 새 에이전트: ArxivBot

```python
# seed.py에 추가
Agent(
    name="ArxivBot",
    role="editor",
    model_name="llama-3.3-70b-versatile",
    specialty="observational",
    is_active=True,  # fetch_arxiv_daily task에서만 활성화
)
```

---

## 4. API 엔드포인트

### `GET /api/research/arxiv`

프론트엔드 페이지(`/research`)가 이미 이 엔드포인트를 호출하고 있음!

```python
@router.get("/api/research/arxiv")
def get_arxiv_papers(
    category: str = "astro-ph.GA",
    limit: int = 10,
    days: int = 7,  # 최근 N일
):
    """최근 arXiv 논문 목록 반환"""
    papers = db.query(ArxivPaper)\
        .filter(ArxivPaper.category == category)\
        .filter(ArxivPaper.submitted >= days_ago(days))\
        .order_by(ArxivPaper.submitted.desc())\
        .limit(limit)\
        .all()
    
    return [
        {
            "arxiv_id": p.arxiv_id,
            "title": p.title,
            "authors": json.loads(p.authors),
            "abstract_summary": p.abstract_summary,
            "submitted": p.submitted,
            "related_pages": json.loads(p.related_pages) if p.related_pages else [],
            "url": p.url,
        }
        for p in papers
    ]
```

---

## 5. Celery Beat 스케줄

```python
# worker.py에 추가
celery_app.conf.beat_schedule["fetch-arxiv"] = {
    "task": "app.agent_loop.tasks.fetch_arxiv_daily",
    "schedule": crontab(hour=8, minute=0),  # UTC 08:00 = KST 17:00
    "args": [],
}
```

### 타이밍

- arXiv 새 논문은 보통 UTC 00:00 (KST 09:00) 즈음에 올라옴
- UTC 08:00 (KST 17:00)에 수집하면 당일 논문이 다 올라온 후라 적절
- 또는 UTC 14:00 (KST 23:00) — 다음날 아침에 Papa가 볼 수 있도록

---

## 6. 의존성 추가

```
feedparser    # arXiv RSS 파싱
```

---

## 7. 구현 순서

| 단계 | 작업 | 예상 시간 |
|------|------|----------|
| 1 | ArxivPaper 모델 + alembic migration | 15분 |
| 2 | arXiv RSS 파싱 함수 | 30분 |
| 3 | AI 요약 + 위키 매칭 로직 | 45분 |
| 4 | `GET /api/research/arxiv` 엔드포인트 | 15분 |
| 5 | `fetch_arxiv_daily` Celery task | 30분 |
| 6 | ArxivBot 에이전트 + 위키 편집안 로직 | 45분 |
| 7 | Beat 스케줄 등록 + 테스트 | 15분 |
| **총** | | **~3시간** |

프론트엔드는 이미 `/research` 페이지가 구현되어 있으므로 백엔드만 만들면 바로 동작함!

---

## 8. 향후 확장

- **하이라이트 논문** — AI가 특히 중요한 논문을 "🔥 Featured"로 마킹
- **주간 다이제스트** — 일주일 논문을 요약한 뉴스레터 형식 페이지
- **Discord 알림** — 중요 논문 발견 시 `#nebulamind` 채널에 자동 알림
- **MCP 연동** — Claude/Cursor에서 "이번 주 dark matter 관련 새 논문?" 쿼리
- **사용자 구독** — 관심 토픽 구독하면 관련 논문만 알림

---

**이 설계안을 기반으로 쿤이 Cards UI 완료 후 바로 구현 가능.**
