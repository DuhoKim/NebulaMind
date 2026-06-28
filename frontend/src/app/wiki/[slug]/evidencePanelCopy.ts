export type EvidenceSide = "support" | "counter" | "neutral";

export interface EvidencePanelItemLike {
  id?: number | string | null;
  title?: string | null;
  url?: string | null;
  stance?: string | null;
  votes_agree?: number | null;
  votes_disagree?: number | null;
  comments_count?: number | null;
  link_count?: number | null;
  quality_v2?: number | null;
}

export type EvidenceVoteSignalVerdict = "net_support" | "net_weakening" | "split" | "unresolved" | "unvoted";
export type EvidenceVoteCockpitSegmentKind = "support" | "weakening" | "unresolved";

export interface EvidenceVoteCockpitSegment {
  kind: EvidenceVoteCockpitSegmentKind;
  label: string;
  count: number;
  percent: number;
  color: string;
  background: string;
}

export interface EvidenceVoteCockpitVisuals {
  eyebrow: "At-a-glance vote balance";
  summary: string;
  dominantLabel: string;
  segments: EvidenceVoteCockpitSegment[];
}

export interface EvidenceVoteSignal {
  supportVotes: number;
  weakeningVotes: number;
  unresolvedVotes: number;
  totalVotes: number;
  netSupport: number;
  verdict: EvidenceVoteSignalVerdict;
  verdictLabel: string;
  headline: string;
  detail: string;
}

export interface EvidencePanelCopy {
  total: number;
  supportCount: number;
  counterCount: number;
  neutralCount: number;
  hasDirectionalStance: boolean;
  sourceLabel: string;
  directionalSplitLabel: string;
  neutralOnlySummary: string | null;
}

export interface EvidenceCardDensityMeta {
  sideLabel: string;
  voteLabel: string;
  activityLabel: string;
  qualityLabel: string | null;
  hasActivity: boolean;
}

export type ClaimSourceContradictionLaneKind = "support" | "counter" | "unresolved";

export interface ClaimSourceContradictionLane {
  kind: ClaimSourceContradictionLaneKind;
  label: string;
  count: number;
  percent: number;
  color: string;
  background: string;
}

export interface ClaimSourceContradictionSource {
  sourceId: number | null;
  title: string;
  side: EvidenceSide;
  voteLabel: string;
  qualityLabel: string | null;
  anchorHref: string;
  externalHref: string | null;
}

export interface ClaimSourceContradictionAtlas {
  total: number;
  supportCount: number;
  counterCount: number;
  unresolvedCount: number;
  hasContradiction: boolean;
  tensionScore: number;
  headline: string;
  summary: string;
  lanes: ClaimSourceContradictionLane[];
  primarySupport: ClaimSourceContradictionSource | null;
  primaryCounter: ClaimSourceContradictionSource | null;
}

export interface PageContradictionClaimLike {
  id?: number | string | null;
  text?: string | null;
  trust_level?: string | null;
  evidence_count?: number | null;
  con_count?: number | null;
  section?: string | null;
}

export interface PageContradictionRankingItem {
  claimId: number;
  claimText: string;
  trustLevel: string;
  sectionLabel: string;
  evidenceCount: number;
  supportCount: number;
  counterCount: number;
  unresolvedCount: number;
  tensionScore: number;
  rankScore: number;
  rankLabel: string;
  tierLabel: string;
  sourceSurveyed: boolean;
  sourceSurveyState: string;
  sourceHref: string;
  evidencePanelId: string;
  lanes: ClaimSourceContradictionLane[];
}

export interface PageContradictionRankingAtlas {
  totalClaims: number;
  surfacedClaims: number;
  surveyedClaims: number;
  hasRankedClaims: boolean;
  headline: string;
  summary: string;
  items: PageContradictionRankingItem[];
}

function pluralCount(count: number, singular: string, plural = `${singular}s`): string {
  return `${count.toLocaleString()} ${count === 1 ? singular : plural}`;
}

