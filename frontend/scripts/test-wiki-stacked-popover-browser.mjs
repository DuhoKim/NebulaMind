import assert from "node:assert/strict";
import crypto from "node:crypto";
import fs from "node:fs";
import http from "node:http";
import net from "node:net";
import os from "node:os";
import path from "node:path";
import { spawn } from "node:child_process";

const frontendRoot = path.resolve(import.meta.dirname, "..");
const nextPort = Number(process.env.WIKI_STACKED_POPOVER_NEXT_PORT || 3033);
const chromePortBase = Number(process.env.WIKI_STACKED_POPOVER_CHROME_PORT || 9234);
const baseUrl = process.env.WIKI_STACKED_POPOVER_BASE_URL || `http://127.0.0.1:${nextPort}`;
const chromeBinary = process.env.CHROME_BIN || "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const STARTUP_TIMEOUT_MS = 45_000;
const SELECTOR_TIMEOUT_MS = 30_000;
const CDP_COMMAND_TIMEOUT_MS = 45_000;
const allScenarios = [
  {
    name: "claim-mini-map",
    routePath: process.env.WIKI_STACKED_POPOVER_MINIMAP_PATH || "/wiki/galaxy-evolution-v2",
    firstEscapeMarker: "mini_map_only",
  },
  {
    name: "source-trace",
    routePath: process.env.WIKI_STACKED_POPOVER_SOURCE_TRACE_PATH || "/wiki/source-trace-browser-fixture",
    firstEscapeMarker: "source_trace_only",
  },
  {
    name: "page-atlas-ranking",
    routePath: process.env.WIKI_STACKED_POPOVER_PAGE_ATLAS_PATH || "/wiki/source-trace-browser-fixture",
    firstEscapeMarker: "page_atlas_panel_closed_focus_returned",
  },
  {
    name: "paper-footprint",
    routePath: process.env.WIKI_STACKED_POPOVER_PAPER_FOOTPRINT_PATH || "/wiki/source-trace-browser-fixture",
    firstEscapeMarker: "paper_footprint_modal_closed_panel_open",
  },
];
const scenarioFilter = (process.env.WIKI_STACKED_POPOVER_ONLY || "").split(",").map((value) => value.trim()).filter(Boolean);
const scenarios = scenarioFilter.length > 0
  ? allScenarios.filter((scenario) => scenarioFilter.includes(scenario.name))
  : allScenarios;
assert.ok(scenarios.length > 0, `No browser scenarios selected by WIKI_STACKED_POPOVER_ONLY=${process.env.WIKI_STACKED_POPOVER_ONLY || ""}`);

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function waitFor(predicate, timeoutMs, description) {
  const start = Date.now();
  let lastError;
  while (Date.now() - start < timeoutMs) {
    try {
      const value = await predicate();
      if (value) return value;
    } catch (error) {
      lastError = error;
    }
    await sleep(250);
  }
  throw new Error(`Timed out waiting for ${description}${lastError ? `: ${lastError.message}` : ""}`);
}

function requestJson(url) {
  return new Promise((resolve, reject) => {
    const req = http.get(url, (res) => {
      let body = "";
      res.setEncoding("utf8");
      res.on("data", (chunk) => (body += chunk));
      res.on("end", () => {
        if ((res.statusCode || 0) >= 400) {
          reject(new Error(`${url} returned ${res.statusCode}: ${body.slice(0, 240)}`));
          return;
        }
        try {
          resolve(JSON.parse(body));
        } catch (error) {
          reject(error);
        }
      });
    });
    req.on("error", reject);
    req.setTimeout(8_000, () => req.destroy(new Error(`${url} timed out`)));
  });
}

async function waitForHttpOk(url, timeoutMs) {
  await waitFor(async () => {
    try {
      const res = await fetch(url, { redirect: "manual" });
      return res.status >= 200 && res.status < 500;
    } catch {
      return false;
    }
  }, timeoutMs, `${url} to respond`);
}

function spawnLogged(command, args, options = {}) {
  const output = [];
  const child = spawn(command, args, { ...options, stdio: ["ignore", "pipe", "pipe"] });
  child.stdout.on("data", (chunk) => output.push(String(chunk)));
  child.stderr.on("data", (chunk) => output.push(String(chunk)));
  child.outputTail = () => output.join("").split(/\r?\n/).slice(-24).join("\n");
  return child;
}

async function stopChild(child, name) {
  if (!child || child.exitCode !== null) return;
  child.kill("SIGTERM");
  for (let i = 0; i < 30; i += 1) {
    if (child.exitCode !== null) return;
    await sleep(100);
  }
  child.kill("SIGKILL");
  for (let i = 0; i < 20; i += 1) {
    if (child.exitCode !== null) return;
    await sleep(100);
  }
  console.warn(`${name} required SIGKILL during cleanup`);
}

