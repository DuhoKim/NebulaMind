export type TrustVisibilityLevel = "consensus" | "accepted" | "debated" | "challenged" | "unverified";

export type TrustVisibilityLevelSummary = {
  claims: number;
  sources: number;
};

export type TrustVisibilitySummary = {
  totalClaims: number;
  totalSources: number;
  levels: Record<TrustVisibilityLevel, TrustVisibilityLevelSummary>;
};

export const TRUST_LEVEL_ORDER: TrustVisibilityLevel[] = [
  "consensus",
  "accepted",
  "debated",
  "challenged",
  "unverified",
];

const TRUST_LEVEL_META: Record<TrustVisibilityLevel, {
  label: string;
  icon: string;
  color: string;
  background: string;
  border: string;
  description: string;
}> = {
  consensus: {
    label: "Consensus",
    icon: "✓",
    color: "#22c55e",
    background: "rgba(34,197,94,0.13)",
    border: "rgba(34,197,94,0.5)",
    description: "Paper-backed sources currently agree on this claim.",
  },
  accepted: {
    label: "Accepted",
    icon: "●",
    color: "#3b82f6",
    background: "rgba(59,130,246,0.13)",
    border: "rgba(59,130,246,0.5)",
    description: "Supported by verified sources without an active contradiction signal.",
  },
  debated: {
    label: "Debated",
    icon: "≈",
    color: "#f97316",
    background: "rgba(249,115,22,0.13)",
    border: "rgba(249,115,22,0.55)",
    description: "Supported evidence exists, but the claim has tension or an open weakening signal.",
  },
  challenged: {
    label: "Challenged",
    icon: "!",
    color: "#ef4444",
    background: "rgba(239,68,68,0.13)",
    border: "rgba(239,68,68,0.55)",
    description: "Contradictory evidence is strong enough to challenge the claim.",
  },
  unverified: {
    label: "Unverified",
    icon: "?",
    color: "#94a3b8",
    background: "rgba(100,116,139,0.14)",
    border: "rgba(100,116,139,0.45)",
    description: "No provenance-gated trust level has been published yet.",
  },
};

export function normalizeTrustLevel(level: unknown): TrustVisibilityLevel {
  const raw = String(level ?? "unverified").toLowerCase().trim();
  return TRUST_LEVEL_ORDER.includes(raw as TrustVisibilityLevel)
    ? (raw as TrustVisibilityLevel)
    : "unverified";
}

export function trustVisibilityMeta(level: unknown) {
  const normalized = normalizeTrustLevel(level);
  return { level: normalized, ...TRUST_LEVEL_META[normalized] };
}

function pluralizeSources(count: number): string {
  return `${count.toLocaleString()} source${count === 1 ? "" : "s"}`;
}

export function formatClaimTrustBadge(claim: { trust_level?: unknown; evidence_count?: unknown } | null | undefined): string {
  const meta = trustVisibilityMeta(claim?.trust_level);
  const evidenceCount = Number(claim?.evidence_count ?? 0);
  const safeCount = Number.isFinite(evidenceCount) && evidenceCount > 0 ? Math.round(evidenceCount) : 0;
  return `${meta.label} · ${pluralizeSources(safeCount)}`;
}

function makeEmptyLevelSummary(): Record<TrustVisibilityLevel, TrustVisibilityLevelSummary> {
  return TRUST_LEVEL_ORDER.reduce((acc, level) => {
    acc[level] = { claims: 0, sources: 0 };
    return acc;
  }, {} as Record<TrustVisibilityLevel, TrustVisibilityLevelSummary>);
}

export function summarizeTrustClaims(payload: any): TrustVisibilitySummary {
  const levels = makeEmptyLevelSummary();
  const seen = new Set<string>();
  let totalClaims = 0;
  let totalSources = 0;

  for (const section of payload?.sections ?? []) {
    for (const claim of section?.claims ?? []) {
      const key = claim?.id != null ? `id:${claim.id}` : `text:${String(claim?.text ?? "").slice(0, 160)}`;
      if (seen.has(key)) continue;
      seen.add(key);

      const level = normalizeTrustLevel(claim?.trust_level);
      const evidenceCount = Number(claim?.evidence_count ?? 0);
      const safeCount = Number.isFinite(evidenceCount) && evidenceCount > 0 ? Math.round(evidenceCount) : 0;

      levels[level].claims += 1;
      levels[level].sources += safeCount;
      totalClaims += 1;
      totalSources += safeCount;
    }
  }

  return { totalClaims, totalSources, levels };
}

export function formatTrustSummaryLine(summary: TrustVisibilitySummary): string {
  if (!summary.totalClaims) return "No provenance-gated claim badges loaded yet.";
  const levelParts = TRUST_LEVEL_ORDER
    .map((level) => {
      const count = summary.levels[level].claims;
      if (!count) return null;
      return `${count.toLocaleString()} ${level}`;
    })
    .filter(Boolean)
    .join(" / ");
  return `${summary.totalClaims.toLocaleString()} trust-bearing claims · ${levelParts} · ${summary.totalSources.toLocaleString()} paper-source links`;
}