function compactVoteLabel(signal: EvidenceVoteSignal): string {
  if (!signal.totalVotes) return "no counted votes";
  const parts = [
    `${signal.supportVotes.toLocaleString()} support`,
    `${signal.weakeningVotes.toLocaleString()} weakening`,
  ];
  if (signal.unresolvedVotes > 0) parts.push(`${signal.unresolvedVotes.toLocaleString()} unresolved`);
  return parts.join(" · ");
}

function densitySideLabel(side: EvidenceSide): string {
  if (side === "support") return "supporting paper";
  if (side === "counter") return "countering paper";
  return "linked paper";
}

function sourceIdNumber(raw: EvidencePanelItemLike["id"]): number | null {
  const value = Number(raw);
  return Number.isFinite(value) && value > 0 ? Math.floor(value) : null;
}

function sourceQualityLabel(item: EvidencePanelItemLike | null | undefined): string | null {
  const quality = item?.quality_v2 == null ? null : Number(item.quality_v2);
  if (quality === null || !Number.isFinite(quality)) return null;
  const boundedQuality = Math.min(1, Math.max(0, quality));
  return `quality ${Math.round(boundedQuality * 100)}%`;
}

function sourceRank(item: EvidencePanelItemLike): number {
  const signal = buildEvidenceVoteSignal([item]);
  const quality = item.quality_v2 == null || !Number.isFinite(Number(item.quality_v2)) ? 0 : Math.min(1, Math.max(0, Number(item.quality_v2))) * 100;
  return quality + signal.totalVotes;
}

function sourceTitle(item: EvidencePanelItemLike, fallback: string): string {
  const title = String(item.title || "").trim();
  return title || fallback;
}

function contradictionSource(item: EvidencePanelItemLike | undefined, side: EvidenceSide): ClaimSourceContradictionSource | null {
  if (!item) return null;
  const sourceId = sourceIdNumber(item.id);
  return {
    sourceId,
    title: sourceTitle(item, side === "support" ? "Representative supporting source" : "Representative countering source"),
    side,
    voteLabel: compactVoteLabel(buildEvidenceVoteSignal([item])),
    qualityLabel: sourceQualityLabel(item),
    anchorHref: sourceId ? `#evidence-source-${sourceId}` : "#evidence-sources",
    externalHref: item.url || null,
  };
}

export function buildClaimSourceContradictionAtlas(evidence: EvidencePanelItemLike[] | null | undefined): ClaimSourceContradictionAtlas {
  const items = Array.isArray(evidence) ? evidence : [];
  const support = items.filter((item) => evidenceSide(item?.stance) === "support");
  const counter = items.filter((item) => evidenceSide(item?.stance) === "counter");
  const unresolved = items.filter((item) => evidenceSide(item?.stance) === "neutral");
  const total = items.length;
  const supportCount = support.length;
  const counterCount = counter.length;
  const unresolvedCount = unresolved.length;
  const hasContradiction = supportCount > 0 && counterCount > 0;
  const directionalCount = supportCount + counterCount;
  const balance = hasContradiction ? Math.min(supportCount, counterCount) / Math.max(supportCount, counterCount) : 0;
  const coverage = total > 0 ? directionalCount / total : 0;
  const tensionScore = Math.round(balance * coverage * 100);
  const lanes: ClaimSourceContradictionLane[] = [
    {
      kind: "support",
      label: "supporting sources",
      count: supportCount,
      percent: votePercent(supportCount, total),
      color: "#22c55e",
      background: "rgba(34,197,94,0.14)",
    },
    {
      kind: "counter",
      label: "countering sources",
      count: counterCount,
      percent: votePercent(counterCount, total),
      color: "#ef4444",
      background: "rgba(239,68,68,0.14)",
    },
    {
      kind: "unresolved",
      label: "unresolved sources",
      count: unresolvedCount,
      percent: votePercent(unresolvedCount, total),
      color: "#94a3b8",
      background: "rgba(148,163,184,0.14)",
    },
  ];
  const primarySupport = contradictionSource([...support].sort((a, b) => sourceRank(b) - sourceRank(a))[0], "support");
  const primaryCounter = contradictionSource([...counter].sort((a, b) => sourceRank(b) - sourceRank(a))[0], "counter");

  return {
    total,
    supportCount,
    counterCount,
    unresolvedCount,
    hasContradiction,
    tensionScore,
    headline: hasContradiction
      ? `Contradiction pressure: ${supportCount.toLocaleString()} supporting vs ${pluralCount(counterCount, "countering source")}`
      : "No source contradiction mapped yet",
    summary: hasContradiction
      ? "This claim has mapped support and counter-evidence; the atlas surfaces where sources disagree, not which side is correct."
      : "Mapped evidence currently leans one direction; keep watching for counter-sources or unresolved links.",
    lanes,
    primarySupport,
    primaryCounter,
  };
}

