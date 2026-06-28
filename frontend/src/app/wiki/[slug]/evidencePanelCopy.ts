export type EvidenceSide = "support" | "counter" | "neutral";

export interface EvidencePanelItemLike {
  stance?: string | null;
  votes_agree?: number | null;
  votes_disagree?: number | null;
}

export type EvidenceVoteSignalVerdict = "net_support" | "net_weakening" | "split" | "unresolved" | "unvoted";

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
