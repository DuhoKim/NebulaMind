export type ClaimMiniMapSegmentKind = "support" | "counter" | "unresolved";

export interface ClaimMiniMapClaimLike {
  id?: number | string | null;
  trust_level?: unknown;
  evidence_count?: unknown;
  pro_count?: unknown;
  con_count?: unknown;
  unresolved_count?: unknown;
}

export interface ClaimMiniMapSegment {
  kind: ClaimMiniMapSegmentKind;
  label: string;
  count: number;
  percent: number;
  color: string;
}

export interface ClaimMiniMapHoverCopy {
  eyebrow: "Claim mini-map";
  totalSources: number;
  supportCount: number;
  counterCount: number;
  unresolvedCount: number;
  stance: string;
  summary: string;
  segments: ClaimMiniMapSegment[];
}

function safeCount(value: unknown): number {
  const numeric = Number(value ?? 0);
  return Number.isFinite(numeric) && numeric > 0 ? Math.round(numeric) : 0;
}

function percent(count: number, total: number): number {
  if (!total) return 0;
  return Math.round((count / total) * 100);
}

function plural(value: number, singular: string, pluralLabel = `${singular}s`): string {
  return `${value.toLocaleString()} ${value === 1 ? singular : pluralLabel}`;
}

function inferStance(total: number, support: number, counter: number, unresolved: number): string {
  if (!total) return "no mapped sources yet";
  if (counter === 0 && unresolved === 0) return "supporting";
  if (support > 0 && counter / total <= 0.2 && unresolved === 0) return "mostly supporting";
  if (counter > support) return "counter-evidence heavy";
  return "mixed evidence";
}

export function buildClaimMiniMapHover(claim: ClaimMiniMapClaimLike | null | undefined): ClaimMiniMapHoverCopy {
  const totalSources = safeCount(claim?.evidence_count);
  const counterCount = Math.min(safeCount(claim?.con_count), totalSources || safeCount(claim?.con_count));
  const explicitUnresolved = safeCount(claim?.unresolved_count);
  const explicitSupport = claim?.pro_count == null ? null : safeCount(claim.pro_count);

  const supportCount = explicitSupport == null
    ? Math.max(totalSources - counterCount - explicitUnresolved, 0)
    : explicitSupport;
  const inferredTotal = Math.max(totalSources, supportCount + counterCount + explicitUnresolved);
  const unresolvedCount = Math.max(explicitUnresolved, inferredTotal - supportCount - counterCount);
  const stance = inferStance(inferredTotal, supportCount, counterCount, unresolvedCount);

  const segments: ClaimMiniMapSegment[] = [
    { kind: "support", label: "supporting", count: supportCount, percent: percent(supportCount, inferredTotal), color: "#22c55e" },
    { kind: "counter", label: "countering", count: counterCount, percent: percent(counterCount, inferredTotal), color: "#f97316" },
    { kind: "unresolved", label: "unresolved", count: unresolvedCount, percent: percent(unresolvedCount, inferredTotal), color: "#64748b" },
  ];

  return {
    eyebrow: "Claim mini-map",
    totalSources: inferredTotal,
    supportCount,
    counterCount,
    unresolvedCount,
    stance,
    summary: inferredTotal ? formatClaimMiniMapSummary({ supportCount, counterCount, unresolvedCount, totalSources: inferredTotal } as ClaimMiniMapHoverCopy) : "No evidence mini-map yet",
    segments,
  };
}

export function formatClaimMiniMapSummary(map: Pick<ClaimMiniMapHoverCopy, "supportCount" | "counterCount" | "unresolvedCount" | "totalSources">): string {
  if (!map.totalSources) return "No evidence mini-map yet";
  return [
    plural(map.supportCount, "supporting", "supporting"),
    plural(map.counterCount, "countering", "countering"),
    plural(map.unresolvedCount, "unresolved", "unresolved"),
  ].join(" · ");
}