class CdpClient {
  constructor(wsUrl) {
    const parsed = new URL(wsUrl);
    this.host = parsed.hostname;
    this.port = Number(parsed.port);
    this.path = `${parsed.pathname}${parsed.search}`;
    this.socket = null;
    this.buffer = Buffer.alloc(0);
    this.nextId = 1;
    this.pending = new Map();
  }

  async connect() {
    this.socket = net.createConnection({ host: this.host, port: this.port });
    await new Promise((resolve, reject) => {
      this.socket.once("connect", resolve);
      this.socket.once("error", reject);
    });
    const key = crypto.randomBytes(16).toString("base64");
    this.socket.write(
      `GET ${this.path} HTTP/1.1\r\n` +
      `Host: ${this.host}:${this.port}\r\n` +
      `Upgrade: websocket\r\n` +
      `Connection: Upgrade\r\n` +
      `Sec-WebSocket-Key: ${key}\r\n` +
      `Sec-WebSocket-Version: 13\r\n\r\n`,
    );
    let handshake = Buffer.alloc(0);
    await new Promise((resolve, reject) => {
      const onData = (chunk) => {
        handshake = Buffer.concat([handshake, chunk]);
        const marker = handshake.indexOf("\r\n\r\n");
        if (marker !== -1) {
          this.socket.off("data", onData);
          const header = handshake.slice(0, marker).toString("utf8");
          if (!header.includes("101")) {
            reject(new Error(`WebSocket handshake failed: ${header}`));
            return;
          }
          this.buffer = handshake.slice(marker + 4);
          this.socket.on("data", (data) => this.handleData(data));
          if (this.buffer.length) this.handleData(Buffer.alloc(0));
          resolve();
        }
      };
      this.socket.on("data", onData);
      this.socket.once("error", reject);
    });
  }

  handleData(data) {
    this.buffer = Buffer.concat([this.buffer, data]);
    while (this.buffer.length >= 2) {
      const first = this.buffer[0];
      const second = this.buffer[1];
      const opcode = first & 0x0f;
      let offset = 2;
      let length = second & 0x7f;
      if (length === 126) {
        if (this.buffer.length < offset + 2) return;
        length = this.buffer.readUInt16BE(offset);
        offset += 2;
      } else if (length === 127) {
        if (this.buffer.length < offset + 8) return;
        const high = this.buffer.readUInt32BE(offset);
        const low = this.buffer.readUInt32BE(offset + 4);
        length = high * 2 ** 32 + low;
        offset += 8;
      }
      const masked = Boolean(second & 0x80);
      let mask;
      if (masked) {
        if (this.buffer.length < offset + 4) return;
        mask = this.buffer.slice(offset, offset + 4);
        offset += 4;
      }
      if (this.buffer.length < offset + length) return;
      let payload = this.buffer.slice(offset, offset + length);
      this.buffer = this.buffer.slice(offset + length);
      if (masked) {
        payload = Buffer.from(payload.map((byte, index) => byte ^ mask[index % 4]));
      }
      if (opcode === 8) return;
      if (opcode !== 1) continue;
      const message = JSON.parse(payload.toString("utf8"));
      if (message.id && this.pending.has(message.id)) {
        const { resolve, reject } = this.pending.get(message.id);
        this.pending.delete(message.id);
        if (message.error) reject(new Error(JSON.stringify(message.error)));
        else resolve(message.result);
      }
    }
  }

  sendFrame(text) {
    const payload = Buffer.from(text, "utf8");
    const mask = crypto.randomBytes(4);
    const header = [0x81];
    if (payload.length < 126) {
      header.push(0x80 | payload.length);
    } else if (payload.length < 65536) {
      header.push(0x80 | 126, (payload.length >> 8) & 0xff, payload.length & 0xff);
    } else {
      header.push(0x80 | 127, 0, 0, 0, 0, (payload.length >>> 24) & 0xff, (payload.length >>> 16) & 0xff, (payload.length >>> 8) & 0xff, payload.length & 0xff);
    }
    const masked = Buffer.from(payload.map((byte, index) => byte ^ mask[index % 4]));
    this.socket.write(Buffer.concat([Buffer.from(header), mask, masked]));
  }

  command(method, params = {}) {
    const id = this.nextId++;
    this.sendFrame(JSON.stringify({ id, method, params }));
    return new Promise((resolve, reject) => {
      const timeout = setTimeout(() => {
        this.pending.delete(id);
        reject(new Error(`${method} timed out`));
      }, CDP_COMMAND_TIMEOUT_MS);
      this.pending.set(id, {
        resolve: (value) => {
          clearTimeout(timeout);
          resolve(value);
        },
        reject: (error) => {
          clearTimeout(timeout);
          reject(error);
        },
      });
    });
  }