function claimIdNumber(raw: PageContradictionClaimLike["id"]): number | null {
  const value = Number(raw);
  return Number.isFinite(value) && value > 0 ? Math.floor(value) : null;
}

function claimTextValue(claim: PageContradictionClaimLike, fallbackId: number): string {
  const text = String(claim.text || "").replace(/\s+/g, " ").trim();
  return text || `Claim ${fallbackId}`;
}

function normalizeRenderedClaimIds(renderedClaimIds?: Iterable<number | string> | null): Set<number> | null {
  if (!renderedClaimIds) return null;
  const ids = new Set<number>();
  for (const raw of renderedClaimIds) {
    const id = Number(raw);
    if (Number.isFinite(id) && id > 0) ids.add(Math.floor(id));
  }
  return ids.size > 0 ? ids : null;
}

function sectionLabel(section: any): string {
  const raw = section?.title ?? section?.heading ?? section?.name ?? section?.section;
  const label = String(raw || "").trim();
  return label || "Claim layer";
}

function flattenPageContradictionClaims(pageClaims: any, renderedClaimIds?: Iterable<number | string> | null): Array<PageContradictionClaimLike & { sectionLabel: string }> {
  const rendered = normalizeRenderedClaimIds(renderedClaimIds);
  const output: Array<PageContradictionClaimLike & { sectionLabel: string }> = [];
  const seen = new Set<number>();
  const pushClaim = (claim: PageContradictionClaimLike, label: string) => {
    const id = claimIdNumber(claim?.id);
    if (id == null || seen.has(id)) return;
    if (rendered && !rendered.has(id)) return;
    seen.add(id);
    output.push({ ...claim, sectionLabel: label });
  };

  if (Array.isArray(pageClaims)) {
    for (const claim of pageClaims) pushClaim(claim, "Claim layer");
  }

  for (const section of pageClaims?.sections ?? []) {
    const label = sectionLabel(section);
    for (const claim of section?.claims ?? []) pushClaim(claim, label);
  }

  return output;
}

function estimateTensionScore(supportCount: number, counterCount: number): number {
  if (supportCount <= 0 || counterCount <= 0) return 0;
  return Math.round((Math.min(supportCount, counterCount) / Math.max(supportCount, counterCount)) * 100);
}

function trustRankWeight(trustLevel: string): number {
  if (trustLevel === "challenged") return 300;
  if (trustLevel === "debated") return 200;
  if (trustLevel === "unverified") return 80;
  if (trustLevel === "accepted") return 30;
  if (trustLevel === "consensus") return 10;
  return 0;
}

function fallbackLanes(supportCount: number, counterCount: number, unresolvedCount: number): ClaimSourceContradictionLane[] {
  const total = supportCount + counterCount + unresolvedCount;
  return [
    { kind: "support", label: "supporting sources", count: supportCount, percent: votePercent(supportCount, total), color: "#22c55e", background: "rgba(34,197,94,0.14)" },
    { kind: "counter", label: "countering sources", count: counterCount, percent: votePercent(counterCount, total), color: "#ef4444", background: "rgba(239,68,68,0.14)" },
    { kind: "unresolved", label: "unresolved sources", count: unresolvedCount, percent: votePercent(unresolvedCount, total), color: "#94a3b8", background: "rgba(148,163,184,0.14)" },
  ];
}

