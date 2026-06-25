export interface TrustHistoryStats {
  total_raw_rows?: number | null;
  events_returned?: number | null;
  noise_filtered?: number | null;
}

export interface TrustHistoryClaimSummary {
  id: number;
  text: string;
  trust_level: string;
  section?: string | null;
  evidence_count?: number | null;
}

export interface TrustHistoryClaimsPayload {
  sections?: Array<{
    name?: string | null;
    claims?: TrustHistoryClaimSummary[] | null;
  }> | null;
  debates?: Array<{
    topic?: string | null;
    pro?: TrustHistoryClaimSummary | null;
    con?: TrustHistoryClaimSummary | null;
  }> | null;
}

export interface TrustScoreChangeEvent {
  detail?: string | null;
  score_before?: number | null;
  score_after?: number | null;
  score_delta?: number | null;
}

function countOrZero(value: number | null | undefined): number {
  if (typeof value !== "number" || !Number.isFinite(value)) return 0;
  return Math.max(0, Math.trunc(value));
}

function pluralize(count: number, singular: string, plural: string): string {
  return `${count} ${count === 1 ? singular : plural}`;
}

function shouldShowClaimInTrustHistory(claim: TrustHistoryClaimSummary): boolean {
  return claim.trust_level !== "unverified" || countOrZero(claim.evidence_count) > 0;
}

export function collectTrustHistoryClaims(
  payload: TrustHistoryClaimsPayload | null | undefined,
  limit: number = 30,
): TrustHistoryClaimSummary[] {
  const selected: TrustHistoryClaimSummary[] = [];
  const seen = new Set<number>();

  const addClaim = (claim: TrustHistoryClaimSummary | null | undefined, fallbackSection?: string | null) => {
    if (!claim || typeof claim.id !== "number" || seen.has(claim.id)) return;
    if (!shouldShowClaimInTrustHistory(claim)) return;
    seen.add(claim.id);
    selected.push({
      ...claim,
      section: claim.section ?? fallbackSection ?? null,
    });
  };

  for (const section of payload?.sections ?? []) {
    for (const claim of section?.claims ?? []) {
      addClaim(claim, section?.name ?? null);
    }
  }

  for (const debate of payload?.debates ?? []) {
    const topic = debate?.topic ? `Debate: ${debate.topic}` : "Debate";
    addClaim(debate?.pro, topic);
    addClaim(debate?.con, topic);
  }

  return selected.slice(0, countOrZero(limit));
}

function finiteNumber(value: number | null | undefined): number | null {
  return typeof value === "number" && Number.isFinite(value) ? value : null;
}

export function formatTrustScoreChange(event: TrustScoreChangeEvent | null | undefined): string | null {
  if (!event) return null;
  if (event.detail) return event.detail;

  const before = finiteNumber(event.score_before);
  const after = finiteNumber(event.score_after);
  if (before === null || after === null) return null;

  const delta = finiteNumber(event.score_delta) ?? after - before;
  if (Math.abs(delta) <= 0.001) return null;

  return `Score ${before.toFixed(3)} → ${after.toFixed(3)} (${delta >= 0 ? "+" : ""}${delta.toFixed(3)})`;
}

export function formatHiddenRecomputes(count: number | null | undefined): string {
  return `${pluralize(countOrZero(count), "recompute", "recomputes")} hidden`;
}

export function formatTrustHistoryStats(stats: TrustHistoryStats | null | undefined): string {
  const totalRawRows = countOrZero(stats?.total_raw_rows);
  const eventsReturned = countOrZero(stats?.events_returned);
  const hiddenRecomputes = countOrZero(stats?.noise_filtered);

  return [
    `${pluralize(totalRawRows, "raw event", "raw events")} → ${pluralize(eventsReturned, "timeline event", "timeline events")}`,
    formatHiddenRecomputes(hiddenRecomputes),
  ].join(" · ");
}

export const emptyTrustHistoryText = "No timeline events recorded yet.";
