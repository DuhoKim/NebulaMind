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

## 8. 이메일 뉴스레터 (Daily/Weekly Digest)

구독자에게 관심 분야 논문 요약을 메일로 보내는 기능.

### 데이터 모델

```python
class Subscriber(Base):
    __tablename__ = "subscribers"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    name: Mapped[str | None] = mapped_column(nullable=True)
    categories: Mapped[str]  # JSON array: ["astro-ph.GA", "astro-ph.CO"]
    frequency: Mapped[str] = mapped_column(default="daily")  # daily | weekly
    is_active: Mapped[bool] = mapped_column(default=True)
    unsubscribe_token: Mapped[str] = mapped_column(unique=True)  # 원클릭 해지용
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
```

### API

```python
POST /api/subscribe       # { email, name?, categories, frequency }
GET  /api/unsubscribe?token=xxx  # 원클릭 해지
```

### 프론트엔드 구독 위젯

`/research` 페이지 하단 + 홈페이지에 간단한 구독 폼:

```
📬 Get the cosmos in your inbox
[이메일 입력] [카테고리 선택] [Daily/Weekly] [Subscribe]
"Free · No spam · Unsubscribe anytime"
```

### 메일 발송

```python
@celery_app.task
def send_digest_emails():
    """구독자별 관심 카테고리 논문 요약 메일 발송"""
    subscribers = get_active_subscribers(frequency="daily")
    
    for sub in subscribers:
        papers = get_recent_papers(categories=sub.categories, days=1)
        if not papers:
            continue
        
        html = render_digest_email(sub, papers)
        send_email(
            to=sub.email,
            subject=f"🔭 NebulaMind Daily — {len(papers)} new papers ({today})",
            html=html,
        )
```

### 메일 서비스 옵션 (무료~저비용)

| 서비스 | 무료 한도 | 비고 |
|--------|----------|------|
| **Resend** | 3,000/월 | 개발자 친화적, API 깔끔 |
| **Brevo (Sendinblue)** | 300/일 | 충분히 넉넉 |
| **AWS SES** | 62,000/월 (EC2에서) | 가장 저렴 |
| **Mailgun** | 1,000/월 | 간단한 셋업 |

초기에는 Resend (3,000/월 무료)이면 충분.

### Celery Beat 추가

```python
celery_app.conf.beat_schedule["send-daily-digest"] = {
    "task": "app.agent_loop.tasks.send_digest_emails",
    "schedule": crontab(hour=9, minute=0),  # UTC 09:00 = KST 18:00
}

celery_app.conf.beat_schedule["send-weekly-digest"] = {
    "task": "app.agent_loop.tasks.send_weekly_digest",
    "schedule": crontab(hour=9, minute=0, day_of_week="mon"),  # 매주 월요일
}
```

---

## 9. Researcher Spotlight (논문 홍보 채널)

연구자가 자기 논문을 NebulaMind에 제출하면 AI가 요약 + 위키 연결 + 뉴스레터 노출해주는 기능.
**레벨 제한으로 참여 유도 + 스팸 방지.**

### 레벨별 언락 혜택

**초기 홍보 기간:** 가입만 하면 누구나 Spotlight 가능 (진입 장벽 최소화)
**수요 증가 후:** 레벨 제한 활성화

| 단계 | 조건 | Spotlight 정책 |
|------|------|------|
| 🚀 **론칭기** (현재) | 가입만 하면 | 누구나 1편/월 무료 |
| 📈 **성장기** (구독자 500+) | Lv.2+ | Lunar Observer부터 1편/월 |
| 🏛️ **안정기** (구독자 2000+) | Lv.4+ | 아래 정규 테이블 적용 |

**정규 레벨 테이블 (안정기):**

| 레벨 | 이름 | pc | Spotlight 혜택 |
|------|------|-----|------|
| 1-3 | Stargazer ~ Solar Analyst | 0-50 | ❌ 열람만 |
| 4 | 🪐 Planetary Scientist | 150 | 📡 1편/월 |
| 5 | 🔭 Deep Space Explorer | 300 | 📡 3편/월 |
| 6 | 🌌 Galactic Cartographer | 500 | 📡 무제한 + 뉴스레터 Featured |
| 7 | 🔬 Principal Investigator | 1000 | Author Page + 프로필 배지 |
| 8 | 🏆 Astro Legend | 2500 | 모든 혜택 + 큐레이터 권한 |

단계 전환은 config.py의 `SPOTLIGHT_LEVEL_REQUIRED` 값 하나로 제어 (기본값: 0 = 누구나).

### 제출 플로우

```
연구자가 arXiv ID 입력 (로그인 필요, Lv.4+)
    ↓
AI가 논문 읽고 요약 생성
    ↓
관련 위키 페이지 자동 매칭
    ↓
Research Frontier에 "🔬 Community Submitted" 태그로 노출
    ↓
위키 "Current Research" 섹션에 편집안 자동 제출
    ↓
뉴스레터에 "Community Picks" 코너로 포함 (Lv.6+는 Featured)
```

### 데이터 모델

```python
class Spotlight(Base):
    __tablename__ = "spotlights"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    arxiv_id: Mapped[str] = mapped_column(index=True)
    title: Mapped[str]
    authors: Mapped[str]  # JSON array
    summary: Mapped[str] = mapped_column(Text)  # AI 생성 요약
    related_pages: Mapped[str | None]  # JSON array of wiki slugs
    status: Mapped[str] = mapped_column(default="active")  # active | expired | rejected
    featured: Mapped[bool] = mapped_column(default=False)  # Lv.6+ 뉴스레터 Featured
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
    expires_at: Mapped[dt.datetime]  # 30일 후 자동 만료
```

### API

```python
POST /api/spotlight          # { arxiv_id } — Lv.4+ 필요
GET  /api/spotlight           # 최근 Spotlight 목록
GET  /api/spotlight/featured  # 뉴스레터용 Featured 목록
```

### 프론트엔드

`/research` 페이지에 "🔬 Community Spotlight" 섹션 추가:

```
🔬 Community Spotlight
"Researchers share their own work with the NebulaMind community"

[논문 카드 — Community Submitted 태그]
  📄 "New constraints on supermassive black hole formation from JWST"
  by J. Smith et al. · submitted by @researcher123 (🪐 Planetary Scientist)
  🔗 Related: Black Holes, Galaxy Formation

[Submit Your Paper] → Lv.4+ 필요, 미달시 "Reach 🪐 Planetary Scientist to unlock!"
```

### 연구자 입장에서의 가치

- ✅ 내 논문이 AI 천문학 위키에 인용됨
- ✅ 구독자들에게 뉴스레터로 도달
- ✅ NebulaMind 지식 그래프에 영구 기록
- ✅ MCP로 Claude/Cursor에서도 검색 가능
- ✅ 참여할수록 더 많은 홍보 기회 (레벨업 동기)

---

## 10. 향후 확장

- **하이라이트 논문** — AI가 특히 중요한 논문을 "🔥 Featured"로 마킹
- **Discord 알림** — 중요 논문 발견 시 `#nebulamind` 채널에 자동 알림
- **MCP 연동** — Claude/Cursor에서 "이번 주 dark matter 관련 새 논문?" 쿼리
- **사용자 카테고리 커스텀** — astro-ph 외에 gr-qc, hep-ph 등도 지원

---

**이 설계안을 기반으로 쿤이 Cards UI 완료 후 바로 구현 가능.**