function contradictionTierLabel(counterCount: number, supportCount: number, sourceSurveyed: boolean): string {
  if (counterCount >= 2 && supportCount > 0) return "Contradicted";
  if (sourceSurveyed && counterCount > 0 && supportCount > 0) return "Contested";
  if (counterCount > 0) return "Questioned";
  return "Watching";
}

export function buildPageContradictionRankingAtlas(
  pageClaims: any,
  evidenceByClaimId: Record<string | number, EvidencePanelItemLike[] | null | undefined> = {},
  renderedClaimIds?: Iterable<number | string> | null,
): PageContradictionRankingAtlas {
  const claims = flattenPageContradictionClaims(pageClaims, renderedClaimIds);
  let surveyedClaims = 0;
  const items: PageContradictionRankingItem[] = [];

  for (const claim of claims) {
    const claimId = claimIdNumber(claim.id);
    if (claimId == null) continue;
    const evidence = evidenceByClaimId[claimId] ?? evidenceByClaimId[String(claimId)];
    const sourceSurveyed = Array.isArray(evidence);
    if (sourceSurveyed) surveyedClaims += 1;
    const publishedEvidenceCount = safeVoteCount(claim.evidence_count);
    const publishedCounterCount = safeVoteCount(claim.con_count);
    const trustLevel = String(claim.trust_level || "unverified").toLowerCase();

    let evidenceCount = publishedEvidenceCount;
    let supportCount = Math.max(0, publishedEvidenceCount - publishedCounterCount);
    let counterCount = publishedCounterCount;
    let unresolvedCount = 0;
    let tensionScore = estimateTensionScore(supportCount, counterCount);
    let lanes = fallbackLanes(supportCount, counterCount, unresolvedCount);

    if (sourceSurveyed) {
      const sourceAtlas = buildClaimSourceContradictionAtlas(evidence || []);
      evidenceCount = Math.max(publishedEvidenceCount, sourceAtlas.total);
      supportCount = sourceAtlas.supportCount;
      counterCount = sourceAtlas.counterCount;
      unresolvedCount = sourceAtlas.unresolvedCount;
      tensionScore = sourceAtlas.tensionScore;
      lanes = sourceAtlas.lanes;
    }

    if (counterCount <= 0) continue;

    const rankScore = counterCount * 1000 + tensionScore * 10 + evidenceCount + trustRankWeight(trustLevel);
    items.push({
      claimId,
      claimText: claimTextValue(claim, claimId),
      trustLevel,
      sectionLabel: claim.sectionLabel,
      evidenceCount,
      supportCount,
      counterCount,
      unresolvedCount,
      tensionScore,
      rankScore,
      rankLabel: sourceSurveyed
        ? `${counterCount.toLocaleString()} countering · ${supportCount.toLocaleString()} supporting · tension ${tensionScore}%`
        : `${counterCount.toLocaleString()} countering · ${supportCount.toLocaleString()} supporting · source lanes pending`,
      tierLabel: contradictionTierLabel(counterCount, supportCount, sourceSurveyed),
      sourceSurveyed,
      sourceSurveyState: sourceSurveyed ? "source lanes surveyed" : "source lanes pending",
      sourceHref: `#claim-${claimId}`,
      evidencePanelId: `claim-evidence-panel-${claimId}`,
      lanes,
    });
  }

  items.sort((a, b) =>
    b.rankScore - a.rankScore ||
    b.counterCount - a.counterCount ||
    b.tensionScore - a.tensionScore ||
    b.evidenceCount - a.evidenceCount ||
    a.claimId - b.claimId,
  );

  const surfacedClaims = items.length;
  return {
    totalClaims: claims.length,
    surfacedClaims,
    surveyedClaims,
    hasRankedClaims: surfacedClaims > 0,
    headline: surfacedClaims > 0
      ? `${pluralCount(surfacedClaims, "claim")} ranked by counter-source pressure`
      : "No page-level counter-source pressure surfaced",
    summary: "Claims ranked by mapped counter-source pressure; the atlas surfaces where sources disagree, not which side is correct.",
    items,
  };
}

