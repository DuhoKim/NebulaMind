export interface TrustHistoryStats {
  total_raw_rows?: number | null;
  events_returned?: number | null;
  noise_filtered?: number | null;
}

function countOrZero(value: number | null | undefined): number {
  if (typeof value !== "number" || !Number.isFinite(value)) return 0;
  return Math.max(0, Math.trunc(value));
}

function pluralize(count: number, singular: string, plural: string): string {
  return `${count} ${count === 1 ? singular : plural}`;
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