  async evaluate(expression, awaitPromise = true) {
    const result = await this.command("Runtime.evaluate", {
      expression,
      awaitPromise,
      returnByValue: true,
      userGesture: true,
    });
    if (result.exceptionDetails) {
      throw new Error(`Runtime.evaluate exception: ${JSON.stringify(result.exceptionDetails)}`);
    }
    return result.result?.value;
  }

  async pressEscape() {
    await this.command("Input.dispatchKeyEvent", {
      type: "keyDown",
      windowsVirtualKeyCode: 27,
      nativeVirtualKeyCode: 27,
      macCharCode: 27,
      key: "Escape",
      code: "Escape",
    });
    await this.command("Input.dispatchKeyEvent", {
      type: "keyUp",
      windowsVirtualKeyCode: 27,
      nativeVirtualKeyCode: 27,
      macCharCode: 27,
      key: "Escape",
      code: "Escape",
    });
  }

  close() {
    this.socket?.end();
  }
}

const miniMapInteractionScript = String.raw`(async () => {
  const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
  const state = () => ({
    claimBadges: document.querySelectorAll('[data-testid="claim-trust-badge"]').length,
    miniMapTriggers: document.querySelectorAll('[data-testid="claim-trust-badge"]').length,
    panelOpen: Boolean(document.querySelector('[data-testid="evidence-panel-dialog"]')),
    miniMapOpen: Boolean(document.querySelector('[data-testid="claim-mini-map-hover-card"]')),
    activeTestId: document.activeElement?.getAttribute?.('data-testid') || '',
  });
  const waitFor = async (predicate, label) => {
    const start = Date.now();
    while (Date.now() - start < ${SELECTOR_TIMEOUT_MS}) {
      if (predicate()) return;
      await delay(100);
    }
    throw new Error('Timed out waiting for ' + label + ' state=' + JSON.stringify(state()));
  };

  await waitFor(() => document.querySelectorAll('[data-testid="claim-trust-badge"]').length > 0, 'claim badges');
  const claimBadge = document.querySelector('[data-testid="claim-trust-badge"]');
  claimBadge.scrollIntoView({ block: 'center', inline: 'center' });
  claimBadge.click();
  await waitFor(() => document.querySelector('[data-testid="evidence-panel-dialog"]'), 'evidence panel open');

  const miniMapTrigger = document.querySelectorAll('[data-testid="claim-trust-badge"]')[1] || document.querySelector('[data-testid="claim-trust-badge"]');
  const openMiniMap = async () => {
    for (let attempt = 0; attempt < 6; attempt += 1) {
      miniMapTrigger.scrollIntoView({ block: 'center', inline: 'center' });
      miniMapTrigger.focus();
      miniMapTrigger.dispatchEvent(new MouseEvent('mouseenter', { bubbles: true, cancelable: true, view: window }));
      miniMapTrigger.parentElement?.dispatchEvent(new MouseEvent('mouseenter', { bubbles: true, cancelable: true, view: window }));
      await delay(350);
      if (document.querySelector('[data-testid="claim-mini-map-hover-card"]')) return;
    }
    throw new Error('Timed out waiting for claim mini-map hover card open with panel state=' + JSON.stringify(state()));
  };
  await openMiniMap();

  return state();
})()`;

const sourceTraceInteractionScript = String.raw`(async () => {
  const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
  const state = () => ({
    claimBadges: document.querySelectorAll('[data-testid="claim-trust-badge"]').length,
    sourceTraceTriggers: document.querySelectorAll('[data-testid="source-trace-trigger"]').length,
    panelOpen: Boolean(document.querySelector('[data-testid="evidence-panel-dialog"]')),
    sourceTraceOpen: Boolean(document.querySelector('[data-testid="source-trace-hover-card"]')),
    activeTestId: document.activeElement?.getAttribute?.('data-testid') || '',
  });
  const waitFor = async (predicate, label) => {
    const start = Date.now();
    while (Date.now() - start < ${SELECTOR_TIMEOUT_MS}) {
      if (predicate()) return;
      await delay(100);
    }
    throw new Error('Timed out waiting for ' + label + ' state=' + JSON.stringify(state()));
  };

  await waitFor(() => document.querySelectorAll('[data-testid="claim-trust-badge"]').length > 0, 'claim badges');
  await waitFor(() => document.querySelectorAll('[data-testid="source-trace-trigger"]').length > 0, 'source trace triggers');

  const claimBadge = document.querySelector('[data-testid="claim-trust-badge"]');
  claimBadge.scrollIntoView({ block: 'center', inline: 'center' });
  claimBadge.click();
  await waitFor(() => document.querySelector('[data-testid="evidence-panel-dialog"]'), 'evidence panel open');

  const sourceTraceTrigger = document.querySelector('[data-testid="source-trace-trigger"]');
  const openSourceTrace = async () => {
    for (let attempt = 0; attempt < 6; attempt += 1) {
      sourceTraceTrigger.scrollIntoView({ block: 'center', inline: 'center' });
      sourceTraceTrigger.focus();
      sourceTraceTrigger.dispatchEvent(new MouseEvent('mouseenter', { bubbles: true, cancelable: true, view: window }));
      sourceTraceTrigger.parentElement?.dispatchEvent(new MouseEvent('mouseenter', { bubbles: true, cancelable: true, view: window }));
      await delay(350);
      if (document.querySelector('[data-testid="source-trace-hover-card"]')) return;
    }
    throw new Error('Timed out waiting for source trace hover card open with panel state=' + JSON.stringify(state()));
  };
  await openSourceTrace();

  return state();
})()`;

