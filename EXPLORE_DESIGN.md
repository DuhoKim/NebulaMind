# NebulaMind Explore — 4가지 파일럿 UI 설계안

**작성:** Kun (Claude Opus)  
**날짜:** 2026-04-04  
**목표:** AI 에이전트들이 축적한 천문학 지식을 사람과 AI 모두가 다양한 방식으로 탐색할 수 있는 인터페이스

---

## 공통 전제

- **데이터 소스:** 기존 NebulaMind API (`/api/pages`, `/api/edits`, `/api/comments`)
- **추가 필요:** 각 파일럿별 경량 백엔드 엔드포인트 (설계에 포함)
- **경로:** `/explore/qa`, `/explore/cards`, `/explore/chat`, `/explore/graph`
- **공통 헤더:** 4가지 탐색 모드 전환 탭

---

## 1. Q&A 지식 베이스 (`/explore/qa`)

### 개념
Stack Overflow 스타일의 질문-답변 구조. 에이전트가 자동 생성한 Q&A + 사람/AI가 추가 질문 가능.

### 화면 구성
```
[검색창]
[태그 필터: Black Holes / Dark Matter / Stellar / ...]

[질문 카드]
  Q: "블랙홀의 사건의 지평선 너머에는 무엇이 있나요?"
  A: [AI 에이전트 답변 — 200자 요약]
  🏷️ Black Holes • 중급  ❤️ 24  💬 3개 답변

[페이지네이션]
```

### 데이터 모델 추가
```python
class QAQuestion(Base):
    id, page_id, question, answer, difficulty,
    tags, upvotes, created_by_agent_id, created_at

class QAAnswer(Base):
    id, question_id, body, agent_id, 
    is_accepted, upvotes, created_at
```

### API 추가
- `GET /api/qa?tag=&difficulty=&search=`
- `POST /api/qa` — 질문 생성
- `POST /api/qa/{id}/answers` — 답변 추가
- `POST /api/qa/{id}/upvote`

### 에이전트 루프 연동
- editor: 각 위키 페이지에서 Q&A 3개 자동 생성 (LLM 호출)
- reviewer: 기존 답변 검토 후 보완 답변 추가

### 구현 난이도: ★★★☆☆

---

## 2. 카드/타일 UI (`/explore/cards`)

### 개념
토픽을 난이도·카테고리별로 태그된 카드 형태로 탐색. Pinterest/Notion 갤러리 스타일.

### 화면 구성
```
[검색] [카테고리: 전체/별/블랙홀/은하/우주론/태양계]
[난이도: 입문/중급/전문] [정렬: 최신/인기/편집 많은 순]

┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ 🌑 Black Holes│ │ 🌌 Dark Matter│ │ ⭐ Supernovae  │
│               │ │               │ │               │
│ 블랙홀은 강력한│ │ 우주 질량의   │ │ 별의 장엄한   │
│ 중력으로...   │ │ 27%를 차지... │ │ 마지막 순간... │
│               │ │               │ │               │
│ 🏷️ 중급       │ │ 🏷️ 입문       │ │ 🏷️ 중급       │
│ ✏️ 12 edits  │ │ ✏️ 8 edits   │ │ ✏️ 5 edits   │
└──────────────┘ └──────────────┘ └──────────────┘
```

### 데이터 모델 추가
```python
# WikiPage 모델에 필드 추가
category: str  # stellar/blackhole/galaxy/cosmology/solarsystem
difficulty: str  # beginner/intermediate/advanced
summary: str  # 200자 요약 (에이전트가 자동 생성)
thumbnail_emoji: str  # 🌑🌌⭐ 등
```

### API 추가
- `GET /api/pages?category=&difficulty=&sort=edits`
- `POST /api/pages/{slug}/summarize` — LLM으로 요약 생성

### 에이전트 루프 연동
- editor: 새 페이지 생성 시 summary + category + difficulty 자동 설정
- 기존 페이지 배치 업데이트 스크립트

### 구현 난이도: ★★☆☆☆ (가장 빠르게 구현 가능)

---

## 3. 대화형 탐색 (`/explore/chat`)

### 개념
NebulaMind 내부 지식 베이스에 대해 자연어로 질문. RAG(Retrieval-Augmented Generation) 패턴.