export function buildEvidenceCardDensityMeta(item: EvidencePanelItemLike | null | undefined): EvidenceCardDensityMeta {
  const signal = buildEvidenceVoteSignal(item ? [item] : []);
  const comments = safeVoteCount(item?.comments_count);
  const links = safeVoteCount(item?.link_count);
  const activityParts: string[] = [];
  if (comments > 0) activityParts.push(pluralCount(comments, "comment"));
  if (links > 0) activityParts.push(pluralCount(links, "element link"));
  const quality = item?.quality_v2 == null ? null : Number(item.quality_v2);
  let qualityLabel: string | null = null;
  if (quality !== null && Number.isFinite(quality)) {
    const boundedQuality = Math.min(1, Math.max(0, quality));
    qualityLabel = `quality ${Math.round(boundedQuality * 100)}%`;
  }

  return {
    sideLabel: densitySideLabel(evidenceSide(item?.stance)),
    voteLabel: compactVoteLabel(signal),
    activityLabel: activityParts.length > 0 ? activityParts.join(" · ") : "no comments or element links yet",
    qualityLabel,
    hasActivity: activityParts.length > 0,
  };
}

export function evidenceSide(stance?: string | null): EvidenceSide {
  const value = (stance || "").toLowerCase();
  if (value.includes("challenge") || value.includes("contradict") || value.includes("against") || value === "con") {
    return "counter";
  }
  if (value.includes("support") || value.includes("agree") || value === "pro") {
    return "support";
  }
  return "neutral";
}

export function formatLinkedPaperSourceCount(count: number): string {
  const safeCount = Number.isFinite(count) && count > 0 ? Math.floor(count) : 0;
  return `${safeCount.toLocaleString()} linked paper source${safeCount === 1 ? "" : "s"}`;
}

function safeVoteCount(value?: number | null): number {
  const numeric = Number(value);
  return Number.isFinite(numeric) && numeric > 0 ? Math.floor(numeric) : 0;
}

export function buildEvidenceVoteSignal(evidence: EvidencePanelItemLike[] | null | undefined): EvidenceVoteSignal {
  const items = Array.isArray(evidence) ? evidence : [];
  let supportVotes = 0;
  let weakeningVotes = 0;
  let unresolvedVotes = 0;

  for (const item of items) {
    const agree = safeVoteCount(item?.votes_agree);
    const disagree = safeVoteCount(item?.votes_disagree);
    const side = evidenceSide(item?.stance);

    if (side === "support") {
      supportVotes += agree;
      weakeningVotes += disagree;
    } else if (side === "counter") {
      weakeningVotes += agree;
      supportVotes += disagree;
    } else {
      unresolvedVotes += agree + disagree;
    }
  }

  const totalVotes = supportVotes + weakeningVotes + unresolvedVotes;
  const directionalVotes = supportVotes + weakeningVotes;
  const netSupport = supportVotes - weakeningVotes;
  let verdict: EvidenceVoteSignalVerdict = "unvoted";
  let verdictLabel = "No counted evidence votes yet";

  if (totalVotes > 0 && directionalVotes === 0) {
    verdict = "unresolved";
    verdictLabel = "Evidence votes unresolved";
  } else if (totalVotes > 0 && netSupport > 0) {
    verdict = "net_support";
    verdictLabel = `Net +${netSupport.toLocaleString()} support signal`;
  } else if (totalVotes > 0 && netSupport < 0) {
    verdict = "net_weakening";
    verdictLabel = `Net +${Math.abs(netSupport).toLocaleString()} weakening signal`;
  } else if (totalVotes > 0) {
    verdict = "split";
    verdictLabel = "Split support/weakening signal";
  }

  const headlineParts = [
    `${supportVotes.toLocaleString()} support`,
    `${weakeningVotes.toLocaleString()} weakening`,
  ];
  if (unresolvedVotes > 0) headlineParts.push(`${unresolvedVotes.toLocaleString()} unresolved`);

  return {
    supportVotes,
    weakeningVotes,
    unresolvedVotes,
    totalVotes,
    netSupport,
    verdict,
    verdictLabel,
    headline: totalVotes > 0 ? `Counted vote signal: ${headlineParts.join(" · ")}` : "Counted vote signal: no votes yet",
    detail:
      "Agreement on supporting evidence counts toward support; disagreement with supporting evidence counts toward weakening. Countering evidence flips the meaning: agreement counts toward weakening, disagreement counts toward support. Neutral evidence votes stay unresolved.",
  };
}