const pageAtlasInteractionScript = String.raw`(async () => {
  const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
  const state = () => {
    const dialog = document.querySelector('[data-testid="evidence-panel-dialog"]');
    const opener = document.querySelector('[data-testid="page-atlas-open-evidence-map"]');
    return {
      atlasVisible: Boolean(document.querySelector('[data-testid="page-contradiction-atlas-ranking"]')),
      atlasRows: document.querySelectorAll('[data-testid="page-atlas-ranked-claim"]').length,
      atlasOpeners: document.querySelectorAll('[data-testid="page-atlas-open-evidence-map"]').length,
      panelOpen: Boolean(dialog),
      dialogId: dialog?.getAttribute('id') || '',
      openerControls: opener?.getAttribute('aria-controls') || '',
      activeTestId: document.activeElement?.getAttribute?.('data-testid') || '',
      activeAriaLabel: document.activeElement?.getAttribute?.('aria-label') || '',
    };
  };
  const waitFor = async (predicate, label) => {
    const start = Date.now();
    while (Date.now() - start < ${SELECTOR_TIMEOUT_MS}) {
      if (predicate()) return;
      await delay(100);
    }
    throw new Error('Timed out waiting for ' + label + ' state=' + JSON.stringify(state()));
  };

  await waitFor(() => document.querySelector('[data-testid="page-contradiction-atlas-ranking"]'), 'page atlas ranking');
  await waitFor(() => document.querySelector('[data-testid="page-atlas-ranked-claim"]'), 'page atlas ranked row');
  const opener = document.querySelector('[data-testid="page-atlas-open-evidence-map"]');
  opener.scrollIntoView({ block: 'center', inline: 'center' });
  opener.focus();
  opener.click();
  await waitFor(() => document.querySelector('[data-testid="evidence-panel-dialog"]'), 'atlas evidence panel open');
  await waitFor(() => document.activeElement?.getAttribute?.('aria-label') === 'Close evidence panel', 'evidence panel close button focus');

  return state();
})()`;

const paperFootprintInteractionScript = String.raw`(async () => {
  const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
  const state = () => {
    const panel = document.querySelector('[data-testid="evidence-panel-dialog"]');
    const modal = document.querySelector('[data-testid="paper-footprint-modal"]');
    const entry = document.querySelector('[data-testid="paper-footprint-entry-button"]');
    return {
      claimBadges: document.querySelectorAll('[data-testid="claim-trust-badge"]').length,
      entryButtons: document.querySelectorAll('[data-testid="paper-footprint-entry-button"]').length,
      panelOpen: Boolean(panel),
      footprintOpen: Boolean(modal),
      modalRole: modal?.getAttribute('role') || '',
      modalAriaModal: modal?.getAttribute('aria-modal') || '',
      modalLabelledBy: Boolean(modal?.getAttribute('aria-labelledby')),
      modalDescribedBy: Boolean(modal?.getAttribute('aria-describedby')),
      modalText: modal?.textContent || '',
      claimRows: document.querySelectorAll('[data-testid="paper-footprint-claim-row"]').length,
      closeButtons: document.querySelectorAll('[data-testid="paper-footprint-close"]').length,
      activeTestId: document.activeElement?.getAttribute?.('data-testid') || '',
      activeAriaLabel: document.activeElement?.getAttribute?.('aria-label') || '',
      entryControls: entry?.getAttribute('aria-controls') || '',
      modalId: modal?.getAttribute('id') || '',
    };
  };
  const waitFor = async (predicate, label) => {
    const start = Date.now();
    while (Date.now() - start < ${SELECTOR_TIMEOUT_MS}) {
      if (predicate()) return;
      await delay(100);
    }
    throw new Error('Timed out waiting for ' + label + ' state=' + JSON.stringify(state()));
  };

  await waitFor(() => document.querySelectorAll('[data-testid="claim-trust-badge"]').length > 0, 'claim badges');
  const claimBadge = document.querySelector('[data-testid="claim-trust-badge"]');
  const openPanelFromClaimBadge = async () => {
    for (let attempt = 0; attempt < 6; attempt += 1) {
      claimBadge.scrollIntoView({ block: 'center', inline: 'center' });
      claimBadge.focus();
      claimBadge.dispatchEvent(new MouseEvent('mousedown', { bubbles: true, cancelable: true, view: window }));
      claimBadge.dispatchEvent(new MouseEvent('mouseup', { bubbles: true, cancelable: true, view: window }));
      claimBadge.click();
      await delay(350);
      if (document.querySelector('[data-testid="evidence-panel-dialog"]')) return;
    }
    throw new Error('Timed out waiting for hydrated claim badge click to open evidence panel state=' + JSON.stringify(state()));
  };
  await openPanelFromClaimBadge();
  await waitFor(() => document.querySelector('[data-testid="paper-footprint-entry-button"]'), 'paper footprint entry button');
  const entry = document.querySelector('[data-testid="paper-footprint-entry-button"]');
  entry.scrollIntoView({ block: 'center', inline: 'center' });
  entry.focus();
  entry.click();
  await waitFor(() => document.querySelector('[data-testid="paper-footprint-modal"]'), 'paper footprint modal open');
  await waitFor(() => document.activeElement?.getAttribute?.('data-testid') === 'paper-footprint-close', 'paper footprint close button focus');

  return state();
})()`;