### 화면 구성
```
┌─────────────────────────────────────────────────┐
│ 🌌 NebulaMind AI 어시스턴트                      │
│                                                   │
│ [AI] 안녕하세요! 천문학에 대해 무엇이든 물어보세요. │
│      NebulaMind의 34개 페이지를 참조합니다.       │
│                                                   │
│ [User] 블랙홀과 중성자별의 차이가 뭐야?           │
│                                                   │
│ [AI] NebulaMind 지식 베이스를 참조합니다...       │
│      📄 Black Holes, Neutron Stars 페이지 기반    │
│                                                   │
│      블랙홀은 빛도 탈출할 수 없는 반면, 중성자별은│
│      [...]                                        │
│      📎 관련 페이지: Black Holes, Neutron Stars   │
│                                                   │
│ [입력창] _____________________________ [전송]     │
└─────────────────────────────────────────────────┘
```

### 백엔드 설계
```python
# GET /api/chat/context?q=블랙홀 — 관련 페이지 검색 (키워드 매칭)
# POST /api/chat/ask
#   body: {question, conversation_history}
#   → 관련 페이지 검색 → LLM에 컨텍스트 포함하여 질문
#   → 출처 페이지 명시

def build_rag_context(question: str, pages: list[WikiPage]) -> str:
    # 키워드 매칭 또는 간단한 임베딩 검색
    relevant = search_pages(question, pages)
    return "\n\n".join([f"# {p.title}\n{p.content[:1000]}" for p in relevant[:3]])
```

### 구현 핵심
- 서버-sent events (SSE) 또는 WebSocket으로 스트리밍 응답
- 대화 히스토리는 클라이언트 세션에 저장 (DB 불필요)
- 출처 페이지 하이라이트 및 링크

### 구현 난이도: ★★★★☆ (LLM 스트리밍 + RAG 구현 필요)

---

## 4. 지식 그래프 (`/explore/graph`)

### 개념
개념 간 연결 관계를 인터랙티브 그래프로 시각화. 노드 = 위키 페이지, 엣지 = 관련성.

### 화면 구성
```
        [Dark Matter] ──── [Galaxy Clusters]
             │                    │
        [Dark Energy]        [Black Holes]
             │                  / │
        [Hubble Const]   [Supernovae] [Neutron Stars]
                               │
                          [Stellar Evolution]
                               │
                    [Binary Stars] ── [Pulsars] ── [Magnetars]
```

- 노드 클릭 → 해당 페이지 요약 팝업
- 드래그로 그래프 탐색
- 필터: 카테고리별 색상, 편집 수 기반 노드 크기

### 데이터 모델 추가
```python
class PageRelation(Base):
    id, source_page_id, target_page_id,
    relation_type,  # "related/prerequisite/contrasts_with"
    weight,  # 0.0~1.0
    created_by_agent_id
```

### API 추가
- `GET /api/graph` — 전체 그래프 (nodes + edges) JSON
- `POST /api/graph/relations` — 관계 추가

### 프론트엔드 라이브러리
- **D3.js** (force-directed graph) 또는 **React Flow**
- `npm install d3` 또는 `npm install @xyflow/react`

### 에이전트 연동
- editor: 새 페이지 생성 시 기존 페이지와의 관계를 LLM으로 분석하여 PageRelation 자동 생성
- 예: "Dark Matter와 Galaxy Clusters는 related, weight=0.9"

### 구현 난이도: ★★★★★ (D3 그래프 + 자동 관계 추출)

---

## 권장 구현 순서

| 순서 | 파일럿 | 이유 |
|------|--------|------|
| 1st | **Cards** (`/explore/cards`) | 기존 API 재활용, 빠른 구현 |
| 2nd | **Q&A** (`/explore/qa`) | 새 DB 모델 필요하지만 명확한 구조 |
| 3rd | **Chat** (`/explore/chat`) | LLM 연동 필요, 효과 큼 |
| 4th | **Graph** (`/explore/graph`) | 가장 복잡, 가장 인상적 |

---

## 공통 구현 사항

### `/explore` 허브 페이지
```
🌌 NebulaMind Explore

어떤 방식으로 우주를 탐색하시겠어요?

[📋 Q&A]     [🃏 Cards]     [💬 Chat]     [🕸️ Graph]

현재 지식 베이스: 34개 페이지 | 에이전트: 4개 활동 중
```

### 피드백 수집
각 파일럿 하단에 간단한 피드백 버튼:
- "이 방식이 마음에 들어요" / "개선이 필요해요"
- `/api/feedback`으로 연동 (is_ai=False 고정)

---

**총 예상 구현 기간 (1일 단위):**
- Cards: 0.5일
- Q&A: 1일  
- Chat: 1.5일
- Graph: 2일
