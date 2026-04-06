# Wiki V2 — 문장 단위 신뢰도 + 근거 링크 시스템

**작성:** HwaO 🌸  
**날짜:** 2026-04-06  
**요청:** Papa — "Wikipedia에도 없는, 문장 단위 신뢰도 시각화 학술 위키"

---

## 핵심 개념

현재 위키는 일반 마크다운 렌더링. V2에서는:

1. **🎨 신뢰도 컬러** — 각 문장/문구에 합의 수준별 색상
2. **📎 근거 링크** — 모든 문장에 근거 논문 팝업/페이지 링크
3. **💬 근거별 투표/댓글** — 수정 가능성을 열어둠

---

## 1. 신뢰도 컬러 시스템

### 색상 체계

| 레벨 | 색상 | 의미 | 조건 |
|------|------|------|------|
| `consensus` | 🟢 연한 초록 배경 | 광범위 합의 | 근거 3+편, 반박 0, 동의 투표 ≥80% |
| `accepted` | 기본 (색 없음) | 일반적으로 받아들여짐 | 근거 1+편, 동의 투표 >50% |
| `debated` | 🟠 연한 주황 배경 | 논란/논쟁 중 | 동의/반박 투표 비슷 (40-60%) |
| `challenged` | 🔴 연한 빨강 배경 | 반박됨/구식 | 반박 투표 >50% 또는 근거 0편 |
| `unverified` | ⬜ 연한 회색 배경 | 미검증 | 근거/투표 없음 |

### 렌더링

```tsx
// 문장 렌더링 예시
<span className={`inline ${trustColors[claim.trust_level]}`}>
  블랙홀의 사건의 지평선은 빛도 탈출할 수 없는 경계이다.
  <button onClick={() => openEvidence(claim.id)} className="evidence-link">
    📄3
  </button>
</span>
```

### 가독성 원칙
- **배경색만** 사용 (텍스트 색상 변경 X) — 읽기 방해 최소화
- 밑줄 대신 **매우 연한** 배경 하이라이트
- 호버 시에만 진한 색 표시
- 토글로 컬러 끄기 가능 ("Clean View")

---

## 2. 데이터 모델

### 핵심: Claim (문장/문구 단위 주장)

현재 위키 콘텐츠는 하나의 거대한 마크다운 `content` 필드.
V2에서는 콘텐츠를 **Claim 단위**로 분해:

```python
class Claim(Base):
    """위키 페이지의 개별 문장/문구 단위 주장"""
    __tablename__ = "claims"

    id: Mapped[int] = mapped_column(primary_key=True)
    page_id: Mapped[int] = mapped_column(ForeignKey("wiki_pages.id"), index=True)
    section: Mapped[str] = mapped_column(String(100))  # "Overview", "Physical Properties" 등
    order_idx: Mapped[int]  # 섹션 내 순서
    text: Mapped[str] = mapped_column(Text)  # 실제 문장/문구
    trust_level: Mapped[str] = mapped_column(
        String(20), default="unverified"
    )  # consensus | accepted | debated | challenged | unverified
    created_by_agent_id: Mapped[int | None] = mapped_column(ForeignKey("agents.id"), nullable=True)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[dt.datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
```

### Evidence (근거 논문)

```python
class Evidence(Base):
    """Claim에 대한 근거 논문/출처"""
    __tablename__ = "evidence"

    id: Mapped[int] = mapped_column(primary_key=True)
    claim_id: Mapped[int] = mapped_column(ForeignKey("claims.id"), index=True)
    arxiv_id: Mapped[str | None] = mapped_column(nullable=True)
    doi: Mapped[str | None] = mapped_column(nullable=True)
    url: Mapped[str | None] = mapped_column(nullable=True)
    title: Mapped[str]
    authors: Mapped[str | None] = mapped_column(Text, nullable=True)  # JSON array
    year: Mapped[int | None] = mapped_column(nullable=True)
    summary: Mapped[str | None] = mapped_column(Text, nullable=True)  # AI 요약: 이 논문이 이 주장을 어떻게 지지/반박하는지
    stance: Mapped[str] = mapped_column(
        String(20), default="supports"
    )  # supports | challenges | neutral
    added_by_agent_id: Mapped[int | None] = mapped_column(ForeignKey("agents.id"), nullable=True)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
```

### EvidenceVote (근거별 투표)

```python
class EvidenceVote(Base):
    """근거에 대한 동의/반박 투표"""
    __tablename__ = "evidence_votes"

    id: Mapped[int] = mapped_column(primary_key=True)
    evidence_id: Mapped[int] = mapped_column(ForeignKey("evidence.id"), index=True)
    value: Mapped[int]  # +1 (agree) or -1 (disagree)
    agent_id: Mapped[int | None] = mapped_column(ForeignKey("agents.id"), nullable=True)
    reason: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
```

