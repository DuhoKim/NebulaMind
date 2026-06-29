export const MAX_UPLOAD_BYTES = 2 * 1024 * 1024;

export type UploadExtension = ".json" | ".csv";

export type UploadValidation =
  | { ok: true; kind: "json" | "csv"; rowCount: number; message: string }
  | { ok: false; error: string };

export type UploadTokenState = {
  token?: string;
  expires_at?: string;
  used_at?: string | null;
};

export type UploadTokenCheck =
  | { ok: true }
  | { ok: false; status: 401 | 410 | 500; error: string };

function basenameOnly(name: string): string {
  return String(name || "upload").split(/[\\/]+/).filter(Boolean).pop() || "upload";
}

export function getUploadExtension(fileName: string, contentType = ""): UploadExtension | null {
  const lowerName = basenameOnly(fileName).toLowerCase();
  const lowerType = String(contentType || "").toLowerCase();
  if (lowerName.endsWith(".json") || lowerType.includes("application/json")) return ".json";
  if (lowerName.endsWith(".csv") || lowerType.includes("text/csv") || lowerType.includes("application/csv")) return ".csv";
  return null;
}

export function sanitizeUploadFileName(originalName: string): string {
  const base = basenameOnly(originalName)
    .normalize("NFKD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/[^A-Za-z0-9._-]+/g, "-")
    .replace(/-+/g, "-")
    .replace(/-+\./g, ".")
    .replace(/^[._-]+|[._-]+$/g, "")
    .slice(0, 96);
  return base || "labels-upload";
}

export function buildStoredUploadName({
  timestamp,
  token,
  originalName,
}: {
  timestamp: string;
  token: string;
  originalName: string;
}): string {
  const safe = sanitizeUploadFileName(originalName);
  const tokenPrefix = String(token || "no-token").replace(/[^A-Za-z0-9]/g, "").slice(0, 8) || "notoken";
  return `page58_labels_upload_${timestamp}_${tokenPrefix}_${safe}`;
}

function nonEmptyLines(text: string): string[] {
  return String(text || "")
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter(Boolean);
}

function parseCsvCells(line: string): string[] {
  // The upload validator only needs simple exported CSV cells; workspace exports do not embed commas in required fields.
  return line
    .split(",")
    .map((cell) => cell.trim().replace(/^"|"$/g, ""));
}

function hasPresentValue(value: unknown): boolean {
  if (value === null || value === undefined) return false;
  if (typeof value === "string") return value.trim().length > 0;
  if (typeof value === "number" || typeof value === "boolean") return true;
  return false;
}

function hasPrimaryDecision(record: Record<string, unknown>): boolean {
  return hasPresentValue(record.final_decision) || hasPresentValue(record.human_action) || hasPresentValue(record.human_should_count);
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return Boolean(value && typeof value === "object" && !Array.isArray(value));
}

export function validateLabelUploadText(text: string, extension: UploadExtension): UploadValidation {
  if (!text || text.trim().length === 0) {
    return { ok: false, error: "Upload is empty." };
  }

  if (extension === ".json") {
    let parsed: unknown;
    try {
      parsed = JSON.parse(text);
    } catch {
      return { ok: false, error: "Upload must be valid JSON." };
    }

    if (!parsed || typeof parsed !== "object" || Array.isArray(parsed)) {
      return { ok: false, error: "JSON upload must be an object exported from the labeling workspace." };
    }

    const obj = parsed as Record<string, unknown>;
    const rows = Array.isArray(obj.rows) ? obj.rows : [];
    const labelsBySampleId = obj.labels_by_sample_id && typeof obj.labels_by_sample_id === "object" && !Array.isArray(obj.labels_by_sample_id)
      ? (obj.labels_by_sample_id as Record<string, unknown>)
      : null;

    const rowCount = rows.length || (labelsBySampleId ? Object.keys(labelsBySampleId).length : 0);
    if (rowCount < 1) {
      return { ok: false, error: "JSON upload needs at least one labeled row or labels_by_sample_id entry." };
    }

    if (rows.length) {
      for (const [index, row] of rows.entries()) {
        if (!isRecord(row)) {
          return { ok: false, error: `JSON row ${index + 1} must be an object with sample_id and final_decision or human_action/should_count labels.` };
        }
        if (!hasPresentValue(row.sample_id)) {
          return { ok: false, error: `JSON row ${index + 1} must include sample_id.` };
        }
        if (!hasPrimaryDecision(row)) {
          return { ok: false, error: `JSON row ${index + 1} must include final_decision or human_action/should_count labels on the same row as sample_id.` };
        }
      }
    } else if (labelsBySampleId) {
      for (const [sampleId, label] of Object.entries(labelsBySampleId)) {
        if (!sampleId.trim()) {
          return { ok: false, error: "labels_by_sample_id entries must use non-empty sample_id keys." };
        }
        if (isRecord(label)) {
          if (!hasPrimaryDecision(label)) {
            return { ok: false, error: `labels_by_sample_id.${sampleId} must include final_decision or human_action/should_count labels.` };
          }
        } else if (!hasPresentValue(label)) {
          return { ok: false, error: `labels_by_sample_id.${sampleId} must include a non-empty label value.` };
        }
      }
    }

    return { ok: true, kind: "json", rowCount, message: `Accepted JSON label export with ${rowCount} row(s).` };
  }

  const lines = nonEmptyLines(text);
  if (lines.length < 2) {
    return { ok: false, error: "CSV upload needs a header row and at least one data row." };
  }

  const header = parseCsvCells(lines[0]).map((name) => name.toLowerCase());
  const sampleIdIndex = header.indexOf("sample_id");
  if (sampleIdIndex < 0) {
    return { ok: false, error: "CSV upload must include a sample_id column." };
  }
  const decisionIndexes = ["final_decision", "human_action", "human_should_count"]
    .map((name) => header.indexOf(name))
    .filter((index) => index >= 0);
  if (!decisionIndexes.length) {
    return { ok: false, error: "CSV upload must include final_decision or human_action/should_count columns." };
  }

  for (const [index, line] of lines.slice(1).entries()) {
    const rowNumber = index + 2;
    const cells = parseCsvCells(line);
    if (!hasPresentValue(cells[sampleIdIndex])) {
      return { ok: false, error: `CSV row ${rowNumber} must include sample_id.` };
    }
    if (!decisionIndexes.some((decisionIndex) => hasPresentValue(cells[decisionIndex]))) {
      return { ok: false, error: `CSV row ${rowNumber} must include final_decision or human_action/should_count labels.` };
    }
  }

  return { ok: true, kind: "csv", rowCount: lines.length - 1, message: `Accepted CSV label export with ${lines.length - 1} row(s).` };
}

export function verifyUploadToken(candidateToken: string | null | undefined, state: UploadTokenState | null | undefined, now = new Date()): UploadTokenCheck {
  if (!state || !state.token) {
    return { ok: false, status: 500, error: "Upload token is not configured." };
  }
  if (!candidateToken || candidateToken !== state.token) {
    return { ok: false, status: 401, error: "Upload token is missing or invalid." };
  }
  if (state.used_at) {
    return { ok: false, status: 410, error: "This one-time upload token has already been used." };
  }
  if (state.expires_at) {
    const expiresAt = new Date(state.expires_at);
    if (Number.isNaN(expiresAt.getTime()) || expiresAt.getTime() <= now.getTime()) {
      return { ok: false, status: 410, error: "This upload token has expired." };
    }
  }
  return { ok: true };
}