const miniMapFirstEscapeStateScript = String.raw`(() => ({
  panelOpen: Boolean(document.querySelector('[data-testid="evidence-panel-dialog"]')),
  miniMapOpen: Boolean(document.querySelector('[data-testid="claim-mini-map-hover-card"]')),
  activeTestId: document.activeElement?.getAttribute?.('data-testid') || '',
  dialogRole: document.querySelector('[data-testid="evidence-panel-dialog"]')?.getAttribute('role') || '',
  ariaModal: document.querySelector('[data-testid="evidence-panel-dialog"]')?.getAttribute('aria-modal') || '',
  panelLabelledBy: Boolean(document.querySelector('[data-testid="evidence-panel-dialog"]')?.getAttribute('aria-labelledby')),
}))()`;

const sourceTraceFirstEscapeStateScript = String.raw`(() => ({
  panelOpen: Boolean(document.querySelector('[data-testid="evidence-panel-dialog"]')),
  sourceTraceOpen: Boolean(document.querySelector('[data-testid="source-trace-hover-card"]')),
  activeTestId: document.activeElement?.getAttribute?.('data-testid') || '',
  dialogRole: document.querySelector('[data-testid="evidence-panel-dialog"]')?.getAttribute('role') || '',
  ariaModal: document.querySelector('[data-testid="evidence-panel-dialog"]')?.getAttribute('aria-modal') || '',
  panelLabelledBy: Boolean(document.querySelector('[data-testid="evidence-panel-dialog"]')?.getAttribute('aria-labelledby')),
}))()`;

const miniMapSecondEscapeStateScript = String.raw`(() => ({
  panelOpen: Boolean(document.querySelector('[data-testid="evidence-panel-dialog"]')),
  miniMapOpen: Boolean(document.querySelector('[data-testid="claim-mini-map-hover-card"]')),
  activeTestId: document.activeElement?.getAttribute?.('data-testid') || '',
}))()`;

const sourceTraceSecondEscapeStateScript = String.raw`(() => ({
  panelOpen: Boolean(document.querySelector('[data-testid="evidence-panel-dialog"]')),
  sourceTraceOpen: Boolean(document.querySelector('[data-testid="source-trace-hover-card"]')),
  activeTestId: document.activeElement?.getAttribute?.('data-testid') || '',
}))()`;

const pageAtlasAfterEscapeStateScript = String.raw`(() => ({
  atlasVisible: Boolean(document.querySelector('[data-testid="page-contradiction-atlas-ranking"]')),
  atlasRows: document.querySelectorAll('[data-testid="page-atlas-ranked-claim"]').length,
  panelOpen: Boolean(document.querySelector('[data-testid="evidence-panel-dialog"]')),
  activeTestId: document.activeElement?.getAttribute?.('data-testid') || '',
  activeText: document.activeElement?.textContent?.trim() || '',
  openerControls: document.activeElement?.getAttribute?.('aria-controls') || '',
}))()`;