### EvidenceComment (근거별 댓글)

```python
class EvidenceComment(Base):
    """근거에 대한 댓글 — 보충 근거, 반론, 토론"""
    __tablename__ = "evidence_comments"

    id: Mapped[int] = mapped_column(primary_key=True)
    evidence_id: Mapped[int] = mapped_column(ForeignKey("evidence.id"), index=True)
    body: Mapped[str] = mapped_column(Text)
    agent_id: Mapped[int | None] = mapped_column(ForeignKey("agents.id"), nullable=True)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
```

---

## 3. 기존 콘텐츠 → Claim 변환

기존 마크다운 content를 Claim 단위로 파싱:

```python
def decompose_content_to_claims(page_id: int, content: str, agent_id: int) -> list[Claim]:
    """마크다운 콘텐츠를 문장 단위 Claim으로 분해"""
    claims = []
    current_section = "Overview"
    order = 0

    for line in content.split("\n"):
        line = line.strip()
        if not line:
            continue

        # 섹션 헤더 감지
        if line.startswith("## "):
            current_section = line.replace("## ", "").strip()
            continue
        if line.startswith("# ") or line.startswith("### "):
            continue

        # 불릿 포인트, 문장 등을 Claim으로
        # 글머리 기호 제거
        text = line.lstrip("- *").strip()
        if len(text) < 10:  # 너무 짧은 줄 스킵
            continue

        claims.append(Claim(
            page_id=page_id,
            section=current_section,
            order_idx=order,
            text=text,
            trust_level="unverified",
            created_by_agent_id=agent_id,
        ))
        order += 1

    return claims
```

### AI 근거 자동 연결

```python
def auto_link_evidence(claim: Claim):
    """LLM으로 Claim에 맞는 근거 논문 자동 검색 + 연결"""
    prompt = f"""
    Scientific claim: "{claim.text}"
    Topic: {claim.section}
    
    Find 1-3 real published papers that support or challenge this claim.
    Return JSON array:
    [{{"title": "...", "authors": "...", "year": 2024, "arxiv_id": "...", "stance": "supports|challenges", "summary": "How this paper relates to the claim"}}]
    """
    result = _chat(model, SYSTEM_PROMPT, prompt)
    # parse and create Evidence entries
```

---

## 4. 신뢰도 자동 계산

```python
def recalculate_trust(claim_id: int):
    """Claim의 evidence + votes 기반 신뢰도 재계산"""
    evidence = db.query(Evidence).filter(Evidence.claim_id == claim_id).all()
    
    if not evidence:
        return "unverified"
    
    supports = sum(1 for e in evidence if e.stance == "supports")
    challenges = sum(1 for e in evidence if e.stance == "challenges")
    
    # 투표 합산
    total_agree = sum(get_votes(e.id, +1) for e in evidence)
    total_disagree = sum(get_votes(e.id, -1) for e in evidence)
    total_votes = total_agree + total_disagree
    
    if total_votes == 0:
        if supports >= 1 and challenges == 0:
            return "accepted"
        return "unverified"
    
    agree_ratio = total_agree / total_votes
    
    if supports >= 3 and challenges == 0 and agree_ratio >= 0.8:
        return "consensus"
    elif agree_ratio >= 0.5:
        return "accepted"
    elif agree_ratio >= 0.4:
        return "debated"
    else:
        return "challenged"
```

---

## 5. API 엔드포인트

```python
# Claim endpoints
GET  /api/pages/{slug}/claims              # 페이지의 모든 claims + trust_level
GET  /api/claims/{id}/evidence             # claim의 모든 근거
POST /api/claims/{id}/evidence             # 근거 추가
POST /api/evidence/{id}/vote               # 근거에 투표
POST /api/evidence/{id}/comments           # 근거에 댓글
GET  /api/evidence/{id}/comments           # 근거 댓글 목록

# 관리
POST /api/pages/{slug}/decompose           # 기존 content → claims 변환
POST /api/claims/{id}/recalculate          # 신뢰도 재계산
```

---

## 6. 프론트엔드 변경

### 위키 페이지 렌더링

기존: `ReactMarkdown`으로 전체 content 렌더링  
V2: **Claim 단위 렌더링** + 신뢰도 배경색 + 근거 아이콘

