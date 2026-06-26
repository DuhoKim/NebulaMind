export type EvidenceSide = "support" | "counter" | "neutral";

export interface EvidencePanelItemLike {
  stance?: string | null;
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
