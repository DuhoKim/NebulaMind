import { NextRequest, NextResponse } from "next/server";
import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import {
  MAX_UPLOAD_BYTES,
  buildStoredUploadName,
  getUploadExtension,
  validateLabelUploadText,
  verifyUploadToken,
  type UploadTokenState,
} from "@/lib/agentReportUpload";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

const STATE_PATH = process.env.PAGE58_LABEL_UPLOAD_STATE || path.join(os.homedir(), ".hermes", "tmp", "page58-label-upload-state.json");
const PUBLIC_UPLOAD_DIR = process.env.PAGE58_LABEL_UPLOAD_PUBLIC_DIR || path.join(process.cwd(), "public", "agent-reports", "uploaded-labels");

type StoredUpload = {
  uploaded_at: string;
  original_name: string;
  stored_name: string;
  public_path: string;
  kind: "json" | "csv";
  row_count: number;
  size_bytes: number;
};

type StateFile = UploadTokenState & {
  created_at?: string;
  purpose?: string;
  upload?: StoredUpload;
};

function json(data: unknown, status = 200) {
  return NextResponse.json(data, { status });
}

function tokenFromRequest(request: NextRequest): string | null {
  const queryToken = request.nextUrl.searchParams.get("token");
  if (queryToken) return queryToken;
  const auth = request.headers.get("authorization") || "";
  const match = auth.match(/^Bearer\s+(.+)$/i);
  return match ? match[1] : null;
}

async function loadState(): Promise<StateFile | null> {
  try {
    return JSON.parse(await fs.readFile(STATE_PATH, "utf8")) as StateFile;
  } catch (error) {
    if ((error as NodeJS.ErrnoException).code === "ENOENT") return null;
    throw error;
  }
}

async function saveState(state: StateFile) {
  await fs.mkdir(path.dirname(STATE_PATH), { recursive: true });
  await fs.writeFile(STATE_PATH, JSON.stringify(state, null, 2) + "\n", { mode: 0o600 });
}

function compactTimestamp(date: Date): string {
  return date.toISOString().replace(/[-:]/g, "").replace(/\.\d{3}Z$/, "Z");
}

function statusPayload(state: StateFile | null, token: string | null) {
  const check = verifyUploadToken(token, state || undefined);
  return {
    ready: check.ok,
    status: check.ok ? "ready" : check.status,
    message: check.ok ? "Upload token is valid." : check.error,
    expires_at: state?.expires_at || null,
    used_at: state?.used_at || null,
    upload: state?.upload
      ? {
          uploaded_at: state.upload.uploaded_at,
          original_name: state.upload.original_name,
          stored_name: state.upload.stored_name,
          public_path: state.upload.public_path,
          kind: state.upload.kind,
          row_count: state.upload.row_count,
          size_bytes: state.upload.size_bytes,
        }
      : null,
  };
}

export async function GET(request: NextRequest) {
  const state = await loadState();
  const token = tokenFromRequest(request);
  const payload = statusPayload(state, token);
  return json(payload, payload.ready ? 200 : Number(payload.status) || 500);
}

export async function POST(request: NextRequest) {
  const now = new Date();
  const state = await loadState();
  const token = tokenFromRequest(request);
  const tokenCheck = verifyUploadToken(token, state || undefined, now);
  if (!tokenCheck.ok) {
    return json({ ok: false, error: tokenCheck.error }, tokenCheck.status);
  }

  const form = await request.formData();
  const value = form.get("file");
  if (!value || typeof value === "string" || typeof (value as Blob).arrayBuffer !== "function") {
    return json({ ok: false, error: "Attach a JSON or CSV file in the form field named file." }, 400);
  }

  const file = value as File;
  const originalName = file.name || "labels-upload";
  const extension = getUploadExtension(originalName, file.type);
  if (!extension) {
    return json({ ok: false, error: "Only .json and .csv label exports are accepted." }, 400);
  }

  if (file.size > MAX_UPLOAD_BYTES) {
    return json({ ok: false, error: `File is too large. Maximum accepted size is ${MAX_UPLOAD_BYTES} bytes.` }, 413);
  }

  const text = Buffer.from(await file.arrayBuffer()).toString("utf8");
  const validation = validateLabelUploadText(text, extension);
  if (!validation.ok) {
    return json({ ok: false, error: validation.error }, 400);
  }

  const uploadedAt = now.toISOString();
  const timestamp = compactTimestamp(now);
  let storedName = buildStoredUploadName({ timestamp, token: token || "", originalName });
  if (!storedName.toLowerCase().endsWith(extension)) storedName += extension;

  await fs.mkdir(PUBLIC_UPLOAD_DIR, { recursive: true });
  const absolutePath = path.join(PUBLIC_UPLOAD_DIR, storedName);
  await fs.writeFile(absolutePath, text, { flag: "wx", mode: 0o600 });

  const upload: StoredUpload = {
    uploaded_at: uploadedAt,
    original_name: originalName,
    stored_name: storedName,
    public_path: `/agent-reports/uploaded-labels/${storedName}`,
    kind: validation.kind,
    row_count: validation.rowCount,
    size_bytes: file.size,
  };

  await fs.writeFile(path.join(PUBLIC_UPLOAD_DIR, "latest.json"), JSON.stringify(upload, null, 2) + "\n", { mode: 0o644 });
  await saveState({ ...(state || {}), used_at: uploadedAt, upload });

  return json({ ok: true, message: validation.message, upload });
}