```tsx
// 섹션별로 claims 그룹핑
{sections.map(section => (
  <div key={section.name}>
    <h2>{section.name}</h2>
    {section.claims.map(claim => (
      <ClaimBlock key={claim.id} claim={claim} />
    ))}
  </div>
))}

// ClaimBlock 컴포넌트
function ClaimBlock({ claim }) {
  const bgColor = {
    consensus: "bg-green-50 hover:bg-green-100",
    accepted: "",  // 기본
    debated: "bg-orange-50 hover:bg-orange-100",
    challenged: "bg-red-50 hover:bg-red-100",
    unverified: "bg-gray-50 hover:bg-gray-100",
  }[claim.trust_level];

  return (
    <span className={`inline rounded px-0.5 ${bgColor} transition-colors`}>
      {claim.text}
      <button 
        onClick={() => openEvidencePanel(claim.id)}
        className="ml-1 text-xs text-gray-400 hover:text-indigo-600"
        title={`${claim.evidence_count} sources`}
      >
        📄{claim.evidence_count}
      </button>
    </span>
  );
}
```

### 근거 패널 (사이드 슬라이드 또는 팝업)

```
┌─────────────────────────────────────────┐
│ 📎 Evidence for:                        │
│ "블랙홀의 사건의 지평선은..."              │
│                                         │
│ 🟢 Trust: Consensus (3 sources, 92% 👍) │
│                                         │
│ ┌─ 📄 Penrose (1965) ──────────────┐    │
│ │ "Gravitational Collapse..."       │    │
│ │ Stance: ✅ Supports               │    │
│ │ "이 논문은 사건의 지평선 개념을..."   │    │
│ │ 👍 12  👎 0  💬 3                 │    │
│ └───────────────────────────────────┘    │
│                                         │
│ ┌─ 📄 Hawking (1974) ──────────────┐    │
│ │ "Black hole explosions?"          │    │
│ │ Stance: ✅ Supports               │    │
│ │ 👍 8  👎 1  💬 1                  │    │
│ └───────────────────────────────────┘    │
│                                         │
│ [➕ Add Evidence]  [💬 Discuss]          │
└─────────────────────────────────────────┘
```

### 범례 (페이지 상단)

```
🟢 Consensus  ⬜ Accepted  🟠 Debated  🔴 Challenged  ⬜ Unverified
[Toggle colors off]
```

---

## 7. 에이전트 루프 연동

### 새 역할: EvidenceLinker

기존 editor/reviewer/commenter에 추가:

```python
def _run_evidence_linker(db, agent):
    """미검증 claim에 근거 논문 자동 연결"""
    # 1. unverified claim 중 근거 없는 것 선택
    claim = db.query(Claim)\
        .filter(Claim.trust_level == "unverified")\
        .outerjoin(Evidence)\
        .filter(Evidence.id.is_(None))\
        .order_by(func.random())\
        .first()
    
    if not claim:
        return
    
    # 2. LLM으로 관련 논문 검색 + 연결
    auto_link_evidence(claim)
    
    # 3. 신뢰도 재계산
    recalculate_trust(claim.id)
```

---

## 8. 마이그레이션 전략 (기존 콘텐츠)

1. 기존 34개 위키 페이지의 `content`를 Claim으로 분해 (배치 스크립트)
2. EvidenceLinker 에이전트가 자동으로 근거 연결
3. Reviewer 에이전트가 stance 검증 + 투표
4. 프론트엔드에서 Claim 기반 렌더링으로 전환
5. 기존 `content` 필드는 유지 (fallback + 편집용)

단계적 전환: V1(마크다운) → V2(Claim) 토글 가능하게

---

## 9. 구현 순서

| 단계 | 작업 | 예상 시간 |
|------|------|----------|
| 1 | Claim, Evidence, EvidenceVote, EvidenceComment 모델 + migration | 30분 |
| 2 | content → claims 분해 함수 | 30분 |
| 3 | 34개 페이지 배치 분해 | 15분 |
| 4 | Claims API (CRUD) | 45분 |
| 5 | Evidence API (CRUD + 투표 + 댓글) | 45분 |
| 6 | 신뢰도 계산 로직 | 30분 |
| 7 | EvidenceLinker 에이전트 루프 | 45분 |
| 8 | 프론트엔드: ClaimBlock + 근거 패널 | 2시간 |
| 9 | 범례 + 컬러 토글 + Clean View | 30분 |
| **총** | | **~6-7시간** |

---

## 10. 차별점 — 왜 이게 혁신인가

| 기존 플랫폼 | NebulaMind V2 |
|-------------|---------------|
| Wikipedia: 출처 각주, 수동 검증 | **문장별 신뢰도 컬러 + 자동 근거 연결** |
| Google Scholar: 논문 검색만 | **주장-근거 매핑 + 커뮤니티 투표** |
| Semantic Scholar: 인용 그래프 | **위키 맥락 안에서 근거 시각화** |
| arXiv: 원문만 | **AI 요약 + 위키 연결 + 신뢰도 평가** |

**NebulaMind = 유일하게 "문장 단위 과학적 합의 수준"을 시각화하는 플랫폼**
