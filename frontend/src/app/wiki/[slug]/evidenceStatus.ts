export type EvidenceStatusTone = "green" | "amber" | "slate";

export interface EvidenceStatusMeta {
  label: string;
  detail: string;
  trustBlocking: boolean;
  tone: EvidenceStatusTone;
}

export function evidenceStatusMeta(status?: string | null): EvidenceStatusMeta {
  const normalized = (status || "active").trim().toLowerCase() || "active";
  if (normalized === "provisional") {
    return {
      label: "provisional",
      detail: "Not in trust until promoted.",
      trustBlocking: true,
      tone: "amber",
    };
  }
  if (normalized === "active") {
    return {
      label: "active",
      detail: "Included in trust calculation.",
      trustBlocking: false,
      tone: "green",
    };
  }
  return {
    label: normalized,
    detail: "Evidence status reported by the API.",
    trustBlocking: false,
    tone: "slate",
  };
}