function votePercent(count: number, total: number): number {
  if (!total) return 0;
  return Math.round((count / total) * 100);
}

function pluralVote(count: number, label: string): string {
  return `${count.toLocaleString()} ${label} vote${count === 1 ? "" : "s"}`;
}

function dominantVoteLabel(signal: EvidenceVoteSignal): string {
  if (!signal.totalVotes) return "waiting for counted votes";
  const leaders = [
    ["support", signal.supportVotes],
    ["weakening", signal.weakeningVotes],
    ["unresolved", signal.unresolvedVotes],
  ] as const;
  const max = Math.max(...leaders.map(([, count]) => count));
  const winners = leaders.filter(([, count]) => count === max && count > 0);
  if (winners.length !== 1) return "split vote cockpit";
  return `${winners[0][0]} votes dominate this cockpit`;
}

export function buildEvidenceVoteCockpitVisuals(signal: EvidenceVoteSignal): EvidenceVoteCockpitVisuals {
  const segments: EvidenceVoteCockpitSegment[] = [
    {
      kind: "support",
      label: "support",
      count: signal.supportVotes,
      percent: votePercent(signal.supportVotes, signal.totalVotes),
      color: "#22c55e",
      background: "rgba(34,197,94,0.16)",
    },
    {
      kind: "weakening",
      label: "weakening",
      count: signal.weakeningVotes,
      percent: votePercent(signal.weakeningVotes, signal.totalVotes),
      color: "#ef4444",
      background: "rgba(239,68,68,0.16)",
    },
    {
      kind: "unresolved",
      label: "unresolved",
      count: signal.unresolvedVotes,
      percent: votePercent(signal.unresolvedVotes, signal.totalVotes),
      color: "#94a3b8",
      background: "rgba(148,163,184,0.16)",
    },
  ];

  return {
    eyebrow: "At-a-glance vote balance",
    summary: signal.totalVotes > 0
      ? segments.map((segment) => pluralVote(segment.count, segment.label)).join(" · ")
      : "No counted evidence votes yet",
    dominantLabel: dominantVoteLabel(signal),
    segments,
  };
}

export function buildEvidencePanelCopy(
  evidence: EvidencePanelItemLike[] | null | undefined,
  trustLevel?: string | null,
): EvidencePanelCopy {
  const items = Array.isArray(evidence) ? evidence : [];
  let supportCount = 0;
  let counterCount = 0;
  let neutralCount = 0;

  for (const item of items) {
    const side = evidenceSide(item?.stance);
    if (side === "support") supportCount += 1;
    else if (side === "counter") counterCount += 1;
    else neutralCount += 1;
  }

  const total = items.length;
  const hasDirectionalStance = supportCount > 0 || counterCount > 0;
  const sourceLabel = formatLinkedPaperSourceCount(total);
  const directionalSplitLabel = hasDirectionalStance
    ? `${supportCount.toLocaleString()} supporting · ${counterCount.toLocaleString()} countering`
    : "directional stance split not published";
  const normalizedTrustLevel = String(trustLevel || "unverified").toLowerCase();
  const verb = total === 1 ? "is" : "are";
  const neutralOnlySummary = total > 0 && !hasDirectionalStance
    ? `${sourceLabel} ${verb} linked to this ${normalizedTrustLevel} claim; directional support/counter stance split is not published yet.`
    : null;

  return {
    total,
    supportCount,
    counterCount,
    neutralCount,
    hasDirectionalStance,
    sourceLabel,
    directionalSplitLabel,
    neutralOnlySummary,
  };
}