const paperFootprintAfterEscapeStateScript = String.raw`(() => ({
  panelOpen: Boolean(document.querySelector('[data-testid="evidence-panel-dialog"]')),
  footprintOpen: Boolean(document.querySelector('[data-testid="paper-footprint-modal"]')),
  entryButtons: document.querySelectorAll('[data-testid="paper-footprint-entry-button"]').length,
  activeTestId: document.activeElement?.getAttribute?.('data-testid') || '',
  activeText: document.activeElement?.textContent?.trim() || '',
  activeAriaLabel: document.activeElement?.getAttribute?.('aria-label') || '',
  panelRole: document.querySelector('[data-testid="evidence-panel-dialog"]')?.getAttribute('role') || '',
  panelAriaModal: document.querySelector('[data-testid="evidence-panel-dialog"]')?.getAttribute('aria-modal') || '',
}))()`;

const scenarioScripts = {
  "claim-mini-map": {
    interaction: miniMapInteractionScript,
    firstEscape: miniMapFirstEscapeStateScript,
    secondEscape: miniMapSecondEscapeStateScript,
    assertInitial(initial) {
      assert.equal(initial.panelOpen, true, "Evidence panel should be open before claim mini-map stacked Escape smoke.");
      assert.equal(initial.miniMapOpen, true, "Claim mini-map hover card should be open above/with the evidence panel before first Escape.");
      assert.equal(initial.activeTestId, "claim-trust-badge", "Claim badge should own keyboard focus before first Escape.");
    },
    assertFirstEscape(afterFirstEscape) {
      assert.equal(afterFirstEscape.miniMapOpen, false, "First Escape should close only the claim mini-map hover card.");
      assert.equal(afterFirstEscape.panelOpen, true, "First Escape should leave the evidence panel dialog open.");
      assert.equal(afterFirstEscape.activeTestId, "claim-trust-badge", "First Escape should return focus to the claim badge mini-map trigger.");
      assert.equal(afterFirstEscape.dialogRole, "dialog", "Evidence panel should keep dialog role after top-popover Escape.");
      assert.equal(afterFirstEscape.ariaModal, "true", "Evidence panel should keep aria-modal after top-popover Escape.");
      assert.equal(afterFirstEscape.panelLabelledBy, true, "Evidence panel should keep aria-labelledby after top-popover Escape.");
    },
    assertSecondEscape(afterSecondEscape) {
      assert.equal(afterSecondEscape.panelOpen, false, "Second Escape should close the evidence panel after the top mini-map hover card is gone.");
    },
  },
  "source-trace": {
    interaction: sourceTraceInteractionScript,
    firstEscape: sourceTraceFirstEscapeStateScript,
    secondEscape: sourceTraceSecondEscapeStateScript,
    assertInitial(initial) {
      assert.ok(initial.sourceTraceTriggers > 0, "Source-trace fixture should render at least one source-trace trigger.");
      assert.equal(initial.panelOpen, true, "Evidence panel should be open before source-trace stacked Escape smoke.");
      assert.equal(initial.sourceTraceOpen, true, "Source-trace hover card should be open above/with the evidence panel before first Escape.");
      assert.equal(initial.activeTestId, "source-trace-trigger", "Source-trace trigger should own keyboard focus before first Escape.");
    },
    assertFirstEscape(afterFirstEscape) {
      assert.equal(afterFirstEscape.panelOpen, true, "First Escape should leave the evidence panel dialog open for source-trace stack.");
      assert.equal(afterFirstEscape.sourceTraceOpen, false, "First Escape should close only the source-trace hover card.");
      assert.equal(afterFirstEscape.activeTestId, "source-trace-trigger", "First Escape should return focus to the source-trace trigger.");
      assert.equal(afterFirstEscape.dialogRole, "dialog", "Evidence panel should keep dialog role after source-trace Escape.");
      assert.equal(afterFirstEscape.ariaModal, "true", "Evidence panel should keep aria-modal after source-trace Escape.");
      assert.equal(afterFirstEscape.panelLabelledBy, true, "Evidence panel should keep aria-labelledby after source-trace Escape.");
    },
    assertSecondEscape(afterSecondEscape) {
      assert.equal(afterSecondEscape.panelOpen, false, "Second Escape should close the evidence panel after the source-trace hover card is gone.");
    },
  },
  "page-atlas-ranking": {
    interaction: pageAtlasInteractionScript,
    firstEscape: pageAtlasAfterEscapeStateScript,
    secondEscape: pageAtlasAfterEscapeStateScript,
    assertInitial(initial) {
      assert.equal(initial.atlasVisible, true, "Page atlas fixture should render the page-level contradiction atlas ranking.");
      assert.ok(initial.atlasRows > 0, "Page atlas fixture should render at least one ranked claim row.");
      assert.ok(initial.atlasOpeners > 0, "Page atlas fixture should render an evidence-map opener.");
      assert.equal(initial.panelOpen, true, "Atlas opener should open the evidence panel before Escape.");
      assert.equal(initial.dialogId, initial.openerControls, "Atlas opener aria-controls should target the opened evidence panel dialog id.");
      assert.equal(initial.activeAriaLabel, "Close evidence panel", "Evidence panel close button should receive initial dialog focus.");
    },
    assertFirstEscape(afterFirstEscape) {
      assert.equal(afterFirstEscape.atlasVisible, true, "Page atlas should remain visible after closing the evidence panel.");
      assert.equal(afterFirstEscape.panelOpen, false, "Escape should close the evidence panel opened from the page atlas row.");
      assert.equal(afterFirstEscape.activeTestId, "page-atlas-open-evidence-map", "Escape should return focus to the page atlas evidence-map opener.");
      assert.equal(afterFirstEscape.activeText, "Open evidence map", "Focus-return target should be the atlas opener button, not the page body.");
    },
    assertSecondEscape(afterSecondEscape) {
      assert.equal(afterSecondEscape.panelOpen, false, "A second Escape should leave the atlas evidence panel closed.");
      assert.equal(afterSecondEscape.activeTestId, "page-atlas-open-evidence-map", "Second Escape should not steal focus away from the atlas opener.");
    },
  },
  "paper-footprint": {
    interaction: paperFootprintInteractionScript,
    firstEscape: paperFootprintAfterEscapeStateScript,
    secondEscape: paperFootprintAfterEscapeStateScript,
    assertInitial(initial) {
      assert.ok(initial.claimBadges > 0, "Paper-footprint fixture should render claim badges.");
      assert.ok(initial.entryButtons > 0, "Evidence panel should render a paper-footprint entry button for mapped evidence.");
      assert.equal(initial.panelOpen, true, "Evidence panel should remain open while the paper footprint modal is stacked above it.");
      assert.equal(initial.footprintOpen, true, "Paper footprint modal should open from an evidence-card entry button.");
      assert.equal(initial.modalRole, "dialog", "Paper footprint should use dialog role.");
      assert.equal(initial.modalAriaModal, "true", "Paper footprint should be modal for assistive tech.");
      assert.equal(initial.modalLabelledBy, true, "Paper footprint should have aria-labelledby.");
      assert.equal(initial.modalDescribedBy, true, "Paper footprint should have aria-describedby.");
      assert.ok(initial.modalText.includes("on this page only"), "Paper footprint should visibly scope itself to the current page.");
      assert.ok(initial.modalText.includes("not a final verdict"), "Paper footprint should avoid truth adjudication copy.");
      assert.ok(initial.claimRows > 0, "Paper footprint should list linked visible claims.");
      assert.equal(initial.activeTestId, "paper-footprint-close", "Paper footprint close button should receive initial modal focus.");
      assert.equal(initial.entryControls, initial.modalId, "Paper footprint opener aria-controls should target the opened modal.");
    },
    assertFirstEscape(afterFirstEscape) {
      assert.equal(afterFirstEscape.panelOpen, true, "First Escape should leave the parent evidence panel open.");
      assert.equal(afterFirstEscape.footprintOpen, false, "First Escape should close only the paper footprint modal.");
      assert.equal(afterFirstEscape.activeTestId, "paper-footprint-entry-button", "First Escape should return focus to the footprint opener.");
      assert.equal(afterFirstEscape.panelRole, "dialog", "Parent evidence panel should keep dialog role after footprint Escape.");
      assert.equal(afterFirstEscape.panelAriaModal, "true", "Parent evidence panel should remain modal after footprint Escape.");
    },
    assertSecondEscape(afterSecondEscape) {
      assert.equal(afterSecondEscape.panelOpen, false, "Second Escape should close the parent evidence panel after the footprint modal is gone.");
      assert.equal(afterSecondEscape.footprintOpen, false, "Second Escape should not reopen the paper footprint modal.");
      assert.equal(afterSecondEscape.activeTestId, "claim-trust-badge", "Second Escape should return focus to the original claim badge.");
    },
  },
};

async function waitForPageReady(cdp, routePath) {
  await waitFor(async () => {
    try {
      const ready = await cdp.evaluate(`(() => ({ href: location.href, readyState: document.readyState }))()`);
      return ready && ready.href.includes(routePath) && ready.readyState !== "loading";
    } catch {
      return false;
    }
  }, STARTUP_TIMEOUT_MS, `Chrome page navigation to stabilize for ${routePath}`);
}

async function runBrowserScenario(scenario, index) {
  const routePath = scenario.routePath;
  const pageUrl = new URL(routePath, baseUrl).toString();
  const chromePort = chromePortBase + index;
  const chromeProfile = path.join(os.tmpdir(), `nebulamind-stacked-popover-chrome-${process.pid}-${scenario.name}`);
  const scripts = scenarioScripts[scenario.name];
  assert.ok(scripts, `No scripts registered for scenario ${scenario.name}`);

  let chrome;
  let cdp;
  fs.rmSync(chromeProfile, { recursive: true, force: true });
  try {
    await waitForHttpOk(pageUrl, STARTUP_TIMEOUT_MS);
    chrome = spawnLogged(chromeBinary, [
      "--headless=new",
      "--disable-gpu",
      "--no-first-run",
      "--no-default-browser-check",
      "--disable-background-networking",
      `--remote-debugging-port=${chromePort}`,
      `--user-data-dir=${chromeProfile}`,
      pageUrl,
    ]);
    const target = await waitFor(async () => {
      const pages = await requestJson(`http://127.0.0.1:${chromePort}/json/list`);
      return pages.find((page) => page.type === "page" && page.webSocketDebuggerUrl);
    }, STARTUP_TIMEOUT_MS, `Chrome DevTools target for ${scenario.name}`);
    cdp = new CdpClient(target.webSocketDebuggerUrl);
    await cdp.connect();
    await cdp.command("Runtime.enable");
    await cdp.command("Page.enable");
    await waitForPageReady(cdp, routePath);

    const initial = await cdp.evaluate(scripts.interaction);
    scripts.assertInitial(initial);

    await cdp.pressEscape();
    await sleep(300);
    const afterFirstEscape = await cdp.evaluate(scripts.firstEscape);
    scripts.assertFirstEscape(afterFirstEscape);

    await cdp.pressEscape();
    await sleep(350);
    const afterSecondEscape = await cdp.evaluate(scripts.secondEscape);
    scripts.assertSecondEscape(afterSecondEscape);

    console.log(`STACKED_POPOVER_CASE_OK name=${scenario.name} first_escape=${scenario.firstEscapeMarker} second_escape=panel_closed url=${pageUrl}`);
    if (scenario.name === "source-trace") {
      console.log(`SOURCE_TRACE_STACK_OK first_escape=source_trace_only second_escape=panel_closed url=${pageUrl}`);
    }
    if (scenario.name === "page-atlas-ranking") {
      console.log(`PAGE_ATLAS_BROWSER_OK first_escape=page_atlas_panel_closed_focus_returned second_escape=panel_remained_closed url=${pageUrl}`);
    }
    if (scenario.name === "paper-footprint") {
      console.log(`PAPER_FOOTPRINT_BROWSER_OK first_escape=paper_footprint_modal_closed_panel_open second_escape=panel_closed_focus_claim_badge url=${pageUrl}`);
    }
    return {
      name: scenario.name,
      ok: true,
      route: routePath,
      url: pageUrl,
      firstEscapeMarker: scenario.firstEscapeMarker,
      firstEscape: afterFirstEscape,
      secondEscape: afterSecondEscape,
    };
  } catch (error) {
    console.error(`STACKED_POPOVER_CASE_FAIL name=${scenario.name} ${error.message}`);
    if (chrome) console.error(`chrome_tail_${scenario.name}:\n${chrome.outputTail()}`);
    throw error;
  } finally {
    cdp?.close();
    await stopChild(chrome, `chrome ${scenario.name}`);
    for (let i = 0; i < 8; i += 1) {
      try {
        fs.rmSync(chromeProfile, { recursive: true, force: true });
        break;
      } catch (cleanupError) {
        if (i === 7) console.warn(`chrome_profile_cleanup_warning ${scenario.name} ${cleanupError.message}`);
        await sleep(250);
      }
    }
  }
}

async function main() {
  assert.ok(fs.existsSync(path.join(frontendRoot, ".next", "BUILD_ID")), "Run npm run build before smoke:wiki-stacked-popover-browser so next start can serve a production build.");
  assert.ok(fs.existsSync(chromeBinary), `Chrome binary not found at ${chromeBinary}; set CHROME_BIN to override.`);

  const next = process.env.WIKI_STACKED_POPOVER_BASE_URL
    ? null
    : spawnLogged("npm", ["run", "start", "--", "-p", String(nextPort)], { cwd: frontendRoot });
  const results = [];
  try {
    for (let i = 0; i < scenarios.length; i += 1) {
      results.push(await runBrowserScenario(scenarios[i], i));
    }
    console.log(`STACKED_POPOVER_BROWSER_OK cases=${results.length}/${scenarios.length} first_escape=top_popover_only second_escape=panel_closed`);
    console.log(`STACKED_POPOVER_BROWSER_JSON ${JSON.stringify({ ok: true, cases: results })}`);
  } catch (error) {
    console.error(`STACKED_POPOVER_BROWSER_FAIL ${error.message}`);
    if (next) console.error(`next_tail:\n${next.outputTail()}`);
    process.exitCode = 1;
  } finally {
    await stopChild(next, "next");
  }
}

await main();
